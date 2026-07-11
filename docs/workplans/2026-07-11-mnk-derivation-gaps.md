# M₃/M₄ binding-weight closure — the open DERIVATION gaps (qou-v0yw, now ungated)

**Date:** 2026-07-11
**Bean:** `qou-v0yw` (now tagged `ungated`).
**Gate status:** the Subgoal-2 owner reversal (2026-07-11, PR #3607) opened the geometric /
substrate-derivation routes for all agents. This document enumerates the concrete open
**derivation** targets so the work is actionable — and states, per gap, the **anti-fit
checkpoint** that separates a derivation (wireable) from a fit (bookkeeping only).

## The setting (established, not open)

Binding is the body-order tower `B(K) = Σ_{n} m_e·a_D^(n)·wₙ(K)`, and the corpus has already
fixed everything **except** the coordination geometry:

| Piece | Status | Source |
|---|---|---|
| per-cluster energy `a_D^(n)` | **derived** (na-Stokes period, deuteron-anchored) | #3545 Parts 1–6 |
| per-bond `b*` = connected `tr_M` = centered Gram norm | **derived** (exact identity) | #3545 Part 12 |
| bond-extensivity `B ~ Σ_bonds b*` | **derived** (bond translation-invariance) | #3545 Part 11 |
| Milnor `Mₙ` of a **given** link | **derived + validated** (Magnus `μ̄`-tower) | #3545 Part 7 |
| 2-body count `M₂ = C(A,2)` (A≤4) | **derived, fit-free** (deuteron-pinned `w₂`) | #3588 |
| edge set = max-contact packing (principle) | **derived** (variational) | #3545 Part 13 |
| **which link `𝓑_K` per isotope (A≥5)** | **OPEN** — the gaps below | #3545 Parts 8–9, #3585 |

**The fit vs derivation line (the discipline this whole doc serves).**
Inverting AME binding for per-isotope `wₙ` (#3534: `4.353, 9.331, 15.919`) is a **fit** —
`A−1` unknowns vs 1 equation per isotope, no predictive content, **never canonical**. A
**derivation** fixes `wₙ = a_D^(n)·Mₙ(K)` from topology/geometry with **only the deuteron
anchor**, then **predicts** `B(K)` for isotopes it never touched (⁶Li, ⁷Li, ⁹Be, ¹²C) and is
tested against AME. #3585 showed the naive equal-weight / all-subsets `C(A,n)` version
**fails** that test (+920% at ⁶Li) — informative, not fatal: it says the edge-set must
*restrict* which subsets bond. That restriction is GAP-1.

---

## GAP-1 — the max-contact edge set for A≥5 (the primary blocker)

**Statement.** For A≤4 all nucleon spheres mutually touch, so max-contact `= C(A,2)` (simplex)
— #3588's fit-free result. For A≥5 not all can touch: the edge set is the specific
max-contact **sphere-packing contact graph** (triangular bipyramid `#e=9`, octahedron `#e=12`,
pentagonal bipyramid, …). This is a **pure 3-D geometry** problem — no free parameter.

**Why derivation, not fit.** The contact numbers are geometric facts about unit-sphere
packings, computed independently of binding data. `B(K) = a_D^(2)·b*·#contacts` then
**predicts** the A≥5 binding.

**First compute (concrete).** Enumerate max-contact packings for A=5,6,7 (known
Erdős–type contact-graph maxima), evaluate `B_2(A) = B(D)·#contacts`, compare to AME2020
(`AME_B_LI5/LI6/LI7_MEV_VALIDATION` are live in `codata_constants.py`). Extend
`binding_edge_set_selection.py` (#3545 Part 13) past the A≤4 simplex.

**Anti-fit checkpoint.** The contact count must come from the packing geometry, **not** be
chosen to match `B_AME`. If A=6 needs `#contacts=12` but max-contact packing gives `9`, that
is a **real prediction gap** to report (likely the cluster/halo deviation, GAP-4), not a knob
to turn.

---

## GAP-2 — the M₃ (Borromean-triple) count per isotope

**Statement.** The 3-body term rides on top of the pairwise edges: `M₃(K) = #` jointly-linked
triples with `μ̄₁₂₃ ≠ 0` (irreducible Borromean 3-body — a chain gives `μ̄₁₂₃=0`). ⁴He's magic
surplus (residual 14.95 MeV over the `C(4,2)=6` pairwise backbone, #3588) is exactly this term.

**Why derivation, not fit.** `μ̄₁₂₃` is a computed topological integer of `𝓑_K` (Magnus
expansion, machinery validated #3545 Part 7). Given the link, `M₃` is not free.

**First compute.** Once GAP-1 fixes the A≥5 contact graph, promote it to a link (assign
crossings/framing per the canonical braid convention) and run the validated
`binding_mn_milnor_linking.py` `μ̄`-tower on it; count nonzero triples. Test `⁴He`: does the
`M₃` term reproduce the 14.95 MeV residual with `w₃ = a_D^(3)` (fixed), no tuning?

**Anti-fit checkpoint.** `w₃` is `a_D^(3)` (na-Stokes, deuteron-anchored) — **not** solved from
⁴He's residual. If `a_D^(3)·M₃(⁴He)` misses 14.95 MeV, report the miss; do not back out `w₃`.

---

## GAP-3 — the derived `R(q,x)` q-difference kernel (the weight generating function)

**Statement.** The weights `wₙ` are the output of `G(qx;q) = R(q,x)·G(x;q)`. #3545 Part 3
showed **no parameter-free constant-ratio kernel** reproduces the extracted weights to 5%
(`[n]_q²` lone near-miss at 6.9%), and a tuned recursion is the banned 7th ansatz. The open
target is a `R(q,x)` **derived** from the fibre root-of-unity singularity structure of
`λ_SW` (formalize-first), not fit to `wₙ`.

**Why derivation, not fit.** `R(q,x)` from the na-Stokes / Habiro fibre structure is fixed by
the framework; its `wₙ` are then predictions. Fitting `R` to the anchors is the forbidden move.

**First step (formalize-first).** Per §3.3 discipline: state the invariant `R` must satisfy
(the `D(m)` Habiro tower target, #3545 Part 2 — `(q−1)²·Φ_cyclotomic` leading structure) and
try to derive `R` from it symbolically before any numerical search. This is the
research-grade leg; couple to the s5-so3 keystone (`W_λ` / Identity I).

**Anti-fit checkpoint.** If `R` is obtained by inverting `wₙ` data → fit, not canonical.

---

## GAP-4 — cluster/halo deviations below max-contact (⁶Li, ⁹Be)

**Statement.** ⁶Li (α+d) and ⁹Be sit *below* max-contact — loosely bound, genuine
nuclear-structure deviation the max-contact principle alone does not fix. The α-cluster level
is #3551's scope (Brink/Hafstad–Teller deltahedra — the α-instance of the same max-contact
principle).

**Why (partly) derivation.** The α-cluster contact-graph is itself a max-contact geometry one
level up (α's as the units). The deviation is where the two-level structure (nucleon-level vs
α-level packing) must be reconciled — a structural, not fitted, question, but the hardest.

**Anti-fit checkpoint.** A per-isotope "correction" tuned to `B_AME(⁶Li)` is a fit. The α+d
cluster structure must be **read off the geometry**, then tested.

---

## Coordination

- Overlaps the active binding thread: #3545 (13-part audit, the derivation map), #3585 (the
  A≥5 blow-up that motivates GAP-1), #3588 (the fit-free 2-body anchor), #3549/#3551 (α-cluster
  contact graphs = GAP-4 territory), #3548 (`W_λ` transfer matrix = GAP-3/s5-so3).
- **Coordinate before solo compute** on any of these — several are live sibling scopes.
- s5-so3 keystone ledger (`docs/coordination/s5-so3-keystone.md`) is the GAP-3 hub.

**Nothing here is a result** — this is the actionable open-gap map, scope-(a). No compute, no
witness, no wiring. Each gap names its first concrete step and its anti-fit checkpoint.
