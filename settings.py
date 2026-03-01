from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        chk = value.lower()
        if chk not in ["dev", "test", "prod"]:
            raise ValueError("ENVIRONMENT os not dev/test/prod")
        #    ... # implement me!
        # prepare validator that will check whether the value of ENVIRONMENT is in (dev, test, prod)
        return value
