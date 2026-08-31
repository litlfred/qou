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

## Result: 42 of the 79 classes are inhabited by `Unit` and zero — including all three the sizing audit named

**26 by machine, 16 more by hand** (see "the method is per-class hand construction" below).

The 90 findings sit on **80 distinct context classes** (79 named, plus 4
declarations with no instance binder at all). Probing each one by generating the
most trivial model available and asking `lean` whether it type-checks:

| | |
|---|---|
| classes probed | 79 |
| **INHABITED with no hypotheses** | **42** (26 machine + 16 hand) |
| still undecided — INCONCLUSIVE, see method below | 37 |
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

### So the method is per-class hand construction — and it is fast

Having refuted the tool route, I applied the only method shown to work. Eleven of
the undecided classes hand-adjudicated in one sitting, all **inhabited**, all
`lean`-direct exit 0, in
[`2026-08-30-context-classes-hand-adjudicated.lean`](2026-08-30-context-classes-hand-adjudicated.lean):

`EwInterfaceKnotContext`, `FermionBosonKnotLinkContext`,
`AtomicLPStabilityContext`, `ZHabiroConvergenceClass`,
`SpectralSequenceH3ExplicitContext`, `Terms26HigherOperationsContext`,
`SortingColorEnergyContext`, `DecayChannelContext`, `SchurWeylMassContext`,
`ConfinementFrobeniusReciprocityContext`, `EInfinityIdentificationsContext`.

**Floor: 26 → 38.**

**And the `extends` family — 5 classes the prober skips on sight — is
unlocked.** They inherit `QOU.Shared.MarkovTraceContext`, which per the header
of [`QOU/Hecke/InstanceH2.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/InstanceH2.lean)
had **never been instantiated anywhere in the tree**. That file (a sibling's
work, already on `main`) supplies `rankOneModel`, showing `ℚ` is a
`HeckeAlgebra ℚ n 1 ℚ` at *every* `n` — at `q = 1` the parameter `h = q − q⁻¹`
vanishes, so the class is satisfied by a rank-1 algebra where `H_n(1)` has
dimension `n!`. Added here: the same model carries a **Markov trace**
(`trace = id`, `z = 1`), hence a `MarkovTraceContext`. `ExplicitAlphaKH4Context`
follows immediately; `QmnRecursiveMemoizedContext` and
`WedderburnBratteliRecursionContext` follow after one elaboration obstacle worth
recording.

**The parent must be an `instance`, not a `def`.** A child whose field types
mention the *inherited* ring (`chi : ℕ → ℕ → R`) elaborates that `R` as
`@MarkovTraceContext.R inst` with `inst` found by **instance search**, not from
the term supplied for `toMarkovTraceContext`. With a `def` every numeral field
reports `failed to synthesize OfNat QOU.Shared.MarkovTraceContext.R 0` — which
reads as a missing algebraic instance and is really a missing *context*
instance. Ascribing the numerals does not help, nor does `{ ctx with … }`.
`ExplicitAlphaKH4Context` sailed through only because its one field is
`n_classes : ℕ`, a type that never mentions `R`.

**A second parent falls the same way.** `QOU.Shared.OperatorSelectionLPContext`
is inhabited at all-zero, which takes `DemazureFiberMarkovTraceContext` with it.
Its `strong_duality` is a **field** — so LP strong duality is now assumed as a
class field in **three** independent places (`HasFiniteLPDuality`,
`ConfinementFrobeniusReciprocityContext`, and this parent). That is worth
noticing on its own: it is the same missing Mathlib result standing in three
different places, and the `ProperCone` finding above says the ingredients for it
are already available.

**The `extends` family is now closed: all five.** Three shared parents were
inhabited to do it — `MarkovTraceContext`, `OperatorSelectionLPContext` and
`ArchimedeanEval` (the last being the first plus `Rat.castHom ℝ`, giving
`q_real = 1`). The prober skipped all five on the single syntactic ground that
they `extends` something; none of them was hard.

The credit is theirs and the finding is the same one twice over, one layer
apart: a hypothesis that reads as "this is the Hecke algebra with its Markov
trace" is satisfied by `ℚ`.

**The rate is the useful number, not the count.** Eleven classes in roughly
an hour of working time, several minutes of which is `lean` startup on a
cold import rather than thought. At that rate the remaining ~42 undecided are
**hours, not the week** the sizing audit projected — its estimate assumed each
one needed the mathematics the class was standing in for, and so far not one
has.

Several say something sharper than "inhabited":

- **`SchurWeylMassContext`** — the Schur–Weyl decomposition
  `tr_M(𝒜) = Σ_λ s_λ χ_λ / H_q(λ)` holds over the **empty** partition set.
  `partitions` is a context field and no claim requires it to be the partitions
  of `3A`, so `Z` and `N` — the two parameters the class takes — are inert and
  the identity reduces to `0 = 0`.
- **`DecayChannelContext`** — "uniqueness of the decay channel off the boundary
  variety" is discharged by `on_boundary := fun _ => True`. Nothing in the class
  ties the boundary predicate to the energy `E_λ` it is supposed to be the
  vanishing locus of.

- **`ConfinementFrobeniusReciprocityContext`** — the master reciprocity formula
  `⟨O⟩_T = Σ_{i,j∈A*} u*ᵢ (G⁻¹)_{ij} ⟨O,bⱼ⟩` holds with the physical expectation
  and the Frobenius pairing both zero, since both are context fields and nothing
  relates them. Separately worth noting: `strong_duality : primal_obj = dual_obj`
  is a **field**, so LP strong duality is assumed here rather than derived —
  consistent with `HasFiniteLPDuality` doing the same, and the honest reading of
  what the class provides.
- **`EInfinityIdentificationsContext`** — all six `E_∞`-page identifications hold
  at `n_pages := 0`, which makes the six-term sum empty and the "unified mass
  formula" claim `0 = 0 + 0 + 0`.

These are §3b-cond item 5 in a form a syntactic checker cannot see: the *shape*
is right, and the constraint is missing between fields rather than within one.

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
