import Mathlib.Tactic

/-!
# The bar-odd channel is the ι-odd antisymmetric off-diagonal contraction

**Bar-grade selection rule for the 5₂ state-integral chirality split.**

The Andersen–Kashaev state integral for `5₂`, frame-reduced, splits (A1,
`qbeta-5two-chirality-state-integral`, derived two independent ways) into a
bar-even *index* channel and a bar-odd *chirality* channel:
$$\hat Z \;=\; R^{1/8}\,\underbrace{H^{+}_{1}H^{-}_{1}}_{\text{bar-even}}
   \;+\; i\Bigl(-\tfrac{R^{1/8}}{2}\Bigr)\,
   \underbrace{\bigl(\beta\,H^{+}_{2}H^{-}_{0} - \beta^{-1}H^{+}_{0}H^{-}_{2}\bigr)}
   _{\text{bar-odd}} .$$

Writing `p := H⁺₂H⁻₀` and `q := H⁺₀H⁻₂`, the bar-odd home is the β-graded
**antisymmetric off-diagonal contraction**
$$\omega(\beta,p,q) \;=\; \beta\,p - \beta^{-1}q .$$

The **amphichiral involution** `ι : (β,p,q) ↦ (β⁻¹, q, p)` swaps the two
off-diagonal products *and* inverts the modulus (`β ↔ β⁻¹` is the bar action on
the cusp modulus, `τ ↦ -τ̄`).  This file proves the structural facts that
localise the whole 5₂ bar-odd frontier:

* `omega_iota_odd` — `ω` is **ι-odd**: `ω(ι(β,p,q)) = -ω(β,p,q)`.
* `sEven_iota_invariant` — the companion `s(β,p,q) = β p + β⁻¹q` is **ι-even**.
* `omega_of_iotaFixed` / `omega_zero_on_iotaFixed` — on the **ι-fixed locus**
  (`β²=1`, `p=q`) the contraction **vanishes**.  This locus is simultaneously
  (i) the *amphichiral* locus — reproducing the corpus fact `V(4₁)_odd = 0`
  (`4₁` amphichiral ⇒ `u=0`, `CS=0` ⇒ ι-fixed) — and (ii) the *search grade*
  of the B-tranche walls B1.2 (the symmetric GK bilinear) and B1.3 (a single
  span vector), both **ι-even / ι-fixed objects**.  Hence those searches were
  structurally on `ω`'s zero locus: an ι-even object cannot carry the ι-odd
  bar-odd datum.
* `omega_ne_zero_imp_chiral` — contrapositive: a nonzero bar-odd datum
  **forces** a chiral (non-ι-fixed) knot.  This is the structural reason the
  frontier needed `5₂` (chiral) and not `4₁` (amphichiral).

**Scope.**  This is a *selection rule*, not a bridge.  It says which algebraic
object carries the bar-odd datum (the ι-odd antisymmetric off-diagonal), and
therefore why the ι-even searches returned nothing.  It does **not** derive the
anchor-dependent `c₃` swing: the numerical companion
(`qbeta_5two_barodd_antisym_offdiagonal_probe.py`) shows the ι-odd home is
*anchor-smooth* (≈ 4.6 ppm across the muon↔proton anchors) while `c₃` swings
≈ 3.47 %, so `ω` alone cannot realise the swing — the residual is the
anchor-dependent meridian-holonomy deformation `q₀ ↦ u`, not a smoother object
choice.  Comparison to observed only; no `c_k` is wired; nothing here inverts
`Q_β`/CODATA.

Generic field throughout (§7c base-ring): the substrate→archimedean wall is not
crossed — no ordering, no `Real.*`, no numerical `q₀`.
-/

namespace QOU.QBeta.BarOddAntisymOffDiagonal

variable {F : Type*} [Field F]

/-- The β-graded antisymmetric off-diagonal contraction — the bar-odd channel of
the frame-reduced `5₂` state integral (A1 chirality split, `Im Ẑ` up to the
`-R^{1/8}/2` chirality dressing).  `p = H⁺₂H⁻₀`, `q = H⁺₀H⁻₂`, `β` the cusp
modulus. -/
def omega (β p q : F) : F := β * p - β⁻¹ * q

