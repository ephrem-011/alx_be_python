dogs=(1301543.971331596)
p2p_fee=0.009
pts_per_25k_dogs=20
fee=p2p_fee*dogs
tot_pts=0
count=0
usdt_count=0
column=0
while(dogs>=25228):
    column+=1
    dogs = dogs - fee
    usdt_count+=dogs*0.0005365
    increment=int((dogs/25000))*pts_per_25k_dogs
    tot_pts+=increment
    count+=1
    print (column,"---",increment,"pts for",dogs,"dogs. And usdt count is",usdt_count )
print ("Total points is", tot_pts)
print (usdt_count)
print("Count is", count)