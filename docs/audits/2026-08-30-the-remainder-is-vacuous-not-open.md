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

## Result: 52 of the 79 classes are inhabited by `Unit` and zero — including all three the sizing audit named

**26 by machine, 26 more by hand** (see "the method is per-class hand construction" below).

> **🛑 The running total was over by one for two turns, and the correction is
> worth stating rather than silently applying.** I had been adding the machine
> figure to the hand figure as though the two sets were disjoint. They are not:
> `CPTClosure` is in the 26 *because* it was converted out of the undecided list
> by the sibling-import tool fix, so it was being counted twice. And
> `ShellClosureMonotone` — a real finding, below — is **not one of the 79**: it
> backs no projection in the 90 and surfaced only while adjudicating
> `HasFrobeniusStability`, so it does not belong in this denominator either.
> Net: the total went 48 → **47** on that correction, and back to **48** when
> `LpDualStabilityContext` was adjudicated afterwards (the LP pair, below). The
> two 48s are not the same 48 — do not read the round trip as "nothing changed".
> This is the same class of error as the ones this audit records against itself
> further down, and it arrived the same way: arithmetic across two lists instead
> of a set operation on them.

The 90 findings sit on **80 distinct context classes** (79 named, plus 4
declarations with no instance binder at all). Probing each one by generating the
most trivial model available and asking `lean` whether it type-checks:

| | |
|---|---|
| classes probed | 79 |
| **INHABITED with no hypotheses** | **52** (26 machine + 26 hand) |
| scored NOT vacuous — genuine claim | 21 — `MatrixChainEqBuildChains`, the four §4 gates, `HasFiniteLPDuality`, `ConvergenceBound`, `QIntRatioBoundSmall`, `H2SAngleS3HolonomyConjecture`, `DeltaTauMSurrogateTaylorCoeff2`, `FiberAdjointInvolutionContext`, `QuantumObservableUniverseExistsContext`, `DressedMassSubstrateSplit`, `WhiteheadVolumeConjectureLimit`, `HasDqSquaredNonvanishing`, + 6 already inhabited in the corpus |
| REFUTABLE — false as stated | 2 (`SkeinMassRelationHolds`, `DoubleMagicConjecture`) |
| INERT — no direction can be invoked | 2 (`RadiusOfConvergenceGateClass`, `ConfinementPhaseStratificationContext`) |
| **DRAINED — proved outright, class deleted** | 2 (`ProtonPairSkeinApprox`, `NeutronPairSkeinApprox`) |
| still undecided | **0** |
| hand-verified before any tooling existed | 5 of 5 |

**The list is empty.** All 79 are adjudicated: 52 vacuous, 21 genuine, 2 false
as stated, 2 inert, 2 drained by proof. See the final tranche below for the last
six, which are the most encouraging six in the set.

`HasDqSquaredNonvanishing` is worth a line of its own, because its ledger entry
is arguably **already dispositioned**: on 2026-08-23 the circular instance
(`… [hf : Fact (cqd.dq ≫ cqd.dq ≠ 0)] := ⟨hf.out⟩`) was removed, leaving what
the file calls "an honest open carrier". Its field constrains a parameter, so it
is not vacuous by shape; but whether the three hypotheses it binds
(`hq`, `hd_sq`, `hcross`) force the conclusion is the open question the file
exists to pose, so it is neither witnessed nor refuted here.

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

### 🛑 A second narrowing, and it corrects my own count

**"Inhabited" means VACUOUS only for an *unparameterised* class.** For a class
`C x`, a downstream `theorem foo [C x] : P x` quantifies over `x`; exhibiting
`C x₀` for one `x₀` shows the hypothesis is **satisfiable**, not that it assumes
nothing. I was not distinguishing these, and the headline count was loose.

Measured over the 42: **36 are unparameterised** — for those, inhabited ⇒
vacuous, and the strong reading holds. **Five take a value parameter**, and they
split again:

