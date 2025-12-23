#-------------------------------------------------------------------------Automobile management system----------------------------------------------------------------------#
#---------------------------------------------------------------------------------Welcome Page------------------------------------------------------------------------------#
#================================================================================# ARYA-MOTO #==============================================================================#
#----------------------------------------------#(Automatic Resource Yard for Automobiles – Management of Terminal Operations)#----------------------------------------------#

import pyfiglet

print("\n" * 2)
text = pyfiglet.print_figlet(text = "ARYA-MOTO", colors = "BLUE", width = 100)



RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GREY = "\033[90m"
RESET = "\033[0m"
    
def style_line(text):
    styled = ""
    for ch in text:
        if ch == "#":
            styled += MAGENTA + ch
        elif ch == "-":
            styled += GREEN + ch
        else:
            styled += YELLOW + ch
    styled += RESET
    return styled

print(style_line("#--------------------------------------------------------------------Automobile Service management system-------------------------------------------------------------------#"))
print(style_line("#---------------------------------------------------------------------------------Welcome Page------------------------------------------------------------------------------#"))
print(style_line("#================================================================================# ARYA-MOTO #==============================================================================#"))
print(style_line("#----------------------------------------------#(Automatic Resource Yard for Automobiles – Management of Terminal Operations)#----------------------------------------------#"))

#print(style_line("#--------------------------------------------------------------------------Automobile management system-----------------------------------------------------------------------#", "\n" ,"#---------------------------------------------------------------------------------Welcome Page------------------------------------------------------------------------------#", "\n" ,"#================================================================================# ARYA-MOTO #==============================================================================#", "\n" ,"#----------------------------------------------#(Automatic Resource Yard for Automobiles – Management of Terminal Operations)#----------------------------------------------#"))

print("\n" * 5)


print(style_line("........................................................................................................................................................................."))
print("\n")

print("\t" * 4 ,"Welcome to ARYA-MOTO, the Automatic Resource Yard for Automobiles – Management of Terminal Operations!")
print("\t" * 4 ,"This system is designed to streamline the management of automobile resources and terminal operations.")
print("\t" * 4 ,"Please follow the instructions provided in the system to navigate through the various functionalities.")
print("\n")
print(style_line("........................................................................................................................................................................."))

print("\n" * 2)

import shutil

def welcome_box():
    screen_width = 128

    box_width = 38  
    left_padding = (screen_width - box_width) // 2
    
    #ASCII color codes
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    GREY = "\033[90m"
    RESET = "\033[0m"

    # Color format for menu box
    border_color = CYAN
    text_color = YELLOW

    title_text = "MENU".center(box_width - 2)
    top = border_color + "╔" + "═" * (box_width - 2) + "╗" + RESET
    mid = border_color + "║" + text_color + title_text + border_color + "║" + RESET
    bot = border_color + "╚" + "═" * (box_width - 2) + "╝" + RESET

    print(" " * left_padding + top)
    print(" " * left_padding + mid)
    print(" " * left_padding + bot)

welcome_box()




print("\n"*2)

def menu_box(text):
    screen_width = 128
    RED = "\033[91m"
    RESET = "\033[0m"

    styled_text = ""  
    for ch in text:
        if ch in "12345":  
            styled_text += RED + ch + RESET  
        else:
            styled_text += ch  
    return styled_text  

def main():
    print(menu_box("[1]" + " Register a customer"))
    print(menu_box("[2]" + " Log-in "))
    print(menu_box("[3]" + " About Us"))
    print(menu_box("[4]" + " Exit"))



    opt = input(("Enter your choice: "))
    if opt == "1":
        print("You have chosen to register a customer.")
        import register
        register.main()
    elif opt == "2":
        import login
        login.main()
    elif opt == "3":
        import about_us
        about_us.main()
    elif opt == "4":
        print("Exiting the program. Thank you for using ARYA-MOTO!")
        text = pyfiglet.print_figlet(text = "THANK  YOU", colors = "BLUE", width = 100)
    else:
        print("Invalid option. Please try again.")
        main()

Choose = main()


