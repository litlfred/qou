import mpmath as mp
mp.mp.dps = 50
q = mp.mpf("1.1099793132717013149866657930777598687799017684617")
def qbracket(k): return (q**k - q**(-k)) / (q - 1/q)
print("q-deformed L_pn factor:", 2 * qbracket(5) / qbracket(2))
print("Classical L_pn factor:", 5.0)
