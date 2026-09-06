class Training_Engine:
    def __init__(self,training,mode,starting):
        self.training=training
        self.mode=mode
        self.starting=starting
        self.first_fitness=self.first_average_fitness()
        self.first_sharpness=self.first_average_sharpness()
        self.first_moral=self.first_average_moral()
        if isinstance(self.starting,dict):
            self.starting=[self.starting]
        else:
            self.check_training()

    def first_average_fitness(self):
        First_Sum_Fitness=0
        for player in self.starting:
            First_Sum_Fitness+=player['fitness']
        First_Average_Fitness=First_Sum_Fitness//11
        return First_Average_Fitness

    def first_average_sharpness(self):
        First_Sum_Sharpness=0
        for player in self.starting:
            First_Sum_Sharpness+=player['sharpness']
        First_Average_Sharpness=First_Sum_Sharpness//11
        return First_Average_Sharpness

    def first_average_moral(self):
        First_Sum_Moral=0
        for player in self.starting:
            First_Sum_Moral+=player['morale']
        First_Average_Moral=First_Sum_Moral//11
        return First_Average_Moral
    
    def check_training(self):
        for player in self.starting:
            if self.training=='physical':
                if self.mode=='easy':
                    if player['position']!='GK':
                        if player['physical']+1<=100:
                            if player['fitness']-3>=0:
                                if player['sharpness']+2<=100:
                                    player['physical']+=1
                                    player['fitness']-=3
                                    player['sharpness']+=2
                if self.mode=='medium':
                    if player['position']!='GK':
                        if player['physical']+2<=100:
                            if player['fitness']-6>=0:
                                if player['sharpness']+3<=100:
                                    player['physical']+=2
                                    player['fitness']-=6
                                    player['sharpness']+=3
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            if player['physical']+3<=100:
                                if player['sharpness']+4<=100:
                                    player['physical']+=3
                                    player['fitness']-=9
                                    player['sharpness']+=4
            if self.training=='passing':
                if self.mode=='easy':
                    if player['position']!='GK':
                        if player['passing']+1<=100:
                            if player['fitness']-3>=0:
                                if player['sharpness']+2<=100:
                                    player['passing']+=1
                                    player['fitness']-=3
                                    player['sharpness']+=2
                if self.mode=='medium':
                    if player['position']!='GK':
                        if player['passing']+2<=100:
                            if player['fitness']-6>=0:
                                if player['sharpness']+3<=100:
                                    player['passing']+=2
                                    player['fitness']-=6
                                    player['sharpness']+=3
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            if player['passing']+3<=100:
                                if player['sharpness']+4<=100:
                                    player['passing']+=3
                                    player['fitness']-=9
                                    player['sharpness']+=4
            if self.training=='shooting':
                if self.mode=='easy':
                    if player['position']!='GK':
                        if player['shooting']+1<=100:
                            if player['fitness']-3>=0:
                                if player['sharpness']+2<=100:
                                    player['shooting']+=1
                                    player['fitness']-=3
                                    player['sharpness']+=2
                if self.mode=='medium':
                    if player['position']!='GK':
                        if player['shooting']+2<=100:
                            if player['fitness']-6>=0:
                                if player['sharpness']+3<=100:
                                    player['shooting']+=2
                                    player['fitness']-=6
                                    player['sharpness']+=3
                if self.mode=='hard':
                    if player['fitness']>20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            if player['shooting']+3<=100:
                                if player['sharpness']+4<=100:
                                    player['shooting']+=3
                                    player['fitness']-=9
                                    player['sharpness']+=4
            if self.training=='defending':
                if self.mode=='easy':
                    if player['position']!='GK':
                        if player['defending']+1<=100:
                            if player['fitness']-3>=0:
                                if player['sharpness']+2<=100:
                                    player['defending']+=1
                                    player['fitness']-=3
                                    player['sharpness']+=2
                if self.mode=='medium':
                    if player['position']!='GK':
                        if player['defending']+2<=100:
                            if player['fitness']-6>=0:
                                if player['sharpness']+3<=100:
                                    player['defending']+=2
                                    player['fitness']-=6
                                    player['sharpness']+=3
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            if player['defending']+3<=100:
                                if player['sharpness']+4<=100:
                                    player['defending']+=3
                                    player['fitness']-=9
                                    player['sharpness']+=4
            if self.training=='dribbling':
                if self.mode=='easy':
                    if player['position']!='GK':
                        if player['dribbling']+1<=100:
                            if player['fitness']-3>=0:
                                if player['sharpness']+2<=100:
                                    player['dribbling']+=1
                                    player['fitness']-=3
                                    player['sharpness']+=2
                if self.mode=='medium':
                    if player['position']!='GK':
                        if player['dribbling']+2<=100:
                            if player['fitness']-6>=0:
                                if player['sharpness']+3<=100:
                                    player['dribbling']+=2
                                    player['fitness']-=6
                                    player['sharpness']+=3
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            if player['dribbling']+3<=100:
                                if player['sharpness']+4<=100:
                                    player['dribbling']+=3
                                    player['fitness']-=9
                                    player['sharpness']+=4
            if self.training=='pace':
                if self.mode=='easy':
                    if player['position']!='GK':
                        if player['pace']+1<=100:
                            if player['fitness']-3>=0:
                                if player['sharpness']+2<=100:
                                    player['pace']+=1
                                    player['fitness']-=3
                                    player['sharpness']+=2
                if self.mode=='medium':
                    if player['position']!='GK':
                        if player['pace']+2<=100:
                            if player['fitness']-6>=0:
                                if player['sharpness']+3<=100:
                                    player['pace']+=2
                                    player['fitness']-=6
                                    player['sharpness']+=3
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            if player['pace']+3<=100:
                                if player['sharpness']+4<=100:
                                    player['pace']+=3
                                    player['fitness']-=9
                                    player['sharpness']+=4
            if self.training=='attacking':
                if self.mode=='easy':
                    if player['position']!='GK':
                        if player['shooting']+0.5<=100 and player['dribbling']+0.5<=100 and player['passing']+0.5<=100 and player['pace']+0.5<=100:
                            if player['fitness']-4>=0:
                                if player['sharpness']+2<=100:
                                    player['shooting']+=0.5
                                    player['dribbling']+=0.5
                                    player['passing']+=0.5
                                    player['pace']+=0.5
                                    player['fitness']-=4
                                    player['sharpness']+=2
                if self.mode=='medium':
                    if player['position']!='GK':
                        if player['shooting']+1<=100 and player['dribbling']+1<=100 and player['passing']+1<=100 and player['pace']+1<=100:
                            if player['fitness']-8>=0:
                                if player['sharpness']+3<=100:
                                    player['shooting']+=1
                                    player['dribbling']+=1
                                    player['passing']+=1
                                    player['pace']+=1
                                    player['fitness']-=8
                                    player['sharpness']+=3
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            if player['shooting']+2<=100 and player['dribbling']+2<=100 and player['passing']+2<=100 and player['pace']+2<=100:
                                if player['sharpness']+4<=100:
                                    player['shooting']+=2
                                    player['dribbling']+=2
                                    player['passing']+=2
                                    player['pace']+=2
                                    player['fitness']-=12
                                    player['sharpness']+=4
            if self.training=='defensive':
                if self.mode=='easy':
                    if player['position']!='GK':
                        if player['defending']+0.5<=100 and player['physical']+0.5<=100 and player['pace']+0.5<=100:
                            if player['fitness']-4>=0:
                                if player['sharpness']+2<=100:
                                    player['physical']+=0.5
                                    player['defending']+=0.5
                                    player['pace']+=0.5
                                    player['fitness']-=4
                                    player['sharpness']+=2
                if self.mode=='medium':
                    if player['position']!='GK':
                        if player['defending']+1<=100 and player['physical']+1<=100 and player['pace']+1<=100:
                            if player['fitness']-8>=0:
                                if player['sharpness']+3<=100:
                                    player['physical']+=1
                                    player['defending']+=1
                                    player['pace']+=1
                                    player['fitness']-=8
                                    player['sharpness']+=3                
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            if player['defending']+2<=100 and player['physical']+2<=100 and player['pace']+2<=100:
                                if player['sharpness']+4<=100:
                                    player['physical']+=2
                                    player['defending']+=2
                                    player['pace']+=2
                                    player['fitness']-=12
                                    player['sharpness']+=4            
            if self.training=='balance':
                if self.mode=='easy':
                    if player['position']!='GK':
                        if player['shooting']+0.3<=100 and player['dribbling']+0.3<=100 and player['passing']+0.3<=100 and player['defending']+0.3<=100 and player['physical']+0.3<=100 and player['pace']+0.3<=100:
                            if player['fitness']-4>=0:
                                if player['sharpness']+2<=100:
                                    player['shooting']+=0.3
                                    player['dribbling']+=0.3
                                    player['passing']+=0.3
                                    player['pace']+=0.3
                                    player['physical']+=0.3
                                    player['defending']+=0.3
                                    player['fitness']-=4
                                    player['sharpness']+=2                   
                    if player['position']=='GK':
                        if player['diving']+0.3<=100 and player['handling']+0.3<=100 and player['kicking']+0.3<=100 and player['reflexes']+0.3<=100 and player['speed']+0.3<=100 and player['positioning']+0.3<=100:
                            if player['fitness']-4>=0:
                                if player['sharpness']+2<=100:
                                    player['diving']+=0.3
                                    player['handling']+=0.3
                                    player['kicking']+=0.3
                                    player['reflexes']+=0.3
                                    player['speed']+=0.3
                                    player['positioning']+=0.3
                                    player['fitness']-=4
                                    player['sharpness']+=2
                if self.mode=='medium':
                    if player['position']!='GK':
                        if player['shooting']+0.5<=100 and player['dribbling']+0.5<=100 and player['passing']+0.5<=100 and player['defending']+0.5<=100 and player['physical']+0.5<=100 and player['pace']+0.5<=100:
                            if player['fitness']-8>=0:
                                if player['sharpness']+3<=100:
                                    player['shooting']+=0.5
                                    player['dribbling']+=0.5
                                    player['passing']+=0.5
                                    player['pace']+=0.5
                                    player['physical']+=0.5
                                    player['defending']+=0.5
                                    player['fitness']-=8
                                    player['sharpness']+=3
                    if player['position']=='GK':
                        if player['diving']+0.5<=100 and player['handling']+0.5<=100 and player['kicking']+0.5<=100 and player['reflexes']+0.5<=100 and player['speed']+0.5<=100 and player['positioning']+0.5<=100:
                            if player['fitness']-8>=0:
                                if player['sharpness']+3<=100:
                                    player['diving']+=0.5
                                    player['handling']+=0.5
                                    player['kicking']+=0.5
                                    player['reflexes']+=0.5
                                    player['speed']+=0.5
                                    player['positioning']+=0.5
                                    player['fitness']-=8
                                    player['sharpness']+=3
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            if player['shooting']+1<=100 and player['dribbling']+1<=100 and player['passing']+1<=100 and player['defending']+1<=100 and player['physical']+1<=100 and player['pace']+1<=100:
                                if player['fitness']-12>=0:
                                    if player['sharpness']+4<=100:
                                        player['shooting']+=1
                                        player['dribbling']+=1
                                        player['passing']+=1
                                        player['pace']+=1
                                        player['physical']+=1
                                        player['defending']+=1
                                        player['fitness']-=12
                                        player['sharpness']+=4
                        if player['position']=='GK':
                            if player['diving']+1<=100 and player['handling']+1<=100 and player['kicking']+1<=100 and player['reflexes']+1<=100 and player['speed']+1<=100 and player['positioning']+1<=100:
                                if player['fitness']-12>=0:
                                    if player['sharpness']+34<=100:
                                        player['diving']+=1
                                        player['handling']+=1
                                        player['kicking']+=1
                                        player['reflexes']+=1
                                        player['speed']+=1
                                        player['positioning']+=1
                                        player['fitness']-=12
                                        player['sharpness']+=4

    def average_fitness(self):
        Second_Sum_Fitness=0
        for player in self.starting:
            Second_Sum_Fitness+=player['fitness']
        Average_Fitness=Second_Sum_Fitness//11
        return Average_Fitness
    
    def defrencce_fitness(self):
        return self.average_fitness()-self.first_fitness

    def average_sharpness(self):
        Sum_Sharpness=0
        for player in self.starting:
            Sum_Sharpness+=player['sharpness']
        Average_Sharpness=Sum_Sharpness//11
        return Average_Sharpness

    def defrenccd_sharpness(self):
        if self.average_sharpness()-self.first_sharpness>=0:
            return f'+ {self.average_sharpness()-self.first_sharpness}'
        else:
            return self.average_sharpness()-self.first_sharpness

    def average_moral(self):
        Sum_Moral=0
        for player in self.starting:
            Sum_Moral+=player['morale']
        Average_Moral=Sum_Moral//11
        return Average_Moral

    def defrencce_moral(self):
        if self.average_moral()-self.first_moral==0:
            return '+0'

    def return_result(self,train_type,train_mode):
        if train_type=='attacking':
            if train_mode=='easy':
                return f'Shooting:  +0.5\n\nDribbling: +0.5\n\nPassing: +0.5\n\nPace: +0.5\n\nFitness: -4\n\nSharpness: +2\n\nMoral: +0'
            if train_mode=='medium':
                return f'Shooting:  +1\n\nDribbling: +1\n\nPassing: +1\n\nPace: +1\n\nFitness: -8\n\nSharpness: +3\n\nMoral: +0'
            else:
                return f'Shooting:  +2\n\nDribbling: +2\n\nPassing: +2\n\nPace: +2\n\nFitness: -12\n\nSharpness: +4\n\nMoral: +0'
        if train_type=='defensive':
            if train_mode=='easy':
                return f'Defending:  +0.5\nP\nhysical: +0.5\n\nPace: +0.5\n\nFitness: -4\n\nSharpness: +2\n\nMoral: +0'
            if train_mode=='medium':
                return f'Defending:  +1\n\nPhysical: +1\n\nPace: +1\n\nFitness: -8\n\nSharpness: +3\n\nMoral: +0'
            else:
                return f'Defending:  +2\n\nPhysical: +2\n\nPace: +2\n\nFitness: -12\n\nSharpness: +4\n\nMoral: +0'
        if train_type=='balance':
            if train_mode=='easy':
                return f'Shooting:  +0.3\n\nDribbling: +0.3\n\nPassing: +0.3\n\nDefending:  +0.3\n\nPhysical: +0.3\n\nPace: +0.3\n\nFitness: -4\n\nSharpness: +2\n\nMoral: +0'
            if train_mode=='medium':
                return f'Shooting:  +0.5\n\nDribbling: +0.5\n\nPassing: +0.5\n\nDefending:  +0.5\n\nPhysical: +0.5\n\nPace: +0.5\n\nFitness: -8\n\nSharpness: +3\n\nMoral: +0'
            else:
                return f'Shooting:  +1\n\nDribbling: +1\n\nPassing: +1\n\nDefending:  +1\n\nPhysical: +1\n\nPace: +1\n\nFitness: -12\n\nSharpness: +4\n\nMoral: +0'
        else:
            if train_mode=='easy':
                return f'{train_type.captilize()}: +1\n\nFitness: -3\n\nSharpness: +2\n\nMoral: +0'
            if train_mode=='medium':
                return f'{train_type.captilize()}: +2\n\nFitness: -6\n\nSharpness: +3\n\nMoral: +0'
            else:
                return f'{train_type.captilize()}: +3\n\nFitness: -9\n\nSharpness: +4\n\nMoral: +0'