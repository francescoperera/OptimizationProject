"Most up-to-date script"


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

			  # "A,B,C"
start = [[1,0,0],
		[1,0,0],
		[0,1,0],
		[0,1,0],
		[0,0,1],
		[0,0,1]]  # pair AB, outbound from A, inbound to B

end = [[0,1,0],
		[0,0,1],
		[1,0,0],
		[0,0,1],
		[1,0,0],
		[0,1,0]]

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
		xijt = emptyCargoPlanes[i][j]
		objExpr += emptyCost[i] * xijt

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

#outboundPlanes = LinExpr()

#inboundPlanes = LinExpr()
"""
for i in range(len(dailyAirportPairs)):
	#outboundPlanes = LinExpr()

	#inboundPlanes = LinExpr()
	for j in range(1,days):
		for k in range(len(airports)):
			print "airport pair, day,airport :" + dailyAirportPairs[i] + "," + str(j) + ","+airports[k]
			outboundEmptyPlane = emptyCargoPlanes[i][j] * end[i][k]
			print "outboundEmptyPlane is " + str(outboundEmptyPlane)
			outboundPlanes += outboundEmptyPlane
			outboundCargoPlane = cargoPlanes[i][j] * end[i][k]
			print "outboundCargoPlane is " + str(outboundCargoPlane)
			outboundPlanes += outboundCargoPlane
			outboundPlanes += groundPlanes[k][j] * start[i][k]
			print "z is " + str(groundPlanes[k][j])


			if  i == 0:
				l = 2
			elif i ==1:
				l = 4
			elif i == 2:
				l=0
			elif i ==3:
				l=5
			elif i == 4:
				l=2
			elif i == 5:
				l = 3

			inboundEmptyPlane = emptyCargoPlanes[l][j-1] * start[l][k]
			inboundPlanes += inboundEmptyPlane
			inboundCargoPlanes = cargoPlanes[l][j-1] * start[l][k]
			inboundPlanes += inboundCargoPlanes
			inboundPlanes += groundPlanes[k][j-1]* start[i][k]
"""
for i in range(len(airports)):
	#outboundPlanes = LinExpr()

	#inboundPlanes = LinExpr()
	for j in range(1,days):
		outboundPlanes = LinExpr()

		inboundPlanes = LinExpr()
		outboundPlanes += groundPlanes[i][j]
		inboundPlanes += groundPlanes[i][j-1]

		for k in range(len(dailyAirportPairs)):
			#print 
			#print "airport pair, day,airport :" + dailyAirportPairs[k] + "," + str(j) + ","+airports[i]
			outboundEmptyPlane = emptyCargoPlanes[k][j] * start[k][i]
			#print "outboundEmptyPlane is " + str(outboundEmptyPlane)
			outboundPlanes += outboundEmptyPlane
			outboundCargoPlane = cargoPlanes[k][j] * start[k][i]
			#print "outboundCargoPlane is " + str(outboundCargoPlane)
			outboundPlanes += outboundCargoPlane
			#outboundPlanes += groundPlanes[i][j] * start[k][i]
			#print "z is " + str(groundPlanes[i][j])

			if  k == 0:
				l = 2
			elif k ==1:
				l = 4
			elif k == 2:
				l=0
			elif k ==3:
				l=5
			elif k == 4:
				l=1 #2
			elif k == 5:
				l = 3

			if  start[k][i] == 0:
				inboundEmptyPlane = 0
				inboundCargoPlanes = 0
			else:
				inboundEmptyPlane = emptyCargoPlanes[l][j-1] * end[l][i]
				inboundCargoPlanes = cargoPlanes[l][j-1] * end[l][i]
			#print "inboundEmptyPlane is " + str(inboundEmptyPlane)
			inboundPlanes += inboundEmptyPlane
			#print "inboundCargoPlane is " + str(inboundCargoPlanes)
			#print
			inboundPlanes += inboundCargoPlanes
			#inboundPlanes += groundPlanes[i][j-1]* start[k][i]


		myModel.addConstr(lhs = outboundPlanes, sense = GRB.EQUAL, rhs = inboundPlanes, name = "planes flow balance "+airports[i]+str(j))

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

for i in range(len(airports)):
	outboundPlanes = LinExpr()
	inboundPlanes = LinExpr()

	outboundPlanes += groundPlanes[i][0]
	inboundPlanes += groundPlanes[i][4]
	for k in range(len(dailyAirportPairs)):
		print 
		print "airport pair, airport :" + dailyAirportPairs[k] + "," +airports[i]
		outboundEmptyPlane = emptyCargoPlanes[k][0] * start[k][i]
		print "outboundEmptyPlane is " + str(outboundEmptyPlane)
		outboundPlanes += outboundEmptyPlane
		outboundCargoPlane = cargoPlanes[k][0] * start[k][i]
		print "outboundCargoPlane is " + str(outboundCargoPlane)
		outboundPlanes += outboundCargoPlane
		#outboundPlanes += groundPlanes[k][0]

		if  k == 0:
			l = 2
		elif k ==1:
			l = 4
		elif k == 2:
			l=0
		elif k ==3:
			l=5
		elif k == 4:
			l=1 #2
		elif k == 5:
			l = 3

		inboundEmptyPlane = emptyCargoPlanes[l][4] * start[k][i]
		print "inboundEmptyPlane is " + str(inboundEmptyPlane)
		inboundPlanes += inboundEmptyPlane
		inboundCargoPlanes = cargoPlanes[l][4] * start[k][i]
		print "inboundCargoPlane is " + str(inboundCargoPlanes)
		print
		inboundPlanes += inboundCargoPlanes
		#inboundPlanes += groundPlanes[k][4]

	myModel.addConstr(lhs = outboundPlanes, sense = GRB.EQUAL, rhs = inboundPlanes, name = "wrap around planes flow balance " + airports[i])

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







