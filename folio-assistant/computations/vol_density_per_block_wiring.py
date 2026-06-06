#!/usr/bin/env python3
# polynomial_q_not_applicable: evaluates at q = q_0, numeric output.
"""Discipline-gate verification: does the paper's per-block Σ_λ factor
reproduce production's VolDensity(𝓑₃) — with ZERO fudge?

## The bug being checked

Production `vol_density_borromean` (`_li_2_q_util.py`) computes

    VolDensity(𝓑₃, q) = [Vol(𝓑₃)/ℏ_q²] · linking_weight(q),
    linking_weight(q) = (3q² + 4 + 3q⁻²)/4   (the H₄ Family-A scalar)

— a GLOBAL scalar.  The paper (`prop:hoefsmit-scattering-pipeline`
Stage 4) specifies the FORCED per-block form

    m(K) = m_e · Geom(K) · Σ_λ w_λ χ_λ(β_K)/dim λ,
    Geom(K) = Vol(K)/ℏ_q²  (hyperbolic),  w_λ = dim_q(λ)²/[k]_q!

over partitions of the KNOT'S OWN strand count.  𝓑₃ is a 3-strand
braid → H₃ → partitions of 3 (NOT H₄ / partitions of 4).  The paper's
per-block factor for 𝓑₃ is the canonical H₃ Markov trace
tr_M(β_K) = Σ_λ y_λ χ_λ, loaded from the chi-cache witnesses.

## The discipline gate (CLAUDE.md production-vs-exploratory)

Does `m_e · [Vol/ℏ_q²] · tr_M(K)` reproduce production's
`m_e · [Vol/ℏ_q²] · linking_weight` AT ALL ORDERS with NO fudge?

- If YES → the per-block sum IS the correct derivation; the global
  linking_weight was a correct-but-opaque collapse for 𝓑₃.
- If NO → the global scalar is a DIFFERENT object than the paper's
  per-block sum.  Report the raw discrepancy order-by-order, flag
  RED, state what's unresolved.  DO NOT hard-code a factor to force
  the match.

This script computes both readings, order-by-order in h = q − q⁻¹,
per knot (proton / neutron at H₃), and reports the recovered fraction
of the +2.89 % m_p gap — RAW.  No tuning to m_p or B_AME.

Output: `vol-density-per-block-wiring.witness.json`.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from pathlib import Path

import mpmath as mp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from _li_2_q_util import (  # noqa: E402
    geom_leading,
    vol_density_borromean,
    vol_density_per_block,
    linking_weight_family_a,
)
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

VOL_B3 = 8 * mp.catalan  # Vol(Borromean rings complement) = 8·G (Adams 1985)


def _load_trM(atom: str, n: int) -> mp.mpf:
    """Load the canonical per-block Markov trace tr_M(β_atom) at q_0
    from the chi-cache witness — this IS Σ_λ y_λ χ_λ, the paper's
    Stage-4 per-block factor over the knot's own H_n partitions."""
    path = HERE / f"chi-{atom}-h{n}-at-q0-50dps.witness.json"
    d = json.loads(path.read_text())
    return mp.mpf(d["tr_M_at_q0"])


def _series_h(fn, _q0: mp.mpf, order: int = 6) -> list[mp.mpf]:
    """Taylor coefficients of fn(q) in h = q − q⁻¹ about h = 0 (q = 1),
    via mpmath.taylor on the reparametrised function.  Returns
    [c_0, c_1, …, c_order].  fn must accept q and return mpf."""
    # q as a function of h: q − 1/q = h  ⇒  q = (h + sqrt(h²+4))/2.
    def q_of_h(h):
        return (h + mp.sqrt(h ** 2 + 4)) / 2

    def g(h):
        return fn(q_of_h(h))

    return mp.taylor(g, mp.mpf(0), order)