- **Parameter inert** (still vacuous): `SchurWeylMassContext (Z N)` — no claim
  mentions `Z` or `N`, as documented above; `KnotFactorSpectralContext (n)` and
  `MassVolumeFactorization (K n)`, where `n` only indexes a context field.
- **Data-only** (vacuous *despite* being parameterised): a class with **no Prop
  fields at all** is inhabited at every parameter by supplying the data.
  `HasMarkovTrace P q` is one field, `value : R_q`; `HasBindingMultiplicity S`
  is one field, `mu : R_q → ℕ`. Neither states anything, so `[HasMarkovTrace P q]`
  assumes nothing anywhere — it is a "hand me a value" carrier, not a hypothesis.
  The parameterised/vacuous distinction turns on **whether the class has claims**,
  not on whether it has parameters.

  A sharper case is `NobleGasMultiOperator`, which *does* carry a claim —
  `bindingMultiplicity S q ≥ 2` at noble-gas `Z` — but the claim constrains the
  `[HasBindingMultiplicity S]` instance, and that instance is free data.
  Choosing `mu := fun _ => 2` satisfies it. **The pair is jointly vacuous while
  neither half looks it**: the claim is real, and the thing it is a claim about
  is unconstrained. A checker reading either declaration alone passes both.

### A hypothesis binder that cannot fail

`LevelSufficient` takes a side condition `(_h_cover : kMax P q ≤ P.coarseStrands)`,
which reads as a genuine covering requirement. But `kMax P _q :=
P.markovClass.strandCount` and `P.coarseStrands := P.markovClass.strandCount`
are **the same expression**, so the inequality is `le_refl` — for every `P` and
every `q`. That is not a witness at one parameter; it is a theorem about the
class, and it is in the gate file as `cover_always`.

This is worth separating from vacuity. The class's *field* (`trace_eq`) is a
real claim about two Markov-trace carriers; what is empty is the **side
condition the signature advertises**, and a reader scanning the binder list has
no way to see that.
- **Degenerate-parameter witness** (NOT vacuous at general parameters):
  `HasArgumentPrinciple (f ω₁ ω₂ S)`, satisfied by taking the pole set `S := ∅`;
  `SharedDenominatorCuspHolonomy (q x n)`, satisfied at `n := 0` where the `∀`
  over `Fin n` is empty. For these two the honest claim is that the class is
  satisfiable and that its content is concentrated away from the degenerate
  value — not that a `[C]` binder assumes nothing.

So: **~40 vacuous, 2 satisfiable-at-a-degenerate-parameter.** The corrected
reading does not disturb the main finding — all three classes the sizing audit
named are unparameterised and vacuous — but the two must not be counted as
vacuous, and they were.

**The same distinction rehabilitates a class I had called contentful.**
`HasStrongDuality (sdp) (_h)` already has a corpus instance,
`instHasStrongDualityEmpty`, at the **empty-constraint** SDP. That is an honest
degenerate witness in exactly the `BorromeanQuark` mould: it establishes
satisfiability at `ι = Empty` and says nothing about a general `sdp`. It does
*not* make the class vacuous, and I would have mis-scored it in either
direction without looking.

### And the prober cannot see existing instances at all

It always generates a fresh model and never asks `inferInstance`. Measured over
the 38 undecided, **at least 6 are already inhabited somewhere in the corpus** —
`BorromeanQuark`, `HasStrongDuality`, `QFactRatioBound`, `RhoPrefactorStructural`,
`Term7ShellCorrectionClass`, and `SkeinMultisetInvariant` (whose
`skeinMultisetInvariant_refl` a single-line grep misses because the signature
wraps). Each needs reading before it is scored, per the paragraph above: an
existing instance may be unconditional, parameterised-degenerate, or itself
hypothesis-laden, and those are three different verdicts.

### All six read and scored — and NONE of them adds to the vacuity count

This is the opposite of what counting them would have given, which is why they
were not counted.

