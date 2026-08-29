---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-006-26-related-results-and-perspectives
section_title: "Related results and perspectives"
section_number: 2.6
pages: 13-14
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
relation to previous works on the subject :
• An analogous problem has already been considered on the real line instead of the circle,
see [8, 16]. In this case, one still has a positively multiplicative graph whose corresponding
algebra is the fusion ring for the representation theory ofU(k). The continuous limit of this
discrete model corresponds to convolution of co-adjoint orbits of U(k) instead of adjoint
orbits [26, 11], and there is a central limit theorem towards a Dyson Brownian motion on
the real line. Up to our knowledge, no quantitative central limit theorem has been obtained
in this framework; it is however expected that the method used in the present paper could
be adapted to the real line.
• There exists a natural quotient of Bk,n which describes the movement of a particle on a
discrete lattice of type Ak conditioned to stay in a macroscopic alcove of size n. The graph
is still positively multiplicative and the corresponding algebra is the fusion algebra of type
Ak at level n. Such processes have been intensively studied in the wider setting of aﬃne
semisimple Lie algebras by Defosseux [18]. In particular, our result in the particular case
µr =µ for 1≤r≤m and n,m going to inﬁnity is similar to [18, Theorem 8.1]. The latter
theorem also mention a Donsker’s type theorem for the sequence ( ξn(µ1∗···∗ µi))1≤i≤m.
Such results could also be obtained for general sequences m from our results by imposing
that (‖µi‖2)1≤i≤m is constant and (‖µi‖3)1≤i≤m is bounded as m,n goes to inﬁnity. We
mention also that asymptotic results in the simplest case of a random walk in an alcove
have been obtained before by Grabiner [27].
• Considering nonintersecting particles on the discrete circle conditioned to not intersect is
not new. A ﬁrst work in this direction has been done by Fulmek [22] in the case where
only one particle at a time jumps to a free next location: this correspond to considering
the adjacency matrix of Bk,n only, and not the other commutating adjacency matrices
AI for I ⁄= (k,k − 2,..., 0). The author then proved exact formulas for the transition
probabilities. This work has been later generalized by Krattenthaler to other small steps
cases and similar graphs (corresponding to other aﬃne Lie algebras) [37]. In this paper,
the author also obtained in the small step case local limit theorems similar to the ones of
the present paper.
Beware that the stochastic processes studied above and in the present paper are diﬀerent
from the the periodic TASEP with k particles on a circle of size n: indeed, the TASEP is a
continuous time Markov process whose transition matrix is given by the adjacency matrix
of Bk,n, whereas our model is a discrete time Markov process whose Markov kernel is a
Doob h-transform of this adjacency matrix. The two Markov processes have very diﬀerent
behaviors. For example, the stationary distribution of TASEP is the uniform distribution
on Bk,n whereas the stationary distribution of our model is given by µh(I) = |V (ξn(I))|2
nk .
• The cylindric hexagonal dimer model is a particular instance of the present framework by
considering the transition matrixA =∑n−k
i=1 AI (i) withI(i) = (k−1+i,k−2,..., 0) (this is a
consequence of the quantum Pieri rules forQH(Gk,n) from [5, p.5] and the bijection between
hexagonal dimer models and nonintersecting paths, see [32, Figure 1]). This relation has
already been deeply studied when considering the conﬁguration on the real line [16], and it
14 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
is expected that such correspondence also holds on the circle. See also [12] for results on
the winding number for the cylindric hexagonal dimer model when k,n are large.
• The relation between nonintersecting particles on the circle and the unitary group has
already been considered from a probabilistic perspective in the continuous case by Metcalfe,
O’Connell and Warren [43]. They build Markov processes on Tk by using the convolution of
a family of commuting Markov kernels which are continuous version of our Markov kernel
Ah
I . They also relate this construction to the convolution of orbits on Uk. Our work can be
seen as a discrete version of theirs.
• Regarding the geometric application of our results, we mention that there have already been
some combinatorial results on counting rational functions with prescribed critical points
(see [48]). From a quantum cohomological perspective, the relation between the quantum
cohomology of the Grassmannian and the orbits of the unitary group goes back to [3]. It
would be very interesting to pursue this relation from a probabilistic point of view. Note
also that the quantum cohomology of the Grassmannian also appear in the study of the
so-called rigid system, see [4].
Our work is a ﬁrst step towards two main interesting and challenging directions :
• The ﬁrst natural question is the behavior of the system when k grows with n. The prob-
ability distribution at time t
k of a Dyson unitary Brownian motion with parameter (1 , 1)
converges in some sense toward the marginal µ⊠t of the free unitary Brownian, see [7] for a
formal deﬁnition of the latter and a proof. It can be easily deduced from our work that un-
der good normalization hypotheses, ξn(m) is close toµ⊠t for somet> 0 whenk =O(logn).
However, it is expected that such approximation holds for k =O(n). It would be very in-
teresting to study this problem and related questions (see also [41] for the distribution of
the winding number in the continuous case when k goes to inﬁnity).
• The graph Bk,n is a particular instance of a Kirillov-Reshetikhin crystal, and there is a full
family of similar graphs which extend the present framework to other Kirillov-Reshetikhin
crystals, see [29]. They corresponds each time to movements of colored particles on a circle
or a segment conditioned to not intersect, sometimes with some additional symmetries. We
expect that our results could be extended to this larger setting in some cases: the main
diﬃculty is to get a explicit diagonalization of the adjacency matrixA, which is not obvious
in the more general setting (see [36] for an approach to this problem). Another interesting
direction would be to consider graphs related to the equivariant quantum cohomology of
the Grassmannian instead of the usual one, see [14]: the corresponding graph describes
particles moving on a discrete circle and conditioned to not intersect, but with jumping
rates depending on the location. Once again, the main challenge is to explicitly diagonalize
the adjacency matrix; we expect that such a task would be manageable when all jumping
rates but one are equal.
