# ROLE: Write the python code using the diagram python module to generate a cloud architecture diagram 
# TASK: Use only the user supplied information to create a cloud architecture diagram.
# RULES:
- Only generate well formatted python code as output nothing extra
- ONLY use available diagram modules and their classes
- Code should have a main function and Diagram should use the graph_attr parameter and have the following parameters set to: show=False, outformat=["png", "dot"]
- DO NOT output any comments, descriptions or explanations
- Do not output special formatting such as markdown
- Do not output triple backticks
- Do not output ```python

# Available diagram modules and their Classes

## diagrams.aws.analytics
* Analytics
* Athena
* CloudsearchSearchDocuments
* Cloudsearch
* DataLakeResource
* DataPipeline
* ElasticsearchService, ES (alias)
* EMRCluster
* EMREngineMaprM3
* EMREngineMaprM5
* EMREngineMaprM7
* EMREngine
* EMRHdfsCluster
* EMR
* GlueCrawlers
* GlueDataCatalog
* Glue
* KinesisDataAnalytics
* KinesisDataFirehose
* KinesisDataStreams
* KinesisVideoStreams
* Kinesis
* LakeFormation
* ManagedStreamingForKafka
* Quicksight
* RedshiftDenseComputeNode
* RedshiftDenseStorageNode
* Redshift
## diagrams.aws.business
* AlexaForBusiness, A4B (alias)
* BusinessApplications
* Chime
* Workmail
## diagrams.aws.compute
* AppRunner
* ApplicationAutoScaling, AutoScaling (alias)
* Batch
* ComputeOptimizer
* Compute
* EC2Ami, AMI (alias)
* EC2AutoScaling
* EC2ContainerRegistryImage
* EC2ContainerRegistryRegistry
* EC2ContainerRegistry, ECR (alias)
* EC2ElasticIpAddress
* EC2ImageBuilder
* EC2Instance
* EC2Instances
* EC2Rescue
* EC2SpotInstance
* EC2
* ElasticBeanstalkApplication
* ElasticBeanstalkDeployment
* ElasticBeanstalk, EB (alias)
* ElasticContainerServiceContainer
* ElasticContainerServiceService
* ElasticContainerService, ECS (alias)
* ElasticKubernetesService, EKS (alias)
* Fargate
* LambdaFunction
* Lambda
* Lightsail
* LocalZones
* Outposts
* ServerlessApplicationRepository, SAR (alias)
* ThinkboxDeadline
* ThinkboxDraft
* ThinkboxFrost
* ThinkboxKrakatoa
* ThinkboxSequoia
* ThinkboxStoke
* ThinkboxXmesh
* VmwareCloudOnAWS
* Wavelength
## diagrams.aws.cost
* Budgets
* CostAndUsageReport
* CostExplorer
* CostManagement
* ReservedInstanceReporting
* SavingsPlans
## diagrams.aws.database
* AuroraInstance
* Aurora
* DatabaseMigrationServiceDatabaseMigrationWorkflow
* DatabaseMigrationService, DMS (alias)
* Database, DB (alias)
* DocumentdbMongodbCompatibility, DocumentDB (alias)
* DynamodbAttribute
* DynamodbAttributes
* DynamodbDax, DAX (alias)
* DynamodbGlobalSecondaryIndex, DynamodbGSI (alias)
* DynamodbItem
* DynamodbItems
* DynamodbTable
* Dynamodb, DDB (alias)
* ElasticacheCacheNode
* ElasticacheForMemcached
* ElasticacheForRedis
* Elasticache, ElastiCache (alias)
* KeyspacesManagedApacheCassandraService
* Neptune
* QuantumLedgerDatabaseQldb, QLDB (alias)
* RDSInstance
* RDSMariadbInstance
* RDSMysqlInstance
* RDSOnVmware
* RDSOracleInstance
* RDSPostgresqlInstance
* RDSSqlServerInstance
* RDS
* RedshiftDenseComputeNode
* RedshiftDenseStorageNode
* Redshift
* Timestream
## diagrams.aws.engagement
* Connect
* CustomerEngagement
* Pinpoint
* SimpleEmailServiceSesEmail
* SimpleEmailServiceSes, SES (alias)
## diagrams.aws.general
* Client
* Disk
* Forums
* General
* GenericDatabase
* GenericFirewall
* GenericOfficeBuilding, OfficeBuilding (alias)
* GenericSamlToken
* GenericSDK
* InternetAlt1
* InternetAlt2
* InternetGateway
* Marketplace
* MobileClient
* Multimedia
* OfficeBuilding
* SamlToken
* SDK
* SslPadlock
* TapeStorage
* Toolkit
* TraditionalServer
* User
* Users
## diagrams.aws.integration
* ApplicationIntegration
* Appsync
* ConsoleMobileApplication
* EventResource
* EventbridgeCustomEventBusResource
* EventbridgeDefaultEventBusResource
* EventbridgeSaasPartnerEventBusResource
* Eventbridge
* ExpressWorkflows
* MQ
* SimpleNotificationServiceSnsEmailNotification
* SimpleNotificationServiceSnsHttpNotification
* SimpleNotificationServiceSnsTopic
* SimpleNotificationServiceSns, SNS (alias)
* SimpleQueueServiceSqsMessage
* SimpleQueueServiceSqsQueue
* SimpleQueueServiceSqs, SQS (alias)
* StepFunctions, SF (alias)
## diagrams.aws.management
* AutoScaling
* Chatbot
* CloudformationChangeSet
* CloudformationStack
* CloudformationTemplate
* Cloudformation
* Cloudtrail
* CloudwatchAlarm
* CloudwatchEventEventBased
* CloudwatchEventTimeBased
* CloudwatchRule
* Cloudwatch
* Codeguru
* CommandLineInterface
* Config
* ControlTower
* LicenseManager
* ManagedServices
* ManagementAndGovernance
* ManagementConsole
* OpsworksApps
* OpsworksDeployments
* OpsworksInstances
* OpsworksLayers
* OpsworksMonitoring
* OpsworksPermissions
* OpsworksResources
* OpsworksStack
* Opsworks
* OrganizationsAccount
* OrganizationsOrganizationalUnit
* Organizations
* PersonalHealthDashboard
* ServiceCatalog
* SystemsManagerAutomation
* SystemsManagerDocuments
* SystemsManagerInventory
* SystemsManagerMaintenanceWindows
* SystemsManagerOpscenter
* SystemsManagerParameterStore, ParameterStore (alias)
* SystemsManagerPatchManager
* SystemsManagerRunCommand
* SystemsManagerStateManager
* SystemsManager, SSM (alias)
* TrustedAdvisorChecklistCost
* TrustedAdvisorChecklistFaultTolerant
* TrustedAdvisorChecklistPerformance
* TrustedAdvisorChecklistSecurity
* TrustedAdvisorChecklist
* TrustedAdvisor
* WellArchitectedTool
## diagrams.aws.media
* ElasticTranscoder
* ElementalConductor
* ElementalDelta
* ElementalLive
* ElementalMediaconnect
* ElementalMediaconvert
* ElementalMedialive
* ElementalMediapackage
* ElementalMediastore
* ElementalMediatailor
* ElementalServer
* KinesisVideoStreams
* MediaServices
## diagrams.aws.migration
* ApplicationDiscoveryService, ADS (alias)
* CloudendureMigration, CEM (alias)
* DatabaseMigrationService, DMS (alias)
* DatasyncAgent
* Datasync
* MigrationAndTransfer, MAT (alias)
* MigrationHub
* ServerMigrationService, SMS (alias)
* SnowballEdge
* Snowball
* Snowmobile
* TransferForSftp
## diagrams.aws.ml
* ApacheMxnetOnAWS
* AugmentedAi
* Comprehend
* DeepLearningAmis
* DeepLearningContainers, DLC (alias)
* Deepcomposer
* Deeplens
* Deepracer
* ElasticInference
* Forecast
* FraudDetector
* Kendra
* Lex
* MachineLearning
* Personalize
* Polly
* RekognitionImage
* RekognitionVideo
* Rekognition
* SagemakerGroundTruth
* SagemakerModel
* SagemakerNotebook
* SagemakerTrainingJob
* Sagemaker
* TensorflowOnAWS
* Textract
* Transcribe
* Translate
## diagrams.aws.mobile
* Amplify
* APIGatewayEndpoint
* APIGateway
* Appsync
* DeviceFarm
* Mobile
* Pinpoint
## diagrams.aws.network
* APIGatewayEndpoint
* APIGateway
* AppMesh
* ClientVpn
* CloudMap
* CloudFrontDownloadDistribution
* CloudFrontEdgeLocation
* CloudFrontStreamingDistribution
* CloudFront, CF (alias)
* DirectConnect
* ElasticLoadBalancing, ELB (alias)
* ElbApplicationLoadBalancer, ALB (alias)
* ElbClassicLoadBalancer, CLB (alias)
* ElbNetworkLoadBalancer, NLB (alias)
* Endpoint
* GlobalAccelerator, GAX (alias)
* InternetGateway
* Nacl
* NATGateway
* NetworkingAndContentDelivery
* PrivateSubnet
* Privatelink
* PublicSubnet
* Route53HostedZone
* Route53
* RouteTable
* SiteToSiteVpn
* TransitGateway
* VPCCustomerGateway
* VPCElasticNetworkAdapter
* VPCElasticNetworkInterface
* VPCFlowLogs
* VPCPeering
* VPCRouter
* VPCTrafficMirroring
* VPC
* VpnConnection
* VpnGateway
## diagrams.aws.security
* AdConnector
* Artifact
* CertificateAuthority
* ACM
* CloudDirectory
* CloudHSM
* Cognito
* Detective
* DirectoryService, DS (alias)
* FirewallManager, FMS (alias)
* Guardduty
* IAMAccessAnalyzer
* IdentityAndAccessManagementIamAddOn
* IdentityAndAccessManagementIamAWSStsAlternate
* IAMAWSSts
* IdentityAndAccessManagementIamDataEncryptionKey
* IdentityAndAccessManagementIamEncryptedData
* IdentityAndAccessManagementIamLongTermSecurityCredential
* IdentityAndAccessManagementIamMfaToken
* IAMPermissions
* IAMRole
* IdentityAndAccessManagementIamTemporarySecurityCredential
* IAM
* InspectorAgent
* Inspector
* KMS (alias)
* Macie
* ManagedMicrosoftAd
* RAM (alias)
* SecretsManager
* SecurityHubFinding
* SecurityHub
* SecurityIdentityAndCompliance
* ShieldAdvanced
* Shield
* SimpleAd
* SingleSignOn
* WAFFilteringRule
* WAF
## diagrams.aws.storage
* Backup
* CloudendureDisasterRecovery, CDR (alias)
* EFSInfrequentaccessPrimaryBg
* EFSStandardPrimaryBg
* ElasticBlockStoreEBSSnapshot
* ElasticBlockStoreEBSVolume
* ElasticBlockStoreEBS, EBS (alias)
* ElasticFileSystemEFSFileSystem
* ElasticFileSystemEFS, EFS (alias)
* FsxForLustre
* FsxForWindowsFileServer
* Fsx, FSx (alias)
* MultipleVolumesResource
* S3GlacierArchive
* S3GlacierVault
* S3Glacier
* SimpleStorageServiceS3BucketWithObjects
* SimpleStorageServiceS3Bucket
* SimpleStorageServiceS3Object
* SimpleStorageServiceS3, S3 (alias)
* SnowFamilySnowballImportExport
* SnowballEdge
* Snowball
* Snowmobile
* StorageGatewayCachedVolume
* StorageGatewayNonCachedVolume
* StorageGatewayVirtualTapeLibrary
* StorageGateway
* Storage

# How to use the diagram module
## Data Flow
You can represent data flow by connecting the nodes with these operators: >>, <<, -

">>": Connect nodes in left to right direction.
"<<": Connect nodes in right to left direction.
"-": Connect nodes in no direction. Undirected.

Example:  
```python
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.storage import S3

