class MissingError(Exception):

    def __init__(self, logger):
        super().__init__(self)
        self.logger = logger

    def __str__(self):
        self.logger.warning("【异常】找不到相关图像")