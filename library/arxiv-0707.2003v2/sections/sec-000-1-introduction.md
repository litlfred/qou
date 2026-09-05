---
doc_id: arxiv-0707.2003v2
doc_title: "A geometric model for Hochschild homology of Soergel bimodules BEN WEBSTER GEORDIE WILLIAMSON School of Mathematics Mathematisches Institut Institute for Advanced Study der Univers"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 0707.2003v2.pdf
source_sha256: 0b8fe37aabeee412
doc_brief: "A geometric model for Hochschild homology of Soergel bimodules BEN WEBSTER GEORDIE WILLIAMSON School of Mathematics Mathematisches Institut Institute for Advanced Study der Universität Freiburg — An"
---
In this paper, we consider the Hochschild homology of Soerge l bimodules,
and construct a geometric interpretation of it. This will al low us to explicitly
compute the Hochschild homology of a special class of Soerge l bimodules.
Soergel bimodules are bimodules over a polynomial ring, whi ch appear natu-
rally both in the study of perverse sheaves on ﬂag varieties a nd of the semiring
of projective functors on the BGG category O. Recently interest in them has
been rekindled by the appearance of connections with link homology as shown
by Khovanov [Kh].
Khovanov’s work showed that one aspect of Soergel bimodules w hich had not
been carefully studied up to that date was, in fact, of great i mportance: their
Hochschild homology . While the operation of taking Hochsch ild homology is
1
hard to motivate from a representation theoretic perspecti ve, we argue that it
is, in fact, naturally geometric, rather than purely combin atorial/algebraic.
Let G be a connected reductive complex algebraic group, with Lie a lgebra
g. Let B be a Borel of G, T a Cartan subgroup of G, t be its Lie algebra,
n = dim T be the rank of G, and W = NG(T )/T be the Weyl group of G. For
any w∈ W , we let Gw = BwB . Note that T is a deformation retract of B , so,
we have H ∗
B(X)∼= H ∗
T (X) for all B -spaces X . We will freely switch between
B - and T -equivariant cohomology throughout this paper.
We note that Gw is a closed subvariety of G which is smooth if and only if
the corresponding Schubert variety Bw⊂ G/B =B is (and thus Gw typically
singular). Note that B× B acts on Gw by left and right multiplication, and
that restricting to the diagonal, we get the action of B by conjugation. Of
course, we also have left and right actions of B but we will never consider
these separately . We willalways mean the conjugation action.
Now consider the graded ring S = H ∗
T (pt, C) = C[t∗], which is endowed with
the obvious W -action. Given a simple reﬂection s, denote by Rs the bimodule
S⊗Ss S[1] where Ss is the subring of invariants under the reﬂection s and, by
convention, [a] denotes the grading shift (M [a])i = M i+a .
We now come to the deﬁnition of Soergel bimodules:
Deﬁnition 1 A Soergel bimodule is (up to grading shift) a direct summand
of the tensor product Ri = Rs⊗S Rt⊗S···⊗ S Ru in the category of graded
S -bimodules, where i = ( s, t, . . . , u) is a sequence of (not necessarily distinct)
simple reﬂections.
The motivation for studying Soergel bimodules comes from re presentation
theory , geometry and connections between the two. In fact, o ne has the fol-
lowing theorem:
Theorem 1.1 (Soergel) The indecomposable Soergel bimodules are parame-
terized (up to a shift in the grading) by the Weyl group [So4, S atz 6.14].
The irreducible Soergel bimodule corresponding to w∈ W may be obtained
as Rw∼= IH∗
B×B(Gw) [So3, Lemma 5], where IH∗ denotes intersection coho-
mology as deﬁned by Goresky and MacPherson [GM].
We choose our grading conventions on IH∗ so that the 0th degree is the mirror
of Poincar´ e duality , that is, so that the lowest degree component of Rw sits in
degree−ℓ(w).
2
More generally , Soergel bimodules can be identiﬁed with the B×B -equivariant
hypercohomology H∗
B×B(G,F) of sumsF of shifts of B×B -equivariant semi-
simple perverse sheaves on G.
Our central result is a geometric description of Hochschild homology HH∗(−)
of these modules.
Theorem 1.2 LetF be a semi-simple B× B -equivariant perverse sheaf on G
and let R be its B× B -equivariant cohomology . Then
HH∗(R)∼= H∗
B(G,F),
where B acts by conjugation (i.e., by the diagonal inclusion֒→B× B ). In
particular, we have
HH∗(Rw)∼= IH∗
B(Gw).
Unfortunately ,IH∗
B(Gw) has a single grading, whereas HH∗(Rw) has two: by
decomposition into the components HHi (“the Hochschild grading”), and one
coming from the grading on Rw (“the polynomial grading”). This isomor-
phism takes the single grading on IH∗
B(Gw) to the difference of the two grad-
ings on HH∗(Rw).
We can give a geometric interpretation of these gradings, bu t in a somewhat
roundabout manner. A result of Rasmussen [Ra] shows that
Theorem 1.3 Assume G = SL( n) or GL(n). Then IC(Gw) is equivariantly
formal. Thus, the map
i∗
T : IH∗
T (Gw)→ H∗
T (T, IC(Gw))∼= H ∗
T (T )⊗ IC(Gw)e
is injective and an isomorphism after tensoring with the fra ction ﬁeld of S .
Furthermore, since H ∗
T (T, IC(Gw))∼= S⊗C H ∗(T, IC(Gw)) by the K ¨ unneth
theorem, we can equip this S module with a bigrading, with an “equivariant”
grading from the ﬁrst factor, and a “topological” grading fro m the second.
Theorem 1.4 The intersection cohomology IH∗
B(Gw) obtains “topological”
and “equivariant” gradings by transport of structure from t he map i∗ and
HH∗(Rw) obtains the same by the isomorphism of Theorem 1.2. These are
related to the “Hochschild” and “polynomial” gradings by
degt(γ) = deg h(γ) deg e(γ) = deg p(γ)− 2 degh(γ)
where deg∗(x) denotes the degree of x in the grading whose name begins with
the letter∗.
3
The case where Gw is smooth is of special interest to us, so any reader who is
unhappy with the presence of intersection cohomology and pe rverse sheaves
can restrict to that case, in which case intersection cohomo logy is canonically
isomorphic to ˇCech cohomology .
Theorem 1.5 If Gw is smooth (in any type), then the Hochschild homology of
Rw is of the form
HH∗(Rw) =∧•(γ1, . . . , γn)⊗C S
where{γi}i=1,...,m are generators with
degh(γi) = 1 deg p(γi) = 2 ki
for positive integers ki determined by the geometry of Gw .
These integers can be calculated using the action of w on the root system, or
in SL(n) by presenting Gw/B as an iterated Grassmannian bundle.
While the indecomposable modules Rw are perhaps most natural from the
perspective of geometry or representation theory , deﬁnitio n (1) (and the study
of knot homology , which we discuss brieﬂy in Section 2) encou rages us to
concentrate on the modules Ri . We call these particular Soergel bimodules
Bott-Samelson for reasons which will be clariﬁed in Section 5.
Bott-Samelson modules are naturally identiﬁed with the equi variant homol-
ogy of the “groupy” Bott-Samelson space
Gi∼= Ps×B Pt×B···× B Pu.
and essentially the analogues of all appropriate theorems c onnecting the B×
B -orbit closures in G with Soergel bimodules are true here.
Theorem 1.6 If G = SL(n) or GL(n), then for all i, we have
Ri∼= H ∗
B×B(Gi) HH∗(Ri)∼= H ∗
B(Gi).
The T -conjugation on Gi is equivariantly formal, and the injection
i∗
T : H ∗
T (Gi)→ H ∗
T (GT
i )
induces a bigrading on H ∗
T (Gi) matching that on HH∗(Ri) as in Theorem 1.4.
The structure of the paper is as follows: In Section 2, we discuss the importance
of the Hochschild homology of Soergel bimodules in knot theo ry . In Section 4,
we prove Theorem 1.2, using the formalism of dg-modules, the relevant points
of which we will summarize in Section 3. In Section 5, we will c over in more
detail how to construct Soergel bimodules as equivariant in tersection coho-
mology of various varieties. Finally , in Section 6, we prove Theorems 1.3 – 1.6.
4
