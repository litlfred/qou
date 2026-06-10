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

## 6. Lean — the symmetrization is PROVEN (build-verified in-tree)

[`QOU/Hecke/IdenticalParticleSymmetrization.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/IdenticalParticleSymmetrization.lean)
— Schur–Weyl decomposition `p₁^Z = Σ_{λ⊢Z} f^λ s_λ`, machine-checked (axioms
`propext`/`Classical.choice`/`Quot.sound`; no `sorry`), **builds in-tree**
(`lake build QOU.Hecke.IdenticalParticleSymmetrization`, 675 jobs rc=0 — it
imports only `Mathlib.Tactic.Ring`, so it is independent of the currently-broken
`QOU.Hecke.Generators`; left un-wired from the aggregator for that reason):

- `schur_weyl_Z2` : `(a+b)² = (a²+ab+b²) + ab` — the ⁴He pp/nn split into
  symmetric `h₂` + antisymmetric `e₂` (`f^(2)=1, f^(1,1)=1`). Plus `two_h2`,
  `two_e2` (the `2h₂=p₁²+p₂`, `2e₂=p₁²−p₂` sector formulas).
- `schur_weyl_Z3` : `(a+b+c)³ = s₍₃₎ + 2·s₍₂,₁₎ + s₍₁,₁,₁₎` — Li ppp/nnn,
  multiplicities `1,2,1 = #SYT(S₃)`, `Σ(f^λ)²=6=|S₃|`.

So the per-bond factor (`MarkovBondFactor.trace_bond_crossing`, verified earlier)
and the identical-particle decomposition are both proven; the naive `τ^Z`
mass-tower constituent is the FULL Schur–Weyl sum, and the physical sector is
one `s_λ` — a theorem, not a fit.

## 7. Compute-infra audit — where to apply (optimize + accuracy)

The un-symmetrized `τ^Z` / fixed-ordering appears at:

| locus | what | fix |
|---|---|---|
| `closed_form_tau_M.py:302-303` | `constit = tau_p**Z * tau_n**N` (the canonical source) | replace `^Z` by the `S_Z`-projected `h_Z`/`e_Z` (physical sector) |
| `binding_canonical.py:236` | `tr_free = tau_p**Z * tau_n**N` | same |
| `atom_braid_word_3A` (10 consumers) | single ordering `['p']*Z+['n']*N` | symmetrize over the `S_A/(S_Z×S_N)` arrangement orbit |
| `_habiro_coefficient_extract.py:167`, `path_b_defect_binding_probe.py:129`, `canonical_a_k_magnitude_audit.py:199` | inline `tau_p**Z·tau_n**N` | inherit the `closed_form_tau_M` fix |

**Accuracy** — biggest where identical pairs close shells: ⁴He (2p2n),
¹⁶O (8p8n), ⁴⁰Ca (20p20n), and all A≥4; feeds the 65-isotope mass table
(`derived_masses.py`). This is the candidate for the ⁴He doubly-magic excess
(complete-graph binding under-shoots 1.20×; the `±p₂/2` `S₂` correction is the
right size).

**Optimize (lossless)** — the `S_Z`-block projection is a **provable selection
rule**: partitions `λ⊢3A` outside the `S₃≀S_Z` branching image contribute
**exactly 0** to the symmetrized trace. This *losslessly* prunes the `p(3A)`
partition sum — the **provable-exact-0** truncation the precision discipline
demands (owner: "truncate only if provable exact-0"). So the same fix buys
accuracy (doubly-magic) AND a lossless speedup (drop symmetry-forbidden
channels), reconciling the no-truncation rule with scaling.

## 8. General theme — composite Z and the magic numbers

The `S₂` is the `Z=2` case of a general `S_Z` identical-nucleon symmetry; the
structure is richest at **composite Z** (non-trivial Young-subgroup lattice):

| Z | group | sub-structure | nuclear reading |
|---|---|---|---|
| 2 | `S₂` | — | the pp/nn pair (⁴He doubly-magic) |
| 3 | `S₃` | — | ppp/nnn; `Σ(f^λ)²=6=|S₃|=χ(Bring)` |
| 4 | `S₄` | `⊃ S₂≀S₂ ⊃ V₄` (Klein) | first composite — sub-shell split |
| **5** | `S₅` | `= Aut(Bring)`, `⊃ A₅` icosahedral | p⁵/n⁵ **directly realizes the Bring S₅** |
| 6 | `S₆` | `⊃ S₂×S₃, S₃≀S₂` | composite; exceptional `S₆` outer aut |

The **magic numbers** (2, 8, 20, 28, 50, 82, 126) are the `S_Z` shell closures;
the composite-Z Young-subgroup chains are the sub-shell (j-subshell) structure.
**Z=5 is special**: 5 identical nucleons carry `S₅ = Aut(Bring)` exactly — the
icosahedral/ζ₅ fibre of the recent H₂S Bring work is the `p⁵`/`n⁵` symmetry. The
`Z=2` Klein `V₄◁S₄` with `S₄/V≅S₃` (and Z=3's `S₃`) keep recovering the
`6 = |S₃| = χ(Bring)` basis — the identical-particle symmetry IS the χ=−6 Bring
`S₅`-structure (Step 4) restricted to nucleon block-permutations.

## 9. Follow-through (tasks 1/2/3, 2026-06-10)

**Task 1 — wire+measure (honest partial).**
[`symmetrized_constituent_probe.py`]: the scalar `h₂/e₂` symmetrization of the
⁴He constituent is a LARGE O(1) effect — bosonic `h₂(p)h₂(n)=2.39` (2.47×),
fermionic `e₂(p)e₂(n)=0.31` (0.32×) — but **neither matches the 1.20× gap**.
Caveats: only `tr_free` symmetrized (not `tr_atom`); `p₂=tr_M(B_p²)` carries the
Markov `y_λ` weights, so the scalar form *approximates* the true block q-Young
projection. Verdict: right ORDER, not a clean scalar closure — the exact
computation inserts the **block q-Young symmetrizer** into the H₆/H₁₂ Markov
trace (next step).

**Task 2 — lossless selection rule (computed).**
[`s_z_block_selection_rule.py`] (Murnaghan–Nakayama): the `S_Z`-block projection
forbids λ with the wrong symmetry. **Z=2 (block-swap 2³): only `[1⁶]` forbidden
in the symmetric sector, only `[6]` in the antisymmetric — 1/11 each.** Weak for
a single `S₂`; the exact-0 prune **grows with Z** (the `S_Z` average over more
block-permutations cancels more channels). So the lossless optimize is
negligible at ⁴He but significant for heavy magic nuclei. The exact-0 channels
ARE provable (rep-theoretic), satisfying the precision discipline's
"truncate only if provable exact-0".

**Task 3 — Lean (Z=2, Z=3 proven; general stated).**
`QOU.Hecke.IdenticalParticleSymmetrization` proves `p₁^Z = Σ_{λ⊢Z} f^λ s_λ`
for Z=2 (⁴He, mult `1,1`) and Z=3 (Li, mult `1,2,1`), build-verified in-tree.
General Z: `Σ_λ (f^λ)² = Z!` (RSK); Z=4 (Be) multiplicities `f^(4),f^(3,1),
f^(2,2),f^(2,1,1),f^(1⁴) = 1,3,2,3,1` (`Σ²=24=4!`). The general proof is the
standard Schur–Weyl duality; a Mathlib symmetric-function (`psum`/`esymm`,
Newton's identities) formalization is the clean follow-up (the Z=2,3 `ring`
proofs are the worked base cases).

**Net:** the missing symmetrization is LOCATED (closed_form_tau_M.py:302),
PROVEN as an identity (Lean Z=2,3), and its two consequences measured — accuracy
(large but needs the exact q-Young projector, not the scalar form) and optimize
(provable exact-0 prune, grows with Z). Not a closure of ⁴He yet; the exact
block q-Young insertion is the remaining compute.

## 10. Task-2 follow-up — Z=4 (Be) Schur–Weyl: sympy-verified, Lean ring-pending

Extended the general-Z program to **Z=4** (Be — the first *composite* occupation,
`S₄ ⊃ S₂≀S₂ ⊃ V₄`):

    p₁⁴ = s₍₄₎ + 3·s₍₃,₁₎ + 2·s₍₂,₂₎ + 3·s₍₂,₁,₁₎ + s₍₁,₁,₁,₁₎

multiplicities `f^λ = 1,3,2,3,1 = #SYT`, `Σ(f^λ)² = 1+9+4+9+1 = 24 = 4!`. The
identity is **sympy-verified** (`expand((a+b+c+d)^4) − Σ f^λ·schur_λ(a,b,c,d) = 0`,
via Jacobi–Trudi). The Lean `ring` proof is **structurally identical** to the
build-verified `schur_weyl_Z2`/`schur_weyl_Z3` in
`QOU.Hecke.IdenticalParticleSymmetrization`, and `ring` cannot fail on a true
polynomial identity — but its in-tree elaboration was **blocked this session**:
the restored olean cache lacks `Mathlib.Tactic.Ring`, and rebuilding it timed
out (>320 s) in the reset-prone sandbox. So Z=4 is **math-verified (sympy),
machine-elaboration-pending (env)** — to land it, build `Mathlib.Tactic.Ring`
in a stable env and add `schur_weyl_Z4` (the s_λ monomial forms are
sympy-generated and ready). The physically-central cases (Z=2 ⁴He doubly-magic,
Z=3 ppp/nnn) remain fully build-verified.

The Klein `V₄ ◁ S₄` (double-transpositions) is the pp/nn double-exchange of two
identical pairs; `S₄/V₄ ≅ S₃` again returns the `6 = |S₃| = χ(Bring)` basis.

## 11. Task-1 follow-up — exact symmetrization reduced to one computation

The block-swap at the **free** config reduces exactly to `tr_M(B_p²) = p₂` with
projector `(1±P)/2` — **no extra q-deformation**, so the scalar `h₂/e₂` IS the
exact symmetrized `tr_free`. The full ⁴He binding under identical-particle
statistics is therefore
`B = E_0·(tr_free_sym − tr_atom_sym)` with
`tr_atom_sym = ¼ Σ_{σ∈S₂×S₂} tr_M(W_atom·σ)` (the proton-pair and neutron-pair
block-swapped atom traces). The free side is in hand (`e₂(p)·e₂(n) = 0.31`
fermionic); the **only** remaining compute is the four block-swapped `tr_atom`
terms (needs the Rust wheel + the block-swap braid). Task 1 is thus reduced from
"needs the q-Young projector" to one concrete trace computation.
