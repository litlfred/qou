# The self-assuming-projection remainder is vacuous, not open — and the lit is already held

**Date:** 2026-08-30 · **Bean:** `qou-z9ws` (arc parent `qou-rq9n`, ledger `qou-s3zd`)
· **Evidence:** [`2026-08-30-context-classes-are-inhabited-by-zero.lean`](2026-08-30-context-classes-are-inhabited-by-zero.lean)
(lean-direct exit 0) · **Tool:** [`scripts/lean-context-class-inhabitation-probe.py`](../../scripts/lean-context-class-inhabitation-probe.py)

---

## The claim under test

The self-assuming-projection drain ended at **90 genuine** ledger findings. The
sizing audit
[`2026-08-30-sizing-the-self-assuming-projection-drain.md`](2026-08-30-sizing-the-self-assuming-projection-drain.md)
recorded the remainder as week-shaped, on this reasoning:

> *"Constructing a witness means supplying the mathematics the context class
> was standing in for. For many of these — `KnotOperatorSelectionContext`,
> `HoefsmitScatteringPipelineContext`, `NucleonOrderingFactorizationContext` —
> that **is** the open research, not a formalisation chore."*

**That was asserted, never measured.** It is the load-bearing sentence of the
whole remainder assessment — it is what makes the job a week rather than a
session, and it is what makes "do the research" the natural next step. So it is
worth measuring before spending the week.

## Result: 26 of the 79 classes are inhabited by `Unit` and zero — including all three the sizing audit named

The 90 findings sit on **80 distinct context classes** (79 named, plus 4
declarations with no instance binder at all). Probing each one by generating the
most trivial model available and asking `lean` whether it type-checks:

| | |
|---|---|
| classes probed | 79 |
| **INHABITED with no hypotheses (machine-proved)** | **26** |
| unproven — INCONCLUSIVE, see method below | 26 |
| skipped — generator could not build a model at all | 27 |
| hand-verified before any tooling existed | 5 of 5 |

**All three classes the sizing audit named** — `KnotOperatorSelectionContext`,
`HoefsmitScatteringPipelineContext`, `NucleonOrderingFactorizationContext` — are
inhabited by `Unit` and zero. So is `MassVolumeFactorization`, which cites
Thurston and Murakami–Murakami; so is `HasArgumentPrinciple`, whose all-zero
model takes the pole set to be empty.

The 26:

`AlgebraicQuantumVolumeSpecializationContext`, `BetaStabilityContext`,
`BindingAssemblyContext`, `CatEigenspaceDecompositionContext`,
`CoreLeviContext`, `CrystalBasisCorrespondence`, `HasArgumentPrinciple`,
`HeckeBaerStarGenericContext`, `HelicityContext`,
`HoefsmitScatteringPipelineContext`, `JetPrefixGbFiltrationContext`,
`JointTowerSdpConfinementContext`, `KnotFactorSpectralContext`,
`KnotMassUnifiedContext`, `KnotOperatorSelectionContext`,
`MassFormulaRegimeSwitchingContext`, `MassVolumeFactorization`,
`NucleonOrderingFactorizationContext`, `PairSkeinMassContext`,
`RMatrixBraidingContext`, `ReidemeisterMassInvarianceContext`,
`SharedDenominatorCuspHolonomy`, `SixTermMassFormulaContext`,
`WedderburnWeightCanonicalContext`, `Wigner2CoefficientContext`, and
`CPTClosure` (added by the sibling-import fix; see the refutation below).

A class inhabited that cheaply constrains nothing. A `[C]` binder on it assumes
nothing, and the downstream `[C]`-conditional declaration is therefore not
conditional on anything. **Constructing a witness for such a class is not
progress — it is the defect**, and it is the same one the q-NS carriers in
`ConditionalClasses.lean` carried until 2026-08-30, where every field was an
existential over data the instance itself chose.

## 🛑 Inhabited does NOT mean the block is bad — state this narrowly

A class may legitimately *name* a modelled object together with its defining
law, with the real work downstream. `BorromeanQuark`
(`brings-surface/orbital-fourier-decomposition.lean`) is the worked
counter-example: it carries `orbitalDim n = Σ_{ℓ<n} modeSpaceDim ℓ` as its
single modelling input, and the file then **derives** `orbital_dim_eq_square :
Σ_{ℓ<n} modeSpaceDim ℓ = n²` unconditionally. That class is inhabitable — by the
corpus's own theorem — and that is §3b-cond working exactly as intended.

The discriminator is what the downstream declaration *does* with the field:

- **derives something from it** → §3b-cond working (`BorromeanQuark`);
- **projects it verbatim** → §3b-cond item 5, and if the class is *also*
  inhabited by zero, the declaration is conditional on nothing and states
  nothing.

All 90 findings are of the second kind by construction — that is what the
criterion detects. So the inhabitation result is decisive **for them**, and must
not be generalised into "context classes are bad".

## A second, different finding: `Term7ShellCorrectionClass` is provable

