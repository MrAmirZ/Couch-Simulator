import tkinter as tk
from tkinter import ttk
import random
import copy
from Players import players
import Match as mtc
import Calendar as cal
import Training as Train

Game=tk.Tk()
Game.title('Couch Simulatur')
Game.geometry('1920x1080')
Game.attributes("-fullscreen",True)

SUBTITLE_FONT=('bahnschrift',22)
TEXT_FONT=('bahnschrift',18)
BUTTON_FONT=('bahnschrift',16)
COMBO_FONT=('bahnschrift',12)

MENU_BG = "#2a2b2c"
HEADER_MENU_BG="#454648"
MENU_ITEM_FG="#ffffff"

Start_Frame=tk.Frame(Game,bg=MENU_BG)
Start_Frame.place(x=0,y=0,width=1920,height=1080)
Create_Couch_Frame=tk.Frame(Game,bg=MENU_BG)
Select_couch_Frame=tk.Frame(Game,bg=MENU_BG)
Select_Team_Frame=tk.Frame(Game,bg=MENU_BG)
Loading_Frame=tk.Frame(Game,bg=MENU_BG)
Header_Menu_Frame=tk.Frame(Game,bg=HEADER_MENU_BG)
Menu_Separator_Frame=tk.Frame(Game,bg='white',width=1)
Menu_Frame=tk.Frame(Game,bg=MENU_BG)
Squad_Frame1=tk.Frame(Game,bg=MENU_BG)
Squad_Frame2=tk.Frame(Game,bg=MENU_BG)
Player_Frame=tk.Frame(Game,bg=MENU_BG)
Training_Frame=tk.Frame(Game,bg=MENU_BG)
Tactic_Team_Frame1=tk.Frame(Game,bg="#00CE1F")
Tactic_Team_Frame2=tk.Frame(Game,bg="#00CE1F")
Tactic_Separator_Frame=tk.Frame(Tactic_Team_Frame2,bg="#3f3f46")
Statistics_Goal_Frame=tk.Frame(Game,bg=MENU_BG)
Calendar_Frame=tk.Frame(Game,bg=MENU_BG)
Match_Frame=tk.Frame(Game,bg=MENU_BG)

s1=tk.StringVar()
s2=tk.StringVar()
s3=tk.StringVar()
s4=tk.StringVar()

t1=tk.StringVar()
t2=tk.StringVar()
t3=tk.StringVar()
t4=tk.StringVar()
t5=tk.StringVar()
t6=tk.StringVar()
t7=tk.StringVar()
t8=tk.StringVar()
t9=tk.StringVar()
t10=tk.StringVar()
t11=tk.StringVar()
t12=tk.StringVar()
t13=tk.StringVar()

r1=tk.StringVar()
r2=tk.StringVar()
r3=tk.StringVar()
r4=tk.StringVar()
r5=tk.StringVar()
r6=tk.StringVar()
r7=tk.StringVar()
r8=tk.StringVar()
r9=tk.StringVar()
r10=tk.StringVar()
r11=tk.StringVar()
r12=tk.StringVar()

Fullscreen=True
Game_Player=copy.deepcopy(players)
q=0
Last_Country_Selected='Spain'
Confirm_Win_Control=0
Team='Barcelona'
League_Table=[]
Currect_Day=1
Match_Index=0
x2=1200
x_x_x=100
x_x=50
x=20
y2=30
y_y_y=130
y_y=80
y=20
s=0
n=0
League = {}
Players_Squad1=[]
Players_Squad2=[]
League_Team={}
l=[]
titles = ['#', 'Team', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'PTS']
Player_Info=[]
Tactics_List=['4-3-3','4-4-2','5-3-2','4-2-4','4-5-1','4-1-2-1-2','3-5-2','4-3-2-1']
Tactics=[]
Player_Starting_Place_List=[]
Player_Bench_Place_List=[]
Currect_Place="#00a20d"
Wrong_Place="#ff0000"
tx1=[600,1000,400,800,150,350,600,850,1000,150,600]
ty1=[600,450,500,500,450,250,300,250,100,100,50]
tp1=['GK','RB','CB','CB','LB','CM','CDM','CM','RW','LW','ST']
tx2=[600,1000,400,800,150,1000,450,750,150,450,750]
ty2=[600,450,500,500,450,200,250,250,200,50,50]
tp2=['GK','RB','CB','CB','LB','RM','CM','CM','LM','ST','ST']
tx3=[600,1000,350,600,850,150,350,600,850,450,750]
ty3=[600,450,500,500,500,450,250,300,250,50,50]
tp3=['GK','RB','CB','CB','CB','LB','CM','CDM','CM','ST','ST']
tx4=[600,1000,400,800,150,450,750,1000,450,750,150]
ty4=[600,450,500,500,450,250,250,100,50,50,100]
tp4=['GK','RB','CB','CB','LB','CM','CM','RW','ST','ST','LW']
tx5=[600,1000,400,800,150,1000,450,600,750,150,600]
ty5=[600,450,500,500,450,200,250,300,250,200,100]
tp5=['GK','RB','CB','CB','LB','RM','CM','CDM','CM','LM','ST']
tx6=[600,1000,400,800,150,600,400,800,600,450,750]
ty6=[600,450,500,500,450,350,250,250,200,100,100]
tp6=['GK','RB','CB','CB','LB','CDM','CM','CM','CAM','ST','ST']
tx7=[600,400,600,800,1000,450,600,750,150,450,750]
ty7=[600,450,450,450,200,250,300,250,200,100,100]
tp7=['GK','CB','CB','CB','RM','CM','CDM','CM','LM','ST','ST']
tx8=[600,1000,450,750,150,400,600,800,500,700,600]
ty8=[600,450,500,500,450,325,325,325,200,200,50]
tp8=['GK','RB','CB','CB','LB','CM','CM','CM','CAM','CAM','ST']
tbx=50
tby=700
Combo_Captain=[]
Combo_Penalty_Taker=[]
Combo_Short_Free_Kick_Taker=[]
Combo_Long_Free_Kick_Taker=[]
Combo_Corner_Taker=[]
Combo_Long_Throw_Taker=[]
Combo_Target_man=[]
Combo_Playmaker=[]
Combo_Pressing_Leader=[]
Combo_Fast_Break_Runner=[]
Combo_Ball_Winner=[]
Selected=None
Currect_Formation='4-3-3'

def toggle_fullscreen(event=None):
    global Fullscreen
    Fullscreen=not Fullscreen
    Game.attributes("-fullscreen",Fullscreen)

def exit_game(event=None):
    Game.destroy()

def start():
    L_Welcome_Start.place_forget()
    Start_btn.place_forget()
    Create_Couch_Frame.place_forget()
    Start_Frame.place(x=0,y=0,width=1920,height=1080)
    L_Select_Or_Create_Couch.place(x=605,y=150)
    Create_Couch_btn.place(x=550,y=250)
    Select_Couch_btn.place(x=750,y=250)

def create_couch():
    Start_Frame.place_forget()
    Create_Couch_Frame.place(x=0,y=0,width=1920,height=1080)

def select_couch():
    pass

def select_team():
    global L_Couch_Team,q,Last_Country_Selected,Team
    m1=s1.get()
    m2=s2.get()
    m3=s3.get()
    if m1 and m2 and m3:
        if not m1.isalpha():
            L_Report_Age.config(text='Your Name is Wrong')
        elif not m2.isdigit():
            L_Report_Age.config(text='Your Age is Wrong')
        elif int(m2)>80 or int(m2)<18:
            L_Report_Age.config(text='Age Must Betwen 18 and 80')
        else:
            Create_Couch_Frame.place_forget()
            Select_couch_Frame.place_forget()
            Select_Team_Frame.place(x=0,y=0,width=1920,height=1080)
            L_Report_Age.config(text='')
    elif not m1 or not m2 or not m3:
        L_Report_Age.config(text='Fill all the Field')

