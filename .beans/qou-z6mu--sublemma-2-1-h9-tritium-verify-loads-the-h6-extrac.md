---
# qou-z6mu
title: 'sublemma_2_1_h9_tritium_verify loads the H6 extract, and provably cannot use it: reconstruct_chi_h6_via_sublemma is never called'
status: completed
type: task
priority: normal
created_at: 2026-08-22T10:01:37Z
updated_at: 2026-08-22T12:27:12Z
---

## What

`computations/sublemma_2_1_h9_tritium_verify.py`:

- **loads** the H6 deuteron extract at runtime —
  `h6_data = json.loads(h6_path.read_text())` (line ~223), with a
  dedicated `--h6` CLI flag defaulting to
  `sublemma-2-1-A-operator-extract.witness.json` (line ~196);
- **opens with** a module docstring saying it "Loads the H_6 deuteron
  A^ξ_{μν'}(I_pn) extraction ... and the new H_9 A^λ_{ξν}(I_2)
  extraction";
- and the **only** consumer of that data, `reconstruct_chi_h6_via_sublemma`
  (line ~120), **is never called** — not in this file, not anywhere in the
  repo (grep across `--include=*.py`, excluding `_deprecated/` and
  worktree mirrors: one hit, the `def` itself).

## Measured, not inferred

The H6 extract's A matrices differ materially between the colour-blind
and colour-weighted p-n interface — **1.2e-4** worst relative, and the
deuteron `tr_M` moves `0.5750908 -> 0.5751722` on the same change.

Ran the verifier against both extracts and diffed every leaf field of the
emitted witness (excluding `computedAt` / `commitSha` / `durationMs` /
`scriptHash` / `environment`):

    differing leaf fields: 0

Bit-identical. The H6 input cannot reach the output.

## Scope — narrower than it first looks

The **emitted witness `description` is accurate**: it says Path B uses
`sublemma-2-1-A-operator-extract-h9-nn.witness.json`, and it does not
claim the H6 extract is consumed. So this is NOT a false witness claim
and NOT hollow verification of what the witness asserts — Path A vs
Path B at H_9 is a real check and really passes (30/30 over-determined,
max rel res 1.22e-13).

What is wrong is the **source**: a loaded-but-unused input, a CLI flag
that changes nothing, and a module docstring describing a computation
that does not run. A reader (or an agent tracing convention propagation,
which is how this surfaced) reasonably concludes the H6 pn interface is
cross-checked at H_9. It is not.

## How it surfaced

Porting `sublemma_2_1_A_operator_extract.py` off float64 (`qou-zck8`,
PR #5427) changed that witness's matrices from JSON numbers to decimal
strings. I traced every consumer for the string/number break and patched
the two bare `np.array(A_info["matrix_re"])` sites here — then noticed
the committed witness predated the weighted extract yet matched a fresh
run exactly, which is what prompted the swap experiment above.

Note the `dtype=float` fix at line ~171 is inside the dead function. It
is correct and kept, but it is currently inert; the live fix is the
second site (~line 299), which reads the H9 extract.

## Next honest step

Decide which of these it is:

1. **Revive it** — call `reconstruct_chi_h6_via_sublemma` and add its
   result as a third compared path. Then the H6 interface genuinely is
   cross-checked, and the `dtype=float` fix becomes live. This is the
   option that matches the docstring's intent.
2. **Remove it** — drop the function, the `--h6` flag and the load, and
   correct the module docstring. Cheaper, and honest.

Do not leave it as-is: the current state reads as option 1 while
behaving as option 2.


---

## RESOLVED (2026-08-22, PR #5427) — revived, not removed

The bean offered two dispositions. **Option 1 (revive)** was taken, because
measurement settled it: the function was never broken.

`reconstruct_chi_h6_via_sublemma` reproduces all 11 chi^xi from the
extracted A matrices to **5.5e-15**. Wired in as a guard on the CONSUMED
EXTRACT, it discriminates the exact defect this arc chased:

    canonical (colour-weighted) extract -> 5.51e-15   assertion passes
    colour-blind (pre-fix) extract      -> 9.17e-05   assertion FAILS

Verified end to end against both extracts, not in isolation: under the
blind one the witness goes `allPassed: false`, which the failed-assertion
ratchet would then catch.

**What it buys that the existing check cannot.** Under the blind extract
`overdetermined_path_a_eq_path_b_machine_eps` still passes 30/30. Path A
vs Path B is a structural identity holding for ANY word — convention-
agnostic by construction, and structurally incapable of seeing a frame
mismatch. This guard is the first thing in the file that can.

## Correction to this bean's framing

The bean implied the file's hardcoded `-H/2` inner was an off-convention
crossing to be fixed alongside. **It is not**, and I was wrong to read it
that way. Measured positionally against `atom_canonical_crossings`:

| atom | file len | canon len | gen-index mismatches | `d` mismatches |
|---|---|---|---|---|
| tritium | 35 | 35 | 18 | 25 |
| he3 | 35 | 35 | 18 | 25 |

The equal lengths are coincidence. `tritium_braid()` / `he3_braid()` build
a **different braid**, not a drifted one — `_proton_body()` carries its own
quark/gluon structure and claims to mirror `build_atom_nf`, not
`atom_canonical_crossings`. Since Path A = Path B is convention-agnostic,
that divergence costs the file's verification claim nothing, and "fixing"
the interface to weighted would have been wrong-headed.

**Left open, not settled here:** whether that 18/25 divergence is an
intentional independent test braid or drift from an older `build_atom_nf`.
Cheap to state, not cheap to resolve. Worth its own bean if anyone intends
this file to verify the *canonical* tritium rather than the sub-lemma.

## Also fixed in passing

First version serialized the guard residual as `fmt(mp.mpf(...))`, padding
a float64 to 50 digits; `witness_float64_padding_audit` caught it verbatim
("claims 0.0000000000000055131896... really 5.5131896097107105e-15"). The
value is genuinely float64 — the reconstruction is numpy and
`chi_lambda_fast` returns complex — so there is no mpf to carry from the
source. Now `.17g`, true float64 precision. Importing mpmath for it also
tripped the never-raises-dps ratchet; both imports removed.
