"""
Group name: CAS 309
Group members:
    Nguyen Duy Nguyen Ho - S372109
    Van Tuan Khuat - S377095
    Linh Chi Doan - S364721
    Nguyen Hao Vo - S377196
GitHub repository:
    https://github.com/k3vjnh0/HIT137-SoftwareNow-Assignment-2-CAS309.git
"""

from my_modules.helper import check_input_conditions, clear_screen, get_encrypted_text
from my_modules.q1_t1_extract_text import CSVTextExtractor
from my_modules.q1_t2_research import TextProcessor
from my_modules.q1_t3_1_most_common_words import TopWordsExtractor
from my_modules.q1_t3_2_most_common_tokens import UniqueTokenCounter
from my_modules.q1_t4_named_entity_recognition import NERProcessor
from my_modules.q2_c1_gatekeeper import ImageModifier
from my_modules.q2_c2_chamber_of_strings import StringCipherProcessor
from my_modules.q3_encrypted import CaesarCipher


def main_menu():
    clear_screen()
    return input(
        "MAIN MENU\n"
        "\tSelect an option:\n"
        "1. Question 1 - Natural Language Processing (NLP) Tasks\n"
        "2. Question 2 - The Quest for the Hidden Treasure\n"
        "3. Question 3 - Fixing error-prone codes\n"
        "4. GitHub Repository\n"
        "5. Exit\n"
        "Enter your choice: "
    )


def sub_menu(title, options):
    clear_screen()
    menu_text = f"{title}\n" + "\n".join(
        [f"{idx}. {desc[0]}" for idx, desc in options.items()]
    )
    return input(f"{menu_text}\nEnter your choice: ")


class MenuManager:
    def __init__(self):
        self.main_menu_actions = {
            "1": self.handle_question_1,
            "2": self.handle_question_2,
            "3": self.handle_question_3,
            "4": self.handle_question_4,
            "5": self.exit_program,
        }

    def handle_question_1(self):
        q1_options = {
            "1": ("Task 1 - Extract Text", task1_extract_text),
            "2": ("Task 2 - Test Installed Libraries", taks2_research),
            "3": ("Task 3.1 - Count Words", task3_1_count_word),
            "4": ("Task 3.2 - Tokenize Text", task3_2_tokenize_text),
            "5": ("Task 4 - Named Entity Recognition - BioBert", task4_ner_biobert),
            "6": ("Task 4 - Named Entity Recognition - SciSpaCy", task4_ner_scispacy),
            "7": ("Return to Main Menu", None),
        }
        self.process_sub_menu("QUESTION 1 - NLP TASKS", q1_options, "7")

    def handle_question_2(self):
        q2_options = {
            "1": ("Chapter 1 - The Gatekeeper", chapter1_the_gatekeeper),
            "2": (
                "Chapter 2 - The Chamber of Strings (ASCII)",
                chapter2_the_chamber_of_strings_ascii,
            ),
            "3": ("Chapter 2 - Deciphered Cryptogram", chapter2_deciphered_cryptogram),
            "4": ("Return to Main Menu", None),
        }
        self.process_sub_menu("QUESTION 2 - THE HIDDEN TREASURE", q2_options, "4")

    def handle_question_3(self):
        fixing_error_prone_codes()

    def handle_question_4(self):
        show_github_repository()

    def process_sub_menu(self, title, options, return_option_key):
        """
        Process the submenu options.

        :param title: Title of the submenu
        :param options: A dictionary of options for the submenu
        :param return_option_key: The option key that triggers a return to the main menu
        """
        while True:
            choice = sub_menu(title, options)
            if choice in options:
                # Execute the function associated with the choice
                if (
                    choice == return_option_key
                ):  # Check if the selected option is to return to main menu
                    break  # Exit the submenu immediately and return to main menu
                else:
                    options[choice][1]()
                    if self.prompt_to_stay_in_submenu():
                        break

    def prompt_to_stay_in_submenu(self):
        """
        Prompt the user to return to the main menu or stay in the current submenu.

        :param return_option_key: The option key that triggers a return to the main menu
        """
        while True:
            choice = input("\nDo you want to return to the main menu? (y/n): ").lower()
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def exit_program(self):
        print("Exiting program.")
        exit()

    def run(self):
        while True:
            choice = main_menu()
            if choice in self.main_menu_actions:
                self.main_menu_actions[choice]()


def task1_extract_text():
    print("\nRunning Task 1: Extract 'text' from csv files")
    extractor = CSVTextExtractor(
        "./input", "./output/extracted_text.txt", ["TEXT", "SHORT-TEXT"]
    )
    extractor.extract_text_from_csv_files()


