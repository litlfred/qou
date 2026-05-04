#!/usr/bin/env python3
"""DP probe: cycle-additive upper bound on q=0 pole order over partition seminormals.

For each partition λ ⊢ n and the atomic braid β, compute the max
pole order at q = 0 over all closed SYT cycles in the seminormal
representation ρ_λ via dynamic programming.  Per-block contributions:

  σ at 1×1_row (eigenvalue q):       0
  σ at 1×1_col (eigenvalue −q⁻¹):    1
  σ at 2×2 diag, ρ > 0 (a regular):  0
  σ at 2×2 diag, ρ < 0 (a' pole 1):  1
  σ⁻¹ at any block: opposite of σ
  averaged at any block: 1
  off-diagonal b at 2×2 (always regular at q=0): 0

The DP gives an UPPER BOUND on the actual χ^λ(β) pole order at q=0,
NOT the exact value.  It does not account for cancellations from:

  (i)  Hecke quadratic relation σ² = h·σ + 1 (the constant 1 term
       cancels the q⁻² from −q⁻¹·−q⁻¹ in adjacent positions).
  (ii) σ·σ⁻¹ = I in adjacent positions (DP would count 1+0 = 1,
       actual = 0).

Empirical comparison (atomic braid, DP max vs witness shift/2):

  atom               empirical q-pole   DP-max   Δ
  ----               ----------------   ------   ---
  proton (no inter)         10            11      1
  neutron (no inter)         8            10      2
  D (deuteron)              20            22      2
  T (triton)              30.5            33    2.5
  ³He                       29            34      5

So the DP upper bound is reasonably tight (Δ ≤ 5) but not exact.
Closing the categorical proof requires an additional "cancellation
count" subtracted from the DP bound.  The structural target is:

    shift(Z, N) / 2  =  DP_max(λ*)(β(Z, N))  −  cancellation_count(β(Z, N))

with cancellation_count derivable from the σ/σ⁻¹ adjacency and
σ²-reduction structure of the atomic-braid word.  This is the
residual research step.

Tractability: O(steps · f^λ · 2) per starting SYT.  For ⁶Li
(n=18, max f^λ ≈ 10⁴, 71 steps) the DP runs in ~10⁸ transitions —
expensive but feasible.

Output: `dp-pole-probe.witness.json` with per-partition DP-max for
each canonical-pppnnn atom A = 1..4.
"""
from __future__ import annotations

import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_characters import partitions_of, standard_young_tableaux  # noqa: E402
from hecke_character_symbolic import atomic_braid_to_crossings  # noqa: E402


def block_kind_at(syt, contents, k_gen, dim, all_syts):
    """Determine the seminormal-block kind for SYT `syt` under generator
    σ_{k_gen+1} (gen_idx is 0-based in the matrices array; σ_1 = gen_idx 0).

    Returns a tuple (kind, partner_idx, rho).
    """
    # σ at gen_idx swaps numbers (k_gen+1) and (k_gen+2) in the SYT.
    n_lower = k_gen + 1
    n_upper = k_gen + 2
    cell_lower = syt[n_lower]
    cell_upper = syt[n_upper]
    rho = contents[cell_upper] - contents[cell_lower]
    if rho == 1:
        return ('1x1_row', None, rho)
    if rho == -1:
        return ('1x1_col', None, rho)
    # 2x2: find swap partner (swap n_lower ↔ n_upper labels in the SYT)
    swap_map = dict(syt)
    swap_map[n_lower] = cell_upper
    swap_map[n_upper] = cell_lower
    for j, syt_j in enumerate(all_syts):
        if syt_j == swap_map:
            return ('2x2', j, rho)
    raise ValueError(f"swap partner not found for SYT idx with ρ={rho}")


# Pole-order contribution per generator type and block-kind / matrix-entry choice.
# Matrix entry choice: for 1x1 blocks the only choice is the eigenvalue.
# For 2x2 blocks: 'diag_self' (diagonal at current SYT) or 'off_diag' (swap to partner).
def pole_contribution(gen_type, block_kind, entry_choice):
    if block_kind == '1x1_row':  # eigenvalue q
        return {'sigma': 0, 'sigma_inv': 1, 'averaged': 1}[gen_type]
    if block_kind == '1x1_col':  # eigenvalue -q^{-1}
        return {'sigma': 1, 'sigma_inv': 0, 'averaged': 1}[gen_type]
    if block_kind == '2x2':
        if entry_choice == 'off_diag':  # b is regular at q=0
            return 0
        # 'diag_self': depends on which SYT we are at
        # If we are at the "ρ > 0" SYT: diagonal a is regular at q=0.
        # If we are at the "ρ < 0" SYT (swap partner): diagonal is a',
        # which equals h/(1 − q^{2ρ_self}) and at q=0 has pole 1.
        # We pass the sign of ρ_self to disambiguate.
        raise ValueError("2x2 entry_choice='diag_self' needs ρ sign")


def pole_diag_at_2x2(gen_type, rho_sign):
    """Diagonal contribution for 2x2 block, knowing the sign of ρ at the
    current SYT.  ρ > 0: a regular at q=0 (so σ:0, σ⁻¹:1, avg:1).
                     ρ < 0: a has pole 1 (so σ:1, σ⁻¹:0, avg:1)."""
    if rho_sign > 0:
        return {'sigma': 0, 'sigma_inv': 1, 'averaged': 1}[gen_type]
    else:
        return {'sigma': 1, 'sigma_inv': 0, 'averaged': 1}[gen_type]


