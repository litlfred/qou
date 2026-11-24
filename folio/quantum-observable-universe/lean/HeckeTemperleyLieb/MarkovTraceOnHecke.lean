/-
Copyright (c) 2026 litlfred. All rights reserved.

# Markov trace on Hecke algebras — scaffold (2026-06-04)

This file scaffolds the Markov-trace infrastructure on Iwahori-Hecke
algebras `H_n(q)` needed for the Q_β residue A composite-operator
identification (paths B, C, D in
`docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`).

## What this provides

A type-level scaffold for:
- The Hecke algebra `H_n(q)` (axiomatised; Mathlib has only basic stub)
- The Markov trace `tr_M : H_n(q) → R` as a linear functional
- Class `MarkovTraceCompatibility` axiomatising the Markov properties:
  (M1) Linearity, (M2) Conjugation invariance, (M3) Markov reduction
       `tr_M(x · σ_{n-1}) = z · tr_M(x)` for `x ∈ H_{n-1}`

## Cross-refs

- `QBetaCategoricalPrecisionLadder.lean` (`τ_M(T_β)` is the canonical Q_β source)
- Audit: [`docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`](../../../../../docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md)
- AGENTS.md §"Hecke-Skein convention"
- [wenzl1988] doi:10.1007/BF01239526 (Markov trace on H_n(q))
-/

import Mathlib.Algebra.Algebra.Defs
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

namespace QOU.Machinery

/-! ## Hecke algebra `H_n(q)` — abstract scaffold

The Iwahori-Hecke algebra is presented as a quotient of the braid
group algebra of `B_n` by the relation `(σ_i - q)(σ_i + q⁻¹) = 0`
(AGENTS.md §7a Hecke-Skein convention). Mathlib has only a basic
stub; here we axiomatise the structure for downstream consumers. -/

/-! ### Removed: the `QOU.Machinery.HeckeAlgebra` marker class

There used to be a second class of that name here:

```lean
class HeckeAlgebra (R) [CommRing R] (q : R) (n : ℕ) (H) [Ring H] [Algebra R H] : Prop where
  hecke_structure : True
```

described as an "opaque marker … instance gates the categorical promotion". It
gated nothing: the sole field is `True`, so `⟨trivial⟩` instantiates it and any
`[HeckeAlgebra …]` hypothesis drawn from it carries no content — the skill's
`: True`-carrier pattern (`lean-proof-vacuity-audit.md` §7).

It also collided by name with the real `QOU.Hecke.HeckeAlgebra`
(`embed` / `quadratic` / `braid` / `farCommute` / `spans`), which is what every
actual consumer in the tree uses.

Removed rather than fixed, because it had **zero consumers**: all five importers
of this module referenced it zero times, and no file reached it via
`open QOU.Machinery`. The real class now also has a real instance at `n = 2`
(`QOU.Hecke.InstanceH2`), so a contentless marker has nothing left to mark. -/

/-! ## Markov trace as a linear functional -/

/-- A **Markov trace** on `H_n(q)` is a linear functional satisfying
the Markov reduction property.

Two of the three Markov laws are now **enforced** as Lean propositions
over the `(tr : H → R)` parameter (`H` is a `Ring`, `R`-algebra): (M1)
`R`-linearity of `tr` and (M2) conjugation invariance `tr (x·y) = tr (y·x)`.
The third law, (M3) Markov reduction `tr (x·σ_{n-1}) = z·tr (x)`, still
requires the generator `σ_{n-1}` — not a parameter of this class — so it
remains documentation for the eventual instance, not an enforced field. -/
class MarkovTrace (R H : Type*) [CommRing R] [Ring H] [Algebra R H]
    (tr : H → R) : Prop where
  /-- (M2) Conjugation invariance / cyclicity: `tr (x·y) = tr (y·x)`. -/
  cyclic : ∀ x y : H, tr (x * y) = tr (y * x)
  /-- (M1a) Additivity — part of `R`-linearity of `tr`. -/
  map_add : ∀ x y : H, tr (x + y) = tr x + tr y
  /-- (M1b) `R`-scalar compatibility — the rest of `R`-linearity. -/
  map_smul : ∀ (r : R) (x : H), tr (r • x) = r * tr x
  -- (M3) Markov reduction `tr (x·σ_{n-1}) = z·tr (x)` needs the generator
  -- `σ_{n-1}`, absent from this class's signature — documented, not enforced.

