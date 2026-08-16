---
doc_id: arxiv-1301.4504v4
doc_title: "Prepared for submission to JHEP DEDICATED TO JOHN PRESKILL ON THE OCCASION OF HIS 60 TH BIRTHDAY Quantum Computation vs. Firewalls Daniel Harlowa Patrick Haydenb aPrinceton Center "
section_id: sec-020-6-the-structure-of-the-hilbert-space
section_title: "The Structure of the Hilbert Space"
section_number: 6
pages: 56-59
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "DEDICATED TO JOHN PRESKILL ON THE OCCASION OF HIS 60 TH BIRTHDAY Quantum Computation vs. Firewalls Daniel Harlowa Patrick Haydenb aPrinceton Center for Theoretical Science, Princeton University, Princ"
---
The main argument of this paper is now complete, and although the paper is already
long, we can’t resist making a few comments about the possible implications of our
results for how to think about the interior of a black hole. In the introduction we brieﬂy
discussed two alternatives, “strong complementarity” and “standard complementarity”,
for how to think about Alice the infalling observer’s quantum mechanics. It is very
important to decide which, if either, of these frameworks is the correct way to think
about black hole interiors. In this section we assess the status of each in turn in light
of our computational arguments. This section has substantial overlap with a paper by
Susskind [91] appearing simultaneously with this one, and which explains some of these
ideas in more detail.
The least restrictive idea for how to think about Alice is to imagine that she has
her own quantum mechanics, possibly approximate since she encounters a singularity
later, which is a priori independent of the quantum mechanics of an observer at inﬁnity
like Charlie. This type of theory has been argued for by Banks and Fischler for a while,
who attempt to realize it precisely as quantum mechanics with no approximations for
anybody, in a formalism called “holographic spacetime” [10, 11]. The basic idea will be
discussed using as illustration ﬁgure 1 above. In this framework it seems necessary for
consistency [14, 15] for Alice and Charlie to agree about the results of measurements in
the green region of the ﬁgure. It is fairly clear in this setup that if Alice indeed cannot
decode the radiation before jumping in, we are free to change her state in a way that
produces no observable contradiction with the fact that Charlie, who is able to decode,
will later conclude that that RB was entangled with B. Charlie, not having access to
the degrees of freedom behind the horizon, will not be able to check thatB is entangled
with A. Moreover a previous objection to strong complementarity [1], that it required
some sort of discontinuity in the experiences of a sequence of observers who jump in
at diﬀerent times, is not relevant since the only thing that determines whether or not
RB can be decoded is whether or not the observer ever falls in. So Alice’s inability to
decode apparently to allows strong complementarity to be consistent without ﬁrewalls.
Although strong complementarity is in some sense straightforward, it is rather
unsatisfying. Each observer having her own description of the universe, approximate
or not according to taste, and with no clear precise relationship between them, seems
to us like a rather inelegant fundamental framework. In particular it is to be contrasted
with AdS/CFT [45, 46, 92], where there is a single Hilbert space and set of operators
which is conventionally understood to describe all of the physics in AdS space within
a single sharp framework. It would be reassuring if strong complementarity could be
set into such a framework, in which its ambiguities would be understood as arising
– 55 –
Figure 6 . The construction of bulk operators by Kabat, Lifschytz, and Lowe for an AdS
black hole. Here the yellow region is a lightcone ending on the operator and extending out
to the boundary, and the operator is constructed by integrating a CFT operator over the
boundary of the yellow region against a kernel that depends on the position of the operator.
Note that as the operator approaches the horizon the operator becomes sensitive to the entire
history on the boundary and thus to the details of the quantum state.
from measurements that are not precisely well-deﬁned. Without such an embedding,
it would seem like strong complementarity would amount to a step backwards; even in
AdS space the CFT would not be a complete description of the physics of an infalling
observer.47 As we discussed above this embedding has been called A = RB in the
context of ﬁrewalls; in the remainder of this section we sketch a basic proposal for how
it could work more precisely.
We imagine that there is a single Hilbert space H, which we will think of as the
CFT Hilbert space in an AdS setup to be concrete. To understand Charlie’s physics on
some spatial slice like the black one in ﬁgure 1, we need to compute expectation values
of some set of operators Cn, which approximately commute. 48 Indeed there is a fairly
well-known construction [51] for constructing these operators in some cases, which we
illustrate in ﬁgure 6.
Our proposal for the interior is then that there is another set of operators, which
we will callAn’s, which are also mutually commuting with each other and whose expec-
tation values in the same (Heisenberg picture) state used by Charlie describe Alice’s
experience on the red slice in ﬁgure 1. Some of the An’s are interpreted by Alice as
47The point of view of that follows here is in some respects close to that of [16], although we disagree
with their assertion that their construction by itself addresses the argument of AMPS.
48It is interesting to ask whether approximately commute means up to powers in N−1 or up to
exponentially small terms in N. We are agnostic about this here.
– 56 –
being outside the horizon, and she can also try to construct them using the method
of [51]. Consistency then requires that these An’s are equal to the appropriate Cn’s to
prevent disagreement between Alice and Charlie about events in the green region of
ﬁgure 1. Others of the An’s are interpreted by Alice as being behind the horizon and,
as shown in the ﬁgure the construction of [51], breaks down in that case. These An’s
naively do not seem to have low energy interpretations for Charlie. From the AMPS
argument however we know that to have a smooth horizon it must be that there are
some operators just outside the horizon, which act on what we’ve been calling B, mea-
surements of which need to be close to perfectly correlated measurements of some of
the behind-the-horizon An’s. Before the Page time, none of Charlie’s Cn’s are expected
to have this correlation with the B operators, and as recently argued by Susskind,
Verlinde, and Verlinde [18, 52] Charlie can then interpret the An’s as just being some
complicated mess acting on the remaining black hole. After the Page time, however,
Charlie expects the operators acting on B to be perfectly correlated with nonlocal Cn’s
acting on what we’ve called RB in the radiation. So it must be that from Charlie’s
point of view the appropriate An’s now act on the complicated subfactor of the ra-
diation which puriﬁes B. Hence the name A = RB. This clearly is rather nonlocal,
but as shown in the ﬁgure the breakdown of the construction of [51] suggests that the
construction of operators behind the horizon does indeed depend on sensitive details
of the state.
This idea is very confusing to interpret however if Alice is able to decode the
Hawking radiation, because she then has two low energy observables which she wants
to identify with the same quantum mechanical operator on the same Hilbert space.
This is sometimes called cloning, although it isn’t really because the theory is quantum
mechanical and thus doesn’t clone, but it seems like a rather serious problem for the
physical interpretation of quantum mechanics. By doing low-energy manipulations of
the Hawking radiation Alice would be able to construct a situation where looking at
some localized piece of the Hawking radiation far from the black hole is indistinguishable
from looking behind the horizon. At a minimum this type of observable bizarreness
would allow acausal communication, and in any event it doesn’t seem particularly less
crazy than the idea that there is a ﬁrewall. In the context of the discussion of this
paper however, if Alice in principle cannot decode RB then there does not seem to be
any such problem with interpreting An as being behind the horizon from Alice’s point
of view and out in the radiation from Charlie’s point of view. This is something like
strong complementarity, but now realized in a single quantum theory.
– 57 –
Acknowledgements
We have beneﬁted enormously from discussions with many people about ﬁrewalls. In
particular Juan Maldacena was of invaluable help in discussing many aspects of this
work from its inception to its completion. We are also grateful Igor Klebanov for techni-
cal assistance with the brane setup and Joe Polchinski for suggesting using strings and
in general being a good sport. We additionally thank Scott Aaronson, Nima Arkani-
Hamed, Tom Banks, Alex Belin, Adam Brown, Raphael Bousso, Borun Chowdhury,
Xi Dong, Liam Fitzpatrick, Ben Freivogel, Daniel Gottesman, Tom Hartman, Simeon
Hellerman, Jared Kaplan, Don Marolf, Alex Maloney, Jonathan Maltz, Jonathan Op-
penheim, Don Page, Kyriakos Papadodimas, Greg Prisament, Suvrat Raju, Grant
Salton, Steve Shenker, Eva Silverstein, Douglas Stanford, Leonard Susskind, Brian
Swingle, Erik Verlinde, Herman Verlinde, John Watrous, Edward Witten and all of
the participants of the Stanford Firewall Alert meeting for providing a stimulating and
chaotic environment for discussing the ideas in this paper and many others as well.
Finally we both especially thank John Preskill, to whom we dedicate this paper on
his 60th birthday. DH spent several months at the beginning of this project studying
John’s excellent lecture notes, without which he would have been able to contribute lit-
tle. DH is supported by the Princeton Center for Theoretical Science. PH is supported
by the Canada Research Chairs program, the Perimeter Institute, CIFAR, NSERC and
ONR through grant N000140811249. The Perimeter Institute is supported by Industry
Canada and Ontario’s Ministry of Economic Development & Innovation.