"""//               ..,,:::;;iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii;::1ffLLLLLLLLLLL
//              ..,,::;iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii;::::iiiiiiii;ii11ttttttttt
//           .,,,:;;;;iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii:. ,:;iiiiiiiiiiiii;;;;;;;;;;
//         .,..,:;iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii:. ,t1iiiiiiiiiiiiiiiiiiiiiiiii
//            :iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii;,  ;C00L1iiiiiiiiiiiiiiiiiiiiiii
//           :iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii;,  :tG0000Gfiiiiiiiiiiiiiiiiiiiiii
// ::::::,,..;iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii:. ,tG00000000Liiiiiiiiiiiiiiiiiiiii
// ;;;;iiii::iiiiiiiiiiiiiiiiiiiii;iiiiiiiiii;.  ;C00000000000C1iiiiiiiiiiiiiiiiiii
// 11i;::;i;;iiiiiiiiiiiiiiii;;;iiii;iiiiii;,  :f0Ct11fC0000000G1;iiiiiiii;;;;i:;ii
// 11111i;:;iiiiiiiiiiiiiiiiiiiiiiii:;iii;,  ,tG00i,. .,iL000000L,:iii;;;;itLCf:ii;
// 1111111i:;iiiiiiiiiiiiiiiiiiii;;iii;:,..,:t0000t,    .:L0000C;,,;;;ifCG88@@L:;;:
// 11111111i;iiiiiiiiiiiiiiiiiiiiiii;;;:::;ii;f000Gt:.. .:f000L;,::;tG8@@@@88Gt:;;i
// 11111111i;iiiiiiiiiiiiiiiiiiiiiii,.:,::;;ii;f0000Cft1tLG0Gf::,,iC8@@8@80CC0C;iii
// 11111111;;iiiiiiiiiiiiiiiiiiii;,.  :;;:;:;ii;1C00000000GLi::,iC8@88@80CG8@@81;;i
// 1111iii;;iiiiiiiiiiiiiiiiiii;,  ..:iiii;:;iii;itCGGGCLti;:::f8@888@8CC8@@@@@8L1i
// 1111;;;;;;;;iiiiiiiiiiiiii;.  .iLCt;;ii;;iiiiii;;i;:::,:::;L8@888@0L0@@@@@@@@8Gf
// 1111111i;;:;iiiiiiiiiiii;,  .1C0000Gt;;iiiiiiiiiii;:;;;;;;G@8888@GC8@@@@@@@8GG08
// 111111i;;;;:iiiiiiiiiii:.  :LGLLLCG00C1;;iiiiiiiiiiiiii;iG@888@@CC@@@@@@@0CG8@@@
// i1111111111;;iiiiiiiii:  .1GL;,..,iL000Li;iiiiiiiiiiii;i0@888@@0C@@@@@@8CC8@@@@@
// .,;i11111111;;iiiiiii:  ;L001,    .:f000Gi:iiiiiiiii;;;C@8888@@@@@@@@8GC8@@@@@@@
//    .,:;iiiii;:;iiiii:  iGG00L:.    .;G000L,;iiii;::::::C8@@8@@@@@@@@0C0@@@@@@@@@
//         ..... .:iiii: .tGGG00L1;,..,iGGGGf.:;iii;,..,. .:f88@@@@@@@CC8@@@@@@@@@@
//                 :iii;.:;tGGGG00GCLffCGGGL:,:iiii;..f0i    L@@@@@@@@8@@@@@88@@@@@
//                  ,:ii;ii;1LGGGGG00GGGGGf;::;ii;;, ;8t.    f@@@@@@@@@@@@@@@8@@@@@
//                    ,;iiiii;1LGGGGGGGGLi,:;:;i1tfi .:      C@@@@@@@@@8GLC8@@@@@@@
//                     .:iiiii;i1fLCCCCt:,:;;:1C08@0i:::::;;i0@@@@@@@0LiiG@@@@@@@@@
//                       ,;iiiiii;iii;:,:;;;;t8@@8@@@88888@@@@@8088G1::f8@@@@@@@@@@
//                        .:iiiiiiii;;;;iii;f8@@@@@@@@@@@@@@@@@@8Gi,,t08G0@@@@@@@@@
//                          ,;iiiiiiiiiiii;i8@80GG@@@@@@@@@@@@@@8t:1G80G88888@@@@@@
//                           .:iiiiiiiiiii;180CC0@@@@@@@@@@@@@@@CL08008@@888@@@@@@@
//                             :iiiiiiiiii;;CG88@@@@@8GG0@@@@@@@@@@@@@888@@@@@@@@@@
//                             ,iiiiiiii;:::0@@8@@8GGG0@@@@@@888@@@@@@@@@@@@@@@@@@@
"""