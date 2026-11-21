# Pre-registration: strand order and Yukawa strengths of the right-handed singlet channels

Bean `qou-99qc`. Written 2026-11-21 before the Lean file or any number. Owner (Carl,
2026-11-21) adopted the right-handed singlet of #8694 (the `−q⁻¹` line `s = q·ud − du` of the
Jimbo crossing on matter ⊗ Higgs) and chose *"derive order + strengths"*. Companion Lean (to be
written): `folio/quantum-observable-universe/lean/QOU/QuarkState/YukawaStrandOrder.lean`.

## Corpus-grep done before this file

Six paths + `bun scripts/corpus-search.ts` (returned no seeds for "Yukawa", "Higgs vacuum",
"right-handed", "lepton partner", "neutrino knot": the knowledge graph is not populated in this
checkout, so that silence is not evidence). Found:

| object | where | bears on |
|---|---|---|
| tensor order quark (left) ⊗ lepton (right) in the β vertex; nucleon on strands 1–3, lepton on 4 | `ChargedCurrentW.lean` (#8638, open) | a convention for quark/lepton, says nothing about the Higgs |
| `P·Ř = R₀ + h·E⊗F`; charge conjugation swaps `E⊗F ↔ F⊗E` | same | candidate relation between the two orders |
| owner-ruled `leftLine` / `rightLine` and `weakVertex − σ = −h·leftLine` | `LeftLineDefinition.lean`, `WeakVertexLeftProjector.lean` | letter-level: defined for any realisation of the letter, so blind to which tensor factor is which |
| `tr e_H = 1`, vev slot weight 0 (hypercharge-shifted Higgs grading) | `HiggsVacuumResidual.lean`, `YukawaVacuumPairing.lean` (#8694) | normalisation of the vev weight |
| `CategoricalHiggsIdempotent` fields `v, g, g′, λ` | content class, no instance | no Yukawa field |
| "the muon's Yukawa coupling" read as `Vol(4₁)` dressing (`m_μ/m_e = Vol(4₁)/ℏ_q²`) | `appendix-standard-model/cal2-higgs-knot-coupling.md` | interpretive, generation ratio only (μ/e), CAL-2 |
| SM blocks: `v` has no derivation; quark masses all open | `sm-params-higgs.md`, `sm-params-quark-masses.md`, beans `qou-z3x8`, `qou-rpt1`, `qou-myxi` | no strength |
| lepton-partner dictionary: quark = unknot strand, generation label = partner crossing count (3/5/7) | #8698 (merged) | first generation: all four fields carry label 3 |
| mass formula `m(K) = m_e·Vol(K)·ρ(K)/ℏ_q²` | AGENTS.md / mass-theory | `Vol = 0` for the unknot and every torus knot (trefoil) |

## Predictions (stated before computing)

**Strand order.**
1. Charge conjugation `C` (`u ↔ d` on both strands) conjugates the corpus crossing to the
   strand-flipped crossing: `C·Ř·C = P·Ř·P`. So the Higgs-left singlet is the `C`-image of the
   matter-left one, and the two orders exchange the vev entries `q²/(q²+1) ↔ 1/(q²+1)`, which is
   also `q ↦ q⁻¹` on the entries.
2. The weak insertion `−h·P_L` annihilates the singlet in BOTH orders, so the left-handed vertex
   does not select an order. The owner-ruled `leftLine`/`rightLine` are letter-level and hold for
   both realisations.
3. The order-free reduction exists but does not use the vacuum: the right pivotal partial trace
   over the Higgs strand, `(id ⊗ tr)((1 ⊗ diag(a,b))·P_R)`, is a scalar on the matter strand iff
   `a = q²·b`, and then equals `b·q²/(q²+1)·1`; with the bare `K = diag(q, q⁻¹)` it is `[2]⁻¹·1`,
   and the mirror statement holds for the Higgs-left order with the left trace and `K⁻¹`. Under
   the owner-ruled `tr e_H = 1` the vev weight is `1` and the reduction is the plain compression,
   which is order-dependent. Expected verdict: **order NOT forced** by the corpus.

**Strengths.** Expected verdict: **NOT derived**. Each candidate rule, with what it gives:
* generation label only (all four first-generation fields carry 3): equal strengths, split `0`;
* channel quantum dimension (every singlet channel has `qdim 1`): equal, split `0`;
* `tr e_H = 1`: one normalisation shared by all channels, type-blind, split `0`;
* type only (`y_u = y_d = y_q`, `y_ν = y_e = y_ℓ`): split `= (y_q² − y_ℓ²)(c̃ − c)`, which is
  `−(y_q² − y_ℓ²)·(q²−1)/(q²+1)` matter-left and the negative Higgs-left: nonzero, order-odd,
  and it needs `y_q, y_ℓ`, which nothing fixes;
* flavour slot only (`y_u = y_ν`, `y_d = y_e`): split `0`;
* partner-knot volume `Vol·ρ`: `0` for unknot and trefoil, no strength;
* `Vol(4₁)/ℏ_q²`: a μ/e generation ratio, does not reach the first-generation four.
Each is a new rule unless a corpus artifact fixes it; none is expected to be found.

**Traces.** The Yukawa energy is a sum of one-strand operators; the one-term trace returns the
strand sum and the covariant all-pairs connected term is `0` for it (`twoTerm_allPairs_formula`),
so the two give the same split. No MeV number will be produced, because no strength is derived.

## Scope

No strength is fitted, chosen or tuned; no order is selected by `Q_β`, `m_n − m_p` or any mass.
If both verdicts come out as predicted, no comparison with CODATA is made. The only numbers
evaluated are the structural factors `q²/(q²+1)`, `1/(q²+1)`, `[2]⁻¹`, `(q²−1)/(q²+1)` at the
proton `q₀` (70 dps); each multiplies an underived strength.
