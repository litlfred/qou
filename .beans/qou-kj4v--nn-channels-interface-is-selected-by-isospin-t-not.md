---
# qou-kj4v
title: 'NN channels: interface is selected by isospin T, not by nucleon content -- crossing-multiplicity route is REFUTED, not merely unfitted'
status: todo
type: task
created_at: 2026-08-09T02:34:49Z
updated_at: 2026-08-09T02:34:49Z
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