def check_country():
    global Last_Country_Selected,q,Team,Teams
    if Last_Country_Selected!=s4.get():
        Last_Country_Selected=s4.get()
        q=0
        Teams=list(Game_Player[s4.get()].keys())
        Team=Teams[0]
        L_Couch_Team.config(text=Team)
    Select_Team_Frame.after(1,check_country)

def next_team():
    global q,Last_Country_Selected,Team,Teams
    if Last_Country_Selected!=s4.get():
        q=0
        Last_Country_Selected=s4.get()
    Teams=list(Game_Player[s4.get()].keys())
    q=q+1
    if q==len(Teams):
        q=0
    Team=Teams[q]
    L_Couch_Team.config(text=Team)

def previous_team():
    global q,Last_Country_Selected,Team,Teams
    if Last_Country_Selected!=s4.get():
        q=0
        Last_Country_Selected=s4.get()
    Teams=list(Game_Player[s4.get()].keys())
    q=q-1
    if q<0:
        q=len(Teams)-1
    Team=Teams[q]
    L_Couch_Team.config(text=Team)

def confirm():
    global s1,s2,s3,Confirm_Win,Confirm_Win_Control,s,n,Loading_Time
    if Confirm_Win_Control==0:
        m1=s1.get()
        m2=s2.get()
        m3=s3.get()
        Confirm_Win=tk.Toplevel()
        Confirm_Win.title('Confirm Win')
        Confirm_Win.geometry('445x200+530+285')
        L_Couch=tk.Label(Confirm_Win,text='Please Review Your Selections.'+'\n'+f'Couch Name:{m1} \nCouch Age:{m2} \nCountry:{m3} \nTeam:{Team}\n'+'Are You Sure You Want To Start Your Career With This Team?',font=COMBO_FONT)
        L_Couch.place(x=0,y=0)
        Confirm_Btn=tk.Button(Confirm_Win,text='Confirm',font=BUTTON_FONT,command=loading)
        Back_Btn=tk.Button(Confirm_Win,text='Back',font=BUTTON_FONT,command=back_confirm)
        Confirm_Btn.place(x=250,y=140)
        Back_Btn.place(x=125,y=140)
        Loading_Time = [6,8,10]
        s=random.choice(Loading_Time)
        n=0
        Confirm_Win_Control=1
    elif Confirm_Win_Control==1:
        if Confirm_Win.winfo_exists():
            return
        else:
            Confirm_Win_Control=0
            confirm()

def back_confirm():
    global Confirm_Win,Confirm_Win_Control
    Confirm_Win.destroy()
    Confirm_Win_Control=0

def loading():
    global Confirm_Win,s,n,Loading_Time,L_Loading,Teams,Currect_Formation
    Confirm_Win.destroy()
    Select_Team_Frame.place_forget()
    Loading_Frame.place(x=0,y=0,width=1920,height=1080)
    if n%2==0:
        L_Loading.config(text='Loading...')
    if n%2==1:
        L_Loading.config(text='Loading..')
    n=n+1
    if s>n:
        Loading_Frame.after(500,loading)
    else:
        n=0
        Loading_Frame.place_forget()
        Teams=list(Game_Player[s4.get()].keys())
        create_league()
        L_Team_Name.config(text=f'{Team} \n Team')
        L_Team_Budget.config(text=f'{readonly_number(Game_Player[s4.get()][Team]['budget'])}$ \n Budget')
        Currect_Formation=Game_Player[s4.get()][Team]['formation']
        L_Team_Overall.config(text=f'{show_overall_team(Game_Player[s4.get()][Team]['starting'],Currect_Formation)} \n OVR')
        main_menu()

def readonly_number(number):
    return f'{number:,}'

def create_league():
    global Teams
    if League:
        return
    Teams=list(Game_Player[s4.get()].keys())
    for team in Teams:
        League[team] = {"P": 0,"W": 0,"D": 0,"L": 0,"GF": 0,"GA": 0,"GD": 0,"PTS": 0}

def main_menu():
    global Teams,Game_Calendar
    Squad_Frame1.place_forget()
    Squad_Frame2.place_forget()
    Training_Frame.place_forget()
    Tactic_Team_Frame1.place_forget()
    Statistics_Goal_Frame.place_forget()
    Calendar_Frame.place_forget()
    Header_Menu_Frame.place(x=0,y=0,width=1920,height=60)
    Menu_Separator_Frame.place(x=0,y=61,width=1920,height=1)
    Menu_Frame.place(x=0,y=62,width=1920,height=1080)
    Teams=list(Game_Player[s4.get()].keys())
    Game_Calendar=cal.create_calendar(Teams)
    L_Team_Name.config(text=f'{Team} \n Team')
    L_Team_Budget.config(text=f'{readonly_number(Game_Player[s4.get()][Team]['budget'])}$ \n Budget')
    Currect_Formation=Game_Player[s4.get()][Team]['formation']
    L_Team_Overall.config(text=f'{show_overall_team(Game_Player[s4.get()][Team]['starting'],Currect_Formation)} \n OVR')
    show_league()

def show_league():
    global League_Table
    for i in range(12):
        League_Table[i][1].config(text=Teams[i])
        League_Table[i][0].config(text=i+1)
        League_Table[i][2].config(text=League[Teams[i]]['P'])
        League_Table[i][3].config(text=League[Teams[i]]['W'])
        League_Table[i][4].config(text=League[Teams[i]]['D'])
        League_Table[i][5].config(text=League[Teams[i]]['L'])
        League_Table[i][6].config(text=League[Teams[i]]['GF'])
        League_Table[i][7].config(text=League[Teams[i]]['GA'])
        League_Table[i][8].config(text=League[Teams[i]]['GD'])
        League_Table[i][9].config(text=League[Teams[i]]['PTS'])

