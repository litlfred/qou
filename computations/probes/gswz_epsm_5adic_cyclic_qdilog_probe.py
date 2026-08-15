"""5-adic cyclic quantum dilogarithm at the Q_25 place — eps_m-class data for the 5_2 symbols.

Bean qou-9p9y (eps_m layer, 5-adic increment; finite-field validation
merged in PR #4490: cgz_cyclic_qdilog_unit_probe.py, Thm 7.4 gamma=2).
Scope-(a); no fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 12).

CONSTRUCTION. CGZ (arXiv:1712.04887) realize the Chern-class units via

    D_zeta(x) = prod_{k=1}^{m-1} (1 - zeta^k x)^k,
    P_zeta(X) = D_zeta(x)/D_zeta(1),  x^m = X,

well-defined mod m-th powers over the Kummer extension (their Lemma
2.4); GSWZ's eps_m (arXiv:2412.04241 eqn (16)) are the corresponding
Chern-class values, R = c^2 (CGZ Thm 7.4, verified finite-field-side
in the merged probe).

THE PLACE STRUCTURE (why Q_25, and why everything is a unit there):
K_5 = Q_25 x Q_5 splits the 5_2 trace field at p = 5. The Q_5
component has mu = mu_4 only, so P_{zeta_m} is undefined there for
m not dividing 4 — a first run on the full product ring hit exactly
this (D_zeta non-unit in the Q_5 component). The construction lives
per place; this probe works in the Q_25 component, where:
* mu(Q_25) = mu_24 contains zeta_m = omega^{24/m} for EVERY m | 24;
* Teichmuller representatives are distinct mod 5, so 1 - omega^s is
  a unit whenever 24 does not divide s;
* the symbols' roots x = omega^t (t*m = j mod 24) with j in {1,2,6}
  never produce a vanishing factor (t*m = j != 0 mod 24), so every
  D-value and P-value is a UNIT — classes are pure Teichmuller data.
* a unit's class mod m-th powers (m prime to 5) is carried entirely
  by its Teichmuller part (1 + 5Z_25 is m-divisible), so
  class(u) = dlog_omega(teich(u)) mod gcd(m, 24), exactly computable.

WHAT THIS CHECKS (exact arithmetic in the lifted quadratic component
(Z/5^8)[y]/(y^2 + p y + r), Hensel-split from alpha^3 - alpha^2 + 1):

1. Component split integrity: the Hensel-lifted linear root a and
   quadratic cofactor reproduce the cubic exactly mod 5^8, and
   omega = image of the Teichmuller zeta_24 has exact order 24 with
   pairwise-distinct-mod-5 powers.
2. Identity (21) 5-adically: (1-X)^r D(zeta^r x)/D(x) =
   prod_{k<r}(1 - zeta^k x)^m — the implementation guard (this
   identity caught a flattened pdf exponent in the finite-field run).
3. Teichmuller class extraction is total: every P-value's Teichmuller
   part lies in <omega> (dlog exists).
4. ROOT-DIFFERENCE LAW (the falsifiable theory check): for roots
   x' = zeta_m^r x of the same X, Lemma 2.4(a) gives
   P(x')/P(x) = prod_{k<r}(1-zeta^k x)^m / (1-X)^r, whose class mod
   m-th powers is -r * class(1-X) (the m-th-power factor dies). The
   probe verifies class(P(x')) - class(P(x)) = -r*class(1-X)
   mod gcd(m,24) for every root pair, every m | 24, every symbol.
   In particular per-symbol classes are root-dependent exactly when
   class(1-X) != 0 — the honest reason the eps-class of a SINGLE
   symbol is only canonical on the full Bloch combination.

OUTPUT (recorded for the harness): per (m, symbol) the class
exponents for each root choice. STRUCTURAL FINDING (honest): an m-th
root of zeta_24^j exists inside mu_24 only when gcd(m,24) | j, so at
the base place the computable pairs are j=2 (m=2) and j=6
(m in {2,3,6}); the j=1 symbol — hence the full c-weighted
xi-combination — requires the next unramified Kummer level
mu_{24m} (24m | 25^f - 1), queued as the following increment. NO
printed target exists for these 5-adic values (honest scope): they
are candidate eps_m data, falsifiable against future printed
constants (e.g. the (287) normalization C once bean qou-xx9f
resolves).
"""

import json
import math
import sys

P5 = 5
W = 8
MOD = P5**W

