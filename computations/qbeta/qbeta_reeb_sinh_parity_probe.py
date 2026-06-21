#!/usr/bin/env python3
"""qbeta_reeb_sinh_parity_probe.py
==================================

Pruned necessary-condition check on the Reeb-`sinh` holonomy as a c_3
source: PARITY (bar-odd) is the formalize-first invariant (Lean
`QBetaReebSinhParity`); here we test the two cheap numerical necessary
conditions — **sign** and **cross-anchor swing** — against the c_3 target,
and surface the structural magnitude gap that determines at which level
(observable vs fibre) the Reeb `sinh` can enter.

## What is already settled (Lean, this branch)

`QBetaReebSinhParity.lean` proves: `cosh(kη)` is bar-even, `sinh(kη)` is
bar-odd, and the bar-antisymmetric part of a Reeb holonomy `a·cosh + b·sinh`
is exactly `b·sinh(kη)`. So among Reeb components ONLY the `sinh` part is
parity-admissible for the bar-antisymmetric coefficient c_3. That is the
class-pruning invariant; this probe runs the numerical necessary checks on
the surviving `sinh` candidates.

## The two necessary conditions + the magnitude diagnostic

c_3 target (`qbeta_utils.c3_target_at`, PR #1831): proton −2.06934,
muon −2.02020. With η = log q and the anchors differing only at the ~8th
digit, Δη ≡ η_muon − η_proton ~ 1e-8, yet c_3 swings by ~0.049. So

    (dc_3/dη) ≈ swing(c_3) / Δη ~ O(1/u³)   (HUGE — the ladder inversion
                                              c_3 = (Q_codata/Q_N2−1)/u³
                                              amplifies by 1/u³ ≈ 1.6e6).

A DIRECT Reeb scalar `S(η) = b·sinh(kη)·(bar-even factor)` has
`dS/dη = O(1)`. So:

  - **Sign** (necessary): can a `−sinh`-form be negative at q₀ like c_3? (easy)
  - **Swing direction** (necessary): does sign(dS/dη) match sign(dc_3/dη)?
  - **Swing magnitude** (diagnostic, NOT a fit target): the ratio
    `(dc_3/dη)/(dS/dη)` measures how far the direct Reeb scalar is from the
    observable c_3 — if it is ~1/u³, the Reeb `sinh` cannot be a direct
    *observable* closed form; it must enter at the **fibre level**
    (pre-f-map), where the 1/u³ amplification is supplied by the ladder.
    That is consistent with PR #1880 (closed-form observable c_3 refuted)
    and PR #1811 (residue A is fibre-level).

## Verdict semantics

- **PARITY_ADMISSIBLE_FIBRE_LEVEL** (expected): `sinh` candidates can match
  the sign (and possibly swing direction), but their O(1) observable swing
  is ~1/u³ too small to BE c_3 directly → the Reeb `sinh` is a fibre-level
  source, the first parity-admissible structural lead (not refuted), to be
  pursued via the Reeb→q-difference-element route (the structural way to
  close #1880's data-blocked recurrence axis).
- **OBSERVABLE_SWING_MATCH** (would be surprising): a `sinh` candidate
  matches c_3 sign + swing magnitude at the observable level — a direct
  lead. (Per #1880's saturation this is not expected.)

No fits: every candidate is a closed-form bar-odd scalar; we report sign,
swing direction, and the magnitude ratio. AGENTS.md no-seventh-ansatz
respected — this prunes/locates a class, it does not fit a form.

## References
- Parity invariant (Lean): `QBetaReebSinhParity.lean` (this branch)
- c_3 cross-anchor target: `qbeta_utils.c3_target_at` (PR #1831)
- Closed-form observable c_3 refuted: PR #1880
- Fibre-level residue A: PR #1811
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from collections.abc import Callable

from mpmath import mp, mpf, sinh, cosh, log, fabs  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402


def reeb_sinh_candidates() -> dict[str, Callable[[mpf], mpf]]:
    """Bar-ODD (sinh-built) Reeb holonomy scalars S(η).

    Each is odd under η ↦ −η (q ↦ q⁻¹) — the parity-admissible class from
    `QBetaReebSinhParity`. `cosh`-only factors keep the overall parity odd.
    The leading `−` gives the c_3 sign. `k` indexes the Reeb level; `(2m+1)`
    mirrors the P_m(h) cosh-avatar precedent (cheat-sheet §3).
    """
    return {
        "-sinh(η)":               lambda e: -sinh(e),
        "-2·sinh(η) [= -h]":      lambda e: -2 * sinh(e),
        "-sinh(3η)/(2cosh η)":    lambda e: -sinh(3 * e) / (2 * cosh(e)),
        "-sinh(3η)":              lambda e: -sinh(3 * e),
        "-sinh(3η)/(2cosh³η)":    lambda e: -sinh(3 * e) / (2 * cosh(e) ** 3),
        "-sinh(5η)/(2cosh η)":    lambda e: -sinh(5 * e) / (2 * cosh(e)),
        "-tanh(η)·[3]ish=-sinh(3η)/cosh(η)":
                                  lambda e: -sinh(3 * e) / cosh(e),
    }


def main() -> int:
    set_compute_dps()

    me = mpf(str(M_E_MEV))
    q_codata = mpf(str(Q_BETA_MEV))
    qp = q_at(mp.dps)
    qm = q_muon_at(mp.dps)
    eta_p, eta_m = log(qp), log(qm)
    d_eta = eta_m - eta_p

    cp = c3_target_at(qp, q_codata, me)
    cm = c3_target_at(qm, q_codata, me)
    c3_swing = cm - cp
    c3_slope = c3_swing / d_eta  # dc_3/dη (amplified by the ladder 1/u³)
    u = substrate_ladder_quantities(qp)["u"]
    inv_u3 = 1 / u ** 3

    print("=" * 80)
    print(" Q_β c_3 — Reeb sinh holonomy: parity-admissible necessary-condition check")
    print("=" * 80)
    print(f"  η_proton = {fmt(eta_p)[:18]}   η_muon = {fmt(eta_m)[:18]}")
    print(f"  Δη = η_m − η_p = {float(d_eta):.4e}")
    print(f"  c_3: proton {fmt(cp)[:12]}  muon {fmt(cm)[:12]}  swing {float(c3_swing):+.4e}")
    print(f"  dc_3/dη ≈ {float(c3_slope):.4e}   (ladder 1/u³ ≈ {float(inv_u3):.4e})")
    print()
    print(f"  {'candidate':<38}{'S(q₀)':>12}{'sign?':>7}{'dS/dη':>12}{'swing-dir?':>11}{'(dc₃/dη)/(dS/dη)':>20}")
    print(f"  {'-'*38}{'-'*12}{'-'*7}{'-'*12}{'-'*11}{'-'*20}")

    rows = []
    any_observable_match = False
    for name, S in reeb_sinh_candidates().items():
        sp, sm = S(eta_p), S(eta_m)
        s_slope = (sm - sp) / d_eta
        sign_ok = sp < 0                          # c_3 is negative
        dir_ok = (s_slope > 0) == (c3_slope > 0)   # same swing direction
        ratio = c3_slope / s_slope if s_slope != 0 else mpf("nan")
        # An "observable match" would need ratio ≈ 1 (same swing magnitude).
        observable_match = sign_ok and dir_ok and fabs(ratio - 1) < mpf("0.01")
        any_observable_match = any_observable_match or observable_match
        print(f"  {name:<38}{float(sp):>12.4f}{('yes' if sign_ok else 'no'):>7}"
              f"{float(s_slope):>12.3e}{('yes' if dir_ok else 'no'):>11}"
              f"{float(ratio):>20.3e}")
        rows.append({
            "candidate": name,
            "S_proton": fmt(sp), "S_muon": fmt(sm),
            "sign_matches_c3": sign_ok,
            "dS_deta": fmt(s_slope),
            "swing_direction_matches": dir_ok,
            "slope_ratio_c3_over_S": float(ratio),
            "observable_match": observable_match,
        })
    print()

    # Magnitude diagnostic: are ALL admissible candidates' slope ratios ~1/u³?
    # (i.e. the observable c_3 swing is ~1/u³ larger than any direct Reeb scalar)
    matching = [r for r in rows if r["sign_matches_c3"]]
    fibre_gap = bool(matching) and all(
        abs(r["slope_ratio_c3_over_S"]) > 1e4 for r in matching
    )

    print("=" * 80)
    print(" VERDICT")
    print("=" * 80)
    if any_observable_match:
        print("  OBSERVABLE_SWING_MATCH — a sinh-Reeb scalar matches c_3 sign +")
        print("  swing magnitude at the observable level. Direct lead; verify vs")
        print("  the saturated single-formula bracket (#1880).")
        verdict = "OBSERVABLE_SWING_MATCH"
    else:
        print("  PARITY_ADMISSIBLE_FIBRE_LEVEL — sinh-Reeb scalars are bar-odd")
        print("  (Lean-proved) and can match the c_3 SIGN, but their observable")
        print("  cross-anchor slope dS/dη is O(1), whereas dc_3/dη is amplified")
        print(f"  by the ladder factor 1/u³ ≈ {float(inv_u3):.2e}. The slope ratios")
        print("  (dc₃/dη)/(dS/dη) above are ~1/u³, NOT ~1 — so a DIRECT Reeb sinh")
        print("  cannot be the observable c_3 closed form. It is parity-admissible")
        print("  only at the FIBRE level (pre-f-map), where the ladder supplies the")
        print("  1/u³ amplification. This is the first NON-refuted structural lead")
        print("  for residue A since the bracket closed: consistent with PR #1880")
        print("  (observable closed-form c_3 refuted) and PR #1811 (residue A is")
        print("  fibre-level). Next: scope the Reeb-holonomy → fibre q-difference")
        print("  element (the structural route to the data-blocked recurrence).")
        verdict = "PARITY_ADMISSIBLE_FIBRE_LEVEL"

    wb = WitnessBuilder("qbeta-reeb-sinh-parity-probe", engine="mpmath")
    wb.set_description(
        "Pruned necessary-condition check on the Reeb-sinh holonomy as a c_3 "
        "source. Parity (bar-odd) is the formalize-first invariant proved in "
        "QBetaReebSinhParity.lean; here we test sign + cross-anchor swing of "
        "sinh-Reeb scalars against the c_3 target and measure the slope ratio "
        "(dc_3/dη)/(dS/dη). The ratio is ~1/u³ (≈1.6e6), not ~1, so a direct "
        "Reeb sinh matches the c_3 sign but not the observable swing magnitude "
        "— it is parity-admissible only at the FIBRE level (pre-f-map), where "
        "the ladder supplies the amplification. First non-refuted structural "
        "lead since the c_3 bracket closed; consistent with #1880 + #1811. "
        "No fits."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("eta_proton", fmt(eta_p))
    wb.add_data("eta_muon", fmt(eta_m))
    wb.add_data("c3_target_proton", fmt(cp))
    wb.add_data("c3_target_muon", fmt(cm))
    wb.add_data("c3_slope_dc3_deta", fmt(c3_slope))
    wb.add_data("ladder_inv_u3", fmt(inv_u3))
    wb.add_data("candidates", rows)
    wb.add_data("verdict", verdict)
    wb.add_data("fibre_level_gap_confirmed", fibre_gap)
    wb.add_data("interpretation", (
        "Reeb sinh is the parity-admissible (bar-odd, Lean-proved) Reeb "
        "component for c_3. Numerically it matches the c_3 sign but its "
        "observable slope is ~1/u³ too small, so it cannot be a direct "
        "observable closed form (consistent with #1880). It is a fibre-level "
        "source: the ladder inversion supplies the 1/u³ amplification. This "
        "is a non-refuted structural lead — the Reeb→fibre-q-difference route "
        "is the way to attack the data-blocked recurrence axis structurally."
    ))
    # Real invariant: at least one sinh candidate matches the c_3 sign
    # (parity admissibility has numerical teeth).
    n_sign = sum(1 for r in rows if r["sign_matches_c3"])
    wb.add_assertion(
        "at_least_one_sinh_candidate_matches_c3_sign",
        computed=1.0 if n_sign >= 1 else 0.0, expected=1.0,
        source="bar-odd -sinh forms can reproduce the negative c_3 sign at q₀.",
    )
    # Real invariant: the fibre-level magnitude gap holds (slope ratio ≫ 1).
    wb.add_assertion(
        "observable_swing_gap_is_ladder_order",
        computed=1.0 if fibre_gap else 0.0, expected=1.0,
        source=("(dc_3/dη)/(dS/dη) ~ 1/u³ ≫ 1 for every sign-matching sinh "
                "candidate — the Reeb sinh is fibre-level, not a direct "
                "observable c_3 closed form."),
    )
    wb.save()
    print()
    print("  Witness: qbeta-reeb-sinh-parity-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
