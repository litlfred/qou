---
doc_id: arxiv-2106.01332v4
doc_title: "Braided matter interactions in quantum gravity via 1-handle attachment"
section_id: sec-006-vi-isotopy-inv-ariants-of-braided-networks
section_title: "ISOTOPY INV ARIANTS OF BRAIDED NETWORKS"
section_number: VI
pages: 10-13
source_pdf: 2106.01332v4.pdf
source_sha256: 44c19a99624997bf
doc_brief: "Braided matter interactions in quantum gravity via 1-handle attachment — 9 sections: INTRODUCTION; (for C𝓁(6)) and B3 (for C𝓁(4)). In; THEORIES ON RIBBON GRAPHS"
---
The fact that isotopy classes of trivalent braided networks are used in the scheme described above implicitly
raises two important issues. The ﬁrst relates to the possibility of associating conserved quantities to particles
embedded in braided networks. Secondly, we ideally want to consider invariants that distinguish diﬀerent particles
in Bilson-Thompson’s model, and diﬀerent conﬁgurations of particle networks. In the previous literature the
invariant link has been used to argue that particles correspond to diﬀerent states [2]. This is a link-valued invariant
of braided networks, in the sense that it associates a topological link to a given braided network. In [8], the
author has constructed certain topologies on braided networks that distinguish diﬀerent topological conﬁgurations
associated to particles in Bilson-Thompson’s model. We follow a diﬀerent paradigm in the present article, which is
particularly suitable to distinguish diﬀerent braided network conﬁgurations. We utilize, in fact, algebraic invariants
of isotopy classes of braided networks based on Kauﬀman-Lins recoupling theory [4]. We provide a formulation of
invariants closely related to those of [24, 25], where we do not preserve Reidemeister move I, but rather we have
invariance under the framed Reidemeister move I. In fact, the invariants given by Mizusawa and Murakami in [25]
are suitable as well in the precise formulation thereby given, although twists would be neglected and the particles in
Bilson-Thompson model would be indistinguishable. Topologically, the isotopy classes of Bilson-Thompson particles
can be distinguished by their combed position. Since during the evolution with respect to time the bradied network
might be substantially deformed (for instance by 1-handle slides), it might not be straightforward to individuate the
particles in a braided network, and having some global factor in the invariant provides information that might not be
immediately retrived. One further subtlety concerns the fact that Matsuzaki’s moves treat embeddings in the 3-space
R3, or its compactiﬁcation S3. For diﬀerent manifolds, which are not simply connected, some diﬀerences arise, such
as the fact that there are diﬀerent types of unknotted surfaces (depending on which holes they wrap around), but
the local moves remain unchanged, and the same paradigm can be applied.
Now, we show that classical results of Kauﬀman and Lins, suit well our machinery. We ﬁx a natural number n≥ 1,
and let q be a 2nth root of unity. We let each trinion of a trivalent braided network correspond to a spin network
vertex where the Jones-Wenzl projector is used [4], Section 4, Deﬁnition 3 with the integer triple {a,b,c} which is
q-admissible, i.e. a +b +c is even, a +b−c,b +c−a,c +a−b≥ 0 and a +b +c≤ 2n− 4. In this perspective,
each ribbon of a ribbon network consists of a edges for some a, and the crossings are “cabled” as well. We consider
all q-admissible triples at each vertex, and normalize the vertices by dividing by their θ values divided by the traces
∆i of the projectors at the incident edges. In fact, the trinions so considered are orthonormal bases, as seen in [26],
of the skein vector space with three boundary arcs. See also [24], and compare with [25], where this construction
appears as well. Then, using the skein relation for the Jones polynomial at a root of unity A (related to q viaA2 =q
as usual), and the recursive deﬁnition of the Jones-Wenzl projector, we can associate a numerical value KLn(N ) to
any braided network as follows. Each twisted edge is written as a power of A times a double half twist, as observed
before, and each vertex is multiplied by its conjugate, determined as in [24, 26] by taking the mirror image and
multiplying the results of smoothing all crossings and iterating the Jones-Wenzl projectors. For each ﬁxed choice of
admissible triples, this value has been proven to be a framed isotopy invariant of trivalent graphs up to powers of
the value A. See [4], Section 4. We argue that indeed this is an isotopy invariant of braided networks, by verifying
that Matsuzaki’s moves are preserved. Moreover, the extra powers of A (or q) that appear in the statement of the
original result of Kauﬀman and Lins, in our setting, play the role of counting the twists of the edges. In what follows,
we will use a notational convention to refer to braids in our computations. Namely, we will suppose the braids being
placed vertically as in Figure 1 and Figure 3, and algebraically described as composition of twists and crossings as
in a representation of the framed braid group. A twist will be denoted by the symbol θ, while a crossing is denoted
byR. Horizontal juxtaposition is indicated as a tensor product, and the straight ribbon (i.e. the identity element of
11
the framed braid group) is indicated by |2n, where 2 refers to the two edges of the ribbon. For example, with m = 2,
the positron on the top-left of Figure 1 is given by ( |2⊗R)(R−1⊗| 2)θ⊗3, where the composition symbol has been
omitted, and reading from right to left corresponds to braids from top to bottom.
Theorem 2. LetN be a trivalent (oriented) braided network and let n≥ 1. Then, KLn(N ) is an isotopy invariant
ofN .
Proof. We need to verify that KLn(N ) preserves Matsuzaki’s moves since, as observed above, braided networks
are isotopic if and only if their diagrams are related by a ﬁnite sequence of these moves. Invariance under framed
Reidemeister moves II and III are the fundamental results of Kauﬀman in the construction of the Jones polynomial
from the (now called) Kauﬀman bracket polynomial. Sliding ribbons above and below trivalent networks is seen to
preserve the value of KLn as a consequence of framed Reidemeister moves II and III, once the recursive deﬁnition
of Jones-Wenzl projector is applied at the vertex. In fact, after smoothing, one obtains that the lines of a ribbon
overpass/underpass closed Jordan curves, or cups and caps. Either way, using the Reidemeister moves II and III one
can slide the ribbon as required. This is also observed in Section 4.3 of [4], and it works for any ﬁxed admissible
colouring. We need to verify the framed Reidemeister move I (i.e. cancellation of kinks). This does not appear, at
least in the form needed for our purposes, explicitly in the work of [4]. We proceed as follows. First, consider a
single strand self-crossing to give a positive twist. Smoothing at the single crossing we obtain A·◦| +A−1·| , where◦
indicates a closed Jordan curve,| denotes a straight line and we use a· symbol to separate scalars from diagrams they
refer to. Using the renormalization value for ◦ =−A2−A−2, we ﬁnd the value−A3·| . Applying the same procedure
to the self-crossing that generates negative loops, one obtains A−3·| . So, concatenation of positive and negative
kinks gives the straight strand |, as expected. Now, in general, the ribbons of the braided network N correspond to
groups of more strands, so the positive loops consist of parallel strands that twist together to give a self-crossing. We
show how to proceed with m = 2 strands, since a simple induction generalizes this step to all values of m. Using the
computation for the positive and negative twists just obtained, we see that a single line can be slid above and below
a kink, since both evaluations simply give−A±3·R, where R± indicates a crossing of two lines (positive or negative).
A self-crossing with two strands twisted positively, which we indicate with the symbol θ2, can therefore be rewritten
as the tangle
θ2 = (d⊗| )(|⊗|⊗ R)(|⊗ R⊗| )(b⊗|⊗| )(θ1⊗| ), (5)
whereb is the birth (i.e. cap) tangle, d is the death (i.e. cup) tangle, θ1 = (d⊗| )(|⊗ R)(b⊗| ) is the decomposition of
(positive) twist tangle into compositions of generators of the tangle category. Using θ =−A3·| , and by Reidemeister
moves II and III, the previous expression becomes −A6·R2. Similar computations show that the negative twist is
written as−A−6·R−2. The concatenation of positive and negative twists gives the straight lines ||. In the general
case for θm, a self-crossing of m strands, one obtains
θm = (−1)3mA±3m· (|m−2⊗R±)··· (R±⊗|m−2)(R±⊗|m−2)··· (|m−2⊗R±), (6)
where + or− depends on whether we consider positive or negative twists, respectively, where the symbol|m indicates
m straight parallel lines. It follows that the composition of twists for arbitrary m gives|m. In this case, as before,
the argument works for any ﬁxed admissible colouring. To show invariance under IH move, one considers that this
corresponds to a change of an orthonormal basis to another one, and therefore consists of applying a unitary matrix,
see [26], and the value of KLn(N ) does not change. In this case we need to let the colourings vary over all the
admissible possibilities.
A. Examples and Computations
The computation of twists in Theorem 2 suggests that the invariant KLn distinguishes, in general, the particles
of Bilson-Thompson model, in the sense that two braided networks that are identical, except for two regions that
enclose one of the particles of Figure 1 or Figure 3, generally have diﬀerent values of KLn. Of course, in order to
give a speciﬁc statement of this sort, regarding what particles are distinguished, one needs to ﬁx the values of q (i.e.
A) and n. It is not the scope of the present article to ﬁx values for them, but we rather are contented with showing
that the theory is nontrivial.
12
We observe that no isotopy invariant of braided networks is suitable to distinguish Z0 and γ bosons, as they diﬀer
by an application of the framed Reidemeister move I which, by construction, is preserved by any isotopy invariant of
braided networks.
By means of example we show that the invariant KL4 does change when we replace a boson γ by a boson W +,
so that the algebraic setting detects the topological non-equivalence of diﬀerent bosons. Setting n = 4, means that
each ribbon edge is represented by parallel lines whose total sum does not exceed 6. Since the two networks are
assumed to be identical outside the region enclosing the two particles W + and γ, we can substantially compute the
invariantKL4 of W + and γ as depicted in Figure 3, as the computation of KL4 would give identical values, when
computing the rest of the braided network. We rewrite the twists of W + using the computation performed in the
proof of Theorem 2. The computations are identical for each colouring, with the only diﬀerence being that one needs
to take into account the number of strands in the twists. For example, trinions all coloured with two strands (the
triple{2, 2, 2} isq-admissible), gives us an overall factor of A18 and the braids of W + are replaced by R2⊗R2⊗R2,
two consecutive crossings that braid the edges of each ribbon. We perform now smoothing of each crossing and utilize
the deﬁnition of the Kauﬀman bracket polynomial. Observe that performing the two smoothings on a ribbon produces
two diagrams, one with a straight ribbon and an extra factor of A2, and one with the ribbon removed and a factor
of 1−A−4. The computation is therefore reduced simply to the product of these factors. We denote by |i the braid
with i straight ribbons, where i = 0, 1, 2, 3. We obtain that the braid W + can be replaced in the braided network by
the sum of terms
W + =−A24·| 6−A18·[A2(1−A−4) + 2A4(1−A−4)]·| 4−A18[(1−A−4) + 2A2(1−A−4)2]·| 2−A18(1−A−4)3·| 0. (7)
By deﬁnition, we have that the evaluation with the boson γ, with the same colour, is simply |6, which appears
up to a factor in Equation (7). When computing KL4 of W +, the terms with lower powers of | disappear, since
they contain turnbacks that are annihilated by the Jones-Wenzl projectors. In general, considering all colourings,
KL4 distinguishes the two bosons, as previously claimed. We remark that in the previous computation we have
pairs of ribbons or single ribbons, instead of triples representing framed braids. In general, this is a middle step of a
computation and, therefore, it is not to be considered as a physically meaningful conﬁguration of a braided network.
It has been pointed out, in [2], that in order to introduce a nontrivial dynamics for braided particles, it is
necessary to consider moves such that (what we have here called) braided networks do not constitute noiseless
subsystems. In practice, what the authors of the article [2] have realized, is that it is not enough to consider braided
networks as arising from triangulations of manifolds and only local moves that are derived from Pachner moves. A
natural question to ask, is whether performing surgery on manifolds to introduce dynamics represents an example
of such a paradigm. We argue that this is indeed the case, and that the invariant KLn shows this. In fact, (very
tedious) computations show that there are cases where the interaction/decay of two particles in a braided network,
obtained via surgery as described above, produces another braided network whose KLn invariant is diﬀerent from
the initial one. Applying Theorem 2 it follows that initial and ﬁnal state are not isotopy equivalent and, there-
fore, the topology of the system has been changed during surgery, giving an aﬃrmative answer to the previous question.
We brieﬂy describe the computations related to electron/positron annihilation producing one virtual photon. Recall
that, in the setting of the present article, virtual means that the photon produced in the process lives on the handle
that mediates the interaction. We set n = 4, and consider the colouring where all edges are assigned value 2 (the
remaining colours are computed in the same way). Let us indicate the value associated to this colouring by KL2
4(N ).
Suppose that e+ and e− are right-handed. First, observe that the value of two braided networks that are identical
outside two regions containinge+ ande− diﬀer by a multiplication of a (Laurent) polynomial f(A±1), where A refers
to the positron, andA−1 refers to the electron. Therefore, to compute KL2
4(N ), for a braided networkN containing a
positron and an electron, we can perform the computation of KL2
4(e−) for the electron, and obtain the contribution of
e+ simply by changing the variableA−1 to its inverseA. This computation can be simpliﬁed as follows. One ﬁrst uses
the formula obtained in Theorem 2 to rewrite the twisting of each ribbon as composition of two negative crossings.
This produces an overall factor of −A−18 multiplying the braid corresponding to e−. Now, we obtain a braid in pure
twist form by applying two rotations of trinions [19]. We remark, here, that we can perform this operation by means
only of framed Reidemeister moves, without twisting the vertex, or using the IH move, since the number of twists is
even (due to the orientability assumption discussed above) [16]. No overall multiplying factor is introduced during
this process. We can also see this by applying Proposition 3 in Section 4.2 of [4], since two opposite rotations would
be utilized. In pure twist form, the right handed electron e− can be written as [0 ,−2,−1], see table at page 12 of
[19]. Now, we use the computation for the composition of two negative crossings R−2 = A−2·| 2 + (1−A4)·| 0, as
obtained in Theorem 2, to complete the computation. This requires three iterations to give the result
KL2
4(e−) =−A−24·KL2
4(|6) +A−18Q(A)·KL2
4(|4) +A−18P (A)(1−A4)·KL2
4(|2), (8)
13
where
P (A) :=A−18[2A−2(1−A4)− (1−A4)(−A2−A−2)], Q (A) :=A−22(1−A4)−P (A)A−2. (9)
As previously observed, we also have
KL2
4(e+) =−A24·KL2
4(|6) +A18Q(A−1)·KL2
4(|4) +A18P (A−1)(1−A−4)·KL2
4(|2), (10)
where the polynomials P and Q are deﬁned in Equation (9). Let N be a braided network containing e− and e+ and
suppose that, via surgery on the base manifold,N undergoes an annihilation ofe− ande+ on an attached handle (over
which a virtual boson is exchanged). Let us denote by N′ the braided network obtained after surgery, and by ˆN the
network obtianed fromN by removing e+ and e− and replacing them with two particles γ. From the computations
giving Equation (8) and Equation (10) we have that
KL2
4(N ) =KL2
4( ˆN ) +KL2
4( terms containing Q(A±),P (A±)). (11)
The extra terms in Equation (11) correspond to the braids with two ribbons, or a single ribbon, after the smoothings
ofe±, and their coeﬃcients do not generally vanish identically, but their contribution to KL4 evaluations are trivial,
since they contain turnbacks annihilated by the Jones-Wenzl projector. Summing the contributions due to the other
q-admissible colourings, we see directly that the surgery corresponding to annihilation electron/positron changes the
isotopy class of the braided network since, in general, we have that KL4( ˆN ) is diﬀerent from KL4(N′).
