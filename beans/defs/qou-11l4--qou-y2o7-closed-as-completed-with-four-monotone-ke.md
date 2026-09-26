---
# qou-11l4
title: 'qou-y2o7 closed as completed with four monotone-kernel consumers unlisted: four qbeta probes are locked to the grouped ordering and its blast radius never named them'
status: todo
type: task
created_at: 2026-09-14T09:49:46Z
updated_at: 2026-09-14T09:49:46Z
---

## Measured

`chi_monotone_transfer.chi_all_lambda` REFUSES the canonical word:

    grouped   gens [0,0,0,0,0,0,0,1,1,1,1]  -> OK, chi_(3) = 1.38249446339
    borromean gens [0,1,0,1,0,1,0,0,1,0,0]  -> ValueError: non-monotone word:
                                               gen 0 after 1

That is `qou-y2o7`'s exact mechanism — a consumer of this kernel is **locked**
to the grouped ordering and cannot be moved by editing its word builder; it
would crash. `qou-y2o7` is marked **completed** and its "Blast radius — 18
consumers" section names exactly one qbeta probe,
`qbeta_delta_vs_deltaTbeta_settled_probe`.

**Four more import the same kernel and build the same grouped nucleon word:**

  * `qbeta/qbeta_chi_block_symbolic_closure_probe`
  * `qbeta/qbeta_d_frame_baseline_element_consistency_probe`
  * `qbeta/qbeta_d_frame_trace_baseline_probe`
  * `qbeta/qbeta_epsnpq_functional_mismatch_probe`

All four compute `chi_lambda(beta_n) - chi_lambda(beta_p)` off
`_word(_PROTON_G0, _PROTON_G1)`. None is in the list of 18. Fourteen live
files import `chi_monotone_transfer`; the rest are kernel infrastructure
(`chi_general_word` as fallback, `chi_window_transfer`,
`reduced_block_kernel`, the conformance harness) or already-known probes.

## How they were found, which is the point

Not by re-auditing the kernel. `intra_ordering_structural_assembly_audit`
(bean `qou-t29k`) selects on the SHAPE of the word assembly — all of `g0` then
all of `g1` — and these four turned up in its baseline. The kernel lock was
then visible one import line away. `qou-y2o7`'s own closing note says the
lesson for future audits is that "a selector keyed on *breakage*" misses
things; a selector keyed on the assembly shape found what its own
consumer-enumeration missed.

## Severity: LOWER than it sounds, and worth saying so

A monotone-kernel caller cannot silently report a wrong-frame number. It
either uses the grouped word (correctly, by construction) or raises. So these
four are **safer** than the two sites escalated under `qou-u8ji` and
`qou-y1w0`, where the canonical word computes fine and quietly destroys the
agreement with experiment. The defect here is that the frame is undeclared and
its forcing mechanism is invisible at the call site — not that a wrong number
is in circulation.

## Two separable pieces of work

1. **Declare the frame** (cheap, zero numeric change): route each `_word`
   through `pyhecke.atom.grouped_word_from_chains` and say in the docstring
   that grouped is FORCED by `chi_monotone_transfer`, which raises on the
   canonical word. Drains them from `qou-t29k`'s ratchet into its advisory E
   count, where they stay visible.
2. **Migrate the kernel** (the real fix, and `qou-y2o7`'s own remedy): swap to
   `chi_general_word.chi_all_lambda_any`, which accepts a non-monotone word —
   `closed_form_tau_M` already did exactly this. THEN the frame becomes a
   choice rather than a constraint, and the choice needs the same
   quantity-class triage as every other `qou-t29k` site. These four compute a
   CROSS-NUCLEON DIFFERENCE, which is not in the invariant class, so that
   choice will move their numbers.

Do 1 without 2 and nothing is fixed, only labelled — which is why `qou-t29k`'s
check E counts declared uses out loud instead of letting them disappear.

## Not claimed

That `qou-y2o7`'s completed work is wrong. Everything it did land was verified.
The gap is enumeration: it fixed the consumers it found.
