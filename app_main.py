import os, sys

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

sumoBinary = "d:/software/Sumo/bin/sumo-gui.exe"
sumoCmd = [sumoBinary, "-c", "D:/software/Sumo/doc/examples/sumo/simple_nets/cross/cross3ltl/test.sumocfg"]

import traci
traci.start(sumoCmd)
step = 0
while step < 1000:
   traci.simulationStep()
   print('...')
   #if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
   #    traci.trafficlight.setRedYellowGreenState("0", "GrGr")
   step += 1

traci.close()
