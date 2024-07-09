from .config import settings


api_base_url = f'http://localhost:{settings.API_MOCKS_PORT}'


class OrderClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        
    def get_order_packages(id: str):
        pass
    
class PackageClient:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        
    def updated_package(id: str, body: dict):
        pass
    

order_client = OrderClient(api_base_url)
package_client = PackageClient(api_base_url)