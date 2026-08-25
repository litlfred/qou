# Front 4-B: pairwise linking cannot carry the intra-nucleon EM self-energy

**Bean:** `qou-bhfg`. **Date:** 2026-08-25. **Kind:** formalize-first prune
(AGENTS.md §"Formalize-first probe discipline"), machine-checked.

## What 4-B needs

The two-like-charge EM-linking invariant gates **two** fronts at once: the
`m_d − m_u` extraction and 69 % of the ³He mirror residual. Stage-1 scoping is
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

**Two objects are missing, not one** — corrected after the retraction above:

1. **A computable `μ̄₁₂₃` for ≥ 3 components.** The corpus has a name and a
   conjecture class, not a computation. Tractable: for a closed braid with
   vanishing pairwise linking, `μ̄₁₂₃` has no indeterminacy and is the degree-2
   Magnus coefficient of a longitude word — a finite computation of the same
   shape as `crossSum` above.
2. **The map from a triple linking number to an energy.** The same gap as
   everywhere on this surface, and untouched by any of the above.

Do not report 4-B as "one object away". It is two, and only the first is
currently tractable.
