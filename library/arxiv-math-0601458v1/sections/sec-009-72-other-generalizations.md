---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON"
section_id: sec-009-72-other-generalizations
section_title: "Other Generalizations"
section_number: 7.2
pages: 58-60
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS JEFFREY MORTON — Interest in combinatorial interpretations of mathematica l entities stems from the convenience of the concrete models they provi de."
---
7.2.1. Higher-Valence Stuﬀ Operators. We have described stuﬀ types and operators
in terms of quantum mechanics, but it should be clear that they also h ave an
independent interest as algebraic objects in their own right. Stuﬀ t ypes form a
categoriﬁed Hilbert space, but also a categoriﬁed algebra, since th ey have a concept
of multiplication in the space.
The key fact behind our approach has been that stuﬀ types and st uﬀ operators
form 2-categories of groupoids over either one or two copies of FinSet0. Stuﬀ
operators have an action which are the equivalent of linear operato rs on this 2-
Hilbert space. This action arises because of the fact that taking a p ullback over
one copy of FinSet0 under both a stuﬀ type and an operator removes two of the
maps to this underlying FinSet0, and gives an object with one such map.
In fact, there is no reason why we must restrict ourselves to grou poids with either
one or two maps to FinSet0 - the categoriﬁed versions of vectors or matrices. We
have done so because these are the most directly relevant to quan tum mechanics,
but for categoriﬁed algebra, it makes sense to generalize to look at the equivalent of
“p-forms”, or “p-index tensors” (the natural inner product obscures the diﬀere nce
between vectors and covectors in this setting). These would be gr oupoids with
projections into p copies of FinSet0. Contraction of two tensors over some pair
of indices would amount to identifying the corresponding copies of FinSet0 and
taking a pullback of the two projections into this copy.
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS 59
The categoriﬁed p-forms could be seen as p-sort types: types of structure (or
stuﬀ) which could be put on p underlying sets of diﬀerent “sorts” of objects.
The notion of a club described by Max Kelly in [8] can be seen as a signiﬁcant
generalization of this setup, where the categories involved need no t be groupoids.
There is a body of results about these which may bear on the ideas ab ove, and turn
out to be relevant to other physical situations.
7.2.2. Multisort Species and QFT. In appendix C.1 we refer to a description of
generalized species as functor categories between ! /BZ and ˆ
/C0 for groupoids /BZ and
/C0 . These “species” are the “structure types” of our terminology, which correspond
to the case where both groupoids are 1, the one-element groupoid, in which case
!1 = FinSet0 and ˆ1 = Set. These correspond to functors from ﬁnite sets to sets
of structures which can be put on them. We also mentioned the 2-rig ˆ!n, a.k.a
Set[Z1, . . . ,Zn], the 2-rig of n-sort structure types: these correspond to functors
from collections ﬁnite sets of n “sorts” (i.e. n copies of FinSet0) to sets of structures
which can be put on these.
We could reverse this point of view in the case of structure types, t o view them
as faithful functors from groupoids of structures into the grou poid of ﬁnite sets
(giving the “underlying” set of a structure) and then weaken the r equirement that
the functor be faithful to get the more general “stuﬀ types”, s o too we can reverse
our point of view of multisort structure types, to view them as faith ful functors from
a groupoid of “ n-sort structures” down to FinSet0
n, giving the n underlying sets
of each sort. These functors will be faithful for the same reason as in the case n = 1.
Weakening this requirement would give us a notion of stuﬀ type corre sponding to
functions of more than one variable. Deﬁning creation and annihilatio n operators
on each sort of element would let us deﬁne a Weyl algebra for n sorts of particles
- that is, the algebra of operators for n quantum harmonic oscillators. This is
interesting, since a quantum ﬁeld theory may be represented as a c ollection of
harmonic oscillators.
Replacing the various sorts of ﬁnite sets with ﬁnite sets over monoid s - in particu-
lar, over U (1), as in our discussion of U (1)-stuﬀ types - we may ﬁnd an elementary
categorical description of a simple QFT. Further research in this dir ection may
prove fruitful.
7.2.3. Beyond FinSet0. We have described the 2-Hilbert space of categoriﬁed states
(stuﬀ types) and 2-algebra of operators (stuﬀ operators) for the categoriﬁed quan-
tum harmonic oscillator in terms of some over categories. The 2-cat egory StuﬀTypes
is the slice category of Gpd over the groupoid FinSet0, while the 2-category
StuﬀOps is the slice category of Gpd over FinSet0
2.
The groupoid FinSet0 appears in both of these cases, in the fact that it does
allows stuﬀ operators to act on stuﬀ types by means of pullbacks. B ut the 2-Hilbert
space structure of StuﬀTypes does not depend on the fact that the groupoid it
lies over is FinSet0: the linear structure is inherited entirely from the direct sums
of groupoids, and the inner product depends only on the fact that any two stuﬀ
types Ψ and Φ are groupoids over the same groupoid G, and thus that we can ﬁnd
a groupoid⟨Ψ, Φ⟩ by taking a weak pullback over G.
Similarly, the algebraic properties of StuﬀOps - its linear structure, composi-
tion, and action on StuﬀTypes - derive from Gpd and the possibility of forming
pullbacks. We could derive the same structures for the 2-categor y of groupoids over
60 JEFFREY MORTON
G2 for any groupoid G. What’s more, just as not all matrices need to be square,
and linear transformations needn’t be endofunctions on some single vectorspace, we
could take two diﬀerent groupoids G and G’, and take the 2-category of groupoids
over G× G’. We could compose these in the obvious way, treating them as “span s”
between G and G’ - and also as functors between categories of groupoids over G
and G’ just as stuﬀ operators are endofunctors of groupoids over FinSet0.
Why did we choose the speciﬁc groupoid FinSet0 (or its M -coloured counter-
part) for the constructions we actually studied? Because its deca tegoriﬁcation is /C6 ,
which is the spectrum of the number operator for the quantum har monic oscilla-
tor. This may suggest how to ﬁnd other groupoids G for which these constructions
have some particular physical interest. Indeed, as remarked bef ore, Kelly’s theory
of “clubs” ([8]) generalizes our framework by, among other things, allowing cate-
gories which are not groupoids. Perhaps phenomena related to gro upoids can be
found which can be given a treatment like the one we have given for th e oscillator.
