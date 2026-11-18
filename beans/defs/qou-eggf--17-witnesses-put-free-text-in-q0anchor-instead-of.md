---
# qou-eggf
title: 17 witnesses put free text in q0Anchor instead of the token; the vocabulary cannot parse it
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-03T04:57:50Z
updated_at: 2026-10-04T15:11:42Z
parent: qou-5vkl
---

## The finding

`q0_anchor_consistency_audit.py` on `main` (`8ddfeaf1b7`) reports **18
`Q0_FLIP`s**. Only **one** is a genuine anchor-vs-value mismatch
(`hadron-knot-table.witness.json`, retired value A — that is `qou-tekx` stage 2).
The other **17** are a different defect entirely, and nothing tracked them.

They put **free text in `q0Anchor`**, where the taxonomy expects one of five
tokens. Three distinct strings:

| count | string found in `q0Anchor` | should be |
|---:|---|---|
| 15 | `'proton (experimental pin)'` | `proton` |
| 1 | `'muon (convention-free geometric pin) @ CODATA 2022'` | `muon` |
| 1 | `'both: proton q_at() + muon q_muon_at() @ CODATA 2022'` | `comparison` |

**The values are correct; only the label is malformed.** Verified on three of
them — each carries a real, right `q0Value`, and each has `q0AnchorReason`
**absent**. The producers packed the rationale into the token field instead of
using the field that exists for exactly that. This is the **inverse** of
`qou-mw1p` (completed), which established `q0AnchorReason` as the home for that
free text: mw1p fixed "token with no reason", this is "reason inside the token".

## Two of the three are mechanical; the third is not

- 15 + 1 → set `q0Anchor` to the bare token, move the gloss to
  `q0AnchorReason`.
- The `'both: …'` one is semantically a **comparison**, and the taxonomy is
  explicit that a comparison carries `q0Values` (a mapping, one entry per pin
  read) and **no bare `q0Value`**. It currently carries a bare `q0Value`
  (`1.10997859564273904668179512938`), which under the correct token is itself a
  `Q0_FLIP`. So fixing the label alone would move it from one flip class to
  another; its producer must emit `q0Values`.

## Scope and ownership

All 17 are `qbeta-*` witnesses from the `qou-cds1` / `qou-pdix` arc — the same
in-flight work that owns the 10 residual convention-C bindings in `qou-t9r1`.
**Fix at the producer, never by hand-editing a witness** (AGENTS.md). That means
touching 17 live producers belonging to another session, which is why this is a
bean and not a PR.

Witnesses (17):

```
qbeta-blind-sector-is-the-tl-kernel          qbeta-holonomy-spectrum-sign-obstruction
qbeta-bond-decay-rates-from-transfer-spectrum qbeta-imq-elliptic-generator-refutation
qbeta-bring-elliptic-generator                qbeta-level-k-binding-operator
qbeta-bring-tau0-and-jet-tower-closure        qbeta-level-k-operator-and-real-decays
qbeta-c3-muon-anchor-codata-edition-attribution  <- the 'both:' one
qbeta-cosine-parametrisation-justification    qbeta-nucleon-difference-ellipticity-structural
qbeta-d-frame-z-determinations-experimental-budget  <- the 'muon (...)' one
qbeta-decay-functional-unification-protium    qbeta-tanh-em-match-is-formal
qbeta-decay-operator-elliptic-spectrum
qbeta-discriminant-curve-in-q
qbeta-eigenphase-tower-and-fraction-readings
```

## Why it matters beyond tidiness

`Q0_FLIP` is the flip-flop detector. With 17 of its 18 hits being label-shape
noise from one producer family, the **one real flip is 6 % of the signal** — a
reader triaging the gate sees 18 reds and has to read every one to find the
single anchor-vs-value mismatch. Draining these makes the gate mean what its
name says.

## Measurement note

I first reported this as "16". It is **17** (15 + 1 + 1), against 18 total
flips. Re-count from the audit output rather than trusting either figure.



---

## Worked 2026-09-04 (PR #6654) — and the bean's own 17 were already fixed

**The 17 named above are ALL clean on `main`**, every one carrying a bare token
(`proton` x15, `ambiguous` x1, `muon` x1). Checked individually, not sampled.

Note one deviation from this bean's own prescription: the `'both: ...'` witness
(`qbeta-c3-muon-anchor-codata-edition-attribution`) became **`ambiguous`**, not
the `comparison` + `q0Values` this bean recommended. Not adjudicated here;
recording it so the next reader does not assume the recommendation was followed.

## The live 13 are a DISJOINT set — this drained and refilled in one day

    Q0_FLIP                  1   (hadron-knot-table, retired value A, qou-tekx stage 2)
    Q0_ANCHOR_UNRECOGNISED  13

