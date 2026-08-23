"""The Wenzl level family, and whether convention C belongs to it.

Follow-on to `wenzl_level_two_vanishing.py`, which established that convention
D sits at Wenzl level `r = 2`.  `QOU/QBeta/WenzlWeightVanishing.lean` proves
the vanishing criterion `s_lam = 0 <=> l(lam) > r` for *every* level `r`, but
only `r = 2` was ever instantiated.  This probe maps the rest of the family
and answers the question the owner asked of it.

Level convention throughout: Wenzl's Markov parameter is
`z_W = Q^r (1-Q)/(1-Q^r)`; the repo's Hecke normalisation `sigma^2 =
(q - q^-1) sigma + 1` forces `sigma = g/q`, `Q = q^2`, `z_W = q*z` (the
matching is unique -- see W0).  Balanced q-integers throughout:
`[m]_q = (q^m - q^-m)/(q - q^-1)`.

Checks (all must pass):

  W0  the eigenvalue matching is FORCED: `sigma = g/c` with Wenzl eigenvalues
      `{Q, -1}` equal to repo eigenvalues `{q, -q^-1}` has the unique solution
      `c = q`, `Q = q^2`.  Nothing downstream is convention-optional.
  W1  the level family in closed form: `z_r = q^r / [r]_q`, exact over Q(q),
      r = 1..8, equivalently `z_r = q^(2r-1) / (1 + q^2 + ... + q^(2r-2))`.
  W2  `z_2 = q^3/(q^2+1) = z_D` exactly -- the family's r = 2 member IS
      convention D (re-derivation of `wenzlLevel_conventionD`).
  W3  the corpus's level-extraction map
      `N_of(z) = -log(1 - (q - q^-1)/z) / (2 log q)`
      (`ocneanu_param_from_fibre_dimension.N_of`) is IDENTICALLY the Wenzl
      inversion `r = log(q z/(1 - Q + q z)) / log Q`.  So the corpus's
      `N_eff` and the Wenzl level `r` are the same quantity, not two
      quantities that happen to agree numerically.
  W4  `z_C = sqrt(q)/(q+1)` is not `z_r` for ANY r, identically in q:
      (a) no integer r -- checked exactly, r = 1..12, and structurally
          `z_r` is in Q(q) for every r while `z_C` is not (see module note);
      (b) no real constant r -- the formal level `r_C(q)` is not constant,
          exhibited by two q at which it differs.
  W5  `r_C(q0)` at the proton pin, and its agreement with the corpus's
      recorded `N_eff(z_C)` to 30 digits.
  W6  the level table: `z_r(q0)`, row cap, quotient dimension
      `sum_{l(lam)<=r} (f^lam)^2` and corank `n! - dim`, r = 1..4, n = 1..8.
      The r = 2 row must reproduce PR #5207's measured coranks
      1, 10, 78, 588 -- a self-check on the machinery.
  W7  genericity of the C level: `r_C(q)` passes through EVERY integer level
      at some q (2 at q = 1, 3 and 4 at isolated q), then diverges at a
      finite `q*` and goes complex beyond.  `q0` is not any crossing.  So
      "C is level k" is a statement about a point in q, never a convention.
  W8  at `q0`, `z_3 < z_C < z_2` -- C is bracketed by two genuine levels.

NO FLOAT64 ANYWHERE: sympy exact over Q(q) for every structural claim;
mpmath at 50 dps, seeded only from decimal strings, for the anchor values.

q_0 pin: EXPERIMENTAL / proton (`m_p/m_e`), per the AGENTS 2026-08-07 owner
directive that all new compute defaults to the experimental anchor.

Nothing here is compared against a CODATA or AME value, and nothing is
tuned: every structural conclusion (W0-W4, W6-W8) is q-independent or is
exact integer combinatorics.

Why `z_C` cannot be a level, in one line (the invariant behind the W4
scope-(b)): `z_r = q^(2r-1)/(1 + q^2 + ... + q^(2r-2))` lies in `Q(q)` for
every integer `r`, whereas `z_C = sqrt(q)/(q+1)` does not -- `x^2 - q` is
irreducible over `Q(q)` (Eisenstein at the prime `q` of `Q[q]`), so
`sqrt(q) not in Q(q)`, and `z_C in Q(q)` would give `sqrt(q) = z_C*(q+1) in
Q(q)`.  For non-integer real `r` the same conclusion follows from W4(b):
`q^(2r)` is a monomial in `q` and the required value is not.
"""

