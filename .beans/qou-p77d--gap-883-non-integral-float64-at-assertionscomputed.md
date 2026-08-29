---
# qou-p77d
title: 'GAP: 883 non-integral float64 at .assertions[].computed/.expected across 300 witnesses — the class #5910 deferred'
status: todo
type: task
priority: normal
created_at: 2026-08-29T02:28:37Z
updated_at: 2026-08-29T11:09:27Z
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
