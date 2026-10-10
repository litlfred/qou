---
# qou-g7z6
title: Drain the mass-endomorphism sidecar backlog (126/126 stale)
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T12:04:07Z
updated_at: 2026-10-04T15:18:55Z
parent: qou-mub3
---

Surfaced while verifying #6016, not caused by it.

`bun run folio-assistant/content/pipeline/qa-staleness.ts content/quantum-observable-universe/mass-endomorphism`
reports **126 blocks; fresh=0, stale/partial=126** on 2026-08-29. Pre-existing.
#6016 refreshed exactly one sidecar — the block whose `.lean` it renamed — and
reverted the other 127 so a rename PR did not become a chapter sweep.

**Why this is a batch audit run, not idle-pass work.** A chapter-scoped
`qa-sweep` rewrites all 128 sidecars in one go, which AGENTS.md explicitly
sanctions as a single bulk commit ("regenerate N sidecars after checker fix")
— but the idle-backlog policy caps a pass at ≤ 10 sidecars, so this does not
fit there.

**Most of it is not mechanical.** The stale sets are dominated by
agent-reviewed criteria — `da-*` (13 of them), `voice-*`, `proof-rater-*`,
`expo-milnor-clarity`, `milnor-brevity` — which a sweep marks
`[needs-agent]` rather than resolving. The script criteria re-run cheaply; the
agent ones are the actual cost, and whoever takes this should scope that first.

Two measured cautions for whoever does:
- `qa-sweep` / `qa-staleness` take a **directory**; a file path dies `ENOTDIR`.
- Never hand-edit a sidecar to clear staleness.

Unclaimed as of 2026-08-29; opened so it is not lost in a chat transcript.


---

## 2026-08-29 — SCOPED. The split is 37 % mechanical / 63 % agent

The bean asked whoever took this to scope the agent share first. Measured, on
`origin/main`:

    126 blocks, ALL `PART` (none fresh, none wholly stale)
    3,130 stale criterion-occurrences over 98 distinct criteria

      automated (script, cheap re-run)   1,155   36.9 %
      agent-reviewed (the real cost)     1,975   63.1 %   over 39 distinct criteria
      unresolved                             0    0.0 %

So the bean's qualitative call — *"most of it is not mechanical"* — is right,
and the number is **63 %**, not a handful of criteria.

**Classify by the registry's `automated:` field, not by the name prefix.** The
prefix is not a reliable guide: `proof-*` splits across both kinds
(`proof-lean-compiles` is automated, `proof-rater-novelty` is not), and the
whole `trap-*` family is agent despite looking like a lint. Source of truth is
`folio-assistant/content/pipeline/qa-criteria-registry.ts`, which carries
`automated: true|false` on each of its 121 entries (80 automated, 41 agent).

**A parser caution, because it bit here and it is the usual class.** A first
pass matched whole registry entries with `\{\s*id:\s*"..."(.*?)\n  \}` and
silently dropped **41 % of the occurrences** into "not in this registry" —
every `da-*` and every `trap-*`, i.e. exactly the agent-heavy families whose
size is the question. They were in the registry all along; the entry-boundary
pattern did not match them. Walking `id:` markers and taking the first
`automated:` before the next `id:` resolves all 98 criteria with none left
over. If a scoping run reports a large unclassified bucket, suspect the parser
before believing the bucket.

**Heaviest agent criteria** (occurrences): `fit-section-chapter` 95,
`da-false-claim` 95 and each of the twelve other `da-*` at 95, `milnor-brevity`
76, `expo-milnor-clarity` 76, then the `proof-rater-*` trio and the
`proof-no-*` family at 33 each.

### What this means for whoever drains it

- The **mechanical 37 %** is one sanctioned bulk `qa-sweep` over the chapter
  directory — AGENTS.md permits the single bulk commit for exactly this.
- The **agent 63 %** is not drained by that sweep; it is *marked*
  `[needs-agent]`, which converts a silent backlog into an explicit queue of
  ~1,975 judgements. That is a real budget, and it should be a deliberate
  decision rather than a side effect of running the sweep.

Not run here: firing a 128-file sidecar rewrite that also opens a ~2,000-item
agent queue is a scoping decision for the owner, not an idle-pass action. The
measurement above is what was missing to make that decision.


---

## 2026-08-29 — the mechanical half is RUN, and the prescribed remedy is
## weaker than this bean assumed

Ran `qa-sweep` over the chapter directory. It works, but not the way the
bean (or my own scoping entry above) described it.

    total stale+missing   5,854 -> 4,967   (-887)
      everything else     5,575 -> 3,833   (-1,742)
      detangler family      279 -> 1,134   (  +855)

    1,015 criteria newly evaluated (810 n/a, 205 pass)
       37 verdict transitions: 16 fail->pass, 10 pass->n/a,
          6 warn->pass, 5 pass->fail
      129 sidecars

