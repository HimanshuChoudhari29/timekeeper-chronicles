import time
import os
import sys

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03):
    """Print text with typing effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_banner(title):
    """Print a beautiful banner for each scene."""
    width = 60
    print("\n" + "=" * width)
    print(f"{title:^{width}}")
    print("=" * width)

def print_scene_banner(scene_name):
    """Print scene-specific banner."""
    banner = f"""
    ╔══════════════════════════════════════════════════════╗
    ║                    {scene_name:^36}                  ║
    ╚══════════════════════════════════════════════════════╝
    """
    print(banner)

class TimekeeperChronicles:
    def __init__(self):
        self.player_name = ""
        self.inventory = []
        self.health = 100
        self.knowledge = 0
        self.courage = 0
        self.compassion = 0
        self.chapter = 1
        self.ending = ""
        
        # Chapter progress tracking
        self.chapter1_complete = False
        self.chapter2_complete = False
        self.chapter3_complete = False
        
        # Key decisions
        self.saved_owl = False
        self.helped_robot = False
        self.found_artifact = False
        self.understood_truth = False
    
    def start_game(self):
        """Start the game from the very beginning."""
        clear_screen()
        self.print_welcome()
        
        # Start with main menu
        while True:
            choice = self.show_main_menu()
            
            if choice == "1":
                self.play_full_game()
                break
            elif choice == "2":
                self.show_instructions()
            elif choice == "3":
                self.exit_game()
                break
    
    def print_welcome(self):
        """Print welcome message."""
        print_banner("TIMEKEEPER CHRONICLES")
        print("\n" + "~" * 60)
        print("      AN EPIC TEXT ADVENTURE WITH MULTIPLE CHAPTERS")
        print("                    AND ENDINGS")
        print("~" * 60)
        time.sleep(1)
    
    def show_main_menu(self):
        """Show main menu and get choice."""
        print("\n" + "-" * 60)
        print("MAIN MENU")
        print("-" * 60)
        print("1. Start New Adventure")
        print("2. Game Instructions")
        print("3. Exit Game")
        
        return self.get_valid_input("\nEnter your choice (1-3): ", ["1", "2", "3"])
    
    def get_valid_input(self, prompt, valid_choices):
        """Get valid input from user."""
        while True:
            user_input = input(prompt).strip()
            if user_input in valid_choices:
                return user_input
            else:
                type_text(f"Please enter one of: {', '.join(valid_choices)}")
    
    def show_instructions(self):
        """Show game instructions."""
        clear_screen()
        print_banner("HOW TO PLAY")
        print("\n🌟 STORY OVERVIEW:")
        print("  You are a Timekeeper, destined to restore balance")
        print("  across three chapters of adventure.")
        
        print("\n🎮 GAME FEATURES:")
        print("  • 3 Chapters with multiple scenes each")
        print("  • 6 Different endings based on your choices")
        print("  • Inventory system with collectible items")
        print("  • Character stats that affect gameplay")
        print("  • Beautiful scene banners")
        
        print("\n📊 CHARACTER STATS:")
        print("  Health: Affects survival in dangerous situations")
        print("  Knowledge: Unlocks intelligent choices")
        print("  Courage: Allows brave actions")
        print("  Compassion: Opens kind-hearted options")
        
        print("\n🎯 TIPS:")
        print("  • Explore everything")
        print("  • Talk to characters")
        print("  • Be kind when possible")
        print("  • Your choices truly matter!")
        
        input("\nPress Enter to return to main menu...")
        clear_screen()
    
    def exit_game(self):
        """Exit the game."""
        clear_screen()
        print_banner("THANK YOU FOR PLAYING!")
        type_text("\nMay your adventures always be epic!")
        time.sleep(2)
        sys.exit()
    
    # ==================== CHAPTER 1: THE AWAKENING ====================
    
    def chapter_1_intro(self):
        """Chapter 1 introduction."""
        clear_screen()
        print_banner("CHAPTER 1: THE AWAKENING")
        time.sleep(1)
        
        type_text(f"\n{self.player_name}, you awaken in a strange chamber.")
        type_text("Ancient machinery hums around you. Dust particles float")
        type_text("in beams of colored light. A voice echoes in your mind:")
        type_text("\n'You are the last Timekeeper. The Chrono-Core is failing.'")
        type_text("'Balance must be restored. Begin your journey...'")
        
        input("\nPress Enter to continue...")
        self.scene_1_1()
    
    def scene_1_1(self):
        """Scene 1.1: The Awakening Chamber."""
        clear_screen()
        print_scene_banner("THE AWAKENING CHAMBER")
        
        type_text("\nYou stand in a circular chamber with three archways.")
        type_text("Each glows with a different color:")
        type_text("1. BLUE archway - Hums with mechanical energy")
        type_text("2. GREEN archway - Smells of fresh earth and growth")
        type_text("3. RED archway - Flickers with unstable energy")
        type_text("\nOn a pedestal before you lies a CRYSTAL CHRONICLE.")
        
        while True:
            print("\n" + "─" * 50)
            print("What will you do?")
            print("1. Take the Crystal Chronicle")
            print("2. Enter the BLUE archway")
            print("3. Enter the GREEN archway")
            print("4. Enter the RED archway")
            print("5. Examine the chamber walls")
            
            choice = self.get_valid_input("\nChoice (1-5): ", ["1", "2", "3", "4", "5"])
            
            if choice == "1":
                if "Crystal Chronicle" not in self.inventory:
                    type_text("\nYou take the CRYSTAL CHRONICLE.")
                    type_text("It glows warmly in your hand, showing glimpses of time.")
                    self.inventory.append("Crystal Chronicle")
                    self.knowledge += 10
                else:
                    type_text("\nYou already have the Chronicle.")
            
            elif choice == "2":
                type_text("\nYou enter the blue archway...")
                time.sleep(1)
                return self.scene_1_2_mechanical()
            
            elif choice == "3":
                type_text("\nYou enter the green archway...")
                time.sleep(1)
                return self.scene_1_2_garden()
            
            elif choice == "4":
                type_text("\nYou enter the red archway...")
                time.sleep(1)
                return self.scene_1_2_volcanic()
            
            elif choice == "5":
                type_text("\nThe walls show murals of Timekeepers past.")
                type_text("They maintained balance between Order, Growth, and Chaos.")
                type_text("The last mural shows the Chrono-Core cracking.")
    
    def scene_1_2_mechanical(self):
        """Scene 1.2: Mechanical Labyrinth."""
        clear_screen()
        print_scene_banner("MECHANICAL LABYRINTH")
        
        type_text("\nYou enter a maze of moving gears and clockwork.")
        type_text("A mechanical owl is trapped under a fallen gear!")
        type_text("Its eyes flicker weakly. Nearby, a CONTROL PANEL glows.")
        
        while True:
            print("\n" + "─" * 50)
            print("What will you do?")
            print("1. Free the mechanical owl")
            print("2. Examine the control panel")
            print("3. Search for tools")
            print("4. Return to the chamber")
            
            choice = self.get_valid_input("\nChoice (1-4): ", ["1", "2", "3", "4"])
            
            if choice == "1":
                type_text("\nYou struggle to lift the heavy gear.")
                if self.courage >= 20:
                    type_text("Your courage gives you strength! The owl is freed!")
                    type_text("It hoots gratefully and gives you a GEAR KEY.")
                    self.saved_owl = True
                    self.inventory.append("Gear Key")
                    self.compassion += 15
                else:
                    type_text("The gear is too heavy. You need more courage.")
                    self.health -= 10
            
            elif choice == "2":
                if "Crystal Chronicle" in self.inventory:
                    type_text("\nThe Chronicle activates the panel!")
                    type_text("You learn about the Chrono-Core's three aspects.")
                    self.knowledge += 10
                else:
                    type_text("\nThe panel shows strange symbols you don't understand.")
            
            elif choice == "3":
                type_text("\nYou find an OIL CAN among the machinery.")
                if "Oil Can" not in self.inventory:
                    self.inventory.append("Oil Can")
                    type_text("This might be useful for stuck mechanisms.")
            
            elif choice == "4":
                type_text("\nYou return to the main chamber.")
                time.sleep(1)
                return "complete_chapter1"
    
    def scene_1_2_garden(self):
        """Scene 1.2: Eternal Garden."""
        clear_screen()
        print_scene_banner("ETERNAL GARDEN")
        
        type_text("\nYou enter a garden frozen in perpetual bloom.")
        type_text("A crystal tree at the center has one dying branch.")
        type_text("A small fox with clockwork patterns watches you.")
        
        while True:
            print("\n" + "─" * 50)
            print("What will you do?")
            print("1. Examine the crystal tree")
            print("2. Approach the clockwork fox")
            print("3. Collect a glowing flower")
            print("4. Return to the chamber")
            
            choice = self.get_valid_input("\nChoice (1-4): ", ["1", "2", "3", "4"])
            
            if choice == "1":
                type_text("\nThe tree's sap is time itself.")
                type_text("The dying branch represents fading memories.")
                if "Oil Can" in self.inventory:
                    type_text("\nYou use the oil can on the branch.")
                    type_text("The branch revives slightly! Time sap drips into a vial.")
                    self.inventory.append("Time Sap Vial")
                    self.compassion += 10
            
            elif choice == "2":
                type_text("\nThe fox approaches cautiously.")
                if self.compassion >= 10:
                    type_text("It trusts you! The fox leads you to a hidden SPRING.")
                    type_text("Drinking from it restores your health!")
                    self.health = min(100, self.health + 30)
                else:
                    type_text("The fox runs away. You need to show more compassion.")
            
            elif choice == "3":
                type_text("\nYou collect a LUMINA BLOSSOM.")
                if "Lumina Blossom" not in self.inventory:
                    self.inventory.append("Lumina Blossom")
                    type_text("It glows with soft, comforting light.")
            
            elif choice == "4":
                type_text("\nYou return to the main chamber.")
                time.sleep(1)
                return "complete_chapter1"
    
    def scene_1_2_volcanic(self):
        """Scene 1.2: Volcanic Forge."""
        clear_screen()
        print_scene_banner("VOLCANIC FORGE")
        
        type_text("\nYou enter a chamber of molten metal and roaring fires.")
        type_text("A forge at the center holds an unfinished artifact.")
        type_text("The heat is intense! (-20 health if you stay too long)")
        
        self.health -= 20
        
        while True:
            print("\n" + "─" * 50)
            print(f"Health: {self.health}/100")
            print("\nWhat will you do?")
            print("1. Examine the unfinished artifact")
            print("2. Try to work the forge")
            print("3. Search for cooling mechanisms")
            print("4. Return to the chamber (quickly!)")
            
            choice = self.get_valid_input("\nChoice (1-4): ", ["1", "2", "3", "4"])
            
            if choice == "1":
                type_text("\nThe artifact is a TIME HAMMER, powerful but incomplete.")
                type_text("It could repair broken time streams.")
                self.found_artifact = True
            
            elif choice == "2":
                if self.courage >= 30:
                    type_text("\nYou brave the heat and complete the hammer!")
                    type_text("You gain the TEMPORAL HAMMER!")
                    self.inventory.append("Temporal Hammer")
                    self.courage += 20
                else:
                    type_text("\nThe heat is too much! You need more courage.")
                    self.health -= 10
            
            elif choice == "3":
                type_text("\nYou find COOLING RUNES etched in the walls.")
                type_text("Understanding them could help withstand heat.")
                self.knowledge += 15
            
            elif choice == "4":
                type_text("\nYou retreat from the intense heat.")
                time.sleep(1)
                return "complete_chapter1"
    
    def complete_chapter_1(self):
        """Complete Chapter 1 and move to Chapter 2."""
        clear_screen()
        print_banner("CHAPTER 1 COMPLETE!")
        
        type_text("\nA portal swirls into existence before you.")
        type_text("The voice returns: 'You have taken your first steps.'")
        type_text("'Now, journey to the Chrono-Core. Restore balance...'")
        
        self.chapter1_complete = True
        self.chapter = 2
        
        # Stat bonuses based on choices
        if self.saved_owl:
            type_text("\nThe mechanical owl hoots encouragement.")
            self.courage += 5
        
        type_text("\n\nChapter 1 Statistics:")
        print(f"  Health: {self.health}/100")
        print(f"  Knowledge: {self.knowledge}")
        print(f"  Courage: {self.courage}")
        print(f"  Compassion: {self.compassion}")
        print(f"  Inventory: {', '.join(self.inventory)}")
        
        input("\nPress Enter to continue to Chapter 2...")
        self.chapter_2_intro()
    
    # ==================== CHAPTER 2: THE CHRONO-CORE ====================
    
    def chapter_2_intro(self):
        """Chapter 2 introduction."""
        clear_screen()
        print_banner("CHAPTER 2: HEART OF TIME")
        time.sleep(1)
        
        type_text("\nYou emerge in the Core Chamber.")
        type_text("The CHRONO-CORE floats at the center - a magnificent")
        type_text("crystal sphere with three fractured sections.")
        type_text("\nEach fracture pulses with different energy:")
        type_text("• MECHANICAL fracture (blue) - Gears grinding")
        type_text("• ORGANIC fracture (green) - Roots withering")
        type_text("• ELEMENTAL fracture (red) - Energy arcing")
        
        input("\nPress Enter to continue...")
        self.scene_2_1()
    
    def scene_2_1(self):
        """Scene 2.1: Core Chamber."""
        clear_screen()
        print_scene_banner("CORE CHAMBER")
        
        type_text("\nThree paths lead to the fractures. A console displays:")
        type_text("'Chrono-Core Stability: 42% - CRITICAL'")
        type_text("\nA damaged but conscious robot lies nearby.")
        
        while True:
            print("\n" + "─" * 50)
            print(f"Core Stability: 42%")
            print("\nWhat will you do?")
            print("1. Approach the MECHANICAL fracture (blue)")
            print("2. Approach the ORGANIC fracture (green)")
            print("3. Approach the ELEMENTAL fracture (red)")
            print("4. Check the damaged robot")
            print("5. Use the main console")
            
            choice = self.get_valid_input("\nChoice (1-5): ", ["1", "2", "3", "4", "5"])
            
            if choice == "1":
                return self.scene_2_2_mechanical()
            
            elif choice == "2":
                return self.scene_2_2_organic()
            
            elif choice == "3":
                return self.scene_2_2_elemental()
            
            elif choice == "4":
                type_text("\nThe robot sparks weakly: 'Core... failing...'")
                type_text("'Three keys... needed... for restoration...'")
                if self.helped_robot == False:
                    type_text("\nWill you try to repair it? (yes/no)")
                    repair = input("> ").lower()
                    if repair in ['yes', 'y']:
                        if "Oil Can" in self.inventory or "Gear Key" in self.inventory:
                            type_text("\nYou repair the robot! It gives you a CORE SCHEMATIC.")
                            self.inventory.append("Core Schematic")
                            self.helped_robot = True
                            self.compassion += 20
                        else:
                            type_text("\nYou lack the tools to repair it properly.")
            
            elif choice == "5":
                if "Crystal Chronicle" in self.inventory:
                    type_text("\nThe Chronicle interfaces with the console.")
                    type_text("You learn: All three fractures must be healed simultaneously.")
                    self.understood_truth = True
                    self.knowledge += 25
                else:
                    type_text("\nThe console shows complex time equations.")
    
    def scene_2_2_mechanical(self):
        """Scene 2.2: Mechanical Fracture."""
        clear_screen()
        print_scene_banner("MECHANICAL FRACTURE")
        
        type_text("\nGears grind painfully against each other.")
        type_text("A massive mainspring is overwound and cracking.")
        
        while True:
            print("\n" + "─" * 50)
            print("What will you do?")
            print("1. Try to release the spring tension")
            print("2. Lubricate the grinding gears")
            print("3. Align the misaligned cogs")
            print("4. Return to main chamber")
            
            choice = self.get_valid_input("\nChoice (1-4): ", ["1", "2", "3", "4"])
            
            if choice == "1":
                if "Temporal Hammer" in self.inventory:
                    type_text("\nYou use the hammer to safely release tension!")
                    type_text("The mechanical fracture begins healing!")
                    self.inventory.append("Mechanical Key")
                    return "repair_progress"
                else:
                    type_text("\nToo dangerous without proper tools!")
                    self.health -= 15
            
            elif choice == "2":
                if "Oil Can" in self.inventory:
                    type_text("\nYou oil the gears! They move smoothly again.")
                    type_text("Progress made on mechanical repair.")
                    self.knowledge += 10
            
            elif choice == "3":
                if "Gear Key" in self.inventory:
                    type_text("\nThe Gear Key fits perfectly! Cogs realign.")
                    type_text("The fracture stabilizes significantly.")
                    self.courage += 15
            
            elif choice == "4":
                type_text("\nYou return to the main chamber.")
                time.sleep(1)
                return "core_chamber"
    
    def scene_2_2_organic(self):
        """Scene 2.2: Organic Fracture."""
        clear_screen()
        print_scene_banner("ORGANIC FRACTURE")
        
        type_text("\Vines of crystallized time are withering.")
        type_text("The life energy here is fading rapidly.")
        
        while True:
            print("\n" + "─" * 50)
            print("What will you do?")
            print("1. Water the withering vines")
            print("2. Prune the dead growth")
            print("3. Sing to the crystals (requires compassion)")
            print("4. Return to main chamber")
            
            choice = self.get_valid_input("\nChoice (1-4): ", ["1", "2", "3", "4"])
            
            if choice == "1":
                if "Time Sap Vial" in self.inventory:
                    type_text("\nThe Time Sap revitalizes the vines!")
                    type_text("New growth appears immediately.")
                    self.inventory.append("Organic Key")
                    return "repair_progress"
                else:
                    type_text("\nYou have nothing that would help.")
            
            elif choice == "2":
                type_text("\nYou carefully prune dead sections.")
                type_text("Healthy growth has more room now.")
                self.compassion += 10
            
            elif choice == "3":
                if self.compassion >= 30:
                    type_text("\nYour kind song resonates with the crystals!")
                    type_text("They pulse with renewed life energy.")
                    self.health += 20
            
            elif choice == "4":
                type_text("\nYou return to the main chamber.")
                time.sleep(1)
                return "core_chamber"
    
    def scene_2_2_elemental(self):
        """Scene 2.2: Elemental Fracture."""
        clear_screen()
        print_scene_banner("ELEMENTAL FRACTURE")
        
        type_text("\nRaw temporal energy arcs dangerously.")
        type_text("Reality itself seems unstable here.")
        
        while True:
            print("\n" + "─" * 50)
            print("What will you do?")
            print("1. Try to contain the energy")
            print("2. Ground the electrical arcs")
            print("3. Channel the energy safely")
            print("4. Return to main chamber")
            
            choice = self.get_valid_input("\nChoice (1-4): ", ["1", "2", "3", "4"])
            
            if choice == "1":
                if "Lumina Blossom" in self.inventory:
                    type_text("\nThe blossom absorbs excess energy!")
                    type_text("The fracture stabilizes.")
                    self.inventory.append("Elemental Key")
                    return "repair_progress"
                else:
                    type_text("\nThe energy is too wild to contain!")
                    self.health -= 25
            
            elif choice == "2":
                if self.knowledge >= 40:
                    type_text("\nYour knowledge lets you ground the energy safely.")
                    type_text("The arcing reduces significantly.")
                    self.knowledge += 10
            
            elif choice == "3":
                if self.courage >= 50:
                    type_text("\nYou bravely channel the energy!")
                    type_text("It flows smoothly instead of arcing.")
                    self.courage += 20
            
            elif choice == "4":
                type_text("\nYou retreat from the unstable area.")
                time.sleep(1)
                return "core_chamber"
    
    def complete_chapter_2(self):
        """Complete Chapter 2 and move to Chapter 3."""
        clear_screen()
        print_banner("CHAPTER 2 COMPLETE!")
        
        # Count how many fractures were healed
        keys_collected = sum(1 for key in ["Mechanical Key", "Organic Key", "Elemental Key"] 
                           if key in self.inventory)
        
        type_text(f"\nYou have collected {keys_collected}/3 fracture keys.")
        
        if keys_collected == 3:
            type_text("\nALL FRACTURES HEALED! The Chrono-Core stabilizes at 85%.")
            type_text("A final challenge awaits at the Core Nexus...")
            self.chapter2_complete = True
            self.chapter = 3
        elif keys_collected >= 1:
            type_text(f"\nPartial success. The Core stabilizes at {45 + keys_collected * 15}%.")
            type_text("You can proceed, but the final challenge will be harder.")
            self.chapter2_complete = True
            self.chapter = 3
        else:
            type_text("\nYou failed to heal any fractures.")
            type_text("The Core destabilizes completely!")
            return "bad_ending_early"
        
        type_text("\n\nChapter 2 Statistics:")
        print(f"  Health: {self.health}/100")
        print(f"  Knowledge: {self.knowledge}")
        print(f"  Courage: {self.courage}")
        print(f"  Compassion: {self.compassion}")
        print(f"  Keys Collected: {keys_collected}/3")
        
        input("\nPress Enter to continue to Chapter 3...")
        self.chapter_3_intro()
    
    # ==================== CHAPTER 3: FINAL CONVERGENCE ====================
    
    def chapter_3_intro(self):
        """Chapter 3 introduction."""
        clear_screen()
        print_banner("CHAPTER 3: FINAL CONVERGENCE")
        time.sleep(1)
        
        type_text("\nYou stand at the NEXUS OF TIME.")
        type_text("Past, present, and future swirl around you.")
        type_text("The voice speaks clearly now:")
        type_text("'Timekeeper, you have come far. Now make your choice.'")
        type_text("'Three paths lie before you, each with consequences...'")
        
        input("\nPress Enter to face the final choice...")
        self.scene_3_final()
    
    def scene_3_final(self):
        """Final scene with multiple ending choices."""
        clear_screen()
        print_scene_banner("NEXUS OF TIME")
        
        type_text("\nThree portals shimmer before you:")
        type_text("1. PORTAL OF ORDER - Perfect stability, no change")
        type_text("2. PORTAL OF BALANCE - Harmony with both order and change")
        type_text("3. PORTAL OF EVOLUTION - Constant change, unpredictable")
        
        type_text("\nThe Chrono-Core awaits your decision.")
        type_text("Your actions throughout the journey will affect the outcome...")
        
        while True:
            print("\n" + "─" * 50)
            print("FINAL CHOICE:")
            print("1. Enter Portal of ORDER")
            print("2. Enter Portal of BALANCE")
            print("3. Enter Portal of EVOLUTION")
            print("4. Make your OWN choice (requires high stats)")
            
            choice = self.get_valid_input("\nYour final decision (1-4): ", ["1", "2", "3", "4"])
            
            if choice == "1":
                return self.ending_order()
            
            elif choice == "2":
                return self.ending_balance()
            
            elif choice == "3":
                return self.ending_evolution()
            
            elif choice == "4":
                if self.knowledge >= 70 and self.courage >= 70 and self.compassion >= 70:
                    return self.ending_true_timekeeper()
                else:
                    type_text("\nYou lack the wisdom, courage, or compassion")
                    type_text("to forge your own path. Choose another option.")
    
    # ==================== ENDINGS ====================
    
    def ending_order(self):
        """Order Ending."""
        clear_screen()
        print_banner("ENDING: THE PERFECT CLOCK")
        
        type_text(f"\n{self.player_name}, you choose perfect order.")
        type_text("\nTime becomes a precise, unchanging mechanism.")
        type_text("Every moment is predictable, safe, and eternal.")
        type_text("\nBut in removing all uncertainty...")
        type_text("...you also remove choice, growth, and surprise.")
        type_text("\nThe world becomes a beautiful, frozen clock.")
        type_text("And you its eternal, lonely keeper.")
        
        self.ending = "ORDER ENDING: The Perfect Clock"
        return "game_over"
    
    def ending_balance(self):
        """Balance Ending - Best ending."""
        clear_screen()
        print_banner("ENDING: HARMONY RESTORED")
        
        type_text(f"\n{self.player_name}, you choose balance!")
        type_text("\nThe Chrono-Core harmonizes order and change.")
        type_text("Time flows naturally, with both stability and growth.")
        
        # Check for best ending conditions
        if (self.saved_owl and self.helped_robot and 
            self.found_artifact and self.understood_truth):
            type_text("\nBecause of your compassion and wisdom throughout,")
            type_text("you achieve PERFECT HARMONY!")
            type_text("\nThe Chrono-Core sings with joy. All beings thrive.")
            type_text("You become the greatest Timekeeper in history.")
            self.ending = "PERFECT ENDING: Master Timekeeper"
        else:
            type_text("\nBalance is restored, though imperfectly.")
            type_text("The world continues, better than before.")
            type_text("You have done well, Timekeeper.")
            self.ending = "GOOD ENDING: Harmony Restored"
        
        return "game_over"
    
    def ending_evolution(self):
        """Evolution Ending."""
        clear_screen()
        print_banner("ENDING: RIVER OF CHANGE")
        
        type_text(f"\n{self.player_name}, you choose constant evolution.")
        type_text("\nTime becomes a rushing river of change.")
        type_text("Innovation flourishes! Discoveries abound!")
        
        if self.knowledge >= 60:
            type_text("\nYour wisdom guides the changes wisely.")
            type_text("Civilization advances rapidly but safely.")
            type_text("A golden age of discovery begins!")
            self.ending = "EVOLUTION ENDING: Guided Progress"
        else:
            type_text("\nWithout guidance, change becomes chaos.")
            type_text("The future is exciting but dangerous.")
            type_text("Only time will tell if this was wise...")
            self.ending = "CHAOTIC ENDING: Unchecked Evolution"
        
        return "game_over"
    
    def ending_true_timekeeper(self):
        """True Timekeeper Ending - Secret best ending."""
        clear_screen()
        print_banner("ENDING: THE TRUE TIMEKEEPER")
        
        type_text(f"\n{self.player_name}, you forge a FOURTH PATH!")
        type_text("\nYou realize time needs neither control nor freedom.")
        type_text("It simply IS. You become one with time itself.")
        type_text("\nYou are everywhere and everywhen.")
        type_text("Guiding subtly, helping gently, existing eternally.")
        type_text("\nThis was the true purpose of a Timekeeper.")
        type_text("Not to control time... but to understand it.")
        
        self.ending = "TRUE ENDING: Becomes Time Itself"
        return "game_over"
    
    def bad_ending_early(self):
        """Bad ending if player fails in Chapter 2."""
        clear_screen()
        print_banner("ENDING: TIME'S COLLAPSE")
        
        type_text(f"\n{self.player_name}, you have failed.")
        type_text("\nThe Chrono-Core shatters completely.")
        type_text("Time unravels like a frayed rope.")
        type_text("\nMoments scatter, memories fade,")
        type_text("and existence itself begins to unwrite.")
        type_text("\nAll because you couldn't heal the fractures.")
        
        self.ending = "BAD ENDING: Time's Collapse"
        return "game_over"
    
    def play_full_game(self):
        """Play the complete game with all chapters."""
        # Get player name
        clear_screen()
        type_text("What is your name, destined Timekeeper? ")
        self.player_name = input("> ").strip()
        if not self.player_name:
            self.player_name = "Timekeeper"
        
        # Start Chapter 1
        self.chapter_1_intro()
        
        # Handle Chapter 1 completion
        result = "complete_chapter1"
        
        if result == "complete_chapter1":
            self.complete_chapter_1()
        
        # Chapter 2 gameplay loop
        current_scene = "core_chamber"
        repairs_complete = 0
        
        while current_scene != "chapter2_complete":
            if current_scene == "core_chamber":
                result = self.scene_2_1()
                current_scene = result
            
            elif current_scene == "repair_progress":
                repairs_complete += 1
                type_text(f"\n✓ Fracture repaired! ({repairs_complete}/3)")
                if repairs_complete >= 3:
                    current_scene = "chapter2_complete"
                else:
                    current_scene = "core_chamber"
            
            elif current_scene in ["mechanical_fracture", "organic_fracture", "elemental_fracture"]:
                # These should return to core_chamber or repair_progress
                pass
        
        # Complete Chapter 2
        self.complete_chapter_2()
        
        # Final choice and ending
        final_result = self.scene_3_final()
        
        if final_result == "game_over":
            self.show_final_stats()
    
    def show_final_stats(self):
        """Show final game statistics."""
        clear_screen()
        print_banner("ADVENTURE COMPLETE")
        
        print("\n" + "=" * 60)
        print(f"HERO: {self.player_name}")
        print(f"ENDING: {self.ending}")
        print("=" * 60)
        
        print("\n📊 FINAL STATISTICS:")
        print(f"  Health: {self.health}/100")
        print(f"  Knowledge: {self.knowledge}/100")
        print(f"  Courage: {self.courage}/100")
        print(f"  Compassion: {self.compassion}/100")
        
        print("\n🎒 INVENTORY:")
        if self.inventory:
            for item in self.inventory:
                print(f"  • {item}")
        else:
            print("  (Empty)")
        
        print("\n🌟 ACHIEVEMENTS:")
        achievements = []
        if self.saved_owl: achievements.append("Saved the Mechanical Owl")
        if self.helped_robot: achievements.append("Repaired the Core Robot")
        if self.found_artifact: achievements.append("Found the Temporal Artifact")
        if self.understood_truth: achievements.append("Understood the Core Truth")
        
        if achievements:
            for ach in achievements:
                print(f"  ✓ {ach}")
        else:
            print("  (No major achievements)")
        
        print("\n" + "=" * 60)
        
        # Ask to play again
        print("\nWould you like to:")
        print("1. Play Again (Try for different ending)")
        print("2. Return to Main Menu")
        print("3. Exit Game")
        
        choice = self.get_valid_input("\nChoice (1-3): ", ["1", "2", "3"])
        
        if choice == "1":
            # Reset game
            self.__init__()
            self.play_full_game()
        elif choice == "2":
            self.start_game()
        else:
            self.exit_game()

def main():
    """Main function to run the game."""
    game = TimekeeperChronicles()
    game.start_game()

# Start the game
if __name__ == "__main__":
    main()