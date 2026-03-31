from abc import ABC, abstractmethod


class ConfigProvider[ConfigType](ABC):
    @abstractmethod
    async def get_config(self) -> ConfigType: ...


class MultiProjectConfigProvider[ConfigType](ABC):
    @abstractmethod
    async def get_config(self, project_id: int) -> ConfigType: ...


class StaticConfigProvider[T](ConfigProvider[T]):
    def __init__(self, config: T):
        self.config = config

    async def get_config(self) -> T:
        return self.config
