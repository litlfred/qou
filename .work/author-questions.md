# Author Questions — Meat-Adding Pass Analysis

Compiled while upgrading ~250 placeholder canonicals on PR #806.
Each question has 2-4 concrete options to pick from.

## Status — After Q1 / Q2 / Q4 author selections

| Decision | Author choice | Status |
|----------|---------------|--------|
| Q1: next-pass strategy | **(B) shared typeclass infrastructure** | 4 typeclass roots committed in `QOU/Shared/`; 30 Hecke-themed blocks refactored to `extends QOU.Shared.MarkovTraceContext` |
| Q2: conjecture pattern | **be consistent with existing patterns** (= option A leave distinct) | Conjecture classes keep `class + def trivialModel` per `lean-generation.md`; provable kinds get the new shared-typeclass pattern |
| Q4: first chapter | **(A) Hecke-themed (~40 blocks)** | 30/40 refactored; 10 hand-crafted typed blocks were correctly skipped (they already have substantive typed fields) |

**Remaining work** (not started):
- LP-dual blocks (~10) → `QOU.Shared.OperatorSelectionLPContext`
- Wedderburn blocks (~15) → `QOU.Shared.WedderburnBlockDecompositionContext` (Wedderburn script ran with 0 hits — all such blocks already hand-crafted)
- Sobolev blocks (~5) → `QOU.Shared.SobolevHkRegularityContext`
- ~108 hand-crafted blocks remain with bespoke typed fields (not refactored — already have substantive content)

## Status — Backlog-exhaustion grind (2026-05-19 late evening)

After this round (38 newly-typed blocks):

- 118 files still carry abstract `: Prop` (down from 143 at session start)
- 73 commits ahead of `origin/main`
- 259 Lean files modified vs main

Most-typed identity classes covered in this round:

| Identity shape | Examples |
|----------------|----------|
| Closed-form equation | `shift = 18Z + 21N + 1`, `m_𝔋 = (q − 1)² · |q − q⁻¹| · Σ|c_w|`, `n_R = t_P = q/(q − 1) = 1/ℏ_q` |
| Inequality bound | `\|T(ρ) − ℏ_q² Δ⁽¹⁾(ρ)\| ≤ ℏ_q⁴‖ρ‖q⁻²/(1 − q⁻²)`, `‖B(v)‖ ≤ C_q‖v‖‖d_q v‖` |
| Energy / spectral law | `μ_k = [k]_q²`, `E_q(k) = C_q ε^{2/3} [k]_q^{-5/3}` |
| Matrix-product identity | Vieta `λ_+λ_− = −1`, Binet formula for `(T^n)_{ij}` |
| Move-by-move trace law | Reidemeister table (R1, R2_q, R3, far-commute, Markov-I/II) |
| `iff` characterisation | NS-blowup iff Levi-form positive, parity-mirror iff `q = q⁻¹` |
| Conditional regime | parity_regime_selection (`A` parity dispatches Q-value formula) |
| Cocycle / group law | fibre-functor atlas `g(i,k) = g(j,k) · g(i,j)` |

## Status — Backlog-exhaustion continuation (2026-05-19 evening)

19 more blocks hand-crafted with typed sub-claims in this round
(after the initial structural pass):

| Block | Chapter | Typed identity captured |
|-------|---------|-------------------------|
| `wenzl_qmn_synergy` | BraidsAndKnots | `tr_M(T_w) = z^{ℓ(w)}` + Wenzl/q-MN cross-check |
| `root_of_unity_truncation` | FluidDynamics | Bernstein bound + NS↔Levi contact-geometric iff |
| `brane_tower_q_laplacian_decay` | Observations | Geometric-tail bound `≤ ℏ_q⁴ ‖ρ‖_L² · q⁻²/(1−q⁻²)` |
| `per_nucleon_shift_additive_linearity` | BraidKnot | Closed form `shift(Z, N) = 18Z + 21N + 1` |
| `toffoli_transfer_matrix` | Information | Factorisation, antisymmetry, classical limit |
| `q_ns_wellposedness` | FluidDynamics | Energy inequality + exp spectral decay |
| `acoustic_horizon_conditions` | FluidDynamics | `ℳ = 1`, `0 < ‖∇ℳ²‖`, `0 ≤ T_{00}k^μk^ν` |
| `helicity_conservation` | FluidDynamics | `ℋ_q(t) = ℋ_q(0)` + CWF decomposition + Moffatt limit |
| `discrete_vortex_spectrum` | FluidDynamics | `λ_k = [k]_q²ℏ_q/L_q²` + intensity-level `E_j` |
| `core_levi_form` | FluidDynamics | Aspect/Levi-cond/eigenvalue bounds |
| `p1_spectral_sobolev` | FluidDynamics | Discrete-spectrum + `μ_k = [k]_q²` |
| `parity_regime_selection` | ParticleInteractions | 3 Q-value regime equations |
| `demand_stability` | ParticleInteractions | Beta-stable + shell-closed + doubly-magic |
| `ground_state_ordering` | ParticleInteractions | Interleaving + tail-pack + boundary correction |
| `strangelet_crossing_energy` | Observations | `Q = 0` + purely-strong `E_cross` + binding inequality |
| `hecke_satisfies_blitvic_hypothesis` | Observations | Hecke quadratic relation `σᵢ² = h·σᵢ + 1` |
| `parity_violation_skein` | Descartes | `(λ_sym, λ_alt) = (q, −q⁻¹)` + parity ↔ `q=q⁻¹` |
| `eos_borromean_cfl` | Descartes | Fermi-gas EOS + CFL-gap + stiffness ratio |
| `shell_structure_eigenvalues` | Descartes | Binet formula `(T^n)_{ij}` + traced volume |

