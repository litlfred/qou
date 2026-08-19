"""The eps_m invariant is bracketed: B is too small (root-dependent), F is too large (class collapses).

Beans qou-w4gn, qou-y3xv, qou-9p9y. Scope-(a); no fit; nothing wired;
audit: docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 31).

WHERE THIS PICKS UP. Addendum 30 re-scoped Addenda 27-29: the m >= 3
root ambiguity they measured belongs to MY descent-to-base composite,
not to CGZ's P_zeta, which is root-independent by their Lemma 2.4(a)
because its shift factor lies in H^x n. The stated next increment was
to compute the class where CGZ actually put it -- in F^x/(F^x)^n --
rather than descending to the base at all. This probe does that, and
the answer is not a value: it is a bracketing.

THE COMPUTATION. For a unit u of F, the class in F^x/(F^x)^m is carried
entirely by the Teichmuller part (1 + 5R is uniquely m-divisible when
gcd(m, 5) = 1), so it is read off as teich(u)^{(5^d - 1)/m} in mu_m.
(Applying the exponent to u itself does NOT work -- the 1 + 5R factor
survives; an earlier version of this probe did that and returned no
class at all.)

RESULT 1 -- Lemma 2.4(a), confirmed empirically. With
P_zeta(xi) = D(x_1)^2 D(x_2) / D(1)^3 and xi = 2[z_1] + [z_2], the class
is 0, and it is 0 for ALL NINE choices of the pair of cube roots. Root
independence is therefore not merely asserted from CGZ but measured
here.

RESULT 2 -- and it is why this is a bracketing, not a value. The class
map is NOT globally trivial: it returns a nonzero class on an element
built from the ring generator. But on the objects that matter it is
identically zero -- the class of P_zeta(w) is 0 for EVERY ONE of the 23
admissible base arguments w. So in F the invariant carries no
information about xi at all; the 0 above is vacuous.

THE BRACKET:

    base B = Q_25          root-independence FAILS (Addenda 27-29),
                           the class distinguishes things
    F = Q_5(mu_1872)       root-independence HOLDS (Lemma 2.4(a)),
                           the class is identically 0 on base arguments

Neither field supports the invariant. The useful field is intermediate,
or -- more likely, reading CGZ -- the invariant is not this bare class
at all: their Lemma 2.4(d),(e) record that P_zeta is Phi-invariant and
transforms under Gal by the cyclotomic character, and their R_zeta lands
in K_2 / Galois cohomology rather than in a quotient of units. A bare
class in F^x/(F^x)^n throws exactly that structure away, which is
consistent with it collapsing.

HONESTY: this is a negative that localises the difficulty rather than
resolving it. No eps_m value is claimed at any m >= 3; the m = 2 value
from PR #4968 is untouched. The non-vacuity control below is what makes
the collapse a finding rather than a broken class function.
"""

import json
import pathlib
import subprocess
import sys
import tempfile
import os
import importlib.util

HERE = pathlib.Path(__file__).resolve().parent
checks, detail = {}, {}

_spec = importlib.util.spec_from_file_location(
    "m3probe", HERE / "gswz_epsm_descent_m3_probe.py")
