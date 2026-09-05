# Replacing the operator-selection objective: options, motivation, blast radius

**Date:** 2026-09-05 · **Beans:** `qou-sv7h`, `qou-v7qj` · **Status:** options for
the author; **no replacement is chosen here**.

`6b7d2ec4a8` proved the operator-selection LP degenerate and deliberately
proposed no replacement — *"choosing one is a decision about the physics."* This
document is the groundwork for that decision: what is already settled, what is
newly measured, what the LP and the physics motivate, and what each option costs.

---

## 1. What is being decided, and why it now matters more

Two things read the LP's optimum and its duals:

- **`prop:mass-coefficient-shadow-price`** — the *interpretation* of the mass
  coefficients as LP duals;
- **`unified_iterative_correction`** — `lp_shadow_price` (the per-partition
  weight `y_λ`) and the **Pass-2 gate** (keep partitions with `tr(M_λ) ≤ 0`).

The second is why this is urgent now.
[`2026-09-05-uic-sign-forced-by-gate.md`](../audits/2026-09-05-uic-sign-forced-by-gate.md)
measures that **the Pass-2 gate is what forces `binding_energy < 0`**, and the
same near-constant gated-set size explains the A-independence. So the wrong sign
that `qou-sv7h` has been chasing traces to a gate whose justification is the
thing `6b7d2ec4a8` disproved.

---

## 2. What is already settled — cite, do not re-derive

From [`2026-08-24-operator-selection-lp-objective-defect.md`](../audits/2026-08-24-operator-selection-lp-objective-defect.md)
and `6b7d2ec4a8`:

| # | Result | Status |
|---|---|---|
| S1 | `b₁ = 𝟏` ⇒ `G[1][j] = t_j`: the first Frobenius row **is** the objective. The program minimises `t·x` s.t. `t·x ≥ 0`, so the optimum is **identically 0**. | proved, all `n`, all `q`, all conventions |
| S2 | By strong duality `n_target·y_0* = 0` with `n_target > 0` ⇒ **`y_0* = 0`**. | proved |
| S3 | The argmin is a **positive-dimensional face** — six vertices at `n=3`, in mirror pairs; the returned vertex is a pivoting artefact. | proved |
| S4 | **No linear objective selects `𝓑₃`.** It is relative-interior (all six constraints strictly slack), and a linear functional minimised at a relative-interior point is constant on the polyhedron. | **scope-(b) structural exclusion** |
| S5 | Minimum-norm and maximum-min-slack both fail — the uniform point beats `𝓑₃` on both. | measured |
| S6 | The six-term mass formula does **not** run on the LP. Its coefficients come from the chirality/writhe/ribbon route in closed form (`C_[3,2,1] = [2][4][6]h / (2[3]³[5])`). The shadow-price reading is a parallel interpretation, not the derivation. | measured |

**S4 is the load-bearing one for this decision**: it forecloses the entire class
"keep the LP, change the linear objective". S6 is what bounds the blast radius —
the numbers survive; the *reading* is what fails.

---

## 3. What is newly measured here — an index-set mismatch, and a type error

### 3.1 There is no partition-indexed LP

Both programs index their Frobenius positivity constraints by **NF basis
element**:

- `prop:operator-selection-lp`: `Σ_j G_ij x_j ≥ 0 ∀ i ∈ {1..d}`, `d = n!`
- `prop:confinement-lp`: the same, `i ∈ {1..6}` for `H₃(q)`

But `prop:mass-coefficient-shadow-price` claims the dual of *"the corresponding
**partition's** Frobenius positivity constraint"*, and `lp_shadow_price(partition)`
and the Pass-2 gate are both **per-partition**. At `n = 3` that is **6
constraints against 3 partitions**. The object the gate takes a dual of is not
in either program.

### 3.2 The natural bridge makes it a *matrix*, not a scalar

`H_n(q) ≅ ⊕_λ M_{d_λ}`, so the `n!` scalar constraints group into partition
blocks of size `d_λ²`:

| n | partitions | `d_λ` | `d_λ²` | Σ |
|---|---|---|---|---|
| 3 | 3 | 1, 2, 1 | 1, 4, 1 | 6 = 3! |
| 4 | 5 | 1, 3, 2, 3, 1 | 1, 9, 4, 9, 1 | 24 = 4! |
| 5 | 7 | 1, 4, 5, 6, 5, 4, 1 | 1, 16, 25, 36, 25, 16, 1 | 120 = 5! |

