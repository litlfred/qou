---
# qou-z23u
title: 'precision-gates is red on arrival: ten blocking gates, all inherited debt'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-03T15:43:09Z
updated_at: 2026-10-04T15:13:30Z
parent: qou-9nnz
---

## Measured 2026-09-03 on main `26bd234527` — and mostly already owned

**Check-before-work paid off: bean `qou-hah0` (in-progress) already owns this**
and has landed two of its fixes on main — `2b768409987` (the preflight only
checked `mpmath`, so 4 of 8 reds were phantoms dying on ModuleNotFoundError)
and `ba4c0cf3e1a` (a float64-padding red). Do not re-diagnose from scratch;
read that bean first. What follows is what is NEW since its 2026-08-30 run.

### The 18 "flips" were 1 flip and 17 unmappable LABELS (fixed, 82b2535ce8 + d2767e894e)

`Q0_FLIP` is documented as *"anchor and q0Value disagree"* — a checked
contradiction. One branch returned it when the anchor label could not be mapped
to a pin at all, where nothing was compared. 17 of 18 were that branch:
witnesses writing prose into the token field (`'proton (experimental pin)'`,
`'both: proton q_at() + muon q_muon_at() @ CODATA 2022'`).

This reconciles `qou-hah0`'s `Q0_FLIP 1` with today's 18 — the prose-labelled
witnesses landed after their run.

**And the producers were not careless: `stamp_staleness_metadata` had no reason
slot for a string anchor.** `q0AnchorReason` was written on exactly one path,
the `q0_anchor=False` branch. A producer wanting to say *why* had one field to
say it in. An API gap presenting as seventeen producer defects.

Fixed both ends: new `Q0_ANCHOR_UNRECOGNISED` verdict (still CI-failing —
"could not check" is never green — but counted apart from a real flip), and
`q0_anchor_reason` added to the helper with all 17 call sites split. All 17
re-run, 17 ok / 0 failed, **every computed number byte-identical** including
`q0Value`. `Q0_ANCHOR_UNRECOGNISED` 17 → 0.

### tower-walk probe: two gates, one root (producer fixed, WITNESS NOT REGENERATED)

`tower_walk_magic_replication_probe` sat in `never_raises_dps` AND
`witness_float64_padding` at once. Its comment says it aggregates 77 traces in
mpmath so float64 error does not compound — correct intent, not delivered:
**`mp.dps` on entry was 15**, mpmath's default, where an mpf sum accumulates
exactly as a float sum. Then it serialized with a bare `fmt`, default width
**60** digits, on values whose source is `float(abs(np.trace(st)))` — float64
by construction. 22 padded fields.

The halves pull opposite ways: raising dps fixes the arithmetic and makes the
serialization worse. Both fixed.

**The witness is stale until someone re-runs it with a real compute budget.**
Recorded runtime 40 min; this container measured 5 of 77 partitions in 434 s
for the first of five configurations. The walk touches no mpmath so the dps
raise costs nothing on the hot path — the machine is just slower.

### Still open

- **`hadron-knot-table` — the one real Q0_FLIP.** `qou-hah0` settled the
  direction (audit right, witness stale, per the CODATA-2022 migration) and
  says to claim it separately: its producer runs >50 min for one bound atom
  before its own timeout. Not an idle-pass fix.
- **1 false positive in the padding audit**: `hardcoded-literal-audit.witness.json`
  `data.rows[349].hits[0].literal` is a literal that audit FOUND in source and
  recorded as evidence (`matches_constant: AME_B_TRITIUM_MEV_VALIDATION`). The
  detection is sound — it IS a double's expansion — but the padding audit
  cannot tell a quoted number from a computed one. Wants a declared
  quoted-evidence carve-out in the style of `precision_tier`, counted apart.
