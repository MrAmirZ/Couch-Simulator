class Training_Engine:
    def __init__(self,training,mode,starting):
        self.training=training
        self.mode=mode
        self.starting=starting
        if isinstance(self.starting,dict):
            self.starting=[self.starting]
        else:
            self.check_training()
    def check_training(self):
        for player in self.starting:
            if self.training=='physical':
                if self.mode=='easy':
                    if player['position']!='GK':
                        player['physical']+=1
                        player['fitness']-=3
                if self.mode=='medium':
                    if player['position']!='GK':
                        player['physical']+=2
                        player['fitness']-=6
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            player['physical']+=3
                            player['fitness']-=9
            if self.training=='passing':
                if self.mode=='easy':
                    if player['position']!='GK':
                        player['passing']+=1
                        player['fitness']-=3
                if self.mode=='medium':
                    if player['position']!='GK':
                        player['passing']+=2
                        player['fitness']-=6
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            player['passing']+=3
                            player['fitness']-=9
            if self.training=='shooting':
                if self.mode=='easy':
                    if player['position']!='GK':
                        player['shooting']+=1
                        player['fitness']-=3
                if self.mode=='medium':
                    if player['position']!='GK':
                        player['shooting']+=2
                        player['fitness']-=6
                if self.mode=='hard':
                    if player['fitness']>20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            player['shooting']+=3
                            player['fitness']-=9
            if self.training=='defending':
                if self.mode=='easy':
                    if player['position']!='GK':
                        player['defending']+=1
                        player['fitness']-=3
                if self.mode=='medium':
                    if player['position']!='GK':
                        player['defending']+=2
                        player['fitness']-=6
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            player['defending']+=3
                            player['fitness']-=9
            if self.training=='dribbling':
                if self.mode=='easy':
                    if player['position']!='GK':
                        player['dribbling']+=1
                        player['fitness']-=3
                if self.mode=='medium':
                    if player['position']!='GK':
                        player['dribbling']+=2
                        player['fitness']-=6
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            player['dribbling']+=3
                            player['fitness']-=9
            if self.training=='pace':
                if self.mode=='easy':
                    if player['position']!='GK':
                        player['pace']+=1
                        player['fitness']-=3
                if self.mode=='medium':
                    if player['position']!='GK':
                        player['pace']+=2
                        player['fitness']-=6
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            player['pace']+=3
                            player['fitness']-=9
            if self.training=='attacking':
                if self.mode=='easy':
                    if player['position']!='GK':
                        player['shooting']+=0.5
                        player['dribbling']+=0.5
                        player['passing']+=0.5
                        player['pace']+=0.5
                        player['fitness']-=4
                if self.mode=='medium':
                    if player['position']!='GK':
                        player['shooting']+=1
                        player['dribbling']+=1
                        player['passing']+=1
                        player['pace']+=1
                        player['fitness']-=8
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            player['shooting']+=2
                            player['dribbling']+=2
                            player['passing']+=2
                            player['pace']+=2
                            player['fitness']-=12
            if self.training=='defensive':
                if self.mode=='easy':
                    if player['position']!='GK':
                        player['physical']+=0.5
                        player['defending']+=0.5
                        player['pace']+=0.5
                        player['fitness']-=4
                if self.mode=='medium':
                    if player['position']!='GK':
                        player['physical']+=1
                        player['defending']+=1
                        player['pace']+=1
                        player['fitness']-=8
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            player['physical']+=2
                            player['defending']+=2
                            player['pace']+=2
                            player['fitness']-=12
            if self.training=='balance':
                if self.mode=='easy':
                    if player['position']!='GK':
                        player['shooting']+=0.3
                        player['dribbling']+=0.3
                        player['passing']+=0.3
                        player['pace']+=0.3
                        player['physical']+=0.3
                        player['defending']+=0.3
                        player['fitness']-=4
                    if player['position']=='GK':
                        player['diving']+=0.3
                        player['handling']+=0.3
                        player['kicking']+=0.3
                        player['reflexes']+=0.3
                        player['speed']+=0.3
                        player['positioning']+=0.3
                        player['fitness']-=4
                if self.mode=='medium':
                    if player['position']!='GK':
                        player['shooting']+=0.5
                        player['dribbling']+=0.5
                        player['passing']+=0.5
                        player['pace']+=0.5
                        player['physical']+=0.5
                        player['defending']+=0.5
                        player['fitness']-=8
                    if player['position']=='GK':
                        player['diving']+=0.5
                        player['handling']+=0.5
                        player['kicking']+=0.5
                        player['reflexes']+=0.5
                        player['speed']+=0.5
                        player['positioning']+=0.5
                        player['fitness']-=8
                if self.mode=='hard':
                    if player['fitness']<20:
                        return 'Fitness is too low for Hard Training.'
                    else:
                        if player['position']!='GK':
                            player['shooting']+=1
                            player['dribbling']+=1
                            player['passing']+=1
                            player['pace']+=1
                            player['physical']+=1
                            player['defending']+=1
                            player['fitness']-=12
                        if player['position']=='GK':
                            player['diving']+=1
                            player['handling']+=1
                            player['kicking']+=1
                            player['reflexes']+=1
                            player['speed']+=1
                            player['positioning']+=1
                            player['fitness']-=12