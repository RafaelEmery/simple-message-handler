from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOCALSTACK_PORT: int
    API_MOCKS_PORT: int

    CANCELED_ORDERS_QUEUE_NAME: str
    ORDER_CANCELED_TOPIC_NAME: str
    PACKAGE_CANCELED_TOPIC_NAME: str
    
    class Config:
        env_file = '.env'


settings = Settings()