- 4 NEW `never_raises_dps` producers (31/6/3/2 constructions), 10 NEW q0-value
  drifts all at −0.0769 ppb (the CODATA-2022 anchor migration; scoped under
  `qou-3f7a` / `qou-tekx`), 3 raw-float64 regressions, 69 NEW unstamped.


## Result: 10 blocking reds -> 8, and the two that went green were one root each

Measured with the full `scripts/precision-gates.sh` on this branch.

**Green: `float64-padding ratchet`.** 70 padded occurrences -> 12, NEW 58 -> 0,
exit 1 -> 0; everything left is under baseline and in `_deprecated`. Four
fixes, and only the first was cosmetic:

1. `tower_walk_magic_replication_probe` — 22 fields. Aggregated in mpmath
   "so float64 error does not compound", at `mp.dps` **15**, where an mpf sum
   accumulates exactly as a float sum. Then serialized with a bare `fmt`,
   default width **60**, on values sourced from `float(abs(np.trace(st)))`.
   The halves pull opposite ways — raising dps fixes the arithmetic and makes
   the serialization worse — which is why it sat in TWO gates at once.
2. `qbeta_three_nucleon_nf_alpha_spread_probe` — `mp.mpf("0.99839767")` is the
   RIGHT idiom, defeated by ORDERING: module scope, dps still 15, so the mpf
   held the 53-bit double; `main()` raised dps to 50 and `str()` printed that
   double out to fifty digits. The code looks correct on its own line.
3+4. `path_b_defect_binding_probe` / `path_b_habiro_mass_probe` — **not
   cosmetic**. `M_AME` was a MIXED dict (`"n"` mpf from the registry, five
   siblings bare floats) feeding a binding energy computed as ~1876 − ~1876 ≈
   1e-5 MeV. Catastrophic cancellation, measured at **2.525e-9 relative**, and
   the witness moved by exactly that: `B_AME_MeV`
   `0.000001270690003244…` -> `0.000001270689999999…`. The padding flag was a
   SYMPTOM of a real numerical defect, not fake precision over a right answer.

   Did NOT swap in the registry's `M_D_MEV_VALIDATION` though the producer
   already imports two registry constants: those are NUCLEAR masses
   (1875.61294500), these are ATOMIC (1876.12393). The tidy-up would have
   silently changed what is compared.

**Green: `import-time dps ratchet`** — fix (2) is one of its sites.

**`q0-anchor flip` still red, but honestly: 1, not 18.** The 17 unmappable
labels are gone (see above) and the remainder is `hadron-knot-table`, which
`qou-hah0` says to claim separately with a real compute budget.

The last padding NEW was a **false positive** and is now carved out:
`hardcoded-literal-audit.witness.json` records literals it FOUND in source as
evidence. The mechanism already existed and already held two other audits'
witnesses — only the name was wrong (`SELF_OUTPUTS` for a set that was never
just self-output). Renamed `QUOTED_EVIDENCE_WITNESSES`, kept a LIST rather than
a heuristic (a "looks like evidence" test is what would let real padding hide),
and it now reports itself by name, since an exclusion nobody can see is
indistinguishable from a hole.

### Still red (8), none touched by this work
`q0-anchor flip` (1, needs a compute budget) · `q0-anchor refill ratchet`
(owned by `qou-fl0a`) · `never-raises-dps` (3 NEW) · `raw-float64` (3 regressed)
· `q0-value drift` (10 NEW at −0.0769 ppb, scoped under `qou-3f7a`/`qou-tekx`)
· `CODATA stale-edition` · `mixed mpf/f64` (1 over baseline) · `witness
scriptFile provenance` (1 NOT_A_PRODUCER).


## 10 -> 7 blocking reds. Third gate green: `never-raises-dps`

**The two remaining NEW producers were FALSE POSITIVES**, and the audit's own
docstring contains half the reason:

  > `mp.dps` is GLOBAL STATE, so an imported helper legitimately inherits the
  > precision its caller set.

