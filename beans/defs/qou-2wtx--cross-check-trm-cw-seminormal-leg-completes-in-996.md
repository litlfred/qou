---
# qou-2wtx
title: cross_check_trM_cw_seminormal_leg completes in 996s and FAILS (worst 1.91e+00) where its committed witness says allPassed — the 300s budget hid a pass-to-fail regression
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T18:49:51Z
updated_at: 2026-10-04T15:18:31Z
parent: qou-5vkl
---

## The measurement

`cross_check_trM_cw_seminormal_leg.py` was the **seventh** TIMEOUT in the q0-muon
staleness sweep. Measured with a generous budget, it does **not** time out —
it **completes in 996 s (16.6 min), exit 1**:

    triton    A=3  |Δ|/ref=1.20e+00  FAIL  [1s]
    helium-3  A=3  |Δ|/ref=9.55e-01  FAIL  [1s]
    helium-4  A=4  |Δ|/ref=1.91e+00  FAIL  [995s]

    worst |Δ|/ref = 1.91e+00  (FAIL)
    witness -> cross-check-trM-cw-seminormal.witness.json  allPassed: False

**The committed witness says `allPassed: True`.** So the producer no longer
reproduces its own committed result, and the direction is **pass → fail**.

## The magnitude, and why it is not rounding

The witness was last *regenerated* by `6647e7e4ed`, whose message records
**"all 6 atoms 1ppQ-confirmed (worst 7.28e-49)"**. Today's worst is
**1.91e+00** — forty-nine orders of magnitude. The two commits that touched the
witness since (`d106e6bad9`, `4101909790`) only stamped provenance; they did not
recompute values.

## Candidate cause — NAMED, NOT ESTABLISHED

The producer's code changed after the witness was last regenerated:

| commit | date | what |
|---|---|---|
| `6647e7e4ed` | 2026-07-18 | witness regenerated, worst 7.28e-49 |
| `9df06e0fbe` | 2026-07-18 | `mp.fsum` for the tr_M sum |
| **`34b2a75d43`** | **2026-08-23** | **`fix(qou-fl9i)`: raise 822 sub-canonical `mp.dps` sites to `set_compute_dps()`** |

A precision change five weeks after the last regeneration is the obvious
suspect. **It is a suspect, not a finding** — I have not bisected it, and my
container also runs `mpmath 1.4.1` against the sweep's recorded `1.3.0`, which
is a second untested candidate. Do not record either as the cause without
measuring.

Also unrepeated: this is **one run**. Confirm reproducibility before acting.

## Why this matters beyond one producer

**The sweep's budget is what hid it.** At the 300 s per-producer budget this
producer returns TIMEOUT; it needs 996 s. So the verdict that looked like "too
slow to measure" was concealing a live **pass → fail regression** in a
cross-check between two independent routes to `tr_M`.

That sharpens `qou-uz7q`'s conclusion. I closed that bean's step 2 as "the two
fast ones need no budget; the four long ones need a long-compute plan." This
case adds the missing half: **the cost of a too-low budget is not merely
`UNMEASURED` — it can be a hidden regression.** A budget that lets a 996 s
producer finish would have surfaced this weeks ago.

**And the population growth is what surfaced it at all.** This producer only
entered scope because main's `4101909790` ("label 229 witnesses from their own
payload") stamped its witness muon, which is the same event behind the 47 → 142
denominator growth in `qou-6q7q`. The two findings are one event seen twice.

## Cross-links

- `qou-dau6` / `qou-3zby` — the same *family* (`cross_check_trM_1ppb`), a
  **different script**, and a different diagnosis (C/D convention straddle +
  muon/proton pin mismatch). Not assumed to be the same cause here.
- `qou-uz7q` — the TIMEOUT-verdict work this came out of.
- `qou-6q7q` — the population growth that brought it into scope.


---

## Reproduced — and BOTH named suspects are now REFUTED

The bean above listed three things to close before acting. Two are closed and
the third killed my own hypothesis.

**1. "One run, unrepeated" — closed.** Re-ran the fast A=3 cases: identical,
`triton 1.20e+00 FAIL`, `helium-3 9.55e-01 FAIL`. The failure reproduces.

