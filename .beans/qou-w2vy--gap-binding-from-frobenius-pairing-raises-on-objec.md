---
# qou-w2vy
title: 'GAP: binding_from_frobenius_pairing raises on object dtype -- latent behind term 1''s hang'
status: todo
type: task
priority: high
created_at: 2026-08-31T04:44:27Z
updated_at: 2026-08-31T04:45:03Z
---

Blocks qou-i7ju together with qou-4m9u. Evidence:
docs/audits/2026-08-31-binding-energy-cannot-run.md.

## The gap

`binding_from_frobenius_pairing(1,1)` raises on main in 0.52s:

    TypeError: no supported conversion for types: (dtype('float64'), dtype('O'))

This is the SAME failure class the COO accumulator already fixed in
unified_iterative_correction -- scipy sparse refusing object dtype the moment an
mpf enters -- and it is UNFIXED here.

## Why nobody noticed

binding_energy applies term 1 (unified_iterative_correction) FIRST, and that
never returns for A>=2. Control never reaches term 3. The crash is latent behind
the hang.

Demonstrated: stub term 1 only, leave terms 2 and 3 as main has them ->

    binding_energy(1,1) deuterium RAISES TypeError
    binding_energy(1,2) tritium   RAISES TypeError
    binding_energy(2,2) he4       RAISES TypeError
    binding_energy(3,4) li7       RAISES TypeError

4 of 4. So binding_energy for A>=2 has TWO independent blockers, and fixing only
the performance one converts a hang into a crash.

## Corroboration

computations/hadron-knot-table.witness.json:
    computedAt      2026-06-17T04:13:13
    scriptCommitSha 08ec1c0d0999b6b6d8c902a4ec8fa5344a383a2d

2.5 months old. Its binding values predate whatever broke term 3, and nothing
since has been able to reproduce them.

## Term 2 for contrast

sdp_cross_channel_contribution(1,1) = 0.0 with BOTH the current and the
corrected matrices (27.9s / 67.1s). Unaffected, and zero, AT A=2 ONLY --
sdp_cross_channel.py consumes _build_ysn_matrices directly, so larger A is
untested and must not be assumed either way.

## Not established

The corrected-family run of term 3 had not completed at 10 min and is NOT
reported. Whether the crash is independent of which matrices are used is
untested -- though a dtype-conversion error suggests it is.
