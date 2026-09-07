# The self-assuming projection reaches the paper — and the class surface is honest

**Date:** 2026-09-07 · **Bean:** `qou-9yt9` · **PR:** litlfred/qou#6987

Follow-on to the axiom tranche of #6933 (twenty-one axioms removed: eleven
false, eight vacuous, one shadowing, one collapsing). That tranche drained the
`axiom` surface. This one asks the same two questions of the **conditional
class** surface, which no axiom gate can see, and gets opposite answers.

## The two questions, and the answers

| | axiom surface (#6933) | class surface (this) |
|---|---|---|
| **Is it vacuous?** — would Lean close it unaided | 8 of 112 yes | **0 of 27 yes** |
| **Does it reach the paper?** | not measured | **8 content blocks** |

The class surface is **not** vacuous, and that is the useful negative. Its
problem is *visibility*.

## Why a conditional class is invisible

    class C (args) : Prop where
      field : P
    theorem P_holds (args) [hi : C args] : P := hi.field

Zero axioms, zero sorries. `#print axioms` on `P_holds` is clean.
`scripts/lean-axiom-guard.py` counts nothing; the vacuity detectors see a
theorem with a real proof term. The unproved assertion has moved into the
**signature**, where no axiom gate looks.

`scripts/lean-cited-not-proved-audit.py` already knows this — it is the third
of its three categories, and its own docstring calls it *"the category a reader
is most likely to mistake for a proof."* Its live figures, re-measured today at
`<working tree>` (3711 files):

    REAL `sorry` TERMS         10   (10 cited, 0 uncited)
    REAL `axiom` DECLARATIONS 112   (110 cited)
    CLASSES                   992 declared, 344 inhabited, 648 with NO instance

So the class category is ~6× the axiom category. Nothing here re-derives that;
it was already measured, and re-deriving it is what the corpus-grep checklist
exists to prevent. What follows is what was *not* measured.

## 1. The class hypotheses are not vacuous barriers

`scripts/lean-class-hypothesis-vacuity-probe.py` — the class analogue of
`lean-axiom-provability-probe.py`. For each self-assuming candidate: delete the
instance binder naming the class, replace the body with a short tactic block,
compile. Exit 0 means Lean proves the conclusion outright and the class was
standing in for nothing.

**Result: 0 of 27 scored candidates provable.** `FAIL=27, SKIP=14, NOBASE=0`.

Read the direction correctly. A PASS is a proof; a FAIL is evidence of nothing
— the tactic list is deliberately short, because a long one turns the probe
into an unbounded proof search whose failures say nothing. So this is **not**
"the 27 claims are hard". It is "none of them is trivially free", which is what
distinguishes them from the eight vacuous axioms of #6933.

Two properties of the measurement, both load-bearing:

- **Every probe compiles the file UNCHANGED first.** A file that is red before
  the probe touches it — a missing olean, a red import — would fail in the
  direction that reads as *"the class is load-bearing"*, which is the
  comfortable answer. `NOBASE=0` says no verdict here is environmental.
- **The 14 SKIPs are a coverage statement, not a gap.** They are the
  explicit-structure-argument idiom (`theorem f (S : Bundle) : P := S.field`),
  which has no instance binder to delete. That idiom is also the one that does
  **not** hide: an explicit argument must be supplied by name at the call site,
  while an instance binder is inferred silently. The probe covered the hiding
  form and skipped the visible one.

## 2. Eight paper claims are backed by a projection

`scripts/lean-self-assuming-content-join.py` joins the 41 self-assuming
declarations against every `lean.ref` in `content/`.

**8 content blocks of provable kind** — 1 `theorem`, 6 `proposition`, 1
`corollary`, **zero `conjecture`** — have a projection as their formal backing.
Seven carry no §3b-cond item-3 conditional-banner signal.

| block | kind | md | banner |
|---|---|---|---|
| `categorical-self-duality` | proposition | 32 w | no |
| `quantum-observable-universe-exists` | proposition | 41 w | no |
| `strong-multiplicativity` (fred2005) | theorem | 55 w | no |
| `electron-period-base` | proposition | 79 w | no |
| `jet-prolongation-C` | corollary | 86 w | no |
| `flavor-dressed-mass-from-substrate-split` | proposition | 120 w | no |
| `categorical-jet-prolongation` | proposition | 212 w | **yes** |
| `sw-period-residue-sum` | proposition | 730 w | no |

### The banner column is phrasing, not honesty

`sw-period-residue-sum` scores **no** and its `.md` is the most carefully
scoped narrative in the set: it states what the enclosed pole set $E$ is, why
$E$ is not identifiable under the classical-jet rule, that the branch locus is
bar-symmetric so the unit circle is inadmissible, which prolongation remains
open, and it cites the beans (`qou-6v5l`, `qou-qx7j`). The regex is looking for
a banner *form* it does not use.

**Nothing is repaired on the strength of this table.** It is a candidate list
for reading, which is the same contract the underlying audit states for itself.

### Read one before you trust the list — `quantum-observable-universe-exists`

It looked like the sharpest case: a 41-word proposition asserting that
*"Setting $\mathbf{C} = \mathbf{Rep}(U_q(\mathfrak{sl}_2))$, $A =
\mathcal{O}_q(\mathrm{SU}(2))$, and $\tau$ the forgetful functor realizes the
axioms explicitly"*, whose Lean assumes `Nonempty (…)` and projects it.

It is not an over-claim. The block carries
`proofs: ["prf:quantum-observable-universe-exists"]`, and that proof block is a
worked narrative proof — the construction, four cited axiom lemmas
(`lem:qou-exists-axiom-1..4`), Woronowicz's Haar state, Chari–Pressley, Kassel
— concluding *"under the Chern-class hypothesis"*, with Tannaka–Krein named as
background and explicitly not re-proved. The Lean file's own docstring is
equally scrupulous: it records that the hypotheses are ring conditions rather
than a field, why `∀ k, [Field k]` was both too strong and too weak, and that
the remaining work is the Drinfeld–Jimbo representation category itself.

So this is the corpus's ordinary, honest posture: **proved in narrative against
cited literature, not proved in Lean, because the category is not in Mathlib.**
What is genuinely missing is one sentence on the *proposition's* `.md` saying
so. That is a follow-up, and it is a `.md` repair, not a Lean one.

## Corrections made before shipping, both mine

- **The join first reported 9, not 8.** It matched on the declaration's last
  name segment and paired `prop:quantum-universe-exists` with
  `QuantumObservableUniverse.exists_instance`. Both declarations are real and
  distinct — `QuantumUniverse.exists_instance` is at
  `quantum-universe-exists.lean:43` and is not self-assuming at all. The join
  now matches fully-qualified names. A defect would have been reported in a
  clean block.
- **"14 single-field classes are item-5 violations" was too strong**, and was
  the framing this tranche started from. Reading three of them
  (`SkeinMultisetInvariant`, `HasStrongDuality`, `FiberAdjointInvolutionContext`)
  shows honest §3b-cond carriers: documented openness, literature citations,
  and in the third case a docstring recording a *prior* repair of exactly the
  degenerate `∃ inv, True` shape. Field count does not decide this.

## What is not established

- That the 27 FAILs are hard. See the direction note above.
- That the seven no-banner blocks are over-claims. One was read and is not.
- Anything about the 648 uninhabited classes beyond the count, which is not
  new here.

## Files

- `scripts/lean-class-hypothesis-vacuity-probe.py` (new)
- `scripts/lean-self-assuming-content-join.py` (new)
- `scripts/lean-self-assuming-audit.py` (detector fixes landed in `e674c94003`)

---

## Addendum 1 (same day) — the discriminator this should have used, and what it says

Two things were missed in the sections above, both found by following the
corpus-grep checklist *after* the fact rather than before.

### The corpus already sized this, and the number is 112, not 41

[`docs/audits/2026-08-30-sizing-the-self-assuming-projection-drain.md`](2026-08-30-sizing-the-self-assuming-projection-drain.md)
(bean `qou-z9ws`, completed) measures **112** self-assuming projections and
sizes them at ~102 independent fixes. The "41" above is not a correction of it
and is not a regression — **they count different populations**:

| | population | date |
|---|---|---|
| **112** | `proof-no-self-assuming-projection` verdicts adjudicated **`genuine`** in the vacuity review ledger, of 191 entries | 2026-08-30 |
| **41** | raw candidates `scripts/lean-self-assuming-audit.py` reports **today**, after the three detector fixes in `e674c94003` | 2026-09-07 |

Quote the number *with its population and its date*, or the next reader
reconciles a 2.7× gap that is not there.

### The discriminator: is the bundle ever BUILT?

That audit's test is sharper than anything used above — sharper than field
count, sharper than the banner regex — and it is the ledger's own:

> *"A projection like this is the legitimate Mathlib accessor idiom ONLY when
> something builds the bundle."*

An accessor on an inhabited structure exposes an axiom of a thing that exists.
An accessor on an uninhabited one exposes an axiom of a thing nobody has
produced. Applied to the eight paper-facing claims
(`scripts/lean-carrier-inhabited-check.py`):

| block | carrier | builders |
|---|---|---|
| `strong-multiplicativity` | `NoncommutativeFormalGroup` | **0** |
| `sw-period-residue-sum` | `SWPeriodResidue` | **0** |
| `flavor-dressed-mass-from-substrate-split` | `DressedMassSubstrateSplit` | **0** |
| `categorical-self-duality` | `CategoricalInstanton` | **0** |
| `categorical-jet-prolongation` | `CategoricalJetProlongation` | **0** |
| `jet-prolongation-C` | `JetProlongationQOU` | **0** |
| `electron-period-base` | `ElectronBaseTower` | **0** |
| `quantum-observable-universe-exists` | `QuantumObservableUniverseExistsContext` | **0** |

**All eight. So by the ledger's own rule, none of the eight is the legitimate
accessor idiom** — each is a paper claim of provable kind resting on a
hypothesis nothing in the corpus has ever witnessed. That is honest §3b-cond
*only where the block says so*, which is what this tranche repairs.

### Correcting the "honest §3b-cond carriers" claim above

The main audit says reading three single-field classes showed "honest §3b-cond
carriers" and that field count does not decide it. **The second half stands;
the first was a generalisation from an unmeasured sample.** Under the
inhabitation test the three split: `SkeinMultisetInvariant` has an instance,
`HasStrongDuality` has one, and `FiberAdjointInvolutionContext` has **none** —
its docstring says why, which is the honest form, but it is not the accessor
idiom. Two of three, not three of three.

### The detector that produced this table was wrong first, and the control caught it

The obvious line-anchored grep

    grep -E "^\s*(instance|def)[^:]*:\s*<Carrier>\b"

returns **zero for every carrier including the known-inhabited controls**,
because this corpus writes instance headers across four lines with the result
type last. That false zero points the *finding-shaped* way — it reports a
carrier as uninhabited, which is the interesting answer — and it was believed
for one tool call, until a positive control run on `SkeinMultisetInvariant`
(read by hand an hour earlier, so known to have an instance) came back empty.

`scripts/lean-carrier-inhabited-check.py` scans declarations, not lines, and
its `--selftest` fails unless all four known-inhabited carriers are found; it
also refuses to report at all if its built-in control goes missing. This is the
fifteenth-odd entry in the same taxonomy the convention work keeps adding to,
and the first one in this arc that was mine.

---

## Addendum 2 (same day) — census, not sample: 30 % of carriers ARE inhabited

The 2026-08-30 sizing audit applied the inhabitation discriminator to **12
sampled** declarations of 112, found 0 legitimate, and stated its own
uncertainty carefully:

> *"0 of 12 does not mean 0 of 112. By the rule of three, an observed zero in
> n=12 is consistent with a true legitimate rate up to roughly **25 %** at 95 %
> confidence."*

Checking one carrier is a few seconds, so the sample was never necessary.
`scripts/lean-self-assuming-carrier-census.py` runs the same discriminator over
**every** candidate the scanner currently reports:

    41 candidates over 37 distinct carriers
    inhabited 11   uninhabited 26   (30 % legitimate accessor idiom)

**Inhabited (11)** — `BorromeanQuark`, `ConvergenceBound`, `HasStrongDuality`,
`MatrixChainEqBuildChains`, `NobleGasMultiOperator`, `QFactRatioBound` (4
instances), `QIntRatioBoundSmall` (4), `ShellClosureMonotone`,
`SkeinMultisetInvariant`, `Term7ShellCorrectionClass`, `TheoremA`.

**That vindicates the earlier audit's caution rather than undercutting it.**
Its stated 25 % ceiling was well calibrated; the measured rate lands just past
it, and its sample's zero was simply not representative. Two cautions on
reading the two numbers together: the populations differ (its 112 are ledger
`genuine` verdicts as of 2026-08-30; these 41 are today's raw scanner
candidates), and inhabitation is necessary, not sufficient — `qou-z9ws`'s own
adjudicator separates `Fact`-wrapper and degenerate-slice instances from
substantive ones, and this census does not.

### The paper-facing subset is worse than the corpus average, not better

All **8** carriers behind the eight paper-facing claims are in the uninhabited
26. So:

| population | legitimate accessor idiom |
|---|---|
| all 37 carriers | 11 / 37 = **30 %** |
| the 8 backing a content block of provable kind | **0 / 8** |

The projections that reach the paper are exactly the ones with nothing behind
them. That is the finding this tranche exists for, and it is sharper stated as
a contrast than as an absolute.

---

## Addendum 3 (same day) — correcting my own "112", and why inhabitation alone cannot reproduce the ledger's verdicts

### The 112 is a 2026-08-30 figure and I quoted it as though it were current

Addendum 1 says *"the corpus already sized this, and the number is 112, not
41."* Both halves were dated correctly and the sentence still reads as a live
count. Measured today, `docs/audits/lean-vacuity-review-ledger.json` holds
**61** rows in `proof-no-self-assuming-projection`:

| verdict | count |
|---|---|
| `genuine` | **33** |
| `legit` | 14 |
| `needs-agent` | 14 |

So the drain since 2026-08-30 has taken the `genuine` population **112 → 33**.
Quote 33 as the live figure and 112 only with its date.

### Applying the discriminator to the ledger's own population

Of the 33 `genuine` rows: **9** name a declaration that no longer exists under
that name (repaired or renamed since), **5** have a proof body this resolver
cannot parse — it handles `:= ivar.field` and nothing else — and **19** resolve
to a carrier. Of those 19: **10 inhabited, 9 uninhabited.**

**That is NOT ten mis-adjudications, and reading it that way would be the
error this whole tranche is about.** `qou-z9ws` built an adjudicator precisely
because inhabitation is *necessary, not sufficient*, and it separates three
kinds of instance:

- **`Fact`-wrapper** — `instance … [hf : Fact P] : C … := ⟨hf.out⟩`. Supplies
  nothing; it relabels the assumption, and whoever must discharge `Fact P` is
  exactly where the gap already was.
- **degenerate slice** — inhabits only the diagonal (`f_k = f_inf`), where the
  bound reads `0 ≤ …` and closes by `positivity`, while the projected theorem
  quantifies over arbitrary arguments.
- **substantive** — instances covering the class's parameter domain.
  `QIntRatioBoundSmall`'s four discharge `m = 1,2,3,4` and the class binds
  `_hm4 : m ≤ 4`, so they **exhaust** it.

Only the third makes a projection legitimate. So the honest reading of 10/19 is
that **the cheap necessary condition does not reproduce the ledger's verdicts,
and the adjudicator is doing real work** — not that the verdicts are wrong.

### What this means for the numbers in Addendum 2

The 30 % there is a rate of *inhabitation*, an upper bound on the legitimate
rate, not the legitimate rate itself. The **0 / 8** on the paper-facing subset
is unaffected: an uninhabited carrier fails the necessary condition outright,
so no adjudication can rescue it. State it that way — the contrast is between
a bound and a certainty, and only the certainty carries the finding.

---

## Addendum 4 (same day) — the ledger's `needs-agent` backlog is 9/14 mechanically decidable

The 14 `needs-agent` rows in `proof-no-self-assuming-projection` are **not
unadjudicated**. Read one and the shape is clear:
`ConfinementPhaseStratification_open` carries a full written analysis
concluding *"On the merits it is the ordinary item-5 shape"* and
`stale_prev_verdict: "genuine"`. It is `needs-agent` because the **file sha
moved** — a verdict goes stale the moment the file changes, by design.

So draining them is re-verification, not adjudication: confirm the declaration
is byte-identical to what was reviewed, then restore the verdict. That is the
pattern the surviving `genuine` rows already use (*"RE-VERIFIED 2026-08-30 …
Declaration byte-identical against the recorded revision. Verdict
unchanged."*).

The inhabitation discriminator gives an **independent** second signal for most
of them:

| | count | what it means |
|---|---|---|
| **uninhabited carrier** | **9** | fails the necessary condition outright; no adjudication can rescue it, so a restored `genuine` needs only the byte-identity check |
| inhabited carrier | 2 | `shell_closure_monotone` (`ShellClosureMonotone`), `he4_strong_duality_value` (`HasHe4ChannelActiveSet`) — these need the real `qou-z9ws` adjudication: Fact-wrapper vs degenerate slice vs substantive |
| carrier unresolved | 3 | `ConfinementSDP`, `whitehead_volume_conjecture`, `four_term_pair_nucleon` — the resolver handles `:= ivar.field` and these are not that shape |

The nine uninhabited: `ConfinementPhaseStratification_open`,
`sdp_lp_projection`, `base_mass_is_norm_of_base_trace`,
`descended_trace_is_base_trace`, `jet_prolongation_C`,
`mass_anchor_stable_forward`, `mass_direction_sanity_forward`,
`bar_even_kernel_implies_direction_sanity`,
`bar_even_kernel_implies_radius_of_convergence`.

**Not drained here, deliberately.** Restoring a verdict writes a `file_sha`
and a dated reviewer block per entry, and the byte-identity check against each
recorded revision is per-entry work that should not be batched behind one
mechanical signal — the inhabitation result is a *second* witness, not a
substitute for the check the ledger's own contract asks for. It is a bounded,
well-specified next tranche, and this is what it costs: 9 re-verifications, 2
genuine adjudications, 3 resolver extensions.
