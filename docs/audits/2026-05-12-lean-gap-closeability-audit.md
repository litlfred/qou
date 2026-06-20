# 2026-05-12 — Lean gap-closeability audit

> Companion to [`2026-05-12-lean-p4-canonical-instance-review.md`](./2026-05-12-lean-p4-canonical-instance-review.md).
> Coordinates with **PR #644**.

## Purpose

After the P4 review concluded that both Phase 4 `sorry`s are §3b-cond
canonical-instance conjectural inputs (not gaps), the user asked
"continue to close gaps". This document records the audit of every
remaining `sorry` under `content/quantum-observable-universe/` and
classifies each by **closeability in the current sandbox**.

The blunt finding: **no further honestly-closeable gap was found in
this sandbox**. Every remaining `sorry` falls into one of six
categories (§§1–6 below), each of which is either
- explicitly out-of-bounds per AGENTS.md §3b-cond (trivial-skeleton
  rejected),
- structurally unprovable as written (would require restating the
  manuscript claim, which is an author decision, not an agent edit),
- a `sorry` BY DESIGN whose existing comment notes that closing
  under the current bound would require `False`,
- an open mathematical problem,
- a Mathlib-analysis / category-theory proof that requires the Lean
  toolchain to validate (not installed in the sandbox), or
- a long polynomial-identity case-split that would equally need
  toolchain validation.

This audit is intended for the **next agent with Lean toolchain
access** to prioritise without re-walking the same ground.

---

## §1. §3b-cond canonical-instance conjectural inputs

Per **AGENTS.md §3b-cond**:

> The class instance is the only `sorry` in the entire downstream
> chain.

A `sorry` inside a `class … canonical` (or analogous) instance IS the
conjectural axiom. It is **not** a discharge-eligible proof gap.
Discharging it via trivial-skeleton picks (specialising `α := Empty`,
pinning `M := canonical`, `≡ 0`, `Empty.elim`, etc.) silently drops
the conjectural content and is rejected by
`content/pipeline/trivial-skeleton-audit.ts` per the upgrade-pattern
taxonomy in
[`docs/audits/2026-05-08-trivial-skeleton-workplan.md`](./2026-05-08-trivial-skeleton-workplan.md).
Patterns A/B/C in that workplan describe content-bearing canonical
upgrades; trivial discharges do neither.

**Examples** (non-exhaustive — pattern is canonical class instances
across `braids-and-knots/`):

| File | Line | Class |
|---|---|---|
| `braids-and-knots/conj-magic-shell-stabilization.lean` | 535 | `MagicShellCrossCoupling.canonicalCrossCoupling` (P4.B) |
| `braids-and-knots/prop-rigid-monoidal-structural-gap-invariance.lean` | (canonical instance) | `RigidMonoidalStructuralGapInvariance.canonical` (P4.A) |
| Other `braids-and-knots/conj-*.lean` and `braids-and-knots/prop-*.lean` files following the same canonical-instance pattern | — | — |

**Status:** **not closeable here.** Long-term upgrade is pattern A/B
in the trivial-skeleton workplan (e.g. `MarkovTraceAxiomatic` Mathlib
typeclass for P4.A; substrate-derived `Δ_shell` data instance for
P4.B). Both require upstream infrastructure not yet landed.

---

## §2. Free-field uniqueness with no constraint axiom

These theorems claim `Subsingleton X` or `e₁ = e₂` for two
inhabitants of a structure `X` whose underlying field is a bare `ℕ`,
`H`, etc., with no axiom forcing it to be determined by the other
fields. The claim is **structurally unprovable as written** —
two inhabitants can share every other field but differ in the bare
field.

In several cases the file already carries a **DIAGNOSTIC** comment
documenting this:

> The `Subsingleton` claim is too strong. The underlying structure
> carries free fields (parameters / morphisms / opaque functions)
> that admit distinct valid values, so two instances need not
> coincide. To recover a meaningful uniqueness claim, sharpen with
> a constraining hypothesis (fixing the carrier object, fixing the
> substrate parameter, or quantifying over a quotient by structural
> equivalence) — see `frobenius-pairing-unique.lean` for the pattern.
> Sorry retained with this diagnosis rather than closed-as-stated.

**Examples:**

