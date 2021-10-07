import collections
from random import choice

# 声明一张牌，rank=卡片大小  suit=卡片花色
Card = collections.namedtuple('Card', ['rank', 'suit'])


# 声明一副扑克牌，不包含 大小王， 公52张牌
class Poker:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # ranks = 2-10 JQKA
    suits = 'spades diamonds clubs hearts'.split()  # suits = 黑桃 方块 梅花 红桃

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


poker = Poker()
print(" ---- ---- ----")
print("Poker number = ", len(poker))
print("Random Choice on the Poker: ", choice(poker))
print("Random Choice on the Poker: ", choice(poker))
print("Random Choice on the Poker: ", choice(poker))

print(" ---- ---- ----")

print("Get all the A: ")
print(poker[12::13])

print(" ---- ---- ----")

print("Card('Q', 'hearts') in poker = ", Card('Q', 'hearts') in poker)

print(" ---- ---- ----")

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
card = poker[10]
print("card = ", card)
print("card.rank = ", card.rank)
print("Poker.ranks.index(card.rank)", Poker.ranks.index(card.rank))
print("len(suit_values) = ", len(suit_values))


def spades_high(card):
    rank_value = Poker.ranks.index(card.rank)
    print("rank_value = ", rank_value, "spades_high = ", rank_value * len(suit_values) + suit_values[card.suit])

    return rank_value * len(suit_values) + suit_values[card.suit]


print(" ---- ---- ----")

for card in sorted(poker, key=spades_high):
    print(card)
# Output
# Card(rank='2', suit='clubs')
# Card(rank='2', suit='diamonds')
# Card(rank='2', suit='hearts')
# ... (46 cards omitted)
# Card(rank='A', suit='diamonds')
# Card(rank='A', suit='hearts')
# Card(rank='A', suit='spades')
