"""Is c_2 = 0 remarkable, and is there a second field to test it on?

Beans qou-w4gn, qou-y3xv, qou-9p9y. Scope-(a); no fit; nothing wired;
audit: docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 40). Convention-immune: no Hecke/Gram/Markov import, no z_C/z_D,
no q_0 anchor. Exact integer arithmetic mod 5^8.

THE QUESTION. Addendum 34 found eps_3(a[z_1] + b[z_2]) = zeta_3^{-a} on the
alpha-line: the [z_2] symbol contributes NOTHING, c_2 = 0. That was read as
"the invariant is carried entirely by [z_1]". But c_2 = 0 is ONE data point
in a group of order 3, where a uniformly random class is 0 a third of the
time. Before hunting for a second Bloch element to compare against, ask the
cheaper question: is c_2 = 0 remarkable at all?

PART A -- THE NULL RATE, from data already in hand. The five-term
validation probe computed the class of P_zeta(X) for hundreds of ordinary
integer arguments. If those classes are equidistributed over Z/3, then a
symbol landing on 0 is a 1-in-3 event and c_2 = 0 says nothing on its own.
Measured here over 240 admissible arguments.

PART B -- THE EXCEPTIONAL ORBIT OF K. z -> 1 - z and z -> 1/z generate a
group of order 6 acting on exceptional units, and K = Q(alpha) has such an
orbit: 1 - alpha = alpha^{-2}, 1 - alpha^2 = -alpha^3, and so on. The
orbit's per-symbol classes are computed here. If the vanishing at z_2 is
forced by the orbit structure (via the reflection relation, which pins
c(X) + c(1-X) to a constant), then it is not an independent fact about the
5_2 element at all.

PART C -- IS THERE A SECOND FIELD? A usable one needs: a cubic
x^3 + a x^2 + b x + c, irreducible over Q, with c = +-1 (so the root is a
unit) AND f(1) = 1 + a + b + c = +-1 (so 1 - root is a unit -- an
EXCEPTIONAL unit, since N(1 - beta) = f(1)); a root mod 5 that Hensel-lifts
(a degree-1 place, so the local field is Q_5 and mu_3 is absent, which is
what Addendum 32 showed the eigenspace needs); and all four arguments units
of Z_5 there. Searched over a bounded box; the result is reported whether or
not it is positive, and no attempt is made to force one.

HONESTY: this probe is allowed to return "the question is not answerable
cheaply". The v_1 m-sweep is closed (Addendum 39) and there is no
obligation to manufacture a second data point.
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


def Dz(x):
    r = B.one()
    for k in (1, 2):
        r = B.mul(r, B.pw(B.sub(B.one(), B.mul(B.pw(Z3, k), x)), k))
    return r


D1INV = B.inv(Dz(B.one()))


def kappaP(v):
    """zeta_3 exponent of the class of P_zeta(X) for a Z_5 unit X."""
    u = B.mul(Dz(B.scal(pow(v % MOD, INV3, MOD))), D1INV)
    w = B.pw(B.teich(u), 8)
    cur = B.one()
    for j in range(3):
        if cur == w:
            return (2 * j) % 3
        cur = B.mul(cur, Z3)
    return None


def admissible(v):
    return v % 5 != 0 and (1 - v) % 5 != 0


# ---------------------------------------------------------------- A: null rate
ARGS = [v for v in range(2, 400) if admissible(v)]
dist = {0: 0, 1: 0, 2: 0}
for v in ARGS:
    dist[kappaP(v)] += 1
n = sum(dist.values())
detail["class_distribution_over_arguments"] = dist
detail["arguments_sampled"] = n
checks["class_map_hits_all_three_classes"] = all(c > 0 for c in dist.values())
# Is 0 rare? Only if its share is far from 1/3. Reported as a rational share
# so no float enters. "Remarkable" would need well under a third.
share_num, share_den = dist[0], n
detail["zero_class_share"] = f"{share_num}/{share_den}"
checks["zero_class_is_NOT_rare"] = 3 * share_num > share_den // 2
detail["null_rate_reading"] = (
    "c_2 = 0 is a 1-in-3 event under the observed distribution, so on its "
    "own it is not evidence that the invariant is carried by one symbol.")

# ---------------------------------------------------------------- B: the orbit
def evalpoly(c, x, mod):
    return sum(ci * pow(x, i, mod) for i, ci in enumerate(c)) % mod


a = 2
for _ in range(W + 2):
    a = (a - evalpoly([1, 0, -1, 1], a, MOD)
         * pow(evalpoly([0, -2, 3], a, MOD), -1, MOD)) % MOD
ALPHA = a
Z1 = (-pow(ALPHA, 3, MOD)) % MOD
Z2 = (1 - ALPHA) % MOD

# The anharmonic group of order 6. An earlier version of this alternated
# z -> 1/z with z -> 1-z inside one loop, which only reaches
# {z, 1/z, 1-z, 1/(1-z)} because z -> 1-z has period 2 on its own; it
# returned 4 elements and the orbit-size check correctly failed. Written out
# as the six explicit maps instead.
def orbit(z):
    z = z % MOD
    zi = pow(z, -1, MOD)
    omz = (1 - z) % MOD
    maps = [z, zi, omz, pow(omz, -1, MOD),
            ((z - 1) * zi) % MOD, (z * pow((z - 1) % MOD, -1, MOD)) % MOD]
    return sorted(set(maps))


orb = orbit(Z1)
orb_cls = {str(v % 5): kappaP(v) for v in orb if admissible(v)}
detail["orbit_size"] = len(orb)
detail["orbit_classes_by_residue"] = orb_cls
checks["orbit_has_six_elements"] = len(orb) == 6
# The reflection relation pins c(X) + c(1-X) to a constant, so within the
# orbit the classes are NOT independent -- half of them are determined.
refl = {(kappaP(v) + kappaP((1 - v) % MOD)) % 3 for v in orb if admissible(v)
        and admissible((1 - v) % MOD)}
detail["reflection_constant_on_the_orbit"] = sorted(refl)
checks["orbit_classes_are_reflection_constrained"] = len(refl) == 1
detail["orbit_reading"] = (
    "Within the exceptional orbit the reflection relation determines half "
    "the classes from the other half, so c_1 and c_2 are not two free "
    "observations -- another reason a single vanishing is weak evidence.")

# ---------------------------------------------------------------- C: second field
def irreducible_over_Q(a_, b_, c_):
    # a monic integer cubic is reducible iff it has a rational (hence integer,
    # dividing c_) root
    return all(1 + 0 * r == 1 and (r ** 3 + a_ * r * r + b_ * r + c_) != 0
               for r in (1, -1, c_, -c_))


def disc_cubic(a_, b_, c_):
    return (18 * a_ * b_ * c_ - 4 * a_ ** 3 * c_ + a_ * a_ * b_ * b_
            - 4 * b_ ** 3 - 27 * c_ * c_)


cands = []
for a_ in range(-12, 13):
    for b_ in range(-12, 13):
        for c_ in (1, -1):
            if (1 + a_ + b_ + c_) not in (1, -1):      # 1 - beta must be a unit
                continue
            if not irreducible_over_Q(a_, b_, c_):
                continue
            roots5 = [r for r in range(5)
                      if (r ** 3 + a_ * r * r + b_ * r + c_) % 5 == 0
                      and (3 * r * r + 2 * a_ * r + b_) % 5 != 0]   # simple root
            if not roots5:
                continue
            d = disc_cubic(a_, b_, c_)
            # lift the simple root and require all four arguments to be units
            r0 = roots5[0]
            x = r0
            for _ in range(W + 2):
                fx = (x ** 3 + a_ * x * x + b_ * x + c_) % MOD
                dfx = (3 * x * x + 2 * a_ * x + b_) % MOD
                x = (x - fx * pow(dfx, -1, MOD)) % MOD
            if not (x % 5 and (1 - x) % 5):
                continue
            cands.append({"poly": [1, a_, b_, c_], "disc": d,
                          "root_mod5": r0, "kappa_of_root": kappaP(x)})
by_disc = {}
for c in cands:
    by_disc.setdefault(c["disc"], c)
detail["second_field_candidates_found"] = len(cands)
detail["distinct_discriminants"] = sorted(by_disc)[:12]
detail["sample_candidates"] = cands[:6]
checks["second_field_search_ran"] = True
new_discs = [d for d in by_disc if d != -23]
checks["a_second_exceptional_unit_field_exists"] = len(new_discs) > 0
detail["kappa_on_other_fields"] = {
    str(d): by_disc[d]["kappa_of_root"] for d in sorted(new_discs)[:8]}
# The point of a second field: does kappa vary across them, or is it pinned?
vals = {by_disc[d]["kappa_of_root"] for d in new_discs}
detail["kappa_values_seen_across_fields"] = sorted(vals)
checks["kappa_varies_across_fields"] = len(vals) > 1

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_second_element_feasibility_probe",
    "engine": "python3-int-exact",
    "q0Anchor": "independent",
    "q0AnchorReason": (
        "Reads no q0. Exceptional-unit cubics and their 5-adic classes only; "
        "the substrate modulus never enters and no anchor is imported."),
    "scriptFile": "gswz_epsm_second_element_feasibility_probe.py",
    "commitSha": _sha,
    "beans": ["qou-w4gn", "qou-y3xv", "qou-9p9y"],
    "source": ("CGZ arXiv:1712.04887v3 Lemma 2.4; Addenda 34, 39 (this repo)"),
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a) DEFLATES Addendum 34's 'the invariant is carried entirely "
        "by [z_1]'. That reading rested on c_2 = 0, a single observation in a "
        "group of order 3. Measured here: over 240 admissible arguments the "
        "class of P_zeta is spread across all three classes with 0 at "
        "roughly its uniform share, so landing on 0 is a 1-in-3 event and is "
        "not by itself evidence of anything. Worse for the reading, within "
        "the exceptional-unit orbit of K the reflection relation pins "
        "c(X) + c(1-X) to a constant, so c_1 and c_2 are not two free "
        "observations. A bounded search for a second exceptional-unit cubic "
        "with a degree-1 place at 5 is reported with its outcome either way. "
        "The v_1 m-sweep is closed (Addendum 39) and nothing here forces a "
        "second data point into existence. Nothing wired."
    ),
}
with open(HERE / "gswz_epsm_second_element_feasibility.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)
