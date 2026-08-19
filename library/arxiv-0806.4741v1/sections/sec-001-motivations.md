---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane P. Bieliavsky G´ eom´ etrie et Physique math´ ematique Universit´ e Catholique de Louvain 2, Chemin du Cyclotron, B-1348 Louva"
section_id: sec-001-motivations
section_title: "Motivations"
section_number: null
pages: 1-3
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
doc_brief: "The deformation quantizations of the hyperbolic plane P. Bieliavsky Géométrie et Physique mathématique Université Catholique de Louvain 2, Chemin du Cyclotron, B-1348 Louvain-la-Neuve, Belgium — We"
---
The idea of the formal deformation quantization program [1], initiated by Bayen, Flato, Fronsdal, Lichnerow-
icz and Sternheimer, is to generalize the Weyl product to an arbitrary symplectic (or Poisson) manifold. In
this context, the framework of quantum mechanics is the same as classical mechanics, observables are the
same, and quantization arises as a deformation of the algebra of functions on the manifold, from a commu-
tative to a non-commutative one.
A formal star product (or deformation quantization) of a symplectic manifold (M,ω ) is an associative C[[ℏ]]-
bilinear product:
⋆ :C∞(M)[[ℏ]]×C∞(M)[[ℏ]]−→C∞(M)[[ℏ]] : (u,v )↦→u⋆v (1)
such that, for u,v∈C∞(M), the formal series
u⋆v =
∞∑
k=0
ℏkCk(u,v ) (2)
1
arXiv:0806.4741v1  [math-ph]  30 Jun 2008
involves bi-diﬀerential operators Ck :C∞(M)×C∞(M)→C∞(M) satisfying the following properties:
(i) C0(u, v) = uv
(ii) C1(u,v )−C1(v,u ) = 2 i{u, v} where{,} denotes the Poisson bracket on C∞(M) associated to ω.
Two such star products⋆i (i = 1, 2) on the same symplectic manifoldM are called equivalent if there exists
a formal series of the form
T = I +
∞∑
k=1
ℏkTk (3)
where the Tk’s are diﬀerential operators on C∞(M) such that for all u,v∈C∞(M), one has
u⋆ 2v = T (T−1u⋆ 1T−1v ) ; (4)
the latter expression will be shortened by ⋆2 =T (⋆1).
The ﬁrst existence proofs were given in the 80’s independently by Dewilde-Lecomte, Fedosov and Omori-
Maeda-Yoshioka [2, 3, 4]. Equivalence classes of star products on a symplectic manifold are in 1-1 corre-
spondence with the space of formal series with coeﬃcients in the second de Rham cohomology space of M
[5, 6].
The most important example of star product is the so-called Moyal star product ⋆0
ℏ on the plane R2 endowed
with its standard symplectic structure Ω:
u⋆ 0
ℏv := u.v +i ℏ
2{u,v} +
∞∑
k=2
(i ℏ/2)k
k! Ωi1j1··· Ωikjk∂i1···iku∂j1···jkv , (5)
=
∞∑
k=0
(i ℏ/2)k
k!
k∑
p=0
(−1)p k!
p!(k−p)!∂k−p
a ∂p
𝓁u∂p
a∂k−p
𝓁 v , (6)
where
ΩikΩkj =−δk
i , {u,v} = Ωij∂iu∂jv :=∂au∂𝓁v−∂𝓁u∂av . (7)
In the context of formal deformation quantization, one does not worry about the convergence of the series
(2). In particular, a formal star product does not, in general, underlie any operator algebraic or spectral
theory. However, situations exist where star products occur as asymptotic expansions of operator calculi.
The most known example is provided by the Weyl product which has the following integral representation:
(u⋆W v)(x) = (π ℏ)−2n
∫
R2n×R2n
u(y)v(z)ei 2
ℏS0(x,y,z)dydz, (8)
where
S0(x,y,z ) = Ω(x,y ) + Ω(y,z ) + Ω(z,x ), (9)
Ω denoting the standard symplectic two-form on R2n. The product represented by (8) enjoys an important
property: it is internal on the Schwartz space, the space of rapidly decreasing functions, on R2n[7]. Thus,
the product of two (Schwartz) functions is again a (Schwartz) function —rather than a formal power series
as in the formal context. Such a situation will be referred to as non-formal deformation quantization. Note
that Moyal’s star product (5) can be deﬁned as a formal asymptotic expansion of Weyl’s product.
In this paper, we will be interested in invariant deformation quantizations. When a group L acts on M by
symplectomorphisms, a star product is saaid to be L- invariant if for all g∈ L, u,v∈C∞(M):
g⋆(u⋆v ) = g⋆u⋆g ⋆v . (10)
When L preserves a symplectic connection∇ on M:
L⊂ Aﬀ(∇)∩ Symp(ω), (11)
then, Fedosov’s construction yields an L-invariant star product. The notion of equivalence of L-invariant
star products is the same as above except that each diﬀerential operator Tk is required to commute with
2
the action of L. The set of L-equivariant equivalence classes of L-invariant star products is in this case
parametrized by the space H2
dR(M)L[[ℏ]] of series with coeﬃcients in the classes of L-invariant 2-forms on
M [8].
Although the study of deformation quantization admitting a given symmetry is natural, one may mention
important speciﬁc situations where the symmetric situation is relevant. Firstly, the observable algebra of a
conformal ﬁeld theory deﬁnes an algebra of vertex operators. Thus any ﬁnite dimensional limit of such a
theory must contains some remanent of this structure. In particular if the limit procedure is equivariant the
remanent will also be symmetric. For instance, in the seminal work of Seiberg and Witten [[9]] it is shown
that , in the limit of a large B-ﬁeld on a ﬂat brane, the limit of the vertex operator algebra is an associative
invariant product on the space of functions on the brane that has the symmetry of the initial brane and
ﬁelds conﬁguration. Accordingly it becomes natural to inquire about all the associative composition law of
functions compatible with a given symmetry group (especially for non-compact symmetries). Actually, let
us emphasize that our considerations go beyond string theory, but concern any Kac-Moody invariant theory.
Moreover, it is known since the seminal works [10, 9] that noncommutative geometry (and deformation
theory) has intricate links with string theory. A manifestation of this statement stems from the fact that, in
ﬂat space-time, the worldvolume of a D-brane, on which open strings end, is deformed into a noncommutative
manifold in the presence of a B-ﬁeld. In particular, in the limit in which the massive open string modes
decouple, the operator product expansion of open string tachyon vertex operators is governed by the Moyal-
Weyl product[9, 11]. This can be schematically written as e iP.X(τ)eiQ.X(τ′)∼ (eiP.X M
⋆ eiQ.X)(τ′), where
X represents the string coordinates on the brane, P andQ the momenta of the corresponding string states,
τ and τ′ parameterize the worldsheet boundary, and where the classical limit f
M
⋆ g→f.g is recovered for
B→ 0. It is not clear how this generalizes to an arbitrary curved string background supporting D-brane
conﬁgurations. Nevertherless, some particular examples have been tackled in the litterature. The SU(2)
WZW model for instance supports symmetric D-branes wrapping S2 spheres in the SU (2) group manifold.
It has been shown that in an appropriate limit the worldvolume of these branes are deformed into fuzzy
spheres [12, 13, 14, 15]. The latter fuzzy spheres can be related to the Berezin/geometric quantization of S2
hence to star product theory (see [16] and references therein). The appearance of noncommutative structures
was also pointed out in relation with other backgrounds, like the Melvin Universe [17, 18, 19, 20, 21, 22, 23]
or the Nappi-Witten plane wave [19, 24], see e.g. [25] for a recent review. Another model that has attracted
much attention in recent years is the SL(2 , R) WZW model, describing string propagation on AdS3 (and
its euclidian counterpart, the H+
3 model), see e.g. [26] and [27]. This model has played, and still plays an
important role in the understanding of string theory in non-compact and curved space-times. It appears as
ubiquitous when dealing with black holes in string theory and is also particularly important in connection
with the AdS/CFT correspondence. In this perspective, much eﬀort has been devoted in studying the D-
brane conﬁgurations this model can support (see e.g. [28]). The most simple and symmetric D-branes in
AdS3 turn out to wrapAdS2 andH2 spaces in the SL(2, R) group manifold. The question one could then ask
is: what is the low energy eﬀective dynamics of open string modes ending on such branes? By analogy with
the ﬂat case, it seems not unreasonable to expect a ﬁeld theory deﬁned on a noncommutative deformation of
the D-branes’ worldvolume. This deformation would have to enjoy some properties, namely to respect the
symmetries of the model, just like the Moyal product and the fuzzy sphere construction do in their respective
cases.
In the present paper, we will be concerned with the speciﬁc situation of formal and non-formal deformation
quantizations of the hyperbolic plane. In this particular case, a third motivation relies on the relevance of
the hyperbolic plane in the study of Riemann surfaces through the uniformization theorem (establishing the
hyperbolic plane D as the metric universal covering space of every constant curvature hyperbolic surface).
Therefore, invariant deformations of the Poincar´ e disk could constitute a step towards a spectral theory of
non-commutative Riemann surfaces.
