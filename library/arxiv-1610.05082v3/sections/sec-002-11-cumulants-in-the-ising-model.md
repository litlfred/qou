---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-002-11-cumulants-in-the-ising-model
section_title: "Cumulants in the Ising model"
section_number: 1.1
pages: 1-2
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
in statistical physics. It was introduced in 1920 by Wilhelm Lenz who gave it as a problem to his
Ph.D. student Ernst Ising [15]. It can be deﬁned on any ﬁnite graph, but we restrict ourselves to ﬁnite
subsets Λ of Zd. For any lattice site i∈ Λ, there is a random variable σi which is equal to either 1 or
−1 and represents the spin at site i. A spin conﬁguration ω = (σi(ω))i∈Λ is an assignment of spins to
every site of Λ.
The distribution of spins depends on the magnetic ﬁeld h and the inverse temperature β in a way
that will be detailed later (see Section 2.1). In particular, spins corresponding to neighbour sites i and
j are more likely to be aligned (i.e. both equal to 1 or both equal to −1); the bigger β is (i.e. the
lower the temperature is), the more important is this phenomenon.
In his Ph.D. thesis [15], Ising solved the model for the one-dimensional case d = 1, and showed
that there is no phase transition. But in 1936, Peierls [28] showed that, in dimensions 2 and 3, when
h = 0, the Ising model undergoes a phase transition at a critical inverse temperature βc. He used a
combinatorial argument now known as Peierls’ argument. The two-dimensional model for h = 0 was
then exactly solved by Onsager [27] in 1944, using analytic techniques and the transfer matrix method.
It turns out that in higher dimensions, there is also a phase transition for h = 0 (see [28] or [10] for a
more modern treatment) and no phase transition when there is a magnetic ﬁeld h⁄= 0 [20, 33].
The Ising model is a priori deﬁned on a ﬁnite subset Λ⊂ Zd, but it is well-known that we can take
the thermodynamic limit Λ↑ Zd (see eg. [10]).
This deﬁnes, for each pair of parameters ( β,h ), a measure µβ,h on the set {−1, 1}Zd
of spin con-
ﬁgurations on the whole d-dimensional lattice Zd. (In low temperature without magnetic ﬁeld, i.e. β
large and h = 0, this measure is not unique; we will consider the one corresponding to + boundary
conditions, see Section 2.1 for details.)
The Ising model has since been studied in thousands of research articles, under various aspects.
Among many others, a subject of interest has been the decay of joint cumulants of the spins (also
called truncatedk-point functions or Ursell functions in the physics literature). The joint cumulant of
order r of spins σi1,...,σ ir is deﬁned as
κβ,h(σi1,...,σ ir) = [t1...t r] log
⟨
exp(t1σi1 +··· +trσir)
⟩
β,h.
The covariance is the joint cumulant of order 2 (more detail in Section 2.2).
Bounds on cumulants in the physics literature are often called cluster properties. There is in fact a
hierarchy of cluster properties (corresponding to sharper or weaker bounds on cumulants); we refer to
[4] or [21, Chapter 6, §1] for deﬁnitions of various kinds of cluster properties.
2010 Mathematics Subject Classiﬁcation. 82B20,60F05.
Key words and phrases. Ising model, cumulants, central limit theorems, cluster expansions, weighted dependency
graphs.
Both authors are partially supported by grant SNF-149461 from Swiss National Science Fundations.
1
arXiv:1610.05082v3  [math.PR]  27 Jun 2017
2 JEHANNE DOUSSE AND VALENTIN F ´ERAY
In the case of the Ising model, a ﬁrst bound on cumulants was obtained by Martin-L¨ of [22, Eq. (20)]
— see also [19, Section 1] —: he proved that the joint cumulantκβ,h(σi;i∈A) decreases exponentially
in diam(A)/r, where diam(A) is the the diameter ofA andr the order of the cumulants. In [5], Duneau,
Iagolnitzer and Souillard sharpened this bound in presence of a magnetic ﬁeld (h⁄= 0), or forh = 0 and
very high temperature: κβ,h(σi;i∈ A) decays exponentially in 𝓁T (A), the minimum length of a tree
connecting vertices of A (see Section 2.3 for a formal deﬁnition of the tree-length). In [21], Malyshev
and Minlos have a similar result in the case h = 0 and very low temperature. Both their approaches
use cluster expansion, a powerful tool introduced by Mayer and Montroll [23] which consists in viewing
our model in terms of macroscopic geometrical objects instead of considering its original microscopic
components. Both proofs use additional ingredients of diﬀerent nature: Duneau, Iagolnitzer and
Souillard use Lee-Yang circle theorem and complex analysis arguments, while Malyshev’s and Minlos’
approach relies on combinatorial developments and bounds on joint cumulants for contours as an
intermediate step (contours will be deﬁned in Section 3.2).
