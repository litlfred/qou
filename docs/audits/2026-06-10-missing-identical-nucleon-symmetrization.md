# Missing identical-nucleon S_Z×S_N symmetrization in the mass-tower endomorphism (2026-06-10)

**Status:** located finding (owner-directed). The doubly-magic pp/nn double
pairing (⁴He) is **not represented** in the canonical mass chain — the
constituent factorization treats identical nucleons as *distinguishable*.
Owner hypothesis (confirmed): "an extra S₂ symmetry acting on p-p, n-n and the
bound electron(s) … maybe a semidirect product (electron ⋊ S₂ on nn, pp)."

## 1. Where it's missing (stepping the cheat-sheet chain)

| chain step | identical-particle symmetrization? |
|---|---|
| 1 cat action / 2 Hecke / 3 Markov | — (single-strand-set level) |
| 5 Wedderburn `tr_M = Σ_λ y_λ χ^λ` over λ⊢3A | the **full** trace *does* carry all of S_{3A} … |
| **5l closed form** `tr_M = tr_M³(𝓑_p)^Z·tr_M³(𝓑_n)^N·∏fᵢ` | **…but the factorization DROPS it** — `^Z`/`^N` are plain powers (distinguishable `V^{⊗Z}`) |
| 9 mass / 9b binding (tower) | inherits the un-symmetrized factorization + a **single** nucleon ordering |
| (whole chain) | **no** exchange / wreath / Pauli / spin-statistics step anywhere |

**Compute loci.**
- `closed_form_tau_M.py:302` — `constit_part = tau_p**Z * tau_n**N` (plain powers).
- `mass_at_3A_proper.atom_braid_word_3A` — `ordering = ['p']*Z + ['n']*N`
  (one fixed arrangement; `k < A−1` chain bonds).
- The tower endomorphism (`mass_tower_operator_valued`, `mass_endomorphism`)
  consumes that single-ordering braid; no symmetrization over the S_Z×S_N
  orbit of arrangements.

## 2. The missing math

The Z protons live on 3Z strands as **identical** 3-strand blocks. The
distinguishable factorization uses `V_p^{⊗Z}`, whose trace is the **power sum**
`p₁^Z = (tr_M 𝓑_p)^Z = tau_p^Z`. Identical particles require projecting onto a
definite-symmetry subspace under the block-permutation group:

- physical algebra = **wreath product** `H₃ ≀ S_Z` (S_Z permutes the Z identical
  H₃ proton-blocks), likewise `H₃ ≀ S_N` for neutrons;
- the symmetrized traces are the **complete/elementary symmetric functions**
  of the block eigenvalues, `h_Z` (bosonic/symmetric) or `e_Z` (fermionic/
  antisymmetric — Pauli), NOT the power `p₁^Z`. For Z = 2:

  `p₁² = h₂ + e₂ ,  h₂ = (p₁² + p₂)/2 ,  e₂ = (p₁² − p₂)/2`

  so the symmetrized constituent differs from the naive `tau_p²` by
  `±p₂/2 = ±(tr_M(𝓑_p²-block) )/2` — an **O(1)** correction, the right size for
  the ⁴He doubly-magic excess (the complete-graph derived binding under-shoots
  ⁴He by 1.20×; see `2026-06-10-binding-bond-graph-compute-audit-and-derivation.md`).

**The electron — semidirect, as the owner posited.** The bound electron(s)
enter through the interface factors `f_pe` (p-e crossings), a **different
species** not permuted by the nucleon S_Z×S_N. So the symmetry that acts on the
nucleus is

  `G = (H₃ ≀ S_Z) × (H₃ ≀ S_N)` on the nucleon blocks,

with the electron strand fixed by it — and if the electron's binding *couples*
to the nucleon-pair exchange (it sees the pp/nn shells), the realized group is a
**semidirect** `⟨electron⟩ ⋊ (S_Z × S_N)`: the electron acts, S₂ permutes the
pp and nn pairs only. For ⁴He: `(S₂ × S₂) ⋊ ⟨e⟩`.

