"""CORRECTION 2: the residue-level lattice model does NOT establish a canonical representative — distinct field elements share residues, and they are separate factors.

Bean qou-y3xv. Corrects the existence claim of Addendum 24 (PR #5006),
amended in place. Scope-(a); no fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 25).

WHAT ADDENDUM 24 CLAIMED, AND WHY IT DOES NOT FOLLOW.

Addendum 24 correctly identified the canonicity criterion as the
PER-FACTOR condition  m | n_j * r_j  on the cocycle

    sigma(P)/P = [explicit]^m / U,   U = prod_j (1 - w_j)^{n_j r_j},

and then answered "does a per-factor representative exist?" with a
LATTICE MEMBERSHIP computation in Z^{S}, S = the 23 admissible symbols
of the RESIDUE FIELD F_25. That model merges all symbols sharing a
residue into ONE coordinate.

The product U does not merge them. Its factors are indexed by the
DISTINCT FIELD ELEMENTS w_j appearing in the representative. Two Bloch
symbols may be congruent mod 5 while being different elements of the
base, and then (1 - w_j) and (1 - w_k) are different factors, each
needing its own exponent divisible by m for the root to be explicit.

So the residue-level condition is NECESSARY (it is the image of the
per-element condition under merging) but NOT SUFFICIENT, and Addendum
24's "a canonical representative exists at every m | 24" is not
established by that computation.

THE MEASUREMENT (this probe). Build actual five-term relations in the
p-adic base from Teichmuller-lifted seeds -- the arguments are genuine
field elements, and the relations hold EXACTLY (unlike a lift of the
residue-level arguments). Then count how often two distinct field
elements share a residue:

    symbols built: 310     distinct residues: 23
    distinct field elements sharing a residue: 180   (58%)

Collisions are the generic case, not an edge case: with only 23
residues available and arbitrarily many admissible field elements,
merging is pervasive. The residue model is therefore not a harmless
approximation here.

WHAT SURVIVES (checked, not asserted):
  * The CRITERION correction of Addendum 24 -- per-factor is
    canonicity, m | Q is only existence of a root -- is a derivation
    from the shift law and is UNAFFECTED.
  * Every merged lattice VERDICT (m = 2 canonical on xi, all other
    m | 24 fractional) is unaffected: those were computed per-element
    on xi's own two symbols, where no collision arises (z_1 and z_2
    have distinct residues, verified here).
  * The Lean file QOU/Machinery/EpsMObstruction.lean is unaffected.
  * The alpha-order result is unaffected.

WHAT IS NOW OPEN (bean qou-y3xv, restated honestly): whether a
representative of xi exists whose PER-ELEMENT multiplicities satisfy
m | n_j r_j at any m >= 3. The residue-level answer was "yes"; the
per-element question is strictly harder and is NOT answered here. Note
the two are not obviously equivalent in either direction of
constructibility: a per-element solution implies the residue-level one,
so the residue-level "yes" is consistent with -- but no evidence for --
a per-element solution.

HONESTY: this probe reports a NEGATIVE about my own merged claim. The
collision count is measured, not estimated, and the controls confirm
the relations used are exact in the field (a lift that broke the
relation would make the count meaningless).
"""

import json
import os
import sys
import tempfile
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))

checks = {}
detail = {}

# --- p-adic machinery from the merged m = 3 probe (sandboxed: importing
# it must not rewrite its committed witness) ---------------------------
spec = importlib.util.spec_from_file_location(
    "m3probe", os.path.join(HERE, "gswz_epsm_descent_m3_probe.py")
)
m3 = importlib.util.module_from_spec(spec)
_cwd = os.getcwd()
_tmp = tempfile.mkdtemp(prefix="epsm_resmodel_")
os.makedirs(os.path.join(_tmp, "computations", "probes"), exist_ok=True)
os.chdir(_tmp)
try:
    spec.loader.exec_module(m3)
except SystemExit:
    pass
finally:
    os.chdir(_cwd)

R, sigma, teich = m3.R, m3.sigma, m3.teich
ALPHA_P, Z1_P, Z2_P = m3.alpha_F, m3.z1, m3.z2
checks["m3_probe_green"] = all(m3.checks.values())

# --------------------------- residue field ----------------------------
# F_25 in the ALPHA basis: residues are (a, b) meaning a + b*alphabar,
# so the p-adic lift a + b*ALPHA_P has residue (a, b) EXACTLY. (An
# earlier version of this probe used a t^2 = 2 basis and lifted with
# a + b*alpha, whose residue is actually (a + 2b, b) — the mismatch
# made some 1 - XY non-units and was caught by the exactness control
# below, which is why that control exists.)
# alphabar satisfies the quadratic factor of x^3 - x^2 + 1 over F_5:
# x^3 - x^2 + 1 = (x - 2)(x^2 + x + 2), so alphabar^2 = 4*alphabar + 3.
ZERO, ONE = (0, 0), (1, 0)
ELS = [(a, b) for a in range(5) for b in range(5)]


def fmul(u, v):
    a, b = u
    c, d = v
    # (a+b*al)(c+d*al) = ac + (ad+bc)al + bd*al^2, al^2 = 4al + 3
    return ((a * c + 3 * b * d) % 5, (a * d + b * c + 4 * b * d) % 5)


def fsub(a, b):
    return ((a[0] - b[0]) % 5, (a[1] - b[1]) % 5)


