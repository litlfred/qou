#!/usr/bin/env python3
"""The float64 path out of the UIC resolvent cone is gone -- and what is left.

Owner directive 2026-09-12, verbatim: "excise float64".  Bean `qou-oiz3`;
follows PR #7237 / bean `qou-t6be`, which measured `mu_lambda` and `s_*` in
float64 and deliberately did not fix them ("fixing it moves every binding
number").

WHAT THIS PROBE ESTABLISHES

1. TYPE.  Every quantity on the resolvent path -- `S_REEB_PLANCK` (s_*),
   `q_laplacian_eigenvalue` (mu_lambda), `q_resolvent_weight` (rho_lambda),
   `partition_character_sigma1`, and the four derived columns of
   `_PARTITION_TABLE` -- is an `mpf`.

2. SOURCE.  The named functions no longer MENTION the float64 route.  Checked
   by AST over each function's own body, not by grep over the file, so a
   `math.log` in a neighbouring function cannot make this pass or fail.  The
   distinction matters: a value can be `mpf`-TYPED and float64-VALUED (see 5),
   so a type check alone is not evidence the path is gone.

3. VALUE.  s_* moves off its float64 twin by 1.99757e-16 relative -- i.e. it
   is a DIFFERENT number, not the same one re-typed.  The old constant is
   reconstructed here from the float64 `q_parameter.Q` so the comparison is
   against what the tree actually held, not against a remembered figure.

4. STABILITY under a working-precision increase, and the INPUT CEILING, which
   are two different facts and are checked separately.  rho_lambda recomputed
   at `mp.dps` = 70 and 90 agrees to 1.96e-71 -- that is the ARITHMETIC
   reproducing itself, and it is silent about the input, because both runs read
   the same `_Q_MP`.  What bounds the input is measured against `q_at(90)`:
   `_Q_MP` is built from `Q_50_DIGIT_STR` and sits 9.91e-52 from a
   full-precision solve.  So the honest statement is 50 significant digits,
   which is BELOW `OUTPUT_DPS = 60` -- a value serialized at 60 digits from
   this q has ~8 digits nothing supplies.  Recorded as a residual, not fixed
   here; it is 36 orders of magnitude tighter than the float64 path it
   replaces.  An earlier draft of this docstring asserted the 70 -> 90 check
   would land near 1e-50 and "not further"; it lands at 1e-71, because it never
   touched the input at all.

5. THE RESIDUAL, measured rather than asserted away.  `q_hook_product`,
   `q_factorial` and `wedderburn_weight` return `mpf` and accumulate
   `mp.mpf(1) * q_int(k)` over the FLOAT64 `q_int` -- float64 values in mpf
   clothing.  So C_lambda = m_e * H_q * y_lambda * rho_lambda is still
   float64-limited through three of its four factors.  Measured against an
   all-mpf recomputation the residual is ~1e-15, which is LARGER than the
   ~2.5e-16 this excision removes.  Asserted as an upper bound so a regression
   fails, and reported as an open surface: the root fix is `q_int` itself,
   which is 124 Python files and 243 witnesses (bean `qou-oiz3`) and is an
   owner call, not an agent sweep.

WHAT IS NOT CLAIMED

That the binding numbers are now correct, or that they were wrong before.  A
float64 residual of ~1e-16 is the floor of the arithmetic that produced it: it
BOUNDS the damage and cannot distinguish a correctly-rounded float64 from a
slightly-wrong one.  What settles that is the mpf recomputation, and what it
says is recorded in the audit -- the per-atom totals move by at most 8.44e-16
relative (2.54e-17 MeV absolute), and at k_exact = 4, Z = 4, N = 4 that
relative figure EXCEEDS the per-block float64 floor by 3.8x, through
cancellation rather than through error growth.

scope-(a); no fit; no c_k; nothing wired; L2 unchanged.
"""
from __future__ import annotations

import ast
import inspect
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))

import _path_bridge  # noqa: F401,E402

from mpmath import mp  # noqa: E402

