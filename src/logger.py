import logging

f_formattter = '%(asctime)s:%(levelname)s:%(name)s: %(message)s'
c_formatter = '[%(asctime)s] [%(levelname)-8s]> %(name)-12s: %(message)s'
logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
file_handler.setFormatter(logging.Formatter(f_formattter))
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(c_formatter))
console_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