*Method note worth reusing:* helium-4 alone is 995 of the 996 s, while triton
and helium-3 take **1 s each and also fail**. So every hypothesis below was
testable in ~2 seconds instead of ~17 minutes. When a long producer fails on a
cheap case too, test on the cheap case.

**2. mpmath version — REFUTED.** Downgraded to the sweep's recorded `1.3.0`,
re-ran, restored `1.4.1`. Output **byte-identical** (`1.20e+00` / `9.55e-01`).
The environment is exonerated.

**3. `34b2a75d43` — REFUTED, and it was my leading suspect.** It *does* touch
this producer directly (3 insertions, 1 deletion):

```diff
-mp.mp.dps = 50
+import _path_bridge
+from _precision import set_compute_dps
+set_compute_dps()
```

Restored the pre-commit file and ran: **identical**, `1.20e+00` / `9.55e-01`.

The arithmetic said so before the test did, and I should have weighted it
harder: `set_compute_dps()` *raises* precision (50 → 65), and a precision change
moves a cross-check by ~1e-50, not by **191 %**. **A 1.91e+00 relative
discrepancy is structural, not numerical.** I named a precision commit as the
suspect because it was the most recent change to the file, which is proximity,
not mechanism.

## Where it actually has to be

The producer is unchanged in effect; the environment is exonerated. So the cause
is in a **dependency** that changed between the last witness regeneration
(`6647e7e4ed`, 2026-07-18, worst 7.28e-49) and now. Commit counts in the import
cone since that point:

| module | commits since `6647e7e4ed` |
|---|---|
| `mass_at_3A_proper.py` | 22 |
| `pyhecke/gram.py` | 18 |
| `wedderburn_jones_markov.py` | 8 |
| `hecke_core_legacy.py` | 3 |

**Candidate, explicitly untested:** an O(1) relative shift is the signature of a
**convention change**, and the C → D Markov-parameter migration
(`z = √q/(q+1)` → `z = q³/(q²+1)`) is exactly that shape and was live across this
window. `pyhecke/gram.py` — which carries `z` — has 18 commits in it. Do not
record that as the cause without bisecting; I have now named two suspects on
plausibility and both were wrong.

**Next step is a bisect over the cone, not more reasoning.** The 2-second A=3
case makes it affordable: ~5 steps over 18 `gram.py` commits.


---

## BISECTED — and my third hypothesis was wrong too

`git bisect run` over 4445 revisions between the last good witness regeneration
and HEAD, using the 2-second A=3 case as the test:

> **first bad commit: `2c35a52e08` — *"tnjb: finish the remaining 16 — the
> 'environment limit' was solvable"*** (2026-08-08)

**It is a pure witness-regeneration commit.** 19 files, all `*.witness.json`
plus `q0_anchor_manifest.json` and the migration script itself. **No producer
source changed** — which is why all three of my source-level suspects missed.

## The mechanism, verified end to end

The producer's own docstring, line 30:

> *reference is loaded from `markov/markov-peel-atomic-tr-m.witness.json`*

read at line 76. And `computations/markov/markov-peel-atomic-tr-m.witness.json`
is **one of the 19 files `2c35a52e08` rewrote** (80 lines changed).

So: **the tnjb migration regenerated the reference the cross-check compares
against, and the cross-check was never re-run to match.** It has been failing
since 2026-08-08 — sixteen days.

## This is NOT a bad commit — it is a missed downstream

`2c35a52e08` did the right thing: `tnjb`'s scope is witnesses whose recorded q₀
their producer can no longer reproduce, and regenerating those is a correction.
What was missed is that one of them is a **reference input to a cross-check**,
so regenerating it silently moved the goalposts for a consumer that nobody
re-ran. Blame the dependency edge, not the commit.

## Three hypotheses, three refutations, one bisect

| # | hypothesis | how it died |
|---|---|---|
| 1 | mpmath 1.4.1 vs the sweep's 1.3.0 | downgraded and re-ran — byte-identical |
| 2 | `34b2a75d43`, the `mp.dps` → `set_compute_dps()` change to this very file | ran the pre-commit file — identical |
| 3 | the C → D Markov-convention migration in `gram.py` | bisect landed elsewhere entirely |

All three were named on **plausibility and proximity**; none survived contact
with a measurement. The bisect cost roughly ten minutes and answered what an
hour of reading the diff could not. **When a cheap decisive test exists, run it
before naming a suspect at all.**

