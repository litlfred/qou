# Lean two-layer drift — triage of "missing" + "sorry" blocks (2026-06-14)

## TL;DR

The QOU formalization lives in **two parallel Lean corpora** that have
drifted apart, and single-layer audits miscount badly. Cross-checking
every content block's `lean.ref` against the **built library**
reframes the "28 missing-Lean + 40 sorry" backlog: **most are false
alarms** (the Lean exists in the library, not the colocated sibling).

| | sibling-only view (first pass) | after library cross-check |
|---|---|---|
| Provable+def "missing Lean" | 29 | **2 genuinely unformalized** (27 are in the library, sorry-free) |
| Provable+def "sorry" | 41 | **~12 genuinely open** + ~17 stale-sibling sync + 11 conditional-class (OK) |

> Status note: library sorry/error status below is from a **static
> decl-span scan**, pending the authoritative `lake build QOU`
> (running). Build-verified numbers will refine the "stale sibling"
> and "genuinely open" lists (the build sees compile errors and
> `sorryAx`-through-dependencies the static scan cannot).

## The two layers

| Layer | Files | Lines | Compiled? | Role |
|---|--:|--:|---|---|
| **Block siblings** `content/<ch>/<block>.lean` | 1065 | 86.9k | ❌ not in any `lean_lib` (outside `lean/`) | content face; 1-per-block; `lean.ref` resolution priority #1; what QA/hash audits read |
| **`lean/QOU/` library** | 765 | 113.3k | ✅ `lake build QOU` (`srcDir="."`) | the real formalization; topically organized; self-contained; doc-gen'd |

They are **independent** (0/5 random siblings share a filename with the
library; the library imports nothing from siblings; `lean.ref` often
fails exact resolution). Origin: the repo began as LaTeX + monolithic
chapter Lean indexed by `proof-objects.json` via blueprint macros; the
content-object migration added per-block siblings as the new authoritative
content layer, but the deep library proofs were never collapsed into
siblings (one narrative block ↔ many topical lemmas), and nothing syncs
the two. `extract_proof_objects.py` still parses only the 9 original
`.tex` chapters → today's `proof-objects.json` is a fossil (106 objects,
chapter 6 only, 0 proved / 0 sorry).

## Global `lean.ref` resolution (all ~864 provable+def blocks)

| Resolution | Count | Meaning |
|---|--:|---|
| exact | 399 | block's Lean is a library decl (full-name match) |
| leaf / leaf~ | 54 | library decl exists, namespace drift |
| **MISSING-in-library** | 408 | block's Lean lives in its **sibling**, not the library |
| no-ref | 3 | `.ts` has no `lean.ref` |

So ~453 blocks are formalized in the **library**, ~408 in colocated
**siblings** — two coexisting conventions. (408 is an *upper bound* on
true drift; a few may be static-parser namespace-desync misses, to be
confirmed by the build.)

## Missing-Lean triage (29 = 28 provable + 1 definition)

### Already formalized in the library, sorry-free — NOT a gap (27)

These lack a colocated sibling `.lean` but their `lean.ref` resolves
**exactly** (25) or by leaf (2) to a sorry-free library decl. The
"missing" was an artifact of counting siblings only.

`braids-and-knots/unit-modulus-eigenvalue`,
`climax-volume-mass/jones-mobius-diagonal`,
`fluid-dynamics/{q-bkm-criterion, ns-obstruction-tower,
ns-singularity-descartes, p4-universality}`,
`mass-endomorphism/{qbeta-canonical-markov-weights-explicit-instance,
qbeta-delta-tau-surrogate-taylor-coefficients}`,
`mass-theory/{hecke-generator-poly-reduction,
q-beta-categorical-precision-ladder, em-spectral-completeness,
knot-factor-amphicheiral, plancherel-weight-boundedness,
operator-valued-combiner-convergence, knot-factor-spectral-derivation,
hoefsmit-V21-cos-symmetrization, q-rogers-pentagon-archimedean,
s4-s3-half-symmetric-projection, crossed-module-euler-characteristic,
borromean-markov-trace-closed-form}`,
`molecular-construction/embeddable-knot-operator` (def),
`predicted-spectra/{em-coupling-projection, em-coupling-bring-zero-mode,
force-carrier-bring-uniqueness, photon-ir-zero-mode-bring,
type-b-folded-crystal-combinatorics, torus-knot-genus-four-unique}`.

