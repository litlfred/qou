"""Which m | 24 admit a non-vacuous eps_m at the degree-1 place -- and m = 2 does not.

Beans qou-w4gn, qou-y3xv, qou-9p9y. Scope-(a); no fit; nothing wired;
audit: docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 37). Convention-immune: no Hecke/Gram/Markov import, no z_C/z_D,
no q_0 anchor. Exact integer arithmetic.

WHY. Addenda 32-35 computed eps_3 at the degree-1 place of K = Q(alpha),
where F = Q_5. Before computing any value at another m it is worth knowing
WHERE a value can exist at all: CGZ's invariant lives in the
chi^{-1}-eigenspace of F_m^x/(F_m^x)^m, and an eigenspace carries
information only when it is a PROPER subgroup. This probe maps that over
the whole divisor lattice of 24 rather than guessing.

MY OWN GUESS WAS WRONG, WHICH IS WHY THIS IS MEASURED. The scheduled note
that queued this work said the eigenspace argument "needs mu_m not in Q_5,
which holds only for m coprime to 4". That is false: mu_m is in Q_5 exactly
when m | 4 (the roots of unity of Q_5 are mu_4, since 1 + 5 Z_5 is
torsion-free), so m = 8, 12, 24 qualify despite sharing a factor with 4.

THE CENSUS. For every m | 24, F_m = Q_5(zeta_m) is unramified (5 does not
divide m) of degree d = ord_m(5), and

    F_m^x / (F_m^x)^m  =  Z/m  x  Z/m
                          ^Teichmueller  ^valuation

(the 1 + 5 O part is uniquely m-divisible for gcd(m,5) = 1, hence trivial
in the quotient). Frobenius multiplies the Teichmueller exponent by 5 and
fixes the valuation, while chi^{-1}(phi_5) = 5^{-1} mod m. The eigenspace is
computed here by BRUTE FORCE over all m^2 classes with that action, and only
then compared against the closed form m . gcd(m, 4) -- so the formula is
checked, not assumed.

THE RESULT, and it splits three ways:

  m in {1, 2, 4}      G = Gal(F_m/F) is TRIVIAL (F_m = F = Q_5), the
                      eigenspace is the whole group, and no value exists.
  m = 3               gcd(m, w_F) = 1 with w_{Q_5} = 4, so Theorem 1.2
                      applies directly and the lift is UNIQUE. This is the
                      case Addenda 33-35 computed.
  m in {6, 8, 12, 24} G = Z/2 and the eigenspace is proper, but
                      gcd(m, 4) > 1, so by Proposition 2.5 only
                      R_zeta(xi)^{w_F} is defined. That power is still
                      NON-TRIVIAL in these groups, so information survives.

AND THE PART THAT CORRECTS ME. m = 2 is vacuous, and not merely at this
place -- FOR EVERY FIELD OF CHARACTERISTIC NOT 2. Since -1 is a non-trivial
square root of 1 and lies in every such field, F_2 = F always, G is always
trivial, and w_F is always even, so gcd(2, w_F) = 2 > 1 and only
R_zeta(xi)^{w_F} is defined -- which is 1 in a group of exponent 2. So
CGZ's Theorem 1.2 NEVER applies at n = 2 and there is no non-vacuous m = 2
invariant to compute.

Throughout this arc I have written that "the m = 2 result of PR #4968 is
untouched", treating it as the one solid value. Addendum 30 had already
re-scoped it as measuring my descent-to-base composite rather than CGZ's
invariant; this adds the sharper point that at m = 2 there was never a
non-vacuous CGZ target to hit. The +1 it reports is forced by the group,
not a measurement of anything. That does not make the #4968 computation
wrong -- it makes it empty as a CGZ value.

HONESTY: this is a census of where values can exist, not a value at any new
m. Nothing wired.
"""

import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
checks, detail = {}, {}