## Why it stayed hidden for 16 days

The producer needs **996 s**; the sweep's per-producer budget is **300 s**, so
its verdict was `TIMEOUT` — which reads as "too slow to measure" and is in fact
"a live pass → fail regression nobody has looked at". That is the concrete cost
of the budget, and it is the strongest argument in `qou-uz7q` for raising it —
stronger than any of the timing evidence there.

## Fix

Re-run `cross_check_trM_cw_seminormal_leg` and commit the regenerated witness —
**if** the new numbers are the correct ones. That question is open and is not
mine to settle here: `|Δ|/ref` of 1.20, 0.955 and 1.91 are enormous for a
cross-check between two routes to `tr_M`, so the regenerated peel reference and
the seminormal leg now disagree structurally. Someone has to decide **which leg
is right** before either is blessed. Do not simply regenerate the witness to
make the red go away.


---

## Option 3 — hunting the O(1) term. Four hypotheses tested, four refuted.

Full failure list, including the two small atoms the 90-second runs never reached:

| atom | Z | N | A | s | a | i | **cw** | legB/legA |
|---|---|---|---|---|---|---|---|---|
| neutron | 0 | 1 | 1 | 5 | 2 | 4 | **0** | 1.070 |
| deuteron | 1 | 1 | 2 | 11 | 4 | 7 | **1** | 1.481 |
| helium-3 | 2 | 1 | 3 | 18 | 6 | 10 | **1** | 1.955 |
| triton | 1 | 2 | 3 | 16 | 6 | 12 | **1** | 2.200 |
| helium-4 | 2 | 2 | 4 | 23 | 8 | 15 | **1** | 2.910 |

**1. Constant normalisation — REFUTED.** The ratio is not constant.

**2. Missing q-power per strand — REFUTED.** `ratio^(1/A)` = 1.070, 1.217, 1.301,
1.250, 1.306; `ratio^(1/3A)` = 1.023 … 1.093. Neither is constant. `q₀ = 1.110`,
`q₀³ = 1.368` are near enough to tempt and not near enough to be true.

**3. The colour-weighted p–n seam — REFUTED, and this was my leading
hypothesis.** The **neutron classifies ZERO crossings as `cw`** — `a_cw`/`b_cw`
and δ never enter its computation — and it is still **7 % wrong**. Worse for the
hypothesis: **`cw` count is exactly 1 for every bound atom**, independent of Z,
N and A. So the composition-dependence I reported last turn (triton 2.200 vs
helium-3 1.955 at equal A) **cannot** come from seam count; there is only ever
one seam. I named the seam because the producer's docstring flags it as
CRITICAL — proximity again, not mechanism.

**4. The `i` (σ⁻¹) count — REFUTED.** It is the only structural count that
orders correctly (4, 7, 10, 12, 15 against 1.070, 1.481, 1.955, 2.200, 2.910),
which is exactly why it needed testing rather than adopting: `ratio/i` runs
0.267 → 0.183 and `ratio^(1/i)` runs 1.017 → 1.074. Monotone, not a law.

## Stop fitting — the method is wrong

Five points and several plausible structural counts is a numerology generator,
not a diagnosis. Every one of the four above was a curve through the end-to-end
ratio. **The end-to-end ratio cannot identify the defect**; only a term-by-term
comparison of the two legs' ingredients can.

## The observation that reframes it

The re-pin moved leg A's neutron value by **8 significant figures**
(`0.92323329718…` → `0.92323322991…`), while leg B differs by **7 %**. An
un-changed leg B would therefore have been ~7 % off *before* `2c35a52e08` too,
and the assertion would already have been red. It was green.

**So leg B must have changed at that commit as well** — and `2c35a52e08` touched
exactly one non-witness file: `q0_anchor_manifest.json`, **+17 stems**. Adding a
stem changes what `q_parameter` resolves for producers in leg B's cone. That is
a mechanism that would move *both* legs, and it is the first hypothesis in this
list that is not a curve fit.

**Next, and it is a measurement not an argument:** compute leg B's neutron value
at `2c35a52e08^` and at `2c35a52e08`. If it moves, the manifest entries are the
carrier and the fix is a scope question about those 17 stems. If it does not
move, the bisect's "first bad" is an artifact of leg A alone and the 7 % predates
the window entirely — which would mean this cross-check has been wrong for far
longer than sixteen days.

