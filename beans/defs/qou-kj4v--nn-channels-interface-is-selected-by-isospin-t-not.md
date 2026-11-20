---
# qou-kj4v
title: 'NN channels: interface is selected by isospin T, not by nucleon content -- crossing-multiplicity route is REFUTED, not merely unfitted'
status: todo
pr: 8278
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T02:34:49Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---


Branch: claude/anchor-followups-2026-08-08.
Full write-up: docs/audits/2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md
Lean: QOU/QBeta/InterfaceScalar.lean sections IsospinOrdering + ChannelSelection.

## The ask, and why it cannot be answered as posed

Asked: derive why identical nucleons take TWO crossings (m_pp = m_nn = 2), not
a fit. That is exactly the m_* tuning bean qou-h7mh forbids, so it needed a
derivation. It gets a REFUTATION instead, which is stronger.

Nature has FOUR two-nucleon channels, not three:

    channel            S  T   B/MeV       state
    pn 3S1 deuteron    1  0   +2.224566   BOUND
    pn 1S0 virtual     0  1   -0.066      unbound
    pp 1S0             0  1   ~-0.1       unbound
    nn 1S0             0  1   ~-0.1       unbound

The two pn rows have the SAME nucleon content and OPPOSITE boundness. Any
m_pp/m_pn/m_nn assignment is a function of content, so it gives them the same
energy. No integer choice can work -- the defect is in what the multiplicities
are allowed to depend on, not in their values.

Lean: `content_keyed_interface_refuted`. Trivial proof, load-bearing step.

Also killed on the way: the naive braid-topology argument runs BACKWARDS
(identical => pi_1 = B_n so sigma is already a loop; distinguishable => P_n so
only sigma^2 closes -- predicts sigma^2 for pn, sigma for pp/nn, i.e. binds pp
and unbinds the deuteron).

## The variable that works costs nothing

T is already in the algebra. sigma^2 = h.sigma + 1 has eigenvalues q, -1/q; its
projectors P+ (T=1, symmetric) and P- (T=0, antisym) were ALREADY proved
complementary + orthogonal (proj_add_eq_one, proj_mul_eq_zero). Scalars:

    mu+ = (z+1/q)/(q+1/q) = 0.75270211325196540159
    mu- = (q-z)/(q+1/q)   = 0.24729788674803459841      mu+ + mu- = 1

MEASURED: these EQUAL the n=2 Wedderburn weights y_(2), y_(1,1) from
y_lambda_su_n(2, q0, 2) to 3.3e-52 (round-off at 50 dps). Selecting a channel is
choosing a Young diagram, and T fixes the diagram. Zero new parameters.

## DERIVED, every q, no fit

Convention D has z = q^3/(q^2+1), and

    2z - h = (q^4 + 1) / (q(q^2 + 1))        identity, residual 0.0 at 50 dps

positive for all q>0. Since mu+ - mu- = (2z-h)/(q+1/q):

    mu- < mu+  for every q>0   =>   B+ < B-
    => THE ISOSPIN SINGLET IS ALWAYS THE MORE BOUND CHANNEL.

That is the deuteron-vs-pp/nn ordering, forced, with no crossing count. First
structural result in this line to get the sign right without tuning.
Lean: two_z_sub_h_conventionD, h_lt_two_z_conventionD, mu_singlet_lt_mu_triplet,
singlet_binds_more, mu_sum_eq_one.

## Where it stops -- and it is NOT a missing crossing

    reading                 T=1       T=0     splitting
    -alpha*ln(mu)         +1.1892   +5.8485    4.6593
    nature                 ~-0.07   +2.2246    2.2906     (model 2.034x high)

Sign right, magnitude 2.034x too big, and BOTH model channels bind.

mu+ + mu- = 1 is why: projection only REMOVES trace weight, so mu_T < 1 and
B_T > 0 for both T. The projector decomposition can NEVER give an unbound
channel. Unbinding needs mu > 1, i.e. leaving the convex decomposition of 1
(stacked_crossing_gt_one: sigma^2 gives mu = h.z+1 = 1.12809).

DEEPER OBSTRUCTION. In S-wave Pauli LOCKS spin to isospin (space symmetric =>
spin and isospin symmetry opposite): S=1 <=> T=0, S=0 <=> T=1. A Pauli-consistent
interface carries a projector in EACH SU(2), and

    mu(3S1) = mu+^spin * mu-^iso = mu-^spin * mu+^iso = mu(1S0) = 0.186142

EXACTLY DEGENERATE, because multiplication commutes. A FLAVOUR-ONLY interface
cannot split 3S1 from 1S0 at all, whatever the functional. In the SM that split
is the TENSOR force (3S1-3D1 mixing), a spin-SPACE coupling; the Hecke interface
has one index (the strand) and no space index to carry it. Separately nature's
T=1 sits at -0.066 MeV from an unnaturally large scattering length
(a_s ~ -23.7 fm) -- a near-critical fixed point, i.e. fine-tuning, not symmetry.
Both halves of the residual are dynamical, not representational.

