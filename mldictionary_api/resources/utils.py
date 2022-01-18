from mldictionary_api.domains.environment import EnvironmentEnum


limit_requests: dict[EnvironmentEnum, bool] = {
    EnvironmentEnum.DEVELOPMENT: False,
    EnvironmentEnum.LOCAL: True,
    EnvironmentEnum.PRODUCTION: True,
    EnvironmentEnum.TESTING: False,
}
