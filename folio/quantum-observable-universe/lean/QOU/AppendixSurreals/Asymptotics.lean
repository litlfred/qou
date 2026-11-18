import Mathlib.Algebra.Order.Monoid.WithTop
import QOU.AppendixSurreals.Basic
import QOU.AppendixSurreals.StandardPart

/-!
# QOU.AppendixSurreals.Asymptotics — ω-adic Big-O valuation

Axiomatises the surreal **ω-adic order** `Ow : K → WithTop K`
(leading exponent in Conway normal form) and records the standard
dictionary relating it to classical Big-O / little-o / Θ / ∼.

The valuation signature is axiomatised as a typeclass `OmegaOrder`;
the classical-Big-O bridge is stated as a conjectural class
`SurrealBigOBridge` per AGENTS.md §3b (conjectural propagation).

Mathlib does not yet expose Conway normal form on `𝐍𝐨`, so the
canonical surreal model is still not constructed here.  `OmegaOrder`
is nevertheless **populated**, by the Hahn model in
`HahnOmegaOrder.lean` — see below.

## History: how this class came to be instantiable (2026-08-16)

`OmegaOrder` previously had **no instance anywhere in this tree**, which left
every `[OmegaOrder]`-conditional result untested for satisfiability — a class
that asserts a great deal but has never been shown consistent is not much better
than one that asserts nothing, which is the defect bean `qou-ffwk` is about.
A first attempt to supply a model from Mathlib's Hahn-series API found **three
obstructions**. Recorded because two of them are still live for the *surreal*
model, and because obstruction 2 is the one this class was changed to remove.

1. **No degenerate model is available — still true.** `SurrealField` requires
   `omegaSurreal : K` with `omegaSurreal_gt_natCast : ∀ n : ℕ, (n : K) < _`.
   No real exceeds every natural, so `SurrealField ℝ` is **impossible**; the
   cheap witness that would settle non-emptiness cannot exist, and any
   `SurrealField` model must be genuinely non-archimedean. This is why
   `SpectralNormalForm`, which needs `IsInfinitesimal`/`IsFinite` and hence
   `SurrealField`, is *still* unwitnessed even though `OmegaOrder` now is.

2. **The exponent type was self-referential — FIXED.** `Ow` was typed
   `K → WithTop K`, exponents in the field itself. That is right for `𝐍𝐨`,
   closed under `ω`-exponentiation, but it has no counterpart in Mathlib, whose
   valuation is `HahnSeries.orderTop : HahnSeries Γ R → WithTop Γ` with `Γ`
   separate. The class now carries `Γ` as its own parameter (take `Γ := K` for
   the surreal reading) and weakens `[SurrealField K]` to
   `[CommRing K] [Algebra ℝ K]`, which is all the scaling axiom ever used.
   Bean `qou-x20w`.

3. **`orderTop` multiplicativity — PROVED.** Mathlib offers only the inequality
   `orderTop_add_le_mul`. The equality `Ow_mul` states is now derived in
   `HahnOmegaOrder.lean` from `HahnSeries.order_mul` over a domain, together
   with the two zero cases.

Still open for the *surreal* carrier: the `Lex` order transfer, and a `birthday`
function satisfying the `nadd` sub-additivity and midpoint bounds `SurrealField`
demands.

Notation: in LaTeX we write `$O_\omega$` (Big-O register, via the
`\ordw` macro).  In Lean the identifier is `Ow` for ASCII usability.

LaTeX label: `rem:conway-normal-form`.

## References

- [conway1976] Conway, *On Numbers and Games*, Academic Press.
- [gonshor1986] Gonshor, *An Introduction to the Theory of Surreal
  Numbers*, Cambridge University Press.
  https://doi.org/10.1017/CBO9780511629143
- [berarducci-mantova2018] Berarducci, Mantova, *Surreal numbers,
  derivations and transseries*, JEMS 20 (2018) 339–390.
  https://doi.org/10.4171/JEMS/769
