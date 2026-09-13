---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-031-323-regular-sampling
section_title: "Regular Sampling"
section_number: 3.2.3
pages: 77-80
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
In section 3.2.1 and section 3.2.2, we showed how to sample the free particle
propagator for single bead and multiple beads. We proposed the transition probabilities
Tl′r′(R → R′) according to the free particle propagator part gF (R′), so we have
Eq.(3.19) which is gF (R′)Tlr(R′→R ) =gF (R)Tl′r′(R→R ′), therefore we can use a
simple version of acceptance rate A(s→s′) which is Eq.(3.21), to judge if we accept
the new state s′ or not. Those moves can simplify the acceptance rate A(s→s′), but
they can make the spatial conﬁgurations of involved beads more or less correlated.
So, In order to make the algorithm more robust, we can add some moves such that
the new conﬁguration of each bead does not depend on other beads. For example, as
is used in most Monte Carlo simulations, we can add moves with proposed transition
67
probabilities obeying Eq.(3.16) which is Tl′r′(R → R′) = Tlr(R′ → R), and use
Eq.(3.18) to judge if we accept the new state s′ or not. In these cases, the common
choices for Tl′r′(R→R ′) can be a constant over an interval or independent gaussian
functions. We can randomly select m beads from bead 0 to bead N,m can be at least
1 and at most N + 1, we put the label of the m beads into a group call it M, e.g., if
we select bead 0, 2, 4, then M ={0, 2, 4}, etc.
The proposed transition probability Tl′r′(R→R ′) can be written as,
Tl′r′(R→R ′) =
∏
I∈M
( A∏
i=1
TI(ri→r′
i)
)
, (3.57)
where TI(ri→r′
i) is the proposed transition probability for particle i in bead I, and
it is normalized to 1, ∫
dr′
iTI(ri→r′
i) = 1. (3.58)
There can usually be two choices.
Choice 1 For constantTl′r′(R→R ′), we can choose TI(ri→r′
i) as,
TI(ri→r′
i) = 1
(2α)3. (3.59)
In this case the new position r′i of particle i in a bead can be proposed from its
current positionri by,
r′
i =ri +αui, (3.60)
where ui = (ux,uy,uz) is a 3 dimensional random number and each of its
componentsux,uy,uz ranges from−1 to 1 uniformly.α is a number which controls
the step size of proposed move, it can be chosen to make the correspondingly
acceptance rate A(s→s′) around 20∼ 80%.
Choice 2 For independent gaussian functionTl′r′(R→R ′), we can chooseTI(ri→r′
i)
as,
TI(ri→r′
i) =
( 1√
2πσ2
)3
e−
(r′
i−ri)2
2σ2 . (3.61)
68
In this case the new position r′i of particle i in a bead can be proposed from its
current positionri by,
r′
i =ri +σgi, (3.62)
where gi is the gaussian random number deﬁned in Eq.(3.34), and σ is the
standard deviation of the gaussian function, which can control the corresponding
acceptance rate A(s→s′).
In the above two choices,Tl′r′(R→R ′) =Tlr(R′→R ), and the new conﬁguration
R′
I is proposed from the current RI, with a 3A dimensional vector ΛI which can be
either composed of ui orgi for each particle,
R′
I =RI + ΛI. (3.63)
If we propose new conﬁgurations for all the beads with the same 3 A dimensional
random vector Λ at the same time, namely,
R′
I =RI + Λ, (3.64)
it will still obey Eq.(3.16), Tl′r′(R→R ′) =Tlr(R′→R ). We can this kind of move
as a ‘shift’.
The regular sampling methods mentioned in this section are useful to guarantee
uncorrelated samples but we do not perform them very often. This is because they are
not as eﬃcient as the multi-level sampling. If we just move few beads a time, it is not
computationally eﬃcient since we need to update the whole path anyway. If we move
the same number of or more beads than the multi-level sampling method, we need
to use very small α, σ or Λ values in order to achieve similar acceptance rates as the
multi-level sampling. This means they are not able to explore the conﬁguration space
as eﬃciently as multi-level sampling does.
69