| class | verdict | why |
|---|---|---|
| `BorromeanQuark` | **false positive — name collision** | not scored |
| `Term7ShellCorrectionClass` | **unconditional** | already known provable; adds nothing new |
| `HasStrongDuality` | parameterised-degenerate | `ι = Empty` only |
| `QFactRatioBound` | parameterised-degenerate | `k = 0` and `k = 1` only, under real hypotheses |
| `SkeinMultisetInvariant` | parameterised-degenerate | the reflexive diagonal only |
| `RhoPrefactorStructural` | parameterised-degenerate **and self-satisfying** | deuterium only, via a placeholder |

**`BorromeanQuark` is a ten-way name collision.** `class BorromeanQuark` is
declared **ten times** across `content/`, in ten different files. The instance
that matched is `observations/borromean-quark.lean:120`, inhabiting the class at
`:87` whose field is `bare_mass : ℝ → ℝ`. The class the ledger flags is
`brings-surface/orbital-fourier-decomposition.lean:180`, whose field is
`orbitalDim : ℕ → ℕ`. **Different classes, same name** — so the match was an
artifact of grepping a name, the very error AGENTS.md §"Grep the claim SHAPE"
warns about, and the same shape as the `markovZ` overload.

**`SkeinMultisetInvariant` is the sharpest of the four degenerates.** Its
instance is `skeinMultisetInvariant_refl config config h h := ⟨rfl⟩` — the
*reflexive diagonal*, where the claim `skeinPolynomialSym c₁ = skeinPolynomialSym
c₂` is `rfl` by construction. The class's actual content is about **distinct**
configurations sharing a nucleon multiset, and the corpus's witness sits exactly
where that content is absent.

**`RhoPrefactorStructural` carries the arc's own defect inside a corpus
instance.** `instRhoPrefactorStructural_deuterium` satisfies
`ρ = round([d_λ*]_q)` by supplying `q_int := q_int_placeholder q 1`, and
`q_int_placeholder q rho := fun _ => (rho : ℝ)` — i.e. it *defines* the
q-integer to be `ρ`, making the claim `|ρ − ρ| ≤ 1/2`. The file is candid about
this (it is named a placeholder and justified at the classical limit `q = 1`),
so this is disclosed rather than hidden; but the instance does not witness the
class's claim at general `q`, it witnesses it by construction.

**`QFactRatioBound` is the honest §3b-cond pattern** and worth naming as the
positive example: two instances, `qFactRatioBound_zero` and
`qFactRatioBound_one`, at `k = 0` and `k = 1`, each carrying the real hypotheses
`q > 1` and `q < 2`. Small-instance coverage with the general case open, stated
as such.

### 🛑 The collision also threatens results of mine

Five of the 79 bundle names are declared more than once: `BorromeanQuark` (×10),
`RMatrixBraidingContext`, `DoubleMagicConjecture`, `HasFiniteLPDuality`,
`MassVolumeFactorization` (×2 each). I inhabited two of them, so which
declaration a witness targets matters:

- **`RMatrixBraidingContext` — my witness covers only one of the two, and the
  ledger flags both.** I inhabited the library copy
  (`QOU/Braiding/r_matrix_braiding_structure.lean:30`). The content-block sibling
  (`braids-and-knots/r-matrix-braiding-structure.lean:46`) is a **strict
  superset** — it adds `Rcheck1`, `Rcheck2` and `claim_braid_relation` — and
  carries two of its own ledger findings (`r_matrix_braiding_structure`,
  `braid_rep_from_R_check`). Those are **not** covered by my witness.
- `MassVolumeFactorization`: the prober compiled against a copy of the flagged
  file itself, so its verdict targets the right declaration.

**Gap closed, and the superset does constrain something.** The sibling is
inhabited too, by a commutative model — but **not** by the same one. `V3 := ℕ`
with `comp := (·*·)` and any values satisfies the Yang–Baxter claim, exactly as
in the library copy; the *added* `claim_braid_relation`
`Ř₁Ř₂Ř₁ = Ř₂Ř₁Ř₂` then reduces to `a²b = ab²`, which in ℕ forces `Ř₁ = Ř₂`
(`7,11` gives `539 = 847`). So the sibling's extra field is not free: it is
satisfiable, and it pins the two braid operators equal in any commutative model.
That is a mild constraint rather than none, and it is the difference between the
two declarations.