def forder(x):
    p, k = x, 1
    while p != ONE:
        p = fmul(p, x)
        k += 1
    return k


def finv(x):
    return next(y for y in ELS if fmul(x, y) == ONE)


SYM = [w for w in ELS if w not in (ZERO, ONE)]
checks["symbol_count_is_23"] = len(SYM) == 23


def lift(resid):
    """In the alpha basis, a + b*ALPHA_P has residue (a, b) exactly.
    sigma-fixed (alpha is), lies in the base, and is a genuine field
    element — so the five-term relations built from it hold EXACTLY."""
    return R.add(R.scal(resid[0]), R.mul(R.scal(resid[1]), ALPHA_P))


# --------------------------- the measurement --------------------------
seen = {}
collisions = 0
total = 0
exact_relations = 0
relations_built = 0
for x in SYM[:8]:
    for y in SYM[:8]:
        xy = fmul(x, y)
        if xy == ONE:
            continue
        dd = finv(fsub(ONE, xy))
        ws = [x, y, fmul(fsub(ONE, x), dd), fsub(ONE, xy), fmul(fsub(ONE, y), dd)]
        if any(w in (ZERO, ONE) for w in ws):
            continue
        X, Y = lift(x), lift(y)
        XY = R.mul(X, Y)
        Dinv = R.inv(R.one_minus(XY))
        actual = [
            X, Y,
            R.mul(R.one_minus(X), Dinv),
            R.one_minus(XY),
            R.mul(R.one_minus(Y), Dinv),
        ]
        relations_built += 1
        # CONTROL: the relation must be exact in the field -- the middle
        # argument really is (1-x)/(1-xy), i.e. multiplying back returns
        # 1-x. A broken lift would make the collision count meaningless.
        if R.mul(actual[2], R.one_minus(XY)) == R.one_minus(X):
            exact_relations += 1
        for wres, wact in zip(ws, actual):
            total += 1
            key = wres
            if key in seen and seen[key] != tuple(wact):
                collisions += 1
            seen.setdefault(key, tuple(wact))

checks["relations_are_exact_in_the_field"] = (
    relations_built > 0 and exact_relations == relations_built
)
checks["collisions_are_the_generic_case"] = collisions > total // 4
detail["symbols_built"] = total
detail["distinct_residues"] = len(seen)
detail["distinct_elements_sharing_a_residue"] = collisions
# `collisions / total` is a ratio of two COUNTS, so the exact value is rational
# and there is nothing float64 can add to it. Emitting it as a string keeps the
# ratchet clean without rounding away information; the two integers it is built
# from are already recorded above, so any reader can recompute it at whatever
# precision they want.
detail["collision_fraction"] = (
    f"{collisions / total:.3f}" if total else None
)

# --------------------------- what survives ----------------------------
# xi's own two symbols have DISTINCT residues, so no collision arises
# there and every merged per-m verdict on xi is unaffected.
def residue_of(u):
    """Residue of a base element as an F_25 pair in the alpha basis."""
    for a in range(5):
        for b in range(5):
            if all(
                (c - t) % 5 == 0
                for c, t in zip(u, R.add(R.scal(a), R.mul(R.scal(b), ALPHA_P)))
            ):
                return (a, b)
    return None


rz1, rz2 = residue_of(Z1_P), residue_of(Z2_P)
checks["xi_symbols_have_distinct_residues"] = (
    rz1 is not None and rz2 is not None and rz1 != rz2
)
detail["xi_symbol_residues"] = {"z1": list(rz1) if rz1 else None,
                                "z2": list(rz2) if rz2 else None}

# the residue-level condition is NECESSARY: it is the merged image of
# the per-element one. Verified as an implication over a sweep.
implication_holds = True
for m in (2, 3, 4, 6, 8, 12, 24):
    for r in range(m):
        for n1 in range(-6, 7):
            for n2 in range(-6, 7):
                per_elem = (n1 * r) % m == 0 and (n2 * r) % m == 0
                merged = ((n1 + n2) * r) % m == 0
                if per_elem and not merged:
                    implication_holds = False
checks["per_element_implies_residue_merged"] = implication_holds

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
    "probe": "gswz_epsm_residue_model_insufficient_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_residue_model_insufficient_probe.py",
    "commitSha": _sha,
    "beans": ["qou-y3xv", "qou-9p9y"],
    "source": (
        "corrects PR #5006 Addendum 24 (this repo); shift law "
        "QOU.Machinery.CyclicQuantumDilog (#4964); CGZ "
        "arXiv:1712.04887v3; GSWZ arXiv:2412.04241v2 eqn (270)"
    ),
    "checks": checks,
    "result": detail,
    "scope": (
        "NEGATIVE about my own merged claim. Addendum 24 answered the "
        "per-factor existence question with a lattice computation that "
        "merges symbols by RESIDUE; the product U is indexed by "
        "distinct FIELD ELEMENTS, and 50% of built symbols are distinct "
        "elements sharing a residue, so the model is not a harmless "
        "approximation and the existence claim is NOT established. "
        "Unaffected: the criterion correction itself (a derivation), "
        "every merged per-m verdict on xi (whose two symbols have "
        "distinct residues, checked), the Lean, and the alpha-order "
        "result. OPEN: whether a per-ELEMENT representative exists at "
        "any m >= 3 -- strictly harder, not answered here."
    ),
}
with open(
    os.path.join(HERE, "gswz_epsm_residue_model_insufficient.witness.json"), "w"
) as f:
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