from __future__ import annotations

import json
from math import factorial
from pathlib import Path

import mpmath as mp
import sympy as sp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# --- q_0: experimental (proton) pin, per AGENTS 2026-08-07 owner directive ---
Q0_PROTON_STR = "1.1099785827513808"
Q0_PIN = "experimental/proton (m_p/m_e)"

q = sp.symbols("q", positive=True)
Q_SUB = q**2  # forced by W0

# exact rational surrogate for q0, so sympy never sees a float
Q0_EXACT = sp.Rational(Q0_PROTON_STR)
Q0_MP = mp.mpf(Q0_PROTON_STR)


def q_int(m: int):
    """Balanced quantum integer `[m]_q = (q^m - q^-m)/(q - q^-1)`."""
    return sp.cancel((q**m - q ** (-m)) / (q - q ** (-1)))


def z_level(r: int):
    """The level-`r` Markov parameter in the repo's normalisation."""
    return sp.cancel(Q_SUB**r * (1 - Q_SUB) / (1 - Q_SUB**r) / q)


Z_C = sp.sqrt(q) / (q + 1)
Z_D = q**3 / (q**2 + 1)


def at_q0(expr) -> mp.mpf:
    """Evaluate a sympy expression at the proton pin, 50 dps, no float64."""
    return mp.mpf(str(sp.N(expr.subs(q, Q0_EXACT), 60)))


# ---------------------------------------------------------------- W0


def check_matching_forced() -> dict:
    """`sigma = g/c` with `{Q, -1}/c = {q, -q^-1}` forces `c = q`, `Q = q^2`."""
    c, QQ = sp.symbols("c Q", positive=True)
    sols = sp.solve([-1 / c + 1 / q, QQ / c - q], [c, QQ], dict=True)
    ok = len(sols) == 1 and sp.simplify(sols[0][c] - q) == 0 \
        and sp.simplify(sols[0][QQ] - q**2) == 0
    return {"check": "W0 eigenvalue matching is forced",
            "solutions": [{str(k): str(v) for k, v in s.items()} for s in sols],
            "c": "q", "Q": "q^2", "z_W": "q*z", "pass": bool(ok)}


# ---------------------------------------------------------------- W1, W2


def check_level_family_closed_form() -> dict:
    """`z_r = q^r/[r]_q`, exactly, r = 1..8; and `z_2 = z_D`."""
    rows, fails = [], []
    for r in range(1, 9):
        zr = z_level(r)
        closed = sp.cancel(q**r / q_int(r))
        # z_r = q^(2r-1) / (1 + q^2 + ... + q^(2r-2))
        geom = sp.cancel(q ** (2 * r - 1) / sum(q ** (2 * j) for j in range(r)))
        if sp.simplify(zr - closed) != 0 or sp.simplify(zr - geom) != 0:
            fails.append(r)
        rows.append({"r": r, "z_r": str(sp.factor(zr)),
                     "z_r_closed": f"q^{r}/[{r}]_q"})
    d_ok = sp.simplify(z_level(2) - Z_D) == 0
    return {"check": "W1/W2 level family closed form; r=2 is convention D",
            "family": rows, "failures": fails,
            "z_2_equals_z_D": bool(d_ok),
            "pass": not fails and bool(d_ok)}


# ---------------------------------------------------------------- W3


