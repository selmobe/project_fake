###########################################
###########################################
##
## author: Selmo Rodrigues
## realease: 0.0.0
##
##
##
#############################################


import time
from datetime import datetime

def simulated_service():
    end_time = time.time() + 5 * 60  # 5 minutos a partir do tempo atual
    while time.time() < end_time:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'Serviço em execução - {current_time}')
        time.sleep(10)

if __name__ == '__main__':
    # Apenas um ajuste no corpo dos dados
    simulated_service()
