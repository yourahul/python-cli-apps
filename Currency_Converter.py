USD_TO_INR = 87.0
CNY_TO_INR = 12.15  
EUR_TO_INR = 102.35 

def usd_to_inr(usd):
    return usd * USD_TO_INR

def inr_to_usd(inr):
    return inr / USD_TO_INR

def cny_to_inr(cny):
    return cny * CNY_TO_INR

def inr_to_cny(inr):
    return inr / CNY_TO_INR

def eur_to_inr(eur):
    return eur * EUR_TO_INR

def inr_to_eur(inr):
    return inr / EUR_TO_INR

print("Currency Converter")
print("1. USD to INR")
print("2. INR to USD")
print("3. CNY to INR")
print("4. INR to CNY")
print("5. EUR to INR")
print("6. INR to EUR")

choice = input("Choose conversion (1-6): ")

try:
    if choice == '1':
        usd = float(input("Enter USD: "))
        print(usd, "USD =", usd_to_inr(usd), "INR")
    elif choice == '2':
        inr = float(input("Enter INR: "))
        print(inr, "INR =", inr_to_usd(inr), "USD")
    elif choice == '3':
        cny = float(input("Enter CNY: "))
        print(cny, "CNY =", cny_to_inr(cny), "INR")
    elif choice == '4':
        inr = float(input("Enter INR: "))
        print(inr, "INR =", inr_to_cny(inr), "CNY")
    elif choice == '5':
        eur = float(input("Enter EUR: "))
        print(eur, "EUR =", eur_to_inr(eur), "INR")
    elif choice == '6':
        inr = float(input("Enter INR: "))
        print(inr, "INR =", inr_to_eur(inr), "EUR")
    else:
        print("Invalid choice")
except ValueError:
    print("Please enter a valid number")
