---
# qou-p77d
title: 'GAP: 883 non-integral float64 at .assertions[].computed/.expected across 300 witnesses — the class #5910 deferred'
status: in-progress
type: task
priority: normal
created_at: 2026-08-29T02:28:37Z
updated_at: 2026-08-29T18:29:56Z
---

## 2 of the 883 are already drained (PR #5952, bean `qou-t39x`) — 2026-08-29

Recorded so the tranche does not re-open them, and because the instance
reproduces this bean own reasoning from the opposite direction.

`computations/probes/qbeta_exponentiated_per_block_probe.py` had
`computed = float(results["proton"]["c"][2])` and `expected = -1.0` in its
`scale_fix_c2_minus1_solvable_and_exact` assertion. Both sat in the
INTEGRAL-EXCUSED majority — the value is exactly -1.0 — and both are now
`mp.nstr(..., 40)` and the string "-1", fixed at the producer and re-run, which
is the route this bean prescribes for a `computed` field.

It is a live instance of the "integral is safe by ACCIDENT OF CURRENT VALUE"
warning, and a sharp one: the cast was discarding a 35-DIGIT agreement (the
assertion tests |c+1| < 1e-35 at 60 dps) in order to report -1.0. Nothing was
excused about it except the current value.

Worth carrying into the sweep design: it surfaced from the OTHER end. The
raw-float64 ratchet went red on the same assertion tolerance, a bare 1e-35
literal — the #5910 declared-threshold class, repairable textually. Fixing that
put me inside the function, where the `computed` cast was visible three lines
up. The two classes co-occur in the same assertion dict, so a producer opened
for a #5910-style tolerance fix should have its `computed`/`expected` checked in
the same pass rather than left for a second visit.

After: raw-float64 ratchet NEW dirty 0, REGRESSED 0; integral-float population
down by exactly the 2 fields.

