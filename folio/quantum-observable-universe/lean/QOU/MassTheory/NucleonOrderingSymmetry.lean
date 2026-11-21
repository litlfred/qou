import Mathlib.Data.List.Count
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.MassTheory.NucleonOrderingSymmetry

**The same-species orbit symmetrization of an atomic braid word is the IDENTITY
MAP; the cross-species reordering is not a symmetry of the construction at all.**

Bean `qou-prjo`. Companion to
[`TransversePairingClusterDecomposition`](TransversePairingClusterDecomposition.lean)
(the pairing is exactly bilinear) and
[`GermRootVectorGaugeFixing`](GermRootVectorGaugeFixing.lean).

## Why this file exists

PR #4849 measured the multi-generator transverse NA-Stokes pairing, found it
super-pairwise, and then disqualified it on the ground that it depends on the
nucleon **ordering** (`pnn` / `npn` / `nnp`), citing the corpus orbit identity
`tr_M(β) = tr_M(rep)` as evidence that the corpus's own scalar observable is
ordering-invariant.

That citation conflates two different permutation groups. The corpus identity
(`computations/atom_orbit_reduction.py`;
`docs/audits/2026-05-30-orbit-trace-identity-proof.md`) is over `S_Z × S_N` —
protons among protons, neutrons among neutrons — and its **Lemma 1** establishes
it by showing that such a permutation leaves the braid **word** unchanged. This
file formalises exactly that distinction:

* `wordOf_of_speciesPreserving` — a species-preserving relabelling leaves the
  word **literally equal**. Hence
* `sum_symmetrize_eq_nsmul` — summing any readout `f` over a finite set of such
  relabellings gives `card • f (word)`: **orbit-symmetrization over the forced
  group is the identity map**, for every readout, scalar or operator-valued. It
  cannot cancel anything, so a nonzero residual survives it trivially.
* `ifaces_pnn_ne_ifaces_npn` and `wordOf_pnn_ne_wordOf_npn` — a **cross-species**
  reordering changes the interface list, hence changes the word. It is therefore
  not a symmetry of the construction, and no invariance under it can be assumed.

## What is NOT proved — read before citing

* Nothing here derives a **magnitude**: no binding energy, no `Δ_λ`, no
  transverse-pairing value, no AME comparison. `sorry-free ≠ derived`.
* This does **not** revive the transverse route. It removes one of the two
  blockers #4849 named (the demand for a nucleon-symmetric readout, which is
  vacuous). The other — *which* two germ observers, plus the representation
  gauge — is untouched and still binding.
* `wordOf_pnn_ne_wordOf_npn` is proved under the hypotheses that the `pn`
  interface letter is distinct from the `nn` one and does not occur inside
  either intra-nucleon chain. Both hold for the corpus letters
  (`pp = σ`, `nn = σ⁻¹`, `pn = σ − h(½ − δ/4)` on the interface generator,
  which no intra chain uses), but they are hypotheses here, not corpus facts
  imported into Lean.

**Base ring (§7c).** No ring at all: the content is combinatorial. Letters live
in a generic type `L` (`DecidableEq` only where the counting argument needs
it); the symmetrization lemma takes a
generic `AddCommMonoid M` target. No `ℝ`, no ordering, no `Real.*`.

## References
- Ref: [leitner2026] `docs/audits/2026-05-30-orbit-trace-identity-proof.md`
  (Lemma 1 — the word is unchanged under a same-species permutation).
- Ref: [leitner2026] `docs/audits/2026-08-09-nastokes-orbit-symmetric-readout.md`
-/

namespace QOU.MassTheory.NucleonOrdering

/-! ## 1. Species, interfaces, and the atomic word -/

/-- A nucleon species. -/
inductive Species
  | p
  | n
  deriving DecidableEq, Repr

/-- The adjacency type of a neighbouring pair — the corpus `_interface_type`. -/
inductive Iface
  | pp
  | pn
  | nn
  deriving DecidableEq, Repr

open Species Iface

/-- `_interface_type` of `computations/atom_orbit_reduction.py`: like species give
`pp` / `nn`, unlike species give `pn` in either order. -/
def iface : Species → Species → Iface
  | Species.p, Species.p => Iface.pp
  | Species.n, Species.n => Iface.nn
  | _, _ => Iface.pn

/-- The interface list of an ordering — the corpus `interface_multiset`, kept
ordered. -/
def ifaces : List Species → List Iface
  | [] => []
  | [_] => []
  | a :: b :: rest => iface a b :: ifaces (b :: rest)

variable {L : Type*}

/-- The atomic braid word of an explicit species ordering, in the shape of
`atom_orbit_reduction.atom_braid_word_ordered`: per nucleon its species
intra-chain, followed by the adjacency-typed interface letter joining it to the
next nucleon.

`intra` supplies the two species chains and `lk` the three interface letters;
the generator-index bookkeeping of the Python emitter is irrelevant to every
statement below and is omitted. -/
def wordOf (intra : Species → List L) (lk : Iface → L) : List Species → List L
  | [] => []
  | [s] => intra s
  | a :: b :: rest => intra a ++ lk (iface a b) :: wordOf intra lk (b :: rest)

/-! ## 2. Same-species relabelling fixes the word — Lemma 1, formalised -/

/-- **The word depends on the nucleon labelling only through the species
string.** A relabelling `σ` of nucleon indices that preserves species
(`s (σ k) = s k` — exactly the condition defining `S_Z × S_N`) leaves the
species string, hence the whole word, **literally unchanged**.

