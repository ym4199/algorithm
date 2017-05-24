class mac:
    """macdonald"""

    def __init__(self,name,money):
        self.name = name
        self.money = money

    def mac_menu(self):
        while(True):
            choice = input('메뉴를 골라주세요. 1.상하이버거 2.빅맥 3.1955 0.그만둔다\n:')
            if choice == '1':
                # print('가격은 8000원 입니다.')
                self.mac_menu_set('상하이버거')
            elif choice == '2':
                #print('가격은 6000원 입니다.')
                self.mac_menu_set('빅맥')
            elif choice == '3':
                #print('가격은 7000원 입니다.')
                self.man_menu_set('1955')
            elif choice == '0':
                print('안녕히가세요.')
                break
            else:
                print('정해지면 말씀해주세요.')


    def mac_menu_set(self,buger):
        print('{}을 선택하셨습니다.'.format(buger))
        while(True):
            choice = input('메뉴 구성을 선택해 주세요.\n  1. single 2. set 0.No \n:')
            if choice == '1':
                print('{} single 고르셨습니다.'.format(buger))
                break
            elif choice =='2':
                print('{} set 고르셨습니다.'.format(buger))
                self.desert_menu()
            elif choice =='0':
                break
            else:
                print('다시 선택해주세요.')

    def desert_menu(self):
        while(True):
            choice = input('디저트를 골라주세요\n 1.ice_cream 2.pie 0.No\n:')
            if choice == '1':
                print('잠시만 기다려주세요')
                break
            elif choice == '2':
                print('잠시만 기다려주세요')
                break
            elif choice == '0':
                break
            else:
                pass