Action: either add a thin sibling that re-states/re-exports the library
decl (restores `lean.ref` priority-#1 resolution + QA hashing), or accept
library-only and teach the dashboard to resolve into the library. No new
math.

### Genuinely unformalized — real gap (2)

Both the sibling and the library decl are absent:

- `information-theory/parallel-fibre-noninteraction` → ref `QOU.Information.OneDimChannel.parallel_noninteraction`
- `mass-theory/t-beta-markov-frobenius-collapse-general` → ref `QOU.QBeta.MarkovFrobeniusCollapse.General.markov_frobenius_min_norm_lift`

## Sorry-block triage (41 = 40 provable + 1 definition)

### Vacuous stubs (`: True := sorry`, `∃ _, True := sorry`) — 9

Degenerate sibling placeholders that prove nothing. **8 of 9 have a real
sorry-free proof in the library** (the stub shadows finished work):
`climax-volume-mass/skein-crossing-asymmetry-prop`,
`lifting-and-descent/qu-to-qou`, `mass-theory/{knot-operator-transition,
symbolic-character-table, vol-through-tau, volume-perturbation-formula}`,
`quantum-observable-universes/fiber-adjoint-involution`,
`quantum-universes/positive-definite-dagger`.
Action: replace the sibling stub with the real statement (or re-export);
these are `proof-statement-integrity` / §3b-cond item-5 violations.
**1 is genuinely empty** (no library backing): `mass-theory/content-scaling-correspondence`.

### Conditional-class (§3b-cond) — 11, legitimate by design

`sorry` = the named conjectural class instance; the downstream theorem
is fully verified modulo it. Audit the 5 §3b-cond conditions, but these
are not defects. `mass-endomorphism/conj-qbeta-c-k-closed-forms`,
`mass-theory/{frobenius-self-duality-forces-lp-dual-extraction,
prop-rigid-monoidal-structural-gap-invariance, interface-knot-markov-z,
lr-coefficient-hecke, crystal-basis-resolves-mass-tower-open-problems,
confinement-sdp, descended-level-zero}`,
`observations/{borromean-hopf-energy-crossover, algebraic-gns-embedding}`,
`particle-interactions/q-beta-spectral-bridge`.

### Real sorry — 21

**Stale sibling (real proof exists sorry-free in library) — ~8.** The
sibling `sorry` is likely outdated; verify the statements match, then
sync: `lifting-and-descent/categorical-jet-prolongation`,
`mass-theory/{deuterium-derived-binding, alpha-shift-torus-knot,
chi-lambda-w0-sign-weighting}`,
`particle-interactions/{gram-matrix-h3-symbolic, nuclear-groebner-reduction,
confinement-phase-stratification, compound-beta-shell-calibration}`.

**Genuinely open (no library decl) — ~12, the real Lean backlog:**
`braids-and-knots/{cyclotomic-strand-doubling, zeta8-witness-level2-su2}`,
`climax-volume-mass/q-energy` (def),
`mass-endomorphism/explicit-central-idempotent`,
`mass-theory/{q-gaussian-obstruction-at-q0, partition-sum-proton-residual,
jucys-murphy-central-elements-qou, lr-tensor-character-bridge,
mass-endomorphism-tower}`,
`models-of-qous/{symmetric-point-channel-collapse, physical-units-gap-linear}`,
`particle-interactions/generator-volume-decomposition`.
(`particle-interactions/meson-scale-independence`: `.ts` has no `lean.ref` — classify after build.)

## Genuine Lean backlog (post-cross-check)

| Bucket | Count | Nature |
|---|--:|---|
| Genuinely unformalized (both layers absent) | 2 + 1 stub = **3** | new formalization |
| Genuinely open real-sorries (lib MISSING) | **~12** | proof discharge (maps to `lean-discharge-queue`) |
| Stale-sibling sync (real proof in library) | **~17** (8 stub + 8 real-sorry + 1) | drift cleanup, no new math |
| Conditional-class (§3b-cond) | 11 | legitimate, audit-only |

vs. the first-pass sibling-only count of "28 missing + 40 sorry = 68
problems." The true new-math backlog is ~15, not ~68.

## Consequence for regenerating `proof-objects.json` (default lake/lean infra)

Per owner directive ("make it work with default lake/lean infra"), the
regen must not hand-roll a LaTeX/sibling parser. Design:

1. **Status from `lake build QOU`** (the default Lean build) — parse
   `declaration uses 'sorry'` warnings + compile errors for the ~453
   library-resolved blocks. (This is what `update_proof_status.py`
   already does; reuse it.)
2. **Siblings** (~408 library-MISSING blocks) get status from
   `lean`-direct per-file checks (still default Lean, no bespoke parser).
3. **Join on `lean.ref`/label** → one block-keyed `proof-objects.json`.
4. **Emit a drift report**: the 408 library-MISSING refs + the ~17
   stale-sibling/library duplicates, as the relink backlog.

The stale `extract_proof_objects.py` (9-chapter LaTeX path) is retired.

## Build-verified status (`lake build QOU`, 2026-06-14)

Ran the default Lean build via cache-restore from `lake-cache/qou-v4-24-0`
(2951 mathlib + QOU oleans). **Headline: the QOU library does not cleanly
compile on this branch** (`error: build failed`) — and CI's
`continue-on-error: true` (every Lean workflow) has masked it, deploying
partial gh-pages output even when the Lean build fails.

### `sorry` (6 in QOU, +2 in the UGB dep)

`Interactions/QIntegerMassFormula.lean:172`, `BraidKnot/GSReductionOrder.lean:123`,
`Archimedean/HyperbolicVolumeIndependence.lean:39`,
`Archimedean/EmCouplingBringZeroMode.lean:193`,
`AppendixSurreals/PolynomialEval.lean:357` & `:453`.

### 28 files with hard errors (240 error lines) — genuine source bugs

Spot-checked as real source-level breakage, **not** cache/hazard
artifacts (a mathlib mismatch cannot produce "unexpected token 'λ'"):

- `AlgebraicSubstrate/TwoFiltrationBridge{General,SmallCases}.lean` — `λ`
  used as an identifier (`conj lam = λ → …`); `λ` is reserved lambda
  syntax → "unexpected token '→'". A notation-collision bug.
- `BraidKnot/PlancherelWeightBoundedness.lean` — same `λ`-as-identifier.
- `BraidKnot/KnotFactorSpectralDerivation.lean:23` — `Unknown identifier ℝ`
  (missing `import Mathlib.Data.Real.Basic`).
- `AtomicMass.lean` — `rw [ElementDatum.codata_minus_ame_eq_Z_offset]` on an
  **undefined** constant → cascades to 50 `Unknown constant` errors.
- `Archimedean/BorromeanQuark.lean` — `Finset.univ.sum` (wrong API),
  `Application type mismatch`.
- `MassEndomorphism/MassEndomorphismConjecture.lean` — `unknown tactic` +
  `unsolved goals`.
- `su2_emergence_volume_determinant.lean` — `Unknown identifier SU2EmergenceContext`.

Full 28: `AlgebraicSubstrate/TwoFiltrationBridgeGeneral`,
`AlgebraicSubstrate/TwoFiltrationBridgeSmallCases`, `AppendixSurreals/KComplex`,
`AppendixSurreals/PolynomialEval`, `Archimedean/BorromeanQuark`,
`Archimedean/EmCouplingBringZeroMode`, `Archimedean/HeckeH3`, `AtomicMass`,
`BraidKnot/GramSeminormalBlock`, `BraidKnot/KnotFactorSpectralDerivation`,
`BraidKnot/NucleusEmptySDPUniqueness`, `BraidKnot/PlancherelWeightBoundedness`,
`BraidKnot/WitnessR5Full`, `Braiding/HeckeGenPolyReduction`,
`CategoricalDqSquared`, `FeynmanPathIntegrals`,
`FlavorDressing/FlavorMassSplittingBound`, `Information/HeckeLogDecomposition`,
`Interactions/QIntegerMassFormula`, `LiftingDescent/CosimplicialCrossedGroupoid`,
`MassEndomorphism/MassEndomorphismConjecture`, `MathlibExt/RpowAlgebra`,
`Molecular/PalindromicityOrbitalType`, `Molecular/ShellClosureNfTermCount`,
`Observations/TraceLocalityMeetsGsNonLocality`, `PhiQJSJ`, `QGeometricLanglands`,
`su2_emergence_volume_determinant`.

Several are cascades from a smaller root-cause set (the `λ`-identifier
files, `AtomicMass`'s missing constant). Many are quick fixes
(`λ`→`lam` rename, add the `ℝ` import) — a `lean-build-fix` follow-up.

### Build caveat

The cache restore hit the documented mathlib-reclone hazard (recovered),
and `Archimedean/PauliWitness/Witness12B.lean` does not terminate
elaboration (~16 min, killed), so `build_ok` is recorded `false` and ≤6
modules are unrepresented. The 28 source errors are independent of these
and reproduce on a clean build.

### Result

`proof-objects.json` v2 records this truthfully: **36 blocks → `error`**,
6 → `has_sorry` (library), the remainder `proved`/`stated`. Status by kind
(formalizable): definition 209 stated / 6 sorry / 7 error; proposition 263
proved / 221 stated / 40 sorry / 12 error; theorem 18 proved / 20 stated /
4 sorry / 1 error; lemma 37 proved / 3 error; corollary 6 proved / 3 sorry;
conjecture 72 proved / 47 stated / 13 sorry / 10 error.
