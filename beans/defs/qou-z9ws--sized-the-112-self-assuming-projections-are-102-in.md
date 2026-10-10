---
# qou-z9ws
title: 'SIZED: the 112 self-assuming projections are ~102 independent defects, not one systemic pattern'
status: completed
type: task
priority: normal
created_at: 2026-08-30T13:41:46Z
updated_at: 2026-10-10T10:30:38Z
---

Full measurement: docs/audits/2026-08-30-sizing-the-self-assuming-projection-drain.md

## Ratio — 0 of 12 legitimate

Sampled 12 of the 112 `genuine` `proof-no-self-assuming-projection` entries,
deterministic and evenly spaced (indices 0,9,18,28,37,46,56,65,74,84,93,102).
Applied the ledger's own discriminator: a projection is the legitimate Mathlib
accessor idiom ONLY when something builds the bundle.

**Every sampled bundle is uninhabited.** All 12 adjudications stand; the prior
agent was right on this sample.

Uncertainty stated rather than hidden: 0/12 is consistent with a true legitimate
rate up to ~25% (rule of three, 95%). The sample rules out the category being
mostly noise; it does not rule out a dozen or two legitimate cases in the rest.

## Two detectors disagreed on 2 of 12, and BOTH were wrong

- one called `DemazureFiberMarkovTraceContext` inhabited at
  demazure_fiber_markov_trace.lean:95 -- that line is the FLAGGED DECLARATION,
  `def ... [ctx : ...] : ... := ⟨ctx.claim_i..., ctx.claim_ii..., ...⟩`, matched
  because `Foo :=` appeared on it;
- the other called `DirectionSanityGateClass` inhabited at
  q-beta-direction-sanity-gate.lean:99 -- that is
  `theorem ... : ¬ DirectionSanityGateClass m`, a REFUTATION, matched by a
  "bundle in the conclusion" rule.

Resolved by reading the source. A producer search that cannot separate a
constructor from a consumer or a negation is not evidence, and this category is
precisely where that distinction lives.

## Sizing — ~102 independent fixes, not one pattern

Measured over all 112:

  distinct bundle types            102
  bundles appearing exactly once    95
  most-repeated bundle               3   (RMatrixBraidingContext)
  bodies projecting a field         90
  bodies with no visible projection 21
  projections onto `claim*` fields  66

The NAMING is systemic -- two-thirds land on `claim_i/ii/iii`-style fields, the
§3b-cond item-5 shape -- but those fields belong to 102 different context
classes, 95 of them singletons. There is no shared structure to fix once.

## Verdict: week-shaped, not session-shaped

The recorded disposition is "construct a witness instance and prove the property
there, or drop the pseudo-theorem". Constructing a witness means supplying the
mathematics the context class stood in for, and for several
(KnotOperatorSelectionContext, HoefsmitScatteringPipelineContext,
NucleonOrderingFactorizationContext) that IS the open research. Dropping is
cheap per case but changes what the block claims, so it is authorial each time.
The binding constraint is per-case judgement across ~102 unrelated contexts.

## Cheaper decompositions, if wanted

- The 21 bodies with NO visible projection are a different sub-shape, not
  characterised here; possibly smaller and more uniform. Measure before the 90.
- The 7 bundles occurring more than once are the only places one fix covers more
  than one defect.

## Follow-up: both leads worked. One was my own regex.

**RETRACTED — the "21 no-visible-projection bodies" is not a sub-shape.** That
count came from a body scan keyed on a hard-coded instance-name list
(`ctx|inst|h|hC|c|s|dl|kec|hi|self`). Against ANY `identifier.field`, **19 of
21 project**; they bind the instance as `d`, `hZ`, `hT`, `dc`, `hyp`, `fac`,
`jgcs`, `hArg`, `lpd`, `chart` etc. No sub-shape, no cheaper decomposition, and
the recommendation to measure it first is withdrawn. Same failure mode as the
two producer detectors: a name-keyed pattern reporting absence where it had only
failed to look.