m3 = importlib.util.module_from_spec(_spec)
_cwd = os.getcwd(); _tmp = tempfile.mkdtemp(prefix="epsm_bracket_")
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
teich, sigma = m3.teich, m3.sigma
m, d = 3, m3.d
zeta_m = R.pw(m3.zeta_N, m3.N // m)
M_ORD = 5 ** d - 1
checks["m_divides_teichmuller_order"] = M_ORD % m == 0


def unit(u):
    return any(c % 5 for c in u)


def Dz(x):
    r = R.one()
    for k in range(1, m):
        r = R.mul(r, R.pw(R.one_minus(R.mul(R.pw(zeta_m, k), x)), k))
    return r


def cls(u):
    """Class in F^x/(F^x)^m, read on the Teichmuller part."""
    v = R.pw(teich(u), M_ORD // m)
    t = R.one()
    for j in range(m):
        if v == t:
            return j
        t = R.mul(t, zeta_m)
    return None


D1 = Dz(R.one())
checks["D1_is_a_unit"] = unit(D1)
x1 = m3.mth_root_teich_dlog624(Z1)
x2 = m3.mth_root_teich_dlog624(Z2)
checks["cube_roots_exact"] = R.pw(x1, m) == Z1 and R.pw(x2, m) == Z2


def P_of_xi(a, b):
    return R.mul(R.mul(R.pw(Dz(a), 2), Dz(b)), R.pw(R.inv(D1), 3))


P = P_of_xi(x1, x2)
c0 = cls(P)
detail["class_of_P_xi"] = c0
checks["class_is_defined"] = c0 is not None

# RESULT 1: Lemma 2.4(a) measured — invariant over all m^2 root choices
vals = set()
for t1 in range(m):
    for t2 in range(m):
        vals.add(cls(P_of_xi(R.mul(R.pw(zeta_m, t1), x1),
                             R.mul(R.pw(zeta_m, t2), x2))))
detail["classes_over_root_choices"] = sorted(str(v) for v in vals)
checks["lemma_24a_root_independence_measured"] = (
    len(vals) == 1 and c0 in vals)

# RESULT 2: the class map is NOT globally trivial ...
X = [0, 1] + [0] * (d - 2)
nonzero_witness = None
for a in range(5):
    for b in range(1, 5):
        cand = R.add(R.scal(a), R.mul(R.scal(b), X))
        if unit(cand) and cls(cand) not in (0, None):
            nonzero_witness = {"a": a, "b": b, "class": cls(cand)}
            break
    if nonzero_witness:
        break
checks["class_map_is_not_globally_trivial"] = nonzero_witness is not None
detail["nonzero_class_witness"] = nonzero_witness

# ... but it IS trivial on every admissible base argument
dist = {}
tested = 0
for a in range(5):
    for b in range(5):
        w = R.add(R.scal(a), R.mul(R.scal(b), AL))
        if not unit(w) or not unit(R.one_minus(w)):
            continue
        xr = m3.mth_root_teich_dlog624(w)
        if R.pw(xr, m) != w:
            continue
        tested += 1
        c = cls(R.mul(Dz(xr), R.inv(D1)))
        dist[str(c)] = dist.get(str(c), 0) + 1
detail["class_distribution_over_base_arguments"] = dist
detail["base_arguments_tested"] = tested
checks["class_collapses_on_all_base_arguments"] = (
    tested > 0 and dist.get("0", 0) == tested)

# P itself is not in the base — so the zero is not the trivial
# "it landed in B, and B^x is inside (F^x)^m" explanation.
checks["P_is_not_sigma_fixed"] = sigma(P) != P

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_field_bracketing_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_field_bracketing_probe.py",
    "commitSha": _sha,
    "beans": ["qou-w4gn", "qou-y3xv", "qou-9p9y"],
    "source": ("CGZ arXiv:1712.04887v3 eqn (20), Lemma 2.4(a),(d),(e); "
               "Addenda 27-30 (this repo)"),
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a) BRACKETING, not a value. Computing CGZ's class in "
        "F^x/(F^x)^m (read on the Teichmuller part) gives 0 for xi, and "
        "0 for all NINE root choices -- Lemma 2.4(a) confirmed by "
        "measurement. But the class is identically 0 on ALL 23 "
        "admissible base arguments, while being nonzero on an element "
        "off the base, so the invariant carries no information about xi "
        "in F and the 0 is vacuous. Bracket: B = Q_25 is too small "
        "(root-independence fails) and F = Q_5(mu_1872) too large (the "
        "class collapses). Reading CGZ, the invariant is likely not "
        "this bare class at all -- their Lemma 2.4(d),(e) keep Galois "
        "structure that a quotient of units discards. No eps_m value is "
        "claimed at m >= 3; the m = 2 result of PR #4968 is untouched."
    ),
}
with open(HERE / "gswz_epsm_field_bracketing.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)