Not vacuous — **provable**. Its field is `∃ a, a < 0 ∧ a = alpha5_value`, and
`alpha5_value : ℝ := -1` is a literal, so the class asserts `-1 < 0` and
`norm_num` closes it (verified, in the evidence file).

Carrying a proved fact as a class hypothesis is harmless in itself. What makes
it a finding is the source's own comment on that literal:

```lean
noncomputable def alpha5_value : ℝ := -1  -- sign-constraint witness; magnitude awaits derivation
```

So the genuinely open part — the **magnitude** of `α₅` — is encoded nowhere,
while the part that *is* encoded is a theorem. That is the
`proof-claims-unencoded` shape, not the self-assuming-projection one, and it
wants a different disposition.

## Do we need any literature? No — and here is the measurement

The question is worth answering precisely, because "the research is open" and
"we lack the sources" are different claims and only one of them was ever
checked.

**First: for most of these classes the blocker is not mathematics at all.** No
paper fixes a class that asserts nothing; the fix is re-encoding it so its
claims constrain a *parameter* rather than data the instance picks. That is the
q-NS remedy, and it needed no literature either.

**Second: for the classes that are genuinely contentful, the library already
holds the sources.** Measured over `library/*/sections/` and `library/*/ocr/`
(corpus-grep path 5 plus the fourth OCR tier), counting distinct documents:

| topic | needed by | documents held |
|---|---|---|
| Kerov–Vershik asymptotics | `ConvergenceBound` | **32** |
| Littlewood–Richardson | `DoubleMagicConjecture` | **27** |
| elliptic functions | `HasArgumentPrinciple` | **15** |
| volume conjecture / Kashaev | `WhiteheadVolumeConjectureLimit`, `MassVolumeFactorization` | **14** (index rows) |
| Călugăreanu–White–Fuller | `HelicityContext` | **3** + 1 OCR-only |
| Yang–Baxter / Drinfeld | `RMatrixBraidingContext` | 1 (index row) |

Note `INDEX.md` is a bad proxy and should not be used alone: it returns **0**
rows for Littlewood–Richardson against **27** documents in `sections/`. Use the
deeper tiers, and remember the OCR tier — the Călugăreanu hit includes
`library/procrsoclondona92/` (Moffatt & Ricca 1992, *Helicity and the
Calugareanu invariant*), whose `sections/` is a JSTOR banner and whose real text
is in `ocr/`.

**Third: the one apparent gap turns out to be a Mathlib question, not a
literature one — and the corpus's claim about it is too strong.**
`HasFiniteLPDuality` carries this docstring:

> *"Needs abstract LP duality infrastructure that does not exist in Mathlib"*

Convex-duality *textbook* material is indeed thin in the library
(`complementary slackness`: **0** documents; `linear programming`: 3). But the
docstring's claim is about Mathlib, and it overstates. Verified by import
against the restored cache:

```
@ProperCone.hyperplane_separation : ... Convex ℝ K → IsCompact K → Disjoint K ↑C →
                                        ∃ f, (∀ x ∈ C, 0 ≤ f x) ∧ ∀ x ∈ K, f x < 0
@ProperCone.innerDual              : Set E → ProperCone ℝ E
     ProperCone.innerDual_innerDual : ProperCone.innerDual ↑(ProperCone.innerDual ↑C) = C
```

A Farkas-type separation theorem for proper cones, plus the conic bidual — which
is the substrate for conic (hence LP and SDP) strong duality under a
strict-feasibility condition. What Mathlib appears to lack is a *packaged*
standard-form LP duality theorem, which is a build on top of existing API rather
than a from-scratch project. So `HasFiniteLPDuality` and `HasStrongDuality` are
**not literature-blocked**; they are ordinary formalisation work with the
ingredients already present.

**Scope this honestly.** I could not enumerate Mathlib in this container: the
clone carries **0 `.lean` sources** and **6990 oleans**, with no `Mathlib.olean`
root, and it is a *subset* — the import cone of what QOU builds. So "absent from
this cache" is not evidence of "absent from Mathlib", and the claim above is the
positive one only: those three declarations **are** present and do resolve.

### So the answer is: no lit needed

If something *would* help, it is not a paper. In descending order of value:

1. **A decision, not a document** — whether a vacuous context class should be
   re-encoded against parameters (the q-NS remedy) or the pseudo-theorem simply
   dropped. That is authorial: it changes what each content block claims.
2. **Convex-optimisation duality in the library** would be genuinely useful for
   its own sake (Boyd–Vandenberghe, or Schrijver §7.2/§7.4 which the class
   already cites) — but as reference material, not as a blocker. Offer it if
   it's cheap; nothing waits on it.

## Method, and why the tool has a `--selftest`

The prober generates the most trivial model it can — `Unit` for every `Type`
field, `0` then `1` for every scalar, `fun _ => default` for every function —
and compiles it. The asymmetry is deliberate:

- **a pass is decisive** — the class is inhabited, full stop;
- **a failure is inconclusive**, and says only that *this generator's* defaults
  did not satisfy the fields.

