---
doc_id: arxiv-math-0511710v2
doc_title: "Higher gauge theory"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-8
source_pdf: 0511710v2.pdf
source_sha256: f88f50d459080490
doc_brief: "Higher gauge theory — Just as gauge theory describes the parallel transport of poi nt particles using connections on bundles, higher gauge theory describe s the parallel transport of 1-dimensional"
---
Ordinary gauge theory describes how 0-dimensional particl es transform as we
move them along 1-dimensional paths. It is natural to assign a group element
1
to each path:
•
g
/d37/d37 •
The reason is that composition of paths then corresponds to m ultiplication in
the group:
•
g
/d37/d37 •
g′
/d37/d37 •
while reversing the direction of a path corresponds to takin g inverses:
• •
g−1
/d121/d121
and the associative law makes the holonomy along a triple com posite unam-
biguous:
•
g
/d37/d37 •
g′
/d37/d37 •
g′′
/d37/d37 •
In short, the topology dictates the algebra!
Now suppose we wish to do something similar for 1-dimensiona l ‘strings’
that trace out 2-dimensional surfaces as they move. Naively we might wish our
holonomy to assign a group element to each surface like this:
• /d37/d37/d57/d57g
/d11/d19 •
There are two obvious ways to compose surfaces of this sort, v ertically:
• /d27/d27/d47/d47
g
/d11/d19
/d67/d67
g′
/d11/d19
•
and horizontally:
• /d37/d37/d57/d57g
/d11/d19 • /d37/d37/d57/d57g′
/d11/d19 •
Suppose that both of these correspond to multiplication in t he group G. Then
to obtain a well-deﬁned holonomy for this surface regardles s of whether we do
vertical or horizontal composition ﬁrst:
• /d27/d27/d47/d47
g1
/d11/d19
/d67/d67
g′
1
/d11/d19
• /d27/d27/d47/d47
g2
/d11/d19
/d67/d67
g′
2
/d11/d19
•
2
we must have
(g1g2)(g′
1g′
2) = ( g1g′
1)(g2g′
2).
This forces G to be abelian!
In fact, this argument goes back to a classic paper by Eckmann and Hilton
[1]. They showed that even if we allow G to be equipped with two products, say
gg ′ for vertical composition and g ◦ g′ for horizontal, so long as both products
share the same unit and satisfy this ‘ interchange law’:
(g1g′
1) ◦ (g2g′
2) = ( g1 ◦ g2)(g′
1 ◦ g′
2)
then in fact they must agree — so by the previous argument, bot h are abelian.
The proof is very easy:
g ◦ g′ = (g1) ◦ (1g′) = ( g ◦ 1)(1 ◦ g′) = gg ′
Pursuing this approach, we would ultimately reach the theor y of connections
on abelian gerbes [2-8]. If G = U(1), such a connection can be locally identiﬁed
with a 2-form — but globally it is a subtler object, just as a co nnection on
a U(1) bundle can be locally identiﬁed with a 1-form, but not g lobally. In
fact, connections on abelian gerbes play an important role i n string theory [9-
11]. Just as ordinary electromagnetism is described by a con nection on a U(1)
bundle, usually called the ‘vector potential’ and denoted A, the stringy analogue
of electromagnetism is described by a connection on a U(1) ge rbe, called the B
ﬁeld.
To go beyond this and develop a theory of nonabelian higher gauge ﬁelds,
we must let the topology dictate the algebra. Readers famili ar with higher
categories will already have noticed that 1-dimensional pi ctures above resemble
diagrams in category theory, while the 2-dimensional pictu res resemble diagrams
in 2-category theory. This suggests that the holonomies in h igher gauge theory
should take values in some ‘categoriﬁed’ analogue of a Lie gr oup — that is, some
gadget resembling a Lie group, but which is a category rather than a set. We
call this ‘Lie 2-group’.
In fact, Lie 2-groups and their Lie 2-algebras have already b een studied [12,
13] and interesting examples have been constructed using th e mathematics of
string theory: central extensions of loop groups [14]. But e ven without knowing
this, we could be led to the deﬁnition of a Lie 2-group by consi dering a kind of
connection that gives holonomies both for paths and for surfaces .
So, let us assume that for each path we have a holonomy taking v alues in
some Lie group G, where composition of paths corresponds to multiplication in
G. Assume also that for each 1-parameter family of paths with ﬁ xed endpoints
we have a holonomy taking values in some other Lie group H, where vertical
composition corresponds to multiplication in H:
• /d27/d27/d47/d47
h
/d11/d19
/d67/d67
h′
/d11/d19
•
3
Next, assume that we can parallel transport an element g ∈ G along a 1-
parameter family of paths to get a new element g′ ∈ G:
•
g
/d37/d37
g′
/d57/d57h
/d11/d19 •
This picture suggests that we should think of h as a kind of ‘arrow’ or ‘morphism’
going from g to g′. We can use categories to formalize this. In category theory ,
when a morphism goes from an object x to an object y, we think of the morphism
as determining both its source x and its target y. The group element h does
not determine g or g′. However, the pair ( g, h) does.
For this reason, it is useful to create a category G where the set of objects,
say Ob(G), is just G, while the set of morphisms, say Mor( G), consists of ordered
pairs f = (g, h) ∈ G × H. Switching our notation to reﬂect this, we rewrite the
above picture as
•
g
/d37/d37
g′
/d57/d57f
/d11/d19 •
and write f : g → g′ for short.
In this new notation, we can vertically compose f : g → g′ and f ′: g′ → g′′ to
get f f′: g → g′′, as follows:
•
g
/d27/d27g′
/d47/d47
f
/d11/d19
g′′
/d67/d67
f ′
/d11/d19
•
This is just composition of morphisms in the category G. However, we can also
horizontally compose f1: g1 → g′
1 and f2: g2 → g′
2 to get f1 ◦ f2: g1g2 → g′
1g′
2, as
follows:
•
g1
/d37/d37
g′
1
/d57/d57f1
/d11/d19 •
g2
/d37/d37
g′
2
/d57/d57f2
/d11/d19 •
We assume this operation makes Mor( G) into a group with the pair (1 , 1) ∈
G × H as its multiplicative unit.
The good news is that now we can assume an interchange law sayi ng this
4
holonomy is well-deﬁned:
•
g1
/d27/d27g2 /d47/d47
f1
/d11/d19
g3
/d67/d67
f ′
1
/d11/d19
•
g′
1
/d27/d27g′
2 /d47/d47
f2
/d11/d19
g′
3
/d67/d67
f ′
2
/d11/d19
•
namely:
(f1f ′
1) ◦ (f2f ′
2) = ( f1 ◦ f2)(f ′
1 ◦ f ′
2)
without forcing either G or H to be abelian! Instead, the group Mor( G) is forced
to be a semidirect product of G and H.
The structure we are rather roughly describing here turns ou t to be none
other than a ‘Lie 2-group’. This is an ‘internal category’ in the category of Lie
groups. In other words, it is a category where the set of objec ts is a Lie group,
the set of morphisms is a Lie group, and all the usual category operations are
Lie group homomorphisms.
This audacious process — taking a familiar mathematical con cept deﬁned
using sets and function and transplanting it to live within s ome other category
— is far from new. For example, a Lie group is a group in Diﬀ, the category of
smooth manifolds and smooth maps. The general idea of an ‘int ernal category’
living within some other category was described by Charles E hresmann [15] in
the early 1960’s. In the next section we begin by reviewing th is idea. In the
rest of the paper, we use it to categorify the theory of Lie gro ups, Lie algebras,
bundles and connections. Before we proceed, let us sketch ou r overall plan.
The starting point is the ordinary concept of a principal ﬁbe r bundle. Such
a bundle can be speciﬁed using the following ‘gluing data’:
• a base manifold M ,
• a cover of M by open sets {Ui}i∈I ,
• a Lie group G (the ‘gauge group’ or ‘structure group’),
• on each double overlap Uij = Ui ∩ Uj a G-valued function gij,
• such that on triple overlaps the following transition law ho lds:
gijgjk = gik.
Such a bundle is augmented with a connection by specifying:
• in each open set Ui a smooth functor hol i: P1(Ui) → G from the path
groupoid of Ui to the gauge group,
• such that for all paths γ in double overlaps Uij the following transition
law holds:
holi(γ) = gij holj(γ) g−1
ij .
5
Here the ‘path groupoid’ P1(M ) of a manifold M has points of M as objects
and certain equivalence classes of smooth paths in M as morphisms. There are
various ways to work out the technical details and make P1(M ) into a ‘smooth
groupoid’; here we follow the approach of Barrett [16], who u ses ‘thin homotopy
classes’ of paths. Technical details aside, the basic idea i s that a connection
on a trivial G-bundle gives a well-behaved map assigning to each path γ in the
base space the holonomy hol( γ) ∈ G of the connection along that path. Saying
this map is a ‘smooth functor’ means that these holonomies co mpose when we
compose paths, and that the holonomy hol( γ) depends smoothly on the path γ.
A basic goal of higher gauge theory is to categorify all of thi s and to work
out the consequences. As mentioned, the key tool is internal ization. This leads
us immediately to the concept of a Lie 2-group, and also to tha t of a ‘smooth 2-
space’: a category in Diﬀ, or more generally in some category of smooth spaces
that allows for inﬁnite-dimensional examples.
Using these concepts, Bartels [17] has deﬁned a ‘principal 2 -bundle E over
M with structure 2-group G’. To arrive at this deﬁnition, the key steps are to
replace the total space E and base space M of a principal bundle by smooth
2-spaces, and to replace the structure group by a Lie 2-group . In this paper we
only consider the case where M is an ordinary space, which can be regarded as
a 2-space with only identity morphisms. We show that for a sui table choice of
structure 2-group, principal 2-bundles give abelian gerbe s over M . For another
choice, they give nonabelian gerbes. This sets the stage for a result relating
the 2-bundle approach to higher gauge theory to Breen and Mes sing’s approach
based on nonabelian gerbes [18].
Just as a connection on a trivial principal bundle over M gives a functor
from the path groupoid of M to the structure group, one might hope that
a ‘2-connection’ on a trivial principal 2-bundle would deﬁn e a 2-functor from
some sort of ‘path 2-groupoid’ to the structure 2-group. Thi s has already been
conﬁrmed in the context of higher lattice gauge theory [19-2 1]. Thus, the main
issues not yet addressed are those involving diﬀerentiabil ity.
To address these issues, we deﬁne for any smooth space M a smooth 2-
groupoid P2(M ) such that:
• the objects of P2(M ) are points of M : • x
• the morphisms of P2(M ) are thin homotopy classes of smooth paths
γ: [0, 1] → M such that γ(s) is constant in a neighborhood of s = 0
and s = 1: x •
γ
/d39/d39 • y
• the 2-morphisms of P2(M ) are ‘bigons’: that is, thin homotopy classes of
smooth maps Σ: [0 , 1]2 → M such that Σ( s, t) is constant near s = 0 and
s = 1, and independent of t near t = 0 and t = 1: x •
γ 1
/d39/d39
γ 2
/d55/d55 • yΣ
/d11/d19
6
The ‘thin homotopy’ equivalence relation, borrowed from th e work of Mackaay
and Picken [7, 22], guarantees that two maps diﬀering only by a reparametriza-
tion deﬁne the same bigon. This is important because we seek a reparametrization-
invariant notion of surface holonomy .
We deﬁne a ‘2-connection’ on a trivial principal 2-bundle ov er M to be a
smooth 2-functor hol: P2(M ) → G , where G is the structure 2-group. This means
that the 2-connection assigns holonomies both to paths and b igons, independent
of their parametrization, compatible with the standard ope rations of composing
paths and bigons, and depending smoothly on the path or surfa ce in question.
We also deﬁne 2-connections for nontrivial principal 2-bun dles, and state
a theorem obtaining these from Lie-algebra-valued diﬀeren tial forms. We then
show that for a certain class of structure 2-groups, such diﬀ erential forms reduce
to Breen and Messing’s ‘connections on nonabelian gerbes’ [ 18]. The surprise
is that we only obtain connections satisfying a certain cons traint: the ‘fake
curvature’ must vanish!
To understand this, one must recall [12] that a Lie 2-group G amounts to
the same thing as a ‘crossed module’ of Lie groups ( G, H, t, α), where:
• G is the group of objects of G, Ob( G):
• H is the subgroup of Mor( G) consisting of morphisms with source equal
to 1 ∈ G:
• t: H → G is the homomorphism sending each morphism in H to its target,
• α is the action of G as automorphisms of H deﬁned using conjugation in
Mor(G) as follows: α(g)h = 1 gh1g−1.
Diﬀerentiating all this data one obtains a ‘diﬀerential cro ssed module’ (g, h, dt, dα),
which is just another way of talking about a Lie 2-algebra [23 ].
In these terms, a 2-connection on a trivial principal 2-bund le over M with
structure 2-group G consists of a g-valued 1-form A together with an h-valued
2-form B on M . Translated into this framework, Breen and Messing’s ‘fake
curvature’ is the g-valued 2-form
dt(B) + FA,
where FA = dA + A ∧ A is the usual curvature of A. We show that if and
only if the fake curvature vanishes , one obtains a well-deﬁned 2-connection
hol: P2(M ) → G .
The importance of vanishing fake curvature in the framework of lattice gauge
theory was already emphasized by Girelli and Pfeiﬀer [21]. T he special case
where also FA = 0 was studied by Alvarez, Ferreira, Sanchez and Guillen [24 ].
The case where G = H has been studied already by the second author of this
paper [25]. Our result subsumes these cases in a common frame work.
This paper is an introduction to work in progress [23], which began in rudi-
mentary form as an article by the ﬁrst author [26], and overla ps to some extent
with theses by Bartels [17] and the second author [27]. Barte ls’ thesis develops
7
the general theory of 2-bundles. The second author’s thesis investigates the
relationship between nonabelian higher gauge theory and th e physics of strings.
Aschieri, Cantini and Jurˇ co [28, 29] have also studied this subject, using con-
nections on nonabelian gerbes. Other physicists, includin g Chepelev [30] and
Hofman [31], have also studied nonabelian higher gauge ﬁeld s.
