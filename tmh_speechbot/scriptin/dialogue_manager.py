from eliza import Eliza

eliza = Eliza()
eliza.load("tmh_speechbot/data/doctor.txt")
response = eliza.runFromApi("What is your name?")
