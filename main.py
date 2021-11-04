import time

print(" ___  _                                        _  _        _              ")
print("| _ \| |_   ___  _ _   ___        ___ _ __ __ (_)| |_  __ | |_   ___  _ _ ")
print("|  _/|   \ / _ \| ' \ / -_)      (_-/ \ V  V /| ||  _|/ _||   \ / -_)| '_|")
print("|_|  |_||_|\___/|_||_|\___|      /__/  \_/\_/ |_| \__|\__||_||_|\___||_|  ")

time.sleep(0.5)
print("")
print("Initializing...")
time.sleep(1)
print("")
print("Hello and welcome to the ultimate phone switcher!")

currentphone = input("Which phone are you currently using? iPhone or Android? >>> ")
currentphone = currentphone.lower()

def iphonecall():
  time.sleep(0.5)
  print("Perfect. Let's see the choices.")
  time.sleep(1)
  budget = input("Do you want an advanced, a mid-range or a budget phone? >>> ")
  budget == budget.lower()

  if budget == "advanced":
    print("Great! I would suggest the all-new iPhone 13 Pro.")
    print("Have fun with your new phone!")
  elif budget == "mid-range":
    print("Nice! I would suggest the all-new iPhone 13.")
    print("Have fun with your new phone!")
  elif budget == "budget":
    iphonecoolcam = input("Do you need a really good camera? >>> ")
    iphonecoolcam == iphonecoolcam.lower

    if iphonecoolcam == "yes":
      print("Nice! I would suggest the all-new iPhone 13.")

    else:
      print("Okay. I would suggest the 2020 2nd-gen iPhone SE.")

    print("Have fun with your new phone!")

def androidcall():
  time.sleep(1)
  budget = input("Do you want an advanced, a mid-range or a budget phone? >>> ")
  budget == budget.lower()

  g_or_s = input("Would you prefer a Google or Samsung phone? >>> ")
  g_or_s == g_or_s.lower()

  def andbrandchooser(x):
    time.sleep(0.75)
    print("I would suggest the " + x + ".")

  def coolcam():
    outst_cam = input("Do you need an outstanding camera? >>> ")
    outst_cam == outst_cam.lower

    if outst_cam == "yes":
      andbrandchooser("all-new Google Pixel 6 Pro")
    
    else:
      andbrandchooser("all-new Google Pixel 6")

  if budget == "advanced":
    if g_or_s == "google":
      coolcam()
    elif g_or_s == "samsung":
      andbrandchooser("all-new Samsung Galaxy S21 Ultra")
    else:
      coolcam()

    print("Have fun with your new phone!")
  elif budget == "mid-range":
    if g_or_s == "google":
      coolcam()
    elif g_or_s == "samsung":
      andbrandchooser("new Samsung Galaxy S21")
    else:
      coolcam()

    print("Have fun with your new phone!")
  elif budget == "budget":
    if g_or_s == "google":
      goodcam = input("Do you need a good camera? >>> ")
      goodcam == goodcam.lower

      if goodcam == "yes":
        andbrandchooser("new Google Pixel 5a")
      else:
        andbrandchooser("2020 Google Pixel 4a with 5G")

    elif g_or_s == "samsung":
      andbrandchooser("2020 Samsung Galaxy S20")

    else:
      goodcam = input("Do you need a good camera? >>> ")
      goodcam == goodcam.lower

      if goodcam == "yes":
        andbrandchooser("new Google Pixel 5a")
      else:
        andbrandchooser("Google Pixel 4a with 5G")

    print("Have fun with your new phone!")


if currentphone == "iphone":
  print("Okay! Great!")
  switch_iphone = input("Would you like to continue with a new iPhone or switch to Android? >>> ")
  switch_iphone == switch_iphone.lower

  time.sleep(0.5)

  if switch_iphone == "switch":
    print("Okay. Let's look at the Android options available.")
    androidcall()

  elif switch_iphone == "continue":
    iphonecall()

  else:
    print("Please re-run and enter either 'switch' or 'continue'.")

elif currentphone == "android":
  print("Good choice!")
  switch_android = input("Would you like to continue with a new Android phone or switch to iPhone? >>> ")
  switch_android == switch_android.lower

  time.sleep(0.5)

  if switch_android == "switch":
    iphonecall()

  elif switch_android == "continue":
    androidcall()

  else:
    print("Please re-run and enter either 'switch' or 'continue'.")

else:
  print("Sorry, this program was only designed for Android and Apple phones.")
  print("Please re-run and enter either 'iphone' or 'android'.")