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
| S7 | **The two-row re-posing is already named in the corpus, by the partition-indexed LP itself.** `aK_via_lp_dual_full.py:231-258`: *"under convention D the `ℓ(λ) ≥ 3` blocks vanish identically, so this LP needs re-posing on the two-row quotient"* — and it deliberately does **not** repair it, emitting `null` rather than "manufacture an `a_K` the data does not support". Bean `qou-u2jg`; consequence tracked on `qou-8na1`. | stated, not done |

**S7 is why O3′ below is not a new idea.** It is the same re-posing, reached
from the SDP side by a falsifier rather than from the `a_K` side by a guard —
an independent arrival at a route the corpus had already named and declined to
take unilaterally. Cite it; do not present the quotient as novel.

**S4 is the load-bearing one for this decision**: it forecloses the entire class
"keep the LP, change the linear objective". S6 is what bounds the blast radius —
the numbers survive; the *reading* is what fails.

---

## 3. What is newly measured here — an index-set mismatch, and a type error

### 3.1 The LP the proposition NAMES is not partition-indexed — but a partition-indexed one does exist elsewhere

> **🛑 CORRECTED 2026-09-05, before this proposal was acted on.** This section
> was headed *"There is no partition-indexed LP"* and asserted that the object
> the gate takes a dual of *"is not in either program"*, extended to the whole
> corpus. **That is false, and it failed for the documented reason: I surveyed
> `content/` and did not run the corpus-grep checklist over `computations/`
> (path 3) or `.beans/` (path 6).** Both hold the counter-example. What
> survives is a narrower claim, stated below.

The two *content-block* programs index their Frobenius positivity constraints
by **NF basis element**:

- `prop:operator-selection-lp`: `Σ_j G_ij x_j ≥ 0 ∀ i ∈ {1..d}`, `d = n!`
- `prop:confinement-lp`: the same, `i ∈ {1..6}` for `H₃(q)`

`prop:mass-coefficient-shadow-price` claims the dual of *"the corresponding
**partition's** Frobenius positivity constraint in the nuclear operator
selection LP"*, and `lp_shadow_price(partition)` and the Pass-2 gate are both
**per-partition**. At `n = 3` that is **6 constraints against 3 partitions**.
So the LP the proposition *names* cannot supply the object it claims.

**A partition-indexed LP does exist, in compute, and the proposition does not
cite it.** [`computations/aK_via_lp_dual_full.py`](../../computations/aK_via_lp_dual_full.py)
poses exactly the program the proposition needs — its own header states it:

```
Basis: Wedderburn projectors {π_λ : λ ⊢ n}
t_λ     = w_λ · χ^λ(W_atom)
G_λλ'   = w_λ · δ_λλ'            (block-diagonal Frobenius Gram)
n_target = |tr_M(W_atom)|
```

Its committed witness `a-K-via-lp-dual-full.witness.json` carries per-partition
duals (`per_partition[i].u_lambda_star`), and `len(y_star)` is **3 / 11 / 30**
at `n = 3 / 6 / 9` — exactly `p(n)`, not `n!`. At `H₃`, proton:
`y*_[3] = y*_[2,1] = 1.0`, `y*_[1,1,1] = 0`.

**So the corrected finding is an ambiguity, not an absence**, and it is still
substantive: two inequivalent programs in this corpus are both called "the
operator-selection LP", one indexed by `n!` basis elements and one by `p(n)`
partitions; `prop:mass-coefficient-shadow-price` cites the first by label while
making a claim only the second could support; and nothing reconciles them.
`hecke_core_legacy.lp_shadow_price` — the function the binding gate actually
calls — implements **neither**: it returns `w_λ/d_λ − 1/[k]_q!` in closed form
and solves no program at all.

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

## 7. FALSIFIER RUN — it fires, and points at its own repair

The test in §8 was run before any content was committed to O3. **It fires**, by
a mechanism I had not predicted, which is why the result is constructive.
Probe: [`computations/probes/sdp_o3_falsifier_probe.py`](../../computations/probes/sdp_o3_falsifier_probe.py), 6/6.

**What O3 does fix.** The LP's S1 defect genuinely does **not** reproduce. All
six LP-optimal vertices are excluded by the PSD constraint, and not marginally:

| vertex | min eigenvalue | |
|---|---|---|
| `(1,2,3)`, `(1,2,4)` | **−7.3286461578** | excluded |
| `(1,3,5)`, `(1,4,5)`, `(2,3,5)`, `(2,4,5)` | **−3.85251717557** | excluded |

**What breaks instead.** Solving for the Markov weights from the six basis
traces — 6 equations, 3 unknowns, so consistency *is* the validation (residual
8.02e-17, `Σ y_λ d_λ = 1.0` exactly) — gives

