
def topicOne(num):
    hol_list, zzak_list = [], []
    for idx in range(1, num+1):
        if idx % 2 != 0:
            hol_list.append(idx)
            print(f"{idx}은 홀수 입니다.")

        elif idx % 2 == 0:
            zzak_list.append(idx)
            print f"{idx}은 짝수 입니다."
        breakpoint()
    return hol_list, zzak_list
breakpoint()

topicOne(10)



# def add_num(insert_num , plus_num):
#     insert_num += plus_num
#     return insert_num

# default_number = 0  # 계산하기 전의 값으므로 0입니다.

# print(add_num(default_number, 3))  # 첫 번째 계산
# add_number = add_num(default_number, 3)  # 첫 번째 계산이 끝난 후의 값을 저장.
# print(add_num(add_number, 4))  # 두 번째 계산