## 3. The fix / test (concrete)

The single-ordering trace `tr_M(p^Z n^N)` should be replaced by the
**S_Z×S_N-symmetrized average over the S_A/(S_Z×S_N) distinct arrangements** of
the identical nucleons (equivalently, the wreath-symmetrized constituent
`h_Z`/`e_Z` instead of `tau_p^Z`). For ⁴He the orbit is the
`4!/(2!2!) = 6` arrangements (ppnn, pnpn, pnnp, npnp, nppn, nnpp), whose
chain-bond multisets differ (`{pp,pn,nn}` vs `{pn,pn,pn}` …). The **doubly-magic
correction = (symmetrized − single-ordering)**. Test: does the symmetrized
binding move ⁴He from 1.20× toward B_AME while leaving D (no like-pair, single
arrangement) unchanged?

## 4. Trace through Bring's surface

The arrangement count is the tell. ⁴He's identical-nucleon orbit has **6**
arrangements (`S₄/(S₂×S₂)`), and **6** is the framework's recurring Bring number:

- `6 = |S₃| = dim_ℂ H₃(q) = #` GS-NF knot operators = `|χ(Bring)|` (Step 4,
  `prop:x5-bring-weight-identification`; Bring's curve has genus 4, χ = −6).
- Bring's curve automorphism group is **S₅** (order 120). The nucleon
  arrangement group `S₄ ⊂ S₅` is the point-stabilizer; the **electron is the
  5th point**, so `(nucleon S₄) ⋉ ⟨e⟩ ↪ S₅` is exactly the owner's semidirect
  structure realized as the Bring/icosahedral symmetry.
- `S₅` has **n₅ = 6 Sylow-5 subgroups**; S₅ acting on those 6 by conjugation is
  the exceptional map `S₅ ↪ S₆` — the same **6** as the H₃ / χ(Bring) basis.
  So the 6 nucleon arrangements ↔ the 6 Sylow-5's ↔ the 6 Bring sheets / H₃
  knot-operators.
- The S₂×S₂ ⊂ S₄ is the **Klein-four** `V = {e,(12)(34),(13)(24),(14)(23)}`
  (the double-transpositions) — the normal V₄ ◁ S₄ whose quotient `S₄/V ≅ S₃`
  is **again the 6-element Bring basis**. The pp/nn double-exchange is precisely
  this V₄, and the recent H₂S work (`ζ₅ chiral fibre of Bring`, the `1/√5`)
  lives on the same S₅/A₅ icosahedral fibre.

**Reading:** the identical-nucleon symmetrization is not an ad-hoc add-on — it
is the `S₄ ⋉ ⟨e⟩ ↪ S₅ = Aut(Bring)` action that the χ=−6 step already names,
restricted to the nucleon block-permutations. The mass-tower endomorphism
currently projects onto the **trivial** S_Z×S_N (the `^Z` power), discarding the
V₄ double-transposition (= the doubly-magic pairing) that the Bring S₅ symmetry
supplies.

## 5. Discipline

- This is a **located structural gap + a symmetric-function-level prediction**,
  NOT a fitted closure. The symmetrization is forced (identical-particle
  statistics + the existing χ=−6 S₅ structure), with one physical choice to pin
  (symmetric `h_Z` vs antisymmetric `e_Z` = boson vs Pauli-fermion shell).
- Next: the arrangement-symmetrization probe (§3) to measure the correction's
  size against the ⁴He doubly-magic excess; if it lands, wire the wreath-
  symmetrized constituent into `closed_form_tau_M` (replacing `^Z` by `h_Z`/`e_Z`).
- Cross-refs: `2026-06-10-binding-bond-graph-compute-audit-and-derivation.md`
  (the bond-graph / edge-set refutation — the static graph fails at exactly D
  and ⁴He, the two arrangements-symmetry extremes); Step 4 χ=−6 Bring.
