# rl-6-nimmt (reinforcementlearning-6-nimmt)

Tring to build an agent that plays the card game "6 nimmt" better than random players or players with some simple decision logic.

### Todos

- [X] Implement 6 nimmt
- [X] Implement random players
- [ ] Implement reinforcement learning agent

### Current tournament results with win rates 

```
player1 (RandomPlayer): 48206 / 100000 48.21%
player2 (RandomPlayer): 48511 / 100000 48.51%
draw: 3283 / 100000 3.28%

player1 (SmartPlayer1): 47925 / 100000 47.93%
player2 (SmartPlayer1): 48085 / 100000 48.09%
draw: 3990 / 100000 3.99%

player1 (RandomPlayer): 30129 / 100000 30.13%
player2 (SmartPlayer1): 66639 / 100000 66.64%
draw: 3232 / 100000 3.23%

player1 (SmartPlayer1): 41009 / 100000 41.01%
player2 (SmartPlayer2): 54794 / 100000 54.79%
draw: 4197 / 100000 4.20%

player1 (RandomPlayer): 22566 / 100000 22.57%
player2 (SmartPlayer2): 74396 / 100000 74.40%
draw: 3038 / 100000 3.04%

player1 (SmartPlayer2): 48043 / 100000 48.04%
player2 (SmartPlayer2): 47845 / 100000 47.84%
draw: 4112 / 100000 4.11%

player1 (RandomPlayer): 31545 / 100000 31.55%
player2 (RandomPlayer): 31619 / 100000 31.62%
player3 (RandomPlayer): 31747 / 100000 31.75%
draw: 5089 / 100000 5.09%

player1 (RandomPlayer): 23770 / 100000 23.77%
player2 (RandomPlayer): 23981 / 100000 23.98%
player3 (SmartPlayer1): 47254 / 100000 47.25%
draw: 4995 / 100000 5.00%

player1 (RandomPlayer): 18480 / 100000 18.48%
player2 (SmartPlayer1): 38358 / 100000 38.36%
player3 (SmartPlayer1): 37861 / 100000 37.86%
draw: 5301 / 100000 5.30%

player1 (RandomPlayer): 18468 / 100000 18.47%
player2 (RandomPlayer): 18418 / 100000 18.42%
player3 (SmartPlayer2): 58395 / 100000 58.39%
draw: 4719 / 100000 4.72%

player1 (RandomPlayer): 14575 / 100000 14.57%
player2 (SmartPlayer1): 32368 / 100000 32.37%
player3 (SmartPlayer2): 47981 / 100000 47.98%
draw: 5076 / 100000 5.08%

player1 (SmartPlayer1): 31479 / 100000 31.48%
player2 (SmartPlayer1): 31489 / 100000 31.49%
player3 (SmartPlayer1): 31463 / 100000 31.46%
draw: 5569 / 100000 5.57%

player1 (SmartPlayer1): 26887 / 100000 26.89%
player2 (SmartPlayer1): 27217 / 100000 27.22%
player3 (SmartPlayer2): 40465 / 100000 40.47%
draw: 5431 / 100000 5.43%

player1 (RandomPlayer): 9260 / 100000 9.26%
player2 (SmartPlayer2): 42891 / 100000 42.89%
player3 (SmartPlayer2): 42780 / 100000 42.78%
draw: 5069 / 100000 5.07%

player1 (SmartPlayer1): 20329 / 100000 20.33%
player2 (SmartPlayer2): 37160 / 100000 37.16%
player3 (SmartPlayer2): 37091 / 100000 37.09%
draw: 5420 / 100000 5.42%

player1 (SmartPlayer2): 31590 / 100000 31.59%
player2 (SmartPlayer2): 31404 / 100000 31.40%
player3 (SmartPlayer2): 31357 / 100000 31.36%
draw: 5649 / 100000 5.65%
```
