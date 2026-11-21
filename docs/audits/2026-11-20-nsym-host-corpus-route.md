# 𝒩_sym host composition (⊗ or ⊕): what the rest of the corpus says

Date: 2026-11-20. Scope: the open composition rule in
`conj:g-action-on-substrate` (owner ruling 2026-11-20: left open until a
structural derivation decides). This audit reads the corpus structure only. The
back-solved anchor `𝒩_sym(q₀) ≈ 213.11` (`computations/n_sym_numerical_anchor.py`,
which divides a G_F-derived `N_v` by `∏_{k=2,3,4}[2k]_q²/[2]_q`) is **not** used
to choose anything.

## Verdict

The corpus decides neither reading (a) `[4]²[6]` nor reading (b) `2[4]+[6]` as
the block states them. It fixes a third structure, conditional on the
torus-link identification and the sector postulate, which the block already
depends on:

1. **Tensor product across distinct carriers.** `W`, `Z` and the `T(2,8)` carrier sit
   on disjoint strand pairs `σ₁, σ₃, σ₅` in
   `H_{(2,2,2)}(q) ≅ H₂(q)^{⊗3} ⊂ H₆(q)`
   (`mass-theory/weak-spectral-completeness.md:63-65`;
   `mass-theory/hoefsmit-ew-cell-content.md:3-9`). That parabolic factorisation
   is a theorem of the Hecke relations. Only the exhaustion statement is a
   conjecture.
2. **`W⁺` and `W⁻` share one slot.** There is one `W` link, `T(2,4)`
   (`knots-particles-confinement/electroweak-higgs-torus-link-triplet.md`, display
   at top). `W⁻` carries the swap image `a_{W⁻} = a_{W⁺}^{-1}` of `W⁺`
   (`knots-particles-confinement/electroweak-triplet-charge-spin-from-involution.md:2`).
   Their σ-odd sector vectors are negatives of each other, so they span one line
   (Lean, below). So `W⁺` and `W⁻` are neither two tensor factors, which
   reading (a) needs, nor two independent summands, which reading (b) counts.
   Table 1 of the block is consistent with this: it lists `W^±` as the `T^±`
   weight spaces of the single adjoint `(1,0)`, not as separate irreducibles.

Under this structure, if (G-2) and (G-4) are taken as given, the composite
counts each carrier once:

  `[4]_q · [6]_q · tr_F(e_H) = [4]_q [6]_q ≈ 26.2530` at q₀ = 1.10997859564273904668.

The value is recorded and was not compared with 213.11 to choose it.

### What the corpus does NOT supply

- **The per-host weights `[4]`, `[6]` are not q-dimensions of the slot objects.**
  The Hoefsmit slot is `V ⊗ V`, with `dim_q = [2]² = [3] + [1]` (Lean). With
  `dim_q V_j = [2j+1]`, `[4]` and `[6]` are `dim_q V_{3/2}` and
  `dim_q V_{5/2}`. Neither spin occurs in Table 1. The adjoint `(1,0)` that
  Table 1 assigns to `W^±` and `Z` has `dim_q = [3]` in total. (G-2) therefore
  gets `[2k]` from the crossing number of `T(2,2k)`, not from a representation.
  That makes (G-2) a separate gap.
- **The `H` slot.** In the Hoefsmit realisation, `H` is the `σ₅⁸ = T(2,8)` slot, whose `A₊` part is the Higgs (`electroweak-higgs-torus-link-triplet.md` §"σ₅⁸ bar-grading"). (G-2)'s `[2]` does not match `[8]`. Under (G-4) the factor is 1 either way.
- **Trace multiplicativity across slots** is a property of the Markov/Ocneanu
  trace on split braids. It is not formalised here: the Lean below proves
  multiplicativity only for a weighted diagonal trace on a product index set.

## A different corpus route to N_v

`electroweak-higgs-torus-link-triplet.md:66` uses the tree term
`q·([2]/2)·[4]·[6]·[8]`, one factor per carrier with `[4]` counted once. This
agrees with point 2 above and conflicts with the anchor script's
`∏[2k]²/[2]`. Two separate factorisations of `N_v` are live in the corpus.

## Inconsistencies found (flag; not edited)

- `mass-theory/weak-spectral-completeness.md:157` quotes
  `𝒩_sym^Plancherel = q⁶(1+q²+q⁴)/3` (≈ 2.338). `weak-symmetric-normalization.md`
  gives `q⁴(1+q²+q⁴)/3` (≈ 1.897), and `hoefsmit-ew-cell-content-table2-data.md`
  tabulates ≈ 1.90. The q⁶ prefactor looks like a misprint. The stated factor of
  "~22" (41.69/1.90) matches the q⁴ form.
- `weak-symmetric-normalization`'s `𝒩_sym ≈ 1.90` and the g-action block's
  `𝒩_sym` (target ≈ 213.11) share a symbol but are different objects.

## Lean

`folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/NSymHostStructure.lean`
(module `QOU.QuantumObservableUniverses.NSymHostStructure`). Imports Mathlib
only. Generic `CommRing`/`Field`. `lean -DautoImplicit=false -s 65536` exit 0.
Every declaration's axioms are within `[propext, Classical.choice, Quot.sound]`,
with no `sorryAx`.

| declaration | content |
|---|---|
| `qdim_sum` | weighted trace additive over `⊕` (reading b) |
| `qdim_tensor`, `qdim_three_slots` | multiplicative over `⊗` / three slots (reading a) |
| `qdim_joint_projector` | trace of `E_{abc}` = product of slot weights |
| `orthogonal_summands_compose_zero` | idempotents on different summands compose to 0 |
| `oddPart_Wminus_eq_neg_Wplus`, `Wplus_Wminus_dependent`, `oddPart_ne_zero` | W⁻ odd vector = −W⁺'s; nonzero iff a² ≠ 1 |
| `q2_sq_eq_q3_add_one`, `q4_eq` | `[2]²=[3]+1`; `[4]=[2][3]−[2]` |

## Corpus-grep record

- `corpus_search`: unavailable in this session.
- `folio/`, `docs/`, `computations/`: grepped for `rm sym}`, `N_sym`, `n-sym`, and the Hoefsmit, triplet and torus-link blocks.
- `library/`: `INDEX.md` has no electroweak hit. There are 10+ full-text hits in `sections/`/`ocr/` on standard electroweak physics, none on this categorical composition rule. A citation cannot settle this question because the rule is internal to the corpus.
- `beans/`: not mounted (0 files), so this path was **not searched**.

No derivation of ⊗ versus ⊕ for the G-action itself was found. That is a statement about these searches, not a proof that none exists.
