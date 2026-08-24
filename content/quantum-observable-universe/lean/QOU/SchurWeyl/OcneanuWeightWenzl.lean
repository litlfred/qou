import Mathlib.Order.Interval.Finset.Nat
import QOU.SchurWeyl.OcneanuWeight
import QOU.QBeta.WenzlWeightVanishing

/-!
# QOU.SchurWeyl.OcneanuWeightWenzl — the derived weight IS `schurPrincipal` at level 2

## Why this file exists

`QOU/QBeta/WenzlWeightVanishing.lean` says of its own central definition:

> Wenzl's theorem — **the external input, and the only one** — is that these *are* the
> Ocneanu/Markov trace weights on `H_n(Q)` at Markov parameter `z_W = Q^r(1−Q)/(1−Q^r)`.

and `docs/audits/2026-08-16-two-row-cap-proved-and-deltalambda-magnitude.md` records the
consequence: the two-row cap and everything built on it are proved *about* `schurPrincipal 2 Q μ`,
a named rational expression, and reading them as statements about the mass channel's Ocneanu weight
is that citation.  `#print axioms` cannot see the dependency, because it is carried by the choice of
object rather than by an axiom.

`OcneanuWeight.ocneanuWeight` is a different object with a different provenance: it was **derived**
from the Markov defining conditions in exact `ℚ(q,z)` (`computations/schurweyl/ocneanu_weight_general_n.py`)
and is Lean-proved to reproduce this repository's own proved `n = 3` Markov weights
(`OcneanuWeightMarkov3`).  This file proves the two coincide at convention D:

```
ocneanuWeight q (q³/(q²+1)) μ = schurPrincipal 2 (q²) μ / (q²+1)^{|μ|}
```

for **every** Young diagram, no genericity hypothesis, no `sorry`.

## What that does and does not achieve

It does **not** discharge the Wenzl citation.  It **relocates** it.  Before, the citation attached to
a formula recalled from the literature.  After, it attaches to the single statement

> `ocneanuWeight` satisfies the Markov property `tr(x·σ_n) = z·tr(x)` at general `n`

about a formula that was derived from those very conditions and is checked against the proved
`n = 3` case.  That statement is open — see `OcneanuWeight`'s docstring and bean `qou-uer7` — but it
is now a well-posed Lean goal rather than a bibliography entry, and proving it would discharge the
corpus's only external input here outright.

The immediate payoff is smaller and concrete: the vanishing result
`ocneanuWeight_conventionD_eq_zero_of_three_rows`, proved standalone in `OcneanuWeight`, is a
duplicate of `schurPrincipal_eq_zero_iff` and is re-derived here from it, with the sharper **iff**.

## Base ring (§7c)

Generic `[Field R]` throughout — no `ℝ`, no ordering.  `hookLength_eq_hook` is pure `ℕ`
combinatorics.

LaTeX label: `thm:ocneanu-weight-is-schur-principal`
-/

namespace QOU.SchurWeyl

open YoungDiagram QOU.QBeta.WenzlWeight

/-- `OcneanuWeight.hookLength` (a `Finset.card`, hence `decide`-evaluable on concrete diagrams)
agrees on cells with `QOU.QBeta.WenzlWeight.hook` (arm + leg via `rowLen`/`colLen`).

Two definitions of one notion is a duplication; this lemma is the price of the computable one, and
is stated so that no other file has to choose between them. -/
theorem hookLength_eq_hook {mu : YoungDiagram} {x : ℕ × ℕ} (hx : x ∈ mu.cells) :
    hookLength mu x = hook mu x := by
  obtain ⟨i, j⟩ := x
  have hmem : (i, j) ∈ mu := by simpa using (YoungDiagram.mem_cells (i, j)).mp hx
  have hrow : j < mu.rowLen i := YoungDiagram.mem_iff_lt_rowLen.mp hmem
  have hcol : i < mu.colLen j := YoungDiagram.mem_iff_lt_colLen.mp hmem
  have harm : (mu.cells.filter (fun d => d.1 = i ∧ j ≤ d.2)).card = mu.rowLen i - j := by
    have hset : mu.cells.filter (fun d => d.1 = i ∧ j ≤ d.2)
        = (Finset.Ico j (mu.rowLen i)).image (fun k => (i, k)) := by
      ext d
      simp only [Finset.mem_filter, Finset.mem_image, Finset.mem_Ico, YoungDiagram.mem_cells]
      constructor
      · rintro ⟨hd, rfl, hj⟩
        exact ⟨d.2, ⟨hj, YoungDiagram.mem_iff_lt_rowLen.mp hd⟩, rfl⟩
      · rintro ⟨k, ⟨hjk, hk⟩, rfl⟩
        exact ⟨YoungDiagram.mem_iff_lt_rowLen.mpr hk, rfl, hjk⟩
    rw [hset, Finset.card_image_of_injective _ (by intro a b hab; simpa using hab), Nat.card_Ico]
  have hleg : (mu.cells.filter (fun d => d.2 = j ∧ i < d.1)).card = mu.colLen j - i - 1 := by
    have hset : mu.cells.filter (fun d => d.2 = j ∧ i < d.1)
        = (Finset.Ioo i (mu.colLen j)).image (fun k => (k, j)) := by
      ext d
      simp only [Finset.mem_filter, Finset.mem_image, Finset.mem_Ioo, YoungDiagram.mem_cells]
      constructor
      · rintro ⟨hd, rfl, hi⟩
        exact ⟨d.1, ⟨hi, YoungDiagram.mem_iff_lt_colLen.mp hd⟩, rfl⟩
      · rintro ⟨k, ⟨hik, hk⟩, rfl⟩
        exact ⟨YoungDiagram.mem_iff_lt_colLen.mpr hk, rfl, hik⟩
    rw [hset, Finset.card_image_of_injective _ (by intro a b hab; simpa using hab), Nat.card_Ioo]
  unfold hookLength hook
  simp only [harm, hleg]
  omega