/-- The ι-even companion — the bar-even *index* channel shape.  Symmetric under
the amphichiral involution (see `sEven_iota_invariant`); this is the grade the
symmetric GK bilinear (B1.2) and the span-vector search (B1.3) live in. -/
def sEven (β p q : F) : F := β * p + β⁻¹ * q

/-- **`ω` is ι-odd.**  The amphichiral involution `ι : (β,p,q) ↦ (β⁻¹,q,p)`
(swap the off-diagonal products, invert the modulus) sends `ω` to `-ω`.  This is
the algebraic bar-oddness of the chirality channel. -/
theorem omega_iota_odd (β p q : F) (hβ : β ≠ 0) :
    omega β⁻¹ q p = - omega β p q := by
  unfold omega
  rw [inv_inv]
  ring

/-- **The companion `s` is ι-even.**  In contrast to `ω`, the bar-even index
shape is invariant under `ι` — so it can only ever produce ι-fixed values. -/
theorem sEven_iota_invariant (β p q : F) (hβ : β ≠ 0) :
    sEven β⁻¹ q p = sEven β p q := by
  unfold sEven
  rw [inv_inv]
  ring

/-- **Direct vanishing on the ι-fixed locus.**  If the modulus is self-dual
(`β² = 1`, i.e. `β⁻¹ = β`) and the two off-diagonal products agree (`p = q`),
the bar-odd contraction is `0`.  This is the amphichiral / symmetric-search
locus. -/
theorem omega_of_iotaFixed (β p q : F) (hβ : β ≠ 0) (hsq : β * β = 1)
    (hpq : p = q) : omega β p q = 0 := by
  have hinv : β⁻¹ = β := by
    rw [inv_eq_of_mul_eq_one_right hsq]
  unfold omega
  rw [hinv, hpq]
  ring

/-- **Parity route to the same fact.**  On any ι-fixed triple, ι-oddness forces
`ω = -ω`, hence `2ω = 0`, hence `ω = 0`.  Stated via the fixed-point hypotheses
`β⁻¹ = β` (self-dual modulus) and `q = p` so that `ι(β,p,q) = (β,p,q)`; needs
only `2 ≠ 0` in `F`.  Mirrors the physics: an amphichiral (ι-fixed) datum has no
bar-odd part. -/
theorem omega_zero_on_iotaFixed (β p q : F) (hβ : β ≠ 0)
    (hself : β⁻¹ = β) (hpq : q = p) (h2 : (2 : F) ≠ 0) :
    omega β p q = 0 := by
  -- ι fixes (β,p,q): ω(β,p,q) = ω(β⁻¹,q,p) = -ω(β,p,q).
  have hfix : omega β⁻¹ q p = omega β p q := by rw [hself, hpq]
  have hodd : omega β⁻¹ q p = - omega β p q := omega_iota_odd β p q hβ
  rw [hfix] at hodd
  have hself2 : omega β p q = - omega β p q := hodd
  have h2w : (2 : F) * omega β p q = 0 := by linear_combination hself2
  exact (mul_eq_zero.mp h2w).resolve_left h2

/-- **A nonzero bar-odd datum forces a chiral knot.**  Contrapositive of
`omega_of_iotaFixed`: if `ω(β,p,q) ≠ 0` then the triple is *not* ι-fixed — the
modulus is not self-dual or the off-diagonal products differ.  This is the
structural reason the bar-odd `c₃` frontier required the chiral `5₂` and could
not be sourced from the amphichiral `4₁` (`V(4₁)_odd = 0`). -/
theorem omega_ne_zero_imp_chiral (β p q : F) (hβ : β ≠ 0)
    (hne : omega β p q ≠ 0) : ¬ (β * β = 1 ∧ p = q) := by
  rintro ⟨hsq, hpq⟩
  exact hne (omega_of_iotaFixed β p q hβ hsq hpq)

end QOU.QBeta.BarOddAntisymOffDiagonal
