#  블랙잭 프로젝트

#  블랙잭 하우스 룰

# 덱의 크기는 무제한입니다.
# 조커는 없습니다.
# 잭/퀸/킹은 모두 10으로 계산됩니다.
# 에이스는 11 또는 1로 계산할 수 있습니다.
# 다음 리스트를 카드 덱으로 사용합니다:
# ```
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# ```
# 리스트 안의 카드는 무작위로 뽑힐 확률이 동일합니다.
# 카드가 뽑힌 후에도 덱에서 카드는 제거되지 않습니다.
# 컴퓨터는 딜러입니다.
##==============================================================================

import random
from jack_art import logo

def deal_card():
    """카드를 받으세요."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """합을 계산합시다."""
    if sum(cards) == 21 and len(cards) == 2:
       return 0 #블랙잭이면 0으로 표시!
    
    elif 11 in cards and sum(cards) > 21:
       cards.remove(11)
       cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
  """사용자와 컴퓨터와 비교!"""
  if user_score == computer_score:
    return "무승부입니다."
  elif user_score == 0:
    return "블랙잭!! 축하합니다 당신이 이겼어요!!."
  elif computer_score == 0:
    return "블랙잭! 컴퓨터가 이겼습니다.ㅠ"
  elif user_score > 21:
    return "당신의 점수가 21점이 넘었어요 당신이 패배했습니다.ㅜ"
  elif computer_score > 21:
    return "컴퓨터의 점수가 21점이 넘었어요 당신이 이겼습니다!!."
  elif user_score > computer_score:
    return "축하합니다 당신이 이겼습니다!!"
  else:
    return "컴퓨터가 이겼습니다. 당신은 패배했어요.ㅜ"

#"""게임시작"""
print("블랙잭 게임에 오신걸 환영합니다!!!!!")

def game_start():

    print(logo)
    

    user_cards = []
    computer_cards = []
    user_score = 0 # 점수도 초기화!!
    computer_score = 0
    end_of_game = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    #게임 스타트
    while not end_of_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f" 사용자 카드: {user_cards}, 현재 점수: {user_score}")
        print(f" 컴퓨터의 첫번째 카드: {computer_cards[0]}")

        
        if user_score == 0 or computer_score == 0 or user_score > 21:
                end_of_game = True
                print("수고하셨습니다!.")
        else:
                another_card = input("추가로 카드를 뽑을 것입니까? y / n : ").lower()
                if another_card == 'y':
                    
                    user_cards.append(deal_card())

                else:
                    end_of_game = True
                    
                
    #컴퓨터차례
    while computer_score != 0 and computer_score < 17:
        
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" 최종 사용자 카드: {user_cards}, 최종점수: {user_score}")
    print(f" 최종 컴퓨터 카드: {computer_cards}, 최종점수: {computer_score}")
    print(compare(user_score, computer_score))

while True:
  start = input("블랙잭 게임을 시작하시겠습니까? y / n: ")
  if start != 'y':
    print("수고하셨습니다. 게임을 종료하겠습니다.")
    break
    
  else:
    game_start()
    
  