# ---- Hensel split of x^3 - x^2 + 1 over Z/5^W -----------------------
a = 2
for _ in range(6):
    fa = (a * a * a - a * a + 1) % MOD
    dfa = (3 * a * a - 2 * a) % MOD
    a = (a - fa * pow(dfa, -1, MOD)) % MOD
assert (a * a * a - a * a + 1) % MOD == 0
p_ = (a - 1) % MOD
r_ = (a * (a - 1)) % MOD
# consistency: -a*r = 1 mod 5^W
assert (-a * r_) % MOD == 1

# ---- quadratic component ring (Z/5^W)[y]/(y^2 + p_ y + r_) ----------


def mul2(u, v):
    a0, a1 = u
    b0, b1 = v
    c0 = a0 * b0
    c1 = a0 * b1 + a1 * b0
    c2 = a1 * b1
    # y^2 = -p_ y - r_
    return ((c0 - c2 * r_) % MOD, (c1 - c2 * p_) % MOD)


def pw2(u, n):
    r = (1, 0)
    b = u
    while n:
        if n & 1:
            r = mul2(r, b)
        b = mul2(b, b)
        n >>= 1
    return r


def inv2(u):
    seed = None
    for c0 in range(5):
        for c1 in range(5):
            t = mul2(u, (c0, c1))
            if t[0] % 5 == 1 and t[1] % 5 == 0:
                seed = (c0, c1)
                break
        if seed:
            break
    assert seed is not None, "not a unit in Q_25 component"
    inv = seed
    for _ in range(5):
        t = mul2(u, inv)
        inv = mul2(inv, ((-t[0] + 2) % MOD, (-t[1]) % MOD))
    return inv


def emb(c):
    """[c0, c1, c2] (cubic-ring element) -> quadratic component."""
    c0, c1, c2 = c
    return ((c0 - c2 * r_) % MOD, (c1 - c2 * p_) % MOD)


def one_minus2(t):
    return ((1 - t[0]) % MOD, (-t[1]) % MOD)


# ---- Teichmuller zeta_24 in the component ---------------------------
# (compute in the cubic ring as before, then embed)
def _mul3(x, y):
    prod = [0] * 5
    for i in range(3):
        for j in range(3):
            prod[i + j] = (prod[i + j] + x[i] * y[j]) % MOD
    c4, c3 = prod[4], prod[3]
    prod[2] = (prod[2] + c4 + c3) % MOD
    prod[1] = (prod[1] - c4) % MOD
    prod[0] = (prod[0] - c4 - c3) % MOD
    return prod[:3]


def _pw3(x, n):
    r = [1, 0, 0]
    b = x[:]
    while n:
        if n & 1:
            r = _mul3(r, b)
        b = _mul3(b, b)
        n >>= 1
    return r


z = [0, 1, 0]
prev = None
stab = False
for s in range(1, 12):
    z = _pw3(z, 25)
    if z == prev:
        stab = True
        break
    prev = z[:]
assert stab
OMEGA = emb(z)

checks = {}

# (1) split integrity + omega order 24, distinct mod 5
OM = [pw2(OMEGA, t) for t in range(24)]
order_ok = pw2(OMEGA, 24) == (1, 0) and all(OM[t] != (1, 0) for t in range(1, 24))
mod5_reps = {(u[0] % 5, u[1] % 5) for u in OM}
checks["component_split_and_omega_order24"] = bool(
    order_ok and len(mod5_reps) == 24
)


def teich2(u):
    v = u
    prev = None
    for s in range(1, 12):
        v = pw2(v, 25)
        if v == prev:
            return v
        prev = v
    raise AssertionError("teich2 did not stabilize")


def dlog_omega(u):
    t = teich2(u)
    for e in range(24):
        if OM[e] == t:
            return e
    return None


def dzeta2(m, x):
    step = 24 // m
    r = (1, 0)
    for k in range(1, m):
        r = mul2(r, pw2(one_minus2(mul2(OM[(step * k) % 24], x)), k))
    return r


MS = [2, 3, 4, 6, 8, 12, 24]

