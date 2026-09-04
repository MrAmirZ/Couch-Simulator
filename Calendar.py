import random

def create_calendar(teams):
    teams=teams.copy()
    random.shuffle(teams)
    Calendar=[]
    Total_Team=len(teams)
    Total_Week=Total_Team-1
    Matches_Per_Week=Total_Team//2
    Second_Half = []
    for Half_Season in range(Total_Week):
        Matches=[]
        for Week in range(Matches_Per_Week):
            Home=teams[Week]
            Away=teams[-Week-1]
            Matches.append([Home,Away])
        Calendar.append(Matches)
        teams=[teams[0]]+[teams[-1]]+teams[1:-1]
    for week in Calendar:
        matches = []
        for home,away in week:
            matches.append((away,home))
        Second_Half.append(matches)
    Calendar.extend(Second_Half)
    return Calendar