| File | Line | Issue |
|---|---|---|
| `quantum-observable-universes/categorical-q-connection-unique.lean` | 41 | `Subsingleton (CategoricalQConnection C)`; carrier has free fields. |
| `quantum-observable-universes/q-resolvent-unique.lean` | 34 | `Subsingleton (QResolvent H)`; same diagnostic. |
| `quantum-observable-universes/q-exponential.lean` | 64 | `QExponential.unique`: same `D_q` ⇒ same `e_q` — but `D_q` can have many fixed points (header explicitly calls this a "Conjecture — depends on non-degeneracy of the flow equation on grouplikes"). |
| `quantum-observable-universes/categorical-laplace-transform-exists.lean` | 28 | Reverse direction: existence requires constructing a `CategoricalLaplace A` whose `monoidal_unit : ∀ one, transform one s = one` quantifies over all `one : A → A`, forcing `transform = id` modulo `s`; then `monoidal_mul` quantifies over all `q_conv`, requiring `q_conv = (∘)` for arbitrary `q_conv` — false. Structurally inconsistent under `[Nonempty A]`. |
| `braids-and-knots/confinement-level-unique.lean` | 29 | `L₁.level = L₂.level` from matching `braidIndex, nStrands, q` — but `level : ℕ` is a bare field on `ConfinementLevel`. |
| `braids-and-knots/dressed-particle.lean` | 61 | `dressComposition`: `P₂.level = P₀.level` from bare-equality alone — `level : ℕ` is a bare field. |

**Status:** **not closeable here.** Restating the theorem would
change the manuscript claim and is an author decision, not an agent
edit.

---

## §3. `sorry` BY DESIGN / false-as-stated

These theorems carry an existing `sorry` whose accompanying comment
notes that closing it under the current statement would derive
`False`, or whose universal quantification is too broad and the
statement is genuinely false on part of the parameter space.

**Examples:**

| File | Line | Note |
|---|---|---|
| `braids-and-knots/partition-sum-proton-residual.lean` | 111 | Comment: *"Until one of (a)–(c) is taken, this remains `sorry` BY DESIGN — closing it under the current bound would require False, since the same witness-axiom strategy used for the neutron case would here yield a contradiction (the same proof pattern would prove the negation)."* |
| `observations/double-slit-massive-pattern.lean` | 95 | Statement requires `fringe_spacing 1 < envelope_width q` for arbitrary `q ≠ 0, q ≠ 1`. With `q = 0.5`: `q² = 0.25`, `(1 − q⁻¹)² = 1`, so RHS coefficient is `0.25 (1 + r)`; for `r > 0` small (allowed by `hr : 0 < ratio_Reeb_spatial`), the inequality fails. Statement holds for `q > 1` only. |
| `braids-and-knots/transfer-matrix-level-independence.lean` | 81 | `transfer_matrix_path_independence`: hypothesis is `h_isotopy : True` (placeholder), conclusion is arbitrary `transferMatrix1 = transferMatrix2` for two `R_q`. False. |
| `braids-and-knots/transfer-matrix-level-independence.lean` | 68 | `transfer_matrix_level_independence`: claim is `constituentProduct = compositePolynomial` for arbitrary `H : HadronConfig`, but the structure has the two as independent free `R_q` fields. False without an additional axiom on `HadronConfig`. |

**Status:** **not closeable here.** Closing would require either
restating the manuscript claim, demoting `theorem` → `conjecture`, or
adding a new axiom to the data-carrying structure.

---

## §4. Open mathematical problems

The claim itself is an open or deep theorem — not a tactic-massage
gap.

**Examples:**

| File | Line | Theorem |
|---|---|---|
| `algebraic-substrate/macroscopic-stability-equivalence.lean` | 66 | `macroscopic_iff_rh` — the prime-number-theorem optimal-error ↔ Riemann hypothesis equivalence (von Koch 1901). |
| `algebraic-substrate/macroscopic-stability-equivalence.lean` | 78 | `rh_iff_persistence` — RH ↔ spectral persistence under `q → 1`. |
| `algebraic-substrate/tannaka-krein-isomorphism.lean` | 38 | `Nonempty (RepLoc ≃ ComodH)` between two opaque axiomatised types with no further axioms — no possible witness without restating in terms of an actual fibre functor. |
| `braids-and-knots/knot-particle-correspondence.lean` | 34 | `Function.Bijective markovTraceMap` where `markovTraceMap` is `axiom`. Bijectivity of an opaque function between opaque types is not provable. |

