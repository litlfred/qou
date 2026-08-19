---
doc_id: deligne-mostow-1986
doc_title: ""
section_id: sec-017-8-extending-s-by-continuity
section_title: "Extending S^ by continuity"
section_number: 8
pages: 38-42
source_pdf: deligne-mostow-1986.pdf
source_sha256: d9850f70ab2fecbd
doc_brief: "PUBLICATIONS MATHÉMATIQUES DE L ’I.H.É.S. PIERRE DELIGNE G. D. MOSTOW — 27 sections: P. DELIGNE AND G. D. MOSTOW; P. DELIGNE AND G. D. MOSTOW; Cohomology of a rank one local sys"
---
Let X, Y be complex algebraic varieties which are separated as algebraic varieties,
i.e. which are Hausdorff in their complex topology.
(8.1) One knows that any quasi-finite map /: X ->Y—i.e. a map whose fibers
are finite—admits a factorization X <^ X -^ Y, with j an open embedding, and / a
finite map (== quasi-finite and proper). If X and Y are connected and normal, of the
same dimension, there is an unique such factorization for which X is normal. One calls
this X the normalization of Y in X.
For more general spaces, and for some maps with totally disconnected but possibly
infinite fibers, a simple topological generalization of this construction has been given
by R. H. Fox [7].
The spaces X and Y are taken to be Hausdorff and locally connected. A conti-
nuous map /: X ->Y is called a spread if, for any x in X, one obtains a fundamental
system of neighborhoods ofx by taking, for each neighborhood V of f{x), the connected
component of/'^V) containing x. A spread/is called complete if, for any y e Y,
/-^^projiim^/-1^)),
the projective limit being taken on the neighborhoods V ofj\
^ Fox proves that each spread /: X ->Y can be embedded in a complete spread
/: X -> Y with the following universal property: any commutative diagram of solid
arrows
X -----^ X'
\-^(8.1.1) f I r
Y ———-Y'
41
6
42 P.DELIGNEANDG.D.MOSTOW
withy a complete spread, can be completed as shown. For any y eY, one has
/-^^projiim^/-1^)),
the projective limit being taken on the neighborhoods V ofy. It is clear from the uni-
versal property that X is unique up to unique isomorphism, and functorial. We will
call it the completion of X over Y. It contains X as a dense subspace, and the topology
of X is induced by that of X. The space X is locally connected.
(8.2) We define a space X to be connected if it is non-empty and has no proper open
and closed subset.
A map y:X->Y is called a covering map if each y e Y has a neighborhood V for
which there exists a discrete set D (possibly empty), and a commutative diagram
<p-i(V) ^^ VxD
\ /-
V
If Y is connected and X non-empty, such a map is onto.
A map y:X->Y is called a local homeomorphism at x e X if A: has a neighborhood U
which maps homeomorphically onto a neighborhood off{x). The map y is called a
local homeomorphism if this holds at all points x e X.
Assume that X is a connected covering space of a connected locally simply connected
open subset U of Y. The composed map X -> U <->- Y is then a spread. Assume
further that eachj» in Y has a fundamental system i^y of open neighborhoods such that
(8.2.1) for V in Vy, V n U is connected;
(8.2.2) for V'CV" in ^, ^(V n U) ^ ^(V" n U).
As^is a local homeomorphism, X is open in X. As X is a covering ofU, one has
further X^J-^U).
Fix a base point o e U. One knows that the functor {g: U -> U) i-^"1^)
is an equivalence of the category of coverings of U with that of discrete sets on which
7Ti(U, o) acts. In particular, the connected components of U correspond to the orbits
of7Ti(U, o) on ,§^~l(o). For W open in U, connected and containing o, the same applies
to W and the restriction functor {g : U —> U) H- QT^W) -> W) from coverings of U to
coverings of W corresponds to the functor: restriction of the action of 71:1 (U, o) to 7ri(W, o).
In particular, ifU corresponds to 7Ci(U, o)/K, ^Q^W) is 7ri(W, o)\7Ti(U, o)/K.
This applies to X. If a lifting 7ofo is chosen in X, the map 7Ci(U, o)—^/''"1^) :(5\->a.^
identifies y"'1^) with a suitable homogeneous space 7ri(U, o)/K of7Ti(U, o).
Fix j^eY, and a neighborhood V e Vy. Let us assume at first that o e V.
The decomposition group Dy is then defined as the image of TT^V n U, o) in 7ri(U, o) and
one has
^(/-'(V n U)) = D,WU, .)/K.
42
MONODROMY OF HYPERGEOMETRIC FUNCTIONS 43
For V'CV in V^, (8.2.1) and (8.2.2) imply that ^(/-'(V'n U))-^ ^(/-'(V n U))
hence
(8.2.3) /-^^WU^/K.
For G e TCi(U, o)/K, cs.V is a lifting of o in the connected component /"^(V) 3 of
/"^(V) corresponding to the double coset Dy crK. If we use it as a base point, the fibre at
o of the covering/-^V)^ of V n U is identified with Dy aK/K == Dy/Dy n aKa-1. To
the component/" ^V)^ there corresponds a point J in/"1^). The /"^(V)^ O/'^V),
for V a neighborhood ofj/, are the trace on X of a fundamental system of neighborhood
of y in X.
For o not necessarily in V, one chooses o' in V e U and a path p from o to o' in U.
This path lifts as a path from 7 to some lifting y et o'. It defines an isomorphism
of 7Ti(U, o) with 7Ti(U, o') via which the above constructions, which make sense for o',
can be pushed back into ^(U, o). For instance, the decomposition group Dy C T^(U, o)
is defined as the image of the decomposition group Dy C 7^(U, o'). It depends on the
path p. One still has (8.2.3).
(8.2.4) A covering map /: X —" U is normal if the ^(U, o) homogeneous space
y^o) is isomorphic to a homogeneous spaces 7Ti(U, o)/K, with K a normal subgroup.
If /: X -> U is a normal covering map, the group ^(U, o) acts on X by deck-trans-
formations, and this action extends to X by functoriality. We leave to the reader to
check that, under the conditions (8.2.1), (8.2.2), one has
1) ^(U,.)\X^Y;
2) for each y e Y, the stabilizer in T^(U, o) of a point 3^ in y"1^) is the conjugate of the
decomposition groiip Dy determined by a path in U corresponding to y.
Remark. — Let K denote the kernel of the action of7i;i(U, o) on X. Then T^(U, o)/K
acts properly discontinuously on X but not necessarily on X.
(8.3) Let w be a continuous function from X to a topological space B. We
assume B regular, i.e. that any neighborhood of any point contains a closed neighborhood.
The function w then extends as a continuous function on X if and only if, for any ^ e X,
w{x) has a limit for x -> x in X (convergence ofw on the filter of traces on X of neighbor-
hoods of x in X).
In the situation (8.2) (with o e V for simplicity), one can treat w as a multivalued
function on U. Ifxinf'1^) corresponds to the connected component/"1 (V)^ of/""!^),
the restriction of w ^/"^(V^ is a multivalued function Wy on V n U. That w{x) has
a limit for x -> x means that there is b in B, and for each neighborhood W of b a neigh-
borhood V ofy, sach that all determinations of Wy{u), for u e V n U, are in W.
Example (8.4). — If we take for Y the unit disk D C C, for U the punctured unit
disk D* and for X the universal covering of D*, the completion of X over D is deduced
43
44 P. DELIGNE AND G. D. MOSTOW
from X by adding one point above o : X = X u {o}. For X real > o, the function ^
has a limit for z -> o in X, but it has no limit for non real \ with 8S\ > o. Similarly
z. log z has no limit.
(8.5) With the assumptions (8.2.1) and (8.2.2) on (Y, U), let 3S be the flat
fiber space on U defined by an action 6 of 7i:i(U, o) on a regular topological space B,
and let (X, o) be the smallest covering of (U, o) on which 3S becomes trivial: one has
/-^o) = ^(U, o)/Ker(6). A continuous section w of 88 defines by pull-back to X an
equivariant continuous map from X to B (and conversely). We write w for this map.
When does it extend to X? Unravelling (8.3)3 we find that w has a limit for x ->y
above y if and only if there is a horizontal section h of 88 over the trace on U of a neigh-
borhood V e V^ ofjy, toward which w converges for y1 ->y (y e U), in the following
sense. For y^ e V n U and Wi a neighborhood of b{y^ in the fibre 88^ of 38 at y^,
there is a neighborhood V ofy such that for any y^ e V n U, and for Wg a neighborhood
ofb{y^) in the fiber of. 88 at j^? obtained by horizontal transport ofW^ along any path
in V n U fromj^ toj/a, one has w{y^) e W2. This holds if b has a system of horizontal
neighborhoods W which are fiber arbitrarily small, such that w(j^) is in W for y^ close
enough to y. Of course, b defines the limit of w.
In the rest of section 8, the notation and assumptions (4.0) as well as the assumption N ^ 4
are in force.
(8.6) As in (3.8), fix a base point o e Q^, and let p : (C[, o) -> (Q, o) be the
smallest covering of (Q, o) on which the flat projective space bundle B(a)o becomes
trivial. For QC Y C Q^ and Y open in Q^, the composed map Cl-^Y is a
spread. We will write Y for the completion of Q^over Y. The assumptions (8.2.1)
and (8.2.2) are satisfied by (Y, QJ.
It follows from (8.2.4) that
(8.6.1) ^i(Q,,o) acts on CLsu
(8.6.2) ^l(Q^)\^sst = Qsst.
Proposition (8.7). — The map S^ of (3.8) extends as a continuous map from C[^ to
the closed ball B(a)^, provided with the topology (5.4). The inverse image ofB{(x.)^ consists of
the stable points,
Proof. — We are in the situation envisioned in (8.5), if we take for 88 the flat
fiber space with fiber B(a)^, completing B(a)^. That the extendability criterion of (8.6)
applies is (6.8) forjy stable and (7.3) forjy semi-stable. Further, the limit occuring in
criterion (8.5) lies in ^B(a)^ if and only \fy is in Q^usp-
The extended map C[^ -> B(a),4- is also denoted S^. It is TT^Q, o)-equivariant.
44
MONODROMY OF HYPERGEOMETRIC FUNCTIONS 45
(8.8) For T a stable partition ofS (cf. (6.9)), the system of the Q^ , for T' finer
than T, is topologically constant along Q^, and the inverse image C^T of Q,T in CLt
is hence a covering of Q,T(- d(T)). By (6.9), on each connected component ^
of^T?th^ Sat ball bundle B(a(T))+ trivializes, and can be identified with a flat sub-ball
bundle of the constant bundle B(a)o4', in such a way that
(8.8.1) ^D^JO^
From (3.9), we hence get:
Proposition (8.9). — For any component Q^ off^y, w^ \ ^ is an etale map from ^
to a sub-ball o/B(a)^.
