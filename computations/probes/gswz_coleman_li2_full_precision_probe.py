"""Full-precision Coleman Li2 at Teichmuller points — Besser-de Jeu layer for the GSWZ harness.

Bean qou-9p9y (T3 of the Habiro attack plan) — THE previously-missing
ingredient, now available: Besser-de Jeu, "Li(p)-service? An algorithm
for computing p-adic polylogarithms", Math. Comp. 77 (2008) 1105-1134
(library/s0025-5718-07-02027-3/S0025-5718-07-02027-3.pdf), supplemented by Besser,
"Finite and p-adic polylogarithms" (library/arxiv-math-0006051v1/0006051v1.pdf) and
Besser-de Jeu arXiv:0707.3682 (library/arxiv-0707.3682v2/0707.3682v2.pdf).
Scope-(a); no fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 8).

THE ALGORITHM (Besser-de Jeu Props 4.2/4.3, precision from Prop 6.1):

1. Prop 4.3: Li^(p)_n(z) = g_n(1/(1-z)) with g_n in Q[[v]] determined by
       g_0(v) = v - 1 - (v-1)^p / (v^p - (v-1)^p),
       g'_{n+1}(v) = -g_n(v)/(v - v^2),   g_n(0) = 0.
   The coefficients a_{n,k} are p-INTEGRAL (proof of Prop 6.1) with
       v_p(a_{n,k}) >= k/(p-1) - log_p(k) - c(n,p),
   c(2,5) ~ 4.06, so ~60 terms give mod-5^6 exactness at |v| = 1;
   we take N = 120 terms (tail valuation > 20).

2. Prop 4.2 (telescoped Frobenius): for zeta != 1 a (p^f - 1)-th root
   of unity,
       Li_n(zeta) = (p^{nf}-1)^{-1} sum_{r=0}^{f-1} p^{n(f-r)} Li^(p)_n(zeta^{p^r}).
   Here p = 5, f = 2 (25 = 1 mod 24, so zeta_24^{25} = zeta_24 in the
   product ring K_5 = Q_25 x Q_5 of GSWZ Example 4.3).

3. Roots of unity kill the Iwasawa log (24*log zeta = 0), so
       D_5(zeta) = Li_2(zeta) + (1/2) log(zeta) log(1-zeta) = Li_2(zeta)
   EXACTLY at every Teichmuller point — the full-precision D_5 needs
   only Props 4.2 + 4.3.

WHAT THIS CHECKS (exact arithmetic in (Z/5^8)[x]/(x^3 - x^2 + 1)):

1. g_2 coefficient integrality (v_5 >= 0, the Prop 6.1 premise) and
   the proven tail bound at the working truncation.
2. GSWZ (273) row 1: Li_2(zeta24) vs ALL printed digits
   (alpha^2, alpha to 5^3; const to 5^4).
3. GSWZ (273) row 3: Li_2(zeta24^6) vs ALL printed digits (to 5^4).
4. GSWZ (273) row 2 ADJUDICATION: the pdf superscript reads zeta24^5
   while (274)/(275) decompose over [zeta24^2]; the mod-5^3 layer
   matched exponent 2 and found exponent 5 Frobenius-inconsistent.
   Full-precision Li_2(zeta24^5) AND Li_2(zeta24^2) vs the printed row
   settle the reading digit-by-digit.
5. Internal Frobenius equivariance: Li_2(zeta24^5) = phi_5(Li_2(zeta24))
   at full working precision (Galois-equivariance of Coleman Li_2 on
   Teichmuller points; phi_5 from the merged Hensel layer).
6. Consistency with the merged mod-p layer: Li_2(zeta)/25 mod 5 equals
   the Prop-3.2 finite-polylog values for all three targets.
7. GSWZ (274) at full printed-coefficient precision: c1*D5(zeta24) +
   c2*D5(zeta24^2) + c3*D5(zeta24^6) vs printed D5(xi) of (271),
   mod 5^4 (capped by c2's two printed digits).

HONESTY: eps_m units at full precision remain queued on qou-9p9y; this
probe completes the DILOG layer (mod-5^3-exact -> full precision).
"""

