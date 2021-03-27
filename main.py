
s = "barfoothefoobarman"
words = ["foo","bar"]



w = len(s) # lungimea sirului
n = len(words) # cate cuvinte sunt date
k = len(words[0]) # lungimea cuvintelor
d = {cuv: 0 for cuv in words}
for cuv in words:
    d[cuv] += 1
# indexam fiecare cuvant din lista si de cate ori apare
sol = []
for i in range(w - (n * k) + 1):
# parcurgem indicii din sir până ne rămâne o "permutare"
    new_dict = {cuv: 0 for cuv in words}
    # indexam din nou de cate ori apar cuv

    for l in range(n): # cate cuvinte sunt
        indice = i + l * k # trecem peste cuv pe care le-am verificat deja, daca lungimea e 3 si sunt 2 cuv initial trecem prin indice = i, apoi indice = i + 3 si ne oprim
        cuv = s[indice: indice + k] # cuv pe care il verificam
        if cuv in words: # daca exista in words
            new_dict[cuv] += 1 # indexam aparitia lui
            if new_dict[cuv] > d[cuv]: # daca am depasit nr de aparitii din words e clar ca solutia nu e buna si ne oprim
                break
        else: # daca cuvantul nu e in words solutia nu e buna
            break
    else: # daca a reusit sa treaca prin for -> permutare gasita si adaugam indicele de pe care incepe
        sol.append(i)


print(sol)