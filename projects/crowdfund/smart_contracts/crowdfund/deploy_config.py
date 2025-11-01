import logging
import time

import algokit_utils

logger = logging.getLogger(__name__)


# define deployment behaviour based on supplied app spec
def deploy() -> None:
    from smart_contracts.artifacts.crowdfund.crowdfund_client import (
        CreateCampaignArgs,
        CrowdfundFactory,
    )

    algorand = algokit_utils.AlgorandClient.from_environment()
    deployer_ = algorand.account.from_environment("DEPLOYER")

    factory = algorand.client.get_typed_app_factory(
        CrowdfundFactory, default_sender=deployer_.address
    )

    app_client, result = factory.deploy(
        on_update=algokit_utils.OnUpdate.AppendApp,
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
    )

    if result.operation_performed in [
        algokit_utils.OperationPerformed.Create,
        algokit_utils.OperationPerformed.Replace,
    ]:
        algorand.send.payment(
            algokit_utils.PaymentParams(
                amount=algokit_utils.AlgoAmount(algo=1),
                sender=deployer_.address,
                receiver=app_client.app_address,
            )
        )

    # Create a sample campaign for testing
    goal_microalgos = 5_000_000  # 5 ALGO
    deadline_timestamp = int(time.time() + 86400)  # 24 hours from now
    
    response = app_client.send.create_campaign(
        args=CreateCampaignArgs(goal=goal_microalgos, deadline_timestamp=deadline_timestamp)
    )
    logger.info(
        f"Created campaign on {app_client.app_name} ({app_client.app_id}) "
        f"with goal=5 ALGO, deadline={deadline_timestamp}, received: {response.abi_return}"
    )
