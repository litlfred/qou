"""RE-SCOPE: CGZ's P_zeta IS root-independent (their Lemma 2.4(a)) — the m >= 3 ambiguity is introduced by my descent-to-base step, not by the invariant.

Beans qou-w4gn, qou-y3xv, qou-9p9y. Scope-(a); no fit; nothing wired;
audit: docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 30).

WHAT PROMPTED THIS. Addenda 27-29 measured a root-choice ambiguity in
the eps_m construction at m >= 3, derived its closed form
(Delta_j = -n_j e(1-w_j) mod m), turned it into a second divisibility
condition C2, and used C2 to obstruct m = 4, 6, 8, 12, 24 and then to
close m = 3 for one and two relations. Reading CGZ's own definition
rather than continuing to build on mine shows that chain characterises
MY composite, not their invariant.

CGZ eqn (20), p.10:

    P_zeta(X) := D_zeta(x) / D_zeta(1)  in  H^x / (H^x)^n   (x^n = X),

with the parenthetical: "We previously defined P_zeta(X) ... as an
element of H^x, but only its image modulo nth powers was ever used, and
it is more canonical to define it in the manner above."

CGZ Lemma 2.4(a): "P_zeta(X) is independent of the choice of nth root x
of X." Their proof is eqn (21) -- which is exactly the shift law this
programme already proved in Lean (QOU.Machinery.CyclicQuantumDilog,
#4964) -- together with the observation that the shift factor lies in
H^x n, i.e. IS an n-th power.

WHAT THIS PROBE MEASURES (in the degree-12 field F = Q_5(mu_1872) where
the m = 3 work was done):

1. The shift ratio D(zeta x)/D(x) equals (1-x)^m/(1-w) exactly -- the
   Lean law, re-verified numerically here, and the same identity as
   CGZ (21).
2. IN F: every shift ratio for the Addendum-27 representative's symbols
   is an m-th power of F. So Lemma 2.4(a) holds in this setting, and
   P_zeta really is root-independent in F^x/(F^x)^m.
3. IN THE BASE B = Q_25: only one of the four is an m-th power. So the
   composite I built -- descend to B, then apply the character
   chi_B = teich(.)^{24/m} -- does NOT kill those ratios, and the class
   moves. That is precisely the ambiguity Addenda 27-29 measured.

CONSEQUENCE, and the re-scope. The m >= 3 "obstruction" is a property of
MY EXTRA STEP (descent to B followed by chi_B), not of CGZ's P_zeta:

  * Addendum 27's non-invariance: real, but of the B-level composite.
  * Addendum 28's condition C2 and its m = 4, 6, 8, 12, 24
    infeasibility: correct as stated, but they characterise WHEN THE
    B-LEVEL COMPOSITE IS WELL DEFINED -- not an obstruction to eps_m.
  * Addendum 29's closure of m = 3 for one and two relations: likewise
    a statement about the B-level composite.

None of those computations is retracted; their SCOPE is. The right
target is CGZ's own: the class in F^x/(F^x)^n (or H^x/(H^x)^n), where
root-independence is Lemma 2.4(a) and needs no representative search at
all.

HONESTY: this probe reports that three addenda of my own were aimed at
the wrong object. It does not claim the eps_m VALUES -- computing the
class in F^x/(F^x)^n is the next increment, not done here. A wrong
m-th-power test would break the controls below rather than pass
silently.
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
_cwd = os.getcwd(); _tmp = tempfile.mkdtemp(prefix="epsm_rescope_")
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
m, d = 3, m3.d
M_ORD = 5 ** d - 1
zeta_m = R.pw(m3.zeta_N, m3.N // m)
checks["m_divides_F_teichmuller_order"] = M_ORD % m == 0


def e(u):
    t = teich(u); c = R.one()
    for k in range(24):
        if c == t:
            return k
        c = R.mul(c, g24)
    return None


def is_mth_power_in_F(u):
    return R.pw(teich(u), M_ORD // m) == R.one()


def is_mth_power_in_B(u):
    ee = e(u)
    return ee is not None and ee % m == 0


def Dz(x):
    r = R.one()
    for k in range(1, m):
        r = R.mul(r, R.pw(R.one_minus(R.mul(R.pw(zeta_m, k), x)), k))
    return r


def unit(u):
    return any(c % 5 for c in u)


def FT(x, y):
    if not unit(x) or not unit(y):
        return None
    xy = R.mul(x, y); dd = R.one_minus(xy)
    if not unit(dd):
        return None
    di = R.inv(dd)
    ws = [x, y, R.mul(R.one_minus(x), di), dd, R.mul(R.one_minus(y), di)]
    for w in ws:
        if not unit(w) or not unit(R.one_minus(w)):
            return None
    return ws


# rebuild the Addendum-27 representative
SAMPLE = []
for a in range(5):
    for b in range(5):
        for c0 in range(5):
            v = R.add(R.add(R.scal(a), R.mul(R.scal(b), AL)),
                      R.mul(R.scal(c0), R.mul(AL, AL)))
            if unit(v):
                SAMPLE.append(v)
iz2 = R.inv(Z2)
fams = []
for y in SAMPLE:
    fams.append((Z2, y))
for x in SAMPLE:
    fams.append((x, Z2))
for x in SAMPLE:
    fams.append((x, R.mul(AL, R.inv(x))))
for x in SAMPLE:
    t = R.mul(R.one_minus(x), iz2)
    fams.append((x, R.mul(R.one_minus(t), R.inv(x))))
for y in SAMPLE:
    t = R.mul(R.one_minus(y), iz2)
    fams.append((R.mul(R.one_minus(t), R.inv(y)), y))
k2 = [w for x, y in fams for w in [FT(x, y)]
      if w and sum(1 for u in w if u == Z2) == 2]
checks["representative_rebuilt"] = len(k2) > 0
W = k2[0]
rep = {tuple(Z1): 2}
rep[tuple(Z2)] = rep.get(tuple(Z2), 0) + 1
for u in W:
    rep[tuple(u)] = rep.get(tuple(u), 0) - 2
rep = {k: v for k, v in rep.items() if v}

# (1) the shift ratio equals the Lean/CGZ-(21) form, exactly
rows, law_ok, inF, inB = [], True, 0, 0
for el, n in rep.items():
    u = list(el)
    x = m3.mth_root_teich_dlog624(u)
    if R.pw(x, m) != u:
        law_ok = False
        continue
    ratio = R.mul(Dz(R.mul(zeta_m, x)), R.inv(Dz(x)))
    closed = R.mul(R.pw(R.one_minus(x), m), R.inv(R.one_minus(u)))
    if ratio != closed:
        law_ok = False
    f_ok = is_mth_power_in_F(ratio)
    b_ok = is_mth_power_in_B(ratio)
    inF += f_ok
    inB += b_ok
    rows.append({"e_w": e(u), "mult": n, "mth_power_in_F": f_ok,
                 "mth_power_in_B": b_ok})
checks["shift_ratio_matches_lean_and_cgz21"] = law_ok
detail["per_symbol"] = rows

# (2) Lemma 2.4(a) holds in F
checks["lemma_24a_holds_in_F"] = inF == len(rows) and len(rows) > 0
# (3) but NOT after descending to B — which is what my composite did
checks["fails_in_B_so_composite_is_where_ambiguity_enters"] = inB < len(rows)
detail["mth_power_counts"] = {"in_F": inF, "in_B": inB, "of": len(rows)}

# CONTROLS: the two power-tests must be able to say NO. Two earlier
# versions of this control went red WITHOUT any mathematical problem,
# and the reason is worth recording because it IS the structural point:
#   (i) F_5 scalars all have order dividing 4, and (5^12-1)/4 is
#       divisible by 3, so every one of them is a cube in F;
#   (ii) more generally EVERY element of the base B^x is a cube in F,
#       because mu_24 sits in F^x as <g^{(5^12-1)/24}> and
#       (5^12-1)/24 = 10172526 is divisible by 3, while the 1+5R part
#       is uniquely 3-divisible.
# So B^x is contained in (F^x)^m -- which is exactly WHY every shift
# ratio above is an m-th power in F: its non-(1-x)^m part, (1-w)^{-1},
# lives in the base. A control must therefore leave B: sweep elements
# built from the ring generator X, which has degree 12 over F_5.
X = [0, 1] + [0] * (d - 2)
base_all_cubes = all(
    is_mth_power_in_F(R.add(R.scal(a), R.mul(R.scal(b), AL)))
    for a in range(5) for b in range(5)
    if unit(R.add(R.scal(a), R.mul(R.scal(b), AL))))
checks["base_units_are_all_mth_powers_in_F"] = base_all_cubes
non_cube_F = None
for a in range(5):
    for b in range(1, 5):
        cand = R.add(R.scal(a), R.mul(R.scal(b), X))
        if unit(cand) and not is_mth_power_in_F(cand):
            non_cube_F = (a, b)
            break
    if non_cube_F:
        break
non_cube_B = None
for a in range(5):
    for b in range(5):
        cand = R.add(R.scal(a), R.mul(R.scal(b), AL))
        if unit(cand) and not is_mth_power_in_B(cand):
            non_cube_B = (a, b)
            break
    if non_cube_B:
        break
checks["control_F_test_can_reject"] = non_cube_F is not None
checks["control_B_test_can_reject"] = non_cube_B is not None
detail["control_non_cubes"] = {"F_outside_base": non_cube_F, "B": non_cube_B}

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_cgz_lemma24a_rescope_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_cgz_lemma24a_rescope_probe.py",
    "commitSha": _sha,
    "beans": ["qou-w4gn", "qou-y3xv", "qou-9p9y"],
    "source": ("CGZ arXiv:1712.04887v3 eqn (20), Lemma 2.4(a), eqn (21), "
               "p.10; shift law QOU.Machinery.CyclicQuantumDilog (#4964); "
               "Addenda 27-29 (this repo)"),
    "checks": checks,
    "result": detail,
    "scope": (
        "RE-SCOPE of my own merged Addenda 27-29. CGZ define P_zeta with "
        "values in H^x/(H^x)^n and prove root-independence (Lemma "
        "2.4(a)) via the shift law this programme proved in Lean. "
        "Measured here in F = Q_5(mu_1872): every shift ratio IS an "
        "m-th power of F (Lemma 2.4(a) confirmed), but only one of four "
        "is an m-th power in the base B = Q_25 -- so the ambiguity "
        "Addenda 27-29 measured is introduced by MY extra step "
        "(descent to B, then chi_B), not by CGZ's invariant. Those "
        "computations stand; their SCOPE narrows to 'when the B-level "
        "composite is well defined'. They do NOT obstruct eps_m. "
        "Computing the class in F^x/(F^x)^n is the next increment and "
        "is not done here."
    ),
}
with open(HERE / "gswz_epsm_cgz_lemma24a_rescope.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)