- [ehrlich2012] Ehrlich, *The absolute arithmetic continuum*,
  Bull. Symbolic Logic 18 (2012) 1–45.
  https://doi.org/10.2178/bsl/1327328438
-/

namespace QOU.AppendixSurreals

universe u s w

/-- A commutative `ℝ`-algebra `K` admits an **ω-adic order** with
    exponents in `Γ`: the leading exponent in Conway normal form,
    valued in `WithTop Γ`.

    Classical analogue is the p-adic order `ord_p`.  Under the QOU
    notational convention, the symbol is typeset as `$O_\omega$`
    (Big-O register) because the equivalence
    `f = O(g) ⟺ Ow(f) ≤ Ow(g)` makes Big-O the natural reading.

    ## Why the exponent group is a separate parameter

    Until 2026-08-16 this class fixed `Ow : K → WithTop K` and required
    `[SurrealField K]`.  Exponents-in-`K` is right for `𝐍𝐨`, which is
    closed under `ω`-exponentiation — but it is a *self-referential*
    structure, and it made the class **uninstantiable**: it left `Ow`
    with no model anywhere in this tree, so every `[OmegaOrder]`-
    conditional result was untested for satisfiability.  See bean
    `qou-x20w`, and `qou-ffwk` for the carrier-hygiene work that
    surfaced it.

    Two changes fix that, both conservative:

    * exponents move to their own `Γ`, matching the standard shape of a
      leading-exponent valuation (and Mathlib's
      `HahnSeries.orderTop : HahnSeries Γ R → WithTop Γ`); take
      `Γ := K` to recover the old reading for `𝐍𝐨`;
    * the base weakens from `[SurrealField K]` to a commutative ring
      with an algebra over an arbitrary scalar ring `S`, which is all
      `Ow_algebraMap_mul` ever used.  It was previously phrased with
      `SurrealField.ofReal`; nothing about a leading-exponent valuation
      needs the scalars to be the reals, and leaving them abstract also
      keeps this module clear of the §7c mixed-regime rule (a generic
      base ring beside a real-field type is exactly what that rule
      forbids).  Surreal callers instantiate `S := ℝ`, since every
      `SurrealField` is canonically a real algebra via
      `SurrealField.toAlgebra` with `algebraMap` equal to `ofReal`.

    Together these admit the Hahn model in `HahnOmegaOrder.lean`. -/
-- Ref: [conway1976] §III (Conway normal form)
-- Ref: [gonshor1986] §5 (leading exponent)
class OmegaOrder (K : Type u) [CommRing K]
    (S : Type s) [CommRing S] [Algebra S K]
    (Γ : Type w) [AddCommMonoid Γ] [PartialOrder Γ] where
  /-- The ω-adic order, valued in `WithTop Γ`. -/
  Ow : K → WithTop Γ
  /-- Zero has order `⊤`. -/
  Ow_zero : Ow 0 = ⊤
  /-- Multiplication is valuation-additive: `Ow (x·y) = Ow x + Ow y`. -/
  Ow_mul : ∀ x y : K, Ow (x * y) = Ow x + Ow y
  /-- Rescaling by a nonzero real leaves the leading exponent
      unchanged (finite nonzero reals have `Ow = 0`). -/
  Ow_algebraMap_mul : ∀ (r : S) (x : K), algebraMap S K r ≠ 0 →
      Ow (algebraMap S K r * x) = Ow x

namespace OmegaOrder

variable {K : Type u} [CommRing K] {S : Type s} [CommRing S] [Algebra S K]
  {Γ : Type w} [AddCommMonoid Γ] [PartialOrder Γ] [OmegaOrder K S Γ]

/-- **Surreal Big-O** relation: `x ≼ y` iff `Ow x ≤ Ow y`.
    Equivalent under the Hahn bridge to classical `x = O(y)`. -/
def preceq (x y : K) : Prop := Ow (S := S) (Γ := Γ) x ≤ Ow (S := S) (Γ := Γ) y

