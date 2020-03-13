def Name2Color(G,colordict):

#The function iterates through the edge data of the graph and assign colors
#based on a dictionary. Keys are the prefix of road names and values are colors

    for u,v,k,d in G.edges(keys=True, data=True):
        if 'name' in d and type(d['name'])!=list:
            sp = d['name'].split()
            for m in range(len(colordict)):
                if sp[0].lower() == list(colordict.keys())[m]:
                    d['color'] = list(colordict.items())[m][1]
        elif 'name' in d and type(d['name'])==list:
            dls =  d['name'][0]
            sp = dls.split()
            for m in range(len(colordict)):
                if sp[0].lower() == list(colordict.keys())[m]:
                    d['color'] = list(colordict.items())[m][1]
    return G

def ListRoadPrefixes (G):
    # The function get all the roads names in the graph, if an edge contains
    #multiple names it gets only the first one. Then we obtain the prefixses
    #and put them in a list

    # Get name of roads
    ce= [d for u,v,k,d in G.edges(keys=True, data='name')]
    #Get a list of all of the street prefixes
    fns = []
    for n in ce:
        if n!= None and type(n)!=list:
            ns = n.split()
            fns.append(ns[0])
        elif n!= None and type(n)==list:
            nls = n[0]
            ns = nls.split()
            fns.append(ns[0])
    return fns
