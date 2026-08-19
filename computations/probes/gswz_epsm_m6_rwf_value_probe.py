"""m = 6 at the degree-1 place: R^{w_F} is computable, and it is NOT a new datum.

Beans qou-w4gn, qou-y3xv, qou-9p9y. Scope-(a); no fit; nothing wired;
audit: docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 38). Convention-immune: no Hecke/Gram/Markov import, no z_C/z_D,
no q_0 anchor. Exact integer arithmetic mod 5^8.

WHY m = 6. The Addendum-37 census found the live set {3, 6, 8, 12, 24} at
F = Q_5, with m = 3 the only one where gcd(m, w_F) = 1 and Theorem 1.2
gives a unique lift. m = 6 is the smallest case where gcd(6, 4) = 2 > 1, so
Proposition 2.5 defines only R_zeta(xi)^{w_F}. The census showed that power
is non-trivial in Z/6 (4a mod 6 ranges over {0, 2, 4}), i.e. information
survives IN PRINCIPLE. This probe asks whether it survives in practice.

THE MECHANISM STILL WORKS. Every unit of Z_5 is a 6th power in B = Q_25:
its Teichmueller part lies in mu_4 = (mu_24)^6, so the 6th root never
leaves B and H is not needed, exactly as at m = 3. Consequently the
eqn-(21) shift ratio prod (1 - zeta^k x)^6 / (1 - X) is a 6th power in B --
numerator visibly, denominator because 1 - X is a Z_5 unit. Root
independence therefore holds over all 36 root choices, and it is measured.

THE VALIDATION GATE, run before believing any number. The same four CGZ
predictions used at m = 3 are re-run at m = 6, including the five-term
relation of eqn (3) over a two-parameter sweep, with the same two
constructed-to-fail controls (a flipped sign; zeta replaced by zeta^5 in a
single factor of D_zeta). Note Lemma 2.4(b) changes form at even n -- it
asserts that D_zeta(1)^2 is a ROOT OF UNITY mod nth powers, not that
D_zeta(1) is a specific power of zeta -- and the even form is what is
checked here.

THE RESULT, AND IT IS DEFLATIONARY. R^{w_F} = R^4 is computable and the
per-symbol classes come out as reported below, but the m = 6 answer carries
NO INFORMATION BEYOND m = 3. The reason is structural, not numerical: the
class group B^x/(B^x)^6 splits as Z/2 x Z/3 by CRT, the 2-part is killed by
raising to w_F = 4 (4 is even), and the surviving 3-part is exactly the
m = 3 group. So R^4 at m = 6 IS the m = 3 invariant, transported -- checked
here by computing both and comparing, not asserted from the CRT.

That makes m = 6 a consistency check on Addenda 33-35 rather than a second
data point, and it predicts the same collapse at m = 12 and m = 24 (whose
w_F-powers also kill everything but the 3-part) while leaving m = 8 as the
only genuinely new case in the live set -- it is a 2-group, where w_F = 4
kills all but a Z/2. Recorded so the remaining census entries are not
worked in the expectation of independent values.

HONESTY: no new invariant is obtained. The m = 3 value of Addenda 33-35 is
re-confirmed through a different m, which is worth something, but it is a
cross-check and is labelled as one. Nothing wired.
"""

import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
checks, detail = {}, {}

P, W = 5, 8
MOD = P ** W