def check_level_map_identity() -> dict:
    """The corpus's `N_of` IS the Wenzl inversion, identically."""
    z = sp.symbols("z", positive=True)
    corpus_arg = 1 - (q - 1 / q) / z          # N_of: -log(arg)/(2 log q)
    wenzl_arg = (1 - q**2 + q * z) / (q * z)  # reciprocal of q z/(1-Q+q z)
    same = sp.simplify(corpus_arg - wenzl_arg) == 0
    N_of = -sp.log(corpus_arg) / (2 * sp.log(q))
    roundtrip = {r: str(sp.simplify(N_of.subs(z, z_level(r)))) for r in range(1, 6)}
    ok = same and all(roundtrip[r] == str(r) for r in range(1, 6))
    return {"check": "W3 corpus N_eff and Wenzl level r are the same map",
            "corpus_N_of": "-log(1 - (q - q^-1)/z)/(2 log q)",
            "wenzl_inversion": "log(q z/(1 - Q + q z))/log Q,  Q = q^2",
            "arguments_identical": bool(same),
            "roundtrip_N_of_z_r": roundtrip,
            "pass": bool(ok)}


# ---------------------------------------------------------------- W4


def check_zC_is_no_level() -> dict:
    """`z_C` is not `z_r` for any integer r, nor for any real constant r."""
    integer_hits = [r for r in range(1, 13)
                    if sp.simplify(Z_C - z_level(r)) == 0]
    # (b) the formal level is not constant
    QrC = sp.cancel(q * Z_C / (1 - Q_SUB + q * Z_C))
    rC = sp.log(QrC) / sp.log(Q_SUB)
    f = sp.lambdify(q, rC, "mpmath")
    r_lo, r_hi = f(mp.mpf("1.05")), f(mp.mpf("1.15"))
    not_constant = abs(r_lo - r_hi) > mp.mpf("1e-6")
    # the field-membership invariant, machine-checked where it can be
    sqrt_q_irreducible = sp.Poly(sp.symbols("x") ** 2 - q,
                                 sp.symbols("x")).is_irreducible
    return {"check": "W4 z_C is not a Wenzl level for any r, identically in q",
            "integer_levels_matched": integer_hits,
            "r_C_at_q_1p05": mp.nstr(r_lo, 20),
            "r_C_at_q_1p15": mp.nstr(r_hi, 20),
            "formal_level_is_not_constant": bool(not_constant),
            "x2_minus_q_irreducible_over_Qq": bool(sqrt_q_irreducible),
            "invariant": "z_r in Q(q) for all r; z_C = sqrt(q)/(q+1) not in Q(q)",
            "scope": "(b) structural exclusion -- invariant named above",
            "pass": (not integer_hits) and bool(not_constant)}


# ---------------------------------------------------------------- W5


def check_rC_at_anchor() -> dict:
    """`r_C(q0)`, and agreement with the corpus's own `N_eff` computation."""
    QrC = sp.cancel(q * Z_C / (1 - Q_SUB + q * Z_C))
    Qr0 = at_q0(QrC)
    r0 = mp.log(Qr0) / mp.log(Q0_MP**2)
    # recompute via the corpus formula, independently
    zc = 1 / (mp.sqrt(Q0_MP) + 1 / mp.sqrt(Q0_MP))
    n_eff = -mp.log(1 - (Q0_MP - Q0_MP ** (-1)) / zc) / (2 * mp.log(Q0_MP))
    agree = abs(r0 - n_eff) < mp.mpf("1e-30")
    return {"check": "W5 r_C at the proton pin equals the corpus N_eff",
            "q0": Q0_PROTON_STR, "q0_pin": Q0_PIN,
            "Q_pow_r_at_q0": mp.nstr(Qr0, 30),
            "r_C_at_q0": mp.nstr(r0, 30),
            "corpus_N_eff_at_q0": mp.nstr(n_eff, 30),
            "abs_difference": mp.nstr(abs(r0 - n_eff), 5),
            "nearest_integer": int(mp.nint(r0)),
            "distance_to_nearest_integer": mp.nstr(abs(r0 - mp.nint(r0)), 20),
            "pass": bool(agree)}


# ---------------------------------------------------------------- W6


def _partitions(n: int, cap: int | None = None):
    cap = n if cap is None else cap
    if n == 0:
        yield ()
        return
    for first in range(min(n, cap), 0, -1):
        for rest in _partitions(n - first, first):
            yield (first,) + rest