The neutron is the right probe: A=1, 11 crossings, **no `cw`**, runs in under a
second.


---

## SOLVED — leg A is convention C, leg B is convention D

Injecting the two weight sets that `33a6c7aa4d` records for `n = 3`
(C = `(0.4153958, 0.2809296, 0.0227449)`, D = `(0.5054042, 0.2472979, 0)`) into
leg B's assembly, everything else held fixed:

| atom | leg A (peel) | leg B with **D** | leg B with **C** |
|---|---|---|---|
| proton | 1.06530614425 | 1.14575976903 — **7.55 %** | 1.06530621987 — **7.1e-8** |
| neutron | 0.923233229912 | 0.987743749165 — **6.99 %** | 0.923233296353 — **7.2e-8** |

**The peel reference is still in the excised convention C.** Leg B has computed
in D since `33a6c7aa4d`. That mismatch *is* the O(1) discrepancy, and it grows
with A because more crossings accumulate more of the weight difference.

## Two stacked defects, both now quantified

| # | defect | size | introduced |
|---|---|---|---|
| 1 | **convention**: leg A = C, leg B = D | **O(1)**, 7 % → 191 % | `33a6c7aa4d` (2026-08-09) |
| 2 | **pin straddle**: leg A proton, leg B muon-by-assert | **7.1e-8** | `2c35a52e08` (2026-08-08) |

The 7.1e-8 residual that survives once the conventions agree is defect 2 — the
μ–p tension, ~6× the bare 1.15e-8 gap, accumulated across the word.

## Which leg is right: LEG B

Not a physics judgement — a **policy** one, already made. The owner ruling of
2026-08-15 makes convention **D** canonical and excises C. Leg B is already D.
**The peel reference is the stale artifact**, carrying weights from a convention
the corpus has abandoned.

So the fix is ordered and non-arbitrary:

1. **Regenerate `markov/markov-peel-atomic-tr-m.witness.json` under convention D.**
   That removes the O(1) term.
2. **Then** settle the pin — both legs at proton per the standing directive,
   which means dropping leg B's `assert q.startswith("1.109978595557")` and its
   `QOU_Q0_ANCHOR=ideal` default. That removes the 7.1e-8.
3. The 1ppQ assertion should then return to the ~1e-50 it recorded at
   `6647e7e4ed`.

**Do not do step 2 first.** With the O(1) term still present a pin fix changes
nothing visible and would look like it failed.

## The hypothesis arc, recorded because the pattern is the lesson

Convention C→D was hypothesis 3, and I got it wrong three times before getting
it right:

1. **Named** it on plausibility — an O(1) shift is convention-shaped.
2. **Refuted** it because `git bisect` landed on `2c35a52e08` instead. Wrong
   reason: the assert tolerance is `1e-15`, so defect 2's 1e-8 flipped the test
   first and **masked** defect 1 a day later. *A bisect on a boolean assert
   finds the first flip, not the dominant cause.*
3. **Rehabilitated** it on reading `33a6c7aa4d`'s docstring.
4. **"Refuted" it again** by calling `_y_lambda_at_convention_C_HISTORICAL` and
   getting output identical to the live function — then checked the weights
   themselves and found that function **returns D**. It is dead code, exactly as
   its own docstring says. The test was **inconclusive, not a refutation**, and
   only printing the weights rather than the trace revealed that.
5. **Confirmed** by injecting the C weights by hand.

Step 4 is the one worth keeping: *a comparison between two code paths proves
nothing until you verify they actually differ.*


---

## CONFIRMED by regeneration — the peel witness is simply STALE

Ran `markov_peel_atomic_witness.py` non-destructively (whole `computations/`
tree snapshotted and restored, nothing committed; 134 s wall). **Every row
moved**, and they moved onto leg B:

| Z,N | peel **committed** | peel **regenerated** |
|---|---|---|
| (1,0) proton | 1.0653061442544499756666 | **1.1457596924573008696890** |
| (0,1) neutron | 0.9232332299116371779702 | **0.9877436881158095716340** |
| (1,1) deuteron | 0.3883571411977909894164 | **0.5751722439177718708265** |
| (1,2) triton | 0.1040710573547306741701 | **0.2293101021045565073320** |
| (2,1) helium-3 | 0.2065784335106723458722 | **0.4037670368514281703686** |
| (2,2) helium-4 | 0.0553584155445984267886 | **0.1609741454424073818258** |

