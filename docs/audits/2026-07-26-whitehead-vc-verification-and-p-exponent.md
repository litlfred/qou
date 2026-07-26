# Whitehead link Volume-Conjecture verification + the p-exponent gate on the exact prefactor

**Date:** 2026-07-26
**Branch:** `claude/whitehead-habiro-kashaev-lupmgo`
**Follow-up to:** PR #4274 (merged — Whitehead Kashaev/colored-Jones factor-2 reconstruction)

## Summary

The Whitehead link (L5a1) is a **conditional B1 row** in
[`b1-hyperbolic-rows-theorem`](../../content/quantum-observable-universe/appendix-surreals/b1-hyperbolic-rows-theorem.md),
whose Step 3 (the Volume-Conjecture asymptotic) is the per-knot gap. PR #4274 supplies
the in-corpus **numerical** VC verification for that row. This note records what is
established, what is Lean-proved, and the one sub-item that remains genuinely open.

## What is established (numerically, PR #4274)

1. **Leading order — formula-free.** The reduced colored Jones (built from the
   validated `U_q(sl₂)` R-matrix, `whitehead_colored_jones.py`) at `q = e^{2πi/N}`
   grows at rate `Vol(L5a1) = 4·G = 3.66386` (regular ideal octahedron), identifying
   the braid `β_W = σ₁σ₂⁻¹σ₁σ₂⁻¹σ₁` against the negative control `[1,1,2,2,-1]`
   (torus link L4a1, Vol 0). Witness: `whitehead-volume-identification.witness.json`.

2. **Sub-leading — mpmath exact-root.** With exact anchors N=6,8,10,12
   (fast O(N⁸) path, dps=60): `c₀ = −0.53 ± 0.08 → factor ≈ 1.97 → FACTOR 2`,
   under the prefactor map `c₀ = −0.87 + ½·ln(factor)`. The fit is validated by the
   figure-eight exact reference `c₀ = −0.273 ≈ −¼ln3`. Witness:
   `whitehead-c0-mpmath.witness.json`.

## What is Lean-proved (this PR, sorry-free)

`QOU/Archimedean/WhiteheadVolumeCatalan.lean` — the Step-2 geometric input, over the
shared `catalan_G` / Lobachevsky infrastructure:

- `vol_L5a1 = 4·G` (`rfl`);
- **`vol_L5a1 = vol_B3 / 2`** — exact half-Borromean identity (one octahedron vs two);
- `vol_L5a1 = 8·Λ(π/4)`, positivity, `3.66 < vol_L5a1 < 3.67`, `vol_L5a1 < vol_B3`.

The **Volume Conjecture itself is NOT Lean-proved** and is not laundered into a theorem
(§Axiomatization-is-NOT-a-Proof): the asymptotic stays a conjecture-class; the numerics
above are evidence for its instance, not a proof.

## The open sub-item: the growth exponent p (gates the *exact* prefactor)

The factor-2 assignment assumes **p = 3/2**, the growth exponent
`log|J| = (Vol/2π)N + p·log N + c₀ + …`. That is the value for a hyperbolic **knot**
(1 cusp). The Whitehead is a **2-cusp link**, where p need not be 3/2.

**Discriminating control (exact data through N=14, both links/knots).** The exact-root
tower now reaches N=14 for both objects (Whitehead N=14 anchor `|J_red| = 117161.339`,
95 min at dps=60). The p-free fit is run in matched windows so the figure-eight (whose
true exponent is 3/2) calibrates the method's bias:

| fit window | figure-eight 4₁ (true p=3/2) | Whitehead L5a1 |
|---|---|---|
| (p,c₀,d), N=6,8,10,12 | 1.617 | 1.596 |
| (p,c₀,d), **N=8,10,12,14** | **1.538** (→ 3/2) | **1.151** |
| (p,c₀,d,e), N=6..14 | 1.450 | 0.657 |
| (p,c₀), N=10,12,14 | 1.545 | 1.555 |

**The figure-eight cleanly converges to ≈1.5; the Whitehead does not.** Over the same
windows its p-free exponent scatters **0.66–1.60** and, crucially, *destabilises* when
N=14 is added (the N=8–14 window drops to 1.15, the 5-point fit to 0.66) rather than
tightening onto 3/2 as the figure-eight does. So p is **not pinned to 3/2** for the
2-cusp link, and the *exact* prefactor (hence an exact `c₀`, hence turning "factor ≈ 2"
into an exact statement) is **contingent on p**.

**Scope (per §"refuted"/"open" discipline):** this is a *scope-limited* open item, not a
refutation. The factor-2 reading is correct **under p = 3/2**; what is open is whether
the 2-cusp link exponent is 3/2 or a distinct value. Two routes to close it:

1. **More N.** N=14 is now done (above) and did **not** stabilise p — it made the fit
   *worse*-behaved, the signature that the simple `p·log N + c₀ + d/N` ansatz is the
   wrong asymptotic form for the 2-cusp link (a distinct power, or an extra `log N` /
   per-cusp Gaussian factor). N=16 (~4 h) alone is unlikely to settle it without the
   correct functional form; this route is now secondary to the theory route.
2. **Theory (primary).** Derive the 2-cusp-link refined-VC exponent (Ohtsuki–Takata-type
   saddle/Gaussian-per-cusp analysis) and the adjoint Reidemeister torsion of L5a1
   (trace field `ℚ(i)`), giving the exact prefactor directly — the analogue of the
   figure-eight's `1/3^{1/4}` (torsion `√3`).

## Status of the Whitehead B1 row

Leading-order VC (Vol→4G) verified in-corpus; refined prefactor factor-2 established
**under p=3/2**; exact prefactor open on the link exponent. The row's Step-1/Step-2 are
Lean-supported (Bloch–Suslin unconditional; `WhiteheadVolumeCatalan` geometric input);
Step-3 remains the conjecture-class gap, now with in-corpus numerical evidence.