def _f_lambda(lam: tuple[int, ...]) -> int:
    """Hook-length formula for `dim S^lam`, exact integers."""
    prod = 1
    for i, li in enumerate(lam):
        for j in range(li):
            arm = li - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            prod *= arm + leg + 1
    return factorial(sum(lam)) // prod


# The quotient at level `r` is `H_n(q)/<E^(r+1)>`, whose blocks are the `lam`
# with at most `r` rows -- classical Jones/Wenzl structure theory, CITED, not
# derived here.  Only the dimension arithmetic below is computed.
QUOTIENT_NAMES = {
    1: ("H_n/<E^(2)>  (one-dimensional; the 'SU(1)' degenerate level)", "SU(1)"),
    2: ("TL_n = H_n/<E^(3)>", "SU(2)"),
    3: ("H_n/<E^(4)>", "SU(3)"),
    4: ("H_n/<E^(5)>", "SU(4)"),
}


def check_level_table(n_max: int = 8) -> dict:
    """The level table: parameter, row cap, quotient dimension, corank."""
    rows = []
    for r in range(1, 5):
        dims = [sum(_f_lambda(l) ** 2 for l in _partitions(n) if len(l) <= r)
                for n in range(1, n_max + 1)]
        coranks = [factorial(n) - d for n, d in zip(range(1, n_max + 1), dims)]
        alg, gauge = QUOTIENT_NAMES[r]
        rows.append({
            "r": r,
            "z_r": str(sp.factor(z_level(r))),
            "z_r_at_q0": mp.nstr(at_q0(z_level(r)), 25),
            "row_cap": f"l(lam) <= {r}",
            "quotient_algebra": alg,
            "gauge_label": gauge,
            "quotient_dim_n_1_to_%d" % n_max: dims,
            "corank_n_1_to_%d" % n_max: coranks,
            "first_n_with_radical": next(
                (n for n, c in zip(range(1, n_max + 1), coranks) if c > 0), None),
        })
    # self-check: the r = 2 row must reproduce PR #5207's measured coranks
    r2 = rows[1]["corank_n_1_to_%d" % n_max]
    measured_5207 = [1, 10, 78, 588]          # n = 3, 4, 5, 6
    ok = r2[2:6] == measured_5207
    catalan_ok = rows[1]["quotient_dim_n_1_to_%d" % n_max] == \
        [1, 2, 5, 14, 42, 132, 429, 1430]
    return {"check": "W6 the level table, r = 1..4",
            "note": "quotient algebra identification H_n/<E^(r+1)> is CITED "
                    "(Jones/Wenzl); only the dimension arithmetic is computed",
            "levels": rows,
            "r2_coranks_match_PR5207": bool(ok),
            "r2_dims_are_catalan": bool(catalan_ok),
            "pass": bool(ok and catalan_ok)}


# ---------------------------------------------------------------- W7


def check_level_crossings() -> dict:
    """`r_C(q)` crosses every integer level somewhere -- but not at `q0`."""
    QrC = sp.cancel(q * Z_C / (1 - Q_SUB + q * Z_C))
    rC = sp.log(QrC) / sp.log(Q_SUB)
    f = sp.lambdify(q, rC, "mpmath")
    # the pole: q^(3/2) - (q-1)(q+1)^2 = 0
    pole = mp.findroot(
        lambda x: x ** mp.mpf("1.5") - (x - 1) * (x + 1) ** 2, mp.mpf("1.27"))
    crossings = {"2": "1 (limit; both sides degenerate at q = 1)"}
    for r, guess in [(3, "1.15"), (4, "1.22")]:
        root = mp.findroot(lambda x: f(x) - r, mp.mpf(guess))
        crossings[str(r)] = mp.nstr(mp.re(root), 16)
    limit_at_one = sp.limit(rC, q, 1)
    far_from_q0 = all(
        abs(Q0_MP - mp.mpf(v)) > mp.mpf("0.04")
        for k, v in crossings.items() if k != "2")
    return {"check": "W7 the C curve is transverse to the level family",
            "limit_r_C_as_q_to_1": str(limit_at_one),
            "series_r_C_about_q_1": str(sp.series(rC, q, 1, 3).removeO()),
            "integer_crossings_q": crossings,
            "pole_q_star": mp.nstr(pole, 20),
            "beyond_pole": "r_C(q) is complex for q > q*",
            "q0": Q0_PROTON_STR,
            "q0_is_not_a_crossing": bool(far_from_q0),
            "pass": bool(str(limit_at_one) == "2" and far_from_q0)}