Not one of the 13 appears in the 17 above. **Every one was first committed
2026-09-01 to 2026-09-04** — during and after the drain.

**Because the producers were never touched.** 12 still carried
`q0_anchor="proton (experimental pin)"` at the stamp site, so each re-run
re-emitted it. This is `qou-q0rf`'s revolving-door thesis reproduced on a second
gate, with the mechanism visible rather than inferred: outputs were cleaned while
the source kept writing.

## Fixed at the producer (PR #6654)

* **12 uniform sites** -> token + `q0_anchor_reason`. Verified AT THE VALUE, not
  transcribed from the label (sibling commits `4f68183902`, `ec597e2e49`,
  `f4d031de71` all found labels disagreeing with their own numbers): all 12
  carry the canonical proton 50-digit `1.1099785827513808...`, 10 as a literal
  and 2 via `CONST.Q_50_DIGIT_STR`.
* **`qbeta_kd_monodromy_reading_closed`** wrote `'none (exact symbolic
  identities in q)'` -> **`independent`**, verified two ways (the anchor line is
  the only q0-ish token in the file; import cone is stdlib + sympy only). Its
  `q0_value="n/a"` is **dropped**, per the audit's own rule that a single value
  "asserts the one pin the label denies".
* **`markov_bond_rule_forces_pairwise`** passed `q0_anchor=True` -- **my own**,
  from this session's P30 port. A 4th defect class this bean's table does not
  have: only `False` is special-cased (`is False`), so `True` was stamped
  verbatim.
* **`aoperator_a5_crosscheck`** defaulted to the literal `"unrecognised"`, which
  is the audit's VERDICT NAME and not a token it accepts -- a latent 5th source
  that has never fired. Now `ambiguous` with a conditional reason.

## The arrival rate now has a check

`stamp_staleness_metadata` warns to stderr on an anchor outside the five tokens.
**Warn, not raise, deliberately**: stamping happens at the END of a producer and
several here run past 40 minutes, so raising would discard a whole compute to
correct a label -- and the repo settled this same question in this direction when
the owner declined a blocking `precommit-precision-warn.sh` on 2026-08-25. It
changes no value, so `test_only_False_suppresses_not_any_falsy_value` passes
unmodified. 34/34 tests green (run by direct import; pytest is not installed here
and PyPI read-timed out).

## Measurement note worth keeping

The "no number moved" check was WRONG on its first pass: 11 of 12 read MOVED,
and the sole difference in each was `gitCommit` -- a provenance field this family
writes under a name the mask did not have (`commitSha` was masked). Recording
WHICH field differed turned a false alarm into a one-line mask fix instead of a
second full sweep. With it masked: 12/12 byte-identical.

## Still open

* 2 producers exceed 240 s (`qbeta_derived_w_overdetermined_test`,
  `qbeta_interface_w_deciding_test`); re-running on a long budget.
* Whether the guard should BLOCK rather than warn is a real question and is
  deliberately not decided here.
* The 12 producers hardcode the proton 50-digit literal rather than calling
  `q_at()`, so they will not track a re-pin. Out of scope for this bean
  (`qou-0hnz` territory), recorded so it is not lost.


### Long-compute cost of the last 2 witnesses (measured, 2026-09-04)

`qbeta_derived_w_overdetermined_test_probe` and `qbeta_interface_w_deciding_test_probe`
are genuinely expensive, not stuck. Run CONCURRENTLY with a 3000 s budget, both
hit `EXIT=124` having printed only **2 candidate rows in ~50 min**, and neither
wrote a witness -- so a timeout here costs the whole run.

Each row evaluates all four isotopes and 4He is `n = 3*(Z+N) = 12`, the expensive
case. Relaunched SERIALLY (full CPU each) with a 9000 s budget.

Two things for whoever re-runs these: budget in HOURS not minutes, and run them
one at a time -- the concurrent attempt gave each roughly half a CPU and bought
nothing. Until they land, their two witnesses keep the old prose label and the
gate reads `Q0_ANCHOR_UNRECOGNISED: 2` rather than 0. Their PRODUCERS are already
fixed, so this is a provenance lag, not a correctness gap, and it closes on the
next successful run by anyone.


### 🛑 The real blocker is SESSION IDLE, not the compute budget (measured 2026-09-04)

Second attempt at the two long producers: relaunched **serially** at ~13:31 with a
9000 s budget. At the 14:20 check-in: **zero python3 processes**, `slow.done`
empty (so even the `echo EXIT=` never ran -- the wrapper itself was killed), and
`qbeta_derived_w_overdetermined_test_probe.log` last written **13:33:46**, having
reached 337 bytes.

