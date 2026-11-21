---
# qou-q0dr
title: 'q0-anchor refill: five probes whose premise has moved — re-run as failing record, update, or retire?'
status: todo
type: task
priority: normal
parent: qou-c20n
created_at: 2026-11-21T07:30:00Z
updated_at: 2026-11-21T07:30:00Z
---

Found while draining the q0-anchor refill ratchet (PR #8751, owner request
2026-11-21). These five witnesses have no top-level `q0Anchor`, so they stay
on the ratchet. Each producer runs, but its re-run records assertion FAILURES
because what the probe measured has since changed upstream. Re-running was
therefore NOT committed; the decision is the owner's.

| witness | what fails on re-run | why |
|---|---|---|
| `probes/the_character_closure_block_and_a_lean_file_publish_convention_c_probe` | 2 of 5 checks (was 1 of 5) | the block's table no longer matches the C-frame gap it was written to expose |
| `probes/the_em_coupling_projection_block_cites_a_producer_that_leaves_no_witness_probe` | check 4 | the producer the table names now emits a witness: the finding was fixed |
| `qbeta/qbeta-zd-rescore-price` | "dashboard Q_beta row is the priced z_D figure" (5.84e8 vs 4.3157e8 ppb) | the dashboard moved to the tower-summed E0 and the nuc11 element after the probe |
| `probe-k3-selfnormalized-recheck` | crashes: `fr_pullback_k3_test.dim_q` no longer exists | the k3 module was rewritten (`dim_q_mp`, self-normalised denominators); the probe's monkeypatch premise is gone |
| `qbeta/d1b-published-41-quiver-confirms-node-count` | path fixed by hand -> runs, then C5/C6 fail | library refresh #8515 re-sectioned physrevd108106023; the C61/C81 matrices are now OCR'd as bracket glyphs, so the width scan finds no rows |

## Options (same for each)
1. **Re-run and commit the failing witness** as the current record, with the
   producer stamped. Cost: minutes. Risk: five witnesses with `allPassed:
   false` that record "this defect has since been fixed"; the
   failed-assertion audits will report them.
2. **Update the probe to the current state** (new assertions, or read the
   old OCR from git history for d1b-41). Cost: ~30-60 min each. Commits to
   maintaining probes whose question is answered.
3. **Retire the probe** (move it under `fsh-guts/deprecated/`, keep the
   witness as a dated record). Needs an explicit retirement rule for the
   ratchet, since a baseline must not be widened.

Default if nothing is decided: nothing changes; the ratchet keeps reporting
these five.
