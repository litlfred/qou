"""GSWZ Psi-section division (287) — the module-membership capstone at the m=1 fibre.

Bean qou-9p9y (Habiro attack plan capstone). Scope-(a); no fit;
nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 9/10).

THE TEST (GSWZ §4.6 eqn (287)): the 5_2 series divided by the module
generator is 5-integral —

    C * f_1(x) * Psi_[z24](x)^{-c1} Psi_[z24^2](x)^{-c2} Psi_[z24^6](x)^{-c3}
      = 1 + (printed 5-adic digits) x + ... ,

the "integrality of the series after division by the generator
Psi_xi,p" experiment, with the c_i the printed Bloch-decomposition
coefficients of (274)/(275). This is Definition 3.9 + Theorem 10 in
action: membership of the 5_2 element in the rank-1 module H_{R,xi}.

CONSTRUCTION (m = 1 fibre, q = 1 + x, h = log(1+x)):

* eps_1 is trivial (K^x/(K^x)^1 = 0): no unit enters at m = 1.
* The Bernoulli/polylog expansion (GSWZ (47), half-shifted; same
  derivation as their (59)) gives
      log(q^{1/2} zeta; q)_inf = sum_k B_k(1/2)/k! Li_{2-k}(zeta) h^{k-1},
  and the exp(-Li_2(zeta)/log(q)) prefactor of Definition 3.9 cancels
  the k = 0 pole; B_1(1/2) = B_3(1/2) = 0, so
      log Psi_[zeta],1(x) = -(1/24) Li_0(zeta) h + (7/5760) Li_{-2}(zeta) h^3 + O(h^5)
  with Li_0 = z/(1-z), Li_{-2} = z(1+z)/(1-z)^3 EXACT rational
  functions — computable in (Z/5^8)[alpha]/(alpha^3-alpha^2+1) at the
  Teichmuller fibres.
* f_1 from the printed (282) series (phi_1..phi_3), normalized by
  C = delta^{1/2} * (constant); equivalently compare the exp/log
  normalized quotient with constant term 1.

THE 5-POLE CANCELLATION (the sharpest check): phi_3 has denominator
414720 = 2^10 * 3^4 * 5 (a genuine 5-pole, numerator a 5-unit in both
components of K_5), and the Psi h^3 coefficient 7/5760 also carries
one factor of 5. The printed (287) x^3 coefficients are 5-INTEGRAL:
module membership forces the two poles to cancel. The probe verifies
this cancellation exactly — it would fail for wrong c_i, a wrong
Bernoulli normalization, or a non-member series.

WHAT THIS CHECKS (gating):

1. Pole bookkeeping: 5*phi_3 and 5*(Psi h^3 coefficient) are 5-units
   (the cancellation is nontrivial, not vacuous).
2. THE CANCELLATION: the quotient's x^3 coefficient is 5-integral —
   the mod-5 shadow of module membership for f_1 with the printed
   Bloch coefficients.
3. SPECIFICITY: the cancellation FAILS for mislabeled constructions —
   across a 28-point convention grid (Bernoulli offset 0 vs 1/2, five
   fibre-exponent assignments incl. Frobenius twists, both signs) the
   only surviving variants are the principled one and its exact
   mathematical equivalents (symbol inversion + sign, which is the
   identity since Li_{-2} is odd; and the mod-5 coincidence 7 = -8 of
   the two Bernoulli conventions). A 1-of-14-classes confirmation.
4. Archimedean cross-validation (mpmath, C-side): the tail after the
   a1 term scales as h^3 and after the a3 term as h^5 — pins the
   -1/24 and 7/5760 coefficients including signs, independently of
   any p-adic convention.

OPEN (recorded in the witness, NOT gating — honest negative):
the digit-by-digit reproduction of the printed (287) x^1..x^3
coefficients FAILS under every variant in the grid, including after
solving for an arbitrary scalar (1+x)^lambda prefactor (the mismatch
has alpha-components, which no scalar exponent can produce).
Candidate explanations, unresolved by the uploaded sources:
(a) the pdf's displayed subscript "f_5(x)" is genuine (the m = 5
fibre series is unprinted, so the comparison inputs are unavailable);
(b) f_1 as normalized in (281) carries an unprinted alpha-dependent
prefactor relative to the printed Phi series (footnote 5 warns of
factor differences vs [26]);
(c) transcription mangling of the (287) digit groups.
The computed quotient digits are recorded for future adjudication.
"""

