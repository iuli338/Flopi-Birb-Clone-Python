import json
import pygame

class Highscore:

    json_file_name = "highscore.json"
    highscore:int = 0
    font = pygame.font.Font(None, 38)
    white = (255, 255, 255)
    hscoreText = font.render("Highscore: " + str(highscore), True, white)
    hscoreTextRect = hscoreText.get_rect()
    hscoreTextRect.move_ip((800//2)-(hscoreTextRect.width // 2),(600//2)-(hscoreTextRect.height//2))

    def init():
        # Init the JSON file:
        try:
            # Open de JSON file
            with open(Highscore.json_file_name, "r") as json_file:
                data = json.load(json_file)
            
            # Read the highscore
            Highscore.highscore = data.get("highscore")
            Highscore.hscoreText = Highscore.font.render("Highscore: " + str(Highscore.highscore), True, Highscore.white)

            if Highscore.highscore is not None:
                print(f"The highscore is: {Highscore.highscore}")
            else:
                print("Highscore not found in the JSON file.")
        except FileNotFoundError:
            print(f"The JSON file '{Highscore.json_file_name}' does not exist.")
            
            # Creating the dictionary to be writen
            data = {"highscore": Highscore.highscore}
            
            # If there is no JSON file it will be created
            with open(Highscore.json_file_name, "w") as json_file:
                json.dump(data, json_file)

            print(f"Highscore {Highscore.highscore} has been saved to {Highscore.json_file_name}.")

    def UpdateHighScore(curScore:int):
        if curScore > Highscore.highscore:
            Highscore.highscore = curScore
            # Write the new highscore in the JSON
            # Creating the dictionary to be writen
            data = {"highscore": Highscore.highscore}
            
            # If there is no JSON file it will be created
            with open(Highscore.json_file_name, "w") as json_file:
                json.dump(data, json_file)

            print(f"Highscore {Highscore.highscore} has been saved to {Highscore.json_file_name}.")
            # Update the highscore text
            Highscore.hscoreText = Highscore.font.render("Highscore: " + str(Highscore.highscore), True, Highscore.white)

    def Draw(screen:pygame.Surface,isGameOver:bool):
        if isGameOver == True:
            screen.blit(Highscore.hscoreText,Highscore.hscoreTextRect)
