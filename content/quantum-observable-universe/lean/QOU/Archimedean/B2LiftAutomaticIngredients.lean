/-
# B2 τ-lift — the *automatic* (moduli-independent) ingredients, Lean-locked

Branch `claude/q-deformed-saddle-offsets-bdn992`. Bean `qou-8mbd`. Follows the two
2026-08-02 audits `2026-08-02-hodge-lift-bring-h1-model.md` (§2 "ρ ↔ Hodge
conjugation is CANONICAL/automatic"; nome equivariance `τ(q̄) = −conj(τ(q))`
forced by the nome) and `2026-08-02-moc-gauss-manin-not-derivable.md` (the MOC
period map `Φ` is the single irreducible open wall). Compute:
`computations/alpha_em/hodge_lift_bring_model.py` (10/10 PASS).

Those audits establish that two of the B2 lift's would-be-open ingredients carry
**no arithmetic content** — they hold for *any* moduli — so they are NOT open
fields of the lift. This file Lean-locks the two of them that are still
prose/compute-only, sorry-free in Lean core (no Mathlib), sharpening exactly
what the single open MOC field (`PeriodMapWeightReduction.PeriodMapWeight`, left
uninstantiated) must still carry:

## Brick 1 — nome exponent-group equivariance (audit §2, Python check 3)

The nome `q = e^{2πiτ}` makes the three modulus-involutions the *exponent*
involutions `τ ↦ −τ` (bar/inversion `q ↦ q⁻¹`) and `τ ↦ ½ − τ` (channel-swap
`q ↦ −q⁻¹`). This is a **homomorphism fact**, not a coincidence at the two
degenerate points. We model the quarter-period exponent lattice as the finite
group `Z4` and the nome as the group homomorphism `unitExp : Z4 → GInt` onto the
Gaussian units `{1, i, −1, −i}` (the values the nome takes at the degenerate
locus). Then, over the whole exponent group:

* `unitExp_add_eq_mul` — `unitExp` is a genuine group homomorphism
  (`e(a+b) = e(a)·e(b)`), faithful (`unitExp_distinct`);
* `unitExp_neg_eq_conj` — **`τ ↦ −τ` ↔ `q ↦ q⁻¹ = q̄`** (inverse = conjugation
  on the unit circle): exponent negation is nome conjugation;
* `unitExp_channelSwap` — **`τ ↦ ½ − τ` ↔ `q ↦ −q⁻¹ = −q̄`**: the half-shift is
  the channel swap, and it FIXES the degenerate pair `{i, −i}` (the exponent-level
  refinement of `SigmaJGeometricCarrier.transpose_fixes_degenerate_pair`).

Brick 1 generalizes the two-point facts `bar_exchanges_degenerate_pair` /
`transpose_fixes_degenerate_pair` to the full unit group with the homomorphism
structure explicit — the exact content of audit §2's "forced by the nome,
automatic for any moduli".

## Brick 2 — Weil vs Galois real structures compose to complex conjugation

Extends the just-landed `HodgeWeilRealStructure.lean` (`c = SWAP∘conj` antilinear
Weil real structure vs `F = SWAP` ℂ-linear Galois structure on the explicit
`H¹(Bring) = H^{1,0} ⊕ H^{0,1}` model). The audit §2 "`c` is canonical / carries
no arithmetic content" is sharpened by locking the algebra RELATING the two
involutions:

* `weil_galois_compose` — **`c ∘ F = F ∘ c = conjV`**: the Weil and Galois real
  structures differ exactly by complex conjugation (the standard fact for a
  variety over ℝ). `conjV` is itself an antilinear involution
  (`conjV_involutive`, `conjV_antilinear`);
* `c_swaps_hodge_other` — `c(0, b) = (b̄, 0)`: `c` maps `H^{0,1} → H^{1,0}`,
  completing the Hodge-piece swap begun by the existing `c_swaps_hodge`;
* `c_fixed_iff_real_form` — **complete** characterization `Fix(c) = {(w, w̄)}`
  (the existing `c_fixes_real_form` gave only `⊇`); together with
* `FGal_fixed_iff` — `Fix(F) = {(a, a)}` (the diagonal) — this distinguishes the
  two real forms: `c`'s fixed locus is the Weil real cohomology `H¹(ℝ)`, `F`'s is
  the ℂ-linear diagonal. They are different subspaces, so the antilinear/linear
  distinction has fixed-locus content.

## Honesty (STRICT, AGENTS.md §"Axiomatization is NOT a Proof")

Everything here is **moduli-independent / automatic** — it is exactly the part of
the B2 lift that carries no arithmetic content. **No `PeriodMapWeight` / period
map `Φ` / MOC instance is fabricated anywhere.** The single open wall (the
categorical τ-functor producing the holomorphic period map `Φ`) is untouched;
these bricks only strip the *already-automatic* ingredients into machine-checked
form so the residual open field is seen in isolation. Nothing wires `1/(8π)` to
production; the identification stays phase-4.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-/
import Init.Data.Int.Basic
import QOU.Archimedean.SigmaJGeometricCarrier
import QOU.Archimedean.HodgeWeilRealStructure