MEASURED 2026-08-29 (PR #5996) — A THIRD OF THE 883 MUST NOT BE DRAINED THE
PRESCRIBED WAY, AND THE RANKING IN THIS BEAN STARTS IN THAT THIRD.

This bean says the ranked worst-offenders list "is where it would start". I
started there, opened the #1 entry, and it is in the bucket where the
prescribed repair is wrong.

    583  A. producer raises mp.dps -> mpf carries real digits, the float()
            cast genuinely discards them. Repair as prescribed.
    291  B. producer NEVER raises mp.dps (or pins <= 15) -> the computation is
            float64-equivalent however much mpmath it imports.
      9  C. producer not found.

For B, float(x) -> mp.nstr(x, 40) prints forty digits of a double. Not a
repair; LAUNDERING, against AGENTS.md "never report a float64 agreement as
exact / to N digits".

SIX OF THE TOP EIGHT OFFENDERS ARE B. The largest single entry,
channel_product_mass.py at 64 fields (7% of the tranche), imports mpmath,
calls mp.log and casts back at :109/:111/:116 — while M_E_MEV, M_P_MEV,
m_n_derived_3input and Q are all plain floats and mp.dps is never raised off
its default 15. Its assertion tolerance is 2%, so precision is not the binding
constraint there by ~14 orders of magnitude.

B IS NOT "ALREADY FINE" — those producers are float64 while PRESENTING as
mpmath computations. But the fix is upstream (mpf(str(CONST)) + a real dps,
the pattern the corpus already uses at binding_link_volumes.py:111 and
option_e_v8_hecke_involution_isospin_mirror.py:43), not a serialization change
at the assertion. It changes what the numbers MEAN, not how they are written,
so it should not ride in on a drain. Wants its own bean.

WORK ORDER, corrected: drain within bucket A, ranked by --by-precision.
Starts at probe_he4_canonical_tr_m_fingerprint.py (18) and hadron_knot_table.py
(14). NOT started — #5996 is the measurement that fixes the order, nothing more.

TOOLING: --by-precision on assertion_value_float64_triage.py prints the split
and warns, in its own output, that the unsplit ranking above it is the wrong
thing to work. --selftest (7 cases) pins the discriminator on the #1 A and the
#1 B by name, four synthetic producers (no-dps / 15 / 60 / set_compute_dps),
and that an unknown producer lands in C rather than silently in A or B.

MEASUREMENT CORRECTION, mine: my first pass said 958 fields / 325 witnesses.
The excess is entirely computations/_deprecated (74) and the generated
qou-mass mirror (1), both out of scope. This bean 883/300 is right and
reproduces exactly. Recorded rather than quietly dropped — the failure mode all
session has been adopting whichever number agreed with me.

BUCKET B MEASURED 2026-08-29 (PR #5996) — IT IS THREE JOBS, AND THE BIGGEST IS
NOT A PRECISION FIX AT ALL.

291 fields over 58 producers. Split by what the producer actually is:

    15 producers  import mpmath but never raise mp.dps
                  -> plausibly mechanical: add set_compute_dps(), verify the
                     mpf actually flows, and they become bucket A.
    43 producers  NO MPMATH AT ALL — float64 end to end.
                  -> not a serialization or dps problem. "Fixing" one means
                     RE-DERIVING the computation in mpmath, per producer,
                     changing values that feed real claims.

The float64 constants they pull: q_parameter (38), experimental_constants
(16), codata_constants (12), codata_table (1). Those modules export plain
floats BY DESIGN — the corpus pattern for wanting precision is mpf(str(CONST))
at the call site (binding_link_volumes.py:111,
option_e_v8_hecke_involution_isospin_mirror.py:43).

FOR THE 43, THE CORPUS ALREADY DEFINES THE HONEST OUTCOMES and none is a
sweep:
  1. port to mpf — real work, per producer, moves values;
  2. declare precision_tier AND deprecate — note the audit is explicit that
     'precision_tier: "float64" alone excuses nothing', so a producer cannot
     self-excuse (witness_raw_float64_audit.py:311-332). main landed one of
     these on 2026-08-29: 4f246d4320 'the four H_9 A-operator extracts are
     float64 by measurement';
  3. establish float64 is adequate for what the producer claims, and say so.

Worked case for (3): channel_product_mass.py is the #1 offender at 64 fields,
and its assertion tolerance is 2% of the observed mass. Precision is not the
binding constraint there by ~14 orders of magnitude. Draining it would change
64 numbers and improve nothing that any claim rests on.

RECOMMENDATION (judgement, not a finding): do the 15, and treat the 43 as a
separate bean. Folding a mathematical re-derivation into a drain labelled
'remove float casts' is the same smuggling the zero-gain rule already refuses.


## Bucket B has a single upstream cause (measured 2026-08-29)

`computations/substrate/experimental_constants.py` casts every CODATA mass to
binary64 at import (`M_E_MEV = float(_M_E_MEV)`, same for M_P/M_N). Every
bucket-B producer that starts from those constants is float64 end to end no
matter how much mpmath it calls afterwards — `channel_product_mass.py`, the
corpus's single largest offender at 64 assertion fields, is exactly this.

The cast's stated reason is HALF STALE. Measured in
`computations/audits/experimental_constants_float64_rationale_probe.py` (6/6):

  * "an mpf would break json.dumps" — TRUE for a bare `json.dumps`, FALSE for
    the witness path, which is where the bucket-B fields come from.
    `qou_substrate/witness.py` uses `json.dump(..., default=str)`.
  * "importers' float arithmetic stays intact" — holds for arithmetic,
    comparison, f-strings. The real hazard is `math.log(mpf)`, which does not
    raise, it silently downcasts.
  * "~266 importers" — actually 204 live (+4 generated mirror).

DECISION NOT TAKEN — it is the owner's. Flipping three constants changes
numbers across the mass sector.

## Retracted this session

Claimed 13 producers / 52 fields were misfiled B→A via a one-hop import-cone
check. WRONG: the inherited `set_compute_dps()` in `mass_at_3A_proper` is
inside a function. Classifier stays file-local; both wrong versions pinned in
its selftest.

Also: "round-trips through float64" is NOT proof of laundering. It flagged 55
of the 302 already-drained fields; all 55 are exact k·2^-235 ULP residuals,
and a power of two round-trips losslessly. Flag for reading, never decide.


## CODATA flip DONE; bucket B does NOT generalise (2026-08-29, PR #6022)

Owner authorised both halves. First half landed, second half largely did not,
and the reason is the useful part.

### Flip (done)
`experimental_constants.py` casts removed — the registry already held mpf.
- No CODATA INPUT moved (rel 0.0 on m_e/m_p/m_n). Only derived quantities
  changed, by the float64 error they carried: Q_β 4.1e-50, κ=m_e/3 9.8e-17.
- 204 importers screened both sides, fresh subprocess each: 6 fail before,
  23 after, **6 after fixing → 0 attributable**.
- Fixed at cause: 96 `mpf(repr(CONST))` sites (broken for mpf, correct for
  float — the other 84 in the tree left alone); 2 bare `json.dump` given
  `default=str`; one silent `math.sqrt(mpf)` downcast in the module itself.

### Bucket B splits on q₀, which is float64 BY DESIGN
`q_parameter.Q` is a float (17 digits vs a canonical 50). `q_parameter.py`
header says do NOT change it; `q_at(dps)` is the accessor. So:
- 26 q-independent (82 fields) — ran them: **ok=4, reverted=22**
- 32 q-dependent (209 fields) — BLOCKED on a per-producer proton/muon anchor
  choice. Layer-straddle hazard; not mechanical. NOT attempted.

### The 22 reverts are diagnoses, not failures
- 17 "no gain", 12 with ZERO casts (`0+0`) — float64 enters by a route neither
  a dps raise nor a cast removal touches.
- 5 LAUNDERING — guard caught the value still round-tripping through binary64.
  Worked case: `codata_reconciliation` emitted
  `0.782333409309999949776…` = Q_NEUTRON_MEV (exact mpf) pushed through a
  double downstream and printed at 40 digits.

### Landed
qbeta_counit_substrate_consistency (17→65 digits), chi_free_via_lr,
qbeta_5two_tail_law_deep_cn_probe, qbeta_uw_reparam_probe.
Fields 599 → 593; ratchet NEW 0 / REGRESSED 0 / exit 0.

### Process notes for the next agent
- Pipe a long producer run to a FILE, never through `tail` — buffering swallows
  every verdict and a kill loses them all. Made this mistake twice today.
- Scope before running: my first pilot took the 6 LARGEST producers, 4 of them
  q-dependent and certain to revert.


## MERGED 2026-08-29 — 883 → 593 fields, 300 → 208 files

Two PRs on main: #5996 (`3eb2375`, bucket-A drain) and #6022 (`22b84c2`,
CODATA constants off float64 + 4 bucket-B producers).

**Bucket A: 139 producers drained.** Of 302 committed float→string fields,
**258 genuinely gained digits**. Every drain judged against a FRESH UNMODIFIED
baseline re-run, never the committed witness — three of the first five targets
already drift on an unmodified re-run, so the committed file blames the cast
removal for movement that was already there.

**The upstream cause, fixed.** `experimental_constants.py` cast every CODATA
mass to binary64 at import while `codata_2022_source` already held them as mpf
at full width. Removed. No input value moved (rel change 0.0 on M_E/M_P/M_N);
only `Q_NEUTRON_MEV` (4.1e-50) and `KAPPA` (9.8e-17) changed, by exactly the
float64 error they were carrying. 204 importers screened both sides in fresh
subprocesses: **0 new failures**.

## STILL OPEN — three jobs, not one

1. **32 q-dependent producers / 209 fields.** `q_parameter.Q` is a `float`
   (17 digits vs the canonical 50). DELIBERATE — `q_parameter.py` says not to
   change `Q`/`Q_50_DIGIT_STR` and provides `q_at(dps)`. So every producer
   reading `Q` has a float64 ceiling on its q-dependent arithmetic. Fixing
   them means `Q` → `q_at(dps)` per producer, which forces a PROTON-VS-MUON
   ANCHOR CHOICE each time — the layer straddle AGENTS.md singles out.
   **Owner decision, 32 times. Not guessable.**
2. **22 diagnosed reverts.** 17 "no gain" (12 with ZERO casts to remove — the
   float64 arrives by a route neither a dps raise nor a cast removal touches)
   and 5 laundering-guard hits (`codata_reconciliation` emitted
   `0.782333409309999949776…`: an exact mpf round-tripped through a double
   downstream, printed at 40 digits). Each needs its entry point found.
3. **The 593 remaining fields.** Re-measure; do not quote this figure.

## Traps established, each pinned by a selftest

- **The A/B split is a STATIC HEURISTIC and cannot settle any single
  producer.** A one-hop import-cone check reported "13 misfiled B→A" —
  RETRACTED: the inherited `set_compute_dps()` in `mass_at_3A_proper` is
  INSIDE A FUNCTION, and the hits came from an `ast.walk` descending into
  `def` bodies. An earlier regex draft was worse — it skipped comments with
  `line[0] != "#"`, letting through a docstring line starting with a backtick,
  so three producers were reclassified on the strength of PROSE.
- **"Round-trips through float64" does NOT prove laundering.** It flagged 55
  of 302 drained fields; all 55 are exact `k·2^-235` ULP residuals, and a
  power of two round-trips losslessly. Flag for reading, never decide.
- **The flip alone is necessary but NOT sufficient.** mpmath defaults to
  `mp.dps = 15` (~53 bits), so mpf constants still compute at float64 grade
  until the producer raises dps. Removing casts without raising dps is WORSE
  than nothing — it serializes a 53-bit value at full width (the
  float64-padding defect).
- **`math.log(mpf)` does not raise, it DOWNCASTS.** This module's own
  `Q_NEUTRON_MEV_ERR` was quietly the last float64 quantity after the casts
  came off.
- **`mpf(repr(x))` is right for a float, broken for an mpf.** `repr(mpf('.78'))`
  is `"mpf('0.78')"`, unparseable. 96 sites unwrapped; the OTHER 84 in the tree
  lift genuine floats and must stay.
