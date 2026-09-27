import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fintype.Prod
import QOU.Shared.ZPowFinsetProd
import Mathlib.Algebra.Group.Defs
import Mathlib.Algebra.Order.Group.Defs

/-!
# QOU.Eightfold.GaugeAnsatzNesting — a coarser gauge ansatz is a special case of a finer one

Issue #7092 asks whether the duality/σ ratio on the Ptolemy coordinates is a **coboundary**
for a gauge action, and it is answered on the exact `L6a4` class-1 point with **three**
verdicts (`computations/ptolemy/ptolemy_duality_sigma_coboundary_test.py`):

* the **scalar** ansatz `λ_v^{t_i}` — the issue as written — is **not** a coboundary, for
  either σ;
* the **`PGL(3)` torus** (snappy's `128 × 6` decoration-change action) **is** one for `σ_b`
  and is not for `σ_a`;
* the resulting torus element does **not lift** to a diagonal `SL(3)` matrix over `K`.

Read as three independent measurements, the first two look like they are in tension. They
are not, and this file is why: **the scalar ansatz is a sub-torus of the `PGL(3)` torus**,
so the two verdicts are one chain rather than two results.

## The arithmetic behind it

Writing the two exponent matrices as snappy and the probe build them, over the `128`
**non-vertex** coordinates,

* `A_torus  i (lev, k) = #{ v : cusp v = k, t v ≥ lev + 1 }` for `lev ∈ {0, 1}`,
* `A_scalar i k        = ∑ over v with cusp v = k of t v`,

and on those rows every `t v ≤ 2` (the value `3` occurs only on the `32` vertex
coordinates, which the action matrix excludes), so `#{lev ∈ {0,1} : t v ≥ lev+1} = t v` and

`A_scalar[:, k] = A_torus[:, (0,k)] + A_torus[:, (1,k)]`

**exactly over `ℤ`** — measured `128/128`, and failing on `32/32` vertex rows, where
`min 3 2 = 2 ≠ 3`, which is what makes the restriction load-bearing rather than incidental
(`computations/ptolemy/ptolemy_gauge_ansatz_nesting.py`).

## What is proved here

The general fact, of which that identity is one instance: if a coarse exponent row `B` is
obtained from a fine row `A` by **summing over the fibres** of a map `φ` on the columns,
then every coarse gauge value is a fine gauge value — take `z c := lam (φ c)`. Hence

`coboundary for the coarse ansatz → coboundary for the fine one`,

so a *fine* "no" would force a *coarse* "no", and the observed (fine yes, coarse no) is the
only informative pattern; the reverse is excluded outright.

The consequence for #7092 is stated as `strictly_stronger`: the issue as written asks a
**strictly stronger** question than the one that admits the affirmative answer, so its
negative is not evidence against the torus positive.

## Scope

This is the group theory of the two ansätze, machine-checked, and nothing more. It does
**not** say that the ratio is a coboundary for either — that is the measured content of the
probe above — and it does **not** bear on whether `ρ ↦ ρ⁻ᵀ` *induces* `σ_b` as a map on the
variety, which is the open conjecture of bean `qou-qjhc`.
-/

namespace QOU.Eightfold

variable {ι J L G : Type*} [Fintype J] [Fintype L] [DecidableEq L] [CommGroup G]

/-- The gauge value of one exponent row `A` under an assignment `z` of scalars to columns:
`∏_c z c ^ A c`. Integer exponents, so this is a `zpow` product in a `CommGroup`. -/
def gaugeVal (z : J → G) (A : J → ℤ) : G := ∏ c : J, z c ^ A c

/-- **A coarse row is a fine row summed over the fibres of `φ`.**  Then the coarse gauge
value of `lam` is the fine gauge value of `lam ∘ φ` — the coarse ansatz is the fine one
restricted to assignments constant on each fibre. -/
theorem gaugeVal_comp_of_fiberSum (φ : J → L) (A : J → ℤ) (B : L → ℤ)
    (hB : ∀ l, B l = ∑ c ∈ Finset.univ.filter (fun c => φ c = l), A c) (lam : L → G) :
    gaugeVal (fun c => lam (φ c)) A = gaugeVal lam B := by
  classical
  have hfib :
      ∏ l : L, ∏ c ∈ Finset.univ.filter (fun c => φ c = l), lam (φ c) ^ A c
        = ∏ c : J, lam (φ c) ^ A c :=
    Finset.prod_fiberwise_of_maps_to (fun c _ => Finset.mem_univ (φ c)) _
  calc gaugeVal (fun c => lam (φ c)) A
      = ∏ l : L, ∏ c ∈ Finset.univ.filter (fun c => φ c = l), lam (φ c) ^ A c := by
        rw [gaugeVal, hfib]
    _ = ∏ l : L, lam l ^ B l := by
        refine Finset.prod_congr rfl ?_
        intro l _
        rw [hB l, ← QOU.Shared.prod_zpow_eq_zpow_sum]
        refine Finset.prod_congr rfl ?_
        intro c hc
        rw [(Finset.mem_filter.mp hc).2]
    _ = gaugeVal lam B := rfl

/-- **The form the coboundary question is asked in.**  `IsCoboundary A r` says the observed
ratio `r`, one value per coordinate, is `∏_c z c ^ A c` for some gauge `z` — simultaneously
for every coordinate. -/
def IsCoboundary (A : ι → J → ℤ) (r : ι → G) : Prop :=
  ∃ z : J → G, ∀ i, r i = gaugeVal z (A i)

/-- **The chain.**  If every coarse row is the corresponding fine row summed over the fibres
of `φ`, then a coarse coboundary is a fine coboundary.  Contrapositively a fine *no* forces
a coarse *no*, so (fine yes, coarse no) is the only informative pattern and (fine no, coarse
yes) is impossible. -/
theorem isCoboundary_fine_of_coarse {A : ι → J → ℤ} {B : ι → L → ℤ} (φ : J → L)
    (hB : ∀ i l, B i l = ∑ c ∈ Finset.univ.filter (fun c => φ c = l), A i c)
    {r : ι → G} (h : IsCoboundary B r) : IsCoboundary A r := by
  obtain ⟨lam, hlam⟩ := h
  refine ⟨fun c => lam (φ c), fun i => ?_⟩
  rw [gaugeVal_comp_of_fiberSum φ (A i) (B i) (hB i) lam]
  exact hlam i

/-- **#7092 asks the strictly stronger question.**  Under the fibre-sum relation the coarse
(scalar) question implies the fine (torus) one, so a coarse negative is consistent with a
fine positive and is not evidence against it. -/
theorem strictly_stronger {A : ι → J → ℤ} {B : ι → L → ℤ} (φ : J → L)
    (hB : ∀ i l, B i l = ∑ c ∈ Finset.univ.filter (fun c => φ c = l), A i c)
    {r : ι → G} (hfine_no : ¬ IsCoboundary A r) : ¬ IsCoboundary B r :=
  fun h => hfine_no (isCoboundary_fine_of_coarse φ hB h)

/-- **The instance the probe measures.**  The two `PGL(3)`-torus columns of a cusp sum to
that cusp's scalar column, i.e. `φ` forgets the diagonal level (`Bool`) and keeps the cusp.
Measured `128/128` exactly over `ℤ` in
`computations/ptolemy/ptolemy_gauge_ansatz_nesting.py`.

Binders are restated rather than inherited: the section's `[Fintype J]` does not by itself
give `Fintype (Bool × L)` at the instantiation `J := Bool × L`. -/
theorem isCoboundary_torus_of_scalar {ι L G : Type*} [Fintype L] [DecidableEq L]
    [CommGroup G] {A : ι → (Bool × L) → ℤ} {B : ι → L → ℤ}
    (hB : ∀ i l, B i l = A i (false, l) + A i (true, l))
    {r : ι → G} (h : IsCoboundary B r) : IsCoboundary A r := by
  classical
  refine isCoboundary_fine_of_coarse (fun c : Bool × L => c.2) ?_ h
  intro i l
  have hfil : (Finset.univ.filter (fun c : Bool × L => c.2 = l))
      = {(false, l), (true, l)} := by
    ext c
    obtain ⟨b, m⟩ := c
    cases b <;> simp [Prod.ext_iff]
  rw [hfil, Finset.sum_insert (by simp), Finset.sum_singleton, hB i l]

end QOU.Eightfold
