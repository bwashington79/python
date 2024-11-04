acronyms = {"LOL": "laugh out loud",
            "IDK": "I don't know",
            "TBH": "to be honest"}

print(acronyms["TBH"])

acronyms["TBH"] = "updated"

print(acronyms["TBH"])

'''print(acronyms["IDD"]) crashes app'''

'''doesn't crash app'''

print(acronyms.get("IDD"))


print(1+1)