#1-misol
# def orta_arifmetik_topish(list1, list2):
#     umumiy_elementlar_soni = len(list1) + len(list2)
#     umumiy_qiymat = sum(list1) + sum(list2)
#     orta_arifmetik = umumiy_qiymat / umumiy_elementlar_soni
#     return orta_arifmetik

# list1 = [1, 1, 3, 4, 4, 5, 6, 7]
# list2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
# print(orta_arifmetik_topish(list1, list2))

#2-misol
# def boshiga_qoshish(string, lista):
#     yangi_lista = [string + str(element) for element in lista]
#     return yangi_lista

# input_list = [1, 4, 3, 9]
# input_string = "RM"
# output_list = boshiga_qoshish(input_string, input_list)
# print(output_list)

#3-misol
# input_list = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

# max_sum_list = max(input_list, key=sum)
# print(max_sum_list)

#4-misol
# def butun_sonlar_soni(royxat):
#     soni = sum(isinstance(x, int) for x in royxat)
#     return soni

# input_list = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# output = butun_sonlar_soni(input_list)
# print(output)

#5-misol
# def eng_kop_takrorlanuvchi(royxat):
#     takrorlanuvchi_sonlar = {}
#     for element in royxat:
#         if royxat.count(element) > 1:
#             takrorlanuvchi_sonlar[element] = royxat.count(element)
#     if takrorlanuvchi_sonlar:
#         eng_kop_takrorlanuvchi_element = max(takrorlanuvchi_sonlar, key=takrorlanuvchi_sonlar.get)
#         takrorlanish_soni = takrorlanuvchi_sonlar[eng_kop_takrorlanuvchi_element]
#         print(f"{eng_kop_takrorlanuvchi_element} -> {takrorlanish_soni} marta")

# input_list = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
# eng_kop_takrorlanuvchi(input_list)

#6-misol
# def sonni_qoshish_va_qaytarish(royxat):
#     son = int(''.join(map(str, royxat))) + 1
#     natija = list(map(int, str(son)))
#     return natija

# input_list1 = [1, 2, 3]
# input_list2 = [9]
# input_list3 = [9, 9, 9, 9]

# output1 = sonni_qoshish_va_qaytarish(input_list1)
# output2 = sonni_qoshish_va_qaytarish(input_list2)
# output3 = sonni_qoshish_va_qaytarish(input_list3)

# print(output1)
# print(output2)
# print(output3)

#7-misol
# def kvadratlar(sonlar):
#     kvadratlar_royxati = [x ** 2 for x in sonlar]
#     return kvadratlar_royxati

# n = int(input("Qancha son kiritmoqchisiz? "))
# print(f"{n} ta sonni kiritng:")
# sonlar = list(map(int, input().split()))

# natija = kvadratlar(sonlar)
# print(natija)

#8-misol
# def boshiga_qoshish(sonlar, nomlar):
#     yangi_royxat = [nomlar[i] + str(sonlar[i]) for i in range(len(sonlar))]
#     return yangi_royxat

# sonlar = [1, 4, 3, 9]
# nomlar = ['chelsea', 'real', 'barca', 'MU']
# natija = boshiga_qoshish(sonlar, nomlar)
# print(natija)

#9-misol
# def eng_katta_topish(list):
#     return max(list)

# input_list = [4, 9, 6, 2, 8]
# output = eng_katta_topish(input_list)
# print("Eng katta element:", output)

#10-misol
# def fibonachi(son):
#     a, b = 0, 1
#     fibonachi_sonlar = []
#     while b <= son:
#         fibonachi_sonlar.append(b)
#         a, b = b, a + b
#     return fibonachi_sonlar

# n = int(input("Fibonachi sonlarini qancha chiqarishni xohlaysiz? "))
# natija = fibonachi(n)
# print("Output:", natija)









