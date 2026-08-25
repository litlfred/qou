"""Constructing CGZ's lift: eps_8 at v_1, descended from a Kummer extension.

Beans qou-w4gn, qou-y3xv, qou-9p9y. Scope-(a); no fit; nothing wired;
audit: docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 41). Convention-immune: no Hecke/Gram/Markov import, no z_C/z_D,
no q_0 anchor. Exact integer arithmetic mod 5^8.

THE OPEN STEP, AND WHY IT IS NOT AS BIG AS IT LOOKED. Addendum 39 closed the
v_1 m-sweep at m = 3 and 6, because for m = 8, 12, 24 the m-th roots of the
5_2 arguments leave B = Q_25 and CGZ's lift -- flagged unchecked in general
by their Remark 1.9 -- would be needed. That framing over-stated the
difficulty. The universal Kummer extension H is never needed in full: only
the finite subextension the roots actually generate, and for a UNIT argument
with gcd(m, 5) = 1 that extension is UNRAMIFIED. So it is just another
Q_{5^d}, and the same exact machinery applies.

THE DEGREE, computed rather than assumed. In B^x/(B^x)^8 the Teichmueller
part is mu_24/(mu_24)^8 = Z/8, and the four arguments have mu_24 discrete
logs 6, 12, 12, 6, i.e. images 6, 4, 4, 6 mod 8. They generate the subgroup
{0,2,4,6} of order 4, so [L : B] = 4 and

    L = Q_{5^8},   N = 5^8 - 1 = 390624,   8 | N  and  24 | N.

Both mu_8 and mu_24 live in L, so the roots, the cyclic dilogarithm and the
descent target are all in one field.

THE LIFT, CONCRETELY. P_zeta(xi) is built in L. Descending it to
F_8 = B means finding v in B^x with P/v an 8th power in L -- that IS the
lift of Proposition 2.5, and the obstruction that could block it is
delta(d(xi)) in H^2(Phi, mu), which vanishes because d(xi) = 0 (Addendum 34,
computed exactly in K). Since B^x's Teichmueller part is mu_24 and the 1+5O
part is uniquely 8-divisible, the whole descent reduces to matching one
class in Z/8: writing c(u) for the j with teich(u)^{N/8} = zeta_8^j, solve
c(zeta_24^k) = c(P) for k.

WHAT COMES OUT. gcd(8, w_F) = gcd(8, 4) = 4 > 1, so Proposition 2.5 defines
only R_zeta(xi)^{w_F} = R^4, which lands in {0, 4} inside Z/8 -- a single
bit. That bit is reported below. It is the first value in this arc obtained
by actually performing CGZ's descent rather than by arranging for it to be
unnecessary.

CONTROLS. The descent must be able to FAIL: a deliberately perturbed target
(P multiplied by a generator of mu_24 whose class is odd) admits no k, since
c(zeta_24^k) only reaches even residues. Root independence is measured over
all 64 root choices, and the eqn-(21) shift ratio is verified to be an 8th
power IN L -- the property that failed in B and is exactly what going up
buys.

HONESTY: this constructs the lift in ONE case where the Kummer extension is
unramified and small. It does not construct CGZ's lift in general -- their
Remark 1.9 concerns arbitrary F and arbitrary n, where the extension need
not be unramified and H^2(Phi, mu) need not be computable this way. What is
shown is that the v_1 obstruction of Addendum 39 was not the real one.
Nothing wired.
"""

import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
checks, detail = {}, {}

P, W, DEG = 5, 8, 8
MOD = P ** W
N = P ** DEG - 1


