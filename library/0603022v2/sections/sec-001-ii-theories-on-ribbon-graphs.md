---
doc_id: 0603022v2
doc_title: "Quantum gravity and the standard model"
section_id: sec-001-ii-theories-on-ribbon-graphs
section_title: "THEORIES ON RIBBON GRAPHS"
section_number: II
pages: 2-3
source_pdf: 0603022v2.pdf
source_sha256: 46e24c0289f61d44
doc_brief: "Quantum gravity and the standard model — 9 sections: INTRODUCTION; THEORIES ON RIBBON GRAPHS; CONSERVED DEGREES OF FREEDOM"
---
We start with a compact three manifold Σ of genus at
least 3. Given a two-dimensional surface S in Σ , we can
regard S as a union of trinions: 2-surfaces with three dis-
tinct/disjoint regions of connection (legs, for want of a
better name) to other such surfaces (Fig.1). Choosing a
maximal set of non-intersecting cuts on S gives a par-
ticular decomposition, or scoring, of S into trinions. We
shall call a scored 2-surface a ribbon graph Γ . It is a graph
in the sense of the obvious deformation of S into a rib-
bon graph with a node for each trinion and a connecting
ribbon edge or leg connecting each pair of nodes.
3
FIG. 1: A trinion and a trinion decomposition of a 2-surface S.
A map from a ribbon graph to a quantum system can
be made by associating a ﬁnite-dimensional state space
Ht to each trinion t and the tensor product operation to
trinion gluings. The speciﬁc map from a trinion t to its
Hilbert space may depend on the choice of a quantum
group Gq. In this case one labels each open edge of a
trinion with a representation of Gq and t with the asso-
ciated intertwiner. For the present work, we just need a
functor that assigns a ﬁnite-dimensional vector space to
each trinion. Thus, the state space associated to a given
Γ is
HΓ =
⨂
t∈Γ
Ht, (1)
with the label t running over all trinions in Γ and a sum
over labels (if they are present). Nothing that follows de-
pends on the choice of Gq, so we make the trivial choice
of no labels.
The state space of the theory is
H =
⨁
Γ
HΓ , (2)
where the sum is over all topologically distinct embed-
dings of all such surfaces in Σ with the natural inner
product ⟨Γ |Γ ′⟩= δ ΓΓ ′.
Some speciﬁc examples of theories with such state
spaces are: graphs labeled by quantum groups (where
representations of the quantum groupGq label the edges
and Ht is the space of Gq-invariant tensors on S), topo-
logical ﬁeld theory , Loop Quantum Gravity in both 2 + 1
and 3 + 1 (in which case the algebra is SUq(2) and the
quantum deformation is deﬁned in terms of the cosmo-
logical constant Λ by q = exp { 2π
k+2 }, with k = 6π
GΛ [10])
and, in general, the functorial construction of topologi-
cal quantum ﬁeld theories when the source category is
2-dimensional surfaces S.
Local dynamics on H can be deﬁned by excising sub-
graphs of Γ and replacing them with new ones. The gen-
erators of such dynamics are given graphically in Fig.2.
Given a ribbon graph Γ , application of Ai results in
ˆAi|Γ ⟩=
∑
α
|Γ ′
αi ⟩ (3)
where Γ ′
αi are all the ribbon graphs obtained from Γ by
an application of one move of type i (i = 1, 2, 3).
A1 =
A2 =
A3 =
(5)
FIG. 2: The three generators of evolution on the ribbon graph
space H. They are called expansion, contraction and exchange
moves.
FIG. 3: These two graphs are not distinguished by the usual
trinion decomposition of H.
Together with the identity , these moves generate the
evolution algebra
A evol = {1, A i} , i = 1, 2, 3 (4)
on H .
This is a basic description of such theories which will
sufﬁce for the purposes of this paper.