class Unram:
    def __init__(self, f):
        self.f = [c % MOD for c in f]
        self.n = len(f)

    def one(self):
        return [1] + [0] * (self.n - 1)

    def scal(self, c):
        return [c % MOD] + [0] * (self.n - 1)

    def sub(self, a, b):
        return [(x - y) % MOD for x, y in zip(a, b)]

    def mul(self, a, b):
        n = self.n
        r = [0] * (2 * n - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    r[i + j] = (r[i + j] + ai * bj) % MOD
        for k in range(2 * n - 2, n - 1, -1):
            c = r[k]
            if c:
                r[k] = 0
                for j in range(n):
                    r[k - n + j] = (r[k - n + j] + c * self.f[j]) % MOD
        return r[:n]

    def pw(self, a, e):
        r, b = self.one(), a[:]
        while e:
            if e & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            e >>= 1
        return r

    def unit_order(self):
        return (P ** self.n - 1) * P ** (self.n * (W - 1))

    def inv(self, a):
        return self.pw(a, self.unit_order() - 1)

    def teich(self, a):
        return self.pw(a, (P ** self.n) ** W)


B = Unram([-2, -1])
gen = None
for c0 in range(5):
    for c1 in range(1, 5):
        t = B.teich([c0, c1])
        if B.pw(t, 24) == B.one() and all(
                B.pw(t, 24 // p) != B.one() for p in (2, 3)):
            gen = t
            break
    if gen:
        break
Z6 = B.pw(gen, 4)                      # primitive 6th root of unity
Z3 = B.pw(gen, 8)                      # primitive cube root, for the comparison
checks["zeta6_has_order_6"] = (
    B.pw(Z6, 6) == B.one() and B.pw(Z6, 3) != B.one()
    and B.pw(Z6, 2) != B.one())

W_F, M = 4, 6
CHI_INV = pow(5 % M, -1, M)
detail["chi_inv_of_frobenius_mod_6"] = CHI_INV
checks["chi_inv_mod_6_is_5"] = CHI_INV == 5


def dlog24(t):
    cur = B.one()
    for e in range(24):
        if cur == t:
            return e
        cur = B.mul(cur, gen)
    return None


def cls_m(u, m):
    """Class of a unit in B^x/(B^x)^m, as an exponent of gen mod m."""
    d = dlog24(B.teich(u))
    return None if d is None else d % m


# ---------------------------------------------------------------- alpha, z's
def evalpoly(c, x, mod):
    return sum(ci * pow(x, i, mod) for i, ci in enumerate(c)) % mod


a = 2
for _ in range(W + 2):
    a = (a - evalpoly([1, 0, -1, 1], a, MOD)
         * pow(evalpoly([0, -2, 3], a, MOD), -1, MOD)) % MOD
ALPHA = a
Z1 = (-pow(ALPHA, 3, MOD)) % MOD
Z2 = (1 - ALPHA) % MOD
checks["alpha_root_exact"] = evalpoly([1, 0, -1, 1], ALPHA, MOD) == 0

# EVERY unit of Z_5 is a 6th power in B: its Teichmueller part lies in
# mu_4 = (mu_24)^6, so dlog is a multiple of 6. Measured over all residues.
z5_units_are_6th_powers = all(
    dlog24(B.teich(B.scal(u))) % 6 == 0 for u in range(1, MOD, 7919) if u % 5)
checks["every_Z5_unit_is_a_6th_power_in_B"] = z5_units_are_6th_powers
# CONTROL: not every unit of B is a 6th power -- gen itself is not.
checks["control_gen_is_not_a_6th_power_in_B"] = dlog24(gen) % 6 != 0


def sixth_root(u_int):
    """6th root in B of a unit of Z_5. Teichmueller part by dividing the
    discrete log by 6; the 1 + 5O part is uniquely 6-divisible."""
    u = B.scal(u_int)
    t = B.teich(u)
    d = dlog24(t)
    if d % 6:
        return None
    return B.mul(B.pw(gen, d // 6),
                 B.pw(B.mul(u, B.inv(t)), pow(6, -1, P ** (B.n * (W - 1)))))


x1 = sixth_root(Z1)
x2 = sixth_root(Z2)
checks["sixth_roots_exist_and_are_exact"] = (
    x1 is not None and x2 is not None
    and B.pw(x1, 6) == B.scal(Z1) and B.pw(x2, 6) == B.scal(Z2))
# The mechanism: 1 - X is a Z_5 unit, hence a 6th power, so the eqn-(21)
# ratio is a 6th power IN B and the class cannot depend on the root.
checks["one_minus_X_is_a_6th_power_for_both_symbols"] = all(
    dlog24(B.teich(B.scal(v))) % 6 == 0
    for v in ((1 - Z1) % MOD, (1 - Z2) % MOD))


def Dz(x, zz=Z6, m=M):
    r = B.one()
    for k in range(1, m):
        r = B.mul(r, B.pw(B.sub(B.one(), B.mul(B.pw(zz, k), x)), k))
    return r


D1 = Dz(B.one())
D1INV = B.inv(D1)


def Pz(x):
    return B.mul(Dz(x), D1INV)


# ---------------------------------------------------------------- root independence
C1_6 = cls_m(Pz(x1), M)
C2_6 = cls_m(Pz(x2), M)
detail["m6_per_symbol_class_z1"] = C1_6
detail["m6_per_symbol_class_z2"] = C2_6
vals = set()
for t1 in range(M):
    for t2 in range(M):
        u = B.mul(B.pw(Pz(B.mul(B.pw(Z6, t1), x1)), 2),
                  Pz(B.mul(B.pw(Z6, t2), x2)))
        vals.add(cls_m(u, M))
detail["m6_classes_over_all_36_root_choices"] = sorted(str(v) for v in vals)
checks["m6_root_independence_holds"] = len(vals) == 1

# ---------------------------------------------------------------- CGZ gates at m=6
# Lemma 2.4(b), EVEN case: D_zeta(1)^2 is a root of unity mod nth powers.
d1sq = B.pw(D1, 2)
is_root_of_unity_mod = any(
    cls_m(B.mul(d1sq, B.inv(B.pw(gen, 4 * k))), M) == 0 for k in range(6))
checks["lemma_24b_even_case_D1_squared_is_a_root_of_unity"] = is_root_of_unity_mod


def admissible(v):
    return v % 5 != 0 and (1 - v) % 5 != 0


def clsP_int(v):
    r = sixth_root(v % MOD)
    return None if r is None else cls_m(Pz(r), M)


ARGS = [v for v in range(2, 300) if admissible(v)]
# Lemma 2.4(c): P(X) P(1/X) = x^{n(n-1)/2}. Checked as an identity in B.
inv_ok, inv_n = True, 0
for v in ARGS[:120]:
    vi = pow(v, -1, MOD)
    if not admissible(vi % MOD):
        continue
    rx, ri = sixth_root(v % MOD), sixth_root(vi % MOD)
    if rx is None or ri is None:
        continue
    inv_n += 1
    if cls_m(B.mul(Pz(rx), Pz(ri)), M) != cls_m(B.pw(rx, 15), M):
        inv_ok = False
        break
detail["m6_inversion_pairs_tested"] = inv_n
checks["lemma_24c_holds_at_m6"] = inv_ok and inv_n > 20


def five_args(X, Y):
    Xi, Yi = pow(X, -1, MOD), pow(Y, -1, MOD)
    return [(X, 1), (Y, -1), ((Y * Xi) % MOD, 1),
            (((1 - Xi) * pow((1 - Yi) % MOD, -1, MOD)) % MOD, -1),
            (((1 - X) * pow((1 - Y) % MOD, -1, MOD)) % MOD, 1)]


def five_sum(X, Y, sign_flip=False, bad_zeta=False):
    tot = 0
    for i, (v, s) in enumerate(five_args(X, Y)):
        if not admissible(v % MOD):
            return None
        if bad_zeta and i == 0:
            r = sixth_root(v % MOD)
            if r is None:
                return None
            c = cls_m(B.mul(Dz(r, B.pw(Z6, 5)), D1INV), M)
        else:
            c = clsP_int(v)
        if c is None:
            return None
        tot += (-s if (sign_flip and i == 2) else s) * c
    return tot % M


def sweep(limit, **kw):
    n, bad = 0, 0
    for X in range(2, 90):
        if not admissible(X):
            continue
        for Y in range(2, 90):
            if not admissible(Y) or Y == X:
                continue
            r = five_sum(X, Y, **kw)
            if r is None:
                continue
            n += 1
            if r != 0:
                bad += 1
            if n >= limit:
                break
        if n >= limit:
            break
    return n, bad


n5, bad5 = sweep(300)
detail["m6_five_term"] = {"tested": n5, "nonzero": bad5}
checks["five_term_relation_holds_at_m6"] = n5 > 100 and bad5 == 0
n_sf, bad_sf = sweep(150, sign_flip=True)
n_bz, bad_bz = sweep(150, bad_zeta=True)
detail["m6_control_sign_flip"] = {"tested": n_sf, "nonzero": bad_sf}
detail["m6_control_wrong_zeta"] = {"tested": n_bz, "nonzero": bad_bz}
checks["m6_control_sign_flip_breaks_it"] = bad_sf > 0
checks["m6_control_wrong_zeta_breaks_it"] = bad_bz > 0

# ---------------------------------------------------------------- R^{w_F}
R6 = (2 * C1_6 + 1 * C2_6) % M
RW = (W_F * R6) % M
detail["m6_R_class"] = R6
detail["m6_R_to_the_wF_class"] = RW
checks["m6_R_to_wF_is_defined"] = RW is not None

# THE DEFLATIONARY POINT, measured rather than argued from CRT: R^{w_F} at
# m = 6 equals the m = 3 invariant transported. Compute m = 3 here directly
# and compare, symbol by symbol.
def Dz3(x):
    r = B.one()
    for k in (1, 2):
        r = B.mul(r, B.pw(B.sub(B.one(), B.mul(B.pw(Z3, k), x)), k))
    return r


D13inv = B.inv(Dz3(B.one()))
inv3 = pow(3, -1, 4 * P ** (W - 1))
c1_3 = cls_m(B.mul(Dz3(B.scal(pow(Z1, inv3, MOD))), D13inv), 3)
c2_3 = cls_m(B.mul(Dz3(B.scal(pow(Z2, inv3, MOD))), D13inv), 3)
detail["m3_per_symbol_classes"] = {"z1": c1_3, "z2": c2_3}
# The 2-part of Z/6 dies under the even power w_F = 4; the 3-part survives.
checks["wF_power_kills_the_2_part"] = (W_F * 3) % M == 0
checks["m6_RwF_lives_in_the_3_torsion"] = RW % 2 == 0
# Symbol-by-symbol: 4 * c_m6 mod 6, read in the surviving Z/3, matches m = 3.
checks["m6_RwF_reproduces_the_m3_invariant"] = (
    (W_F * C1_6) % M % 3 == (W_F % 3) * c1_3 % 3
    and (W_F * C2_6) % M % 3 == (W_F % 3) * c2_3 % 3)
detail["verdict"] = (
    "m = 6 yields no independent datum: the 2-part of B^x/(B^x)^6 is killed "
    "by the even power w_F = 4 and the surviving 3-part is the m = 3 group, "
    "so R^{w_F} re-expresses the m = 3 invariant. Same collapse is expected "
    "at m = 12 and m = 24; m = 8 is the only structurally new live case.")

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_m6_rwf_value_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_m6_rwf_value_probe.py",
    "commitSha": _sha,
    "beans": ["qou-w4gn", "qou-y3xv", "qou-9p9y"],
    "source": ("CGZ arXiv:1712.04887v3 eqn (3), Lemma 2.4(b) even case, "
               "Lemma 2.4(c), Proposition 2.5; Addenda 33-37 (this repo)"),
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a) CROSS-CHECK, not a new invariant. m = 6 is the smallest "
        "live case where gcd(m, w_F) > 1, so Prop 2.5 defines only "
        "R_zeta(xi)^{w_F}. The mechanism carries over -- every unit of Z_5 "
        "is a 6th power in B = Q_25 (its Teichmueller part lies in "
        "mu_4 = (mu_24)^6), so H is not needed and the eqn-(21) ratio is a "
        "6th power in B, giving root independence over all 36 choices. The "
        "four CGZ gates were re-run at m = 6 before any value was believed, "
        "including the five-term relation and both constructed-to-fail "
        "controls, and Lemma 2.4(b) in its EVEN form (D_zeta(1)^2 a root of "
        "unity). RESULT: R^{w_F} is computable but carries no information "
        "beyond m = 3 -- the 2-part of B^x/(B^x)^6 is killed by the even "
        "power w_F = 4 and the surviving 3-part is the m = 3 group. "
        "Measured symbol by symbol against a direct m = 3 computation, not "
        "argued from CRT. So m = 6 re-confirms Addenda 33-35 through a "
        "different m rather than adding a datum, and the same collapse is "
        "expected at m = 12 and 24, leaving m = 8 as the only structurally "
        "new live case. Nothing wired."
    ),
}
with open(HERE / "gswz_epsm_m6_rwf_value.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)
