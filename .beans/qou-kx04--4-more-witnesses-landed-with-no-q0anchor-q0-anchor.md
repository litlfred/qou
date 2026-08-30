---
# qou-kx04
title: 4 more witnesses landed with no q0Anchor (Q0_ANCHOR_MISSING 1885 -> 1889)
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T22:39:50Z
updated_at: 2026-08-16T15:20:51Z
parent: qou-pq8k
---


The follow-on to `qou-rw91`, which is now closed. While reading the
`Q0_ANCHOR_MISSING` list-diff to identify rw91's third witness, the *next*
commit turned out to add four more:

```
7377d6624  chore(witness): refresh stale q0 audit witnesses (counts moved)
           Q0_ANCHOR_MISSING 1885 -> 1889
     + chi-numpy-dtype-fix-benchmark.witness.json
     + dt-crossknot-snappy-slope-hardening.witness.json
     + qbeta-decay-channel-convention-status.witness.json
     + qbeta-ohtsuki-nz-bridge-b6.witness.json
```

Deliberately out of scope for rw91: a different landing, and re-running four of
someone else's producers uninvited is not that bean. Left at 1886 after rw91's
three were declared.

**The vocabulary they need now exists.** `q0Anchor: "independent"` +
verdict `Q0_INDEPENDENT` landed in `b4b293fc` / `e6cc6ac5`, so a producer that
never reads q₀ can say so instead of being indistinguishable from one that
forgot. Per witness the question is only which of three is true:

- reads q₀ → declare `muon` or `proton` (proton is the standing default for new
  compute, owner directive 2026-08-07) with the matching `q0Value`;
- never reads q₀ → `w.save({"q0Anchor": "independent"})`, **no** `q0Value` (one
  there is now a `Q0_FLIP`);
- reads q₀ but the pin is undetermined → `ambiguous`.

Answer it from the **import cone**, not the top-level file. `qbeta-ohtsuki-nz-
bridge-b6` is the strongest candidate: its b4 sibling was verified q₀-free in
rw91 (π, √3, the exact Ohtsuki rungs, 4₁ geometry via `t2.V41_integrated`, whose
own imports are json/subprocess/datetime/pathlib/mpmath only), so b6 is very
likely the same — but *verify* it, do not inherit the verdict.

Trap, from `fcdefee4ed`: use `save(extra=...)`. `add_data("q0Anchor", …)` nests
under `data`, where the audit reading `body["q0Anchor"]` cannot see it — the
witness stays classified MISSING with the field visibly present.

Re-run the producer; do not hand-edit the JSON. All three rw91 producers
reproduced byte-identical numeric payloads, so a clean re-run is cheap evidence
that nothing else moved.

Also still unstamped and now expressible: `chi-deuteron-h6.witness.json` from
`qou-pin1`, a purely symbolic artifact that settled for "manifest `ambiguous`,
drop the stamp" because `independent` did not exist yet.


