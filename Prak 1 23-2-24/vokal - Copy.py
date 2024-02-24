def menghitungVokal(string):
    jumlah_vokal = 0
    for i in string:
        if i in "aiueoAIUEO":
            jumlah_vokal += 1
    print(jumlah_vokal)


kalimat = input()
menghitungVokal(kalimat)
