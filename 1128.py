nlist=[]

menu = 0

while menu != 9:
    print("1. 리스트 출력")
    print("2. 리스트 추가")
    print("3. 리스트 삭제")
    print("4. 리스트 변경")
    print("5. 종료")
    print("-----------------")
    menu = int(input("매뉴 선택하세요"))
    print("-----------------")

    if menu == 1:
      
        for i in range(len(nlist)):
            print(i+1, nlist[i])
        print("-----------------")

    elif menu == 2:
        name = input("데이터 입력하시오:")
        nlist.append(name)
        print(nlist)
    elif menu == 3:
        name = input("삭제 하고자 하는 데이터 입력:")
        if name in nlist:
            nlist.remove(name)
            print(nlist)
        else:
            print("not found")
    elif menu == 4:
        old_name = input("변경하고자 하는 데이터 입력:")
        if old_name in nlist:
            new_name = input("새로운 데이터 입력")
            index = nlist.index(old_name)
            nlist[index] = new_name
            print(nlist)
        else:
            print("not found")

print("프로그램 종료")