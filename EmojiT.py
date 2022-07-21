print("""
    ______                  _   _ ____
   / ____/___ ___  ____    (_) ( )_____)
  / __/ / __ `__ \/ __ \  / / / / /   
 / /___/ / / / / / /_/ / / / / / /    
/_____/_/ /_/ /_/\____/_/ / /_/_/     
                     /___/            
""")
print("The easiest way to make EmojiCoder prgrams (even though it defeats the point)")
print("by github/whyisthesheep; EmojiCoder by github/SarahNathanson")
print("")
print("What would you like your program to do\n]> 1: Print a string\n]> (more options soon)")
option = input("]> ")
if option == "1":
    text = input("str (no number support yet): ")
    for letter in text:
      textb = bin(int(str(ord(letter))))
      output = textb.replace("b", "")
      output = output.replace("0", "🌚")
      output = output.replace("1", "🌝")
      print("👋🔡" + output)
input("")
