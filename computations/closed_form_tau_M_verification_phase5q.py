"""
closed_form_tau_M_verification_phase5q.py — Phase 5q verification of
the combined Phase 5c.1 + 5l closed form for tr_M(𝓑_K).

Computes:
  (a) the empirical tr_M(𝓑_K) via the full y_λ · χ_λ pipeline
      (H_{3A} character recomputation per atom — the expensive
      route the closed form sidesteps)
  (b) the closed-form prediction
        tr_M^3(𝓑_p)^Z · tr_M^3(𝓑_n)^N · ∏ f_i(q)
      using `closed_form_tau_M.closed_form_tau_M`
  (c) the relative error |a - b| / |a|

Across atoms D, T, ³He, ⁴He at the substrate canonical q_0.

If the rel.err is below 1e-12 across all atoms, this validates the
closed form for use in production tr_M scripts and unlocks the
migration described in `docs/canonical-derivation-cheat-sheet.md` §5
action #4.

  Ref: prop:interface-knot-markov-z.md (Phase 5c.1 interface identity)
  Ref: prop:constit-factor-tau-M-proton-identity.md (Phase 5l constit identity)
  Ref: closed_form_tau_M.py (the shared utility under test)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q0, Q_50_DIGIT_STR  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from hecke_characters import chi_lambda_braid, partitions_of  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from canonical_braid_marshalling import marshal_to_chi_lambda_braid  # noqa: E402
from hecke_core import _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1  # noqa: E402
from closed_form_tau_M import (  # noqa: E402
    closed_form_tau_M, closed_form_ratio, interface_census,
)

ATOMS = [
    ("D",   1, 1),
    ("T",   1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
]


def marshal_intra(chain_g0, chain_g1, h_val: float):
    """Marshal an H_3 nucleon intra word for chi_lambda_braid."""
    chain_with_gens = (
        [(c, d, 0) for c, d in chain_g0]
        + [(c, d, 1) for c, d in chain_g1]
    )
    return marshal_to_chi_lambda_braid(chain_with_gens, h_val)


def compute_tau_M_nucleon_H3(g0, g1, q_val: mp.mpf,
                              dps: int = 50) -> mp.mpf:
    """tr_M^3(nucleon, q) — proton or neutron H_3 Markov trace."""
    h_val = float(Q0 - 1 / Q0)
    word = marshal_intra(g0, g1, h_val)
    q_str = mp.nstr(q_val, dps, strip_zeros=False)
    total = mp.mpf(0)
    for lam in partitions_of(3):
        y = y_lambda_wenzl_bridge_numeric(lam, q_val, dps=dps)
        chi = chi_lambda_braid(lam, word, q_value=q_str,
                                precision="mpfr_50dps")
        total += y * mp.mpf(str(chi))
    return total


def compute_tau_M_full(Z: int, N: int, q_val: mp.mpf,
                       dps: int = 50, *, label: str = "") -> mp.mpf:
    """tr_M(𝓑_K) via the FULL y_λ · χ_λ pipeline at H_{3A}.

    This is the expensive route — the closed form sidesteps the
    H_{3A} partition sum.

    Per Gemini PR #863 review (long-compute logging discipline): emits
    periodic progress lines for n ≥ 12 (4He and beyond) including units/sec
    metric, wall elapsed time, and ETA so bottlenecks are visible.
    """
    h_val = float(Q0 - 1 / Q0)
    word = atom_braid_word_3A(Z, N, include_inter=True)
    word_m = marshal_to_chi_lambda_braid(word, h_val)
    n = 3 * (Z + N)
    q_str = mp.nstr(q_val, dps, strip_zeros=False)
    total = mp.mpf(0)
    parts = list(partitions_of(n))
    num_parts = len(parts)
    t_start = time.time()
    PROGRESS_THRESHOLD_N = 12  # Long-compute logging kicks in at H_12 (⁴He+)
    PROGRESS_EVERY = 10        # one line per 10 partitions processed
    for i, lam in enumerate(parts):
        y = y_lambda_wenzl_bridge_numeric(lam, q_val, dps=dps)
        chi = chi_lambda_braid(lam, word_m, q_value=q_str,
                                precision="mpfr_50dps")
        total += y * mp.mpf(str(chi))
        if n >= PROGRESS_THRESHOLD_N and (i + 1) % PROGRESS_EVERY == 0:
            elapsed = time.time() - t_start
            done = i + 1
            rate = done / elapsed if elapsed > 0 else 0.0
            remaining = num_parts - done
            eta = remaining / rate if rate > 0 else float("inf")
            prefix = f"      [{label}] " if label else "      "
            print(f"{prefix}progress: {done}/{num_parts} partitions  "
                  f"{rate:.3f} parts/sec  elapsed {elapsed:.1f}s  "
                  f"ETA {eta:.1f}s")
    return total


def main() -> int:
    set_compute_dps(50)
    builder = WitnessBuilder(
        "closed-form-tau-M-verification-phase5q", engine="python"
    )
    # Per Copilot PR #863 review: prop:interface-knot-markov-z is wired
    # to `delta-lambda-fr-identity-phase5c.witness.json`, not this Phase 5q
    # verification witness — so setting contentBlock here would be a stale
    # claim (audit-wiring would flag it as orphan + stale).  This Phase 5q
    # script is a STANDALONE verification artifact for the combined
    # Phase 5c.1 + 5l closed form (downstream consumer of both props).
    # Mark as auditOnly anchored to the cheat sheet's §5 action #4 entry.
    builder.set_audit_only("docs/canonical-derivation-cheat-sheet.md")

    q_val = mp.mpf(Q_50_DIGIT_STR)
    print(f"=== Phase 5q: closed-form tr_M(𝓑_K) verification ===\n")
    print(f"  q_0 = {Q_50_DIGIT_STR}\n")

    # Compute the two H_3 building blocks once.
    print(f"Computing H_3 building blocks at q_0...")
    t0 = time.time()
    tau_p = compute_tau_M_nucleon_H3(_PROTON_G0, _PROTON_G1, q_val)
    print(f"  tr_M^3(𝓑_p, q_0) = {float(tau_p):.16f}  "
          f"[{time.time()-t0:.2f}s]")
    t0 = time.time()
    tau_n = compute_tau_M_nucleon_H3(_NEUTRON_G0, _NEUTRON_G1, q_val)
    print(f"  tr_M^3(𝓑_n, q_0) = {float(tau_n):.16f}  "
          f"[{time.time()-t0:.2f}s]")
    print()

    results = []
    for name, Z, N in ATOMS:
        print(f"  {name} (Z={Z}, N={N}):")
        t0 = time.time()
        tau_full_empirical = compute_tau_M_full(Z, N, q_val, label=name)
        t_emp = time.time() - t0
        t0 = time.time()
        # Explicit chi_lambda_braid convention — the empirical slow path
        # above is bound to chi_lambda_braid via marshal_to_chi_lambda_braid
        # (line 93). The closed-form side must use the same convention to
        # validate the marshalling-pipeline-faithful behavior. The default
        # default for closed_form_tau_M switched to "bring_color_weighted"
        # 2026-06-01 (canonical/derived per substrate δ), so we pass
        # explicitly here to preserve this script's original verification
        # purpose.
        tau_full_closed = closed_form_tau_M(
            Z, N, q_val, tau_p, tau_n,
            pn_convention="chi_lambda_braid",
        )
        t_cf = time.time() - t0
        rel_err = (abs(tau_full_empirical - tau_full_closed)
                   / abs(tau_full_empirical)) if tau_full_empirical != 0 else mp.mpf("inf")
        census = interface_census(Z, N, pn_convention="chi_lambda_braid")
        ratio = closed_form_ratio(Z, N, q_val, pn_convention="chi_lambda_braid")
        results.append({
            "atom": name,
            "Z": Z, "N": N,
            "tau_M_empirical": float(tau_full_empirical),
            "tau_M_empirical_str": mp.nstr(tau_full_empirical, 30),
            "tau_M_closed_form": float(tau_full_closed),
            "tau_M_closed_form_str": mp.nstr(tau_full_closed, 30),
            "rel_err": float(rel_err),
            "interface_ratio": float(ratio),
            "interface_census": census,
            "wall_seconds_empirical": t_emp,
            "wall_seconds_closed": t_cf,
            "speedup_factor": t_emp / t_cf if t_cf > 0 else float("inf"),
        })
        print(f"    empirical tr_M = {float(tau_full_empirical):.16f}  "
              f"[{t_emp:.2f}s]")
        print(f"    closed-form    = {float(tau_full_closed):.16f}  "
              f"[{t_cf:.4f}s]")
        print(f"    rel.err        = {float(rel_err):.4e}")
        print(f"    interface census: {census}")
        print(f"    interface ratio (closed): {float(ratio):.6f}")
        print(f"    speedup: {t_emp/t_cf:.0f}x")
        print()

    max_rel_err = max(r["rel_err"] for r in results)
    print(f"=== Verdict ===\n")
    print(f"  Max rel.err. across {len(results)} atoms: {max_rel_err:.4e}")
    if max_rel_err < 1e-12:
        verdict = "closed-form-verified-50dps"
        print(f"\n  ✓ CLOSED FORM VERIFIED at mpfr-50-dps precision:")
        print(f"      tr_M(𝓑_K) = tr_M^3(𝓑_p)^Z · tr_M^3(𝓑_n)^N · ∏ f_i(q)")
        print(f"    across D, T, ³He, ⁴He.  Migration of the 4 production")
        print(f"    tr_M scripts (cheat-sheet §5 action #4) is now unblocked.")
    elif max_rel_err < 1e-6:
        verdict = "closed-form-verified-6dps"
        print(f"\n  ⚠ Closed form agrees to ~6 dps; investigate remaining drift.")
    else:
        verdict = "closed-form-discrepancy"
        print(f"\n  ✗ Closed form does NOT match empirical (rel.err {max_rel_err:.2e}).")

    builder.set_description(
        "Phase 5q: empirical verification of the combined Phase 5c.1 "
        "(interface-knot Markov-axiom factor) + Phase 5l (constit-side "
        "disjoint-product) closed form for tr_M(𝓑_K) across D, T, ³He, "
        "⁴He at q_0.  Compares the full y_λ · χ_λ pipeline at H_{3A} "
        "(expensive) against tr_M^3(𝓑_p)^Z · tr_M^3(𝓑_n)^N · ∏_i f_i(q) "
        "(closed form, evaluated through `closed_form_tau_M.py`).  "
        "Verification unblocks the migration of 4 production tr_M scripts "
        "(cheat-sheet §5 action #4)."
    )
    builder.add_parameter("q_0", str(q_val))
    builder.add_parameter("atoms", [name for name, _, _ in ATOMS])
    builder.add_data("tau_M_proton_H3", float(tau_p))
    builder.add_data("tau_M_neutron_H3", float(tau_n))
    builder.add_data("per_atom_results", results)
    builder.add_data("verdict", verdict)
    builder.add_data("max_rel_err", float(max_rel_err))
    builder.add_assertion(
        name="closed_form_tau_M_matches_empirical",
        computed=float(max_rel_err),
        expected=0.0,
        tolerance=1e-12,
        unit="dimensionless",
        source=(
            f"Phase 5q: max relative error between empirical tr_M(𝓑_K) "
            f"and the closed-form prediction across {len(results)} atoms "
            f"at q_0.  Identity holds at mpfr-50-dps precision if "
            f"max rel.err < 1e-12."
        ),
    )
    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).
    builder.add_data("lean_uniqueness_ref", {
        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",
        "framework_doc":
            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",
    })

    builder.save()
    print(f"\nWitness written: closed-form-tau-M-verification-phase5q.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
