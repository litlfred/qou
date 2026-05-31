import Mathlib

/-!
# QOU.BraidKnot.InterfaceComposition

Canonical-braid interface composition for content block
`canonical-braid-interface-composition`, plus the **Tier 1.B follow-up
lemmas** flagged in
[`docs/audits/2026-05-30-tier-1b-orbit-reduction.md`](../../../../../docs/audits/2026-05-30-tier-1b-orbit-reduction.md)
§Follow-ups and the orbit-trace identity proof:

* **Lemma 1 — word-construction invariance.** A same-species permutation
  `σ ∈ S_Z × S_N` leaves the atomic braid word unchanged. At the ordering
  (species-sequence) level this is the statement that a permutation of the
  proton block (resp. neutron block) — a *constant* list — equals that block,
  so the concatenated canonical ordering, and hence the braid word built from
  it, is fixed.
* **Interface-minimality.** The canonical `p…pn…n` ordering attains the
  minimum number of mixed proton–neutron interfaces, `n_pn = 1`, over every
  ordering containing at least one proton and one neutron.

An ordering is modelled as a `List Bool` (`true` = proton, `false` = neutron),
matching the species sequence consumed by `atom_braid_word_3A`.

> **Authoring note.** The `sorry`-marked proofs are routine list combinatorics;
> they are *stated* here (the formalisation deliverable) and discharged on a
> `lake build` pass — the Lean toolchain was not installed in the authoring
> session, so the proof bodies are not yet machine-checked.
-/

namespace QOU.BraidKnot

/-- An atom ordering of nucleon blocks: `true` = proton, `false` = neutron.
    The species sequence consumed by `atom_braid_word_3A`. -/
abbrev Ordering := List Bool

/-- Adjacent nucleon pairs — the `A-1` inter-nucleon interfaces. -/
def adjPairs (l : Ordering) : List (Bool × Bool) := l.zip l.tail

/-- Mixed proton–neutron interfaces `n_pn`. -/
def nPN (l : Ordering) : ℕ := (adjPairs l).countP (fun p => decide (p.1 ≠ p.2))

/-- Proton–proton interfaces `n_pp`. -/
def nPP (l : Ordering) : ℕ := (adjPairs l).countP (fun p => p.1 && p.2)

/-- Neutron–neutron interfaces `n_nn`. -/
def nNN (l : Ordering) : ℕ := (adjPairs l).countP (fun p => !p.1 && !p.2)

/-- Interface composition triple `(n_pp, n_pn, n_nn)` (content block
    `def:canonical-braid-interface-composition`). -/
structure InterfaceComposition where
  /-- proton–proton interface count -/
  pp : ℕ
  /-- proton–neutron interface count -/
  pn : ℕ
  /-- neutron–neutron interface count -/
  nn : ℕ

/-- Interface composition of an ordering. -/
def composition (l : Ordering) : InterfaceComposition := ⟨nPP l, nPN l, nNN l⟩

/-- The canonical `p…pn…n` ordering for `(Z, N)`. -/
def canonical (Z N : ℕ) : Ordering :=
  List.replicate Z true ++ List.replicate N false

/-! ## Lemma 1 — word-construction invariance (ordering level) -/

/-- A same-species permutation acts trivially on the canonical ordering:
    any rearrangement of the proton block and the neutron block reproduces the
    canonical ordering, because each block is a constant list. Hence the braid
    word built from the ordering is unchanged (the content of Lemma 1).

    Proof sketch: `List.perm_replicate` gives `pp = replicate Z true` and
    `nn = replicate N false` from the same-species permutation hypotheses; the
    concatenation is then definitionally `canonical Z N`. -/
theorem same_species_perm_fixes (Z N : ℕ) (pp nn : Ordering)
    (hp : pp ~ List.replicate Z true) (hn : nn ~ List.replicate N false) :
    pp ++ nn = canonical Z N := by
  sorry -- Ref: [manuscript] docs/audits/2026-05-30-orbit-trace-identity-proof.md (Lemma 1)

/-! ## Interface-minimality of the canonical ordering -/

/-- The canonical ordering of a genuine atom (`Z, N ≥ 1`) has exactly one mixed
    proton–neutron interface (the single `p…p ∣ n…n` boundary). -/
theorem canonical_nPN_eq_one (Z N : ℕ) (hZ : 0 < Z) (hN : 0 < N) :
    nPN (canonical Z N) = 1 := by
  sorry -- Ref: [manuscript] canonical-braid-interface-composition.md (n_pn = 1 for Z,N ≥ 1)

/-- Any ordering containing both a proton and a neutron has at least one mixed
    interface — a list with no mixed adjacent pair is constant on a single
    species, contradicting the presence of both. -/
theorem nPN_pos_of_mixed (l : Ordering) (ht : true ∈ l) (hf : false ∈ l) :
    1 ≤ nPN l := by
  sorry -- Ref: [manuscript] docs/audits/2026-05-30-tier-1b-orbit-reduction.md (interface-minimality)

/-- **Interface-minimality.** Among all orderings with at least one proton and
    one neutron, the canonical `p…pn…n` ordering attains the minimum number of
    mixed proton–neutron interfaces (`n_pn = 1`). Derived from
    `canonical_nPN_eq_one` (= 1) and `nPN_pos_of_mixed` (≥ 1). -/
theorem canonical_nPN_min (Z N : ℕ) (hZ : 0 < Z) (hN : 0 < N)
    (l : Ordering) (ht : true ∈ l) (hf : false ∈ l) :
    nPN (canonical Z N) ≤ nPN l := by
  rw [canonical_nPN_eq_one Z N hZ hN]
  exact nPN_pos_of_mixed l ht hf

end QOU.BraidKnot
