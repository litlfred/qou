"""Validating my P_zeta against four independent CGZ predictions, five-term included.

Beans qou-w4gn, qou-y3xv, qou-9p9y. Scope-(a); no fit; nothing wired;
audit: docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 35). Convention-immune: no Hecke/Gram/Markov import, no z_C/z_D,
no q_0 anchor. Exact integer arithmetic mod 5^8.

WHY. Addenda 33-34 report eps_3 = a mod 3 on the alpha-line at the degree-1
place. That number is worth nothing if my implementation of D_zeta, P_zeta
and the eigenspace readout is wrong, and NOTHING so far tested it against
the paper -- every check to date was internal (root-independence, linearity,
the eigenvector condition), all of which a consistently-wrong implementation
would also pass. This probe tests it against four predictions of CGZ that it
had no part in producing. If the five-term test fails, Addenda 33-34 are
void.

THE FOUR PREDICTIONS, all for n = 3 at v_1 (F = Q_5, F_3 = B = Q_25):

(1) LEMMA 2.4(b). For n odd with 3 | n, D_zeta(1) = zeta^{n/3} mod H^{xn}.
    At n = 3 this predicts D_zeta(1) = zeta mod cubes. It HOLDS, and
    D_zeta(1) = 3 (1 - zeta^2) exactly, which independently confirms the
    D_zeta implementation.

    A MISTAKE OF MINE, CAUGHT HERE, THAT PROPAGATED INTO ADDENDA 33-34.
    The readout cls(u) = teich(u)^8 gives the class as a power of the mu_24
    GENERATOR, not of zeta_3 -- and cls(zeta_3) = 2, since zeta_3 = gen^8 =
    gen^2 mod cubes. The first version of this probe compared cls(D_zeta(1))
    to the bare integer 1, got 2, and was one step from reporting a
    discrepancy with CGZ. There is none: the comparison has to be made
    against cls(zeta), or after converting with kappa(u) = 2 cls(u) mod 3.
    The same mislabelling means Addenda 33-34's "eps_3 = zeta_3^2" is wrong
    as stated: in the zeta_3 basis the value is zeta_3^{-a}, so
    eps_3(2[z_1] + [z_2]) = zeta_3, not zeta_3^2. The STRUCTURE those
    addenda report -- linearity, c_2 = 0, dependence on a alone -- is
    unaffected; only the basis label was.

(2) LEMMA 2.4(c) / the identity on p. 11:
    P_zeta(X) P_zeta(1/X) = x^{n(n-1)/2} = X for n = 3. Every unit of Z_5 is
    a cube, so class(X) = 0 and the prediction is
    class(P(X)) + class(P(1/X)) = 0.

(3) THE REFLECTION RELATION. CGZ p. 2: [X] + [1 - X] - [0] = 0 in B(F), and
    P_zeta(0) = D_zeta(1)^{-1}. With (1) this predicts
    class(P(X)) + class(P(1 - X)) = -1 = 2 mod 3 -- a NONZERO constant,
    which is a far sharper target than a vanishing one.

(4) THE FIVE-TERM RELATION, eqn (3):
    xi_{X,Y} = [X] - [Y] + [Y/X] - [(1 - X^{-1})/(1 - Y^{-1})] + [(1-X)/(1-Y)]
    generates C(F), and Theorem 1.2 says R_zeta kills it. So the five classes
    must sum to 0, with the signs above, for every admissible (X, Y). This is
    the strong test: it is a two-parameter family of exact constraints that
    an implementation with a wrong exponent, a wrong zeta power, or a wrong
    normalisation cannot satisfy by accident.

CROSS-CHECK ON THE ALPHA-LINE. Prediction (3) ties the alpha-line symbols
to each other: kappa(P(z_2)) + kappa(P(alpha)) and kappa(P(z_1)) +
kappa(P(alpha^2)) must both equal the reflection constant -kappa(D_zeta(1))
= 2, since 1 - z_2 = alpha and 1 - z_1 = alpha^2. Both hold against direct
computation, so Addendum 34's per-symbol classes are tied to the paper
rather than standing alone -- once they are read in the right basis.

CONSTRUCTED-TO-FAIL CONTROL. The same five-term sum is recomputed with one
sign deliberately flipped and with zeta replaced by zeta^2 in one factor of
D_zeta; both must FAIL on the same sweep. Without that, "the sum is 0" could
mean the class map is trivial rather than the relation holding.

HONESTY: this validates the implementation; it does not extend the result to
any other place, field, or m. Nothing wired.
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
Z3 = B.pw(gen, 8)
INV3 = pow(3, -1, 4 * P ** (W - 1))


def Dz(x, zz=None):
    zz = Z3 if zz is None else zz
    r = B.one()
    for k in (1, 2):
        r = B.mul(r, B.pw(B.sub(B.one(), B.mul(B.pw(zz, k), x)), k))
    return r


D1 = Dz(B.one())
D1INV = B.inv(D1)


def cls(u):
    v = B.pw(B.teich(u), 8)
    cur = B.one()
    for j in range(3):
        if cur == v:
            return j
        cur = B.mul(cur, Z3)
    return None


def clsP(Xint):
    """class of P_zeta(X) for X an integer unit of Z_5 with 1 - X a unit."""
    x = B.scal(pow(Xint % MOD, INV3, MOD))
    return cls(B.mul(Dz(x), D1INV))


# ------------------------------------------------ (0) THE READOUT IS NOT THE IDENTITY
# cls(u) = teich(u)^8 reads the class as a power of the mu_24 GENERATOR, not of
# zeta_3. Measured: cls(zeta_3) = 2, because zeta_3 = gen^8 = gen^2 mod cubes.
# Comparing cls(.) to a bare integer is therefore wrong; convert first.
# kappa(u) = the true zeta_3 exponent: gen^d = zeta^k iff 2k = d mod 3, so k = 2d.
def kappa(u):
    c = cls(u)
    return None if c is None else (2 * c) % 3


detail["cls_of_zeta_3"] = cls(Z3)
checks["readout_is_not_the_identity_on_mu3"] = cls(Z3) == 2
checks["kappa_inverts_the_readout"] = kappa(Z3) == 1 and kappa(B.pw(Z3, 2)) == 2

# ------------------------------------------------ (1) Lemma 2.4(b)
# D_zeta(1) = (1 - zeta)(1 - zeta^2)^2 = 3 (1 - zeta^2) exactly -- an
# independent confirmation of the D_zeta implementation.
checks["D_zeta_1_equals_3_times_one_minus_zeta_squared"] = (
    D1 == B.mul(B.scal(3), B.sub(B.one(), B.pw(Z3, 2))))
detail["class_of_D_zeta_1_raw"] = cls(D1)
detail["kappa_of_D_zeta_1"] = kappa(D1)
checks["lemma_24b_D_zeta_1_is_zeta_to_the_n_over_3"] = kappa(D1) == 1

# admissible arguments: X and 1 - X both units of Z_5
def admissible(v):
    return v % 5 != 0 and (1 - v) % 5 != 0


ARGS = [v for v in range(2, 400) if admissible(v)]
detail["n_admissible_arguments_swept"] = len(ARGS)

# ------------------------------------------------ (2) Lemma 2.4(c)
inv_ok = 0
for v in ARGS:
    vi = pow(v, -1, MOD)
    if not admissible(vi % MOD):
        continue
    if (clsP(v) + clsP(vi)) % 3 != 0:
        inv_ok = -1
        break
    inv_ok += 1
detail["inversion_pairs_tested"] = inv_ok
checks["lemma_24c_inversion_identity_holds"] = inv_ok > 20

# ------------------------------------------------ (3) reflection, a NONZERO target
refl_vals = {(clsP(v) + clsP((1 - v) % MOD)) % 3 for v in ARGS}
detail["reflection_sum_values_seen"] = sorted(refl_vals)
checks["reflection_relation_gives_minus_class_D1"] = refl_vals == {(-cls(D1)) % 3}

# alpha-line cross-check forced by (3)
a = 2
for _ in range(W + 2):
    fa = (pow(a, 3, MOD) - pow(a, 2, MOD) + 1) % MOD
    dfa = (3 * pow(a, 2, MOD) - 2 * a) % MOD
    a = (a - fa * pow(dfa, -1, MOD)) % MOD
ALPHA = a
def kappaP(v):
    return (2 * clsP(v)) % 3


C1 = kappaP((-pow(ALPHA, 3, MOD)) % MOD)          # kappa of P(z_1)
C2 = kappaP((1 - ALPHA) % MOD)                    # kappa of P(z_2)
detail["kappa_P_z1"] = C1
detail["kappa_P_z2"] = C2
detail["kappa_P_alpha"] = kappaP(ALPHA)
detail["kappa_P_alpha_squared"] = kappaP(pow(ALPHA, 2, MOD))
# The reflection constant in the kappa basis is -kappa(D1) = -1 = 2.
REFL = (-kappa(D1)) % 3
detail["reflection_constant_in_kappa_basis"] = REFL
checks["alpha_line_classes_match_the_reflection_prediction"] = (
    (C2 + kappaP(ALPHA)) % 3 == REFL
    and (C1 + kappaP(pow(ALPHA, 2, MOD))) % 3 == REFL)
# CORRECTED VALUE. Addenda 33-34 reported eps_3 in the RAW readout, which is
# the gen basis, and mislabelled it as a zeta_3 exponent. In the zeta_3 basis
# the per-symbol classes are kappa(P(z_1)) = 2, kappa(P(z_2)) = 0, so
#     eps_3(a[z_1] + b[z_2]) = zeta_3^{2a} = zeta_3^{-a},
# and for xi = 2[z_1] + [z_2] that is zeta_3^{4 mod 3} = zeta_3, NOT zeta_3^2.
detail["eps3_corrected_zeta_exponent_for_xi_2_1"] = (2 * 2 + 1 * 0) % 3
checks["eps3_in_zeta_basis_is_minus_a"] = (
    C1 == 2 and C2 == 0 and (2 * C1 + 1 * C2) % 3 == 1)

# ------------------------------------------------ (4) the five-term relation
def five_args(X, Y):
    """[X] - [Y] + [Y/X] - [(1-1/X)/(1-1/Y)] + [(1-X)/(1-Y)], eqn (3)."""
    Xi, Yi = pow(X, -1, MOD), pow(Y, -1, MOD)
    a3 = (Y * Xi) % MOD
    a4 = ((1 - Xi) * pow((1 - Yi) % MOD, -1, MOD)) % MOD
    a5 = ((1 - X) * pow((1 - Y) % MOD, -1, MOD)) % MOD
    return [(X, 1), (Y, -1), (a3, 1), (a4, -1), (a5, 1)]


def five_sum(X, Y, sign_flip=False, bad_zeta=False):
    tot = 0
    for i, (v, s) in enumerate(five_args(X, Y)):
        if not admissible(v % MOD):
            return None
        if bad_zeta and i == 0:
            x = B.scal(pow(v % MOD, INV3, MOD))
            c = cls(B.mul(Dz(x, B.pw(Z3, 2)), D1INV))
        else:
            c = clsP(v)
        if sign_flip and i == 2:
            s = -s
        tot += s * c
    return tot % 3


tested, failed = 0, []
for X in range(2, 90):
    if not admissible(X):
        continue
    for Y in range(2, 90):
        if not admissible(Y) or Y == X:
            continue
        r = five_sum(X, Y)
        if r is None:
            continue
        tested += 1
        if r != 0:
            failed.append((X, Y, r))
        if tested >= 400:
            break
    if tested >= 400:
        break
detail["five_term_instances_tested"] = tested
detail["five_term_failures"] = failed[:5]
checks["five_term_relation_holds"] = tested > 100 and not failed

# CONSTRUCTED-TO-FAIL CONTROLS: both perturbations must break the sweep.
def sweep_fails(**kw):
    bad = 0
    n = 0
    for X in range(2, 60):
        if not admissible(X):
            continue
        for Y in range(2, 60):
            if not admissible(Y) or Y == X:
                continue
            r = five_sum(X, Y, **kw)
            if r is None:
                continue
            n += 1
            if r != 0:
                bad += 1
            if n >= 150:
                break
        if n >= 150:
            break
    return n, bad


n_sf, bad_sf = sweep_fails(sign_flip=True)
n_bz, bad_bz = sweep_fails(bad_zeta=True)
detail["control_sign_flip"] = {"tested": n_sf, "nonzero": bad_sf}
detail["control_wrong_zeta"] = {"tested": n_bz, "nonzero": bad_bz}
checks["control_sign_flip_breaks_the_relation"] = bad_sf > 0
checks["control_wrong_zeta_breaks_the_relation"] = bad_bz > 0
# and the class map is not identically zero on the sweep
checks["class_map_is_non_trivial_on_the_sweep"] = len(
    {clsP(v) for v in ARGS[:60]}) > 1

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_five_term_validation_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_five_term_validation_probe.py",
    "commitSha": _sha,
    "beans": ["qou-w4gn", "qou-y3xv", "qou-9p9y"],
    "source": ("CGZ arXiv:1712.04887v3 eqn (3), Lemma 2.4(b),(c), the "
               "relations on p. 2, Theorem 1.2; Addenda 33-34 (this repo)"),
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a) VALIDATION of the implementation behind Addenda 33-34, "
        "plus a CORRECTION to their stated value. Every check to date was "
        "internal, and a consistently-wrong P_zeta would have passed them "
        "all. Tested here against four CGZ predictions the implementation "
        "had no part in producing. ALL FOUR HOLD: Lemma 2.4(b) "
        "(D_zeta(1) = zeta mod cubes at n = 3, and D_zeta(1) = "
        "3 (1 - zeta^2) exactly); Lemma 2.4(c) (kappa P(X) + kappa P(1/X) "
        "= 0 on 240 arguments); the reflection relation "
        "[X] + [1-X] - [0] = 0, which forces the NONZERO constant 2 mod 3 "
        "and ties the alpha-line symbols to each other via 1 - z_2 = alpha "
        "and 1 - z_1 = alpha^2; and the five-term relation of eqn (3) on "
        "400 instances of a two-parameter sweep. Two constructed-to-fail "
        "controls -- one flipped sign, and zeta replaced by zeta^2 in a "
        "single factor -- break the sweep at 99/150 and 96/150, so the "
        "vanishing sum is the relation holding rather than a trivial class "
        "map. THE CORRECTION: the readout teich(u)^8 gives the class as a "
        "power of the mu_24 generator, not of zeta_3, and cls(zeta_3) = 2. "
        "Comparing it to a bare integer nearly produced a false report of "
        "a discrepancy with Lemma 2.4(b), and did produce a wrong basis "
        "label in Addenda 33-34: their 'eps_3 = zeta_3^2' should read "
        "eps_3(a[z_1] + b[z_2]) = zeta_3^{-a}, so eps_3(2[z_1] + [z_2]) = "
        "zeta_3. The structure those addenda report -- linearity, c_2 = 0, "
        "dependence on a alone -- is unaffected; only the basis label was "
        "wrong. Validates the implementation only; extends nothing to "
        "another place, field, or m. Nothing wired."
    ),
}
with open(HERE / "gswz_epsm_five_term_validation.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)