## NOT claimed

- does NOT fix the 2H magnitude (2.034x high).
- does NOT show B = -alpha*ln(mu) is right; the degeneracy result argues no
  flavour-only mu can be.
- Markov property is still an axiom+sorry (jones-markov-trace.lean).
- m_pp/m_pn/m_nn left at 1. Nothing here licenses changing them, and the
  refutation says nothing ever will.

## Next

The open lever is a SPACE index on the interface -- something carrying L, so
that 3S1-3D1 mixing has somewhere to live. Until then the NN sector is
sign-correct and magnitude-wrong by construction.

## 2026-08-09 — THE DEUTERON IS REACHABLE UNDER D. It was NOT under C.

Bean qou-c6gx's headline impossibility result was CONVENTION-C SPECIFIC and no
longer holds. It recorded:

    "Required mu = 0.587762445 => d = +0.088442110 = +0.42304594*h -- POSITIVE,
     outside the Hecke range d in [-h, 0]."

Recomputed under convention D with the writhe term wired (commit 0f608066):

    required mu = 0.5877150637      current mu = 0.5082297894
    required d  = mu_req - z_D = -0.02497297346
    admissible  d in [-h, 0] = [-0.2090603, 0]
    d_req / h   = -0.119453         ->  INSIDE RANGE

The required offset is now NEGATIVE and sits at 12 % of the way down the Hecke
interval. The floor theorem (`bond_energy_floor`, `mu_unreachable`) does not
apply to D -- z_D = 0.6127 > 1/2, so AM-GM never bites -- and the scope
correction already in InterfaceScalar.lean said so. This is the POSITIVE
statement that correction implied but did not make: **no impossibility remains
at the deuteron.**

WHY IT FLIPPED: the required mu barely moved (0.58776 -> 0.58772; it is just
exp(-B_AME/alpha) up to the writhe shift). What moved is the RANGE. Under C the
band [z-h, z] = [0.290, 0.499] sat entirely BELOW the target; under D it is
[0.404, 0.613] and CONTAINS it.

## What remains, stated precisely

Reachable is not derived. Writing d = -h*t, so t is the p-n colour weight:

    derived   t = 1/2 - delta/4 = 0.499656   (colour-weighted, delta = 0.0013757)
    required  t = 0.119453
    ratio                        4.183

So the deuteron needs a colour weight ~4.2x further from colour-blind than the
derived one. The interface CAN reach AME; the derived weight does not put it
there. That is a much better-posed gap than C's "no admissible element exists".

NOT CHASED: 0.499656/0.119453 = 4.183 and alpha = 4.18598 MeV agree to 0.07 %.
alpha is an ENERGY and t is DIMENSIONLESS -- units mismatch, numerology. Same
class as the ln(1-h) coincidence dismissed in qou-4waf. Recorded so nobody
re-finds it.

## Consequences for the beans that assumed impossibility

  * qou-c6gx: "The hard result: AME is below the model's floor" and "no crossing
    sign, no colour weight, no crossing multiplicity, and no stacking can reach
    the deuteron" are FALSE under D. The measurements stand; the conclusion was
    C-specific.
  * The A-scaling refutations in that bean (per-bond deficit changes sign,
    spread 7.105 MeV/bond) were also computed under C and should be re-run
    before being cited.

### Cross-link (2026-10-11)

the colour-weighted p-n factor `z − h(1/2 − δ/4)` is **bar-mixed** (`δ̄ = −q²δ`, defect `(q−1)⁵(q+1)³(q²+1)/(12q⁵)` ≈ 1.67e-5 at the anchor), so bar-invariance does not select it. Record: [`2026-10-11-atom-word-provenance.md`](../../docs/audits/2026-10-11-atom-word-provenance.md).

## Progress Update (PR #8278 — `status: in-progress`)

- [x] Formalized pure Lean 4.24.0 module(s) (`QOU/MassTheory/IsospinChannelReachabilityAndB3ChainSign.lean`, `QOU/MassTheory/PeeledMarkovDefectAndHigherInterleaving.lean`, `QOU/MassTheory/GradedLogPairCancellationAndH3TowerCollapse.lean`) with `0 sorry` and `0` findings across all 6 static vacuity audits.
- [x] Added 50-dps `mpmath` probe `computations/probes/isospin_b3chain_markov_defect_logjet_h3tower_probe.py` and 2-commit stamped witness `computations/probes/isospin-b3chain-markov-defect-logjet-h3tower-probe.witness.json` (`allPassed: true`, `0` raw `float64`).
- [x] Opened and signed [PR #8278](https://github.com/litlfred/qou/pull/8278) (`ready: b3288da132ea8d0d185d184a5e18432c89e4858e`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8278, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
