---
name: compute-integration-watcher
roles: [collaborator, owner]
user_invocable: true
inherits: local/integration-watcher
description: >
  Cross-layer wiring integration watcher — watches for newly-landed
  mathematical improvements (Lean proofs, propositions, lemmas,
  axiom→theorem upgrades, witness data) on `origin/main` AND on
  open PRs, and checks whether each one has been wired into the
  production compute chain. Complements `local/compute-audit` (which
  scans antipatterns *inside* one script). Inherits shared mechanics
  (Monitor, subscriptions, queue, ledger, idle sweep, author-ask,
  watch-prepared-PRs, witness-drift recovery, billing-quick-fail
  flake, post-completion one-voice, sibling-PR comment protocol,
  backlog-found PR spin-up, handover docs) from
  `local/integration-watcher`.
allowed-tools: Read Edit Write Bash Grep Glob Agent Monitor Skill
---

# /compute-integration-watcher

A concrete instance of [`local/integration-watcher`](integration-watcher.md).
The parent encodes the shared mechanics; this file fills the nine
domain-specific slots A-I.

**Setup:** use `NAME=compute-integration-watcher` everywhere the
parent's §1 references `${NAME}`. Files at
`todos/compute-integration-watcher-queue.json` and
`todos/compute-integration-watcher-ledger.md`.

When a new mathematical claim lands on `main` (or an open PR
introduces one), the claim is not "done" until the compute chain
that consumes it has been updated to reflect it. A Lean theorem
proving `c_3 = -2` (`prop:hopf-jones-c3-categorical`) is only
valuable if the 6-term mass-formula sweep actually uses `c_3 = -2`
rather than a fitted free parameter.

This watcher answers, on every new commit/PR event AND on demand
against all existing blocks: **for each math improvement, is the
matching compute consumer wired in, using the correct primitives,
at the correct precision, against the correct constants?**

## Slot A — Goal statement

Every `prop:` / `thm:` / `lem:` / `cor:` block in the paper has:
(1) a Lean sibling (proved or §3b-cond conditional-class);
(2) a probe witness with `contentBlock: "<label>"`;
(3) at least one production-chain consumer that imports the probe
witness or its derived constant; (4) numerical-equivalence
cross-check at $q_0$ in the consumer's witness; (5) anti-staleness
wiring via `upstream_witness_hashes`. Anything missing is a wiring
gap.

## Slot B — §3 trigger filter

```bash
SHA=<event sha>
changed=$(git diff-tree --no-commit-id --name-only -r "$SHA")

is_wiring_event=false

# (i) Any new/changed provable content block (with Lean sibling)
echo "$changed" | grep -qE 'content/.*\.(md|ts|lean)$' && {
  for f in $(echo "$changed" | grep -E 'content/.*\.ts$'); do
    grep -qE '^export default (theorem|lemma|proposition|corollary|definition)\(' "$f" && is_wiring_event=true
  done
}

# (ii) Any change to a production-chain consumer or witness producer
echo "$changed" | grep -qE '^folio-assistant/computations/(derive_|paper_six_term|build_|atomic_mass|mass_table|probe_).*\.py$' && is_wiring_event=true

# (iii) Any change to a witness JSON (drift / new claim)
echo "$changed" | grep -qE '\.(witness|derivation)\.json$' && is_wiring_event=true
```

For PR review-comment events, pass through if the comment body
mentions: `wired`, `wiring`, `consumer`, `production chain`,
`probe`, `witness`, `not consumed`, `KeyError`, `staleness`.

## Slot C — §4b dispatch table

| Specialist | When to run | What it checks |
|------------|-------------|----------------|
| `compute-audit` (P1-P32) | Any changed `.py` | In-script patterns; backs I8 (float64-precision-loss), I9 (hardcoded literal) |
| `witness_dependency_drift.py` | Any changed witness | I4 (upstream-witness-hash drift) |
| `canonical_derivation_pipeline_compliance.py` | Session start + after any prop:/witness: change | Cross-chain wiring contracts |
| `validate.ts` (`bun run validate <paper>`) | Any content-block change | I5 (broken `contentBlock` label), I12 (`lean.ref` mismatch) |
| `derivation_chain_validator.py` | Any changed `.derivation.json` | I13 (incomplete upstream coverage) |
| `proof-narrative-lean-equivalence` | New Lean prop landed | I1 (proven-in-Lean, no probe) sanity check |