**Status:** **not closeable here.** Open / requires deep
infrastructure.

---

## §5. Mathlib analysis / topology / category-theory infrastructure

The proof is in principle finite but requires Mathlib infrastructure
(filter limits, polynomial continuity, category-theory equivalences,
adjoint identities) that needs the Lean toolchain to author and
validate. The sandbox does not have a Lean toolchain (per
[`scripts/session-status.sh`](../../scripts/session-status.sh) and
the toolchain pin in
[`lean-toolchain`](../../lean-toolchain)), so an attempt would be
unverifiable.

**Examples:**

| File | Line | Required infra |
|---|---|---|
| `braids-and-knots/q-casimir.lean` | 781 | `qNumberSym_classical_limit`: `Tendsto (fun q ↦ (q^n − q^(−n))/(q − q⁻¹)) (𝓝[≠] 1) (𝓝 n)`. Needs `Polynomial.eval_geom_sum` + `Polynomial.continuous_eval` chain. |
| `braids-and-knots/q-momentum.lean` | 120 | `single_term_limit`: same family. |
| `algebraic-substrate/substrate-self-duality.lean` | 57 | `IsIso (selfDualityMorphism S)`: rigorous categorical zig-zag from `snake_left` / `snake_right`. |
| `quantum-observable-universes/q-codifferential-formula-prop.lean` | 140 | Adjoint-identity composition from `d_q_decomposition` + axiomatised adjoint pairs. |
| `algebraic-substrate/explicit-formula.lean` | 73, 104 | Explicit formula manipulations. |
| `algebraic-substrate/hasse-weil-bound.lean` | 43, 59, 74 | Hasse–Weil over function fields. |

**Status:** **needs toolchain.** Tractable for an agent with
`lake build` access.

---

## §6. Concrete polynomial identities (long case-split)

Finite mechanical computations whose proof is a long expansion
(`Finset.sum_range_succ` × N, then `ring`). Without `lake build` to
validate, the risk of subtle errors is high.

**Examples:**

| File | Line | Expansion length |
|---|---|---|
| `braids-and-knots/markov-trace-antipode-polynomial-symmetry.lean` | 119 | 21 case-splits via `Finset.sum_range_succ`; existing comment fully sketches the human-readable justification but defers the elaboration as "a routine exercise that does not change the categorical content". |
| `braids-and-knots/q-casimir.lean` | 644, 653, 668, 670 | Ring-normalisations inside `QCasimir_comm_E`; multiple intermediate identities (`h1`, `h2`, `hWE`) already established but the final assembly is non-trivial. |
| `braids-and-knots/q-casimir.lean` | 681 | `QCasimir_comm_F`: parallel to `QCasimir_comm_E` via `E ↔ F` involution. |

**Status:** **needs toolchain.** Tractable for an agent with
`lake build` access; not safe to attempt without.

---

## Recommendations for the next agent

1. **Do not** attempt to close §1 sorries by trivial-skeleton picks
   — that is the exact pattern rejected by the trivial-skeleton
   audit pipeline, and re-introducing it would silently drop
   conjectural content. Pursue patterns A/B/C from
   `2026-05-08-trivial-skeleton-workplan.md` instead.
2. **Do not** "close" §2 or §3 sorries by changing the statement —
   that is an author decision (manuscript-level change), not an
   agent edit. Demote to `conjecture` only with author confirmation.
3. **§4** is genuinely out of scope.
4. **§5 and §6** are the **honestly-closeable backlog** for an agent
   with Lean toolchain access. Start with §6 (mechanical polynomial
   identities — lowest infrastructure cost). For §5, prefer the
   `lean_multi_attempt` / `lean_goal` MCP tools per AGENTS.md
   "Use MCP tools, not shell commands".

## Appendix — sandbox capability note

This audit was produced in a sandbox without `lake`, `elan`, or any
Lean toolchain installed. An attempt to write tactic-level proofs
without `lake build` validation would be unverifiable and is a
known anti-pattern (per the round-trip in
[`2026-05-12-lean-p4-canonical-instance-review.md`](./2026-05-12-lean-p4-canonical-instance-review.md)
where trivial-skeleton discharges were committed and then reverted).

The right next step is to **rerun this gap-closure pass on a
toolchain-enabled environment** (e.g. via the `lean_setup` MCP tool
described in AGENTS.md "Lean MCP server" section), starting with the
§6 polynomial identities.
