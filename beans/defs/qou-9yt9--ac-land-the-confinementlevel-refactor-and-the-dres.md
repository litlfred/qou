---
# qou-9yt9
title: 'A+C: land the ConfinementLevel refactor and the DressedParticle shadowing fix'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T09:08:06Z
updated_at: 2026-11-16T19:46:00Z
parent: qou-v2om
---

## Landed (A + C)

**A — ConfinementLevel refactor.** `level_canonical` deleted; `valid` is now a
parameter indexed by `BraidDatum` with `level_valid`/`level_min` as proof
fields. `unique` is a one-line theorem, `nonempty` a real `Nat.find`
construction, `level_eq_find` new. **No axioms at all** on all three — not even
`propext`. Registered in the axiom guard, exit 0.

Also repaired `prop:confinement-level-exists`, unplanned: its Lean backing was
the junk record `⟨0,1,0,0⟩`, proving the *type* inhabited rather than that any
braid has a level.

`.md` rewritten: its three stated reasons over-attributed — uniqueness needs
only antisymmetry, and neither monotonicity nor upward-closure does any work in
it. Both kept, correctly scoped.

**C — DressedParticle unshadowed.** The library had already done the refactor
its sibling called "pending" (`shell_on_bare`, `level_preserved` as proof
fields; `dressing_composes` proved from them). Sibling replaced by a witness
extract, matching the pattern `confinement-level-exists.lean` already used.

Axioms 136 → 134, flagged 21 → 19. All touched files lean-direct exit 0;
`check-sidecars` exit 0.

## Two traps recorded

1. **The root `.lake` olean tree precedes the paper's in `LEAN_PATH`**, so a
   `lean-direct-cone.sh` rebuild into the paper tree is INVISIBLE — the stale
   root copy shadows it. Three files reported spurious unknown-identifier errors
   until the paper tree was put first. Root olean 09:08:28 vs source 09:09:25 vs
   paper-tree olean 09:11:28.
2. **`check-sidecars.sh` prints `→ refresh` UNCONDITIONALLY** for every changed
   content-block `.lean` (line 107). It is an advisory reminder, not a staleness
   verdict, and it does not set the failure flag. I misread it as a failure for
   several turns; the discriminator is the `⚠` lines and the exit code.


## NINTH false axiom — `KnotOperatorEnergy.shadowPrice_canonical` (same class, refactored)

`climax-volume-mass/knot-operator-energy-unique.lean`. Plain structure with
`shadowPrice : R` free; the axiom asserted two records agreeing on
`partition` and `q` share it. Refuted by `⟨[],0,0,none⟩` vs `⟨[],0,1,none⟩`.
**Third docstring in this family to name its own defect** — *"requires ... a
structure refactor carrying the LP-canonicity as a proof field."*

Same three-way pattern as #7: false uniqueness axiom **plus** a junk-record
existence witness (`{partition := [1], q := 0, shadowPrice := 0}`), so
`prop:knot-operator-energy-exists` was vacuously backed too.