# (2) identity (21) in the component — multiplication-only form
# (1-X)^r D(zeta^r x) = [prod_{k<r}(1-zeta^k x)^m] * D(x); scalar sweep
# points (2, 3, 7 are not Teichmuller roots, so no factor vanishes).
ok21 = True
for m in MS:
    step = 24 // m
    for rr in range(1, min(m, 4)):
        for xa in (2, 3, 7):
            x = (xa % MOD, 0)
            X = pw2(x, m)
            lhs = mul2(
                pw2(one_minus2(X), rr),
                dzeta2(m, mul2(OM[(step * rr) % 24], x)),
            )
            rhs = dzeta2(m, x)
            for k in range(rr):
                rhs = mul2(rhs, pw2(one_minus2(mul2(OM[(step * k) % 24], x)), m))
            if lhs != rhs:
                ok21 = False
checks["identity_21_5adic_exact"] = ok21

SYMBOLS = [1, 2, 6]
C = {1: 86, 2: 8, 6: 106}

# (3)+(4): classes per (m, symbol, root) + root-difference law
all_teich_ok = True
law_ok = True
eps_classes = {}
for m in MS:
    g = math.gcd(m, 24)
    step = 24 // m
    for j in SYMBOLS:
        roots = [t for t in range(24) if (t * m) % 24 == j % 24]
        if not roots:
            continue
        X = OM[j]
        clsX = dlog_omega(one_minus2(X))
        if clsX is None:
            all_teich_ok = False
            continue
        d1inv = inv2(dzeta2(m, (1, 0)))
        per_root = {}
        for t in roots:
            e = dlog_omega(mul2(dzeta2(m, OM[t]), d1inv))
            if e is None:
                all_teich_ok = False
                continue
            per_root[t] = e % g
        # root-difference law: t' = t + step*rr  =>  e' - e = -rr*clsX mod g
        ts = sorted(per_root)
        for t in ts:
            for t2 in ts:
                if t2 == t:
                    continue
                rr = ((t2 - t) // step) % m
                if (per_root[t2] - per_root[t] - (-rr * clsX)) % g != 0:
                    law_ok = False
        eps_classes[f"m{m}_sym{j}"] = {
            "classes_per_root_t": per_root,
            "class_of_1_minus_X_mod_g": clsX % g,
            "g": g,
        }
checks["teichmuller_extraction_total"] = all_teich_ok
checks["root_difference_law"] = law_ok

# xi-combination: empty at the base place by the gcd obstruction
# (gcd(m,24) | 1 fails for every m > 1 — the j=1 symbol has no root in
# mu_24); recorded as the structural finding, next Kummer level queued.
xi_classes = {}
for m in MS:
    g = math.gcd(m, 24)
    keys = {j: f"m{m}_sym{j}" for j in SYMBOLS}
    if not all(k in eps_classes for k in keys.values()):
        continue
    tot = 0
    for j in SYMBOLS:
        pr = eps_classes[keys[j]]["classes_per_root_t"]
        tmin = min(pr)
        tot += C[j] * pr[tmin]
    xi_classes[f"m{m}"] = tot % g
assert xi_classes == {}, "gcd obstruction lifted? update the docstring"

print(json.dumps(checks, indent=1))
print(json.dumps({"xi_class_minimal_root_convention": xi_classes}, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

import subprocess

_sha = subprocess.run(
    ["git", "rev-parse", "HEAD"], capture_output=True, text=True
).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_5adic_cyclic_qdilog_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_5adic_cyclic_qdilog_probe.py",
    "commitSha": _sha,
    "beans": ["qou-9p9y"],
    "source": (
        "CGZ arXiv:1712.04887v3 eqns (8)/(20)/(21) (library/arxiv-1712.04887v3/1712.04887v3.pdf); "
        "GSWZ arXiv:2412.04241v2 eqns (16)/(275) (library/arxiv-2412.04241v2/2412.04241v2.pdf); "
        "finite-field validation: cgz_cyclic_qdilog_unit_probe.py (merged #4490)"
    ),
    "place": "Q_25 component of K_5, ring (Z/5^8)[y]/(y^2+py+r) Hensel-split",
    "checks": checks,
    "eps_class_data": eps_classes,
    "xi_class_minimal_root_convention": xi_classes,
    "scope": (
        "scope-(a): P_zeta classes of the 5_2 symbols at the Q_25 place, "
        "every m | 24, with the root-difference law verified as the "
        "falsifiable theory check; per-symbol classes are root-dependent "
        "exactly by -r*class(1-X) (honest caveat: only the full Bloch "
        "combination is canonical); no printed target exists for these "
        "values — candidate eps_m data for the harness (bean qou-xx9f "
        "gates external adjudication)"
    ),
}
with open(
    "computations/probes/gswz_epsm_5adic_cyclic_qdilog.witness.json", "w"
) as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
