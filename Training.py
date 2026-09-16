def player_stat(player,stat,amount):
    player[stat]=min(player[stat]+amount,100)

class Training_Engine:
    def __init__(self,training_type,mode,starting=None,gk_training_type=None):
        self.training=training_type
        self.mode=mode
        self.starting=starting
        self.gk_training=gk_training_type
        if isinstance(self.starting,dict):
            self.starting=[self.starting]
        self.first_fitness=self.first_average_fitness()
        self.first_sharpness=self.first_average_sharpness()
        self.first_moral=self.first_average_moral()
        self.check_training()

    def first_average_fitness(self):
        First_Sum_Fitness=0
        for player in self.starting:
            First_Sum_Fitness+=player['fitness']
        First_Average_Fitness=First_Sum_Fitness//len(self.starting)
        return First_Average_Fitness

    def first_average_sharpness(self):
        First_Sum_Sharpness=0
        for player in self.starting:
            First_Sum_Sharpness+=player['sharpness']
        First_Average_Sharpness=First_Sum_Sharpness//len(self.starting)
        return First_Average_Sharpness

    def first_average_moral(self):
        First_Sum_Moral=0
        for player in self.starting:
            First_Sum_Moral+=player['morale']
        First_Average_Moral=First_Sum_Moral//len(self.starting)
        return First_Average_Moral
    
    def check_training(self):
        for player in self.starting:
            if player['position']!='GK':
                if self.training=='physical':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'physical',1)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low.'
                    if self.mode=='medium':
                        if player['fitness']-6>=0:
                            player['fitness']-=6
                            player_stat(player,'physical',2)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'physical',3)
                            player_stat(player,'sharpness',4)
                if self.training=='passing':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'passing',1)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='medium':
                        if player['fitness']-6>=0:
                            player['fitness']-=6
                            player_stat(player,'passing',2)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'passing',3)
                            player_stat(player,'sharpness',4)
                if self.training=='shooting':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'shooting',1)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='medium':
                        if player['fitness']-6>=0:
                            player['fitness']-=6
                            player_stat(player,'shooting',2)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'                     
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'shooting',3)
                            player_stat(player,'sharpness',4)
                if self.training=='defending':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'defending',1)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='medium':
                        if player['fitness']-6>=0:
                            player['fitness']-=6
                            player_stat(player,'defending',2)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'defending',3)
                            player_stat(player,'sharpness',4)
                if self.training=='dribbling':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'dribbling',1)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='medium':
                            if player['fitness']-6>=0:
                                player['fitness']-=6
                                player_stat(player,'dribbling',2)
                                player_stat(player,'sharpness',3)
                            else:
                                return 'your fitness is very low.'                             
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'dribbling',3)
                            player_stat(player,'sharpness',4)
                if self.training=='pace':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'pace',1)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitnes is very low'
                    if self.mode=='medium':
                        if player['fitness']-6>=0:
                            player['fitness']-=6
                            player_stat(player,'pace',2)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'pace',3)
                            player_stat(player,'sharpness',4)
                if self.training=='attacking':
                    if self.mode=='easy':
                        if player['fitness']-4>=0:
                            player['fitness']-=4
                            player_stat(player,'shooting',0.5)
                            player_stat(player,'pace',0.5)
                            player_stat(player,'passing',0.5)
                            player_stat(player,'dribbling',0.5)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='medium':
                        if player['fitness']-8>=0:
                            player['fitness']-=8
                            player_stat(player,'shooting',1)
                            player_stat(player,'pace',1)
                            player_stat(player,'dribbling',1)
                            player_stat(player,'passing',1)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=12
                            player_stat(player,'shooting',2)
                            player_stat(player,'dribbling',2)
                            player_stat(player,'passing',2)
                            player_stat(player,'pace',2)
                            player_stat(player,'sharpness',4)
                if self.training=='defensive':
                    if self.mode=='easy':
                        if player['fitness']-4>=0:
                            player['fitness']-=4
                            player_stat(player,'defending',0.5)
                            player_stat(player,'physical',0.5)
                            player_stat(player,'pace',0.5)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low.'
                    if self.mode=='medium':
                        if player['fitness']-8>=0:
                            player['fitness']-=8
                            player_stat(player,'defending',1)
                            player_stat(player,'physical',1)
                            player_stat(player,'pace',1)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low.'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=12
                            player_stat(player,'defending',2)
                            player_stat(player,'physical',2)
                            player_stat(player,'pace',2)
                            player_stat(player,'sharpness',4)
                if self.training=='balance':
                    if self.mode=='easy':
                        if player['fitness']-4>=0:
                            player['fitness']-=4
                            player_stat(player,'shooting',0.3)
                            player_stat(player,'dribbling',0.3)
                            player_stat(player,'pace',0.3)
                            player_stat(player,'passing',0.3)
                            player_stat(player,'defending',0.3)
                            player_stat(player,'physical',0.3)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low.'
                    if self.mode=='medium':
                            if player['fitness']-8>=0:
                                player['fitness']-=8
                                player_stat(player,'shooting',0.5)
                                player_stat(player,'dribbling',0.5)
                                player_stat(player,'pace',0.5)
                                player_stat(player,'passing',0.5)
                                player_stat(player,'defending',0.5)
                                player_stat(player,'physical',0.5)
                                player_stat(player,'sharpness',3)
                            else:
                                return 'your fitness is very low.'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=12
                            player_stat(player,'shooting',1)
                            player_stat(player,'dribbling',1)
                            player_stat(player,'pace',1)
                            player_stat(player,'passing',1)
                            player_stat(player,'defending',1)
                            player_stat(player,'physical',1)
                            player_stat(player,'sharpness',4)
            else:
                if self.training=='diving':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'diving',1)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low.'
                    if self.mode=='medium':
                        if player['fitness']-6>=0:
                            player['fitness']-=6
                            player_stat(player,'diving',2)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'diving',3)
                            player_stat(player,'sharpness',4)
                if self.training=='handling':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'handling',1)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low.'
                    if self.mode=='medium':
                        if player['fitness']-6>=0:
                            player['fitness']-=6
                            player_stat(player,'handling',2)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'handling',3)
                            player_stat(player,'sharpness',4)
                if self.training=='kicking':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'kicking',1)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low.'
                    if self.mode=='medium':
                        if player['fitness']-6>=0:
                            player['fitness']-=6
                            player_stat(player,'kicking',2)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'kicking',3)
                            player_stat(player,'sharpness',4)
                if self.training=='reflexes':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'reflexes',1)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low.'
                    if self.mode=='medium':
                        if player['fitness']-6>=0:
                            player['fitness']-=6
                            player_stat(player,'reflexes',2)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'reflexes',3)
                            player_stat(player,'sharpness',4)
                if self.training=='speed':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'speed',1)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low.'
                    if self.mode=='medium':
                        if player['fitness']-6>=0:
                            player['fitness']-=6
                            player_stat(player,'speed',2)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'speed',3)
                            player_stat(player,'sharpness',4)
                if self.training=='positioning':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'positioning',1)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low.'
                    if self.mode=='medium':
                        if player['fitness']-6>=0:
                            player['fitness']-=6
                            player_stat(player,'positioning',2)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'positioning',3)
                            player_stat(player,'sharpness',4)
                if self.training=='sweeperkeeper':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'speed',0.5)
                            player_stat(player,'reflexes',0.5)
                            player_stat(player,'handling',0.5)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low.'
                    if self.mode=='medium':
                        if player['fitness']-6>=0:
                            player['fitness']-=6
                            player_stat(player,'speed',1)
                            player_stat(player,'reflexes',1)
                            player_stat(player,'handling',1)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'speed',2)
                            player_stat(player,'reflexes',2)
                            player_stat(player,'handling',2)
                            player_stat(player,'sharpness',4)
                if self.training=='goalkeeper':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'kicking',0.5)
                            player_stat(player,'diving',0.5)
                            player_stat(player,'positionning',0.5)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low.'
                    if self.mode=='medium':
                        if player['fitness']-6>=0:
                            player['fitness']-=6
                            player_stat(player,'kicking',1)
                            player_stat(player,'diving',1)
                            player_stat(player,'positioning',1)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'kicking',2)
                            player_stat(player,'diving',2)
                            player_stat(player,'positioning',2)
                            player_stat(player,'sharpness',4)
                if self.training=='balance':
                    if self.mode=='easy':
                        if player['fitness']-3>=0:
                            player['fitness']-=3
                            player_stat(player,'diving',0.3)
                            player_stat(player,'reflexes',0.3)
                            player_stat(player,'speed',0.3)
                            player_stat(player,'positioning',0.3)
                            player_stat(player,'kicking',0.3)
                            player_stat(player,'handling',0.3)
                            player_stat(player,'sharpness',2)
                        else:
                            return 'your fitness is very low.'
                    if self.mode=='medium':
                        if player['fitness']-6>=0:
                            player['fitness']-=6
                            player_stat(player,'diving',0.5)
                            player_stat(player,'reflexes',0.5)
                            player_stat(player,'speed',0.5)
                            player_stat(player,'positioning',0.5)
                            player_stat(player,'kicking',0.5)
                            player_stat(player,'handling',0.5)
                            player_stat(player,'sharpness',3)
                        else:
                            return 'your fitness is very low'
                    if self.mode=='hard':
                        if player['fitness']<20:
                            return 'Fitness is too low for Hard Training.'
                        else:
                            player['fitness']-=9
                            player_stat(player,'diving',1)
                            player_stat(player,'reflexes',1)
                            player_stat(player,'speed',1)
                            player_stat(player,'positioning',1)
                            player_stat(player,'kicking',1)
                            player_stat(player,'handling',1)
                            player_stat(player,'sharpness',4)

    def average_fitness(self):
        Second_Sum_Fitness=0
        for player in self.starting:
            Second_Sum_Fitness+=player['fitness']
        Average_Fitness=Second_Sum_Fitness//len(self.starting)
        return Average_Fitness
    
    def defrencce_fitness(self):
        return self.average_fitness()-self.first_fitness

    def average_sharpness(self):
        Sum_Sharpness=0
        for player in self.starting:
            Sum_Sharpness+=player['sharpness']
        Average_Sharpness=Sum_Sharpness//len(self.starting)
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
        Average_Moral=Sum_Moral//len(self.starting)
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
                return f'{train_type.capitalize()}: +1\n\nFitness: -3\n\nSharpness: +2\n\nMoral: +0'
            if train_mode=='medium':
                return f'{train_type.capitalize()}: +2\n\nFitness: -6\n\nSharpness: +3\n\nMoral: +0'
            else:
                return f'{train_type.capitalize()}: +3\n\nFitness: -9\n\nSharpness: +4\n\nMoral: +0'