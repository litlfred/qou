"""The root ambiguity has a closed form — giving a SECOND divisibility condition, an obstruction at m >= 4, and an open door at m = 3.

Beans qou-w4gn, qou-y3xv, qou-9p9y. Scope-(a) except where marked; no
fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 28).

WHERE THIS PICKS UP. Addendum 27 built a PER-ELEMENT representative at
m = 3 and 6, closed the canonical descent on it (the gate
c_canon^m = sigma(P)/P held exactly, a first at m >= 3), and got
eps_3 = omega^1 -- but the value was NOT invariant: re-running the whole
chain under x_j -> zeta_m^t x_j swept it through all of mu_3. This probe
explains that exactly, and turns it into a criterion.

THE CLOSED FORM. Twisting one root, x_j -> zeta_m x_j, changes D(x_j) by
the Lean-proved shift law (21) at r = 1:

    D(zeta x)/D(x) = (1 - x)^m / (1 - w),      w = x^m.

P therefore changes by [(1-x_j)^m / (1-w_j)]^{n_j}, and chi_B kills the
m-th power (chi_B(u^m) = teich(u)^{24} = 1), so the class moves by

    Delta_j  =  -n_j * e(1 - w_j)   (mod m),

with e the base Teichmuller discrete logarithm. VERIFIED against all
four measured twists of the Addendum-27 representative -- exact, not
approximate, including the two symbols whose twists left the value fixed.

THE CRITERION. A well-defined eps_m therefore needs BOTH:

    (C1)  m | n_j * e(w_j)       -- canonical cocycle integral (Add. 27)
    (C2)  m | n_j * e(1 - w_j)   -- value root-choice invariant (new)

equivalently mu*_w | n_w with mu*_w = m / gcd(m, gcd(e(w), e(1-w))).

This is exactly the shape of CGZ's own construction: their Bloch
elements are D * [zeta_D] (their Section 7 circular-unit discussion,
arXiv:1712.04887v3 p.33), a root-of-unity symbol carrying a
MULTIPLICITY chosen so the ambiguity dies. The multiplier is not
decoration; C2 is what it is for.

THE OBSTRUCTION, and why a residue-level negative is valid HERE. The
conditions depend only on residues, and an element-level representative
MERGES into a residue-level one satisfying the same conditions (m | n_j a
for each j implies m | (sum_j n_j) a over a fixed residue). So

    residue-level infeasible  ==>  element-level infeasible,

which is the sound direction. (The converse is NOT sound and is the
error Addendum 25 retracted: residue-level feasibility does not give an
element-level representative.) Measured over the 23 admissible symbols
and 506 five-term relations:

    m =  3 : xi in L*_m + R   -> TRUE   (door open)
    m =  4, 6, 8, 12, 24      -> FALSE  (genuine obstruction)

with the count of SPECIAL symbols (those satisfying both conditions at
any multiplicity, mu* = 1) explaining the pattern: 3 of 23 residues at
m = 3 and 6, 2 at m = 4, and NONE at m = 8, 12, 24.

SCOPE (STRICT).
  * The m >= 4 result excludes THIS CONSTRUCTION -- the D_zeta descent
    with chi_B and freely chosen m-th roots -- and not the existence of
    eps_m as a map. A different construction (CGZ's own eta-elements,
    or any route that pins the roots rather than choosing them) is
    untouched.
  * m = 3 has the NECESSARY condition satisfied. That is not a value:
    an element-level representative meeting both conditions still has
    to be exhibited, and the single-relation family does not contain
    one (searched: 550 relations containing the actual z_2, every
    coefficient).
"""

import json
import pathlib
import subprocess
import sys
from math import gcd

HERE = pathlib.Path(__file__).resolve().parent
checks, detail = {}, {}

# ---------- F_25 in the alpha basis (albar^2 = 4 albar + 3) ----------
ZERO, ONE = (0, 0), (1, 0)
ELS = [(a, b) for a in range(5) for b in range(5)]


def fmul(u, v):
    a, b = u
    c, d = v
    return ((a * c + 3 * b * d) % 5, (a * d + b * c + 4 * b * d) % 5)


def fsub(u, v):
    return ((u[0] - v[0]) % 5, (u[1] - v[1]) % 5)


def forder(x):
    p, k = x, 1
    while p != ONE:
        p = fmul(p, x)
        k += 1
    return k


def finv(x):
    return next(y for y in ELS if fmul(x, y) == ONE)


G = next(x for x in ELS if x != ZERO and forder(x) == 24)
DL, _p = {}, ONE
for _k in range(24):
    DL[_p] = _k
    _p = fmul(_p, G)
e = lambda x: DL[x]
AL = (0, 1)
Z1 = fsub(ONE, fmul(AL, AL))
Z2 = fsub(fmul(Z1, Z1), fsub(Z1, (2, 0)))
checks["alpha_line_identities"] = (
    fsub(ONE, Z1) == fmul(AL, AL) and fsub(ONE, Z2) == AL)

