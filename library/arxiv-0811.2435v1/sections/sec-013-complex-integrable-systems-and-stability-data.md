---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic"
section_id: sec-013-complex-integrable-systems-and-stability-data
section_title: "Complex integrable systems and stability data"
section_number: null
pages: 35-38
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
In this section we explain how complex integrable systems (w ith some ad-
ditional structures) give rise to stability data in the grad ed Lie algebra gΓ
associated with a symplectic lattice. In particular, Seibe rg-Witten diﬀeren-
tial can be interpreted as the central charge for a complex in tegrable system,
while the BPS degeneracies are interpreted via our “numeric al” Donaldson-
Thomas invariants as the number of certain gradient trees on the base of a
complex integrable system.
Recall that a complex integrable system is a holomorphic map π :X→B
where (X,ω 2,0
X ) is a holomorphic symplectic manifold, dim X = 2 dim B,
and the generic ﬁber of π is a Lagrangian submanifold, which is a polarized
abelian variety. We assume (in order to simplify the exposit ion) that the
polarization is principal. The ﬁbration π is non-singular outside of a closed
subvarietyBsing⊂B of codimension at least one. It follows that on the open
subsetBsm :=B\Bsing we have a local system Γ of symplectic lattices with
the ﬁber over b∈Bsm equal to Γ b :=H1(Xb, Z),Xb =π−1(b) (the symplectic
structure on Γ b is given by the polarization).
Furthermore, the set Bsm is locally (near each point b ∈ Bsm) em-
bedded as a holomorphic Lagrangian subvariety into an aﬃne s ymplectic
space parallel to H1(Xb, C). Namely, let us choose a symplectic basis γi∈
Γ b, 1≤ i≤ 2n. Then we have a collection of holomorphic closed 1-forms
αi =
∫
γi
ω2,0
X , 1≤ i≤ 2n in a neighborhood of b. There exists (well-deﬁned
locally up to an additive constant) holomorphic functions zi, 1≤ i≤ 2n
such that αi = dzi, 1 ≤ i≤ 2n. They deﬁne an embedding of a neigh-
borhood of b into C2n. The collection of 1-forms αi gives rise to an ele-
35
ment δ∈ H 1(Bsm, Γ∨⊗ C). We assume that δ = 0. This assumption is
equivalent to an existence of a section Z ∈ Γ(Bsm, Γ ⊗O Bsm) such that
αi =Z(γi), 1≤i≤ 2n.
Deﬁnition 5 We call Z the central charge of the integrable system.
Hence, for every point b∈Bsm we have a symplectic lattice Γ b endowed
with an additive map Zb : Γ b→ C. Our goal will be to deﬁne a continuous
family of stability data on graded Lie algebras gΓ b with central charges Zb.
First, we show an example of section Z.
Example 2 (Seiberg-Witten curve)
Let B = C be a complex line endowed with a complex coordinate u. We
denote by X 0 =T∗ (C\{ 0}) the cotangent bundle to the punctured line. We
endow it with the coordinates (x,y ),y⁄= 0 and the symplectic form
ω2,0 =dx∧ dy
y .
There is a projection π0 :X 0→B given by
π(x,y ) = 1
2 (x2−y− c
y ) ,
wherec is a ﬁxed constant. Fibers of π0 are punctured elliptic curves
y + c
y =x2− 2u .
We denote by X the compactiﬁcation of X 0 obtained by the compactiﬁcations
of the ﬁbers. We denote by π : X→ B the corresponding projection. Then
Zu ∈ H 1(π−1(u), C) is represented by a meromorphic 1-form λSW = xdy
y
(Seiberg-Witten form). The form λSW has zero residues, hence it deﬁnes
an element of H 1(π−1(u), C) for any u∈ Bsm, where Bsm = B\{b−,b +}
consists of points where the ﬁber of π is a non-degenerate elliptic curve.
The dense open set Bsm⊂B carries a K¨ ahler form
ω1,1
B = Im
(∑
1≤i≤n
αi∧αn+i
)
.
We denote by gB the corresponding K¨ ahler metric.
36
For any t∈ C∗ we deﬁne an integral aﬃne structure on C∞-manifold
Bsm given by a collection of closed 1-forms Re( tαi), 1≤ i≤ 2n. For any
simply-connected open subset U⊂ Bsm and a covariantly constant section
γ∈ Γ(Bsm, Γ ) we have a closed 1-form
αγ,t = Re
(
t
∫
γ
ω2,0
X
)
=d Re(tZ(γ)) ,
and the corresponding gradient vector ﬁeld vγ,t =g−1
B (αγ,t). Notice that this
vector ﬁeld is a constant ﬁeld with integral direction in the integral aﬃne
structure associated with closed 1-forms Im( tαi), 1≤i≤ 2n.
Similarly to [40] we can construct inﬁnite oriented trees ly ing in B such
that its external vertices belong to Bsing, and edges are positively oriented
trajectories of vector ﬁelds vγ,t. All internal vertices have valency at least 3,
and every such vertex should be thought of as a splitting poin t: a trajectory
of the vector ﬁeld vγ,t is split at a vertex into several trajectories of vector
ﬁelds vγ1,t,...,v γk,t such that γ =γ1 +··· +γk.
The restriction of the function Z to a tree gives rise to a C-valued function
such that on the trajectory of vector ﬁeld vγ,t it is equal to the restriction
of Z(γ) to this trajectory. We assume that this function approach t o zero
as long as we approach an external vertex of the tree (which be longs to
Bsing). It is easy to see that tZ(γ) is a positive number at any other point
of the tree (hence it deﬁnes a length function). We expect tha t for any point
b∈Bsm andγ∈ Γ b there exist ﬁnitely many such trees which pass the point
b in the direction of γ (we can think of b as a root of the tree, hence we
can say above that we consider oriented trees such that all ex ternal vertices
except of the root belong to Bsing). Here we choose an aﬃne structure with
t∈ R>0(Z(γ)−1
b ). Probably the number of such trees for ﬁxed b,γ is ﬁnite,
since their lengths should be bounded. 8
For a ﬁxed t∈ C∗ the union Wt of all trees as above is in fact a countable
union of real hypersurfaces in Bsm. They are analogs of the walls of second
kind. The set Wt depends on Arg t only. The union ∪θ∈[0,2πi)Wteiθ swap the
whole spaceBsm. Let us denote by W (1) the union over all t∈ C∗/R>0 of the
sets of internal vertices of all trees in W (1) (splitting points of the gradient
trajectories). This is an analog of the wall of ﬁrst kind.
8In [40] we modiﬁed the gradient ﬁelds near Bsing in order to guarantee the convergence
of inﬁnite products in the adic topology. It seems that we wer e too cautious, and the
convergence holds without any modiﬁcation.
37
In [40] we suggested a procedure of assigning rational multi plicities to
edges of trees (see also [27],[28]). This leads to the follow ing picture. Con-
sider the total space tot(Γ ) of the local system Γ . It follows from above
assumptions and considerations that we have a locally const ant function
Ω : tot(Γ )→ Q which jumps at the subset consisting of the lifts of the wall
W (1) to tot(Γ ). Then for a ﬁxed b∈ Bsm the pair ( Z, Ω) deﬁnes stability
data on the graded Lie algebra gΓ b of the group of formal symplectomor-
phisms of the symplectic torus TΓ b. In this way we obtain a local embedding
Bsm֒→Stab(gΓ b).
In the above example of Seiberg-Witten curve, the wall W (1) is an oval-
shaped curve which contains two singular points b±∈ Bsing. A typical Wt
looks such as follows.
b− +b
The wall-crossing formula coincides with the one for T (2)
a,b (see Introduc-
tion).
Remark 13 1) We expect that the above considerations are valid for a lar ge
class of complex integrable systems, e.g. Hitchin system.
2) In the case when we have a 3d complex compact Calabi-Yau mani-
fold X, the moduli space MX of complex structures on X is locally embed-
ded into the projective space P(H 3(X, C)) as a base of a Lagrangian cone
LX⊂ H 3(X, C). It carries a K¨ ahler metric (Weil-Petersson metric). We
can repeat the above considerations given for integrable sy stems, replacing the
gradient ﬂows by the attractor ﬂow (see e.g. [13]). The above case of inte-
grable systems is obtained in the limit, when the cone become s “very sharp”.