namespace QOU.Archimedean.B2LiftAutomaticIngredients

open QOU.Archimedean.SigmaJGeometricCarrier
open QOU.Archimedean.SigmaJGeometricCarrier.GInt
open QOU.Archimedean.HodgeWeilRealStructure

/-! ## Brick 1 — the nome exponent group `Z4 → {1, i, −1, −i}` -/

/-- The quarter-period exponent lattice `ℤ/4ℤ` — the group of nome exponents `τ`
modulo the period, on the degenerate stratum where `q ∈ {1, i, −1, −i}`. Lean-core
inductive (no Mathlib `ZMod`), so every law below is `decide`/`rfl`. -/
inductive Z4 where
  | z0 | z1 | z2 | z3
  deriving DecidableEq, Repr

namespace Z4

/-- Exponent addition (mod 4) — the additive group law `τ + τ'`. -/
def add : Z4 → Z4 → Z4
  | z0, y => y
  | z1, z0 => z1 | z1, z1 => z2 | z1, z2 => z3 | z1, z3 => z0
  | z2, z0 => z2 | z2, z1 => z3 | z2, z2 => z0 | z2, z3 => z1
  | z3, z0 => z3 | z3, z1 => z0 | z3, z2 => z1 | z3, z3 => z2

/-- Exponent negation `τ ↦ −τ` (the involution the bar/inversion `q ↦ q⁻¹`
lifts to). -/
def neg : Z4 → Z4
  | z0 => z0 | z1 => z3 | z2 => z2 | z3 => z1

/-- `−(−τ) = τ`: exponent negation is an involution. -/
theorem neg_neg (n : Z4) : neg (neg n) = n := by cases n <;> rfl

end Z4

/-- **The nome `q = e^{2πiτ}` on the degenerate stratum**, as a map from the
exponent group to the Gaussian units: `e(0)=1`, `e(1)=i`, `e(2)=−1`, `e(3)=−i`
(the fourth roots of unity `i^n`). -/
def unitExp : Z4 → GInt
  | Z4.z0 => one
  | Z4.z1 => I
  | Z4.z2 => neg one
  | Z4.z3 => neg I

/-- The four nome values, pinned. -/
theorem unitExp_values :
    unitExp Z4.z0 = one ∧ unitExp Z4.z1 = I
      ∧ unitExp Z4.z2 = neg one ∧ unitExp Z4.z3 = neg I := by decide

/-- The half-period value `e(2) = −1` (`unitExp z2` is the order-2 element — the
`½`-shift that realizes the channel swap below). -/
theorem unitExp_half : unitExp Z4.z2 = neg one := rfl

/-- **`unitExp` is a group homomorphism** `e(a+b) = e(a)·e(b)`: the nome turns
exponent addition into unit multiplication. (16-case `decide`; breaks under any
mis-assignment of the four roots.) -/
theorem unitExp_add_eq_mul (a b : Z4) :
    unitExp (Z4.add a b) = unitExp a * unitExp b := by
  cases a <;> cases b <;> decide

/-- **`unitExp` is faithful** — the four nome values are pairwise distinct, so the
homomorphism is injective onto the units (the exponent group law is non-vacuous
content, not a collapse). -/
theorem unitExp_distinct :
    unitExp Z4.z0 ≠ unitExp Z4.z1 ∧ unitExp Z4.z0 ≠ unitExp Z4.z2
      ∧ unitExp Z4.z0 ≠ unitExp Z4.z3 ∧ unitExp Z4.z1 ≠ unitExp Z4.z2
      ∧ unitExp Z4.z1 ≠ unitExp Z4.z3 ∧ unitExp Z4.z2 ≠ unitExp Z4.z3 := by decide

/-- **`τ ↦ −τ` ↔ `q ↦ q⁻¹ = q̄`.** Exponent negation is nome conjugation:
`e(−τ) = conj(e(τ))` for every exponent (on the unit circle `q⁻¹ = q̄`). This is
audit §2's `τ(q̄) = −conj(τ(q))` read as an exponent-group identity — automatic,
moduli-independent. -/
theorem unitExp_neg_eq_conj (n : Z4) :
    unitExp (Z4.neg n) = GInt.conj (unitExp n) := by
  cases n <;> decide

/-- **`τ ↦ ½ − τ` ↔ `q ↦ −q⁻¹ = −q̄`.** The channel-swap half-shift `z2 + (−τ)`
maps to `−conj(e(τ))`. Note it FIXES the degenerate pair (`n = z1 ↦ z1`,
`n = z3 ↦ z3`): the exponent-level refinement of
`SigmaJGeometricCarrier.transpose_fixes_degenerate_pair`. -/
theorem unitExp_channelSwap (n : Z4) :
    unitExp (Z4.add Z4.z2 (Z4.neg n)) = neg (GInt.conj (unitExp n)) := by
  cases n <;> decide

