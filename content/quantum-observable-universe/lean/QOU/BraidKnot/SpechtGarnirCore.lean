import QOU.BraidKnot.Specht

/-!
# QOU.BraidKnot.SpechtGarnirCore — toward the Garnir straightening (brick-4 spanning)

The spanning half of the standard-basis theorem (`polytabloid_garnir_core` in
`SpechtSpanningCore`) is the straightening algorithm: every polytabloid is a
combination of *standard* polytabloids, via the **Garnir relations**. This module
builds the full algebraic machinery of the Garnir relation **sorry-free**,
reducing the straightening core to a single geometric input (a two-column
row-index bound) plus the dominance termination measure.

## Landed (all sorry-free)

| § | Declaration | Statement |
|---|---|---|
| 1 | `polytabloid_rep_colStab` | column-alternating: `σ·e_t = sgn(σ)·e_t` for `σ ∈ C_t` |
| 1b | `conjStab`, `rep_polytabloid` | equivariance `rep σ (e_t) = e_{σ·t}` (every `σ`) |
| 2 | `antisym`, `antisym_sum`, `antisym_zsmul` | the antisymmetriser `b_H` and its linearity |
| 2 | `antisym_rep`, `antisym_eq_zero` | alternating + involution-vanishing of `b_H` |
| 2 | `antisym_of_eq_zero` | per-tabloid vanishing `b_H ⟦s⟧ = 0` from a row-fixing involution |
| 3 | `antisym_colStab` | column collapse `b_H e_t = |H|·e_t` for `H ≤ C_t` |
| 3 | `antisym_polytabloid` | `b_H(e_t) = Σ_{σ∈H} sgn(σ)·e_{σ·t}` |
| 5 | `tabloid_swap_sameRow`, `antisym_swap_eq_zero` | a same-row transposition fixes `⟦s⟧`, hence kills it |
| 5 | `exists_sameRow_of_card_lt` | row pigeonhole: `|X| > #rows ⟹ two labels collide` |
| 6 | `suppSubgroup`, `swap_mem_suppSubgroup` | the Garnir subgroup `S_X` (supported on `X`) |
| 7 | `antisym_supp_polytabloid_eq_zero` | the Garnir vanishing `b_{S_X} e_t = 0` (modulo the bound) |
| 7 | `garnir_relation` | **the Garnir relation** `Σ_{σ∈S_X} sgn(σ)·e_{σ·t} = 0` (modulo the bound) |

## Residual for `polytabloid_garnir_core` (not in this file)

Two geometric inputs remain: (a) the `A ∪ B` Garnir-set construction from a
non-standard violation, supplying the row-index bound `rowPattern (π·t) l < μ'_j`
for all `π ∈ C_t` with `|X| > μ'_j`; and (b) the **dominance** termination
measure under which the straightening rewrite `e_t = Σ (more dominant)` strictly
decreases. Both depend on the dominance order on tabloids, which Mathlib lacks.
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtGarnirCore

open QOU.BraidKnot.Specht
open Equiv (Perm)

variable {k : Type} [CommRing k]
variable {μ : YoungDiagram}

/-- **Column-alternating property.** A column permutation acts on `e_t` by its sign:
`rep σ (e_t) = sgn(σ) · e_t` for `σ ∈ C_t`. -/
theorem polytabloid_rep_colStab (t : Tableau μ) {σ : Perm (Fin (nOf μ))}
    (hσ : σ ∈ colStab t) :
    Mtab.rep μ σ (polytabloid (k := k) t) = (Equiv.Perm.sign σ : ℤ) • polytabloid (k := k) t := by
  unfold polytabloid
  rw [map_sum, Finset.smul_sum]
  refine Fintype.sum_bijective (fun π : colStab t => (⟨σ, hσ⟩ * π : colStab t))
    (Equiv.mulLeft (⟨σ, hσ⟩ : colStab t)).bijective _ _ (fun π => ?_)
  -- LHS summand at π = RHS summand at σ·π
  have hsq : (Equiv.Perm.sign σ : ℤ) * (Equiv.Perm.sign σ : ℤ) = 1 := by
    simp [← Units.val_mul, Int.units_mul_self]
  have hco : ((⟨σ, hσ⟩ * π : colStab t) : Perm (Fin (nOf μ))) = σ * (π : Perm (Fin (nOf μ))) := by
    rw [Subgroup.coe_mul]
  rw [map_zsmul, Mtab.rep_of,
    ← mul_smul (Equiv.Perm.sign σ : ℤ)
      (Equiv.Perm.sign ((⟨σ, hσ⟩ * π : colStab t) : Perm (Fin (nOf μ))) : ℤ)
      (Mtab.of (k := k) (((⟨σ, hσ⟩ * π : colStab t) : Perm (Fin (nOf μ))) • t)),
    hco, map_mul, Units.val_mul, ← mul_assoc, hsq, one_mul, mul_smul]

