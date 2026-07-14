import QOU.AppendixSurreals.StandardPart

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

variable {K : Type u} [SurrealField K]

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
class SurrealLimitTransfer (K : Type u) [SurrealField K] where
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

end SurrealLimitTransfer

/-- **Limit comparison through the surreal order.**  If `aₙ ≤ bₙ`
    eventually and both sequences converge, the limits compare — the
    entire argument routed through one surreal inequality at `ω` and
    the proved monotonicity of the standard part.  (The classical
    strict-inequality collapse is visible here: `evalOmega a <
    evalOmega b` is compatible with equal standard parts, which is why
    only `≤` survives the wall.) -/
theorem tendstoReal_le_of_eventuallyLE (K : Type u) [SurrealField K]
    [SurrealLimitTransfer K] (a b : ℕ → ℝ) (L M : ℝ)
    (ha : TendstoReal a L) (hb : TendstoReal b M)
    (hab : EventuallyLE a b) : L ≤ M := by
  have hle : SurrealLimitTransfer.evalOmega (K := K) a
      ≤ SurrealLimitTransfer.evalOmega (K := K) b :=
    SurrealLimitTransfer.evalOmega_le_of_eventuallyLE a b hab
  have hfa :=
    SurrealLimitTransfer.evalOmega_isFinite_of_tendstoReal (K := K) a L ha
  have hfb :=
    SurrealLimitTransfer.evalOmega_isFinite_of_tendstoReal (K := K) b M hb
  have hst := standardPart_le_of_le hfa hfb hle
  rwa [SurrealLimitTransfer.standardPart_evalOmega_of_tendstoReal a L ha,
       SurrealLimitTransfer.standardPart_evalOmega_of_tendstoReal b M hb]
    at hst

end QOU.AppendixSurreals
