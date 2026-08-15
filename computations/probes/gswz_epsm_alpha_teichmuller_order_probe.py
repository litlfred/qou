"""The alpha-obstruction is MAXIMAL: alpha generates the base Teichmuller group mu_24, so no canonical m-th root exists for any m > 1.

Bean qou-y3xv (the sharpening of the m | 24 sweep). Scope-(a) for the
eps_m consequence, scope-(b) for the root-existence exclusion (proved
invariant: the ORDER of alpha in mu_24). No fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 22).

WHAT THIS SHARPENS. The m | 24 sweep (same PR) reported each level as
canonical-integral or fractional using a PER-FACTOR criterion:
m | n_i r_i for each i separately, with n = (2, 1). That criterion is
NOT sharp. Because the alpha-line identities make BOTH base elements
powers of the SAME element,

    1 - z_1 = alpha^2,    1 - z_2 = alpha,    z_1 = -alpha^3,

the fractional part of the canonical cocycle is a single alpha-power:

    c_canon's base part = alpha^{-(2*2*r_1 + 1*r_2)/m}
                        = alpha^{-(4 r_1 + r_2)/m},

so the SHARP criterion is the COMBINED one, m | (4 r_1 + r_2), which
is strictly weaker (easier to satisfy) than the per-factor pair. It is
intrinsic: rescaling the primitive root zeta_m -> zeta_m^u multiplies
both r_i by the same unit mod m, so divisibility is unaffected.

RESULT 1 (the sharp criterion does not rescue any level). Re-scored
across the lattice, the combined value (4 r_1 + r_2) mod m is
   m=2: 0 (integral),  m=3: 1,  m=4: 2,  m=6: 4,
   m=8: 2,  m=12: 10,  m=24: 22.
Only m = 2 vanishes. So the sweep's published verdicts STAND under the
sharper test — the obstruction survives being tested more permissively,
which strengthens rather than corrects the table. (m=8 improves 6 -> 2
and m=24 improves 18/10 -> 22 without reaching 0.)

RESULT 2 (why no root choice can help — the proved invariant). alpha
is sigma-fixed, hence lies in the base B = Q_25, whose Teichmuller
group is mu_24. Its discrete logarithm is measured here:

    e_alpha := dlog_{g24} teich(alpha) = 13,   gcd(13, 24) = 1,

i.e. **alpha is a PRIMITIVE GENERATOR of mu_24** (exact order 24).
Consequences, each checked:

  (a) alpha is an m-th power in B for NO m > 1 (m | 24): the m-th
      powers of mu_24 are <g24^m>, and m | 13 is false for every
      m > 1. So there is no base m-th root of alpha to choose --
      the canonical construction cannot be repaired by a better
      choice; it needs a different Bloch REPRESENTATIVE (one whose
      1 - w_i avoid alpha), or CGZ's square-argument eta-elements.
  (b) Since e_alpha is a unit mod 24, the criterion
      m | e_alpha * (4 r_1 + r_2) is equivalent to m | (4 r_1 + r_2)
      -- the arithmetic of the lattice is governed entirely by the
      shift exponents, with alpha contributing no divisibility of
      its own. Checked both ways here.
  (c) m = 2 is canonical NOT because alpha is a square (it is not:
      13 is odd) but because 4 r_1 + r_2 = 4 is even, so the
      exponent is an INTEGER and no root of alpha is required. The
      uniqueness of m = 2 in the sweep is thereby explained, not
      merely observed.

SCOPE (STRICT, per the (a)/(b) discipline):
  * scope-(b) STRUCTURAL EXCLUSION, invariant named: "alpha has no
    m-th root in B for any m > 1" is forced by the ORDER of alpha in
    the cyclic group mu_24 (order 24, generator). This excludes the
    root-choice repair of THIS cocycle, permanently.
  * scope-(a) for eps_m itself: this does NOT show eps_m(xi) is
    undefined or unreachable at m >= 3. eps_m is a function of the
    BLOCH CLASS; a different representative of the same class (five-
    term-related, or CGZ's eta-form with square arguments) has
    different 1 - w_i and may well avoid alpha entirely. What is
    excluded is one route on one representative.

HONESTY: every check can fail (a wrong dlog, a non-generator alpha, a
mis-stated criterion, or a lattice row disagreeing with the committed
sweep witness would each break a specific check); the sweep's own
per-m data is READ FROM ITS COMMITTED WITNESS rather than restated, so
a drift between the two is caught.
"""

import json
import os
import sys
import tempfile
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))

checks = {}
detail = {}

# ---- load the m = 2 field machinery (d = 8, fastest) -----------------
# The imported probe writes its own witness on execution, so run it with
# cwd redirected into a temp dir: importing a probe for its machinery
# must NEVER rewrite that probe's committed witness (its provenance sha
# would silently follow whatever HEAD this probe happened to run at).
spec = importlib.util.spec_from_file_location(
    "m2probe", os.path.join(HERE, "gswz_epsm_descent_m2_probe.py")
)
m2 = importlib.util.module_from_spec(spec)
_cwd = os.getcwd()
_tmp = tempfile.mkdtemp(prefix="epsm_alpha_")
os.makedirs(os.path.join(_tmp, "computations", "probes"), exist_ok=True)
os.chdir(_tmp)
try:
    spec.loader.exec_module(m2)
except SystemExit:
    pass
finally:
    os.chdir(_cwd)

R, sigma, teich = m2.R, m2.sigma, m2.teich
alpha, z624 = m2.alpha_F, m2.z624
checks["m2_probe_green"] = all(m2.checks.values())

