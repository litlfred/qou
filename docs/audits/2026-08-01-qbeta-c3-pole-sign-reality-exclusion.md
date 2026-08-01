# c₃ bar-odd S: the pole-sign candidate excluded + reality invariance (Lean)

**Date:** 2026-08-01 · **Axis:** Q_β c₃ (bar-odd `S`, the open `q₀ → m` link)
· **Branch:** `claude/reeb-flow-tetraplectic-q2460a` (PR #4457) · **Tier:**
scope-(a) family exclusion + scope-(b) class exclusion (invariant Lean-proved).
**No c_k wired; C14 anti-fit; registry untouched; `u(q₀)` stays OPEN.**

## What was tested (the one derived candidate the sign opens)

Prior pole-seed probes (`qbeta_c3_barodd_pole_seed_newton_probe.py`,
`qbeta_c3_phib_pole_seed_sensitivity_probe.py`) seeded Thurston's 4₁ gluing
Newton with the pole **magnitude** `q₀^{−(2k+1)}`. The actual pole of the
compact `Φ_q(x) = ∏(1+q^{2n+1}x)^{−1}` is

    x_k = −q₀^{−(2k+1)}     (phase π — derived, not fitted).

Probe [`qbeta_c3_pole_sign_complexification_probe.py`](../../computations/qbeta/qbeta_c3_pole_sign_complexification_probe.py)
(witness 4/4) tests the principal-branch complexification
`m² := x_k ⇒ u_k = iπ − (2k+1)·log q₀` against the diagonal-crossing gate
(`signflip_requires_diagonal_cross`).

## Findings

1. **Scope-(a) — fixed-k family excluded.** For every `k` (0..19) the sign of
   the corrected leading form `(√3/4)(Re²u − Im²u)` is identical at the muon
   and proton anchors (anchor-blind at the 1e-8 anchor separation). The sign
   boundary `(2k+1) = π/log q₀ ≈ 30.1090` is crossed by **no odd integer**
   between the two anchor values (checked, not assumed). No fixed-k member
   can reproduce `S(muon) > 0 > S(proton)`.
2. **Numerological trap flagged (C14).** Near `k = 15` the leading-form
   magnitude dips to `O(S)`. Choosing `k` per anchor to chase sign or
   magnitude would be a two-parameter fit and is **not** performed.
3. **Scope-(b) — the whole real-seed class excluded (proved invariant).**
   [`QOU/QBeta/NewtonRealityInvariance.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/NewtonRealityInvariance.lean)
   (sorry-free, lean-direct exit 0): the Newton step of conjugation-
   equivariant maps preserves the real axis (`conjEquivariant_newtonStep`,
   `iterate_real`); a convergent all-real sequence has a real limit
   (`limit_real`); hence a real seed — **either sign** — can never converge
   to the cusp shape `e^{iπ/3}` (`real_seed_limit_ne_of_im_ne`). The concrete
   real-coefficient polynomial instance (`conjEquivariant_realPolynomial`)
   ties this to the literal gluing Newton. Invariant cited per
   AGENTS.md §Before declaring "refuted": conjugation equivariance +
   closedness of ℝ. This upgrades the prior probes' computed golden-branch
   negatives to a class exclusion.

## Sharpened open link (honest boundary)

`u(q₀)` remains **open**, now sharpened to: the required phase is strictly
interior — `0 < |arg m²| < π` with the anchor asymmetry crossing the diagonal
`|Re u| = |Im u|`. Neither the real axis (either sign, scope-(b)) nor the
principal branch of the pole's own log (scope-(a)) reaches it. This composes
with: smooth `m(q₀)` excluded (NZ ratio test), F1–F3 excluded
(`UDeformFamilyPruning`), and the CS magnitude deficit at substrate scale
(pole-seed probe finding C).

## Cross-references

- Gate: [`2026-07-26-sdeformed-channel-signflip.md`](2026-07-26-sdeformed-channel-signflip.md)
- Prior pole-seed: [`2026-07-11-qbeta-c3-pole-cusp-phase-tractability.md`](2026-07-11-qbeta-c3-pole-cusp-phase-tractability.md)
- Reeb/CS backbone: [`../scope/2026-08-01-reeb-tetraplectic-cs-threeform-identification.md`](../scope/2026-08-01-reeb-tetraplectic-cs-threeform-identification.md)
- Gap bean: `qou-82w7`.