Verified against a copy of the sibling file (siblings have no module, so this
witness cannot live in the committed gate file — it is the same copy-and-compile
route the prober uses):

```sh
{ echo "import Mathlib.Tactic"; cat content/quantum-observable-universe/braids-and-knots/r-matrix-braiding-structure.lean; \
  echo 'open QOU.Braiding in'; echo 'example : RMatrixBraidingContext where'; \
  echo '  V3 := ℕ'; echo '  comp := fun a b => a * b'; \
  echo '  R12 := 2'; echo '  R13 := 3'; echo '  R23 := 5'; \
  echo '  Rcheck1 := 7'; echo '  Rcheck2 := 7'; \
  echo '  claim_yang_baxter := by ring'; echo '  claim_braid_relation := by ring'; } > /tmp/rm.lean
LEAN_PATH=<mathlib libs>:<QOU build lib> lean /tmp/rm.lean   # exit 0

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

### A fourth shape: the ORDER is trivial, so the inequality cannot be false

Everything above is vacuous because a *witness exists* — the class is inhabited
at some value, so the binder assumes nothing. `ShellClosureMonotone` does not
need a value.
[`QOU/BraidKnot/ShellClosureStability.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/ShellClosureStability.lean)
declares, at file scope,

```lean
local instance : LE R_q := ⟨fun _ _ => True⟩
```

so `≤` on `R_q` **is** `fun _ _ => True` for every declaration in that file. The
class field

```lean
monotone : frobeniusStability D_prev q ≤ frobeniusStability D q
```

therefore elaborates to `True`, and `⟨trivial⟩` inhabits the class at **every**
`(D_prev, D, q, h)`. The gate file carries that as a theorem general in all
four arguments (`shellClosureMonotone_always`), not as a witness at one tuple.

**What this costs.** `shell_closure_monotone` is claim (1) of the shell-closure
proposition — "the Frobenius stability index does not decrease under a one-step
dressing". It is not merely unproved: **it cannot be false**, and neither can
the first conjunct of `shell_closure_terminality`, which is assembled from it.
The second conjunct routes through `NobleGasMultiOperator`, already scored above
as jointly vacuous with its free `HasBindingMultiplicity` data. So all three
claims of the proposition are empty in Lean, by three different mechanisms.

The file half-knows this. Its own `shellClosureMonotone_refl` carries the
comment *"`≤` on `R_q` is the trivial (`fun _ _ => True`) order (local instance
above), so `x ≤ x` is `True`"* — which reads as an observation about the
reflexive case. It is the general fact, and stating it only for `D_prev = D`
makes every other instance look like it costs something.

`HasFrobeniusStability` itself is the `HasMarkovTrace` shape one more time: a
single data field `sigma : R_q → R_q`, no Prop fields, inhabited at every `D`.

**Floor: 46 → 47.**  (`LpDualStabilityContext` takes it to 48; see the LP pair below.)

### And one scored NOT vacuous

`MatrixChainEqBuildChains (config j hj)` goes the other way, recorded because a
drain that only reports vacuity is not a measurement. Its field

```lean
eq : matrixChain (chainCrossings config j) = (buildChains config).get! j
```

relates a right fold over the crossing sequence to the left fold in
`buildChains`, and nothing about it is trivial. The gate file proves it at
`config = [proton, proton]`, `j = 0`, where both sides evaluate to `2 • T_pp` —
an entry-by-entry computation, not a projection. **So the class is satisfiable
and non-trivial and does not join the vacuity count.**

Its projection still carries a defect, a different one.
`matrixChain_eq_buildChains` states exactly the class field and discharges it
with `exact matrixChain_eq_buildChains_axiom config j hj` — §3b-cond item 5, a
theorem proved by projecting a hypothesis identical to its own conclusion. What
the witness shows is that the honest route is open in both directions: for a
*concrete* config the claim is decidable by unfolding and needs no class at all,
and the *general* statement (all transfer matrices commute, so `foldl` and
`foldr` agree) is a real lemma someone can prove. The class stands in for work,
not for nothing — which is the distinction the rest of this audit is about.

