---
# qou-jcmw
title: 'PROBE A1: compute HH^1(H_5(zeta_5)) at the Bring root of unity'
status: completed
type: task
priority: high
created_at: 2026-08-07T17:20:58Z
updated_at: 2026-08-08T18:55:00Z
---

Direct finite-dim Hochschild-1 computation at the ACTUAL Bring case (H_5, 5th root of unity), extending the verified n=3 mechanism check (hh1_hecke_outer_derivations.py: dim HH^1=1 at roots of unity, 0 generic). Uses the merged HochschildH1.lean Der/Inn infra + OuterDerivationResidue. Deliverable: dim HH^1(H_5(zeta_5)) and the outer-derivation structure. Tractable, decisive, formalizable. NECESSARY not sufficient for res!=0 (see bean B). Parent thread: PR #4687.


## DONE 2026-08-08 (PR #4788, branch claude/l2-gap-prunes-2026-08-08)

**dim HH^1(H_5(zeta_5)) = 1** — semisimple control at generic q gives 0. Built a
general-n engine (regular rep constructed programmatically); regresses exactly
against the merged hand-coded hh1_hecke_outer_derivations.py at n=3 (0/1/1).

**The outer class is TRACE-VISIBLE**: it acts with rank 1 on the 7-dimensional
cocenter HH_0, so it CAN move tr_M. Inner derivations act as zero on HH_0, so the
induced action is canonically attached to the class. This direction is EXACT
(rank_p <= rank_0, so a non-containment mod p persists to characteristic 0), and
it closes the degree-mismatch worry the 08-08 assessment raised.

**The bar-parity sub-test is VACUOUS — but this DUPLICATES bean `qou-qb8b`,
which landed on main first the same day** (docs/audits/2026-08-08-hh1-outer-
class-bar-parity-prune-does-not-exist.md). Cite that one; mine is independent
corroboration only, and its audit explicitly advised NOT running this leg.
Corpus-grep failure on my part: checked at session start, not re-checked before
claiming. The genuinely new parts are the H_5(zeta_5) dimension count + cocenter
rank (which qou-qb8b left as "remains worth doing") and the cost correction
(480 unknowns, not the 14,400 that audit estimated -- so H_5 is cheap). Over Q(zeta), bar is a sigma-semilinear
algebra automorphism of H_n(zeta) itself. With dim HH^1 = 1, [D^bar] = mu.[D]
forces mu.sigma(mu) = 1; Hilbert 90 gives mu = nu/sigma(nu); and since
sigma(a) = -a for a = zeta - zeta^{-1}, the generators nu.D and a.nu.D of the
SAME line are bar-even and bar-odd respectively. Parity is a property of a chosen
GENERATOR, not of the class -- it carries no information on a 1-dim HH^1 and
cannot prune anything. Free corollary: im(D_0), ker(D_0) automatically bar-stable.
Verified in exact Q(i) on H_3; hypotheses confirmed for zeta_5 in Q[x]/Phi_5.

Net: the lead was expected to die cheaply in one of three ways and died in none.
All three cheap dismissals are spent; it must now be worked or left on its merits.
Still true: nobody has shown the c_3 swing IS this class, and q_0 is not a root of
unity. Audits: 2026-08-08-hh1-h5-bring-root-cocenter-action.md,
2026-08-08-bar-parity-gate-is-vacuous-on-one-dim-hh1.md