P, W = 5, 8
MOD = P ** W
DIVISORS = [m for m in range(1, 25) if 24 % m == 0]
detail["divisors_of_24"] = DIVISORS


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# ---------------------------------------------------------------- mu_m in Q_5?
# Measured, not asserted: search Z/5^W for an element of exact order m.
def mu_m_in_Q5(m):
    for u in range(1, MOD):
        if u % P == 0:
            continue
        if pow(u, m, MOD) == 1 and all(
                pow(u, m // r, MOD) != 1 for r in {q for q in (2, 3) if m % q == 0}):
            return True
    return False


in_Q5 = {m: mu_m_in_Q5(m) for m in DIVISORS}
detail["mu_m_contained_in_Q5"] = in_Q5
checks["mu_m_in_Q5_exactly_when_m_divides_4"] = all(
    in_Q5[m] == (4 % m == 0) for m in DIVISORS)
# THE CORRECTION to my scheduled note: "coprime to 4" would exclude 8, 12, 24.
coprime_to_4 = {m for m in DIVISORS if gcd(m, 4) == 1}
qualifying = {m for m in DIVISORS if not in_Q5[m]}
detail["m_with_mu_m_outside_Q5"] = sorted(qualifying)
detail["m_coprime_to_4"] = sorted(coprime_to_4)
checks["my_coprime_to_4_guess_was_wrong"] = qualifying != coprime_to_4

# ---------------------------------------------------------------- degrees
def ord_mod(a, m):
    if m == 1:
        return 1
    k, cur = 1, a % m
    while cur != 1:
        cur = (cur * a) % m
        k += 1
    return k


deg = {m: ord_mod(5, m) for m in DIVISORS}
detail["degree_of_F_m_over_Q5"] = deg
checks["degree_is_1_iff_mu_m_in_Q5"] = all(
    (deg[m] == 1) == in_Q5[m] for m in DIVISORS)
checks["all_other_m_give_degree_2"] = all(
    deg[m] == 2 for m in DIVISORS if not in_Q5[m])

# ---------------------------------------------------------------- eigenspaces
# Class group F_m^x/(F_m^x)^m = Z/m (Teichmueller) x Z/m (valuation).
# phi_5: (a, v) -> (5a, v).  chi^{-1}(phi_5) = 5^{-1} mod m.
def eigenspace(m):
    if m == 1:
        return [(0, 0)], 1
    if deg[m] == 1:                       # G trivial: no condition at all
        return [(a, v) for a in range(m) for v in range(m)], m * m
    c = pow(5 % m, -1, m) if gcd(5, m) == 1 else None
    eig = [(a, v) for a in range(m) for v in range(m)
           if ((5 * a) % m, v % m) == ((c * a) % m, (c * v) % m)]
    return eig, m * m


sizes, totals, proper = {}, {}, {}
for m in DIVISORS:
    eig, tot = eigenspace(m)
    sizes[m], totals[m] = len(eig), tot
    proper[m] = len(eig) < tot
detail["eigenspace_size"] = sizes
detail["group_order"] = totals
detail["eigenspace_is_proper"] = proper

# The brute-force sizes must match the closed form m . gcd(m, 4) where G is
# nontrivial. Checked, not assumed -- an error in either side shows up here.
checks["eigenspace_size_matches_closed_form"] = all(
    sizes[m] == m * gcd(m, 4) for m in DIVISORS if deg[m] == 2)
checks["eigenspace_proper_exactly_for_the_degree_2_m"] = all(
    proper[m] == (deg[m] == 2) for m in DIVISORS)
detail["m_with_proper_eigenspace"] = sorted(m for m in DIVISORS if proper[m])
# CONTROL: the test does NOT report "proper" everywhere -- m | 4 is vacuous.
checks["control_eigenspace_is_vacuous_for_m_dividing_4"] = all(
    not proper[m] for m in DIVISORS if 4 % m == 0)

# ---------------------------------------------------------------- Thm 1.2 / Prop 2.5
W_F = 4                                    # w_{Q_5}: the roots of unity of Q_5
checks["w_F_of_Q5_is_4"] = sum(
    1 for u in range(1, MOD) if u % P and pow(u, 4, MOD) == 1) == 4
uniq = {m: gcd(m, W_F) == 1 for m in DIVISORS}
detail["thm12_applies_unique_lift"] = uniq
checks["unique_lift_exactly_for_odd_m"] = all(
    uniq[m] == (m % 2 == 1) for m in DIVISORS)

# When gcd(m, w_F) > 1 only R^{w_F} is defined. Is that power still
# non-trivial on the Teichmueller line Z/m? Yes iff m does not divide w_F.
survives = {m: any((W_F * a) % m != 0 for a in range(m)) for m in DIVISORS}
detail["R_to_the_wF_still_nontrivial"] = survives
checks["R_to_wF_dies_exactly_when_m_divides_wF"] = all(
    survives[m] == (W_F % m != 0) for m in DIVISORS)

live = sorted(m for m in DIVISORS if proper[m] and survives[m])
detail["m_where_a_nonvacuous_value_can_exist"] = live
checks["live_m_are_3_6_8_12_24"] = live == [3, 6, 8, 12, 24]

# ---------------------------------------------------------------- m = 2, anywhere
# -1 is a nontrivial square root of 1 in every field of characteristic != 2,
# so F_2 = F always, G is always trivial, and w_F is always even.
checks["m2_eigenspace_is_the_whole_group"] = not proper[2]
checks["m2_R_to_wF_is_trivial"] = not survives[2]
detail["m2_verdict"] = (
    "CGZ Theorem 1.2 never applies at n = 2 in any field of characteristic "
    "!= 2: -1 is a nontrivial square root of 1, so F_2 = F, G is trivial, "
    "w_F is even, and only R^{w_F} is defined -- which is 1 in a group of "
    "exponent 2. There is no non-vacuous m = 2 invariant to compute, so the "
    "+1 of PR #4968 is forced by the group rather than measured.")

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_m_lattice_eigenspace_census_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_m_lattice_eigenspace_census_probe.py",
    "commitSha": _sha,
    "beans": ["qou-w4gn", "qou-y3xv", "qou-9p9y"],
    "source": ("CGZ arXiv:1712.04887v3 Theorem 1.2, Remark 1.9, "
               "Proposition 2.5; Addenda 32-35 (this repo)"),
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a) CENSUS of where a value can exist, not a value at any new "
        "m. Over F = Q_5 (the degree-1 place of K = Q(alpha)), for each "
        "m | 24 the class group F_m^x/(F_m^x)^m is Z/m x Z/m and the "
        "chi^{-1}-eigenspace is computed by brute force over all m^2 classes "
        "with the actual Frobenius action, then checked against the closed "
        "form m . gcd(m, 4). Three-way split: m | 4 has trivial Gal, a "
        "vacuous eigenspace and no value; m = 3 satisfies gcd(m, w_F) = 1 "
        "with w_{Q_5} = 4 so the lift is unique (the case already computed); "
        "m in {6, 8, 12, 24} has a proper eigenspace but gcd > 1, so only "
        "R^{w_F} is defined -- and that power is still non-trivial there, so "
        "information survives. Corrects the guess that queued this work: "
        "mu_m lies in Q_5 exactly when m | 4, NOT when m shares a factor "
        "with 4, so 8, 12 and 24 qualify. Also corrects a claim repeated "
        "throughout this arc: m = 2 is vacuous in EVERY field of "
        "characteristic != 2, because -1 forces F_2 = F and w_F even, so "
        "Theorem 1.2 never applies at n = 2 and only R^{w_F} = 1 is defined. "
        "The +1 of PR #4968 is forced by the group, not measured -- which "
        "does not make that computation wrong, but makes it empty as a CGZ "
        "value. Nothing wired."
    ),
}
with open(HERE / "gswz_epsm_m_lattice_eigenspace_census.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)