## Slot D — §4c finding taxonomy (the 13 I-patterns)

### Group A — Missing wiring

| Finding | Severity | Definition |
|---------|----------|------------|
| `I1-PROVEN-IN-LEAN-NO-PROBE` | major | Block has Lean proved (0 sorrys or §3b-cond) but no probe script + no witness with `contentBlock` referencing the label |
| `I2-PROBE-ONLY-NOT-CONSUMED` | major | Probe witness exists, but production consumers don't import it |
| `I2a-PROBE-SUPERSEDES-PRODUCTION-LEMMA` | critical | Sub-case: new prop is the substrate-pure/no-fit version of an existing production lemma; needs full "fate of predecessor" decision per the §I2a 4-step bookkeeping |
| `I3-WIRED-BUT-GUARDED-OFF` | major | Consumer references the witness but the call is behind `if False` / off-by-default env var |

### Group B — Stale wiring

| Finding | Severity | Definition |
|---------|----------|------------|
| `I4-WITNESS-HASH-DRIFT` | critical | Consumer's `upstream_witness_hashes` map disagrees with the on-disk witness SHA1 |
| `I5-CONTENTBLOCK-MISSING-LABEL` | critical | Witness's `contentBlock` field names a label that has no `.ts`/`.md` file |
| `I6-EMPTY-DATA-SECTION` | critical | Production witness has `"data": {}` or `"data": []` (sweep crashed silently) |
| `I7-PROBE-STALE-VS-MD` | major | Probe `computedAt` > 7 days behind the prop `.md` mtime |

### Group C — Wrong primitive

| Finding | Severity | Definition |
|---------|----------|------------|
| `I8-FLOAT64-VS-MPMATH-50DPS` | critical | Production chain uses `float64` where witness has 50-dps precision; erodes faithfulness |
| `I9-HARDCODED-CODATA-DERIVED` | major | Production script contains a literal that should be from registry (also P31 in `compute-audit`) |
| `I10-LEGACY-MASS-FORMULA` | major | Consumer imports a deprecated formula superseded by current 6-term form |

### Group D — Cross-paper / cross-layer

| Finding | Severity | Definition |
|---------|----------|------------|
| `I11-CROSS-PAPER-USES-NOT-CONSUMED` | minor | `uses[]` contains `paper-dir:label` but no compute consumer references the upstream paper's witness |
| `I12-LEAN-REF-MISMATCH` | major | Content block's `lean.ref` URI does not resolve; caught by `bun run validate` lean-ref-resolves rule |
| `I13-INCOMPLETE-UPSTREAM-COVERAGE` | major | Production consumer expects entry X but upstream witness's `results` / `data` doesn't include X (KeyError or silent skip) |

## Slot E — §4d discharge bands (examples)

| Band | Examples |
|------|----------|
| **Auto-discharge** | `I4-WITNESS-HASH-DRIFT` → rerun script + recommit; `I8-FLOAT64-VS-MPMATH-50DPS` → wrap with `mp.mpf(str(...))`; `I9-HARDCODED-CODATA-DERIVED` → `codata_constants` import; `I10-LEGACY-MASS-FORMULA` → swap to `paper_six_term_isotope_sweep`; `I5-CONTENTBLOCK-MISSING-LABEL` (only if a near-neighbour exists) |
| **Author-assist** | `I1-PROVEN-IN-LEAN-NO-PROBE` (probe authoring is a write task); `I2a` (fate-of-predecessor needs owner sign-off); `I3-WIRED-BUT-GUARDED-OFF` (promoting to default-on needs cross-check); `I6-EMPTY-DATA-SECTION` (silent failure root-cause); `I7-PROBE-STALE-VS-MD` (sign-off on new numbers); `I13` (extending upstream producer or accepting `pending` row) |
| **Defer** | Conjecture-class props don't need compute consumers (CLAUDE.md §3b) — skip in idle sweep |