**Applied the owner's A ruling by analogy** — same defect class, and no library
counterpart exists (unlike #8), so the refactor was the only option that keeps
the claims. One design choice worth naming: the determining data is carried as
a **function** `dualValue : List ℕ → R → R` with `shadowPrice_eq`, NOT as a
relation with a uniqueness field. A structure carrying its own conclusion would
be the self-assuming projection AGENTS.md §3b-cond item 5 forbids; here
uniqueness follows from functionality.

The real content — that the LP dual exists and is unique (Schrijver §7.4) — now
sits explicitly in the `dualValue` parameter a caller supplies, instead of
being smuggled in by a witness that ignored its own indices.

Axioms 134 → 133, flagged 19 → 18. All three blocks lean-direct exit 0,
zero axioms; check-sidecars exit 0.

## The docstring sweep — a useful NEGATIVE

Grepping `"proof field" | "not free data" | "does not enforce"` across
`content/` returns 11 files; excluding Mathlib and the already-fixed ones, only
**one** new instance (this ninth). So this family is **three** — #7, #8, #9 —
not an open-ended class. That is a cheaper and far more specific detector than
the over-quantification rules, because it keys on the author having ALREADY
noticed the defect and written it down.


## The class surface (2026-09-07, PR #6987)

Two measurements, opposite directions, both new.

**Vacuity — clean negative.** `scripts/lean-class-hypothesis-vacuity-probe.py`
deletes the instance binder and asks Lean for the conclusion unaided:
**0 of 27 scored provable** (FAIL=27, SKIP=14, NOBASE=0). The same question on
the axiom surface found 8 of 112 (#6933). So the conditional-class surface is
not vacuous — its problem is visibility.

`NOBASE=0` is what makes that usable: every probe compiles the file UNCHANGED
first, since a red baseline fails in the direction that reads as "the class is
load-bearing". The 14 SKIPs are the explicit-structure-argument idiom, which
has no instance binder and is also the idiom that does not hide.

**Reach — 8 paper claims.** `scripts/lean-self-assuming-content-join.py` joins
the 41 self-assuming declarations against every `lean.ref` in `content/`:
8 blocks of provable kind (1 theorem, 6 propositions, 1 corollary, **zero
conjectures**); 7 carry no §3b-cond item-3 banner signal.

**Two of my own errors caught before shipping.** The join first said 9 — it
matched last name segments and paired `prop:quantum-universe-exists` with
`QuantumObservableUniverse.exists_instance`, two real distinct declarations.
And "14 single-field classes are item-5 violations" was too strong: reading
three shows honest §3b-cond carriers. Field count does not decide it.

**Nothing repaired**, deliberately. The banner column measures phrasing, not
honesty — `sw-period-residue-sum` scores NO BANNER over the most scrupulous
narrative in the set, and `prop:quantum-observable-universe-exists` turned out
to carry a worked narrative proof over four cited axiom lemmas.

Audit: `docs/audits/2026-09-07-self-assuming-projection-reaches-the-paper.md`

**Still open:** the opaque-operator disposition (now five, spanning
`IwahoriHeckeAPI.lean` and the vertex-algebra file) needs an author decision.
Follow-up tranche: read the seven no-banner blocks one at a time and add
§3b-cond item-3 banners where genuinely absent — a `.md` repair, not Lean.


## The banner tranche (2026-09-07, PR #7011)

Read the eight projection-backed paper claims one at a time. **Five repaired,
three deliberately left.**

**The discriminator the corpus already had, and I should have used first.**
`qou-z9ws` / `2026-08-30-sizing-the-self-assuming-projection-drain.md`: a
projection is the legitimate Mathlib accessor idiom ONLY when something BUILDS
the bundle. Measured on all eight carriers: **0 builders, every one**. So none
is the accessor idiom — each is a paper claim of provable kind resting on a
hypothesis nothing in the corpus has ever witnessed.

**41 vs 112 reconciled**, neither correcting the other: 112 = `genuine`
verdicts in the vacuity review ledger (of 191) on 2026-08-30; 41 = raw scanner
candidates today, post-`e674c94003`. Different populations, different dates.

**Repaired:** `thm:strong-multiplicativity` (the `.md` asserted, verbatim, the
claim its own Lean docstring says the accessor does not establish — seven
weeks side by side); `prop:categorical-self-duality` (and its Lean docstring's
`variational_einstein` pointer, which goes to the Einstein equation, not the
self-duality step — the Bogomolny derivation is narrative-only);
`prop:flavor-dressed-mass-from-substrate-split` (banner into the prose, since
`authorNotes` are render-skipped; plus the missing `uses[]` edge to
`lem:pair-skein-mass-formula`); `prop:electron-period-base` (`lean.ref`
retargeted to `second_period_contains_me`, which DERIVES the identity the
prose states); `cor:jet-prolongation-C`.

**Left alone, read in full:** `sw-period-residue-sum` (730 words, scrupulous),
`quantum-observable-universe-exists` (worked narrative proof in its `proofs:`
sibling), `categorical-jet-prolongation` (already bannered).

**My own detector was wrong first, in the flattering direction.** A
line-anchored inhabitation grep returns 0 for EVERY carrier including the
known-inhabited controls — this corpus writes instance headers across four
lines with the result type last — and a 0 reads as "uninhabited", the
interesting answer. Caught by a control on `SkeinMultisetInvariant`, read by
hand an hour earlier. `scripts/lean-carrier-inhabited-check.py` scans
declarations, and refuses to report if its control goes missing.


### Census + ledger triage (same tranche, PR #7011)

**Census replaces the sample.** `qou-z9ws` checked 12 of 112 and found 0
legitimate, stating a 25 % ceiling at 95 %. Checking a carrier takes seconds,
so: **41 candidates, 37 carriers, 11 inhabited / 26 uninhabited = 30 %.** Its
caution was well calibrated; its sample's zero was not representative.

**But 30 % is an UPPER BOUND, not the legitimate rate** — inhabitation is
necessary, not sufficient, and `qou-z9ws`'s adjudicator exists to separate
Fact-wrappers and degenerate slices from substantive instances. The **0/8** on
the paper-facing subset is untouched: an uninhabited carrier fails the
necessary condition outright.

**Corrected my own "112" → the live figure is 33.** The ledger holds 61 rows in
this category today: 33 `genuine`, 14 `legit`, 14 `needs-agent`.

**Bounded next tranche, costed.** The 14 `needs-agent` are re-verification, not
adjudication — they carry written analyses and `stale_prev_verdict: genuine`
and are pending only on a moved file sha. Split: **9 uninhabited** (restored
`genuine` needs only the byte-identity check), **2 inhabited**
(`shell_closure_monotone`, `he4_strong_duality_value` — real adjudication),
**3** the `:= ivar.field` resolver cannot reach.


### Ledger drain (PR #7036) — queue to zero, and my cost estimate was wrong in KIND

`proof-no-self-assuming-projection`: **41 genuine / 20 legit / 0 needs-agent.**

`file_sha` is `sha256(whole file)[:12]`, so any edit anywhere expires every
verdict in the file. `scripts/lean-vacuity-ledger-reverify.py` compares the
DECLARATION at the recorded revision against HEAD: **14/14 IDENTICAL**, 0
changed. Every expiry was collateral, so all fourteen prior readings are
restored with a dated RE-VERIFIED line.

**I costed this at 9 + 2 + 3 and it was none of those.** The inhabitation
signal was the wrong tool: the question was never "what is the verdict" but
"does the old verdict still apply".

**Tension flagged, not overturned.** Four restored `legit` verdicts sit on
carriers with ZERO builders (`sdp_lp_projection`, both `CatDescendedInputs`
ones, `jet_prolongation_C`) while qou-z9ws's rule says legitimate ONLY when
something builds the bundle. One-directional: `genuine` on an inhabited carrier
is fine (necessary, not sufficient); `legit` on an uninhabited one is not.

**Author decision, framed in Addendum 5** with options/costs/risks and a
default: does the discriminator apply to a DEFINITIONAL structure at all?
`jet_prolongation_C`'s docstring makes the `Group.mul_assoc` case; the reply is
that `Group` has instances and `JetProlongationQOU` has none. Default if
nothing is decided: the flags stay and nothing moves. My judgement: narrow the
rule to hypothesis carriers — but it changes another agent's measured
criterion, so it is not mine to make.


## HeckeAnyonicSubstrate — both carriers closed (PR #7357, 2026-09-14)

`proof-claims-unencoded` **9 -> 7**; `total_defects` 70 -> 68; review ledger 321 -> 319.
Grepping the audit run for `HeckeAnyonic` now returns nothing.

**Four defects, two of them not in the ledger.**

1. Library `heckeQuadratic : Prop` — ENCODED from the block's own displayed
   equation `(T_{s_i} - q)(T_{s_i} + 1) = 0`, and CONSUMED by
   `braidAction_injective` (first reader of the field in the corpus).
   `NormalForm` gained `AddCommGroup`/`Module R` instance fields, which the
   field's own docstring had already named as the blocker.
2. **The `.ts` lean.ref pointed at a DELETED declaration.** Not flagged
   anywhere. `qou:QOU.IwahoriHecke.Tw.HeckeAnyonicSubstrate` was removed
   2026-09-05 by the `qou-k4oq` retraction; the manifest was never updated.
3. Content stub deleted (§0a shadowing stub) — also the same-namespace
   duplicate the sibling-divergence audit reports.
4. File header enumerated "observation-functor compatibility", which no field
   carries and none ever did. Corrected (it CANNOT be encoded here — no tau);
   the content lives at `KazhdanLusztigClassicalLimit.kl_compatible_with_tau`.

**2 and 3 hid each other.** Ref resolution checks the SIBLING FIRST, so the
dangling ref resolved to the stub beside it and validation stayed green.
Neither is visible while the other is present — worth remembering as a shape.

**Left open, deliberately (author's call, not mine).** The class is STILL
satisfiable by a degenerate model (`zeroQCounterModel` at q=0; `PUnit` at any
q, already in local/lean-generation). Encoding more fields will not change it:
the conjecture's content is EXHAUSTION, and exhaustion cannot be stated by a
class whose INSTANCE chooses `NormalForm`. Fixing it means making
`NormalForm`/`braidAction` caller-supplied parameters — the `DimMasterPentagon`
shape from #6671 — a class-arity change reaching `KazhdanLusztigClassicalLimit`,
`RootOfUnityMTCTruncation` and `lusztig-canonical-basis-q-eq-1`.

**Two TRAPs measured this session, both about the tooling, not the corpus:**

- `lean-shadow-verify.sh` keys staleness on the source's GIT COMMIT DATE, so it
  CANNOT see uncommitted work. My first run reported `rebuild=0` and 3x EXIT=0
  against the OLD olean — a false green on the file I was editing. Commit
  first, then sweep; `rebuild=N>0` is the signal the run means anything.
- The vacuity ledger does NOT self-prune, though
  `local/lean-proof-vacuity-audit` says it does. After the fix,
  `--review-ledger` left both keys and did not write the file;
  `--check-ledger` exits 0 with an entry pointing at a DELETED path. The last
  shrink (350 -> 321) was an explicit `33 deleted` commit. Prune by hand.

**Remaining 7:** HadronFibreEmbedding, DegreeZeroDatum, RungRule,
TransferMatrixEigenphase (ledger `legit` — leave), KnotOperator,
BringPeriodSublattice, TannakaKreinReconstruction.

## BringPeriodSublattice / magic-numbers-bring (PR #7359, 2026-09-14)

`proof-claims-unencoded` **9 -> 8** on main's base (the 8 still holds BOTH
HeckeAnyonicSubstrate carriers, fixed on #7357 and not yet in main). Combined
once both land: **6**.

**The ledger flagged the SMALLER half again.** It flags
`structure BringPeriodSublattice`'s two universe-`Prop` fields
(`s5_stable`, `tau_stable`). The bigger defect was unflagged:
**`MagicNumbersBring` is declared TWICE with different fields and OPPOSITE
dispositions** —

- library `QOU/Conjectures/MagicNumbersBring.lean` (`QOU.Conjectures`):
  no instance, with a standing comment explaining that the identity model
  `magicLattice n := n` "discharges rank_eq_magic by rfl for ANY set of
  naturals ... captures none of the conjecture's content";
- content sibling (`QOU.AlgebraicSubstrate`): a global
  `instance canonical` that IS that identity model (`rank := n`,
  `s5_stable := True`, `tau_stable := True`).

So one file declared the conjecture open and the file beside it closed it
using the construction the first one names and rejects. Deleted the sibling
(§0a shadowing stub + §3b-tax fabricated instance), repointed the ref to
`qou:QOU.Conjectures.MagicNumbersBring`. Zero consumers of
`ranks_match_magic_set` / `BringPeriodSublattice` / the sibling `magicSet`.

**PATTERN, now twice in two carriers — worth expecting on the rest.** In both
HeckeAnyonicSubstrate and this one, the ledger-flagged bare-`Prop` field was
accompanied by a LARGER unflagged defect in the same file: a dangling
`lean.ref` there, a fabricated instance here. The detector keys on field
types and cannot see either. **When you open a flagged carrier, read the whole
file and its `.ts`/`.jsonld`, not just the flagged field.**

**Also: `ranks_match_magic_set` was vacuous independently of the class** —
`exists L, L.rank = n` is satisfied by `<n, True, True>` for every n,
because `rank` is a free `Nat` field. A conditional theorem can be vacuous
for a reason that has nothing to do with the conjecture it cites.

**Branch hygiene note:** I cut this branch from the HeckeAnyonicSubstrate
branch by mistake, so #7359 initially carried #7357's six commits.
Rebased `--onto origin/main` and force-pushed before any review. Check
`git diff --name-only origin/main...HEAD` after `git checkout -b`.

**Remaining 6** (post-both-merges): HadronFibreEmbedding, DegreeZeroDatum,
RungRule, TransferMatrixEigenphase (ledger `legit` — leave), KnotOperator,
TannakaKreinReconstruction.


## KnotOperator / universal-ilp-algorithm (PR #7359, 2026-09-14)

`proof-claims-unencoded` **8 -> 7** on this branch (PR running total 9 -> 7;
combined with #7357 once both land: **5**).

**THIRD time the flagged field was the smaller half.** And this one shows why
"is the field consumed?" is the WRONG test: `is_knot : Prop` WAS read —
`universal_ilp` had `K.is_knot AND ...` — but reading a field whose value the
CONSTRUCTOR picked constrains nothing. Parameterised it
(`IsSingleComponent` caller-supplied) and proved the structure refutable:
`knotOperator_isEmpty_of_never_single_component`.

**The larger unflagged half: `gram_matrix` is the ZERO matrix**, so
`frobenius_positive` is `0 >= 0` and the whole LP predicate holds of every
operator. Its docstring already SAID this and nothing checked it; now
`universal_ilp_holds_of_zero_gram` proves it, so it stops compiling the moment
a real Gram lands.

**Corpus correction while there:** that docstring called the intended
Halverson-Ram Gram "sharper". Under convention D it is SINGULAR —
`mass-theory/frobenius-gram-matrix`: `y_(1^3) = 0` symbolically, the (1^3)
block IS the radical, `det G = 0` exactly, `G_INV` gone and `G_PINV` on
`H_3(q)/rad` in its place. **NOT wired** — `frobenius_positive` over a rank-5
form is a different condition and the radical's treatment is a modelling
choice. Author's call.

**Remaining 5** (post-both-merges): HadronFibreEmbedding, DegreeZeroDatum,
RungRule, TransferMatrixEigenphase (ledger `legit` — leave),
TannakaKreinReconstruction.

## HadronFibreEmbedding (PR #7360, 2026-09-14) — the ledger said FIXED and it was not

`proof-claims-unencoded` **9 -> 8** on main's base. With all three PRs landed: **4**.

**A ledger entry saying `FIXED` is not evidence the carrier is clean.** This
entry read `FIXED 2026-09-07` / `dead-field-removed` and the carrier kept
tripping the audit — because that fix removed one of **TWO** universe-`Prop`
fields and kept the other. **Trust the audit run, not the ledger verdict.**

**Why it kept `confined`: a NAME COLLISION.** The docstring recorded
"`confined` is kept: it is read by four declarations". Re-measured, those four
read a DIFFERENT `confined`:
- `DownQuark.confined` / `UpQuark.confined` are **Bool** (`= true := rfl`);
- `ConfinedParticle.confined` / `ConfinementPhaseStratification.confined` are
  applied to a parameter (`h.confined q`) — functions on another carrier;
- `confinedNet` is a different name again;
- and the standalone `confined` predicate was itself removed 2026-09-02 for
  being `fun _ _ => True`.

**Zero** `.confined` projections on a `HadronFibreEmbedding`, **zero**
`confined :=` sites. Dead. Removed.

**Two lessons, and this carrier failed BOTH ways at once:**
1. **A field name is not an identifier** — resolve a "who reads this?" claim to
   the DECLARATION, not the token. Same hazard AGENTS.md records for
   `markovZ`.
2. **Consumption is not the test anyway** (established on `KnotOperator`): a
   universe-`Prop` field is chosen by the constructor, so a genuine reader
   still gets no constraint.

Both docstrings corrected: with both Prop fields gone the structure is pure
data and encodes NONE of the four conditions it advertises.

**Remaining 3** (post-all-three-merges): DegreeZeroDatum, RungRule,
TannakaKreinReconstruction. (`TransferMatrixEigenphase` is ledger `legit`.)


## DegreeZeroDatum (PR #7360, 2026-09-14) — the capstone proved nothing, and I was wrong about it

`proof-claims-unencoded` **9 -> 7** on this branch. With all three PRs landed: **3**.

**I had called this carrier "a legitimate use". The ledger was right; I was
wrong.** Machine-checked before touching it:

    example : exists d : DegreeZeroDatum, Inaccessible d :=
      horizon_nonempty { formallyProvable := False, extractSteps := fun n => n }
        not_false          -- compiled, exit 0

The capstone headline — "a Turing-complete substrate necessarily hosts a region
where degree-0 truth is inaccessible" — was proved by DEFINING a datum whose
provability proposition is literally False. The structure carried no datum at
all, only a Prop and a step-count, so there was nothing for provability to be
ABOUT.

**Why the wrong reading is tempting, and this is the transferable part:** the
theorems DO take `not provable` as an explicit hypothesis, which LOOKS properly
conditional. But a hypothesis about a constructor-chosen proposition is free to
discharge. **A conditional-looking signature is not evidence of conditionality
when the antecedent mentions a universe-Prop field.**

Parameterised over a caller-supplied Datum + FormallyProvable; added
`not_inaccessible_of_all_provable` for refutability.

## TRAP (new, distinct from the commit-date one): a probe that IMPORTS the file you changed

Run before committing, my two probes returned exit 0 and exit 1 — **both
backwards** — because they compiled against the stale olean. I caught it ONLY
because I had written the expected exit codes down first.

And `lean-shadow-verify.sh` reports `rebuild=0` even post-commit for a target
module: it compiles the TARGET fresh and rebuilds only its DEPENDENCIES into
the shadow. A probe that imports the target still gets the stale olean.

**Recipe that works** (real tree untouched, 2876 -> 2876 oleans):
1. `cp -al <paper>/.lake/build/lib/lean $SHADOW`  (COMPLETE, not sparse — Lean
   resolves a package from the first LEAN_PATH root holding it);
2. `rm -f $SHADOW/<Mod>.olean` then `lean ... -o $SHADOW/<Mod>.olean`  (unlink
   first, or the hardlink writes through into the real tree);
3. prepend $SHADOW to LEAN_PATH with the real paper root removed;
4. run the probes.

**Write down the expected exit code BEFORE running a verification probe.** It
is the only thing that distinguished a real result from a stale-olean artifact
here.

**Remaining 2** (post-all-three-merges): RungRule, TannakaKreinReconstruction.
(TransferMatrixEigenphase is ledger `legit`.)


## RungRule (PR #7360, 2026-09-14) — the property is NOT expressible in Lean

`proof-claims-unencoded` **9 -> 6** on this branch. With all three PRs: **2**.

`substrate_derived : Prop` was dead (written once as `True` by
`depthBasedRule`, read nowhere). But the interesting part is WHY it was
removed rather than parameterised:

**Its stated property — "the rule does not directly reference any real-valued
AME constant" — is a claim about how `k` is DEFINED, not about `k` as a
function.** Two extensionally equal functions differ in provenance; Lean sees
only the extension. So neither a field NOR a caller-supplied predicate on `k`
can carry it. Parameterising would have produced a different, weaker property
wearing the same name.

**Generalisable test before reaching for the parameterise hammer: is the
property EXTENSIONAL?** If it is about the definition/provenance/syntax rather
than the value, no Lean encoding exists and the honest home is a source audit.
This corpus already runs that shape — `scripts/precision-gates.sh` carries a
no-free-parameter certificate. Recorded in the docstring so nobody "restores"
the field.

**Scope discipline, stated for consistency:** removal keeps `RungRule n`s
arity, so `DeltaLambda`, `DeuteronVerification` and `CrystalDeltaLambdaScaffold`
are untouched. Parameterising would have reached all three — which is exactly
why I DECLINED to parameterise `HeckeAnyonicSubstrate` on #7357. Same boundary,
applied the same way: in-file removal of a measured-dead field is corpus-derived
(the `HadronFibreEmbedding` precedent); a 3-consumer arity change is the
authors call.

Consumers verified, not assumed: shadow sweep `rebuild=3`, 3x EXIT=0.

**Remaining 1**: TannakaKreinReconstruction. (TransferMatrixEigenphase is
ledger `legit` and stays.)


## TannakaKreinReconstruction (PR #7360, 2026-09-14) — I predicted wrong, and the LEDGER was the defect

`proof-claims-unencoded` **9 -> 5** on this branch. With all three PRs: **1**
(TransferMatrixEigenphase, ledger `legit`, stays).

**I predicted this would follow the arc pattern (flagged field = smaller half).
It does not.** This file had already had a careful honesty pass; the ledger was
wrong about it.

**The verdict describes a field that no longer exists.** Prior evidence names
TWO fields — "monoidal_equiv, universal_property are typed with the UNIVERSE
Prop". Commit 21bac468c6 had already replaced monoidal_equiv with
`equiv : C = RepCat` (real DATA, a CategoryTheory.Equivalence) and renamed it so
name and type agree.

**TRAP — a ledger re-verification can RESTORE a verdict older than the sha it
checks against:**

    adjudication reviewed_at   2026-09-07T09:55:00Z
    commit 21bac468c6          2026-09-07T19:24:51Z    <- 9.5 HOURS LATER

`file_sha` records 21bac468c6. `lean-vacuity-ledger-reverify.py` compares the
declaration against that sha — post-fix vs post-fix — reports IDENTICAL, and
restores a PRE-fix verdict saying "the prior reading applies unchanged".
**Cheap invariant it could check: `reviewed_at` >= commit-time-of(file_sha).**
Reported, not fixed (someone elses tool).

**Combined with the HadronFibreEmbedding finding, the ledger is now known
unreliable in BOTH directions**: a `FIXED` verdict that was not (HFE), and a
`genuine` verdict on an already-fixed carrier (TK). **Trust the audit run.**

**Disposition: `@marker`, not a code change.** The remaining field asserts
terminality over factorisations through Hopf-algebra representation categories.
VERIFIED not assumed: Mathlib `RepresentationTheory.Rep` is
`abbrev Rep (k G : Type u) [Ring k] [Monoid G]` — a MONOID. No `Rep k H` for a
Hopf algebra to quantify over; also why `RepCat` is a carried field. So the
justification is correct. Applied the AGENTS.md 3b-tax `@marker` opt-out; audit
row moves MAJOR -> EXEMPT. Ledger re-adjudicated genuine -> legit (not pruned:
the candidate still exists, now exempt).

NOT laundering under 1a: the field is unchanged and no less open; `@marker`
makes an already-written justification machine-readable. Audit label: "honestly
framed; tracked not counted".

SCOPE: verified Mathlib Rep needs [Monoid G]; did NOT exhaustively establish
that no other Mathlib route states terminality.

**qou-9yt9 proof-claims-unencoded arc is now COMPLETE** at 1 remaining, which
is ledger-`legit` and correctly stays.


## MEASURED: 52 of 318 ledger verdicts predate the revision they cite (2026-09-14)

New script `scripts/lean-vacuity-ledger-freshness-audit.py`. MEASUREMENT ONLY —
the re-verify tool is not changed and the ledger is not edited.

Invariant: `reviewed_at >= authored-time of the earliest revision whose content
hashes to file_sha`. A verdict cannot have been made against a revision that did
not yet exist.

    entries                                     318
      invariant holds                            92
      STALE (verdict predates its own sha)       52    <- 34 genuine, 16 legit, 2 advisory
      file_sha matches no revision                0
      no reviewed_at (freshness uncheckable)    174

Lead times reach **645 hours (27 days)**. The **174 undated** entries are a
second, larger gap: `--check-ledger` cannot assess freshness on 55% of the
ledger at all.

**Two confounds ruled out, not assumed:**
1. Rebase-merge (rule 8) rewrites COMMITTER dates and would manufacture exactly
   this signature. Measured both ways — committer and author dates give
   IDENTICAL counts (92/52/174). Script uses author date regardless.
2. Content oscillation — `git log` is newest-first, so naive keying dates a hash
   by its NEWEST occurrence. Script keeps the EARLIEST. Same counts.

Hash convention confirmed against a known case first: sha256(blob)[:12] of the
file at 21bac468c6 is exactly f5b88ba3250d.

**OPEN DECISION (owner).** Whether `lean-vacuity-ledger-reverify.py` should
enforce this invariant, and what to do with the 52 + 174. Not taken here — it is
someone elses tool and a re-adjudication sweep is a change, not a measurement.


## Sibling coordination with #7361 — verified non-collision (2026-09-14)

A different agent's PR #7361 (`claude/vh1o-second-arm-verdicts-2026-09-14`) widens the
audit script's second `exempt_reason` arm (`"derivation pending"` alongside
`"triage pending"`) and writes 13 adjudications. It flagged possible overlap on all
three of my PRs. **Measured, both directions, no collision:**

1. **Its arm-widening cannot un-exempt my `@marker`.** Two independent mechanisms in
   `content/pipeline/lean-vacuity-axiom-audit.ts`: `MARKER_OPT_OUT` (line 2053) suppresses
   at *detection*; `LEDGER_TRACKED_EXEMPT` (line 1724) — the widened arm — governs
   ledger-seeding of an *already-emitted* candidate. A `@marker` candidate never reaches
   the second gate. Doubly safe: my TannakaKrein verdict is `legit`, and only `genuine`
   promotes under their change.
2. **Ledger writes are disjoint.** Diffed their ledger against `origin/main`: 13 entries
   added/changed, **0** touching my four carriers. Theirs are the q-NS / vortex /
   root-of-unity / cosimplicial family; mine are the seven `Prop`-carrier keys. Clean union.

Replied once on #7361 with the measurement and the merge protocol (re-run the audit,
never hand-merge the generated witness).

**One stale figure left uncorrected, deliberately.** My own auto-`/coordinate` comment on
#7357 quotes the combined `proof-claims-unencoded` residual as **4**; it is now **1**
(TannakaKrein closed afterwards). The three PR bodies — the read-first durable artifacts —
carry the live figures, so three correction comments would be noise.


## ARC LANDED — all three PRs merged 2026-09-14, and the predicted figure held exactly

Owner gave the merge word; #7357, #7359, #7360 are on `main` as `42f9215581`,
`a73425a3f4`, `d45e2686ce`.

**`proof-claims-unencoded` 9 → 1**, verified by running the audit **on `main` itself**
after merging rather than trusting the pre-merge runs. The surviving 1 is
`TransferMatrixEigenphase` (`QOU/QBeta/EigenphaseCarrierVacuity.lean`), verdict `legit` —
the exact declaration all three PR bodies named as the one that correctly stays.
`--check-ledger` exit 0. Main's committed witness reproduces byte-for-byte apart from
`generated` and `scanned_files 3854 → 3856` (two `.lean` landed between the run and the
merge); every substantive count identical, so no follow-up commit.

### Four things worth carrying, none of them the count

**1. A branch that merged `main` in cannot be rebase-merged.** GitHub returns
`405 This branch can't be rebased`. Rule 8's remaining options are squash — forbidden
without explicit per-PR permission — and a merge commit, the documented exception. Merge
commits were used for all three, which preserves the per-cluster commits rule 8 exists to
protect. **Merge permission is not method permission**; say which you used and why.

**2. Each merge conflicted the next, and the ledger union held every time.** Resolution
was identical three times: three-way diff against the merge base with a HARD ASSERTION of
zero intersection in del/del, mod/mod, ourmod/theirdel, ourdel/theirmod and add/add, then
apply ours onto theirs. 330 → 328 → 325. The assertion never fired — but it is what makes
the union a verification rather than a hope, and it is cheap.

**3. A new conflict class: the shared bean itself.** #7359 and #7360 both conflicted on
THIS file, because #7357 carried its own appends into `main` first. Resolved as a
chronological append-union (theirs, then ours), with the section list printed and checked
after each resolve — 16 sections, none dropped. `scripts/bean-append-merge.py` exists for
this but is on the unmerged #7350, so it was done by hand.

**4. The audit dirties a witness that is not yours.** Every run of
`lean-vacuity-axiom-audit.ts` rewrites `computations/witness-raw-float64-audit.witness.json`
(ratchet 981 → 978 dirty). That is another arc's drain — restore it, never commit it. A
blanket `git checkout -- computations/` was safe ONLY because these branches own nothing
there, confirmed before each use; on a branch that owns files there it deletes them.

### Status: this bean stays IN-PROGRESS

The three PRs are landed and verified, but this bean is a long-running arc covering more
than them, and two decisions raised during the arc are still open and recorded on
`qou-a30t` (another agent's bean, deliberately not taken over):

- **(a)** the ledger-freshness invariant `reviewed_at >= commit-time(file_sha)` — 52 of 318
  verdicts predate the revision they cite, 174 carry no `reviewed_at` at all;
- **(b)** the two `QHookBound` verdicts — my recommendation to flip them to `legit` is
  **WITHDRAWN**, after measuring that `QFactRatioBound`'s index is unbounded with instances
  only to `k = 3`.

Neither is enacted. Closing this bean would bury both.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


---

## Round 47 Progress (`lane-e925`, 2026-11-16 — PR #8154)

- **PR:** [litlfred/qou#8154](https://github.com/litlfred/qou/pull/8154) (`ffb527fcd5e3aac0c7b00570fecb3e6dded50749`), signed `ready: ffb527fcd5e3aac0c7b00570fecb3e6dded50749` ([comment](https://github.com/litlfred/qou/pull/8154#issuecomment-6925680171)).
- **New sorry-free Lean 4 module `folio/quantum-observable-universe/lean/QOU/BraidKnot/ConfinementLevelFiltration.lean`:**
  - Formalises anti-monotonicity (`FiltrationMinLevel.le_of_imp`) and equivalence invariance (`FiltrationMinLevel.eq_of_iff`) of the minimum valid `ConfinementLevel` under filtration inclusion ($V_1 \subseteq V_2 \implies \ell_{\min}(V_2) \le \ell_{\min}(V_1)$), upward-closure characterisation (`FiltrationMinLevel.valid_iff_level_le`), functional-parameter shadow-price uniqueness (`IndexedShadowPrice.shadowPrice_unique`) vs the explicit counterexample for an unconstrained field (`unconstrainedShadowPrice_not_canonical`), and multi-step `DressedParticle` shell-chain level invariance (`LevelPreservingChain.level_eq`).
- **Wired all orphaned sorry-free arc modules into `folio/quantum-observable-universe/lean/QOU.lean`:**
  - Added `QOU.Information.GeometryOfIncompleteness`, `QOU.OptionE.RungSelection`, `QOU.BraidKnot.HeckeAnyonicSubstrate`, and `QOU.BraidKnot.ConfinementLevelFiltration` to `QOU.lean` so all 12 modules in the `ConfinementLevel` / `DressedParticle` arc are reachable from the top-level umbrella and verified 100% sorry-free and axiom-free (`qou_9yt9_all_12_modules_sorry_and_axiom_free` and `qou_9yt9_all_12_modules_wired_in_QOU_umbrella` PASS).
