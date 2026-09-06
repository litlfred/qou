---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-008-21-the-models-of-hyperbolic-space
section_title: "The models of hyperbolic space"
section_number: 2.1
pages: 53-67
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
In contrast withSn and Rn, the hyperbolic space Hn may be described
in various diﬀerent ways, no-one of which is prevalent in the literature. Each
description is a model for Hn. We ﬁrst introduce the hyperboloid model,
which has a more algebraic ﬂavour, and then we turn to the disc and half-
space models that are somehow more geometric (and easier to visualise in
dimensionsn = 2 and 3).
2.1.1. Hyperboloid. The sphereSn is the set of all points with norm 1
in Rn+1, equipped with the Euclidean scalar product. Analogously, we may
deﬁneHn as the set of all points of norm−1 in Rn+1, equipped with the usual
Lorentzian scalar product. This set forms a hyperboloid with two sheets, and
we choose one.
Deﬁnition 2.1.1. TheLorentzian scalar producton Rn+1 is:
⟨x,y⟩ =
n∑
i=1
xiyi−xn+1yn+1.
It has signature(n, 1). A vectorx∈ Rn+1 is time-like, light-like, orspace-like
if⟨x,x⟩ is negative, null, or positive respectively. Thehyperboloid modelIn is
deﬁned as follows:
In =
{
x∈ Rn+1⏐⏐⟨x,x⟩ =−1, xn+1> 0
}
.
The set of pointsx with⟨x,x⟩ =−1 is ahyperboloid with two sheets, and
In is the connected component (sheet) withxn+1> 0. Let us prove a general
fact. For us, a scalar product is a real non-degenerate symmetric bilinear form.
45
46 2. HYPERBOLIC SPACE
Figure 2.1. The hyperboloid with two sheets deﬁned by the equation
⟨x,x⟩ =−1. The modelIn for Hn is the upper sheet.
Proposition 2.1.2. Let⟨,⟩ be a scalar product on Rn+1. The function
f : Rn→ R given by
f (x) =⟨x,x⟩
is everywhere smooth and has diﬀerential
dfx (y ) = 2⟨x,y⟩.
Proof. The following equality holds:
⟨x +y,x +y⟩ =⟨x,x⟩ + 2⟨x,y⟩ +⟨y,y⟩.
The component⟨x,y⟩ is linear iny while⟨y,y⟩ is quadratic. □
Corollary 2.1.3.The hyperboloidIn is a Riemannian manifold.
Proof. The hyperboloid is the set of points withf (x) =⟨x,x⟩ =−1. For
all x∈In the diﬀerentialy↦→ 2⟨x,y⟩ is surjective and hence the hyperboloid
is a diﬀerentiable submanifold of codimension 1.
The tangent spaceTxIn atx∈In is the hyperplane
Tx = kerdfx =
{
y
⏐⏐⟨x,y⟩ = 0
}
=x⊥
orthogonal tox in the Lorentzian scalar product. Sincex is time-like, the
restriction of the Lorentzian scalar product tox⊥ is positive deﬁnite and hence
deﬁnes a metric tensor onIn. □
The hyperboloidIn is a model for hyperbolic spaceHn. We will soon prove
that it is simply connected, complete, and has constant curvature−1.
2.1. THE MODELS OF HYPERBOLIC SPACE 47
2.1.2. Isometries of the hyperboloid. The isometries ofIn are easily
classiﬁed using linear algebra.
Let O(n, 1) be the group of linear isomorphismsf of Rn+1 that preserve
the Lorentzian scalar product,i.e. such that⟨v,w⟩ =⟨f (v ),f (w )⟩ for any
v,w ∈ Rn. An element inO(n, 1) preserves the hyperboloid with two sheets,
and the elements preserving the upper sheetIn form a subgroup of index two
inO(n, 1) that we indicate withO+(n, 1).
Proposition 2.1.4. The following equality holds:
Isom(In) =O+(n, 1).
Proof. Pickf ∈ O+(n, 1). If x∈ In then f (x)∈ In and f sends x⊥ to
f (x)⊥ isometrically, hencef∈ Isom(In). ThereforeO+(n, 1)⊆ Isom(In).
To prove the converse inclusion we show that for every pairx,y ∈In and
every linear isometryg :x⊥→y⊥ there is an elementf∈O+(n, 1) such that
f (x) = y and f|x⊥ = g. Since isometries are determined by their ﬁrst-order
behaviour at a pointx, this impliesIsom(In)⊆O+(n, 1).
Via elementary linear algebra we prove thatO+(n, 1) acts transitively on
In and hence we may suppose thatx = y = (0,..., 0, 1). Now x⊥ = y⊥ is
the horizontal hyperplane andg∈O(n). To deﬁnef simply take
f =
(g 0
0 1
)
.
The proof is complete. □
The isometry groups ofSn and Rn are described analogously:
Proposition 2.1.5. The following equalities hold:
Isom(Sn) =O(n + 1),
Isom(Rn) =
{
x↦→Ax +b
⏐⏐A∈O(n),b∈ Rn}
.
Proof. The proof is analogous to the one above. □
We have also proved the following fact. Aframe at a pointp in a Rie-
mannian manifoldM is an orthonormal basis forTpM.
Corollary 2.1.6.Let M =Sn, Rn, or Hn. Given two pointsp,q ∈M and
two frames atp andq, there is a unique isometry that carries the ﬁrst frame
to the second.
2.1.3. Subspaces. We introduce the following natural objects.
Deﬁnition 2.1.7. Ak-dimensional subspace of Rn,Sn,In is respectively:
• an aﬃnek-dimensional space inRn,
• the intersection of a(k + 1)-dimensional vector subspace ofRn+1
withSn,
48 2. HYPERBOLIC SPACE
• the intersection of a(k + 1)-dimensional vector subspace ofRn+1
withIn, when it is non-empty.
Remark 2.1.8. Elementary linear algebra shows that the following condi-
tions are equivalent for any(k + 1)-dimensional vector subspaceW⊂ Rn+1:
(1) W∩In⁄= ∅,
(2) W contains at least a time-like vector,
(3) the signature of⟨,⟩|W is (k, 1).
A k-subspace in Rn,Sn, Hn is itself isometric to Rk,Sk, Hk. The non-
empty intersection of two subspaces is always a subspace. An isometry of
Rn,Sn, Hn sendsk-subspaces tok-subspaces.
Exercise 2.1.9. LetS be ak-subspace inRn,Sn, orHn andp∈S a point.
There is a unique(n−k)-subspaceS′ intersectingS orthogonally inp.
2.1.4. Reﬂections.We now introduce a basic kind of isometry. There-
ﬂectionrS along a subspaceS inIn is an isometry ofIn deﬁned as follows. By
deﬁnitionS =In∩W with⟨,⟩|W non-degenerate, henceRn+1 =W⊕W⊥ and
we setrS|W = id andrS|W⊥ =−id. Analogous deﬁnitions work for subspaces
ofSn and Rn.
Exercise 2.1.10. The reﬂectionrS has ﬁxed setS and preserves all the
subspaces orthogonal toS. It is orientation-preserving if and only ifS has
even codimension.
Proposition 2.1.11. Reﬂections along hyperplanes generate the isometry
groups ofSn, Rn, and Hn.
Proof. It is a standard linear algebra fact that orthogonal reﬂections along
vector hyperspaces generateO(n). This proves the caseSn and shows that
reﬂections generate the stabiliser of any point inRn and Hn. To conclude it
suﬃces to check that reﬂections act transitively on points: to sendx to y,
reﬂect along the hyperplane orthogonal to the segment connectingx to y in
its midpoint. □
2.1.5. Lines. A 1-subspaceisa line. Wenowshowthatlinesandgeodesics
are the same thing. We recall the hyperbolic trigonometric functions:
sinh(t) = et−e−t
2 , cosh(t) = et +e−t
2 .
Proposition 2.1.12. A non-trivial complete geodesic inSn, Rn, or Hn is a
line run at constant speed. Concretely, letp∈M be a point andv∈TpM a
unit vector. The geodesicγ exiting fromp with velocityv is:
• γ(t) = cos(t)·p + sin(t)·v ifM =Sn,
• γ(t) =p +tv ifM = Rn,
• γ(t) = cosh(t)·p + sinh(t)·v ifM =In.
2.1. THE MODELS OF HYPERBOLIC SPACE 49
Proof. Letp∈In be a point,v∈TpM a unit vector, andγ the geodesic
exiting fromp with velocityv. The planeW ⊂ Rn+1 generated byp and v
intersects In into a linel containing p and tangent tov. To prove thatl is
the support ofγ we use a symmetry argument: the reﬂectionrl ﬁxesp andv
and henceγ, thereforeγ is forced to be contained in its ﬁxed locus, which is
l. This shows that non-trivial geodesics are lines run at constant speed.
We now consider the curveα(t) = cosh( t)·p + sinh(t)·v. We have
α(0) = p andα′(0) = v. It remains to prove thatα parametrizesl with unit
speed, and from this we deduce thatγ =α. We note that
⟨α(t),α (t)⟩ = cosh2(t)⟨p,p⟩ + 2 cosh(t) sinh(t)⟨p,v⟩ + sinh2(t)⟨v,v⟩
=− cosh2(t) + sinh2(t) =−1.
Thereforeα parametrizesl. Its velocity is
α′(t) = cosh′(t)·p + sinh′(t)·v = sinh(t)·p + cosh(t)·v
whose squared norm is− sinh2(t) + cosh 2(t) = 1 . Therefore γ = α. The
proofs forSn and Rn are analogous. □
Corollary 2.1.13.The spacesSn, Rn, and Hn are complete.
Proof. The previous proposition shows that geodesics are deﬁned onR,
hence the space is complete by the Hopf – Rinow Theorem 1.2.8. □
It is easy to show that two points inHn are contained in a unique line.
Remark 2.1.14. Euclid’s ﬁfth postulate holds only inR2. Given a liner
and a pointP ⁄∈ r, there is exactly one line passing throughP and disjoint
fromr in R2, there is no-one inS2, and there are inﬁnitely many inH2.
We can easily calculate the distance between two points.
Proposition 2.1.15. Letp,q ∈M be two points. We have
• cos(d(p,q )) =⟨p,q⟩ ifM =Sn,
• cosh(d(p,q )) =−⟨p,q⟩ ifM =In.
Proof. Letγ be a geodesic that goes fromp toq at unit speed. We have
γ(0) = p and γ(t) = q with t =d(p,q ). Setv =γ′(0) and use Proposition
2.1.12 to conclude. □
2.1.6. The Poincaré disc.We introduce two models ofHn, thedisc and
the half-space, that are easier to visualise especially in the dimensionsn = 2, 3
we are interested in. The ﬁrst model is thePoincaré disc
Dn =
{
x∈ Rn ⏐⏐‖x‖< 1
}
.
The metric tensor onDn is obviously not the Euclidean one ofRn, but
instead is induced by a particular diﬀeomorphism betweenIn andDn that we
construct now. We identify Rn with the horizontal hyperplanexn+1 = 0 in
50 2. HYPERBOLIC SPACE
P
Dn
I n
Figure 2.2. The projection towardsP = (0,..., 0,−1) induces a bijec-
tion between the hyperboloid modelIn and the disc modelDn.
Rn+1 and note that the projection towardsP = (0,..., 0,−1) depicted in
Figure 2.2 induces a bijection betweenIn and the horizontal discDn⊂ Rn.
The projectionp may be written as:
p(x1,...,x n+1) = (x1,...,x n)
xn+1 + 1
and is indeed a diﬀeomorphismp :In→Dn that transports the metric tensor
onIn to some metric tensorg onDn.
Proposition 2.1.16. The metric tensorg atx∈Dn is:
gx =
( 2
1−‖x‖2
)2
·gE
x
wheregE is the Euclidean metric tensor onDn⊂ Rn.
Proof. The inverseq :Dn→In ofp is:
q(x) =
( 2x1
1−‖x‖2,..., 2xn
1−‖x‖2, 1 +‖x‖2
1−‖x‖2
)
.
Pickx∈Dn. Rotationsaroundthe xn+1 axisareisometriesof In andcommute
with p, therefore they are isometries of(Dn,g ) too. Up to rotating we may
takex = (x1, 0,..., 0) and ﬁnd
dqx = 2
1−x 2
1
·