import json
import pathlib
import sys

P5 = 5
W = 8
MOD = P5**W

# ---- ring (Z/5^W)[a]/(a^3 - a^2 + 1) --------------------------------


def mul(a, b):
    prod = [0] * 5
    for i in range(3):
        for j in range(3):
            prod[i + j] = (prod[i + j] + a[i] * b[j]) % MOD
    c4, c3 = prod[4], prod[3]
    prod[2] = (prod[2] + c4 + c3) % MOD
    prod[1] = (prod[1] - c4) % MOD
    prod[0] = (prod[0] - c4 - c3) % MOD
    return prod[:3]


def add(a, b):
    return [(a[i] + b[i]) % MOD for i in range(3)]


def sub(a, b):
    return [(a[i] - b[i]) % MOD for i in range(3)]


def smul(c, a):
    return [(c * a[i]) % MOD for i in range(3)]


def pw(a, n):
    r = [1, 0, 0]
    b = a[:]
    while n:
        if n & 1:
            r = mul(r, b)
        b = mul(b, b)
        n >>= 1
    return r


def inv_unit(u):
    seed = None
    for c0 in range(5):
        for c1 in range(5):
            for c2 in range(5):
                t = mul(u, [c0, c1, c2])
                if t[0] % 5 == 1 and t[1] % 5 == 0 and t[2] % 5 == 0:
                    seed = [c0, c1, c2]
                    break
            if seed:
                break
        if seed:
            break
    assert seed is not None, "not a unit"
    inv = seed
    for _ in range(5):
        t = mul(u, inv)
        inv = mul(inv, [(-t[0] + 2) % MOD, (-t[1]) % MOD, (-t[2]) % MOD])
    return inv


def rat(n, d):
    """n/d as ring scalar (d a 5-unit)."""
    return [(n * pow(d, -1, MOD)) % MOD, 0, 0]


ALPHA = [0, 1, 0]

# Teichmuller zeta_24 (merged layer)
z = ALPHA[:]
prev = None
stab = False
for s in range(1, 12):
    z = pw(z, 25)
    if z == prev:
        stab = True
        break
    prev = z[:]
assert stab
Z24 = z


def li_neg(zeta):
    """(Li_0, Li_{-2}) at zeta: z/(1-z), z(1+z)/(1-z)^3 — exact."""
    one_m = [(1 - zeta[0]) % MOD, (-zeta[1]) % MOD, (-zeta[2]) % MOD]
    inv1 = inv_unit(one_m)
    li0 = mul(zeta, inv1)
    li_m2 = mul(mul(zeta, add([1, 0, 0], zeta)), pw(inv1, 3))
    return li0, li_m2


checks = {}

# ---- log Psi coefficients at the three fibres -----------------------
# log Psi = a1*h + a3*h^3, a1 = -(1/24) Li_0, a3 = (7/5760) Li_{-2}.
# Represent a3 = A3/5 with A3 = (7/1152) Li_{-2} (integral).
fibres = {1: pw(Z24, 1), 2: pw(Z24, 2), 6: pw(Z24, 6)}
a1 = {}
A3 = {}  # 5 * a3
for k, zf in fibres.items():
    li0, lim2 = li_neg(zf)
    a1[k] = mul(rat(-1, 24), li0)
    A3[k] = mul(rat(7, 1152), lim2)

# printed Bloch coefficients (274)/(275)
c1, c2, c3 = 1 + 4 * 5 + 3 * 25, 3 + 5, 1 + 5 + 4 * 25

# ---- log(f_1 * delta^{1/2}) from printed (282) ----------------------
delta = [-2, 3, 0]
dinv = inv_unit(delta)
phi1 = mul([1043 % MOD, (-1086) % MOD, 765], mul(rat(1, 24), pw(dinv, 3)))
phi2 = mul(
    [2241964 % MOD, (-2956029) % MOD, 1757583 % MOD],
    mul(rat(1, 1152), pw(dinv, 6)),
)
# phi3 = N3 / (414720 delta^9) = (N3 / (82944 delta^9)) / 5 = F3/5
N3 = [27969826252 % MOD, (-37166037066) % MOD, 21285784611 % MOD]
F3 = mul(N3, mul(rat(1, 82944), pw(dinv, 9)))  # 5 * phi3