| λ | `d_λ` | `y_λ` |
|---|---|---|
| `(3)` | 1 | 0.50540422650393 |
| `(2,1)` | 2 | 0.24729788674803 |
| `(1,1,1)` | 1 | **1.45e-17 — zero** |

That is the **SU(2) specialisation**: at convention-D `z`, the Markov weight
vanishes for partitions with more than 2 rows. A zero-weight block **does not
enter the objective at all**, so a `Φ` supported only there is PSD (1×1, entry
+1 > 0), has objective 0, and has `Σx = 0.0202 ≠ 0` — hence scales to any
`n_target`. **The SDP optimum is also identically 0, attained on a ray.**

**And the ray is already named.** It matches the corpus's known
`RADICAL = (1, −1/q, −1/q, 1/q², 1/q², −1/q³)` — the q-antisymmetriser — to a
relative spread of **6.4e-51**. That is the radical of the Frobenius form under
convention D, for which `G_PINV` / `gram_quotient_inverse` already exist.

### O3′ — the amended option

Pose the block-PSD program on the **quotient by the radical**, i.e. over the
partitions with **nonzero Markov weight** (≤ 2 rows, for SU(2)). There every
`y_λ > 0`, so PSD feasibility forces `Σ_λ y_λ tr(Φ_λ) ≥ 0` with equality only at
`Φ = 0`, which the net constraint excludes. The degeneracy is gone by
construction, and no new object is needed — the quotient is already built.

**Not novel — see S7.** `aK_via_lp_dual_full.py` states this exact repair in its
own source and declines to apply it. What the falsifier adds is *why* the
quotient is the right cut rather than one convenient one: the degenerate ray is
not merely "a block with zero weight", it is the q-antisymmetriser radical
matched to 6.4e-51, so quotienting by the radical is the canonical move and not
a choice. The two arrivals also disagree about nothing, which is worth stating:
`aK_via_lp_dual_full`'s LP has `G = diag(w_λ)`, so a zero weight makes its Gram
**singular**, and the SDP's zero-objective PSD ray is the same fact in the dual
picture.

## 8. Recommendation — my judgement, not a finding

**O2 now, unconditionally; O3′ (not bare O3) as the real work; O1/O5 declined.**

O2 is free and removes a false statement from a hot file. O3′ is the only route
that produces the object the downstream code assumes exists — a per-partition
dual — and it is motivated from both sides: the Wedderburn decomposition makes
the partition block the natural constraint unit, and the corpus's own physical
reading ("which Wedderburn blocks the bound state saturates") is block-shaped
already. The falsifier upgraded O3 → O3′ for the cost of one probe, which is
exactly what it was for.

I decline **O5**: a non-degenerate program that still cannot select is a worse
epistemic position than a visibly broken one, because it stops advertising its
own failure.

**Do not start O3′ expecting it to fix the sign.** S4 and the relative-interior
finding say the feasible geometry does not distinguish `𝓑₃`, and re-posing the
program does not touch that. The honest expectation is that O3′ fixes the **type
error** and leaves selection open.

## 9. O3′ FALSIFIER RUN — not falsified

The check §7 left open — *is every surviving weight strictly positive at n > 3?*
— was run. Probe:
[`computations/probes/sdp_o3prime_weight_positivity_probe.py`](../../computations/probes/sdp_o3prime_weight_positivity_probe.py), 5/5.

| n | partitions | > 2 rows | all zero | ≤ 2 rows | all > 0 | min surviving `y_λ` |
|---|---|---|---|---|---|---|
| 3 | 3 | 1 | ✓ | 2 | ✓ | 0.2472978867 |
| 6 | 11 | 7 | ✓ | 4 | ✓ | 0.0151238101 |
| 9 | 30 | 25 | ✓ | 5 | ✓ | 0.003740086277 |
| 12 | 77 | 70 | ✓ | 7 | ✓ | 0.0002287296319 |

At every `n` from 3 to 12: the > 2-row partitions vanish **exactly**, every
survivor is **strictly positive**, and `Σ_λ y_λ f^λ = 1` throughout.

**Both halves are provable, and the measurement agrees with the proofs.** The
vanishing is structural — `schur_principal_sym`'s own note: for a shape with
more than `N` rows the cell `(N+1, 1)` has content `−N`, so the numerator picks
up `[N + (−N)]_q = [0]_q = 0`. The positivity likewise: for a ≤ 2-row shape the
minimum content is `−1`, so every numerator factor is `[m]_q` with `m ≥ 1` and
every hook is `≥ 1`, both positive at `q > 1`.

