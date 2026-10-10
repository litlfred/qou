---
# qou-m549
title: 'Raw-float64 ratchet is RED on main: 5 witnesses, drained at the producer (PR #6453)'
status: completed
type: bug
priority: normal
created_at: 2026-09-03T20:35:04Z
updated_at: 2026-09-08T07:45:48Z
---

## Measured, and re-measured after main took 55 commits

`python3 computations/witness_raw_float64_audit.py --strict` on `origin/main`:

| head | NEW | REGRESSED | exit |
|---|---|---|---|
| `d502ed06ce` (2026-09-03) | 2 | 3 | 1 |
| `fbbd7d5364` | 2 | 3 | 1 |
| `2a7dfce761` (2026-09-03, +55 commits) | 2 | 3 | 1 |

Identical across all three, so no sibling has drained any of them and this is
not a stale reading. The five:

    NEW        4  computations/probes/arc-count-diagnostic-degeneracy.witness.json
    NEW        2  computations/probes/bpp-higher-a-sparse.witness.json
    REGRESSED  12 -> 22   computations/delta-n2-lp-dual-extraction.witness.json
    REGRESSED  89 -> 91   computations/audits/braid-encoding-audit.witness.json
    REGRESSED  18 -> 20   computations/meson-spectrum-predictions.witness.json