### The four §4 gate classes are the good case — and two of them are much weaker than they read

`MassAnchorStableGateClass`, `MassDirectionSanityGateClass`,
`DirectionSanityGateClass` and `BarEvenKernel` all score **NOT vacuous**. Each
takes real-valued parameters, each field is a genuine constraint on them, and
each file carries a `_reject` theorem showing the class is refutable at a bad
parameter — the property a gate is supposed to have and which no vacuous class
in this audit possesses. `BarEvenKernel` is inhabited at its *intended* point
(`pole := uSubstrate`, `c2 := -1`, `c3 := J_Hopf(1) = -2`), a real instance
rather than a degenerate one, and three of its four fields are an exact equality
or a 1e-6 relative tolerance.

They also needed a route the prober does not have: they are **content-block
siblings**, not modules, so nothing can `import` them. The witnesses are in
[`2026-08-30-gate-classes-admit-zero.lean`](2026-08-30-gate-classes-admit-zero.lean)
and compile via
[`scripts/lean-sibling-witness-check.sh`](../../scripts/lean-sibling-witness-check.sh),
which concatenates siblings ahead of a witness fragment and runs `lean`-direct.

**The measurement that came out of scoring them.** Both direction gates are
stated additively, `|m − target| ≤ threshold · target` with `threshold = 10`.
That is not "within 10× of the target" — it is a band of width `20 · target`
*centred* on the target, reaching well below zero on one side:

| gate | target | pass band |
|---|---|---|
| `MassDirectionSanityGateClass` | 2.46 | `[−22.14, 27.06]` |
| `DirectionSanityGateClass` | 0.99824 | `[−8.98, 10.98]` |

Two consequences are **proved**, not asserted:

- **Zero clears both.** A candidate predicting magnitude `0` — no signal at all
  — instantiates each class.
