import os, sys
import time

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("请设置环境变量：SUMO_HOME")

sumoBinary = "d:/software/Sumo/bin/sumo-gui.exe" # 启动图形界面
#sumoBinary = 'd:/software/Sumo/bin/sumo.exe'
sumoCmd = [sumoBinary, "-c", "D:/software/Sumo/doc/examples/sumo/simple_nets/cross/cross3ltl/test.sumocfg"]

import traci
traci.start(sumoCmd)
step = 0
while step < 1000:
   traci.simulationStep()
   time.sleep(1.0)
   stepTime = traci.simulation.getTime()
   vehicle_ids = traci.vehicle.getIDList()
   print('{0}: {1};'.format(stepTime, len(vehicle_ids)))
   #if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
   #    traci.trafficlight.setRedYellowGreenState("0", "GrGr")
   step += 1
traci.close()