import hecke_core_legacy as H  # noqa: E402
import q_parameter as QP  # noqa: E402
from pyhecke.wedderburn import partition_dimension, partitions_of  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import COMPUTE_DPS, set_compute_dps, fmt  # noqa: E402

CHECKS: list[tuple[str, bool]] = []

# The functions whose bodies must not mention the float64 route, and what
# counts as that route.  `float(` is banned outright: AGENTS.md permits it only
# inside an f-string for display, and none of these has one.
FLOAT64_CALLS = {"math.log", "math.exp", "math.sqrt", "math.pow", "float"}
CONE = [
    "q_laplacian_eigenvalue",
    "q_resolvent_weight",
    "partition_character_sigma1",
    "partition_spectral_log_rate",
    "_partition_table_exact",
    "conjugate_pair_cross_term",
    "unified_iterative_correction_jet",
    "atom_markov_trace",
    "atom_frobenius_norm_sq",
]
# Partitions the accumulator actually weights: dim >= 2 (the one-dimensional
# trivial and sign blocks carry y_lambda = 0 exactly and contribute nothing,
# so a relative error on their scale is a relative error on zero).
LAMBDAS = [lam for k in range(2, 8) for lam in partitions_of(k)
           if partition_dimension(lam) >= 2]


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))


def _dotted(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return _dotted(node.value) + "." + node.attr
    return ""


def float64_calls_in(fn_name: str) -> list[str]:
    """Names of float64-returning calls in one function's OWN body."""
    tree = ast.parse(textwrap.dedent(inspect.getsource(getattr(H, fn_name))))
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = _dotted(node.func)
            if name in FLOAT64_CALLS or name == "q_int":
                bad.append(name)
    return bad


# ── the all-mpf reference: the same formulas over an mpf q-integer ──────
def _q_int_mp(n: int):
    return (QP.Q_MP ** n - QP.Q_INV_MP ** n) / QP.HA_MP


def _hooks(lam):
    lam = list(lam)
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    return [(li - j - 1) + (conj[j] - i - 1) + 1
            for i, li in enumerate(lam) for j in range(li)]


def _hq(lam, qi):
    H_ = mp.mpf(1)
    for hl in _hooks(lam):
        H_ *= qi(hl)
    return H_


def _qfact(n, qi):
    f = mp.mpf(1)
    for i in range(1, n + 1):
        f *= qi(i)
    return f


def _y(lam, qi):
    n = sum(lam)
    dq = _qfact(n, qi) / _hq(lam, qi)
    return (dq ** 2 / _qfact(n, qi)) / partition_dimension(lam) - 1 / _qfact(n, qi)


def _mu(lam, qi):
    s = mp.mpf(0)
    for i, li in enumerate(lam):
        for j in range(li):
            c = j - i
            s += qi(c) * qi(c + 1)
    return s


def main() -> int:
    set_compute_dps()
    print("=" * 74)
    print("  float64 excised from the UIC resolvent cone -- and what is left")
    print("=" * 74)
    print(f"  mp.dps = {mp.dps}   q0 = {QP.Q_50_DIGIT_STR[:24]}...  (proton pin)")
    print("  convention D (z = q^3/(q^2+1)) -- the Markov parameter is not on")
    print("  this path; recorded because every binding number in this repo is.")
    print()

    # ── 1. TYPE ────────────────────────────────────────────────────────
    print("  1. type")
    typed = {
        "S_REEB_PLANCK (s_*)": H.S_REEB_PLANCK,
        "q_laplacian_eigenvalue (mu)": H.q_laplacian_eigenvalue((2, 2)),
        "q_resolvent_weight (rho)": H.q_resolvent_weight((2, 2)),
        "partition_character_sigma1": H.partition_character_sigma1((2, 1)),
        "partition_spectral_log_rate": H.partition_spectral_log_rate((2, 1)),
    }
    for nm, v in typed.items():
        check(f"{nm} is mpf", isinstance(v, mp.mpf), type(v).__name__)

    tbl = {tuple(e["partition"]): e for e in H._partition_table()}
    cols = ("C_lambda_resolvent_MeV", "resolvent_weight_planck",
            "q_laplacian_eigenvalue", "chi_sigma1", "spectral_log_rate")
    bad_cols = [(lam, c) for lam in LAMBDAS for c in cols
                if not isinstance(tbl[lam][c], mp.mpf)]
    check("every derived _PARTITION_TABLE column is mpf on every weighted block",
          not bad_cols, f"{len(LAMBDAS)} blocks x {len(cols)} columns")

    # ── 2. SOURCE ──────────────────────────────────────────────────────
    print()
    print("  2. source (AST over each function's own body)")
    offenders = {fn: float64_calls_in(fn) for fn in CONE}
    offenders = {k: v for k, v in offenders.items() if v}
    check("no math.log / math.exp / math.sqrt / float() / q_int in the cone",
          not offenders, str(offenders) if offenders else f"{len(CONE)} functions")

    # ── 3. VALUE: s_* is a different number, not a re-typed one ────────
    print()
    print("  3. value")
    s_f64 = (QP.Q - 1.0) / QP.Q          # exactly what the tree held before
    gap = abs(mp.mpf(s_f64) - H.S_REEB_PLANCK) / H.S_REEB_PLANCK
    print(f"     s_* float64 {s_f64!r}")
    print(f"     s_* mpf     {mp.nstr(H.S_REEB_PLANCK, 40)}")
    print(f"     relative gap {mp.nstr(gap, 8)}   (float64 eps = "
          f"{mp.nstr(mp.mpf(2) ** -52, 6)})")
    check("s_* differs from its float64 twin at the float64 floor",
          mp.mpf("1e-17") < gap < mp.mpf("1e-15"), mp.nstr(gap, 8))

    # ── 4. STABILITY under dps 70 -> 90 ────────────────────────────────
    print()
    print("  4. stability under a working-precision increase, 70 -> 90")
    worst_stab = mp.mpf(0)
    worst_lam = None
    for lam in LAMBDAS:
        with mp.workdps(70):
            a = +H.q_resolvent_weight(lam)
        with mp.workdps(90):
            b = +H.q_resolvent_weight(lam)
        with mp.workdps(120):
            r = abs((b - a) / b)
        if r > worst_stab:
            worst_stab, worst_lam = r, lam
    print(f"     worst rho_lambda move {mp.nstr(worst_stab, 8)} at {worst_lam}")
    check("rho_lambda is stable at 70 -> 90 far past the float64 floor",
          worst_stab < mp.mpf("1e-45"), mp.nstr(worst_stab, 8))

    # The stability check above is silent about the INPUT: both runs read the
    # same `_Q_MP`.  Measure that separately against a full-precision solve.
    with mp.workdps(120):
        q_full = QP.q_at(90)
        q_ceiling = abs(QP.Q_MP - q_full) / q_full
    print(f"     _Q_MP vs q_at(90): {mp.nstr(q_ceiling, 8)}  -- the INPUT "
          f"ceiling, ~50 digits, BELOW OUTPUT_DPS = 60")
    check("the q input carries ~50 digits, so 1e-50 (not 1e-70) is the honest "
          "ceiling on anything built from it",
          mp.mpf("1e-56") < q_ceiling < mp.mpf("1e-46"), mp.nstr(q_ceiling, 8))

    # ── 5. THE RESIDUAL ────────────────────────────────────────────────
    print()
    print("  5. residual float64: q_hook_product / q_factorial / wedderburn_weight")
    print("     accumulate mp.mpf(1) * q_int(k) over the FLOAT64 q_int.")
    removed = mp.mpf(0)
    residual = mp.mpf(0)
    r_lam = None
    for lam in LAMBDAS:
        mu_mp, mu_f64 = _mu(lam, _q_int_mp), _mu(lam, QP.q_int)
        s_mp = H.S_REEB_PLANCK
        allmpf = _hq(lam, _q_int_mp) * _y(lam, _q_int_mp) / (mu_mp + s_mp) * M_E_MEV
        now = _hq(lam, QP.q_int) * _y(lam, QP.q_int) / (mu_mp + s_mp) * M_E_MEV
        was = (_hq(lam, QP.q_int) * _y(lam, QP.q_int)
               * mp.mpf(1.0 / (mu_f64 + mp.mpf(s_f64))) * M_E_MEV)
        removed = max(removed, abs((now - was) / allmpf))
        r = abs((now - allmpf) / allmpf)
        if r > residual:
            residual, r_lam = r, lam
    print(f"     this excision REMOVES at most {mp.nstr(removed, 8)} (relative)")
    print(f"     it LEAVES at most            {mp.nstr(residual, 8)} at {r_lam}")
    check("the residual is bounded (regression guard)",
          residual < mp.mpf("5e-15"), mp.nstr(residual, 8))
    check("the residual is LARGER than what this excision removes -- so the "
          "cone is not clean and the audit must not say it is",
          residual > removed, f"{mp.nstr(residual, 6)} > {mp.nstr(removed, 6)}")

    # ── witness ────────────────────────────────────────────────────────
    w = WitnessBuilder("uic-float64-excision", engine="python+mpmath")
    w.set_description(
        "Owner directive 2026-09-12 'excise float64'. mu_lambda (q-Laplacian "
        "eigenvalue) and s_* (Reeb-Planck spectral parameter) and their whole "
        "downstream cone in hecke_core_legacy now carry mpmath.mpf. Checks: "
        "type on 5 scalars + 5 table columns over 31 weighted blocks; AST over "
        "8 function bodies for math.log/exp/sqrt/float()/q_int; s_* moves "
        "1.99757e-16 off its float64 twin; rho_lambda stable at dps 70 -> 90. "
        "RESIDUAL, recorded not fixed: q_hook_product / q_factorial / "
        "wedderburn_weight are mpf-typed and float64-VALUED through q_int, "
        "leaving ~1e-15 -- larger than the ~2.5e-16 this removes. Bean "
        "qou-oiz3; follows PR #7237 / bean qou-t6be."
    )
    w.set_audit_only("docs/audits/2026-09-12-uic-float64-excision.md")
    w.add_data("precision", {
        "compute_dps": COMPUTE_DPS,
        "q0_source": "q_parameter.Q_MP (Q_50_DIGIT_STR, 50 digits)",
        "q0_ceiling_note": (
            "_Q_MP carries 50 significant digits, BELOW OUTPUT_DPS = 60. A "
            "value serialized at 60 digits from it has ~8 padded digits. "
            "Recorded as a residual, not fixed here."),
        "s_star_float64": repr(s_f64),
        "s_star_mpf": fmt(H.S_REEB_PLANCK),
        "s_star_relative_gap": fmt(gap),
    })
    w.add_data("surface", {
        "functions_ast_checked": CONE,
        "float64_calls_found": offenders,
        "weighted_blocks": len(LAMBDAS),
    })
    w.add_data("residual_float64", {
        "cause": "q_int is float64; q_hook_product/q_factorial/wedderburn_weight "
                 "accumulate mp.mpf(1) * q_int(k) over it",
        "worst_relative_removed_by_this_pr": fmt(removed),
        "worst_relative_remaining": fmt(residual),
        "worst_remaining_partition": str(r_lam),
        "root_fix_blast_radius": "124 python files, 243 witnesses -- owner call",
    })
    w.add_data("dps_stability", {
        "dps_low": 70, "dps_high": 90,
        "worst_rho_relative_move": fmt(worst_stab),
        "worst_partition": str(worst_lam),
        "note": ("this measures the ARITHMETIC reproducing itself, not the "
                 "input -- both runs read the same _Q_MP"),
        "q_input_ceiling_vs_q_at_90": fmt(q_ceiling),
    })
    for nm, ok in CHECKS:
        w.add_assertion(nm, computed="1" if ok else "0", expected="1",
                        tolerance="0", source="uic_float64_excision_probe")
    print()
    print(f"  witness: {w.save()}")
    npass = sum(1 for _n, ok in CHECKS if ok)
    print(f"  {npass}/{len(CHECKS)} checks passed")
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
