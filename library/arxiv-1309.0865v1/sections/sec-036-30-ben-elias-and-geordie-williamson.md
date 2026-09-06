---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-036-30-ben-elias-and-geordie-williamson
section_title: "BEN ELIAS AND GEORDIE WILLIAMSON"
section_number: 30
pages: 30-31
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
The analogous statement can be made for standard bimodules, or tensor products of standard
and Bott-Samelson bimodules.
Proof. We show thatBs ⊗RQ ∼=R ⊗RsQ is isomorphic toQ ⊗QsQ, which implies the
lemma by a simple induction. One has an obvious inclusion i :R ⊗Rs֒→ Q ⊗QsQ
and it is enough to show that this is surjective. However, any 0 ⁄=f ∈R divides the
s-invariant polynomialfs (f ) and inQ ⊗QsQ we have
s(f ) ⊗ 1
fs (f ) = 1
f ⊗ 1.
It follows that i is surjective, and the lemma follows. The analogous proof fo r stan-
dard bimodules is even simpler. □
In particular, base change from R toQ on the right will send a Bott-Samelson bi-
module to a Q-bimodule, not just an (R,Q )-bimodule, and the base change functor
is monoidal. Let BSBimQ denote the essential image of BSBim inside the category of
Q-bimodules. By the above lemma, it is the full subcategory of Q-bimodules gener-
ated by the bimodules Bs,Q
def= Q ⊗QsQ. Let SBimQ denote its Karoubi envelope. We
deﬁne StdBimQ similarly .
AsQ-bimodules we have a splitting
(3.7) Bs,Q ∼=Q ⊕Qs.
One way to observe this is that the sequences (3.4) and (3.5) a re split. In fact, they
“split each other:” the composition R → Bs → R is multiplication by αs, which
becomes invertible inQ. Therefore, any Soergel bimodule overQ splits into standard
bimodules. When the realization is faithful one has
Hom(Qw,Q v) =
{
Q ifw =v
0 otherwise,
so that standard bimodules overQ are indecomposable and pairwise non-isomorphic.
It follows that SBimQ is equivalent to the (additive closure of the) 2-groupoid of W
overQ.
We conclude SBimQ has a drastically different behaviour to SBim — SBim is far
from being a 2-groupoid! In the following, we will refer to th e faithful monoidal
functor
SBim → SBimQ
as localization. It plays an important role in what follows, essentially bec ause SBimQ
is such a simple category . We already know that Hom spaces bet ween various Qw
are either rank 1 or 0. Because the passage to the localizatio n is injective, and be-
cause morphisms between various Qw are so easy , we can study morphisms in SBim
based on what their restrictions are to simple summands in SBimQ after localization.
Given an explicit morphism f in BSBim, we will be able to write down explicitly
SOERGEL CALCULUS 31
its restriction to each standard summand of the source and ta rget in SBimQ, and in
doing so, will be able to conclude whether or not f = 0.
Remark 3.21. One may use the homogeneous fraction ﬁeld Q′ instead of the full frac-
tion ﬁeld, and the results in this paper pertaining to locali zation will be (essentially)
unchanged. The homogeneous fraction ﬁeld is graded; howeve r,Q′ ∼= Q′(2) so that
the grading does not yield any interesting invariants (even the parity is irrelevant,
as investigation reveals). Though more difﬁcult, all the lo calization results in this
paper should hold if one only inverts the simple roots αs and their W -conjugates.
One advantage to using Q over these alternatives is that Q is a ﬁeld.
Part 2. Diagrammatics