/-! ## 1b. Equivariance `rep σ (e_t) = e_{σ·t}`

The permutation action carries one polytabloid to another: `σ · e_t = e_{σ·t}`
for **every** `σ` (not just `σ ∈ C_t`). The proof reindexes the column-stabiliser
sum of `e_{σt}` by conjugation `π ↦ σπσ⁻¹`, which is a bijection
`C_t ≃ C_{σ·t}` because `colStab` is the stabiliser of the (equivariant) column
pattern. Together with §1's column-alternating law this is what lets a Garnir
element `Σ_σ sgn(σ)·σ` act on `e_t` as a combination of polytabloids `e_{σt}`.
-/

/-- Conjugation sends the column stabiliser of `t` into that of `σ · t`:
`π ∈ C_t ⟹ σπσ⁻¹ ∈ C_{σ·t}`. -/
theorem conj_mem_colStab_smul {σ π : Perm (Fin (nOf μ))} (t : Tableau μ)
    (hπ : π ∈ colStab t) : σ * π * σ⁻¹ ∈ colStab (σ • t) := by
  rw [mem_colStab] at hπ
  rw [mem_colStab, colPattern_smul, mul_smul, mul_smul,
    ← mul_smul σ⁻¹ σ (colPattern t), inv_mul_cancel, one_smul, hπ]

/-- **Conjugation bijection** `C_t ≃ C_{σ·t}`, `π ↦ σπσ⁻¹`. -/
def conjStab (σ : Perm (Fin (nOf μ))) (t : Tableau μ) :
    colStab t ≃ colStab (σ • t) where
  toFun π := ⟨σ * (π : Perm (Fin (nOf μ))) * σ⁻¹, conj_mem_colStab_smul t π.2⟩
  invFun ρ := ⟨σ⁻¹ * (ρ : Perm (Fin (nOf μ))) * σ, by
    have h := conj_mem_colStab_smul (σ := σ⁻¹) (σ • t) ρ.2
    rwa [inv_inv, ← mul_smul, inv_mul_cancel, one_smul] at h⟩
  left_inv π := by
    ext1
    show σ⁻¹ * (σ * (π : Perm (Fin (nOf μ))) * σ⁻¹) * σ = (π : Perm (Fin (nOf μ)))
    rw [mul_assoc σ (π : Perm (Fin (nOf μ))) σ⁻¹, inv_mul_cancel_left, inv_mul_cancel_right]
  right_inv ρ := by
    ext1
    show σ * (σ⁻¹ * (ρ : Perm (Fin (nOf μ))) * σ) * σ⁻¹ = (ρ : Perm (Fin (nOf μ)))
    rw [mul_assoc σ⁻¹ (ρ : Perm (Fin (nOf μ))) σ, mul_inv_cancel_left, mul_inv_cancel_right]