**Do not quote the -887 alone; it understates the work by 2x.** The real
movement is -1,742, masked by a +855 regression confined entirely to the
nine `detangler-*` criteria plus `foreshadows-point-forward`, each of which
goes from a handful of stale blocks to all 126.

**Three corrections to my own scoping entry above.**

1. **"The mechanical 37 % is one sanctioned bulk sweep" is not the whole
   truth.** Of 1,155 automated stale occurrences, the sweep took 49
   distinct criteria to zero — but the aggregate moved only 1,155 -> 1,139,
   because the detangler family absorbed the gain. Whether a criterion is
   `automated: true` does **not** by itself predict that `qa-sweep` will
   resolve it.
2. **The detangler regression is not the sweep writing placeholders**, which
   was my first hypothesis. Checked at the entry: the new detangler entries
   are real script verdicts with fresh `script_hash`es —
   `detangler-no-forward-ref` moved `fail -> pass` on a genuine
   re-evaluation, and `foreshadows-point-forward` went from ABSENT to a
   real `n/a`. **`qa-staleness` reports them stale immediately after
   `qa-sweep` wrote them**, so the two tools disagree about freshness for
   this family. That is an open item (below), not something to paper over.
3. **Block-level status cannot move here and that is expected.** Still
   126 PART / 0 fresh, and it will stay there while the agent 63 % is
   unworked: a block is fresh only when *every* criterion is. Do not read
   "126 PART" as "the sweep did nothing".

**Five new failures, all real.** `voice-author-notes-pollution` flipped
pass -> fail on `categorical-mass-markov-proof`, both
`qbeta-canonical-markov-weights-explicit-instance` blocks, and both
`qou-motivic-galois-instance` blocks. One checker got stricter; these are
genuine one-voice findings for whoever drains that axis.

### Still open

- **The agent 63 %** (~1,975 judgements over 39 criteria) — untouched, and
  the sweep marks rather than drains it. Unchanged from the scoping entry.
- **NEW: `qa-sweep` and `qa-staleness` disagree on the detangler family.**
  A criterion written by the sweep, with a current `script_hash`, is
  reported stale by the staleness scanner on the same tree. Until that is
  resolved, the detangler bucket cannot be drained by any number of sweeps,
  and its count is not a meaningful backlog signal. Worth its own bean if
  anyone takes the detangler axis.


---

## 2026-09-03 — CLAIM RELEASED. Mechanical half done; agent half unclaimed.

Returning this to `todo`. It has sat `in-progress` under my claim since
2026-08-29 with no commit against it for five days, which under the
stalled-claim policy makes it a takeover candidate — but it reads to a sibling
as active work, so the honest move is to release it rather than let someone
route around a claim nobody is working.

**Done, landed on `main` in #6021:**

- Scoped: 3,130 stale criterion-occurrences over 98 criteria — **36.9 %
  automated / 63.1 % agent-reviewed**, 0 unresolved.
- Ran the mechanical `qa-sweep`: total stale+missing **5,854 -> 4,967**, of
  which the real movement is **-1,742** masked by a **+855** detangler
  artefact. 1,015 criteria newly evaluated, 129 sidecars, 5 genuine new
  `voice-author-notes-pollution` failures.

**Re-measured today on `d502ed06ce9`, and it has drifted back:**

    stale=3339  missing=1853  total=5192     (I left it at 3114/1853/4967)
    blocks: 126 PART, 0 fresh                 (unchanged)

**+225 in five days, ~45/day.** So the mechanical sweep is not a one-time fix
for this chapter either; it erodes at roughly the rate of ordinary editing.

**What remains, and the one thing to settle first:**

1. **The agent 63 %** — ~1,975 judgements over 39 criteria. A budget, not a
   task, and one chapter of ~36.
2. **🛑 Do not start (1) until `qou-grph` is settled.** An unknown slice of that
   63 % is graph-invalidated and **cannot be reported fresh no matter how many
   judgements are spent on it** — `qa-staleness.ts` never computes the `graph`
   hash, so nine criteria are permanently stale by construction (re-verified on
   folio-assistant `origin/main` 2026-08-31: still zero occurrences). Spending
   ~2,000 judgements against a bucket with a structurally unclearable slice is
   the expensive form of the mistake `qou-grph` documents.

Unclaimed as of 2026-09-03. Whoever takes it should re-measure rather than
quote the figures above — they moved 4.5 % in five days.