SYM = [w for w in ELS if w not in (ZERO, ONE)]
IDX = {w: i for i, w in enumerate(SYM)}
N = len(SYM)

# ---------- (1) the closed form, against Addendum 27's measurements ----
# representative rows (element e-value, multiplicity) and the measured
# per-unit-twist shift of chi_B, both from the merged Addendum-27 run.
# The measured twists come from the merged Addendum-27 run, whose
# discrete logarithms use the p-adic probe's generator g24 = zeta_624^26.
# A different generator of F_25^x rescales every dlog by a unit, so the
# comparison MUST be done in one convention -- importing the p-adic
# module rather than re-deriving e-values here. (An earlier version of
# this probe mixed the two and its own check caught it.) The lattice
# test below is unaffected: mu* is invariant under that rescale, since
# gcd(m, u*g) = gcd(m, g) for a unit u mod 24.
import os as _os, tempfile as _tf, importlib.util as _iu
_spec = _iu.spec_from_file_location(
    "m3conv", HERE / "gswz_epsm_descent_m3_probe.py")
_m3 = _iu.module_from_spec(_spec)
_cwd = _os.getcwd(); _tmp = _tf.mkdtemp(prefix="epsm_ambig_")
_os.makedirs(_os.path.join(_tmp, "computations", "probes"), exist_ok=True)
_os.chdir(_tmp)
try:
    _spec.loader.exec_module(_m3)
except SystemExit:
    pass
finally:
    _os.chdir(_cwd)
_R, _teich = _m3.R, _m3.teich
_g24 = _R.pw(_m3.z624, 26)


def _e(u):
    tt = _teich(u); c = _R.one()
    for k in range(24):
        if c == tt:
            return k
        c = _R.mul(c, _g24)
    return None


# rebuild the Addendum-27 representative's four elements in that ring
_AL, _Z1, _Z2 = _m3.alpha_F, _m3.z1, _m3.z2


def _unit(u):
    return any(c % 5 for c in u)


def _FT(x, y):
    if not _unit(x) or not _unit(y):
        return None
    xy = _R.mul(x, y); dd = _R.one_minus(xy)
    if not _unit(dd):
        return None
    di = _R.inv(dd)
    ws = [x, y, _R.mul(_R.one_minus(x), di), dd,
          _R.mul(_R.one_minus(y), di)]
    for w in ws:
        if not _unit(w) or not _unit(_R.one_minus(w)):
            return None
    return ws


_SAMPLE = []
for _a in range(5):
    for _b in range(5):
        for _c0 in range(5):
            _v = _R.add(_R.add(_R.scal(_a), _R.mul(_R.scal(_b), _AL)),
                        _R.mul(_R.scal(_c0), _R.mul(_AL, _AL)))
            if _unit(_v):
                _SAMPLE.append(_v)
_iz2 = _R.inv(_Z2); _fams = []
for _y in _SAMPLE:
    _fams.append((_Z2, _y))
for _x in _SAMPLE:
    _fams.append((_x, _Z2))
for _x in _SAMPLE:
    _fams.append((_x, _R.mul(_AL, _R.inv(_x))))
for _x in _SAMPLE:
    _t = _R.mul(_R.one_minus(_x), _iz2)
    _fams.append((_x, _R.mul(_R.one_minus(_t), _R.inv(_x))))
for _y in _SAMPLE:
    _t = _R.mul(_R.one_minus(_y), _iz2)
    _fams.append((_R.mul(_R.one_minus(_t), _R.inv(_y)), _y))
_k2 = [w for _x, _y in _fams for w in [_FT(_x, _y)]
       if w and sum(1 for u in w if u == _Z2) == 2]
_W = _k2[0]
_rep = {tuple(_Z1): 2}
_rep[tuple(_Z2)] = _rep.get(tuple(_Z2), 0) + 1
for _u in _W:
    _rep[tuple(_u)] = _rep.get(tuple(_u), 0) - 2
_rep = {k: v for k, v in _rep.items() if v}
# measured per-unit-twist shifts, keyed by that convention's e(w)
MEASURED = {3: (+2, -1), 22: (-3, 0), 12: (-2, 0), 15: (-4, +1)}
form_ok = {}
for _el, _n in _rep.items():
    _ew = _e(list(_el)); _e1w = _e(_R.one_minus(list(_el)))
    if _ew not in MEASURED:
        continue
    pred = (-_n * _e1w) % 3
    form_ok[_ew] = (pred == MEASURED[_ew][1] % 3)
checks["representative_rebuilt_matches_addendum27"] = (
    sorted(form_ok) == sorted(MEASURED))
E1W = {_e(list(_el)): _e(_R.one_minus(list(_el))) for _el in _rep}
checks["ambiguity_closed_form_matches_all_measured_twists"] = all(form_ok.values())
detail["closed_form_check"] = {
    str(k): {"mult": MEASURED[k][0], "e_1_minus_w": E1W[k],
             "predicted": (-MEASURED[k][0] * E1W[k]) % 3,
             "measured": MEASURED[k][1] % 3} for k in E1W}