/-- **Surreal little-o** relation: `x ≺ y` iff `Ow x < Ow y`.
    Equivalent under the bridge to classical `x = o(y)`. -/
def prec (x y : K) : Prop := Ow (S := S) (Γ := Γ) x < Ow (S := S) (Γ := Γ) y

/-- `≼` is reflexive. -/
theorem preceq_refl (x : K) : preceq (S := S) (Γ := Γ) x x := le_refl _

/-- `≼` is transitive. -/
theorem preceq_trans {x y z : K}
    (hxy : preceq (S := S) (Γ := Γ) x y) (hyz : preceq (S := S) (Γ := Γ) y z) :
    preceq (S := S) (Γ := Γ) x z :=
  le_trans hxy hyz

/-- `≺` refines `≼`. -/
theorem preceq_of_prec {x y : K} (h : prec (S := S) (Γ := Γ) x y) :
    preceq (S := S) (Γ := Γ) x y := le_of_lt h

/-- Rescaling by a nonzero real preserves the Big-O class. -/
theorem preceq_algebraMap_mul_left (r : S) (hr : algebraMap S K r ≠ 0) (x y : K) :
    preceq (S := S) (Γ := Γ) (algebraMap S K r * x) y ↔ preceq (S := S) (Γ := Γ) x y := by
  change Ow (S := S) (Γ := Γ) (algebraMap S K r * x) ≤ Ow (S := S) (Γ := Γ) y ↔
    Ow (S := S) (Γ := Γ) x ≤ Ow (S := S) (Γ := Γ) y
  rw [Ow_algebraMap_mul (S := S) r x hr]

/-- `prec` is irreflexive: no surreal element is strictly smaller in ω-order than itself. -/
theorem prec_irrefl (x : K) : ¬ prec (S := S) (Γ := Γ) x x :=
  lt_irrefl (Ow (S := S) (Γ := Γ) x)

/-- `prec` is transitive. -/
theorem prec_trans {x y z : K}
    (hxy : prec (S := S) (Γ := Γ) x y) (hyz : prec (S := S) (Γ := Γ) y z) :
    prec (S := S) (Γ := Γ) x z :=
  lt_trans hxy hyz

/-- Rescaling the left argument by a nonzero scalar preserves strict little-o dominance `≺`. -/
theorem prec_algebraMap_mul_left (r : S) (hr : algebraMap S K r ≠ 0) (x y : K) :
    prec (S := S) (Γ := Γ) (algebraMap S K r * x) y ↔ prec (S := S) (Γ := Γ) x y := by
  change Ow (S := S) (Γ := Γ) (algebraMap S K r * x) < Ow (S := S) (Γ := Γ) y ↔
    Ow (S := S) (Γ := Γ) x < Ow (S := S) (Γ := Γ) y
  rw [Ow_algebraMap_mul (S := S) r x hr]

end OmegaOrder

/-- **Non-degenerate cosmological endpoint evaluation carrier** (`qou-g4x1`):
    separates the ultraviolet/Big-Bang endpoint `q_bb : K` from the infrared/Heat-Death
    endpoint `q_hd : K` via strict ω-adic valuation dominance `prec (evalQ q_bb) (evalQ q_hd)`. -/
class BigBangHeatDeathEndpointValuation
    (K : Type u) [CommRing K] (S : Type s) [CommRing S] [Algebra S K]
    (Γ : Type w) [AddCommMonoid Γ] [PartialOrder Γ] [OmegaOrder K S Γ]
    (evalQ : K → K) (q_bb q_hd : K) : Prop where
  /-- The ultraviolet endpoint valuation strictly precedes the infrared endpoint valuation. -/
  uv_prec_ir : OmegaOrder.prec (S := S) (Γ := Γ) (evalQ q_bb) (evalQ q_hd)

/-- Under `[BigBangHeatDeathEndpointValuation K S Γ evalQ q_bb q_hd]`, the surreal evaluation
    at the Big-Bang endpoint `q_bb` is strictly distinct from the evaluation at the
    Heat-Death endpoint `q_hd`. -/
