import QOU.Observations.StandardPart
import QOU.Core.CutLimit

/-!
# QOU.AppendixSurreals.SurrealLimitTransfer — limits as surreal equalities

Conjecture class packaging the analytic → surreal transfer: an
ω-evaluation `evalOmega` assigning to every real sequence a surreal
value, algebra-compatible, order-compatible on eventual domination,
and computing limits through the standard-part map.  A convergent
limit statement `aₙ → L` becomes the surreal proximity *equality*
`IsClose (evalOmega a) (ofReal L)` — equality up to an infinitesimal —
and on the nose `standardPart (evalOmega a) = L`.

**Epistemic status (primary conjecture, class-axiomatised).**  For the
concrete surreals such an evaluation exists model-theoretically
(Robinson ultrapower; Berarducci–Mantova germ evaluation at `ω`), but
it is not constructible from the abstract `SurrealField` interface
alone, so it is carried as a content-bearing class with **no
instance** — the honest open state per AGENTS.md §3b-tax.  No instance
is fabricated.

The payoff is the two *derived* theorems (fully proved from the class
fields):

- `standardPart_evalOmega_of_tendstoReal` — limits are computed by
  `st ∘ evalOmega`;
- `tendstoReal_le_of_eventuallyLE` — the limit-comparison inequality,
  derived purely through the surreal order and `standardPart_le_of_le`.

The second shows the "inequality → surreal statement → real
inequality" round trip promised by the alien-calculus ↔ surreal
integration review (2026-07-13): the eventual pointwise inequality is
transferred to a single surreal inequality at `ω`, and the archimedean
inequality between the limits is recovered by the (proved)
monotonicity of the standard part.

LaTeX label: `conj:surreal-limit-transfer`

## References

- [robinson1966] Robinson, *Non-standard Analysis* (ultrapower model).
- [berarducci-mantova2018] Berarducci–Mantova, *Surreal numbers,
  derivations and transseries*, JEMS 20 (2018) (germs at `ω`).
-/

namespace QOU.AppendixSurreals

open SurrealField

universe u

variable {K : Type u} [SurrealBase K]

/-- ε–N convergence of a real sequence (self-contained form; avoids
    pulling topology into the surreal kernel). -/
def TendstoReal (a : ℕ → ℝ) (L : ℝ) : Prop :=
  ∀ ε : ℝ, 0 < ε → ∃ N : ℕ, ∀ n : ℕ, N ≤ n → |a n - L| < ε

/-- Eventual pointwise domination of one real sequence by another. -/
def EventuallyLE (a b : ℕ → ℝ) : Prop :=
  ∃ N : ℕ, ∀ n : ℕ, N ≤ n → a n ≤ b n

/-- **Conjecture (surreal limit transfer).**  An ω-evaluation of real
    sequences into `K`: constants map to `ofReal`, algebra is
    respected pointwise, eventual domination transfers to the surreal
    order, and a convergent sequence evaluates infinitesimally close
    to its limit.

    The fields carry the conjecture's *hypotheses* (the existence of a
    structured evaluation); the theorems below derive consequences
    from them.  `@conjecture: primary` — no other conjecture class is
    assumed. -/
class SurrealLimitTransfer (K : Type u) [SurrealBase K] where
  /-- Evaluation of a real sequence at the surreal `ω`. -/
  evalOmega : (ℕ → ℝ) → K
  /-- Constant sequences evaluate to the embedded real. -/
  evalOmega_const : ∀ r : ℝ, evalOmega (fun _ => r) = ofReal r
  /-- Additivity. -/
  evalOmega_add : ∀ a b : ℕ → ℝ,
    evalOmega (fun n => a n + b n) = evalOmega a + evalOmega b
  /-- Multiplicativity. -/
  evalOmega_mul : ∀ a b : ℕ → ℝ,
    evalOmega (fun n => a n * b n) = evalOmega a * evalOmega b
  /-- Eventual pointwise domination transfers to the surreal order. -/
  evalOmega_le_of_eventuallyLE : ∀ a b : ℕ → ℝ,
    EventuallyLE a b → evalOmega a ≤ evalOmega b
  /-- A convergent sequence evaluates infinitesimally close to its
      limit: the limit statement as a surreal equality-up-to-ε. -/
  evalOmega_isClose_of_tendstoReal : ∀ (a : ℕ → ℝ) (L : ℝ),
    TendstoReal a L → IsClose (evalOmega a) (ofReal L)

namespace SurrealLimitTransfer

variable [SurrealLimitTransfer K]

/-- A convergent sequence evaluates to a **finite** surreal. -/
theorem evalOmega_isFinite_of_tendstoReal (a : ℕ → ℝ) (L : ℝ)
    (h : TendstoReal a L) :
    IsFinite (evalOmega (K := K) a) := by
  have hc : IsClose (evalOmega (K := K) a) (ofReal L) :=
    evalOmega_isClose_of_tendstoReal a L h
  have hinf : IsInfinitesimal (evalOmega (K := K) a - ofReal L) := hc
  have hfin : IsFinite (evalOmega (K := K) a - ofReal L) := hinf.isFinite
  have heq : evalOmega (K := K) a
      = (evalOmega (K := K) a - ofReal L) + ofReal L := by ring
  rw [heq]
  exact hfin.add (ofReal_isFinite L)