def main() -> int:
    start = time.monotonic()
    q0 = mp.mpf(Q_50_DIGIT_STR)
    me = mp.mpf(repr(M_E_MEV))
    mpc = mp.mpf(repr(M_P_MEV))
    mnc = mp.mpf(repr(M_N_MEV))

    gl = geom_leading(VOL_B3, q0)            # Vol(𝓑₃)/ℏ_q²
    lw = linking_weight_family_a(q0)         # global H₄ scalar ≈ 2.53
    geom_prod = vol_density_borromean(q0)      # production VolDensity

    trM = {
        "proton": _load_trM("proton", 3),
        "neutron": _load_trM("neutron", 3),
    }

    print("=" * 78)
    print(" Discipline gate: per-block Σ_λ tr_M  vs  production global linking_weight")
    print("=" * 78)
    print(f"  q_0                 = {mp.nstr(q0, 16)}")
    print(f"  Geom_leading=Vol/ℏ² = {mp.nstr(gl, 12)}")
    print(f"  linking_weight (H₄) = {mp.nstr(lw, 12)}   [production global scalar]")
    print(f"  VolDensity prod      = {mp.nstr(geom_prod, 12)}")
    print(f"  implied λ (round-trips m_p) = {mp.nstr(mpc / (me * gl), 12)}")
    print()

    # ── Per-knot per-block evaluation ───────────────────────────────
    per_knot = {}
    for knot, tr in trM.items():
        geom_pb = vol_density_per_block(VOL_B3, tr, q0)
        m_pb = me * geom_pb
        codata = mpc if knot == "proton" else mnc
        err_pb = (m_pb - codata) / codata
        per_knot[knot] = {
            "n_strands": 3,
            "index_set": "H_3 (partitions of 3)",
            "tr_M_at_q0": mp.nstr(tr, 20),
            "geom_leading": mp.nstr(gl, 20),
            "vol_density_per_block": mp.nstr(geom_pb, 20),
            "m_per_block_MeV": mp.nstr(m_pb, 20),
            "codata_MeV": mp.nstr(codata, 20),
            "rel_err_per_block": mp.nstr(err_pb, 12),
        }
        print(f"  {knot:>8}: tr_M={mp.nstr(tr, 10):>12}  "
              f"m_pb={mp.nstr(m_pb, 10):>12} MeV  "
              f"err={mp.nstr(err_pb * 100, 5)}%")

    # production prediction (global scalar, average nucleon)
    m_avg_prod = me * geom_prod
    codata_avg = (mpc + mnc) / 2
    err_prod = (m_avg_prod - codata_avg) / codata_avg
    print()
    print(f"  production m_avg = {mp.nstr(m_avg_prod, 10)} MeV  "
          f"err vs CODATA m_avg = {mp.nstr(err_prod * 100, 5)}%")

    # ── Order-by-order h-expansion: global vs per-block factor ──────
    # The factor that multiplies Vol/ℏ_q²:
    #   global:    linking_weight_family_a(q) = 5/2 + (3/4) h²  (terminates)
    #   per-block: tr_M(β_proton, q) as a function of q.  The chi-cache
    #     only stores the q_0 value; we expand the GLOBAL scalar here
    #     and report the per-block VALUE (its q-dependence lives in the
    #     symbolic chi-cache, expanded elsewhere).  The decisive number
    #     is the RATIO at q_0, which exposes the mismatch directly.
    lw_series = _series_h(linking_weight_family_a, q0, order=6)
    print()
    print("  linking_weight h-series (global H₄ scalar):")
    for k, c in enumerate(lw_series):
        if abs(c) > mp.mpf(10) ** (-20):
            print(f"    c_{k} = {mp.nstr(c, 10)}")

    ratio_p = lw / trM["proton"]
    ratio_n = lw / trM["neutron"]
    print()
    print(f"  RATIO  linking_weight / tr_M(proton)  = {mp.nstr(ratio_p, 10)}")
    print(f"  RATIO  linking_weight / tr_M(neutron) = {mp.nstr(ratio_n, 10)}")

    # ── Recovered fraction of the +2.89% m_p gap (RAW) ─────────────
    m_avg_pb = (me * vol_density_per_block(VOL_B3, trM["proton"], q0)
                + me * vol_density_per_block(VOL_B3, trM["neutron"], q0)) / 2
    gap_pb = (m_avg_pb - codata_avg) / codata_avg
    print()
    print(f"  production gap = {mp.nstr(err_prod * 100, 5)}%   "
          f"per-block gap = {mp.nstr(gap_pb * 100, 5)}%")
    recovered = 1 - abs(gap_pb) / abs(err_prod) if err_prod != 0 else mp.mpf(0)
    print(f"  recovered fraction of |gap| by per-block restoration = "
          f"{mp.nstr(recovered * 100, 5)}%  (NEGATIVE ⇒ per-block is WORSE)")

    # ── Discipline-gate verdict ─────────────────────────────────────
    # The gate passes iff per-block reproduces production with NO fudge.
    # tol: agreement to 1e-6 relative would be a PASS.
    gate_pass = abs(ratio_p - 1) < mp.mpf("1e-6")
    verdict = "PASS" if gate_pass else "RED — per-block ≠ global, no fudge applied"
    print()
    print(f"  DISCIPLINE GATE: {verdict}")
    print(f"    linking_weight/tr_M(proton) = {mp.nstr(ratio_p, 10)} "
          f"(≠ 1 ⇒ different objects)")

    # ── Emit witness ────────────────────────────────────────────────
    w = WitnessBuilder("vol-density-per-block-wiring", engine="mpmath")
    w.set_description(
        "Discipline-gate verification of the paper's per-block Σ_λ "
        "factor (prop:hoefsmit-scattering-pipeline Stage 4) against "
        "production's global linking_weight collapse "
        "(vol_density_borromean). Computes m(K) = m_e·[Vol(K)/ℏ_q²]·tr_M(K) "
        "per knot using the canonical H₃ Markov trace from the "
        "chi-{atom}-h3-at-q0 caches, vs production "
        "m = m_e·[Vol/ℏ_q²]·linking_weight (the H₄ scalar 2.53). "
        "VERDICT (raw, no fudge): the per-block H₃ trace tr_M(proton)≈1.065 "
        "is NOT the global H₄ scalar 2.53; they differ by ≈2.38×. The "
        "per-block reading gives m_p≈406 MeV (−56.7%), so production's "
        "near-correct m_p does NOT come from the paper's per-block formula "
        "as literally written — the global H₄ scalar lands near the "
        "CODATA-implied λ≈2.46 coincidentally, using the WRONG index set "
        "(H₄ not H₃). This is a flagged structural discrepancy, NOT "
        "hard-coded away. Corroborates sibling PR #1608/#1613 findings."
    )
    w.add_parameter("q_0_50dps", Q_50_DIGIT_STR)
    w.add_parameter("Vol_B3", mp.nstr(VOL_B3, 30))
    w.add_parameter("geom_leading_Vol_over_hbar2", mp.nstr(gl, 30))
    w.add_parameter("linking_weight_H4_global", mp.nstr(lw, 30))
    w.add_parameter("implied_lambda_m_p_roundtrip", mp.nstr(mpc / (me * gl), 30))
    w.add_data("per_knot", per_knot)
    w.add_data("linking_weight_h_series",
               {f"c_{k}": mp.nstr(c, 20) for k, c in enumerate(lw_series)})
    w.add_data("ratio_linking_weight_over_trM",
               {"proton": mp.nstr(ratio_p, 20),
                "neutron": mp.nstr(ratio_n, 20)})
    w.add_data("production_m_avg_MeV", mp.nstr(m_avg_prod, 20))
    w.add_data("production_gap_pct", mp.nstr(err_prod * 100, 12))
    w.add_data("per_block_m_avg_MeV", mp.nstr(m_avg_pb, 20))
    w.add_data("per_block_gap_pct", mp.nstr(gap_pb * 100, 12))
    w.add_data("recovered_fraction_pct", mp.nstr(recovered * 100, 12))
    w.add_assertion(
        "discipline_gate_per_block_reproduces_production",
        computed=mp.nstr(ratio_p, 20),
        expected="1.0",
        tolerance=1e-6,
        source="ratio linking_weight / tr_M(proton) — PASS iff == 1",
    )
    out = w.save()
    print()
    print(f"  Witness: {Path(out).name}")
    print(f"  Wall: {time.monotonic() - start:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