So a *genuinely per-partition* Frobenius constraint is a **block-PSD**
constraint `X_λ ⪰ 0`, and its dual is a matrix `Y_λ ⪰ 0` of size `d_λ × d_λ` —
**not a scalar**. The program is a semidefinite one, and the corpus already has
the entry point: `pyhecke.lp_dual_solver.solve_psd_operator_selection_sdp`,
alongside the LP form (both verified present).

### 3.3 The code discards exactly the partitions where its own type is correct

A scalar shadow price is well-defined only where `d_λ = 1` — i.e. the trivial
and sign representations `(k)` and `(1^k)`, the only 1-dimensional irreps.

`lp_shadow_price` sets `y_λ = w_λ/d_λ − y_0` with `y_0 = 1/[k]_q!`, which **is**
`min_λ(w_λ/d_λ)`, so it zeroes exactly two partitions per level. Measured at
k = 2..7, **the zeroed set is identical to the `d_λ = 1` set at every k**.

> The code zeroes precisely the partitions where a scalar dual makes sense, and
> keeps the ones where the dual is a matrix.

That is not an argument that the weights are wrong by some amount; it is an
argument that the *type* is wrong, in a way that is exactly inverted.

---

## 4. Motivation from the LP

**The degeneracy has a cause, and the cause suggests the repair.** S1 holds
because the identity is in the basis, so the objective `t·x = tr_M(Φ)` coincides
with the `i = 1` constraint. Any fix must break that coincidence. Three
structural routes exist:

1. **Drop the `i = 1` constraint** — but it is the physically meaningful one
   (`tr_M(Φ) ≥ 0`, pairing with the identity), so dropping it removes content.
2. **Change the objective off the trace** — but S4 says *no* linear objective
   selects the intended answer, so this fails for the selection reading, though
   it could still yield a well-posed program with different content.
3. **Change the constraint geometry** — move from `n!` scalar constraints to
   `#partitions` block-PSD constraints. This is the only route that both breaks
   the coincidence (the objective is a scalar functional; the constraints become
   matrix inequalities, so no constraint can *be* the objective) **and** produces
   the per-partition dual the downstream code already assumes.

**The SDP route is also the one the corpus half-built.** `solve_psd_operator_
selection_sdp` exists; AGENTS.md's LP/SDP dual contract already mandates emitting
`y_star`, `active_set`, `duality_gap` for exactly this family; and
`rem:sdp-regime-switch` is a block about switching between the two.

---

## 5. Motivation from the physics

The physical reading the corpus attaches to the dual is stated in AGENTS.md:

> the dual variables ARE the binding-energy shadow prices. The active demand
> channels (`y_star[i] > 0`) are the "most receptive sub-braids" — they identify
> **which Wedderburn blocks the bound state actually saturates**.

That sentence is already partition-indexed and already block-shaped: *Wedderburn
blocks*, not basis elements. The physics wants to know which **channels** are
saturated, and a channel is a partition.

Two consequences:

- **The right object is the support/rank of `Y_λ`, not its scalar value.** A
  channel can be partially saturated — saturated in some directions of its
  `d_λ`-dimensional block and slack in others. A scalar `y_λ` cannot express
  that; `rank Y_λ ∈ {0, …, d_λ}` can. The `Δ_λ = (−1)^{n(λ)}·dim V_λ` result
  (proved, general-`n`) is *already* dimension-valued, which is the same shape.
- **Confinement is naturally a PSD statement.** "The operator pairs
  non-negatively with all basis elements" is `Gx ≥ 0` entrywise, which is basis-
  dependent; "the operator is non-negative on every channel" is `X_λ ⪰ 0`, which
  is basis-independent. The second is the invariant statement, and confinement
  ought to be invariant.

**Counter-motivation, stated honestly.** None of this says an SDP *selects* `𝓑₃`
either. S4 excludes linear objectives; it does not establish that a semidefinite
one succeeds, and the audit's finding that `𝓑₃` is not distinguished by the
feasible geometry **at all** ("whatever selects it is topological or physical")
applies to any program over that same feasible set. Re-posing as an SDP changes
the *type* of the dual — which is what the downstream code needs — without any
guarantee that it fixes selection.

---

## 6. The options

### O1 — Do nothing
- **Means:** the LP stays degenerate; the shadow-price reading stays disproved in
  the blocks and un-corrected in the code; the sign stays wrong.
- **Costs:** none now.
- **Risks:** `lp_shadow_price`'s docstring keeps asserting a disproved
  identification, and the next agent re-derives this. The binding sign stays
  unexplained-in-practice even though the mechanism is now known.
- **Commits to:** nothing.
- **This is the default if you say nothing.** It is safe — S6 means no published
  number moves — but it leaves a known-false docstring in a hot file.

