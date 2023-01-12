from Bot10 import Bot

lines = open('10.in').read().strip().split('\n')
compvalues = {17, 61}
bot = []
output = [[] for _ in range(30)]


lines = sorted(lines)

#print(len(lines))
#process bot lines
for line in lines:
    t = line.split(' ')
    if t[0] == 'bot':
        id = int(t[1])
        low = int(t[6])
        high = int(t[11])
        bot.append(Bot(id, t[5], t[10], low, high))

bot = sorted(bot, key = lambda x: x.Id)

#print('Number of bots:' + str(len(bot)))
# process value lines
v = 0
for line in lines:
    t = line.split(' ')
    if t[0] == 'value':
        v += 1
        val = int(t[1])
        b = int(t[5])
        bot[b].Values.append(val)

i = 0
moved = False
part1 = False
while True:
    assert len(bot[i].Values) <= 2
    if not part1 and set(bot[i].Values) == compvalues:
        print('Part 1: ' + str(i))
        part1 = True
    if len(bot[i].Values) == 2:
        moved = True
        low = min(bot[i].Values)
        high = max(bot[i].Values)
        bot[i].Values = []
        if bot[i].LowToType == 'bot':
            bot[bot[i].LowToNum].Values.append(low)
        else:
            output[bot[i].LowToNum].append(low)

        if bot[i].HighToType == 'bot':
            bot[bot[i].HighToNum].Values.append(high)
        else:
            output[bot[i].HighToNum].append(high)
    
    i = i + 1 
    if i == len(bot):
        if moved:
            i = 0
            moved = False
        else:
            break
    #i = (i + 1) % len(bot)
# for b in bot:
#     print(b, sep = '/', end = '')
# print()
for i in range(len(output)):
      print(output[i], sep = ' ', end = '')
print()

part2 = 1
for i in range(3):
    part2 *= output[i][0]
print('Part2: ' + str(part2))        
        

    


