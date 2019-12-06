def verwijder_dubbel_1(a_list):
    nieuwe_lijst=[]
    for i in a_list:
        if i not in nieuwe_lijst:
            nieuwe_lijst.append(i)
    nieuwe_lijst.sort()
    print(nieuwe_lijst)

verwijder_dubbel_1([3,1,7,4,4,1,6])

def verwijder_dubbel_2(any_list):
    nieuwe_lijst=[]
    for i in any_list:
        if i not in nieuwe_lijst:
            nieuwe_lijst.append(i)
    
    print(nieuwe_lijst)


verwijder_dubbel_2([(1,2,3), ['a', 'b'], 2, 3, ['a', 'b'], 1])    