def taks2_research():
    print("\nRunning Task 2: Research")
    processor = TextProcessor()
    sample_text = "Aspirin is a medication used to reduce pain, fever, or inflammation."
    processor.process_text_with_spacy(sample_text)
    processor.tokenize_with_biobert(sample_text)


def task3_1_count_word():
    print("\nRunning Task 3.1: Count Words and Save Top 30 Words")
    extractor = TopWordsExtractor(
        "./output/extracted_text.txt", "./output/top_30_words.csv", 30
    )
    extractor.extract_top_words()


def task3_2_tokenize_text():
    print("\nRunning Task 3.2: Tokenize Text and Save Top 30 Tokens")
    token_counter = UniqueTokenCounter(
        "./output/extracted_text.txt",
        "./output/top_30_tokens.csv",
        "distilbert-base-uncased",
        30,
    )
    token_counter.count_unique_tokens()


def task4_ner_biobert():
    print("\nRunning Task 4: NER with BioBert")
    biobert_ner = NERProcessor("judithrosell/BioBERT_BC5CDR_NER_new", "biobert")
    biobert_ner.perform_ner(
        "./output/extracted_text.txt", "./output/ner_biobert_results.csv"
    )


def task4_ner_scispacy():
    print("\nRunning Task 4: NER with SciSpaCy")
    scispacy_ner = NERProcessor("en_ner_bc5cdr_md", "scispacy")
    scispacy_ner.perform_ner(
        "./output/extracted_text.txt", "./output/ner_scispacy_results.csv"
    )


def chapter1_the_gatekeeper():
    print("\nRunning Chapter 1: The Gatekeeper")
    modifer = ImageModifier("./input/chapter1.jpg", "./output/chapter1out.jpg")
    modifer.modify_image()


def chapter2_the_chamber_of_strings_ascii():
    print("\nRunning Chapter 2: The Chamber of Strings - ASCII code")
    # Example string
    sample_string = "56aAww1984sktr235270aYmn145ss785fsq31D0"
    while True:
        string = get_encrypted_text("./input/example_string.txt", sample_string)
        if len(string) < 16:
            print("The length of the string must be at least 16 characters.")
        else:
            break
    processor = StringCipherProcessor(string=string)
    processor.process_string()


def chapter2_deciphered_cryptogram():
    print("\nRunning Chapter 2: The Chamber of Strings - Deciphered Cryptogram")
    # Example ciphertext
    sample_ciphertext = """
    VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY
    NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
    URYYQBAQ QRFPNEIR ZR NG ZL ORFG ZNEVYLA ZBAEBR
    """
    ciphertext = get_encrypted_text("./input/ciphertext.txt", sample_ciphertext)
    modifier = StringCipherProcessor(ciphertext=ciphertext)
    modifier.find_key()
    key = check_input_conditions("Enter the correct key: ")
    decrypted_text = modifier.caesar_decrypt(key)
    print(f"Deciphered Cryptogram: {decrypted_text}")


def fixing_error_prone_codes():
    print("\nRunning Question 3: Fixing the error-prone codes")
    cipher = CaesarCipher()
    sample_code = """
    tybony_inevnoyr = 100
    zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

    qrs cebprff_ahzoref():
        tybony tybony_inevnoyr
        ybpny_inevnoyr = 5
        ahzoref = [1, 2, 3, 4, 5]

        juvyr ybpny_inevnoyr > 0:
            vs ybpny_inevnoyr % 2 == 0:
                ahzoref.erzbir(ybpny_inevnoyr)
            ybpny_inevnoyr -= 1

        erghea ahzoref

    zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
    erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

    qrs zbqvsl_qvpg():
        ybpny_inevnoyr = 10
        zl_qvpg['xrl4'] = ybpny_inevnoyr

    zbqvsl_qvpg(5)

    qrs hcqngr_tybony():
        tybony tybony_inevnoyr
        tybony_inevnoyr += 10

        sbe v va enatr(5):
            cevag(v)
            v += 1

        vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
            cevag("Pbaqvgvba zrg!")

        vs 5 abg va zl_qvpg:
            cevag("5 abg sbhaq va gur qvpgvbanel!")

        cevag(tybony_inevnoyr)

        cevag(zl_qvpg)
        cevag(zl_frg)
    """
    encrypted_code = get_encrypted_text("./input/encrypted_code.txt", sample_code)
    decrypted_code = cipher.decrypt(encrypted_code, cipher.key)
    print(f"Decrypted code:\n{decrypted_code}")
    input("Press Enter to return to the main menu.")


def show_github_repository():
    print("\nSource code can be found at:")
    print("https://github.com/k3vjnh0/HIT137-SoftwareNow-Assignment-2-CAS309.git")
    input("Press Enter to return to the main menu.")


if __name__ == "__main__":
    menu_manager = MenuManager()
    menu_manager.run()
