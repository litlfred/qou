---
doc_id: arxiv-1301.4504v4
doc_title: "Prepared for submission to JHEP DEDICATED TO JOHN PRESKILL ON THE OCCASION OF HIS 60 TH BIRTHDAY Quantum Computation vs. Firewalls Daniel Harlowa Patrick Haydenb aPrinceton Center "
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-8
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "DEDICATED TO JOHN PRESKILL ON THE OCCASION OF HIS 60 TH BIRTHDAY Quantum Computation vs. Firewalls Daniel Harlowa Patrick Haydenb aPrinceton Center for Theoretical Science, Princeton University, Princ"
---
2 The Firewall Argument 7
2.1 A Quantum Black Hole from the Outside 8
2.2 A Quantum Black Hole from the Inside 10
2.3 A Way Out? 12
3 The AMPS Experiment as a Quantum Computation 13
3.1 Quantum Computing is Hard 15
3.2 Implementing a General Unitary Transformation with Quantum Gates 18
3.3 Why is Alice’s Computation Slower than the Black Hole Dynamics? 22
3.4 Two Counting Arguments 25
4 Quantum Coding and Error Correction 26
4.1 Review of Error Correcting Codes 26
4.2 Computational Complexity, Stabilizer Codes, and NP-Hardness 31
4.3 Alice’s Task as Error Correction 34
4.4 Error Correction and Zero-Knowledge Proofs 36
5 More General Black Holes 40
5.1 Schwarzschild in a Box 40
5.2 Reissner-Nordstrom 42
5.3 Near Extremal AdS Throat 43
5.3.1 The Brane Setup 45
5.3.2 Hawking-Page Transition for Toroidal Black Holes 47
5.3.3 Time Scales 49
6 The Structure of the Hilbert Space 55
A The Absorption Probability for a Nambu-Goto String 58
– 1 –
1 Introduction
The recently proposed ﬁrewall phenomenon [1] has dramatically emphasized the extent
to which black holes remain interesting and mysterious in quantum gravity. Using
“reasonable” assumptions about the structure of the quantum theory of black holes,
the authors of [1], henceforth referred to as AMPS, have argued that unitarity of black
hole evaporation, along with some limited form of locality, is inconsistent with a smooth
horizon for an observer falling into an “old” black hole. 1 There has been signiﬁcant
discussion of this claim in the literature, but in our view none of the followup work so
far has decisively challenged the original argument.
We will review the AMPS argument in section 2 below, but a key point in moti-
vating their setup is a claim that an infalling observer is able to extract information
from the Hawking radiation of a black hole prior to falling in. 2 The model black hole
of Hayden and Preskill [3], also partially reviewed below, suggests that this should be
possible provided that the observer is able to perform a sophisticated nonlocal mea-
surement on the Hawking radiation that has come out so far. In this paper we will
argue using methods from the theory of quantum computation that this measurement
can almost certainly not be done fast enough and thus that the AMPS experiment is
not operationally realizable even in principle.
As a simple example, consider a Schwarzschild black hole in 3 + 1 dimensions. Its
entropy is proportional toM 2 in Planck units, and it evaporates in a time proportional
toM 3. A would-be AMPS experimentalist thus has to extract information fromn∼M 2
bits of Hawking radiation in a timeT∼n3/2 to be able to jump in before the black hole
evaporates. From a computer science point of view this is very special: the decoding
needs to be accomplished in a time that scales as a low-order polynomial in n. In
order to get at the information our experimentalist would need to apply a unitary
transformation to the Hawking radiation which “unscrambles” the desired information
by putting it into an easily accessible subfactor of the Hilbert space.3 As we will review
below in section 3.2, applying a generic unitary transformation to an n-bit Hilbert
space requires time that is exponential in n. Only very special unitary transformations
1We recently found out that a similar argument was made by Braunstein, later joined by Pirandola
and ˙Zyczkowski, back in 2009 [2], who called the ﬁrewall an “energetic curtain”. Some details of
their model do not seem consistent with standard assumptions about black hole physics, however, and
restoring those assumptions seems to rule out their curtain-avoiding resolution.
2As emphasized by AMPS, the observer does not actually need to do the experiment to get into
trouble. The possibility of the experiment being done is enough to argue against a smooth horizon.
We will be more precise below about what is meant by “extract information”.
3In line with standard parlance we will sometimes refer to this operation as “decoding”; we will
see the precise connection to what is called decoding in quantum information theory in section 4.
– 2 –
can be implemented faster, and in this paper we will argue that the decoding operation
relevant to AMPS is unlikely to be special in this way. In fact we conjecture, but
cannot rigorously prove, that the decoding time for Hawking radiation will in general
be exponential in the entropy of the remaining black hole. 4
In light of our discussion, a ﬁrewall enthusiast might nonetheless argue that even
though the decoding cannot be done the information is still “there”. It has been clear
for some time however that operational constraints are important in understanding the
structure of the Hilbert space used in describing black hole evaporation, and we view
our results in this context. More concretely the real issue at stake is for which types of
situations we should trust eﬀective ﬁeld theory (EFT). Traditionally EFT was viewed
as holding away from local regions with high energy density or spacetime curvature. If
this were the only way in which EFT could break down however, then we would seem
to be led inexorably to information loss [4]. If we wish to maintain belief in unitarity, as
AdS/CFT strongly suggests we should, then there must be a more broad set of criteria
for when EFT is not be valid. It is not trivial however to ﬁnd such criteria which do
not ﬂagrantly violate the extraordinary level to which EFT has been experimentally
tested. Careful analysis of thought experiments near black holes in the mid 1990’s [5–7]
led to an additional criterion involving causality:
• Two spacelike-separated low-energy observables which cannot both be causally
accessed by some single observer do not need to be realized even approximately
as distinct and commuting operators on the same Hilbert space.
This criterion was claimed to preclude the apparent contradiction between unitarity
and local EFT in Hawking’s argument. It is clear that it does not lead to obvious
testable violations of EFT, and it was also claimed to avoid more subtle problems like
quantum cloning and unacceptably large baryon number violation. The key point for
us however is that this criterion, which is a profound statement about the structure of
the Hilbert space of quantum gravity, was motivated by operational constraints. It says
that whether or not quantum information is “there” is indeed related to its practical
accessibility.5
The deep insight of AMPS is that even with this stronger causal restriction on
when we may use eﬀective ﬁeld theory there is still a paradox that seems to require
4It may seem that beating a small power with an exponential is overkill, but we will show that for
more general types of black holes the exponential really is necessary to prevent the AMPS experiment
from being done. In those cases it will be recurrence phenomena rather than evaporation which doom
the experiment.
5The authors of [7] also attempted to give a less operational reason for the break down of EFT
involving large integrated boosts, although aspects of this claim were later questioned [8]. It remains
to be seen whether a similar argument might exist for the breakdown we advocate here.
– 3 –
more modiﬁcation of the rules, either by having ﬁrewalls or by further violating eﬀective
ﬁeld theory. We interpret our results as supporting a new criterion for the validity of
eﬀective ﬁeld theory:
• Two spacelike-separated low-energy observables which are not both computation-
ally accessible to some single observer do not need to be realized even approxi-
mately as distinct and commuting operators on the same Hilbert space.
By computationally inaccessible we mean that one or both of them is so quantum-
mechanically nonlocal that measuring it would require more time and/or memory than
the observer fundamentally has available. This criterion clearly implies the previous
one, but it is stronger: as we will see, it can apply even if both observables are within
the past lightcone of some observer. In Minkowski space this criterion (and also the
causality criterion) is irrelevant, but in spacetimes with singularities there are observers
whose available time is fundamentally limited. This is also true in spacetimes where
the fundamental Hilbert space is eﬀectively ﬁnite, for example the de Sitter static
patch. In that case recurrence phenomena limit how much time is available for low-
energy observation rather than a singularity. 6 Our proposal violates what AMPS call
postulate II, and we will see below that it seems to remove the contradiction that led
AMPS to argue for ﬁrewalls.
Lest the reader worry we are throwing the baby out with the bathwater, we here
point out that a traditional asymptotic observer at inﬁnity, whom we will refer to as
Charlie, has all the time and memory needed to measure the Hawking radiation as
carefully as he likes. Our arguments are thus no threat to the unitarity of black hole
evaporation as a precise quantum mechanical process; there will be new restrictions on
the validity of eﬀective ﬁeld theory only for an observer we call Alice who falls into the
black hole before it evaporates. 7
Both the weaker “causality” criterion and the stronger “computational” criterion
are negative statements; they tell us what the Hilbert space is not. It is of course
very important to understand what the structure of the Hilbert space is, and there
are two interesting proposals. The ﬁrst, sometimes called “strong complementarity”,
takes the point of view that each observer has her own quantum mechanical theory,
6In [9] these limits were used to conjecture that “precise” descriptions of spacetime require observers
who have access to an inﬁnite amount of information. This conjecture is distinct from the idea proposed
here, but they are clearly related.
7There could be “cosmological” restrictions on what Charlie is able to do, but it seems that these
should be decoupled from restrictions “intrinsic” to the black hole. From our discussion of Udyn in
section 3.3 it seems that in a completely pristine environment Charlie should even be able to test
unitarity in polynomial time; we won’t address whether or not Charlie would be able to do this in a
“noisy” environment.
– 4 –
which is precise for some special observers and approximate in general.8 There are then
consistency conditions between the diﬀerent theories to ensure that observers who can
communicate with each other agree on the results of low-energy experiments visible to
them both. Within this framework it was argued [14, 15] that if the AMPS experiment
cannot be done, the ﬁrewall argument breaks down. 9 The basic point is that physical
restrictions on what measurements can be done weaken the overlap conditions, allowing
for more “disagreement” between Alice and Charlie’s quantum mechanical descriptions
of what is going on.
The other proposal for the Hilbert space structure, which might be called “standard
complementarity”, claims that there is a single Hilbert space in which states undergo
exact unitary evolution. The quantum physics of various observers are embedded into
this single Hilbert space in such a way that each observer has for each time slice a set of
distinct operators that approximately commute. The semiclassical interpretation of an
operator according to one observer can be quite diﬀerent from that of another observer
however, and in particular things which are inside the horizon according to one observer
might be outside from the point of view of another. This viewpoint is essentially that
of [5–7], and in the context of ﬁrewalls it is sometimes called “ A = RB” for reasons
we will soon see. It has been suggested by several people 10 as a way out of ﬁrewalls,
but it has so far run into various paradoxes involving apparent cloning and acausality
[14, 18]. We postpone further discussion of these two options until after we present the
ﬁrewall argument, but it seems that in either framework our computational breakdown
of EFT may be suﬃcient to avoid the paradoxes without any need for ﬁrewalls. 11
It is also interesting to think about whether more general types of black holes have
ﬁrewalls. For example Reissner-Nordstrom black holes semiclassically seem to take
an inﬁnite amount of time to evaporate, apparently allowing ample time for quantum
computation prior to jumping in. We will explain however that the well-known “frag-
8This general point of view has been advocated by Banks and Fischler, who have tried to realize
it more concretely in a formalism called “holographic spacetime” [10, 11]. In their setup quantum
mechanics is precise for all observers, even those who encounter singularities or recurrences. They
have recently argued that their formalism evades the ﬁrewall argument [12], but their claim requires
a decoupling in Charlie’s description of the black hole dynamics between the near-horizon ﬁeld theory
modes and the horizon degrees of freedom. Such a decopuling seems rather implausible, especially in
the context of the mining operations of [1, 13].
9In [15] one of us tried to argue, for a reason having nothing to do with computation, that the
experiment cannot be done. That argument proved unconvincing, and we regard the computational
complexity arguments of this paper to be much stronger.
10Including but probably not limited to [14, 16, 17].
11Another interesting proposal, raised again recently in the ﬁrewall discussion by John Preskill and
Alexei Kitaev, is the Maldacena/Horowitz “black hole ﬁnal state” scenario [19]. Our results could
have interesting implications for that idea, but we won’t explore them here.
– 5 –
mentation” phenomenon [20, 21] destroys the black hole well before the computation
can be completed. Big AdS black holes do not evaporate at all, so the AMPS argument
does not directly apply to them, but arguments have been put forward suggesting that
they nonetheless have ﬁrewalls. In particular Don Marolf has argued that one could
simply mine the black hole until half of its entropy is gone, after which the mining
equipment would play the role of the Hawking radiation in the original AMPS argu-
ment. If the decoding time is indeed exponential in the entropy of the black hole,
as we argue it is, then it becomes comparable to the Poincar´ e recurrence time of the
AdS-Schwarzschild space [22]; we argue that no observer or computer can isolate itself
from a big black hole for so long in AdS space.
The strictest test of our criticism of the AMPS experiment uses a setup suggested to
us by Juan Maldacena, in which a large AdS black hole is placed very far down a throat
whose geometry is asymptotically Minkowski. By putting the decoding apparatus out
in the Minkowski region, it seems that one could use the redshift to arbitrarily speed
up the decoding time compared to the evaporation time. We will explain in section 5
however that the decoupling which makes the decay slow in this situation also makes
it very diﬃcult to send the results of the computation back down the throat, and for
a particular example we show that, for a wide variety of probes, the time required
to successfully send a message down the throat is longer than the recurrence time of
the black hole down the throat. So indeed it seems there is a fairly robust conspiracy
preventing the AMPS experiment from being done. These results are consistent with
a point of view expressed by Aaronson [23] that the laws of physics should not permit
computational machines that radically alter the basic structure of complexity theory.
At most, they should force some marginal changes around the edges, as in the case of
Shor’s factoring algorithm.
It is interesting to note that if our computational complexity argument is correct,
it supersedes many of the classic black hole thought experiments [3, 5–7]. In particular
the argument of [3] that the scrambling of information by a black hole in a time no
faster than M logM is necessary to prevent observable cloning would be no longer be
needed.
An objection to our argument that we have sometimes encountered is the following:
say that we have a quantum computer which is simulating some quantum gravity theory
likeN = 4 Super Yang-Mills theory. Somebody who is working the computer could
decide to make a black hole in the simulation, let it evaporate for a while, pause the
simulation, use the computer to decode the radiation while the simulation is paused,
and then start the simulation again. In this way divine intervention from the outside
is able to circumvent our claim that the radiation cannot be decoded in time for an
infalling observer to see it. One can try to make this proposal sound somewhat less
– 6 –
artiﬁcial by setting it in AdS, where the claim would be that, since the spacetime is
not globally hyperbolic, these manipulations can be done by coupling the bulk to an
arbitrary external system at the boundary and manipulating this coupling at will. From
our point of view however the main question at stake here is whether or not nonsingular
initial data on some Cauchy surface generate singularities (such as ﬁrewalls) beyond
those predicted by low energy physics. We are less concerned about the question of what
happens if some godlike entity, external to the system, disrupts it in some arbitrary
way. In particular if something subtle like standard complementarity is going on in the
structure of the Hilbert space, then outside manipulations which naively don’t aﬀect
the region behind the horizon might actually have rather drastic eﬀects on it. 12 We
would be more concerned by this argument if the coupling of AdS to the external
system were accomplished in a manner in which it were clear that low energy physics
might be expected to hold throughout the joint system, and indeed one can interpret
the throat geometry we discuss in section 5 as a realization of this. In that setup
physical restrictions seem to prevent any observer from overcoming the computational
complexity of decoding.
This introduction has telegraphically sketched our main points. In the remainder
of the paper we will make the case again in much more depth. Because of our expected
audience we will try to keep our discussions of quantum computation and coding self-
contained, but the same deﬁnitely cannot be said for our discussions of black holes and
gravity. Other work on ﬁrewalls includes [25–35].
