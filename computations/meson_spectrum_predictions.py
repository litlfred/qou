#!/usr/bin/env python3
"""
Meson spectrum predictions from CAL-3 + derived character ratios.

Given m_π (CAL-3) and q₀, predict the full pseudoscalar meson
spectrum using the DERIVED per-partition character ratios under
additional σ₁ crossings.

For n extra σ₁ crossings (pion → kaon: n=2, pion → η: n=4):
  (3):     χ scales by q^n
  (1,1,1): χ scales by q^{-n}
  (2,1):   χ transforms via the 2×2 Hoefsmit matrix

The mass ratio m(meson_n)/m_π = tr_M(n extra) / tr_M(pion)
× (normalization factor, cancels in ratio if same topology).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import (  # noqa: E402 — canonical PDG registry
    M_PI_PM_MEV_VALIDATION,
    M_K_PM_MEV_VALIDATION,
)
from hecke_characters import build_seminormal_matrices, partitions_of  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402


def meson_braid_word(n_extra):
    """Meson braid with n_extra additional σ₁ crossings beyond pion."""
    base = [(1,0,0),(1,0,1),(1,0,0),(1,0,1),(1,0,1),(1,0,0)]
    return base + [(1,0,1)] * n_extra


def _mp_trace(M):
    """Trace of an mpmath matrix as an mpf (no float64 round-trip)."""
    return mp.fsum(M[i, i] for i in range(M.rows))


def _chi_block(word, q_mpf, shape):
    """χ^λ(word) for one Wedderburn block, in exact mpmath arithmetic.

    Uses the mpf dispatch of `build_seminormal_matrices` (returns
    `mp.matrix`) and carries the whole product in mpmath — numpy would
    silently re-truncate an `mp.matrix` back to float64 (see
    `build_seminormal_matrices_mp`'s docstring), which is the exact trap
    this drain removes.
    """
    sigmas, dim, _ = build_seminormal_matrices(tuple(shape), q=q_mpf)
    if dim == 0:
        return mp.mpf(0)
    prod = mp.eye(dim)
    I = mp.eye(dim)
    h_val = q_mpf - 1 / q_mpf
    for (c, d, g) in word:
        d_term = d * h_val if d != 0 else mp.mpf(0)
        prod = prod * (c * sigmas[g] + d_term * I)
    return _mp_trace(prod)


def shape_character(word, q_val, shape):
    """χ^λ(word) for a single Wedderburn block.

    The per-shape piece of `full_markov_trace`, exposed so the q^{±n}
    scaling law stated in this module's docstring can be checked rather
    than assumed — see the assertion in main().
    """
    q_mpf = q_val if isinstance(q_val, mp.mpf) else mp.mpf(str(q_val))
    return _chi_block(word, q_mpf, shape)


def full_markov_trace(word, q_val):
    """Full Markov trace Σ_λ y_λ · χ^λ(word), in exact mpmath arithmetic."""
    q_mpf = q_val if isinstance(q_val, mp.mpf) else mp.mpf(str(q_val))
    total = mp.mpf(0)
    for part_list in partitions_of(3):
        shape = tuple(part_list)
        chi = _chi_block(word, q_mpf, shape)
        y = y_lambda_wenzl_bridge_numeric(list(shape), q_mpf, dps=50)
        total += y * chi
    return total


def main():
    set_compute_dps()
    set_compute_dps()
    q = Q_MP

    m_pi = mp.mpf(str(M_PI_PM_MEV_VALIDATION))  # MeV, PDG (codata_constants)

    # PDG meson masses for comparison (carried as mpf — no float64 in witness)
    pdg = {
        "π±": mp.mpf(str(M_PI_PM_MEV_VALIDATION)),
        "K±": mp.mpf(str(M_K_PM_MEV_VALIDATION)),
        "η": mp.mpf("547.862"),
        "η'": mp.mpf("957.78"),
        "φ": mp.mpf("1019.461"),
        "D±": mp.mpf("1869.66"),
    }

    print("=" * 70)
    print("  Meson spectrum predictions from CAL-3 + character ratios")
    print("=" * 70)
    print()

    # Compute Markov traces for mesons with increasing crossing count
    tr_pi = full_markov_trace(meson_braid_word(0), q)

    print(f"  tr_M(π) = {mp.nstr(tr_pi, 10)} (6 crossings, base meson)")
    print()

    mesons = [
        ("π (base)", 0, 6, "π±"),
        ("K (ūs)", 2, 8, "K±"),
        ("η-like (s̄s-ūu)", 4, 10, "η"),
        ("10+2 crossings", 6, 12, None),
        ("14 crossings", 8, 14, "D±"),
    ]

    print(f"  {'Meson':>20s}  {'cross':>5s}  {'tr_M':>12s}  {'ratio':>8s}  "
          f"{'m_pred':>10s}  {'m_PDG':>10s}  {'miss':>8s}")

    results = []
    for name, n_extra, n_cross, pdg_key in mesons:
        word = meson_braid_word(n_extra)
        tr = full_markov_trace(word, q)
        ratio = tr / tr_pi
        m_pred = m_pi * ratio

        pdg_val = pdg.get(pdg_key, None)
        miss_str = ""
        if pdg_val:
            miss_pct = (m_pred - pdg_val) / pdg_val * 100
            miss_str = f"{mp.nstr(miss_pct, 3)}%"

        print(f"  {name:>20s}  {n_cross:>5d}  {mp.nstr(tr, 8):>12s}  "
              f"{mp.nstr(ratio, 4):>8s}  {mp.nstr(m_pred, 6):>10s}  "
              f"{(mp.nstr(pdg_val, 6) if pdg_val else '—'):>10s}  {miss_str:>8s}")

        results.append({
            "name": name,
            "pdg_key": pdg_key,
            "crossings": n_cross,
            "n_extra": n_extra,
            # fmt, not the bare value: these are mpf and a raw float in a
            # witness is what the raw-float64 ratchet counts. `pdg_val` may be
            # None for a meson with no PDG entry, so it is only formatted when
            # present rather than stringified unconditionally.
            "tr_M": fmt(tr),
            "ratio_to_pion": fmt(ratio),
            "m_pred_MeV": fmt(m_pred),
            "m_PDG_MeV": fmt(pdg_val) if pdg_val is not None else None,
        })

    print()
    print("  NOTE: these ratios assume the SAME meson topology with")
    print("  additional σ₁ crossings. Real mesons differ by spin,")
    print("  flavor mixing, and binding topology. The predictions are")
    print("  structural (from Hecke representation theory), not fitted.")

    w = WitnessBuilder("meson-spectrum-predictions", engine="python")
    w.set_description(
        "Meson spectrum predictions from CAL-3 (m_π) + derived Hecke "
        "character ratios. Uses the trace ratio tr_M(n)/tr_M(π) with "
        "increasing crossing count."
    )
    w.set_audit_only("docs/audits/2026-05-27-meson-spectrum-predictions.md")
    w.add_data("results", results)

    # `kaon_predicted` read `computed=1, expected=1` — it recorded that a
    # number had been produced, which reaching this line already implies, and
    # said nothing about whether the character structure it came from is
    # right. The predictions all miss PDG by 56-79%, so there is no external
    # value to check them against; what IS checkable is the scaling law this
    # module's own docstring states and every prediction depends on. For n
    # extra σ₁ crossings the one-dimensional blocks must scale exactly:
    # χ_(3) by q^n (σ_i eigenvalue q) and χ_(1,1,1) by (-q⁻¹)^n. The check is
    # now in exact mpmath (no float64 floor): residual ~10^{-(dps)}, so 1e-40
    # relative still has decades of headroom — not a band chosen to pass
    # (qou-26f2). Kept relative rather than exact because the seminormal `b`
    # entries carry an mp.sqrt (irrational), so equality is to working dps.
    chi3_base = shape_character(meson_braid_word(0), q, (3,))
    chi111_base = shape_character(meson_braid_word(0), q, (1, 1, 1))
    rel_tol = mp.mpf("1e-40")
    scaling_ok = 0
    scaling_checked = 0
    for _name, n_extra, _n_cross, _key in mesons:
        word_n = meson_braid_word(n_extra)
        for shape, base, factor in (
                ((3,), chi3_base, q ** n_extra),
                ((1, 1, 1), chi111_base, (-1 / q) ** n_extra)):
            scaling_checked += 1
            want = factor * base
            scaling_ok += int(
                abs(shape_character(word_n, q, shape) - want)
                <= rel_tol * abs(want))
    w.add_assertion("one_dim_block_characters_scale_as_q_pow_n",
                    computed=scaling_ok, expected=scaling_checked, tolerance="0",
                    source="For each meson row, χ_(3) scales by q^n and "
                           "χ_(1,1,1) by (-q⁻¹)^n under n extra σ₁ crossings "
                           "— the Hoefsmit eigenvalue structure the mass "
                           "ratios are read off, checked to 1e-40 relative in "
                           "exact mpmath arithmetic.")
    w.add_data("kaon_prediction", {
        # Keyed on the ROW NAME, not on a float equality against `pdg["K±"]`.
        # That comparison broke the moment the payload was serialized — the
        # row's `m_PDG_MeV` became a formatted string while `pdg["K±"]` stayed
        # an mpf, so `next()` matched nothing and raised StopIteration. An
        # identity test on a name survives a change of representation; an
        # equality test on a formatted number does not.
        "m_pred_MeV": next(r["m_pred_MeV"] for r in results
                           if r["pdg_key"] == "K±"),
        "m_PDG_MeV": fmt(pdg["K±"]),
        "note": "structural ratio from character growth, not a fit; there is "
                "no independent expected value for the prediction itself",
        "has_independent_expected_value": False,
    })
    print(f"\n  Witness: {w.save()}")


if __name__ == "__main__":
    main()
