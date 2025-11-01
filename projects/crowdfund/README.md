# 🚀 Algorand Crowdfunding dApp

**My dApp is a XXX built on Algorand**

A decentralized crowdfunding platform built on the Algorand blockchain, enabling transparent and secure fundraising campaigns with smart contract automation.

## 📖 Project Description

This dApp revolutionizes crowdfunding by leveraging Algorand's fast, secure, and low-cost blockchain technology. Campaign creators can launch fundraising initiatives while contributors can support projects with confidence, knowing their funds are protected by smart contracts.

## 🎯 What it does

The Algorand Crowdfunding dApp provides a complete decentralized fundraising ecosystem:

- **Campaign Creation**: Anyone can create a fundraising campaign with customizable goals and deadlines
- **Secure Contributions**: Contributors can fund campaigns using ALGO tokens with full transparency
- **Automated Fund Management**: Smart contracts automatically handle fund collection and distribution
- **Goal Tracking**: Real-time monitoring of fundraising progress and milestones
- **Refund Protection**: Automatic refunds if campaigns don't meet their goals within the deadline
- **Transparent Operations**: All transactions and campaign data are publicly verifiable on-chain

## ✨ Features

### 🔐 **Smart Contract Security**
- Funds are locked in smart contracts until campaign goals are met
- Automatic refund mechanism for failed campaigns
- Immutable campaign terms and conditions

### 🌍 **Decentralized & Transparent**
- No central authority controlling funds
- Public campaign data and contribution history
- Real-time progress tracking

### ⚡ **Algorand-Powered Performance**
- Near-instant transaction finality (< 5 seconds)
- Minimal transaction fees (< $0.01)
- Carbon-negative blockchain technology

### 🎨 **User-Friendly Interface**
- Intuitive campaign creation workflow
- Easy contribution process
- Comprehensive dashboard for creators and contributors

### 📊 **Advanced Analytics**
- Campaign performance metrics
- Contributor insights
- Success rate statistics

## 🔗 Deployed Smart Contract

**Deployed Smart Contract Link: XXX**

## 💻 Code Implementation

```python
//paste your code
```

## 🛠 Tech Stack

- **Blockchain**: Algorand
- **Smart Contracts**: AlgoPy (Algorand Python)
- **Development Framework**: AlgoKit
- **Language**: Python 3.12+
- **Dependency Management**: Poetry

## 🚀 Quick Start Guide