# non-vacuity: the formula is not trivially zero everywhere
checks["closed_form_is_nontrivial"] = any(
    (-MEASURED[k][0] * E1W[k]) % 3 != 0 for k in E1W)

# ---------- (2) special symbols ---------------------------------------
special = {}
for m in (3, 4, 6, 8, 12, 24):
    special[m] = sum(1 for w in SYM if e(w) % m == 0 and e(fsub(ONE, w)) % m == 0)
detail["special_symbol_counts"] = special
checks["no_special_symbols_at_8_12_24"] = all(special[m] == 0 for m in (8, 12, 24))

# ---------- (3) the combined-condition lattice test -------------------
def FT(x, y):
    xy = fmul(x, y)
    if xy == ONE:
        return None
    d = finv(fsub(ONE, xy))
    ws = [x, y, fmul(fsub(ONE, x), d), fsub(ONE, xy), fmul(fsub(ONE, y), d)]
    if any(w in (ZERO, ONE) for w in ws):
        return None
    return ws


REL = []
for x in SYM:
    for y in SYM:
        ws = FT(x, y)
        if ws is None:
            continue
        v = [0] * N
        for w in ws:
            v[IDX[w]] += 1
        REL.append(v)
detail["five_term_relations"] = len(REL)


def hnf(cols):
    cols = [c[:] for c in cols]
    basis = []
    for i in range(N):
        act = [c for c in cols if c[i] != 0]
        if not act:
            continue
        while len(act) > 1:
            act.sort(key=lambda c: abs(c[i]))
            p0 = act[0]
            for c in act[1:]:
                q = c[i] // p0[i]
                for k in range(N):
                    c[k] -= q * p0[k]
            act = [c for c in act if c[i] != 0]
        piv = act[0]
        if piv[i] < 0:
            piv = [-t for t in piv]
        basis.append((i, piv))
        cols = [c for c in cols if c[i] == 0]
    return basis


def inlat(v, basis):
    v = v[:]
    for i, piv in basis:
        if v[i] % piv[i]:
            return False
        q = v[i] // piv[i]
        for k in range(N):
            v[k] -= q * piv[k]
    return all(t == 0 for t in v)


xi = [0] * N
xi[IDX[Z1]] += 2
xi[IDX[Z2]] += 1
combined = {}
for m in (3, 4, 6, 8, 12, 24):
    Lm = []
    for w in SYM:
        mu = m // gcd(m, gcd(e(w), e(fsub(ONE, w))))
        v = [0] * N
        v[IDX[w]] = mu
        Lm.append(v)
    combined[m] = inlat(xi, hnf(REL + Lm))
detail["combined_condition_feasible"] = combined
checks["obstructed_at_4_6_8_12_24"] = not any(
    combined[m] for m in (4, 6, 8, 12, 24))
checks["m3_door_open"] = combined[3]

# CONTROL: the weaker per-element-only condition still succeeds, so the
# infeasibility above is the SECOND condition biting, not a broken test.
weaker = {}
for m in (3, 24):
    Lm = []
    for w in SYM:
        mu = m // gcd(m, e(w))
        v = [0] * N
        v[IDX[w]] = mu
        Lm.append(v)
    weaker[m] = inlat(xi, hnf(REL + Lm))
detail["weaker_condition_control"] = weaker
checks["control_weaker_condition_still_feasible"] = all(weaker.values())
# CONTROL: the tester rejects a non-member
checks["control_tester_rejects"] = not inlat(
    xi, hnf([[24 if k == i else 0 for k in range(N)] for i in range(N)]))

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_root_ambiguity_criterion_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_root_ambiguity_criterion_probe.py",
    "commitSha": _sha,
    "beans": ["qou-w4gn", "qou-y3xv", "qou-9p9y"],
    "source": ("CGZ arXiv:1712.04887v3 §7 circular units p.33; GSWZ "
               "arXiv:2412.04241v2 eqn (270); shift law "
               "QOU.Machinery.CyclicQuantumDilog (#4964); Addendum 27"),
    "checks": checks,
    "result": detail,
    "scope": (
        "The root ambiguity has the closed form Delta_j = -n_j e(1-w_j) "
        "mod m (verified against every measured twist), giving a SECOND "
        "condition m | n_j e(1-w_j) alongside Addendum 27's "
        "m | n_j e(w_j) -- together mu*_w | n_w with mu* = m/gcd(m, "
        "gcd(e(w), e(1-w))). This is the shape of CGZ's own D*[zeta_D] "
        "elements, whose multiplicity exists for exactly this reason. "
        "Residue-level infeasibility is a SOUND element-level "
        "obstruction (element solutions merge into residue ones; the "
        "converse is the Addendum-25 error and is not used): the "
        "combined condition is INFEASIBLE at m = 4, 6, 8, 12, 24 -- "
        "excluding THIS construction there, not eps_m as a map -- and "
        "FEASIBLE at m = 3, where an element-level representative "
        "meeting both conditions still has to be exhibited (the "
        "single-relation family contains none)."
    ),
}
with open(HERE / "gswz_epsm_root_ambiguity_criterion.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)