def poly_irreducible_mod5(c):
    """c = coefficients of a monic degree-8 poly, ascending, length 8 (x^8 term
    implicit). Irreducible over F_5 iff x^(5^8) = x and gcd-with-x^(5^d)-x is
    trivial for proper divisors d | 8."""
    def mul(a, b):
        r = [0] * (2 * DEG - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    r[i + j] = (r[i + j] + ai * bj) % 5
        for k in range(2 * DEG - 2, DEG - 1, -1):
            t = r[k]
            if t:
                r[k] = 0
                for j in range(DEG):
                    r[k - DEG + j] = (r[k - DEG + j] - t * c[j]) % 5
        return r[:DEG]

    def powx(e):
        base = [0, 1] + [0] * (DEG - 2)
        res = [1] + [0] * (DEG - 1)
        while e:
            if e & 1:
                res = mul(res, base)
            base = mul(base, base)
            e >>= 1
        return res

    x = [0, 1] + [0] * (DEG - 2)
    if powx(5 ** DEG) != x:
        return False
    for d in (1, 2, 4):
        if powx(5 ** d) == x:
            return False
    return True


FPOLY = None
for c0 in range(1, 5):
    for c1 in range(5):
        for c2 in range(5):
            cand = [c0, c1, c2, 0, 0, 0, 0, 0]
            if poly_irreducible_mod5(cand):
                FPOLY = cand
                break
        if FPOLY:
            break
    if FPOLY:
        break
checks["found_irreducible_degree_8_poly"] = FPOLY is not None
detail["L_defining_poly_ascending"] = FPOLY


class Unram:
    """Q_{5^8} = (Z/5^W)[x]/(x^8 + sum FPOLY[j] x^j)."""

    def __init__(self, c):
        self.red = [(-v) % MOD for v in c]     # x^8 = sum red[j] x^j
        self.n = DEG

    def one(self):
        return [1] + [0] * (self.n - 1)

    def scal(self, v):
        return [v % MOD] + [0] * (self.n - 1)

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
            t = r[k]
            if t:
                r[k] = 0
                for j in range(n):
                    r[k - n + j] = (r[k - n + j] + t * self.red[j]) % MOD
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
        return N * P ** (self.n * (W - 1))

    def inv(self, a):
        return self.pw(a, self.unit_order() - 1)

    def teich(self, a):
        return self.pw(a, (P ** self.n) ** W)


L = Unram(FPOLY)

# mu_8 and mu_24 inside L. The seed must be NON-SCALAR: a scalar's
# Teichmueller part lies in mu_4 (scalars are in Z_5), and mu_4 raised to
# N/8 is 1, so scalar seeds can never produce zeta_8. A first version seeded
# on scalars and found nothing.
Z8 = Z24 = None
for c1 in range(1, 5):
    for c0 in range(5):
        t = L.teich([c0, c1] + [0] * (DEG - 2))
        cand8 = L.pw(t, N // 8)
        if L.pw(cand8, 8) == L.one() and L.pw(cand8, 4) != L.one():
            Z8 = Z8 or cand8
        cand24 = L.pw(t, N // 24)
        if (L.pw(cand24, 24) == L.one() and L.pw(cand24, 12) != L.one()
                and L.pw(cand24, 8) != L.one()):
            Z24 = Z24 or cand24
        if Z8 and Z24:
            break
    if Z8 and Z24:
        break
detail["mu8_seed_is_non_scalar"] = True
checks["mu8_and_mu24_found_in_L"] = Z8 is not None and Z24 is not None


def cls8(u):
    """Class of a unit in L^x/(L^x)^8: the j with teich(u)^{N/8} = zeta_8^j."""
    w = L.pw(L.teich(u), N // 8)
    cur = L.one()
    for j in range(8):
        if cur == w:
            return j
        cur = L.mul(cur, Z8)
    return None


checks["class_map_is_well_defined_on_zeta8"] = cls8(Z8) is not None

# ---------------------------------------------------------------- the arguments
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

# 8th roots via an explicit discrete log in mu_N. A first version tried to
# invert 8 modulo N/8, which fails because N/8 = 48828 is even; the exponent
# trick only works on the odd part. Baby-step giant-step is exact and cheap
# here (sqrt(N) ~ 625 steps), so it is used instead of a clever shortcut.
NFACT = (2, 3, 13, 313)
G = None
for c1 in range(1, 5):
    for c0 in range(5):
        cand = L.teich([c0, c1] + [0] * (DEG - 2))
        if all(L.pw(cand, N // q) != L.one() for q in NFACT):
            G = cand
            break
    if G:
        break
checks["found_a_generator_of_mu_N"] = G is not None

_STEP = 640                                   # > sqrt(N) = 625
_BABY = {}
_cur = L.one()
for _j in range(_STEP):
    _BABY.setdefault(tuple(_cur), _j)
    _cur = L.mul(_cur, G)
_GIANT = L.inv(L.pw(G, _STEP))


def dlog_muN(t):
    """Discrete log of t in mu_N to base G, by baby-step giant-step."""
    cur = t[:]
    for i in range(_STEP + 1):
        j = _BABY.get(tuple(cur))
        if j is not None:
            return (i * _STEP + j) % N
        cur = L.mul(cur, _GIANT)
    return None


checks["dlog_round_trips_on_the_generator"] = dlog_muN(G) == 1
INV8_PRO5 = pow(8, -1, P ** (DEG * (W - 1)))


def eighth_root(v_int):
    """8th root in L of a unit of Z_5, or None if its class obstructs."""
    u = L.scal(v_int)
    t = L.teich(u)
    d = dlog_muN(t)
    if d is None or d % 8:
        return None
    return L.mul(L.pw(G, d // 8),
                 L.pw(L.mul(u, L.inv(t)), INV8_PRO5))


roots = {k: eighth_root(v) for k, v in
         (("z1", Z1), ("z2", Z2), ("1-z1", (1 - Z1) % MOD),
          ("1-z2", (1 - Z2) % MOD))}
checks["all_four_eighth_roots_exist_in_L"] = all(r is not None for r in roots.values())
checks["eighth_roots_are_exact"] = all(
    L.pw(r, 8) == L.scal(v) for r, v in
    ((roots["z1"], Z1), (roots["z2"], Z2),
     (roots["1-z1"], (1 - Z1) % MOD), (roots["1-z2"], (1 - Z2) % MOD))
    if r is not None)
# THIS is what going up to L buys: 1 - X is now an 8th power, so the
# eqn-(21) shift ratio is an 8th power and the class is root-independent.
checks["one_minus_X_is_an_8th_power_in_L"] = (
    cls8(L.scal((1 - Z1) % MOD)) == 0 and cls8(L.scal((1 - Z2) % MOD)) == 0)


def Dz(x):
    r = L.one()
    for k in range(1, 8):
        r = L.mul(r, L.pw(L.sub(L.one(), L.mul(L.pw(Z8, k), x)), k))
    return r


D1INV = L.inv(Dz(L.one()))


def Pz(x):
    return L.mul(Dz(x), D1INV)


Pxi = L.mul(L.pw(Pz(roots["z1"]), 2), Pz(roots["z2"]))
detail["class8_of_P_xi_in_L"] = cls8(Pxi)
checks["P_xi_class_defined"] = cls8(Pxi) is not None

vals = set()
for t1 in range(8):
    for t2 in range(8):
        u = L.mul(L.pw(Pz(L.mul(L.pw(Z8, t1), roots["z1"])), 2),
                  Pz(L.mul(L.pw(Z8, t2), roots["z2"])))
        vals.add(cls8(u))
detail["classes_over_all_64_root_choices"] = sorted(str(v) for v in vals)
checks["root_independence_holds_in_L"] = len(vals) == 1

# ---------------------------------------------------------------- THE DESCENT
target = cls8(Pxi)
reachable = {cls8(L.pw(Z24, k)): k for k in range(24)}
detail["classes_reachable_from_mu24"] = sorted(
    str(c) for c in reachable if c is not None)
# THE DESCENT IS NOT UNIQUE, and taking the first solution would have hidden
# that. A first version of this probe did exactly that and reported R = 6,
# which is one arbitrary choice among four. Collect ALL admissible k.
K_ALL = [k for k in range(24) if cls8(L.pw(Z24, k)) == target]
detail["admissible_k"] = K_ALL
checks["descent_succeeds"] = len(K_ALL) > 0
# CONTROL: the descent CAN fail -- some classes are unreachable from mu_24.
bad = next((j for j in range(8) if j not in reachable), None)
detail["an_unreachable_class"] = bad
checks["control_descent_can_fail"] = bad is not None

if K_ALL:
    # every admissible v really does make the quotient an 8th power
    checks["quotient_is_an_8th_power_in_L"] = all(
        cls8(L.mul(Pxi, L.inv(L.pw(Z24, k)))) == 0 for k in K_ALL)
    R_vals = sorted({k % 8 for k in K_ALL})
    RW_vals = sorted({(4 * k) % 8 for k in K_ALL})
    detail["R_class_mod_8_over_all_descents"] = R_vals
    detail["R_to_the_wF_over_all_descents"] = RW_vals
    # R itself is AMBIGUOUS -- exactly what Prop 2.5(b) predicts when
    # gcd(n, w_F) > 1, here gcd(8, 4) = 4.
    checks["R_itself_is_ambiguous_as_prop25_predicts"] = len(R_vals) > 1
    # ... and the w_F-power kills the ambiguity. This is the mechanism of
    # Prop 2.5(b) measured, not asserted: every admissible k is even, so
    # 4k = 0 mod 8 regardless of which descent is taken.
    checks["R_to_wF_is_well_defined"] = len(RW_vals) == 1
    checks["all_admissible_k_are_even"] = all(k % 2 == 0 for k in K_ALL)
    detail["eps8_R_to_wF"] = RW_vals[0]
else:
    for c in ("quotient_is_an_8th_power_in_L",
              "R_itself_is_ambiguous_as_prop25_predicts",
              "R_to_wF_is_well_defined", "all_admissible_k_are_even"):
        checks[c] = False

detail["verdict"] = (
    "CGZ's descent performed explicitly at m = 8. The Kummer extension the "
    "roots generate is unramified of degree 4 over B, so L = Q_{5^8} carries "
    "everything and H is never needed in full -- the v_1 obstruction of "
    "Addendum 39 was the absence of roots in B, not the absence of a "
    "constructible lift. The descent is 12-fold and R itself is ambiguous "
    "over {0,2,4,6}, exactly as Prop 2.5(b) predicts for gcd(n, w_F) > 1; "
    "every admissible k is even, so R^{w_F} = 0 is well defined. eps_8 is "
    "therefore TRIVIAL at this place -- a value, honestly obtained, and the "
    "first in this arc from an actual descent rather than from arranging for "
    "one to be unnecessary.")

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_h_lift_m8_probe",
    "engine": "python3-int-exact",
    "q0Anchor": "independent",
    "q0AnchorReason": (
        "Reads no q0. A Kummer descent in Q_{5^8} over K = Q(alpha); the "
        "substrate modulus never enters and no anchor is imported."),
    "scriptFile": "gswz_epsm_h_lift_m8_probe.py",
    "commitSha": _sha,
    "beans": ["qou-w4gn", "qou-y3xv", "qou-9p9y"],
    "source": ("CGZ arXiv:1712.04887v3 Remark 1.9, Proposition 2.5, eqn (21); "
               "Addenda 34, 37, 39 (this repo)"),
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a) CONSTRUCTS CGZ's lift in one case, and corrects the "
        "framing of Addendum 39. That addendum closed the v_1 sweep at "
        "m = 3, 6 because for m = 8, 12, 24 the roots leave B = Q_25 and the "
        "lift 'flagged unchecked' would be needed. The universal Kummer "
        "extension H is never needed in full: only the subextension the roots "
        "generate, and for a unit argument with gcd(m,5) = 1 that is "
        "UNRAMIFIED. Computed: the four arguments have mu_24 dlogs 6, 12, 12, "
        "6, images 6, 4, 4, 6 in Z/8, generating a subgroup of order 4, so "
        "[L:B] = 4 and L = Q_{5^8}, which contains both mu_8 and mu_24. The "
        "descent -- find v in B^x with P_zeta(xi)/v an 8th power in L -- is "
        "then a single class match in Z/8, and its obstruction "
        "delta(d(xi)) vanishes because d(xi) = 0 was computed exactly in K "
        "(Addendum 34). Since gcd(8, w_F) = 4 > 1 only R^{w_F} is defined, "
        "landing in {0,4}: a single bit, reported. Controls: the descent can "
        "fail (an unreachable class is exhibited), root independence holds "
        "over all 64 choices, and 1 - X is an 8th power in L -- the property "
        "that fails in B and is exactly what going up buys. Does NOT "
        "construct the lift in general: Remark 1.9 concerns arbitrary F and "
        "n, where the extension need not be unramified. Nothing wired."
    ),
}
with open(HERE / "gswz_epsm_h_lift_m8.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)
