---
# qou-u1b5
title: 'EPIC: formalize vdV Lemma 4 (Fresnel/erfc non-cancellation) — discharge VdVWhiteheadLemma4'
status: todo
type: epic
created_at: 2026-08-11T00:36:10Z
updated_at: 2026-08-11T00:36:10Z
---

EPIC RE-SCOPE 2026-08-19 -- remaining bricks go from BUILD to ASSEMBLE.

The epic's TARGET is still genuinely open: VdVWhiteheadLemma4 has no instance
anywhere in the corpus, and main's 18-file Kashaev* lane is 4_1 (kashaevProd is
defined in FigureEightVolume.lean), not the Whitehead link.  So this epic is
NOT redundant.

But its MACHINERY is already on main, generically, in QOU/MathlibExt/: six
Gaussian* files, CompositeEulerMaclaurin, CorrectedTrapezoid, TrapezoidRule.
qou-shrp learned this the expensive way -- it rebuilt a weaker first-order
Euler-Maclaurin rule nine days after the composite one landed, and the lane had
ALREADY applied it to the same function (logSinc = phi - log 2).

STANDING RULE for every remaining brick, before writing a line:
  grep -rln "<topic>" content/quantum-observable-universe/lean/QOU/MathlibExt/ \
                      content/quantum-observable-universe/lean/QOU/Knot/
"I checked what landed since my fork point" is NOT the corpus-grep checklist --
it cannot see a file that has been on main for nine days.
Audit: docs/audits/2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md

CROSS-REFERENCE 2026-08-19 -- A SECOND WHITEHEAD-LINK VC PROGRAM EXISTS, and
this epic is its natural partner rather than a duplicate.

  QOU/Knot/WhiteheadVolumeConjecture.lean   (beans qou-t2sc / qou-dw20 / qou-1gkf)
  QOU/Knot/WhiteheadSaddleClausen.lean      (825 lines, SORRY-FREE)

They take van der Veen's Lemma-1 POSITIVE-sum route and have the MAGNITUDE:
whitehead_vc_innerSum_half -- the inner sum sum_k S_{n,k} at the slice
n = floor(N/2) has scaled log -> 4G, sorry-free.

This epic has the PHASES: ||J_N(W)|| <= majorant,
tendsto_log_whiteheadLinkMajorant_vol -> 4G, and the residue isolated as
VdVWhiteheadLemma4 -- which still has NO INSTANCE anywhere in the corpus.

THE GAP BETWEEN THE TWO ENDS IS EXACTLY LEMMA 4: non-cancellation of the phased
outer sum sum_n (2n+1) chi_{N,n}^{-1} (sum_k S_{n,k}).  Discharging it joins the
two halves into the VC for J_N(W) proper.  So this epic is OPEN and WORTH DOING;
coordinate with qou-t2sc before extending either side.

CAUTION for whoever picks this up: their theorem NAMED whitehead_volume_conjecture
is not the VC for J_N(W).  It assumes hk : kashaev N = whiteheadInnerSum N ((N-1)/2),
so it is about the inner sum at one slice.  Their docstring is honest about this
("placeholder link", bean qou-1gkf tracks the fix); the name alone is not.
Audit: docs/audits/2026-08-19-volume-conjecture-work-overlap-sweep.md

PROGRESS 2026-08-19 -- THE OPEN PROBLEM IS NARROWED (sorry-free, no proof claimed).

QOU/Knot/WhiteheadLowerRate.lean.  The upper half of the VC is ALREADY CLOSED
unconditionally on main -- norm_whiteheadLinkKashaev_le (triangle) against
tendsto_log_whiteheadLinkMajorant_vol (sorry-free) -- so everything still open
lives on the lower side only.  VdVWhiteheadLemma4 as stated (a two-sided
polynomial comparison majorant <= N^p ||J_N||) is therefore MORE than the
conjecture needs.

  class WhiteheadLinkLowerRate :
    forall eps > 0, eventually  4G - eps <= (2 pi/N) log ||J_N||

  whiteheadLink_volume_of_lowerRate   -- the VC from that class alone
  lowerRate_of_lemma4                 -- Lemma 4 => the class, so NOTHING IS LOST
  eventually_one_lt_norm              -- the class forces ||J_N|| > 1, so
                                         Real.log's junk value at 0 never bites
  vol_borromean_half_pos              -- via Cl_2_pi_div_two_pos

All sorry-free; axioms [propext, Classical.choice, Quot.sound].

NO INSTANCE EXISTS for either class.  This does not prove Lemma 4 and does not
close the epic; it relocates the open problem to the weakest form that suffices,
which is also the form the sibling programme (qou-t2sc, WhiteheadSaddleClausen)
is closest to -- it already has the inner sum at the saddle slice attaining 4G,
and what remains there is non-cancellation of the outer phased n-sum.

NEXT: the outer-sum non-cancellation.  The phase is QUADRATIC in n
(WhiteheadPhaseAlgebra: chi_{N,n} e^{N pi i/8} = exp(n'^2 pi i/(2N)) exp(n pi i/(2N)),
n' = n - N/2), so this is a Gauss-sum / stationary-phase statement over a ~sqrt(N)
window -- and the generic infra is already on main (GaussianWindowSum,
GaussianTailBound, GaussianSumBound, GaussianTiltedSum, GaussianThetaSum,
GaussianShearIntegral).  ASSEMBLE, do not build: grep MathlibExt/ first.
Ledger: docs/coordination/whitehead-link-volume-conjecture-join.md

