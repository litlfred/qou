---
name: compute-integration-watcher
roles: [collaborator, owner]
user_invocable: true
inherits: local/integration-watcher
watch_arg: compute
description: >
  Cross-layer wiring auditor — watches for newly-landed mathematical
  improvements (Lean proofs, propositions, lemmas, axiom→theorem
  upgrades, witness data) on `origin/main` AND on open PRs, and
  checks whether each one has been wired into the production compute
  chain. Complements `local/compute-audit` (which scans for
  performance/correctness antipatterns inside scripts).  Runs in two
  modes: REACTIVE (watch new commits / PR events) and IDLE-SWEEP
  (walk all existing content blocks and audit wiring).
allowed-tools: Read Bash Grep Glob Edit Write Agent Monitor
---

# Compute Integration Watcher

## Role

When a new mathematical claim lands on `main` (or an open PR introduces
one), the claim is not "done" until the compute chain that consumes it
has been updated to reflect it.  A Lean theorem proving
`c_3 = -2` (`prop:hopf-jones-c3-categorical`) is only valuable if the
6-term mass-formula sweep actually uses `c_3 = -2` rather than a fitted
free parameter.

This skill answers, on every new commit/PR event AND on demand against
all existing blocks: **for each math improvement, is the matching
compute consumer wired in, using the correct primitives, at the
correct precision, against the correct constants?**

It is the *cross-layer* counterpart to:

- `local/compute-audit` — patterns INSIDE one script (P1–P32)
- `local/watch` — event-stream router for upstream commits / PRs
- `local/proof-gap-audit` — paper claims missing Lean proofs
- `local/proof-integration-watcher` — proof-side analogue of this
  skill (chases sorries / naked conjectures across main + sibling
  PRs).  Same watch-and-act loop, different layer.  When both
  skills are armed in the same session: `proof-integration-watcher`
  owns proof-QA gaps; this skill owns compute-wiring gaps.  Gaps
  that bridge both layers (e.g. a Lean theorem proved on main with
  no compute consumer) are double-claimed: pick the one whose
  delivery cycle reaches main first.

Where those skills look at one layer in isolation, **this** skill
looks at the boundary between layers: paper → compute, Lean → compute,
upstream witness → downstream consumer.

## When to use

| User phrase | Action |
|------------|--------|
| "audit math compute" / "audit compute integration" | full idle-sweep |
| "is X wired in?" / "where is X consumed?" | targeted wiring check |
| "what props are not in compute?" | idle-sweep, filtered to NOT_WIRED |
| "watch main + check wiring" | reactive mode (sub-mode of `watch`) |
| "validate mass-table sweep pipeline" | run pipeline + cross-check witnesses |
| post-merge of a `prop:*` block | reactive (auto-triggered from `watch` §3 Q3) |
| idle / waiting on long task | start an idle-sweep agent in background |

## Invocation modes

### A. REACTIVE (called from `watch` §3 Q3 — "Can we reuse?")

When `watch` sees a new commit on `main` (or PR event) that adds or
changes a `prop:` / `thm:` / `lem:` / `cor:` block (or its `.lean`
sibling), and Q3 hits step 4 ("Computation"), invoke this skill on the
affected label.  Outputs:

- WIRED / PROBE-ONLY / NOT-WIRED verdict
- list of consumer scripts that currently use (or should use) the block
- recommended fix (script edit, witness regen, new probe)

### B. IDLE-SWEEP (user-invoked or background)

When the foreground task is blocked (long Rust build, CI wait, big
agent), launch this skill in the background.  It walks every
`prop:*` / `thm:*` / `lem:*` content block, checks the
`local/compute-integration-watcher` patterns I1–I13 below, and emits
a ranked workplan to
`docs/audits/<date>-compute-integration-sweep.md`.

The idle-sweep MUST be safe to interrupt — checkpoint every 50 blocks
to a `.wip.json` so a partial sweep is still useful.

### C. AUTHOR-QUESTION QUEUE (idle-driven)

Per the repo owner's accessibility directive, when the foreground
task is blocked, this skill maintains a queue of *author questions*
and pulls one off when idle to ask via the `AskUserQuestion` tool.

