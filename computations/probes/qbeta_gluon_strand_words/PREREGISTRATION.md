# Pre-registration: gluon strands that change the nucleon word (issue #8833, front 3)

Written and committed before the Lean file and probe are run. The colour-trace routes are
closed (`qbeta_colour_factor`: F ≤ 1 as a separate factor; `qbeta_colour_gl6`: F = 1 once
order and trace element are derived). What remains is a gluon that changes the **word**.

## Inputs (rulings, none chosen here)

* γγ rule: words are products of V_i = σ_iσ_{i+1}⁻¹ (`GammaGammaWordSelection`). On three
  strands the only vertex is V₀, which is the corpus gluon unit (`gg_gluon_segment`), so on
  three strands a word change is V₀^k only. A gluon that changes the word beyond that needs
  extra strands.
* Nucleon word V₀³ on quark strands 0–2; D1 sectors on the quark strands.
* Normalisation as derived in `qbeta_lepton_normalisation` (premises N1–N3): unobserved strands
  summed, divide by [2]^c (c = closure components), framing q^{−2·writhe} (= 1 for γγ words).
* Confinement: reading 3, whole word (owner 2026-09-12/13): χ_λ(W) ≥ 0 for every block kept
  under convention D. The (C²)^{⊗n} representation carries exactly the two-row blocks, and
  χ_(n−d,d) = tr_d − tr_{d−1} (plain trace on the weight space with d down-spins). Applied as
  a reported filter.

## The closed family

n ∈ {4, 5} strands; strands 3.. are gluon strands. W = X · V₀³, X every product of 1 to L
vertices from {V₀, …, V_{n−2}} (L = 6 for n = 4, L = 5 for n = 5; fixed here because braid
traces are unbounded in word length) that touches a gluon strand and whose strand permutation
maps {0, 1, 2} to itself (quarks stay quarks; gluon strands close among themselves).

## Value

ε_X(W) = Tr(K^{⊗n} (P_X ⊗ 1) ρ(W)) / [2]^{c(W)}, P_X the D1 sector on strands 0–2 (proton:
one down-spin; neutron: two). F(W) = (ε_n − ε_p)(W) / (ε_n − ε_p)(V₀³), compared with
F_required = 2.40397.

## Lean first

`QOU/QBeta/GluonLoopParity.lean`: from `gammaGamma_components_parity`, a γγ word on 5 strands
whose quark strands give 3 components has an odd number of gluon loops, so the two gluon
strands close into one loop.

## Reported

For every word: F, c, the reading-3 verdict. Ranges of F over all words and over reading-3
survivors. No word is selected by closeness to F_required.

## Correction (before the probe ran)

The Lean section above had the parity backwards. n + c even with c = 3 + g gives g even on five
strands, so the two gluon strands close into **two** loops (`five_strands_two_gluon_loops`), and
g odd on four strands, so the one gluon strand is one loop (`four_strands_one_gluon_loop`). Lean
caught it: the false statement did not prove. Family and value are unchanged.
