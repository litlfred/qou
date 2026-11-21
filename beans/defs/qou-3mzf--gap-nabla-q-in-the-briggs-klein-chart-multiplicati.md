---
# qou-3mzf
title: 'GAP: nabla_q in the Briggs-Klein chart: multiplicative integral over E_i equals int ln_q(1+t)/t dt'
status: todo
type: task
priority: normal
created_at: 2026-11-21T19:47:08Z
updated_at: 2026-11-21T23:09:22Z
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


2026-11-21 (N2 thread), branch-point / residue check of lambda = X dz on the colour cubic F = X^3+(z+1)X^2+(z^2+z+1)X+(z^3+z^2+z+1) (sympy, exact):
- disc_X F = -(16z^6+24z^5+35z^4+50z^3+35z^2+24z+16), six simple branch points (z ~ -0.975+-0.223i, 0.106+-0.937i, 0.119+-1.054i). No branching over infinity (three sheets X ~ -z, +iz, -iz), so Riemann-Hurwitz gives genus 1, matching prop:color-elliptic.
- At a branch point (z - z_b = s^2) X dz = (X_b + ...)·2s ds is holomorphic: residue 0.
- z = -1 is NOT special: F(X,-1) = X(X^2+1), three distinct finite roots, so X dz has no pole there on any sheet. The pole that D_q ln_q(1+t) = 1/(1+t) needs (residue 1 at t = -1) is absent in the z coordinate.
- The only poles are over z = infinity, with residues 0, +5i/16, -5i/16 (sheets X ~ -z, -iz, +iz; sum 0). Purely imaginary, not 1. Rescaling by 16/(5i) to get residue 1 would be a chosen normalisation, i.e. a fit, and is not done.
- Weight: a primitive of X dz gives elliptic periods plus logs (weight <= 1). -Li_2^q(-z) is an iterated integral (Jackson primitive of the classical primitive of ds/(1+s)), weight 2. One prolongation step of X dz cannot supply both the missing pole at -1 and the second integration unless the q-prolongation itself raises weight, which conj:qdifference-kernel-prolongation-symbol does not specify.
Scope (a): this construction, with the classical form X dz on the colour cubic, does not give the D_q ln_q(1+t) shape. Not a structural exclusion; the prolongation is still undefined. Bean stays open.


2026-11-21 (N2 thread), second form with a pole over z = -1:
- F(0,z) = (z+1)(z^2+1), so X has a simple zero on one sheet over z = -1: X = -2(z+1) + 5(z+1)^3 + ... (sympy). Hence dlog X has residue exactly 1 there, with no normalisation chosen: the curve supplies the ds/(1+s) pole intrinsically. The trace of dlog X over the three sheets is dlog((z+1)(z^2+1)), so the same form also has poles over z = +-i.
- Weight-2 test (classical, not q): I(z) = int_0^z log(-X(t))/t dt on the real sheet (X(0) = -1, X(-1) = 0). It is NOT -Li2(-z): z=0.5: 0.244628 vs 0.448414; z=1: 0.493480 vs 0.822467; z=2: 0.982559 vs 1.436746 (mpmath, 40 dps).
- Striking: I(1) = pi^2/20 to 50 digits (-Li2(-1) = pi^2/12; ratio 3/5). Not explained. F(X,z)(1-z)(X-1)(X-z) = (1-z)X^5 - (1-z^5)X + z(1-z^4), a quintic, so a fifth-root-of-unity structure is plausible but unproved.
- PSLQ at z = 2, 1/2, 1/4 (60 dps, coeffs <= 500) on {I, pi^2, log^2 z, log z log(1+z), Li2(-z), Li2(-z^5), log z log X(z), Li2(-X), Li2(-X^5), log^2 X} found no relation. Absence of evidence in that basis only.
Scope (a): the curve provides the right pole (residue 1 over z=-1) but the classical iterated integral built from it is a different function from -Li2(-z). Bean stays open.


2026-11-21 (N2 thread), explaining I(1) = pi^2/20:
- Structure found: the colour cubic is F(X,t) = (s(X) - s(t))/(X - t) with s(u) = u + u^2 + u^3 + u^4 (sympy, exact). So the curve is [5]_X = [5]_t, i.e. (X^5-1)/(X-1) = (t^5-1)/(t-1), minus the diagonal, and it is symmetric under X <-> t. The real branch through (0,-1) and (-1,0) is swapped with itself, with fixed point at s'(t) = 0, t ~ -0.606.
- pi^2/20 is still NOT explained. PSLQ at z = 2 and 1/2 (60 dps, coeffs <= 1000) on a non-redundant 11-term basis including Li2 of fifth powers of z and X(z) found no relation.
- q-version test, answered by continuity: any q-deformation of I(z) that tends to I(z) as q -> 1 cannot equal -Li2^q(-z), because -Li2^q(-z) tends to -Li2(-z) and I(z) != -Li2(-z) (e.g. z = 1: pi^2/20 vs pi^2/12). So this route can match only through a deformation that is discontinuous at q = 1, or a different inner form. Scope (a).

2026-11-21: pi^2/20 is the n=5 case of a family. On the curve [n]_X = [n]_t (n odd), the real branch X(t) on t in [0,1] gives I_n(1) = int_0^1 log(-X)/t dt = pi^2/(4n): measured n=3 (1/12, exact: I=-Li2(-1)), 5 (1/20, 40 digits), 7 (1/28), 9 (1/36), 11 (1/44), mpmath quad 20-30 digits + identify. Even n: no negative real branch. For n=5 the two complex branches give Re = 3pi^2/80 each; all three sum to pi^2/8 = int log([4]_t) dlog t. Symbol reduction: t[4]_t = X[4]_X gives X^t = -X^[4]_t mod Steinberg; the quotient by X<->t is rational, v=Xt=(u+1)(u^2+1)/(2u+1), u=X+t. So the 5 in pi^2/20 comes from n, not from a fifth-root dilog value. Open: prove I_n(1)=pi^2/(4n); not proved, numeric only.

2026-11-21 proof attempt for I_n(1)=pi^2/(4n), not closed. Useful reductions: (a) on the real branch X=-y, the curve is (1+y^n)/(1+y) = (1-t^n)/(1-t), with the factor y+t (the X=t component) split off; (b) in K2 mod Steinberg, X^t == [n-1]_X ^ [n-1]_t, from X[n-1]_X = t[n-1]_t = S. A numeric check of the Rogers-dilog boundary split did NOT reproduce pi^2/(4n) (n=3 gave -1/4 pi^2 vs +1/12), so my sign or branch handling of L at negative arguments is wrong; do not reuse those numbers. Still numeric only.
