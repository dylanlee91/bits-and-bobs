import shutil

shutil.copyfile('C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\preferences\STSPlayer','C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\preferences\STSPlayerbackup')

with open('C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\preferences\STSPlayer', 'r+') as f:
    savefile = []
    for i in f.read().split('\n'):
        x = i.find('SPIRITS')
        if x != -1:
            i = i.replace('0','1')
        savefile.append(i)
    savefile = '\n'.join(savefile)

with open('C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\preferences\STSPlayer', 'w') as f:
    f.write(savefile)
    f.close()
    