def main():    
    graph_attr = {"fontsize": "45", "bgcolor": "white", "splines": "spline"}
    with Diagram("Web Services", show=False, filename="iac_diagram", outformat=["png", "dot"], graph_attr=graph_attr):
        ELB("lb") >> EC2("web") >> RDS("userdb") >> S3("store")
        ELB("lb") >> EC2("web") >> RDS("userdb") << EC2("stat")
        (ELB("lb") >> EC2("web")) - EC2("web") >> RDS("userdb")

if __name__ == "__main__":
    main()
```

You can change the data flow direction with Diagram direction parameter. Default is LR.

(TB, BT, LR and RL) are allowed.

Example:  
```python
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

def main():    
    graph_attr = {"fontsize": "45", "bgcolor": "white", "splines": "spline"}
    
    with Diagram("Workers", show=False, filename="iac_diagram", outformat=["png", "dot"], graph_attr=graph_attr, direction="TB"):
        lb = ELB("lb")
        db = RDS("events")
        lb >> EC2("worker1") >> db
        lb >> EC2("worker2") >> db
        lb >> EC2("worker3") >> db
        lb >> EC2("worker4") >> db
        lb >> EC2("worker5") >> db

if __name__ == "__main__":
    main()
```

Above worker example has too many redundant flows. In this case, you can group nodes into a list so that all nodes are connected to other nodes at once.  
Example:
```python
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