**Cross-validation, and it is the strong part.** At `n = 3` the hook-content
product formula gives `(3) 0.50540422650393`, `(2,1) 0.24729788674803`,
`(1,1,1) 0` — matching **to all 14 digits** the weights the O3 falsifier solved
*independently*, by linear system from the six Markov basis traces. Two
unrelated routes, same answer.

**One numerical caveat, not structural.** The minimum surviving weight decays by
a factor **0.2473 per +2 in n** (0.2473 at n = 3 → 0.000229 at n = 12). It stays
strictly positive, but a program solved in float64 at large `n` would eventually
be unable to distinguish it from zero. The accumulator's `k_max = 11` sits at
**9.2e-4**, comfortable; anything reaching `n ≳ 30` would need care.

**So O3′ stands.** Both falsifiers this proposal wrote for itself have now been
run: one killed bare O3 and produced O3′, the other cleared O3′.

## 9b. OWNER RULING 2026-09-05 — O2 and O3′ both chosen; O2 applied, O3′ begun

The author picked **1 and 2** from the options put to them: O2 (fix the
documentation) and O3′ (re-pose as the block SDP on the radical quotient).
O1/O4/O5 not chosen.

**O2 is applied.** Six sites, no number moved. The corrected statement is that
`y_0 = 1/[k]_q!` is `min_λ(w_λ/d_λ)` — a weight normalisation — and not the
dual of any normalisation constraint; the actual net-constraint dual of
`prop:operator-selection-lp` is identically zero. Two content blocks
(`mass-coefficient-shadow-price`, `knot-operator-energy`), one Lean docstring,
three sites in `hecke_core_legacy.py`. Content validate exit 0; `lean`-direct
exit 0. `shell-closure-stability.md` carries the same *shape* of claim about the
**confinement** LP and was deliberately left — that is a different program and
deciding it is a measurement, not a doc fix.

**O3′ is begun, formalize-first.**
[`QOU/MassTheory/BlockSDPNondegeneracy.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/BlockSDPNondegeneracy.lean)
— five declarations, `lean`-direct exit 0, `#print axioms` clean on all five
(`propext, Classical.choice, Quot.sound`; no `sorryAx`):

| declaration | what it settles |
|---|---|
| `obj_pos_of_pos_weights` | On the quotient, **every** feasible point has strictly positive objective — no zero-objective ray, so no degenerate optimum. |
| `exists_zero_obj_of_zero_weight` | The O3 falsifier as a theorem: **one** vanishing weight suffices to restore the degeneracy at any target. The positivity hypothesis is load-bearing. |
| `feasible_smul` | The value is homogeneous of degree one in `n_target` — the property the LP provably lacks. |
| `trace_nonneg_of_posSemidef` | The bridge from `Φ_λ ⪰ 0`, built on the corpus's own `QOU.MathlibExt.PosSemidefTraceZero`. |

**Still not proved, and the file says so:** that O3′ *selects*. S4 is untouched
by re-posing. Non-degeneracy buys a well-defined optimal value that responds to
the target; uniqueness of the minimiser stays open. The remaining O3′ work is
the compute — re-posing the actual program on the quotient and recomputing —
which has not been started.

---

## 9d. 🛑 CORRECTION TO §9c — the selection is ATOM-INDEPENDENT (PR #6841)

§9c below reads O3′'s selection as the corpus's physical framing — *"which
Wedderburn blocks the bound state actually saturates"*. **That reading is
wrong.** Measured after #6752 merged:

The objective factors as `t_λ = w_λ · χ^λ(W_atom)`, where `w_λ` depends only on
the partition and `q` — identical for every atom at a given `n` — and `χ^λ` is
where all atom-dependence lives. **argmin(`t`) = argmin(`w`) in 6 of 6 rows**:
the character never moves the selection. Corroborated directly: two atoms at
`n = 3` and two at `n = 9` give the **same block** with **different prices**.

- **The pricing result STANDS.** `y_0*` is nonzero and atom-dependent, where the
  full LP has `y_0* = 0` identically. That was the defect O3′ repairs.
- **The selection is a function of `n` alone.** At fixed `n` it is the same block
  for the proton, the neutron and every other atom, so it is not "the block
  *this* bound state saturates".

**And the obvious explanation is refuted too.** Spread dominance (`w` varies more
than `χ`) holds at `n = 6` and **fails at `n = 9`**, where χ-spread 6.448×/6.712×
exceeds w-spread 5.915× and the argmin is unmoved anyway. The mechanism is left
**open**; the probe asserts the refutation rather than a replacement guess.

Probe: `computations/probes/o3prime_selection_is_atom_independent_probe.py`, 4/4.

---

## 9c. 🛑 O3′ APPEARS TO SELECT — correcting my own §8 recommendation

> **Superseded in part by §9d above**: the selection is real but
> **atom-independent**, so the physical reading in this section is withdrawn.
> The pricing result and the uniqueness measurement below are unaffected.

§8 says *"do not start O3′ expecting it to fix the sign … the honest expectation
is that O3′ fixes the **type error** and leaves selection open."* The first half
stands. **The second half looks wrong, and it is cheap to check.**

**The reduction.** Under the natural lift of the scalar per-block coefficient to
a matrix — `T_λ = t_λ · I`, which is what makes the existing scalar program a
special case of the block SDP — the O3′ program

```
min  Σ_λ ⟨T_λ, Φ_λ⟩   s.t.   Σ_λ tr(Φ_λ) = n_target,   Φ_λ ⪰ 0   (λ surviving)
```

reduces to a **scalar LP in the traces**, `min Σ_λ t_λ τ_λ` s.t. `Σ τ_λ =
n_target`, `τ_λ ≥ 0`. Its optimum puts all trace on `argmin_λ t_λ`. **That is a
selection, provided the argmin is unique.**

**Measured** over every row of `a-K-via-lp-dual-full.witness.json`, restricted
to surviving blocks (`w_λ ≠ 0`):

| row | n | survivors | argmin block | `t_min` | gap to runner-up | unique |
|---|---|---|---|---|---|---|
| 0 | 3 | 2 | (2,1) | 0.4470411475 | 56.3 % | yes |
| 1 | 3 | 2 | (2,1) | 0.4206261579 | 34.8 % | yes |
| 2 | 6 | 4 | (3,3) | 0.06426714922 | 19.9 % | yes |
| 3 | 9 | 5 | (5,4) | 0.01654969522 | 110.8 % | yes |
| 4 | 9 | 5 | (5,4) | 0.02878684856 | 84.0 % | yes |
| 5 | 12 | 7 | (6,6) | 0.004682720982 | 104.9 % | yes |

**Unique in all six, by a wide margin** — the smallest gap is 19.9 %, so this is
not a near-tie that numerical noise could flip.

**What is selected, precisely, and what is not.** The **block** (the support) is
determined; the **operator** is not — any `Φ_λ ⪰ 0` on that block with the right
trace is optimal, so a `d_λ × d_λ` family remains. That is weaker than "selects
`Φ*`" and stronger than "selects nothing", and it is exactly the content the
corpus's own physical reading asks for: *"the active demand channels identify
which Wedderburn blocks the bound state actually saturates"* (AGENTS.md,
§LP/SDP duals).

