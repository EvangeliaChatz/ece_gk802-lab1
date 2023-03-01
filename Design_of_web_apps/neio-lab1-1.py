
    #Εργαστηριακή άσκηση 1
#Χατζηλυγερούδη Ευαγγελία,ΑΜ:1018865
#εισαγγή βιβλοθηκών
import requests # εισαγωγή της βιβλιοθήκης 
import datetime # χρησιμοποείται στα cookies

#ΟΡΙΣΜΟΣ ΧΡΩΜΑΤΩΝ               
def COLORS2(colored_bold_text, purple_text):

    style2_background_light_green_bold = f"\x1b[48;2;238;225;239m\x1b[38;2;172;43;182m\x1b[1m{colored_bold_text}\x1b[0m"
    style3purple = f"\x1b[38;2;172;43;182m\x1b[0.5m{purple_text}\x1b[0m"
    #style4_green = f"\x1b[38;2;62;123;46m\x1b[0.5m{green_text}\x1b[0m"

    if colored_bold_text:
     return style2_background_light_green_bold
    else :
     return style3purple
 
#ΕΙΣΑΓΩΓΗ URL
def give_url():
    url = input('\n' + '\u2022\033[1mΕισάγετε ένα URL για να εμφανιστεί μέρος της HTML της σελίδας:\033[0m')
    print('Το URL είναι:', f"{COLORS2(purple_text= {}, colored_bold_text= url)}", '\n')
    return url

#ΕΚΦΩΝΗΣΗ-ΕΡΩΤΗΜΑ ΓΙΑ ΠΡΟΒΟΛΗ ΤΟΥ ΚΩΔΙΚΑ
def more(text):
    count = 0
    for line in text.split('\n'):
        print(f"{COLORS2(purple_text= line, colored_bold_text={})}")
        count += 1
        if count % 1 == 0:
            reply = input('\n' +'Θέλετε να δείτε κι άλλες γραμμές της HTML (y/n)? ')
            if reply == 'n':
                break

#ΖΗΤΗΣΗ URL
def request_to_url(url):
    with requests.get(url) as response:  # το αντικείμενο response

        #ορίζω τις μεταβλητές
        status_code = response.status_code
        reason = response.reason
        html = response.text
        keno = ' '

        print( 'O κώδικας HTML της σελίδας είναι: '+ '\n')
        more(html)
        print('\n'+ 'Ο κωδικός κατάστασης είναι:'+ f"{COLORS2(purple_text ={}, colored_bold_text = status_code)+ COLORS2(purple_text={} , colored_bold_text=reason)}" + '\n')
 
#ΚΕΦΑΛΙΔΕΣ
def show_headers(url):
    response = requests.head(url)
    print('\n'+'\033[1m\u2022Όλες οι κεφαλίδες της σελίδας είναι οι παρακάτω:\033[0m' + '\n')
    print('\n'+'\033[1m\u2022Παρακάτω παρουσιάζονται ο Server & τα Cookies της σελίδας\033[0m')
    for header, value in response.headers.items():
        print(f"{COLORS2(colored_bold_text= header, purple_text={}) + COLORS2(colored_bold_text=':', purple_text={})+COLORS2(colored_bold_text={}, purple_text=value)}")
        server_ = value
        if server_ is not None:
             
            if header == 'Server' and value is not None:
                print(response)
                print('\n' + '(α)Ο Server της σελίδας είναι: ' + f"{COLORS2(colored_bold_text= server_ , purple_text={})} " + '\n') 
            else :
                print('\n' + '\x1b[38;2;220;20;60m\x1b[1m(α)Ο server του δεν αναγνωρίζεται\x1b[0m' + '\n')#για παράδειγμα στο facebook.com

            
              

#COOKIES
def find_cookies(url):
    response = requests.get(url)
    #όταν δεν υπάρχουν cookies(π.χ. www.upatras.gr)
    if len(response.cookies) == 0:
      print(COLORS2(purple_text='Δεν υπάρχουν cookies σε αυτήν την σελίδα', colored_bold_text={}))
    else :
        print('(β,γ)Τα Cookies της σελίδας είναι τα παρακάτω:')
        for cookie in response.cookies:
            if cookie.expires is not None:
                #ορίζω τη μεταβλητή του χρονικού διαστήματος εγκυρότητας
                expiration_days = datetime.datetime.fromtimestamp(cookie.expires) - datetime.datetime.now().replace(microsecond=0)
                print(COLORS2(colored_bold_text='Το Cookie με όνομα', purple_text={}), f"{COLORS2(colored_bold_text= cookie.name, purple_text={})}", 'λήγει σε', f"{COLORS2(colored_bold_text= expiration_days, purple_text={}) }")


#MAIN
def main():
    url = ('https://'+ give_url())# Προσδιορισμός του url από το χρήστη
    print('\033[1m\u2022Πραγματοποίηση αιτήματος HTTP\033[0m')# Αίτημα HTTP στο URL
    request_to_url(url)# Ζητάει URL από το χρήστη
    show_headers(url) # Εμφανίζει τις κεφαλίδες
    find_cookies(url)# Εμφανίζει τα cookies

if __name__ == '__main__':
    main()