/-- **Equivariance of the polytabloid.** `rep σ (e_t) = e_{σ·t}` for every `σ`. -/
theorem rep_polytabloid (σ : Perm (Fin (nOf μ))) (t : Tableau μ) :
    Mtab.rep μ σ (polytabloid (k := k) t) = polytabloid (k := k) (σ • t) := by
  unfold polytabloid
  rw [map_sum]
  refine Fintype.sum_bijective (conjStab σ t) (conjStab σ t).bijective _ _ (fun π => ?_)
  have hsgn : Equiv.Perm.sign ((conjStab σ t π : Perm (Fin (nOf μ))))
      = Equiv.Perm.sign (π : Perm (Fin (nOf μ))) := by
    show Equiv.Perm.sign (σ * (π : Perm (Fin (nOf μ))) * σ⁻¹)
      = Equiv.Perm.sign (π : Perm (Fin (nOf μ)))
    rw [map_mul, map_mul, map_inv, mul_comm (Equiv.Perm.sign σ),
      mul_assoc, mul_inv_cancel, mul_one]
  have harg : ((conjStab σ t π : Perm (Fin (nOf μ))) • (σ • t))
      = σ • ((π : Perm (Fin (nOf μ))) • t) := by
    show (σ * (π : Perm (Fin (nOf μ))) * σ⁻¹) • (σ • t) = σ • ((π : Perm (Fin (nOf μ))) • t)
    rw [mul_smul, mul_smul, ← mul_smul σ⁻¹ σ t, inv_mul_cancel, one_smul]
  rw [map_zsmul, Mtab.rep_of, hsgn, harg]

/-! ## 2. The abstract antisymmetriser

For a finite group `H ≤ S_n`, the antisymmetriser `b_H x = Σ_{σ∈H} sgn(σ)·(σ·x)`.
Two abstract facts power every Garnir relation:

* `antisym_rep` — `b_H` is *alternating*: `τ·(b_H x) = sgn(τ)·b_H x` for `τ ∈ H`.
* `antisym_eq_zero` — if a sign-`(−1)` involution `τ ∈ H` *fixes* `x`, then `b_H x = 0`
  (the sign-reversing pairing `σ ↦ στ` cancels termwise — no characteristic
  assumption). This is the vanishing that makes a Garnir element kill `e_t`.
-/

/-- The **antisymmetriser** over a finite subgroup `H`. -/
noncomputable def antisym (H : Subgroup (Perm (Fin (nOf μ)))) [Fintype ↥H]
    (x : Mtab (k := k) μ) : Mtab (k := k) μ :=
  ∑ σ : H, (Equiv.Perm.sign (σ : Perm (Fin (nOf μ))) : ℤ) • Mtab.rep μ (σ : Perm (Fin (nOf μ))) x

/-- `b_H` distributes over finite sums (it is additive: `rep` is linear). -/
theorem antisym_sum (H : Subgroup (Perm (Fin (nOf μ)))) [Fintype ↥H]
    {ι : Type*} (s : Finset ι) (f : ι → Mtab (k := k) μ) :
    antisym (k := k) H (∑ i ∈ s, f i) = ∑ i ∈ s, antisym (k := k) H (f i) := by
  unfold antisym
  simp_rw [map_sum, Finset.smul_sum]
  rw [Finset.sum_comm]

/-- `b_H` commutes with `ℤ`-scaling. -/
theorem antisym_zsmul (H : Subgroup (Perm (Fin (nOf μ)))) [Fintype ↥H]
    (c : ℤ) (x : Mtab (k := k) μ) :
    antisym (k := k) H (c • x) = c • antisym (k := k) H x := by
  unfold antisym
  rw [Finset.smul_sum]
  refine Finset.sum_congr rfl (fun σ _ => ?_)
  rw [map_zsmul, smul_comm]

/-- **Alternating property.** `τ · (b_H x) = sgn(τ) · b_H x` for `τ ∈ H`. -/
theorem antisym_rep (H : Subgroup (Perm (Fin (nOf μ)))) [Fintype ↥H]
    {τ : Perm (Fin (nOf μ))} (hτ : τ ∈ H) (x : Mtab (k := k) μ) :
    Mtab.rep μ τ (antisym (k := k) H x) = (Equiv.Perm.sign τ : ℤ) • antisym (k := k) H x := by
  unfold antisym
  rw [map_sum, Finset.smul_sum]
  refine Fintype.sum_bijective (fun σ : H => (⟨τ, hτ⟩ * σ : H))
    (Equiv.mulLeft (⟨τ, hτ⟩ : H)).bijective _ _ (fun σ => ?_)
  have hsq : (Equiv.Perm.sign τ : ℤ) * (Equiv.Perm.sign τ : ℤ) = 1 := by
    simp [← Units.val_mul, Int.units_mul_self]
  have hco : ((⟨τ, hτ⟩ * σ : H) : Perm (Fin (nOf μ))) = τ * (σ : Perm (Fin (nOf μ))) := by
    rw [Subgroup.coe_mul]
  rw [map_zsmul,
    show Mtab.rep μ τ (Mtab.rep μ (σ : Perm (Fin (nOf μ))) x)
        = Mtab.rep μ (τ * (σ : Perm (Fin (nOf μ)))) x from by rw [map_mul]; rfl,
    ← mul_smul (Equiv.Perm.sign τ : ℤ)
      (Equiv.Perm.sign ((⟨τ, hτ⟩ * σ : H) : Perm (Fin (nOf μ))) : ℤ)
      (Mtab.rep μ ((⟨τ, hτ⟩ * σ : H) : Perm (Fin (nOf μ))) x),
    hco]
  congr 1
  rw [map_mul, Units.val_mul, ← mul_assoc, hsq, one_mul]

