import logging 
except ConnectionError as e:
	logging.error('Ошибка сети')
	raise ConnectionError('Ошибка сети')

except ConnectionError:
	logging.error('Ошибка сети')
	raise
