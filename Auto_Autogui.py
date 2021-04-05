import pyautogui

#print(pyautogui.position())
pyautogui.hotkey('Win', 'm')
pyautogui.PAUSE = 2.5
pyautogui.hotkey('Win', 'r')
pyautogui.PAUSE = 2.5
pyautogui.typewrite("chrome.exe https://www.google.com/")
pyautogui.PAUSE = 2.5
pyautogui.click(227, 52)
pyautogui.typewrite("https://open.spotify.com/")
pyautogui.typewrite(["enter"])
pyautogui.PAUSE = 2.5
pyautogui.click(82, 219)
pyautogui.PAUSE = 2.5
pyautogui.click(422, 101)
pyautogui.typewrite("Iron Maiden")
pyautogui.typewrite(["enter"])
pyautogui.PAUSE = 2.5
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite("Álbuns")
pyautogui.click(1724, 90)
pyautogui.typewrite(["enter"])
pyautogui.PAUSE = 2.5
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite("Piece of Mind")
pyautogui.click(1724, 90)
pyautogui.typewrite(["enter"])
pyautogui.PAUSE = 2.5
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite("To tame a land")
pyautogui.click(1724, 90)
pyautogui.click(289, 516)
pyautogui.screenshot('music_spotify.png')