/-- **Vanishing.** A sign-`(−1)` involution `τ ∈ H` fixing `x` forces `b_H x = 0`. -/
theorem antisym_eq_zero (H : Subgroup (Perm (Fin (nOf μ)))) [Fintype ↥H]
    {τ : Perm (Fin (nOf μ))} (hτ : τ ∈ H) (hτ2 : τ * τ = 1)
    (hsgn : Equiv.Perm.sign τ = -1) (x : Mtab (k := k) μ) (hfix : Mtab.rep μ τ x = x) :
    antisym (k := k) H x = 0 := by
  unfold antisym
  refine Finset.sum_involution (fun σ _ => σ * ⟨τ, hτ⟩) ?_ ?_ (fun σ _ => Finset.mem_univ _) ?_
  · intro σ _
    have hco : ((σ * ⟨τ, hτ⟩ : H) : Perm (Fin (nOf μ))) = (σ : Perm (Fin (nOf μ))) * τ := by
      rw [Subgroup.coe_mul]
    have hsg : (Equiv.Perm.sign ((σ * ⟨τ, hτ⟩ : H) : Perm (Fin (nOf μ))) : ℤ)
        = -(Equiv.Perm.sign (σ : Perm (Fin (nOf μ))) : ℤ) := by
      rw [hco, map_mul, hsgn]; push_cast; ring
    have hre : Mtab.rep μ ((σ * ⟨τ, hτ⟩ : H) : Perm (Fin (nOf μ))) x
        = Mtab.rep μ (σ : Perm (Fin (nOf μ))) x := by
      rw [hco, map_mul]
      show Mtab.rep μ (σ : Perm (Fin (nOf μ))) (Mtab.rep μ τ x) = Mtab.rep μ (σ : Perm (Fin (nOf μ))) x
      rw [hfix]
    rw [hsg, hre, neg_smul, add_neg_cancel]
  · intro σ _ _ hcon
    have hone : (⟨τ, hτ⟩ : H) = 1 := mul_left_cancel (a := σ) (by rw [mul_one]; exact hcon)
    have hτ1 : τ = 1 := by
      have h := congrArg (fun y : H => (y : Perm (Fin (nOf μ)))) hone
      simpa using h
    rw [hτ1, Equiv.Perm.sign_one] at hsgn
    exact absurd hsgn (by decide)
  · intro σ _
    ext1
    rw [Subgroup.coe_mul, Subgroup.coe_mul]
    show (σ : Perm (Fin (nOf μ))) * τ * τ = (σ : Perm (Fin (nOf μ)))
    rw [mul_assoc, hτ2, mul_one]

/-- **Per-tabloid Garnir vanishing.** If a sign-`(−1)` involution `τ ∈ H` carries
the tableau `s` to a *row-equivalent* one (`{τ·s} = {s}` as tabloids), the
antisymmetriser kills the basis tabloid: `b_H ⟦s⟧ = 0`. This is `antisym_eq_zero`
specialised to a basis vector `⟦s⟧`, with the fixing hypothesis supplied by a row
transposition. It reduces the full Garnir vanishing `b_{S_X} e_t = 0` to the
pigeonhole "for every `π ∈ C_t` there is a row transposition in `S_X` fixing the
tabloid `{π·t}`" (because `|X|` exceeds the relevant column length). -/
theorem antisym_of_eq_zero (H : Subgroup (Perm (Fin (nOf μ)))) [Fintype ↥H]
    {τ : Perm (Fin (nOf μ))} (hτ : τ ∈ H) (hτ2 : τ * τ = 1)
    (hsgn : Equiv.Perm.sign τ = -1) (s : Tableau μ)
    (hrow : Tabloid.mk (τ • s) = Tabloid.mk s) :
    antisym (k := k) H (Mtab.of (k := k) s) = 0 := by
  apply antisym_eq_zero (k := k) H hτ hτ2 hsgn
  rw [Mtab.rep_of]
  simp only [Mtab.of, hrow]