Against leg B's D values:

| atom | committed vs leg B | **regenerated vs leg B** |
|---|---|---|
| proton | 7.02e-2 | **6.68e-8** |
| neutron | 6.53e-2 | **6.18e-8** |

**The O(1) term vanishes on regeneration.** So the "merely stale" reading is
right and the alternative — that the peel output genuinely corresponds to C
weights despite `markov_peel_rust_bridge.py:258` using `z = q³/(q²+1)` — is
**refuted**. The engine is D; only the committed artifact was C-era.

**The ~6.5e-8 that survives is defect 2**, the pin straddle: the regenerated
peel is stamped `proton` (unchanged before → after) while leg B asserts muon.
It is the same scale as the 7.1e-8 measured by injecting C weights, from the
other direction.

## The fix is now verified end to end, in order

1. **Regenerate `markov/markov-peel-atomic-tr-m.witness.json`** — measured:
   removes the O(1) term, 7 % → 6.7e-8. 134 s.
2. **Then** drop leg B's `assert q.startswith("1.109978595557")` and its
   `QOU_Q0_ANCHOR=ideal` default so both legs sit at proton — should remove the
   remaining 6.5e-8.
3. The 1ppQ assertion should then return toward the ~1e-50 recorded at
   `6647e7e4ed`.

Step 1 alone is a **10⁶× improvement** and is a pure regeneration — no source
change, no judgement about which leg is right, and the engine already
implements the canonical convention.

## NOT COMMITTED

The regenerated witness was captured to `/tmp/peel_after.json` and the tree
restored. `markov-peel-atomic-tr-m.witness.json` is a canonical reference behind
the L1 certification; committing it belongs to the owner or to #5722's C→D
migration, not to a drive-by from this branch. #5722 was offered it and has not
replied.


---

## Cross-link: main's `reference_anchor_straddle_audit` finds the OTHER axis

`c16f82a1d9` landed a corpus-wide straddle audit — **120 straddles, 11 on the
`atomic-tr-m-mpfr-50dps` pattern** — generalising the same class this bean's
*defect 2* belongs to. Worth being precise about the relationship, because the
two look similar and are not:

| | axis compared | finds | blind to |
|---|---|---|---|
| `reference_anchor_straddle_audit` (main) | producer's `resolve_q0_anchor` vs reference's declared `q0Anchor` | **pin** mismatch — this bean's defect 2 | convention |
| this bean | `y_λ` weights actually used, C vs D | **convention** mismatch — defect 1, the O(1) term | pin |

**A convention mismatch is invisible to a pin-only audit by construction.** Both
sides can declare the *same* anchor — the regenerated peel and its consumer would
both say `proton` — and still differ by 7 % to 191 %, because the disagreement is
in the Wedderburn weights, not the anchor. Measured: `grep -cE
'convention|y_lambda'` over that audit returns **0**.

So the two are complementary, and the corpus currently has a detector for the
1e-8 axis and none for the O(1) one. That asymmetry is worth closing — the
cheaper defect is the one that is now caught.