/-! ## Jones-Wenzl projector + Markov-trace evaluation -/

/-- The **Jones-Wenzl projector** `p_n ∈ H_n(q)`: the nonzero idempotent that
kills every Jones projection `e_i`, `i < n-1`.

Restated 2026-11-21 (owner "Fix", bean `qou-c8p8`). The earlier form had the
single field `p * p = p`, with `q` and `n` occurring in no field, so `1` and `0`
inhabited it at every rank. The generators are now a parameter `σ`, and the
strand-killing relation is enforced.

**Convention (derived from the corpus, not chosen).** The Jones projection is
`QOU.Machinery.HeckeTower.jonesIdempotent q σ = (q+q⁻¹)⁻¹ • (q•1 − σ)`. So
`p · e_i = 0` is `p · (q•1 − σ_i) = 0`, i.e. `p σ_i = q p`. The comment this
replaces said `p σ_i = −q⁻¹ p`. That is the opposite eigenchannel and
contradicts the corpus's own `e`. The relation is written with `q•1 − σ_i`
rather than with `e_i`, so it needs no `q⁻¹` and holds over a `CommRing`;
when `q + q⁻¹ ≠ 0` the two forms are equivalent. -/
class JonesWenzlProjector (R H : Type*) [CommRing R] [Ring H] [Algebra R H]
    (q : R) (σ : ℕ → H) (n : ℕ) (p : H) : Prop where
  /-- Idempotence of the projector: `p · p = p`. -/
  idempotent : p * p = p
  /-- The projector is not zero. -/
  ne_zero : p ≠ 0
  /-- Right strand-killing: `p · (q•1 − σ_i) = 0` for `i < n − 1`. -/
  kill_right : ∀ i, i + 1 < n → p * (q • (1 : H) - σ i) = 0
  /-- Left strand-killing: `(q•1 − σ_i) · p = 0` for `i < n − 1`. -/
  kill_left : ∀ i, i + 1 < n → (q • (1 : H) - σ i) * p = 0

/-! ## Open: residue A as a Markov-trace residue

The Q_β residue A at `u_substrate` is conjecturally the Markov-trace
residue of a composite Wenzl × Demazure operator (path D). This is
not yet statable here; see the removal note below. -/

/-! **Removed 2026-11-15: `ResidueACompositeIdentification`.** Its only
field was `composite_markov_residue : True`, so it asserted nothing, and no
file used it. The missing statement — the Markov-trace residue of the
composite Wenzl × Demazure operator at `u_substrate` equals the Q_β residue
A — needs that operator to be constructed first. Recorded in bean `qou-n2un`. -/

/-! ## Concrete `H₃(q)` Markov trace — the real structure

This realizes the `MarkovTrace` intent above for `n = 3` with an explicit
linear functional on the NF free module `Fin 6 → R`, replacing the
`True` marker with proved laws. The NF basis order is
`[γ, σ₀, σ₁, L₊, L₋, e⁻]`, identical to `gram.NF_BASIS`; the data mirror
`computations/.../gram.py` (`hm`, `TR_M`) and the
symbolic `pyhecke.trace_formal`. The mathematics is cross-verified in
Python against `gram.py` (randomized) and over ℚ(s) by
`tools/pyhecke/tests/test_trace_formal.py`. -/
namespace H3

variable {R : Type*} [CommRing R]

/-- Markov-Ocneanu-Wenzl weights on the GB-NF basis `[γ, σ₀, σ₁, L₊, L₋,
e⁻]` of `H₃(q)` (mirrors `gram.TR_M` / `trace_formal.TR_M_formal`):
`tr_M(e⁻) = h·z² + z` — the 2026-05-19 fix, NOT `z³`. `z` is the Markov
parameter, `h = q − q⁻¹`. -/
def TRM (z h : R) : Fin 6 → R := ![1, z, z, z ^ 2, z ^ 2, h * z ^ 2 + z]

/-- The **Markov trace** on the NF free module `Fin 6 → R`: the linear
functional `v ↦ ∑ᵢ vᵢ · TRMᵢ`. The real structure behind the `True`
marker. -/
def trM (z h : R) (v : Fin 6 → R) : R := ∑ i, v i * TRM z h i

