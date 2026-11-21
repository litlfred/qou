# Pre-registration: is there a right-handed singlet `e_R` in the corpus? (route Y, step 2)

Bean `qou-99qc`. Written 2026-11-21 before the Lean file was written or any number evaluated.
Owner (Carl, 2026-11-21): *"1 Find e_R in corpus"*. Companion Lean (to be written):
`folio/quantum-observable-universe/lean/QOU/QuarkState/RightHandedSingletChannel.lean`.

## Why

Route Y (`YukawaVacuumPairing.lean`, this PR) showed that a two-point pairing of the Higgs vacuum
with a doublet strand gives split 0 (type-blind) or gives energy only to the neutral slot `ν`
(charge selection). In the Standard Model the electron mass comes from the THREE-point vertex
`L̄ Φ e_R` with a weak singlet `e_R` (`T³ = 0`, `Y = −2`). The question is whether the corpus
already holds an object with that role.

## Corpus-grep (six paths + `bun scripts/corpus-search.ts`), done before this file

Terms: right-handed, singlet, `e_R`, chirality, mirror crossing, `σ⁻¹` orientation, bar image of
the doublet, the photon chiral term `σ₀σ₁⁻¹`, `P_L`/`P_R`, trivial `T³` rep, Weyl/Dirac,
CPT / Type-B folding, q-antisymmetric / quantum determinant. Candidates found:

| # | candidate | where |
|---|---|---|
| C1 | the right line (`−q⁻¹` eigenline) of the Jimbo crossing `Ř` on two doublet strands, i.e. the `q`-antisymmetric pair | `rightLine` (`LeftLineDefinition.lean`, owner-ruled `leftLine`); `Ř` in `ChargedCurrentW.lean` (#8638), `YukawaVacuumPairing.compress_*` |
| C2 | the weak-vertex right projector `P_R`, where the insertion `−h·P_L` vanishes | `WeakVertexLeftProjector.insertion_mul_rightLine`; #8638 |
| C3 | the right line of `σ₁` inside the `(3,1)` of `H₄`, called "a singlet" | `FlavourDoubletFourStrands.lean` |
| C4 | the mirror / bar image of the doublet (`σ ↦ σ⁻¹`, `q ↦ q⁻¹`) | `leftLine_mirror`, `WeakChiralityRootLabel.lean` |
| C5 | the photon's chiral term `σ₀σ₁⁻¹` | `def:photon`, `PhotonPairNormalForm.lean` |
| C6 | the sign block `(1³)`, killed by convention D | `RightLineTraceObstruction.lean`, `ocneanuWeight_conventionD_eq_zero_of_three_rows` |
| C7 | `u_R`, `d_R`, `e_R` as LABELS of states | `ChiralityGradingConstruction.lean` (`Gen1Quark`), bean `qou-fbrp`, `HyperchargeBatteryReduction.lean` (battery B2) |
| C8 | literature: Furey's minimal right ideal (`ν_R`, `e_R` singlets from an idempotent) | `library/arxiv-1611.09182v1` §7.3 (held) |

C2 is C1 on two strands (the weak insertion on a crossing is `−h` times the triplet projector).

## Test (what "qualifies" means)

A candidate qualifies as the `e_R` role iff, with the Standard-Model electric charges used as
input labels (as in #8676 and route Y):
1. it carries `T³ = 0` under the quantum-group weight `K = q^{2T³}` (the `T³` of `OverStrandWeight`);
2. its electric charge makes `L̄ Φ e_R` invariant under the unbroken grading, i.e. it has
   `Q = −1` and `Y = −2` (and the analogues: `d_R` `Q = −1/3`, `u_R` `Q = +2/3`);
3. it is distinct from the left component `e_L` (`T³ = −½`).

## Predictions (stated before computing)

* **C1 qualifies on 1–3.** The `−q⁻¹` eigenline of `Ř` on `V ⊗ V` is one-dimensional, spanned
  by `s = q·ud − du` (`q² + 1 ≠ 0`). Under strand gradings `diag(x₁r, x₁r⁻¹) ⊗ diag(x₂r, x₂r⁻¹)` it
  has eigenvalue `x₁x₂`: `T³ = 0`, charge = sum of the two hypercharge centres. Its quantum
  dimension `Tr((K⊗K)P_R)` is `1`; the left (triplet) line has `[3]`. The weak insertion
  annihilates it.
* **Charge of the singlet of (matter strand) ⊗ (Higgs strand).** `= Q(matter up) + Q(Higgs down)`.
  With `Φ = (φ⁺, φ⁰)`: `ν_R` (lepton) and `u_R` (quark). With `Φ̃ = (φ⁰*, φ⁻)`: `e_R`
  (lepton) and `d_R` (quark). Expected: the four right-handed hypercharges of battery B2,
  `{+4/3, −2/3, −2, 0}`. NOTE in advance: `hypercharge_determined_of_isospin_zero` says `Y` on a
  `T³ = 0` object is fixed by `Q`, so matching B2 adds no information beyond matching `Q`.
* **Forced vs free.** A functional on `V ⊗ V` supported on the right line is forced up to ONE
  scalar (the Yukawa strength `y`). Which Higgs slot carries the vev (`Φ` or `Φ̃`) is forced by the
  target charge. The ORDER of the two strands (matter left or Higgs left) is not fixed by
  anything found: a selection, enumerated.
* **Induced energy.** Compressing the idempotent `P_R` by the vev gives the matter slot it picks
  the diagonal entry `q²/(q²+1)` or `1/(q²+1)` (they sum to 1; both `→ ½` as `q → 1`), which one
  depending on the order and the Higgs slot.
* **Split** (`#8676` four-strand form):
  `split = y_d² c_Φ̃ + y_ν² c_Φ − y_u² c_Φ − y_e² c_Φ̃`. Four free strengths. Equal strengths give
  `0`. No number is forced; no MeV value will be produced.
* **Traces.** The Yukawa energy is a sum of one-strand operators, so on a fixed flavour-content
  sector the one-term quantum trace `Tr(K^{⊗4}·)/Tr(K^{⊗4})` returns the strand sum, and the
  scored two-term covariant all-pairs form adds no pair term from it: both give the same
  split. The non-covariant adjacent insertion is reported as a labelled comparison only.
* **C3–C8 fail the test** (expected): C3 lives on the Hecke side, which commutes with the
  quantum-group action and carries no `T³`; C4 maps a doublet to a doublet; C5 is an operator,
  not a state, and is a Hecke element (no `T³`); C6 is `Λ³V = 0` for `sl₂`; C7 are labels with no
  object; C8 is literature that supports the idempotent mechanism but is not a corpus object.

## Scope (what a PASS would and would not mean)

* PASS means: the corpus object C1 has the quantum numbers of `e_R` and supplies the shape of the
  three-point vertex. Reading it AS the electron's right-handed component makes `e_R` a
  two-strand (lepton ⊗ Higgs) channel. That reading is an identification, scope (a), and is put
  to the owner, not adopted.
* No Yukawa strength is fitted, chosen or tuned. No selection between the two orders by how a
  number lands. CODATA `Q_β` is quoted for comparison only.

## Post-registration note (2026-11-21, added after the run; nothing above was changed)

The owner adopted the reading (option 1 of PR #8694) on 2026-11-21: the right line of the
matter ⊗ Higgs crossing is read as the right-handed field, so `e_R` is a two-strand
(lepton ⊗ Higgs) channel. The strand order and the four Yukawa strengths stay open. The probe and
witness above still say "owner call" because they record the state at run time; they were not
re-run for this note.
