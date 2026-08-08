---
# qou-n1c4
title: 'dual-path xref: regenerate the muon-pinned y_lambda + markov-peel upstreams onto the proton anchor'
status: todo
type: task
created_at: 2026-08-08T16:59:17Z
updated_at: 2026-08-08T16:59:17Z
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