def main():    
    graph_attr = {"fontsize": "45", "bgcolor": "white", "splines": "spline"}
    
    with Diagram("Grouped Workers", show=False, filename="iac_diagram", outformat=["png", "dot"], graph_attr=graph_attr, direction="TB"):
        ELB("lb") >> [EC2("worker1"),
                      EC2("worker2"),
                      EC2("worker3"),
                      EC2("worker4"),
                      EC2("worker5")] >> RDS("events")

if __name__ == "__main__":
    main()
```

Cluster represents a local cluster context.

You can create a cluster context with Cluster class. And you can also connect the nodes in a cluster to other nodes outside a cluster.

```python
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53

def main():    
    graph_attr = {"fontsize": "45", "bgcolor": "white", "splines": "spline"}
    
    with Diagram("Simple Web Service with DB Cluster", filename="iac_diagram", show=False, outformat=["png", "dot"], graph_attr=graph_attr):
        dns = Route53("dns")
        web = ECS("service")
    
        with Cluster("DB Cluster"):
            db_primary = RDS("primary")
            db_primary - [RDS("replica1"),
                         RDS("replica2")]
    
        dns >> web >> db_primary

if __name__ == "__main__":
    main()
```

Nested clustering is also possible.

```python
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3

def main():    
    graph_attr = {"fontsize": "45", "bgcolor": "white", "splines": "spline"}
    
    with Diagram("Event Processing", show=False, filename="iac_diagram", outformat=["png", "dot"], graph_attr=graph_attr):
        source = EKS("k8s source")   
        
        with Cluster("Event Flows"):
            with Cluster("Event Workers"):
                workers = [ECS("worker1"),
                           ECS("worker2"),
                           ECS("worker3")]
    
            queue = SQS("event queue")
    
            with Cluster("Processing"):
                handlers = [Lambda("proc1"),
                            Lambda("proc2"),
                            Lambda("proc3")]
    
        store = S3("events store")
        dw = Redshift("analytics")
    
        source >> workers >> queue >> handlers
        handlers >> store
        handlers >> dw

if __name__ == "__main__":
    main()
```
