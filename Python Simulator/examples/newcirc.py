inet['network'] = Network()
inet['simulator'] = Simulator(inet['network'])

# inet interface uses 'net' and 'sim'
net = inet['network']
sim = inet['simulator']

# create infinitely spiking neuron from t=0 onwards
Const = net.createInputTrain([1], True) 

# create nodes In and Re
In = net.createInputTrain([0,0,0,1], False) 
Re = net.createInputTrain([0,0,0,0,0,0,0,1], False) 

# create node Cin
Hld = net.createLIF(thr=1, V_reset=1, m=0.5)
net.createSynapse(Const, Hld, w=0.5, d=1)
net.createSynapse(In, Hld, w=1, d=1)
net.createSynapse(Re, Hld, w=-2, d=1)

Raster_1 = sim.createRaster()
Raster_1.addTarget(Const)
Raster_1.addTarget(In)
Raster_1.addTarget(Re)
Raster_1.addTarget(Hld)

Multimeter_1 = sim.createMultimeter()
Multimeter_1.addTarget(Hld)