The queue lives in `docs/audits/compute-integration-question-queue.md`
(gitignored — survives branch switches per the `.beans/` convention).
Each entry carries:

- **trigger context** (commit / PR / sweep that surfaced the question)
- **question stem** (≤2 sentences)
- **3–4 mutually exclusive options** with descriptions
- **priority** (P0/P1/P2 — P0 blocks production wiring; P2 is design)
- **session-touch** (does answering require touching content / Lean?)

The queue is consumed in priority order.  When a foreground task
goes idle (long Rust build, CI wait, sleeping on a background
agent), pull the highest-priority pending question, ask it via
`AskUserQuestion`, capture the answer in the queue entry under
`answer:`, and act on it before pulling the next.

Add to the queue (do not ask immediately) when:

- An I-pattern fix has architectural sub-decisions (e.g. which
  directory should the new block live in, which Lean namespace).
- A sibling PR introduces a wiring choice that needs owner
  sign-off (e.g. fate-of-predecessor when a new prop supersedes
  a production lemma — pattern I2-a).
- A pattern hit is ambiguous between two I-numbers (the new pattern
  itself becomes a queue entry: "should we split I-N into I-N-a
  and I-N-b?").

Skill rule: **never block on the queue.**  If no pending P0/P1
question and the foreground is busy, work the next compute
integration improvement instead.

## The 13 integration antipatterns (I1–I13)

### Group A — Missing wiring

- **I1. PROVEN-IN-LEAN, NO PROBE.** A `prop:`/`thm:`/`lem:` block has a
  `.lean` sibling with 0 sorrys (or §3b-cond conditional-class), but
  no `folio-assistant/computations/probe_*` script and no
  `*.witness.json` referencing the label via `contentBlock`.  Fix:
  write a probe that exercises the claim at q₀ + emits a witness
  whose `contentBlock` field points at the prop.

- **I2. PROBE-ONLY (NOT CONSUMED IN PRODUCTION).** A probe witness
  exists, but the production consumers
  (`paper_six_term_isotope_sweep.py`, `derive_m_p_hecke_full_tower_50dps.py`,
  `derive_m_n_hecke_full_tower_50dps.py`, `atomic_mass_via_rho_k.py`,
  `mass_table_ppb.py`) do not import or reference the probe's witness
  file or its derived constants.  Fix: thread the probe's result into
  the relevant production formula or, if intentionally probe-only,
  add a `# probe-only: <reason>` line to the script header.

  - **I2-a. PROBE-ONLY that SUPERSEDES a production lemma.** Sub-case
    of I2 — the new prop is the *substrate-pure / no-fit* version of
    what an existing production `lem:` / `prop:` was already using as
    input (typical sign: the new block's `.md` calls itself the
    "substrate-pure counterpart of `lem:foo`").  Wiring it in is
    NOT a single-script edit; it also requires:
    1. A "fate of the predecessor" decision — keep as physical
       interpretation (`interprets:` link), demote to `remark`,
       deprecate-banner, or delete.  **Default: keep + complementary**
       unless the predecessor's narrative content already lives
       elsewhere.
    2. Calibration-count accounting update — if the predecessor was
       a CAL input (CLAUDE.md §"three-cal discipline"), the
       substrate prop typically reduces the CAL count by one.  Update
       `canonical-script-input-audit.witness.json`'s classification
       AND the affected scripts' `calibration_inputs` metadata.
    3. Sweep for downstream consumers of the predecessor's
       derived-output constants (`μ_u`, `μ_d`, `mu_d - mu_u`, etc.).
       Those constants disappear under the new substrate prop;
       repoint them to the substrate formula OR mark `_VALIDATION`
       per the existing convention.
    4. Before deprecating the predecessor's block, verify the
       physical-interpretation narrative content has a home.  In
       QOU's content tree, dressed-quark masses are introduced
       *only* inside `lem:nucleon-mass-splitting` — there is no
       dedicated `prop:dressed-quark-mass` block.  Deleting the
       lemma would orphan the dressed-quark narrative.

    Practical workflow when this sub-pattern fires: open a fresh
    sibling PR (do NOT bundle with the audit doc PR), name it
    `claude/wire-<prop-label>`, list the four bookkeeping items
    above in the PR body, and request owner review **on the fate
    decision** before pushing the production-formula edits.

    **Three-phase delivery (validated on PR #696 for
    `prop:flavor-dressed-mass-from-substrate-split`):**
    - **Phase 1 — Foundation.**  Author the new structural
      content blocks (def + props + thm + remark) and their Lean
      stubs.  Update the chapter manifest.  Run
      `bun run validate <paper>` and confirm pass.  Commit + push
      for early review.
    - **Phase 2 — Predecessor deletion + downstream repointing.**
      Delete the lemma's `.{ts,md,lean}` files. Grep `content/`
      for every `uses[]` / `interprets[]` / markdown-link
      reference and repoint to the new prop.  Update the chapter
      manifest to remove the deleted blocks.  Re-run
      `bun run validate` to catch any residual references.
      Commit + push.
    - **Phase 3 — Production wiring.**  Author a NEW probe script
      `probe_<new_prop_slug>.py` whose witness's `contentBlock`
      points to the new prop AND whose assertions cross-check the
      substrate-pure formula against the appropriate CODATA /
      validation anchor.  Add the new prop's label to
      `reference_blocks` in the canonical sweep's witness.  This
      lets downstream consumers see the dependency without
      inlining the cross-check.  Commit + push.

    Across the three phases keep `bun run validate` clean.  Each
    phase is a single commit; reviewers can read the diff per
    phase rather than as a giant atomic squash.

- **I3. WIRED BUT GUARDED OFF.** A consumer references the witness but
  the call is behind an `if False`, an env var defaulting to off, or a
  legacy fallback that hides it. Fix: promote to default-on after a
  numerical-equivalence cross-check at q₀.

### Group B — Stale wiring

- **I4. WITNESS-HASH DRIFT.** A consumer's witness records an
  `upstream_witness_hashes` map; the SHA1 of one of the upstreams on
  disk no longer matches.  Fix: rerun the script (or the producer that
  emits the upstream witness) and recommit both.  See
  `witness_dependency_drift.py` (PR #663).

- **I5. CONTENTBLOCK REFERENCES MISSING LABEL.** A witness's
  `contentBlock` field names a label that has no `.ts` / `.md` file in
  `content/`.  Fix: either create the block or point the field at the
  closest neighbour. (E.g. the 2026-05-16 finding:
  `atomic_mass_via_rho_k.py` → `prop:atomic-mass-via-rho-k`
  undefined.)

- **I6. EMPTY `data` SECTION IN PRODUCTION WITNESS.** A production
  witness file has `"data": {}` or `"data": []` (sweep crashed or
  exits cleanly without populating).  Fix: run the script under
  `python -X faulthandler`; usually exposes a silent exception that
  was caught and turned into no-op.  (Spotted on
  `paper-six-term-isotope-sweep.witness.json` 2026-05-16: rows present
  at top level instead of under `data` — schema drift.)

- **I7. PROBE WITNESS COMPUTED-AT > 7 DAYS BEHIND THE PROP'S `.md`
  MTIME.** Indicates the prop has been edited and the probe is stale.
  Fix: rerun probe + regen witness; if numbers shift, surface to
  author for sign-off before recommitting.

### Group C — Wrong primitive

- **I8. PRODUCTION CHAIN USES `float64` WHERE WITNESS USES
  `mpmath_50dps`.** The witness's value is faithful to ~50 digits;
  the consumer's `q_parameter.Q` (or any internal `float()`) erodes it
  to ~15 digits.  Trace the value through `mp.mpf(str(...))` instead
  of `float(...)` and confirm the consumer's final precision matches
  the witness's.  (Reference fix:
  `paper_six_term_isotope_sweep.py` `mp.mpf(str(z_mark))` per PR #534
  Gemini comment #3.)

- **I9. HARDCODED CODATA / DERIVED LITERAL OUTSIDE THE REGISTRY.**
  Production script contains a numerical literal (mass, Q-value,
  ratio, constant) that *should* be derived from a prop or imported
  from `codata_constants.py` / `experimental_constants.py`.  This is
  P31 in `compute-audit`, surfaced here because it also breaks
  wiring.  Fix: import the registry symbol, run the audit scanner.

- **I10. LEGACY MASS FORMULA USED IN PLACE OF CANONICAL.** A consumer
  imports / inlines a deprecated formula superseded by the current
  6-term form (e.g. `compute_mass_at_level`, `crt_markov_v4`,
  `markov_invariant_unified_mass`, `paper_six_term_canonical_t1`).
  Fix: replace the call with `paper_six_term_isotope_sweep` or its
  helper functions; keep the deprecated import in `_deprecated/`
  only.

### Group D — Cross-paper / cross-layer

- **I11. CROSS-PAPER `uses[]` NOT CONSUMED.** A block's `uses[]`
  contains a `paper-dir:label` (e.g. `unital-groebner-bases:cor:pbw`)
  but no compute consumer references the upstream paper's witness.
  Fix: either drop the cross-paper `uses[]` if it's only narrative
  context, or wire the dependent witness in via a `from
  upstream-paper-witness import …` block.

- **I12. WITNESS `lean.ref` MISMATCH.** A content block's `lean.ref`
  URI (`<pkg>:Decl.Path`) does not resolve to an actual Lean
  declaration in the named Lake package.  Fix: either create the Lean
  decl or update the `ref:` URI.  Detected by
  `bun run validate <paper>` under the `lean-ref-resolves` rule;
  surfaced here because it commonly catches "Lean theorem renamed,
  forgot to update content block".

### Group E — Discipline drift

- **I13. FITTED LITERAL LABELLED AS SUBSTRATE-CANONICAL.** A
  production script defines a module-level high-precision numerical
  literal (`X = mp.mpf("1.234567890...")`) AND its docstring or
  emitted witness claims the value is "substrate" / "canonical" /
  "derived" / "predicted", but the literal was solved from CODATA
  (or any other empirical anchor) rather than computed from the
  three permitted calibrations (CAL-1 / 2 / 3).  The discrepancy
  propagates into downstream `canonical_status` taxonomies, making
  the framework's predictive accuracy look better than it is.
  Detected by `fitted_labelled_canonical_audit.py` (warn-only in
  CI; 0-issue baseline).  Fix: rename the variable to include
  `_FITTED_FROM_*`, add a CAL-4-VIOLATION banner to the docstring,
  emit `derivation_status: "FITTED_FROM_CODATA"` + `cal_class:
  "CAL-4-VIOLATION"` in the witness, and demote any downstream
  `canonical_status` label to a less-substrate-claiming taxonomy
  slot (e.g. `"borromean-tower-via-fitted-lambda"` instead of
  `"canonical-substrate"`).  Tracked in
  `docs/canonical-derivation-cheat-sheet.md §5 fix #1`; originating
  case was `LAMBDA_PROTON_DOC / LAMBDA_NEUTRON_DOC` in
  `m_p_borromean_verification_50dps.py`.

## Workflow

### Reactive mode (per-commit / per-PR-event)

For each new `prop:*` / `thm:*` / `lem:*` / `cor:*` label introduced or
changed by the commit:

1. `git diff <prev_sha>..<new_sha> -- content/` — find affected labels.
2. For each label `L`:
   - Walk **I1–I13** below in order.  Stop at the first hit; emit a
     concrete fix recommendation.
   - If clean, emit a one-liner: `L: ✓ wired`.
3. Roll the per-label results up into a single comment summary, with
   actionable items at the top.
4. If the commit was a sibling-PR (not main), and the wiring
   recommendation is small and local to my branch, **act on it**
   under `watch §3 Q4 — Act`; otherwise queue as a TODO under the
   sibling PR.

### Idle-sweep (full content scan)

1. Enumerate every `prop:*.ts` / `thm:*.ts` / `lem:*.ts` / `cor:*.ts`
   under `content/quantum-observable-universe/`.
2. For each label `L`:
   - **Step 1 — Lean status.** Read the `.lean` sibling; count
     sorrys, axioms, classes.  Skip blocks where the Lean side is
     "conjecture-class" (CLAUDE.md §3b-cond) — those don't need a
     compute consumer.
   - **Step 2 — Probe presence.** Grep
     `folio-assistant/computations/*.witness.json` for
     `"contentBlock": "L"`.  Record producer script name.
   - **Step 3 — Production consumption.** Grep
     `folio-assistant/computations/{derive_*,paper_six_term*,build_*_chain,atomic_mass_*}` for the
     producer witness file name OR for the prop label string.
   - **Step 4 — Apply I-patterns.** Walk I1–I12 in order; emit
     hits.
3. Emit `docs/audits/<YYYY-MM-DD>-compute-integration-sweep.md`
   with: per-label table, aggregate counts by pattern, recommended
   next actions ranked by leverage × tractability.
4. For sweep results that flag fixes ≤30 minutes apiece, batch
   them into a single follow-up branch named
   `claude/compute-integration-fixes-<YYYY-MM-DD>`.

### Mass-table sweep validation (sub-mode)

Triggered by "validate mass-table sweep" / "is the mass pipeline
working?":

1. Run `python3 paper_six_term_isotope_sweep.py` (the canonical 6-term
   formula) and capture stdout + the regenerated witness.
2. Cross-check each isotope row against
   `atomic-tr-m-mpfr-50dps.witness.json` (T1 source) and
   `term6-habiro-residue-mpfr-50dps.witness.json` (T6 source).
3. For any `KeyError "no canonical T1 for X"`, report the missing atom
   and check whether PR #683's Rust χ pipeline now covers it (the
   `4-way 1ppb gate now covers 8 atoms` commit promises ⁶Li, ⁷Li,
   ⁷Be, ⁸Be).
4. Report ABSOLUTE prediction error AND ISOSPIN-DEGENERACY error
   separately — the absolute number tracks calibration health, the
   isospin number tracks structural correctness independent of
   calibration.
5. Run `python3 canonical_derivation_pipeline_compliance.py` for the
   compliance dashboard; emit per-contract pass/warn/fail.

## Tooling

| Question | Tool / file |
|---------|-------------|
| Which props have probes? | `grep '"contentBlock":' folio-assistant/computations/*.witness.json` |
| Which probes have production consumers? | `grep -l '<witness-name>' folio-assistant/computations/derive_*.py paper_six_term_isotope_sweep.py atomic_mass_via_rho_k.py mass_table_ppb.py` |
| What's the canonical mass formula? | `paper_six_term_isotope_sweep.py` (per its own docstring) |
| What's the m_p production chain? | `derive_m_p_hecke_full_tower_50dps.py` → `build_proton_mass_50dps_chain.py` → `atomic-tr-m-mpfr-50dps.witness.json` |
| What's the m_n production chain? | `derive_m_n_hecke_full_tower_50dps.py` → `build_neutron_mass_50dps_chain.py` |
| Witness dependency drift | `python3 witness_dependency_drift.py` |
| Compute-audit scan | `python3 compute_audit_scan.py` (I8/I9 cross-coverage) |
| Canonical derivation chain doc | `docs/audits/derivation-chain-mass-tower.md` |
| Compliance dashboard | `canonical_derivation_pipeline_compliance.py` |

## Verification checklist before declaring a prop "wired"

1. **Lean side proved** (or §3b-cond conditional-class instance).
2. **Probe witness exists** with `contentBlock: "<label>"` and a
   numerical assertion that fails CI if the prop is broken.
3. **At least one production-chain consumer** imports the probe
   witness, the producer script, or the derived constant (visible
   via `grep` in the consumer file).
4. **Numerical-equivalence cross-check** at q₀ — if the prop closes
   to within X%, the consumer's witness records that residual.
5. **Anti-staleness wiring** — consumer's witness has
   `upstream_witness_hashes` entry for the probe witness.
6. **`bun run validate`** passes (catches I5 / I12).

## Anti-patterns this skill explicitly rejects

- **Auto-fixing wiring on someone else's PR branch.** I-pattern hits
  on sibling PRs become a comment on that PR (one comment, batched),
  not a force-push to its branch.  Per CLAUDE.md author-only-closes
  rule, the sibling PR's owner accepts the recommendation.
- **Generating new probes for conjecture-class props.** Conjectures
  (CLAUDE.md §3b) don't need compute consumers — their witnesses are
  axiomatic.  Skip them in idle-sweep.
- **Declaring "wired" based on docstring-only mention.** A line
  `# uses prop:foo` in a comment is *not* wiring; the consumer
  must actually load the witness or compute the derived constant.
- **Numerology / three-route-convergence claims** — also explicitly
  rejected in `local/compute-audit`; restated here because the
  wiring step can mask them ("we wired it, look at the agreement!"
  when the routes compute different categorical objects).

## Pattern → reference example

| Pattern | Example on main (2026-05-18) |
|---------|------------------------------|
| I1 | `prop:chi-lambda-w0-sign-weighting` — Lean proven (PR #672 merge), no probe witness |
| I2 | `prop:flavor-split-substrate` — probe `probe_flavor_split_substrate.py` exists, no production consumer beyond docstring mention in `derive_m_p_hecke_full_tower_50dps.py:58` |
| I3 | (placeholder — fill in when a real instance is spotted) |
| I4 | (caught by `witness_dependency_drift.py` — running it weekly is the policy) |
| I5 | `prop:atomic-mass-via-rho-k` referenced by `atomic_mass_via_rho_k.py` — content block does not exist (2026-05-16 audit) |
| I6 | `paper-six-term-isotope-sweep.witness.json` — top-level `data: []` (rows are under top-level `rows`, schema-shift artifact) |
| I7 | `light-isotope-sweep.witness.json` — 9 days behind main as of 2026-05-18 |
| I8 | `paper_six_term_isotope_sweep.py:Z_MARK` — fixed in PR #534 by wrapping `mp.mpf(str(z_mark))` |
| I9 | P31 hits in `compute-audit-scan.witness.json` (26 hits as of 2026-05-17) |
| I10 | `paper_six_term_isotope_sweep.py` docstring lists 4 retired formulas — confirm no live imports of them |
| I11 | (sweep produces these — check `uses[]` cross-paper entries) |
| I12 | Detected by `bun run validate`; `lean-ref-resolves` rule |

## Tie-in with `local/watch`

`watch` §3 Q3 ("Can we reuse?") step 4 ("Computation") is the entry
point.  When the commit adds a `prop:*` block, `watch` should
delegate to this skill, capture its verdict, and either act-or-defer
per Q4.  When the commit adds *only* a witness (no new prop), this
skill is unnecessary — `compute-audit` already covers in-script
patterns.

For the idle-sweep, the SessionStart hook may optionally arm this in
addition to `watch`; see `.claude/skills/local/compute-integration-watcher.md`
§ "When to use" for the trigger phrases.

## Output template (per-label)

```
prop:<label>     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Lean:        ✓ 0 sorrys  (qou:QOU.Foo.bar, n axioms)
  Probe:       ✓ probe_foo.py → foo-probe.witness.json (computedAt: …)
  Production:  ✗ NOT consumed in production chain (I2)
               ↳ recommend: thread probe_foo into paper_six_term_isotope_sweep at term N
  Anti-stale:  ✓ upstream_witness_hashes has 1 entry
  Validate:    ✓ bun run validate clean
  Verdict:     PROBE-ONLY
  Action:      I2 fix — see docs/audits/<date>-compute-integration-sweep.md row K
```

## CLAUDE.md interaction

This skill respects the same rules as `compute-audit`:

- Never write to **protected files** (deploy/google-viewers.txt,
  deploy/github-collaborators.txt, .github/CODEOWNERS).
- Never close / resolve TodoItems (human-only per CLAUDE.md §4a).
- Cite the matching I-pattern (I1–I12) for every recommended fix.
- For dual paths (probe-only vs production), preserve the
  probe-only path as an opt-out — never delete it.