def starting_team_squad():
    global Team,x,y
    Menu_Frame.place_forget()
    Squad_Frame2.place_forget()
    Squad_Frame1.place(x=0,y=0,width=1920,height=1080)
    for btn in Players_Squad1:
        btn.destroy()
    Players_Squad1.clear()
    for player in Game_Player[s4.get()][Team]['starting']:
        Players_Squad1_Btn=tk.Button(Squad_Frame1,font=TEXT_FONT,text=f"{player['position']}       {player['name']}       {player['overall']}",command=lambda p=player:show_player(p,'starting'),bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
        Players_Squad1_Btn.place(x=x,y=y,width=1480)
        Players_Squad1.append(Players_Squad1_Btn)
        y=y+60
    x=20
    y=20

def bench_team_squad():
    global Team,x,y
    Squad_Frame1.place_forget()
    Squad_Frame2.place(x=0,y=0,width=1920,height=1080)
    for btn in Players_Squad2:
        btn.destroy()
    Players_Squad2.clear()
    for player in Game_Player[s4.get()][Team]['bench']:
        Players_Squad2_Btn=tk.Button(Squad_Frame2,font=TEXT_FONT,text=f"{player['position']}  {player['name']}  {player['overall']}",command=lambda p=player:show_player(p,'bench'),bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
        Players_Squad2_Btn.place(x=x,y=y,width=1480)
        Players_Squad2.append(Players_Squad2_Btn)
        y=y+60
    x=20
    y=20

def show_player(player,page):
    global Currect_Page
    Squad_Frame1.place_forget()
    Squad_Frame2.place_forget()
    Player_Frame.place(x=0,y=0,width=1920,height=1080)
    Currect_Page=page
    L_PlayerInfo.config(text=f'Player Info {player['name']}')
    for i in range(len(Player_Info)):
        Player_Info[i].config(text=f'{list(player.keys())[i]}: {list(player.values())[i]}')

def back_player():
    Player_Frame.place_forget()
    if Currect_Page=='starting':
        starting_team_squad()
    else:
        bench_team_squad()

def training_frame():
    Menu_Frame.place_forget()
    Training_Frame.place(x=0,y=0,width=1920,height=1080)

def tactic_team():
    Menu_Frame.place_forget()
    Tactic_Team_Frame1.place(x=0,y=0,width=1920,height=1080)
    players_formation(Currect_Formation)
    L_Overall_Team.config(text=f'Overall: {show_overall_team(Game_Player[s4.get()][Team]['starting'],Currect_Formation)}')

def players_formation(formation):
    global Player_Starting_Place,Currect_Formation
    Currect_Formation=formation
    for i in Player_Starting_Place_List:
        i.destroy()
    Player_Starting_Place_List.clear()
    if formation=='4-3-3':
        for i in range(11):
            Player_Starting_Place=tk.Button(Tactic_Team_Frame1,command=lambda i=i: select_starting(i))
            Player_Starting_Place.place(x=tx1[i],y=ty1[i])
            if Game_Player[s4.get()][Team]['starting'][i]['position']==tp1[i]:
                Player_Starting_Place.config(bg=Currect_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {tp1[i]}')
            else:
                Player_Starting_Place.config(bg=Wrong_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']}\n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {Game_Player[s4.get()][Team]['starting'][i]['position']} => {tp1[i]}')
            Player_Starting_Place_List.append(Player_Starting_Place)
            show_overall_team(Game_Player[s4.get()][Team]['starting'],Currect_Formation)
    if formation=='4-4-2':
        for i in range(11):
            Player_Starting_Place=tk.Button(Tactic_Team_Frame1,command=lambda i=i: select_starting(i))
            Player_Starting_Place.place(x=tx2[i],y=ty2[i])
            if Game_Player[s4.get()][Team]['starting'][i]['position']==tp2[i]:
                Player_Starting_Place.config(bg=Currect_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {tp2[i]}')
            else:
                Player_Starting_Place.config(bg=Wrong_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {Game_Player[s4.get()][Team]['starting'][i]['position']} => {tp2[i]}')
            Player_Starting_Place_List.append(Player_Starting_Place)
            show_overall_team(Game_Player[s4.get()][Team]['starting'],Currect_Formation)
    if formation=='5-3-2':
        for i in range(11):
            Player_Starting_Place=tk.Button(Tactic_Team_Frame1,command=lambda i=i: select_starting(i))
            Player_Starting_Place.place(x=tx3[i],y=ty3[i])
            if Game_Player[s4.get()][Team]['starting'][i]['position']==tp3[i]:
                Player_Starting_Place.config(bg=Currect_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {tp3[i]}')
            else:
                Player_Starting_Place.config(bg=Wrong_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {Game_Player[s4.get()][Team]['starting'][i]['position']} => {tp3[i]}')
            Player_Starting_Place_List.append(Player_Starting_Place)
            show_overall_team(Game_Player[s4.get()][Team]['starting'],Currect_Formation)
    if formation=='4-2-4':
        for i in range(11):
            Player_Starting_Place=tk.Button(Tactic_Team_Frame1,command=lambda i=i: select_starting(i))
            Player_Starting_Place.place(x=tx4[i],y=ty4[i])
            if Game_Player[s4.get()][Team]['starting'][i]['position']==tp4[i]:
                Player_Starting_Place.config(bg=Currect_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {tp4[i]}')
            else:
                Player_Starting_Place.config(bg=Wrong_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {Game_Player[s4.get()][Team]['starting'][i]['position']} => {tp4[i]}')
            Player_Starting_Place_List.append(Player_Starting_Place)
            show_overall_team(Game_Player[s4.get()][Team]['starting'],Currect_Formation)
    if formation=='4-5-1':
        for i in range(11):
            Player_Starting_Place=tk.Button(Tactic_Team_Frame1,command=lambda i=i: select_starting(i))
            Player_Starting_Place.place(x=tx5[i],y=ty5[i])
            if Game_Player[s4.get()][Team]['starting'][i]['position']==tp5[i]:
                Player_Starting_Place.config(bg=Currect_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {tp5[i]}')
            else:
                Player_Starting_Place.config(bg=Wrong_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {Game_Player[s4.get()][Team]['starting'][i]['position']} => {tp5[i]}')
            Player_Starting_Place_List.append(Player_Starting_Place)
            show_overall_team(Game_Player[s4.get()][Team]['starting'],Currect_Formation)
    if formation=='4-1-2-1-2':
        for i in range(11):
            Player_Starting_Place=tk.Button(Tactic_Team_Frame1,command=lambda i=i: select_starting(i))
            Player_Starting_Place.place(x=tx6[i],y=ty6[i])
            if Game_Player[s4.get()][Team]['starting'][i]['position']==tp6[i]:
                Player_Starting_Place.config(bg=Currect_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {tp6[i]}')
            else:
                Player_Starting_Place.config(bg=Wrong_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {Game_Player[s4.get()][Team]['starting'][i]['position']} => {tp6[i]}')
            Player_Starting_Place_List.append(Player_Starting_Place)
            show_overall_team(Game_Player[s4.get()][Team]['starting'],Currect_Formation)
    if formation=='3-5-2':
        for i in range(11):
            Player_Starting_Place=tk.Button(Tactic_Team_Frame1,command=lambda i=i: select_starting(i))
            Player_Starting_Place.place(x=tx7[i],y=ty7[i])
            if Game_Player[s4.get()][Team]['starting'][i]['position']==tp7[i]:
                Player_Starting_Place.config(bg=Currect_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {tp7[i]}')
            else:
                Player_Starting_Place.config(bg=Wrong_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {Game_Player[s4.get()][Team]['starting'][i]['position']} => {tp7[i]}')
            Player_Starting_Place_List.append(Player_Starting_Place)
            show_overall_team(Game_Player[s4.get()][Team]['starting'],Currect_Formation)
    if formation=='4-3-2-1':
        for i in range(11):
            Player_Starting_Place=tk.Button(Tactic_Team_Frame1,command=lambda i=i: select_starting(i))
            Player_Starting_Place.place(x=tx8[i],y=ty8[i])
            if Game_Player[s4.get()][Team]['starting'][i]['position']==tp8[i]:
                Player_Starting_Place.config(bg=Currect_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {tp8[i]}')
            else:
                Player_Starting_Place.config(bg=Wrong_Place,padx=15,pady=10,text=f'{Game_Player[s4.get()][Team]['starting'][i]['name']} \n {Game_Player[s4.get()][Team]['starting'][i]['overall']} \n {Game_Player[s4.get()][Team]['starting'][i]['position']} => {tp8[i]}')
            Player_Starting_Place_List.append(Player_Starting_Place)
            show_overall_team(Game_Player[s4.get()][Team]['starting'],Currect_Formation)
    show_bench()

def show_bench():
    global tbx, tby
    for btn in Player_Bench_Place_List:
        btn.destroy()
    Player_Bench_Place_List.clear()
    tbx=50
    tby=700
    for i in range(len(Game_Player[s4.get()][Team]['bench'])):
        player=Game_Player[s4.get()][Team]['bench'][i]
        Player_Bench_Place=tk.Button(Tactic_Team_Frame1,text=f"{player['name']}\n{player['overall']}\n{player['position']}",bg="white",font=TEXT_FONT,command=lambda i=i: select_bench(i),width=10,height=3)
        Player_Bench_Place.place(x=tbx, y=tby)
        Player_Bench_Place_List.append(Player_Bench_Place)
        tbx +=150

def show_overall_team(starting_players,formation):
    total=0
    if formation=='4-3-3':
        for i in range(11):
            if starting_players[i]['position']==tp1[i]:
                total+=starting_players[i]['overall']
            else:
                total+=starting_players[i]['overall']-7
    if formation=='4-4-2':
        for i in range(11):
            if starting_players[i]['position']==tp2[i]:
                total+=starting_players[i]['overall']
            else:
                total+=starting_players[i]['overall']-7
    if formation=='5-3-2':
        for i in range(11):
            if starting_players[i]['position']==tp3[i]:
                total+=starting_players[i]['overall']
            else:
                total+=starting_players[i]['overall']-7
    if formation=='4-2-4':
        for i in range(11):
            if starting_players[i]['position']==tp4[i]:
                total+=starting_players[i]['overall']
            else:
                total+=starting_players[i]['overall']-7
    if formation=='4-5-1':
        for i in range(11):
            if starting_players[i]['position']==tp5[i]:
                total+=starting_players[i]['overall']
            else:
                total+=starting_players[i]['overall']-7
    if formation=='4-1-2-1-2':
        for i in range(11):
            if starting_players[i]['position']==tp6[i]:
                total+=starting_players[i]['overall']
            else:
                total+=starting_players[i]['overall']-7
    if formation=='3-5-2':
        for i in range(11):
            if starting_players[i]['position']==tp7[i]:
                total+=starting_players[i]['overall']
            else:
                total+=starting_players[i]['overall']-7
    if formation=='4-3-2-1':
        for i in range(11):
            if starting_players[i]['position']==tp8[i]:
                total+=starting_players[i]['overall']
            else:
                total+=starting_players[i]['overall']-7
    Overall_Team=total//11
    return Overall_Team

def tactic_frame():
    update_team_roles()
    Tactic_Team_Frame1.place_forget()
    Tactic_Team_Frame2.place(x=0,y=0,width=1920,height=1080)
    Tactic_Separator_Frame.place(x=700, y=0, relheight=1)
    Combo_Mentality_Tactic_Frame2.set(Game_Player[s4.get()][Team]['tactics']['mentality'])
    Combo_Pressing_Tactic_Frame2.set(Game_Player[s4.get()][Team]['tactics']['pressing'])
    Combo_Defensive_Line_Tactic_Frame2.set(Game_Player[s4.get()][Team]['tactics']['defensive_line'])
    Combo_Build_Up_Tactic_Frame2.set(Game_Player[s4.get()][Team]['tactics']['build_up'])
    Combo_Width_Tactic_Frame2.set(Game_Player[s4.get()][Team]['tactics']['width'])
    Combo_Chance_Creation_Tactic_Frame2.set(Game_Player[s4.get()][Team]['tactics']['chance_creation'])
    Combo_Tempo_Tactic_Frame2.set(Game_Player[s4.get()][Team]['tactics']['tempo'])
    Combo_Time_Wasting_Tactic_Frame2.set(Game_Player[s4.get()][Team]['tactics']['time_wasting'])
    Combo_Counter_Attack_Tactic_Frame2.set(Game_Player[s4.get()][Team]['tactics']['counter_attack'])
    Combo_Offside_Trap_Tactic_Frame2.set(Game_Player[s4.get()][Team]['tactics']['offside_trap'])
    Combo_Defensive_Style_Tactic_Frame2.set(Game_Player[s4.get()][Team]['tactics']['defensive_style'])
    Combo_Attacking_Focus_Tactic_Frame2.set(Game_Player[s4.get()][Team]['tactics']['attacking_focus'])
    Combo_Creative_Freedom_Tactic_Frame2.set(Game_Player[s4.get()][Team]['tactics']['creative_freedom'])

def back_tactic_frame2():
    Tactic_Team_Frame2.place_forget()
    Tactic_Team_Frame1.place(x=0,y=0,width=1920,height=1080)

def captain_power():
    global Combo_Captain
    Combo_Captain.clear()
    for player in Game_Player[s4.get()][Team]['starting']:
        if player['position']=='GK':
            power=player['positioning']*0.35+player['reflexes']*0.25+player['handling']*0.20+player['overall']*0.20
        else:
            power=player['passing']*0.35+player['defending']*0.25+player['physical']*0.2+player['overall']*0.2
        text=f'{player['name']} - {player['position']} - {round(power)}'
        Combo_Captain.append(text)
    return Combo_Captain

def penalty_power():
    global Combo_Penalty_Taker
    Combo_Penalty_Taker.clear()
    for player in Game_Player[s4.get()][Team]['starting']:
        if player['position']!='GK':
            power=player['shooting']*0.7+player['physical']*0.2+player['dribbling']*0.1
            text=f'{player['name']} - {player['position']} - {round(power)}'
            Combo_Penalty_Taker.append(text)
    return Combo_Penalty_Taker

def short_free_kick_power():
    global Combo_Short_Free_Kick_Taker
    Combo_Short_Free_Kick_Taker.clear()
    for player in Game_Player[s4.get()][Team]['starting']:
        if player['position']!='GK':
            power=player['shooting']*0.6+player['passing']*0.3+player['dribbling']*0.1
            text=f'{player['name']} - {player['position']} - {round(power)}'
            Combo_Short_Free_Kick_Taker.append(text)
    return Combo_Short_Free_Kick_Taker

def long_free_kick_power():
    global Combo_long_Free_Kick_Taker
    Combo_Long_Free_Kick_Taker.clear()
    for player in Game_Player[s4.get()][Team]['starting']:
        if player['position']!='GK':
            power=player['passing']*0.6+player['shooting']*0.3+player['dribbling']*0.1
            text=f'{player['name']} - {player['position']} - {round(power)}'
            Combo_Long_Free_Kick_Taker.append(text)
    return Combo_Long_Free_Kick_Taker

def corner_Taker_power():
    global Combo_Corner_Taker
    Combo_Corner_Taker.clear()
    for player in Game_Player[s4.get()][Team]['starting']:
        if player['position']!='GK':
            power=player['passing']*0.5+player['dribbling']*0.2+player['shooting']*0.3
            text=f'{player['name']} - {player['position']} - {round(power)}'
            Combo_Corner_Taker.append(text)
    return Combo_Corner_Taker

def long_throw_taker_power():
    global Combo_Long_Throw_Taker
    Combo_Long_Throw_Taker.clear()
    for player in Game_Player[s4.get()][Team]['starting']:
        if player['position']!='GK':
            power=player['physical']*0.6+player['passing']*0.3+player['pace']*0.1
            text=f'{player['name']} - {player['position']} - {round(power)}'
            Combo_Long_Throw_Taker.append(text)
    return Combo_Long_Throw_Taker

def target_man_power():
    global Combo_Target_man
    Combo_Target_man.clear()
    for player in Game_Player[s4.get()][Team]['starting']:
        if player['position']!='GK':
            if player['position']=='ST':
                power=(player['physical']*0.45+player['shooting']*0.3+player['pace']*0.15+player['dribbling']*0.1)+6
            elif player['position'] in ['CAM','LW','RW']:
                power=(player['physical']*0.45+player['shooting']*0.3+player['pace']*0.15+player['dribbling']*0.1)+2
            else:
                power=player['physical']*0.45+player['shooting']*0.3+player['pace']*0.15+player['dribbling']*0.1
            text=f'{player['name']} - {player['position']} - {round(power)}'
            Combo_Target_man.append(text)
    return Combo_Target_man

def playmaker_power():
    global Combo_Playmaker
    Combo_Playmaker.clear()
    for player in Game_Player[s4.get()][Team]['starting']:
        if player['position']!='GK':
            if player['position']=='CAM':
                power=(player['passing']*0.6+player['dribbling']*0.3+player['shooting']*0.1)+5
            elif player['position']=='CM':
                power=(player['passing']*0.6+player['dribbling']*0.3+player['shooting']*0.1)+3
            elif player['position']=='CDM':
                power=(player['passing']*0.6+player['dribbling']*0.3+player['shooting']*0.1)+1
            else:
                power=player['passing']*0.6+player['dribbling']*0.3+player['shooting']*0.1
            text=f'{player['name']} - {player['position']} - {round(power)}'
            Combo_Playmaker.append(text)
    return Combo_Playmaker

def pressing_leader_power():
    global Combo_Pressing_Leader
    Combo_Pressing_Leader.clear()
    for player in Game_Player[s4.get()][Team]['starting']:
        if player['position']!='GK':
            if player['position'] == 'CDM':
                power=(player['physical']*0.45+player['defending']*0.35+player['pace']*0.20)+5
            elif player['position'] == 'CM':
                power=(player['physical']*0.45+player['defending']*0.35+player['pace']*0.20)+3
            elif player['position'] in ['CB', 'CAM']:
                power=(player['physical']*0.45+player['defending']*0.35+player['pace']*0.20)+2
            elif player['position'] in ['RW', 'LW', 'ST']:
                power=(player['physical']*0.45+player['defending']*0.35+player['pace']*0.20)+1
            else:
                power=player['physical']*0.45+player['defending']*0.35+player['pace']*0.20
            text=f'{player['name']} - {player['position']} - {round(power)}'
            Combo_Pressing_Leader.append(text)
    return Combo_Pressing_Leader

def fast_break_runner_power():
    global Combo_Fast_Break_Runner
    Combo_Fast_Break_Runner.clear()
    for player in Game_Player[s4.get()][Team]['starting']:
        if player['position']!='GK':
            if player['position']=='ST':
                power=(player['pace']*0.45+player['shooting']*0.3+player['dribbling']*0.25)+5
            elif player['position'] in ['RW','LW']:
                power=(player['pace']*0.45+player['shooting']*0.3+player['dribbling']*0.25)+4
            elif player['position']=='CAM':
                power=(player['pace']*0.45+player['shooting']*0.3+player['dribbling']*0.25)+2
            else:
                power=player['pace']*0.45+player['shooting']*0.3+player['dribbling']*0.25
            text=f'{player['name']} - {player['position']} - {round(power)}'
            Combo_Fast_Break_Runner.append(text)
    return Combo_Fast_Break_Runner

def ball_winner_power():
    global Combo_Ball_Winner
    Combo_Ball_Winner.clear()
    for player in Game_Player[s4.get()][Team]['starting']:
        if player['position']!='GK':
            power=player['defending']*0.6+player['physical']*0.3+player['pace']*0.1
            text=f'{player['name']} - {player['position']} - {round(power)}'
            Combo_Ball_Winner.append(text)
    return Combo_Ball_Winner

def select_starting(number):
    global Selected
    if Selected is None:
        Selected = ("starting", number)
        Player_Starting_Place_List[number].config(bg="yellow")
        return
    place, index = Selected
    if place == "starting":
        swap_starting(index, number)
    else:
        swap_player(number, index)

def select_bench(number):
    global Selected
    if Selected is None:
        Selected = ("bench", number)
        Player_Bench_Place_List[number].config(bg="yellow")
        return
    place, index = Selected
    if place == "starting":
        swap_player(index, number)
    else:
        swap_bench(index, number)

def update_team_roles():
    Combo_Captain_Tactic_Frame2["values"] = captain_power()
    Combo_Penalty_Taker_Tactic_Frame2["values"] = penalty_power()
    Combo_Short_Free_Kick_Tactic_Frame2["values"] = short_free_kick_power()
    Combo_long_Free_Kick_Tactic_Frame2["values"] = long_free_kick_power()
    Combo_Left_Corner_Tactic_Frame2["values"] = corner_Taker_power()
    Combo_Right_Corner_Tactic_Frame2["values"] = corner_Taker_power()
    Combo_Long_Throw_Tactic_Frame2["values"] = long_throw_taker_power()
    Combo_Target_Man_Tactic_Frame2["values"] = target_man_power()
    Combo_Playmaker_Tactic_Frame2["values"] = playmaker_power()
    Combo_Pressing_Leader_Tactic_Frame2["values"] = pressing_leader_power()
    Combo_Fast_Break_Runner_Tactic_Frame2["values"] = fast_break_runner_power()
    Combo_Ball_Winner_Tactic_Frame2["values"] = ball_winner_power()

def swap_starting(first,second):
    global Selected
    Game_Player[s4.get()][Team]['starting'][first], Game_Player[s4.get()][Team]['starting'][second] = Game_Player[s4.get()][Team]['starting'][second], Game_Player[s4.get()][Team]['starting'][first]
    Selected = None
    players_formation(Currect_Formation)

def swap_bench(first,second):
    global Selected
    Game_Player[s4.get()][Team]['bench'][first], Game_Player[s4.get()][Team]['bench'][second] = Game_Player[s4.get()][Team]['bench'][second], Game_Player[s4.get()][Team]['bench'][first]
    Selected = None
    players_formation(Currect_Formation)

def swap_player(starting,bench):
    global Selected
    Game_Player[s4.get()][Team]['starting'][starting], Game_Player[s4.get()][Team]['bench'][bench] = Game_Player[s4.get()][Team]['bench'][bench], Game_Player[s4.get()][Team]['starting'][starting]
    Selected = None
    players_formation(Currect_Formation)

def statistics_goal():
    Menu_Frame.place_forget()
    Statistics_Goal_Frame.place(x=0,y=0,width=1920,height=1080)

def calendar():
    Menu_Frame.place_forget()
    Calendar_Frame.place(x=0,y=0,width=1920,height=1080)

def play_match():
    global Game_Calendar,Currect_Day,Game_Player,match
    Menu_Frame.place_forget()
    Match_Frame.place(x=0,y=0,width=1920,height=1080)
    for i in Game_Calendar[Currect_Day]:
        if Team in i:
            home=Game_Player[s4.get()][i[0]]
            away=Game_Player[s4.get()][i[1]]
            L_Home_Game.config(text=i[0])
            L_Away_Game.config(text=i[1])
            match=mtc.Match_Engine(home,away)
def start_match():
    Start_Game_Btn.place_forget()
    if match.pause==True:
        match.pause=False
        match.minute=46
    update_match()

def update_match():
    global match
    event=match.game_engine()
    L_Home_Goal.config(text=match.home_goal)
    L_Away_Goal.config(text=match.away_goal)
    if event=='half time':
        L_Result_Match.config(text='half time')
        Start_Game_Btn.place(x=700,y=700)
        return
    elif event=='full time':
        L_Result_Match.config(text='full time')
        return
    else:
        L_Result_Match.config(text=f'{match.minute} {event}')
    Match_Frame.after(1000,update_match)

Game.bind("<F11>",toggle_fullscreen)
Game.bind("<Alt-F4>",exit_game)

L_Welcome_Start=tk.Label(Start_Frame,text='Welcome to the Couch Simulator'+'\n'+'Please Click the Button',font=SUBTITLE_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
L_Welcome_Start.place(x=530,y=150)
Start_btn=tk.Button(Start_Frame,text='Start',font=('arial',20),command=start,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Start_btn.place(x=700,y=250)
L_Select_Or_Create_Couch=tk.Label(Start_Frame,text='Please Select One',font=SUBTITLE_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
Create_Couch_btn=tk.Button(Start_Frame,text='Create Couch',font=BUTTON_FONT,command=create_couch,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Select_Couch_btn=tk.Button(Start_Frame,text='Select Couch',font=BUTTON_FONT,command=select_couch,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
L_Create_Your_Couch=tk.Label(Create_Couch_Frame,text='Create Your Couch',font=SUBTITLE_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
L_Name_Couch=tk.Label(Create_Couch_Frame,text='Couch Name:',font=TEXT_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
L_Age_Couch=tk.Label(Create_Couch_Frame,text='Couch Age:',font=TEXT_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
L_Country_Couch=tk.Label(Create_Couch_Frame,text='Country:',font=TEXT_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
E_Name_couch=tk.Entry(Create_Couch_Frame,textvariable=s1,font=COMBO_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
E_Age_Couch=tk.Entry(Create_Couch_Frame,textvariable=s2,font=COMBO_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Country_Couch=ttk.Combobox(Create_Couch_Frame,values=list(players.keys()),font=COMBO_FONT,textvariable=s3)
Create_Couch_Btn=tk.Button(Create_Couch_Frame,text='Create',font=BUTTON_FONT,command=select_team,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Back_Create_Couch_Btn=tk.Button(Create_Couch_Frame,text='Back',font=BUTTON_FONT,command=start,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
L_Report_Age=tk.Label(Create_Couch_Frame,font=BUTTON_FONT,fg='red',bg=MENU_BG)
L_Create_Your_Couch.place(x=620,y=50)
L_Name_Couch.place(x=600,y=200)
L_Age_Couch.place(x=600,y=250)
L_Country_Couch.place(x=600,y=300)
E_Name_couch.place(x=750,y=210)
E_Age_Couch.place(x=730,y=260)
Country_Couch.place(x=700,y=310)
Create_Couch_Btn.place(x=760,y=360)
Back_Create_Couch_Btn.place(x=650,y=360)
L_Report_Age.place(x=670,y=150)
L_Choose_Team=tk.Label(Select_Team_Frame,text='Choose your Team',font=('arial',24),bg=MENU_BG,fg=MENU_ITEM_FG)
L_Couch_Team=tk.Label(Select_Team_Frame,font=SUBTITLE_FONT,text='Barcelona',bg=MENU_BG,fg=MENU_ITEM_FG)
Next_Selected_Team=tk.Button(Select_Team_Frame,text='>',font=BUTTON_FONT,command=next_team,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Back_Selected_Team=tk.Button(Select_Team_Frame,text='<',font=BUTTON_FONT,command=previous_team,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
L_Select_Team=tk.Label(Select_Team_Frame,text='Select a Country:',font=TEXT_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
Combo_Select_Coutry=ttk.Combobox(Select_Team_Frame,font=COMBO_FONT,textvariable=s4,values=list(players.keys()))
Combo_Select_Coutry.set('Spain')
Save_Team_Btn=tk.Button(Select_Team_Frame,text='Save',font=BUTTON_FONT,command=confirm,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
L_Choose_Team.place(x=620,y=50)
L_Couch_Team.place(x=700,y=350)
Next_Selected_Team.place(x=1050,y=350)
Back_Selected_Team.place(x=450,y=350)
L_Select_Team.place(x=550,y=150)
Combo_Select_Coutry.place(x=750,y=160)
Save_Team_Btn.place(x=720,y=450)
L_Loading=tk.Label(Loading_Frame,font=('bahnschrift',72),bg=MENU_BG,fg=MENU_ITEM_FG)
L_Loading.place(x=580,y=300)
L_Team_Name=tk.Label(Header_Menu_Frame,font=BUTTON_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
L_Team_Overall=tk.Label(Header_Menu_Frame,font=BUTTON_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
L_Team_Budget=tk.Label(Header_Menu_Frame,font=BUTTON_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
L_Team_Position=tk.Label(Header_Menu_Frame,font=BUTTON_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
L_Team_Name.place(x=20,y=5)
L_Team_Budget.place(x=180,y=5)
L_Team_Overall.place(x=340,y=5)
L_Team_Position.place(x=500,y=5)
Squad_Menu_Btn=tk.Button(Menu_Frame,text='Squad',font=BUTTON_FONT,command=starting_team_squad,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Transfer_Market_Menu_Btn=tk.Button(Menu_Frame,text='Transfer Market',font=BUTTON_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Training_Menu_Btn=tk.Button(Menu_Frame,text='Tranning',font=BUTTON_FONT,command=training_frame,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Tactics_Menu_Btn=tk.Button(Menu_Frame,text='Tactics',font=BUTTON_FONT,command=tactic_team,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Calendar_Menu_Btn=tk.Button(Menu_Frame,text='Calendar',font=BUTTON_FONT,command=calendar,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Statistics_Menu_Btn=tk.Button(Menu_Frame,text='Statistics',font=BUTTON_FONT,command=statistics_goal,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Next_Day_Match_Menu_Btn=tk.Button(Menu_Frame,text='Next Day',font=BUTTON_FONT,command=play_match,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Save_Menu_Btn=tk.Button(Menu_Frame,text='Save Game',font=BUTTON_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Bench_Squad_Btn=tk.Button(Squad_Frame1,text='Bench',font=TEXT_FONT,command=bench_team_squad,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Back_Bench_To_Starting_Squad=tk.Button(Squad_Frame2,text='Back',font=TEXT_FONT,command=starting_team_squad,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Back_Menu_Squad1_Btn=tk.Button(Squad_Frame1,text='Back Menu',font=TEXT_FONT,command=main_menu,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Back_Menu_Squad2_Btn=tk.Button(Squad_Frame2,text='Back Menu',font=TEXT_FONT,command=main_menu,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
L_Choose_Training=tk.Label(Training_Frame,text='Choose Training',font=SUBTITLE_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
Physical_Training_Btn=tk.Button(Training_Frame,text='Physical \n\n+ Physical',font=TEXT_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG,width=15)
Shooting_Training_Btn=tk.Button(Training_Frame,text='Shooting \n\n+ Shooting',font=TEXT_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG,width=15)
Passing_Training_Btn=tk.Button(Training_Frame,text='Passing \n\n+ Passing',font=TEXT_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG,width=15)
Pace_Training_Btn=tk.Button(Training_Frame,text=f'Pace \n\n+ Pace',font=TEXT_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG,width=15)
Dribbling_Training_Btn=tk.Button(Training_Frame,text=f'Dribbling \n\n+ Dribling',font=TEXT_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG,width=15)
Defending_Training_Btn=tk.Button(Training_Frame,text=f'Defending \n\n+ Defenfing',font=TEXT_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG,width=15)
Attacking_Training_Btn=tk.Button(Training_Frame,text=f'Attacking \n\n+ Shooting\n+ Dribbling\n+ Passing\n+ Pace',font=TEXT_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG,width=15)
Defensive_Training_Btn=tk.Button(Training_Frame,text=f'Defensive \n\n+ Defending\n+ Physical\n+ Pace',font=TEXT_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG,width=15,height=6)
Balance_Training_Btn=tk.Button(Training_Frame,text=f'Balance \n\n+ All',font=TEXT_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG,width=15,height=6)
Back_Training_Menu_Btn=tk.Button(Training_Frame,text=f'Back',font=TEXT_FONT,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG,command=main_menu)
Squad_Menu_Btn.place(x=50,y=700)
Transfer_Market_Menu_Btn.place(x=200,y=700)
Training_Menu_Btn.place(x=450,y=700)
Tactics_Menu_Btn.place(x=630,y=700)
Calendar_Menu_Btn.place(x=800,y=700)
Statistics_Menu_Btn.place(x=1000,y=700)
Next_Day_Match_Menu_Btn.place(x=1175,y=700)
Save_Menu_Btn.place(x=1330,y=700)
Bench_Squad_Btn.place(x=1320,y=730)
Back_Bench_To_Starting_Squad.place(x=1320,y=730)
Back_Menu_Squad1_Btn.place(x=100,y=730)
Back_Menu_Squad2_Btn.place(x=100,y=730)
L_Choose_Training.place(x=620,y=70)
Physical_Training_Btn.place(x=220,y=170)
Shooting_Training_Btn.place(x=620,y=170)
Passing_Training_Btn.place(x=1020,y=170)
Pace_Training_Btn.place(x=220,y=320)
Dribbling_Training_Btn.place(x=620,y=320)
Defending_Training_Btn.place(x=1020,y=320)
Attacking_Training_Btn.place(x=220,y=470)
Defensive_Training_Btn.place(x=620,y=470)
Balance_Training_Btn.place(x=1020,y=470)
Back_Training_Menu_Btn.place(x=1320,y=730)
L_PlayerInfo=tk.Label(Player_Frame,font=SUBTITLE_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
Back_Player_Btn=tk.Button(Player_Frame,text='Back',font=TEXT_FONT,command=back_player,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
L_PlayerInfo.place(x=650,y=20)
Back_Player_Btn.place(x=100,y=720)
L_Overall_Team=tk.Label(Tactic_Team_Frame1,font=TEXT_FONT,bg="#00CE1F")
L_Overall_Team.place(x=0,y=0)
Tactics_Frame2_Btn=tk.Button(Tactic_Team_Frame1,text='Tactics',font=BUTTON_FONT,command=tactic_frame)
Tactics_Frame2_Btn.place(x=1200,y=670,width=300)
Back_Menu_Tactic_Frame1=tk.Button(Tactic_Team_Frame1,text='Back',font=TEXT_FONT,command=main_menu)
Back_Menu_Tactic_Frame1.place(x=1200,y=750,width=300)
L_Team_Instruction_Sub=tk.Label(Tactic_Team_Frame2,text='Team Instruction',font=SUBTITLE_FONT,bg="#00CE1F")
L_Team_Instruction_Sub.place(x=10,y=0)
L_Mentality_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Mentality:',font=TEXT_FONT,bg="#00CE1F")
L_Pressing_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Pressing:',font=TEXT_FONT,bg="#00CE1F")
L_Defensive_Line_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Defensive Line:',font=TEXT_FONT,bg="#00CE1F")
L_Build_Up_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Build Up:',font=TEXT_FONT,bg="#00CE1F")
L_Width_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Width:',font=TEXT_FONT,bg="#00CE1F")
L_Chance_Creation_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Chance Creation:',font=TEXT_FONT,bg="#00CE1F")
L_Tempo_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Tempo:',font=TEXT_FONT,bg="#00CE1F")
L_Time_Wasting_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Time Wasting:',font=TEXT_FONT,bg="#00CE1F")
L_Counter_Attack_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Counter Attack:',font=TEXT_FONT,bg="#00CE1F")
L_Offside_Trap_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Offside Trap:',font=TEXT_FONT,bg="#00CE1F")
L_Defensive_Style_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Defensive Style:',font=TEXT_FONT,bg="#00CE1F")
L_Attacking_Focus_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Attacking Focus:',font=TEXT_FONT,bg="#00CE1F")
L_Creative_Freedom_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Creative Freedom:',font=TEXT_FONT,bg="#00CE1F")
Combo_Mentality_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=['Ultra Defensive','Defensive','Balance','Attacking','Ultra Attacking'],textvariable=t1)
Combo_Pressing_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=['Low','Normal','High'],textvariable=t2)
Combo_Defensive_Line_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=['Very Deep','Deep','Normal','High','Very High'],textvariable=t3)
Combo_Build_Up_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=['Slow Build Up','Possession','Balanced','Direct Passing','Long Ball'],textvariable=t4)
Combo_Width_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=['Very Narrow','Narrow','Balanced','Very Wide'],textvariable=t5)
Combo_Chance_Creation_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=['Crosses','Short Passing','Mixed','Though Balls'],textvariable=t6)
Combo_Tempo_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=['Very Slow','Slow','Normal','Fast','Very Fast'],textvariable=t7)
Combo_Time_Wasting_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=['Off','Sometimes','Always'],textvariable=t8)
Combo_Counter_Attack_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=['On','Off'],textvariable=t9)
Combo_Offside_Trap_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=['On','Off'],textvariable=t10)
Combo_Defensive_Style_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=['Drop Back','Balance','Press After Possession Loss','Constant Pressure'],textvariable=t11,width=23)
Combo_Attacking_Focus_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=['Left','Right','Center','Mixed'],textvariable=t12)
Combo_Creative_Freedom_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=['Disciplined','Balanced','Free'],textvariable=t13)
L_Mentality_Tactic_Frame2.place(x=10,y=50)
L_Pressing_Tactic_Frame2.place(x=10,y=110)
L_Defensive_Line_Tactic_Frame2.place(x=10,y=170)
L_Build_Up_Tactic_Frame2.place(x=10,y=230)
L_Width_Tactic_Frame2.place(x=10,y=290)
L_Chance_Creation_Tactic_Frame2.place(x=10,y=350)
L_Tempo_Tactic_Frame2.place(x=10,y=410)
L_Time_Wasting_Tactic_Frame2.place(x=10,y=470)
L_Counter_Attack_Tactic_Frame2.place(x=10,y=530)
L_Offside_Trap_Tactic_Frame2.place(x=10,y=590)
L_Defensive_Style_Tactic_Frame2.place(x=10,y=650)
L_Attacking_Focus_Tactic_Frame2.place(x=10,y=710)
L_Creative_Freedom_Tactic_Frame2.place(x=10,y=770)
Combo_Mentality_Tactic_Frame2.place(x=130,y=55)
Combo_Pressing_Tactic_Frame2.place(x=125,y=115)
Combo_Defensive_Line_Tactic_Frame2.place(x=190,y=175)
Combo_Build_Up_Tactic_Frame2.place(x=120,y=235)
Combo_Width_Tactic_Frame2.place(x=95,y=295)
Combo_Chance_Creation_Tactic_Frame2.place(x=200,y=355)
Combo_Tempo_Tactic_Frame2.place(x=105,y=415)
Combo_Time_Wasting_Tactic_Frame2.place(x=175,y=475)
Combo_Counter_Attack_Tactic_Frame2.place(x=190,y=535)
Combo_Offside_Trap_Tactic_Frame2.place(x=160,y=595)
Combo_Defensive_Style_Tactic_Frame2.place(x=195,y=655)
Combo_Attacking_Focus_Tactic_Frame2.place(x=195,y=715)
Combo_Creative_Freedom_Tactic_Frame2.place(x=215,y=775)
L_Team_Roles_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Team Roles',font=SUBTITLE_FONT,bg="#00CE1F")
L_Captain_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Captain:',font=TEXT_FONT,bg="#00CE1F")
L_Penalty_Taker_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Penalty Taker:',font=TEXT_FONT,bg="#00CE1F")
L_Short_Free_Kick_Taker_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Short Free Kick Taker:',font=TEXT_FONT,bg="#00CE1F")
L_Long_Free_Kick_Taker_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Long Free Kick Taker:',font=TEXT_FONT,bg="#00CE1F")
L_Left_Corner_Taker_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Left Corner Taker:',font=TEXT_FONT,bg="#00CE1F")
L_Right_Corner_Taker_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Right Corner Taker:',font=TEXT_FONT,bg="#00CE1F")
L_Long_Throw_Taker_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Long Throw Taker:',font=TEXT_FONT,bg="#00CE1F")
L_Target_Man_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Target Man:',font=TEXT_FONT,bg="#00CE1F")
L_Playmaker_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Playmaker:',font=TEXT_FONT,bg="#00CE1F")
L_Pressing_Leader_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Pressing Leader:',font=TEXT_FONT,bg="#00CE1F")
L_Fast_Break_Runner_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Fast Break Runner:',font=TEXT_FONT,bg="#00CE1F")
L_Ball_Winner_Tactic_Frame2=tk.Label(Tactic_Team_Frame2,text='Ball Winner:',font=TEXT_FONT,bg="#00CE1F")
Combo_Captain_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=captain_power(),textvariable=r1)
Combo_Penalty_Taker_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=penalty_power(),textvariable=r2)
Combo_Short_Free_Kick_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=short_free_kick_power(),textvariable=r3)
Combo_long_Free_Kick_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=long_free_kick_power(),textvariable=r4)
Combo_Left_Corner_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=corner_Taker_power(),textvariable=r5)
Combo_Right_Corner_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=corner_Taker_power(),textvariable=r6)
Combo_Long_Throw_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=long_throw_taker_power(),textvariable=r7)
Combo_Target_Man_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=target_man_power(),textvariable=r8)
Combo_Playmaker_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=playmaker_power(),textvariable=r9)
Combo_Pressing_Leader_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=pressing_leader_power(),textvariable=r10)
Combo_Fast_Break_Runner_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=fast_break_runner_power(),textvariable=r11)
Combo_Ball_Winner_Tactic_Frame2=ttk.Combobox(Tactic_Team_Frame2,font=BUTTON_FONT,values=ball_winner_power(),textvariable=r12)
L_Team_Roles_Tactic_Frame2.place(x=800,y=0)
L_Captain_Tactic_Frame2.place(x=800,y=60)
L_Penalty_Taker_Tactic_Frame2.place(x=800,y=120)
L_Short_Free_Kick_Taker_Tactic_Frame2.place(x=800,y=180)
L_Long_Free_Kick_Taker_Tactic_Frame2.place(x=800,y=240)
L_Left_Corner_Taker_Tactic_Frame2.place(x=800,y=300)
L_Right_Corner_Taker_Tactic_Frame2.place(x=800,y=360)
L_Long_Throw_Taker_Tactic_Frame2.place(x=800,y=420)
L_Target_Man_Tactic_Frame2.place(x=800,y=480)
L_Playmaker_Tactic_Frame2.place(x=800,y=540)
L_Pressing_Leader_Tactic_Frame2.place(x=800,y=600)
L_Fast_Break_Runner_Tactic_Frame2.place(x=800,y=660)
L_Ball_Winner_Tactic_Frame2.place(x=800,y=720)
Combo_Captain_Tactic_Frame2.place(x=895,y=65)
Combo_Penalty_Taker_Tactic_Frame2.place(x=960,y=125)
Combo_Short_Free_Kick_Tactic_Frame2.place(x=1045,y=185)
Combo_long_Free_Kick_Tactic_Frame2.place(x=1040,y=245)
Combo_Left_Corner_Tactic_Frame2.place(x=1005,y=305)
Combo_Right_Corner_Tactic_Frame2.place(x=1015,y=365)
Combo_Long_Throw_Tactic_Frame2.place(x=1005,y=425)
Combo_Target_Man_Tactic_Frame2.place(x=935,y=485)
Combo_Playmaker_Tactic_Frame2.place(x=935,y=545)
Combo_Pressing_Leader_Tactic_Frame2.place(x=990,y=605)
Combo_Fast_Break_Runner_Tactic_Frame2.place(x=1015,y=665)
Combo_Ball_Winner_Tactic_Frame2.place(x=935,y=725)
Back_Tactic_Frame2=tk.Button(Tactic_Team_Frame2,text='Back',font=TEXT_FONT,command=back_tactic_frame2)
Back_Tactic_Frame2.place(x=1330,y=750)
L_Statistics_Goal_Frame=tk.Label(Statistics_Goal_Frame,text='Goal',font=TEXT_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
L_Statistics_Goal_Frame.place(x=700,y=0)
Statistics_First_Day=tk.Label(Statistics_Goal_Frame,text='Game is Not Started!',font=SUBTITLE_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
Statistics_First_Day.place(x=600,y=360)
Statistics_Back_Btn=tk.Button(Statistics_Goal_Frame,text='Back',font=TEXT_FONT,command=main_menu,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Statistics_Back_Btn.place(x=1330,y=750)
L_Calendar_Comming_Soon=tk.Label(Calendar_Frame,text='Comming Soon',font=SUBTITLE_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
L_Calendar_Comming_Soon.place(x=650,y=360)
Calendar_Back_Btn=tk.Button(Calendar_Frame,text='back',font=TEXT_FONT,command=main_menu,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Calendar_Back_Btn.place(x=1330,y=750)
L_Result_Match=tk.Label(Match_Frame,font=('arial',30),bg=MENU_BG,fg=MENU_ITEM_FG)
L_Result_Match.place(x=680,y=400)
Start_Game_Btn=tk.Button(Match_Frame,text='Start',font=TEXT_FONT,command=start_match,bg=HEADER_MENU_BG,fg=MENU_ITEM_FG)
Start_Game_Btn.place(x=700,y=700)
L_Home_Game=tk.Label(Match_Frame,font=SUBTITLE_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
L_Away_Game=tk.Label(Match_Frame,font=SUBTITLE_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
L_VS_Game=tk.Label(Match_Frame,text='VS',font=SUBTITLE_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
L_Home_Goal=tk.Label(Match_Frame,text='0',font=SUBTITLE_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
L_Away_Goal=tk.Label(Match_Frame,text='0',font=SUBTITLE_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
L_Home_Game.place(x=200,y=50)
L_VS_Game.place(x=700,y=50)
L_Away_Game.place(x=1200,y=50)
L_Home_Goal.place(x=500,y=50)
L_Away_Goal.place(x=900,y=50)

for i in range(12):
    row=[]
    for j in range(10):
        L_League_Menu=tk.Label(Menu_Frame,font=COMBO_FONT,fg=MENU_ITEM_FG,bg=MENU_BG)
        L_League_Menu.place(x=x_x,y=y_y)
        row.append(L_League_Menu)
        x_x=x_x+130
        if x_x==1350:
            x_x=50
            y_y=y_y+50
    League_Table.append(row)
for i in range(10):
    L_Subtitle_League=tk.Label(Menu_Frame,font=COMBO_FONT,fg=MENU_ITEM_FG,bg=MENU_BG)
    L_Subtitle_League.place(x=x_x,y=30)
    l.append(L_Subtitle_League)
    x_x=x_x+130
for i in range(10):
    l[i].config(text=titles[i])
for i in range(15):
    L_Player_Info=tk.Label(Player_Frame,font=TEXT_FONT,bg=MENU_BG,fg=MENU_ITEM_FG)
    L_Player_Info.place(x=x_x_x,y=y_y_y)
    Player_Info.append(L_Player_Info)
    y_y_y=y_y_y+100
    if y_y_y==730:
        x_x_x=x_x_x+300
        y_y_y=130
for i in range(8):
    Tactics_Btn=tk.Button(Tactic_Team_Frame1,font=BUTTON_FONT,text=Tactics_List[i],command=lambda tc=Tactics_List[i]:players_formation(tc))
    Tactics_Btn.place(x=x2,y=y2,width=300)
    Tactics.append(Tactics_Btn)
    y2=y2+80
check_country()
show_overall_team(Game_Player[s4.get()][Team]['starting'],Currect_Formation)
Game.mainloop()