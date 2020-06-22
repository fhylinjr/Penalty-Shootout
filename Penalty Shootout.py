import random
class Pshootout:
    def __init__(self):
        diffmode=eval(input('Select difficulty mode for Penalty Shootout Game\nEnter 1 for easy mode and 2 for hard mode: '))
        self.diffmode=diffmode
        scored=0
        self.scored=scored
        saved=0
        self.saved=saved
        
    def getIntro(self):
        projectfile=open('Intro.txt','r')
        for i in range(4):
            line=projectfile.readline()
            print(line)
        projectfile.close()
        return 'Good luck!'
    
    def getResult(self):
        if self.scored>self.saved:
            return 'You won the shootout. Congrats!'
        elif self.scored<self.saved:
            return 'You lost the shootout. Better luck next time'

    def getShootout(self,shot):
        resultfile=open('projectresult.txt','w')
        for n in range(5):
            playerOption=['TL','ML','BL','TM','M','BM','TR','MR','BR']
            goalie=random.choices(playerOption,k=6)
            if self.diffmode==1:
                shot=input('\nSelect where you would like to shoot (TL, ML, BL, TM, M, BM, TR, MR or BR): ')
                if playerOption.count(shot)==0:
                    print('You entered wrong key. You shot wide away from goal.')
                    self.saved+=1
                elif playerOption.count(shot)!=0:
                    if goalie[0]==shot or goalie[1]==shot or goalie[2]==shot:
                        print('Goalie stopped your shot. Too Bad')
                        self.saved+=1
                    elif goalie[0]!=shot and goalie[1]!=shot and goalie[2]!=shot:
                        print('You scored! Nice Try!')
                        self.scored+=1
                print('Your score is: ',self.scored,'-',self.saved)

            elif self.diffmode==2:
                shot=input('\nSelect where you would like to shoot (TL, ML, BL, TM, M, BM, TR, MR or BR): ')
                if playerOption.count(shot)==0:
                    print('You entered wrong key. You shot wide away from goal.')
                    self.saved+=1
                elif playerOption.count(shot)!=0:
                    if goalie[0]==shot or goalie[1]==shot or goalie[2]==shot or goalie[3]==shot or goalie[4]==shot or goalie[5]==shot:
                        print('Goalie stopped your shot. Too Bad')
                        self.saved+=1
                    elif goalie[0]!=shot and goalie[1]!=shot and goalie[2]!=shot and goalie[3]!=shot and goalie[4]!=shot and goalie[5]!=shot:
                        print('You scored! Nice Try!')
                        self.scored+=1
                print('Your score is: ',self.scored,'-',self.saved)
        print('At the end of the shootout, the score was: ',self.scored,'-',self.saved,file=resultfile)
        resultfile.close()
        return '\nGame has ended successfully.'

penalties=Pshootout()
print(penalties.getIntro())
print(penalties.getShootout('shot'))
print(penalties.getResult())


            


    
    
          
