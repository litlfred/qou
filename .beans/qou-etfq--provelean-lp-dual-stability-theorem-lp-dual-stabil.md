---
# qou-etfq
title: 'PROVE(lean): lp_dual_stability — theorem lp_dual_stability [ctx : LpDualStabilityContext] : (∀ i : Fin ctx.channels, 0 ≤ (F [cited bertsimas1997,manuscript]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - cite-bertsimas1997
created_at: 2026-08-01T23:31:07Z
updated_at: 2026-08-22T06:20:00Z
parent: qou-k1mq
---

**File:** `QOU/ParticleInteractions/lp_dual_stability.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/ParticleInteractions/lp_dual_stability.lean

### `lp_dual_stability`  —  line 89  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem lp_dual_stability [ctx : LpDualStabilityContext] : (∀ i : Fin ctx.channels, 0 ≤ (Finset.univ.sum fun j : Fin ctx.channels => ctx.G i j * ctx.x_star j)) ∧ (∀ i : Fin ctx.channels, |ctx.y_star i| ≤ ctx.κ_G * ctx.t_norm) ∧ (Finset.univ.sum fun j : Fin ctx.channels => ctx.G ctx.σ_0_idx j * ctx.x`
- **Cited:** `[bertsimas1997]`, `[manuscript]`, `[bertsimas1997]`
  - [bertsimas1997] Bertsimas, Tsitsiklis (1997), *Introduction to Linear Optimization* — (no DOI/URL)
  - [manuscript] quantum-observable-universe/particle-interactions/lp-dual-stability.md
- **Tractability:** Feasibility + dual-bound |y_star| ≤ κ_G·t stability; LP duality (dual bound) Mathlib lacks.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.

---

## 2026-08-22 — before formalizing this, read: the narrative's own table does not follow from its witness

Surfaced by `agent:p02` on the nuclear-interactions trap-drain and **re-measured
independently in the coordinating session**. This is not a Lean problem — the
Lean statement above is fine — but it changes what clause 3 is supposed to be
*true of*, so it belongs here rather than in a drive-by commit.

Setup, all three inputs taken from the corpus rather than assumed: the Gram
matrix and `q0` of
[`computations/confinement-operator-selection.witness.json`](../computations/confinement-operator-selection.witness.json)
(`q0 = 1.1099785955541805`, the **old-muon** pin), and the NF basis
`(1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀)`. Sub-units expanded by the Hecke relation
(`σ₀⁻¹ = σ₀ − h`, `σ₀² = h·σ₀ + 1`).

**Measurement 1 — `Gx` is strictly positive for every sub-unit in the table.**

| sub-unit | computed `Gx` | true `min(Gx)` | table's `Min(Gx)` |
|---|---|---|---|
| `σ₀` | `(+0.50, +1.10, +0.25, +0.55, +0.55, +0.36)` | **+0.25** | +0.12 |
| `σ₀⁻¹` | `(+0.29, +1.00, +0.14, +0.50, +0.50, +0.25)` | **+0.14** | +0.07 |
| `σ₀σ₁⁻¹` | `(+0.14, +0.32, +0.50, +0.25, +1.10, +0.55)` | **+0.14** | **−0.11** |
| `σ₀²` (Hopf) | `(+1.10, +0.73, +0.55, +0.36, +0.36, +0.63)` | **+0.36** | +0.18 |

The `−0.11` of
[`tbl:lp-dual-stability-table-data`](../content/quantum-observable-universe/nuclear-interactions/lp-dual-stability-table-data.md)
row 5 is the only negative number in the chapter and the entire evidential basis
for the confinement reading. Where it sits, the computation gives **+0.32**.
Under `def:lp-stable` that sub-unit is **LP-stable**, and the row's **No** is a
**Yes**.

**Measurement 2 — the printed rows are not `Gx`, and three of the four are wrong
in exactly the same deterministic way.** Applying the map

    (c₁, c₂, c₃, c₃/2, c₄, c₄/2)      to the true Gx = (c₁ … c₆)

reproduces the `σ₀`, `σ₀⁻¹` and `σ₀²` rows **exactly — all six entries, at the
printed two decimal places**. It deviates from the `σ₀σ₁⁻¹` row at **four of six**
positions. So the table is not four sloppy transcriptions: three rows share one
rule, and the fourth — the only **No**, the one the confinement argument rests
on — does not follow it.

I am **not** claiming to know what produced that map, and it should not be
guessed at. What is measured is that the `−0.11` is not derivable from the
witness by the rule that reproduces its three siblings exactly.

**Measurement 3 — the constants quoted alongside are also unsupported.** The
Gram spectrum is
`(−0.85506727, 0.10179668, 0.85506727, 0.85506727, 0.85506727, 3.4769499)`, so
`κ_G = 34.16` reading `λ_max/λ_min⁺`, or `4.07` reading `|λ_max|/|λ_min|` —
neither is the `≈ 7.0` quoted, and understating `κ_G` makes clause 2's dual bound
`|y*| ≤ κ_G·‖t‖` **4.9× tighter than justified**. `λ_min = −0.855067`, not the
`−0.956` of `rem:lp-dual-stability-confinement-reading`. Neither quantity appears
as a key in the witness, so both are hand-carried.

**Measurement 4 — clause 2 and the strong-duality clause have no numerical
backing at all.** Every LP-dual field in that witness is `null` — `y0_star`,
`y_star`, `active_set`, `primal_obj`, `dual_obj`, `duality_gap` — and three carry
`"STUB — re-run script through lp_dual_solver.py to populate"`. The consuming
`.ts` records `status: "verified"`. This is the AGENTS.md §"LP / SDP duals"
requirement unmet on the flagship LP witness of the chapter.

### What this means for the formalization

The `Next step` above still holds — LP duality is genuinely missing from Mathlib
and must not be laundered through an axiom or class. But **clause 3 should not be
formalized against the current narrative**: if the Lean is discharged with a
context whose `G` and `x_star` are the witness's, clause 1 (`0 ≤ Gx`) will hold
for every sub-unit in the table, including the one the paper says fails. Settle
what the table is meant to compute first — regenerate it through
`lp_dual_solver.py` so the dual fields are real — then state the Lean against
the regenerated numbers.

Worth noting for whoever does that: the recurring Gram entry `0.49932033`
(`G[0][1]`, `G[0][2]`, and six more places) is `√q/(q+1)` at this pin — the
**convention-C** Markov parameter, excised by the 2026-08-15 ruling in favour of
D (`z_D = q³/(q²+1) = 0.61269`). So the witness needs a convention pass too, not
only a dual-fields pass.