Correct, and enforced by `is_runnable()`. The state flows the OTHER way too. A
runnable producer doing `import X`, where X calls `set_compute_dps()` at module
scope, has dps raised before a line of its own code runs. MEASURED by importing
each candidate's module-scope imports and reading `mp.dps`:
`magnus_sign_row_truncation_probe` and `magnus_tr_decay_perpair_cluster_probe`
both go **15 -> 140** via `he4_magnus_omega2_sign_sparse_probe`. Reported as
computing at 15 with 34 constructions; they compute at 140.

Careful NOT to reopen `qou-nk3h`/`qou-txru`: that removed clause asked whether a
raiser NAME appeared in an import, which proves nothing (`chi_sym_alt_closed_form`
imported one, never called it, ran at 15, took the padding ratchet red). This
asks whether the IMPORTED MODULE'S OWN CODE calls a raiser at module scope.
Self-test cases for both distinctions; 9 -> 13 cases.

Reported, not silently exempted — the header names each file and what it
inherits from, because that inheritance is fragile.

### 🛑 The real find here is not a gate: `e-0-lp-dual-h3.witness.json` is STALE ON MAIN

Committed: `positive_cone_strong_duality_worst_relative_gap = 1.42400633925e-50`,
`passed: true`. Re-run from a **pristine checkout, no edits**:
`8.87357464011e-14`, `passed: false` against `tolerance="1e-15"`. All eight
recorded duality gaps moved ~33 orders (`proton_net` 1.04e-48 -> 8.99e-15).

A production LP's strong-duality check has been failing for some time and the
committed witness says it passes. Nothing gated: the witness-failed-assertion
ratchet is ADVISORY. **Which rank treatment is right is a numerics question
about a production LP and is NOT settled here** — it needs someone with the
budget to answer it. Witness regenerated so the corpus records reality.

**My own retraction, recorded because the reasoning was seductive.** I first saw
that shift right after adding `set_compute_dps()` and wrote a confident
mechanism: global dps widens the LP's input strings, `_input_dps` raises derived
precision, the pseudo-inverse cutoff moves ~1e-12 -> ~1e-56, different singular
values count as zero. Plausible, specific, and **wrong** — the pristine run gives
the identical failing value. I got as far as writing it into a source comment
before running the one experiment that settles it. **Run the unmodified producer
FIRST** when a number moves after your edit; it is one command and it is the only
thing that separates correlation from cause.

### Still red (7)
`q0-anchor flip` (1, needs compute budget) · `q0-anchor refill` (`qou-fl0a`) ·
`raw-float64` (3 regressed) · `q0-value drift` (10 NEW, `qou-3f7a`) ·
`CODATA stale-edition` · `mixed mpf/f64` (1) · `witness scriptFile provenance` (1).


## Session 3: mixed mpf/f64 green, raw-float64 regressions drained, q0 unrecognised → 0

**`mixed mpf/f64` — green (1 → 0).** `winner_vs_fusion = abs(best_a[1] -
fusion_sum)` in `meson_gmor_derivation_probe`, reported at 18 digits against
`tolerance="1e-30"`. `best_a` is `(name, value, miss_pct)`: `value` is mpf,
`miss_pct` is a float used only for selection and printing. Taint works on
NAMES, so one float element taints the tuple and the mpf-only subtraction gets
flagged. Unpacked into its own name — NOT marked `float64-intentional`, which
would record a deliberate f64 measurement this is not. Witness byte-identical
apart from an environment stamp.

**`raw-float64` — the 3 REGRESSED drained to 0.** All three arrived on bulk
drains that ADDED assertion/payload fields as bare Python floats
(`computed=float(x)`, `expected=0.1228605135`, `tolerance=1e-8`); each producer
already imported `fmt`. delta-n2 22→12, braid-encoding 91→89, meson-spectrum
20→18, all back to baseline.

Three mistakes worth carrying forward:
- **A regex over source is not a refactor.** `tolerance=<num>` matched
  `target_tolerance=1e-9` INSIDE AN F-STRING and produced a SyntaxError.
  Reverted; done by exact line match.
