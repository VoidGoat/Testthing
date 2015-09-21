
eli = [{"Cavalier":["Nick","Kajetan"], "Sugarplum":["Valerie","Hailan"], "Nutcracker":["Eli","Kajetan"], "Clara":["Katherine","Maggie"], "RoseQ":["Erin","Taylor"], "RoseK":["Nick","Kevin"], "Boydoll":["Eli","Luke"],"Girldoll":["Bella","Maggie"],"Spanish":["Peyton","Lara"],"Chinese":["Bella","Lara"],"ArabianF":["Erin","Peyton"],"ArabianM":["Ben","Kevin"]}, 0, "Eli"]
kajetan = [{"Cavalier":["Nick","Kajetan"], "Sugarplum":["Valerie","Hailan"], "Nutcracker":["Eli","Kajetan"], "Clara":["Katherine","Lily"], "RoseQ":["Erin","Taylor"], "RoseK":["Ben","Kevin"], "Boydoll":["Eli","Luke"],"Girldoll":["Maggie","Bella"],"Spanish":["Peyton","Angie","Bella","Lara"],"Chinese":["Maggie","Bella"],"ArabianF":["Erin","Taylor"],"ArabianM":["Ben","Kevin"]},0, "Kajetan"]
erin = [{"Cavalier":["Nick"], "Sugarplum":["Taylor","Valerie"], "Nutcracker":["Kajetan"], "Clara":["Lily", "Katherine"], "RoseQ":["Erin","Hailan"], "RoseK":["Ben","Kevin"], "Boydoll":["Eli"],"Girldoll":["Irina","Maggie"],"Spanish":["Bella","Angie","Peyton","Hailan"],"Chinese":["Maggie","Katherine"],"ArabianF":["Erin","Lara"],"ArabianM":["Ben","Kevin"]}, 0, "Erin"]
nick = [{"Cavalier":["Nick","Kajetan"], "Sugarplum":["Valerie","Hailan"], "Nutcracker":["Eli","Kajetan"], "Clara":["Maggie","Lily"], "RoseQ":["Erin","Taylor"], "RoseK":["Nick","Kajetan"], "Boydoll":["Eli","Luke"],"Girldoll":["Bella","Katherine"],"Spanish":["Peyton","Luke","Lara"],"Chinese":["Sara","Irina"],"ArabianF":["Erin","Taylor"],"ArabianM":["Ben","Kevin"]}, 0, "Nick"]

participants = [eli, kajetan, erin, nick]
masterList = {"Cavalier":["Nick","Kajetan"], "Sugarplum":["Taylor","Valerie"], "Nutcracker":["Kevin","Eli"], "Clara":["Lily","Maggie"], "RoseQ":["Erin","Lara"], "RoseK":["Kevin","Nick"], "Boydoll":["Nick","Eli"],"Girldoll":["Valerie","Angie"],"Spanish":["Peyton","Valerie","Taylor","Angie","Luke"],"Chinese":["Sara","Hailan"],"ArabianF":["Hailan","Dana"],"ArabianM":["Ben"]}

for p in participants:
    for i in p[0]:
        for m in masterList[i]:
            if m in p[0][i]:
                p[1] += 1
for p in participants:
    print (p[2] + ": " + str(p[1]))
