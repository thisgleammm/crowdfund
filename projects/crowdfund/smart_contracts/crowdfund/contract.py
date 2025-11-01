from algopy import ARC4Contract, UInt64, String, Account, Txn, Global
from algopy.arc4 import abimethod

class Crowdfund(ARC4Contract):
    def __init__(self) -> None:
        self.creator = Account(Global.creator_address.bytes)
        self.goal = UInt64(0)
        self.deadline = UInt64(0)
        self.raised = UInt64(0)
        self.active = UInt64(0)

    @abimethod()
    def create_campaign(self, goal: UInt64, deadline_timestamp: UInt64) -> String:
        # Only creator can create a campaign
        assert Txn.sender == self.creator, "Only creator can create campaign"
        # Prevent overlapping campaigns
        assert self.active == UInt64(0), "Campaign already active"
        # Validate parameters
        assert goal > UInt64(0), "Goal must be greater than 0"
        assert deadline_timestamp > Global.latest_timestamp, "Deadline must be in the future"
        
        self.goal = goal
        self.deadline = deadline_timestamp
        self.raised = UInt64(0)
        self.active = UInt64(1)
        return String("Campaign created!")

    @abimethod()
    def contribute(self, amount: UInt64) -> String:
        # Check if campaign is active
        assert self.active == UInt64(1), "Campaign not active"
        # Check if deadline has not passed
        assert Global.latest_timestamp < self.deadline, "Campaign deadline passed"
        # Check minimum contribution
        assert amount > UInt64(0), "Contribution must be greater than 0"
        # Update raised amount
        self.raised = self.raised + amount
        return String("Contribution accepted!")

    @abimethod()
    def claim_funds(self) -> String:
        # Check if there was ever a campaign (goal > 0)
        assert self.goal > UInt64(0), "No campaign exists"
        # Check deadline has passed
        assert Global.latest_timestamp >= self.deadline, "Campaign still running"
        # Check goal was reached
        assert self.raised >= self.goal, "Goal not reached"
        # Only creator can claim
        assert Txn.sender == self.creator, "Only creator can claim funds"
        # Campaign must not have been cancelled (if cancelled, active would be 0 but deadline not passed)
        if Global.latest_timestamp < self.deadline and self.active == UInt64(0):
            assert False, "Campaign was cancelled, cannot claim"
        
        self.active = UInt64(0)
        return String("Funds claimed by creator!")

    @abimethod()
    def refund(self) -> String:
        # Check if there was ever a campaign (goal > 0)
        assert self.goal > UInt64(0), "No campaign exists"
        # Check deadline has passed OR campaign was cancelled
        assert Global.latest_timestamp >= self.deadline or self.active == UInt64(0), "Campaign still running and not cancelled"
        # Check goal was NOT reached
        assert self.raised < self.goal, "Goal was reached, no refunds"
        
        self.active = UInt64(0)
        return String("Refunds available!")

    @abimethod()
    def cancel_campaign(self) -> String:
        # Check campaign is active
        assert self.active == UInt64(1), "No active campaign"
        # Only creator can cancel
        assert Txn.sender == self.creator, "Only creator can cancel campaign"
        # Campaign can only be cancelled before deadline
        assert Global.latest_timestamp < self.deadline, "Campaign deadline already passed"
        
        # Deactivate campaign
        self.active = UInt64(0)
        return String("Campaign cancelled by creator!")