So the reported count is a **lower bound**, and the complement must never be
quoted as a count of contentful classes. The 26 above is a floor, not an
estimate — 26 `unproven` and 27 `skipped` are 53 classes about which these runs
say *nothing*.

Two calibration points for how soft that floor is. Fixing three generator gaps
took the count from **15 to 25** in one pass, without touching a single class —
so the floor moves with the tool, not with the corpus. And I first wrote **26**
into this document, having counted the summary line itself as a result; the
figure is 25.

### 🛑 But "keep fixing the tool" is REFUTED — measured twice, and both were mine

The paragraph above invites an obvious inference: the gaps have all been the
tool, so keep fixing the tool and the floor keeps rising. **I made that
inference, recommended it, and then measured it twice. It does not hold.**

**Attempt 1 — sibling imports.** The prober probes a content-block sibling by
compiling a copy of its file, which inherits *that file's* imports; most
siblings do not import `Mathlib.Tactic`, so `linarith` came back *"unknown
tactic"*. Real defect, and I verified it by hand on `DirectionSanityGateClass`:
`unproven` in the sweep, **INHABITED, exit 0** once the import was prepended. I
then wrote *"15 sibling classes judged with a crippled tactic set"* into a
commit message and a PR body, on the strength of that one case.

**Measured over all 54 undecided classes: the fix converts exactly ONE**
(`CPTClosure`). Not 15. The floor is **26**, not the ~40 the inference implied.

**Attempt 2 — unfolding the claim's own constants.** The reason
`DirectionSanityGateClass` still failed is that the discharge cannot unfold a
`noncomputable def`: the goal comes back as
`|0 - qBetaTargetMagnitudeAtQ0| ≤ directionSanityThreshold * …`, verbatim. My
hand-proof used a bespoke `rw [qBetaTargetMagnitudeAtQ0, directionSanityThreshold,
abs_le]; constructor <;> norm_num`, which the generic list does not contain. So I
made the generator pass each claim's own constants into `norm_num`'s simp set.

**Measured on the six gate classes: it converts ZERO** — `DirectionSanityGateClass`
included, the very class whose hand proof motivated it. That patch was reverted
rather than committed: a change with no measured yield is not an improvement.

**What this actually establishes**, stated narrowly:

- The **hand proof stands** — `DirectionSanityGateClass` *is* inhabited, so at
  least one `unproven` verdict is definitely a harness artifact.
- **How many more, nobody knows.** Two systematic attempts to convert them
  yielded 1 and 0. There is no evidence the remainder is mostly harness, and
  the two data points argue against it.
- So the honest reading of `unproven` + `skipped` is what this document already
  says — *unmeasured* — and the tempting stronger reading, "mostly the tool",
  is now **refuted by measurement**. A per-class hand proof is the only method
  shown to work on them, at roughly the cost the sizing audit originally
  estimated.

Recorded at this length because the error is the one this whole arc is about: I
generalised from a single verified case to a population, put the number in a
commit message and a PR body, and only then measured it.

The `--selftest` pins the five classes inhabited by hand before the script
existed. That guard is load-bearing rather than ceremonial: **the first version
found only 2 of the 5.** It could not resolve a field whose type was another
field of the same class (`mass : CategoricalObj → ℝ`), and so read
`Finset Partition` as `∅`, turning a satisfiable `Σ w = 1` into `0 = 1`. Both
misses surfaced as `unproven`/`skipped` — that is, as *"no finding"*, which is
precisely how a detector reports a tree it never looked at. Two further gaps
found the same way: `ℕ` instantiated for a `[Field R]` binder, and an
ASCII-only identifier pattern that dropped field names like `Δ_K`.

This is the fourteenth-or-so entry in the same family as
[`2026-08-15-detector-blindness-taxonomy.md`](2026-08-15-detector-blindness-taxonomy.md),
and it arrived the same way as the others: a detector reporting a clean result
about a question it had not asked.

## Adjacent observation, not a finding

`observations/terminal-resolution-proof.lean` defines
`proton_topological : ℝ := proton_mass_MeV`, so `row1_proton_matches_CODATA :
|proton_topological - proton_mass_MeV| < 1e-3` is `|x − x| < ε`. **This is
disclosed** — the file's own header says these "are the CODATA values
themselves" and that the deuteron row is "NOT an independent topological
prediction". Recorded here only so a future reader who greps the theorem name
does not rediscover it as a defect. Note there are two different
`proton_topological` in the corpus: this one, and
`QOU/HadronicMass.lean:210`'s `proton_quarks.value`, which is a substantive
claim. Same name, different epistemic status — resolve to the definition before
citing either.

## Reproducing

```sh
# the gate (needs the olean cache restored; never `lake build`)
LEAN_PATH=<mathlib libs>:<QOU build lib> \
  lean docs/audits/2026-08-30-context-classes-are-inhabited-by-zero.lean

# the tool's own regression guard
python3 scripts/lean-context-class-inhabitation-probe.py --selftest

# the sweep
python3 scripts/lean-context-class-inhabitation-probe.py --json out.json
```
