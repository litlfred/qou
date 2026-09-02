---
# qou-z9ws
title: 'SIZED: the 112 self-assuming projections are ~102 independent defects, not one systemic pattern'
status: completed
type: task
priority: normal
created_at: 2026-08-30T13:41:46Z
updated_at: 2026-08-30T14:39:06Z
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