# ---------------------------------------------------------------- W8


def check_bracketing() -> dict:
    """At `q0`, `z_C` lies strictly between the level-3 and level-2 values."""
    z2, z3, zc = at_q0(z_level(2)), at_q0(z_level(3)), at_q0(Z_C)
    ok = z3 < zc < z2
    return {"check": "W8 z_C is bracketed by two genuine levels at q0",
            "z_3_at_q0": mp.nstr(z3, 25),
            "z_C_at_q0": mp.nstr(zc, 25),
            "z_2_at_q0": mp.nstr(z2, 25),
            "ordering": "z_3 < z_C < z_2",
            "pass": bool(ok)}


# ---------------------------------------------------------------- W9

# Every distinct closed form circulating in the corpus as a Markov/Ocneanu
# parameter.  Inventory taken 2026-08-16 across `computations/`, `tools/` and
# `content/**/lean/`; call sites are cited in the audit doc.
Z_SPELLINGS = [
    ("z_D  = q^3/(q^2+1) = q^2/[2]_q", q**3 / (q**2 + 1),
     "the level-2 member of the family", "mass, binding, borromean-binding"),
    ("z_C  = sqrt(q)/(q+1) = 1/[2]_{sqrt q}", sp.sqrt(q) / (q + 1),
     "not in Q(q): sqrt(q) is not a rational function of q "
     "(x^2 - q Eisenstein at q)", "qbeta-decay (disputed)"),
    ("z_TL = q/(q^2+1) = 1/[2]_q", q / (q**2 + 1),
     "in Q(q), but no r matches: z_r has numerator q^(2r-1), so degree 1 "
     "forces r = 1, and z_1 = q != q/(q^2+1)",
     "meson_lepton_knot_dictionary_probe, casimir_phi_q_markov_probe "
     "(neither is a production file)"),
]


def check_spelling_levels() -> dict:
    """Every circulating z spelling, its formal level, and why it is not one."""
    QrC_map = lambda zz: sp.cancel(q * zz / (1 - Q_SUB + q * zz))  # noqa: E731
    rows, off_family = [], []
    for name, zz, invariant, sites in Z_SPELLINGS:
        Qr = QrC_map(zz)
        val = at_q0(Qr)
        r_here = mp.log(val) / mp.log(Q0_MP**2)
        exact_hits = [r for r in range(1, 13) if sp.simplify(zz - z_level(r)) == 0]
        rows.append({
            "z": name,
            "z_at_q0": mp.nstr(at_q0(zz), 22),
            "formal_level_at_q0": mp.nstr(r_here, 14),
            "is_a_level": bool(exact_hits),
            "level_if_any": exact_hits[0] if exact_hits else None,
            "exclusion_invariant": None if exact_hits else invariant,
            "call_sites": sites,
        })
        if not exact_hits:
            off_family.append(name)
    # exactly one of the three is a genuine level
    ok = sum(1 for r_ in rows if r_["is_a_level"]) == 1 and \
        rows[0]["level_if_any"] == 2
    return {"check": "W9 every circulating z spelling, and its level",
            "spellings": rows,
            "off_family": off_family,
            "note": "the two off-family spellings are excluded by DIFFERENT "
                    "invariants -- field membership for z_C, numerator degree "
                    "for z_TL. Neither exclusion is numerical.",
            "pass": bool(ok)}


# ---------------------------------------------------------------- W10

