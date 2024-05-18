# !/usr/bin/env python3

# -*- coding: utf-8 -*-

# library import
from rich.console import Console
from pyfiglet import figlet_format
from termcolor import colored
from time import sleep 
from instainfo import instainfo
from iplook import iplook
from clear import clear
from numscan import numscan
from ketik import ketik
from ip import ip
from cipher import cyb

cyan = ("\033[1m\033[36m")
mawar = ("\033[31;1m")
white = ("\033[37m")
console = Console()
def virus():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = colored('''                             .-""""-.
                           / j      
                          :.d;       ;
                          $$P        :
               .m._       $$         :
              dSMMSSSss.__$$b.    __ :
             :MMSMMSSSMMMSS$$$b  $$P ;
             SMMMSMMSMMMSSS$$$$     :b
            dSMMMSMMMMMMSSMM$$$b.dP SSb.
           dSMMMMMMMMMMSSMMPT$$=-. /TSSSS.
          :SMMMSMMMMMMMSMMP  `$b_.'  MMMMSS.
          SMMMMMSMMMMMMMMM \  .'\    :SMMMSSS.
         dSMSSMMMSMMMMMMMM  \/\_/; .'SSMMMMSSSm 
        dSMMMMSMMSMMMMMMMM    :.;'" :SSMMMMSSMM;
      .MMSSSSSMSSMMMMMMMM;    :.;   MMSMMMMSMMM;
     dMSSMMSSSSSSSMMMMMMM;    ;.;   MMMMMMMSMMM
    :MMMSSSSMMMSSP^TMMMMM     ;.;   MMMMMMMMMMM
    MMMSMMMMSSSSP   `MMMM     ;.;   :MMMMMMMMM;
    "TMMMMMMMMMM      TM;    :`.:    MMMMMMMMM;
       )MMMMMMM;     _/\\    :`.:    :MMMMMMMM
      d$SS$$$MMMb.  |._\\\   :`.:     MMMMMMMM
      T$$S$$$$$$$$$$m;O\\\\"-;`.:_.-  MMMMMMM;
     :$$$$$$$$$$$$$$$b_l./\\ ;`.:    mMMSSMMM;
     :$$$$$$$$$$$$$$$$$$$./\\;`.:  .$$MSMMMMMM
      $$$$$$$$$$$$$$$$$$$$. \\`.:.$$$$SMSSSMMM;
      $$$$$$$$$$$$$$$$$$$$$. \\.:$$$$$SSMMMMMMM
      :$$$$$$$$$$$$$$$$$$$$$.//.:$$$$SSSSSSSMM;
      :$$$$$$$$$$$$$$$$$$$$$$.`.:$$SSSSSSSMMMP
       $$$$$$$$$;"^$J "^$$$$;.`.$$P  `SSSMMMM
       :$$$$$$$$$       :$$$;.`.P'..   TMMM$$b
       :$$$$$$$$$;      $$$$;.`/ c^'   d$$$$$S;
       $$$$$S$$$$;      '^^^:_d$g:___.$$$$$$SSS
       $$$$SS$$$$;            $$$$$$$$$$$$$$SSS;
      :$$$SSSS$$$$            : $$$$$$$$$$$$$SSS
      :$P"TSSSS$$$            ; $$$$$$$$$$$$$SSS;
      j    `SSSSS$           :  :$$$$$$$$$$$$$SS$
     :       "^S^'           :   $$$$$$$$$$$$$S$;
     ;.____.-;"               "--^$$$$$$$$$$$$$P
     '-....-"  bug                  ""^^T$$$$P"
                                                ''' , 'red')

    for N, line in enumerate( x.split( "\n" ) ):
        print(line)
        sleep( 0.05 )
    ketik(colored("===    Welcome To 6Virus Tool V1    ===" , 'red' , attrs=['reverse', 'blink']))
    print(" ")
    ketik(colored("=== insta : @1zsb , github: @6virus ===" ,'green' , attrs=['reverse', 'blink']))
    print(" ")
    console.print("[bold green]|\| [1] Cipher , [2] Host IP , [3] IP Lookup  |\|[/bold green]")
    console.print("[bold green]|/| [4] insta-info , [5] NumScan , [3] Here  |/|[/bold green]")
    console.print("[bold green]|\| [1] Here , [2] Here , [3] Here  |\|[/bold green]" , end="\n\n")
    
    r00t = input(colored("root@6Virus:~$ " , 'green'))
    if r00t == '1':
        cyb()
    elif r00t == '2':
        ip()
    elif r00t == '3':
        iplook()
    elif r00t == '4':
       instainfo()
    elif r00t == '5':
        numscan()
virus()
