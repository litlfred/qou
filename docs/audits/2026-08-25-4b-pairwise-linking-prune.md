# Front 4-B: pairwise linking cannot carry the intra-nucleon EM self-energy

**Bean:** `qou-bhfg`. **Date:** 2026-08-25. **Kind:** formalize-first prune
(AGENTS.md §"Formalize-first probe discipline"), machine-checked.

## What 4-B needs

The two-like-charge EM-linking invariant was recorded as gating **two** fronts
at once: the `m_d − m_u` extraction and 69 % of the ³He mirror residual.

> **🛑 That framing is wrong — see
> [`2026-08-25-4b-corrections-duplication-and-two-fronts.md`](2026-08-25-4b-corrections-duplication-and-two-fronts.md).**
> The two fronts are different objects (two up **quarks** inside a nucleon vs
> the two **protons** of ³He), and the S₃ probe's (A1) *derives* that the
> intra-nucleon self-energy cancels identically in binding energy — which is
> what the mirror split measures. The 69 % is unsourced. This file repeated the
> claim uncritically; the Lean below is unaffected. Stage-1 scoping is
committed
([`quark-mass-extraction-stage1.witness.json`](../computations/quark-mass-extraction-stage1.witness.json)):

    δ_QCD = Δ_pn + E_EM,     Δ_pn = 1.2933 MeV  (framework-derived)

with the lattice comparator `E_EM ≈ 0.8 MeV`. The witness's own `honest_gap`
field names the blocker as the **intra-nucleon** EM self-energy — the
framework's only derived EM mechanism, `tanh(ln q₀) × strong bond`, being
*inter*-nucleon.

## The prune

The first ansatz anyone reaches for is a functional of the **pairwise linking
numbers** of the constituent strands. That class is empty on the proton, and it
is cheap to show.

The proton braid is the Borromean link, presented in the corpus as the closed
braid `(σ₀σ₁⁻¹)³ ∈ B₃`
([`brunnian-property-of-borromean.md`](../content/quantum-observable-universe/knots-particles-confinement/brunnian-property-of-borromean.md)).
Simulating that word — each letter exchanges the strands at positions `i`,
`i+1` and contributes a crossing of its sign between *those two strands* —
gives signed crossing sums of `0` for all three pairs:

| pair | signed crossing sum | `lk` |
|---|---:|---:|
| `(0,1)` | 0 | 0 |
| `(0,2)` | 0 | 0 |
| `(1,2)` | 0 | 0 |

So the pairwise linking data of the proton braid is **identical to the
3-component unlink's**. A self-energy functional of that data alone must
therefore assign the proton whatever it assigns the unlink — which for a
self-energy is `0`, not `0.8 MeV`.

This is a **scope-(b)** exclusion of the ansatz class: the invariant is named,
computed, and machine-checked, per the AGENTS.md requirement that scope-(b)
cite a proved invariant rather than a failed fit.

## The Lean

`QOU/BraidsAndKnots/BorromeanPairwiseLinking.lean`, sorry-free, no
`native_decide`:

| declaration | statement | axioms |
|---|---|---|
| `borromean_perm_id` | the word closes to a genuine **3**-component link | none |
| `borromean_crossSum_zero` | all three pairwise sums vanish | none |
| `hopf_crossSum_ne_zero` | **control** — the same simulator returns `2` on `σ₀²` | none |
| `pairwise_functional_cannot_separate` | any `F` of the pairwise data gives `F 0 0 0` | `propext` |

Three of the four depend on **no axioms at all** — they are pure kernel
computation over a six-letter word.

**The control is the point.** Without `hopf_crossSum_ne_zero` the vanishing
result would be indistinguishable from a simulator that returns zero on
everything. With it, the zeros are a fact about the Borromean word.
`borromean_perm_id` closes the other escape: the strand ordering returns to the
identity, so the zeros are not an artifact of components having been merged.

## What this does NOT say