1+x 2
1
1−x 2
1
0 ··· 0
0 1 ··· 0
... ... ... ...
0 0 ··· 1
2 x1
1−x 2
1
0 ··· 0


.
Thecolumnvectorsformanorthonormalbasisof Tq(x)In. Hencedqx stretches
all vectors of a constant 2
1−x 2
1
. Thereforegx = 4
(1−x 2
1 )2gE
x . □
2.1. THE MODELS OF HYPERBOLIC SPACE 51
The Poincaré disc is aconformal model of Hn: it is a model where the
metric diﬀers from the Euclidean metric only by multiplication by a positive
scalar
( 2
1−‖x‖2
)2 that depends smoothly onx. We note that the scalar tends to
inﬁnity whenx tends to∂Dn. On a conformal model the lengths of vectors are
diﬀerent from the Euclidean lengths, but the angles formed by two adjacent
vectors coincide with the Euclidean ones. Shortly: lengths are distorted but
angles are preserved.
Let us see how we can easily visualisek-subspaces in the disc model.
Proposition 2.1.17. The k-subspaces in Dn are the intersections ofDn
withk-spheres andk-planes of Rn orthogonal to∂Dn.
Proof. Since everyk-subspace is an intersection of hyperplanes, we easily
restrict to the casek =n−1. A hyperplane inIn isIn∩v⊥ for some space-like
vectorv. Ifv is horizontal (i.e. its last coordinate is zero) thenv⊥ is vertical
andp(In∩v⊥) =Dn∩v⊥, a hyperplane orthogonal to∂Dn.
If v is not horizontal, up to rescaling and rotating aroundxn+1 we may
supposev = (α, 0,..., 0, 1) withα> 1. The hyperplane is
{
x 2
1 +... +x 2
n−x 2
n+1 =−1
}
∩
{
xn+1 =αx1
}
.
On the other hand the sphere inRn of centre(α, 0,..., 0) and radius
√
α2− 1
is orthogonal to∂Dn and is described by the equation
{
(y1−α)2 +y 2
2 +... +y 2
n =α2− 1
}
=
{
y 2
1 +... +y 2
n− 2αy1 =−1
}
which is equivalent to||y||2 =−1 + 2αy1. Ify =p(x) the relations
y1 = x1
xn+1 + 1, ‖y‖2 = xn+1− 1
xn+1 + 1
transform the latter equation inxn+1 =αx1. □
Three lines inD2 delimiting a hyperbolic triangle are drawn in Figure 2.3.
Since the disc is a conformal model, the inner anglesα,β,γ are the ones we
see on the picture. In particular we verify easily thatα +β +γ <π.
Exercise 2.1.18. For any triple of positive anglesα,β,γ withα+β +γ <π
there is a triangle with inner anglesα,β,γ . This triangle is unique up to
isometry.
2.1.7. Inversions. To construct our second conformal model we need to
introduce a geometric transformation called inversion.
Deﬁnition 2.1.19. LetS =S(x0,r ) be the sphere inRn centred inx0 and
with radiusr. The inversion along S is the mapϕ: Rn\{x0}→ Rn\{x0}
deﬁned as follows:
ϕ(x) =x0 +r 2 x−x0
‖x−x0‖2.
52 2. HYPERBOLIC SPACE
g
a b
Figure 2.3. Three lines that determine a hyperbolic triangle in the
Poincaré disc. The inner anglesα,β, and γ coincide with the Euclidean
ones, and we haveα +β +γ <π.
Figure 2.4. A tessellation of S2, R2 o H2 is a subdivision of the plane
into polygons. The tessellation ofH2 shown here is obtained by drawing
inﬁnitely many lines in the plane. The triangles have inner anglesπ
2, π
5, π
5
and are all isometric.
The map may be extended continuously on the whole sphereSn, identiﬁed
with Rn∪{∞} through the stereographic projection, by settingϕ(x0) = ∞
andϕ(∞) =x0. A geometric description is shown in Figure 2.5.
We have already talked about conformal models. More generally, a diﬀeo-
morphismf :M→N between twoorientedRiemannian manifoldsis conformal
(respectively,anticonformal) if for anyp∈M the diﬀerentialdfp is the prod-
uct of a scalar dilationλp > 0 and an isometry that preserves (respectively,
inverts) the orientation. The scalar λp depends smoothly onp. A confor-
mal map preserves the angle between two tangent vectors but multiplies their
lengths by
√
λp.
Exercise 2.1.20. The stereographic projection is conformal.
Proposition 2.1.21. The following hold:
(1) every inversion is a smooth and anticonformal map;
2.1. THE MODELS OF HYPERBOLIC SPACE 53
Figure 2.5. The inversion trough a sphere of centreO and radius r
movesP toP′ so thatOP×OP′ =r 2 (left). It transforms ak-sphereS
(blue) into ak-plane (green) ifO∈S (centre) or into ak-sphere (green)
ifO⁄∈S (right).
(2) inversions sendk-spheres andk-planes tok-spheres andk-planes.
Proof. Up to conjugating with translations and dilations we may suppose
x0 = 0 andr = 1. The inversion isϕ(x) = x
‖x‖2 and we show thatdϕx is 1
‖x‖2
times a reﬂection with respect to the hyperplane orthogonal tox. We may
supposex = (x1, 0,..., 0) and calculate the partial derivatives:
ϕ(x1,...,x n) = (x1,...,x n)
‖x‖2 , ∂ϕi
∂xj
= δij‖x‖2− 2xixj
‖x‖4 .
The partial derivatives atx = (x1, 0,..., 0) are
∂ϕ1
∂x1
=− 1
x 2
1
, ∂ϕi
∂xi
= 1
x 2
1
, ∂ϕj
∂xk
= 0
for alli >1 andj⁄=k. This proves our assertion.
The fact that an inversion preserves sphere and planes may be easily re-
duced to the two-dimensional case (with circles and lines), a classical fact of
Euclidean geometry. □
2.1.8. The half-space model. We introduce another conformal model.
The half-space modelis the space
Hn =
{
(x1,...,x n)∈ Rn ⏐⏐xn> 0
}
.
It is obtained from the disc modelDn by an inversion inRn with centreC =
(0,..., 0,−1) and radius
√
2 as shown in Figure 2.6. The boundary∂Hn is
the horizontal hyperplane{xn = 0}, to which we add the point∞ at inﬁnity to
get a bijective correspondence between∂Hn and∂Dn through the inversion.
Proposition 2.1.22. The half-spaceHn is a conformal model forHn. Its
k-subspaces are thek-planes andk-spheres in Rn orthogonal to∂Hn.
54 2. HYPERBOLIC SPACE
C
Dn
Hn
O
Figure 2.6. The inversion along the sphere with centre C =
(0,..., 0,−1) and radius
√
2 transforms the Poincaré discDn into the
half-space modelHn. Heren = 2.
Figure 2.7. Lines and planes in the half-space model forH3.
Proof. The inversion is anticonformal and hence preserve angles, moreover
it transformsk-spheres andk-planes inDn orthogonal to∂Dn intok-spheres
andk-planes inHn orthogonal to∂Hn. □
Some lines and planes inH3 are drawn in Figure 2.7. The metric tensorg
onHn has a particularly nice form.
Proposition 2.1.23. The metric tensor onHn is:
gx = 1
x 2n
·gE
wheregE is the Euclidean metric tensor onHn⊂ Rn.
2.1. THE MODELS OF HYPERBOLIC SPACE 55
Proof. The inversionϕ:Dn→Hn is the function
ϕ(x1,...,x n) = (0,..., 0,−1) + 2 (x1,...,x n−1,xn + 1)
‖(x1,...,x n−1,xn + 1)‖2
= (2x1,..., 2xn−1, 1−‖x‖2)
‖x‖2 + 2xn + 1 .
As seen in the proof of Proposition 2.1.21, the inversionϕ is anticonformal
with scalar dilation
2
‖(x1,...,x n−1,xn + 1)‖2 = 2
‖x‖2 + 2xn + 1.
The mapϕ hence transforms the metric tensor
(
2
1−‖x‖2
)2
·gE inx∈Dn into
the following metric tensor inϕ(x)∈Hn:
( 2
1−‖x‖2
)2
·
(‖x‖2 + 2xn + 1
2
)2
·gE = 1
ϕn(x)2·gE.
The proof is complete. □
2.1.9. Geodesics in the conformal models.The discDn and the half-
spaceHn are conformal models forHn. In both models the hyperbolic metric
diﬀers from the Euclidean one only by a multiplication with some function.
In the half-spaceHn the lines are Euclidean vertical half-lines or half-circles
orthogonal to ∂Hn as in Figure 2.7. Vertical geodesics have a particularly
simple form.
Proposition 2.1.24.The vertical geodesic inHn passing through the point
(x1,...,x n−1, 1) at timet = 0 and pointing upward with unit speed is:
γ(t) = (x1,...,x n−1,et).
Proof. A tangent vectorv at (x1,...,x n)∈Hn has norm‖v‖E
xn where‖v‖E
indicates the Euclidean norm. We get
‖γ′(t)‖ =‖(0,..., 0,et)‖ = et
et = 1.
Thereforeγ(t) runs on a line at unit speed. □
We can easily deduce a parametrisation for the geodesics inDn passing
through the origin. Recall the hyperbolic tangent:
tanh(t) = sinh(t)
cosh(t) = et−e−t
et +e−t = e2t− 1
e2t + 1.
Proposition 2.1.25.The geodesic inDn passing through the origin at time
t = 0 and pointing towardsx∈Sn−1 at unit speed is:
γ(t) = et− 1
et + 1·x =
(
tanh t
2
)
·x.
56 2. HYPERBOLIC SPACE
Proof. We can supposex = (0,..., 0, 1) and obtain this parametrisation
from that of the vertical line inHn through inversion. □
We obtain in particular:
Corollary 2.1.26. The exponential map exp0 : T0Dn→ Dn at the origin
0∈Dn is the diﬀeomorphism:
exp0(x) = e‖x‖− 1
e‖x‖ + 1· x
‖x‖ =
(
tanh‖x‖
2
)
· x
‖x‖.
Since the isometries ofHn act transitively on points, we deduce that the
exponential map at anyp∈ Hn is a diﬀeomorphism. As a consequence, the
injectivity radius ofHn is∞, as in the EuclideanRn.
2.1.10. Isometries of the conformal models.In the half-space model it
is easy to identify some isometries:
Proposition 2.1.27. The following are isometries ofHn:
• horizontal translationsx↦→x +b withb = (b1,...,b n−1, 0),
• dilationsx↦→λx withλ> 0,
• inversions with respect to spheres orthogonal to∂Hn.
Proof. Horizontal translations obviously preserve the metric tensorg =
1
x 2n
·gE. We indicate by‖·‖ and‖·‖ E the hyperbolic and Euclidean norm of
tangent vectors. On a dilationϕ(x) =λx we get
‖dϕx (v )‖ =‖dϕx (v )‖E
ϕ(x)n
= λ‖v‖E
λxn
=‖v‖E
xn
=‖v‖.
Concerning inversions, up to conjugating by translations and dilations it
suﬃces to consider the mapϕ(x) = x
‖x‖2. We have already seen thatdϕx is
1
‖x‖2 times a linear reﬂection. Therefore
‖dϕx (v )‖ =‖dϕx (v )‖E
ϕ(x)n
=‖v‖E/‖x‖2
xn/‖x‖2 =‖v‖E
xn
=‖v‖.
This completes the proof. □
In the disc model we can easily write the isometries that ﬁx the origin:
Proposition 2.1.28. The groupO(n) acts isometrically onDn.
Proof. The metric tensor onDn has a spherical symmetry. □
It is harder to write the isometries that ﬁx another point ofDn orHn.
Proposition 2.1.29. On the conformal modelsDn and Hn, the isometry
group is generated by inversions along spheres and reﬂections along Euclidean
planes orthogonal to the boundary.
2.1. THE MODELS OF HYPERBOLIC SPACE 57
Proof. We know from Proposition 2.1.27 that these maps are isometries
of Hn. One such isometry ﬁxes a hyperplaneS, hence it is the hyperbolic
reﬂectionrS (which is the unique non-trivial isometry ﬁxingS). Hyperbolic
reﬂections generate the isometry group by Proposition 2.1.11.
InDn the proof is the same, we leave as an exercise to prove that a sphere
inversion preserves the metric tensor and is hence an isometry. □
2.1.11. Balls in the conformal models.How does a metric ballB(x0,r )
in the hyperbolic space look like? The answer in the conformal models is
surprisingly simple.
Proposition 2.1.30. In the conformal models balls are Euclidean balls.
Proof. In the disc modelB(0,r ) is a ball centred at0 by symmetry. The
ballB(x0,r ) at another pointx0 is obtained fromB(0,r ) by composing inver-
sions, which send spheres to spheres and hence balls to balls. The inversion
Dn→Hn also sends balls to balls. □
The centre of the ball is not its Euclidean centre in general!
2.1.12. The Klein model. There is a fourth model for the hyperbolic
space that is some kind of intermediate version between the hyperboloid and
the Poincaré disc model.
The Klein or projective model for Hn is obtained by embedding the hy-
perboloid In inside RPn via the projection Rn+1\{ 0} → RPn. The im-
age of this embedding is an open discKn ⊂ RPn bounded by the quadric
x 2
1 +... +x 2
n−x 2
n+1 = 0. We equipKn with the metric tensor transported
fromIn , so thatKn is indeed a model forHn.
When read in the chartxn+1 = 1, the Klein modelKn becomes the open
disc x 2
1 +... +x 2
n < 1. It is like the Poincaré discDn, but with a diﬀerent
metric tensor!
The Klein modelKn is not conformal and its metric tensor is a bit more
complicated than that ofDn orHn. On the other hand, the subspaces inKn
are easier to identify: by deﬁnition, these are just the projective subspaces of
RPn intersected with the open discKn. Therefore lines are straight lines, but
the angles and distances are distorted. Note also that the isometries ofKn
are projective transformations. The distance function is particularly nice:
Exercise 2.1.31. The distance of two distinct pointsp,q inKn is
d(p,q ) = 1
2| logβ(p,q,r,s )|
wherer,s are the intersections of the projective linel containingp andq with
∂Kn, andβ(p,q,r,s ) is the cross-ratio of the four points.
58 2. HYPERBOLIC SPACE
Figure 2.8. A tessellation ofH2 into regular triangles and heptagons in
the Klein model.
2.2. Compactiﬁcation and isometries of hyperbolic space
In this section we compactify the hyperbolic spaceHn by adding some
“points at inﬁnity”. The compactiﬁcation will then be used to classify the
isometries of Hn into three types. We also study the mutual position of two
subspaces and deﬁne some peculiar hyperbolic objects: the horospheres.
2.2.1. Points at inﬁnity.Let a geodesic half-line in Hn be a geodesic
γ : [0, +∞)→ Hn with constant unit speed.
Deﬁnition 2.2.1. The set∂Hn of thepoints at inﬁnityin Hn is the set of
all geodesic half-lines, considered up to the following equivalence relation:
γ1∼γ2 ⇐⇒ sup
t∈[0,+∞)
{
d
(
γ1(t),γ 2(t)
)}
< +∞.
We add its points at inﬁnity toHn by deﬁning
Hn = Hn∪∂Hn.
Proposition 2.2.2.On the disc model there is a natural 1-1 correspondence
between∂Dn and∂Hn and hence between the closed discDn and Hn.
Proof. A geodesic half-lineγ in Dn is a circle or line arc orthogonal to
∂Dn and hence the Euclidean limitlimt→∞γ(t) is a point in∂Dn. We now
prove that two half-lines converge to the same point if and only if they lie in
the same equivalence class.
Suppose that two half-geodesicsγ1, γ2 converge to the same pointp∈
∂Dn. Up to isometries and inversions, we can change the conformal model to
Hn and takep =∞. In this nicer settingγ1 andγ2 are vertical lines:
γ1(t) = (x1,...,x n−1,xnet), γ 2(t) = (y1,...,y n−1,ynet).
The geodesic
γ3(t) = (y1,...,y n−1,xnet)
