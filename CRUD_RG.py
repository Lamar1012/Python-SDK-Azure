from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

credential = AzureCliCredential()

#provide subscription ID

subscription_id = '40dfd449-59b7-457d-8248-391a10a5d290'

resource_mgmt_client = ResourceManagementClient(credential,subscription_id)

resource_group_list = resource_mgmt_client.resource_groups.list()
for resource in resource_group_list:
    print(resource.name)

RGname = 'rg-eastus'

# Create Resource Group with name and location

resource_groups_params = {'location':'eastus'}

# resource_mgmt_client.resource_groups.create_or_update(
# RGname, resource_groups_params)

print('Resource Group is Created!')

#READ
list_of_resource_groups = resource_mgmt_client.resource_groups.list()
for rg in list_of_resource_groups:
    if rg.name == RGname:
        print("Resource Group Found!")
    else:
        print("RG not found!")

#UPDATE

resource_groups_params.update(tags={"Cloudsecurity": "training"})
resource_mgmt_client.resource_groups.update(RGname, resource_groups_params)
print("Update is Successful!")

# READ - all items in resource group 
resource_list= resource_mgmt_client.resources.list_by_resource_group(RGname)
for resource in resource_list:
    print(resource.name + ", " + resource.location)

print("Print list of resources from another resource group")
resource_list= resource_mgmt_client.resources.list_by_resource_group("NetworkWatcherRG")
for resource in resource_list:
    print(resource.name + ", " + resource.location)

#DELETE

delete_async_op = resource_mgmt_client.resource_groups.begin_delete(RGname)

# Will wait on delete operation to finish.
delete_async_op.wait()
print("RG is now deleted!")
