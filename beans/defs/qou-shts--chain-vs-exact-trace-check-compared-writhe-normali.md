---
# qou-shts
title: chain-vs-exact-trace check compared writhe-normalised chain to un-normalised trace (FIXED); the 0.4909 MeV/unit-d residual was mislabelled float64 noise
status: completed
type: task
priority: normal
created_at: 2026-08-15T22:53:20Z
updated_at: 2026-08-15T22:54:04Z
---


## What was wrong, and what it cost

`mass_binding_dashboard` validated its production binding chain against the
exact p(3A) transfer trace via `chain_resid = |B_sym − B_sym_exact|`. But
`_bond_type_L` applies the Lean-proved writhe normalisation
`L_XY → L_XY − (δe/2)·ln(1−h)` (owner directive 2026-08-09,
`QOU/QBeta/WritheNormalisation.lean`) and `tr_m_atom_zn` does not. So the
difference measured that factor rather than the factorisation.

Measured at 50 dps, `chain − exact`:

| iso | d = N−Z | residual |
|---|---|---|
| ²H  | 0  | −0.000338 |
| ⁴He | 0  | −0.000338 |
| ³H  | +1 | −0.491214 |
| ³He | −1 | +0.490539 |

`α·|ln(1−h)|/2 = 0.49087652466781`; the per-bond L discrepancy is
`|ln(1−h)|/2 = 0.11726677260729`, equal-and-opposite on pp/nn, zero on pn.
Matches every digit measured. It cancels iff `#pp = #nn` — the N = Z line —
so the check looked healthy on ²H/⁴He and could never pass on ³H/³He.

The footnote called it *"float64 dashboard noise"* — wrong by ~12 orders of
magnitude. Net effect: the ONLY non-circular check on the production binding
chain was structurally unable to pass off N = Z, and said so in a way that
invited ignoring it.

## Fix

`_chain_writhe_shift(Z, N, alpha)` sums the chain's own normalisation over its
bonds; applied to the trace side. Residual after: `2H 4.4e-16`, `3H 0.0`,
`3He 8.9e-16`, `4He 0.0`. So the chain closed form **is** the exact trace — what
`docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md` §1 claimed, and what
had silently stopped being true when the writhe normalisation and convention D
landed. That audit's ✓ table at ³H/³He is stale; it is not wrong about the
mathematics, only about the current numbers.

## Two corrections to my own work, recorded

1. **My hyperbola probe's CHECK 1 was circular.** It tried `mbd.b_sym_mev`
   (does not exist) and silently fell back to rebuilding the same closed form,
   then reported `4.44e-16` as evidence that "production B_sym IS the
   hyperbola". It compared the expression against itself. Replaced by CHECK 1b
   against the exact trace (worst `1.78e-15` over ²H/³H/³He/⁴He), which is what
   licenses reading the no-peak exclusion as a claim about the *exact* object.
2. **I applied the writhe shift with the wrong sign first**, which doubled the
   residual (0.49 → 0.98) instead of clearing it. The docstring now records that
   diagnostic, since the sign is easy to get backwards and the failure mode is
   distinctive.

## Status

Done, on PR #4973. Not a witness change — this branch modifies zero
`*.witness.json`.
