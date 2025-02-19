CARD_TYPES = ["Mastercard", "Visa", "American Express", "Discover", "UnionPay", "JCB", "Diners Club", "Maestro"]
                            CARD_CATEGORIES = ["Standard", "Premium", "Gold", "Platinum", "Business", "Corporate", "Student/School Card", "Travel Card", "Digital Card"]
                            
                            CARD_BENEFITS = {
                                "Standard": "Basic banking services with no extra benefits.",
                                "Premium": "Includes cashback rewards and lower fees.",
                                "Gold": "Higher withdrawal limits and travel insurance.",
                                "Platinum": "Exclusive airport lounge access and concierge service.",
                                "Business": "Designed for business expenses with accounting tools.",
                                "Corporate": "For large companies with employee spending limits.",
                                "Student/School Card": "Lower fees, discounts on educational services.",
                                "Travel Card": "No foreign transaction fees, better exchange rates.",
                                "Digital Card": "Virtual card for online transactions with extra security."
                            }
                            
                            def get_user_input(prompt):
                                while True:
                                    value = input(prompt).strip()
                                    if value:
                                        return value
                                    print("❌ Error: The field cannot be empty!")

                            def get_numeric_input(prompt, min_val, max_val):
                                while True:
                                    value = input(prompt).strip()
                                    if value.isdigit() and min_val <= int(value) <= max_val:
                                        return int(value)
                                    print(f"❌ Error: Please enter a number between {min_val} and {max_val}!")

                            def choose_option(options, title):
                                print(f"\n📌 Choose {title}:")
                                for i, option in enumerate(options, start=1):
                                    print(f"{i}. {option}")
                            
                                return options[get_numeric_input("👉 Enter the number: ", 1, len(options)) - 1]

                            def generate_card_number():
                                return "".join(str(random.randint(0, 9)) for _ in range(16))

                            def save_to_csv(data, filename="cards.csv"):
                                file_exists = os.path.isfile(filename)
                                with open(filename, mode="a", newline="", encoding="utf-8") as file:
                                    writer = csv.writer(file)
                                    if not file_exists:
                                        writer.writerow(["First Name", "Last Name", "Age", "Card Type", "Category", "Card Number", "Expiration", "Benefits"])
                                    writer.writerow(data)

                            def main():
                                print("\n💳 Welcome to the Card Registration System! 💳\n")

                                first_name = get_user_input("👤 Enter your first name: ")
                                last_name = get_user_input("👤 Enter your last name: ")
                                age = get_numeric_input("🔢 Enter your age (10-100): ", 10, 100)

                                card_type = choose_option(CARD_TYPES, "Card Type")
                                card_category = choose_option(CARD_CATEGORIES, "Card Category")
                                
                                expiration_month = get_numeric_input("📆 Enter expiration month (1-12): ", 1, 12)
                                expiration_year = get_numeric_input("📆 Enter expiration year (2025-2035): ", 2025, 2035)
                                expiration_date = f"{str(expiration_month).zfill(2)}/{expiration_year}"

                                card_number = generate_card_number()

                                card_benefits = CARD_BENEFITS.get(card_category, "No additional benefits.")

                                save_to_csv([first_name, last_name, age, card_type, card_category, card_number, expiration_date, card_benefits])

                                print("\n✅ Card Successfully Created! ✅")
                                print("=" * 40)
                                print(f"👤 Cardholder: {first_name} {last_name} ({age} years old)")
                                print(f"💳 Card Type: {card_type}")
                                print(f"🏷️ Category: {card_category}")
                                print(f"🔢 Card Number: {card_number}")
                                print(f"📆 Expiration Date: {expiration_date}")
                                print(f"🎁 Benefits: {card_benefits}")
                                print("=" * 40)
                                print("\n📂 Data has been saved in cards.csv!")

                            if __name__ == "__main__":
                                main()