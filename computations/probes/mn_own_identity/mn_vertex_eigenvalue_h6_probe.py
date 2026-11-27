"""H6 eigenvalue phases of gamma-gamma words. Pre-registered 857ea510990. mpmath 30 dps."""
import json, itertools, mpmath as mp
from qou_substrate.constants import Q_50_DIGIT_STR  # proton pin, not a typed copy
mp.mp.dps = 30
N = 6
def partitions(n, m=None):
    m = m or n
    if n == 0: yield (); return
    for k in range(min(n, m), 0, -1):
        for p in partitions(n-k, k): yield (k,)+p
def syts(lam):
    out = []
    def rec(T, filled, k):
        if k > sum(lam): out.append(dict(T)); return
        for r in range(len(lam)):
            c = filled[r]
            if c < lam[r] and (r == 0 or filled[r-1] > c):
                T[k] = (r, c); filled[r] += 1; rec(T, filled, k+1); filled[r] -= 1; del T[k]
    rec({}, [0]*len(lam), 1); return out
def rep(lam, q):
    Ts = syts(lam); idx = {tuple(sorted(T.items())): i for i, T in enumerate(Ts)}
    d = len(Ts); h = q - 1/q; gens = []
    for i in range(1, N):  # sigma_{i-1} swaps entries i, i+1
        M = mp.zeros(d, d)
        for j, T in enumerate(Ts):
            (r1, c1), (r2, c2) = T[i], T[i+1]
            if r1 == r2: M[j, j] = q
            elif c1 == c2: M[j, j] = -1/q
            else:
                ax = (c2 - r2) - (c1 - r1)
                a = h/(1 - q**(-2*ax)); ap = h/(1 - q**(2*ax))
                S = dict(T); S[i], S[i+1] = T[i+1], T[i]
                k = idx[tuple(sorted(S.items()))]
                M[j, j] = a; M[k, j] = mp.sqrt(1 + a*ap)
        gens.append(M)
    return gens
def check(g, q):
    h = q - 1/q; I = mp.eye(g[0].rows); err = mp.mpf(0)
    for i, s in enumerate(g):
        err = max(err, mp.mnorm(s*s - h*s - I, 1))
        if i+1 < len(g): err = max(err, mp.mnorm(s*g[i+1]*s - g[i+1]*s*g[i+1], 1))
        for j in range(i+2, len(g)): err = max(err, mp.mnorm(s*g[j] - g[j]*s, 1))
    return err
def word(g, w):
    M = mp.eye(g[0].rows)
    for i, e in w: M = M*(g[i] if e > 0 else mp.inverse(g[i]))
    return M
V = lambda i: [(i, 1), (i+1, -1)]
WORDS = {"W1": V(0), "W2": V(0)+V(3), "W3": V(0)*3+V(3)*3, "W4": V(2)*3,
         "W5a": V(0)+V(2), "W5b": V(1)+V(3), "W6": V(0)*3+V(3)*3+V(2)*3}
def phases(M):
    if M.rows == 1: ev = [M[0, 0]]
    else:
        try: ev = mp.eig(M, left=False, right=False)
        except RuntimeError:  # repeated eigenvalues: roots of the characteristic polynomial
            n = M.rows; c = [mp.mpf(1)]; B = mp.eye(n)
            for k in range(1, n+1):  # Faddeev-LeVerrier
                AB = M*B; ck = -sum(AB[i, i] for i in range(n))/k; c.append(ck)
                B = AB + ck*mp.eye(n)
            with mp.workdps(120):
                ev = mp.polyroots(c, maxsteps=400, extraprec=400)
    return sorted(mp.mpf(mp.nstr(mp.arg(e)/(2*mp.pi), 12)) for e in ev), [mp.nstr(abs(e), 8) for e in ev]
out = {"preregistration": "857ea510990", "results": {}}
for label, q in (("q0", mp.mpf(Q_50_DIGIT_STR)), ("q~1", 1 + mp.mpf('1e-25'))):
    res = {}
    for lam in partitions(N):
        g = rep(lam, q); e = check(g, q)
        assert e < mp.mpf('1e-20'), (lam, e)
        row = {}
        for wn, w in WORDS.items():
            ph, mods = phases(word(g, w))
            row[wn] = {"phase/2pi": [mp.nstr(x, 10) for x in ph], "max|lambda|-1": mp.nstr(max(abs(mp.mpf(m)-1) for m in mods), 4)}
        res[str(lam)] = row
    out["results"][label] = res
json.dump(out, open(__file__.replace('.py', '.out.json'), 'w'), indent=1)
# compact summary: distinct phases per word
for label in out["results"]:
    print("==", label)
    for wn in WORDS:
        s = sorted({p for lam in out["results"][label] for p in out["results"][label][lam][wn]["phase/2pi"]}, key=float)
        m = max(float(out["results"][label][lam][wn]["max|lambda|-1"]) for lam in out["results"][label])
        print(wn, s, "max||λ|-1|=", m)
