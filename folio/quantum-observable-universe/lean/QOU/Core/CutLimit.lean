import QOU.Core.LawvereCut

/-!
# QOU.Core.CutLimit — sequential limits as located cuts

Bean `qou-134z` (item 7 of epic `qou-dk7p`, the surreal/hyperreal limit
transfer), strangler step 1. Owner ruling 2026-11-27: limits are tracked by
cuts, not by ε–δ, and only the comparison with a completed field may use the
one non-constructive axiom `[Coev E]` of `QOU.Core.LawvereCut`.

A sequence `a : ℕ → K` in an ordered field `K` (typically `ℚ`, or any ordered
field in which QOU quantities are compared) determines a cut `seqCut a`:

* a lower probe `x` is accepted when `a` is **eventually ≥ x**;
* an upper probe `y` is accepted when `a` is **eventually ≤ y**.

Lawvere `ev` (interval soundness) holds outright, so `seqCut a` is a `Cut K`
with no hypothesis. **Convergence to `L` is then purely order-algebraic:** the
cut is located (`coev = 0`) and contains `L`. Uniqueness of limits, the
comparison lemma and the squeeze follow from `Cut.Located.eq_of_contains` with
no analytic hypothesis and no axiom.

The axiom enters only where a located cut is asked to *have* a value it was
not given: `seqCut_located_of_coev` reads locatedness off `[Coev E]` for a cut
evaluation whose cuts are sequence cuts (e.g. the Cauchy sequences of a
completion). That is the single point at which this file touches the
transcendental subgraph's comparison step.

This replaces the private hypothesis class `SurrealLimitTransfer` as the
carrier of the three consequence theorems in
`QOU.Observations.SurrealLimitTransfer`; see that file.

No empirical value enters this file.
-/

namespace QOU.Core.CutLimit

open QOU.Core.LawvereCut

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- `a` is eventually at least `x`. -/
def EventuallyGE (a : ℕ → K) (x : K) : Prop := ∃ N : ℕ, ∀ n, N ≤ n → x ≤ a n

/-- `a` is eventually at most `y`. -/
def EventuallyLEc (a : ℕ → K) (y : K) : Prop := ∃ N : ℕ, ∀ n, N ≤ n → a n ≤ y

/-- Eventual pointwise domination of sequences. -/
def EventuallyLE (a b : ℕ → K) : Prop := ∃ N : ℕ, ∀ n, N ≤ n → a n ≤ b n

/-- The cut of a sequence: eventual lower and upper bounds. `ev` holds with
no hypothesis. -/
def seqCut (a : ℕ → K) : Cut K where
  lower x := EventuallyGE a x
  upper y := EventuallyLEc a y
  lower_down _ _ h := fun ⟨N, hN⟩ => ⟨N, fun n hn => le_trans h (hN n hn)⟩
  upper_up _ _ h := fun ⟨N, hN⟩ => ⟨N, fun n hn => le_trans (hN n hn) h⟩
  ev _ _ := fun ⟨N, hN⟩ ⟨M, hM⟩ =>
    le_trans (hN (max N M) (le_max_left _ _)) (hM (max N M) (le_max_right _ _))

/-- **Convergence as a located cut.** `a` converges to `L` when its cut is
located and contains `L`. No ε–N clause and no completed field appear. -/
def ConvergesTo (a : ℕ → K) (L : K) : Prop :=
  (seqCut a).Located ∧ (seqCut a).Contains L

/-- **Uniqueness of limits**, from `Located.eq_of_contains`. -/
theorem ConvergesTo.unique {a : ℕ → K} {L M : K}
    (hL : ConvergesTo a L) (hM : ConvergesTo a M) : L = M :=
  hL.1.eq_of_contains hL.2 hM.2

/-- **Comparison lemma.** If `a ≤ b` eventually, `a → L` and `b → M`, then
`L ≤ M`. -/
theorem ConvergesTo.le_of_eventuallyLE {a b : ℕ → K} {L M : K}
    (ha : ConvergesTo a L) (hb : ConvergesTo b M) (hab : EventuallyLE a b) :
    L ≤ M := by
  by_contra hlt
  push_neg at hlt
  have hε : 0 < (L - M) / 3 := div_pos (sub_pos.mpr hlt) (by norm_num)
  obtain ⟨x, y, hx, hy, hxy⟩ := ha.1 ((L - M) / 3) hε
  obtain ⟨x', y', hx', hy', hxy'⟩ := hb.1 ((L - M) / 3) hε
  have hyL : L ≤ y := ha.2.2 y hy
  have hMx : x' ≤ M := hb.2.1 x' hx'
  obtain ⟨N₁, h₁⟩ := hx
  obtain ⟨N₂, h₂⟩ := hy'
  obtain ⟨N₃, h₃⟩ := hab
  have hxL : x ≤ L := ha.2.1 x ⟨N₁, h₁⟩
  have hMy : M ≤ y' := hb.2.2 y' ⟨N₂, h₂⟩
  set n := max N₁ (max N₂ N₃)
  have e1 := h₁ n (le_max_left _ _)
  have e2 := h₂ n (le_trans (le_max_left _ _) (le_max_right _ _))
  have e3 := h₃ n (le_trans (le_max_right _ _) (le_max_right _ _))
  -- x ≤ a n ≤ b n ≤ y', with x ≥ L - (L-M)/3 and y' ≤ M + (L-M)/3
  have : L - (L - M) / 3 ≤ x := by linarith
  have : y' ≤ M + (L - M) / 3 := by linarith
  linarith

