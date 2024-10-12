from opensearchpy import OpenSearch, helpers
hosts = [
    {'host': '<ipaddress>', 'port': 9200} # ipddress: localhost or 10.2.5.5, ... 
]

client = OpenSearch(
    hosts=hosts,
    http_auth=('admin', 'admin'), #default username and password for this distro
    use_ssl=False,
    verify_certs=False,  # Tương đương với --insecure
    request_timeout=10*60
)

# Kiểm tra kết nối bằng cách lấy thông tin cluster
try:
    info = client.info()
    print("Kết nối thành công đến Open Distro for Elasticsearch")
    print(info)
except Exception as e:
    print(f"Không thể kết nối đến Open Distro for Elasticsearch: {e}")