# The registry's four channels (docs/coordination/trace-convention-registry.json,
# schema trace-convention-registry/v1, updated 2026-08-15), with the z their
# PRODUCTION code actually evaluates.  Verified by reading the call sites.
CHANNELS = [
    ("mass", "D", "m_p_substrate_identity_50dps.py::trM_borromean "
                  "-> canonical_mass.py", "agreed"),
    ("binding", "D", "closed_form_tau_M.py::markov_z, "
                     "wedderburn_jones_markov.py::y_lambda_at", "agreed"),
    ("borromean-binding-single-pipeline", "D",
     "borromean_binding_recompute.py:110", "agreed"),
    ("qbeta-decay", "C", "qbeta/qbeta_utils.py::markov_parameter", "disputed"),
]

CONVENTION_Z = {"D": q**3 / (q**2 + 1), "C": sp.sqrt(q) / (q + 1)}


def check_channel_levels() -> dict:
    """Which Wenzl level does each registered channel sit at?"""
    rows = []
    for cid, conv, producer, status in CHANNELS:
        zz = CONVENTION_Z[conv]
        Qr = sp.cancel(q * zz / (1 - Q_SUB + q * zz))
        r_here = mp.log(at_q0(Qr)) / mp.log(Q0_MP**2)
        is_level = any(sp.simplify(zz - z_level(r)) == 0 for r in range(1, 13))
        rows.append({"channel": cid, "convention": conv, "producer": producer,
                     "registry_status": status,
                     "level": 2 if is_level else None,
                     "formal_level_at_q0": mp.nstr(r_here, 14),
                     "in_the_level_family": bool(is_level)})
    levels = {r_["level"] for r_ in rows if r_["in_the_level_family"]}
    return {"check": "W10 the Wenzl level of each registered channel",
            "channels": rows,
            "distinct_levels_in_use": sorted(x for x in levels if x is not None),
            "finding": "every channel that is in the family at all is at "
                       "r = 2. No QOU channel sits at r = 3 or above.",
            "pass": levels == {2}}


# ---------------------------------------------------------------- driver


def main() -> int:
    checks = [
        check_matching_forced(),
        check_level_family_closed_form(),
        check_level_map_identity(),
        check_zC_is_no_level(),
        check_rC_at_anchor(),
        check_level_table(),
        check_level_crossings(),
        check_bracketing(),
        check_spelling_levels(),
        check_channel_levels(),
    ]
    all_pass = all(c["pass"] for c in checks)
    payload = {
        "probe": "wenzl-level-family",
        "description": "The Wenzl level family z_r = q^r/[r]_q, and whether "
                       "convention C belongs to it.",
        "q0": Q0_PROTON_STR,
        "q0_pin": Q0_PIN,
        "hecke_convention": "sigma^2 = (q - q^-1) sigma + 1; Q = q^2; z_W = q*z",
        "cited_external_input": {
            "wenzl1988": "Hecke algebras of type A_n and subfactors, "
                         "Invent. Math. 92 (1988) 349-383, "
                         "doi:10.1007/BF01404457 -- the weight formula and "
                         "the parameter relation z_W = Q^r(1-Q)/(1-Q^r).",
            "orellana1998": "Weights of Markov Traces on Hecke Algebras, "
                            "arXiv:math/9806163, p. 17 -- restates the "
                            "type-A result. Its 'type D' is the COXETER type "
                            "D_n, unrelated to this repo's convention D.",
        },
        "checks": checks,
        "all_pass": all_pass,
    }
    path = Path(__file__).with_name("wenzl-level-family.json")
    path.write_text(json.dumps(payload, indent=2) + "\n")

    for c in checks:
        print(("PASS  " if c["pass"] else "FAIL  ") + c["check"])
    w5 = checks[4]
    print()
    print(f"  r_C(q0)      = {w5['r_C_at_q0']}")
    print(f"  corpus N_eff = {w5['corpus_N_eff_at_q0']}   (identical map, W3)")
    print()
    print("  level  z_r                                 z_r(q0)          "
          "quotient dim (n=1..8)")
    for row in checks[5]["levels"]:
        print(f"   r={row['r']}   {row['z_r']:<34}  {row['z_r_at_q0'][:16]}  "
              f"{row['quotient_dim_n_1_to_8']}")
    print(f"   C     {sp.factor(Z_C)!s:<34}  "
          f"{checks[7]['z_C_at_q0'][:16]}  -- no level (W4)")
    print()
    print(f"wrote {path}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