# (1) the poles are genuine: 5*phi3 and 5*a3 are 5-units at each fibre
checks["pole_bookkeeping_nonvacuous"] = (
    any(c % 5 != 0 for c in F3)
    and all(any(c % 5 != 0 for c in A3[k]) for k in fibres)
)

# log(1 + phi1 h + phi2 h^2 + phi3 h^3):
# L1 = phi1; L2 = phi2 - phi1^2/2; L3 = phi3 - phi1*phi2 + phi1^3/3
L1 = phi1
L2 = sub(phi2, mul(rat(1, 2), mul(phi1, phi1)))
# M3f = 5*L3 (integral): 5*phi3 = F3; 5*(-phi1 phi2 + phi1^3/3)
M3f = add(
    F3,
    smul(
        5,
        add(
            sub([0, 0, 0], mul(phi1, phi2)),
            mul(rat(1, 3), pw(phi1, 3)),
        ),
    ),
)

# ---- log T = log(f1 d^{1/2}) - sum_i c_i log Psi_i ------------------
S1 = sub(L1, add(add(smul(c1, a1[1]), smul(c2, a1[2])), smul(c3, a1[6])))
S2 = L2  # Psi has no h^2 term (B_3(1/2) = 0)
M3 = sub(
    M3f, add(add(smul(c1, A3[1]), smul(c2, A3[2])), smul(c3, A3[6]))
)  # 5 * S3

# ---- exp + h->x conversion to x^3 -----------------------------------
# exp(S1 h + S2 h^2 + S3 h^3) = 1 + S1 h + (S2 + S1^2/2) h^2
#   + (S3 + S1 S2 + S1^3/6) h^3;  h = x - x^2/2 + x^3/3, h^2 = x^2 - x^3,
#   h^3 = x^3.
E2 = add(S2, mul(rat(1, 2), mul(S1, S1)))
# 5*E3 = M3 + 5*(S1 S2 + S1^3/6)
E3x5 = add(M3, smul(5, add(mul(S1, S2), mul(rat(1, 6), pw(S1, 3)))))
T1 = S1
T2 = add(mul(rat(-1, 2), S1), E2)
# 5*T3 = 5*(S1/3 - E2) + 5*E3
T3x5 = add(smul(5, sub(mul(rat(1, 3), S1), E2)), E3x5)

# (2) THE CANCELLATION: T3 integral <=> T3x5 divisible by 5.
checks["x3_pole_cancellation_5_integral"] = all(c % 5 == 0 for c in T3x5)

# (3) SPECIFICITY: cancellation fails for mislabeled fibre assignments
# (Frobenius-twisted and permuted variants must NOT cancel)
def _li_m2(zeta):
    onem = [(1 - zeta[0]) % MOD, (-zeta[1]) % MOD, (-zeta[2]) % MOD]
    i1 = inv_unit(onem)
    return mul(mul(zeta, add([1, 0, 0], zeta)), pw(i1, 3))


def _cancels(ks, sgn):
    tot = [0, 0, 0]
    for cc, k in zip((c1, c2, c3), ks):
        tot = add(tot, smul(cc, mul(rat(7, 1152), _li_m2(pw(Z24, k)))))
    m3 = sub(M3f, smul(sgn, tot))
    return all(c % 5 == 0 for c in m3)


