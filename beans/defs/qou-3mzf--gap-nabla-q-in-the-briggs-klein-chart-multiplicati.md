---
# qou-3mzf
title: 'GAP: nabla_q in the Briggs-Klein chart: multiplicative integral over E_i equals int ln_q(1+t)/t dt'
status: todo
type: task
priority: normal
created_at: 2026-11-21T19:47:08Z
updated_at: 2026-11-21T20:20:36Z
---

Open input of conj:topological-mass-dilogarithm (folio/quantum-observable-universe/mass-endomorphism/topological-mass-dilogarithm.md; Lean QOU/LiftingDescent/tm_dilogarithm_evaluation.lean, class TmDivisorChartInputs.chart_eval).

Goal: write the categorical q-connection nabla_q = q^-1 nabla + (1 - q^-1)(iota_xi nabla) Theta_A (def in quantum-observable-universes/categorical-q-connection, Lean CategoricalQConnection.nabla_q) explicitly in the Briggs-Klein chart at each exceptional divisor E_i, and show its Yekutieli multiplicative integral norm over E_i equals int_0^{z_i} ln_q(1+t)/t dt = -Li2^q(-z_i) (symmetric [n]_q).

State (2026-11-21, PR #8932):
- The integral is -Li2^q(-z), NOT the Faddeev product Phi_q (def:quantum-dilogarithm-disambiguation; 40-digit check at proton q0: z=0.3 integral 0.280164, Phi_q 19.125). So qou-zbcj's partBHolonomy (partial product of Phi_q) is the wrong function for this step.
- Corpus has: discrete Yekutieli layer (QOU/MathlibExt/YekutieliIntegration.lean, sorry-free), continuum Stokes only as class NonAbelianStokes (QOU/Mathlib/NonAbelianStokes.lean), abstract nabla_q (only theorem: nabla_q = nabla at q=1). No explicit connection on E_i; the tower proof (mass-theory/mass-endomorphism-tower-proof.md) assumes the integrand ln_q(1+t)/t.
- Checked open PRs #8804, #8143, #8171, #8201, #8774, #8904: none has a connection on E_i.

Next honest step: choose coordinates on E_i ~ P^1 in the Briggs-Klein chart, compute nabla_q's connection 1-form there, and check whether its radial transport has the ln_q series (coefficients 1/[n]_q). If it does not, record the negative and the conjecture's integrand needs a different source.


## 2026-11-21 check (thread N2 Lean foundations): cannot be run from the corpus, scope (a)

- The conjecture's integrand is (nabla_A q, L wedge F+), the mass-identity pair, not nabla_q. nabla_q (categorical-q-connection) is abstract; its only theorem is the q=1 case. No component form of either connection on E_i exists in the corpus (main, checked 2026-11-21).
- The corpus's other evaluation of the same MI over the exceptional divisor is prop:mi-sw-abelianisation: |MI| = |a_D^(n)| = |contour integral of lambda_SW^(n)|, via lem:mi-sw-abelianisation-cartan (A^0 = X dz = lambda_SW). Its Lean is a self-assuming projection (status note qou-slpd/qou-kyst). So the two conjectures together would imply |a_D| = -Li2^q(-z_i); nothing derives that.
- The only ln_q(1+r) in the Brings chart setting is def:quaternionic-spectral-resolvents, where it is put in by definition with r = -ln|q| (not the chart radius r = |w_1|^2).
- Choosing a radial 1-form ln_q(1+t)/t dt so the transport matches would be selection against the target. Not done.
- What would unblock it: an explicit Higgs eigenvalue X(z) on S_c (the spectral curve restricted to the divisor), then compute the period and compare with -Li2^q(-z_i).
Bean stays open (open conjecture).


## 2026-11-21 spectral-curve search (thread N2 Lean foundations)
- The spectral curve exists in the corpus: the colour cubic X^3+(z+1)X^2+(z^2+z+1)X+(z^3+z^2+z+1)=0 (prop:color-elliptic, rem:color-bundles), with lambda_SW = X dz (lem:mi-sw-abelianisation-cartan) and 6 branch points (squarefree discriminant).
- Under the classical-jet rule the periods on the exceptional divisor vanish for every n >= 1 (prop:sw-classical-jet-exactness; prop:sw-period-residue-sum: every residue is zero). So prop:mi-sw-abelianisation (MI = |a_D|) with classical jets gives MI = 0, while -Li2^q(-z_i) > 0 for z_i > 0. The two statements are compatible only through a non-classical (q-difference) prolongation, i.e. the open keystone conj:qdifference-kernel-prolongation-symbol.
- Observation (exact, termwise): with the symmetric q-difference operator D_q t^n = [n]_q t^(n-1), D_q ln_q(1+t) = 1/(1+t). So -Li2^q(-z) = int_0^z (1/t) * (D_q-primitive of ds/(1+s))(t) dt: one Jackson primitive and one classical primitive of a form with a simple pole of residue 1 at s = -1. That is the shape a q-difference prolongation would need. Nothing yet identifies ds/(1+s) with X dz on the colour cubic near a branch point; this is an observation, not a derivation.
- z_i is defined only in the older proof (z_i = |V_i(q)|, algebraic volume); the Lean keeps z opaque.
- Possible next step: local expansion of X dz at a branch point (X - X_c ~ c sqrt(z - z_c)) and test whether any q-difference prolongation of it has the D_q ln_q(1+t) shape. Research, not started.
