import logging

# 设置日志模块的配置
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("bin\\log.txt", encoding="utf-8", mode="a")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s -- %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
 
logger.addHandler(handler)
logger.addHandler(console)