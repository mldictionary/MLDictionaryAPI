from enum import unique, Enum


@unique
class EnvironmentEnum(Enum):
    LOCAL = 'Local'
    DEVELOPMENT = 'Development'
    TESTING = 'Testing'
    PRODUCTION = 'Production'
