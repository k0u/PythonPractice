cinema = "star wars: the force awakens "

titles = cinema.split(":")
title = titles[0].upper().center(60)
sub_title = titles[1].strip().title().center(60)

print(title)
print(sub_title)