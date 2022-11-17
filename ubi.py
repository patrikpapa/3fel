halmaz1 = {'egy', 'kettő', 'három'}
halmaz1.clear()
halmaz2 = {"négy","öt","hat"}
halmaz3 = halmaz2.copy()
print(halmaz3)
halmaz4 = {"hét","nyolc","kilenc"}
halmaz5 = {"tíz","tizenegy","tizenkettő"}
halmaz4.difference(halmaz5)
print(halmaz4)
halmaz6 = {"tizenhárom","tizennégy","tizenőt"}
halmaz7 = {"16","17","18"}
halmaz6.update(halmaz7)
print(halmaz6)
halmaz8 = {"19","20","21"}
halmaz9 = {"22","23","24"}
halmaz8.intersection(halmaz9)
print(halmaz8)
halmaz10 = {"25","26","27"}
halmaz11 = {"28","29","30"}
halmaz10.intersection_update(halmaz11)
print(halmaz10)
halmaz12 = {"31","32","33"}
halmaz13 = {"34","35","36"}
print(halmaz12.isdisjoint(halmaz13))
halmaz14 = {"37","38","39"}
halmaz15 = {"40","41","42"}
print(halmaz14.issubset(halmaz15)," Van-e benne ez a halmaz egy másikba?")
halmaz16 = {"43","44","45"}
halmaz17 = {"46","47","48"}
print(halmaz16.issuperset(halmaz17)," Van-e egy másik halmaz ebben a halmazban?")
halmaz18 = {"49","50","51"}
halmaz19 = {"52","53","54"}
print(halmaz18.symmetric_difference(halmaz19)," Visszaaad egy halmazt kulonbséggel.")
halmaz20 = {"55","56","57"}
halmaz21 = {"58","59","60"}
print(halmaz20.pop())
print(halmaz21.add("61"))
print(halmaz20.union(halmaz21))