**The 2 genuinely different ones:**

- `structurallyValidBinding_necessary` — a pure tautology
  `(h : ¬P) : ¬P := h_invalid`, `id` under a name promising a necessity result.
  **FIXED**, removed, header corrected, lean-direct exit 0. Determinate for
  three reasons: the file's own `withinLengthBound` one declaration earlier
  records replacing exactly this shape; the predicate already has a canonical
  name (`BraidWord.structurallyValidBinding`, conj-canonical-knot-id-sdp.lean:156,
  ~20 use sites, identical body); and nothing consumed it — the header's only
  related entry named `structurallyValidBinding_necessary_for_canonical`, which
  does not exist and never did, now corrected.
- `whitehead_volume_conjecture` — NOT a hidden defect. Docstring accurate, the
  unconditional proof is real at WhiteheadSaddleClausen.lean:731 (namespace
  QOU.Knot.WhiteheadSaddle — filename differs from namespace, which is correct,
  not a dead ref), base file is Mathlib-only, port tracked in `qou-1gkf`.

**The 7 repeated bundles: 15 declarations, all 7 uninhabited, so all 15
genuine.** Hand-verified total now **27 of 112, still 0 legitimate**, which
tightens the rule-of-three bound on the legitimate rate from ~25% to ~11%. The
saving from shared fixes is 8 fewer independent fixes out of 112 — it does not
change the week-shaped verdict.

**New finding.** `RMatrixBraidingContext` and `r_matrix_braiding_structure` are
each declared TWICE in namespace `QOU.Braiding`:
braids-and-knots/r-matrix-braiding-structure.lean (153 lines, strict superset —
adds Rcheck1/Rcheck2/claim_braid_relation/braid_rep_from_R_check) and
lean/QOU/Braiding/r_matrix_braiding_structure.lean (65 lines, the subset). The
sibling's header calls the latter "the build-graph copy" — but NOTHING imports
it, and QOU.lean imports six other QOU.Braiding.* modules and not this one
(grep -c = 0). The stated rationale for the mirror does not hold. Authorial:
drop the unimported subset, or add it to the umbrella and have the sibling
reference rather than restate. Not done — it changes what
prop:r-matrix-braiding-structure resolves to under the §0a sibling-first rule.

Ledger 372 -> 371 (the removed tautology is no longer a candidate); gate exit 0,
all 162 candidates carry a fresh verdict.

## Drain batch 1 — 7 removed, and a near-miss worth recording

Removed 7 self-assuming projections from 6 library files (no `.md`/`.ts`
sibling, so nothing but the agent checks them), each with **zero references
anywhere in the corpus** including its own file:

  BranchingConvergence      branching_convergence            := hi.bound
  QHookBound                convergence_rate                 := hi.bound
  QHookBound                wedderburn_weight_perturbation   := hi.bound
  SkewSYT                   knot_invariant_convergence       := hi.bound
  Cl3Zeta5PslqIndependence  pslq_independence                := ctx.claim_pslq_independence
  KnotIndexedConvolutionGrid grid_placement                  := ctx.claim_placement_well_defined
  QHeckeSeminormalCharacterClosure character_closure_holds   := ctx.claim_paths_agree

Content is not lost: it stays in the class field each projected, which asserts
the same proposition under the same hypotheses. Only the restatement goes —
the ledger's own recorded disposition, with no use sites to update.

Genuine `proof-no-self-assuming-projection` 111 -> 103.

## 🛑 TRAP: my first attempt destroyed 767 lines and I nearly shipped it

The bulk edit used a regex `<decl>[\s\S]*?:=[^\n]*\n` to find "the declaration
and its term body". Non-greedy still runs to the FIRST `:=` after the match
start, and when the docstring-anchored start landed earlier in the file than
intended it swallowed everything in between. On `QHookBound.lean` that deleted
**767 lines** — `qIntReal`, `qIntReal_eq_canonical`, `qInt_pos`,
`qInt_ratio_bound_m2` and more, all real proofs — while reporting a cheerful
"removed convergence_rate".

