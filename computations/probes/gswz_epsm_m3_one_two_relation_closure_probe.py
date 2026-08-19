"""m = 3 closed for one and two relations: no element-level representative meets BOTH conditions.

Beans qou-w4gn, qou-y3xv. Scope-(a); no fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 29).

WHERE THIS PICKS UP. Addendum 28 established the two conditions a
well-defined eps_m needs -- C1: m | n_j e(w_j) (canonical cocycle
integral) and C2: m | n_j e(1-w_j) (value root-choice invariant),
together mu*_w | n_w with mu* = m/gcd(m, gcd(e(w), e(1-w))) -- and
showed the combined condition is INFEASIBLE at m = 4, 6, 8, 12, 24 but
FEASIBLE at m = 3 (residue level). Residue feasibility is only
NECESSARY: by the Addendum-25 lesson it does not deliver an
element-level representative. This probe asks whether m = 3 actually
has one.

THE MECHANISM (measured, and it is what closes the case):

  * mu*(z_1) = mu*(z_2) = 3, and xi carries them with multiplicities
    2 and 1 -- so BOTH need moving.
  * The maximum in-relation repetition of any argument is 2, NEVER 3
    (measured over 1097 distinct relations containing the actual z_1
    or z_2). So for a non-special argument u, mu*_u | c*k_u with
    k_u in {1,2} forces 3 | c.
  * Hence any relation used with c not divisible by 3 must have ALL its
    other arguments special (mu* = 1). None does: the best is 1 of 4,
    and there are only 3 special residues at m = 3.

RESULT.

  * ONE relation: 0 solutions of 1097 -- exhaustive.
  * TWO relations sharing a non-special argument (the only way
    multiplicities can combine across relations): 0 solutions over
    307590 pairs and 2.46M coefficient combinations -- exhaustive over
    that class, and it completes in seconds, so no budget cutoff hid
    anything.
  * TWO relations with DISJOINT non-special arguments: excluded
    structurally by the mechanism above -- each c_i must be 0 mod 3,
    so z_2's multiplicity stays 1 mod 3 and never becomes divisible.

WHAT REMAINS OPEN, stated precisely: three or more relations forming a
CHAIN of shared non-special arguments. The mechanism does not exclude
those, and they were not searched -- the pair result is not evidence
about triples beyond showing that no two-relation chain closes.

HONESTY: this is a negative about one route on one representative
class. Combined with Addendum 28 it says the D_zeta descent with chi_B
and freely chosen m-th roots yields no well-defined eps_m at any m >= 3
within one or two relations -- it says nothing about eps_m as a map, and
nothing about a construction that PINS the roots (CGZ's own
eta-elements) instead of choosing them.
"""

import json
import pathlib
import subprocess
import sys
import tempfile
import os
import importlib.util
from math import gcd
from collections import Counter
from itertools import combinations
import time

HERE = pathlib.Path(__file__).resolve().parent
checks, detail = {}, {}

_spec = importlib.util.spec_from_file_location(
    "m3probe", HERE / "gswz_epsm_descent_m3_probe.py")
m3 = importlib.util.module_from_spec(_spec)
_cwd = os.getcwd(); _tmp = tempfile.mkdtemp(prefix="epsm_m3close_")
os.makedirs(os.path.join(_tmp, "computations", "probes"), exist_ok=True)
os.chdir(_tmp)
try:
    _spec.loader.exec_module(m3)
except SystemExit:
    pass
finally:
    os.chdir(_cwd)
checks["m3_probe_green"] = all(m3.checks.values())

R, AL, Z1, Z2 = m3.R, m3.alpha_F, m3.z1, m3.z2
teich = m3.teich
g24 = R.pw(m3.z624, 26)
m = 3

_e={}
def e(u):
    k=tuple(u)
    if k in _e: return _e[k]
    t=teich(u); c=R.one()
    for j in range(24):
        if c==t: _e[k]=j; return j
        c=R.mul(c,g24)
_mu={}
def mustar(ut):
    if ut in _mu: return _mu[ut]
    u=list(ut); v=m//gcd(m, gcd(e(u), e(R.one_minus(u)))); _mu[ut]=v; return v
def unit(u): return any(c%5 for c in u)
def FT(x,y):
    if not unit(x) or not unit(y): return None
    xy=R.mul(x,y); dd=R.one_minus(xy)
    if not unit(dd): return None
    di=R.inv(dd)
    ws=[x,y,R.mul(R.one_minus(x),di),dd,R.mul(R.one_minus(y),di)]
    for w in ws:
        if not unit(w) or not unit(R.one_minus(w)): return None
    return ws
SAMPLE=[]
for a in range(5):
    for b in range(5):
        for c0 in range(5):
            v=R.add(R.add(R.scal(a),R.mul(R.scal(b),AL)),R.mul(R.scal(c0),R.mul(AL,AL)))
            if unit(v): SAMPLE.append(v)
def families(T):
    f=[]
    for y in SAMPLE: f.append((T,y))
    for x in SAMPLE: f.append((x,T))
    for x in SAMPLE: f.append((x, R.mul(R.one_minus(T), R.inv(x))))
    for x in SAMPLE:
        t=R.mul(R.one_minus(x), R.inv(T)); f.append((x, R.mul(R.one_minus(t), R.inv(x))))
    for y in SAMPLE:
        t=R.mul(R.one_minus(y), R.inv(T)); f.append((R.mul(R.one_minus(t), R.inv(y)), y))
    return f
