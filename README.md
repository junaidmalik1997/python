# Welcome to Github Actions Migrations Project 

## Github Actions

 GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.

GitHub Actions goes beyond just DevOps and lets you run workflows when other events happen in your repository. For example, you can run a workflow to automatically add the appropriate labels whenever someone creates a new issue in your repository.

GitHub provides Linux, Windows, and macOS virtual machines to run your workflows, or you can host your own self-hosted runners in your own data center or cloud infrastructure.

## Why Switch to Github Actions

###  It’s all Managed by GitHub
The first and foremost plus point of GitHub Actions over Jenkins is the ease of setup in GitHub Actions. GitHub Actions operate in the cloud. You also have the option of running it locally, which is called a runner. On the contrary, Jenkins does not have an officially managed service offering.

###  Seamless Experience
At first, Jenkins seems more flexible than GitHub Actions. Jenkins is mainly based on accounts and triggers and centers on builds. These do not conform to GitHub events. In contrast to this, GitHub actions cover a wide range. Thus, there is a GitHub Action for every GitHub event.

### Built for Scale
GitHub Actions by default follows the master-slave (coordinator and build nodes) pattern as opposed to the sequential pipeline Jenkins offers us.
However, similar setup is possible with Jenkins but will require additional effort and knowledge to get it up and running.

### Caching Mechanism
In Github Actions you can write yor own mechanism if you require caching. This can be achieved by using plugins in jenkins but they have their own disadvantages like keeping them up to date.


- There are numerous reasons to choose GitHub Actions over Jenkins, but incredible extensibility coupled with relative simplicity stands out as pivotal. GitHub Actions is flexible enough to support almost any conceivable workflow while being powerful enough to handle enterprise-grade concerns.


## The components of GitHub Actions

### Workflows
A workflow is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.

Workflows are defined in the `.github/workflows` directory in a repository, and a repository can have multiple workflows, each of which can perform a different set of tasks. For example, you can have one workflow to build and test pull requests, another workflow to deploy your application every time a release is created, and still another workflow that adds a label every time someone opens a new issue.

### Events
An event is a specific activity in a repository that triggers a workflow run. For example, activity can originate from GitHub when someone creates a pull request, opens an issue, or pushes a commit to a repository. You can also trigger a workflow run on a schedule, by posting to a REST API, or manually.

### Jobs
A job is a set of steps in a workflow that execute on the same runner. Each step is either a shell script that will be executed, or an action that will be run. Steps are executed in order and are dependent on each other. Since each step is executed on the same runner, you can share data from one step to another.

You can configure a job's dependencies with other jobs; by default, jobs have no dependencies and run in parallel with each other. When a job takes a dependency on another job, it will wait for the dependent job to complete before it can run.

### Actions
An action is a custom application for the GitHub Actions platform that performs a complex but frequently repeated task. Use an action to help reduce the amount of repetitive code that you write in your workflow files. An action can pull your git repository from GitHub, set up the correct toolchain for your build environment, or set up the authentication to your cloud provider. You can write your own actions, or you can find actions to use in your workflows in the GitHub Marketplace.

### Runners
A runner is a server that runs your workflows when they're triggered. Each runner can run a single job at a time. GitHub provides Ubuntu Linux, Microsoft Windows, and macOS runners to run your workflows; each workflow run executes in a fresh, newly-provisioned virtual machine. GitHub also offers larger runners, which are available in larger configurations. 

#### Self Hosted Runners
A self-hosted runner is a system that you deploy and manage to execute jobs from GitHub Actions on GitHub.com. Self-hosted runners offer more control of hardware, operating system, and software tools than GitHub-hosted runners provide. With self-hosted runners, you can create custom hardware configurations that meet your needs with processing power or memory to run larger jobs, install software available on your local network, and choose an operating system not offered by GitHub-hosted runners. Self-hosted runners can be physical, virtual, in a container, on-premises, or in a cloud.

You can add self-hosted runners at various levels in the management hierarchy:

- Repository-level runners are dedicated to a single repository.
- Organization-level runners can process jobs for multiple repositories in an organization.
- Enterprise-level runners can be assigned to multiple organizations in an enterprise account.

## Migrated Applications
Following is a list of applications which were migrated from Jenkins to Github Actions.
- scorecard
- notify_rewards
- p66_underperformers_report
- Point Expiration
- scheduled-rewards
- Wingpoints_poh_report
- lfp_reporting
- update-oil-ids
- altria-customers2
- greeneville-newspaper-icontrol-daily
- millers-epiphany-report
- oncue-bybe-pipeline-cron-task
- ridleys-redemptions
- aloha-daily-trxs
- aloha-import
- bybe-daily
- petes-tiers-build
- petes-tiers-cron
- zipcode-scrub
- automated-mysql-backup-verification-coalition
- automated-mysql-backup-verification-proprietary
- deployment-auroratest-job
- deployment-honeymoney-job
- deployment-proptwo-job
- pr-builder-integration-testing
- loyalty
- marketing-velocity-service
- marketing-velocity-service-integration
- promo-builder-api
- query-caching-service
- query-caching-service-integration
- api-testing
- automated-promobuilder-testing
- automated-selenium-suite

All of these applications are hosted on self hosted runners. We used aws ec2 instance as a runner. There are two strategies for using self hosted runners.

- We can set up multiple ec2 instances with less hardware resources and configure one runner on every instance.
- We can use single larger instance and configure multiple runners on it.

We can chose either of the above mentioned strategies, depending on our requirements. To register a single self hosted runner we can run following script.

### Create a folder
- `mkdir actions-runner && cd actions-runner`

### Download the latest runner package
- `curl -o actions-runner-linux-x64-2.299.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.299.1/actions-runner-linux-x64-2.299.1.tar.gz`

### Optional: Validate the hash
- `echo "147c14700c6cb997421b9a239c012197f11ea9854cd901ee88ead6fe73a72c74  actions-runner-linux-x64-2.299.1.tar.gz" | shasum -a 256 -c`

### Extract the installer
- $ tar xzf ./actions-runner-linux-x64-2.299.1.tar.gz

### Create the runner and start the configuration experience
- ` ./config.sh --url https://github.com/username/repo-name --token <Your token here>`

### Last step, run it!
- `./run.sh`

### Use this YAML in your workflow file for each job
- `runs-on: self-hosted`

This script can also be found at Settings-->Actions-->Runners-->New Self Hosted Runners.




