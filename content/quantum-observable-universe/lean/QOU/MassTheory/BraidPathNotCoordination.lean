/-
# The braid's `A − 1` is an edge count; the block's `A − 1` is a vertex degree

`content/.../mass-theory/bk-coordination-multiplicity.md` sets the open
many-body multiplicity to the **per-nucleon coordination number** `z(A) = A − 1`
— in its own words *"the number of nucleon–nucleon bonds incident to one nucleon
in the fully coordinated cluster"* — and reads it off AME2020
(`M_need = B_AME/(m_e·Vol_A)` gives `2.003` for ³H, `2.061` for ³He, against
`z = 2`). `QOU/Mass/CoordinationBinding.lean` machine-checks that reading as the
degree of the complete graph: `coordination_degree : (⊤).degree v = A - 1`.

The canonical atomic braid supplies the integer `A − 1` too. Measured on
`mass_at_3A_proper.atom_braid_word_3A`
(`computations/probes/braid_inter_nucleon_adjacency_probe.py`, 6/6 checks), the
inter-nucleon crossings join nucleon `k` to nucleon `k+1` and nothing else:

    bond set        {(k, k+1) : k < A - 1}   -- the path graph P_A
    degree sequence [1, 2, 2, …, 2, 1]
    edge count      A - 1

so it is tempting to read the braid as **deriving** the multiplicity. This file
says why it does not, and the reason is not a numerical near-miss.

Two objects must be kept apart here. The block's `𝓑_K` is the **census link**
(`8₁₁`, `L6a4`) whose hyperbolic volume carries the isospin leg; the bond set
above belongs to the **3A-strand word**, which is where the `include_inter`
count lives. `atom_braid_word_3A`'s own docstring rules out reading a
topological quantity off that word at all — its averaged letters lie outside
the image of `ρ : Bₙ → Hₙ(q)`, so it is a Hecke element and not a braid. The
measurement feeding this file reads no invariant: it records which **strand
pairs** each letter acts on, which is well defined whether or not the word is a
braid. So `A − 1` here is a combinatorial incidence count, and the block's
`A − 1` is a graph-theoretic degree; neither is a topological reading.

## The coincidence, and why no measurement can settle it

`|E(P_A)| = A - 1` is an **edge count**; `deg_{K_A}(v) = A - 1` is a **vertex
degree**. They are *the same affine function of `A`* (`braid_count_eq_coordination_degree`),
so **no value of `A` separates them** — a table of matching rows is not evidence.
The defect is arity: an extensive total read as an intensive per-nucleon degree.

## What is proved

`handshake_forces_le_two` — the decisive statement, and it needs nothing about
the braid's shape beyond its edge count. If a cluster of `A` nucleons has the
braid's bond count `A − 1` **and** the block's uniform coordination degree
`A − 1`, the handshake identity `A · z = 2 · |E|` gives

    A · (A - 1) = 2 · (A - 1)   ⟹   (A - 1) · (A - 2) = 0   ⟹   A ≤ 2.

So the identification is not merely unsupported at `A ≥ 3`; it is **impossible**
there. `P_A = K_A` iff `A ≤ 2`: the deuteron is the only nucleus where the
braid's bond set is the fully coordinated cluster. This is proved for every `A`,
where the probe measured eight of them.

`degree_le_two` — independently, the braid's own degree is bounded. The bond set
is *defined* here as the measured `{(k, k+1)}` and the bound is **derived** from
it (every bond containing `k` is `(k-1, k)` or `(k, k+1)`), not asserted as a
closed form. With `two_lt_coordination_degree` it gives
`braid_degree_ne_coordination_degree`: at `A ≥ 4` no nucleon of the braid
reaches the coordination degree the block asks of every nucleon.

## Scope

Scope **(a)** for the physics: *this construction, alone, does not derive the
coordination multiplicity.* It does **not** exclude the bond picture, and it
does not touch the `Vol` leg. The exclusion proved here is the narrower and
exact one named in `handshake_forces_le_two` — the two counts cannot both hold
above `A = 2` — whose invariant is the handshake identity.

