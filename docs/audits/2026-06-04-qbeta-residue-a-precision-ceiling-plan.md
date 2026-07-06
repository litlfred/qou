# Residue-A precision ceiling — can A be recomputed to ≥30 digits?

**Date:** 2026-06-04
**PR:** (this branch — `claude/qbeta-residue-a-precision-ceiling-2026-06-04`)
**Status:** PLAN (compute pending)
**Predecessor:** [PR #1804 — residue-A follow-up; D3 period reframe gated on precision](./2026-06-04-qbeta-residue-a-followup-verdict.md)

## The question

PR #1804 Direction 3 (PSLQ period probe) was INCONCLUSIVE because the
residue A is empirically known to only ~12 sig figs, while a 12-constant
period basis needs ≥ ~15 digits to resolve. The author asked: **recompute
A to ≥ 30 digits** to unblock the period reframe and any future
structural search.

## What A actually is (feasibility-critical)

Define the tail terms `x_k := c_k · u_subst^k`. Step 1 of PR #1727
([`qbeta_singularity_type_probe.py`](../../computations/qbeta/qbeta_singularity_type_probe.py))
extracts the **asymptotic limit** of the simple-pole signature

```
L := lim_{k→∞} x_k = lim_{k→∞} c_k · u_subst^k,   estimated as mean over k = 8, 9, 10
residue A := u_subst · L                          (the canonical "1.804e-15")
```

`u_subst` is exact-from-q₀, so `A` and `L` differ only by an exact
factor — they share the **same relative precision**, and "30 digits of
A" ≡ "30 digits of L". The current tail (100 dps compute, c_k from a
50-dps witness; `x_k` shown rounded):

| k | x_k = c_k · u_subst^k |
|---|---|
| 8 | 2.118358844e-13 |
| 9 | 2.117730782e-13 |
| 10 | 2.11774454e-13 |

`L ≈ tail_mean = 2.117944722e-13` (full precision 2.1179447222533e-13),
`tail_relative_spread = 2.0e-4`; residue `A = u_subst·L ≈ 1.804e-15`.

**So the precision limiter is NOT compute precision** — the c_k are
already 50 dps. It is the **asymptotic convergence**: L is the k→∞ limit
of a sequence sampled only at k = 8, 9, 10, which agree to ~4 sig figs.

## The two real obstacles

1. **More rungs (c_11…c_15) are blocked.** The Step-1 method note states
   extracting c_k beyond 10 from R(q₀) requires a postulated canonical
   form per rung — an ansatz fit, forbidden per AGENTS.md.
2. **Extrapolation needs clean asymptotics.** If `x_k = L + B·ρ^k`
   (`L` the tail limit, ρ = u_subst/u_2 set by the second-nearest
   singularity), three points k=8,9,10 give a Shanks/Aitken estimate of
   `L`. But the rungs are non-monotonic (x_8 > x_9 < x_10 slightly), so
   the convergence may not be clean single-geometric — extrapolation
   reliability must be tested, not assumed.

## This PR's actual deliverable

An honest **precision-ceiling analysis**, not a fabricated 30-digit A:

1. **Reload c_k at full witness precision**; recompute `x_k = c_k·u^k` at
   100+ dps to confirm the spread is intrinsic (asymptotic), not compute
   noise.
2. **Sequence-acceleration attempt** — Aitken Δ² and a 3-point
   `x_k = L + B·ρ^k` solve on k=8,9,10; report the extrapolated `L`
   (and `A = u_subst·L`) with an honest error estimate (how much the
   3-point fit can be trusted).
3. **Self-consistency** — if a 4th rung (k=7, transient) is included,
   does the extrapolation stabilise or diverge? Quantify the achievable
   digit count.
4. **Verdict**: state the realistic precision of A/L and the genuine
   unblock path (a higher-order *canonical* c_11+ extraction — a
   separate research program, NOT an ansatz fit).

## Anti-pattern guards (STRICT)

- No ansatz fit for c_11+ (forbidden); extrapolation uses only the
  existing canonical c_2…c_10.
- Report the extrapolated A/L with an explicit, honest error bar — do NOT
  claim more digits than the 3-rung data supports.
- ℏ_q / u_subst from canonical witnesses, never hard-coded.
- Diagnostic-only; no production wiring.

## Planned deliverables (this PR adds all of them)

```
docs/audits/
  2026-06-04-qbeta-residue-a-precision-ceiling-plan.md     # this file
  2026-06-04-qbeta-residue-a-precision-ceiling-verdict.md  # verdict
computations/qbeta/
  qbeta_residue_a_precision_ceiling.py
  qbeta-residue-a-precision-ceiling.witness.json           # auto-emitted
```
