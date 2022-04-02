from mail_merge import Mail_Merge
merging = Mail_Merge()

for name in merging.names:
    merging.create_letter(name)
