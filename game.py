import random

try:
    with open("balance.txt","r") as f:
        balance = int(f.read())
except:
    with open("balance.txt","w") as f:
        f.write("100")
        balance = 100


    print("---[ ANIMAL vs YOU ]----")
    print("\nYou have creadited 💲100 BALANCE")

# Function to save data
def save_data():
    with open("balance.txt","w") as f:
        f.write(str(balance))

while True:
    print("\n1. FIGHT⚔️\n2. BALANCE💵\n3. QUIT🔴")
    try:
        choice = int(input("\nEnter your choice: "))
    except:
        print("⚠️  ERROR-001: Please enter a number")
        continue

    if choice == 1:

        while True:
            print("\n ANIMALS LIST ⬇\n\n1. 🟡 Ant (99% | 💲10)\n2. 🟠 Rabbit (60% | 💲100)\n3. 🔴 Dog (30% | 💲500)\n4. 🟣 Lion (15% | 💲1000)\n5. ⚫ Elephant (7% | 💲2000)\n\n6. ← Back")
        
            try:
                choice = int(input("\nEnter your choice: "))
            except:
                print("⚠️  ERROR-002: Invalid Choice")
                continue

            if choice == 1:
                if balance >= 10:
                    win = False

                    if random.randint(1,100) > 1:
                        win = True
                        print("\nYou win the battel with ANT 🟢+20💲")
                        balance += 20
                        save_data()
                    else:
                        print("\nYou lose the battel with ANT 🔴-10💲")
                        balance -= 10
                        save_data()
                else:
                    required = 10 - balance
                    print(f"\nLow balance: {balance}💲 required {required}💲 more")

            elif choice == 2:
                if balance >= 100:
                    win = False

                    if random.randint(1,100) > 30:
                        win = True
                        print("\nYou win the battel with RABBIT 🟢+250💲")
                        balance += 250
                        save_data()
                    else:
                        print("\nYou lose the battel with RABBIT 🔴-100💲")
                        balance -= 100
                        save_data()
                else:
                    required = 100 - balance
                    print(f"\nLow balance: {balance}💲 required {required}💲 more")

            elif choice == 3:
                if balance >= 500:
                    win = False

                    if random.randint(1,100) > 70:
                        win = True
                        print("\nYou win the battel with DOG 🟢+2000💲")
                        balance += 2000
                        save_data()
                    else:
                        print("\nYou lose the battel with DOG 🔴-500💲")
                        balance -= 500
                        save_data()
                else:
                    required = 500 - balance
                    print(f"\nLow balance: {balance}💲 required {required}💲 more")

            elif choice == 4:
                if balance >= 1000:
                    win = False

                    if random.randint(1,100) > 85:
                        win = True
                        print("\nYou win the battel with LION 🟢+5000💲")
                        balance += 5000
                        save_data()
                    else:
                        print("\nYou lose the battel with LION 🔴-1000💲")
                        balance -= 1000
                        save_data()
                else:
                    required = 1000 - balance
                    print(f"\nLow balance: {balance}💲 required {required}💲 more")

            elif choice == 5:
                if balance >= 5000:
                    win = False

                    if random.randint(1,100) > 93:
                        win = True
                        print("\nYou win the battel with ELEPHANT 🟢+15000💲")
                        balance += 15000
                        save_data()
                    else:
                        print("\nYou lose the battel with ELEPHANT 🔴-5000💲")
                        balance -= 5000
                        save_data()
                else:
                    required = 5000 - balance
                    print(f"\nLow balance: {balance}💲 required {required}💲 more")
                    
            elif choice == 6:
                break

            else:
                print("⚠️  ERROR-003: Invalid Choice")

    elif choice == 2:
        print(f"\nBALANCE: 💲{balance}")

    elif choice == 3:
        print("\nExiting......")
        break
    
    else:
        print("⚠️  ERROR-004: Invalid Choice")
        continue