/-! ## 3. The column collapse `b_K e_t = |K| · e_t`

The bridge from the abstract antisymmetriser to a *Garnir element*: when the
subgroup `K` sits **inside the column stabiliser** `C_t`, the antisymmetriser
acts on `e_t` by the scalar `|K|` (each term `sgn(σ)·(σ·e_t) = sgn(σ)²·e_t = e_t`
collapses by the column-alternating property). Concretely, for the Garnir
element `b_{S_X} = G · b_{S_A × S_B}` with `A,B` single-column cell sets, this is
the `b_{S_A × S_B} e_t = |A|!·|B|!·e_t` step.
-/

/-- **Column collapse.** For a subgroup `H ≤ C_t`, the antisymmetriser acts on the
polytabloid `e_t` by the scalar `|H|`: `b_H e_t = |H| · e_t`. Each summand
`sgn(σ)·(σ·e_t)` equals `sgn(σ)²·e_t = e_t` by the column-alternating property. -/
theorem antisym_colStab (t : Tableau μ) (H : Subgroup (Perm (Fin (nOf μ)))) [Fintype ↥H]
    (hle : H ≤ colStab t) :
    antisym (k := k) H (polytabloid (k := k) t)
      = Fintype.card ↥H • polytabloid (k := k) t := by
  unfold antisym
  have hterm : ∀ σ : H,
      (Equiv.Perm.sign (σ : Perm (Fin (nOf μ))) : ℤ) •
          Mtab.rep μ (σ : Perm (Fin (nOf μ))) (polytabloid (k := k) t)
        = polytabloid (k := k) t := by
    intro σ
    have hsq : (Equiv.Perm.sign (σ : Perm (Fin (nOf μ))) : ℤ)
        * (Equiv.Perm.sign (σ : Perm (Fin (nOf μ))) : ℤ) = 1 := by
      simp [← Units.val_mul, Int.units_mul_self]
    rw [polytabloid_rep_colStab t (hle σ.2),
      ← mul_smul (Equiv.Perm.sign (σ : Perm (Fin (nOf μ))) : ℤ)
        (Equiv.Perm.sign (σ : Perm (Fin (nOf μ))) : ℤ) (polytabloid (k := k) t),
      hsq, one_zsmul]
  rw [Finset.sum_congr rfl (fun σ _ => hterm σ), Finset.sum_const, Finset.card_univ]

/-- **Antisymmetriser as a polytabloid combination.** `b_H(e_t)` is the signed
sum of polytabloids `e_{σ·t}` over `H` — the left-hand side of a Garnir relation.
Immediate from polytabloid equivariance `rep σ (e_t) = e_{σ·t}` (§1b). -/
theorem antisym_polytabloid (H : Subgroup (Perm (Fin (nOf μ)))) [Fintype ↥H]
    (t : Tableau μ) :
    antisym (k := k) H (polytabloid (k := k) t)
      = ∑ σ : H, (Equiv.Perm.sign (σ : Perm (Fin (nOf μ))) : ℤ) •
          polytabloid (k := k) ((σ : Perm (Fin (nOf μ))) • t) := by
  unfold antisym
  exact Finset.sum_congr rfl (fun σ _ => by rw [rep_polytabloid])

/-! ## 5. Tableau-geometry bricks (toward the Garnir pigeonhole)

The Garnir vanishing `b_{S_X} e_t = 0` is fed, per column-permutation `π ∈ C_t`,
by a **row transposition** in `S_X` fixing the tabloid `{π·t}`. The existence of
such a transposition is the pigeonhole (`|X|` exceeds the column length). These
two bricks supply its *consequence* sorry-free: a transposition of two
same-row labels fixes the tabloid, hence kills `⟦s⟧` under any antisymmetriser
whose group contains it.
-/

