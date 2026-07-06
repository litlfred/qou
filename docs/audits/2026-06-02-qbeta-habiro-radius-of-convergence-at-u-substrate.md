# Q_β Habiro element — radius of convergence equals u_substrate

**Date:** 2026-06-02
**Branch:** `claude/qbeta-habiro-element-2026-06-02` (PR #1713)
**Trigger:** Phase B symbolic q-difference attack (Topic 1 of PR #1698 follow-up).

## Result

The Q_β precision-ladder Habiro element `F(u) = Π_{k=2..} (1 + c_k u^k)` has **radius of convergence exactly equal to `u_substrate ≈ 0.008517`** at q₀. Equivalently:

```
lim_{k→∞} c_{k+1} / c_k  =  1 / u_substrate  ≈  117.409001
```

Empirical (SDP-extracted c_k at 50 dps, [`qbeta-decay-sdp-extended-ck.witness.json`](../../computations/qbeta/qbeta-decay-sdp-extended-ck.witness.json)):

| k → k+1 | c_{k+1} / c_k |
|---|---|
| 2→3 | 1.976 (transient) |
| 3→4 | 0.569 |
| 4→5 | 1.069 |
| 5→6 | −2.860 |
| 6→7 | 16.34 |
| 7→8 | 133.84 |
| **8→9** | **117.37** |
| **9→10** | **117.41** |

Asymptotic value at k=8,9,10 matches `1/u_substrate = 117.40900` to 4 significant figures. The first 5–6 c_k are transient (anchor-dependent fingerprint structure); the geometric regime takes over from k ≈ 8.

## Why this matters

**The Q_β precision ladder is evaluated AT the boundary of its own analyticity.** Per AGENTS.md §"Im(q) fibre vs observable" (2026-06-01):

> The c_k Taylor coefficients live in the FIBRE (formal q-deformation, potentially complex). Each q_0 anchor is a different archimedean evaluation of the SAME fibre object.

This finding sharpens that framing: the fibre-level F(u) has a singularity at the substrate evaluation point u = u_substrate. The c_k cross-anchor swing (2.98 % between q_proton and q_muon, documented in 2026-05-31-qbeta-c3-q0-stability-verdict.md) is exactly what you'd expect when probing a complex-analytic function NEAR a pole — the "value" you measure depends sensitively on which anchor you pick because each anchor is a different ray approaching the singularity.

## What this rules out

- ❌ **2-term constant-coefficient linear recurrence** `c_{k+1} = α·c_k + β·c_{k-1}` with α, β constant. Tested across k=3..6; α-spread 318×, β-spread 766×. Refuted.
- ❌ **F(u) analytic everywhere near u_substrate**. The c_k series diverges; tail contributions to `log F` are O(10⁻¹³) per term and DO NOT decay (each `c_k · u^k` is roughly constant at large k).
- ❌ **The Habiro element is a polynomial in u** with finitely many nonzero c_k. The c_k grow geometrically; F is an infinite series with singular behaviour.

## What this confirms (and sharpens)

- ✓ **AGENTS.md fibre-vs-observable framing**: the Q_β c_k do live in the fibre; their archimedean evaluation at q_0 hits a singularity of the underlying analytic structure.
- ✓ **The 4-session c_3 flip-flop**: searching for a REAL formula `c_3 = f(q_0_real)` matching multiple anchors was always going to fail near a singularity — the function value is well-defined fibre-side but anchor-dependent observable-side.
- ✓ **The "accidental cross-order coincidence" of c_3 = −2 with the per-block Δtr_M leading −2** (2026-05-31 audit `qbeta-c3-order-audit-accidental-coincidence.md`): the per-block forms have a smooth leading term; the c_3 value is set by the singular structure of F at u_substrate. Different objects, different orders, coincident value to first significant figure only.

## What the next step looks like

To extract the fibre-level F(u) categorically, one needs to identify the **specific singularity at u = u_substrate**. Candidates (none ruled in yet — research-grade open):

1. **Simple pole** at `u = u_substrate`: F(u) ~ A/(u − u_substrate) near substrate. Test: c_k behaviour `c_k ~ A / u_substrate^{k+1}` to high order; check whether A is a recognizable q_0-rational constant.

2. **Branch point** of fractional order: F(u) ~ (u − u_substrate)^β · G(u) for non-integer β. Test: log-derivative `u · d/du log F = β · u/(u − u_substrate) + O(1)` has a known coefficient.

3. **Essential singularity**: F(u) ~ exp(1/(u − u_substrate)) or similar — the c_k still diverge geometrically with ratio 1/u_substrate, but with an extra exponential prefactor that would show up in the ratio of the asymptotic constant 2.12e-13.

The radius-of-convergence finding does NOT discriminate among these; further structural work (compute the next 10 c_k via SDP, check log-derivative coefficients) is needed.

## Sibling coordination

This finding may be relevant to PR #1521 (α_em Habiro categorical ID) — if α_em's Habiro element `[2]_q · (1 − h²α)` exhibits the same radius-of-convergence pattern (or doesn't), that informs whether u_substrate is a Q_β-specific structural anchor or a universal feature of substrate-evaluated Habiro elements. Will follow up.

## What this PR does NOT claim

- Does NOT identify the specific singularity type.
- Does NOT propose a c_k closed form.
- Does NOT refute or confirm the categorical ID question (still open).

## Files

- Probe: [`computations/qbeta/qbeta_habiro_q_difference_recurrence_probe.py`](../../computations/qbeta/qbeta_habiro_q_difference_recurrence_probe.py)
- Witness: [`computations/qbeta/qbeta-habiro-q-difference-recurrence-probe.witness.json`](../../computations/qbeta/qbeta-habiro-q-difference-recurrence-probe.witness.json)

## Cross-references

- Scope: [`docs/coordination/2026-06-02-qbeta-habiro-element-scope.md`](../coordination/2026-06-02-qbeta-habiro-element-scope.md)
- Fibre-vs-observable framing: AGENTS.md §"Im(q) at fibre vs observable level (2026-06-01)"
- c_3 cross-anchor swing: [`docs/audits/2026-05-31-qbeta-c3-q0-stability-verdict.md`](2026-05-31-qbeta-c3-q0-stability-verdict.md)
- Accidental-coincidence audit: [`docs/audits/2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`](2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md)
- SDP c_k extraction: [`computations/qbeta/qbeta-decay-sdp-extended-ck.witness.json`](../../computations/qbeta/qbeta-decay-sdp-extended-ck.witness.json)