**Sub-pattern detail for I2a:** when this sub-pattern fires, follow
the **three-phase delivery** (validated on PR #696 for
`prop:flavor-dressed-mass-from-substrate-split`):
- **Phase 1 — Foundation.** Author new structural content blocks (def
  + props + thm + remark) and their Lean stubs. Update chapter
  manifest. `bun run validate <paper>` clean. Commit + push.
- **Phase 2 — Predecessor deletion + downstream repointing.** Delete
  the lemma's `.{ts,md,lean}` files. Repoint every `uses[]` /
  `interprets[]` / markdown-link reference. Re-validate. Commit + push.
- **Phase 3 — Production wiring.** Author the new probe script.
  Wire into consumers via the new prop's witness. Commit + push.

## Slot F — §4e author-ask templates

```markdown
**compute-integration-watcher ask — `<label>`** (from <source>)

- Pattern: `<I-N-name>` — <one sentence>
- Severity: <critical | major | minor>
- File: <github-blob-url to `.md`>
- Consumer chain involved: <which production scripts would consume this>
- Attempted: <which scanners/specialists tried>
- Question:
  1. I should write a probe + thread into production (Auto-discharge)
  2. Probe-only is intentional — mark with `# probe-only: <reason>` comment
  3. This is conjecture-class — skip (no compute needed)
  4. <pattern-specific option, e.g. for I2a: "approve the 3-phase fate-of-predecessor handling">
```

## Slot G — §5a backlog discovery

```bash
# 1. Enumerate every prop:/thm:/lem:/cor: content block
find content/quantum-observable-universe -name '*.ts' -type f 2>/dev/null \
  | xargs grep -lE '^export default (theorem|lemma|proposition|corollary|definition)\(' \
  | sort -u > /tmp/_pw_compute_blocks.txt

# 2. For each label, walk I1-I13 (see Slot D)
#    - Step 1 (Lean status): count sorrys + axioms + classes
#    - Step 2 (Probe presence): grep contentBlock in witnesses
#    - Step 3 (Production consumption): grep producer witness name OR label string in production scripts (.py only — not .witness.json!)
#    - Step 4 (Apply patterns): walk I1-I13 in order
```

The trailing `.py` filter on Step 3 is essential: a bare
`derive_*` matches `derive_*.witness.json` files and produces
false-positive "consumer" hits.

## Slot H — §5b prioritisation

Order by **leverage × tractability**:

1. **Critical I-patterns first** (I4 / I5 / I6 / I8 / I2a) — wiring
   gaps that produce silent wrong answers.
2. **Major I-patterns next** (I1 / I2 / I3 / I7 / I9 / I10 / I12 / I13).
3. **Minor / informational** (I11).
4. **Within a severity, prefer high-leverage props** (many
   downstream dependents via `uses[]`).
5. **Skip conjecture-class blocks** in idle sweep.

## Slot I — §6 invariants

| Invariant | Check |
|-----------|-------|
| No new `I1-PROVEN-IN-LEAN-NO-PROBE` introduced | Every prop block touched on this branch with `.lean` proved has a probe witness committed |
| No new `I4-WITNESS-HASH-DRIFT` | Consumer's `upstream_witness_hashes` is in sync with on-disk witness SHA1 |
| No new `I9-HARDCODED-CODATA-DERIVED` | `compute_audit_scan.py` reports no new P31 hits vs `origin/main` |
| No new `I12-LEAN-REF-MISMATCH` | `bun run validate <paper>` passes |

## Domain-specific anti-patterns (extends parent)

- ❌ Auto-fixing wiring on someone else's PR branch. I-pattern
  hits on sibling PRs become a coordination comment (per parent
  §5i), not a force-push.
- ❌ Generating new probes for conjecture-class props (CLAUDE.md
  §3b). Their witnesses are axiomatic; skip in idle-sweep.
- ❌ Declaring "wired" based on docstring-only mention. A line
  `# uses prop:foo` in a comment is *not* wiring; the consumer
  must actually load the witness or compute the derived constant.
- ❌ Three-route-convergence claims — also rejected by
  `canonical-watcher`; restated here because the wiring step
  can mask them ("we wired it, look at the agreement!" when the
  routes compute different categorical objects).
