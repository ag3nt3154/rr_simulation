import numpy as np
import matplotlib.pyplot as plt

class rrbot:

    def __init__(self):
        self.mag = None
        pass
    

    def game_start(self, p1, p2, shuffle=False, start_player=1, print1=False):

        # Generate magazine
        
        self.mag = [p1.mag, p2.mag]
        if print1: print(self.mag)

        # Poison bullets left tracker
        p1_poison_left = self.mag[0].count(1)
        p2_poison_left = self.mag[1].count(1)

        # Determine which player starts first
        if start_player == 1:

            # Bullet counter
            for i in range(len(self.mag[0])):

                if print1: print('---------------------------------')
                if print1: print(f'bullet {i}')

                # Pass multiplier
                pass_mult = 1
                # Bullet points
                if self.mag[0][i] + self.mag[1][i] > 0:
                    bullet_point = -1
                else:
                    bullet_point = 1

                # Player 1 plays
                if i % 2 == 0:

                    # Player 1 decision
                    play = p1.play(i, p1_poison_left, p2_poison_left, pass_mult)
                    if play == 'shoot':
                        if print1: print('player 1 shoots')
                        p1.points += bullet_point * pass_mult
                        p1_poison_left -= self.mag[0][i]
                        p2_poison_left -= self.mag[1][i]
                        if print1: print(f'bullets: {self.mag[0][i]}, {self.mag[1][i]}')
                        if print1: print(f'p1: {p1.points}, p2: {p2.points}')
                    else:
                        if print1: print('player 1 passes')
                        pass_mult *= 2
                        play = p2.play(i, p2_poison_left, p1_poison_left, pass_mult)
                        if play == 'shoot':
                            if print1: print('player 2 shoots')
                            p2.points += bullet_point * pass_mult
                            p1_poison_left -= self.mag[0][i]
                            p2_poison_left -= self.mag[1][i]
                            if print1: print(f'bullets: {self.mag[0][i]}, {self.mag[1][i]}')
                            if print1: print(f'p1: {p1.points}, p2: {p2.points}')
                        else:
                            if print1: print('player 2 passes')
                            if print1: print('player 1 shoots')
                            pass_mult *= 2
                            p1.points += bullet_point * pass_mult
                            p1_poison_left -= self.mag[0][i]
                            p2_poison_left -= self.mag[1][i]
                            if print1: print(f'bullets: {self.mag[0][i]}, {self.mag[1][i]}')
                            if print1: print(f'p1: {p1.points}, p2: {p2.points}')
                
                # Player 2 plays
                else:

                    # Player 2 decision
                    play = p2.play(i, p2_poison_left, p1_poison_left, pass_mult)
                    if play == 'shoot':
                        if print1: print('player 2 shoots')
                        p2.points += bullet_point * pass_mult
                        p1_poison_left -= self.mag[0][i]
                        p2_poison_left -= self.mag[1][i]
                        if print1: print(f'bullets: {self.mag[0][i]}, {self.mag[1][i]}')
                        if print1: print(f'p1: {p1.points}, p2: {p2.points}')
                    else:
                        if print1: print('player 2 passes')
                        pass_mult *= 2
                        play = p1.play(i, p1_poison_left, p2_poison_left, pass_mult)
                        if play == 'shoot':
                            if print1: print('player 1 shoots')
                            p1.points += bullet_point * pass_mult
                            p1_poison_left -= self.mag[0][i]
                            p2_poison_left -= self.mag[1][i]
                            if print1: print(f'bullets: {self.mag[0][i]}, {self.mag[1][i]}')
                            if print1: print(f'p1: {p1.points}, p2: {p2.points}')
                        else:
                            if print1: print('player 1 passes')
                            if print1: print('player 2 shoots')
                            pass_mult *= 2
                            p2.points += bullet_point * pass_mult
                            p1_poison_left -= self.mag[0][i]
                            p2_poison_left -= self.mag[1][i]
                            if print1: print(f'bullets: {self.mag[0][i]}, {self.mag[1][i]}')
                            if print1: print(f'p1: {p1.points}, p2: {p2.points}')
        else:
            # Bullet counter
            for i in range(len(self.mag[0])):

                if print1: print('---------------------------------')
                if print1: print(f'bullet {i}')

                # Pass multiplier
                pass_mult = 1
                # Bullet points
                if self.mag[0][i] + self.mag[1][i] > 0:
                    bullet_point = -1
                else:
                    bullet_point = 1

                # Player 2 plays
                if i % 2 == 0:
                    # Player 2 decision
                    play = p2.play(i, p2_poison_left, p1_poison_left, pass_mult)
                    if play == 'shoot':
                        if print1: print('player 2 shoots')
                        p2.points += bullet_point * pass_mult
                        p1_poison_left -= self.mag[0][i]
                        p2_poison_left -= self.mag[1][i]
                        if print1: print(f'bullets: {self.mag[0][i]}, {self.mag[1][i]}')
                        if print1: print(f'p1: {p1.points}, p2: {p2.points}')
                    else:
                        if print1: print('player 2 passes')
                        pass_mult *= 2
                        play = p1.play(i, p1_poison_left, p2_poison_left, pass_mult)
                        if play == 'shoot':
                            if print1: print('player 1 shoots')
                            p1.points += bullet_point * pass_mult
                            p1_poison_left -= self.mag[0][i]
                            p2_poison_left -= self.mag[1][i]
                            if print1: print(f'bullets: {self.mag[0][i]}, {self.mag[1][i]}')
                            if print1: print(f'p1: {p1.points}, p2: {p2.points}')
                        else:
                            if print1: print('player 1 passes')
                            if print1: print('player 2 shoots')
                            pass_mult *= 2
                            p2.points += bullet_point * pass_mult
                            p1_poison_left -= self.mag[0][i]
                            p2_poison_left -= self.mag[1][i]
                            if print1: print(f'bullets: {self.mag[0][i]}, {self.mag[1][i]}')
                            if print1: print(f'p1: {p1.points}, p2: {p2.points}')
                    
                # Player 1 plays
                else:
                    # Player 1 decision
                    play = p1.play(i, p1_poison_left, p2_poison_left, pass_mult)
                    if play == 'shoot':
                        if print1: print('player 1 shoots')
                        p1.points += bullet_point * pass_mult
                        p1_poison_left -= self.mag[0][i]
                        p2_poison_left -= self.mag[1][i]
                        if print1: print(f'bullets: {self.mag[0][i]}, {self.mag[1][i]}')
                        if print1: print(f'p1: {p1.points}, p2: {p2.points}')
                    else:
                        if print1: print('player 1 passes')
                        pass_mult *= 2
                        play = p2.play(i, p2_poison_left, p1_poison_left, pass_mult)
                        if play == 'shoot':
                            if print1: print('player 2 shoots')
                            p2.points += bullet_point * pass_mult
                            p1_poison_left -= self.mag[0][i]
                            p2_poison_left -= self.mag[1][i]
                            if print1: print(f'bullets: {self.mag[0][i]}, {self.mag[1][i]}')
                            if print1: print(f'p1: {p1.points}, p2: {p2.points}')
                        else:
                            if print1: print('player 2 passes')
                            if print1: print('player 1 shoots')
                            pass_mult *= 2
                            p1.points += bullet_point * pass_mult
                            p1_poison_left -= self.mag[0][i]
                            p2_poison_left -= self.mag[1][i]
                            if print1: print(f'bullets: {self.mag[0][i]}, {self.mag[1][i]}')
                            if print1: print(f'p1: {p1.points}, p2: {p2.points}')

                    

    
        if print1: print(f'player 1 points:{p1.points}')
        if print1: print(f'player 2 points:{p2.points}')
        if print1: print('******************************************')
        return p1.points, p2.points


                        

