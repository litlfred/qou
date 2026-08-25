---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-019-533-time-scales
section_title: "Time Scales"
section_number: 5.3.3
pages: 50-56
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
In this section we work out the time scales for sending signals down the throat from the
Minkowski region to the vicinity of the black hole horizon at r0 in (5.20), as well as the
time to evaporate down to the transition temperature just discussed in the previous
section. Since we will ultimately compare these time scales to the computation and
recurrence times, both of which are exponential in the entropy of the black hole, we
will be focused on extracting only the pieces of them which are exponential in entropy.
Speciﬁcally we will write S0 to mean the entropy of the black hole just after the Page
time, so that it is also roughly the size of the radiation and one half of the entropy of
the original black hole. If we had started the computer any later it would just have
made the task more diﬃcult, and we want to give Alice a fair shot.
We will see shortly that for the decay to be slow enough for Alice to have a chance
at computing, we will need the temperature to be exponentially small in the entropy,
perhaps with some coeﬃcient in front of S0 in the exponent. From equation (5.25) this
means we will need r0 to be exponentially small. From equation (5.24) we see that to
41As in the spherical case, in the microcanonical ensemble the energy at which the black hole is
actually unstable is somewhat lower than this. This decrease depends only on the parameters of the
AdS region of the geometry however, and is insensitive to the total length of the throat. Since we
will need the total length of the throat to exponential in the entropy in the following section, which
will lead to an exponentially long decay time, the additional time to get from T∼L−1 to the actual
instability will be negligible compared to the time to get down to T∼L−1 in the ﬁrst place.
– 49 –
keep the entropy ﬁxed in the same limit we will need L to be exponentially large such
thatLr0 is ﬁxed. Looking at (5.27) we see that the energy above extremality will then
be exponentially small througout the decay process. Having ﬁxed S0 we can also derive
an interesting bound on the AdS radius R in Planck units: we know that we must have
T >L−1 to avoid starting the computation below the phase transition discussed in the
previous section, so we must have
(TL )3 =
(r0L
R
)3
=S0
(R
𝓁p
)−8
> 1. (5.35)
Thus the AdS radius in Planck units is bounded by a polynomial in S0 and we can
neglect it in most equations.
To understand how hard it is to send some particular quanta down the throat, we
need to compute its absorption probability Pabs. This probability will be a function
of the frequency ω of the quanta of interest, and in the limit ωR≪ 1 it can often
be computed analytically [87]. For massless scalars in the extremal black three brane
(5.17) this problem was studied by Klebanov in [88]. 42 A simple generalization of his
result shows that for quanta with frequency ω, angular quantum number 𝓁 on the S5,
and momentum k in the planar direction, the absorption probability is
Pabs∼
(√
ω2−k2R
)8+4𝓁
. (5.36)
In sending signals down the throat, we need to use low enough energy to avoid our
signals backreacting signiﬁcantly on the throat. Certainly a necessary condition is that
we need ω < E, and looking at (5.28) this means we need ω ∼ T up to a power
of the entropy, which as usual we ignore. This means that we must use quanta of
exponentially low energy to send any messages; the absorption probability (5.36) will
thus be exponentially small. It is still possible to send a message, but we must try
many times. Since it takes an energy ω−1 just to produce a message of energy ω, to
have any chance of success sending the message we need a time of order
tmsg∼ 1
ωPabs
. (5.37)
Clearly we have the best chance of sending a message using scalars if we set k =𝓁 = 0.
Other types of communication will have diﬀerent absorption probabilities. For example,
we show in appendix A that the absorption probability for sending messages down
a string threading the throat by moving the string along the S5 is proportional to
42Computing these absorption factors in the extremal background is an excellent approximation for
our purposes since r0≪R and the potential is very close to extremal.
– 50 –
(ωR)2. Apparently this is a better method of communication than the massless scalar,
although we will see it is still not good enough to be of use to Alice. 43 In general we
will parametrize low-energy absorption probabilities as
Pabs = (ωR)b, (5.38)
so neglecting all factors polynomial in S0 we can estimate
tmsg∼ 1
Tb+1. (5.39)
The units here are provided either by powers of 𝓁p orR, it doesn’t much matter. To be
concrete we can evaluate the temperature at the same time that we deﬁned S0, which
was just after the Page time.
Absorption probabilities are also important in understanding how long it takes for
the black hole to evaporate. As Hawking showed in his original paper [89] the energy
ﬂux out of a black hole is
dE
dt =−
∑
n
∫ dω
2π
ωPabs(ω,n )
eβω− 1 , (5.40)
where the sum on n is over diﬀerent modes. It is often the case that only a particular
mode contributes signiﬁcantly, for example for Schwarzschild black holes it is only the
𝓁 = 0 mode. The low energy absorption cross section for Schwarzschild is proportional
to (2GMω )2, from which one can use (5.40) to motivate the usual “Stefan-Boltzmann”
assumption for the decay rate. In that case the low energy approximation breaks down
before the peak of the integrand and numerical analysis is necessary to compute the
prefactor correctly [62], but for us the temperature is very low compared to R−1 so
using the low energy approximation for Pabs throughout is justiﬁed. The intuition of
(5.40) is quite simple; the thermal factor is just the expected occupation number of
the near horizon modes, and by a basic fact about one-dimensional scattering theory
the probability of absorption in from the outside is the same as the probability of
transmission out from the inside.
For the absorption probability (5.36) the decay is dominated by 𝓁 = 0 modes, but
it is necessary to include modes of low but ﬁnite k. Roughly k is quantized in units of
1/L, and since we are interested in the region where TL≫ 1 we will have ω≫ L−1.
We can then convert the sum over discrete modes into an integral over k and write
dE
dt =−
∫ ωdω
2π L3
∫
|k|<ω
d3k
(2π)3
(ω2−k2)4R8
eβω− 1 ∼−L3R8
∫ dω
2π
ω12
eβω− 1∼−L3R8T 13.
(5.41)
43We thank Joe Polchinski for suggesting a stringy telephone.
– 51 –
More generally we can write
dE
dt ∼−
∫ dω
2π
(Lω)a(Rω)bω
eβω− 1 ∼−LaRbTa+b+2, (5.42)
where the parameter b is the same as in (5.38) and the parameter a accounts the
phenomenon just encountered for the scalar. For the string we discuss in appendix A
we havea = 0, b = 2.
To ﬁnd the evaporation time we need to integrate (5.42) to ﬁnd the energy as a
function of time. As the decay proceeds L cannot change because it is ﬁxed by the
boundary conditions at r→∞ , so it will be r0 that gradually decreases. We integrate
from initial energy E = S0T down to ﬁnal energy E =
(
R
𝓁p
)8
L−1. The details of the
integral depend on whether a +b− 2 is positive, negative, or zero, but the ﬁnal power
of T does not. Indeed we ﬁnd
tevap∼ 1
Tb+1, (5.43)
where again we can make up the dimensions with either R or 𝓁p without aﬀecting the
exponent in the entropy. By comparing (5.43) to (5.39) we see that the evaporation
time is always the same order inT as is the time to send any signal at all!44 Which one
is bigger depends on the prefactors we omitted, but there are deﬁnitely cases where
tmsg <t evap so this fact by itself, although certainly troubling, is not enough to kill the
experiment.
In section 3.2 we argued that Alice’s quantum computation takes a time of order
e2S0.45 For now we will be a little more general and write this as
tcomp∼eαS0. (5.44)
The recurrence time is basicallyeS0, but we need to include a red-shift factor to account
for the extremely low energy of the states involved in the recurrences. Thus
trec∼T−1eS0. (5.45)
With these estimates we are ﬁnally in a position to assess the viability of Alice’s
experiment. For the computation to ﬁnish before the black hole evaporates we need
tcomp <t evap, which implies
T <e− α
b+1S0. (5.46)
44It is the same b that appears in both because whichever b is smallest will control the decay rate
and also give the highest probability of success for sending messages.
45The reader should not be confused by us writing e2S0 here and 2 2n there. Previously n was the
entropy in base-2 logarithm while S0 here is the entropy in the natural logarithm. Also our general
result there was tcomp∼ 2n+k+m, but since we are here letting Alice start just after the Page time we
havek +m≈n.
– 52 –
This conﬁrms our earlier claim that the temperature needs to be exponentially small
in the entropy. To be able to send a message down the throat in less than a recurrence
time we need tmsg <t rec, which implies
T >e− 1
bS0. (5.47)
The condition that tcomp <t rec gives
T <e(1−α)S0. (5.48)
It is straightforward to see that all three of these can be satisﬁed only if
b< 1
α− 1. (5.49)
In the text we saw that if UR is completely general then α = 2, in which case the
experiment can be done only if b <1. Neither the string nor the free scalar ﬁeld are
close to this, and actually there is a simple argument that no scalar ﬁeld of any kind
can satisfy this inequality. The coeﬃcient b in the absorption factor is related to the
conformal dimension of the operator that the scalar couples to in the CFT dual as
b = 2∆ [90], so the unitarity bound ∆ > 1 in four dimensions precludes b < 2. A
similar argument can perhaps be constructed for the defect operators that couple to
the ends of general strings but we have not tried to do so.
It is interesting that were the computer able to decrease α it would make it easier
to satisfy these inequalities. In fact we don’t see any particular reason why improved
algorithms shouldn’t be able to use special features of the black hole dynamics to
decreaseα by some order one factor. Ifα could be decreased below 3/2, the string might
become an eﬀective method for communicating down the throat. We stress however
that this is not suﬃcient for doing the AMPS experiment, it is only necessary. For
one thing even if the “true” α could be decreased by algorithms, our discussion below
equation (3.2) suggests that, because of coarse-graining, α should be increased by some
order one factor. More signiﬁcantly, being able to send one piece of classical information
is not enough to do the strongest version of the AMPS experiment. That requires us
to send a particular quantum state which puriﬁes B. Preserving the coherence of this
state would presumably require some sort of apparatus (also made out of ﬂuctuations
on the string) which would also have to make it through the barrier, and even without
the apparatus we probably want k to be at least a little bit bigger than one to be able
to build up any kind of statistics. Getting all of these things to make it through the
barrier at once probably requires us to raisetmsg by some order one power, which would
help compensate for an α that has been decreased by clever algorithms. Even this is
– 53 –
not enough however; the puriﬁcation of B is more likely to be partially reﬂected than
to get all the way through, which means that it will be partially reﬂected many times
before most of it gets through. In fact getting slightly more than half of it through is
enough since somebody living down the throat can do error correction to restore the
other half, but each time that more than half of it is reﬂected the person outside will
need to do error correction before trying to send it again. This will usually succeed,
but there is a smallS0-independent probability it will fail. Since we need the correction
procedure to work every time in order to continue sending the correct state, this means
that eventually it will fail. For these reasons we are quite conﬁdent that the “strong”
AMPS experiment where Alice carries the puriﬁcation of the black hole in with her
can’t be done in this setup.
There is a weaker version of the AMPS experiment where the state of RB is mea-
sured out in the Minkowski region at the end of the quantum computation and what
is sent down the throat to Alice is just a classical record of the result of that measure-
ment. This would be suﬃcient, for example, to implement a Bell inequality test using
the state entangled between B and RB. Because classical information can be cloned,
sending the record of the measurement outcome to Alice is easier than sending RB it-
self; she doesn’t have to worry about error correction and she can send multiple copies
at once. Sending exponentially many copies of the information down the throat at
once is dangerous from a back-reaction point of view however. For example, to do this
using strings would require an exponential number of strings, all parallel and located
at diﬀerent values of x, which would become extremely dense down the throat; the
distances between the strings would become exponentially sub-Planckian. For massless
scalars the total number of modes we can use without backreaction is, at the level of
exponential factors, of order (LT )3. Since L∼T−1, using all of these modes at once is
of no help in trying to beat the exponential in tmsg.
Given the possibility of α < 2 we are not decisively able to rule out this ‘weak”
AMPS experiment, but at a minimum we are comfortable interpreting this section as
casting serious doubt on the feasibility of using an AdS throat to facilitate an AMPS
experiment.46
46Steve Shenker has suggested that another way to buy a little more “room” for dealing with α< 2
is to notice that the classical recurrence time decreases under coarse-graining. For example if one
considers a system of N particles on a line with L lattice points, S =N logL and eS is the time one
has to wait to ﬁnd all N particles on a single lattice point. To ﬁnd all of them on some particular
set of
√
L lattice points however we only need to wait a time of order eS/2. Also we have so far
essentially treated Alice as a “probe observer”, but Borun Chowdhury has pointed out that Alice and
her equipment will have their own recurrence time which is probably signiﬁcantly shorter than that
of the black hole.
– 54 –
