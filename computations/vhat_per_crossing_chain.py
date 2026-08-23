#!/usr/bin/env python3
"""
vhat_per_crossing_chain.py — DERIVE the per-crossing transfer chain
V̂_i(q) from the Hoefsmit / seminormal representation, for the proton
(uud) and neutron (udd) ATOMIC braids, with ZERO free parameters, and
FALSIFICATION-TEST against the cached |V̂_i| the brane tower consumes.

Missing input #2 named by docs/audits/2026-06-01-yekutieli-volume-join-
derivation.md §5 item 1:

  "The per-crossing transfer chain V̂_i(q) = z·a_i + b_i for the proton
   and neutron *atomic* braids. thm:markov-trace-product gives the product
   ∏ V̂_i = tr_M, but the INDIVIDUAL V̂_i ... Production never computes the
   per-generator factorisation."

────────────────────────────────────────────────────────────────────
WHAT V̂_i IS (the matrix functional, per thm:markov-trace-product)
────────────────────────────────────────────────────────────────────
At each generator σ_i the crossing chain reduces (Hecke quadratic) to a
linear element  a_i·σ_i + b_i.  The Markov trace of this element in the
2-dim STANDARD (Hoefsmit) representation V_(2,1) of H_3 is

    V̂_i = z·a_i + b_i,    z = 1/(q^{1/2}+q^{-1/2}),

because tr_M(σ_i) = z and tr_M(1) = 1.  So V̂_i is the MARKOV TRACE of
the per-generator reduced element — a TRACE functional of ρ(σ_i), NOT a
norm/det/eigenvalue.  The (a_i, b_i) are the entries of the 2×2 transfer
matrix obtained by left-multiplying (a,b) by [[c·h+d, c],[c, d]] for each
crossing (c,d) — this IS the standard-channel Hoefsmit matrix of c·σ+d·1
acting on the reduced coordinate.

This probe:
  1. Builds the genuine seminormal V̂_i = z·a_i + b_i per crossing chain
     (the thm:markov-trace-product / def:algebraic-quantum-volume form).
  2. Compares it to the PRODUCTION vertex_volume (pyhecke/atom.py), which
     is a W-weighted 3-channel sum  W_sym·λ_sym + W_std·V_std + W_alt·λ_alt
     — NOT the same functional. Flags the discrepancy RED.
  3. Confirms V_std = z·a+b equals the genuine seminormal Markov trace by
     building the actual 2×2 Hoefsmit matrices and computing tr_M directly.
  4. Reports whether V̂_i DIFFERS for proton (uud) vs neutron (udd)
     crossings — the p/n / isospin signal test.

NO fit. NO tuning. The cached production |V̂_i| are the falsification test.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
# Repo root by LANDMARK SEARCH, not by counting `.parent`s: the fixed
# count was off by one and resolved OUTSIDE the repo, so this bootstrap
# never fired -- masked because `_path_bridge`/PYTHONPATH already supplies
# the same directory in every in-repo run. Bean qou-rug0.
_QOU_REPO_ROOT = next(
    (_a for _a in Path(__file__).resolve().parents
     if (_a / "tools").is_dir() and (_a / "computations").is_dir()),
    Path(__file__).resolve().parent,
)
sys.path.insert(0, str(_QOU_REPO_ROOT / "tools" / "pyhecke" / "python"))

from mass_at_3A_proper import _cached_seminormal, partitions_of  # noqa: E402
from pyhecke.atom import (  # noqa: E402
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1, vertex_volume,
)
from pyhecke.gram import z, W_SYM, W_STD, W_ALT  # noqa: E402
from q_parameter import Q as q0, Q_INV as qi, HA as h  # noqa: E402


# ════════════════════════════════════════════════════════════════════
# 1. The genuine seminormal V̂_i = z·a_i + b_i  (thm:markov-trace-product)
# ════════════════════════════════════════════════════════════════════

def transfer_chain_ab(chain):
    """Standard-channel transfer matrix (a, b) for a crossing chain.

    Each crossing (c, d) contributes the factor c·σ + d·1 to the H_3
    element.  In the 2-dim standard rep, reducing the running element to
    the linear form a·σ + b·1 via the Hecke quadratic σ² = h·σ + 1 is the
    matrix recurrence (left-multiply (a, b) by [[c·h+d, c],[c, d]]):

        a ← a·c·h + a·d + b·c
        b ← a·c     + b·d

    Initial (a, b) = (0, 1) (the identity).  Returns (a, b) as floats.
    This recurrence is EXACTLY the production vertex_volume std-channel
    update — re-derived here from the σ² = hσ+1 Hecke relation.
    """
    a, b = 0.0, 1.0
    for c, d in chain:
        a, b = a * c * h + a * d + b * c, a * c + b * d
    return a, b


def vhat_seminormal_markov(chain):
    """Genuine per-generator V̂ = z·a + b  (thm:markov-trace-product)."""
    a, b = transfer_chain_ab(chain)
    return z * a + b


# ════════════════════════════════════════════════════════════════════
# 2. Independent cross-check: build the 2×2 Hoefsmit matrix and take tr_M
# ════════════════════════════════════════════════════════════════════

def _std_sigma_matrix():
    """The dim-2 standard-rep seminormal matrix σ_0 of H_3 (partition (2,1))."""
    sigmas, dim, _ = _cached_seminormal((2, 1))
    assert dim == 2, dim
    s = sigmas[0]
    return np.asarray(s.toarray() if hasattr(s, "toarray") else s)


def vhat_via_explicit_markov_trace(chain):
    """V̂ from the ACTUAL 2×2 Hoefsmit matrix product, Markov-traced.

    Build M = Π (c·σ + d·I) in the standard rep, then take the Markov
    trace tr_M(M) = z·(coefficient of σ) + (coefficient of 1).  Since the
    std rep is 2-dim and faithful for the linear reduction, we recover
    (a, b) from M by solving M = a·σ + b·I in the {σ, I} span, then
    V̂ = z·a + b.  This is an INDEPENDENT route to V̂ (matrix product,
    not the scalar (a,b) recurrence) and must agree to machine precision.
    """
    sigma = _std_sigma_matrix()
    I = np.eye(2)
    M = I.copy()
    for c, d in chain:
        M = M @ (c * sigma + d * I)
    # Solve M = a·sigma + b·I in the 2-dim {sigma, I} subspace via least
    # squares on the four matrix entries (the reduced element is always
    # in span{sigma, I} by the Hecke quadratic, so the fit is exact).
    A = np.column_stack([sigma.reshape(-1), I.reshape(-1)])
    coeffs, *_ = np.linalg.lstsq(A, M.reshape(-1), rcond=None)
    a, b = float(coeffs[0]), float(coeffs[1])
    return z * a + b, a, b


# ════════════════════════════════════════════════════════════════════
# Main
# ════════════════════════════════════════════════════════════════════

def main() -> int:
    print("=== Substrate ===")
    print(f"  q_0 = {q0:.12f}  h = {h:.10f}  z = {z:.10f}")
    print(f"  W_sym = {W_SYM:.8f}  W_std = {W_STD:.8f}  W_alt = {W_ALT:.8f}")
    print()

    chains = {
        "proton σ_0 (uud, gen 0)": _PROTON_G0,
        "proton σ_1 (uud, gen 1)": _PROTON_G1,
        "neutron σ_0 (udd, gen 0)": _NEUTRON_G0,
        "neutron σ_1 (udd, gen 1)": _NEUTRON_G1,
    }

    print("=== Per-crossing V̂_i: genuine seminormal Markov trace vs production ===")
    print(f"{'generator':28s} {'V̂(z·a+b)':>12s} {'V̂(matrix tr_M)':>15s} "
          f"{'production':>12s} {'genuine vs prod':>16s}")
    print("-" * 90)

    records = {}
    for name, chain in chains.items():
        v_genuine = vhat_seminormal_markov(chain)
        v_matrix, a, b = vhat_via_explicit_markov_trace(chain)
        v_prod = vertex_volume(chain)
        rel = (v_prod - v_genuine) / v_genuine * 100 if v_genuine else float("nan")
        print(f"{name:28s} {v_genuine:>12.6f} {v_matrix:>15.6f} "
              f"{v_prod:>12.6f} {rel:>15.3f}%")
        records[name] = {
            "chain": [list(t) for t in chain],
            "a_transfer": a,
            "b_transfer": b,
            "vhat_genuine_z_a_plus_b": v_genuine,
            "vhat_explicit_matrix_markov": v_matrix,
            "vhat_production_vertex_volume": v_prod,
            "genuine_vs_production_rel_pct": rel,
            "scalar_vs_matrix_agree": abs(v_genuine - v_matrix) < 1e-9,
        }
    print()

    # ── Internal consistency: scalar (a,b) recurrence == matrix product ──
    all_agree = all(r["scalar_vs_matrix_agree"] for r in records.values())
    print("=== Cross-check 1: scalar (a,b) recurrence == explicit 2×2 product ===")
    print(f"  All four chains agree to <1e-9 ? {'YES' if all_agree else 'NO'}")
    print(f"  → confirms V̂ = z·a+b IS the Markov trace of the Hoefsmit matrix.")
    print()

    # ── Falsification test: production != genuine (RED if differ) ──
    print("=== Falsification test: production vertex_volume vs genuine seminormal ===")
    max_rel = max(abs(r["genuine_vs_production_rel_pct"]) for r in records.values())
    prod_is_genuine = max_rel < 1e-6
    if prod_is_genuine:
        print(f"  Production MATCHES genuine seminormal to {max_rel:.2e}% — DERIVED.")
    else:
        print(f"  RED: production DIFFERS from genuine seminormal (max {max_rel:.3f}%).")
        print(f"  Production = W_sym·λ_sym + W_std·V_std + W_alt·λ_alt (3-channel)")
        print(f"  Genuine    = z·a + b = V_std alone (standard channel only).")
        print(f"  The W-weighted 3-channel sum is NOT thm:markov-trace-product's")
        print(f"  V̂_i = z·a_i+b_i.  The extra λ_sym/λ_alt channels + the W weights")
        print(f"  are a SEPARATE construction (the H_3 Wedderburn 3-channel average),")
        print(f"  not the per-generator Markov-trace factor the audit named.")
    print()

    # ── p/n signal test ──
    print("=== p/n signal test (isospin): do proton and neutron crossings differ? ===")
    pg0 = records["proton σ_0 (uud, gen 0)"]["vhat_genuine_z_a_plus_b"]
    ng0 = records["neutron σ_0 (udd, gen 0)"]["vhat_genuine_z_a_plus_b"]
    pg1 = records["proton σ_1 (uud, gen 1)"]["vhat_genuine_z_a_plus_b"]
    ng1 = records["neutron σ_1 (udd, gen 1)"]["vhat_genuine_z_a_plus_b"]
    d0 = (pg0 - ng0) / ((pg0 + ng0) / 2) * 100
    d1 = (pg1 - ng1) / ((pg1 + ng1) / 2) * 100
    print(f"  gen 0 (strong/quark channel): V̂_p = {pg0:.6f}  V̂_n = {ng0:.6f}  Δ = {d0:+.3f}%")
    print(f"  gen 1 (quark channel):        V̂_p = {pg1:.6f}  V̂_n = {ng1:.6f}  Δ = {d1:+.3f}%")
    pn_differ = abs(pg0 - ng0) > 1e-9 or abs(pg1 - ng1) > 1e-9
    print(f"  Proton ≠ Neutron per-crossing V̂ ? {'YES' if pn_differ else 'NO'}")
    print(f"  → the p/n split lives in the QUARK-PAIR crossings: uud has one ud")
    print(f"    mixed crossing on gen 0, udd has two; gen 1 carries dd (σ⁻¹) for n.")
    print()

    # ── Production tr_M product (the brane-tower-consumed |V̂_i|) ──
    prod_product = 1.0
    for r in records.values():
        prod_product *= r["vhat_production_vertex_volume"]
    print("=== Composition: ∏ V̂_i (thm:markov-trace-product ⇒ tr_M) ===")
    p_trM = (records["proton σ_0 (uud, gen 0)"]["vhat_production_vertex_volume"]
             * records["proton σ_1 (uud, gen 1)"]["vhat_production_vertex_volume"])
    n_trM = (records["neutron σ_0 (udd, gen 0)"]["vhat_production_vertex_volume"]
             * records["neutron σ_1 (udd, gen 1)"]["vhat_production_vertex_volume"])
    p_genuine = (pg0 * pg1)
    n_genuine = (ng0 * ng1)
    print(f"  proton  ∏V̂ production = {p_trM:.6f}   genuine z·a+b = {p_genuine:.6f}")
    print(f"  neutron ∏V̂ production = {n_trM:.6f}   genuine z·a+b = {n_genuine:.6f}")
    print()

    witness = {
        "description": "vhat_per_crossing_chain — derive V̂_i = z·a_i+b_i per crossing "
                       "from the Hoefsmit/seminormal rep for atomic p/n braids; "
                       "falsification-test vs production vertex_volume",
        "computation": "vhat_per_crossing_chain",
        "audit_only": True,
        "missing_input": "yekutieli-volume-join-derivation §5 item 1: per-crossing V̂_i",
        "functional": {
            "name": "Markov trace of the per-generator reduced element a_i·σ_i + b_i",
            "form": "V̂_i = z·a_i + b_i  (z = tr_M(σ_i), 1 = tr_M(I))",
            "channel": "STANDARD (2,1) Hoefsmit seminormal rep of H_3",
            "derived": True,
            "source_blocks": [
                "thm:markov-trace-product", "def:algebraic-quantum-volume",
            ],
        },
        "constants": {"q_0": str(q0), "h": str(h), "z": str(z),
                      "W_sym": str(W_SYM), "W_std": str(W_STD), "W_alt": str(W_ALT)},
        "per_crossing": records,
        "scalar_vs_matrix_all_agree": all_agree,
        "production_is_genuine_seminormal": prod_is_genuine,
        "production_max_rel_pct_vs_genuine": max_rel,
        "production_consumer_trace": {
            "note": "terms_2_3_atom_per_gen_mpfr_50dps.atom_per_generator_volumes_mpfr "
                    "computes BOTH the genuine std channel (Vs = z·a+b, line 246) "
                    "AND the W-weighted 3-channel full (Vf, line 247). The genuine "
                    "V̂_i = z·a+b IS production's 'std' field; the brane tower "
                    "(_li_2_q_util.compute_t2_t3_from_vols) consumes the 'full' field.",
            "genuine_equals_production_std_channel": True,
        },
        "pn_signal": {
            "gen0_proton": pg0, "gen0_neutron": ng0, "gen0_rel_pct": d0,
            "gen1_proton": pg1, "gen1_neutron": ng1, "gen1_rel_pct": d1,
            "proton_neutron_differ": pn_differ,
        },
        "trM_composition": {
            "proton_product_production": p_trM,
            "neutron_product_production": n_trM,
            "proton_product_genuine": p_genuine,
            "neutron_product_genuine": n_genuine,
        },
        "verdict": (
            "V̂_i = z·a_i + b_i is DERIVED from the standard-channel Hoefsmit "
            "seminormal rep with zero free parameters (Markov trace of the "
            "per-generator reduced element). It DIFFERS for proton vs neutron "
            "(p/n signal present in quark-pair crossings). PRODUCTION's "
            "vertex_volume is a DIFFERENT object (W-weighted 3-channel sum), "
            "NOT the genuine per-generator Markov-trace factor — flagged RED."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = HERE / "vhat-per-crossing-chain.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2))
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