**This does not contradict S4.** S4 excludes a linear objective selecting `𝓑₃`,
an **operator**, on the NF-indexed polyhedron where `𝓑₃` is relative-interior.
Block selection on the quotient is a different question, and O3′ answering it
does **not** deliver `𝓑₃` — S4's exclusion stands at the operator level.

**Observed pattern, offered as an observation and not a claim:** the selected
block is the **near-square two-row partition** at every n — (2,1), (3,3), (5,4),
(6,6). Six points is not enough to assert a rule; it is enough to say what to
test first.

### Caveats that keep this honest

- **It is the reduction that was measured, not a solver run.** No SDP was
  solved. The measurement is `argmin t_λ` over committed data; the claim that
  this *is* the optimum rests on the reduction above and on
  `obj_pos_of_pos_weights`.
- **The lift `T_λ = t_λ·I` is an assumption**, the natural one, and a different
  lift (a genuinely matrix-valued `T_λ`) need not reduce this way. Whoever
  builds the compute should state which lift they implement.
- **`t_λ > 0` on survivors is measured, not derived** — see the note in
  `BlockSDPNondegeneracy.lean`.

Reproduce:

```sh
python3 -c "import json;from mpmath import mp;mp.dps=30;\
d=json.load(open('computations/a-K-via-lp-dual-full.witness.json'));\
[print(sorted([(p['partition'],mp.nstr(mp.mpf(p['contribution']),10)) \
  for p in r['per_partition'] if mp.mpf(p['y_lambda'])!=0], \
  key=lambda t:mp.mpf(t[1]))[:2]) for r in d['data']['rows']]"
```

---

## 10. What is not claimed

That O3′ **selects** `𝓑₃` or anything else. The scope-(b) exclusion (no linear
objective selects `𝓑₃`) and the relative-interior finding concern the feasible
geometry and are untouched by re-posing the program. That the gate is *wrong* —
only that its justification is disproved and its type is inconsistent with either
program. That any number changes: per S6 the mass coefficients come from the
chirality/writhe/ribbon route in closed form.
