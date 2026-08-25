#!/usr/bin/env python3
"""he4_sdp_compositional_probe.py — ⁴He compositional-channel
operator-selection LP for prop:he4-channel-active-set.

Recreated 2026-07-02: the original producer
(computations/probe_he4_sdp_compositional.py) was lost in a refactor
while the block kept declaring
computations/he4-sdp-compositional-probe.witness.json. This probe
regenerates that witness from the block's .md specification
(content/quantum-observable-universe/mass-theory/he4-channel-active-set.md).

SETUP. The ⁴He = (Z=2, N=2) bound state admits three primary
compositional channels (each summing to A = 4 nucleons):

    index 0:  D ⊕ D      (1,1) + (1,1)
    index 1:  T ⊕ p      (1,2) + (1,0)
    index 2:  ³He ⊕ n    (2,1) + (0,1)

The channel binding residual is

    t_i := Δ_cat(⁴He) − Σ_{j ∈ channel i} Δ_cat(j)

— the binding that the magic-shell coupling must explain beyond the
free-constituent sum. The Δ_cat anchors are LOADED (not hardcoded)
from the empirical-instantiation witness
magic-shell-empirical-instantiation.witness.json (currently under
computations/_deprecated/ — see caveat), so t is COMPUTED from the
anchors. Expected per the .md table (2-decimal rounding):
t ≈ (24.16, 20.38, 21.18) MeV.

LP (prop:operator-selection-lp canonical form, routed through the
repo-mandated entry point lp_dual_solver.solve_operator_selection_lp):

    min t·x   s.t.  Σx = n_target,  G x ≥ 0,   with G = I₃
    n_target = Δ_coupling(2,2) = Δ_cat(⁴He) − 2·Δ_cat(³He) ≈ 13.197 MeV

EXPECTED SOLUTION (the proposition's three claims):
    1. unique primal optimum on T⊕p:  x* = (0, 13.197, 0)
    2. active set = {D⊕D, ³He⊕n}  (indices {0, 2})
    3. dual ordering  y*_{D⊕D} > y*_{³He⊕n} > y*_{T⊕p} = 0,
       with y* ≈ (3.778, 0, 0.796), y0* ≈ 20.380,
       primal_obj = dual_obj ≈ 268.949, duality_gap ≈ 0.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1 catch-up, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
for _p in (str(COMP), str(COMP / "substrate"),
           str(COMP.parent / "tools" / "pyhecke" / "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402

# Channel table: (name, constituent keys in the anchor witness).
CHANNELS = [
    ("D+D",    ["deuteron", "deuteron"]),
    ("T+p",    ["tritium", "proton"]),
    ("3He+n",  ["he3", "neutron"]),
]
IDX_DD, IDX_TP, IDX_3HEN = 0, 1, 2

# .md table values (3-decimal / 2-decimal rounding) — matched to ~1e-2.
MD_T = (24.16, 20.38, 21.18)
MD_N_TARGET = 13.197
MD_X_TP = 13.197
MD_Y0 = 20.380
MD_Y = (3.778, 0.0, 0.796)
MD_OBJ = 268.949
MD_TOL = 1e-2


def _anchor_witness_path() -> Path:
    """Resolve magic-shell-empirical-instantiation.witness.json.

    The .md cites it at computations/ but it currently lives under
    computations/_deprecated/ (which _path_bridge.witness_path skips
    by convention) — check both explicitly."""
    for cand in (
        COMP / "magic-shell-empirical-instantiation.witness.json",
        COMP / "_deprecated" / "magic-shell-empirical-instantiation.witness.json",
    ):
        if cand.exists():
            return cand
    raise FileNotFoundError(
        "magic-shell-empirical-instantiation.witness.json not found in "
        "computations/ or computations/_deprecated/"
    )


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    # Witness name + output_dir are FORCED to reproduce the path the
    # content block declares: computations/he4-sdp-compositional-probe
    # .witness.json (top-level computations/, not probes/ — the
    # WitnessBuilder default would drop it next to this script).
    builder = WitnessBuilder(
        "he4-sdp-compositional-probe",
        engine="scipy",
        output_dir=COMP,
        start_time=t0,
    )
    builder.set_description(
        "⁴He compositional-channel operator-selection LP "
        "(prop:he4-channel-active-set). Channels D⊕D / T⊕p / ³He⊕n with "
        "residuals t_i = Δ_cat(⁴He) − ΣΔ_cat(constituents) from the "
        "magic-shell empirical anchors; G = I₃, n_target = Δ_coupling(2,2) "
        "= Δ_cat(⁴He) − 2·Δ_cat(³He). Solved via the canonical "
        "lp_dual_solver.solve_operator_selection_lp; verifies the unique "
        "T⊕p primal optimum, the {D⊕D, ³He⊕n} active set, and the dual "
        "ordering y*_{D⊕D} > y*_{³He⊕n} > y*_{T⊕p} = 0."
    )
    builder.set_content_block("prop:he4-channel-active-set")

    # ── Anchors: Δ_cat per constituent (50-dps strings → mpmath) ──────
    anchor_path = _anchor_witness_path()
    anchors = builder.add_upstream(anchor_path)
    per_atom = anchors["data"]["per_atom_delta_cat"]
    delta_cat = {
        k: mp.mpf(v["delta_cat_MeV_50dps"]) for k, v in per_atom.items()
    }
    if "_deprecated" in str(anchor_path):
        builder.add_caveat(
            "Δ_cat anchors loaded from computations/_deprecated/"
            "magic-shell-empirical-instantiation.witness.json — the anchor "
            "witness was moved to _deprecated/ after the .md was written "
            "(the .md still cites the top-level path). Values are the "
            "PR #638-closure empirical instantiation table the block was "
            "authored against."
        )

    d_he4 = delta_cat["he4"]
    d_he3 = delta_cat["he3"]

    # ── Residuals t_i and target ──────────────────────────────────────
    t_mp = [d_he4 - sum(delta_cat[c] for c in consts)
            for _, consts in CHANNELS]
    n_target_mp = d_he4 - 2 * d_he3      # Δ_coupling(2,2)

    t = np.array([float(x) for x in t_mp], dtype=float)
    G = np.eye(3)                        # channels orthogonal at leading order
    n_target = float(n_target_mp)

    print("=" * 78)
    print(" ⁴He compositional-channel operator-selection LP "
          "(prop:he4-channel-active-set)")
    print("=" * 78)
    for (name, consts), ti, md in zip(CHANNELS, t, MD_T):
        print(f"  t[{name:<6}] = {ti:12.6f} MeV   "
              f"(constituent sum {float(d_he4) - ti:8.4f};  .md: {md})")
    print(f"  n_target    = {n_target:12.6f} MeV   (.md: {MD_N_TARGET})")
    print()

    # Pin clarabel-MPFR (50 dps). This was `backend="scipy"`, pinned for
    # byte-determinism. Measured 2026-08-23: clarabel-MPFR is byte-deterministic
    # too (6 identical solves, 1 output hash), so that reason never distinguished
    # the two. The real concern was `backend="auto"` choosing silently by whether
    # the Rust binary happened to be built; pinning `clarabel` answers it, and
    # QOU_REQUIRE_CLARABEL=1 makes a missing binary an error rather than a
    # changed answer. Bean `qou/ftuv`.
    res = solve_operator_selection_lp(t, G, n_target, backend="clarabel")
    rd = res.to_dict()

    print(f"  x*          = {[f'{x:.6f}' for x in res.x_star]}")
    print(f"  y0*         = {res.y0_star:.6f}   (.md: {MD_Y0})")
    print(f"  y*          = {[f'{y:.6f}' for y in res.y_star]}   (.md: {MD_Y})")
    print(f"  active_set  = {res.active_set}   (.md: {{D⊕D, ³He⊕n}} = [0, 2])")
    print(f"  primal_obj  = {res.primal_obj:.6f}   (.md: {MD_OBJ})")
    print(f"  dual_obj    = {res.dual_obj:.6f}")
    print(f"  duality_gap = {res.duality_gap:.3e}")
    print()

    # ── Hard assertions: the proposition's three claims ───────────────
    assert res.feasible, "LP infeasible"

    # Claim 1 — unique primal optimum on T⊕p. (Uniqueness holds because
    # the channel costs t_i are pairwise distinct and t_{T⊕p} is the
    # strict minimum, so the vertex (0, n_target, 0) is the unique
    # minimiser of the transportation-form LP.)
    assert t[IDX_TP] < t[IDX_DD] and t[IDX_TP] < t[IDX_3HEN], (
        f"T⊕p is not the strict-min cost channel: t = {t.tolist()}"
    )
    assert res.x_star[IDX_TP] > 0, f"x*_Tp = {res.x_star[IDX_TP]} not > 0"
    assert abs(res.x_star[IDX_TP] - n_target) < 1e-8, (
        f"x*_Tp = {res.x_star[IDX_TP]} != n_target = {n_target}"
    )
    assert abs(res.x_star[IDX_DD]) < 1e-9 and abs(res.x_star[IDX_3HEN]) < 1e-9, (
        f"non-T⊕p primal weights not zero: x* = {res.x_star}"
    )

    # Claim 2 — active set = {D⊕D, ³He⊕n} = indices {0, 2}.
    assert sorted(res.active_set) == [IDX_DD, IDX_3HEN], (
        f"active_set = {res.active_set}, expected [0, 2]"
    )

    # Claim 3 — dual ordering y*_DD > y*_3Hen > y*_Tp = 0.
    y = res.y_star
    assert y[IDX_DD] > y[IDX_3HEN] > y[IDX_TP], (
        f"dual ordering violated: y* = {y}"
    )
    assert abs(y[IDX_TP]) < 1e-9, f"y*_Tp = {y[IDX_TP]} not = 0"

    # Strong duality.
    assert res.duality_gap < 1e-8, f"duality gap = {res.duality_gap}"

    # Numeric match vs the .md table (rounded to 2–3 decimals there).
    for i, (name, _) in enumerate(CHANNELS):
        assert abs(t[i] - MD_T[i]) < MD_TOL, (
            f"t[{name}] = {t[i]} vs .md {MD_T[i]}"
        )
    assert abs(n_target - MD_N_TARGET) < MD_TOL
    assert abs(res.y0_star - MD_Y0) < MD_TOL
    for i in range(3):
        assert abs(y[i] - MD_Y[i]) < MD_TOL, f"y*[{i}] = {y[i]} vs {MD_Y[i]}"
    assert abs(res.primal_obj - MD_OBJ) < MD_TOL

    print("  ✓ all three proposition claims verified; .md numbers "
          f"reproduced within {MD_TOL}")
    print()

    # ── Witness ────────────────────────────────────────────────────────
    builder.add_parameter("channels", [name for name, _ in CHANNELS])
    builder.add_parameter("channel_constituents",
                          {name: consts for name, consts in CHANNELS})
    builder.add_parameter("G", "I_3 (identity Gram — channels orthogonal "
                               "at leading order)")
    builder.add_parameter("n_target_MeV", n_target)
    # REPORTED, not asserted — the literal used to say "scipy linprog (HiGHS,
    # f64)" and stayed put when the solve moved to clarabel-MPFR (2026-08-23),
    # so the witness declared a backend it had not used. Bean `qou/ftuv`.
    builder.add_parameter("lp_backend", f"{res.backend} @ {res.precision_bits} bits")

    builder.add_data("delta_cat_MeV",
                     {k: float(v) for k, v in delta_cat.items()})
    builder.add_data("t_residuals_MeV",
                     {name: float(t[i]) for i, (name, _) in enumerate(CHANNELS)})
    # Full LP-dual field set per AGENTS.md §LP/SDP duals — first-class
    # infra: x_star, y0_star, y_star, active_set, primal_obj, dual_obj,
    # duality_gap, feasible (also mirrored top-level via save(extra=…)).
    builder.add_data("lp_dual", rd)
    builder.add_data("active_set_channels",
                     [CHANNELS[i][0] for i in res.active_set])

    builder.add_assertion(
        name="unique_primal_optimum_on_Tp",
        computed=float(res.x_star[IDX_TP]),
        expected=n_target,
        tolerance=1e-8,
        unit="MeV",
        source="claim 1: x*_{T⊕p} = n_target, all other x*_i = 0 "
               "(strict-min cost channel ⇒ unique vertex optimum)",
    )
    builder.add_assertion(
        name="off_Tp_primal_weights_zero",
        computed=float(abs(res.x_star[IDX_DD]) + abs(res.x_star[IDX_3HEN])),
        expected=0.0,
        tolerance=1e-9,
        source="claim 1 (complement): x*_{D⊕D} = x*_{³He⊕n} = 0",
    )
    builder.add_assertion(
        name="active_set_is_DD_and_3Hen",
        computed=str(sorted(res.active_set)),
        expected=str([IDX_DD, IDX_3HEN]),
        source="claim 2: 𝒜(⁴He) = {D⊕D, ³He⊕n} (dual-tight constraints)",
    )
    builder.add_assertion(
        name="dual_ordering_yDD_gt_y3Hen_gt_yTp_eq_0",
        computed=int(y[IDX_DD] > y[IDX_3HEN] > y[IDX_TP]
                     and abs(y[IDX_TP]) < 1e-9),
        expected=1,
        source="claim 3: y*_{D⊕D} > y*_{³He⊕n} > y*_{T⊕p} = 0",
    )
    builder.add_assertion(
        name="strong_duality_gap_zero",
        computed=float(res.duality_gap),
        expected=0.0,
        tolerance=1e-8,
        source="primal_obj = dual_obj (strong LP duality)",
    )
    builder.add_assertion(
        name="primal_obj_matches_md",
        computed=float(res.primal_obj),
        expected=MD_OBJ,
        tolerance=MD_TOL,
        unit="MeV",
        source="he4-channel-active-set.md §Solution (268.949, 3-decimal)",
    )
    builder.add_assertion(
        name="y0_star_matches_md",
        computed=float(res.y0_star),
        expected=MD_Y0,
        tolerance=MD_TOL,
        unit="MeV",
        source="he4-channel-active-set.md §Solution (y0* = 20.380)",
    )

    out = builder.save(extra=rd)
    print(f"✓ Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
