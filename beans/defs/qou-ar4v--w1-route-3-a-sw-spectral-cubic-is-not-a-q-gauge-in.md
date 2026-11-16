---
# qou-ar4v
title: 'W1 route 3: a SW spectral cubic is not a q-gauge invariant, so Sigma cannot be a q-difference module''s spectral curve'
status: in-progress
pr: 8194
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T10:59:36Z
updated_at: 2026-10-04T15:14:20Z
parent: qou-frzo
---

## Result (2026-09-12, PR #7208)

**Route 3's required input is a difference field `(K, σ)`** — RSZ Astérisque 355
§2.1.1, read directly from `library/arxiv-0903.0853v3`, not paraphrased. A system
`σ_q X = A X` is read modulo gauge, and DVRSZ eq. (2.4.1)
(`library/equations-aux-q-differences`) makes that action **twisted, not
conjugation**: `B = (σ_q F)⁻¹ A F`.

**Finding, scope (b), invariant cited.** With `F = z^k·1` the law is `A ↦ q^{-k}A`,
and a scalar multiple moves the characteristic cubic (`X^{3−k}` coefficient picks up
`t^k`). Stability under `X ↦ tX` forces `a₀(1−t³) = a₁t(1−t²) = a₂t²(1−t) = 0`, so at
any non-root-of-unity scalar — any real `t > 1`, hence every `q₀^{-k}` — **every
non-leading coefficient vanishes**. The only gauge-stable monic cubic is `X³ = 0`.
General, not a fact about this Σ.

For the colour cubic the `z = 0` fibre decides it alone (`X³+X²+X+1`, all three
non-leading coefficients `1`) ⇒ `t = 1`. The **joint** move
`P(λX, μz) = ν·P(X,z) ⇒ λ = μ = ν = 1` is proved too — neither #6769 (base only) nor
the fibre statement reaches it. Read as descent to `E_q = ℂ*/q^ℤ`: the `z=0` root
ratios are 4th roots of unity, so `q·B = B` forces `q⁴ = 1`, and `q₀⁴ ≈ 1.518 ≠ 1`.

**Structural, not a coincidence.** `P` IS quasi-homogeneous — for the PAIRED action
`(X,z) ↦ (X/z, 1/z)`, which is why the palindromic involution lifts (#7185). The
gauge wants an X-motion with no compensating z-motion, and `a_k = 1+z+⋯+z^{3−k}` are
not monomials. Same q-freeness that forced the operator into the q-difference class
(2026-06-25 z2bn audit) is what leaves the gauge nothing to absorb — a pincer on one
property from two sides.

**Artifacts.** Lean `QOU/Mass/QGaugeSpectralRigidity.lean`, sorry-free,
shadow-verify exit 0, 11 declarations all `propext / Classical.choice / Quot.sound`.
Probe `computations/probes/w1_route3_qgauge_spectral_rigidity_probe.py`, 31/31,
exact sympy, three controls (conjugation certified invariant; the `a₀` relation goes
vacuous at a cube root of 1; `X³+z³` returns three scalars and a 1-parameter family).
Audit `docs/audits/2026-09-12-w1-route3-spectral-curve-not-a-q-gauge-invariant.md`.

**NOT closed, deliberately (rule 13a).** The bridge *"the sought `D_q` would have Σ
as its spectral curve"* is an **assumption**, carried as a hypothesis in the Lean and
the probe and never used as a fact. Route 3 itself stays open: a q-difference module
over `(ℂ(z), σ_q)` is fine, and Σ may still enter one as Newton-polygon/slope data,
the Birkhoff connection matrix, or the `E_q` bundle of RSZ §6.3. `D_q` is not
constructed; nothing is fitted or wired.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-12 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (PR #8194)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/W1SpectralRigidityAndEllipticInvolution.lean` (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 advisory` across all 7 static vacuity/borrowed-name audits) and wired into `QOU.lean`.
- [x] Verified exact rational witness in `computations/probes/w1-spectral-rigidity-and-elliptic-involution.witness.json` (`scriptHash: 5e848ba624fe`, `scriptCommitSha: 62bd8cb179998d43808552b8955ff0b3857febae`, `allPassed: true`, `0` raw `float64` fields).
- [ ] Awaiting Merge Manager merge of PR #8194 (`b0ca85df1a1275572e6a829fccdff9eb4eff2fe0`).
