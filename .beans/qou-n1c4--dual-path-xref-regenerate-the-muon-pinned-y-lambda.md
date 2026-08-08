---
# qou-n1c4
title: 'dual-path xref: regenerate the muon-pinned y_lambda + markov-peel upstreams onto the proton anchor'
status: todo
type: task
created_at: 2026-08-08T16:59:17Z
updated_at: 2026-08-08T16:59:17Z
---

## Progress log (2026-08-08)

The wave is **three deep, not two**. `markov_peel_atomic_witness.py` reads
`atomic-tr-m-mpfr-50dps.witness.json` (the Hoefsmit+Wenzl bridge, produced by
`atomic_tr_m_mpfr_50dps.py`), which is muon-pinned too. Correct order:

    regenerate_y_lambda_mpfr.py  ->  atomic_tr_m_mpfr_50dps.py
                                 ->  markov/markov_peel_atomic_witness.py

Three driver defects had to be fixed first (all landed in 9e03e5ee):

1. **12 witnesses were invisible.** They are named `<stem>-witness.json` with a
   HYPHEN, and `dirty_witnesses()` matched only `<stem>.witness.json`. The whole
   y-lambda family is in that set — the base of this very chain. Measured: y_λ
   re-anchored muon→proton and the driver logged `touched: []`, recorded
   NOCHANGE, and left it dirty and UNJUDGED.
2. **Dependency ordering existed but was inert**, and its tests passed anyway
   (fixtures wrote via `write_text`; the corpus writes via `WitnessBuilder`).
3. `dirty_witnesses()` read a failed git call as a clean tree. Defensive fix
   only — not the cause of (1).

### Expect the peel to be rejected again, and do not loosen the bound for it

Its `abs_diff_vs_bridge` is a **residual** — true value near zero — and the
classifier's `ANCHOR_COLLATERAL_MAX` is *relative*. A perfect re-anchor taking
that field from ~1e-7 to ~1e-19 is a 100% relative move and reads as VALUES.
The first run already rejected it at 6.73e-4.

That is the classifier being right for the wrong reason, and the fix is NOT to
widen the tolerance: a bound relaxed to admit one known-good diff stops
constraining every unknown one. Review the peel diff by hand and, if the
residual collapsed as predicted, commit it deliberately by explicit path with
that reasoning recorded.

### Ordering caveat for the 32 downstream consumers

`dependency_order` only sees witnesses named as literal filenames. Producers
reading y_λ through the `_load_y_lambda` helper have no filename in their
source and so get no edge — `chi_at_q0_via_hoefsmit_mpfr.py` sorts ahead of
y_λ for exactly that reason. Verify the order by reading the code before
trusting it on the full set, or teach the analysis the known accessors.

---

Not claimed. Left open deliberately: this is a migration wave, not a
follow-up, and it should be planned rather than picked up mid-session.

## The finding

`computations/chi_dual_path_xref_audit.py` (added f918a887) cross-checks each
χ cache against the markov-peel scalar. The three legs of that comparison are
no longer on the same q₀ pin:

    chi tables    MIXED  — deuteron/⁴He/proton proton-pinned,
                           tritium/helium-3/neutron still muon-pinned
    y_lambda      muon   — computations/y-lambda-mpfr-witness.json
    markov-peel   muon   — computations/markov/markov-peel-atomic-tr-m.witness.json

Relative gap Σ_λ y_λ χ_λ vs the peel scalar:

    proton     2.221e-50     neutron    1.237e-51
    tritium    9.111e-20     helium-3   9.111e-20
    deuteron   1.704e-07     helium-4   3.261e-07

Same pin agrees to ~1e-19; cross-pin lands at 1e-7. ⁴He is the controlled
experiment — the identical 77-partition table scored 9.111e-20 before the
proton rebuild (4fb4ac54) and 3.261e-07 after, with nothing changed but the
anchor.

## Why it is not urgent, and not optional either

The χ rebuild was right. The two upstreams are simply older than their own
producers: `q_parameter` exports the proton pin today, and both stale legs read
it at import —

    markov/markov_peel_atomic_witness.py   ← Q_50_DIGIT_STR
    regenerate_y_lambda_mpfr.py            ← Q_MP

so each re-anchors to proton on its next run. Nothing is wrong that a
regeneration does not fix. But it is not a small regeneration: 14 witnesses
name these two as upstream and ~50 producers consume them, so re-anchoring the
base re-anchors the subtree above it.

## Do it as a wave

Regenerate under `witness_regen_wave.py`, not by hand — same discipline as the
anchor migration: per-witness revert, clean-tree start, classifier verdict per
witness, commit by explicit path. Order matters: `regenerate_y_lambda_mpfr.py`
and `markov_peel_atomic_witness.py` first, then everything that consumes them.

## The acceptance test is already written

Re-run `chi_dual_path_xref_audit.py` afterwards. Every atom should read AGREES
at ~1e-19. Any atom left at 1e-7 means a leg was missed; any atom that goes
DISAGREES at one pin is a real χ defect the split had been masking.

## Two open observations — do not treat as settled

- Both A=1 atoms (proton, neutron) agree to ~1e-50 *despite* being cross-pinned,
  so the single-nucleon comparison is not testing the anchor at all. Whether
  that is a cancellation at n=3 or the peel row for A=1 being derived from the
  same inputs — which would make it circular — is not established.
- The same-pin floor moves with n: ~1e-50 at n=3, 9.111e-20 at both n=9 and
  n=12. Tritium and helium-3 landing on the *identical* 9.111e-20 points at a
  shared input (most likely the y_λ table's precision) rather than anything
  atom-specific. Nothing above n=12 has been measured.

## Related correction, already landed

`_b0vf_complete_he4_witness.py`'s GATE B claimed a "~4.8e-8 intrinsic
two-implementation gap". It is not intrinsic — it is the deuteron's own anchor
mismatch. Worse, GATE B's tolerance is `10·B_D` with B_D measured off that same
cross-pinned deuteron, so the bound inflated to 1.7e-06 and now admits ⁴He's
3.261e-07. Re-run today the gate PASSES: it did not go red, it stopped
discriminating. Corrected in place at the claim; the replacement audit fixes its
bound as a constant and self-tests that it is not derived from a witness.