UPDATE 2026-08-16 (PR #5164, post-rebase). A full unscoped precision-gates run after rebasing onto 61 new main commits shows Q0_ANCHOR_MISSING 1886 -> **1888**: two MORE no-anchor witnesses landed on main in that window, on top of the four this bean already names. The count is growing faster than it is being drained, which is an argument for the anchor declaration being enforced at WitnessBuilder rather than chased per-witness after the fact. Q0_INDEPENDENT holds at 3, Q0_FLIP at 0.

Claimed 2026-08-16 by claude/agent-discussions-queue-gibk4e (session qou-pq8k).


## PROGRESS 2026-08-16 (PR #5164) — 3 of 6 declared

Verdicts from a transitive import cone (ast-based, follows ImportFrom through
computations/ probes/ qbeta/ substrate/), per this bean's instruction to answer
from the cone rather than the top-level file:

| witness | cone | verdict | re-run |
|---|---|---|---|
| dt-crossknot-snappy-slope-hardening | 3 mods, no q0 | **independent** | exit 0 |
| qbeta-ohtsuki-nz-bridge-b6 | 4 mods, no q0 | **independent** | exit 0 |
| qbeta-decay-channel-convention-status | reads q_at(DPS) | **proton** | exit 0 |

Counts: Q0_ANCHOR_MISSING **1888 -> 1885**, Q0_INDEPENDENT **3 -> 5**,
Q0_OK **649 -> 650**, Q0_FLIP 0. The -3 splits exactly 2 independent + 1 OK.

**b6 was verified, not inherited** — the cone agrees with the b4 expectation this
bean flagged, but the expectation was not the evidence.

**convention-status was not neglect.** It already recorded a q0_pin parameter
naming the proton pin; that lands under `data`, where the audit reading
body q0Anchor cannot see it — the fcdefee4ed trap, confirmed live.

**Method note for whoever takes the rest:** the cone is asymmetric. NO q0 in the
cone is conclusive. q0 IN the cone is only an over-approximation — a module may
import Q on a path the producer never evaluates. Both independents above rest on
the conclusive direction; the two below need the weaker direction resolved by
hand.

### STILL OPEN (2 of the named 4+1, plus the +2 drift)
- **chi-numpy-dtype-fix-benchmark** — cone 22 mods, reaches q_parameter
  Q_50_DIGIT_STR *directly* in the producer itself, so it plainly reads q0; the
  open question is only muon-vs-proton (computations-layer q_parameter is the
  muon witness, so likely **muon**, but that must be confirmed, not assumed).
- **chi-deuteron-h6** (from qou-pin1) — cone 19 mods, reaches q_parameter Q via
  hoefsmit_symbolic / hecke_core / mass_at_3A_proper. NOTE this contradicts
  qou-pin1's framing of it as 'a purely symbolic artifact': it is not obviously
  q0-free, and 'independent' is NOT the answer to reach for. Needs the
  over-approximation resolved before any declaration.
- The +2 that landed on main during the 61-commit window are still unidentified
  by name.

ENVIRONMENT: sympy (needed by convention-status) pins mpmath<1.4 and silently
downgraded 1.4.1 -> 1.3.0 on install. Restored to 1.4.1; all three witnesses
here produced under it. snappy installed for dt-crossknot.


UNCLAIMED 2026-08-16: progress above (3 of 6) is landed on main via PR #5164.
Set back to todo rather than left in-progress, since no agent is currently on
it — an in-progress bean with nobody working it is the state the work-plan
policy exists to prevent. The remaining two are described above; read the
method note on cone asymmetry before starting.


## PROGRESS 2026-08-16 (PR #5194) — the last two ANALYSED; artifacts withheld

**Correction to my own note above.** I wrote that `chi-numpy-dtype-fix-benchmark`
was "likely **muon**, since computations-layer q_parameter is the muon witness."
That is wrong. `computations/substrate/q_parameter.py` is not unconditionally
muon — it is manifest-driven: `QOU_Q0_ANCHOR` override, else the producer's stem
under `ideal_muon` in `q0_anchor_manifest.json`, else **proton**. Resolved
authoritatively with `resolve_q0_anchor` rather than inferred:

| producer | resolves | why |
|---|---|---|
| `chi_numpy_dtype_fix_benchmark` | **proton** | stem absent from the manifest -> 2026-08-07 standing default |
| `per_irrep_pole_deuteron_h6` | **ambiguous** | stem IS listed under the manifest's `ambiguous` set: both pin signatures present |

**And a correction in the other direction.** I wrote that the h6 cone
"contradicts qou-pin1's framing of it as a purely symbolic artifact". Half right:
q0 IS reachable (19-module cone), so `independent` would be false — but qou-pin1
had already settled on **`ambiguous`**, which is exactly what the manifest says.
Its instinct was right; my note was harsher than the evidence.

Both source declarations are committed. `ambiguous` here is a QUEUE ENTRY, not a
ruling: it moves h6 out of `Q0_ANCHOR_MISSING` (indistinguishable from a producer
that forgot) into the set that says a human must decide which pin the H6
per-irrep pole extraction evaluates at. No `q0Value` — one there would claim the
ruling has been made.

**The two witnesses were NOT regenerated, deliberately.** Both re-runs were
compromised by this sandbox's stack, not by the edits:

- `chi-numpy-dtype-fix-benchmark`: numpy 2.4.6 (installed in this session) flips
  `allPassed true -> false` and an assertion to `computed: false`, with
  durationMs 408402 -> 32485. The benchmark stops computing. Bean **qou-nz8e**.
- `per-irrep-pole-deuteron-h6`: committed under sympy 1.12 + scipy 1.17.1; this
  sandbox has sympy 1.14 and no scipy. Assertions did not move (the failing one
  is pre-existing on main), but a symbolic producer on a different symbolic
  stack is not evidence.

So the counts are unchanged from the mw1p end state (`Q0_ANCHOR_MISSING 1885`);
the stamps land on the next run in a sound environment. Withholding them is the
point: committing either would have shipped an environment artifact as a result.


## 2026-08-16 — a standing commitment on the b4/b6 reason wording (PR #5210 churn cone)

#5210 (`qou-cwin`) is authorised to re-express the Q_β precision ladder in
**h = q − 1/q** instead of **u = b·ℏ_q²**, and named `qbeta_ohtsuki_nz_bridge_b4/b6`
as in scope. They are explicitly **not** touching these witnesses.

Both `q0AnchorReason` strings name the coordinate:

- b4 — *"Taylor coefficients in a FREE parameter **u** against proved constants…"*
- b6 — *"Same free-parameter-**u** construction as the b4 sibling…"*

**Not changed, and deliberately.** After a u → h reframe these become mildly
anachronistic, not false: the audit-relevant claim is *"no substrate value is
read"*, and that is untouched by a change of coordinate. b4 is robust either way
— it carries the actual evidence (the proved constants, and the import-cone fact
that `sdeformed_channel_signflip_probe` imports only json/subprocess/datetime/
pathlib/mpmath, so the `y_lambda_at` muon-cache straddle is unreachable). b6 is
the thinner one, being largely by-reference to b4.

Regenerating two witnesses to correct wording that is still true would contradict
the discipline the rest of this bean was run under (see the two withheld
witnesses above). **Commitment posted publicly on #5194: if the reframe lands, I
fix the wording then.** Recorded here so it survives the session.

**The general lesson, which is the part worth keeping.** A free-text reason should
state the *invariant* — what is or is not read — and not the *incidental
coordinate*. b4 does this almost by accident (the evidence dominates the variable
name); b6 does not. Passed to #5210 because a `ladder_frame` reason field would be
far more exposed: its entire subject *is* the coordinate.


### 2026-08-16 15:1x — the commitment did NOT fire; strings stand

The #5210 work landed (`#5235 → e2d68dcdc`, `#5210 → 4f542c4d4`) with **much
reduced scope**: `LADDER_FRAME = "u"` in `qbeta_utils` plus a `ladder_frame` key
on `substrate_ladder_quantities`. **No `c_k` value changed and no witness was
regenerated** — the `c₄…` churn that PR originally warned about does not exist,
and `greedy_later_rungs_vanish` now proves it sorry-free.

So the frame **stayed `u`**. It landed a *declaration of* the u-frame, not a
move to h. The b4/b6 `q0AnchorReason` strings naming *"a FREE parameter u"*
describe a variable the producers still have; they are accurate and there is
nothing to fix.

The commitment stays live for a future PR that actually moves the rungs to h.
Recorded as a checked non-event rather than left looking pending — a standing
commitment nobody re-checks is indistinguishable from one nobody honoured.
