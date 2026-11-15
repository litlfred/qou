---
# qou-39bx
title: 'F1 deuteron overshoot: is alpha*L_pn = 2.833 vs B_AME = 2.225 a parameter-free prediction failure?'
status: completed
type: task
priority: normal
created_at: 2026-08-26T03:37:39Z
updated_at: 2026-08-26T04:12:39Z
---

## 2026-08-26 — FRONT 1 CLOSED (scope-(a)). Verdict: parameter-free prediction failure.

**Nothing in B_sym(2H) is free.** Free-parameter inventory: m_e (CAL-1),
q_0 (CAL-2 proxy pin), E_0's FORM (derived, observations/mass-formula-validation.md),
z_D (owner ruling R1, discrete), a = 1 (FORCED by convexity: (1-t)sigma + t sigma^-1
= sigma - h t so a = (1-t)+t = 1), t = 1/2 - delta/4 (derived, R3 +
prop:flavor-split-substrate), writhe (Lean-proved unique up to sign), one p-n bond
(A=2 has one pair). **Continuous free parameters: 0.** So the +27.34 % IS a
prediction failure of the two-body kernel, not a tuning gap.

**LEAN — QOU/MassTheory/DeuteronTwoBodyKernel.lean, 7 theorems, ALL SORRY-FREE.**
lean-direct exit 0 against the real import cone; #print axioms on all seven gives
[propext, Classical.choice, Quot.sound], no sorryAx.
  interfaceFactor_half            z_D - h/2 = (q^4+1)/(2q(q^2+1)) exactly; writhe is
                                  exactly 1 at t=1/2, so B = E_0 ln(2q(q^2+1)/(q^4+1))
  bondL_strictMono                L(q,t) strictly increasing in t -> endpoint bounds sharp
  deuteron_overbinds              for ANY t in [0.499, 1/2]: E_0 L > 1.25 * B_AME
  required_weight_far_from_...    any t giving binding <= 2.4 MeV has t <= 0.4
  no_flavour_split_rescue         the demanded departure from balance > 250x delta/4
Stated as an INEQUALITY on purpose -- "no free parameter" as a Lean congruence would
be a tautology (AGENTS.md No-trivial-trues).

**WHERE THE 27 % LIVES** (each ingredient moved ALONE to hit B_AME, vs what it is
allowed). L_pn is NOT a linking number: it is -ln f_pn, f_pn = the Markov-trace
suppression of the 2-nucleon sub-braid; span{1,sigma_2} is 2-dim (sigma^2 = h sigma
+ 1) and tr_M(W sigma_2) = z tr_M(W) gives f = a z + b directly.
  colour weight t   -0.23159 (to t* = 0.26807)  =  673x the derived flavour split
  energy scale E_0  -21.47 %                    =  1.68e6 x the 128 ppb pin spread
  Markov param z    +12.97 %  (convention C is FARTHER, not nearer)
  writhe term       carries -5.6e-4 of the miss -- cannot hold it
  q_0, pin broken   +2.28 %   vs 1.7e-11 allowed
NO ingredient can carry it.

**CAL-2 ANSWER: no alpha-respecting fix exists.** E_0 enters linearly, so a 21.5 %
miss needs a 21.5 % move; the entire proton-vs-muon pin spread is 128 ppb. Ratio
1.68e6. Any fix must live in L_pn, and inside L_pn the only continuous freedom is t,
ruled out at 673x. What survives: an ADDITIVE term, or replacing the scalar Markov
peel with something carrying the interface's non-abelian content ([sigma_2,sigma_3]
!= 0, traceless -- measured by deuteron_interface_handle_curvature_probe 2026-08-25;
worth 0.6 MeV? open, qou-jqof/qou-dp32).

**SCOPE (a), NOT (b).** B_AME(2H) IS inside the convention-D band [1.5598, 4.2887]
(reached at t = 0.26807), so no invariant excludes the target -- what is excluded is
reaching it at the derived weight. Additive terms untouched. Under the EXCISED
convention C the band was [2.907, 5.178] and 2.2246 sat below all of it; that older
impossibility claim does NOT survive R1 and must not be carried forward.

**TWO CORRECTIONS FOUND**
(a) docs/audits/2026-08-25-low-isotope-binding-error-staleness-vs-gap.md section 6:
    its band [2.051, 3.798] and "t = 0.119453 required" are PRE-WRITHE. Production
    has applied the writhe normalisation to the p-n bond since 2026-08-09, and
    varying t varies delta_e = 2t-1 with it. Writhe-consistent: [1.5598, 4.2887],
    root t = 0.26807. GAP-1's VERDICT is unaffected; only the numbers were wrong.
(b) **QOU.Hecke.ClosedFormInterfaceFactors is CONVENTION C** -- the only other Lean
    formalisation of f_pp/f_nn/f_pn, i.e. the module that LOOKS like the formal
    backing for the production deuteron number. `def markovZ (s : R) := s/(s^2+1)`
    with q = s^2, i.e. z = sqrt(q)/(q+1); its own docstring says "z = 1/(sqrt q +
    1/sqrt q)". A square-root-variable spelling NO C detector scans -- which is how
    it survived the 2026-08-10 drain that AGENTS.md records as clearing .lean to
    zero. Meanwhile QOU/MathlibExt/MarkovBondRule.lean:84 exports `markovZ` under
    convention D and warns C "must not be used as the base": two Lean modules, one
    name, opposite conventions. DeuteronTwoBodyKernel states zD afresh and does not
    import it. Do NOT reconcile by substituting s^2 = q -- not convention-preserving;
    the C module's algebraic theorems are correct FOR C and need RE-DERIVING.
    FOLLOW-UP, not fixed here.

**ARTIFACTS** (branch claude/isotope-mass-binding-dashboard-kdvhz6, PR #5812)
  content/quantum-observable-universe/lean/QOU/MassTheory/DeuteronTwoBodyKernel.lean
  computations/deuteron_two_body_kernel_overshoot_probe.py  (mpf 60 dps, no float64,
    0 free params, B_AME never inverted, 15/15 Lean bounds cross-checked)
  computations/deuteron-two-body-kernel-overshoot.witness.json
  docs/audits/2026-08-26-deuteron-two-body-kernel-parameter-free-failure.md
  scripts/precision-gates.sh --changed: all blocking gates GREEN.

**STILL OPEN** the MAGNITUDE of the missing term (0.608 MeV, and it must be NEGATIVE
at A=2 while positive at A>=3 -- so any candidate additive term must be SIGN-CHANGING
in A, which is the generalisation of this morning's Faddeev-Niemi argument); whether
the interface curvature is its carrier; re-deriving ClosedFormInterfaceFactors under D.