- **The whole `z < 1` region clears `DirectionSanityGateClass`**
  (`admits_everything_below_one`, for every `m ∈ [0,1]`). The threshold's own
  docstring states its purpose as catching *"order-of-magnitude direction errors
  (like PR #1850's z < 1 vs target > 1)"*. `[0,1]` sits strictly inside the pass
  band, so **no candidate can ever be rejected on the ground the docstring
  names.** The same file's target constant is `0.99824`, itself below 1, so the
  "target > 1" in that sentence does not describe this file either.

This is not the vacuity defect — an additive band still rejects a candidate off
by 30×. It is a **weaker claim than the prose around it**, and the mass-side
file half-flags it: it states that the sympy probes implement the
*multiplicative* variant `max(|m|/target, target/|m|) ≤ threshold` while the
Lean gate is additive, and asserts the additive form "admits both variants as
instances". True, and it is the direction that matters — the Lean gate is the
weaker of the two, so clearing it is not evidence of clearing the probe's.

### The LP pair scores oppositely, and the reason generalises

Both classes are about linear-programming strong duality, both sit behind a
ledger projection, and they land on opposite sides. What separates them is
whether the quantities the claim constrains are **free data on the class** or
**parameters supplied by the caller** — which is the same discriminator as the
`NobleGasMultiOperator` / `HasBindingMultiplicity` pair, one layer up.

**`LpDualStabilityContext` — VACUOUS.** Unparameterised, with fourteen data
fields (`channels`, the Gram matrix `G`, `κ_G`, `y_star`, `t`, `x_star`,
`x_partial`, `tr_M_x_star`, `y_0_star`, …) followed by four Prop fields that
constrain only those. The instance chooses everything the claim is about, so
`lp_dual_stability`'s four-part conclusion — primal stability, bounded dual
prices, sub-braid instability, **and strong duality
`tr_M(x*) = y₀* · n_target`** — is conditional on nothing. Floor 47 → 48.

Worth recording *which* model works, because it is exactly the prober's blind
spot: `channels := 0` **fails**, since `partial_unstable` at the empty sum is
`0 < 0`. The witness needs one channel and a negative `x_partial` — a value the
generator never tries, its defaults being zero and empty. That is the whole
reason this class came back `unproven`, and it is a cleaner instance of the
pass/fail asymmetry than any of the abstract statements of it above.

**`HasFiniteLPDuality lp` — NOT vacuous.** Parametric over the LP, with two
fields that constrain that `lp` rather than data of its own. Satisfiable at an
LP with `primal_obj = dual_obj`, and **refutable** at one without — the second
being the file's own `badLP`. Its header already records that two axioms
manufacturing the class for every `lp` each made the library inconsistent, and
that is the strongest possible evidence a class is not vacuous: something that
can be refuted at a parameter assumes something at every parameter. Stated as
`→ False` rather than `¬`, because the class is declared `: Type`, not `: Prop`,
so its instances are data and are not proof-irrelevant.

**Its same-named twin is a third thing, and stays undecided.**
`QOU.BraidKnot.ConfinementNFPartial.HasFiniteLPDuality`, in the
`confinement-nf-partial-proof.lean` content-block sibling, has the same name,
the same two obligations and a *different* `OperatorSelectionLP` — one whose
`primal_obj` and `dual_obj` are `opaque` rather than fields. That single choice
removes both routes at once: no model can be chosen to make
`|primal − dual| = 0` provable, and no `badLP` can be built to refute it, since
nothing reduces. So it is neither witnessed nor refuted here and stays in the
undecided column — recorded because "the LP duality class is settled" would be
wrong, and the two are one grep apart.

### The first two DRAINED the right way — proved, classes deleted

`ProtonPairSkeinApprox` and `NeutronPairSkeinApprox` are the arc's first
findings closed by **disposition 1** (prove it) rather than scored. Both carried
a single field that was the bound itself, on the stated ground that *"the full
proof reduces to a numerical evaluation of `Real.rpow` at `(substrate_q, 1/2)`,
which `norm_num` cannot yet discharge"*.

That is true of `norm_num` and is not a reason the bound cannot be proved. The
root is **eliminated, not evaluated**: writing `s = q^{1/2}`, the only facts
needed are `s > 0` and `s * s = q`; the denominator collapses to
`s + s⁻¹ = (q+1)/s`, so every `pair_skein_mass` is *linear* in `s`, and
`s ∈ (1.0534, 1.0535)` follows from `s * s = 1.1097` by `nlinarith`. Both bounds
close by `field_simp; nlinarith`. Same technique as the `SkeinMassRelationHolds`
refutation, pointed the other way. `HadronicMass.lean`: exit 0, 0 errors, 14 s.

**And the side hypothesis both classes bound is FALSE.**
`q^{1/2} + q^{-1/2} = 2.0027092783…` at `q = 1.1097`, so its distance from the
asserted `2.00228` is `4.293e-4` — **4.3× the `1e-4` tolerance**. That hypothesis
was an explicit argument of both theorems, so neither could ever be invoked: no
proof of it exists to supply. A third failure mode, distinct from both the
vacuous class and the false class field — **a true claim made unreachable by a
false side condition**. Recorded as
`HadronicMass.pair_skein_denom_hypothesis_false` (machine-refuted, not asserted).

**The docstring numbers did not reproduce either**, and the corrections run in
the flattering direction, which is why nobody caught them (mpmath, 50 dps):

| | stated | measured |
|---|---|---|
| `√1.1097` | 1.05341 | 1.0534230 |
| denominator | 2.00228 | 2.0027093 |
| `S_ud` | 312.89 | 312.9442 |
| `proton_from_pair_skein` | 938.15 | 938.25205 |
| `neutron_from_pair_skein` | 939.46 | 939.54729 |
| proton agreement | 0.12 MeV | **0.0200 MeV** |
| neutron agreement | 0.10 MeV | **0.0181 MeV** |

`S_uu = 312.3637` matches the stated `312.37`, so the arithmetic was right for
one of the three pair masses and wrong for the other two. The agreements are 6×
and 5× **better** than claimed.

### A second FALSE class, and a gate that cannot fire at all

**`DoubleMagicConjecture` (`QOU/Interactions/LRFusion.lean`) is FALSE as
stated** — machine-refuted in
[`2026-08-31-double-magic-conjecture-is-false.lean`](2026-08-31-double-magic-conjecture-is-false.lean).
Its `magic_iff_double_magic` field is an iff over *every* `Composite`.
At the all-empty composite `⟨∅, ∅, ∅⟩`: `IsDoubleMagic` holds (by the corpus's
own `emptyDiagram_isSelfConjugate`), so the `←` direction forces
`0 ∈ magicLadder = {2, 8, 20, 28, 50, 82, 126}`, which is false.

**Scope — a (b) structural exclusion of the ENCODING, not the physics.** Both
invariants are already proved in the corpus, which is what licenses the (b):
`magicSet` is that literal `Finset` (`decide`), and `emptyDiagram_isSelfConjugate`
is sorry-free. What is excluded is the iff *as written*, which over-quantifies —
nothing requires `C.ydZ`/`C.ydN` non-empty or `C.ydA.n ≥ 2`, so the empty
composite counts as double-magic for a degenerate reason. Whether double-magic
nuclei sit on the magic ladder is untouched. The repair is a non-degeneracy
hypothesis, and it is authorial.

It matters because two theorems in the same file consume the class
(`composite_self_conjugate_of_double_magic`,
`composite_kappa_zero_of_double_magic`), and an uninhabitable class makes both
**vacuously true** — `False → P` for every `P`. Second such case in the arc.

Note the name is overloaded: this is the unparameterised class in
`LRFusion.lean:133`; a *different* `DoubleMagicConjecture (Z N) extends
LRFusionData Z N` lives in `observations/diagrammatic-double-magic-lr-fusion.lean:58`.
Resolve before citing either.

**`RadiusOfConvergenceGateClass` is INERT — a fourth reason a declaration can be
unreachable.** The gate rests on `axiom qBetaCandidatePoleLocation : ℝ`, an
opaque global with no defining property; measured, the identifier occurs in
exactly four places corpus-wide, all in that one file. So the forward gate needs
a proof of an equation about a constant nothing constrains (none exists), and
the reject theorem takes the *same* unprovable shape as a hypothesis. Neither
direction can ever fire. And it could not discriminate if it could: the pole is
a single *global*, not a function of a candidate, so "a candidate failing to
predict this location is REFUTED" has no argument by which candidates differ.

That is now four distinct unreachability mechanisms in this arc — a false class
field (`SkeinMassRelationHolds`), a false side condition
(`pair_skein_denom_hypothesis_false`), an uninhabitable-because-false class
(`DoubleMagicConjecture`), and an undecidable-because-opaque one here. The
repair is to make the pole a function of the candidate; authorial, not
attempted.

**`H2SAngleS3HolonomyConjecture` — NOT vacuous**, witnessed and refuted in
[`2026-08-31-h2s-and-the-inert-radius-gate.lean`](2026-08-31-h2s-and-the-inert-radius-gate.lean):
satisfiable at `⟨0,0⟩`, refutable at `⟨1,0⟩`. Its thinness is a modelling gap
rather than a §3b-cond defect — the class quantifies over an arbitrary pair of
reals while the physics claim is about one specific measured pair, and nothing
pins `d` to the H₂S angle or the holonomy phase.

**`DeltaTauMSurrogateTaylorCoeff2` — NOT vacuous, and its claim is TRUE.** The
field asserts `deriv (deriv delta_tau_M_surrogate) 1 / 2 = 5/6` for the explicit
rational function `P(q)/(4q⁵(q²+q+1))`. Checked in exact rational arithmetic
(no floats): `N(1) = 0`, `N'(1) = −10`, `N''(1) = −100`, `D(1) = 12`,
`D'(1) = 72`, `D''(1) = 368`, giving `f'(1) = −5/6` (matching the file's own
first-derivative proof) and `f''(1)/2 = 2880/1728/2 = 5/6` ✓. So it is drainable
by disposition 1 — prove the second derivative — which the file's docstring
already calls "bulky but tractable". Not attempted here; it is the largest
single remaining piece of Lean work in this arc.

### The final six — and the tail is not where the hard cases are

The last six resolve **1 inert, 5 genuine**, and the interesting thing is *why*
the five are genuine: **three of them carry an in-source record of having
already been hardened against exactly this defect.** The tail of the ledger is
not the hardest cases; it is largely cases that were already fixed and whose
ledger entries are stale.

- **`FiberAdjointInvolutionContext`** — its own docstring says a bare
  `Nonempty (FiberAdjointInvolution C fh)` *"is provable for every category and
  datum, and asserts nothing … that degenerate witness was what this declaration
  shipped until 2026-08-09"*, citing
  [`2026-08-09-inhabitation-is-a-weak-discriminator.md`](2026-08-09-inhabitation-is-a-weak-discriminator.md).
  The conjunct `inv.adjointObj = fh.obj` was added to close it.
- **`QuantumObservableUniverseExistsContext`** — the structure it asserts
  `Nonempty` of records that `adjointObj` *"was previously a free field … That
  made `adjoint_vanishing` satisfiable by taking `adjointObj := 0`"*, fixed under
  bean `qou-fav8`.
- **`DressedMassSubstrateSplit`** — its docstring records a prior axiom that made
  the library **inconsistent**, and that *"the tautology fix over-corrected into
  unsoundness — the statement stopped being empty by starting to be false."* The
  class is the second repair, deliberately with no instance.
- **`WhiteheadVolumeConjectureLimit`** — a genuine open conjecture (van der Veen,
  arXiv:math/0611181), STATE-AND-QUEUED, with bean `qou-1gkf` tracking the port
  of the already-sorry-free downstream `⌊N/2⌋` result to this exact form.
- **`HasDqSquaredNonvanishing`** — the circular `Fact`-based instance was removed
  2026-08-23, leaving what the file calls "an honest open carrier".

**`ConfinementPhaseStratificationContext` is INERT, and its repair already
exists one file over.** The content-block sibling
`knots-particles-confinement/confinement-phase-stratification.lean` declares
`opaque confined` and `opaque mu` with nothing constraining either, so its class
fields — `IsOpen (confinementLocus P)` and μ-constancy — are neither provable nor
refutable, the same mechanism as the radius gate.

But the library module `QOU/BraidKnot/ConfinementPhaseStratification.lean` is the
model repair, and says so:

> *"Rather than `opaque`-stubbing them, we package them as a typeclass
> `HasRealAxisData`… We therefore package the genuine analytic inputs — **not
> the conclusions** — as a typeclass, and **derive** the trio from them. This
> keeps the class honest: its fields are the hypotheses of the stratification
> theorem, and each theorem below performs a real inference … rather than
> projecting an assumed conclusion."*

And it does derive: `phase_locus_open` is
`rw [confinementLocus_eq_feasible P]; exact h.feasible_isOpen` — it uses
`confined_iff_feasible` to rewrite, then applies openness of a *different* set.
That is §3b-cond item 5 satisfied.

**This is the §0a shadowing-stub defect exactly.** The content block's
`lean.ref` is already `qou:QOU.BraidKnot.ConfinementPhaseStratification`, and
the library file has a `theorem ConfinementPhaseStratification` at line 165 —
the very declaration named. Per §0a, sibling resolution wins over the library
path, so the opaque-stub sibling **intercepts** the honest declaration its own
manifest points at.

Prescribed fix, in AGENTS.md's own words: *"If the decl lives at
`<lakeRoot>/<Decl/Path>.lean` (candidate 2), **do not** add a sibling `.lean` —
let the ref resolve to the library decl."* Deleting the sibling is therefore a
stub removal, not an authorial substitution — the ref does not change. It is not
done here because it also retires the block's `.qa.json` criteria keyed on
`source_hashes.lean`, which wants its own validate-and-sweep cycle rather than
riding on a Lean-only verification.

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
