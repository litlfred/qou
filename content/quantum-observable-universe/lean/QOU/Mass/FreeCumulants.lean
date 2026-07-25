/-
# Free moment–cumulant relation — the first F3 (free-probability) brick

The Δ_λ / abstract-trace route to the H₄ Markov-trace program needs a
free-probability layer that Mathlib does not supply: the moments of a
non-commutative distribution expressed through its **free cumulants**
via a sum over **non-crossing partitions** `NC(n)` (Speicher's
moment–cumulant formula),

  `m_n  =  ∑_{π ∈ NC(n)} ∏_{V ∈ π} κ_{|V|}`,

as opposed to the *classical* moment–cumulant sum over *all* partitions.
The two agree through order 3 (every partition of a ≤ 3-element set is
non-crossing) and first split at order 4: the single crossing partition
`{{1,3},{2,4}}` of `{1,2,3,4}` is present in the classical sum but absent
in the free one. That one missing block-pair is the entire structural
content of *freeness* at leading order, and it is what a q-CLT /
q-Gaussian description of the centred Hecke transfer matrix
(`QOU/Observations/QCltNonCommutative.lean`) must ultimately reproduce.

Mathlib already provides the Catalan numbers (`Nat.catalan`, with
`Nat.catalan n = Nat.centralBinom n / (n + 1)` by `catalan_eq_centralBinom_div`);
we do **not** redefine them. This brick supplies the free-probability
content Mathlib lacks and *bridges to* the Catalan count via its
underlying Mathlib primitive `Nat.centralBinom`: since `|NC(n)| = C_n`,
evaluating the free moment at all cumulants `= 1` counts the
non-crossing partitions and therefore returns `C_n = centralBinom n /
(n+1)` (Theorem `freeMoment_eval_one_eq_catalanCount`). We express the
count through `Nat.centralBinom` rather than importing
`Mathlib.Combinatorics.Enumerative.Catalan` only because that module's
olean is absent from the sandbox cache — `Nat.centralBinom n / (n+1)`
*is* `Nat.catalan n` by the Mathlib theorem cited above. The classical
order-4 moment at all-ones returns `15 = B_4` (the Bell number, all
partitions), so the free/classical gap `= 1` is exactly the one crossing
partition — the combinatorial signature of freeness (Theorem
`classical_sub_free_eval_one_eq_one`).

## Where this sits in the route

  free cumulants κ_k  ──(this brick: NC-partition moment formula)──▶  free moments m_n
        │                                                                    │
        ▼                                                                    ▼
  q-Gaussian / q-CLT of the centred Hecke generator sum  ◀── tr_M joint moments
  (QOU/Observations/QCltNonCommutative.lean, a conditional class)

The *classical* connected-cumulant leg already exists
(`QOU/MassTheory/BodyOrderCumulant.lean`, Ursell/finite-difference
cumulants for the A-body binding); this file is its **free** counterpart,
the piece the Δ_λ magnitude program needs when the underlying algebra is
non-commutative (Hecke), where NC(n) rather than all-partitions governs
the moment expansion.

## Next brick (documented, NOT `sorry`'d)

A `DecidablePred` enumeration of the non-crossing partitions of `Fin n`
(a `Finpartition`-with-no-crossing predicate) and a `decide`-verified
`Fintype.card (NCPartition (Fin n)) = catalan n` for `n ≤ 4`, mirroring
the `decide` count in `QOU/Mass/InvolutionNumbers.lean`. That upgrades
the all-ones *evaluation* bridge here into a genuine bijective count, and
then feeds the general Speicher recursion `m_n = ∑_{s} κ_s ∑_{i₁+…+i_s
= n−s} m_{i₁}⋯m_{i_s}` (proved here for `n ≤ 4`) at arbitrary `n`.

## Base ring (§7c)

Generic `{R : Type*} [CommRing R]` throughout — every statement is a
polynomial identity in the formal cumulants `κ_k` (or a `ℕ`-valued count).
No ordering, no `Real`, no archimedean construct, no substrate `q₀`.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Data.Nat.Choose.Central

namespace QOU.Mass

variable {R : Type*} [CommRing R]

/-! ## Free moments as non-crossing-partition sums