Caught only because the follow-up `grep` for the second declaration came back
EMPTY, which was inconsistent with the script's own success message. Reverted
with `git checkout --`; nothing was committed or pushed.

**The rule this establishes for any bulk Lean edit:** never delimit a
declaration by regex-to-the-next-token. Delimit by LINES, ending at the next
column-0 top-level construct (`/--`, `/-!`, `@[`, `theorem`, `def`, `end`, …),
and put a SIZE GUARD on it. The rewritten extractor aborts above 60 lines; the
seven real spans measured 7-13 lines each, so the guard has three-sigma of
headroom and would have caught the 767-line span instantly.

Second-order lesson: a script that reports success is not evidence it did what
you meant. `git diff --stat` before committing is what should have been the
first check, not the last.

## And the gate caught a second slip

After the removals, three UNTOUCHED declarations in the same two files went
stale (the ledger keys freshness on the whole file hash). I refreshed their
`file_sha`, `reviewed_at`, `reviewer` and `evidence` — the evidence text
literally says *"It remains a `genuine` field-projection"* — and never set the
`verdict` field, leaving them `needs-agent`. The gate failed, correctly, twice
in a row until I read the entry rather than my own intention.

Their bodies were verified byte-identical to `origin/main` before refreshing.

## Batch 3 — the mechanical class is now EMPTY. Drain closed at 112 -> 90.

Removed the last three library zero-reference projections:

  markov_gns_embedding          ⟨inst.repr, inst.repr_add, inst.repr_mul, inst.repr_faithful⟩
  adjoint_vanishing_propagation jgcs.adjoint_vanishing
  dressed_mass_split_hypotheses ⟨h.M_N_pos, h.q_gt_one⟩

The first and third are tuple projections that batch 2's deliberately
conservative single-field guard declined; the second is a single-field
projection whose body line began with `--` comments, so the same guard read it
as a proof. Both were guard conservatism, not new mathematics.

**Extra finding on `adjoint_vanishing_propagation`, recorded in the file
because it outlives the removal.** It bound `(k : ℕ)` — the jet level whose
*propagation* it is named for — and its conclusion,
`Subsingleton ((𝟙_ C) ⟶ jgcs.adjointObj)`, never mentions `k`. The statement
was level-independent, so "the adjoint vanishing at level 0 implies at all
levels" lived entirely in a comment and in the name. Encoding it needs the
level-indexed adjoint object the abstract formulation does not provide.

## Final position

    genuine proof-no-self-assuming-projection   112 -> 90
    ledger entries                              380 -> 348
    gate                                        exit 0, all 139 fresh

Composition of the remaining 90:

    74  referenced elsewhere    — need the witness built or consumers rewritten
    16  content-block siblings  — the .md claims them; removal is AUTHORIAL
     0  library, zero-reference — exhausted

**The mechanical seam is closed.** Everything left needs either mathematics
that is open (constructing a witness for a context class that was standing in
for it) or an authorial decision about what a content block claims. Neither is
an agent's call, which is why this stops here rather than continuing.

Four untouched declarations staled on their file hashes across this batch
(`dressed_mass_from_substrate_split`, `proton_pair_skein_approx`,
`neutron_pair_skein_approx`, `skein_mass_relation_holds`); each verified
byte-identical to origin/main before its verdict was refreshed, verdict field
included.


---

## 2026-08-30 — the sizing verdict is refuted by its own three examples

The bullet this bean rests on — *"for many of these that IS the open research,
not a formalisation chore"* — was asserted, never measured. Measured now:

**25 of the 79 context classes carrying the 90 remaining findings are inhabited
by `Unit` and zero, with no hypotheses at all** (machine-checked, lean-direct).
All THREE classes the sizing doc named as examples of open research —
`KnotOperatorSelectionContext`, `HoefsmitScatteringPipelineContext`,
`NucleonOrderingFactorizationContext` — are among them.

