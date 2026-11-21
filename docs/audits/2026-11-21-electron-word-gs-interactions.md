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

## 2. Method

Probe: [`computations/probes/electron_word_gs_interactions_probe.py`](../../computations/probes/electron_word_gs_interactions_probe.py),
run as `python3 -u computations/probes/electron_word_gs_interactions_probe.py 2>&1 | tee /tmp/elw.log`
(≈ 1 min). It builds `H₃(q)` exactly over `ℚ(q)` (sympy) on the standard basis `T_w`, `w ∈ S₃`,
using `T_w T_s = T_{ws}` if `ℓ(ws) > ℓ(w)` and `h T_w + T_{ws}` otherwise. Checks it passes
before any criterion is computed:

- `σ² = hσ + 1`, the braid relation, `σσ⁻¹ = 1`;
- the owner-ruled Borromean factorisation `γ(0,0,qh)·γ(0,0,−q⁻¹h) = (σ₀σ₁⁻¹)³`, exactly;
- **cross-check against the corpus reducer**: `reduce_nf` from `photon_operator_table.py` (loaded
  from its source by `ast`, without executing that producer) on 8 words, all 6 coefficients,
  at the proton `q₀` at 70 dps: agreement to `1e-55`;
- the Jones convention reproduces the values recorded in commit `70340a13f9`:
  `V(σ₀² ∈ B₂) = −t^{5/2} − t^{1/2}`, `V(σ₀³ ∈ B₂) = −t⁴ + t³ + t`.

C2c is decided by a Gröbner basis at fixed rational `q` (not by numerical root finding). The
generic-`q` run over `ℚ(q)` did not finish in the session (see §4).

## 3. Results