`κ : ℕ → R` supplies the free cumulants `κ_k := κ k` as formal variables.
`freeMomentₙ κ` is `∑_{π ∈ NC(n)} ∏_{V ∈ π} κ_{|V|}`, written out as an
explicit polynomial. `freeMoment0 = 1` is the empty sum convention. -/

/-- Empty-partition convention: `m₀ = 1`. -/
def freeMoment0 (_ : ℕ → R) : R := 1

/-- `m₁ = κ₁`  (NC(1) = {{1}}). -/
def freeMoment1 (κ : ℕ → R) : R := κ 1

/-- `m₂ = κ₂ + κ₁²`  (NC(2): `{{1,2}}`, `{{1},{2}}`). -/
def freeMoment2 (κ : ℕ → R) : R := κ 2 + κ 1 ^ 2

/-- `m₃ = κ₃ + 3 κ₁κ₂ + κ₁³`  (NC(3) = all 5 partitions of `{1,2,3}`, all
non-crossing). -/
def freeMoment3 (κ : ℕ → R) : R := κ 3 + 3 * κ 1 * κ 2 + κ 1 ^ 3

/-- `m₄ = κ₄ + 4 κ₁κ₃ + 2 κ₂² + 6 κ₁²κ₂ + κ₁⁴`.  The 14 = `C₄` terms are the
non-crossing partitions of `{1,2,3,4}`. The pair-partition coefficient is
`2` — only `{{1,2},{3,4}}` and `{{1,4},{2,3}}` are non-crossing; the third
pairing `{{1,3},{2,4}}` **crosses** and is excluded. -/
def freeMoment4 (κ : ℕ → R) : R :=
  κ 4 + 4 * κ 1 * κ 3 + 2 * κ 2 ^ 2 + 6 * κ 1 ^ 2 * κ 2 + κ 1 ^ 4

/-- The **classical** order-4 moment: identical to `freeMoment4` except the
pair-partition coefficient is `3` rather than `2`, because the classical
sum runs over *all* 15 = `B₄` partitions, keeping the crossing pairing
`{{1,3},{2,4}}` (an extra `κ₂²`). -/
def classicalMoment4 (κ : ℕ → R) : R :=
  κ 4 + 4 * κ 1 * κ 3 + 3 * κ 2 ^ 2 + 6 * κ 1 ^ 2 * κ 2 + κ 1 ^ 4

/-! ## Speicher's first-block recursion (`n ≤ 4`)

`m_n = ∑_{s=1}^{n} κ_s ∑_{i₁+…+i_s = n−s} m_{i₁}⋯m_{i_s}`, where `s` is
the size of the block of `π ∈ NC(n)` containing `1` and the inner sum
fills the `s` gaps between its legs with non-crossing partitions
(hence products of lower free moments). These are the defining
recurrences of the free moment sequence and are the base cases of the
general-`n` recursion (next brick). Each is a `ring` identity. -/

/-- `m₂ = κ₁·m₁ + κ₂·m₀`. -/
theorem freeMoment2_recursion (κ : ℕ → R) :
    freeMoment2 κ = κ 1 * freeMoment1 κ + κ 2 * freeMoment0 κ := by
  simp only [freeMoment2, freeMoment1, freeMoment0]; ring

/-- `m₃ = κ₁·m₂ + κ₂·(2·m₁) + κ₃·m₀`. -/
theorem freeMoment3_recursion (κ : ℕ → R) :
    freeMoment3 κ
      = κ 1 * freeMoment2 κ + κ 2 * (2 * freeMoment1 κ) + κ 3 * freeMoment0 κ := by
  simp only [freeMoment3, freeMoment2, freeMoment1, freeMoment0]; ring

/-- `m₄ = κ₁·m₃ + κ₂·(2·m₂ + m₁²) + κ₃·(3·m₁) + κ₄·m₀`.  The inner factor
`2·m₂ + m₁²` is `∑_{i₁+i₂=2} m_{i₁}m_{i₂} = m₀m₂ + m₁m₁ + m₂m₀`, the
non-crossing fillings of the two gaps left by a size-2 first block. -/
theorem freeMoment4_recursion (κ : ℕ → R) :
    freeMoment4 κ
      = κ 1 * freeMoment3 κ
        + κ 2 * (2 * freeMoment2 κ + freeMoment1 κ ^ 2)
        + κ 3 * (3 * freeMoment1 κ)
        + κ 4 * freeMoment0 κ := by
  simp only [freeMoment4, freeMoment3, freeMoment2, freeMoment1, freeMoment0]; ring