**Earlier pass (PR #806):**

| Chapter | Blocks | Status |
|---------|--------|--------|
| `descartes-universe` | 17 | hand-crafted typed sub-claims |
| `braids-and-knots` (BraidKnot) | 21 | hand-crafted typed sub-claims |
| `particle-interactions` | 18 | hand-crafted typed sub-claims |
| `fluid-dynamics` | 7 | hand-crafted typed sub-claims (q-turbulence, helicity, vortex spectrum, p4-universality, q-NS, kelvin-dispersion, vorticity-lower-bound, leray-profile) |
| `fluid-dynamics` | 10 | semantic-named Prop placeholders (acoustic horizon, root of unity, ns-kummer, p1-spectral, ns-singularity, p1-nonlinear, ns-obstruction, quantum-peter-weyl, etc.) |
| All other chapters | 70 | semantic-named Prop placeholders (renamed from `holds : Prop` / `claim_i : Prop`) |

**Counts:**
- **0** generic `holds : Prop` fields remain
- **0** generic `claim : Prop` or `claim_i : Prop` fields remain
- Every Prop field carries a manuscript-themed semantic identifier
- 42 files have numbered sub-claim breakdowns
  (`claim_i_<noun>, claim_ii_<noun>, …`)
- 83 files have single semantic claims
  (`claim_<theorem_name> : Prop`)
- ~60 files have **typed** sub-claims (equations, =, ≤, etc.)

**Scripts (committed for reproducibility):**
- `.work/bulk-split-holds.py` — splits `holds : Prop` into `claim_i, ..., claim_N` based on numbered sub-claims in .md
- `.work/enrich-subclaim-docstrings.py` — extracts first-sentence summaries from .md and appends them to docstrings
- `.work/semantic-rename-claims.py` — renames `claim_i → claim_i_<noun>` based on enriched docstrings
- `.work/semantic-rename-single-claim.py` — renames `claim → claim_<theorem_name>` for single-claim files

**New skill committed:**
- `.claude/skills/local/lean-substantive-pass.md` — captures the
  three-level escalation (hand-craft / bulk-split / docstring-enrich),
  recognised manuscript patterns, type-field heuristics, and
  anti-patterns observed.

**Augmented skill:**
- `.claude/skills/local/proof-integration-watcher.md` — three new
  findings (`holds-prop-placeholder`, `claim-i-generic-docstring`,
  `mechanical-rename-without-md-check`) + auto-discharge band
  pointing at the bulk-script / lean-substantive-pass.

## Patterns observed during the pass

1. **Boxed identities** (`$\boxed{lhs = rhs}$` in .md) → captured as
   `claim_boxed : lhs = rhs` typed claim with `lhs, rhs : ℝ` abstract.
2. **Numbered sub-claim lists** (`1. ... 2. ... 3. ...`) →
   `claim_i, claim_ii, claim_iii : Prop`. Common in propositions
   with "proof has three steps" structure.
3. **Piecewise / regime-switching formulas** (`\begin{cases}`) →
   conditional sub-claims `A → B = ...`.
4. **Equivalence-relation proofs** (refl / sym / trans) →
   three `claim_refl`, `claim_sym`, `claim_trans` predicates that
   compose into `Equivalence` via Mathlib's structure.
5. **Tables of moves** (Reidemeister R1/R2/R3 / Markov-I/II) →
   row-specific sub-claims, one per move.
6. **Existence + Uniqueness** patterns → two sub-claims, often the
   uniqueness half typed (e.g. `=` on a derived field) and the
   existence half abstract.

## Q1 — How aggressive should we be with `claim : Prop` vs typed?

Currently every block carries:

```lean
class FooContext where
  -- typed hypothesis fields (q : ℝ, Z : ℕ, Braid : Type, etc.)
  claim : Prop                 -- (or claim_i, claim_ii, ...)

theorem foo [ctx : FooContext] : ctx.claim := by sorry
```

The `claim : Prop` field is a placeholder — it carries no internal
structure. Refining it requires per-block work to express the
manuscript claim in Lean's type system.

**Options for the next pass**:

1. **(A) Hand-craft chapter-by-chapter** (Descartes + BraidKnot
   done → ParticleInteractions → FluidDynamics → …). Highest
   fidelity, slowest. ~5-30 min per block × 126 remaining =
   10-60 hrs.

2. **(B) Build shared typeclass infrastructure** for common themes
   (Hecke / Markov / Wedderburn / Skein-polynomial / Fluid-dynamics
   Sobolev). Then refactor blocks to use the shared infra. Slowest
   setup but highest reuse — once `MarkovTraceClaim`,
   `WedderburnDecomposition`, `SkeinResolution`, `SobolevHk`
   typeclasses are defined, the per-block work is "name the
   witness fields and instantiate".

3. **(C) Stop here.** The bulk transformation gave every block a
   typed-fields context with named claim Props.  Substantive
   concretisation per block is deferred until specific blocks are
   actively used downstream.

## Q2 — `noncomputable instance` sorries vs the new context pattern

The 27 conjecture-class placeholders use:

```lean
class FooConjecture where
  residual : ℝ
  residual_eq_zero : residual = 0

noncomputable instance : FooConjecture := by sorry
```

The bulk-shape blocks use:

```lean
class FooContext where ...; claim : Prop
theorem foo [ctx] : ctx.claim := by sorry
```

These are different patterns. Should I:

1. **(A) Leave them distinct** — `class … instance` for conjectures,
   `class … theorem` for provable kinds.

2. **(B) Migrate conjecture classes to the new pattern** so all
   `Prop`-valued claims look uniform. The §3b-cond audit may need
   adjustment.

## Q3 — Heuristic field extraction misses for ~50 narrative blocks

The keyword-inference passes added typed fields for blocks whose
.md mentions `q`, `Z`, `N`, `braid`, `partition`, etc. But some
blocks' .md describes the math without using these tokens — e.g.
"the canonical Möbius integration-limit pencil section becomes
stationary". For these, the typed fields are abstract `Type` rather
than meaningful types.

**Are there shared abstractions you'd like me to centralise**
(e.g., a `QOU.Categorical.MöbiusSection` typeclass) that I'd
re-use across multiple blocks? Or per-block hand-crafted is fine?

## Q4 — Which next chapter to deepen (if option A in Q1)?

Suggested ordering by manuscript-importance × Lean-ease:

1. **`particle-interactions`** (18 blocks) — heavy on numerical
   predictions (CODATA + tolerance); good for `norm_num` discharges.
2. **`fluid-dynamics`** (18 blocks) — heavy on q-NS analysis;
   requires substantial Mathlib `Sobolev` / `L^p` infra.
3. **`molecular`** (6 blocks) — LP-dual structure, similar to what
   Descartes-LP work already established.
4. **`wedderburn-mass`** (4 blocks) — categorical, draws on
   already-done BraidKnot infrastructure.
5. **`hadronic-mass`** (3 blocks) — short, focused on nucleon
   binding-energy formulas.

## Q5 — `axiom` vs `class+instance` for the §3b conjecture witnesses?

AGENTS.md §3b prescribes `class C where … ; noncomputable instance
: C := by sorry`. But many of the new conjecture-class fields are
specific equations (`residual = 0`); these could equally be
`axiom C_residual_zero : residual = 0`. The `axiom` form is more
honest about "this is an unproven assumption" but the class form
allows downstream conditional dependence.

**Keep class form or migrate to `axiom` per-claim?**

## Q6 (NEW) — Mechanical-split fidelity check

The bulk-script numbered-sub-claim splits introduced 42 files with
generic docstrings:

```lean
  /-- Manuscript sub-claim (i). -/
  claim_i : Prop
  /-- Manuscript sub-claim (ii). -/
  claim_ii : Prop
  ...
```

These names map to *list positions* in the .md, not semantic content.
A future pass could:

1. **(A) Leave as-is** — names like `claim_i, claim_ii` are mechanical
   but obvious, and downstream code can refer to them.
2. **(B) Add manuscript-fragment summaries** — re-read each .md and
   replace `claim_i : Prop` with a one-line natural-language summary
   in the docstring (still `Prop`-typed). Manual but quick.
3. **(C) Rename to semantic identifiers** — for example
   `claim_i → claim_well_defined`, `claim_ii → claim_unique`,
   `claim_iii → claim_phase_boundary`. Most readable but most work.

## Q7 (NEW) — Should we update `ctx.holds` docstring boilerplate?

The previously-hand-crafted 38 files (Descartes + BraidKnot) still
contain dead text in their bottom docstrings referencing
`ctx.holds`:

> The Lean encoding below is a `theorem foo [ctx] : ctx.holds := by sorry`
> placeholder; the `ctx.holds : Prop` field carries the residual claim,
> awaiting per-block type-level translation.

This is purely cosmetic (the actual class no longer has a `holds`
field; the docstring footer references a name that no longer
exists). Should I:

1. **(A) Sweep and clean** — replace with the updated boilerplate the
   bulk script writes (~38 files, 1 commit, 5 minutes).
2. **(B) Leave it** — readers can see from the class definition that
   `holds` is gone; the docstring footer is historical.
