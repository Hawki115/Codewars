#Rock Paper Scissors!
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    
    if p1 == "rock" and p2 =="scissors":
        return "Player 1 won!"
    
    if p1 == "paper" and p2 =="rock":
        return "Player 1 won!"
    if p1== "scissors" and p2 =="paper":
        return "Player 1 won!"
    

    else:
        return "Player 2 won!"