- **Nothing against `μ̄₁₂₃`.** The Milnor triple linking number is precisely the
  first invariant that is *nonzero* on Borromean rings. This file points at it
  rather than away from it.

  > **🛑 RETRACTED, same day, by the author of the sentence.** This bullet first
  > read *"the corpus already carries `μ̄₁₂₃` (Lean, sorry-free) for the
  > `sin²θ_W` front (#4597), so the object is in hand."* **It does not, and the
  > object is not in hand.** What the corpus carries is
  > `electroweak-triplet-charge-spin-from-involution.lean`'s
  >
  > ```lean
  > def evenTwistTripleLinking (_k : ℕ) : ℤ := 0
  > ```
  >
  > which is defined **only** for the even-twist carrier `T(2,2k)` — a
  > **two**-component link — and is `0` *by definition*, because a 2-component
  > link has no triple. Its docstring says exactly that. It is correct, and it
  > is contentless for a 3-component question. The corpus's other Milnor
  > material (`QOU/KnotTheory/Vassiliev/MilnorVassilievBridge.lean`) is
  > **honest conjecture classes**, not computation.
  >
  > So there is **no computable `μ̄₁₂₃` for ≥ 3 components in the corpus.** That
  > is the actual missing object for 4-B, and it is a bigger gap than this file
  > originally implied.
  >
  > How the error happened, since it is the one AGENTS.md warns about by name:
  > I topic-grepped "Milnor", found several hits including a sorry-free Lean
  > file, and inferred availability — without the **arity** check
  > (§"Grep the claim SHAPE, not only the topic"). One look at the signature
  > settles it: `ℕ → ℤ` on a 2-component family cannot answer a 3-component
  > question.
- **It does not prove `conj:brunnian-property-of-borromean`.** That every
  2-component sublink is the *unlink* is strictly stronger: vanishing linking
  number is necessary, not sufficient. The conjecture stands open, and the
  corpus's own note that naive strand-deletion yields `(σ₀⁻¹)³` — a negative
  trefoil closure needing explicit Reidemeister moves — is exactly why.
- **It does not derive `E_EM`.** No value is claimed. One ansatz class is
  removed and the next target named.

## Next

Attack `E_EM` through `μ̄₁₂₃` rather than pairwise linking. What makes that a
direction rather than a hope is the prune itself: `μ̄₁₂₃` is the *unique*
first-order candidate left once pairwise linking is excluded on a Brunnian
carrier.

**Two objects were missing, not one** — identified after the retraction above.
**The first is now supplied**; the second is not.

1. ~~A computable `μ̄₁₂₃` for ≥ 3 components.~~ **DONE**, same session:
   `QOU/BraidsAndKnots/MilnorTripleLinkingMagnus.lean`, sorry-free, and every
   theorem in it depends on **no axioms at all**.

   | declaration | statement |
   |---|---|
   | `magnus_commutator` | the degree-2 expansion of `[x₁,x₂]` is `1 + X₁X₂ − X₂X₁` |
   | `mubar_borromean_eq_one` | **`μ̄₁₂₃ = 1`** on the Borromean braid (a Lean port — `binding_mn_milnor_linking.py` already had this value; see the corrections audit) |
   | `mubar_unlink_eq_zero` | `μ̄₁₂₃ = 0` on the unlink |
   | `mubar_separates_borromean_from_unlink` | the invariant separates what pairwise linking could not |
   | `noncommutator_degree_one_nonzero` | control on the well-definedness hypothesis |

   **A coherence check fell out.** The degree-1 Magnus coefficients *are* the
   linking numbers, so `magnus_commutator`'s `c1 = c2 = 0` reproduces
   `borromean_crossSum_zero` by a completely different route — a braid-word
   crossing simulation there, a free-group series here. Two independent
   computations agreeing is worth more than either alone. It also verifies
   rather than assumes the condition under which `μ̄₁₂₃` is
   indeterminacy-free.

   **Two topological inputs are consumed, not proved:** Milnor's identification
   of `μ̄₁₂₃` with the `X₁X₂` coefficient of the longitude, and that the
   Borromean longitude is `[x₁, x₂]`. Both are standard and cited.

2. **The map from a triple linking number to an energy.** Still open — but no
   longer untouched. A second formalize-first prune constrains its *shape*.

   `μ̄₁₂₃` reverses sign under an odd permutation of the components. The two
   like-charged strands of the proton are components `1` and `2` (the two up
   quarks, with the down as `3`), and a Coulomb self-energy between two
   **identical** charges must be symmetric under exchanging them. Computed, not
   quoted:

   | declaration | statement |
   |---|---|
   | `mubar_swap_eq_neg` | `μ̄₁₂₃` flips sign under exchanging components 1 and 2 |
   | `odd_symmetric_functional_vanishes` | any **odd** functional of `μ̄₁₂₃` that is exchange-symmetric is `0` |
   | `linear_coefficient_must_vanish` | in particular an exchange-symmetric `E_EM = c·μ̄₁₂₃` forces `c = 0` |

   So `E_EM` cannot be **linear** in `μ̄₁₂₃` — the obvious first ansatz, now
   excluded before anyone fits it. The map must be **even**: `|μ̄₁₂₃|`,
   `μ̄₁₂₃²`, and so on.

   The physics input consumed is only that the self-energy is
   exchange-symmetric. The antisymmetry itself is computed.

So 4-B is **one object away**, that object is the hard one, and its shape is now
constrained from both sides: the input must be `μ̄₁₂₃` (pairwise cannot see the
carrier) and the map must be even in it (odd maps vanish by exchange symmetry).
**No value for `E_EM` is claimed.**