class player:

    def __init__(self, mag_size=8, poison_bullets=3, pass_prob=0, strat=0):
        self.points = 0
        # Generate magazine distribution
        self.mag = [1, 1, 1, 0, 0, 0, 0, 0]
        np.random.shuffle(self.mag)
        self.pass_prob = pass_prob
        self.strat = strat


    def play(self, bullet, self_poison_left, other_poison_left, pass_mult):
        other_poison_prob = other_poison_left / (len(self.mag) - bullet)
        self_poison_prob = self_poison_left / (len(self.mag) - bullet)
        
        if self.strat == 0:
            if pass_mult == 2 and other_poison_left > 0:
                return 'pass'
            else:
                return 'shoot'
        elif self.strat == 1:

            if pass_mult == 2:
                return 'pass'
            elif self.mag[bullet] == 1:
                return 'shoot'
            else:
                if self.pass_prob > other_poison_prob:
                    return 'pass'
                else:
                    return 'shoot'

x = np.arange(100) / 100

y = []

for i in range(len(x)):
    y_ = []
    for j in range(100000):
        bot = rrbot()
        p1 = player(pass_prob=x[i], strat=1)
        p2 = player()
        p1_score, p2_score = bot.game_start(p1, p2)
        if p1_score > p2_score:
            y_.append(1)
        elif p1_score < p2_score:
            y_.append(-1)
        else:
            y_.append(0)
    y.append(np.sum(y_))

y = np.array(y)

plt.plot(x, y)
plt.show()

    
    


    



