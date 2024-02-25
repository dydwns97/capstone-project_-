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

#  # 힌트

#  [이 웹사이트](https://games.washingtonpost.com/games/blackjack/)에서 블랙잭 게임을 해보세요.
# - 프로그램 요구사항에 대한 내용을 [이 페이지](http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF)에서 확인해보세요.
# - 만든 프로그램의 플로우차트를 [여기](https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt)에서 다운로드하세요.
# ; - 아래 힌트를 참고하여 프로그램을 완성하세요.


# ; 1. deal_card()` 함수를 생성하여 아래 리스트에서 무작위 카드를 *반환*하세요.
# ;    11은 에이스를 나타냅니다.
import random
from jack_art import logo

def deal_card():
    """카드를 받으세요."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
# ; 3. `calculate_score()` 함수를 생성하여 입력으로 받은 카드 리스트의 점수를 계산하세요.
# ; 이를 위해 `sum()` 함수를 사용하세요.
# ; 5. `calculate_score()` 함수 내에서 11(에이스)을 확인하세요. 이미 21을 넘은 경우 11을 제거하고 1로 바꿔야 할 수도 있습니다. 
# ; 이를 위해 `append()` 및 `remove()`를 사용할 수 있습니다.

def calculate_score(cards):
    """합을 계산합시다."""
    if sum(cards) == 21 and len(cards) == 2:
       return 0 #블랙잭이면 0으로 표시!
    
    elif 11 in cards and sum(cards) > 21:
       cards.remove(11)
       cards.append(1)
    
    return sum(cards)

# ; 10. `compare()` 함수를 생성하고 사용자 점수와 컴퓨터 점수를 전달하세요.
# ;  컴퓨터와 사용자가 동일한 점수를 가지고 있다면 비깁니다. 컴퓨터가 블랙잭(0)을 가지고 있다면 사용자가 집니다. 
# ; 사용자가 블랙잭(0)을 가지고 있다면 사용자가 이깁니다. 사용자 점수가 21을 초과하면 사용자가 집니다. 컴퓨터 점수가 21을 초과하면 컴퓨터가 집니다.
# ;  위의 경우에 해당하지 않으면 점수가 더 높은 플레이어가 이깁니다.

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

# ; 2. `deal_card()` 및 `append()`를 사용하여 사용자와 컴퓨터에게 각각 2장의 카드를 나눠주세요.
# ;    - `user_cards = []`
# ;    - `computer_cards = []`
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
    # clear()
  



# ; 6. `calculate_score()`를 호출하세요. 만약 컴퓨터 또는 사용자가 블랙잭(0)을 가지고 있거나 사용자의 점수가 21을 초과하면 게임을 종료하세요.

# ; 7. 게임이 종료되지 않은 경우, 사용자에게 추가 카드를 뽑을 것인지 물어보세요. 
# ; 사용자가 '예'를 선택한 경우 `deal_card()` 함수를 사용하여 `user_cards` 리스트에 추가 카드를 뽑으세요. '아니오'를 선택한 경우 게임이 종료됩니다.

# ; 8. 새로운 카드가 뽑힐 때마다 점수를 다시 확인하고 힌트 9에서의 체크를 게임이 종료될 때까지 반복하세요.

# ; 9. 사용자가 끝났으면, 컴퓨터가 플레이할 차례입니다. 컴퓨터는 점수가 17 미만인 한 계속해서 카드를 뽑아야 합니다.



# ; 11. 사용자에게 게임을 다시 시작할지 물어보세요. '예'라고 대답하면 콘솔을 지우고 새로운 블랙잭 게임을 시작하고 art.py에서 로고를 표시하세요.