Also on main: `9c87a54569` ("the 3-way tr_M check was running ONE pair — 3 of 3
diverging was really 12 of 12"). Same neighbourhood, independently found.

**The peel witness is still not regenerated on main** as of +165 commits, so this
bean's step 1 remains open and unclaimed.


---

## The wenzl degradation: my "also C-era" hypothesis is REFUTED, and my staleness test was a FALSE POSITIVE

#5734's survey found `cross_check_trM_wenzl_lr_1ppb` widening 0.7977 → 0.9223
under the D peel, and offered two readings. Chased both.

**Reading 1 — the Wenzl/LR leg is also C-era: REFUTED.** It does not compute a
convention at all; it **loads a third stored witness**,
`rho-k-full-via-wenzl-lr.witness.json`. That witness's producer,
`rho_k_full_via_wenzl_lr.py`, uses `wedderburn_jones_markov.y_lambda_at(n, Q_0)`
— i.e. **D** — and the witness was computed **2026-08-19**, ten days *after* the
C→D excision. It is D by both code and date.

So two D-convention routes disagree by 0.92, which is a **more** interesting
problem than staleness, not a lesser one.

**Reading 2 — that witness is itself stale: REFUTED (after two false positives
of mine, in opposite directions).** Re-running the producer changed the witness,
and I nearly recorded that as a positive. The log says why:

    ✗ unavailable: hecke-tr-m-wenzl-lr binary not built
    atoms: 4; available: 0/4

The witness moved because the re-run **emptied it** — the Rust binary
(`tools/hecke-engine/target/release/hecke-tr-m-wenzl-lr`) is absent in this
container, so 0 of 4 atoms were computed. That is the degraded-rerun hazard
AGENTS.md names verbatim: *"A regeneration is only trustworthy if the rerun
environment can do everything the original could."* Tree was restored; no damage.

**Third time this session an environment fault impersonated a finding**, after
`hadron_knot_table`'s missing scipy and the `_y_lambda_at_convention_C_HISTORICAL`
dead-code control. The shared shape: **a comparison is only evidence once you
confirm both sides actually ran.** A diff is not a verdict.

## Status

The 0.7977 → 0.9223 widening is **unexplained**, and both of the explanations
#5734 offered are now closed off:

- not C-era staleness in the Wenzl/LR leg (refuted by code and date);
- not measured-stale (the probe was degraded, so unmeasured).

Deciding it needs the Rust binary built
(`cargo build --release --bin hecke-tr-m-wenzl-lr`) and the producer re-run in a
capable environment. **#5734's wording remains accurate** — it says "which of
those it is, is NOT established" — so no correction is owed there, only this
narrowing.

Worth noting for whoever picks it up: since both legs are D, a genuine
disagreement at 0.92 would be a *substantive* result about the two routes, not a
bookkeeping fix.

### Reading 2, settled — and it took two false positives to get there

**Attempt 1 said "stale". Degraded environment.** The Rust binary
`hecke-tr-m-wenzl-lr` was absent, so the re-run emitted `available: 0/4` and
*emptied* the witness. The diff was my container, not the corpus.

**Attempt 2, after `cargo build --release` (35 s), said "stale" again. Also
wrong — my own volatile-key mask.** With `available: 4/4`, exactly **6 of 291
fields** moved:

| field | before → after | what it is |
|---|---|---|
| `rows/0..3/duration_ms_total` ×4 | 19→45, 402→280, 390→173, 2065→1285 | **wall-clock noise** |
| `upstream_witness_hashes/0/{sha256,bytes}` | 47239 → 47562 bytes | the **peel witness I just regenerated** — correctly noticed |

**Not one `rho_k` value moved.** The Wenzl/LR reference reproduces exactly and is
**current, not stale**.

AGENTS.md states this trap outright — *"mask volatile keys or you measure your
own harness"* — and I hit it anyway, because my mask listed
`computedAt/commitSha/durationMs/...` and not `duration_ms_total`. A near-miss
on a key name is a full miss.

## So the widening is REAL, and it is the interesting outcome

Every bookkeeping explanation is now closed:

- the Wenzl/LR leg is **D** (uses `y_lambda_at`), by code and by date;
- its reference witness is **current** (values reproduce byte-for-byte);
- the peel is now **D** and current.

**Two current, convention-D routes to `tr_M` disagree by 0.92 on 12 of 12
pair-tests.** That is not a staleness defect to be drained — it is a substantive
disagreement between two independent derivations, and it is exactly the kind of
thing the L1 defence-in-depth cross-checks exist to surface.

Worth stating plainly: **moving the peel to D did not create this; it revealed
it.** Under the C peel the gap was 0.7977 — also red, also 12/12 divergent. The
regeneration changed a wrong-convention red into a correct-convention red, and
the residual is now a real question about the mathematics rather than about
bookkeeping.

## RETRACTION (2026-08-24, later the same day)

The section above concludes: *"every bookkeeping explanation is closed, and the
widening is REAL: two current, convention-D routes to tr_M disagree by 0.92 on
12 of 12 pair-tests."* **That conclusion is withdrawn.** The widening is neither
real nor a disagreement between two routes to the same quantity.

`cross_check_trM_wenzl_lr_1ppb` compares `|tr_M(β_canonical(Z, N))|` against
`|tr_M(β_p ⊗ β_n ⊗ …)|`. Those are **different objects**: the Wenzl LR identity
holds for tensor-product (disjoint) braids, and the canonical atomic braid is not
one — it carries inter-nucleon arc crossings the disjoint product omits.
`rho_k_full_via_wenzl_lr.py` states this in its docstring, dated **2026-05-17**,
including the expected magnitude (*"~80 % relative on D, T, ³He"*). A `1e-9`
tolerance was being applied across a known inequality.

Closed on `main` by `7823271e66` (bean `qou-u6n2`, a different session), which
marks those pair-types `compares_same_object: false` and excludes them from
`any_diverge`.

**What my reasoning did wrong.** The two candidate readings I formed — C-era leg,
stale witness — were both genuinely refuted by measurement, and I treated
"refuted every explanation I thought of" as "the effect is real." That is an
argument from exhaustion of *my own* hypothesis list, and the corpus-grep
checklist exists precisely because that list is not the corpus. I ran the
checklist on the cross-check's identifiers and never on the producer supplying
the outlying leg; `sed -n '1,55p'` on that file answers it in one command.

The two false positives recorded above (the degraded re-run with the Rust binary
absent; the unmasked `duration_ms_total`) stand as recorded — they were errors in
the staleness test, and they are what made the "everything else is closed" framing
feel earned.

**Unaffected.** The seminormal-leg root cause (191 % → 6.7e-8), the two-stacked-
defects chain, and the peel regeneration itself are all independent of this and
stand. `main` reproduced the identical regenerated values from a different
diagnosis and a different environment.


---

## STEP 1 LANDED ON MAIN — and step 2's residual is now measured (PR #5962)

This bean's step 1 ("regenerate the peel witness under convention D") was
recorded as *"still not regenerated on main as of +165 commits, unclaimed"*.
**It has since landed**: `cfe73b8eb5` ("drain(q0): re-run the flip producers at
the derived anchor") regenerated
`computations/markov/markov-peel-atomic-tr-m.witness.json`, and its values match
this bean's predicted regeneration **to every digit**:

    proton    1.1457596924573008696890
    neutron   0.9877436881158095716340
    deuteron  0.5751722439177718708265

Independent confirmation of the diagnosis, from a different session and a
different route.

## The consumer has now been re-run, and the O(1) term is gone

| atom | this bean, C-era peel | now, D peel |
|---|---|---|
| triton | 1.20e+00 | 1.98e-07 |
| helium-3 | 9.55e-01 | 2.53e-07 |
| helium-4 | **1.91e+00** | **2.99e-07** |

Worst **1.91e+00 → 2.99e-07**, a **6.4e6× improvement**. The prediction that
step 1 alone is a ~10^6× improvement was right.

**The ~1e-7 residual is defect 2 exactly as this bean scoped it** — the pin
straddle, peel stamped `proton` against a leg resolving `ideal_muon`. Corroborated
from the other side: the L1 cross-check independently reports `rel_delta_max`
2.9066e-07 for helium-4 (see `qou-wgaw`). Same scale, same cause.

`allPassed` moves True → False. That is the pass→fail regression this bean
found, now landed **with its dominant cause removed** rather than concealed.

## Budget correction — 1501 s, not 996 s

Measured on the same producer, 2026-08-29: **1501 s total, helium-4 alone
1499 s (99.9 %)**. This bean measured 996 s on 2026-08-24. Both are real runs;
the 1.5× gap is **not explained**, and two candidates are untested (slower
container; the convention-D peel changed the work). Budget **1500 s**.

The method note stands and is the reusable part: **the five cheap atoms take
~2 s combined and all of them fail too**, so any hypothesis is testable in
seconds rather than 25 minutes.

## Step 2 remains open

Dropping the leg's `QOU_Q0_ANCHOR=ideal` default and its muon assert so both
legs sit at proton is NOT done here. It is a pin-policy change on an L1
reference, and this PR's subject is the A→C repin. Its expected value is the
remaining ~1e-7.

- **Round 93 (`litlfred/qou#8421`)**: Advanced in `feat/round93-strip-kindratio-kohnokz-resolvent-affinenorm-43c1` (Commit 1 `53341df5af4d7e77e4fbee34d9b0bead3b0b6187`, Commit 2 `2f40c0d2d071ec6bb42d20002fb53171245df01c`, probe sha256 `3d8255f15bbdfc2d9c41114f8ac21a1bec3996e0b1546ef080914210757c628c`).
