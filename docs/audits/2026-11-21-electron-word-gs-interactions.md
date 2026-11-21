# Which braid word is the electron? Gröbner–Shirshov interaction measurements

Date 2026-11-21. Owner question (Carl): *"I'm not sure which one it is. What do we see from the
particle interactions as Gröbner–Shirshov bases calculations for the various forms and what
results in the right particles."* This document **measures**. It does not choose, and it changes
no consumer of the electron word.

Conventions used throughout: Hecke relation `σᵢ² = (q − q⁻¹)σᵢ + 1` (eigenvalues `q`, `−q⁻¹`),
`h = q − q⁻¹`; the photon is `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` (owner ruling 2026-11-20);
Markov trace convention D, `z = q³/(q²+1)`. All algebra is exact over `ℚ(q)` (sympy); nothing in
this study is evaluated against a measured value.

## 1. Criteria (fixed before any result was computed)

This section was committed on its own, before the probe was written or run. The criteria are
structural and model-internal. **No numeric comparison with experiment (masses, `Q_β`, CODATA)
is used, and no criterion is used to rank candidates.** The question each criterion answers is
whether it *separates* the candidates at all.

### Candidates

| id | word | why it is here |
|---|---|---|
| X1 | `σ₀σ₁σ₀` (= `σ₁σ₀σ₁` by the braid relation) | the corpus's `e⁻` (`def:breit-wheeler-pair-production`, `photon_operator_table.py`) |
| X2 | `σ₀²σ₁` | a `B₃`-conjugate of X1: same closure, different `H₃` element. Separates "closure type" from "algebra element" |
| X3 | `σ₀³` | the trefoil braid in `B₂ ⊂ B₃` (the owner's 2026-11-20 identification `e⁻ = T(2,3)`) |
| X4 | `σ₁³` | `σ₀³` conjugated by the half twist; the other `B₂` embedding |
| X5 | `σ₀³σ₁` | reference row: Markov stabilisation of `σ₀³`, closing to the trefoil as a **knot** in `B₃` (4 crossings) |
| X6 | `(σ₀σ₁)²` | reference row: `T(3,2) = T(2,3)` as a 3-strand torus braid (4 crossings; the corpus uses this word in the meson files) |

X5 and X6 are outside the three-crossing set. They are included only because criterion C1 below
predicts, before computing, that **no** word of odd length in `B₃` closes to a one-component link,
so no three-crossing candidate can be the trefoil *knot* on three strands. Positron partners are
taken from the corpus's conjugation (C4).

### C1 — closure type (reported, not used to rank)
Number of components of the closure in `B₃` (cycles of the underlying permutation of three
strands), writhe, and the Jones polynomial by Kauffman bracket over `ℤ[A^{±1}]`, `t = A⁻⁴`. The
Jones convention is fixed by calibration: the unknot is `1`, and the corpus's recorded values for
`σ₀²` (`−t^{5/2} − t^{1/2}`) and `σ₀³` (`−t⁴ + t³ + t`) from commit `70340a13f9` are reproduced.

### C2 — pair production `γγ → e⁻e⁺`
Three readings, all fixed now:

- **C2a, the corpus's channel decomposition.** `def:breit-wheeler-pair-production` and
  `prop:gamma-gamma-generates-particles` reduce `γ(φ)·γ(ψ)` to normal form in the standard basis
  `{1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀}`, labelled `{γ, σ₀, σ₁, L₊, L₋, e⁻}`, and define the `e⁻`
  channel as the coefficient on `σ₀σ₁σ₀`. The test: does the candidate's normal form consist of a
  single basis word (so that the corpus's channel reading applies to it), and if so, is that
  word's coefficient in `NF(γ(φ)γ(ψ))` a nonzero polynomial in the weights? The corpus defines no
  `e⁺` channel; whether the positron's normal form is a single basis word is reported.
- **C2b, photon sector.** Let `P = span{1, σ₀, σ₁, σ₀σ₁⁻¹} = span{1, σ₀, σ₁, σ₀σ₁}`, the linear
  span of single-photon terms. Is the candidate in `P`? Is it a scalar multiple of one photon
  `c·γ(φ)` (requires a nonzero `1`-coefficient)? A candidate inside `P` is reachable by a single
  photon and is not specifically a two-photon product.
- **C2c, exact two-photon product.** Do there exist weights `φ, ψ` and a scalar `c ≠ 0` with
  `γ(φ)γ(ψ) = c·X` exactly, as for the Borromean core `V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h)`? Existence is
  decided by a Gröbner basis of the six coefficient equations plus `c·u − 1 = 0`, at fixed
  rational `q` (existence over the algebraic closure ⇔ the basis is not `{1}`); where a solution
  exists, whether one lies in `ℚ(q)` is reported.

### C3 — annihilation `e⁻e⁺ → γγ`
With `e⁺ = C(e⁻)` from C4: the normal forms of `e⁻·e⁺`, `e⁺·e⁻` and of the pair sum `e⁻ + e⁺`,
and whether each lies in the photon sector `P` (C2b).

### C4 — charge conjugation
The corpus's conjugation is `C: σᵢ ↦ σᵢ⁻¹` on words (`c-equals-bar-iff-all-1dim`,
`def:positron-knot`, `prop:antiparticle-crossing-reversal`: "the mirror operation reverses all
crossings"); the corpus positron is `e⁺ = σ₀⁻¹σ₁⁻¹σ₀⁻¹`. Tests: `C(X)` as a word; whether
`C(X) = X⁻¹` in `H₃`; whether `C(X) ≠ X` in `H₃`; for X1, that `C(X1)` is the corpus's `e⁺`.

### C5 — charge
`thm:ew-triplet-charge-spin-from-involution` is stated for electroweak carriers on the sym/alt
block with carrier eigenvalues `a_c`; it is not defined on a lepton braid word, and that is
recorded rather than forced. The lepton-level charge functional the corpus does define is the
crossing energy of `prop:antiparticle-crossing-reversal`, `E(w) = Σ εᵢ`, `ε = q` for `σᵢ` and
`−q⁻¹` for `σᵢ⁻¹`, with the antiparticle rule `E(C w) = −E(w)|_{q ↔ q⁻¹}`. Computed for each
candidate and its conjugate.

### C6 — β-decay at the normal-form level
Before computing: the corpus states no word identity `n → p e⁻ ν̄`. Its β-decay reading
(`nucleon-nf-observability`, `confinement-operator-selection-interpretation`) is the sign of
the `e⁻` (`σ₀σ₁σ₀`) coefficient of a nucleon's normal form at `q₀`. The test is whether that
reading is *defined* for each candidate, which is the C2a question; no nucleon normal form is
recomputed here.

### Context, not a criterion
The convention-D Markov trace `tr_D(X)` over `ℚ(q)` is printed for each candidate.

## 2. Results

*(Filled in after the probe ran; see the commits after the one that introduced §1.)*