/-- **A same-row transposition fixes the tabloid.** If labels `a, b` lie in the
same row of `s` (`rowPattern s a = rowPattern s b`), then `{(a b)·s} = {s}`. -/
theorem tabloid_swap_sameRow {s : Tableau μ} {a b : Fin (nOf μ)}
    (h : rowPattern s a = rowPattern s b) :
    Tabloid.mk (Equiv.swap a b • s) = Tabloid.mk s := by
  apply Quotient.sound
  show rowPattern (Equiv.swap a b • s) = rowPattern s
  rw [rowPattern_smul]
  funext l
  rw [arrow_smul_apply, Equiv.symm_swap]
  rcases eq_or_ne l a with rfl | hla
  · rw [Equiv.swap_apply_left]; exact h.symm
  · rcases eq_or_ne l b with rfl | hlb
    · rw [Equiv.swap_apply_right]; exact h
    · rw [Equiv.swap_apply_of_ne_of_ne hla hlb]

/-- **Row pigeonhole.** If every label of a set `X` lies in one of fewer than
`|X|` rows of `s` (`rowPattern s l < m` with `m < |X|`), two distinct labels of
`X` share a row. In the Garnir setup `X = A ∪ B` lives in two adjacent columns,
so all its row indices are `< μ'_j` (the longer column length); choosing
`|X| > μ'_j` forces the collision that produces the killing transposition. -/
theorem exists_sameRow_of_card_lt {X : Finset (Fin (nOf μ))} {s : Tableau μ} {m : ℕ}
    (hbound : ∀ l ∈ X, rowPattern s l < m) (hcard : m < X.card) :
    ∃ a ∈ X, ∃ b ∈ X, a ≠ b ∧ rowPattern s a = rowPattern s b := by
  have hmaps : ∀ l ∈ X, rowPattern s l ∈ Finset.range m :=
    fun l hl => Finset.mem_range.mpr (hbound l hl)
  have hlt : (Finset.range m).card < X.card := by rwa [Finset.card_range]
  exact Finset.exists_ne_map_eq_of_card_lt_of_maps_to hlt hmaps

/-- **Concrete row-transposition vanishing.** A same-row transposition `(a b)`
(`a ≠ b`) lying in `H` kills the basis tabloid: `b_H ⟦s⟧ = 0`. This is the
per-`π` input to the Garnir vanishing — the pigeonhole produces exactly such a
transposition in `S_X` for the tableau `π·t`. -/
theorem antisym_swap_eq_zero (H : Subgroup (Perm (Fin (nOf μ)))) [Fintype ↥H]
    {a b : Fin (nOf μ)} (hab : a ≠ b) (hmem : Equiv.swap a b ∈ H)
    (s : Tableau μ) (hrow : rowPattern s a = rowPattern s b) :
    antisym (k := k) H (Mtab.of (k := k) s) = 0 :=
  antisym_of_eq_zero (k := k) H hmem (Equiv.swap_mul_self a b)
    (Equiv.Perm.sign_swap hab) s (tabloid_swap_sameRow hrow)

/-! ## 6. The Garnir subgroup `S_X` (perms supported on a label set)

The Garnir element is the antisymmetriser over the symmetric group `S_X` on the
two-column Garnir set `X = A ∪ B`. We realise `S_X` as the subgroup of
`Perm (Fin n)` fixing every label **outside** `X`; the killing transposition
`(a b)` (`a,b ∈ X`) lives in it. -/

/-- `S_X`: the permutations supported on `X` (fixing the complement of `X`). -/
def suppSubgroup (X : Finset (Fin (nOf μ))) : Subgroup (Perm (Fin (nOf μ))) where
  carrier := {σ | ∀ i, i ∉ X → σ i = i}
  one_mem' := fun _ _ => rfl
  mul_mem' {a b} ha hb := fun i hi => by
    simp only [Equiv.Perm.coe_mul, Function.comp_apply, hb i hi, ha i hi]
  inv_mem' {a} ha := fun i hi => by
    have h := ha i hi
    nth_rewrite 1 [← h]
    exact a.symm_apply_apply i

noncomputable instance instFintypeSuppSubgroup (X : Finset (Fin (nOf μ))) :
    Fintype (suppSubgroup (μ := μ) X) := Fintype.ofFinite _