import json
import sys
from fractions import Fraction

P = 5
W = 8  # working precision 5^W
MOD = P**W
N = 120  # g-series truncation; Prop 6.1 tail valuation >> W

# ---------------------------------------------------------------- ring
# R = (Z/5^W)[x]/(x^3 - x^2 + 1); elements [c0, c1, c2] = c0 + c1*a + c2*a^2


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


# ------------------------------------------- g_2 series (Prop 4.3), exact Q
# power series = list of Fractions, index k = coefficient of v^k, length N+1


def series_mul(a, b):
    out = [Fraction(0)] * (N + 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j in range(0, N + 1 - i):
            if b[j] != 0:
                out[i + j] += ai * b[j]
    return out


def series_inv(a):
    assert a[0] == 1
    inv = [Fraction(0)] * (N + 1)
    inv[0] = Fraction(1)
    for k in range(1, N + 1):
        s = Fraction(0)
        for j in range(1, k + 1):
            s += a[j] * inv[k - j]
        inv[k] = -s
    return inv


def poly_to_series(coeffs_asc):
    s = [Fraction(0)] * (N + 1)
    for i, c in enumerate(coeffs_asc):
        if i <= N:
            s[i] = Fraction(c)
    return s


# d(v) = v^5 - (v-1)^5 = 1 - 5v + 10v^2 - 10v^3 + 5v^4 (constant term 1)
from math import comb

d_coeffs = [0] * 6
d_coeffs[5] += 1
for i in range(6):
    d_coeffs[i] -= comb(5, i) * (-1) ** (5 - i)
assert d_coeffs[0] == 1 and d_coeffs[5] == 0
d_series = poly_to_series(d_coeffs[:5])
# numerator (v-1)^5
num_coeffs = [comb(5, i) * (-1) ** (5 - i) for i in range(6)]
g0 = [-c for c in series_mul(poly_to_series(num_coeffs), series_inv(d_series))]
g0[0] -= 1
g0[1] += 1  # g0 = v - 1 - (v-1)^5/d(v)
assert g0[0] == 0, "g0(0) != 0"

geom = [Fraction(1)] * (N + 1)  # 1/(1-v)


def next_g(g):
    """g_{n+1} from g_n: g'_{n+1} = -(g_n/v)*(1/(1-v)); g_{n+1}(0) = 0."""
    g_over_v = g[1:] + [Fraction(0)]
    deriv = series_mul([-c for c in g_over_v], geom)
    out = [Fraction(0)] * (N + 1)
    for k in range(1, N + 1):
        out[k] = deriv[k - 1] / k
    return out


g1 = next_g(g0)
g2 = next_g(g1)

checks = {}

# (1) 5-integrality of g_2 coefficients + proven tail bound at N
import math

checks["g2_coeffs_5_integral"] = all(c.denominator % 5 != 0 for c in g2)
c25 = (
    5 / 4
    - 1 / math.log(5)
    + math.log(2 * 5 * 4 / math.log(5), 5)
    + math.log(2 * 5 * 4 * 2 / math.log(5), 5)
)
tail_val = (N + 1) / 4 - math.log(N + 1, 5) - c25
checks["tail_bound_exceeds_working_precision"] = tail_val > W


def eval_g2(v):
    """Horner evaluation of g_2 at ring element v (coefficients 5-integral)."""
    r = [0, 0, 0]
    for k in range(N, 0, -1):
        c = g2[k]
        cmod = (c.numerator * pow(c.denominator, -1, MOD)) % MOD
        r = mul(r, v)
        r[0] = (r[0] + cmod) % MOD
    return mul(r, v)  # g2 has zero constant term: sum a_k v^k = v * sum a_k v^{k-1}


# ------------------------------------------------ Teichmuller (merged layer)
alpha = [0, 1, 0]
z = alpha[:]
prev = None
stabilized = False
for s in range(1, 12):
    z = pw(z, 25)
    if z == prev:
        stabilized = True
        break
    prev = z[:]
assert stabilized
zeta24 = z
assert pw(zeta24, 24) == [1, 0, 0]


def li2(zeta):
    """Prop 4.2 with n = 2, f = 2: Li_2(zeta) for zeta^25 = zeta, zeta != 1
    componentwise (1 - zeta a unit)."""
    v1 = inv_unit([(1 - zeta[0]) % MOD, (-zeta[1]) % MOD, (-zeta[2]) % MOD])
    z5 = pw(zeta, 5)
    v2 = inv_unit([(1 - z5[0]) % MOD, (-z5[1]) % MOD, (-z5[2]) % MOD])
    total = add(smul(P**4, eval_g2(v1)), smul(P**2, eval_g2(v2)))
    return mul(total, inv_unit([(P**4 - 1) % MOD, 0, 0]))


Li = {k: li2(pw(zeta24, k)) for k in (1, 2, 5, 6)}


def digits(x, upto):
    """Base-5 digits of x mod 5^upto, least significant first."""
    out = []
    for _ in range(upto):
        out.append(x % 5)
        x //= 5
    return out


def matches_printed(val, printed):
    """printed = dict coord -> list of (power, digit); compare val's
    base-5 digits against the printed expansion THROUGH its highest
    printed power. GSWZ print canonical 5-adic expansions (digits in
    0..4, nonzero terms listed in increasing power), so a power omitted
    BELOW the last printed one has digit 0 by the positional
    convention — zero-filling those positions is exact, not an
    assumption; only digits beyond the highest printed power (the
    trailing dots) are unknown and are not compared."""
    ok = True
    for coord, digs in printed.items():
        idx = {"const": 0, "alpha": 1, "alpha2": 2}[coord]
        maxpow = max(pwr for pwr, _ in digs)
        got = digits(Li_coord(val, idx), maxpow + 1)
        want = [0] * (maxpow + 1)
        for pwr, dg in digs:
            want[pwr] = dg
        if got != want:
            ok = False
    return ok


def Li_coord(val, idx):
    return val[idx] % MOD


# GSWZ (273) printed digits [(5-power, digit), ...] per coordinate
printed_row1 = {  # D5(zeta24)
    "alpha2": [(2, 4), (3, 4)],
    "alpha": [(2, 4), (3, 2)],
    "const": [(2, 2), (3, 1), (4, 2)],
}
printed_row2 = {  # D5(zeta24^5) per the pdf superscript; adjudicated below
    "alpha2": [(2, 2), (3, 2), (4, 1)],
    "alpha": [(2, 3), (3, 3), (4, 1)],
    "const": [(2, 1), (3, 0), (4, 3)],
}
printed_row3 = {  # D5(zeta24^6)
    "alpha2": [(2, 3), (3, 3), (4, 2)],
    "alpha": [(2, 3), (3, 2), (4, 3)],
    "const": [(2, 2), (3, 0), (4, 4)],
}

# (2) row 1: all printed digits
checks["printed_273_row1_zeta24_all_digits"] = matches_printed(
    Li[1], printed_row1
)
# (3) row 3: all printed digits
checks["printed_273_row3_zeta24^6_all_digits"] = matches_printed(
    Li[6], printed_row3
)
# (4) row 2 adjudication: which exponent matches the printed digits?
row2_matches_exp5 = matches_printed(Li[5], printed_row2)
row2_matches_exp2 = matches_printed(Li[2], printed_row2)
checks["printed_273_row2_adjudicated_unique"] = (
    row2_matches_exp5 != row2_matches_exp2
)

# (5) Frobenius equivariance at full precision: Li_2(zeta^5) = phi(Li_2(zeta))
P_poly = [1, -1, 0, 1]
phi = pw(alpha, 5)
for d in range(1, W):
    # Horner for P(phi) and P'(phi)
    val = [(P_poly[0]) % MOD, 0, 0]
    for c in P_poly[1:]:
        val = mul(val, phi)
        val[0] = (val[0] + c) % MOD
    Pp = [3 % MOD, 0, 0]
    for c in [-2, 0]:
        Pp = mul(Pp, phi)
        Pp[0] = (Pp[0] + c) % MOD
    corr = mul(val, inv_unit(Pp))
    phi = [(phi[k] - corr[k]) % MOD for k in range(3)]


def apply_phi(x):
    """Ring endomorphism alpha -> phi (the Frobenius lift)."""
    return add(
        add([x[0] % MOD, 0, 0], smul(x[1], phi)), smul(x[2], mul(phi, phi))
    )


checks["frobenius_equivariance_li2"] = Li[5] == apply_phi(Li[1])

# (6) consistency with the merged mod-p layer (Prop 3.2 values, /25 mod 5)
prop32 = {"zeta24": [2, 4, 4], "zeta24^2": [1, 3, 2], "zeta24^6": [2, 3, 3]}
checks["modp_layer_consistency"] = all(
    [((Li[k][m] // 25) % 5) for m in range(3)] == prop32[name]
    for k, name in ((1, "zeta24"), (2, "zeta24^2"), (6, "zeta24^6"))
)

# (7) (274) decomposition at printed-coefficient precision (mod 5^4;
# capped by c2's two printed digits: c2 known mod 5^2, values in 25*Z)
c1 = 1 + 4 * 5 + 3 * 25
c2 = 3 + 5
c3 = 1 + 5 + 4 * 25
lhs = add(add(smul(c1, Li[1]), smul(c2, Li[2])), smul(c3, Li[6]))
CAP = 5**4
printed_271 = {  # D5(xi), digits to the printed depth
    "alpha2": 3 * 25 + 125 + 2 * 625,
    "alpha": 25 + 3 * 125,
    "const": 2 * 25 + 3 * 125,
}
checks["printed_271_decomposition_mod_5^4"] = (
    lhs[0] % CAP == printed_271["const"] % CAP
    and lhs[1] % CAP == printed_271["alpha"] % CAP
    and lhs[2] % CAP == printed_271["alpha2"] % CAP
)

print(json.dumps(checks, indent=1))
print(
    json.dumps(
        {
            "row2_matches_exp5": row2_matches_exp5,
            "row2_matches_exp2": row2_matches_exp2,
            "Li2_zeta24_digits_const": digits(Li[1][0], 6),
            "Li2_zeta24_digits_alpha": digits(Li[1][1], 6),
            "Li2_zeta24_digits_alpha2": digits(Li[1][2], 6),
        },
        indent=1,
    )
)
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_coleman_li2_full_precision_probe",
    "beans": ["qou-9p9y"],
    "source": (
        "Besser-de Jeu Math. Comp. 77 (2008) 1105-1134 Props 4.2/4.3/6.1 "
        "(library/s0025-5718-07-02027-3/S0025-5718-07-02027-3.pdf); GSWZ arXiv:2412.04241v2 "
        "Example 4.3 eqns (271)/(273)/(274) (library/arxiv-2412.04241v2/2412.04241v2.pdf)"
    ),
    "field": "Q(alpha)/(alpha^3 - alpha^2 + 1) (5_2 trace field), p = 5",
    "parameters": {"working_precision": f"5^{W}", "series_terms": N},
    "checks": checks,
    "row2_adjudication": {
        "matches_exp5": row2_matches_exp5,
        "matches_exp2": row2_matches_exp2,
    },
    "li2_values_base5_digits_lsf": {
        f"zeta24^{k}": {
            "const": digits(Li[k][0], 6),
            "alpha": digits(Li[k][1], 6),
            "alpha2": digits(Li[k][2], 6),
        }
        for k in (1, 2, 5, 6)
    },
    "scope": (
        "scope-(a): full-precision Coleman Li_2 at Teichmuller points via "
        "Besser-de Jeu; D_5 = Li_2 there (Iwasawa log kills roots of "
        "unity); eps_m units still queued (qou-9p9y)"
    ),
}
with open(
    "computations/probes/gswz_coleman_li2_full_precision.witness.json", "w"
) as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