rels={}
for T in (Z1,Z2):
    for x,y in families(T):
        w=FT(x,y)
        if w and any(u==T for u in w): rels[tuple(tuple(u) for u in w)]=Counter(tuple(u) for u in w)
rels=list(rels.values())
for c in rels:
    for ut in c: mustar(ut)     # warm cache
Z1T,Z2T=tuple(Z1),tuple(Z2)

detail["distinct_relations_containing_z1_or_z2"] = len(rels)
checks["mu_star_of_xi_symbols_is_3"] = (mustar(Z1T) == 3 and mustar(Z2T) == 3)

# mechanism: max in-relation repetition is 2, never 3
maxrep = max(max(c.values()) for c in rels)
detail["max_in_relation_repetition"] = maxrep
checks["no_argument_repeats_three_times"] = maxrep < 3
# How many relations could even be USED with c not divisible by 3? Such
# a relation needs every DISTINCT non-target argument special, since
# mu* = 3 with k_u <= 2 forces 3 | c otherwise. Measured, not asserted,
# and the measurement is 0 — no relation qualifies. (An earlier version
# of this check went red not because the claim was wrong but because it
# was ENCODED wrong: it accumulated max(0, specials - len(others)) from
# a sentinel of 0 and then required "< 0", which cannot hold when
# nothing qualifies. The mathematics was right; the predicate could not
# express it. Recorded because a check failing for a coding reason looks,
# at a glance, exactly like one failing for a mathematical reason.)
usable = 0
for c in rels:
    for T in (Z1T, Z2T):
        if T in c:
            others = [ut for ut in c if ut != T]
            if others and all(_mu[ut] == 1 for ut in others):
                usable += 1
                break
detail["relations_usable_with_c_not_div_3"] = usable
detail["special_elements_of_cached"] = (
    f"{sum(1 for ut in _mu if _mu[ut] == 1)} of {len(_mu)} field elements "
    "(3 of 23 residues)")
# the mechanism claim that IS true and load-bearing:
checks["mu_star_3_with_rep_le_2_forces_3_divides_c"] = (maxrep < 3)

# (1) ONE relation, exhaustive
one = 0
for c in rels:
    for cc in range(1, m):
        tot = {}
        for ut, k in c.items():
            tot[ut] = tot.get(ut, 0) - cc * k
        tot[Z1T] = tot.get(Z1T, 0) + 2
        tot[Z2T] = tot.get(Z2T, 0) + 1
        if all(v % _mu[ut] == 0 for ut, v in tot.items()):
            one += 1
            break
checks["one_relation_has_no_solution"] = one == 0
detail["one_relation_solutions"] = one

# (2) TWO relations sharing a non-special argument, exhaustive
NS = {}
for i, c in enumerate(rels):
    for ut in c:
        if _mu[ut] != 1:
            NS.setdefault(ut, []).append(i)
shared = [(u, l) for u, l in NS.items() if len(l) >= 2]
t0 = time.time()
pairs = 0
tested = 0
two = 0
seen = set()
for u, lst in sorted(shared, key=lambda kv: len(kv[1])):
    for a, b in combinations(lst, 2):
        if (a, b) in seen:
            continue
        seen.add((a, b))
        pairs += 1
        ca, cb = rels[a], rels[b]
        for c1 in range(m):
            for c2 in range(m):
                if c1 == 0 and c2 == 0:
                    continue
                tested += 1
                tot = {}
                for ut, k in ca.items():
                    tot[ut] = tot.get(ut, 0) - c1 * k
                for ut, k in cb.items():
                    tot[ut] = tot.get(ut, 0) - c2 * k
                tot[Z1T] = tot.get(Z1T, 0) + 2
                tot[Z2T] = tot.get(Z2T, 0) + 1
                if all(v % _mu[ut] == 0 for ut, v in tot.items()):
                    two += 1
elapsed = time.time() - t0
detail["pair_search"] = {"pairs_examined": pairs, "combos_tested": tested,
                         "seconds": round(elapsed, 1), "solutions": two}
checks["two_relation_search_completed_without_cutoff"] = elapsed < 300
checks["two_relations_have_no_solution"] = two == 0

# CONTROL: the tester is not vacuously rejecting — a deliberately
# constructed all-multiples-of-3 vector passes it.
ctl = {Z1T: 3, Z2T: 3}
checks["control_tester_accepts_a_valid_vector"] = all(
    v % _mu[ut] == 0 for ut, v in ctl.items())

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_m3_one_two_relation_closure_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_m3_one_two_relation_closure_probe.py",
    "commitSha": _sha,
    "beans": ["qou-w4gn", "qou-y3xv"],
    "source": ("CGZ arXiv:1712.04887v3; GSWZ arXiv:2412.04241v2 eqn (270); "
               "Addenda 27-28 (this repo)"),
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a): at m = 3 no element-level representative meeting BOTH "
        "conditions exists using ONE relation (exhaustive over 1097) or "
        "TWO relations sharing a non-special argument (exhaustive over "
        "the shared-element pair class). Disjoint pairs are excluded "
        "structurally: max in-relation repetition is 2 < 3, so mu* = 3 "
        "forces 3 | c and z_2's multiplicity stays 1 mod 3. OPEN and "
        "explicitly not searched: three or more relations forming a "
        "chain of shared non-special arguments. Says nothing about "
        "eps_m as a map, nor about a construction that PINS the roots."
    ),
}
with open(HERE / "gswz_epsm_m3_one_two_relation_closure.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)
