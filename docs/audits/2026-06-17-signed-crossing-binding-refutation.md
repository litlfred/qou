# Signed-crossing (ILP-with-chirality) binding construction — refuted (2026-06-17)

**Branch:** `claude/binding-edge-set-sdp-probe-2026-06-17`
**Probe:** [`computations/probes/signed_crossing_feasibility_probe.py`](../../computations/probes/signed_crossing_feasibility_probe.py)
· witness `computations/signed-crossing-feasibility.witness.json`

## Context

The per-isotope binding `B(K) = E₀·Σ_bonds log(1/f_bond)` has a *derived*,
non-fitted per-bond kernel (`f_pp=z`, `f_nn=z−h`, `f_pn=z−h(½−δ/4)`,
`z=√q/(q+1)`; `∏ f_bond` reproduces the computed `tr_atom/tr_free` to
1.1e‑15). The open piece is the **edge set**. Prior work refuted:

- **continuous LP** (`lp_dual_solver`): fractional occupancies, and
  **circular** — the operator-selection LP takes `n_target = B/E₀` (the
  AME binding) as input, so it fits a known answer rather than predicting.
- **non-negative integer enumeration** (`bond_edge_set_selection_probe.py`):
  no `0 ≤ (n_pp, n_pn, n_nn)` closes D/T/³He/⁴He jointly.

The remaining untested regime was **signed integers** — chirality on the
crossings, `B = E₀·Σ sign·log(1/f)` with `sign ∈ {+1,−1}` — motivated by:
the canonical atom braid (`atom_gen_chains`) *reads the bonds from the
knot* as the complete graph with every crossing `c=+1`, and signed
cancellation could in principle land between integer values.

## Result — refuted

Exhaustive enumeration of every signed assignment to the canonical
complete-graph crossings (`signed_crossing_feasibility_probe.py`, exact
mpmath, `E₀ ≈ 4.186 MeV`):

| atom | graph (pp,pn,nn) | B/E₀ | best pure-chirality B | miss | ≤5% |
|------|------------------|------|-----------------------|------|-----|
| D    | (0,1,0) | 0.531 | 3.890 MeV | 74.9 % | ✗ |
| T    | (0,2,1) | 2.026 | 5.178 MeV | 39.0 % | ✗ |
| ³He  | (1,2,0) | 1.844 | 4.872 MeV | 36.9 % | ✗ |
| ⁴He  | (1,4,1) | 6.760 | 23.64 MeV | 16.4 % | ✗ |

**Pure chirality (signs only, canonical graph fixed): 0/4 close within
±5 %.** Allowing edge *absence* (which re-adds edge **selection** — the
very fitting freedom the construction must avoid) closes only ³He
(0.79 %), still missing D/T/⁴He.

**Deuteron crux (analytic).** The deuteron has only a pn bond (intra-
nucleon crossings cancel in the free/atom ratio), so its binding in log
units must be an integer multiple of `log(1/f_pn) = 0.929`. But
`B(D)/E₀ = 0.531`, and `0.531/0.929 = 0.572` — the deuteron needs **0.57
of a pn bond**. No signed integer (`±0.929`, `0`) reaches 0.531. The
obstruction is a genuinely **fractional effective coupling**, not an
edge or sign choice. (This matches the corpus's earlier "occupancy ≈0.57
halo-loose" finding; signs do not rescue it.)

## Verdict

The entire **crossing-counting family** for binding — continuous LP
(fractional + circular), non-negative integer enumeration, and signed
integer / chirality (this probe) — is **closed**. The deuteron's 0.57
fractional occupancy cannot be represented by any integer crossing
structure. The only non-circular direction left is a **knot-geometry-
dependent bond strength** (the per-nucleus volume route / Path B),
already audited as stalled at ≤2.5 %. This is consistent with the
2026-06-17 binding-frontier audit: the per-isotope binding program is
Subgoal-2 (research-grade, owner-declined 2026-05-08).

**Do not re-propose signed/ILP crossing selection for binding** — it is
examined and refuted here.
