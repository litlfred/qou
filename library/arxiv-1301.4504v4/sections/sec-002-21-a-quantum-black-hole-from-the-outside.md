---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-002-21-a-quantum-black-hole-from-the-outside
section_title: "A Quantum Black Hole from the Outside"
section_number: 2.1
pages: 9-11
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
We’ll ﬁrst discuss Charlie’s description, which is based on the following three postulates:
• According to Charlie, the formation and evaporation of the black hole is a unitary
process. Moreover, in addition to an asymptotic S-matrix, we can also think about
either continuous or discrete time evolution in which at any given time there is a
pure quantum state|Ψ⟩ in some Hilbert space Houtside.
• At any given time in this unitary evolution we can factorizeHoutside into subfactors
with simple semiclassical interpretations:
Houtside =HH⊗HB⊗HR. (2.1)
HereHR are the modes of the radiation ﬁeld outside of the the black hole, roughly
with Schwarzschild coordinate radius r >3GM. HB are the ﬁeld theory modes
in the near-horizon region, roughly with support over 2 GM +ϵ < r <3GM
where ϵ is some UV cutoﬀ. The geometry in this region is close to Rindler
space.HH are the remaining degrees of freedom in the black hole, which we can
heuristically think of as being at the stretched horizon at r = 2GM +ϵ. Clearly
the distinctions between these subfactors are somewhat arbitrary. In particular,
it will be convenient to restrict the modes in HB to have Schwarzschild energy
less than the black hole temperature T = 1
4πGM . Those with higher energy are
not really conﬁned to the near-horizon region and we will include them as part
ofHR. The time evolution of |Ψ⟩ does not respect this factorization and cannot
be computed using low energy ﬁeld theory, but for our purposes it is enough to
consider the state at a given time.
• If|H| and|B| are the dimensionalities of HH andHB respectively, then log|H|
and log|B| are both proportional to the area of the black hole horizon in Planck
units at the time at which we study |Ψ⟩. Thus their size decreases with time.
NaivelyHR is inﬁnite dimensional since all sorts of things could be going on
far from the black hole, but we will restrict its deﬁnition to only run over the
subfactor which in|Ψ⟩ is nontrivially involved in the black hole dynamics. Thus
the size ofHR grows with time.
The third assumption leads to an interesting distinction between “young” and “old”
black holes [3], with the separation based on whether |R| is bigger or smaller than
|H||B|. When the black hole is young, |R| is quite small and B and H are entangled
signiﬁcantly. As the black hole becomes old however, |R| becomes large and B and
H taken together become a small subsystem of the full Hilbert space Houtside. Page’s
– 8 –
theorem [36] then suggests that the combined systemBH has a density operator which
is close to being proportional to the identity operator: 13
ρBH≈ 1
|B||H|IB⊗IH. (2.2)
The time beyond which this is true has come to be called the Page time. More carefully
we would expect a thermal distribution in the Schwarzschild energy at the usual tem-
perature T = 1
4πGM , but since we have put high-frequency modes in HR the thermal
density matrix forHH⊗HB is quite close to (2.2). 14
We can describe the state concisely by saying that BH is maximally entangled
with a subspace in R. More precisely, there is a |Ψ⟩-dependent decomposition ofHR
HR = (HRH⊗HRB)⊕Hother, (2.3)
with|RH| =|H| and|RB| =|B|, such that we can write the state of the full system,
to a good approximation, as 15
|Ψ⟩ =
(
1√
|H|
∑
h
|h⟩H|h⟩RH
)
⊗
(
1√
|B|
∑
b
|b⟩B|b⟩RB
)
. (2.4)
Here h and b label orthonormal bases for HH andHB respectively, and we have cho-
sen convenient complementary bases for HRH andHRB. RH and RB are called the
puriﬁcations of H and B respectively. The state has zero projection onto Hother.
This form of|Ψ⟩ makes it clear that any measurement done onB is perfectly corre-
lated with some other measurement done onRB. This consequence of the entanglement
was emphasized in [1]; in their language measurements done on RB project onto par-
ticular states in the basis |b⟩B. We hope that it is clear however that the presence of
this entanglement does not require any such measurement to be done; once we accept
the three assumptions the entanglement follows directly. Indeed we would argue that
Charlie’s ability to measure RB provides justiﬁcation for accepting the Hilbert space
structure of the model. 16
13Page’s theorem says that in a Hilbert space which can be factorized intoHA⊗HB, with|A|≤| B|,
a typical pure state has SA = log|A|− |A|
2|B| +O
(
1
|A|
)
.
14It is important in what follows that these “low-energy” modes can have quite high proper energy
near the horizon, so they are relevant to the experience of an observer who is near the horizon even
though the Schwarzschild temperature is typically very small compared to any scale relevant to that
observer.
15This representation of the state is called the Schmidt decomposition.
16Remember Charlie stays outside the black hole and has an arbitrarily large amount of time and
resources, so there seems to be no limit on his experimental ability. This will be diﬀerent for Alice,
whom we discuss now.
– 9 –
