---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-014-51-tropical-polygons
section_title: "Tropical polygons"
section_number: 5.1
pages: 54-60
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
B associated to the aﬃne structure. The following deﬁnitions are due to Abouzaid
[4].
Deﬁnition 7. Let B be a two-dimensional singular aﬃne manifold with focus-focus
singularities, and let x ∈B be a non-singular point. Let Γ be a tree all of whose edges
are ﬁnite. Label one univalent vertex pout, and denote the other univalent vertices
MIRROR OF THE PROJECTIVE PLANE 55
by p1,...,p r. A tropical disk in B ending at x is a balanced tropical embedding
v : Γ →B, satisfying the following conditions.
(1) v(pout) = x,
(2) For i = 1,...,r ,v(pi) is a singular point of the aﬃne structure, and v maps the
(unique) edge incident to pi into a monodromy-invariant line of the singularity.
In the case at hand, there is only one singularity, so the only such tr opical disks
are line segments emanating from the singular point in the monodromy -invariant
direction. If there were more singularities with intersecting monodr omy-invariant
lines, we could obtain more complicated tropical disks.
Deﬁnition 8. Let q0,q 1,...,q k be points of B, with qj ∈B( 1
dj
Z). Let Γ be a metric
ribbon tree with k +1 inﬁnite edges. One inﬁnite edge, the root, is labeled with q0 and
it is the output. The other k inﬁnite edges, the leaves, are labeled with q1,...,q k in
counterclockwise order and these are the inputs. Assign to the re gion between qj and
qj+1 the weight ∑ j
i=1di, and give the region between q0 and q1 weight 0. Orient the
tree upward from the root, so that each edge has a “left” and a “r ight” side coming
from the ribbon structure. To each edge e, assign a weight w′
e given by the weight on
the left side of e minus the weight on the right side of e. Deﬁne a corrected weight
we by
we = 0 if w′
e< 0 and e contains a leaf
we = 0 if w′
e> 0 and e contains the root
we =w′
e otherwise
(98)
Then a tropical polygon modeled on Γ is a map u : Γ →B such that:
(1) u converges on the root edge to q0 and on the j-th leaf edge to qj;
(2) on the edge e, the tangent vector ˙ue to the component ue satisﬁes
(99) ∇ ˙ue ˙ue =we ˙ue
and ˙ue converges to 0 on the inﬁnite ends of the root and leaf edges; this
diﬀerential equation only holds outside a ﬁnite set of points where tr opical
disks are attached;
(3) there exists a ﬁnite collection of tropical disks v1,...,v N such that the union
u ∪ {v1,...,v N } is balanced; the balancing condition at a vertex x is the
vanishing of the sum of the derivative vectors ˙ ue of the various components
ofu incident at x and the integral tangent vectors to vi atx, oriented toward
the vertex.
The heuristic motivation for these deﬁnitions is that, if we consider a deformation
of complex structures in which the torus ﬁbers collapse, we expect that a family of
honest holomorphic polygons will likewise collapse onto a piecewise linear complex in
B. We further expect that two types of local limiting behavior can occ ur. Some parts
of the curve may limit to surfaces that ﬁber over straight lines in B intersecting the
torus ﬁbers in paths joining two Lagrangian sections, while other pa rts may limit to
surfaces that ﬁber over straight lines in B intersecting the torus ﬁbers in circles. The
latter are what become the tropical disks, while the former become the rest of the
tropical polygon. The balancing condition comes from the necessity that these parts
56 JAMES PASCALEFF
can be connected up to form a topological polygon with boundary on the Lagrangian
sections. See also [6, Ch. 8].
To unpack this deﬁnition, let us restate it in the simplest case, which is that of
tropical triangles (this mainly simpliﬁes the issues regarding weights) :
Proposition 5.1. Let q1 ∈ B( 1
n Z) and q2 ∈ B( 1
m Z), with n > 0 and m > 0. Let
q0 ∈ B( 1
n+mZ). Let Γ be the ribbon tree with one vertex and three inﬁnite edges.
Then a tropical triangle modeled on Γ consists of three maps u0 : [0, ∞) → B, u1 :
(−∞, 0] →B, u2 : (−∞, 0] →B such that
(1) u0 ≡q0 is a constant map;
(2) u1(0) = u2(0) = q0;
(3) u1(−∞) = q1, u2(−∞) = q2;
(4) We have ∇ ˙u1 ˙u1 = n ˙u1 and ∇ ˙u2 ˙u2 = m ˙u2, outside of a ﬁnite set of points
where tropical disks are attached;
(5) there exists a ﬁnite collection of tropical disks v1,...,v N such that the balanc-
ing condition holds.
We can also unpack the equation ∇ ˙u ˙u = n ˙u. The key outcome of the following
Lemmas is the insight that the tangent vector ˙ u increases by n times the distance
the path u travels. Recall that a path γ is called a geodesic for a connection ∇ if
∇ ˙γ ˙γ = 0.
Lemma 5.2. Let γ : [0, 1] → B be a geodesic for ∇. Deﬁne u : ( −∞, 0] → B by
u(t) = γ(exp(nt)). Then at the point x =γ(s), we have ˙u =ns ˙γ, and ∇ ˙u ˙u =n ˙u.
Proof. We set s = exp(nt). The equation ˙u = ns ˙γ is just the chain rule (note that
˙u =du/dt while ˙γ =dγ/ds). We have
(100) ∇ ˙γ ˙u = ∇ ˙γ(ns ˙γ) = n ˙γ +ns∇ ˙γ ˙γ =n ˙γ
since γ is a geodesic. Multiplying this equation by ns, and using the fact that ∇ is
tensorial in its subscript, we obtain ∇ ˙u ˙u =n ˙u. □
Lemma 5.3. Let u : [a,b ] → B solve ∇ ˙u ˙u = n ˙u. Then if we patch together aﬃne
charts along u to embed a neighborhood of u into Rn, we have
(101) ˙ u(b) − ˙u(a) = n(u(b) −u(a))
where we use the aﬃne structure of Rn to take diﬀerences of points and vectors at
diﬀerent points.
Proof. Deﬁne γ : [exp( na), exp(nb)] → B by γ(s) = u((logs)/n), so that γ is a
geodesic. We can embed a neighborhood of γ into Rn by patching together aﬃne
coordinate charts along γ. Using addition in this embedding, we can write γ(s) =
γ(exp(na)) + (s − exp(na)) ˙γ. We have ˙u(log(s)/n) = ns ˙γ(s), and
(102)
˙u(b) − ˙u(a) = n(exp(nb) − exp(na)) ˙γ =n(γ(exp(nb)) −γ(exp(na))) = n(u(b) −u(a))
□
One more thing to note regarding these tangent vectors ˙ u is how they represent
homology classes on the torus ﬁbers of the ﬁbration over B.
MIRROR OF THE PROJECTIVE PLANE 57
When considering a tropical curve C trop corresponding to a closed holomorphic
curve C, each edge of the tropical curve carries an integral tangent vec tor, which
morally represents the class [C ∩T 2
b ] ∈H1(T 2
b ; Z) that measures how the holomorphic
curve intersects the torus ﬁber T 2
b =π−1(b). Because the curve is closed, this class is
locally constant along each edge of C trop.
When considering a tropical curve C trop representing a holomorphic curve C with
boundary on Lagrangian sections L(i),L (j), the intersection of C with T 2
b would
morally be a path on T 2
b fromL(i)b toL(j)b, whereL(i)b is intersection ofT 2
b andL(i).
LetA(L(i)b,L (j)b) ⊂H1(T 2
b, {L(i)b,L (j)b}; Z) be the subset consisting of such cycles,
which could also be described as the preimage of L(j)b −L(i)b ∈H0({L(i)b,L (j)b}; Z)
under the boundary homomorphism. Hence A(L(i)b,L (j)b) is a torsor for the kernel
of that homomorphism, which is H1(T 2
b ; Z). Using the group structure on T 2
b , we can
identifyA(L(i)b,L (j)b) with the coset
(103) [ L(j)b −L(i)b] +H1(T 2
b ; Z) ⊂H1(T 2
b ; R)
On the other hand, there is an isomorphism ( TbB)R ∼=H1(T 2
b ; R). Hence the class of
[C ∩T 2
b ] can be regarded as a tangent vector to the base, which is in gener al real and
varies along the tropical curve as L(i) and L(j) move relative to one another. The
tangent vector ˙u to the tropical curve is this class.
The balancing condition at a vertex b of the tropical polygon amounts to requiring
that the three paths L(i)b → L(j)b, L(j)b → L(k)b and L(k)b → L(i)b form a con-
tractible loop. At a point where a tropical disk is attached, the path L(i)b →L(j)b
changes discontinuously by a loop in the homology class in H1(T 2
b ; Z) corresponding
to the integer tangent vector to the tropical disk.
The last thing to describe for tropical polygons is their multiplicities. T here is a
multiplicity coming from the diﬀerent ways to attach a disk v to the tropical polygon.
If one incoming edge of the polygon has tangent vector ˙ ue corresponding to a path
γ1 : L(i)b → L(j)b on T 2
b , and the disk has tangent vector w corresponding to a
loop γ2 onT 2
b , there are |γ1.γ2| = | det( ˙ue,w )| points where the disk can be attached,
assuming this determinant is an integer (as it is in the special case belo w). Otherwise,
one must look carefully at exactly where on the torus the paths γ1 andγ2 are located.
For a tropical disk v, we also expect the Gross–Siebert theory to associate a multi-
plicitym(v). Morally speaking, this number should be a virtual count of holomor phic
disks corresponding to v, and it should possible to extract this from the “structure”
on the aﬃne base in the sense of [22]. In the case at hand, where the base has just a
single focus-focus singularity, all of these factors are expect to be one for simple disks,
and zero for multiply covered disks [2]. In the rest of this section, w e adopt this as an
ansatz. Modulo this ansatz, we show in Proposition 5.4 that the trop ical curve counts
agree with the holomorphic curve counts computed in Section 4. Fro m a certain point
of view, this may be regarded as evidence for the ansatz itself, sinc e tropical curve
invariants are intentionally designed to correspond to holomorphic c urve invariants,
and we have computed the latter.
In summary, the multiplicity of a tropical polygon will have both the Gr oss–Siebert
factorsm(v) counting how many holomorphic disks are in each class, as well as simp ler
factors counting how many ways these classes of disks can be atta ched.
58 JAMES PASCALEFF
Figure 13. A tropical triangle. The dotted line extending up from
the singular point is a tropical disk.
Remark 11. After this paper was originally written, an exposition of the closely re -
lated idea of jagged paths appeared [18, Deﬁnition 3.2]. In that paper, the various
multiplicities are packaged in a diﬀerent way, but it turns out the that tropical curve
counts deﬁned there also agree, in the case of ( CP2,D ), with the holomorphic curve
counts computed in Section 4. The multiplicities we seek are packaged into certain
series fd = 1 + ∑
pcpzp where d runs over certain distinguished rays and lines in B.
See [18, §3] for more explanation. In our case, there are two such rays ema nating
from the singularity of the aﬃne structure in the monodromy invaria nt directions.
Our ansatz is equivalent to the fact that the corresponding series reduce, in appro-
priate choices of coordinates, to 1 + z and 1 + w respectively. The salient feature is
that these series have a linear term with coeﬃcient 1 and no higher de gree terms.
5.2. Tropical triangles for (CP2,D ). We now write out explicitly the tropical
curves contributing to the triangle products in the case of ( CP2,D ). Let us use
coordinates (η,ξ ) where the point qa,i ∈B( 1
n Z) has coordinates ( a/n, −i/n)
There is one family of simple tropical disks that emanate from the sing ularity on
the η = 0 line in the vertical direction. Their primitive tangent vectors are ±(0, 1).
Figure 13 shows the the tropical triangle representing the contrib ution of y2p to the
product of x2 and z2. This triangle has multiplicity 2. The singularity of the aﬃne
structure is placed so as to emphasize the tropical disk ending at th e singularity.
Proposition 5.4. Let n >0 and m >0, and take qa,i ∈B( 1
n Z), qb,j ∈B( 1
mZ), and
qa+b,h ∈B( 1
n+mZ).
Supposea and b have diﬀerent signs, and let k = min(|a|, |b|), and h =i +j +s. If
0 ≤s ≤k, there is one tropical triangle connecting these three poin ts. It is balanced
after the addition of either s or k −s tropical disks, depending on the position of the
singularity. The multiplicity of this curve is
(k
s
)
. If s does not lie in this range, there
is no triangle.
Suppose that a andb have the same sign. Then unless h =i+j there is no triangle,
and when h =i +j there is exactly one, which is represented geometrically by the line
segment joining qa,i and qb,j.
Proof. When a and b have the same sign the tropical triangle can have no tropical
disks attached to it. Therefore the tropical triangle is simply a line se gment which
passes through the three points, and this only exists if qa+b,h lies on the line between
qa,i and qb,j.
As for when a and b have diﬀerent signs, let us consider the case a ≤ 0, b ≥ 0,
a+b ≥ 0, and hence k = −a. The other cases are related to this by obvious reﬂections
and re-namings.
MIRROR OF THE PROJECTIVE PLANE 59
By Proposition 5.1, a tropical triangle consists essentially of two map s u1,u 2 :
(−∞, 0] →B, together with some copies of the tropical disk and their multiples.
• The leg u2 of the tree connecting qb,j to qa+b,h cannot have any tropical disks
attached, since both endpoints lie on the same side of the line η = 0. We can
apply Lemma 5.3 to obtain the tangent vector ˙ u2 at qa+b,h as m times the
diﬀerence between the endpoints, or
(104) ˙ u2(qa+b,h) = m(qa+b,h −qb,j) =
(ma −nb
n +m , −(mi −nj +ms)
n +m
)
• The leg u1 of the tree connecting qa,i to qa+b,h crosses the line η = 0 at some
pointx, where tropical disks can be attached. It may bend there, and co ntinue
on to qa+b,h, where the balancing condition ˙u1 + ˙u2 = 0 must hold. This shows
that the portion of u1 connecting x to qa+b,h must be parallel to u2. Hence x
must be on the line joining qb,j and qa+b,h. We obtain the position of x:
(105) x : (η,ξ ) = (0, (−aj +bi +bs)/(ma −nb))
• By Lemma 5.3 at x the tangent vector ˙u1 is given by n times the diﬀerence of
the endpoints x and qa,i:
(106) ˙ u1(x)L =n(x −qa,i) = ( −a, [a(mi −nj) +nbs]/(ma −nb))
we use the subscript L to denote this is the tangent vector coming from the
left.
• If the singularity of the aﬃne structure occurs below the point x, then tropical
disks are line segments going up from the singularity to x in the direction (0, 1).
Adding the vector (0,s ) to ˙u1(x)L, we obtain ˙u1(x)R, the tangent vector from
the right,
(107) ˙ u1(x)R = ˙u1(x)L + (0,s ) = ( −a,a (mi −nj +ms)/(ma −nb))
which is parallel to ˙u2(qa+b,h), as it must be. This shows that we must attach
a collection of tropical disks whose total weight is s.
• If the singularity of the aﬃne structure occurs above x, then tropical disks are
line segments going down from the singularity to x in the direction (0 , −1),
but there is also the monodromy to be taken into account. First we m ust act
on ˙u1(x)L by the monodromy M =
(
1 0
1 1
)
to get
(108) M ˙u1(x)L = (−a, [a(mi −nj) +nbs]/(ma −nb) −a)
Adding the vector (0, −(k −s)) to this, with k = −a, gives the same result as
before for ˙u1(x)R. However, in this case we are attaching a collection of disks
with total weight ( k −s).
• The leg u1 propagates in the direction ˙ u1(x)R from x to qa+b,h. As it does
so, the tangent vector ˙u1 increases by ∆ = n(qa+b,h −x), which is parallel to
˙u1(x)R. By comparing aﬃne lengths of the segment of u1 from qa,i to x and
the segment of u1 from x to qa+b,h, we have the proportion
(109) ˙ u1(x)R : ∆ = [ −a/n] : [(a +b)/(n +m)]
60 JAMES PASCALEFF
and
(110)
( ˙u1(x)R +∆) : ˙u1(x)R = [(a+b)/(n+m)−a/n] : [ −a/n] = [ −(ma−nb)/(n+m)] : [ −a]
Thus
(111) ˙ u1(qa+b,h) =
(
−ma −nb
n +m ,mi −nj +ms
n +m
)
= − ˙u2(qa+b,h)
Verifying the balancing condition at qa+b,h.
Now that we know which tropical curves contribute, we must compu te their mul-
tiplicities. The tropical curve constructed above uses the tropica l disk s or (k −s)
times. This means that either we attach a single simple disk s times, or we attach
some multiple covers of the disk in some fashion as to achieve a total m ultiplicity of
s. By our ansatz, only the simple disks contribute, and each with multip licity one.
Attaching simple disks does introduce a multiplicity, since there are mu ltiple places
to attach this disk. In fact, we have det( ˙u1(x)L, (0, 1)) = −a =k, so there are a total
ofk places for disks to be attached. Thus we get the multiplicity
(k
s
)
or
( k
k−s
)
, which
are equal and give the desired result.
□
Remark 12. The fact that the multiplicities
(k
s
)
and
( k
k−s
)
are equal is an illustration of
the general phenomenon that the exact position of the singularity along its invariant
line does not matter for tropical curve counts.
