def mediaan(num_list):
    num_list.sort()
    even_oneven = len(num_list)%2
    if even_oneven == 0:
        index = len(num_list)/2 -1
        index2 = len(num_list)/2
        mediaan = (num_list[int(index)] + num_list[int(index2)])/2
        print(mediaan)
    else:
        index3 = len(num_list)/2
        print(num_list[int(index3)])

mediaan([1,1,2,3,4,4,5])
mediaan([7,8,9,103])
mediaan([1023,104,17,2])
mediaan([4,7,3,8,9,0,19])