/-- The transposition of two labels of `X` is supported on `X`. -/
theorem swap_mem_suppSubgroup {X : Finset (Fin (nOf μ))} {a b : Fin (nOf μ)}
    (ha : a ∈ X) (hb : b ∈ X) : Equiv.swap a b ∈ suppSubgroup (μ := μ) X := by
  intro i hi
  apply Equiv.swap_apply_of_ne_of_ne
  · rintro rfl; exact hi ha
  · rintro rfl; exact hi hb

/-! ## 7. The Garnir vanishing `b_{S_X} e_t = 0` (modulo the row-index bound)

Assembling §5–§6: if every label of `X` lies in fewer than `|X|` rows of `s`
(the pigeonhole hypothesis), then `b_{S_X} ⟦s⟧ = 0`; lifting over the
column-stabiliser sum gives `b_{S_X} e_t = 0` whenever the bound holds for every
`π · t` (`π ∈ C_t`). This is the **entire** Garnir vanishing reduced to a single
geometric input — the row-count bound for the two-column Garnir set `X = A ∪ B`,
which holds with `m = μ'_j` (the longer column length) once `|X| > μ'_j`. -/

/-- **Per-tabloid Garnir vanishing from the row bound.** -/
theorem antisym_supp_eq_zero_of_card_lt {X : Finset (Fin (nOf μ))} {s : Tableau μ}
    {m : ℕ} (hbound : ∀ l ∈ X, rowPattern s l < m) (hcard : m < X.card) :
    antisym (k := k) (suppSubgroup (μ := μ) X) (Mtab.of (k := k) s) = 0 := by
  obtain ⟨a, ha, b, hb, hne, heq⟩ := exists_sameRow_of_card_lt hbound hcard
  exact antisym_swap_eq_zero (suppSubgroup X) hne (swap_mem_suppSubgroup ha hb) s heq

/-- **Garnir vanishing.** `b_{S_X} e_t = 0` whenever the row-index bound
`rowPattern (π·t) l < m` holds for every `π ∈ C_t` and `l ∈ X`, with `m < |X|`. -/
theorem antisym_supp_polytabloid_eq_zero {X : Finset (Fin (nOf μ))} {t : Tableau μ}
    {m : ℕ} (hcard : m < X.card)
    (hbound : ∀ π : colStab t, ∀ l ∈ X,
      rowPattern ((π : Perm (Fin (nOf μ))) • t) l < m) :
    antisym (k := k) (suppSubgroup (μ := μ) X) (polytabloid (k := k) t) = 0 := by
  unfold polytabloid
  rw [antisym_sum]
  apply Finset.sum_eq_zero
  intro π _
  rw [antisym_zsmul, antisym_supp_eq_zero_of_card_lt (hbound π) hcard, smul_zero]

/-- **The Garnir relation** (textbook form). Modulo the two-column row-index
bound, the signed sum of polytabloids over the Garnir subgroup `S_X` vanishes:
`Σ_{σ ∈ S_X} sgn(σ) · e_{σ·t} = 0`. Combines `antisym_polytabloid` (the
antisymmetriser as a polytabloid sum) with the Garnir vanishing
`antisym_supp_polytabloid_eq_zero`. Splitting `S_X` into its `S_A × S_B` part
(which collapses to `|A|!·|B|!·e_t`) and the rest (more-dominant polytabloids)
turns this into the straightening rewrite `e_t = Σ (more dominant)`. -/
theorem garnir_relation {X : Finset (Fin (nOf μ))} {t : Tableau μ} {m : ℕ}
    (hcard : m < X.card)
    (hbound : ∀ π : colStab t, ∀ l ∈ X,
      rowPattern ((π : Perm (Fin (nOf μ))) • t) l < m) :
    ∑ σ : suppSubgroup (μ := μ) X,
        (Equiv.Perm.sign (σ : Perm (Fin (nOf μ))) : ℤ) •
          polytabloid (k := k) ((σ : Perm (Fin (nOf μ))) • t) = 0 := by
  rw [← antisym_polytabloid (k := k) (suppSubgroup X) t,
    antisym_supp_polytabloid_eq_zero (k := k) hcard hbound]

end QOU.BraidKnot.SpechtGarnirCore
