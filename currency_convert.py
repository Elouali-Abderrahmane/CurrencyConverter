import os, time
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

dollar = """   ||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================| ELOUALI RESERVE NOTE |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| ELOUALI RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||"""


convert = {
    "USD": 1.0,
    "EUR": 0.85,
    "EGP": 30.9,
    "RMB": 6.5,
}

def display_currency():
    for key, value in convert.items():
        print(f"{key}: {value}")


def convert_from_to():
    clear_screen()
    print(dollar)
    display_currency()
    convert_from = input("Choose a currency to convert from: ").strip().upper()
    while True:
        amount_convert_from = float(input("Enter the amount: "))
        if input(f"You entered {amount_convert_from:.1f} {convert_from}. Confirm? (Y/N): ").strip().lower() in ["yes", "y"]:
            break

    clear_screen()

    display_currency()

    convert_to = input("Choose a currency to convert to: ").strip().upper()

    print("Analyzing your request ...Please wait")
    time.sleep(1)
    print(f"Checking for {convert_to}'s best rates available .....Please wait")
    time.sleep(1)
    print(f"Getting a discount price for {convert_to}.....Please wait")
    time.sleep(1)
    if (convert_to in convert and convert_from in convert):
        amout_convert_to = (amount_convert_from * convert[convert_to]) / convert[convert_from]
        clear_screen()
        print(f"Preparing the deal from {convert_from} to {convert_to} .....Please wait")
        time.sleep(1)
        print(f"Exchange Rate: 1 {convert_from} = {convert[convert_to] / convert[convert_from]} {convert_to}")
        time.sleep(0.25)
        print(f"{amount_convert_from} {convert_from} is equal to {amout_convert_to: .2f} {convert_to}")
        if input("Do you accept this transaction? (Y/N): ").strip().lower() in ["yes", "y"]:
            print("Transaction Successful!")
        else:
            print("Transaction Canceled.")
    else:
        print(f"Invalid currency. Conversion canceled")


    if (input("Do you want to perform another conversion? (Y/N): ").strip().lower() in ["yes", "y"]):
        convert_from_to()
    else:
        print("Thanks for using the currency converter!")


convert_from_to()