variable {R : Type*} [Field R]

/-- **The per-cell identity.**  At `z = q³/(q²+1)` the numerator factor of the cell `(i,j)`
collapses to `(q^{2j+4} − q^{2i})/(q²+1)` — a difference of two monomials over the fixed
denominator `q²+1`.  This is the whole content of the bridge; everything else is bookkeeping. -/
theorem ocneanuNumFactor_conventionD (q : R) (hq2 : q ^ 2 + 1 ≠ 0) (i j : ℕ) :
    q ^ (2 * i) * (q ^ 2 - 1 - q * (q ^ 3 / (q ^ 2 + 1)))
        + q ^ (2 * j + 1) * (q ^ 3 / (q ^ 2 + 1))
      = (q ^ (2 * j + 4) - q ^ (2 * i)) / (q ^ 2 + 1) := by
  field_simp
  ring

/-- The `schurPrincipal` numerator factor of the cell `(i,j)`, with the `Q^{n(λ)}` prefactor
distributed one power per cell: `Q^i · (1 − Q^{2 + c}) = q^{2i} − q^{2j+4}`. -/
theorem schurPrincipalNumFactor (q : R) (hq : q ≠ 0) (i j : ℕ) :
    (q ^ 2) ^ i * (1 - (q ^ 2) ^ ((2 : ℤ) + content (i, j))) = q ^ (2 * i) - q ^ (2 * j + 4) := by
  have hq2 : (q ^ 2 : R) ≠ 0 := pow_ne_zero _ hq
  have hc : (2 : ℤ) + content (i, j) = ((j + 2 : ℕ) : ℤ) - ((i : ℕ) : ℤ) := by
    unfold content; push_cast; ring
  rw [hc, zpow_sub₀ hq2, zpow_natCast, zpow_natCast]
  field_simp
  rw [← pow_mul, ← pow_mul]
  ring

/-- **The bridge.**  The derived general-`n` Ocneanu weight, evaluated at convention D's Markov
parameter, is the level-2 principal Schur specialisation up to the normalisation `[2]_{q²}^{|μ|}`:

`ocneanuWeight q (q³/(q²+1)) μ = schurPrincipal 2 (q²) μ / (q²+1)^{|μ|}`

for every Young diagram — no genericity hypothesis on `q` beyond `q ≠ 0` and `q² + 1 ≠ 0`.

See the module docstring for what this settles (the two objects are the same) and what it does not
(the Markov property of either at general `n`). -/
theorem ocneanuWeight_conventionD_eq_schurPrincipal (q : R) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (mu : YoungDiagram) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) mu
      = schurPrincipal 2 (q ^ 2) mu / (q ^ 2 + 1) ^ mu.cells.card := by
  rw [ocneanuWeight, ← Finset.prod_div_distrib, schurPrincipal, nPart,
    ← Finset.prod_pow_eq_pow_sum, ← Finset.prod_mul_distrib, ← Finset.prod_const,
    ← Finset.prod_div_distrib]
  refine Finset.prod_congr rfl ?_
  rintro ⟨i, j⟩ hx
  have hsch := schurPrincipalNumFactor q hq i j
  have hhk : hookLength mu (i, j) = hook mu (i, j) := hookLength_eq_hook hx
  have hQh : ((q ^ 2 : R)) ^ hook mu (i, j) = q ^ (2 * hook mu (i, j)) := by
    rw [← pow_mul]
  simp only [hhk, hQh, Nat.cast_ofNat, ← mul_div_assoc, hsch]
  rcases eq_or_ne (q ^ (2 * hook mu (i, j)) - 1) 0 with hz | hz
  · rw [hz]
    simp [sub_eq_zero.mp hz]
  · have hz' : (1 : R) - q ^ (2 * hook mu (i, j)) ≠ 0 := fun h => hz (by linear_combination -h)
    field_simp
    ring

/-- **The two-row cap for the derived weight, as an `iff`.**

`ocneanuWeight q (q³/(q²+1)) μ = 0 ↔ μ has more than two rows.`

Not proved here: it is `QBeta.WenzlWeight.schurPrincipal_eq_zero_iff` transported along the bridge.
`OcneanuWeight.ocneanuWeight_conventionD_eq_zero_of_three_rows` proves the forward direction
directly and needs no root-of-unity hypothesis; this is the sharper statement and needs `hgen`,
exactly as the corpus theorem does — at a root of unity a hook length can kill a denominator and the
`iff` is false. -/
theorem ocneanuWeight_conventionD_eq_zero_iff (q : R) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → (q ^ 2 : R) ^ k ≠ 1) (mu : YoungDiagram) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) mu = 0 ↔ 2 < mu.colLen 0 := by
  have hQ0 : (q ^ 2 : R) ≠ 0 := pow_ne_zero _ hq
  have hden : ((q ^ 2 + 1 : R)) ^ mu.cells.card ≠ 0 := pow_ne_zero _ hq21
  rw [ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21 mu, div_eq_zero_iff]
  simp only [hden, or_false]
  exact schurPrincipal_eq_zero_iff hQ0 hgen 2 mu

end QOU.SchurWeyl
