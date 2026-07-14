/-
# Seminormal character connector — standard tableaux → the `χ_λ(σ) = c_λ·h` core

Infra 4→5 connector (beans `qou-9vvr` done / `qou-tqab`) of the YT seminormal-sum
program. The algebraic core is proved in
[`SeminormalWeight`](SeminormalWeight.lean) (`fullCharacter_two_mul`:
`2·χ_λ(σ) = (2|R_row| + |S_off|)·h`) and
[`TableauContent`](TableauContent.lean) (content / axial distance). This file
**reuses the canonical `QOU.Mathlib.StandardYoungTableau`** (the `BijOn`-filled
standard tableau — *not* a re-definition) and builds the connector that supplies
that core's `(cellOf, ρ)` data per tableau:

* `cellOf T k` — the cell of `μ` holding entry `k` (the inverse of the bijective
  filling), the position map the character sum ranges over;
* `generatorRho T i` — the axial distance `ρ` of the generator pair `(i, i+1)`,
  i.e. `axialDistance (cellOf T i) (cellOf T (i+1))`, the `ρ` feeding `a_ρ`.

Remaining to *discharge* `symbolic_character_table` (bean `qou-tqab`, coordinate
with #3719 per `docs/coordination/yt-seminormal-infra.md`): the partition of the
SYT set into same-row / same-column / off-diagonal classes for the σ₁ generator,
the conjugate-transpose bijection giving `|R_row| = |R_col|` for a self-conjugate
`μ`, and the wire into that block's abstract `chiSigma`.

-- Ref: [sagan2001] The Symmetric Group, §3.3 (Young's seminormal form)
-/
import QOU.BraidKnot.TableauContent
import QOU.Mathlib.StandardYoungTableau

namespace QOU.BraidKnot.SeminormalCharacterConnector

open QOU.Mathlib QOU.BraidKnot.TableauContent

variable {μ : YoungDiagram}

open Classical in
/-- **The cell holding entry `k`** — the inverse of the bijective filling. For `k`
    in the value range `{1,…,|μ|}` the filling's surjectivity gives a (unique) cell;
    off-range it defaults to `(0,0)`. Noncomputable (choice on surjectivity). -/
noncomputable def cellOf (T : StandardYoungTableau μ) (k : ℕ) : ℕ × ℕ :=
  if h : ∃ c ∈ μ.cells, T.entry c.1 c.2 = k then h.choose else (0, 0)

/-- **Generator axial distance** `ρ = c(cell of i+1) − c(cell of i)`: the axial
    distance of the generator pair `(i, i+1)` in `T`, the `ρ` of the seminormal
    weight `a_ρ` that the character sum ranges over (`TableauContent.axialDistance`). -/
noncomputable def generatorRho (T : StandardYoungTableau μ) (i : ℕ) : ℤ :=
  axialDistance (cellOf T i) (cellOf T (i + 1))

/-- When `k` is actually an entry of `T` (some cell of `μ` maps to it), `cellOf T k`
    is a cell of `μ` and carries entry `k`. -/
theorem cellOf_spec (T : StandardYoungTableau μ) {k : ℕ}
    (hk : ∃ c ∈ μ.cells, T.entry c.1 c.2 = k) :
    cellOf T k ∈ μ.cells ∧ T.entry (cellOf T k).1 (cellOf T k).2 = k := by
  classical
  rw [cellOf, dif_pos hk]
  exact ⟨hk.choose_spec.1, hk.choose_spec.2⟩

/-- The generator axial distance is antisymmetric in the two entries:
    `ρ(i, i+1) = −ρ(i+1, i)` (via `TableauContent.axialDistance_antisymm`) — the
    cell-geometry root of the seminormal ρ ↔ −ρ pairing that makes the reduced-weight
    sum an integer `c_λ` (`SeminormalWeight.two_mul_reducedSum_eq_card`). -/
theorem generatorRho_swap (T : StandardYoungTableau μ) (i : ℕ) :
    axialDistance (cellOf T i) (cellOf T (i + 1))
      = -axialDistance (cellOf T (i + 1)) (cellOf T i) :=
  axialDistance_antisymm _ _

/-- **The `|R_row| = |R_col|` structural core (self-conjugacy ⇒ equal counts).**
    Given a self-inverse map `f` on the standard-tableau index set that carries the
    **same-row** class `Rrow` (`1, 2` in the same row) into the **same-column**
    class `Rcol` and back, the two classes have equal cardinality. The
    **conjugate transpose** `T ↦ Tᵀ` is exactly such an `f` for a self-conjugate
    `μ` (`μ = μᵀ`): it maps `SYT(μ)` to itself, is an involution, and swaps
    same-row ↔ same-column for the pair `1, 2`.

    This is the structural half of the σ₁-character closure: with `|Rrow| = |Rcol|`
    the diagonal contribution `|Rrow|·q + |Rcol|·(−q⁻¹) = |Rrow|·h` is an integer
    multiple of `h`, feeding `SeminormalWeight.fullCharacter_two_mul` (with the
    off-diagonal class empty for the single generator σ₁). Robust `Finset.image`
    proof — no heavy tableau machinery here; the remaining piece (bean `qou-tqab`)
    is *constructing* the transpose involution on the canonical
    `StandardYoungTableau` and discharging its three hypotheses. -/
theorem card_row_eq_card_col {ι : Type*} [DecidableEq ι]
    (Rrow Rcol : Finset ι) (f : ι → ι)
    (hf_row : ∀ t ∈ Rrow, f t ∈ Rcol) (hf_col : ∀ t ∈ Rcol, f t ∈ Rrow)
    (hff : ∀ t, f (f t) = t) :
    Rrow.card = Rcol.card := by
  have hinj : Set.InjOn f (Rrow : Set ι) := fun a _ b _ h => by
    have h2 := congrArg f h; rwa [hff, hff] at h2
  have himg : Rrow.image f = Rcol := by
    apply Finset.Subset.antisymm
    · intro b hb
      rw [Finset.mem_image] at hb
      obtain ⟨a, ha, rfl⟩ := hb
      exact hf_row a ha
    · intro b hb
      rw [Finset.mem_image]
      exact ⟨f b, hf_col b hb, hff b⟩
  rw [← himg, Finset.card_image_of_injOn hinj]

end QOU.BraidKnot.SeminormalCharacterConnector