A class inhabited that cheaply constrains nothing, so a `[C]` binder assumes
nothing and the downstream `[C]`-conditional declaration is conditional on
nothing. **Constructing a witness for one is the defect, not progress** — the
same defect the q-NS carriers had before 2026-08-30.

Stated narrowly: inhabited does NOT mean the block is bad. `BorromeanQuark` is
inhabitable by the corpus's own `orbital_dim_eq_square` and that is §3b-cond
working. The discriminator is whether the downstream declaration *derives* from
the field or *projects* it verbatim; all 90 are the latter by construction.

Second, different finding: `Term7ShellCorrectionClass` is not vacuous but
**provable** — `alpha5_value := -1`, so its field is `-1 < 0`. The open part
(the magnitude, per the source's own comment) is encoded nowhere. That is
`proof-claims-unencoded`, wanting a different disposition.

**Literature: none needed.** Kerov–Vershik 32 documents held, LR 27, elliptic
functions 15, Călugăreanu 3+1 OCR. The one apparent gap is a Mathlib question
and the corpus overstates it: `HasFiniteLPDuality` says LP duality "does not
exist in Mathlib", but `ProperCone.hyperplane_separation` and
`ProperCone.innerDual_innerDual` both resolve against the restored cache.

Artifacts: `scripts/lean-context-class-inhabitation-probe.py` (with
`--selftest`), `docs/audits/2026-08-30-context-classes-are-inhabited-by-zero.lean`,
`docs/audits/2026-08-30-the-remainder-is-vacuous-not-open.md`. PR #6276.

Floor is soft in both directions: three generator fixes moved it 15 → 25 without
touching a class, and 54 classes remain unmeasured rather than established hard.


---

## 2026-08-30 (later) — hand adjudication works, and one class is FALSE

After refuting the "keep fixing the tool" route (yields 1 of 54, then 0 of 6),
applied per-class hand construction. **Floor 26 → 35**, all `lean`-direct exit 0,
in `docs/audits/2026-08-30-context-classes-hand-adjudicated.lean`.

**Rate, which matters more than the count:** nine classes in ~40 min, much of
that `lean` startup rather than thought. The remaining ~44 are **hours, not the
week** the sizing audit projected.

### The one that is not vacuous but FALSE

`QOU.HadronicMass.SkeinMassRelationHolds` asserts
`q·m_p − q⁻¹·m_n = (√q − 1/√q)·m_d` at the constants its own file defines.
**LHS 194.5164, RHS 195.3202 — 0.41 % apart.** Refuted in Lean
(`docs/audits/2026-08-30-skein-mass-relation-is-false.lean`).

**Refutable is worse than vacuous.** A vacuous class makes its downstream
conditional empty; a false one makes it *vacuously true* — it proves nothing and
would equally "prove" the negation. Two consumers, and the second is the
concern: `skein_mass_relation_proton_neutron [SkeinMassRelationHolds] :
SkeinMassRelation` **constructs** the p/n/d Skein mass relation from the false
hypothesis, so that object is unreachable and anything reasoning from it is
vacuous.

Not a claim that the Skein mass relation is wrong as mathematics — only that the
equality *as written, at these constants* is false by 0.41 %, far outside what
the same file treats as agreement (its `row1_proton_matches_CODATA` uses 1e-3
MeV). The repair — approximate form with a stated tolerance, different
constants, or a corrected relation — is authorial.

Proof note: `norm_num` alone cannot close it (the two `rpow` terms survive);
set `s = q^(1/2)`, supply `s*s = q`, rewrite the negative exponent via
`Real.rpow_neg`, `field_simp`, `nlinarith`. The `norm_num at h` before the
rewrite is load-bearing — without it the base is the decimal `1.1097` and the
rewrite finds no occurrence.

Two others say more than "inhabited": `SchurWeylMassContext`'s decomposition
holds over the EMPTY partition set (so its `Z`/`N` parameters are inert), and
`DecayChannelContext`'s "uniqueness off the boundary variety" is discharged by
`on_boundary := fun _ => True`. Both are §3b-cond item 5 with the constraint
missing BETWEEN fields rather than within one — invisible to a syntactic check.

PR #6276.


## 2026-08-31 second tranche — items 1 and 3 closed, item 2 at A 15/15 + B 6/6

All three handed-back items worked. Two were decidable by measurement.

- **Both false classes repaired.** Same defect in each: the .md states one
  thing, the Lean asserts something stronger the .md never claims, and the
  invention is what is false. Neither needed a physics decision.
- **Confinement settled: the library model is canonical** on three criteria
  (.md's SDP-feasibility link; fields are hypotheses not conclusions; 9 vs 2
  consumers). Corrects my own "not mine to pick".
- **Bucket A 15/15, bucket B 6/6.** Four of the six B re-encodings gained a
  real derivation, not just a demotion. Two files claimed "no instance" and
  had one (CPT at Unit/0/id; cusp-holonomy at z = i, verified by compiling).
  `newton_seed_completeness` was statement-identical to its neighbour under a
  docstring claiming a seeding property its type never mentioned.
  `core_levi_cond_aspect_bound` was redundant with its docstring saying the
  opposite. DecayChannel sub-claim (iii) turned out to be the IVT.

**REMAINING: 46 bare projections (31 library, 15 sibling)**, measured by the
new `scripts/sap-projection-liveness.py`. It is a QUEUE, not a defect count --
the four gate accessors in it are the `Group.mul_assoc` idiom over
parameterised classes and were adjudicated legitimate; what those blocks
lacked was the converse of the equivalence their .md claims, now added.

**Two errors of mine, corrected in-branch.** (1) The obvious liveness check
("does the name still occur?") reports 81/81 still live on a tree where nine
were just repaired -- a repaired file keeps the name and a gutted file names
it in the docstring. (2) `7e9230d39a9` converted 82 decls across 69 files
theorem->def; I inferred that hid one from the detector and MEASURED IT FALSE
-- the audit flags it as a def, and it is absent from the ledger because it is
exempt. The 82 stands; the inference did not.


## 2026-09-03 — bucket C, first four repairs (PR #6422)

Four projections repaired to §1a **disposition 3** (name over parameters),
never to a `sorry`: in each the claim is **refutable at free data**, now proved
in-file, so a later `sorry` fails against a standing counterexample.
Library triage 19 → **14 DEFECT** / 2 ACCESSOR / 10 unresolved.

- `knot_operator_selection`, `skein_mass_from_linking` — module docstring
  **asserted the repair** ("does not carry … as a projected field", "ends in
  `sorry`") over code that did neither. In the skein file the *class*
  docstring recorded the field honestly while the module docstring above it
  did not. Mechanism: the rename `claim_skein_mass_from_linking →
  mass_identity` defeats `detectSelfAssuming`'s `CONCLUSION_FIELD` gate.
- `six_term_mass_formula_complete` — the case where naming recovers
  **nothing**: with six opaque terms the claim is the definition of an
  additive split. Both facts proved (`sixTermSplit_sum`,
  `not_sixTermSplit_of_independent`).
- `nucleon_ordering_factorization` — `b67ee924e84` reverted the 2026-08-08
  fix. **14 of its 15 files still project a field it added** (method: field
  in the commit's `+` lines, `:= …field` in the file now). Already analysed
  under `qou-lo1t`; what is new is that they are still in that state.
  **No reliable count of false `sorry` docstrings** — whole-file match says
  8 but cannot separate a live claim from a historical note; my
  docstring-scoped refinement is broken (3 projections vs 14). Upper bound.

**Tooling (`qou-pwut` neighbour, not it):** `qa-agent-entry.ts` hashed only a
sibling `.lean`, so on **180 blocks** whose Lean is at the Lake path the
`lean`/`lean_statement` keys were omitted and an agent verdict could never go
fresh. Now delegates to `resolveCanonicalLean` + the sweep's own lexer (749/750
agreement with committed hashes). Verified fresh on the six-term block.


## 2026-09-03 (later) — CORRECTION: the parser had a third bug and 8 verdicts flip

I recorded above that the Copilot parser fix left the DEFECT/ACCESSOR
partition intact. **That was wrong**, and the way it was wrong is the useful
part.

The comparison ran against the *over-counting* intermediate parser. Three bugs,
two of them mine:

1. under-count — `\w` misses `S'`/`y_λ`, and one name per line (Copilot);
2. over-count — my repair read a **docstring** line with a colon as fields
   (`BindingAssemblyContext`: 4 real, reported 11);
3. mis-classification — a field whose type starts on the **next line** shows an
   empty type, so `CLAIMY` finds no `=` and a **claim field counts as data**.

(2) inflated exactly the rows (3) deflated, so the totals did not move.

Against the corrected parser: **8 of 36 rows flip DEFECT -> ACCESSOR**, all
downward. Library **19 -> 7 DEFECT** (not 10), whole tree **9 / 12 / 15**.

**My structural argument was wrong too:** I said an under-count can only
manufacture a false ACCESSOR. True of bug (1) and irrelevant — the bug that
decides verdicts is in the CLAIM direction and manufactures false DEFECTs.
Generalised from one bug to the partition.

**Evidence the parser is now right, not merely different:** it reproduces the
hand adjudication of 2026-08-31 — all four §4 gate classes read ACCESSOR, which
the old parser contradicted for every one.

No repair is affected (each file was read first; all 8 flipped rows are
untouched). `--selftest` added, pinning the parser against hand-counted
carriers: both earlier bugs were found only because someone knew a file's real
count, and neither showed in the totals.

Sixth repair landed: `sorting_color_energy` — the first where the claim is
**derivable**. `eq_or_eq_of_heckeRelation` proves q and -q^-1 are the ONLY
roots of the manuscript's own Hecke relation, so the block's claim is concluded
to rather than assumed; NoZeroDivisors justified by a ZMod 8 witness, not prose.
Five of its fields (V, V_sq, Sym2, Wedge2, sigma) never appeared in the claim.


## 2026-09-03 (final) — bucket C DRAINED: library 19 -> 0 DEFECT

12 repairs, all to §1a disposition 3, each with a refutation-at-free-data
theorem so a later `sorry` fails against a counterexample rather than prose.
Whole tree now **4 / 25 / 0** (all 4 sibling-tree).

**SIX bugs in `sap-carrier-shape.py`, all pushing the same way.** 2 from
Copilot, 4 from reading a file whose answer I knew. None visible in the
totals; every one either misclassified a CLAIM as data or misattributed the
CARRIER, and both manufacture FALSE DEFECTS:
1. under-count (`\w` misses `S'`; one name per line) — Copilot
2. over-count (docstring line with a colon parsed as 6 fields) — mine
3. multi-line field type -> claim counted as data
4. wrong carrier (first class binder, not the projected one; returned
   `CommRing` twice)
5. one-line `class … where` only -> `unresolved` hid 2 defects + 8 accessors
6. **`CLAIMY` had `≤` but not `≥`** — asymmetry means an absent operator
   lands in the OTHER bucket, not in none. Cleared the last 2 LIB rows.

`--selftest` now pins each shape to a FIXTURE. My first version pinned
`BindingAssemblyContext` and this drain deleted that class 3 commits later —
a test pinned to a carrier the work removes is stale by construction.

**Retracted:** my "zero verdicts flipped" claim (compared against the
over-counting intermediate; 8 of 36 actually flip). Evidence the parser is now
right: it reproduces the 2026-08-31 hand adjudication of all four §4 gate
classes.

**New findings worth their own beans:**
- **convention-C `z_C` live in `.lean`**, sqrt spelling, inside a class field
  type — `lean-markov-convention-audit.py` does NOT see it. Verified
  0.4993203341836945 at the proton pin. Flagged + labelled `skeinNormaliserC`,
  NOT migrated (re-derivation required). -> `qou-cds1`
- **`qa-agent-entry.ts` hashed only a sibling `.lean`** -> on 180 blocks an
  agent verdict could never go fresh. Fixed by delegating to
  `resolveCanonicalLean`; 749/750 lexer agreement.
- **~200 files with 404ing docstring `.md` links** (doubled path segment);
  5 also name a chapter that does not hold their block. Not swept.
- `markov_identification`: a documented correction that **reinstated the
  defect it documents**.
- `jet_prefix_gb_filtration`: the Lean asserted a claim the block **never
  makes** — substitution, not weakening.


### TRAP — a 'prose lies about the code' grep false-positives on prose QUOTING removed code

Nearly published: *"the 2026-08-31 audit claims `magic_iff_double_magic` was
removed; it is still at LRFusion.lean:153"*. **False.** Line 153 sits inside a
```lean fence **within the class docstring**, under the heading
"🛑 The second field is gone (2026-08-31), and it was FALSE" — it quotes the
deleted field to explain why it went.

Verified the right way: strip `/- … -/` first, then read the class body.
`DoubleMagicConjecture` has **exactly one field, `lr_rigidity`**, and
`magic_iff_double_magic` does not occur in code at all. The repair landed
exactly as documented; `IsDoubleMagic` also carries the saturation now.

This is the inverse of the defect I spent the session documenting, and it
matters because the obvious detector for that defect — grep the code for what
the prose says was removed — produces this false positive **systematically**,
on precisely the files that documented their repair most carefully. Any such
detector must strip comments before matching.

**Item 1 of the owner's three-part request is therefore already closed:**
`DoubleMagicConjecture` repaired 2026-08-31 (pre-session), `SkeinMassRelation`
in #6276. No further repair decision is needed on either.

**Third same-name-different-namespace duplication in this drain:**
`QOU.LRFusion.DoubleMagicConjecture` (observations file) is NOT the false one —
its `DoubleMagic Z N := Z ∈ magicSet ∧ N ∈ magicSet` has saturation from the
start and there is no `magic_iff` field. Its flagged `nu_selfConjugate` is a
projection whose docstring **discloses** it ("one of the conditions of the
conjecture itself, lifted to a callable theorem") — the `BondExtensiveBinding`
over-flag class. Ledger says `genuine` (2026-08-09); re-adjudication to
`legit` is a judgement call left to the owner, not taken unilaterally.
(After `MassVolumeFactorization` and `binding_assembly`, that is 3.)


## 2026-09-03 — the sibling tree, and the triage reaches zero in both trees

PR #6539 on `claude/sap-sibling-tree-2026-09-03`, following #6422 (merged,
thirteen library repairs). Four sibling defects; all four repaired.

**`scripts/sap-carrier-shape.py`: library DEFECT 0 / ACCESSOR 14, siblings
DEFECT 0 / ACCESSOR 11, unresolved 0 in each.**

| file | what it actually was |
|---|---|
| `lifting-and-descent/descent-lemma.lean` | conclusion carried as a `structure` field; also `→ₗ[R]` where the `.md` says **algebra** homomorphism, and neither the `G_q`-intertwining nor the QOU-preservation claim encoded at all |
| `braids-and-knots/knot-eigenbasis-complete.lean` | `summands_detected` bound `μ` and **never used it** — the flagged projection was the smaller half |
| `brings-surface/levi-form-defect.lean` | the matter locus was **named but never defined**; `Sing(λ)` existed only as a word in a theorem name |
| `observations/diagrammatic-double-magic-lr-fusion.lean` | `SelfConjugate` was a **free predicate field** — an instance could take `fun _ => True` and discharge all three self-conjugacy hypotheses with `trivial` |

### The pattern this tranche adds to the arc

The four library batches were about *bodies* — `:= ctx.field`. Three of these
four are about **types**: a hypothesis whose subject the instance gets to
choose, or a bound variable that never occurs in the body. Both read as real
constraints and are satisfied by anything. `mu_free_detection_vacuous` (in
knot-eigenbasis) is now a machine-checked demonstration of the first shape, so
a later "simplification" back to it fails against a standing counterexample.

Two were repaired by finding a **real derivation** rather than by naming the
claim over parameters:

* `nu_selfConjugate` — added LR conjugation symmetry `c^ν_{λμ} = c^{ν'}_{λ'μ'}`
  (a theorem of LR theory, not conjecture content) to the data class, **removed**
  `nuZN_selfConj` from the conjecture, and proved it. The conjecture assumes one
  thing fewer than before. This is the §3b-cond item-5 remedy the ledger itself
  prescribes, so it is not a re-adjudication of the prior `genuine` verdict —
  though that verdict's evidence names the **wrong field** (`SelfConjugate`, a
  predicate former, rather than `nuZN_selfConj`).
* `knot_eigenbasis_complete` — added a per-block trace component tied to the
  trace by `tr_eq_sum_blocks`, which makes `tr_ne_zero_of_single_block` and
  `single_summand_detected` follow. Those replace the two deleted re-exports
  rather than merely deleting them.

### A seventh parser bug — and this one INVENTS findings

`sap-projection-liveness.py`'s `_PROJ` matches `:= X.field arg`, which is the
shape of a projection *and* of an ordinary qualified constant. So
`:= Function.Surjective descentMap` — the disposition-3 repair this drain
produces — reported as `PROJECTION`, and the carrier lookup then printed the
nonsense `class CommSemiring not found`.

The six bugs in `sap-carrier-shape.py` all mis-*classified* live rows. This one
manufactures a finding, which is how a drain gets told to re-fix something
already fixed. Fixed by requiring the head identifier to be bound — a binder
name, an instance-binder class head, or a file-level `variable` (which
`body_of`, starting at the decl header, cannot see). Exactly one row moved.

### Left open

* `qou-9552` — `DescartesKnotEigenbasis.all_summands_detected` has the same
  defect in a worse form: the summand index is bound as `_` and the detected
  value is a free `∃ jonesVal : ℝ, jonesVal ≠ 0` tied to no trace, so the field
  asserts that `ℝ` has a non-zero element. Its own docstring discloses the gap.
* Copilot's third review comment on #6422 was never read — `get_review_comments`
  returned `API rate limit already exceeded` on five attempts.
* Fourth same-name-different-namespace duplication found:
  `QOU.LRFusion.DoubleMagicConjecture` (sibling) vs
  `QOU.Interactions.LRFusion.DoubleMagicConjecture` (library), after
  `MassVolumeFactorization`, `binding_assembly` and `ReebBundleComplement`.


## 2026-09-03 21:5xZ — landed under PR #6526, which re-targeted; one dangling consumer left on main
b34a9c689b removed MarkovIdentificationContext while PR #6526 (bean qou-gzgi) was inhabiting it from the proved convention-D Markov trace. Re-targeted the same proof at the new Prop: MarkovIdentificationInstance.markovTrace_branching_of_markovTrace proves markovTrace_branching (#blocks) (Ocneanu weights) (seminormal block traces) (T.tr n x) for every Markov trace at z_D — i.e. the identity this file lists as 'Open' is a theorem at D, one module over. Not fixed here: docs/audits/2026-08-30-context-classes-hand-adjudicated.lean:713 still writes 'instance : MarkovIdentificationContext' and now references a removed class (docs file, not a library module; noting, not repairing).



## 2026-10-10: the .md side now matches the Lean label
The four pair-Skein .md blocks now state that the denominator is the convention-C Markov weight, matching skeinNormaliserC (M6 1a, qou-2cof). Migration remains qou-cds1's.
