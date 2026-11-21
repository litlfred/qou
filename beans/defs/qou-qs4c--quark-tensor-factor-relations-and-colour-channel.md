---
# qou-qs4c
title: 'Relations among colour x spin x flavour x chirality x momentum; settle the colour channel'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
created_at: 2026-11-15T08:00:00Z
updated_at: 2026-11-21T08:00:00Z
parent: qou-qs0e
---

Physics: the factors are NOT independent. Known relations to map onto the substrate:
spin-statistics + colour antisymmetry (baryon spin-flavour-space symmetric, SU(6) 56, mu_p/mu_n = -3/2);
Lorentz (chirality = helicity when massless, mass mixes L/R); weak isospin acts on L only;
Q = T3 + Y with chirality-dependent Y; anomaly cancellation forces N_c = 3 from the quark charges; CKM; confinement.
Schur-Weyl: (3)<->10, (2,1)<->8 (x2), (1^3)<->1 for N = 3; convention D = Schur-Weyl at N = 2.
Settle: is the colour channel (1^3)? Only mu-bar_123 in the sign rep is established (`docs/audits/2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md:86-89`).
Scope (a)/(b) discipline on any exclusion.

## 2026-11-15 — partial (PR #7823); stays open (colour factor's existence is open)
`docs/audits/2026-11-15-quark-factor-relations-and-colour-channel.md` + `QOU/SchurWeyl/ColourChannelSpinStatistics.lean` (lean-direct exit 0, std axioms). Colour (1^3) forced given 4 S3 factors + Fermi + Delta++ (empirical); level 2 cannot host colour (wenzlWeight_eq_zero_iff). OPEN: does the substrate supply a separate colour factor (options A level-3 factor / B mu-bar / C none). Level-2 (2,1) = nucleon isospin channel, not a quark.

## 2026-11-15 — owner: "try quark = strand, explore downstream" (PR #7823)
`docs/audits/2026-11-15-quark-equals-strand-implications.md` + `QOU/SchurWeyl/QuarkStrandConsequences.lean` (lean-direct exit 0, std axioms). Proved: a factorised strand space (colour x spin x flavour) is not a Hecke rep at q>1 (crossing eigenvalues q^2,-1,q^-2 satisfy no quadratic) -> at most one factor is q-deformed; integer charge <-> triality (imported charges). Matches the constituent quark model at q=1; at q0 the corpus deforms isospin (conv D) while physics gauges colour. Nuclear ratio 33.7 = B_d / virtual-state energy: one-crossing ratio is (N+1)/(N-1) <= 3 in any SU(N) frame; owner decision (re-scope as ill-posed) framed in §4. Hypothesis, not a definition yet: quark = one strand's label.

## 2026-11-15 — owner D1 = C (no change for now), via coordinator. §6 options I/II/III stay framed, deferred.

## 2026-11-15 — owner asked "I vs II; does II throw away D; deep impact of II" (from PR #7845 branch, restored 2026-11-21)
`docs/audits/2026-11-15-option-ii-colour-deformation-impact.md`. Same algebra/words/characters; I and II are r=2 and r=3 of one proved Wenzl family; D = level-3 trace conditioned to two colours (Levi argument, not formalised, G1). II keeps every theorem but retires D as the observable; reverses R1 + D7. Measured (exact rationals): Q_beta base -43.16% (D) -> -61.43% (z3); mass-channel weight -18%; compute 119x at n=12; Borromean 1100x cost frame-independent (writhe 0) - corrects my earlier "re-run in SU(3) frame". D1 = C stands.
2026-11-21: the audit is cherry-picked onto `claude/port-unowned-leftovers-2026-11-21` (session https://claude.ai/code/session_01Qmmkt91GpCvJB15AZz7wMr). Caveat for readers: those Q_beta percentages predate the 2026-11-21 two-term-trace ruling (docs/coordination/owner-rulings.md); re-check before quoting.