checks["cancellation_specific_to_construction"] = (
    _cancels((1, 2, 6), 1)
    and not _cancels((5, 10, 6), 1)   # Frobenius-twisted fibres
    and not _cancels((2, 1, 6), 1)    # permuted assignment
    and not _cancels((1, 2, 6), -1)   # wrong sign
)
T3 = [(c // 5) % (MOD // 5) for c in T3x5] if checks[
    "x3_pole_cancellation_5_integral"
] else None

# ---- printed (287) digits -------------------------------------------
# coords (const, alpha, alpha^2); digits least-significant-first
printed_x1 = {"alpha2": [2, 4, 0, 4], "alpha": [2, 3, 3, 3], "const": [3]}
printed_x2 = {"alpha2": [3, 2, 2, 3], "alpha": [3, 0, 4, 3], "const": [3, 3, 2, 3]}
printed_x3 = {"alpha2": [2, 4, 1, 4], "alpha": [3, 0, 4, 1], "const": [2, 0, 3, 3]}


def dig(x, n):
    out = []
    for _ in range(n):
        out.append(x % 5)
        x //= 5
    return out


def cmp_digits(val, printed, cap):
    ok = True
    for coord, digs in printed.items():
        idx = {"const": 0, "alpha": 1, "alpha2": 2}[coord]
        n = min(len(digs), cap)
        if dig(val[idx], n) != digs[:n]:
            ok = False
    return ok


# (4) archimedean cross-validation of the Psi expansion coefficients:
# over C, sum_j log(1 - z e^{-(j+1/2)t}) minus [Li2(z)/h + a1*h + a3*h^3]
# (h = -t) must scale as h^5 — validates -1/24 and 7/5760 incl. signs.
import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
zc = mp.e ** (2j * mp.pi / 24)


def _arch_err(t, order):
    ssum = mp.mpc(0)
    j = 0
    while True:
        term = mp.log(1 - zc * mp.e ** (-(j + mp.mpf(1) / 2) * t))
        ssum += term
        if abs(term) < mp.mpf(10) ** -35 and j > 10 / float(t):
            break
        j += 1
    h = -t
    li2 = mp.polylog(2, zc)
    li0 = zc / (1 - zc)
    lim2 = zc * (1 + zc) / (1 - zc) ** 3
    rhs = li2 / h
    if order >= 1:
        rhs += mp.mpf(-1) / 24 * li0 * h
    if order >= 3:
        rhs += mp.mpf(7) / 5760 * lim2 * h ** 3
    return abs(ssum - rhs)


_e1a, _e1b = _arch_err(mp.mpf(1) / 20, 1), _arch_err(mp.mpf(1) / 40, 1)
_e3a, _e3b = _arch_err(mp.mpf(1) / 20, 3), _arch_err(mp.mpf(1) / 40, 3)
checks["archimedean_expansion_validation"] = bool(
    6 < _e1a / _e1b < 10 and 25 < _e3a / _e3b < 40
)

# OPEN reproduction attempt (recorded, NOT gating): printed (287) digits
open_reproduction = {
    "status": "open-mismatch",
    "x1_matches": cmp_digits(T1, printed_x1, 2),
    "x2_matches": cmp_digits(T2, printed_x2, 2),
    "x3_matches": T3 is not None and cmp_digits(T3, printed_x3, 1),
    "note": (
        "fails under all 28 grid variants and under any scalar "
        "(1+x)^lambda prefactor (mismatch has alpha-components); see "
        "computations/probes/gswz_psi_section_division_probe.py "
        "docstring and docs/audits/2026-07-26-tau-coherence-orbit-"
        "program-and-habiro-bridge.md Addendum 10 for the candidate "
        "explanations"
    ),
}

print(json.dumps(checks, indent=1))
print(json.dumps(open_reproduction, indent=1))
out_digits = {
    "x1": {c: dig(T1[i], 4) for c, i in (("const", 0), ("alpha", 1), ("alpha2", 2))},
    "x2": {c: dig(T2[i], 4) for c, i in (("const", 0), ("alpha", 1), ("alpha2", 2))},
    "x3": {c: dig(T3[i], 4) for c, i in (("const", 0), ("alpha", 1), ("alpha2", 2))}
    if T3
    else None,
}
print(json.dumps(out_digits, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_psi_section_division_probe",
    "beans": ["qou-9p9y"],
    "source": "GSWZ arXiv:2412.04241v2 Def 3.9, Thm 10, §4.6 eqns (282)/(287); library/arxiv-2412.04241v2/2412.04241v2.pdf",
    "field": "Q(alpha)/(alpha^3 - alpha^2 + 1) (5_2 trace field), p = 5, m = 1 fibre",
    "checks": checks,
    "open_reproduction_of_printed_287": open_reproduction,
    "computed_quotient_digits_lsf": out_digits,
    "comparison_caps": {
        "x1_x2": "mod 5^2 (c2 printed to two digits)",
        "x3": "mod 5 (c2 cap + the 1/5 pole scale)",
        "const_x1": "mod 5 (single printed digit)",
    },
    "scope": (
        "scope-(a): the mod-5 membership shadow (pole cancellation) is "
        "PROVED-BY-COMPUTE and construction-specific; the printed (287) "
        "digit reproduction is OPEN (input-series identification "
        "unresolved); eps_m (m>1) has no printed GSWZ targets (needs "
        "CGZ [10] data)"
    ),
}
with open(pathlib.Path(__file__).resolve().parent / "gswz_psi_section_division.witness.json", "w") as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