/-- Bridge to the degenerate-locus shadow (`SigmaJGeometricCarrier`): the nome's
value at exponent `1` is `q = i` and at exponent `3` is `q = −i`, and negating the
exponent of `q = i` recovers the bar exchange `q = i ↦ q = −i`
(`bar_exchanges_degenerate_pair` is the `n = z1` case of `unitExp_neg_eq_conj`). -/
theorem unitExp_recovers_bar_exchange :
    unitExp Z4.z1 = I ∧ unitExp Z4.z3 = neg I
      ∧ unitExp (Z4.neg Z4.z1) = GInt.conj (unitExp Z4.z1) := by decide

/-! ## Brick 2 — Weil vs Galois real structures on the `H¹(Bring)` model -/

/-- `conjV` (whole-`H¹` complex conjugation) is an involution — it is the third
real structure, `c ∘ F = F ∘ c` (see `weil_galois_compose`). -/
theorem conjV_involutive (v : H1) : conjV (conjV v) = v := by
  obtain ⟨a, b⟩ := v
  simp only [conjV, conjPiece_conjPiece]

/-- `conjV` is antilinear — `conjV(λ·v) = λ̄·conjV(v)` (uses `conj_mul`). Together
with `conjV_involutive` this makes `conjV` an antilinear involution like `c`, but
one that does NOT swap the Hodge pieces (it is `c ∘ F`). -/
theorem conjV_antilinear (l : GInt) (v : H1) :
    conjV (smul l v) = smul (GInt.conj l) (conjV v) := by
  obtain ⟨a, b⟩ := v
  simp only [conjV, smul, conjPiece, Prod.mk.injEq]
  refine ⟨?_, ?_⟩ <;> (funext k; exact conj_mul _ _)

/-- **`c ∘ F = F ∘ c = conjV`** — the Weil real structure and the Galois real
structure differ exactly by complex conjugation (the standard `c = conj ∘ F`
relation for a real variety). Both compositions strip the `SWAP` and leave pure
coordinate conjugation. This is what makes the antilinear `c`, not the linear
`F`, the Hodge conjugation: they are conjugate-related, not equal. -/
theorem weil_galois_compose (v : H1) :
    cWeil (FGal v) = conjV v ∧ FGal (cWeil v) = conjV v := by
  obtain ⟨a, b⟩ := v
  exact ⟨rfl, rfl⟩

/-- **`c` swaps the OTHER Hodge piece** — `c(0, b) = (b̄, 0)`: maps `H^{0,1}`
(first slot zero) into `H^{1,0}` (second slot zero). Completes `c_swaps_hodge`
(which handled `H^{1,0} → H^{0,1}`); together they show `c` interchanges the two
pieces both ways. -/
theorem c_swaps_hodge_other (b : Piece) :
    cWeil (fun _ => GInt.zero, b) = (conjPiece b, fun _ => GInt.zero) := by
  simp only [cWeil, SWAP, conjV, conjPiece_zero]

/-- **`Fix(c) = {(w, w̄)}` — the complete real-form characterization.** A vector is
`c`-fixed iff its `H^{0,1}` part is the conjugate of its `H^{1,0}` part. The
existing `c_fixes_real_form` proved only `⊇` (every `(w, w̄)` is fixed); this is
the iff, so `Fix(c)` is *exactly* the Weil real form `H¹(ℝ)`, `dim_ℝ = 8`. -/
theorem c_fixed_iff_real_form (v : H1) :
    cWeil v = v ↔ v.2 = conjPiece v.1 := by
  obtain ⟨a, b⟩ := v
  constructor
  · intro h
    simp only [cWeil, SWAP, conjV, Prod.mk.injEq] at h
    exact h.2.symm
  · intro h
    dsimp only at h
    rw [h]
    exact c_fixes_real_form a

/-- **`Fix(F) = {(a, a)}` — the Galois fixed locus is the diagonal**, NOT the real
form `{(w, w̄)}`. A vector is `F`-fixed iff its two Hodge parts are equal. This
distinguishes the two real structures at the level of fixed loci: `c`-fixed means
`H^{0,1} = conj(H^{1,0})` (`c_fixed_iff_real_form`); `F`-fixed means
`H^{0,1} = H^{1,0}`. Different subspaces — the antilinear/linear distinction has
fixed-locus content. -/
theorem FGal_fixed_iff (v : H1) :
    FGal v = v ↔ v.2 = v.1 := by
  obtain ⟨a, b⟩ := v
  constructor
  · intro h
    simp only [FGal, SWAP, Prod.mk.injEq] at h
    exact h.1
  · intro h
    dsimp only at h
    rw [h]
    rfl

end QOU.Archimedean.B2LiftAutomaticIngredients
