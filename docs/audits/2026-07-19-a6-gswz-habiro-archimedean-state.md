# A6 — GSWZ Habiro-ring-of-a-number-field 5₂ element: archimedean-evaluation state of play

**Date:** 2026-07-19
**Bean:** `qou-j6i3` (A6, open-problem backlog)
**Branch / PR:** `claude/agent-pr-4034-n5-gl1in2` / [#4087](https://github.com/litlfred/qou/pull/4087)
**Scope:** auditOnly; no `c_k` wired; no fit; comparison to observed only.

## What A6 asks, and why the literal form is ill-posed

A6 seeks the **archimedean evaluation at the substrate q₀** of the 5₂ element of
the GSWZ *Habiro ring of a number field* (Garoufalidis–Scholze–Wheeler–Zagier,
[2412.04241](https://arxiv.org/abs/2412.04241)) — the bar-odd carrier for the
c₃ odd-fibre question.

**Structural obstruction (scope-(b), cited invariant).** The Habiro ring has
**no archimedean evaluation off roots of unity**: a generic Habiro element
converges nowhere for |q| ≠ 1 (Habiro; GSWZ). The GSWZ 5₂ element is a
Frobenius + Bloch-group *algebraic* object. So there is **no direct archimedean
value to compute** at q₀ — the literal A6 target does not exist as stated.
Fabricating one (an "evaluation" of a divergent element) would be numerology.

The **well-posed reframing** — the only two routes to a real-q₀ number — is:

1. **Borel–Laplace median resummation** of the q → 1 asymptotic series
   (Costin–Garoufalidis resurgence, proved for torus-knot families,
   [2304.07001](https://arxiv.org/abs/2304.07001)); or
2. **Holomorphic-block / descendant q-series lifts**, which converge for
   |q| ≠ 1 (and q₀ ≈ 1.1097 has |q₀| ≠ 1).

## What the corpus has already derived (do not re-run)

The bar-odd 5₂ block/Stokes territory is **heavily worked** — a ~15-probe
`qbeta_(g3_)5two_*` suite. Corpus-grep summary (each finding scope-(a) unless
noted), so a future agent does not re-derive it:

| probe (witness) | established |
|---|---|
| `qbeta-5two-stokes-barodd-index` | Both Stokes automorphisms S⁺, S⁻ derived at q₀ from published integer q-series; 6 exact gates incl. S⁺ᵀ·S⁻ = 1. Odd datum O = ½(S⁺−S⁻) nonzero, calibration-free — **but anchor-smooth (not the swing; SRigidityPrune binds), and the rotated index is bar-EVEN despite chirality** |
| `qbeta-g3-5two-exact-blocks` | Exact deformed Z₅₂ from the proven Theorem-22 three-block factorization; assembly ratios derived anchor-free (Laurent pole cancellation); three O(1)-comparable saddle terms with distinct phases |
| `qbeta-g3-5two-saddle-exact-predictions` | 5₂ saddle data from the GGM §6.1 potential; cleared cubic (Lean-proved algebraic layer, disc −23); |Im V(σ₁)| = Vol(5₂) to 1e-10; **a nonzero intrinsic pole phase predicted** (the odd-channel carrier the 4₁ null excluded) |
| `qbeta-g3-5two-stokes-sandwich` | The (95a/b) sandwiches fully derived; reproduce the (96/97) q→0 factorizations exactly; every entry an integer q-series to O(q¹⁸), det = 1 |
| `qbeta-g3-5two-block-saddle-dictionary` | **Honest negative:** at the tested τ-window the block terms are **not clean exponentials** (drift 5–12%/step); exponent-level sector identification is drift-limited — "the remaining path to a derived-precision φ_odd is the ANALYTIC M-dictionary, not deeper numerics" |
| `qbeta-5two-habiro-tail-barodd-action` | The bar-odd Habiro-tail action **DRIFTS** (→ ~Vol(5₂)/π, not a clean π²/5-style dilog); chirality (the Cₙ asymmetry) changes the resummation class — genuinely resurgent |
| `qbeta-5two-habiro-archimedean-action-setup` | The naive twist-Gaussian 5₂ ansatz is **falsified** vs Vol(5₂); the exact action needs the verified Masbaum cyclotomic coefficients |

## The convergent finding (what A6 actually stands at)

Assembling the above, the honest A6 state is:

1. **The literal target is ill-posed** (no archimedean evaluation off roots of
   unity). A6 must be read as the resummation/block route, route 1 or 2 above.
2. **The direct odd Stokes/block datum is *not* the c_k swing.** The derived
   odd datum O = ½(S⁺−S⁻) is nonzero and calibration-free but **anchor-smooth**
   (SRigidityPrune binds), and the rotated index is bar-even. This is the same
   pattern the c₃-SETTLED analysis found (the swing is a fibre object with
   structure beyond a real constant, evaluated per-anchor — see AGENTS.md
   §"Im(q) at fibre vs observable level"): the fibre datum exists and is exact,
   but does not hand over a single real archimedean swing value.
3. **The resummed bar-odd channel is genuinely resurgent**, heading to a
   geometric (~Vol(5₂)/π) rather than a clean dilog constant — so there is **no
   closed-form φ_odd to read off**; φ_odd (≈ −0.0041, preliminary) is
   drift-limited at the numerical window.
4. **The real remaining gap is symbolic, not numerical:** derived-precision
   φ_odd requires the **analytic M-dictionary** — the u = 0 H-tower equations
   (89/90), the (94–95) Stokes sandwiches, and wall-crossing to deformed x —
   assembled exactly, not probed harder. This is Lean/symbolic work.

## Disposition

A6 **remains open** — this audit does not close it and claims no new result. It
reframes the ill-posed literal target, corpus-greps the ~15 prior probes so
they are not re-derived, and localizes the genuine remaining gap to the analytic
M-dictionary (symbolic). The next productive step is **not** another numerical
probe at the substrate but the exact assembly of eqs (89/90)+(94/95)+wall-
crossing — best queued for a session with a working Lean/symbolic toolchain
(the algebraic layer is already partly Lean-proved: the cleared cubic, disc −23).

No fit; no c_k wired; no tier change; no over-claim of "refuted" or "closed".
