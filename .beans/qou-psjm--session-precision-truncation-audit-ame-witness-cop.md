---
# qou-psjm
title: 'Session: precision-truncation audit — AME + witness-copy classes, HARD GATE wiring, drain queue'
status: in-progress
type: milestone
priority: normal
created_at: 2026-09-05T12:02:04Z
updated_at: 2026-09-06T04:05:32Z
---

## 2026-09-05 — detector extended, wired, calibrated (branch claude/precision-truncation-audit-sidecar-r5vjkx)

`codata_truncation_audit.py` already existed (#4960, qou-46ke) and was in NO
array — nothing had run it for three weeks. Now a blocking entry in
`scripts/precision-gates.sh`, verified running in the harness.

Four defects fixed, three of them the gate's own defect class:

1. **The canonical was itself truncated.** `str(Q_MP)` renders at ambient
   `mp.dps` = mpmath default **15** at import, so canonical q0 was 15 of its
   50 digits. `classify()` asks `canon.startswith(lit)`, so every q0 literal
   LONGER than 15 digits was reported CLEAN — and long literals are exactly
   the hand-copied ones.
2. **Prefix-only cannot see a WRONG value.** Added `DIVERGENT`, decided on
   the VALUE not the string SHAPE.
3. **No AME coverage.** Added the 7 AME2020 binding energies. 492 of the
   findings are AME.
4. **Two false-positive classes**, caught by re-measuring before shipping:
   `ROUNDED` (correct round-to-nearest, ~20x over-flag) and the MUON pin
   (11.6 ppb from proton, inside tolerance — 195 correct literals scored
   wrong until the muon anchor got its own CANON row).

Measured: **970 blocking in ~500 files** (450 TRUNCATED / 498 DIVERGENT /
22 ROUNDED), 305 exact duplicates not blocking. Baselined; NEW arrivals block.

### CONFIRMED: scripts copy a deprecated witness rather than load it
`8.481798`, `7.718043`, `28.295673` are all present in
`qou-mass/src/qou_mass/data/_deprecated/ame-2020-binding-energies.witness.json`
— the hand-maintained file `codata_constants.py` says "had drifted on
5Li/7Li/9Be" and which was eliminated as a source of truth. ~190 live script
literals are copies of that stale witness. This is the user's own hypothesis,
verified.

### OPEN
- The 970-item drain (value-changing; overlaps qou-46ke / me3r / ce18).
- A general witness-copy detector (class C) — phenomenon confirmed, detector
  not built.
- Scope: `scan()` walks `computations/` only — not `tools/`, not `qou-mass/`.


## 2026-09-05 — drain + witness-copy gate landed (PR #6857, issue #6856)

**Drain (owner-approved: AME + CODATA-edition).** 372 literals routed to the
registry across 178 files. AME 492 -> 55 (89%); total blocking 549 -> 201.
Baseline shrank by draining: 357 removed, 0 added.

Three defects in the drain tool, each caught by measuring:
1. Import placed before the `sys.path` bootstrap — the `qou-0e1t` ordering
   defect reintroduced by the cleaning tool. Broke 5 of 40.
2. Anchoring to any `sys.path` line landed inside indented blocks; the parse
   guard skipped 112 of 212 files — an eighth of the job, reported as success.
3. 11 files still unreachable; every touched file was EXECUTED, and those 11
   reverted. Un-drained is backlog; broken is regression.

**Baseline key is (file, literal) -> count, never line number.** Line numbers
shift when a drain inserts an import; the first pass reported 10 unchanged
findings as NEW.

**Float64 ratchet fired on a net-positive change and was right to.** The
verification pass regenerated 109 witnesses as a SIDE EFFECT, draining raw
float64 from 204 of them while regressing 3. The 3 are reverted, not baselined.

**Witness-value copy audit (class C) — NEW, `computations/audits/`.** 11-digit
floor; SPREAD separates one-producer output (NARROW, 264 in 172 files) from
shared reference constants (587, owned by the other gate). 17 NARROW copies
come from a `_deprecated/` witness. Ratchet blocks NEW; wired blocking.

NOT shipped: an annotated-vs-silent split of the 264. Some are deliberate
freezes; my comment-window detector got the type case wrong (note 6 lines up,
window 4). Left for a hand pass rather than shipping an indefensible number.

### STILL OPEN
- 201 reference-literal findings: 119 q0/muon (outside approved scope; 81 match
  neither anchor and need triage against the three documented muon values),
  55 AME, 27 CODATA.
- 264 NARROW witness-copies need the deliberate-vs-accidental hand pass.
- ~70 touched producers carry stale scriptHashes.
- 23 files skipped by the drain's parse guard; 11 reverted as unreachable.
- Both audits scan `computations/` only — not `tools/`, not `qou-mass/`.


## 2026-09-05 — the q0/muon triage RESOLVED by measurement (PR #6885)

I had left this as "needs an owner ruling on which muon value is canonical".
That question was premature: `qou_substrate/constants.py` already answers it,
and the answer is that TWO values are legitimate.

- `Q_MUON_50_DIGIT_STR` — FROZEN by design, so a witness stays reproducible
  against its own history.
- `q_muon_at()` — RE-DERIVES from MASS_RATIO_MU_E_STR, moves with CODATA.
- They differ by 0.0769 ppb. Both correct, for different callers.

The gate carried only the frozen one, so literals written against the live
derivation scored DIVERGENT (wrong) when they are what today's CODATA implies.
Of 125 q0 findings, 77 are exact prefixes of one of four legitimate values
(41 proton / 17 frozen / 13 ancestor / 6 live). Adding the live row:
TRUNCATED 97 -> 102, DIVERGENT 99 -> 93.

**The 17-digit ancestor is deliberately NOT legitimised** — constants.py names
it as the defect population (336 files, "a literal cannot drift from a source
it does not have"). Pinned as DIVERGENT by fixture.

### My own errors this pass, all caught before landing
1. First framed it as "the canonical is stale" — WRONG, retracted. Frozen by
   design, documented as such.
2. `_canon_str` fixed at 50 digits truncated the 70-digit live canonical —
   the THIRD silently-short canonical in this gate's history. A round-trip
   rule fixed that and broke the other end (M_E_MEV -> 110 digits of binary
   noise). Precision is now stated per row.
3. Rendering 70 digits from a 60-dps value exposed ~10 digits of noise that
   moved with ambient precision. Now derived at 90 dps, and it reproduces
   q-pinning-50-digit.witness.json to all 70 digits exactly.
4. The EXACT fixture re-derived its expected value and so disagreed with the
   row it existed to pin. It now READS the CANON row.


## 2026-09-06 — scope extension (PR #6885), and what is NOT in it

**Reference-literal gate extended** to `tools/`, `qou-mass/`, `scripts/`.
219 baselined (+13), 0 pre-existing counts grew. REGISTRY_FILES extended with
the package-layer registry so the canonical values are not reported.

**Owner-gated finding, not fixed:** `qou-mass/src/qou_mass/api.py:232` carries
`u_MeV = 931.49410242` — CODATA **2018** — in the PUBLIC facade, while
codata_constants.py moved deliberately to the 2022 value 931.49410372 (me3r,
2026-06-30). The external-researcher API is one edition behind the registry it
wraps. Value-changing and owner-gated (me3r / ce18).

Other newly-visible, each needing a different disposition, hence baselined:
4x `q0 = 1.10997858` (drainable); 3 files under `qou-mass/.../_internal/`
which is GENERATED — fix at source in computations/ then re-sync, never
hand-edit; 1 test fixture; 2 detector scripts holding values as patterns.

### MEASURED but deliberately NOT added to #6885
Extending `witness_value_copy_audit` the same way yields **9 NARROW in 5
files**, of which **3 are test files whose literals are the tests' own
assertion targets** for the precision machinery
(`assert str_at_true_precision(v) == "1.5597586581034242"`) — subjects, not
stale copies, so `tests/` needs excluding. Net actionable: **2 files**
(`qou_mass/api.py`, `_internal/y_lambda_su_n.py`).

Held back because #6885 already carries three distinct changes (muon
two-value fix, two ratchet regressions from main, reference-literal scope)
and is blocked on the draft->ready rate limiter. Adding a fourth would grow
it for no gain. Do this as a follow-up.

### Merge blocker
`update_pull_request(draft: false)` on #6885 returns "API rate limit already
exceeded for user ID 662242" — the AGENTS.md 8a GraphQL node-lookup limiter.
Failed 4x. Retry armed (trig_01EtnrNRzCWvErGYjKLT9Z67). NEVER close-and-reopen.
The user granted merge permission ("Merge and continue", 2026-09-06).