/-- Right action of `σ₀` on the NF basis (mirrors `gram.hm(·,1,0,0)`). -/
def mulσ₀ (h : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![v 1, v 0 + h * v 1, v 3, v 2 + h * v 3, v 5, v 4 + h * v 5]

/-- Right action of `σ₁` on the NF basis (mirrors `gram.hm(·,1,0,1)`). -/
def mulσ₁ (h : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![v 2, v 4, v 0 + h * v 2, v 5, v 1 + h * v 4, v 3 + h * v 5]

/-- The **full algebra product** `u · v` on the NF free module of `H₃(q)`.

Each basis element `b_j` is the GB normal form of a generator word `W_j`,
and right-multiplication is an anti-homomorphism `R_{ab} = R_b ∘ R_a`, so
`u · b_j = R_{W_j}(u)` is the composite of `mulσ₀`/`mulσ₁` along `W_j`. By
right-linearity `u · v = ∑_j v_j · (u · b_j)`. The producing words (and
hence the composition order — note `b₃ = σ₁σ₀`, `b₄ = σ₀σ₁`) were pinned by
the symbolic preflight in `gram.py`'s `hm` convention, which also verified
`tr_M(u·v) = tr_M(v·u)` as an identity over `ℚ(z,h)`:

| `j` | basis `b_j` | word `W_j` | `u · b_j` |
|----|------------|-----------|-----------|
| 0 | `γ`  | `()`      | `u` |
| 1 | `σ₀` | `(0)`     | `mulσ₀ u` |
| 2 | `σ₁` | `(1)`     | `mulσ₁ u` |
| 3 | `L₊` | `(1,0)`   | `mulσ₀ (mulσ₁ u)` |
| 4 | `L₋` | `(0,1)`   | `mulσ₁ (mulσ₀ u)` |
| 5 | `e⁻` | `(0,1,0)` | `mulσ₀ (mulσ₁ (mulσ₀ u))` |

**Orientation trap (owner decision D3, 2026-11-15, bean `qou-qs1d`).** The labels
`L₊`, `L₋` are `gram.NF_NAMES`, defined by `gram`'s product. `gram.hm` is LEFT
multiplication with word concatenation, so `gram`'s index 3 is `σ₀σ₁ = L₊`.
`mulNF` is the OPPOSITE product: `mulNF u v` is `v·u` in `gram`'s convention, and
`mulσ₀`, `mulσ₁` are right actions only with respect to `mulNF`. Read in THIS
product (the `H3A` ring), coordinate 3 is `σ₁·σ₀` and coordinate 4 is `σ₀·σ₁`
(`QOU.QuarkState.s1_mul_s0`, `s0_mul_s1`). So `rem:knot-basis-color-content`'s
`L₊ = σ₀σ₁`, computed with `mulNF`, lands at coordinate 4.

No value moves either way: `H₃ ≅ H₃ᵒᵖ` under word reversal, which fixes the
generators and swaps coordinates 3 and 4, and `TRM` is equal (`z²`) on both. Any
use of the `L₊`/`L₋` NAMES together with `mulNF`/`H3A` products must state which
orientation it means. -/
def mulNF (h : R) (u v : Fin 6 → R) : Fin 6 → R := fun i =>
    v 0 * u i
  + v 1 * mulσ₀ h u i
  + v 2 * mulσ₁ h u i
  + v 3 * mulσ₀ h (mulσ₁ h u) i
  + v 4 * mulσ₁ h (mulσ₀ h u) i
  + v 5 * mulσ₀ h (mulσ₁ h (mulσ₀ h u)) i

/-- **(M1) Linearity** — additivity. -/
theorem trM_add (z h : R) (u v : Fin 6 → R) :
    trM z h (u + v) = trM z h u + trM z h v := by
  simp only [trM, Pi.add_apply, add_mul, Finset.sum_add_distrib]

/-- **(M1) Linearity** — homogeneity. -/
theorem trM_smul (z h c : R) (v : Fin 6 → R) :
    trM z h (c • v) = c * trM z h v := by
  simp only [trM, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  exact Finset.sum_congr rfl (fun i _ => by ring)

/-- **(M3) Hecke relation** as an operator identity: `σ₀² = h·σ₀ + 1`. -/
theorem mulσ₀_hecke (h : R) (v : Fin 6 → R) :
    mulσ₀ h (mulσ₀ h v) = h • mulσ₀ h v + v := by
  funext i
  fin_cases i <;>
    simp [mulσ₀, Pi.add_apply, Pi.smul_apply, smul_eq_mul] <;> ring

/-- **(M3) Markov reduction** `tr(x·σ₁) = z·tr(x)` for
`x ∈ H₂ = span{γ, σ₀}` (i.e. `v 2 = v 3 = v 4 = v 5 = 0`). The defining
Markov property at the `H₂ ↪ H₃` inclusion. -/
theorem trM_markov_σ₁ (z h : R) (v : Fin 6 → R)
    (h2 : v 2 = 0) (h3 : v 3 = 0) (h4 : v 4 = 0) (h5 : v 5 = 0) :
    trM z h (mulσ₁ h v) = z * trM z h v := by
  simp only [trM, mulσ₁, TRM, Fin.sum_univ_six, Matrix.cons_val, h2, h3, h4, h5]
  ring

/-- **(M2) Trace cyclicity** `tr_M(u · v) = tr_M(v · u)` — the defining
property of a *trace*, here for the full `H₃(q)` algebra product `mulNF`.
This is what makes `trM` an honest Markov **trace** (not merely a Markov-
reducible functional), and it is exactly the symmetry the `Ind_{H₃}^{H₄}`
Markov-stabilization analysis relies on. Verified over `ℚ(z,h)` by the
symbolic preflight before being formalized; the identity is a polynomial
in the entries of `u`, `v` and the parameters `z, h`, closed by `ring`
after the trace sum and the nested `mulσ` actions are unfolded. -/
theorem trM_cyclic (z h : R) (u v : Fin 6 → R) :
    trM z h (mulNF h u v) = trM z h (mulNF h v u) := by
  simp only [trM, mulNF, mulσ₀, mulσ₁, TRM, Fin.sum_univ_six,
    Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  ring

/-- The concrete n=3 trace is a **real** linear functional satisfying the
Markov **trace** laws — no longer a `True` marker. Bundles (M1) linearity,
(M2) cyclicity, and (M3) the Markov reduction; the bridge for discharging
`markov_trace_origin` once Step 4 names the residue-A element. -/
theorem markovTrace_realized (z h : R) :
    (∀ u v, trM z h (u + v) = trM z h u + trM z h v) ∧
    (∀ c v, trM z h (c • v) = c * trM z h v) ∧
    (∀ u v, trM z h (mulNF h u v) = trM z h (mulNF h v u)) ∧
    (∀ v : Fin 6 → R, v 2 = 0 → v 3 = 0 → v 4 = 0 → v 5 = 0 →
       trM z h (mulσ₁ h v) = z * trM z h v) :=
  ⟨trM_add z h, trM_smul z h, trM_cyclic z h, trM_markov_σ₁ z h⟩

/-! ## Extending past H₃ (open keystone infra)

The `H3` realization above is `n = 3`-specific (the `Fin 6` NF basis
`[γ, σ₀, σ₁, L₊, L₋, e⁻]`). The open Markov-trace-origin claim
in `QOU.BraidKnot.MmuR9V9Closure` (bean `qou-n2un`) needs the trace for
general `n` — the `fun n r => ℏ_rⁿ` family — which requires two ingredients
this file does not yet carry:

1. **The H₄(q) NF basis + `mulNF` table — DONE (verified 2026-08-22).** This
   item is **no longer open**, and the paragraph that followed it described the
   work as still to do for roughly a month after it landed. What exists now:

   - `computations/markov/hecke-regular-nf-h4.witness.json` — "H_n(q)
     regular-rep **GB-NF** generator actions + Ocneanu/Markov trace; H3
     validation + **H4 emission for the Lean H4 Markov-trace formalization**"
     (bean `qou-1jrr`). Generated from the confluent Gröbner normal forms, as
     this block required — not hand-written, not a local-rewriting Python
     reimplementation.
   - `QOU.Machinery.H4Cyclicity` — the `Fin 24` subscript basis (24 = 4! GB
     normal forms, exactly the count this block predicts) with the
     `e₄_eq_mul_*` factorizations. **Sorry-free**, as are
     `H4GeneratorAction`, `HeckeH4RepDecomp`, `BilinearTraceRepBasis` and
     `BilinearTraceCyclicity`: zero real `sorry` across the whole cluster.
   - `QOU.Machinery.MarkovTraceH4` — `trM_cyclic` for `n = 4`, off
     `gram_symm`'s 576 computed entries, reduced through
     `BilinearTraceCyclicity.cyclic_of_gram_symm`.

   The reducer caveat this block recorded was correct and was respected: the
   H₄ table does come from the GB route, not from Hecke + commute +
   adjacent-braid local rewriting (which is non-confluent and yields 60+
   irreducibles rather than 24).
   **Reducer caveat, retained for anyone extending to H₅ (verified
   2026-07-13).** `gram.py`'s `_reduce_nf` is H₃-specific: it applies only the
   Hecke-square and *adjacent* braid moves, which suffice for H₃ (whose two
   generators σ₀,σ₁ are adjacent). H₄ also needs the non-adjacent commuting
   relation `σ₀σ₂ = σ₂σ₀`, and even Hecke + commute + adjacent-braid is **not
   confluent** — a BFS over that rule set yields 60+ irreducible words, not the
   24 = 4! GB normal forms. Use the confluent reducer (hecke-engine's
   `gb_nf_reducer.rs`, Rust, permutation/Coxeter-canonical and general-`n`),
   not a naive local-rewriting Python reimplementation.

2. **The `Ind_{H₃}^{H₄}` Markov stabilization.** The general-`n` trace is built
   from the H₃ trace by the Markov induction/stabilization the (M3) law
   encodes; the `trM_markov_σ₁` reduction here is the `n = 3` base case. The
   `n = 4` case is numerically confirmed — `tr_M⁴(x·σ₂) = z·tr_M³(x)` and
   `tr_M⁴(x) = tr_M³(x)` hold for H₃ words *beyond* the weight-pinning
   constraints (over-determination test, float64) by
   `computations/probes/markov_reduction_h3_to_h4_verify.py`, via the same
   seminormal machinery as `alpha_k_jones_markov_h4.py`. That is evidence for
   ingredient (2); the Lean-grade proof still awaits a symbolic-exact
   cyclicity argument over `ℚ(z,h)` (ingredient (1)'s table is now in hand —
   see item 1 above).

   **Read that citation with three caveats (measured 2026-08-22, bean
   `qou-ze9n`).** The cited probe (a) is written in convention **C**,
   `z = 1/(√q + 1/√q) = 0.4993…`, which the 2026-08-15 ruling excised in
   favour of D's `q³/(q²+1) = 0.6127…`, a 23 % difference; (b) computes in
   float64 throughout, which was never necessary — the seminormal machinery
   accepts and returns `mpf`; and (c) **did not run as committed**, its
   bootstrap omitting `qou-substrate` and pointing at the `pyhecke` package
   directory rather than its parent. (c) is fixed; (a) and (b) are left in
   place as the historical record of what this docstring cites.

   **The conclusion survives all three**, which is why item 2 still stands.
   `computations/probes/markov_reduction_h3_to_h4_conventions.py` re-runs the
   same over-determination test at 50 dps under **both** conventions and finds
   the reduction holds either way, worst residuals ~1e-51 against a 1e-30
   tolerance — agreement to the limit of the arithmetic used, not an
   exactness claim. The reason is structural: `z` is an *input* to the weight
   solve, not an output, so the Ocneanu trace is a one-parameter family and
   the Markov law is insensitive to which member is chosen. Prefer the
   companion probe for new work.

Separately, `markov_trace_origin` also needs **Step 4** — naming the specific
Wenzl–Hoefsmit operator whose trace is `ℏ_rⁿ` (an *identification*, not a
trace-infrastructure gap). That operator is currently unidentified; every
compute attempt at it lives in `fsh-guts/deprecated/computations/`.

**Scope of the gap — Wenzl POSITIVITY is NOT required (W1 audit, 2026-07-25).**
The general-`n` `MarkovTrace` instance needs only the three class fields
(cyclicity + `R`-linearity); every consumer
(`TauFunctorReduction.observationFrame_*`) uses exactly those, and positivity
is not even expressible over the generic `[CommRing R]` the class lives on
(§7c: ordering is post-wall). Wenzl's positive-trace theorem [wenzl1988] is
about the C*/subfactor regime (unitarity, semisimplicity ascent) — surplus
here, exactly as PSD was surplus to the B2 lift (PR #4151,
`LoopWeightRealSymmReduction`). See
`docs/audits/2026-07-25-markovtrace-w1-class-fields-audit.md`. -/

end H3

end QOU.Machinery