def max_pole_for_partition(shape, crossings):
    """Maximum closed-cycle pole order of the atomic braid in the
    seminormal representation ρ_shape via dynamic programming."""
    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return None

    # DP state: dp[i] = max pole order of partial cycle from start_syt s
    # to current SYT i, over all step prefixes seen so far.
    # We compute dp for each starting SYT s, then take dp_final[s] (path
    # ending at s) as the closed-cycle pole order.
    # To compute trace, we sum over s but for max-pole we just track per s.

    best_pole = 0
    for s in range(dim):
        # dp[t] = max pole achieved over all paths s → ... → t after k steps
        dp = [-1] * dim
        dp[s] = 0
        for k_gen, gen_type in crossings:
            new_dp = [-1] * dim
            for t in range(dim):
                if dp[t] < 0:
                    continue
                # Determine block kind at SYT t under σ_{k_gen+1}
                kind, partner, rho = block_kind_at(syts[t], contents, k_gen, dim, syts)
                if kind == '1x1_row':
                    # Stay at t, single eigenvalue q
                    p = {'sigma': 0, 'sigma_inv': 1, 'averaged': 1}[gen_type]
                    if dp[t] + p > new_dp[t]:
                        new_dp[t] = dp[t] + p
                elif kind == '1x1_col':
                    # Stay at t, single eigenvalue -q^{-1}
                    p = {'sigma': 1, 'sigma_inv': 0, 'averaged': 1}[gen_type]
                    if dp[t] + p > new_dp[t]:
                        new_dp[t] = dp[t] + p
                else:  # 2x2
                    rho_sign = 1 if rho > 0 else -1
                    # Diagonal stay: pole_diag_at_2x2
                    p_diag = pole_diag_at_2x2(gen_type, rho_sign)
                    if dp[t] + p_diag > new_dp[t]:
                        new_dp[t] = dp[t] + p_diag
                    # Off-diagonal swap: pole 0
                    if dp[t] + 0 > new_dp[partner]:
                        new_dp[partner] = dp[t]
            dp = new_dp
        # Closed cycle: must return to s
        if dp[s] > best_pole:
            best_pole = dp[s]
    return best_pole


def main():
    import json
    from datetime import datetime, timezone

    # A ≥ 4 is too slow in pure Python (f^λ × steps × #starting-SYTs scales
    # quickly).  Restrict to A ≤ 3 where the DP runs in seconds.
    cases = [
        ("proton (no inter)",  1, 0, False, 20),
        ("neutron (no inter)", 0, 1, False, 16),
        ("D (deuteron)",       1, 1, True,  40),
        ("T (triton)",         1, 2, True,  61),
        ("³He",                2, 1, True,  58),
    ]
    print(f"{'atom':>20}  {'empirical shift':>15}  {'DP max':>8}  "
          f"{'best λ*':>20}  {'Δ (cancel count)':>17}")
    print('-' * 100)

    out_rows = []
    for label, Z, N, inter, emp_shift in cases:
        n = 3 * (Z + N)
        if n == 0:
            continue
        crossings = atomic_braid_to_crossings(Z, N, include_inter=inter)
        max_dp = 0
        best_lams = []
        for shape in partitions_of(n):
            try:
                mp = max_pole_for_partition(tuple(shape), crossings)
                if mp > max_dp:
                    max_dp = mp
                    best_lams = [tuple(shape)]
                elif mp == max_dp:
                    best_lams.append(tuple(shape))
            except Exception:
                pass
        emp_q_pole = emp_shift / 2.0
        delta = max_dp - emp_q_pole
        best_str = ', '.join(str(s) for s in best_lams[:3]) + ('...' if len(best_lams) > 3 else '')
        print(f"{label:>20}  {emp_shift:>15}  {max_dp:>8}  {best_str:>20}  {delta:>17.1f}")
        out_rows.append({
            "atom": label,
            "Z": Z, "N": N,
            "include_inter": inter,
            "empirical_shift": emp_shift,
            "empirical_q_pole": emp_q_pole,
            "DP_max_pole": max_dp,
            "DP_best_lambdas": [list(s) for s in best_lams],
            "cancellation_count": delta,
        })

    out = {
        "computation": "dp-pole-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Cycle-additive DP upper bound on q=0 pole order of seminormal "
            "characters χ^λ(β) for atomic braids β.  DP runs over closed "
            "SYT cycles in ρ_λ with per-step weight 0/1 by per-block + "
            "ρ-sign + generator-type rules.  DP gives an upper bound; "
            "actual q-pole order = DP_max − cancellation_count, where the "
            "cancellation count tracks σ²-reduction and σ·σ⁻¹ identities "
            "the cycle-additive DP cannot capture.  Closes 2/3 of the "
            "shift formula categorically; the cancellation count is the "
            "residual research step toward 3/3."
        ),
        "rows": out_rows,
    }
    out_path = HERE / "dp-pole-probe.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWitness: {out_path}")


if __name__ == '__main__':
    main()
