from Bio.SeqAnalysis.SeqDatabase import SeqDatabase

s = SeqDatabase(["F5GWV9", "A0AVL1", "A0PK19", "A1KZ92", "A2A2A0", "B5ME49", "P98088", "Q7Z5P9", "A0AVL1", "A2A2A0"]
                , "test")
record = s.get()[0:2]
same_record = s.get(["A0AVL1", "A0PK19"])
print(record == same_record)