/-- **Squeeze.** If `a ≤ b ≤ c` eventually, `a → L`, `c → L` and `b → M`,
then `M = L`. -/
theorem ConvergesTo.squeeze {a b c : ℕ → K} {L M : K}
    (ha : ConvergesTo a L) (hb : ConvergesTo b M) (hc : ConvergesTo c L)
    (hab : EventuallyLE a b) (hbc : EventuallyLE b c) : M = L :=
  le_antisymm (hb.le_of_eventuallyLE hc hbc) (ha.le_of_eventuallyLE hb hab)

/-- The usual ε–N convergence, stated in `K`. Kept only as a bridge for
existing statements; new statements use `ConvergesTo`. -/
def TendstoEps (a : ℕ → K) (L : K) : Prop :=
  ∀ ε : K, 0 < ε → ∃ N : ℕ, ∀ n, N ≤ n → |a n - L| < ε

/-- ε–N convergence gives the located cut. -/
theorem convergesTo_of_tendstoEps {a : ℕ → K} {L : K} (h : TendstoEps a L) :
    ConvergesTo a L := by
  refine ⟨fun ε hε => ?_, ?_, ?_⟩
  · obtain ⟨N, hN⟩ := h (ε / 2) (half_pos hε)
    refine ⟨L - ε / 2, L + ε / 2, ⟨N, fun n hn => ?_⟩, ⟨N, fun n hn => ?_⟩, by linarith⟩
    · have := (abs_lt.mp (hN n hn)).1; linarith
    · have := (abs_lt.mp (hN n hn)).2; linarith
  · rintro x ⟨N, hN⟩
    by_contra hlt
    push_neg at hlt
    obtain ⟨M, hM⟩ := h (x - L) (sub_pos.mpr hlt)
    have h1 := hN (max N M) (le_max_left _ _)
    have h2 := (abs_lt.mp (hM (max N M) (le_max_right _ _))).2
    linarith
  · rintro y ⟨N, hN⟩
    by_contra hlt
    push_neg at hlt
    obtain ⟨M, hM⟩ := h (L - y) (sub_pos.mpr hlt)
    have h1 := hN (max N M) (le_max_left _ _)
    have h2 := (abs_lt.mp (hM (max N M) (le_max_right _ _))).1
    linarith

/-- The located cut gives ε–N convergence. -/
theorem tendstoEps_of_convergesTo {a : ℕ → K} {L : K} (h : ConvergesTo a L) :
    TendstoEps a L := by
  intro ε hε
  obtain ⟨x, y, ⟨N, hN⟩, ⟨M, hM⟩, hxy⟩ := h.1 (ε / 2) (half_pos hε)
  have hxL := h.2.1 x ⟨N, hN⟩
  have hLy := h.2.2 y ⟨M, hM⟩
  refine ⟨max N M, fun n hn => abs_lt.mpr ⟨?_, ?_⟩⟩
  · have := hN n (le_trans (le_max_left _ _) hn); linarith
  · have := hM n (le_trans (le_max_right _ _) hn); linarith

theorem convergesTo_iff_tendstoEps {a : ℕ → K} {L : K} :
    ConvergesTo a L ↔ TendstoEps a L :=
  ⟨tendstoEps_of_convergesTo, convergesTo_of_tendstoEps⟩

/-! ### The one point that uses the axiom -/

/-- A cut evaluation whose cuts are sequence cuts (`E.cut r = seqCut (seq r)`),
for instance the Cauchy sequences presenting a completion. -/
structure SeqEvaluation (R : Type*) (K : Type*) [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] where
  seq : R → ℕ → K

/-- The cut evaluation of a `SeqEvaluation`. -/
def SeqEvaluation.toCutEvaluation {R : Type*} (S : SeqEvaluation R K) :
    CutEvaluation R K :=
  ⟨fun r => seqCut (S.seq r)⟩

/-- **Under `[Coev E]`**, every presented sequence that is known to stay
between its lower and upper probes at `L` converges to `L`. This is where the
non-constructive axiom is spent; everything above is axiom-free. -/
theorem convergesTo_of_coev {R : Type*} (S : SeqEvaluation R K)
    [Coev S.toCutEvaluation] (r : R) {L : K} (hL : (seqCut (S.seq r)).Contains L) :
    ConvergesTo (S.seq r) L :=
  ⟨Coev.located (E := S.toCutEvaluation) r, hL⟩

end QOU.Core.CutLimit