theorem endpoint_eval_ne_of_valuation
    {K : Type u} [CommRing K] {S : Type s} [CommRing S] [Algebra S K]
    {Γ : Type w} [AddCommMonoid Γ] [PartialOrder Γ] [OmegaOrder K S Γ]
    {evalQ : K → K} {q_bb q_hd : K}
    [h : BigBangHeatDeathEndpointValuation K S Γ evalQ q_bb q_hd] :
    evalQ q_bb ≠ evalQ q_hd := by
  intro heq
  have hlt := h.uv_prec_ir
  rw [heq] at hlt
  exact OmegaOrder.prec_irrefl (S := S) (Γ := Γ) (evalQ q_hd) hlt

/-- **Non-degenerate Hahn-substrate higher-order residual carrier** (`qou-g4x1`):
    given a coefficient sequence `α : ℕ → S`, a truncated mass prediction `massPred : ℕ → S`,
    and reference data `codata : ℕ → S`, at least one higher-order coefficient `α (k + 2)` is
    non-zero and determines the `(k + 2)`-th truncation residual `massPred k - codata k`. -/
class HahnSubstrateHigherOrderFit
    {S : Type s} [CommRing S] (α massPred codata : ℕ → S) : Prop where
  /-- At least one higher-order Hahn coefficient `α (k + 2)` is non-zero. -/
  exists_nonzero_coeff : ∃ k : ℕ, α (k + 2) ≠ 0
  /-- The `k`-th truncation residual equals the `(k + 2)`-th Hahn coefficient. -/
  residual_eq_coeff : ∀ k : ℕ, massPred k - codata k = α (k + 2)

/-- Under `[HahnSubstrateHigherOrderFit α massPred codata]`, there exists a truncation order `k`
    at which the higher-order Hahn series prediction strictly differs from the uncorrected
    reference value. -/
theorem exists_nontrivial_hahn_residual
    {S : Type s} [CommRing S] {α massPred codata : ℕ → S}
    [h : HahnSubstrateHigherOrderFit α massPred codata] :
    ∃ k : ℕ, massPred k ≠ codata k := by
  obtain ⟨k, hk⟩ := h.exists_nonzero_coeff
  refine ⟨k, ?_⟩
  intro heq
  have hsub : massPred k - codata k = 0 := sub_eq_zero.mpr heq
  rw [h.residual_eq_coeff k] at hsub
  exact hk hsub

/- **Note on the classical Big-O bridge.**

    The natural conjecture would be: a real-valued sequence
    `f : ℕ → ℝ` realises as a surreal via some Hahn-style embedding
    `surrealOf : (ℕ → ℝ) → K`, and classical Big-O on `ℕ → ℝ`
    coincides with the surreal `≼` under this realisation.

    The naïve embedding `surrealOf f := Σₙ f(n) · ω^{-n}` does **not**
    work: the leading exponent of such a series is the index of the
    smallest `n` with `f(n) ≠ 0`, which only sees support, not
    coefficient growth.  Two sequences `f n = n` and `g n = 1` would
    both realise to surreals of `Ow = 0` (or `-1` if reindexed),
    even though `f` is unbounded.

    A correct bridge requires the Berarducci–Mantova differential-field
    interpretation: `surrealOf f` is the value `f̃(ω) ∈ 𝐍𝐨`, where
    `f̃` is the unique transseries extension of `f` and `ω` is the
    surreal infinity.  Under that realisation `Ow(f̃(ω))` is the
    polynomial degree of `f` at infinity, and the Big-O equivalence
    holds for transseries `f, g`.

    Mathlib does not yet expose transseries on `𝐍𝐨`, so the bridge
    is left as an open formal question.  No load-bearing proof in
    this branch depends on it; downstream blocks reference the
    bridge informally via the body-asymptotics catalog
    (`rem:body-asymptotics-catalog`).

    Refs: [berarducci-mantova2018] §6, [ehrlich2012] §6. -/

end QOU.AppendixSurreals
