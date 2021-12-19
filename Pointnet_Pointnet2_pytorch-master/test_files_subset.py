import os
categories = ["airplane","bathtub","bed","bench","bookshelf","bottle","bowl","car","chair","cone","cup","curtain","desk","door","dresser","flower_pot","glass_box","guitar","keyboard","lamp","laptop","mantel","monitor","night_stand","person","piano","plant","radio","range_hood","sink","sofa","stairs","stool","table","tent","toilet","tv_stand","vase","wardrobe","xbox"]
os.system("touch data/modelnet40_normal_resampled/test_size10.txt")
print(len(categories))
for c in categories:
    cmd = f"ls data/modelnet40_normal_resampled/{c}/ | tail -10 | sed -e 's/\.txt$//' >> data/modelnet40_normal_resampled/test_size10.txt"
    #print(cmd)
    os.system(cmd)