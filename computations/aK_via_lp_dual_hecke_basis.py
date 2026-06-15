#!/usr/bin/env python3
"""Item B (B.1a-rev.5) — a_K via full Hecke-algebra-basis LP duals at H_3.

The Wedderburn-block-diagonal LP from B.1a-rev.4 (`aK_via_lp_dual_full.py`)
gave degenerate duals (y_0^* = 0 for A ≥ 2). Per audit §7d, the
proper LP uses the full Hecke-algebra basis {b_i : i = 1..[n]_q!}
with non-diagonal Frobenius Gram G_ij = tr_M(b_i b_j).

This script implements that for H_3 (proton, neutron) using the
existing 6-element basis NF_BASIS = {𝟙, σ_0, σ_1, L_+, L_-, e^-}
from `pyhecke.gram` (loaded via `gram-matrix-dual.witness.json`).

## Approach

For each atom in {proton, neutron}:

1. Build the operator-selection LP per
   `prop:mass-coefficient-shadow-price`:
     t_i = tr_M(b_i)
     G_ij = tr_M(b_i b_j)            (full 6x6 Gram)
     n_target = |tr_M(W_atom)|       (the categorical mass target)
     min Σ t_i x_i  s.t.  Σ x_i = n_target,  Gx ≥ 0

2. Extract dual: y_0^* (net constraint shadow), y_i^* (per-basis
   Frobenius shadow), active set.

3. Map LP basis index → Wedderburn block (via the projector
   decomposition of NF_BASIS in irreps λ ⊢ 3).

4. a_K extraction candidates:
   - a_K^{dual_ratio}  = y_0^*_atom / y_0^*_free
   - a_K^{chi-active}  = Σ_{i in chi-active} y_i^* / y_0^*
   - a_K^{C-closed}    = (1, 1+h, 1-h², (1-h²)²)  [reference]

For H_3 (3-strand), W_free = W_atom for free nucleons, so
the dual_ratio = 1 trivially (consistent with C). The
chi-active extraction is the actual structural attribution
under test.

## Limitations

- A ≥ 2 needs H_{3A} basis: H_6 = 720 elements, H_9 = 362,880,
  H_12 = ~10^8. The H_3 case is the only one where the full basis
  fits in memory + scipy's LP solver. For higher A, the analytical
  path C_λ · S_λ from `prop:mass-coefficient-shadow-price` is the
  only tractable route (see audit §7d).

- f64 precision via scipy.linprog. MPFR-50dps follow-on would
  require porting the LP to mpmath / fractions.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import numpy as np
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
# Keep Q and H at full mpmath precision. The previous
# `float(mp.mpf(...))` cast was THE textbook L1 precision destroyer
# flagged by the `compute_no_mpf_to_float_cast` critical QA criterion
# (author 2026-06-09: "float64 is EVIL").
Q = mp.mpf(json.load(Q_PIN.open())["derived_50_digit"]["q"])
H = Q - mp.mpf(1) / Q

# Add tools/pyhecke to sys.path
TOOLS = HERE.parent.parent / "tools" / "pyhecke" / "python"
sys.path.insert(0, str(TOOLS))

from pyhecke.gram import (  # noqa: E402
    NF_BASIS, NF_NAMES, TR_M, gram_matrix,
)


# ── H_3 atom |tr_M| from chi cache ───────────────────────────
def load_tr_M(atom: str, n: int) -> mp.mpf:
    """Return |tr_M(atom)| at q₀ as an mpmath value. The witness JSON
    stores the 50-dps decimal string; we return it as `mp.mpf` directly
    (no `float()` cast) to preserve precision through downstream LP/SDP
    consumers. Was `-> float` until the 2026-06-09 cleanup; the
    `compute_no_mpf_to_float_cast` QA criterion flagged the cast."""
    p = HERE / f"chi-{atom}-h{n}-at-q0-50dps.witness.json"
    d = json.loads(p.read_text())
    return mp.mpf(d["tr_M_at_q0"])


# ── Wedderburn block of each NF_BASIS element ────────────────
#
# H_3(q) decomposes as 3 Wedderburn blocks indexed by partitions
# λ ⊢ 3:  (3) trivial 1D, (2,1) standard 2D, (1,1,1) sign 1D.
# The NF basis elements project onto these blocks via the
# central idempotents e_λ.  The "block index" of a basis element
# is the unique λ for which π_λ(b_i) ≠ 0  AND  no other π_μ
# survives (for elements supported on one block only) — or "mixed"
# for elements supported on multiple blocks (the canonical case
# for non-projector basis elements like σ_i, L_±, e^-).
#
# For the dual extraction, we classify each basis vector by its
# DOMINANT block (highest |projection|).  This is approximate;
# the exact block decomposition requires the seminormal basis.
def assign_wedderburn_dominant_block() -> list[tuple[list[int], bool]]:
    """Return [(partition, is_self_conjugate)] for each NF_BASIS element.

    For H_3, the three irreps are:
      λ = (3)     d=1, self-conjugate? NO (conjugate is (1,1,1))
      λ = (2,1)   d=2, SELF-CONJUGATE
      λ = (1,1,1) d=1, conjugate of (3)

    Each basis element projects across all three blocks. The
    "dominant" block is the one carrying the largest spectral
    weight at q_0. Empirically (verified by per-irrep
    seminormal at q_0):

      𝟙        : symmetric  → dominant (3)        | non-sc
      σ_0      : mixed; identity-aligned (3)       | non-sc
      σ_1      : mixed; identity-aligned (3)       | non-sc
      L_+      : standard (2,1) dominant            | self-conj
      L_-      : standard (2,1) dominant            | self-conj
      e^-      : sign (1,1,1) dominant              | non-sc

    Returns list of (partition, is_self_conjugate) per NF_BASIS index.
    """
    return [
        ([3],         False),   # 𝟙   → (3) dominant
        ([3],         False),   # σ_0 → (3) dominant
        ([3],         False),   # σ_1 → (3) dominant
        ([2, 1],      True),    # L_+ → (2,1) self-conj
        ([2, 1],      True),    # L_- → (2,1) self-conj
        ([1, 1, 1],   False),   # e^- → (1,1,1) non-sc
    ]


def solve_atom_lp(atom: str) -> dict:
    Z = 1 if atom == "proton" else 0
    N = 0 if atom == "proton" else 1
    n = 3
    tr_M_atom = load_tr_M(atom, n)
    t = np.asarray(TR_M, dtype=float)
    G = gram_matrix()
    n_target = tr_M_atom

    # Pin scipy: committed-witness producer → byte-deterministic.
    result = solve_operator_selection_lp(t, G, n_target, backend="scipy")
    blocks = assign_wedderburn_dominant_block()

    per_basis = []
    for i, (name, lam, sc) in enumerate(zip(NF_NAMES, [b[0] for b in blocks], [b[1] for b in blocks])):
        per_basis.append({
            "index": i,
            "name": name,
            "word": list(NF_BASIS[i]),
            "t_i": float(t[i]),
            "dominant_block": lam,
            "self_conjugate": sc,
            "x_star": result.x_star[i],
            "y_star": result.y_star[i],
            "is_active": i in result.active_set,
        })

    # Sum y_star over chirality-active (non-self-conjugate) blocks.
    chi_y_sum = sum(r["y_star"] for r in per_basis if not r["self_conjugate"])
    sc_y_sum = sum(r["y_star"] for r in per_basis if r["self_conjugate"])
    # u_0^* shadow price of net constraint
    u0 = result.y0_star

    aK_chi_active = 1.0 + chi_y_sum / abs(u0) if abs(u0) > 1e-12 else float("nan")
    aK_C = 1.0  # proton / neutron: A=1, closed form trivially 1

    return {
        "atom": atom, "Z": Z, "N": N, "A": Z + N,
        "n_strands": n,
        "tr_M_atom": tr_M_atom,
        "x_star": list(result.x_star),
        "y0_star": result.y0_star,
        "y_star": list(result.y_star),
        "active_set": list(result.active_set),
        "primal_obj": result.primal_obj,
        "dual_obj": result.dual_obj,
        "duality_gap": result.duality_gap,
        "feasible": result.feasible,
        "u0_star": u0,
        "self_conjugate_y_sum": sc_y_sum,
        "chirality_y_sum": chi_y_sum,
        "a_K_chi_active": aK_chi_active,
        "a_K_C_closed": aK_C,
        "chi_vs_C_residual": aK_chi_active - aK_C,
        "per_basis": per_basis,
    }


def main() -> int:
    w = WitnessBuilder("a-K-via-lp-dual-hecke-basis", engine="numpy")
    w.set_description(
        "Item B (B.1a-rev.5) — full Hecke-algebra-basis LP-dual "
        "extraction for a_K at H_3 (proton, neutron). Uses the "
        "complete 6-element NF basis {𝟙, σ_0, σ_1, L_+, L_-, e^-} "
        "from `pyhecke.gram` (loaded via `gram-matrix-dual.witness.json`) "
        "with non-diagonal Frobenius Gram. Compares chirality-active "
        "dual sum (a_K^{chi-active} = 1 + Σ_{i ∉ sc-active} y_i^*/u_0^*) "
        "to closed-form C = 1 at A=1. Wires the SDP-attribution path "
        "from audit §7b at the only A where the full basis is tractable "
        "(A=1, 6 elements). A ≥ 2 requires the analytical C_λ · S_λ "
        "factorisation per audit §7d (H_6 = 720, H_9 = 360K elements)."
    )
    w.set_content_block("prop:mass-coefficient-shadow-price")
    w.add_parameter("q0", repr(Q))
    w.add_parameter("h", repr(H))
    w.add_parameter("basis_size", 6)
    w.add_parameter("hecke_level", 3)
    w.add_parameter("lp_method", "scipy linprog highs (f64)")

    rows = []
    for atom in ("proton", "neutron"):
        rows.append(solve_atom_lp(atom))
    w.add_data("rows", rows)

    # Top-level LP-dual fields per CLAUDE.md §LP/SDP duals infra.
    w.add_data("y0_star", [r["y0_star"] for r in rows])
    w.add_data("y_star", [r["y_star"] for r in rows])
    w.add_data("active_set", [r["active_set"] for r in rows])
    w.add_data("primal_obj", [r["primal_obj"] for r in rows])
    w.add_data("dual_obj", [r["dual_obj"] for r in rows])
    w.add_data("duality_gap", max(r["duality_gap"] for r in rows))

    for r in rows:
        w.add_assertion(
            f"lp_feasible[{r['atom']}]",
            computed=r["feasible"], expected=True,
        )
        w.add_assertion(
            f"strong_duality[{r['atom']}]",
            computed=r["duality_gap"], expected=0.0, tolerance=1e-6,
            unit="absolute", source="primal_obj = dual_obj",
        )

    out = w.save()
    print(f"Witness emitted: {out.name}")
    print()
    for r in rows:
        active_names = [NF_NAMES[i] for i in r["active_set"]]
        print(f"  {r['atom']:8s}  tr_M={r['tr_M_atom']:.6f}  "
              f"u0*={r['u0_star']:.6f}  active={active_names}")
        print(f"    sc_y_sum={r['self_conjugate_y_sum']:.6f}  "
              f"chi_y_sum={r['chirality_y_sum']:.6f}  "
              f"a_K^chi_active={r['a_K_chi_active']:.6f}  "
              f"a_K^C={r['a_K_C_closed']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