g24 = R.pw(z624, 26)
checks["g24_is_base_mu24_generator"] = (
    sigma(g24) == g24
    and R.pw(g24, 24) == R.one()
    and all(R.pw(g24, 24 // p) != R.one() for p in (2, 3))
)

# ---- RESULT 2: the discrete logarithm of alpha ------------------------
checks["alpha_in_base"] = sigma(alpha) == alpha
ta = teich(alpha)
checks["teich_alpha_in_mu24"] = R.pw(ta, 24) == R.one()

e_alpha = None
t = R.one()
for e in range(24):
    if t == ta:
        e_alpha = e
        break
    t = R.mul(t, g24)
checks["alpha_dlog_found"] = e_alpha is not None
detail["e_alpha"] = e_alpha

from math import gcd

checks["alpha_generates_mu24"] = (
    e_alpha is not None and gcd(e_alpha, 24) == 1
)
# exact order 24, computed independently of the gcd shortcut
order_ta = next(k for k in range(1, 25) if R.pw(ta, k) == R.one())
checks["alpha_teich_order_is_24"] = order_ta == 24
detail["alpha_teich_order"] = order_ta

# (a) alpha is an m-th power in B for no m > 1: g24^13 in <g24^m> iff m | 13
mth_power_levels = [m for m in (2, 3, 4, 6, 8, 12, 24) if e_alpha % m == 0]
checks["alpha_is_mth_power_for_no_m_gt_1"] = mth_power_levels == []
detail["m_with_base_mth_root_of_alpha"] = mth_power_levels

# ---- RESULT 1: the sharp combined criterion across the lattice --------
with open(os.path.join(HERE, "gswz_epsm_descent_m4to24.witness.json")) as f:
    sweep = json.load(f)
checks["sweep_witness_green"] = all(sweep["checks"].values())

# m = 2 and m = 3 live in their own probes/witnesses; their shift data
# is restated here and CROSS-CHECKED against the m2 module for m = 2.
r_by_m = {2: (1, 0), 3: (0, 1)}
for m_str, row in sweep["per_m"].items():
    se = row["shift_exponents"]
    r_by_m[int(m_str)] = (se["r1"], se["r2"])

# cross-check the m = 2 row against the live m2 module (not a restatement)
def shift_exp_m2(x):
    s = R.mul(sigma(x), R.inv(x))
    if s == R.one():
        return 0
    if s == R.scal(-1):
        return 1
    return None


checks["m2_shift_row_matches_live_module"] = (
    shift_exp_m2(m2.x1), shift_exp_m2(m2.x2)
) == r_by_m[2]

lattice = {}
for m in sorted(r_by_m):
    r1, r2 = r_by_m[m]
    per_factor = ((2 * r1) % m == 0) and (r2 % m == 0)
    combined_val = (4 * r1 + r2) % m
    with_alpha = (e_alpha * (4 * r1 + r2)) % 24 % m
    lattice[m] = {
        "r": [r1, r2],
        "per_factor_integral": per_factor,
        "combined_residue": combined_val,
        "combined_integral": combined_val == 0,
        "with_alpha_dlog_residue": with_alpha,
    }
detail["lattice"] = lattice

# only m = 2 is canonical under the SHARP criterion
checks["only_m2_integral_under_sharp_criterion"] = [
    m for m, v in lattice.items() if v["combined_integral"]
] == [2]
# the sharp criterion never contradicts the published (stricter) one:
# per-factor integral => combined integral
checks["sharp_criterion_refines_published"] = all(
    (not v["per_factor_integral"]) or v["combined_integral"]
    for v in lattice.values()
)
# (b) e_alpha is a unit mod 24, so it drops out of the divisibility
checks["alpha_dlog_drops_out_of_criterion"] = all(
    (v["with_alpha_dlog_residue"] == 0) == v["combined_integral"]
    for v in lattice.values()
)
# (c) m = 2 works via an EVEN exponent, not via alpha being a square
checks["m2_integral_and_alpha_not_a_square"] = (
    lattice[2]["combined_integral"] and e_alpha % 2 == 1
)

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

import subprocess

_sha = subprocess.run(
    ["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=HERE
).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_alpha_teichmuller_order_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_alpha_teichmuller_order_probe.py",
    "commitSha": _sha,
    "beans": ["qou-y3xv", "qou-9p9y"],
    "source": (
        "CGZ arXiv:1712.04887v3 (library/arxiv-1712.04887v3/1712.04887v3.pdf); GSWZ "
        "arXiv:2412.04241v2 eqn (270); the m|24 sweep + m=2/m=3 layers "
        "(same branch, PR #4968/#4983)"
    ),
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(b) STRUCTURAL EXCLUSION with the invariant named: alpha "
        "has exact order 24 in the base Teichmuller group mu_24 (dlog "
        "13, a unit), so it is an m-th power in B for NO m > 1 and the "
        "canonical cocycle cannot be repaired by any root choice. "
        "scope-(a) for eps_m itself: a different Bloch REPRESENTATIVE "
        "of the same class (five-term-related, or CGZ's square-argument "
        "eta-form) has different 1-w_i and may avoid alpha entirely — "
        "only one route on one representative is excluded. Also sharpens "
        "the sweep's per-factor integrality criterion to the combined "
        "one m | (4r_1 + r_2); the published verdicts stand under it."
    ),
}
with open(
    os.path.join(HERE, "gswz_epsm_alpha_teichmuller_order.witness.json"), "w"
) as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
