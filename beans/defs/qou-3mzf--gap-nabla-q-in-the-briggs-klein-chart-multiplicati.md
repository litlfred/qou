---
# qou-3mzf
title: 'GAP: nabla_q in the Briggs-Klein chart: multiplicative integral over E_i equals int ln_q(1+t)/t dt'
status: todo
type: task
created_at: 2026-11-21T19:47:08Z
updated_at: 2026-11-21T19:47:08Z
---

Open input of conj:topological-mass-dilogarithm (folio/quantum-observable-universe/mass-endomorphism/topological-mass-dilogarithm.md; Lean QOU/LiftingDescent/tm_dilogarithm_evaluation.lean, class TmDivisorChartInputs.chart_eval).

Goal: write the categorical q-connection nabla_q = q^-1 nabla + (1 - q^-1)(iota_xi nabla) Theta_A (def in quantum-observable-universes/categorical-q-connection, Lean CategoricalQConnection.nabla_q) explicitly in the Briggs-Klein chart at each exceptional divisor E_i, and show its Yekutieli multiplicative integral norm over E_i equals int_0^{z_i} ln_q(1+t)/t dt = -Li2^q(-z_i) (symmetric [n]_q).

State (2026-11-21, PR #8932):
- The integral is -Li2^q(-z), NOT the Faddeev product Phi_q (def:quantum-dilogarithm-disambiguation; 40-digit check at proton q0: z=0.3 integral 0.280164, Phi_q 19.125). So qou-zbcj's partBHolonomy (partial product of Phi_q) is the wrong function for this step.
- Corpus has: discrete Yekutieli layer (QOU/MathlibExt/YekutieliIntegration.lean, sorry-free), continuum Stokes only as class NonAbelianStokes (QOU/Mathlib/NonAbelianStokes.lean), abstract nabla_q (only theorem: nabla_q = nabla at q=1). No explicit connection on E_i; the tower proof (mass-theory/mass-endomorphism-tower-proof.md) assumes the integrand ln_q(1+t)/t.
- Checked open PRs #8804, #8143, #8171, #8201, #8774, #8904: none has a connection on E_i.

Next honest step: choose coordinates on E_i ~ P^1 in the Briggs-Klein chart, compute nabla_q's connection 1-form there, and check whether its radial transport has the ln_q series (coefficients 1/[n]_q). If it does not, record the negative and the conjecture's integrand needs a different source.
