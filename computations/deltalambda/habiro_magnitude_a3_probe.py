import mpmath as mp
mp.mp.dps = 50

# Substrate q0 — muon-canonical computations/ layer value (per Vassiliev audit)
q0 = mp.mpf('1.10997859555733471')
h0 = q0 - 1/q0
print(f"q0 = {q0}")
print(f"h0 = q0 - 1/q0 = {h0}")
print(f"q0 > 1: {q0 > 1}")

# Targets
mu3 = mp.mpf('0.4708')     # AdditiveResidualSimplex #4320
c3  = mp.mpf('0.297')      # BorromeanMagnitudeLift #4364 (H9 lift)
rstar = mu3/c3
print(f"\nmu3 = {mu3}, c3 = {c3}")
print(f"r* = mu3/c3 = {rstar}")
print(f"log2(3) = {mp.log(3)/mp.log(2)}  (numerology coincidence)")

# ---- (1) Habiro/cyclotomic Pochhammer growth at q0 > 1 ----
# (q;q)_n = prod_{k=1}^n (1 - q^k)
def poch(q, n):
    p = mp.mpf(1)
    for k in range(1, n+1):
        p *= (1 - q**k)
    return p

print("\n--- (q;q)_n magnitude at q0>1 (Habiro basis) ---")
prev = mp.mpf(1)
for n in [0,1,2,3,4,5,8,12,20,40]:
    v = poch(q0, n)
    r = abs(v)/prev if n>0 else mp.mpf(1)
    print(f"n={n:3d}  |(q;q)_n| = {mp.nstr(abs(v),8):>16}   ratio_to_prev={mp.nstr(r,6) if n>0 else '-'}")
    if n>0: prev=abs(v)
print("=> magnitude grows without bound for q0>1: cyclotomic completion series DIVERGES")
print("   unless coeffs a_n decay like 1/(q;q)_n (which finite-type/integer Habiro coeffs do NOT)")

# ---- (2) Quantum-integer near-misses to r* (to show any match is a FIT-scan) ----
def qint(n, q):  # [n]_q = (q^n - q^-n)/(q - q^-1)
    return (q**n - q**(-n))/(q - q**(-1))

print("\n--- quantum-integer ratios near r*=1.585 (scan = would be a FIT) ---")
qs = {n: qint(n,q0) for n in range(1,8)}
cands = []
for a in range(1,8):
    for b in range(1,8):
        r = qs[a]/qs[b]
        cands.append((abs(r-rstar), f"[{a}]_q/[{b}]_q", r))
        r2 = qs[a]/2
        cands.append((abs(r2-rstar), f"[{a}]_q/2", r2))
for d,name,val in sorted(cands, key=lambda t: t[0])[:8]:
    print(f"  {name:14s} = {mp.nstr(val,7):>10}   |diff to r*| = {mp.nstr(d,5)}")

# ---- (3) The deficit itself: proved Borromean 3-body closed form ----
# 1 - tau_Borr(h) = h^4 (3 + h^2)/(h^2 + 4)
def borrDeficit(h):
    return h**4 * (3 + h**2) / (h**2 + 4)
defval = borrDeficit(h0)
lead = mp.mpf(3)/4 * h0**4
print(f"\n--- Borromean deficit at q0 (the Hecke Markov value that gives c3) ---")
print(f"1 - tau_Borr(q0) = {mp.nstr(defval,10)}")
print(f"leading (3/4)h^4 = {mp.nstr(lead,10)}")
print(f"weight/Hecke = {mp.nstr(lead/defval,8)} (<=1, per Vassiliev audit)")
print(f"Hecke/weight = {mp.nstr(defval/lead,8)} (+{mp.nstr((defval/lead-1)*100,4)}%)  << needs +{mp.nstr((rstar-1)*100,4)}%")

# ---- (4) alpha_EM-shape finite element [k]_q*(1 - h^2 X): can 0-fit reach r*? ----
print(f"\n--- alpha_EM-shape [k]_q*(1 - h^2 * X) at q0, X from categorical data (0-fit) ---")
Xcands = {
  "X=deficit":  defval,
  "X=lead(3/4)h^4": lead,
  "X=1(bare)": mp.mpf(1),
}
for k in range(1,4):
    kq = qint(k,q0)
    for xn, xv in Xcands.items():
        val = kq*(1 - h0**2 * xv)
        print(f"  [{k}]_q*(1 - h^2*{xn:16s}) = {mp.nstr(val,8):>10}   vs r*={mp.nstr(rstar,6)}  diff={mp.nstr(val-rstar,4)}")
