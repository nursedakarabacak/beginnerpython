 #verilen listedeki rakamlardan oluşan bir liste oluşturalim.
numbers = [1,2,3,4,5,6,7,8,9]
#list2 = []
#for number in numbers :
    #list2.append(number)

#print(list2)


#verilen listedeki rakamların karelerinden oluşan bir liste oluşturalim.
#list3 = []
#for number in numbers :
 #   list3.append(number**2)
#print(list3)


#list4 = [number**2 for number in numbers]
#print(list4)
#listeye eklenicek eleman nerede ekleneceği 
#  verilen listedeki çift rakamlardn bir liste 
#list5 =[]
#for number in numbers :
    #if number % 2 == 0 :
        #list5.append(number)

#print(list5)

#list6 = [number for number in numbers if number % 2 == 0]
#print(list6)
#listedeli çift rakamların karelerinden oluşan bir liste
#list7 = []
#for number in numbers:
    #if number % 2 == 0:
        #list7.append(number**2)
#print(list7)

#list8 = [ number**2 for number in numbers if number % 2 == 0]
#print(list8)

#verilen listedeki 4'ten büyük çift sayıların karelerinden oluşan bir liste oluşturali.
#list10 = []
#for number in numbers :
    #if number > 4 and number % 2  == 0:
        #list10.append(number**2)
#print(list10)

#list9 = [number*number  for number in numbers if numbers if number >4 and number % 2 == 0]
#print(list9)

numbers = [1,2,3,4]
letters = "abcd"
#[(1,'a),(1,b),(1,c),(1,d)...(4,d)] biçiminde ikililerden oluşan liste oluşturalim.
#list = []
#for number in numbers:
    #for letter in letters:
        #list.append((number,letter))
#print(list)

#list = [(number,letters) for number in numbers for letter in letters]
#print(list)

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
#list1'de olup list2'de olmayan elemanların karesinden oluşan bir liste oluşturalım.
#list = []
#for i in list1 :
    #if i not in list2 :
     #   list.append(i**2)
#print(list)
#list = [ i*i for i in list1 if i not in list2 ]
#print(list)


list_ = [[1,2,3],[4,5,6,7],[8,9,10,11,12]]
#verilen listedekn elemanları tek tek alan [1,2,3,4,5,6,7,8,9,10,11,12  ] şeklinde bir liste oluşturalım.
#list = []
#for i in list_: #her alt listesini sırası ile alır 
 #   for j in i: #i lestesinin içindeki elemanlara tek tek ulaşır.
  #      list.append(j)
#print(list)

#list = [j for i in list_  for j in i ]  #ilk listeye eklenecek elemanızmız,
#print(list)