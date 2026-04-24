/-!
# QOU.AppendixSurreals.Asymptotics — ω-adic Big-O valuation

Axiomatises the surreal **ω-adic order** `Ow : K → WithTop K`
(leading exponent in Conway normal form) and records the standard
dictionary relating it to classical Big-O / little-o / Θ / ∼.

The valuation signature is axiomatised as a typeclass `OmegaOrder`;
the classical-Big-O bridge is stated as a conjectural class
`SurrealBigOBridge` per CLAUDE.md §3b (conjectural propagation).

Mathlib does not yet expose Conway normal form on `𝐍𝐨`, so neither
class is populated here — both are intended to be instantiated by
downstream modules that construct or axiomatise a specific surreal
carrier (e.g.\ via a Hahn embedding).

Notation: in LaTeX we write `$O_\omega$` (Big-O register, via the
`\ordw` macro).  In Lean the identifier is `Ow` for ASCII usability.

LaTeX labels: `rem:conway-normal-form`, `rem:conway-normal-form`.

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

import Mathlib.Algebra.Order.Monoid.WithTop
import QOU.AppendixSurreals.Basic
import QOU.AppendixSurreals.StandardPart

namespace QOU.AppendixSurreals

universe u

/-- A surreal field `K` admits an **ω-adic order**: the leading
    exponent in Conway normal form, valued in `WithTop K`.

    Classical analogue is the p-adic order `ord_p`.  Under the QOU
    notational convention, the symbol is typeset as `$O_\omega$`
    (Big-O register) because the equivalence
    `f = O(g) ⟺ Ow(f) ≤ Ow(g)` makes Big-O the natural reading.

    Mathlib does not yet expose Conway normal form, so we axiomatise
    the signature; the canonical model is `K = 𝐍𝐨` with `Ow x` the
    leading `ω`-exponent of `x ∈ 𝐍𝐨^×` (and `⊤` at zero). -/
-- Ref: [conway1976] §III (Conway normal form)
-- Ref: [gonshor1986] §5 (leading exponent)
class OmegaOrder (K : Type u) [SurrealField K] where
  /-- The ω-adic order, valued in `WithTop K`. -/
  Ow : K → WithTop K
  /-- Zero has order `⊤`. -/
  Ow_zero : Ow 0 = ⊤
  /-- Multiplication is valuation-additive: `Ow (x·y) = Ow x + Ow y`. -/
  Ow_mul : ∀ x y : K, Ow (x * y) = Ow x + Ow y
  /-- Rescaling by a nonzero real leaves the leading exponent
      unchanged (finite nonzero reals have `Ow = 0`). -/
  Ow_ofReal_mul : ∀ (r : ℝ) (x : K), r ≠ 0 →
      Ow (SurrealField.ofReal r * x) = Ow x

namespace OmegaOrder

variable {K : Type u} [SurrealField K] [OmegaOrder K]

/-- **Surreal Big-O** relation: `x ≼ y` iff `Ow x ≤ Ow y`.
    Equivalent under the Hahn bridge to classical `x = O(y)`. -/
def preceq (x y : K) : Prop := Ow x ≤ Ow y

/-- **Surreal little-o** relation: `x ≺ y` iff `Ow x < Ow y`.
    Equivalent under the bridge to classical `x = o(y)`. -/
def prec (x y : K) : Prop := Ow x < Ow y

scoped infix:50 " ≼ " => OmegaOrder.preceq
scoped infix:50 " ≺ " => OmegaOrder.prec

/-- `≼` is reflexive. -/
theorem preceq_refl (x : K) : preceq x x := le_refl _

/-- `≼` is transitive. -/
theorem preceq_trans {x y z : K}
    (hxy : preceq x y) (hyz : preceq y z) : preceq x z :=
  le_trans hxy hyz

/-- `≺` refines `≼`. -/
theorem preceq_of_prec {x y : K} (h : prec x y) : preceq x y := le_of_lt h

/-- Rescaling by a nonzero real preserves the Big-O class. -/
theorem preceq_ofReal_mul_left (r : ℝ) (hr : r ≠ 0) (x y : K) :
    preceq (SurrealField.ofReal r * x) y ↔ preceq x y := by
  unfold preceq
  rw [Ow_ofReal_mul r x hr]

end OmegaOrder

/-- **Surreal Big-O ↔ classical Big-O bridge** (conjectural).

    A real-valued sequence `f : ℕ → ℝ` realises as a surreal via
    the Hahn-series embedding
    `surrealOf f := Σₙ f(n) · ω^{-n}`.  The bridge conjecture
    states that classical Big-O on `ℕ → ℝ` coincides with the
    surreal `≼` under this realisation.

    This is the content of Berarducci–Mantova's differential-field
    reading of asymptotics on `𝐍𝐨` restricted to integer exponents.
    Mathlib does not yet expose the Hahn embedding, so we package
    the conjecture as a typeclass per CLAUDE.md §3b (conjectural
    propagation).  An instance supplies both the Hahn realisation
    and the proof of equivalence. -/
-- Ref: [berarducci-mantova2018] §6
-- Ref: [ehrlich2012] §6 (Hahn embeddings in 𝐍𝐨)
class SurrealBigOBridge (K : Type u) [SurrealField K] [OmegaOrder K] where
  /-- Hahn-series realisation of a real sequence as a surreal. -/
  surrealOf : (ℕ → ℝ) → K
  /-- The bridge: classical Big-O is equivalent to surreal `≼`. -/
  bigO_iff_preceq : ∀ f g : ℕ → ℝ,
      (∃ C > 0, ∀ n, |f n| ≤ C * |g n|)
    ↔ OmegaOrder.preceq (surrealOf f) (surrealOf g)

end QOU.AppendixSurreals