- **Serializing changes what you can compare to.** The kaon lookup keyed on
  `r["m_PDG_MeV"] == pdg["K±"]` broke once the payload was formatted — string
  vs mpf, StopIteration. Now keyed on `pdg_key`. An identity test on a label
  survives a change of representation; an equality test on a number does not.
- **`git checkout -- computations/` after a gate run reverts your own source
  edit** along with the audit witnesses, silently. `qou-hah0` recorded this and
  I did it anyway. Scope the revert.

**The gate is still red on a DIFFERENT bucket, and all three look legitimate
rather than defective** — an owner call, not a drain:
- `arc-count-diagnostic-degeneracy` carries `r2_ame_vs_arc_exact` **beside**
  `r2_ame_vs_arc_float`; the float is a convenience rendering.
- `c2-diagonal-insertion-expansion-probe` carries `{"ratio": "372/365",
  "float": 1.019…}` — the exact rational is right there.
- `bpp-higher-a-sparse` has `rows[].seconds`, wall-clock timing. The audit's
  own duration carve-out matches only names containing "dur"/"elapsed" (its
  comment says so explicitly about `wall_sec`), so `seconds` slips through.

None is widened unilaterally: this codebase requires a carve-out to be
DECLARED by the producer, not inferred by the auditor.

**q0-anchor `Q0_ANCHOR_UNRECOGNISED` 1 → 0** — `q0_anchor=True` stamped a
boolean. `False` means "independent", which makes `True` look like its
complement; it is not, so it fell through to the string path. The producer's own
comment said "the bond factors ARE evaluated at the proton pin". Fixed at the
producer AND guarded in `stamp_staleness_metadata`, which now raises on `True`.
Second API-shape defect in that one function this session, both presenting as
producer errors.

**`witness scriptFile provenance` — the NOT_A_PRODUCER is NAMED**, which
`qou-hah0` could not do: `--list NOT_A_PRODUCER` is the flag it was looking
for. It is `b1-kappa-window-extension.witness.json` →
`wlambda_covariance_epic_B1_kappa_window_extension.py`, a script that computes
exactly the right thing and **only prints** — the commit that added the witness
added no script at all, and `durationMs: 53` on a ~28-min compute confirms it
was hand-assembled from stdout. Every derived field was verified reproducible
from `rows` alone (all 8 `windowed_exponents` and the secant, exactly), so the
script now emits its own witness; confirming run in flight.

## BASELINE re-measured 2026-09-05 on main `7904384c45` — **nine**, was ten

Run: `PYTHONPATH=computations:tools/qou-substrate/python:tools/pyhecke/python bash scripts/precision-gates.sh` in a pristine `git worktree` at `origin/main`. **Exit 1.**

```
RED: q0-anchor flip  q0-anchor refill ratchet  import-time dps ratchet
     never-raises-dps ratchet  float64-padding ratchet  q0-value drift ratchet
     CODATA stale-edition  hardcoded braid word (self-test)
     mixed mpf/f64 -> serializer
```

Nine, against the ten of 2026-09-03 on `26bd234527`. **I cannot name which one left**, because this bean records the *count* and not the list — so the nine are written out above, and the next re-measure can compute its own delta instead of inheriting mine. Advisory set unchanged (4).

**None of these are phantoms of the `qou-hah0` class.** All three modules import: the same run with a bare `python3` (no `PYTHONPATH`) produces the *identical* nine-name list, and `pyhecke` is not importable bare — so on this container the preflight-phantom hypothesis and the real-red hypothesis are observationally identical at the RED line, and only the pristine-main baseline separates them. **That is a trap worth recording: a matching RED list is not evidence the reds are real.** Run the baseline.

### Consequence for branch verification, which is why this was measured