### O2 — Correct the documentation only
- **Means:** fix `lp_shadow_price`'s docstring (`y_0` is a normalisation choice,
  not the LP's `y_0*`, which is proved 0), and note in Pass 2 that the
  complementary-slackness justification does not survive `6b7d2ec4a8`.
- **Costs:** an hour; no number moves.
- **Risks:** none — it is strictly a truth repair.
- **Commits to:** nothing; compatible with every other option.
- **Downstream:** none.

### O3 — Re-pose as the partition-block SDP
- **Means:** replace the `n!` scalar Frobenius constraints with `#partitions`
  block-PSD constraints; the dual becomes `Y_λ ⪰ 0` per partition. Use the
  existing `solve_psd_operator_selection_sdp`.
- **Costs:** substantial. A new content block (the program is different
  mathematics, not a restatement), its proof block, Lean, and a re-derivation of
  what `unified_iterative_correction` should read off `Y_λ` — `tr Y_λ`? `rank`?
  a specific eigenvector? That last choice is itself a physics decision.
- **Risks:** the numbers move. Every binding number becomes provisional until it
  lands. And S4's warning applies: this may still not *select* anything.
- **Commits to:** the SDP reading of confinement, which is a real framework
  commitment.
- **Downstream:** `prop:mass-coefficient-shadow-price` and its five citing
  blocks get a *correct* object to point at; the Pass-2 gate gets a principled
  replacement; AGENTS.md's LP/SDP dual contract already covers the witness
  fields.

### O4 — Demote the LP to a verification certificate, and source the gate elsewhere
- **Means:** accept the audit's "constructive residue" — `𝓑₃` is *strictly*
  feasible with min slack `0.342489`, which is a genuine robustness certificate
  — and stop reading the LP as a selection principle. Then `unified_iterative_
  correction` needs a different justification for which partitions contribute.
- **Costs:** moderate in code, large in narrative: something must replace the
  gate, and the honest interim is *no gate* (all partitions contribute).
- **Risks:** removing the gate changes every binding number, and — per the
  measurement in `uic_gate_justification_disproved_probe` — widening the
  contributing set made the sign **more** negative, not less. So this does not
  fix the sign either.
- **Commits to:** giving up LP-based selection.
- **Downstream:** the same five interpretive blocks, but they lose the reading
  rather than gaining a corrected one.

### O5 — Keep the LP, fix only the vacuity
- **Means:** break the objective/constraint coincidence minimally — e.g. drop
  the `i = 1` constraint, keeping the other `n!−1`.
- **Costs:** small.
- **Risks:** **S4 still applies.** The optimum stops being identically 0, but no
  linear objective selects `𝓑₃`, and the argmin's mirror symmetry argument is
  untouched. This buys a non-degenerate program that still does not do the job,
  which is arguably worse than an obviously broken one.
- **Commits to:** little, but it may look like a fix while not being one.

---

## 7. Recommendation — my judgement, not a finding

**O2 now, unconditionally**, and **O3 as the real work**, with O1/O5 declined.

O2 is free and removes a false statement from a hot file; nothing about it
forecloses anything. O3 is the only route that produces the object the
downstream code already assumes exists — a per-partition dual — and it is
motivated from both sides: the Wedderburn decomposition makes the partition
block the natural constraint unit, and the corpus's own physical reading
("which Wedderburn blocks the bound state saturates") is block-shaped already.

I would decline **O5**: a non-degenerate program that still cannot select is a
worse epistemic position than a visibly broken one, because it stops advertising
its own failure.

I would not start O3 expecting it to fix the sign. S4 and the relative-interior
finding say the feasible geometry does not distinguish `𝓑₃`; the honest
expectation is that O3 fixes the **type error** and leaves selection open.

## 8. What would falsify each direction

- **O3 is wrong if** the block-PSD program is *also* degenerate — e.g. if some
  block constraint again duplicates the objective. That is checkable cheaply
  before any content lands: build `G` in the Wedderburn basis at `n = 3` and see
  whether the objective functional is in the span of the block constraints.
- **The whole SDP direction is wrong if** the physics wants a scalar per channel
  after all, in which case the `d_λ = 1` coincidence in §3.3 is telling us the
  framework only ever meant the trivial and sign channels — and the code has it
  exactly backwards.

## 9. What is not claimed

That the gate is wrong — only that its justification is disproved and its type
is inconsistent with either program. That an SDP selects `𝓑₃`. That any number
changes: per S6 the mass coefficients come from the chirality/writhe/ribbon
route in closed form and are untouched by all of this.