The linear chain built on these bonds is separately excluded scope **(b)** at
`q ≠ 1` by `QOU.MassTheory.ChainBondOrderDependence.orderIndependent_iff` with
`QOU.QBeta.InterfaceScalar.charge_independence_iff` (bean `qou-m07y`). Together:
the braid's bond set is a path, the path's count is not a degree, and the path
is not even well defined as a binding functional at the substrate.

Consistent with `QOU.Mass.CoordinationSaturation`: a bounded-degree bond set
gives constant `B/A` (the braid's mean degree is `2(A-1)/A → 2`), the complete
graph gives the unbounded `B/A = ε(A-1)/2`, and observed saturation refutes the
latter.

Everything here is `ℕ`-valued combinatorics — no ring, no archimedean construct,
so §7c has nothing to specialise. Standalone library file (no `.ts`/`.md`
sibling).

Beans `qou-m07y` (chain exclusion), `qou-h7mh` (the bond set is the repair
site), `qou-v0yw` (derive the coordination graph).
-/
import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Image
import Mathlib.Tactic

namespace QOU.MassTheory.BraidPathNotCoordination

/-! ## 1. The two counts -/

/-- The braid's inter-nucleon bond set, as measured on `atom_braid_word_3A`:
generator `3k+2` joins nucleon `k` to nucleon `k+1`, for `k < A - 1`. This is
the path graph `P_A`. -/
def bonds (A : ℕ) : Finset (ℕ × ℕ) :=
  (Finset.range (A - 1)).image (fun k => (k, k + 1))

/-- The block's per-nucleon coordination number `z(A) = A - 1`: the degree of a
vertex in the fully coordinated cluster `K_A`. Mirrors
`QOU.Mass.CoordinationBinding.coordination_degree`. -/
def coordinationDegree (A : ℕ) : ℕ := A - 1

/-- `k ↦ (k, k+1)` is injective — its first component already is. -/
theorem succPair_injective : Function.Injective (fun k : ℕ => (k, k + 1)) := by
  intro a b hab
  exact (Prod.mk.injEq .. ▸ hab).1

/-- **The braid's bond count is `A - 1`.** -/
theorem card_bonds (A : ℕ) : (bonds A).card = A - 1 := by
  rw [bonds, Finset.card_image_of_injective _ succPair_injective,
    Finset.card_range]

/-- **The coincidence.** The braid's *edge count* and the block's *vertex
degree* are the same function of `A`, so no value of `A` can tell them apart.
This is the statement a table of matching rows establishes, and it is weaker
than it looks — it is an identity of two arithmetic expressions, not evidence
that the two counts are the same object. -/
theorem braid_count_eq_coordination_degree (A : ℕ) :
    (bonds A).card = coordinationDegree A := card_bonds A

/-! ## 2. The handshake forcing -/

/-- **A cluster cannot carry the braid's bond count and the block's degree at
once above `A = 2`.**

The hypothesis `handshake` is the identity `∑_v deg v = 2·|E|` specialised to a
`z`-regular cluster (`QOU.Mass.CoordinationBinding.coordination_handshake`
proves it for `K_A`). Feeding it the braid's measured `|E| = A - 1` together
with the block's `z = A - 1` forces `A ≤ 2`.

Stated with `edges` and `z` as arguments so the two inputs are visible and
neither is baked in. A hypothesis `1 ≤ A` was carried in a first draft and the
linter showed it unused — the bound holds for every `A`, so it is dropped rather
than kept for decoration. -/
theorem handshake_forces_le_two (A z edges : ℕ)
    (hz : z = coordinationDegree A) (he : edges = A - 1)
    (handshake : A * z = 2 * edges) : A ≤ 2 := by
  subst hz; subst he
  have hs : A * (A - 1) = 2 * (A - 1) := by
    simpa [coordinationDegree] using handshake
  rcases Nat.eq_zero_or_pos (A - 1) with h | h
  · -- `A - 1 = 0` with `1 ≤ A` already gives `A = 1`.
    omega
  · -- cancel the common factor `A - 1 > 0`: `A = 2`.
    have := Nat.eq_of_mul_eq_mul_right h hs
    omega

/-- **`P_A = K_A` only for `A ≤ 2`.** The braid's bond count equals the complete
graph's bond count `C(A,2)` exactly when `A ≤ 2` — the deuteron is the only
nucleus whose braid bond set is the fully coordinated cluster. At `A = 3`, where
the block calibrates, the counts already differ (`2` against `3`). -/
theorem sub_one_lt_choose_two : ∀ {A : ℕ}, 3 ≤ A → A - 1 < A.choose 2 := by
  intro A
  induction A with
  | zero => intro h; omega
  | succ n ih =>
    intro h
    rcases Nat.lt_or_ge n 3 with hn | hn
    · have hn2 : n = 2 := by omega
      subst hn2; decide
    · have hlt := ih hn
      have pascal : (n + 1).choose 2 = n.choose 2 + n := by
        show (n + 1).choose (1 + 1) = n.choose 2 + n
        rw [Nat.choose_succ_succ, Nat.choose_one_right]
        exact Nat.add_comm _ _
      omega

theorem card_bonds_eq_choose_two_iff (A : ℕ) :
    (bonds A).card = A.choose 2 ↔ A ≤ 2 := by
  rw [card_bonds]
  constructor
  · intro h
    by_contra hA
    push_neg at hA
    exact absurd h (Nat.ne_of_lt (sub_one_lt_choose_two hA))
  · intro h
    interval_cases A <;> decide

/-! ## 3. The braid's degree is bounded -/

/-- Per-nucleon degree in the braid's bond set: the bonds incident to `k`. -/
def degree (A k : ℕ) : ℕ :=
  ((bonds A).filter (fun e => e.1 = k ∨ e.2 = k)).card

/-- Every braid bond incident to nucleon `k` is `(k-1, k)` or `(k, k+1)`. -/
theorem incident_subset (A k : ℕ) :
    (bonds A).filter (fun e => e.1 = k ∨ e.2 = k)
      ⊆ ({(k - 1, k), (k, k + 1)} : Finset (ℕ × ℕ)) := by
  intro e he
  rw [Finset.mem_filter, bonds, Finset.mem_image] at he
  obtain ⟨⟨j, _, rfl⟩, hk⟩ := he
  rcases hk with hk | hk
  · simp only at hk; subst hk; simp
  · simp only at hk
    obtain ⟨m, rfl⟩ : ∃ m, j = m := ⟨j, rfl⟩
    subst hk; simp

/-- **The braid's per-nucleon degree never exceeds 2** — derived from the
measured bond set, not posited as a closed form. -/
theorem degree_le_two (A k : ℕ) : degree A k ≤ 2 := by
  refine le_trans (Finset.card_le_card (incident_subset A k)) ?_
  exact le_trans (Finset.card_insert_le _ _) (by simp)

/-- At `A ≥ 4` the coordination degree the block asks of every nucleon exceeds
`2`. -/
theorem two_lt_coordination_degree {A : ℕ} (hA : 4 ≤ A) :
    2 < coordinationDegree A := by
  simp only [coordinationDegree]; omega

/-- **The separation.** At `A ≥ 4` no nucleon of the braid attains the
coordination degree, so the braid's `A - 1` cannot be the block's `A - 1`. -/
theorem braid_degree_ne_coordination_degree {A : ℕ} (hA : 4 ≤ A) (k : ℕ) :
    degree A k ≠ coordinationDegree A :=
  fun h => absurd (h ▸ degree_le_two A k) (not_le.mpr (two_lt_coordination_degree hA))

/-- Sharper: the braid is not coordination-regular at any `A ≥ 4`, so no choice
of nucleon rescues the reading. -/
theorem not_coordination_regular {A : ℕ} (hA : 4 ≤ A) :
    ¬ (∀ k, degree A k = coordinationDegree A) :=
  fun h => braid_degree_ne_coordination_degree hA 0 (h 0)

end QOU.MassTheory.BraidPathNotCoordination
