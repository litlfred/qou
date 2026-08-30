---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-001-1-introduction-and-statement-of-results
section_title: "Introduction and statement of results"
section_number: 1
pages: 1-3
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
1.1. Cumulants in the Ising model. The Ising model is a mathematical model of ferro-magnetism
in statistical physics. It was introduced in 1920 by Wilhelm Lenz who gave it as a problem to his
Ph.D. student Ernst Ising [19]. It can be deﬁned on any ﬁnite graph, but we restrict ourselves to ﬁnite
subsets Λ of Zd. For any lattice site i∈ Λ, there is a random variable σi which is equal to either 1 or
−1 and represents the spin at site i. A spin conﬁguration ω = (σi(ω))i∈Λ is an assignment of spins to
every site of Λ.
The distribution of spins depends on the magnetic ﬁeld h and the inverse temperature β in a way
that is detailed in Section 2.1. In particular, spins corresponding to neighbour sites i and j are more
likely to be equal. The bigger β is, i.e. the lower the temperature is, the more important is this
phenomenon.
In his Ph.D. thesis [19], Ising solved the model for the one-dimensional case d = 1, and showed
that there is no phase transition. But in 1936, Peierls [33] showed that, in dimensions 2 and 3, when
h = 0, the Ising model undergoes a phase transition at a critical inverse temperature βc. He used
a combinatorial argument now known as Peierls’ argument. The two-dimensional model for h = 0
was then exactly solved by Onsager [32] in 1944, using analytic techniques and the transfer matrix
method. It turns out that in higher dimensions, there is also a phase transition for h = 0 (see [33], or
[13] for a more modern treatment). However, there is no phase transition when there is a magnetic
ﬁeld h⁄= 0 [25, 36].
The Ising model is a priori deﬁned on a ﬁnite subset Λ ⊂ Zd, but it is well-known that we can
take the thermodynamic limit Λ↑ Zd (see eg. [13]). This deﬁnes, for each pair of parameters ( β,h ),
a measure µβ,h on the set {−1, 1}Zd
of spin conﬁgurations on the whole d-dimensional lattice Zd. In
low temperature without magnetic ﬁeld, i.e. β large and h = 0, this measure is not unique; we will
consider the one corresponding to + boundary conditions, see Section 2.1 for details.
The Ising model has been studied in thousands of research articles, under various aspects. Among
many others, a subject of interest has been the decay of joint cumulants of the spins (also called
truncatedk-point functions or Ursell functions in the physics literature). Consider random variables
X1,...,X r with ﬁnite moments deﬁned on the same probability space Their joint cumulant of order
r is deﬁned as
κ(X1,...,X r) = [t1...t r] log
⟨
exp(t1X1 +··· +trXr)
⟩
,
where⟨Y⟩ denotes the expectation ofY and the notation [t1...t r]F stands for the coeﬃcient oft1...t r
in the series expansion of F . The ﬁnite moments assumption ensures that this series expansion exists,
at least formally. The joint cumulant of order 2 is simply the covariance. If all random variables
2010 Mathematics Subject Classiﬁcation. 82B20,60F05.
Key words and phrases. Ising model, cumulants, central limit theorems, cluster expansions, weighted dependency
graphs.
Both authors are partially supported by grant SNF-149461 from Swiss National Science Fundation.
1
2 JEHANNE DOUSSE AND VALENTIN F ´ERAY
X1,··· ,Xr are equal to the same variable X, then κr(X) := κ(X,...,X ) is the usual cumulant of a
single random variable.
Joint cumulants have a long history in statistics and theoretical physics, see e.g. [35]. In the case
where theXi’s are indicator functions of the presence of particles or + spins for example, they are often
referred to as truncated correlation functions or Ursell functions in the statistical physics literature.
In this paper, we will denote by κβ,h(σi1,...,σ ir) the joint cumulant of order r of spins σi1,...,σ ir,
with inverse temperature β and magnetic ﬁeld h.
Bounds on cumulants in the physics literature are often called cluster properties. There is in fact a
hierarchy of cluster properties, corresponding to sharper or weaker bounds on cumulants; we refer to
[5] or [26, Chapter 6, §1] for deﬁnitions of various kinds of cluster properties.
In the case of the Ising model, a ﬁrst bound on cumulants was obtained by Martin-L¨ of [27, Eq. (20)]
— see also [24, Section 1] —: he proved that the joint cumulantκβ,h(σi;i∈A) decreases exponentially
in diam(A)/r, where diam( A) is the the diameter of A and r the order of the cumulants. In [6],
Duneau, Iagolnitzer and Souillard sharpened this bound in presence of a magnetic ﬁeld ( h⁄= 0), or for
h = 0 and very high temperature: κβ,h(σi;i∈A) decays exponentially in 𝓁T (A). Here 𝓁T (A) denotes
the tree-length of A, i.e. the minimal size of a connected set of edges of the lattice Zd such that each
vertex ofA is incident to at least one edge in the set. In [26], Malyshev and Minlos have a similar result
in the case h = 0 and very low temperature. Both their approaches use cluster expansion, a powerful
tool introduced by Mayer and Montroll [28], which is now standard in the study of the Ising model.
Both proofs use additional ingredients of diﬀerent nature: Duneau, Iagolnitzer and Souillard use the
Lee-Yang circle theorem and complex analysis arguments, while Malyshev’s and Minlos’ approach
relies on combinatorial developments and bounds on joint cumulants for contours as an intermediate
step.
These bounds on cumulants will be our starting point to prove central limit theorems for patterns in
the Ising model. In order to make the article more self-contained, we give a simpler and more uniﬁed
approach of the decays of joint cumulants in several regimes where the cluster expansion converges.
To do so, for β1,β 2,h 1 > 0, let us introduce the three diﬀerent regimes
RHT (β1,h 1) :={(β,h ) : 0≤β <β1,|h|≤ h1} (very high temperature),
RLT (β2) :={(β,h ) :β >β2,h = 0} (very low temperature),
RSF (h1) :={(β,h ) :|h|>h 1} (strong magnetic ﬁeld),
and their union
R(β1,β 2,h 1) =RHT (β1,h 1)∪RLT (β2)∪RSF (h1).
The result is stated as follows.
Theorem 1.1. We consider the Ising model on Zd with parameters (β,h ). There exist positive con-
stants ε(d) < 1, β1 = β1(d), β2 = β2(d) and h1 = h1(d) depending on the dimension d, and for any
integerr≥ 1 a constant Dr such that for all A ={i1,...,i r}⊂ Zd, we have
⏐⏐κβ,h(σi1,...,σ ir)
⏐⏐≤Drε(d)𝓁T (A),
for any (β,h )∈R(β1,β 2,h 1).
The notion of tree-length 𝓁T (A) is important to make the connection with weighted dependency
graphs, which we discuss now.
Remark 1.2. In the very high temperature and strong magnetic ﬁeld regimes, one can chose ε(d)
independent of the dimension and Dr = 1 for all r≥ 1 (see the end of Section 3.1). This choice of Dr
is important to study the speed of convergence in the central limit theorem for the magnetization (see
[11, Section 5.3]), but is irrelevant for the purpose of the present article.
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 3
