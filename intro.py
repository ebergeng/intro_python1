import random
# generer ett random tall mellom 0 – 1000
rettTall = random.randint(0, 1000)


# 10 forsøk
for x in range(1,11):
    gjett = int(input("gjett ett tall mellom 0 og 1000: "))
    if gjett == rettTall:
        print("Hurra! du har gjettet rett tall")
    else:
        print("du har gjettet feil tall, prøv på nytt")
        print("du har", 10 - x, "forsøk igjenn")
    #print som sier hvor mange forsøk som er igjenn  
    # hvis rett tall, print gratulerer du har vunnet

# print du har tapt hvis alle forsøk er brukt opp