---
# qou-lp5d
title: 'GAP: 5 convention-C B4 sites are unmigratable by substitution — z_C''s analytic properties ARE their subject'
status: completed
type: task
priority: normal
created_at: 2026-08-25T09:53:00Z
updated_at: 2026-08-29T16:35:03Z
---


## The finding

The 2026-08-25 non-B2 drain (PR #5754) migrated 2 of its 8 assigned B4 sites.
A third turned out to be a mis-binned B2 (fixed in the triage matcher, same PR).
The remaining **5 are blocked, and all for one reason**: the probe's own
SUBJECT — the thing it asserts and concludes — is an analytic property that
`z_C = sqrt(q)/(q+1)` has and `z_D = q^3/(q^2+1)` does not. Substituting z_D
does not move a value; it FALSIFIES the probe's own committed assertions and
desynchronises it from a sorry-free Lean companion.

The B4 label ("emits a committed witness — value change") is therefore wrong
for these, in a way that matters: it reads as a work item, so every future
drain will pick them up, re-derive this, and put them back.

## Measured, exactly and symbolically (sympy, no float anywhere)

| property | z_C = sqrt(q)/(q+1) | z_D = q^3/(q^2+1) |
|---|---|---|
| bar involution q -> 1/q | **bar-EVEN** (bar(z) = z) | **NEITHER** (bar(z_D) = 1/(q^3+q)) |
| order of (z - 1/2) at q=1 | **2** | 1 |
| dz/dq at q=1 | **0** (critical) | 1 |
| (4+6w+2w^2)z' + w z, w = q-1 | **0** (exact) | nonzero rational in w |
| in Q(q)? | no — the only non-rational ingredient | yes, trivially |

Both give z(1) = 1/2, which is why a shallow check would pass.
At the substrate proton pin: z_C = 0.49932033418, z_D = 0.61268803715 (+22.70%).

## The five, with what each would lose

1. **`computations/qbeta/qbeta_z_bar_parity_fmap_class_probe.py:72`**
   Assertion is literally named `z_bar_even_twist_1`. Whole conclusion (the
   "z-alone exclusion" narrowing the z -> c_k f-map class) is that a scalar
   functional of z is bar-even and so can never source the bar-odd a_1.
   Has a **sorry-free Lean companion, `QOU/QBeta/ZBarParity.lean`**.
   Under D: assertion 1 is false and the exclusion argument is gone.

2. **`computations/qbeta/qbeta_eval_map_bar_decomposition_probe.py:48`**
   Claims the evaluation map splits EXACTLY into bar-even h^2/2 plus bar-odd
   -h*z. That exactness needs z bar-fixed. Confirms sorry-free Lean lemmas
   `epsNP_decomp` / `epsNP_bar_image` / `trMNP_decomp`.
   Under D: -h*z_D is neither, so there is no exact split to confirm.

3. **`computations/qbeta/qbeta_t3_carrier_q1_order_preflight_probe.py:68`**
   Kill criterion T3-1 is "z is CRITICAL at q=1: dz/dq|_1 = 0, so rational
   functions of z realize only EVEN vanishing orders at q=1" — hence the
   odd-total-order parity argument excluding the f(z)*kappa sub-class.
   Under D: dz/dq(1) = 1, both parities are realizable, the exclusion evaporates.

4. **`computations/qbeta/qbeta_prearchimedean_z_recursion.py:103`**
   Entire subject is the holonomic structure of z: "z^2 = q/(1+q)^2 in Q(q), so
   every z^k reduces to A_k + B_k*z ... the ONLY non-rational ingredient is
   z(q); its coefficients carry all the holonomic structure." It then verifies
   the ODE above.
   Under D: z is already rational, A + B*z collapses, the ODE is false, and the
   probe has no subject at all.

5. **`computations/probes/qbeta_fmap_power_class_prune.py:89`**
   Builds the EXPLICIT `CanonicalMarkovWeightsH3` instance to record that it is
   a different inhabitant from the bridge object. That Lean instance is titled
   and documented as "an explicit **sqrt(q)-bearing** inhabitant"
   (`QOU/BraidKnot/QBetaCanonicalMarkovWeightsInstance.lean:9,34`) — i.e. it IS
   convention C by construction.
   Under D: the probe stops reproducing the instance it exists to compare against.

## Why this is not a judgement call

All five sit in the Q_beta c_k ladder cone, and AGENTS.md already rules on that
cone directly: it is "convention-C-frame throughout and has not been
re-derived" (bean `qou-cds1`), and — in terms — "**the ladder must be RE-DERIVED
under D, and that is NOT a z-swap**", because
`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free) makes the C-frame
ladder and the mass channel's three-row forcing mutually exclusive. So
substituting z_D into these is already forbidden.

The correct disposition is the D-frame re-derivation under `qou-cds1`, not a
migration. Until then every c_k conclusion downstream stays C-conditional,
which is what AGENTS.md already says.

## What to do

1. **Do not hand these to another drain as B4.** They need a triage bin
   distinguishing "substituting z changes a number" from "substituting z
   falsifies the file's own assertions". The B2 bin ("re-derivation, not
   substitution", already pointing at `qou-cds1`) is the right semantics — the
   B2 *detector* just keys on the ladder-phase shape and these do not carry it.
   Cheapest correct fix: extend the B2 test to also fire when the flagged z
   feeds a committed assertion whose name or docstring asserts a z property
   (bar-parity, criticality, vanishing order, rationality).
2. Alternatively register them in
   `docs/coordination/trace-convention-registry.json` under
   `blocked_migrations` with `stays: "C"` and a `superseded_by` pointing at the
   `qou-cds1` re-derivation, exactly as PR #5754 did for
   `markov_reduction_h3_to_h4_verify::z` — that route is proven to move a site
   out of the ACTIONABLE count.

## Provenance

Measured on branch `claude/convention-c-drain-b4-2026-08-25` (PR #5754),
2026-08-25. The z_C-vs-z_D table is exact sympy, reproducible in a few lines;
no float64 was used anywhere in producing it.

Closed 2026-08-29: landed in PR #5754 (merged 2026-08-25). The five remaining B4 sites and WHY each cannot be z-swapped are recorded in the probe.