Branch `claude/phi-k-is-not-a-trace-retraction-2026-09-05` at `9f0f7709b3` (`--changed`, 12 relevant files) gives exit 1 with **exactly this nine-name list** — byte-identical to pristine main. So the branch contributes nothing to it, and a gates run on a feature branch here **cannot** be reported as a pass/fail signal about that branch. The usable per-branch evidence is the narrower one: the raw-float64 ratchet witnesses regenerate with the new file absent from all of them.

**Do not let this be read as licence to skip the gates.** It says the *summary line* is uninformative on a branch while main is red; the per-gate diff against a main baseline still is informative, and is the check to run.

## BASELINE re-measured 2026-09-07 on pre-merge main `1ec22a904` — **ten**, was nine

The 2026-09-05 entry above wrote out its nine names precisely so the next
re-measure could compute its own delta instead of inheriting a number. Doing
that, and the delta is **+2 blocking, −1 blocking→advisory**:

```
RED: q0-anchor flip  q0-anchor refill ratchet  import-time dps ratchet
     never-raises-dps ratchet  float64-padding ratchet
     reference-literal ratchet          <- NEW since 7904384c45
     witness-value copy ratchet         <- NEW since 7904384c45
     q0-value drift ratchet  CODATA stale-edition
     mixed mpf/f64 -> serializer

ADVISORY: witness failed-assertion ratchet   hardcoded braid word   <- was RED
          f64-into-mpmath   no-free-parameter cert
          witness provenance completeness
```

Run in a pristine `git worktree` at `1ec22a904` with `PYTHONPATH` set — the same
method as the 2026-09-05 baseline, so the comparison is like-for-like. **Exit 1.**

`hardcoded braid word` moved RED → ADVISORY; two ratchets appeared. Net 9 → 10.
Neither new name is attributable here — main moved **683 commits** between the
two baselines — but they are now on the record by name, so the next re-measure
has a two-point series rather than a pair of counts.

### The reason this was run: it cleared four of my own merges

PRs #6817 / #6821 / #6826 / #6948 all reported `exit 1` with a ten-name list,
which on the 2026-09-05 nine-name baseline looked like **+2 introduced by me**.
It is not: pre-merge main alone produces the identical ten names and the
identical advisory set. The four merges contribute **nothing** to the blocking
gates.

That is exactly the check the 2026-09-05 entry prescribes — *"the summary line
is uninformative on a feature branch while main is red; the per-gate diff
against a main baseline still is, and is the check to run"* — and it is the
first time the prescription has been followed and has actually changed a
conclusion. Without it I would have reported an inherited red as my own
regression, or (worse) waved the exit code away as "known debt" and been right
by luck rather than by measurement.

### One environment note

This container needed `mpmath`, `numpy`, `scipy`, `sympy` and `pip install -e
tools/qou-substrate` before the gate would run at all — without them the
preflight **refuses** rather than reporting green, which is the guard behaving
correctly and is worth not "fixing".


## RE-MEASURED 2026-09-11: pristine main is ELEVEN blocking gates, was ten

Full `scripts/precision-gates.sh` (no --changed) in a throwaway worktree at
origin/main 492a90a42, unpiped exit = 1:

  RED: q0-anchor flip | q0-anchor refill ratchet | import-time dps ratchet |
       never-raises-dps ratchet | float64-padding ratchet | raw-float64 ratchet |
       reference-literal ratchet | witness-value copy ratchet |
       q0-value drift ratchet | CODATA stale-edition | mixed mpf/f64 -> serializer

Eleven. The bean's own lesson applies to its own figure: quote the LIST, not the
count, so the next re-measure computes a delta against named gates instead of
inheriting a number. Ten -> eleven cannot be attributed here because the earlier
entry recorded nine/ten names only partially.

TRAP measured the same day: `precision-gates.sh | tail -N` returns TAIL's exit
code. A run piped that way reports `exit 0` while the script itself exits 1.
Read the `^RED:` line; never the exit status of a pipeline.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-11 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
