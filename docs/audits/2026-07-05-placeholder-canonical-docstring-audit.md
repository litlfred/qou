# Audit — QOU "Placeholder canonical" docstring corpus (2026-07-05)

**Branch:** `claude/do-lean-backlog-t153m9` · **Scope:** every
`content/quantum-observable-universe/lean/QOU/**/*.lean` file that
**originally** carried a `Placeholder canonical` header docstring
(the selection was run on the pre-fix corpus; this same PR then rewrites
48 of those headers to `Canonical declaration`, so the marker no longer
matches those files on-branch).

## Why this audit exists

A grep-based "Lean sorry backlog" count on this repo returns 50–100
files. Almost none of them carry a real `sorry`. The count is dominated
by **stale header/declaration docstrings** that *say* things like
*"The body is `sorry`"*, *"statement and proof are pending"*, *"`… := by sorry`
placeholder"* — while the declaration underneath actually **compiles as
a complete term**. This audit classifies the whole corpus so the
docstrings can be made honest without either (a) blindly relabelling
vacuous self-assuming projections as "proved", or (b) leaving genuine
false-`sorry` prose in place.

Predecessor: PR #3361 corrected the first 3 of these
(`discrete_vortex_spectrum`, `qou_obstruction_reduction`,
`root_of_unity_truncation`) and surfaced the broader ~99-file finding as
a follow-up.

## Method

