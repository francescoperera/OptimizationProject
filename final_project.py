from gurobipy import *

airports = ['A','B','C']
dailyAirportPairs = ['AB','AC','BA','BC','CA','CB']
cargoTotalCapacity = 120000
days = 5 
groundCost = 10
emptyCost = [7,3,7,6,3,6]

#cargo demand for each origin- destination pair
demand = [[0 for i in range(days)] for j in range(len(dailyAirportPairs))]
demand[0][0] =  10
demand[0][1] =  20
demand[0][2] =  10
demand[0][3] =  40
demand[0][4] =  30
demand[1][0] =  5
demand[1][1] =  5
demand[1][2] =  5
demand[1][3] =  5
demand[1][4] =  5
demand[2][0] =  2.5
demand[2][1] =  2.5
demand[2][2] =  2.5
demand[2][3] =  2.5
demand[2][4] =  2.5
demand[3][0] =  2.5
demand[3][1] =  2.5
demand[3][2] =  2.5
demand[3][3] =  2.5
demand[3][4] =  2.5
demand[4][0] =  4
demand[4][1] =  4
demand[4][2] =  4
demand[4][3] =  4
demand[4][4] =  4
demand[5][0] =  40
demand[5][1] =  20
demand[5][2] =  30
demand[5][3] =  20
demand[5][4] =  40

outboundFrom = [[1,0,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1],[0,0,1]]  # pair AB, outbound from A, inbound to B
inboundTo = [[0,1,0],[0,0,1],[1,0,0],[0,0,1],[1,0,0],[0,1,0]]

#create model 
myModel = Model("cargoOperations")

#decision variables
emptyCargoPlanes = [[0 for i in range(days)] for j in range(len(dailyAirportPairs))]
for i in range(len(dailyAirportPairs)):
	for j in range(days):
		curVar = myModel.addVar(vtype = GRB.CONTINUOUS, name = "x"+dailyAirportPairs[i]+str(j))
		emptyCargoPlanes[i][j] = curVar

myModel.update()


cargoPlanes = [[0 for i in range(days)] for j in range(len(dailyAirportPairs))]
for i in range(len(dailyAirportPairs)):
	for j in range(days):
		curVar = myModel.addVar(vtype = GRB.CONTINUOUS, name = "y"+dailyAirportPairs[i]+str(j))
		cargoPlanes[i][j] = curVar

myModel.update()

availableCargo = [[0 for i in range(days)] for j in range(len(dailyAirportPairs))]
for i in range(len(dailyAirportPairs)):
	for j in range(days):
		curVar = myModel.addVar(vtype = GRB.CONTINUOUS, name = "u"+dailyAirportPairs[i]+str(j))
		availableCargo[i][j] = curVar

myModel.update()


groundPlanes = [[0 for i in range(days)] for j in range(len(airports))]
for i in range(len(airports)):
	for j in range(days):
		curVar = myModel.addVar(vtype = GRB.CONTINUOUS, name = "z"+airports[i]+str(j))
		groundPlanes[i][j] = curVar

myModel.update()

#linear expression for the objective
objExpr = LinExpr()
for i in range(len(dailyAirportPairs)):
	for j in range(days):
		yijt = emptyCargoPlanes[i][j]
		objExpr += emptyCost[i] * yijt

for i in range(len(airports)):
	for j in range(days):
		zit = groundPlanes[i][j]
		objExpr += groundCost * zit

myModel.setObjective(objExpr,GRB.MINIMIZE)

#constraint for cargo flow balance
for i in range(len(dailyAirportPairs)):
	for j in range(1,days):
		lhs = availableCargo[i][j]
		rhs = availableCargo[i][j-1] + demand[i][j-1] - cargoPlanes[i][j-1] 
		myModel.addConstr(lhs = lhs, sense = GRB.EQUAL, rhs = rhs , name = "cargo flow balance "+dailyAirportPairs[i]+str(j))

myModel.update()


for i in range(len(dailyAirportPairs)):
	outboundPlanes = LinExpr()

	inboundPlanes = LinExpr()
	for j in range(1,days):
		for k in range(len(airports)):
			outboundEmptyPlane = emptyCargoPlanes[i][j] * inboundTo[i][k]
			outboundPlanes += outboundEmptyPlane
			outboundCargoPlane = cargoPlanes[i][j] * inboundTo[i][k]
			outboundPlanes += outboundCargoPlane
			outboundPlanes += groundPlanes[k][j]

			inboundEmptyPlane = emptyCargoPlanes[i][j-1] * outboundFrom[i][k]
			inboundPlanes += inboundEmptyPlane
			inboundCargoPlanes = cargoPlanes[i][j-1] * outboundFrom[i][k]
			inboundPlanes += inboundCargoPlanes
			inboundPlanes += groundPlanes[k][j-1]

		myModel.addConstr(lhs = outboundPlanes, sense = GRB.EQUAL, rhs = inboundPlanes, name = "planes flow balance "+dailyAirportPairs[i]+str(j))

myModel.update()


for i in range(len(dailyAirportPairs)):
	for j  in range(days):
		left = cargoPlanes[i][j]
		right = availableCargo[i][j] + demand[i][j]

		myModel.addConstr(lhs = left,sense = GRB.LESS_EQUAL, rhs = right , name = "cargo planes constraint for pair "+ dailyAirportPairs[i]+ " on day " + str(j))

myModel.update()

for i in range(len(dailyAirportPairs)):
	l = availableCargo[i][0]
	r= availableCargo[i][4] + demand[i][4] - cargoPlanes[i][4] 
	myModel.addConstr(lhs = l, sense = GRB.EQUAL, rhs = r , name = "wrap around cargo flow balance")

myModel.update()

for i in range(len(dailyAirportPairs)):
	outboundPlanes = LinExpr()

	inboundPlanes = LinExpr()
	for k in range(len(airports)):
		outboundEmptyPlane = emptyCargoPlanes[i][0] * inboundTo[i][k]
		outboundPlanes += outboundEmptyPlane
		outboundCargoPlane = cargoPlanes[i][0] * inboundTo[i][k]
		outboundPlanes += outboundCargoPlane
		outboundPlanes += groundPlanes[k][0]

		inboundEmptyPlane = emptyCargoPlanes[i][4] * outboundFrom[i][k]
		inboundPlanes += inboundEmptyPlane
		inboundCargoPlanes = cargoPlanes[i][4] * outboundFrom[i][k]
		inboundPlanes += inboundCargoPlanes
		inboundPlanes += groundPlanes[k][4]

		myModel.addConstr(lhs = outboundPlanes, sense = GRB.EQUAL, rhs = inboundPlanes, name = "wrap around planes flow balance")

myModel.update()

# write the model to file 
myModel.write( filename = "cargoLP.lp" )

myModel.optimize()
#
print( "\nOptimal Objective: " + str( myModel.ObjVal ) )
print( "\nOptimal Solution:" )
solVars = myModel.getVars()
for var in solVars:
	print ( var.varName + " " + str( var.x))







