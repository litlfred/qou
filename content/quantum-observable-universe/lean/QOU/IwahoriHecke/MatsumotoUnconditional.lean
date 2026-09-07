import QOU.Machinery.CoxeterDihedralOrder
import QOU.IwahoriHecke.BruhatReflection

/-!
# The Matsumoto/Bruhat arc, with `DihedralExact` discharged

Everything in the arc — Matsumoto, the `T_w` basis, the subword property, Bruhat transitivity,
lifting — was proved conditional on `CoxeterRankTwo.DihedralExact` and stated hypothesis-free only
on **type `A`**, where `dihedralExact_le_three` supplies it.

`QOU.Machinery.CoxeterDihedralOrder.dihedralExact_full` supplies it for **every** Coxeter system.
This file re-states the arc with that plugged in.

## 🛑 One hypothesis survives, and it is not `DihedralExact`

`hfin : ∀ i j, i ≠ j → M i j ≠ 0` — **no infinite bond orders** — is a *separate* hypothesis and is
**not** discharged here. It enters through `not_isReduced_alternatingWord`, which needs a finite
`M i j` to bound the alternating word.

It is not an oversight of the cosine argument; that argument genuinely cannot see the `m = 0`
case. At `m = 0` the convention `π / 0 = 0` gives `c = −cos 0 = −1`, so the Chebyshev parameter is
`4c² − 2 = 2` and the recursion `x(k+2) = 2·x(k+1) − x k` with `x 0 = x 1 = 1` has the constant
solution `x k = 1`. The scalar therefore returns to its initial value at every `k` and distinguishes
nothing — which is correct, since the infinite dihedral group has no relation to detect.

✅ **That different argument is now made** — `CoxeterDihedralOrder.reflEnd_pair_pow_ne_one_of_infinite`
tracks the `αᵢ`-**coefficient** rather than the form value, gets `1 + 2k` from the shear, and so shows
`fᵢfⱼ` has genuinely infinite order at `m = 0`. That is exactly what the descent lemma needs to
refute its `m = 0` branch instead of excluding it.

🛑 **It is proved but not yet SPENT, deliberately.** Removing `hfin` means changing 17 theorem
signatures and 79 call sites across five merged files, one of which a sibling is actively
extending — against **no** consumer, since every Coxeter matrix in this corpus is
`CoxeterMatrix.Aₙ` and no infinite bond appears anywhere. So `hfin` stays in these statements until
someone wants it gone deliberately; the input is ready. Bean `qou-1u90`.

So the honest scope is: **every Coxeter system whose bond orders are all finite** — which includes
`Bₙ`, `Dₙ`, `E₆₇₈`, `F₄`, `H₃`, `H₄` and every `I₂(m)`, not merely `Aₙ`.

-- Ref: [matsumoto1964] DOI 10.1090/S0002-9904-1964-11211-9
-- Ref: [bjornerbrenti2005] Combinatorics of Coxeter Groups, Thm 2.2.2, Thm 3.3.1
-- Ref: [manuscript] beans qou-06h7, qou-1u90, qou-3k66
-/

namespace QOU.IwahoriHecke.MatsumotoUnconditional

open CoxeterSystem List
open QOU.Machinery.CoxeterBruhat QOU.Machinery.CoxeterDihedralOrder
open QOU.IwahoriHecke.BraidWord QOU.IwahoriHecke.Matsumoto
open QOU.IwahoriHecke.BruhatSubword QOU.IwahoriHecke.BruhatReflection

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

/-- Shorthand for the one surviving hypothesis: every bond order is finite. -/
def FiniteBonds : Prop := ∀ i j : B, i ≠ j → M i j ≠ 0

/-! ## Matsumoto and the `T_w` basis -/

/-- **Matsumoto's theorem for every finite-bond Coxeter system.** -/
theorem matsumoto_of_finiteBonds (hfin : FiniteBonds (M := M))
    {u v : List B} (hu : cs.IsReduced u) (hv : cs.IsReduced v)
    (huv : cs.wordProd u = cs.wordProd v) :
    BraidEquiv (fun a b => M a b) u v :=
  matsumoto' cs (dihedralExact_full cs) hfin hu hv huv

variable {R : Type*} [CommRing R] (q : R)

/-- **The `T_w` basis map for every finite-bond Coxeter system.** -/
theorem exists_Tw_of_finiteBonds (hfin : FiniteBonds (M := M)) :
    ∃ Tw : W → QOU.MathlibExt.IwahoriHecke.HeckeAlgebra R q (fun a b => M a b),
      ∀ l : List B, cs.IsReduced l →
        Tw (cs.wordProd l) = heckeWord q (fun a b => M a b) l :=
  QOU.IwahoriHecke.TwMatsumoto.exists_Tw_of_matsumoto cs q
    (fun _ _ hu hv huv => matsumoto_of_finiteBonds cs hfin hu hv huv)

/-! ## The Bruhat order -/

/-- **The subword property**, for every finite-bond Coxeter system. -/
theorem subword_property_of_finiteBonds (hfin : FiniteBonds (M := M))
    {u w : W} (h : BruhatLe cs u w) {ω : List B} (hred : cs.IsReduced ω)
    (hw : cs.wordProd ω = w) :
    ∃ ω' : List B, ω' <+ ω ∧ cs.wordProd ω' = u :=
  subword_property cs (dihedralExact_full cs) hfin h hred hw

/-- **Transitivity**, for every finite-bond Coxeter system. -/
theorem bruhatLe_trans_of_finiteBonds (hfin : FiniteBonds (M := M))
    {u v w : W} (h₁ : BruhatLe cs u v) (h₂ : BruhatLe cs v w) : BruhatLe cs u w :=
  bruhatLe_trans cs (dihedralExact_full cs) hfin h₁ h₂

/-- **The lifting property**, for every finite-bond Coxeter system. -/
theorem lifting_of_finiteBonds (hfin : FiniteBonds (M := M))
    {u w : W} (h : BruhatLe cs u w) {s : B}
    (hsw : cs.IsRightDescent w s) (hsu : cs.IsRightDescent u s) :
    BruhatLe cs (u * cs.simple s) (w * cs.simple s) :=
  lifting cs (dihedralExact_full cs) hfin h hsw hsu

/-- **`ReflLe → BruhatLe`**, for every finite-bond Coxeter system. -/
theorem bruhatLe_of_reflLe_of_finiteBonds (hfin : FiniteBonds (M := M))
    {u w : W} (h : ReflLe cs u w) : BruhatLe cs u w :=
  bruhatLe_of_reflLe cs (dihedralExact_full cs) hfin h

/-! ## The finite-bond hypothesis is satisfied by the classical families -/

theorem finiteBonds_An (n : ℕ) : FiniteBonds (M := CoxeterMatrix.Aₙ n) :=
  fun i j hij => An_ne_zero n i j hij

theorem finiteBonds_of_pos (hpos : ∀ i j : B, i ≠ j → 0 < M i j) : FiniteBonds (M := M) :=
  fun i j hij => (hpos i j hij).ne'

end QOU.IwahoriHecke.MatsumotoUnconditional
