"""GSWZ p-adic dilogarithm, mod-p layer — Prop 3.2 verified vs all three printed D5 values.

Bean qou-dugz (T1 of the Habiro attack plan; parent gate bean qou-1hlh).
Scope-(a); no fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 5).

CONTEXT. The GSWZ module-side corrections need the p-adic Bloch-Wigner
dilogarithm D_p(z) = Li2(z) + (1/2)log(z)log(1-z) (their eqn (174),
Coleman's Li2, Iwasawa log). Full Coleman integration is heavy, but
their Prop 3.2 (arXiv:2412.04241v2, from Besser's [6, Cor 2.2]) gives
the MOD-p layer in closed form via Kontsevich's finite polylogarithm
li_{2,p}(z) = sum_{k=1}^{p-1} z^k / k^2 (their eqn (177)):

    p^{-2} D_p(zeta^p)  =  li_{2,p}(zeta) / (zeta - 1)^p   (mod p)

for zeta in mu(Q_{p^s}), zeta != 1. In the 5_2 trace field
K = Q(alpha)/(alpha^3 - alpha^2 + 1) at p = 5, the Teichmuller
zeta_24 (verified against printed digits in
gswz_frobenius_teichmuller_probe.py) satisfies 5th-power reachability:
25 = 1 mod 24, so EVERY zeta_24^k is a 5th power (zeta_24^k =
(zeta_24^{5k'})^5 with k' = 5k mod 24), and every printed D5 value of
GSWZ eqn (273) is testable through Prop 3.2:

    D5(zeta24)   = (4*5^2+...)a^2 + (4*5^2+...)a + (2*5^2+...)
    D5(zeta24^2) = (2*5^2+...)a^2 + (3*5^2+...)a + (5^2+...)
    D5(zeta24^6) = (3*5^2+...)a^2 + (3*5^2+...)a + (2*5^2+...)

(The middle row's superscript is 2, not 5: the pypdf extraction mangles
the superscript, but eqn (274) decomposes xi over [zeta24],
[zeta24^2], [zeta24^6], and the Prop-3.2 prediction matches the
printed digits ONLY for exponent 2 — the mismatch under the
exponent-5 reading was itself Frobenius-inconsistent, which is how the
transcription error was caught.)

WHAT THIS CHECKS (exact Z/5^6 arithmetic; comparisons mod 5):

1. Kontsevich sanity: li_{2,5}(1) = 0 mod 5 (their remark below (180)).
2. Prop 3.2 at zeta = zeta24^10: zeta^5 = zeta24^50 = zeta24^2,
   predicting D5(zeta24^2)/25 mod 5 = (1,3,2) in (const, alpha,
   alpha^2) coordinates — the printed value.
3. Prop 3.2 at zeta = zeta24^5: zeta^5 = zeta24^25 = zeta24, predicting
   D5(zeta24)/25 mod 5 = (2,4,4) — the printed value.
4. Prop 3.2 at zeta = zeta24^6: zeta^5 = zeta24^30 = zeta24^6,
   predicting D5(zeta24^6)/25 mod 5 = (2,3,3) — the printed value.

HONESTY: this is the MOD-p layer only; the full Coleman Li2 to higher
5-adic precision (needed for the eps_m corrections at full gate
precision, and for D5 on non-root-of-unity arguments like the printed
(271)) stays queued on qou-dugz/qou-9p9y.
"""

import json
import pathlib
import sys

D = 6
MOD = 5**D
# Ring: (Z/5^6)[x]/(x^3 - x^2 + 1); the reduction x^3 = x^2 - 1 is
# hard-coded in mul() below.


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
    """Invert a unit of the ring by mod-5 seed search + Newton."""
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
    for _ in range(4):
        t = mul(u, inv)
        inv = mul(inv, [(-t[0] + 2) % MOD, (-t[1]) % MOD, (-t[2]) % MOD])
    return inv


def li25(z):
    """Kontsevich finite dilog li_{2,5}(z) = sum_{k=1}^{4} z^k / k^2."""
    total = [0, 0, 0]
    for k in range(1, 5):
        zk = pw(z, k)
        kinv2 = pow(k * k, -1, MOD)
        total = [(total[m] + zk[m] * kinv2) % MOD for m in range(3)]
    return total


# Teichmuller zeta_24 (as in the Frobenius probe)
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
assert stabilized, "Teichmuller iteration did not stabilize"
zeta24 = z

checks = {}

# (1) li_{2,5}(1) = 0 mod 5
l1 = li25([1, 0, 0])
checks["kontsevich_li25_at_1_vanishes_mod_5"] = all(c % 5 == 0 for c in l1)


def prop32_rhs_mod5(zeta):
    """li_{2,5}(zeta) / (zeta-1)^5 mod 5, coords (const, alpha, alpha^2)."""
    num = li25(zeta)
    den = pw([(zeta[0] - 1) % MOD, zeta[1], zeta[2]], 5)
    q = mul(num, inv_unit(den))
    return [c % 5 for c in q]


# printed D5 values of eqn (273), divided by 25, mod 5,
# coords (const, alpha, alpha^2)
printed = {
    "zeta24": [2, 4, 4],
    "zeta24^2": [1, 3, 2],
    "zeta24^6": [2, 3, 3],
}

# (2) zeta = zeta24^10 -> zeta^5 = zeta24^2
checks["prop32_predicts_printed_D5_zeta24^2"] = (
    prop32_rhs_mod5(pw(zeta24, 10)) == printed["zeta24^2"]
)
# (3) zeta = zeta24^5 -> zeta^5 = zeta24^25 = zeta24
checks["prop32_predicts_printed_D5_zeta24"] = (
    prop32_rhs_mod5(pw(zeta24, 5)) == printed["zeta24"]
)
# (4) zeta = zeta24^6 -> zeta^5 = zeta24^30 = zeta24^6
checks["prop32_predicts_printed_D5_zeta24^6"] = (
    prop32_rhs_mod5(pw(zeta24, 6)) == printed["zeta24^6"]
)

print(json.dumps(checks, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_padic_dilog_modp_probe",
    "beans": ["qou-dugz", "qou-1hlh"],
    "source": "GSWZ arXiv:2412.04241v2 §3.1 Prop 3.2, eqns (174)/(177)/(273); uploads/2412.04241v2.pdf",
    "field": "Q(alpha)/(alpha^3 - alpha^2 + 1) (5_2 trace field), p = 5",
    "checks": checks,
    "computed_rhs_mod5": {
        "input_zeta24^10_target_D5_zeta24^2": prop32_rhs_mod5(pw(zeta24, 10)),
        "input_zeta24^5_target_D5_zeta24": prop32_rhs_mod5(pw(zeta24, 5)),
        "input_zeta24^6_target_D5_zeta24^6": prop32_rhs_mod5(pw(zeta24, 6)),
    },
    "scope": "scope-(a): mod-p dilog layer (finite polylog + Prop 3.2) vs printed (273); full Coleman Li2 queued",
}
with open(pathlib.Path(__file__).resolve().parent / "gswz_padic_dilog_modp.witness.json", "w") as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
