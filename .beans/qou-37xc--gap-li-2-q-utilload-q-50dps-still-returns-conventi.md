---
# qou-37xc
title: 'GAP: _li_2_q_util.load_q_50dps still returns convention-C z — 21 callers, must be atomic'
status: todo
type: task
priority: normal
created_at: 2026-08-24T11:19:46Z
updated_at: 2026-08-24T17:13:09Z
---

The largest remaining convention-C site (`qou-cds1`, PR #5622). **Not attempted
as a drive-by** — sized, then deferred, for the reason below.

## The defect

[`computations/_li_2_q_util.py:312`](../computations/_li_2_q_util.py), inside
`load_q_50dps()`:

    z = mpf(1) / (mp.sqrt(q) + mp.sqrt(qi))       # = sqrt(q)/(q+1) = z_C

It should be `z_D = q**3/(q**2+1)`. One line.

The *anchor* half of this helper was already fixed on 2026-08-22 (default
flipped `None`→muon to `anchor="proton"`, beans `qou-dkm2` / `qou-v90i`), so
this is now a single, unentangled convention defect.

## Blast radius — measured, not estimated

29 files call `load_q_50dps`. Splitting by whether they bind the third return:

| | count | affected? |
|---|--:|---|
| **binds `z`** (as `z`, `ZMARK`, `z_markov`, `z_loaded`, `z_anchor`) | **21** | yes |
| discards it (`_`, `_z`) | 6 | no |
| mentions without unpack-assign | 2 | no |

Of the 21, **19 emit a committed witness**. So the change moves numbers in 19
witnesses. Full list in the PR-side inventory; the ones that matter for
sequencing:

- `probe_9b_perlambda_brane_tower.py` — **blocked** on `qou-5t68` (its upstream
  `borromean-binding-recompute.witness.json` is 17–23 % stale).
- `convergence_safe_vhat_tower.py` — already escalated separately; its `z_bar`
  site needs a bar-symmetry decision (`bar(z_C) = z_C`, `bar(z_D) = q^-4·z_D`).
- `derive_m_p_hecke_full_tower_50dps.py`, `vhat_tower_im_cancellation.py`,
  the three `deltalambda/*` probes — long-running; need the measured-timeout
  treatment, not a 900 s harness default.

## Why it must be ONE commit, not incremental

Converting some callers and not others is precisely the defect this PR exists
to remove. Every straddle found so far was a file computing at `z_C` while the
module it consumed or mirrored was already `z_D`:

    delta_lambda_borromean_ascaling edge-set  vs its own tower        16 %
    borromean_per_lambda_fr_probe::tower()   vs the fn it mirrors     16 %
    substrate/hecke_core_symbolic            vs pyhecke.gram       22.70 %

A shared helper is the worst place to create one, because the disagreement is
then between *callers* and invisible in any single file.

There is a direct precedent for doing it atomically: the anchor default flip
above changed the value for 28 call sites in 26 files in one change, and that
was right — the inventory was the work, the edit was one line.

## What the next agent needs

Not a conversion — a **baseline campaign**. Run all 19 witness-emitting callers
before touching the line, record which complete and which are already stale
(several will be: the deuteron ledger was 50 fields stale, `qou-58sa`), then
flip the line, re-run, and attribute. Budget the long ones explicitly;
`scripts/convention-c-convert-one.sh` takes a 5th `timeout_s` argument and
**aborts rather than diffing against a killed baseline**, which is the guard
that matters here.

Do **not** widen any precision baseline to absorb the movement.


## SCOPE EXPANDED (2026-08-24): this bean owns THREE of the remaining sites, not one

Re-checked which of the remaining convention-C sites can be converted
independently. **`convergence_safe_vhat_tower.py:198` and
`probe_9b_perlambda_brane_tower.py:204` cannot** — both take their `z` from
`load_q_50dps`, i.e. from this helper:

    convergence_safe_vhat_tower.py:178   q, qi, z = load_q_50dps()      <- C, via this bean
    convergence_safe_vhat_tower.py:198   z_bar = 1/(sqrt(qi)+sqrt(q))   <- C, local
    probe_9b_perlambda_brane_tower.py:241  q, qi, z_loaded = load_q_50dps()   (LIVE call)

Converting the *local* `z_bar` while `z` still arrives as C from here would put
convention D and convention C into the same `_std_vhat` call — **manufacturing
exactly the straddle this branch exists to remove**, and the same shape as the
`alpha_high_precision` defect (`qou-l1gv`, z_D imported + z_C local in one
functional).

So the atomic unit is larger than the 21 callers: it is this helper **plus** the
local C sites inside its callers. Any plan that converts `load_q_50dps` must
sweep those in the same change.

**Verified independent, so NOT in this unit:**

- `delta_lambda_v_hat_z_transfer_phase5d_4.py:98` — its only `load_q_50dps`
  mention is a **comment** at line 81 recording that it was deliberately
  migrated away from it. Live `q` comes from `q_parameter`. Convertible alone.
- `alpha/alpha_high_precision.py:88` — imports z from `hecke_core`, not from
  here. Blocked on its own defect pile (`qou-l1gv`), not on this bean.

## Corrected count of what remains on qou-cds1

    1  independently convertible   delta_lambda_v_hat_z_transfer_phase5d_4  (slow: >40 min/run)
    1  blocked on its own defects  alpha_high_precision                     (qou-l1gv)
    3  ONE atomic unit             _li_2_q_util + convergence_safe_vhat_tower + probe_9b   (this bean)

Not "5 remaining sites". I had `convergence_safe_vhat_tower` listed as queued
and ready to convert after the z_bar maths was settled — the maths *is* settled
(`z_bar = z(q^-1)`, see `qou-cds1`), but settling it does not make the site
independently convertible, and converting it on that basis would have
introduced a defect.


## Refined again: 16 real users, not 21 — and probe_9b is NOT in the unit after all

Measured the difference between *binding* the helper's third return and *using*
it. Of the 21 binders, **16 use it and 5 never do**:

    BINDS BUT NEVER USES (5)
      delta_lambda_q_dilog_categorical_action.py            z
      deltalambda/deltalambda_k4_complete_graph_...py       z
      e0_lambda_composite.py                                ZMARK   (module level, nothing imports it)
      probe_9b_perlambda_brane_tower.py                     z_loaded
      zhabiro_realq_saddle_probe.py                         z_anchor

Verified by hand for the two that matter: `z_loaded` occurs **exactly once** in
`probe_9b_perlambda_brane_tower.py` — at the binding, line 241 — and `ZMARK`
once in `e0_lambda_composite.py`, with no module importing it.

## 🛑 This corrects my previous note on this bean

The note above puts `probe_9b_perlambda_brane_tower.py` **in** this atomic unit,
on the grounds that line 241 is a *live* `load_q_50dps` call rather than a
comment. That is true and the inference was still wrong: **the call is live, its
`z` result is dead.** The producer's actual z is its own local site at line 204,
so it is not entangled with this helper and can be converted independently — it
remains blocked, but on `qou-5t68` (17–23 % stale upstream witness) alone.

Same error class as the one it was correcting: last time I counted
`load_q_50dps` *mentions* and had to separate calls from comments; this time I
counted *calls* and had to separate live results from dead ones. Checking one
level deeper each time. `convergence_safe_vhat_tower.py` survives both checks —
10 real uses — and stays in the unit.

## Current unit

    _li_2_q_util.py:312                +  16 producers that actually use its z
    of which convergence_safe_vhat_tower.py also carries a local C `z_bar`
    that must convert in the same change

Not in the unit: `probe_9b` (dead z), and the 4 other bind-and-discard callers,
which are unaffected by the conversion because they never read the value. Those
5 are mild dead code; `probe_9b`'s is actively misleading, since a reader
reasonably concludes the producer is anchored to this helper — I did, twice.


## The source change is WRITTEN AND VERIFIED — only the 19-witness campaign remains

Prepared and tested 2026-08-24, then reverted from the working tree rather than
committed, because committing the source alone would put a convention-D helper
above **19 convention-C witnesses** — the exact straddle this branch exists to
remove, multiplied by 19. Atomicity, per this bean's own scope note.

### Two C sites in that function, not one

My triage listed only line 312. There is a second at line **302**, in the
proton branch, inside a `return` expression rather than an assignment:

    return q, qi, mpf(1) / (mp.sqrt(q) + mp.sqrt(qi))

An assignment-keyed detector cannot see it. Same return-form blindness the
AGENTS notes catalogue. **Both** must convert.

### It delegates to the helper rather than re-spelling D

Per `hecke_channel_binding_probe.py:61-68` — *"every convention detector keys
on how z is WRITTEN, and an inline spelling is how a site goes blind"*. A call
site needs no detector at all, so this is strictly better than writing
`q**3/(q**2+1)` here, at the same edit cost.

Import is **function-local**, mirroring `closed_form_tau_M`'s own
function-local `from _li_2_q_util import flavor_split_leading` (line 362), so
the two modules cannot deadlock at import time in either load order.

### Verified (near-zero CPU, no producer run)

Imported `_li_2_q_util` FIRST — the worse order for a cycle — then:

    proton  z returned = 0.612688037146465252 == q^3/(q^2+1)   (was z_C 0.499320334183694452)
    muon    z returned = 0.612688050548890157 == q^3/(q^2+1)   (was z_C 0.499320334033561272)

Exact equality both anchors, no cycle. Note the muon `z_C` is
`0.4993203340335613`, which is the literal the sibling's
`producer_importability_audit` flagged — so that hardcoded value is the
**muon-pin** C, not the proton one.

### The patch, ready to apply

```diff
diff --git a/computations/_li_2_q_util.py b/computations/_li_2_q_util.py
index c981743143..b785447b34 100644
--- a/computations/_li_2_q_util.py
+++ b/computations/_li_2_q_util.py
@@ -253,11 +253,33 @@ def li_2_q_negative_continuation(
     return -h * total
 
 
+def _markov_z(q: mpf) -> mpf:
+    """Markov parameter z(q), via the canonical helper.
+
+    Both branches of `load_q_50dps` used to spell z inline as convention C's
+    `1/(sqrt q + 1/sqrt q)`. They now delegate to
+    `closed_form_tau_M.markov_z`, which is convention D and whose selection is
+    FORCED rather than stipulated (`markovWeights_eq_jones_of_threeRow_eq_zero`,
+    sorry-free).
+
+    Delegating rather than re-spelling `q**3/(q**2+1)` here is deliberate, and
+    the reason is the corpus's, at `hecke_channel_binding_probe.py:61-68`:
+    *"every convention detector keys on how z is WRITTEN, and an inline
+    spelling is how a site goes blind"*. A call site needs no detector.
+
+    Imported inside the function, mirroring `closed_form_tau_M`'s own
+    function-local `from _li_2_q_util import flavor_split_leading` (line 362),
+    so the two modules cannot deadlock at import time regardless of load order.
+    """
+    from closed_form_tau_M import markov_z
+    return markov_z(q)
+
+
 def load_q_50dps(
     path: Path | None = None,
     anchor: str = "proton",
 ) -> tuple[mpf, mpf, mpf]:
-    """Load q_0, q_0^{-1}, and z = 1/(q^{1/2}+q^{-1/2}) at full ``mp.dps``.
+    """Load q_0, q_0^{-1}, and z = q^3/(q^2+1) at full ``mp.dps``.
 
     Returns ``(q, q_inv, z)``.  Shared by every script that ingests
     per-generator Wedderburn volumes — centralized per gemini #687.
@@ -299,7 +321,7 @@ def load_q_50dps(
                 from q_parameter import Q_MP
             q = Q_MP
             qi = mpf(1) / q
-            return q, qi, mpf(1) / (mp.sqrt(q) + mp.sqrt(qi))
+            return q, qi, _markov_z(q)
         if anchor != "muon":
             raise ValueError(
                 f"load_q_50dps: anchor must be 'proton' or 'muon', got {anchor!r}"
@@ -309,8 +331,7 @@ def load_q_50dps(
         d = _json.load(fh)
     q = mpf(d["derived_50_digit"]["q"])
     qi = mpf(1) / q
-    z = mpf(1) / (mp.sqrt(q) + mp.sqrt(qi))
-    return q, qi, z
+    return q, qi, _markov_z(q)
 
 
 def compute_t2_t3_from_vols(
```

### What remains

Apply the patch, then baseline → re-run → diff the **16 real users** (not 21;
5 bind and discard). Land source + all moved witnesses in ONE commit. Deferred
now only because the `delta_lambda_v_hat` converted run holds the CPU and
cleared its 3 h ceiling by **249 seconds** last time — 16 concurrent producers
would push it to EXIT=124 and waste three hours.
