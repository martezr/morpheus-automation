import hvac
from morpheuscypher import Cypher

vault_token = Cypher(morpheus=morpheus).get('secret/vaulttoken')
vault_addr = sys.argv[0]

client = hvac.Client(
    url=vault_addr,
    token=vault_token
)

list_policies_resp = client.sys.list_policies()['data']['policies']
print('List of currently configured policies: %s' % ', '.join(list_policies_resp))