/-- **Limits are computed by `st ∘ evalOmega`**: the analytic limit
    statement becomes an exact surreal-side equality. -/
theorem standardPart_evalOmega_of_tendstoReal (a : ℕ → ℝ) (L : ℝ)
    (h : TendstoReal a L) :
    standardPart (evalOmega (K := K) a) = L := by
  have hc : IsClose (evalOmega (K := K) a) (ofReal L) :=
    evalOmega_isClose_of_tendstoReal a L h
  have hfin := evalOmega_isFinite_of_tendstoReal (K := K) a L h
  have hst := standardPart_eq_of_isClose hfin (ofReal_isFinite L) hc
  rwa [standardPart_ofReal] at hst

/-- The zero sequence evaluates to `0` at `ω`. -/
@[simp]
theorem evalOmega_zero : evalOmega (K := K) (fun _ => 0) = 0 := by
  rw [evalOmega_const, map_zero]

/-- The unit constant sequence evaluates to `1` at `ω`. -/
@[simp]
theorem evalOmega_one : evalOmega (K := K) (fun _ => 1) = 1 := by
  rw [evalOmega_const, map_one]

/-- Pointwise negation commutes with `evalOmega`. -/
theorem evalOmega_neg (a : ℕ → ℝ) :
    evalOmega (K := K) (fun n => -a n) = -evalOmega (K := K) a := by
  apply eq_neg_of_add_eq_zero_left
  have h := evalOmega_add (K := K) (fun n => -a n) a
  simp only [neg_add_cancel] at h
  rw [← h, evalOmega_zero]

/-- Pointwise subtraction commutes with `evalOmega`. -/
theorem evalOmega_sub (a b : ℕ → ℝ) :
    evalOmega (K := K) (fun n => a n - b n) =
      evalOmega (K := K) a - evalOmega (K := K) b := by
  have h := evalOmega_add (K := K) a (fun n => -b n)
  simp only [← sub_eq_add_neg] at h
  rw [h, evalOmega_neg, sub_eq_add_neg]

end SurrealLimitTransfer

/-! ### Consequences, without the transfer hypothesis

Strangler step for bean `qou-134z` (epic `qou-dk7p`, owner ruling 2026-11-27).
The three consequences below used to take `[SurrealLimitTransfer K]` and route
through `evalOmega` and the standard part. They are now proved from
`QOU.Core.CutLimit`: a convergent sequence is a *located cut* containing its
limit, and uniqueness, comparison and the squeeze are order algebra on that
cut. No transfer class, no surreal field and no axiom is needed for them. The
class above stays as the surreal error-tracking carrier; its ultrapower
instance lives behind the transcendental boundary in
`QOU.Transcendental.HyperrealLimitTransfer`. -/

/-- `TendstoReal` is the located-cut convergence of `QOU.Core.CutLimit`. -/
theorem convergesTo_of_tendstoReal {a : ℕ → ℝ} {L : ℝ} (h : TendstoReal a L) :
    QOU.Core.CutLimit.ConvergesTo a L :=
  QOU.Core.CutLimit.convergesTo_of_tendstoEps h

/-- **Limit comparison.** If `aₙ ≤ bₙ` eventually and both sequences
    converge, the limits compare. -/
theorem tendstoReal_le_of_eventuallyLE (a b : ℕ → ℝ) (L M : ℝ)
    (ha : TendstoReal a L) (hb : TendstoReal b M)
    (hab : EventuallyLE a b) : L ≤ M :=
  (convergesTo_of_tendstoReal ha).le_of_eventuallyLE (convergesTo_of_tendstoReal hb) hab

/-- **Uniqueness of sequential limits.** -/
theorem tendstoReal_unique (a : ℕ → ℝ) (L M : ℝ)
    (hL : TendstoReal a L) (hM : TendstoReal a M) : L = M :=
  (convergesTo_of_tendstoReal hL).unique (convergesTo_of_tendstoReal hM)

/-- **Squeeze.** If `a ≤ b ≤ c` eventually, `a → L`, `c → L`, and `b → M`,
    then `M = L`. -/
theorem tendstoReal_squeeze (a b c : ℕ → ℝ) (L M : ℝ)
    (ha : TendstoReal a L) (hb : TendstoReal b M) (hc : TendstoReal c L)
    (hab : EventuallyLE a b) (hbc : EventuallyLE b c) : M = L :=
  (convergesTo_of_tendstoReal ha).squeeze (convergesTo_of_tendstoReal hb)
    (convergesTo_of_tendstoReal hc) hab hbc

end QOU.AppendixSurreals