/-! ## The freeness discriminator

The single crossing partition `{{1,3},{2,4}}` is the whole difference
between the classical and free order-4 moments. -/

/-- **Free/classical order-4 gap = the crossing partition.**
`classicalMoment4 − freeMoment4 = κ₂²`, the contribution of the one
crossing pair-partition `{{1,3},{2,4}}` that freeness removes. -/
theorem classical_sub_free_moment4 (κ : ℕ → R) :
    classicalMoment4 κ - freeMoment4 κ = κ 2 ^ 2 := by
  simp only [classicalMoment4, freeMoment4]; ring

/-! ## Bridge to the Catalan count via the all-ones evaluation

Setting every cumulant to `1` makes each non-crossing partition
contribute `1`, so `freeMomentₙ` evaluated at `κ ≡ 1` equals `|NC(n)| =
C_n`. We express `C_n` as Mathlib's `Nat.centralBinom n / (n + 1)` (which
equals `Nat.catalan n` by `Nat.catalan_eq_centralBinom_div`), grounding
the NC-partition reading of the moment polynomials in Mathlib without
redefining the Catalan numbers. -/

/-- The Catalan values `C₁ = 1, C₂ = 2, C₃ = 5, C₄ = 14`, expressed via
Mathlib's `Nat.centralBinom` (`C_n = centralBinom n / (n+1)`). -/
theorem catalanCount_values :
    Nat.centralBinom 1 / 2 = 1 ∧ Nat.centralBinom 2 / 3 = 2
      ∧ Nat.centralBinom 3 / 4 = 5 ∧ Nat.centralBinom 4 / 5 = 14 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> norm_num [Nat.centralBinom, Nat.choose]

/-- **NC-count bridge.** The free moments at all cumulants `= 1` are the
Catalan numbers `C_n = centralBinom n / (n+1) = |NC(n)|`:
`C₁ = 1, C₂ = 2, C₃ = 5, C₄ = 14`. -/
theorem freeMoment_eval_one_eq_catalanCount :
    freeMoment1 (fun _ => (1 : R)) = ((Nat.centralBinom 1 / 2 : ℕ) : R)
      ∧ freeMoment2 (fun _ => (1 : R)) = ((Nat.centralBinom 2 / 3 : ℕ) : R)
      ∧ freeMoment3 (fun _ => (1 : R)) = ((Nat.centralBinom 3 / 4 : ℕ) : R)
      ∧ freeMoment4 (fun _ => (1 : R)) = ((Nat.centralBinom 4 / 5 : ℕ) : R) := by
  obtain ⟨h1, h2, h3, h4⟩ := catalanCount_values
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [h1]; simp only [freeMoment1]; norm_num
  · rw [h2]; simp only [freeMoment2]; norm_num
  · rw [h3]; simp only [freeMoment3]; norm_num
  · rw [h4]; simp only [freeMoment4]; norm_num

/-- The classical order-4 moment at all-ones is `15 = B₄` (the Bell number:
all 15 partitions of `{1,2,3,4}`), **not** a Catalan number. -/
theorem classicalMoment4_eval_one :
    classicalMoment4 (fun _ => (1 : R)) = 15 := by
  simp only [classicalMoment4]; norm_num

/-- **Combinatorial signature of freeness.** The classical/free gap at the
all-ones evaluation is `15 − 14 = 1`: exactly the single crossing
partition removed by freeness, i.e. `|Partitions(4)| − |NC(4)| = B₄ − C₄`. -/
theorem classical_sub_free_eval_one_eq_one :
    classicalMoment4 (fun _ => (1 : R)) - freeMoment4 (fun _ => (1 : R)) = 1 := by
  simp only [classicalMoment4, freeMoment4]; norm_num

end QOU.Mass