It was red in main's **own committed witness** too — `new_not_baselined: 1,
regressed: 1` from a run on 2026-08-31 — i.e. a red result was committed rather
than fixed, and that record is stale in the direction that *understates* it.

## Fix — PR #6453, `claude/ratchet-red-drain-2026-09-03` @ `43e0526fe5`

Merged onto `2a7dfce761`: clean merge, **NEW 0 / REGRESSED 0 / exit 0**.

Every witness re-run from its producer; none hand-edited. **No baseline entry
added, widened, or rebaselined.**

Four are bucket A (the `float()` cast IS the defect). One is bucket B
(`meson-spectrum-predictions`, float64 at the `build_seminormal_matrices`
library boundary) and is written at the double's own shortest exact width with
the limitation stated in the witness — the remaining 18 stay counted, because
draining them needs `build_seminormal_matrices` ported to mpmath, which moves
`m_K/m_pi`, the one scoreable L2 result. That is bean `qou-p77d` bucket B, not
a ratchet drain.

## TRAPs recorded

- **`seconds` is not a detector gap.** I first called `bpp-higher-a-sparse` one
  and proposed widening the audit's filter. Wrong: the carve-out matches
  *declared provenance names* from `_EPHEMERAL_META_FIELDS`, and
  `.data.rows[].seconds` is payload. Fixed at the producer by *renaming* to
  `elapsed_sec`. A `/time/` test would have excused 177 fields.
- **`fmt` is not universally right.** `_mpf50("493.677")` is correctly built
  from a string, but an mpf is *binary*, so `fmt` at 50 dps prints
  `493.677000...000169688486` — 59 digits of a quantity measured to 6. Same
  false-precision defect as float64 padding, reached from the other direction.
  `mp.nstr(x, 6)` for an experimental input.
- **A single witness field can carry two Python types.** In
  `braid-encoding-audit`, `d` is int `0` for a sigma letter and mpf for
  sigma-inverse; `c` is int `1` for isospin-symmetric letters and mpf `1` for
  the three colour-weighted p-n interfaces. `fmt` spells those differently, so
  a new exact-equality assertion read 84/161 until both slots were coerced
  through `mpf`. I had asserted in a docstring that `c` was always an int; the
  diff against `origin/main` said otherwise.
- **Committed value stale against an upstream that had NOT moved.**
  `markov_trace_assembly_chain` recorded `1.0653062285923893` while
  `markov-trace-assembly-proton.derivation.json` carries `1.1457596924573008`,
  identical on disk and on `origin/main`. A diff-keyed sweep cannot see this.
  The `qou-soj6` disagreement is **39.20% / 64.46%**, not the recorded
  43.46% / 76.88% — smaller than advertised, still four orders outside the
  derivation's claimed `1e-9`, so the finding stands.
- **The raw-float64 ratchet does NOT self-perturb**, contra a sibling's
  question on #6489: three consecutive runs on an unchanged tree (runs 2-3 with
  its own output already dirty) gave identical NEW 2 / REGRESSED 3. Mechanism
  is `SELF_OUTPUTS` / `SELF_OUTPUT_PREFIX` / `AUDIT_SUFFIX` at
  `witness_raw_float64_audit.py:102-128`. I then suggested porting the same
  treatment to `q0_anchor_ratchet.py`; **that suggestion was wrong** — it
  already imports `AUDIT_SUFFIXES` and filters at `_is_in_scope`. I asserted a
  gap from the shape of a report without opening the file.

## Status

Open, `mergeable_state: clean`, waiting only on merge permission. No CI run
exists (Actions are `workflow_dispatch`-only), so the ratchet IS the gate.

## 🛑 SUPERSEDED IN PART, 2026-09-04 — and one of my claims was wrong

**Five of the seven reds this bean claimed were landed on `main` by a sibling
on bean `qou-6sts`**, independently and with the same per-witness targets:
`6c5bb855a9` (arc-count + bpp), `eff0179cbd` (delta-n2 22->0), `c56548fd6c`
(braid-encoding 91->6 — my exact figure), `af5aecfe38` (meson-spectrum 20->0).

PR #6453 is re-scoped to the two they did not cover, both still red on `main`
@ `45c530378e`: `c2-diagonal-insertion-expansion-probe` (3) and
`probe-toroidal-legendre-weinberg-gate` (5). Superseded history preserved at
branch `superseded/ratchet-red-drain-pre-6sts-86546f5882`.

### The claim of mine that their fix refutes

I wrote, of `meson-spectrum-predictions`, that the residual 18 could not be
drained because it "needs porting `build_seminormal_matrices` to mpmath, a
shared-library change that would move `m_K/m_pi`, the one scoreable L2
result". **Both halves are wrong:**

- **No port was needed.** `build_seminormal_matrices_mp` already existed,
  returning `mp.matrix`, already in use by
  `deltalambda/deuteron_magnus_omega2_sign_probe.py`. I asserted a blocker
  without checking whether the exact path was already there.
- **`m_K/m_pi` moved only at the float64 floor.** K: `186.31985677437706`
  -> `186.319856774376948919338662479138`; eta-like `241.2126580626847` ->
  `241.212658062684446633141837881251`. ~15 sig figs agree, i.e. ~1e-15
  relative = ~1e-6 ppb against this observable's 264 ppb L2 target. The
  verdict is untouched; the old digits past the 15th were noise.

**TRAP the sibling identified and I had not:** numpy silently re-truncates an
`mp.matrix` back to float64, so routing an exact matrix through numpy looks
like exact arithmetic and is not.

### TRAP: a red witness may be STALE rather than defective — check the dates

`probe-toroidal-legendre-weinberg-gate`'s five raw float64 are all
`tolerance = 1e-40`, and `qou_substrate.witness._tolerance_literal` ALREADY
converts that to the string `"1e-40"` automatically. It did not fire because
the guard landed 2026-08-29 (`87d8367d55`) and the witness's `computedAt` is
**2026-07-06** — `0679303635` committed a two-month-old artifact without
re-running a producer that takes **0.8 s**. I nearly "fixed" `TOL_XCHECK` at
the producer instead, which would have been a code change papering over a
stale file. **Before fixing a producer, compare the witness's `computedAt`
against the date the relevant guard landed.**

### TRAP: a green delta is not a property of a branch

`main` was red on this gate at FOUR heads over ~24 h, and the set changed at
three of them: 5 -> 6 (c2) -> 7 (toroidal) -> 2 (after the sibling drain).
Two of the seven arrived after this branch was already green. Re-measure the
gate against the CURRENT head before quoting any before/after.


## FIFTH class, 2026-09-04 12:15Z — a wall-clock field the ratchet's vocabulary does not spell

`main` `9a8b09c661` -> `1a31748c96` took the gate NEW 5 -> **NEW 8**. All three
additions are one defect and none is a precision loss:

    /provenance/elapsed_s            = 0.923    qbeta-binding-law-options
    /provenance/elapsed_s            = 2.919    qbeta-tower-log-z-and-roast
    /data/matrix_route_seconds_at_A4 = 1958.9   qbeta-chain-closed-form

TRAP (durable). **The ratchet's wall-clock carve-out matches field names
EXACTLY, and its whole vocabulary is five strings** —
`witness_raw_float64_audit.EPHEMERAL_TIMING_FIELDS` = `durationMs`,
`durationSeconds`, `duration_sec`, `elapsed_sec`, `elapsed_seconds`. A timing
field under any sixth spelling is read as a payload float. This is the SAME
class as the `rows[].seconds` case earlier on this branch, one spelling over,
so treat it as recurring rather than incidental: when a red is a duration,
check the spelling before checking the arithmetic.

Corroborating, and the reason this is a detector gap rather than a producer
defect: `computations/witness_regen_classify.py:152` already lists
`"wall_sec", "elapsed_s", "elapsed_sec", "time_sec"` together as volatile. One
audit in this corpus recognises the spelling; the ratchet does not.

Fixed at the producer — two renames to `elapsed_sec` (key only, value
untouched), and `matrix_route_seconds_at_A4` serialized as the string
`"1958.9"` because it is a RECORDED cost of a prior matrix-route run, not a
measurement this run made, so no carve-out name would be honest for it.

DECISION DELIBERATELY NOT TAKEN: widening `EPHEMERAL_TIMING_FIELDS` to admit
`elapsed_s` is the one-line alternative and would silently excuse **14 further
`elapsed_s` sites** nobody has looked at. Left open; three probes do not settle
it.

TRAP (environment, unrelated to the ratchet). `qbeta_chain_closed_form_probe.py`
**crashed** under `PYTHONPATH=computations` alone —
`ModuleNotFoundError: No module named 'qou_substrate'` — and TRUNCATED its own
witness (175 lines -> nothing) on the way out. `qou_substrate` is not on PyPI,
so a bare container is the default; a producer importing it needs
`tools/qou-substrate/python` on the path too. Mirror image of the `_path_bridge`
trap (`qou-0e1t`): there `PYTHONPATH` MASKED a defect, here too little of it
MANUFACTURED one. Restore the witness from git before re-running, or the crash
looks like a drain.

Branch gate after: NEW 0 / REGRESSED 0 / exit 0. PR #6453 body updated to five
classes.


## 2026-09-04 20:50Z — main NEW 8 -> NEW 9 + REGRESSED 1; two more, both in existing classes

Head `1a31748c96` -> `46a986c804`. Branch back to NEW 0 / REGRESSED 0 / exit 0.

**Class 5, FOURTH site.** `qbeta-strand-multiplicity` `/provenance/elapsed_s
= 0.815` (`qbeta_strand_multiplicity_probe.py:316`). Four `elapsed_s` sites in
two days -- treat this as RECURRING, not incidental. When a red's value is a
duration, check the SPELLING before the arithmetic. Still fixed by renaming to
`elapsed_sec`, NOT by widening `EPHEMERAL_TIMING_FIELDS`; ~14 unexamined
`elapsed_s` sites remain and that decision is still open.

**Class 4 + class 3 TOGETHER, and this is the new lesson.**
`qbeta-ck-basis-constrained-pslq` 17 -> 18 is a one-character revert:

    bc8131bd58~1  18
    bc8131bd58    17   <- #5910 "drain: 1232 declared tolerances in 499 witnesses"
    origin/main   18

reverted by `9350fe0df4`, a merge of main into
`claude/q-riemann-hypothesis-gaps-zgxd8m` carrying a pre-drain copy -- the
same shape as the arc-count/bpp revert already in this bean.

TRAP (the part that is NEW). **"Re-run to restore a reverted drain" is only
valid when the sibling fixed the PRODUCER.** For arc-count/bpp it did.
Here it did not: I re-ran and the float CAME BACK, because #5910 edited the
ARTIFACT (`normalize_assertion_tolerance.py --apply`) while the producer
hard-codes `"tolerance": 1e-8` in a hand-built dict and `json.dump`s it. So
the discriminator before re-running is: **did the drain commit touch the
producer, or only the witness?** `git show <drain> --stat` answers it.

Fixed at the producer with the guard's own string
(`_tolerance_literal(1e-8) -> '1e-08'`, verified). The 17 baselined floats are
`log10` digit counts in the entropy budget -- untouched, still baselined, NOT
silenced; only the regression above the baseline is closed.

Spun out as its own bean: **`qou-9tqx`** -- the drain holds for 489/499, but
**26 of 33** producers with a float-literal tolerance hand-build, so each
undoes it on re-run. Ten already reverted, two fixed here, eight open.


## 2026-09-04 22:30Z — sixth and seventh sites, and I must CORRECT my own "14"

Two more arrived within ten hours (`qbeta-layout-conflict`,
`qbeta-disjoint-support-factorisation`), both `/provenance/elapsed_s`. Seven
sites in two days. Fixed by rename, as before; branch NEW 0 / REGRESSED 0.

**CORRECTION — the "~14 further `elapsed_s` sites" I used to justify NOT
widening the vocabulary is WRONG.** I quoted it in this bean, in two commit
messages, in PR #6453's body, and in a comment on #5910, and it was never
measured properly: it was a raw grep count taken BEFORE the seven fixes and it
included `computations/_deprecated/`.

Measured now, on the post-fix tree, excluding `_deprecated`:

    remaining `elapsed_s` sites            5   (not 14)
    of those, in a `provenance` dict       0
    of those, shape `round(time.monotonic() - t0, 3)`   0

    computations/level1-qvalues.py                      "elapsed_s": elapsed,
    computations/sigma_all_symbolic_decay.py            "elapsed_s": elapsed,
    computations/term5_v2_chirality.py                  "elapsed_s": elapsed,
    computations/staircase_ew_predictions.py            "elapsed_s": time.time() - t_start,
    computations/probes/qbeta_route76_modstd_reach_probe.py   "elapsed_s": 67.0,

**All five are wall-clock durations, and all five are now examined** — which is
exactly the condition my objection said was unmet. `67.0` is integral and the
ratchet already excuses it by design.

So the argument I gave against widening `EPHEMERAL_TIMING_FIELDS` does not
survive its own premise. That does NOT make widening right — it is a change to
the gate's declared vocabulary, and AGENTS.md is deliberately wary of anything
that turns a red green other than at the producer. It makes it an **owner
decision that is now cheap to state**, where before it was an agent guess
resting on a number I had not checked.

The live trade-off, both sides measured:

- **Keep renaming** (status quo). Each new probe that writes a provenance
  timing is a future red; observed rate ~1 per day, ~2 min each. Nothing in
  the gate changes.
- **Declare `elapsed_s`** in `EPHEMERAL_TIMING_FIELDS`. Ends the class. Excuses
  exactly the five above, all inspected, all genuine durations. Precedent
  exists in this corpus: `witness_regen_classify.py:152` already lists
  `elapsed_s` beside `elapsed_sec`, `wall_sec` and `time_sec` as volatile.

Recommendation (my judgement, not a finding): **declare it.** The vocabulary is
a list of names for one concept, not a precision tolerance, and it is already
inconsistent between two audits in this repo. But it is the owner's call and
the no-op is safe — renaming keeps working indefinitely.


**Narrowing my own contamination list (same day).** The correction above says the
bad "~14" figure also appeared "in a comment on #5910". **It did not** — checked
the comment text: it carries the tolerance-drain measurement (489/499, 26 of 33
hand-building producers) and never mentions `elapsed_s`. The real spread is
this bean, two commit messages on `claude/ratchet-red-drain-2026-09-03`, and
PR #6453's body. The first two are immutable; the bean and the PR body are
corrected.

Recorded because a contamination list is the half of a correction that gets
dropped, and I had just written a rule-shaped note saying so while getting my
own list wrong in the direction of over-claiming.


## RESOLVED 2026-09-05 — owner ruled "declare it"

Declared `elapsed_s` in `qou_substrate.witness._EPHEMERAL_META_FIELDS`
(`10fa6a5257`). ONE edit sufficed: `EPHEMERAL_TIMING_FIELDS` is derived by a
SUBSTRING TEST (`"dur"` or `"elapsed"`) over that mask, and `elapsed_s`
contains `"elapsed"`, so the ratchet picked it up with no second edit. This is
the EASY half of the two-half trap that function's own comment documents —
`wall_sec` contains neither substring and would need both halves; NOT added
(`qou-ywee`).

STABLE. It turns no red green, and the arithmetic closes:

    before (stashed)  NEW 0 / REGRESSED 0 / exit 0
    after             NEW 0 / REGRESSED 0 / exit 0
    total_fields      33968 -> 33946  (-22)
    ephemeral carved     50 ->    72  (+22)
    drained_files       190 ->   192  (+2)

Same shape as the 2026-08-24 integral-float reclassification; report it as a
reclassification, never as draining.

Blast radius checked: the mask also drives `_strip_ephemeral_fields`
(substantive-equality) and `_check_producer_takeover` (dropped-field guard).
A changed wall clock now reads as neither a substantive diff nor a dropped
field — correct for a duration, and exactly how `elapsed_sec` already behaves.
`qou_mass._internal.witness_base` IMPORTS the mask rather than restating it,
so the mirror-sync test passes with no second edit (asserted by hand; pytest
is absent in this container).

The seven producer renames stay — `elapsed_sec` is the longer-standing
spelling. The declaration is what stops the EIGHTH site being a red.


## MERGED — 2026-09-05, `87b8d0d693` (PR #6453)

Rebase-merged on the owner's explicit instruction. All 15 commits replayed
(`verify-merge-replay.py`, patch-id based: 15/15, MISSING 0). Branch NOT
deleted, per AGENTS.md rule 9.

**Gate on merged `main`: NEW 0 / REGRESSED 0 / exit 0.** `main` had been red
at twelve consecutive heads over ~50 hours.

### The eighth site — the ruling earned its keep the same day

The final rebase picked up 13 new `main` commits, and one of them brought
`computations/qbeta/qbeta-loop-value-pinned.witness.json` carrying
`/provenance/elapsed_s = 0.407`. That is the **eighth** site of the class,
and the **first to arrive after the declaration landed**. It was absorbed
with no producer edit at all — where sites one through seven each cost a
rename.

This is the datum my original objection lacked. I argued against declaring
on a count (~14 unexamined sites) I had never measured; the real count was
5, all wall-clock, all examined — which removed the objection's premise.
What actually settles it is the **rate**: seven in two days, an eighth
within the day of the ruling.

### TRAP — a raw float count is NOT the ratchet's metric

Caught while writing the merge rationale, and worth recording because the
mistake was one keystroke from being published as a verification.

Counting non-integral floats in the five renamed witnesses gives **1 each,
on the branch, after the fix**. That looks like the drain failed. It did
not: the rename moves the number under a field name the gate *excuses by
design* — the float is still in the artifact. The ratchet applies
`lp_dual` and `ephemeral_duration` carve-outs before counting; a naive
`isinstance(v, float)` walk applies neither.

So a raw count answers exactly one question — *did a sibling drain this
file?* — and answers nothing about redness. Use it for supersession checks
(where it is the right tool, and caught three superseded commits on this
branch); never quote it as a gate result.

### Left open, deliberately

- `qou-9tqx` — #5910's tolerance drain is artifact-level and structurally
  undoable: 26 of 33 producers hand-build their witness, so each re-run
  re-emits its float. Ten already reverted; two fixed here, **eight open**.
  Migrating 26 producers is its own tranche.
- `qou-ywee` — `wall_sec` is also a wall-clock duration in this corpus and
  is deliberately NOT declared. It needs BOTH halves of the two-half trap
  (the mask entry AND the substring test, which `"dur"`/`"elapsed"` do not
  reach), so declaring it blind would be a no-op that reads as a fix.

## 2026-09-08: canonical tracker for the recurring "raw-float64 ratchet is RED on main" event is qou-sknx (most recent OPEN one, 2026-09-04); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 6 / §7.3 C7. Seven beans (08-11 … 09-06) record one recurring event; this one is kept as-is because its body carries its own finding.