1. Enumerate files with the `Placeholder canonical` header (99 remain
   after #3361 fixed 3).
2. **Strip comments**, then grep the *code* for `sorry`. Result:
   **0 / 99 files have a `sorry` in code.** Every `sorry` token in the
   corpus lives in a docstring/comment. The "real-stub carrying a cited
   `sorry`" category is **empty**.
3. Classify each file's principal declaration by kind and proof shape
   (`structure`-only · `theorem`/`def` deriving via real tactics ·
   `theorem`/`def` discharging by pure `ctx.field` projection).
4. Separate files whose docstring makes a **false `sorry`/pending-proof
   claim** from those already honest.

## Classification (99 files)

| Bucket | Count | Docstring state | Action |
|--------|-------|-----------------|--------|
| **A. False-`sorry` docstring, compiles** | **48** | *falsely* says "body is `sorry`" / "`:= by sorry`" / "proof pending" | **Fixed this PR** — reworded to honest §3b-conditional prose; token `sorry` removed |
| **B. Empty-`structure` stub** | **29** | accurate ("full Lean statement is pending") | **Leave** — these are the genuine formalisation backlog |
| **C. Already-honest placeholder** | **22** | says "Placeholder canonical" but makes *no* false-`sorry` claim (e.g. "concretisation requires per-block translation") | **Leave** — docstring not misleading |

### Cross-cutting finding — self-assuming projections

Of the 48 fixed (bucket A) and the 22 in bucket C, the **large majority
are §3b self-assuming projections**: the context `class` carries the
manuscript claim itself as a field (e.g.
`claim_boxed_six_term_expansion : mass = descended - brane_tower + …`),
and the `theorem`/`def` discharges the goal by projecting that field.
Per AGENTS.md §3b-cond *non-degeneracy* rule these type-check but do
**not** derive their conclusion from deeper primitives. The reworded
prose says so explicitly ("the substantive mathematical content is
carried by the context-class axioms, and a full derivation from
substrate primitives remains pending") — it is **not** a claim of
"proved".

A minority genuinely derive content beyond projection (arithmetic /
`ring` / `linarith` / `rfl` on concrete values), e.g.
`exterior_square_borromean` (checks `45 = 9 + 36`), the two `collatz_*`
files, the three `Observations/*` variance/window bounds. The uniform
reworded prose is accurate for these too (they still discharge *from the
class's fields*; the extra arithmetic does not change the conditional
status).

**Detector-coverage finding (measured 2026-07-05).** Running
`content/pipeline/lean-vacuity-axiom-audit.ts` over the whole QOU tree
flags **0 of the 99** corpus files under *any* vacuity criterion — including
its `proof-no-self-assuming-projection` detector. The reason is a
**coverage gap**: that detector matches only a *single conclusion-typed
field returned verbatim* (`… := ctx.field`), whereas every file in this
corpus discharges via a **tuple or applied** projection
(`… := ⟨ctx.a, ctx.b, …⟩`, `… := ⟨ctx.impl_x ctx.active, …⟩`) or a
`refine ⟨…⟩; rw […]` block. So these self-assuming projections are **not**
currently machine-detected.

**Follow-up (not done here), corrected:** the recommendation is therefore
*not* "run the existing `--review-ledger` job" — that job returns 0 on
this corpus. The productive follow-ups are either (a) **extend
`proof-no-self-assuming-projection`** to recognise tuple/applied
projections whose components are all `ctx.<field>` (a change to a
CI-gating checker — its own focused PR, since it will surface new
CRITICAL flags across the corpus), or (b) hand-track buckets A+C. Seeding
~70 ledger entries by hand in one pass is out of scope here.

## Bucket A — fixed this PR (48)

Comment-only reword; cannot affect compilation. See the commit
`docs(lean): correct 48 stale "body is sorry" placeholder docstrings`.

## Bucket B — empty-`structure` stubs, genuine backlog (29)

These declare `structure Foo where` with **no fields**, no proposition,
no proof. Their docstrings ("full Lean statement is pending") are
**accurate**. They are the real Lean formalisation backlog for these
content blocks.

```
AlgebraicSubstrate/HqBiFiltration/BiFiltration.lean
AlgebraicSubstrate/QChebyshevFunction.lean
AlgebraicSubstrate/QVonMangoldtFunction.lean
AppendixSurreals/BlowupCalculus.lean
Archimedean/BreitWheelerPairProduction.lean
Archimedean/QMomentum.lean
Archimedean/QValueTransition.lean
Archimedean/QuarkAntiquarkProduction.lean
Archimedean/TransferMatrixOperator.lean
Archimedean/TypedGarsideElement.lean
BraidKnot/CompoundBetaShellCalibration.lean
BraidKnot/FrobeniusSelfDualityForcesLPDualExtraction.lean
BraidKnot/InterfaceComposition.lean
BraidKnot/IsotopeKnot.lean
BraidKnot/MagicShellCouplingKappa.lean
BraidKnot/ShellSchurWeylSelfDuality.lean
BraidKnot/SpinInvolutionLPDualInvariance.lean
BraidTwistFlip.lean
CMBFunctor.lean
CategoricalMassMarkov.lean
ColorTubeFibers.lean
ComputationalHorizon.lean
HorizonFunctor.lean
Intent.lean
Molecular/ElectronShellCapacity.lean
ObservableSubcategory.lean
QuaternionicSpectralResolvents.lean
SkeinResolutionObstruction.lean
Su2Generators.lean
```

## Bucket C — already-honest placeholders (22)

"Placeholder canonical" header but no false-`sorry` claim; the prose
already flags that concretisation / full derivation is pending. Left
untouched. (Vacuity-ledger candidates per the cross-cutting finding.)

```
Archimedean/em_coupling_projection.lean
Archimedean/parity_violation_skein.lean
Archimedean/reidemeister_action_table.lean
Archimedean/skein_polynomial_transfer_matrix.lean
Archimedean/skew_poisson_integration.lean
BraidKnot/IsotopeKnot/equivalence.lean
BraidKnot/JucysMurphyCentralElementsQOU.lean
BraidKnot/UnstableAtom/decay_channel.lean
BraidKnot/geom_yekutieli_alignment.lean
BraidKnot/hoefsmit_scattering_pipeline.lean
BraidKnot/joint_tower_sdp_confinement.lean
BraidKnot/knot_mass_unified.lean
BraidKnot/mass_formula_regime_switching.lean
BraidKnot/wedderburnWeightCanonical.lean
BraidKnot/wigner2_coefficient.lean
Interactions/inductiveGBReduction.lean
QuantumObservableUniverse/exists_axiom_1_frobenius.lean
QuantumObservableUniverse/exists_axiom_3_chern.lean
WedderburnMass/chirality_residue_mass_term.lean
orbital_fourier_decomposition.lean
qou_canonical_action.lean
variational_equations.lean
```

## Recommendations

1. **The honest Lean formalisation backlog is bucket B (29 empty
   structures)** — not the ~99 grep count. Prioritise these for real
   formalisation.
2. **Buckets A + C (~70) are §3b self-assuming projections** that
   type-check but await derivation from substrate primitives. Seed them
   into the vacuity review ledger and drain via genuine derivation (or
   honest demotion to `conjecture`) over time.
3. **Do not trust a bare `grep sorry` count** as a backlog metric on
   this corpus; strip comments first.
