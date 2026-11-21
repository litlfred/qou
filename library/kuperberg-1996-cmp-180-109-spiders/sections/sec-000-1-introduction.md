---
doc_id: kuperberg-1996-cmp-180-109-spiders
doc_title: "Spiders for Rank 2 Lie Algebras"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-13
source_pdf: kuperberg-1996-cmp-180-109-spiders.pdf
source_sha256: b6c94630554cc15a
toc_source: inferred
doc_brief: "Spiders for Rank 2 Lie Algebras — A spider is an axiomatization of the representation theory of a group, quantum group, Lie algebra, or other group or group-like object."
---
One of the problems of classical invariant theory is to characterize, for all ^-tuples
V\,...,Vn of finite-dimensional, irreducible representations over C of a compact
group G or simple Lie algebra g, the vector space of multilinear functions
/ : Vι x V2 x 
x Vn -> <C
which are invariant under the action of G or cj. In more modern terminology, the
problem is to characterize the dual vector space of invariant tensors
or just Inv(F) if V is a tensor product of irreducibles. (Also, instead of working over
C, one might work over some other field F of characteristic 0.) Of course, for a
simple Lie algebra cj, the dimension of such a vector space is given by Cartan-Weyl
The author was supported by an NSF Postdoctoral Fellowship, grant #DMS-9107908
110 
G Kuperberg
character theory. But it is also useful to consider operations on invariant spaces such
as tensor products and contractions. Even for finite-dimensional, simple Lie algebras
over <C, these operations are not completely understood.
Interest in multilinear invariant theory was revived after the discovery of quan-
tum groups. A quantum Lie group is a non-commutative, non-cocommutative Hopf
algebra Uq(c$) which is a deformation of the universal enveloping algebra £/(g).
The representation theory of a quantum group is just as important as the quantum
group itself and may also be defined using loop groups or conformal quantum field
theory. Among other uses of quantum groups, a quantum invariant of a tangle takes
a vector in an invariant space Inv(K), where V depends on the boundary of the
tangle and other data.
Because of non-cocommutativity, the switching map
τ : K® W ^ W ® V
given by
X ® y f—• y ® x
is in general not an (equivariant) map between quantum group representations. Thus,
there is no natural symmetric group action on invariant spaces with n tensor factors
with n > 2. (There is often a braid group action.) However, the following operations
exist and are natural:
1. Tensor product:
Inv(F) ® Inv(W) --> Inv(K ® W) ,
2. Cyclic permutation:
Inv(F® Jr)->Inv(Jr® K),
3. Contraction:
F* ® W) -> \n\(W).
Since V and W may themselves be tensor products, cyclic permutation of two
tensor factors yields cyclic permutation of n tensor factors, but not general permuta-
tions. Also, contraction must be interpreted carefully, because in a quantum group,
one must reverse order when taking duals: (V ® W)* = P 
0 F*.
A spider is an abstraction of a representation theory with these three operations.
It is a collection of vector spaces, or perhaps modules or sets, to be thought of as
invariant spaces, together with abstract operations called join, rotation, and stitch,
to be thought of as tensor product, cyclic permutation, and contraction. It is both
convenient and conceptually important to depict these operations with certain planar
graphs. These graphs are called webs, hence the term "spider."
Another motivation of the spider operations is that they describe the entire equi-
variant tensor category of representations of a group, Lie algebra, or quantum group.
In general,
the tensor product of two homomorphisms can be defined in terms of tensor prod-
uct and cyclic permutation of invariants, and composition of homomorphisms can
be defined in terms of tensor product and contraction. Contrariwise, the spider
operations can be defined in terms of tensor product and composition of morphisms.
Spiders for Rank 2 Lie Algebras 
111
For this reason, spiders are sometimes defined as a type of (non-symmetric) tensor
category. To construct such a category, one must divide the tensor factors of an
invariant space
Inv(F] <g>...<8> Vn)
into smaller tensor products which serve as the domain and target of a space of mor-
phisms. This involves arbitrary choices that are extraneous to most of the arguments
in this paper, so we will not usually treat spiders as categories.
In this paper, we will define certain spiders in terms of generators and relations,
and we will show that they are isomorphic to the representation theories of rank
two Lie algebras and the quantum deformations of these representation theories.
These results generalize a well-known construction for A\ = sl(2) that first arose in
a paper of Rumer, Teller, and Weyl [18], that was developed later by Temperley and
Lieb [22], and that was greatly developed recently by Jones, Kauffman, Lickorish,
Masbaum, and Vogel [5, 6, 10, 12]. Moreover, Frenkel and Khovanov have recently
established that the bases of invariant spaces that arise when one constructs the A\
spider by generators and relations are dual to the canonical bases of Lusztig [11].
We conjecture that a similar phenomenon holds in the rank 2 cases.
2. The Ax Spider and sl(2, F)
Let V = F
2 be the defining representation of sl(2,F), where F is some field of
characteristic 0. (The complex numbers C are a good choice for F.) Choose a
parameter a e F. Since the vector space V is a self-dual representation, there exists
a non-degenerate, invariant contraction operation σ : V 0 V —> F. For each «, choose
n points on the boundary of a disk in the plane, and let Bn, the set of basis webs,
be the set of crossingless matchings of the n points. For example, if n is odd, Bn
is empty, while B6 has the following 5 elements:
Λ 
7* 
< 
> 
Λ 
7^ 
Λ
By convention, Bo has a single element, the empty disk. Let Wn, the web space,
be the vector space of formal linear combinations of elements of Bn with coeffi-
cients in F.
Theorem 2.1. There exist isomorphisms φn : Wn —> \mr{V®
n).
Theorem 2.1 has few consequences in isolation; it only says that web spaces
have the same dimension as invariant spaces. By the Weyl character formula,
dimlnvίF®") is the number of non-negative lattice paths of length n in one
dimension, and there is a standard combinatorial bijection between such paths and
crossingless matchings. (Idea: Both combinatorial sets are equivalent to balanced
lists of parentheses of length n, such as "(())()" when n = 6.)
112 
G Kuperberg
A rotation operation is the linear extension to a web space of rotation of basis
webs:
A join operation is a bilinear operation on a pair of web spaces. Given two basis
webs, their join is given by connecting their disks by a band:
A join operation extends bilinearly to arbitrary webs. Finally, a stitch operation is
a linear transformation between web spaces. Given a basis web, its stitch at an
adjacent pair of vertices is given by connecting the vertices by an arc:
If the result produces a closed loop, then strictly speaking, it is not a matching of
vertices on the boundary and therefore it is not a basis web. In this case, erase
the closed loop and replace it by a factor of a, the element of F chosen at the
beginning:
The factor of a is a reminder that stitch is a linear operation whose value on a basis
web might be a non-basis web. A stitch also extends linearly from a family of map
Bn -> Wn-2 to a map Wn -+ Wn-2
The combinatorial A\ spider, parameterized by a, is the list of web spaces,
together with all rotation, join, and stitch operations.
Theorem 2.2 (Rumer, Teller, Weyl). If a = —2, then the isomorphisms φn : Wn —»
Inv(Ύ®
n) can be uniquely chosen to send the operations of join to tensor product,
stitch to contraction, and rotation to cyclic permutation of tensor factors composed
with negation.
Spiders for Rank 2 Lie Algebras
113
(The difference in sign between rotation and cyclic permutation of tensor factors
is explained in Sect. 3.)
The conversion of join to tensor product requires some explanation. Tensor prod-
ucts depend on a linear ordering of tensor factors, but the vertices in a web are only
cyclically ordered. To realize an explicit association between webs and invariant ten-
sors, it is necessary to refine the cyclic ordering to a linear ordering. Then join or
tensor product becomes a process of concatenation:
1 J
o i n
The general operation of join corresponds to tensor product modified by cyclic
permutations.
We explicitly construct the φn's to demonstrate their uniqueness. Assume some
non-zero value r 6 V (g) V for ή>2 of a line segment:
r 
- \
i 
i 
I 
= ,
Any other basis web is obtained from a line segment by repeated joins. Therefore
its image under φn is, up to sign, a combination of cyclic permutations and tensor
products of r's. For example, φ/\ of the basis web
H L./7*-£\-J /
while
where p4 is cyclic permutation of four tensor factors. It remains only to determine
r. The stitch of two arcs is one arc:
Applying φ^ and φι to the two sides yields
r) =
114 
G Kuperberg
This equation says that r is the inverse of σ in an indirect sense. More explicitly,
given a basis {ei,e 2} for F, one natural choice for r and σ is:
0 e\) = σ(e2 0 e2) = 0 ,
— £2 '
But in a more direct sense, r is not the inverse of σ, because with this choice of r
and σ, as with every other compatible pair of choices, a closed loop, or σ(r\ is —2.
Checking that the φn's take spider operations to tensor operations reduces to
comparing definitions and simple calculations. The least trivial part of Theorem 2.2
is the assertion that each φn is an isomorphism. Since the domain and target of φn
have the same dimension, it suffices to establish surjectivity. To prove surjectivity,
we use the isomorphism
By the Fundamental Theorem of Invariant Theory of Schur and Weyl, the endomor-
phisms of V®
n are spanned by permutations of tensor factors. Such a permutation
can be depicted by a diagram of matched dots:
It is a composition of many copies of the switching map τ:x<g>y\-^y(&x 
in
End(F 0 F). A calculation demonstrates that τ lies in the image of φ$\
• = 
] ( I
' 
v V
It follows by multilinear expansion that every permutation is in the image of φin
Since the permutations span, φ2n is surjective.
What if a is not —2? The specialization of the spider should describe the repre-
sentation theory of some object related to sl(2, F). The quantum group Uq(sl(2, F))
was invented essentially for this purpose. One parameterization of the A\ spider is
a — —q
χl
2 — q~
x/1 over the field <C(q,q
ι/
2,q
1/
3,...). 
(Note, however, that the spider
is actually defined over the ring <b[q,q~
ι,q
ι/
2,q
1/
3,...], which allows us to spe-
cialize to any value of q G C*.) Another standard notation is a = —[2], where, by
definition,
W- 
qiβ_q-\l2 
'
2.1. Computations with the A\ spider. A basis web, or crossingless matching, is an
equivalence class, modulo boundary-fixing isotopies, of proper embeddings in the
disk of a 1-manifold with no circles. Although proper embeddings of loop-free
1-manifolds suffice to define the web space Wn, it is convenient to define any
properly embedded 1-manifold in the disk as a web. Specifically, a 1-manifold with
Spiders for Rank 2 Lie Algebras
115
n closed loops denotes the web which is a
n times the web obtained by erasing all
closed loops.
Given this meaning for all embedded 1-manifolds, basis webs such as
WΊ 
» = «
can be embedded in larger disks to form 1-manifolds which are therefore other
webs:
= a
(1)
If the Wi's are arbitrary webs, then a diagram such as the one in Eq. (1) denotes a
multilinear expansion and is called a compound web. For example, if
ί'w) = 2[) (j +3{*
then
Another view of a compound web is that it is a sequence of joins and stitches of
the component webs. It can be realized by many different such sequences, but they
all have the same final value.
116 
G Kuperberg
An important class of examples of compound webs are those generated by a
web called a crossing:
•:X: =-<
Given this definition, it is easy to check the identities
These are known as the second and third Reίdemeister moves. In particular, a clever
trick due to Kauffman [6], namely replacing one of the crossings in the third move
by its linear expansion, reduces the third move to the second one. If we interpret
a compound web made from copies of a crossing as a tangle or link projection,
the identities are also known as the second and third Reidemeister moves. More
generally, a projection of a tangle or link such as
evaluates to a vector in some web space. The value of a link projection lies in
Wo, a 1-dimensional vector space with basis the empty web. Its single coeffi-
cient is a Laurent polynomial in q
χl
A. Given invariance under the second and third
Reidemeister moves, this function on link projections is a regular isotopy invariant.
It is also covarίant under full isotopy; it gains a factor of #
± 3 / 4 under the first
Reidemeister move:
3/4*
= 
fl 
«
(Since Wι is 1-dimensional, these two webs must be proportional.) This polynomial
is known as the Kauffman bracket, and up to normalization it equals the Jones
polynomial.
Another important type of compound web is a concatenation of two webs. Given
a web in Wa+b, divide its endpoints into a segment of a points and a segment of
Spiders for Rank 2 Lie Algebras
117
b points. Given another web in Wb+C whose vertices are divided into segments of
length b and c, their concatenation consists of connecting b adjacent pairs:
w2
With concatenation operations, the A\ spider can be understood as a category, iso-
morphic to a subcategory of the (quantum) representation category of sl(2, F), whose
objects are segments of points and whose arrows are webs. For fixed n, the endo-
morphisms of the object consisting of n points form an associative algebra, called
the Temperley-Lieb 
algebra. As a unital algebra, it is generated by 
e\,...9en-ι,
where β[ is a basis web which is a pair of U-turns at the /
th and / + 1
st positions:
e. =
C
It is easy to show that
is a complete set of relations for the Temperley-Lieb algebra.
2.2. Other representations <?/sl(2, F). So far, we have only described Inv(F®
w)
and not
for arbitrary irreducible representations A\,...,Ak 
of sl(2,F). The Lie algebra
sl(2, F) has an irreducible representation Vn of dimension n + 1 for every non-
negative n, and any finite-dimensional irreducible is isomorphic to one of these.
The representation Vn can be viewed as the n
th symmetric power of V, in which
case the equivariant contraction σ induces an equivariant contraction
On : Vn 0 Vn -> C .
It is determined by the rule that
σn(v
n ®w
n) = σ(v®wf 
.
Given positive integers «i,...,«£ with sum n, consider a circle with n distinguished
points, partitioned into consecutive strings of points of length «i,«2,...,«A: Each
118
G Kuperberg
string of points is called an external clasp. The clasped web space 
W(n\,...,nk)
is a vector subspace of the web space Wn, defined as the span of those basis webs
of with no U-turns between two endpoints in the same clasp. The set of such basis
webs is denoted B(n\,...,nk). 
For example, the web
is not a basis web of PF(2,3,4,5), which instead has basis
Like a web with closed loops, a clasped web with £/-turns has a meaning as a web,
but not a basis web. If there are any U-turns, the clasped web is defined to be the
zero web. Thus, W(n\,. ..,rik) is also a quotient space of Wn.
Theorem 2.3. Let N = (n\,...,nk) 
be a multi-index, 
with
When q—\, there is a family of vector space isomorphisms
φN: 
W(N)-+Ίnv(VN)
that send join to tensor product, stitch to contraction, and rotation to cyclic per-
mutation of tensor factors up to sign.
Rotation and join of clasped webs are defined in the same way as for unclasped
webs, but stitch is more complicated. Given a clasped web with two adjacent external
clasps of the same size, the stitch of the web is obtained by identifying the two
clasps and introducing an internal clasp, usually depicted as a box:
Spiders for Rank 2 Lie Algebras 
119
An internal clasp of size n is a particular web in Win that satisfies the axioms
H-0—D-- -IT.
= 0
-k-2
Equation (2.2) uses the convention that a strand labelled by n denotes n parallel
strands. The equation says that an internal clasp is an idempotent of the w-strand
Temperley-Lieb algebra and it annihilates all basis webs other than the identity on
the right. Therefore a clasp concatenated with any web is proportional to a clasp. In
particular, a clasp is unique, if it exists, and it has the same annihilation property
on the left. The Wenzl recursion formula [24] demonstrates that clasps do exist, at
least for most values of q\
n-\
n 
n-\
4-4=
[n-1]
[n]
n-2
n-\
n-\
Internal clasps are also called magic weaving elements [7], boxes [10], and Jones-
Wenzl ίdempotents [12].
An internal clasp is the concatenation of the unique basis web of W(n, 1,1,
!,...,!) with itself:
In terms of representations, this concatenation is a composition of the form
y(&n 
y y 
> y<8>n
Since the composition is a non-zero idempotent, it is the equivariant projection from
V®
n to its highest-weight irreducible summand.
2.3. Isomorphism and equίnumeration. In this section, we prove Theorem 2.3. It is
fairly easy to construct each φN and to prove that is surjective. If n = n\ -\ 
h «£,
there is a projection
and let ΦN = KN ° Φn ° *V> where i^ is the inclusion W(N) C Wn. Suppose that
the /
th clasp of a web w has k tZ-turns, and let m = n — 2k. Then the invariant
KN ° Φn(
w) li
e s in the image of some map which has a tensor factor of the form
V®
m —> Vnn where m < ni9 and any such map must be zero.
Thus, %N ° φn = ΦN °J'N, where j ^ is the projection Wn —> W{N). From this,
it is routine to show that the maps φN take spider operations to spider operations.
Moreover, each φ^ is surjective, because both π^ and φn are surjective and ίn
complements the kernel of πN o φn.
120 
G Kuperberg
We complete the proof that φN is an isomorphism by demonstrating that its
domain and target have the same dimension, thereby generalizing Theorem 2.1 to
the clasped case:
Theorem 2.4. If N is a multi-index, then
dim W(N) = 
άimlrw(VN).
Proof. The proof is by induction on \N\, the number of indices in N. The relation
is straightforward for \N\ ^ 2 , so we first assume that \N\ = 3.
The Clebsch-Gordan theorem states that
dimInv(F; <g> Vj ® Vk) = 1
if each of n, rn, and / is less than or equal to the sum of the other two and if the
sum of all three is even, and
dimInv(F; <8> Fy <g> Vk) = 0
otherwise. On the other hand, B(i,j,k) has at most one element:
This web exists when there are non-negative integers x, y, and z such that i = x + y,
j = x + z, and k = y + z. These two conditions on /, j , and A: are equivalent.
Now suppose that \N\ > 3 and express the multi-index N as JK, where / and K
each have length at least 2. Since the Vn's constitute all finite-dimensional irreducible
representations, and since they are self-dual, there is a decomposition
lnv(Vj ® Vκ) = 0Inv(Fj 0 V{) 0 Inv(F/ ® K^) ,
/
where / is a single index rather than a multi-index. It suffices to establish a bijection
f : B(J,K) ^ \J (B(J,l) x B(
I
where the union is disjoint. The bijection / is very easy to define: A basis web of
w G W(JK) has a minimal cut path, where a cut path is a path whose endpoints
separate J from K. A cut path is minimal if it crosses as few strands as possible:
Let w\ and W2 be the two resulting webs. The cut path crosses some / strands, and
since it is minimal, there can be no U-turns among the / strands in either wi or H>2.
Spiders for Rank 2 Lie Algebras 
121
Thus, the relation f(w) — (w\,W2) defines the desired map /. It is routine to check
that / is both injective and surjective. 
D
Note that minimal cut paths are also useful in practice for generating the basis
of a clasped web space.
Exercise 2.5. List the elements of 5(2,2,2,2,2).
3. Precise Definition of a Spider
In this section, we give a precise definition of a spider. The main way in which
the general notion of a spider is more complicated than the example is that strands
may be oriented and there may be more than one type of strand. Indeed, even in
the A\ case, we may consider n parallel strands as equivalent to one strand labelled
with n, as is already suggested by the notation.
A spider has a strand set S which is a unital semigroup with unit 0. In most
of the examples in the paper, S is a free, non-abelian semigroup. The strand set
has an anti-involution * : S —> S called duality or orientation reversal. For each
s (Ξ S, there is a web space W(s), which may be just a set. For each α, there is
a distinguished web βa G W(aa*), called a bare strand, and 1 = β$ is called the
empty web. Finally, there are three operations that exist for every a and b:
1. Join ^a,b 
W(ά) x W{b) -> W{ab).
2. Rotation pa b : W(ab) -> W(ba).
3. Stitch σa,b :' W{aa*b) -> W{b).
The subscripts of the operations may be dropped when they are clear from context.
A spider may in addition be defined in a (symmetric tensor) category other than
the category of sets. For example, an additive spider is one in which web spaces
are abelian groups, rotation and stitch are additive, and join is additive, while in
a linear spider, the web spaces are vector spaces and the operations are linear or
bilinear.
The three spider operations must satisfy the following axioms, which are
divided into groups according to which operations they involve. We define σb,a,c =
Pc,b
σa,cbPb,aa*c f°
r brevity in the last three axioms.
• Rotation only:
l Pα,0 = Pφ,a = id.
2. pa,bcPc,abPb,ca = id.