The general two-photon product, exact (the `e⁻` row is the corpus's channel):

| basis word | coefficient in `NF(γ(φ)γ(ψ))` |
|---|---|
| `σ₀σ₁σ₀` (`e⁻`) | `φ₀₁ψ₀ + φ₁ψ₀₁` (matches `def:breit-wheeler-pair-production`) |
| `σ₁σ₀` (`L₋`) | `(φ₀₁ψ₀₁ q + φ₁ψ₀ q − φ₁ψ₀₁ q² + φ₁ψ₀₁)/q` |

### 3.1 Table, candidate × criterion

`P` = span of single-photon terms `{1, σ₀, σ₁, σ₀σ₁}`. `C(X)` = mirror `σᵢ ↦ σᵢ⁻¹`.

| | X1 `σ₀σ₁σ₀` | X2 `σ₀²σ₁` | X3 `σ₀³` | X4 `σ₁³` | X5 `σ₀³σ₁` (ref) | X6 `(σ₀σ₁)²` (ref) |
|---|---|---|---|---|---|---|
| **C1** components in `B₃` | 2 | 2 | 2 | 2 | **1** | **1** |
| C1 Jones (`t`) | `−t^{1/2}(t²+1)` Hopf | same, Hopf | `t^{1/2}(t+1)(t³−t²−1)` = trefoil ⊔ unknot | same | `−t⁴+t³+t` trefoil | `−t⁴+t³+t` trefoil |
| NF support | `{σ₀σ₁σ₀}` | `{σ₁, σ₀σ₁}` | `{1, σ₀}` | `{1, σ₁}` | `{σ₁, σ₀σ₁}` | `{σ₁σ₀, σ₀σ₁σ₀}` |
| **C2a** single basis word (corpus channel defined) | **yes**, coeff `φ₀₁ψ₀ + φ₁ψ₀₁` | no | no | no | no | no |
| **C2b** in `P` | **no** | yes | yes | yes | yes | no |
| C2b scalar multiple of one photon | no | no | **yes**: `σ₀³ = h·γ((q⁴−q²+1)/(q(q²−1)), 0, 0)` | **yes**: `h·γ(0, (q⁴−q²+1)/(q(q²−1)), 0)` | no | no |
| **C2c** `γ(φ)γ(ψ) = cX`, `c ≠ 0` solvable | **no** (8 values of `q`, incl. proton `q₀` exactly) | yes | yes (trivially: a photon times `γ(0)`) | yes | yes | no |
| **C3** `X·C(X) = 1` | yes | no (`{1, σ₀, σ₀σ₁σ₀}`) | yes | yes | no | no |
| C3 `X·C(X) ∈ P` | yes (it is `1`) | no | yes | yes | no | yes |
| C3 pair sum `X + C(X) ∈ P` | **no** (all 6 words) | yes | yes | yes | yes | no |
| **C4** `C(X) = X⁻¹` in `H₃` | yes (palindrome) | no | yes | yes | no | no |
| C4 `C(X) ≠ X` | yes | yes | yes | yes | yes | yes |
| C4 `C(X)` a single basis word | no (all 6) | no | no | no | no | no |
| C4 `C(X1)` = corpus `e⁺` `σ₀⁻¹σ₁⁻¹σ₀⁻¹` | yes | — | — | — | — | — |
| **C5** crossing energy `E(X)`, `E(C X)` | `3q`, `−3q⁻¹` | same | same | same | `4q`, `−4q⁻¹` | same |
| C5 rule `E(CX) = −E(X)|_{q↔q⁻¹}` | holds | holds | holds | holds | holds | holds |
| **C6** corpus β-decay reading defined | yes (it is the C2a channel) | no | no | no | no | no |
| `tr_D(X)` (context) | `q³(q⁴+1)/(q²+1)²` | same | `(q⁶+q²−1)/(q(q²+1))` | same | `q²(q⁶+q²−1)/(q²+1)²` | same |

C1 parity, measured over all signed words of length 1, 3, 5 on three strands and proved in Lean
(§5): **every odd-length word in `B₃` closes to exactly two components**. Positive even words close
to one or three. So no three-crossing word in `B₃` closes to a knot on three strands; the trefoil
*knot* needs at least four crossings there (X5, X6).

### 3.2 What each criterion actually tests, and whether it separates X1–X4

- **C1 (components) does not separate** X1–X4: all four close to two components. It separates
  the 3-crossing set from the 4-crossing references, which is the parity theorem. Jones separates
  X1/X2 (Hopf link) from X3/X4 (trefoil ⊔ unknot), as commit `70340a13f9` already recorded.
- **C2a separates, but by construction.** The corpus's `e⁻` channel *is* the coefficient on the
  basis word `σ₀σ₁σ₀`, labelled `e⁻` when the basis was named. Any other candidate fails it because
  it is not that basis word, not because of any interaction. This criterion tests the label, not
  the physics, and **is not evidence for X1**.
- **C2b separates, structurally.** `σ₀σ₁σ₀ = T_{w₀}` is the one standard-basis element outside the
  span of photon terms. `σ₀³` (and every element of `H₂ ⊂ H₃`) lies inside it: `σ₀³` is literally
  `h` times a single photon with weights `(φ₀, φ₁, φ₀₁) = ((h²+1)/h, 0, 0)`. Proved in Lean (§5).
- **C2c separates, structurally.** Two photons can produce exactly a multiple of `σ₀³`, `σ₁³`,
  `σ₀²σ₁` or `σ₀³σ₁`, but not of `σ₀σ₁σ₀` or `(σ₀σ₁)²`: the Gröbner basis is `{1}` at
  `q = 2, 3, 5/2, 7, 111/100, −3, 1/2` and at the proton `q₀` as an exact rational. For X3/X4 this
  is trivial (they are already single photons). It is a measurement at eight specialisations, not
  a proof for generic `q` (§4).
- **C3 separates only through palindromy.** `X·C(X) = 1` holds exactly when the mirror equals the
  inverse, i.e. for palindromic words (X1, X3, X4). Annihilation to the vacuum is then automatic and
  says nothing about which palindrome is the electron. The pair *sum* `X + C(X)` lands in the photon
  sector for X2–X5 and not for X1: that is C2b again, applied to `C(X1)`, which has all six basis
  words.
- **C4 does not separate X1 from X3/X4.** All are chiral at the algebra level (`C(X) ≠ X`); for
  every palindrome `C(X) = X⁻¹`. `C(X1)` is the corpus's `e⁺`. No candidate's positron is a single
  basis word, so the corpus has no `e⁺` channel for any of them.
- **C5 does not separate.** The crossing energy depends only on the signed letter count: `3q` for
  every positive three-letter word. `thm:ew-triplet-charge-spin-from-involution` does not apply to
  lepton words (stated in §1, confirmed: it needs EW carrier eigenvalues `a_c`, not a braid word).
- **C6 does not add information.** The corpus's β-decay reading is the sign of the `e⁻` basis
  coefficient in a nucleon's normal form, i.e. the C2a channel. It is defined for X1 by labelling
  and undefined for every other candidate. The corpus states no word identity `n → p e⁻ ν̄`.

### 3.3 Summary

Of the structural criteria that do not merely restate the basis label, **two separate X1 from
X3/X4, and they point in opposite directions depending on what one wants pair production to mean**:

1. *"The electron must not be a photon."* X1 passes; X3/X4 fail. `σ₀³` is, up to the scalar `h`, a
   single photon in `H₃(q)`, so under X3 the "electron" is indistinguishable in the algebra from a
   coloured photon `γ((h²+1)/h, 0, 0)`.
2. *"`γγ → e⁻ …` must be realisable as a two-photon product."* X3/X4 pass (trivially); X1 fails:
   no pair of photons multiplies to a multiple of `σ₀σ₁σ₀` (at the eight `q` tested). The corpus's
   own Breit–Wheeler reading only needs the `e⁻` *coefficient* to be nonzero, which is C2a.

Neither reading is fixed by the corpus; which is intended is the owner's choice (§6). Nothing here
compares a number with experiment.

Separately, and independent of either reading: **neither 3-crossing candidate closes to the trefoil
knot in `B₃`.** X1 closes to the Hopf link; X3 closes to the trefoil plus a split unknot (it closes
to the trefoil only in `B₂`). The trefoil as a one-component closure on three strands needs four
crossings (X5 `σ₀³σ₁`, X6 `(σ₀σ₁)²`), and X6 fails C2b and C2c exactly as X1 does, while X5 is in `P`
but is not a single photon.

## 4. What is not established

- **C2c for generic `q`.** The Gröbner basis over `ℚ(q)` (variables `φ, ψ, c, u`) did not finish
  within the session. Non-existence at eight specialisations, including the proton `q₀` as an exact
  rational, is strong evidence but not a proof: a generic solution would specialise to all but a
  proper closed set of `q`, so a generic solution that misses all eight values is not excluded by
  this measurement alone. Not formalised.
- **The choice of channel decomposition.** C2a uses the corpus's standard basis. A different basis
  (for example Kazhdan–Lusztig) would give different "channels"; the corpus defines none.
- **Nucleon normal forms** were not recomputed (C6 is about definability, not values).

## 5. Lean

[`QOU/BraidKnot/ElectronWordCandidates.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidKnot/ElectronWordCandidates.lean),
imported in `QOU.lean`. `lean -DautoImplicit=false -s 65536` exit 0 (against the restored Mathlib
oleans, with `QOU/Photon.lean` compiled into a scratch olean dir); `#print axioms` on every
theorem: `propext`, `Quot.sound`, and for the two parity theorems `Classical.choice`. No `sorryAx`.
Orphan gate: `bun run folio/pipeline/lean-orphan-audit.ts --diff <file>` → no new orphans.

- `numCycles_permOf_of_odd`: every odd-length word in `B₃` closes to 2 components;
  `numCycles_permOf_of_even`: even words close to 1 or 3; instances `numCycles_s0s1s0`,
  `numCycles_s0cubed` (both 2) and `numCycles_s0s1_sq` (1). Falsifiable: a wrong generator table or
  orbit count fails `decide`.
- `cube_of_hecke`: `σ₀² = hσ₀ + 1 ⇒ σ₀³ = h·1 + (h²+1)·σ₀` in any `R`-algebra.
- `cube_eq_smul_photon`: with `hu = 1`, `σ₀³ = h · photon σ₀ σ₁ ⟨(h²+1)u, 0, 0⟩` (the corpus photon).

The C2b/C2c facts about `σ₀σ₁σ₀` (outside `P`; not a two-photon product) are not formalised: they
need a basis of `H₃(q)`, and the C2c one is only measured at eight `q`.

## 6. Decision frame for the owner

**The decision:** which braid word the paper calls `e⁻`. It needs the owner because the corpus
fixes the closure type (trefoil, ruling 2026-11-20) and the interaction role (the `e⁻` channel of
`γγ`) separately, and §3 shows no three-crossing word in `B₃` satisfies both.

**Default (no answer):** nothing changes. `e⁻ = σ₀σ₁σ₀` stays the basis label in ~84 files, its
closure stays the Hopf link while the prose says trefoil, and `knot-operator-table.py` keeps the key
`T_{2,2}^{(3)}` that commit `70340a13f9` gave it.

### Option 1 — keep `σ₀σ₁σ₀` and say its closure is the Hopf link
- **Means:** the electron is the longest-element basis word `T_{w₀}`, the one basis element outside
  the photon span; `def:electron-knot`'s "trefoil" becomes "the closure of `σ₀σ₁σ₀`, a Hopf link"
  or the knot claim is dropped.
- **Costs:** prose in `def:electron-knot`, `def:positron-knot`, `def:breit-wheeler-pair-production`
  and the `T_{2,3}` labels (`photon_operator_table.py` key and its witness assertion names,
  `gram-matrix-dual.py`, `lp-duality-check.py`). No number changes.
- **Risks:** contradicts the 2026-11-20 ruling that the electron is the trefoil.
- **Commits to:** an electron identified by algebraic role, not by knot type.

### Option 2 — switch to `σ₀³` (trefoil in `B₂`)
- **Means:** the electron is the trefoil braid in `B₂`, consistent with `c-equals-bar-iff-all-1dim`
  ("`H₂(q)` (leptons)") and with the 2026-11-21 LP ruling, which already uses `σ₀³` for `T_{2,3}`.
- **Costs:** every consumer that treats basis word 6 as the electron would need relabelling; `σ₀³`
  is not a basis word, so the corpus's "`e⁻` channel" of `γγ` and its β-decay "`e⁻` deficit"
  reading lose their definition and need a new one.
- **Risks:** in `H₃`, `σ₀³` is `h` times a photon (§3, Lean), so the electron and a coloured photon
  become the same algebra element up to scale; its closure on three strands is trefoil ⊔ unknot.
  Numbers that would move: the positron target of `knot_operator_lp_selection.py` (recorded optimum
  19.6154195592 for `σ₀⁻¹σ₁⁻¹σ₀⁻¹`; `σ₀⁻³` has a negative identity coefficient and a different
  demand vector); the `e⁻` pair counts pinned in `photon_operator_table.py`; the nucleon "e⁻
  deficit" readings. No L2 dashboard row reads the electron word (`m_e` is CAL-1).
- **Commits to:** a lepton sector in `H₂`, and a new definition of the pair-production channel.

### Option 3 — a four-crossing word that closes to the trefoil knot in `B₃` (`σ₀³σ₁` or `(σ₀σ₁)²`)
- **Means:** keeps "trefoil" literally true on three strands.
- **Costs:** as option 2, plus choosing between two words with the same closure but different `H₃` elements (X5 lies in `P`,
  X6 does not and is, like X1, not a two-photon product).
- **Risks:** choosing between X5 and X6 by which passes a criterion would be selection against the
  target; it needs a structural reason first.
- **Commits to:** four crossings for the electron.

**Recommendation (judgement, not a finding):** option 1 for now. It changes no number, and the
only criterion that favours `σ₀³` (C2c) is passed trivially because `σ₀³` is a photon; deciding the
knot reading can wait until the owner says which of the two meanings of pair production in §3.3 is
intended.

### Blast radius (consumers of the `e⁻` word)

Named in the task and checked: `computations/photon_operator_table.py` (key `T_{2,3}` = `(0,1,0)`,
basis label `e⁻`, pinned `EXPECTED_E_MINUS_PAIRS`) and `computations/photon-operator-table.witness.json`;
`computations/probes/photon_chiral/photon_chiral_ports_probe.py`;
`predicted-spectra/breit-wheeler-pair-production.md` (+ derivation, table);
`appendix-knot-operations/knot-operator-basis-table.md`;
`predicted-spectra/bring-hyperbolic-knot-bloch-decomposition` (`.md`/`.lean`, cites the table);
`computations/lp-duality-check.py` (reads `knot-operator-table.witness.json` key `T_{2,3}`, which
no longer exists after `70340a13f9` and was never committed);
`computations/gamma_gamma_pair_production_decomposition.py` (docstring only; no number uses the
word); `computations/knot_operator_lp_selection.py` (electron and positron targets).

Wider, measured: files with `σ₀σ₁σ₀` / `\sigma_0\sigma_1\sigma_0` / `(0, 1, 0)` on the same line as
`e⁻` / `e^-` / `electron` / `trefoil` / `e_minus`: **84 files** (50 under `folio/`, of which 18 `.lean`;
34 under `computations/`). Command:
`grep -rnE "(σ₀σ₁σ₀|sigma_0\\sigma_1\\sigma_0|\(0, ?1, ?0\)).*(e⁻|e\^-|electron|trefoil|e_minus)|…" computations folio`.
None was edited.

## 7. Adjacent change on the same branch

`computations/knot-operator-table.py`: key `T_{2,5}` → `T_{2,4}^{(3)}` for `(σ₀σ₁)²σ₀`, following
the `T_{2,2}^{(3)}` relabel of `70340a13f9`. Verified in this probe's Kauffman bracket: 2
components, Jones `−t^{3/2}(t⁴ − t³ + t² + 1)` equal to that of `σ₀⁴ ∈ B₂` (the `T(2,4)` link) and
not to that of `σ₀⁵` (cinquefoil, `−t²(t⁵ − t⁴ + t³ − t² − 1)`). No consumer reads that producer's
key (no witness was ever committed). The same mislabelled word survives under `T_{2,5}` "cinquefoil
(muon)" in `photon_operator_table.py:130,227` and its witness, `gram-matrix-dual.py:391`, and
`probes/photon_chiral/photon_chiral_ports_probe.py:75`; not changed.