The session had turns until ~13:35 and was then idle until the 14:20 check-in.
**The process died at the start of that idle gap.** Disk was not the cause (7.0 G
free, 82 %), and neither was the budget -- it had used ~2 min of 9000 s.

**So in this remote environment a detached background compute does not survive
session idle.** `nohup` is not enough; the container is reclaimed and takes the
process with it. This matters for AGENTS.md's long-compute logging discipline,
which reads as though `python3 -u ... | tee log &` and checking back later is a
working pattern. It is -- but only while the session keeps taking turns. A
producer needing more wall time than the session stays active is not runnable
this way, however generous the `timeout`.

Third attempt is under `setsid` (own session/process group) to test whether that
survives; **unverified** -- do not record it as a fix until an idle gap is
observed to pass.

**A misreading to not repeat.** `interface_w`'s log mtime (13:15) is OLDER than
`derived_w`'s (13:33), which looks like the serial loop running out of order. It
is not: 13:15 is the STALE log from the first concurrent attempt, still
untruncated because that producer runs second and was never reached. Check
whether a log was truncated before reading its mtime as evidence of ordering.

### Landing at 12 of 14

The two witnesses are NOT regenerated and are not being chased further. Cost/
benefit: their producers are already fixed and pushed, so this is a **provenance
label on two files** -- any successful run by anyone closes it. Against that,
finishing them needs ~75-90 min of continuous session liveness (6 candidate rows;
the concurrent attempt did 2 rows in 50 min under contention). Spending that on
labels is poor value, and hand-editing a witness to close the gap is forbidden.

Consequence, stated so nobody reads the gate as unfixed: `q0_anchor_consistency_audit`
will report **Q0_ANCHOR_UNRECOGNISED: 2** rather than 0, and both are
`qbeta_derived_w_overdetermined_test` and `qbeta_interface_w_deciding_test`.


### setsid does NOT survive session idle either — the finding is now twice-measured

Third attempt, relaunched under `setsid` (own process/session group) at 14:26.
At the 15:15 check-in, after ~45 min of session idle:

    python3 processes                    0
    /tmp/eggf/slow.done                  empty (the wrapper was killed too)
    derived_w log                        337 bytes, last written 14:26:51

So `setsid` buys nothing. Both `nohup` and `setsid` are killed when the container
is reclaimed at session idle. **Two mechanisms, same result** -- treat this as an
environment property, not a launch-flag problem.

**🛑 A measurement trap that nearly produced the opposite answer.**
`pgrep -c -f qbeta_derived_w` returned **4** right after launch and **1** at the
check-in, and I wrote "python is running" off the 4. Both counts include
**pgrep's own match against the invoking shell's command line**, because the
pattern appears in the command being run. `pgrep -af` shows the truth: the only
match was `/bin/bash -c ...` -- my own shell. Use `pgrep -af` and read the
cmdlines, or the self-match reports a dead compute as alive.

### Final measured gate state (nothing competing for CPU)

    Q0_OK                   1368   (was 1358)
    Q0_ANCHOR_UNRECOGNISED     2   (was 13)
    Q0_FLIP                    1

The 2 are exactly `qbeta-derived-w-overdetermined-test` and
`qbeta-interface-w-deciding-test`, both still reading `'proton (experimental
pin)'` because their witnesses were never regenerated. Their PRODUCERS are fixed;
this closes on the next successful run by anyone.

The 1 flip is `hadron-knot-table` (anchor=muon, value = the retired pin A) --
`qou-tekx` stage 2, not this bean's.


### Fourth attempt also died — and it does NOT cleanly fit the idle explanation

Relaunched ~20:45 to run alongside foreground work. Log last written **21:05:07**,
reaching 14 lines (further than the 6 of earlier attempts), no completion
recorded, and at 22:01 no python3 process alive (`pgrep -af`, per the trap above).

**The session was NOT idle at 21:05** — there were turns either side of it
(notifications at 21:03 and 21:06). So the "dies at container reclaim during
session idle" mechanism, which the three earlier attempts do support, does **not**
explain this one. Cause undetermined for this instance; do not fold it into the
idle finding as a fourth confirmation.

What is unchanged: four attempts, zero completions, so the two witnesses
(`qbeta-derived-w-overdetermined-test`, `qbeta-interface-w-deciding-test`) are not
reachable in this session by any method tried. Their producers are fixed on
`main`; a run in an environment that can hold a > 50 min compute closes them.

## 2026-09-08: canonical ledger for the q₀-gate family is qou-1c4y (the AGENTS.md-named migration tracker); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 3 / §7.3 C3. Sixteen q₀-gate beans, ~10 % cross-reference density, now all point there.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