### Prerequisites
- [Python 3.12+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/) (for LocalNet)
- [AlgoKit CLI](https://github.com/algorandfoundation/algokit-cli#install)

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd crowdfund
   ```

2. **Install dependencies**
   ```bash
   algokit project bootstrap all
   ```

3. **Start local Algorand network**
   ```bash
   algokit localnet start
   ```

4. **Deploy smart contracts**
   ```bash
   algokit project deploy localnet
   ```

## 🎮 Usage

### Creating a Campaign
1. Connect your Algorand wallet
2. Click "Create Campaign"
3. Set funding goal, deadline, and campaign details
4. Deploy your campaign to the blockchain

### Contributing to Campaigns
1. Browse active campaigns
2. Select a campaign to support
3. Choose contribution amount in ALGO
4. Confirm transaction through your wallet

### Campaign Management
- Monitor real-time progress
- Withdraw funds when goals are met
- Automatic refunds for failed campaigns

## 🏗 Project Structure

```
crowdfund/
├── smart_contracts/          # Algorand smart contracts
│   ├── crowdfund/           # Main crowdfunding contract
│   │   ├── contract.py      # Smart contract logic
│   │   └── deploy_config.py # Deployment configuration
│   └── artifacts/           # Compiled contracts
├── tests/                   # Test files
├── .env.localnet           # Local environment config
└── pyproject.toml          # Python dependencies
```

## 🧪 Testing

Run the test suite:
```bash
algokit project run test
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links & Resources

- [Algorand Developer Portal](https://developer.algorand.org/)
- [AlgoKit Documentation](https://github.com/algorandfoundation/algokit-cli)
- [Algorand Python Documentation](https://github.com/algorandfoundation/puya)

## 📞 Support

- 📧 Email: [your-email@example.com](mailto:your-email@example.com)
- 💬 Discord: [Join our community](https://discord.gg/algorand)
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/crowdfund/issues)

---

<div align="center">
  <p>Built with ❤️ on Algorand</p>
  <p>
    <img src="https://img.shields.io/badge/Algorand-000000?style=for-the-badge&logo=algorand&logoColor=white" alt="Algorand">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/AlgoKit-4285F4?style=for-the-badge" alt="AlgoKit">
  </p>
</div>

# Original Setup Documentation

### Pre-requisites

- [Python 3.12](https://www.python.org/downloads/) or later
- [Docker](https://www.docker.com/) (only required for LocalNet)

> For interactive tour over the codebase, download [vsls-contrib.codetour](https://marketplace.visualstudio.com/items?itemName=vsls-contrib.codetour) extension for VS Code, then open the [`.codetour.json`](./.tours/getting-started-with-your-algokit-project.tour) file in code tour extension.

### Initial Setup

#### 1. Clone the Repository
Start by cloning this repository to your local machine.

#### 2. Install Pre-requisites
Ensure the following pre-requisites are installed and properly configured:

- **Docker**: Required for running a local Algorand network. [Install Docker](https://www.docker.com/).
- **AlgoKit CLI**: Essential for project setup and operations. Install the latest version from [AlgoKit CLI Installation Guide](https://github.com/algorandfoundation/algokit-cli#install). Verify installation with `algokit --version`, expecting `2.0.0` or later.

#### 3. Bootstrap Your Local Environment
Run the following commands within the project folder:

- **Install Poetry**: Required for Python dependency management. [Installation Guide](https://python-poetry.org/docs/#installation). Verify with `poetry -V` to see version `1.2`+.
- **Setup Project**: Execute `algokit project bootstrap all` to install dependencies and setup a Python virtual environment in `.venv`.
- **Configure environment**: Execute `algokit generate env-file -a target_network localnet` to create a `.env.localnet` file with default configuration for `localnet`.
- **Start LocalNet**: Use `algokit localnet start` to initiate a local Algorand network.

### Development Workflow

#### Terminal
Directly manage and interact with your project using AlgoKit commands:

1. **Build Contracts**: `algokit project run build` compiles all smart contracts. You can also specify a specific contract by passing the name of the contract folder as an extra argument.
For example: `algokit project run build -- hello_world` will only build the `hello_world` contract.
2. **Deploy**: Use `algokit project deploy localnet` to deploy contracts to the local network. You can also specify a specific contract by passing the name of the contract folder as an extra argument.
For example: `algokit project deploy localnet -- hello_world` will only deploy the `hello_world` contract.

#### VS Code 
For a seamless experience with breakpoint debugging and other features:

1. **Open Project**: In VS Code, open the repository root.
2. **Install Extensions**: Follow prompts to install recommended extensions.
3. **Debugging**:
   - Use `F5` to start debugging.
   - **Windows Users**: Select the Python interpreter at `./.venv/Scripts/python.exe` via `Ctrl/Cmd + Shift + P` > `Python: Select Interpreter` before the first run.

#### JetBrains IDEs
While primarily optimized for VS Code, JetBrains IDEs are supported:

1. **Open Project**: In your JetBrains IDE, open the repository root.
2. **Automatic Setup**: The IDE should configure the Python interpreter and virtual environment.
3. **Debugging**: Use `Shift+F10` or `Ctrl+R` to start debugging. Note: Windows users may encounter issues with pre-launch tasks due to a known bug. See [JetBrains forums](https://youtrack.jetbrains.com/issue/IDEA-277486/Shell-script-configuration-cannot-run-as-before-launch-task) for workarounds.

## AlgoKit Workspaces and Project Management
This project supports both standalone and monorepo setups through AlgoKit workspaces. Leverage [`algokit project run`](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/features/project/run.md) commands for efficient monorepo project orchestration and management across multiple projects within a workspace.

## AlgoKit Generators

This template provides a set of [algokit generators](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/features/generate.md) that allow you to further modify the project instantiated from the template to fit your needs, as well as giving you a base to build your own extensions to invoke via the `algokit generate` command.

### Generate Smart Contract 

By default the template creates a single `HelloWorld` contract under crowdfund folder in the `smart_contracts` directory. To add a new contract:

1. From the root of the project (`../`) execute `algokit generate smart-contract`. This will create a new starter smart contract and deployment configuration file under `{your_contract_name}` subfolder in the `smart_contracts` directory.
2. Each contract potentially has different creation parameters and deployment steps. Hence, you need to define your deployment logic in `deploy_config.py`file.
3. `config.py` file will automatically build all contracts in the `smart_contracts` directory. If you want to build specific contracts manually, modify the default code provided by the template in `config.py` file.

> Please note, above is just a suggested convention tailored for the base configuration and structure of this template. The default code supplied by the template in `config.py` and `index.ts` (if using ts clients) files are tailored for the suggested convention. You are free to modify the structure and naming conventions as you see fit.

### Generate '.env' files

By default the template instance does not contain any env files. Using [`algokit project deploy`](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/features/project/deploy.md) against `localnet` | `testnet` | `mainnet` will use default values for `algod` and `indexer` unless overwritten via `.env` or `.env.{target_network}`. 

To generate a new `.env` or `.env.{target_network}` file, run `algokit generate env-file`

### Debugging Smart Contracts

This project is optimized to work with AlgoKit AVM Debugger extension. To activate it:
Refer to the commented header in the `__main__.py` file in the `smart_contracts` folder.

If you have opted in to include VSCode launch configurations in your project, you can also use the `Debug TEAL via AlgoKit AVM Debugger` launch configuration to interactively select an available trace file and launch the debug session for your smart contract.

For information on using and setting up the `AlgoKit AVM Debugger` VSCode extension refer [here](https://github.com/algorandfoundation/algokit-avm-vscode-debugger). To install the extension from the VSCode Marketplace, use the following link: [AlgoKit AVM Debugger extension](https://marketplace.visualstudio.com/items?itemName=algorandfoundation.algokit-avm-vscode-debugger).

# Tools

This project makes use of Algorand Python to build Algorand smart contracts. The following tools are in use:

- [Algorand](https://www.algorand.com/) - Layer 1 Blockchain; [Developer portal](https://dev.algorand.co/), [Why Algorand?](https://dev.algorand.co/getting-started/why-algorand/)
- [AlgoKit](https://github.com/algorandfoundation/algokit-cli) - One-stop shop tool for developers building on the Algorand network; [docs](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/algokit.md), [intro tutorial](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/tutorials/intro.md)
- [Algorand Python](https://github.com/algorandfoundation/puya) - A semantically and syntactically compatible, typed Python language that works with standard Python tooling and allows you to express smart contracts (apps) and smart signatures (logic signatures) for deployment on the Algorand Virtual Machine (AVM); [docs](https://github.com/algorandfoundation/puya), [examples](https://github.com/algorandfoundation/puya/tree/main/examples)
- [AlgoKit Utils](https://github.com/algorandfoundation/algokit-utils-py) - A set of core Algorand utilities that make it easier to build solutions on Algorand.
- [Poetry](https://python-poetry.org/): Python packaging and dependency management.
It has also been configured to have a productive dev experience out of the box in [VS Code](https://code.visualstudio.com/), see the [.vscode](./.vscode) folder.