This is Lemma 1(a) of the orbit-trace identity proof. Note what it does *not*
say: it is not an invariance of a readout under a nontrivial transformation of
the word. The word never moves. -/
theorem wordOf_of_speciesPreserving {A : ℕ} (intra : Species → List L)
    (lk : Iface → L) (s : Fin A → Species) (σ : Fin A → Fin A)
    (h : ∀ k, s (σ k) = s k) :
    wordOf intra lk (List.ofFn (fun k => s (σ k)))
      = wordOf intra lk (List.ofFn s) := by
  have : (fun k => s (σ k)) = s := funext h
  rw [this]

/-- **Orbit-symmetrization over the forced group is the identity map.**

For *any* readout `f` — scalar trace, operator norm, the transverse pairing,
anything — summing over a finite family `G` of species-preserving relabellings
returns `G.card • f (word)`. Averaging over the `S_Z × S_N` orbit therefore
changes **nothing**: it cannot cancel a residual, and it cannot create one.

The hypothesis is the whole content: it is what fails for a cross-species
reordering (§3). -/
theorem sum_symmetrize_eq_nsmul {A : ℕ} {M : Type*} [AddCommMonoid M]
    (intra : Species → List L) (lk : Iface → L) (s : Fin A → Species)
    (G : Finset (Fin A → Fin A)) (hG : ∀ σ ∈ G, ∀ k, s (σ k) = s k)
    (f : List L → M) :
    (∑ σ ∈ G, f (wordOf intra lk (List.ofFn (fun k => s (σ k)))))
      = G.card • f (wordOf intra lk (List.ofFn s)) := by
  rw [Finset.sum_congr rfl (fun σ hσ => by
    rw [wordOf_of_speciesPreserving intra lk s σ (hG σ hσ)]), Finset.sum_const]

/-! ## 3. Cross-species reordering is not a symmetry -/

/-- The tritium orderings of PR #4849 §5.1 have **different interface lists**:
`pnn ↦ [pn, nn]` but `npn ↦ [pn, pn]`. They are not related by any
species-preserving relabelling, and no corpus identity covers them. -/
theorem ifaces_pnn_ne_ifaces_npn :
    ifaces [Species.p, Species.n, Species.n] ≠ ifaces [Species.n, Species.p, Species.n] := by
  decide

/-- Counting the `pn` interface letter in the word recovers the interface list's
`pn` count, provided that letter is distinct from the other two interface
letters and does not occur inside either intra-nucleon chain. -/
theorem count_link_pn [DecidableEq L] (intra : Species → List L) (lk : Iface → L)
    (hp : lk Iface.pn ∉ intra Species.p) (hn : lk Iface.pn ∉ intra Species.n)
    (hnn : lk Iface.pn ≠ lk Iface.nn) (hpp : lk Iface.pn ≠ lk Iface.pp) :
    ∀ ss : List Species,
      (wordOf intra lk ss).count (lk Iface.pn) = (ifaces ss).count Iface.pn := by
  intro ss
  induction ss with
  | nil => simp [wordOf, ifaces]
  | cons a t ih =>
    cases t with
    | nil =>
      simp only [wordOf, ifaces, List.count_nil]
      cases a
      · exact List.count_eq_zero.mpr hp
      · exact List.count_eq_zero.mpr hn
    | cons b r =>
      have hia : (intra a).count (lk Iface.pn) = 0 := by
        cases a
        · exact List.count_eq_zero.mpr hp
        · exact List.count_eq_zero.mpr hn
      rw [wordOf, ifaces, List.count_append, hia, List.count_cons, List.count_cons, ih,
        Nat.zero_add]
      congr 1
      cases a <;> cases b <;>
        simp [iface, Ne.symm hnn, Ne.symm hpp]

/-- **The cross-species reorderings produce different words.** With the corpus's
distinct interface letters, `pnn` carries one `pn` crossing and `npn` carries
two, so the words are not equal.

Together with `sum_symmetrize_eq_nsmul` this is the whole finding: the group the
corpus's orbit identity ranges over acts trivially, while the group PR #4849
varied over is not a symmetry of the construction — the word genuinely
changes. -/
theorem wordOf_pnn_ne_wordOf_npn [DecidableEq L] (intra : Species → List L) (lk : Iface → L)
    (hp : lk Iface.pn ∉ intra Species.p) (hn : lk Iface.pn ∉ intra Species.n)
    (hnn : lk Iface.pn ≠ lk Iface.nn) (hpp : lk Iface.pn ≠ lk Iface.pp) :
    wordOf intra lk [Species.p, Species.n, Species.n]
      ≠ wordOf intra lk [Species.n, Species.p, Species.n] := by
  intro hEq
  have h1 := count_link_pn intra lk hp hn hnn hpp [Species.p, Species.n, Species.n]
  have h2 := count_link_pn intra lk hp hn hnn hpp [Species.n, Species.p, Species.n]
  rw [hEq, h2] at h1
  have e1 : (ifaces [Species.p, Species.n, Species.n]).count Iface.pn = 1 := by decide
  have e2 : (ifaces [Species.n, Species.p, Species.n]).count Iface.pn = 2 := by decide
  rw [e1, e2] at h1
  exact absurd h1 (by decide)

end QOU.MassTheory.NucleonOrdering
