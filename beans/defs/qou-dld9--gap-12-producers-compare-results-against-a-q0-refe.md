---
# qou-dld9
title: 'GAP: 12 producers compare results against a q0 reference at the OTHER anchor (11 are the tr_m_q_hecke defect exactly)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T21:42:27Z
updated_at: 2026-10-04T15:19:36Z
parent: qou-5vkl
---

## Provenance: the generalization of a defect found and fixed in PR #5723

`tr_m_q_hecke_seminormal` resolves PROTON (undeclared ⇒ runtime default) while
its `REF_WITNESS` was the base-name `atomic-tr-m-mpfr-50dps.witness.json`, which
is `ideal_muon`. A proton-pinned twin sat beside it, unread. Measured:

    atom       vs MUON ref     vs PROTON ref
    proton      7.8403e-8       4.67e-51
    deuteron    1.5143e-7       1.86e-50
    helium-3    2.5171e-7       3.31e-51

The two routes agree EXACTLY. The entire "~1e-7 methodological discrepancy" that
producer had reported for its whole existence was the 11.5 ppb mu-p q0 gap,
amplified ~n-fold because tr_M is a product over ~n crossings. I initially wrote
that residual up as REAL STRUCTURE and retracted it (PR #5723).

**It is not a one-off.** `computations/audits/reference_anchor_straddle_audit.py`
(new, in #5723) reports **120 straddles** corpus-wide, of which:

    11 producers read atomic-tr-m-mpfr-50dps.witness.json (muon) at the proton pin
       -- the SAME defect, with the SAME twin available and unread
    12 producers total are fixable TODAY because an anchor-matched twin exists

The 12:

    atomic_mass_via_rho_k                    markov/markov_trace_axiomatic_multi_atom
    atomic_tr_m_helium4                      probes/rho_f_categorical_probe
    binding_K_direct                         rho_k_h3a_refinement
    canonical_tr_m_three_path_comparison     sigma_shell_from_beta_chain
    cross_check_trM_wenzl_lr_1ppb            sweeps/paper_six_term_isotope_sweep
    deltalambda/rho_k_h3a_residual_decomposition   tr_m_jones_markov_cross_check

`cross_check_trM_wenzl_lr_1ppb` is worth reading first: a 1-ppb cross-check
measuring against the wrong layer cannot mean what its name says.

## CANDIDATES, NOT CONFIRMED DEFECTS

Each of the 12 needs reading before it is called a defect. A producer may
deliberately want the muon reference; the audit cannot see intent, only the
mismatch. The three known-deliberate cases (`atomic_tr_m_mpfr_50dps`,
`markov_peel_atomic_witness`, and now `tr_m_q_hecke_seminormal`) are already
separated out by the audit because they NAME BOTH TWINS -- that is the
discriminator, not the mismatch alone.

## Why nobody saw it, and why that predicts more

The producer computed in float64, whose error was the SAME ORDER as the straddle.
A wrong answer sitting under a noise floor of its own size is invisible to every
check that reads the number. It became legible only once the arithmetic went
exact (#5714 measured the kernel at ~14 digits; #5723 drained three consumers).
So the population at risk is precisely the one that cannot be found by looking at
results -- which is the argument for the detector rather than for spot fixes.

## Measurement discipline note: the first count was 214 and was the wrong question

Two unrelated things both present as "producer pin != reference pin":

  (1) the producer reads `q-pinning-50-digit.witness.json` to OBTAIN q0 -- that
      string IS the muon anchor's definition, so it COMPUTES AT MUON while
      `resolve_q0_anchor` reports the proton default. A mislabel, the documented
      `qou-aj91` class (~85 producers), already being fixed on the stamping side
      by PR #5699. It swamped the result 200:1.
  (2) the producer computes at its own pin and COMPARES ITS RESULT against a
      reference at the other pin -- this bean.

Only (2) is the question here. Anchor-defining sources and audit tooling (which
read witnesses AS DATA TO INSPECT) are excluded by name in the script, with the
reasoning recorded there. Reporting 214 would have buried 12 actionable rows
under 200 belonging to someone else's fix.


## 2026-08-25 ALL 12 ADJUDICATED — 9 fixed, 1 deliberate, 1 false positive, 1 deferred

Read every one rather than assuming the pattern. The 12 split three ways, and
two of the three groups would have been damaged by a blanket fix.

### FIXED (9) — anchor-matched to the existing twin

    atomic_mass_via_rho_k          rho_k_h3a_refinement
    binding_K_direct               sigma_shell_from_beta_chain
    canonical_tr_m_three_path_comparison   paper_six_term_isotope_sweep
    rho_f_categorical_probe (MIRROR: muon pin reading a PROTON peel)
    tr_m_jones_markov_cross_check
    atomic_tr_m_helium4  -- DEFERRED, see below

Six carry a DECLARED pin (`physical_proton` / `ideal_muon`), which is a positive
statement about their layer; the rest resolve proton by runtime default.

### DELIBERATE (1) — `rho_k_h3a_residual_decomposition`

Its docstring already decomposes this exact residual and says explicitly: "WHICH
LAYER IS CORRECT for this probe. MUON -- do not 'fix' this by moving the probe to
the proton pin." It is a probe ABOUT the straddle. Left alone.

**But its stated REASON is stale**: it says regenerating the input at the proton
pin "is part of the bulk migration that is explicitly GATED behind bean
qou-1c4y". The proton twin `atomic-tr-m-mpfr-50dps-proton.witness.json` was
created 2026-08-08 and covers the same five atoms; the probe was last touched
2026-08-16. No regeneration is needed and none is gated. The conclusion may still
stand -- a straddle probe needs the straddle -- but the justification does not.

### FALSE POSITIVE (1) — `markov_trace_axiomatic_multi_atom`

Names the reference five times, in comments and a `"canonical_witness":` dict
value, and NEVER LOADS IT. The audit's regex matched prose. Fixed in the audit
with an AST load-detector (below).

### DEFERRED (1) — `atomic_tr_m_helium4`

The fix is applied and step (A) confirms it works (`|tr_M(n)| = 0.98774368811`,
the proton value). But step (B)'s direct H_12 recursion ran > 25 min without
completing, so its witness cannot be regenerated in this container. Committing
the producer change without the witness would create exactly the staleness this
whole arc is about, so it is EXCLUDED and left for a longer budget.

## The audit's third false-positive class, now fixed

`_names_actually_loaded()` walks the AST and counts a name as loaded only when it
is a call argument, an iterated list element, or a bound constant referenced
elsewhere. A LINE-LOCAL check is not sufficient -- `for legacy_name in ["x.json"]:`
then `HERE / legacy_name` is a real load whose string sits on a different line,
and my first line-local attempt gave TWO WRONG VERDICTS out of three. Selftest
pins all three hand-verified answers.

That is the third such class after audit tooling and pure-comparison scripts.

## Measured effect, with staleness separated from the fix

Diffing witnesses was not enough: the committed baselines are themselves stale
from the 2026-08-22 bridge regeneration, so a re-run moves values for TWO
reasons. Separated by re-running with the reference REVERTED:

    tr_m_jones_markov_cross_check, jones_markov_abs
        committed 0.41539578633  ->  re-run UNCHANGED ref 0.50540422769
        -- a 22% move that is PRE-EXISTING STALENESS, not my edit

    same file, canonical_abs_tr_M
        re-run unchanged ref  1.1457597823   (muon, current)
        re-run anchor-FIXED   1.1457596925   (proton, current)
        -- 7.8e-8: THAT is my edit

Per-producer, the fix's own effect:

    rho_k_h3a_refinement   Schur-Weyl residual  8.5e-8 -> 1.3e-50   PASS
    rho_f_categorical_probe   tr_M_proton       7.9e-8
    sigma_shell_from_beta_chain  abs_tr_M_beta_D  reads proton now
    binding_K_direct       18 of 30 moves are anchor-sized (<1e-6)
    atomic_mass_via_rho_k  RESULTS UNCHANGED -- only provenance metadata moved
                           (the muon read is a fallback Model B overwrites)
    paper_six_term_isotope_sweep   ZERO fields moved

## Two traps in the mechanical fix

1. **Skip guards.** `binding_K_direct` and `atomic_mass_via_rho_k` glob
   `atomic-tr-m-*.witness.json` and skip the primary by name. Renaming that name
   to the proton twin meant the MUON file was no longer skipped and would enter
   through the glob as an "extension" -- silently reintroducing the straddle by
   the back door. Guards widened to skip BOTH layers.
2. **My own diff truncated an exponent.** I reported `rho_k_h3a_refinement` as a
   catastrophic regression, residual `8.5e-8 -> 1.347`. The producer printed
   `1.347e-50  PASS`; my diff sliced the string to 22 chars and cut the `e-50`.
   The fix had worked perfectly. Caught by reading the producer's own output.
