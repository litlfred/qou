# Pre-registration: why every gluon word multiplies proton and neutron by one factor (issue #8833)

Written and committed before the Lean file and probe are run.

## Observation being explained

Reanalysis of the committed `qbeta-gluon-strand-words` witness (2026-11-21, not
preregistered): in all 79 words, ε_p/ε_n equals that of V₀³ to 1.3e-12 (the reference's
digits), and ε_p/ε_n(V₀³) = q₀² numerically. Owner, 2026-11-21: "Go" (prove it).

## Claimed mechanism (to be tested, not assumed)

1. Jimbo R on two strands commutes with the coproduct of the U_q(sl₂) lowering operator F,
   so every braid word ρ(W) commutes with Δⁿ(F).
2. The K-weighted partial trace over the gluon strands, Y = Tr_g(K^{⊗g} ρ(W)), commutes with
   Δ³(F) on the three quark strands.
3. Δ³(F) maps the one-down quark weight space V₁ bijectively onto the two-down space V₂, and
   Y preserves weight. So Y|V₂ = F·Y|V₁·F⁻¹, hence Tr(Y|V₁) = Tr(Y|V₂) =: t.
4. ε_p = q·t/D and ε_n = q⁻¹·t/D, so ε_p = q²·ε_n for every word, and the flavour cell
   ε_n − ε_p = ε_n(1 − q²) is a common-factor multiple of the ruled cell.

## Lean (QOU/QBeta/QuarkWeightTrace.lean)

* Steps 3 and 4 in general: matrices Y₁, Y₂ and an invertible F with F·Y₁ = Y₂·F have equal
  trace, giving ε_p = q²·ε_n.
* Step 1 on two strands: the Jimbo R matrix commutes with Δ(F), an exact 4×4 identity over a
  field.
* Step 3's bijectivity: the 3×3 matrix of Δ³(F) from V₁ to V₂ has nonzero determinant.

Step 2 (the partial trace keeps the intertwining property) is checked in the probe, not proved
in Lean. That is stated in the report.

## Probe (exact rational arithmetic at q = 2 and q = 3/2)

S1 R commutes with Δ(F) (the coproduct convention used is the one the probe finds; the two
standard candidates are tested and both results reported). S2 every one of the 79 words:
Y commutes with Δ³(F). S3 ε_p = q²·ε_n exactly. S4 the 16 negative-ε words obey the same.
A word that fails S2 or S3 is reported as a counterexample, not dropped.
