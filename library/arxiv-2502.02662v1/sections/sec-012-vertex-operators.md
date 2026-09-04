---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-012-vertex-operators
section_title: "Vertex Operators"
section_number: null
pages: 15-17
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
string coupling factors which seem to break the structure of the genus expansion can in fact
be re-summed to preserve this structure.
4.1 A Double Expansion
If we neglect the Ω points and deformation by transpositions 15 the partition function of chiral
Yang-Mills theory on a surface with k boundaries becomes:
Z+
G(U1,...,U k) =
X
d
(qg 2G−2+k
s )d⟨
kY
i=1
 X
α⊢d
pα(Ui)Cα
!
⟩d. (4.1)
We wish to make the string theory structure of these correlators manifest. In string theory,
two expansions must be distinguished. On the one hand, there is the perturbative expansion in
the string coupling gs. On the other hand, there is an expansion over world-sheet instantons,
with expansion parameter e− A
2πα′ , where 1
2πα′ is the string tension and A is the area of the
embedding of the world-sheet in the target space. In our two-dimensional context, the world-
sheet covers the target space and A equals the area of the target space. In order to bring out
the structure of the double expansion, we reshape the expression (4.1) using the Riemann-
Hurwitz formula [26]:
2g− 2 =d(2G− 2) +kd−
X
i
ℓ(αi), (4.2)
15Note that, formally, we have defined a deformed Hurwitz theory for arbitrary values of the parameters t
and u. Therefore, equation (4.1) may be thought of as the corresponding string theory correlation functions
for t =u = 0. We discuss this aspect further in appendix C.
14
whereg denotes the genus of the covering surface and ℓ(αi) is the length of a conjugacy class,
i.e. the number of disjoint cycles of any element in this class. We write
Z+
G(U1,...,U k) =
X
d
qd
X
αi∈Yd
g2g−2
s
 kY
i=1
pαi(Ui)
!

gl(α1)
s Cα1··· gl(αk)
s Cαk

d . (4.3)
Let us analyze the content of equation (4.3). Firstly, we recall that, as explained in section
2.3, the covering space of Hurwitz theory is naturally interpreted as the world-sheet of a string
theory. Therefore, the factor g2g−2
s can be interpreted as the usual weighting factor for the
different world-sheet topologies. However, unlike the standard case, there is no explicit sum
over all possible topologies of the world-sheet in the above expression. This a distinctive feature
of the string theory at hand. Indeed, for each correlator of a Gromov-Witten theory, there
is only one contributing world-sheet at fixed instanton degree d. Nevertheless, an insertion
in the Yang-Mills theory is represented by a sum over all possible conjugacy classes in the
Hurwitz theory, which implies that many genera come into play. One can make this sum over
the genus of the world-sheet manifest by introducing the constrained correlators
⟨·⟩g,d :=⟨·⟩d·δ(g =g(d)), (4.4)
where g(d) in the argument of the δ function is the genus of the covering surface determined
by the Riemann-Hurwitz formula. It is a standard fact in topological string theory that
there exist topological constraints on correlators. In terms of the constrained correlators, the
partition function (4.3) reads
Z+
G(Ui) =
X
g
g2g−2
s
X
d
qd
* X
α⊢d
pα(U1)gl(α)
s Cα
!
···
 X
α⊢d
pα(Uk)gl(α)
s Cα
!+
g,d
. (4.5)
This is manifestly the genus expansion of a string theory and we interpret the sum over d as
the sum over world-sheet instanton degrees. This allows us to identify the string tension as –
see also [4,6] –:
α′ = 1
πg2
YM
. (4.6)
4.2 Vertex Operators
In string theory, correlation functions on a genus g world-sheet at instanton degree d scale
as g2g−2+k
s , where k is the number of insertions on the world-sheet. The genus expansion is
canonically written as a sum over all world-sheet topologies weighted by a factor g2g−2
s . The
remaining factorgk
s is relegated to the normalization of vertex operators: each one comes with
a single factor of the string coupling gs. In Hurwitz theory, the insertion of a conjugacy class
Cα in the target space corresponds to the insertion of ℓ(α) marked points on the worldsheet.
Therefore, each such insertion must be weighted by an additional factor gℓ(α)
s , and this is
indeed what we find. The physical interpretation of this finding is straightforward. By lore,
single cycles correspond to single string states, and come with a single factorgs.16 Accordingly,
16It was noted in [10, 27], based on [9], that there are interesting corrections to this lore. We discuss this
aspect further in section 5.
15
multi-cycles correspond to multi-string states and the length of a conjugacy class counts the
number of strings in the state defined by this conjugacy class.
This state of affairs is complicated by the presence of the coefficients pα(U), which also
scale with N. Consider an element U of the unitary group U(N) that acts non-trivially on a
p-dimensional space, with p≪N. Then,
pα(U) =Nℓ(αi)
Y
i

1− Trp(U|p)αi
N

, (4.7)
where U|p denotes the restriction of the element U to its non-trivial subspace, and Tr p the
trace on this subspace. In other words, pα(U) scales as g−ℓ(α)
s , up to corrections in gs. Thus,
the dominant part of the correlator on a surface of genus g scales asg2g−2
s , as expected from a
Yang-Mills partition function. The identification of the correlation functions of both theories
necessitates that we insert rescaled vertex operators on the string theory side. The dictionary
of observables at order d reads
U→g−d
s (Ce +O(gs)) . (4.8)
Before we move on the implementation of the deformations, we remark that in going from a
field theory to a string theory correlation function in equation (4.4), we have dismantled the
operator algebra structure of the observables. Indeed, in the field theory,
⟨Cα,Cβ⟩d =c γ
αβ⟨Cγ⟩d, (4.9)
where the c γ
αβ are the structure constants of the conjugacy class algebra Cd. In the string
theory, this equation no longer holds, because the Riemann-Hurwitz formula is not preserved
by the product of the algebra, which implies that the value of the genus for which ⟨Cγ⟩g,d is
non-zero depends on γ. The break-down of the algebra is crucial for dealing with the defor-
mations, as we explain momentarily. 17 Finally, we stress that in order to simplify notations,
we systematically write
⟨CαCβ⟩g,d, (4.10)
in order to refer to the correlation function
⟨Cα,Cβ⟩g,d. (4.11)
In this paper, expressions involving products of correlators should always be understood as
the insertion of two separate observables.
