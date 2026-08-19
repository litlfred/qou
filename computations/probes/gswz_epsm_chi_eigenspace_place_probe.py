"""The eps_m invariant's home is a chi^{-1}-EIGENSPACE, and my base field destroyed it.

Beans qou-w4gn, qou-y3xv, qou-9p9y. Scope-(a); no fit; nothing wired;
audit: docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 32). Convention-immune: no Hecke/Gram/Markov import, no z_C/z_D,
no q_0 anchor.

WHAT I HAD NOT READ. CGZ arXiv:1712.04887v3 Remark 1.9 (p. 8) says
Gangl-Kontsevich "did not check in general that the image of P_zeta
could be lifted to a suitable element R_zeta in (F_n^x / F_n^{xn})^{chi^{-1}}".
So the invariant does NOT live in H^x/H^{xn} (that is only P_zeta), and
not in a bare F^x/(F^x)^n either. It lives in the chi^{-1}-EIGENSPACE of
F_n^x/(F_n^x)^n, where F_n = F(zeta_n) and chi is the cyclotomic
character of Gal(F_n/F). Lemma 2.4(e) is the eigenvector condition.

Also, Lemma 2.3 (p. 9) is an ISOMORPHISM F^x/F^{xn} = Hom(Phi, mu) =
H^1(Phi, mu). So computing the Kummer cocycle sigma -> sigma(x)/x is the
same object as the class I already computed in Addendum 31, under an
isomorphism -- it cannot rescue the collapse, and this probe does not
attempt it. That is a negative worth recording: the H^1 reformulation is
not a new route.

THE DIAGNOSIS. An eigenspace is a proper subgroup only when the group
Gal(F_n/F) is nontrivial, i.e. only when the base field does NOT already
contain mu_n. Every field in my programme was F = Q_5(mu_{624m}), which
contains mu_m. So Gal(F_n/F) = 1, the condition of Lemma 2.4(e) is
vacuous, and the "eigenspace" is the whole group. I destroyed the
structure that carries the invariant before computing anything.

THE CORRECT BASE, AND IT IS PLACE-DEPENDENT. The Nahm/alpha-line field is
K = Q(alpha) with alpha^3 - alpha^2 + 1 = 0 (so 1 - z_1 = alpha^2,
1 - z_2 = alpha, z_1 = -alpha^3). Over Q_5 that polynomial factors as
(x - 2)(x^2 + x + 2), giving two places:

    v_1 (degree 1): K_{v_1} = Q_5      mu_3 NOT in F -> Gal(F_3/F) = Z/2
    v_2 (degree 2): K_{v_2} = Q_25     mu_3 IS in F  -> Gal(F_3/F) = 1

Only v_1 carries the eigenspace structure. At v_1, F_3 = Q_25 = the base
B of my m = 2, 3 descent probes.

WHAT THIS REVERSES. Addendum 31 bracketed the invariant between "B = Q_25
too small" and "F = Q_5(mu_1872) too large". The first half is WRONG:
B = Q_25 is exactly F_n at the degree-1 place, and my chi_B = teich(.)^8
map is exactly the projection onto its chi^{-1}-eigenspace. What failed at
the B level was never the field -- it was the lift of P_zeta from H down
to F_n, which is precisely the step Remark 1.9 flags as unchecked. The
second half of the bracket stands.

MEASURED HERE. B^x/(B^x)^3 has order 9 (Teichmueller line x valuation
line; 1 + 5O is uniquely 3-divisible). Frobenius phi_5 acts by 5 = -1
mod 3 on the Teichmueller line and by +1 on the valuation line, while
chi^{-1}(phi_5) = 2 = -1. So the eigenspace is the Teichmueller line,
order 3 -- a PROPER subgroup, and 5 is a witness outside it. Non-vacuous,
unlike the F-level class of Addendum 31, which was identically 0 on all
23 base arguments.

HONESTY: no eps_m value is claimed at any m >= 3. This probe relocates
the target group and shows it is non-vacuous; the lift H -> F_n remains
open. The m = 2 value of PR #4968 is untouched.
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
    """Unramified extension (Z/5^W)[x]/(x^n - sum f[j] x^j), exact integers."""

    def __init__(self, f):
        self.f = [c % MOD for c in f]
        self.n = len(f)

    def one(self):
        return [1] + [0] * (self.n - 1)

    def scal(self, c):
        return [c % MOD] + [0] * (self.n - 1)

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

    def is_unit(self, a):
        return any(c % P for c in a)

    def unit_order(self):
        return (P ** self.n - 1) * P ** (self.n * (W - 1))

    def inv(self, a):
        return self.pw(a, self.unit_order() - 1)

    def teich(self, a):
        return self.pw(a, (P ** self.n) ** W)


# ---------------------------------------------------------------- the two places
poly = [1, 0, -1, 1]          # 1 - x^2 + x^3, coefficients ascending


def evalpoly(c, x, mod):
    return sum(ci * pow(x, i, mod) for i, ci in enumerate(c)) % mod


roots_mod5 = [a for a in range(5) if evalpoly(poly, a, 5) == 0]
detail["roots_of_alpha_poly_mod_5"] = roots_mod5
# (x - 2)(x^2 + x + 2) = x^3 + x^2 + 2x - 2x^2 - 2x - 4 = x^3 - x^2 - 4 = x^3 - x^2 + 1 mod 5
quad_irred = all(evalpoly([2, 1, 1], a, 5) for a in range(5))
checks["alpha_poly_factors_as_predicted"] = roots_mod5 == [2] and quad_irred

# Hensel-lift the degree-1 root: alpha lives in Z_5, so K_{v_1} = Q_5.
a = 2
for _ in range(W + 2):
    fa = evalpoly(poly, a, MOD)
    dfa = evalpoly([0, -2, 3], a, MOD)          # derivative 3x^2 - 2x
    a = (a - fa * pow(dfa, -1, MOD)) % MOD
ALPHA = a
checks["alpha_v1_hensel_root_exact"] = (
    evalpoly(poly, ALPHA, MOD) == 0 and ALPHA % 5 == 2)
detail["alpha_at_v1_mod_5^4"] = ALPHA % (5 ** 4)

z1 = (-pow(ALPHA, 3, MOD)) % MOD
z2 = (1 - ALPHA) % MOD
checks["nahm_line_elements_live_in_Q5_at_v1"] = all(
    v % 5 and (1 - v) % 5 for v in (z1, z2))
checks["z1_identity_1_minus_z1_eq_alpha_sq"] = (
    (1 - z1) % MOD == pow(ALPHA, 2, MOD))

# mu_3 is NOT in Q_5: the only cube root of 1 is 1 itself.
cube_roots_Q5 = [u for u in range(1, MOD) if u % 5 and pow(u, 3, MOD) == 1]
detail["cube_roots_of_unity_in_Z_5^W"] = cube_roots_Q5
checks["mu3_not_in_Q5"] = cube_roots_Q5 == [1]

# ... but IS in Q_25 = F_3 at v_1.
B = Unram([-2, -1])                              # x^2 = -x - 2
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
checks["mu24_generator_found_in_Q25"] = gen is not None
Z3 = B.pw(gen, 8)
checks["mu3_in_Q25"] = (B.pw(Z3, 3) == B.one() and Z3 != B.one())
# CONTROL on the search style above: the same brute force, run in B's residue
# field, DOES turn up three cube roots -- so the empty answer over Q_5 is a
# fact about Q_5, not a search that cannot find anything.
cube_roots_F25 = [(c0, c1) for c0 in range(5) for c1 in range(5)
                  if (c0 or c1)
                  and B.pw(B.teich([c0, c1]), 3) == B.one()]
detail["cube_roots_of_unity_in_F25"] = cube_roots_F25
checks["cube_root_search_finds_three_in_Q25"] = len(cube_roots_F25) == 3

# Gal(F_3/F) = Gal(Q_25/Q_5) = <phi_5>, order 2, acting on mu_24 by t -> t^5.
checks["frobenius_has_order_2_on_mu24"] = (
    B.pw(gen, 5) != gen and B.pw(gen, 25) == gen)
# phi_5 fixes the base pointwise: Teichmueller lifts of F_5 are Fermat-fixed.
checks["frobenius_fixes_base_scalars"] = all(
    B.pw(B.teich(B.scal(c)), 5) == B.teich(B.scal(c)) for c in (1, 2, 3, 4))

# chi(phi_5) = 5 mod 3 = 2; chi^{-1}(phi_5) = 2^{-1} = 2 = -1 mod 3.
CHI = 5 % 3
CHI_INV = pow(CHI, -1, 3)
detail["chi_of_frobenius"] = CHI
detail["chi_inv_of_frobenius"] = CHI_INV
checks["chi_inv_of_frob_is_minus_one"] = CHI_INV == 2

# ---------------------------------------------------------------- B^x/(B^x)^3
# 1 + 5O is uniquely 3-divisible, so it is trivial in the quotient.
one_plus_5O_cubes = True
for c0 in range(5):
    for c1 in range(5):
        u = [(1 + 5 * c0) % MOD, (5 * c1) % MOD]
        # 1 + 5O is the pro-5 part, of order 5^{n(W-1)}; 3 is invertible there.
        rt = B.pw(u, pow(3, -1, P ** (B.n * (W - 1))))
        if B.pw(rt, 3) != u:
            one_plus_5O_cubes = False
checks["one_plus_5O_is_all_cubes"] = one_plus_5O_cubes


def teich_dlog(t):
    """Discrete log of a mu_24 element to base `gen`."""
    cur = B.one()
    for e in range(24):
        if cur == t:
            return e
        cur = B.mul(cur, gen)
    return None


def unit_class(u):
    """Class of a UNIT of B in B^x/(B^x)^3, as an exponent mod 3."""
    return teich_dlog(B.teich(u)) % 3


# The 9 classes: (Teichmueller exponent mod 3, valuation mod 3).
cls_seen = set()
for e in range(3):
    for v in range(3):
        cls_seen.add((unit_class(B.pw(gen, e)), v))
checks["class_group_has_order_9"] = len(cls_seen) == 9

# Frobenius on the two lines.
frob_teich = [(unit_class(B.pw(gen, e)), unit_class(B.pw(B.pw(gen, e), 5)))
              for e in range(3)]
detail["frobenius_on_teichmuller_line"] = frob_teich
checks["frobenius_acts_by_minus_one_on_teichmuller_line"] = all(
    b == (-a) % 3 for a, b in frob_teich)
# phi_5(5) = 5 because 5 lies in Q_5, which phi_5 fixes pointwise (checked above).
checks["frobenius_acts_by_plus_one_on_valuation_line"] = (
    checks["frobenius_fixes_base_scalars"])

# The chi^{-1}-eigenspace: {u : phi_5(u) = u^{chi^{-1}}} = {u : phi_5(u) = u^{-1}}.
eigen = [(a, v) for a in range(3) for v in range(3)
         if ((-a) % 3, v) == ((CHI_INV * a) % 3, (CHI_INV * v) % 3)]
detail["chi_inv_eigenspace"] = eigen
checks["eigenspace_is_the_teichmuller_line_order_3"] = (
    sorted(eigen) == [(0, 0), (1, 0), (2, 0)])
# NON-VACUITY CONTROL: it is a PROPER subgroup -- 5 (class (0,1)) is outside.
checks["eigenspace_is_proper_5_is_outside"] = (0, 1) not in eigen
# CONSTRUCTED-TO-FAIL CONTROL: the valuation line fails the eigen condition.
checks["valuation_line_fails_eigen_condition"] = all(
    (a, v) not in eigen for a in range(3) for v in (1, 2))

# My old chi_B = teich(.)^{(25-1)/3} IS this projection: it kills cubes and
# the valuation part, and is injective on the Teichmueller line.
chiB = [B.pw(B.teich(B.pw(gen, e)), 8) for e in range(3)]
checks["old_chi_B_is_the_eigenspace_projection"] = (
    len({tuple(c) for c in chiB}) == 3
    and B.pw(B.teich(B.pw(gen, 3)), 8) == B.one())

# ---------------------------------------------------------------- the collapse
# My programme's field F' = Q_5(mu_{624m}) contains mu_3 (3 | 1872), so
# F'_3 = F' and Gal(F'_3/F') = 1: Lemma 2.4(e) constrains nothing.
checks["big_field_contains_mu3_so_condition_is_vacuous"] = (1872 % 3 == 0)
detail["eigenspace_size_at_v1"] = len(eigen)
detail["eigenspace_size_over_big_field"] = 9      # trivial group -> whole group
# Place v_2: K_{v_2} = Q_25 already contains mu_3, so it collapses too.
checks["place_v2_also_collapses"] = checks["mu3_in_Q25"]

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_chi_eigenspace_place_probe",
    "engine": "python3-int-exact",
    "q0Anchor": "independent",
    "q0AnchorReason": (
        "Reads no q0. The eps_m relocation is pure algebraic number theory in Z/5^W and the divisor lattice of 24; the substrate modulus never enters, and no pyhecke/Gram/Markov import exists in the cone."),
    "scriptFile": "gswz_epsm_chi_eigenspace_place_probe.py",
    "commitSha": _sha,
    "beans": ["qou-w4gn", "qou-y3xv", "qou-9p9y"],
    "source": ("CGZ arXiv:1712.04887v3 Remark 1.9 (p. 8), Lemma 2.3 and "
               "Lemma 2.4(a),(d),(e) (pp. 9-10); Addenda 27-31 (this repo)"),
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a) RELOCATION of the target, not a value. CGZ Remark 1.9 "
        "puts the invariant in (F_n^x/(F_n^x)^n)^{chi^{-1}} -- the "
        "chi^{-1}-eigenspace of F_n = F(zeta_n) -- with P_zeta in "
        "H^x/H^{xn} only its image. An eigenspace is proper only when "
        "F does not contain mu_n; every field in my programme was "
        "Q_5(mu_{624m}), which does, so the condition of Lemma 2.4(e) "
        "was vacuous throughout. The alpha-line field K = Q(alpha), "
        "alpha^3 - alpha^2 + 1 = 0, has two places over 5: at v_1 "
        "(degree 1) K_v = Q_5 lacks mu_3 and F_3 = Q_25, giving "
        "Gal = Z/2 and an eigenspace of order 3 inside a group of order "
        "9 -- non-vacuous, with 5 a witness outside it; at v_2 K_v = "
        "Q_25 already contains mu_3 and collapses. This REVERSES half of "
        "Addendum 31: B = Q_25 is not 'too small', it is exactly F_n at "
        "v_1, and my chi_B = teich(.)^8 is exactly the eigenspace "
        "projection. What failed at the B level was the lift of P_zeta "
        "from H to F_n -- the step Remark 1.9 flags as unchecked -- not "
        "the choice of field. Separately, Lemma 2.3 is an isomorphism "
        "F^x/F^{xn} = H^1(Phi, mu), so the Kummer-cocycle reformulation "
        "computes the same object as Addendum 31 and is not a new route; "
        "no probe was spent on it. No eps_m value is claimed at m >= 3; "
        "the m = 2 result of PR #4968 is untouched."
    ),
}
with open(HERE / "gswz_epsm_chi_eigenspace_place.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)
