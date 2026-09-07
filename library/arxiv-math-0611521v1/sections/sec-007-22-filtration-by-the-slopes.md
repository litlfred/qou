---
doc_id: arxiv-math-0611521v1
doc_title: "THE q-ANALOGUE OF THE WILD FUNDAMENTAL GROUP"
section_id: sec-007-22-filtration-by-the-slopes
section_title: "Filtration by the slopes"
section_number: 2.2
pages: 10-12
source_pdf: 0611521v1.pdf
source_sha256: 65fcd77b7b0a208e
doc_brief: "THE q-ANALOGUE OF THE WILD FUNDAMENTAL GROUP — We describe an explicit construction of galoisian Stokes op erators for irregular linear q-difference equations."
---
The ﬁltration and the associated graded module. The module M is said to be pure isoclinic of slope
µ if S(M) ={µ} and fuchsian if moreover µ = 0. Direct sums of pure isoclinic modules are called pure
modules 2: they are irregular objects without wild monodromy, as foll ows from [21] and [28]. The tan-
nakian subcategory of E (0) made up of pure modules is calledE (0)
p . Modules with integral slopes also form
tannakian subcategories, which we write E (0)
1 and E (0)
p,1.
It was proved in [26] that the category E (0)
f of fuchsian modules is equivalent to the category of ﬂat holo-
morphic vector bundles over Eq and that its Galois group G(0)
f is isomorphic to Homgr(C∗/qZ,C∗)× C
(here, as in the introduction, Homgr means “morphisms of abstract groups”). Since objects of E (0)
p,1 are
essentially Z-graded objects with fuchsian components, the Galois group of E (0)
p,1 is G(0)
p,1 = C∗× G(0)
f .
Theorem 2.2 [27] Let the letter K stand for the ﬁeld C({z}) (convergent case) or the ﬁeld C((z)) (formal
case). In any case, any object M of Di f f Mod(K,σq) admits a unique ﬁltration (F≤µ(M))µ∈Q by subobjects
such that each F (µ)(M) = F≤µ(M)
F<µ(M) is pure of slope µ (thus of rank r M(µ)). The F (µ) are endofunctors of
Di f f Mod(K,σq) and gr = LF(µ) is a faithful exact C-linear⊗-compatible functor and a retraction of
the inclusion of E (0)
p into E (0). In particular, the functor gr retracts E (0)
1 to E (0)
p,1.In the formal case, gr is
isomorphic to the identity functor.
Corollary 2.3 For each a∈ C∗, the functor ˆω (0)
a = ω (0)
a ◦ gr is a ﬁber functor.
We shall consistently select an arbitrary basepointa∈ C∗ and identify the Galois groupG(0) as Aut⊗( ˆω (0)
a
)
.
Corollary 2.4 The Galois group G(0) of E (0) is the semi-direct product St ⋊ G(0)
p of the Galois group G(0)
p
of E (0)
p by a prounipotent group, the Stokes group St.
From now on, we only consider modules with integral slopes.
Further studies would have to be based on the work [11] by van der Put and Reversat.
Description in matrix terms. We now introduce notational conventions which will be used all along this
paper for a module M in E (0)
1 and its associated graded module M0 = gr(M), an object of E (0)
p,1. The module
M may be given the shape M = (C({z})n,Φ A), with:
(1) A = AU =
de f


zµ1A1 . . . . . . . . . . . .
. . . . . . . . . Ui,j . . .
0 . . . . . . . . . . . .
. . . 0 . . . . . . . . .
0 . . . 0 . . . zµkAk


,
2It should be noted that we call in the present paper a pure isoc linic (resp. pure) module what was called a pure (resp. tamel y
irregular) module in previous papers.
10
where the slopes µ1 <··· < µk are integers, ri∈ N∗, Ai∈ GLri(C) (i = 1, . . . ,k) and
U = (Ui,j)1≤i< j≤k∈ ∏
1≤i< j≤k
Matri,r j (C({z})).
The associated graded module is then a direct sumM0 = P1⊕···⊕ Pk, where, for 1≤ i < j≤ k, the module
Pi is pure of rank ri and slope µi and can be put into the form Pi = (C({z})ri,Φ zµiAi ). Therefore, one has
M0 = (C({z})n,Φ A0 ), where the matrix A0 is block-diagonal (it is the same as AU, with all Ui,j = 0).
We write G⊂ GLn for the algebraic subgroup and g for its Lie algebra, made up of matrices of the form:
(2) F =


Ir1 . . . . . . . . . . . .
. . . . . . . . .Fi,j . . .
0 . . . . . . . . . . . .
. . . 0 . . . . . . . . .
0 . . . 0 . . . Irk


and f =


0r1 . . . . . . . . . . . .
. . . . . . . . . Fi,j . . .
0 . . . . . . . . . . . .
. . . 0 . . . . . . . . .
0 . . . 0 . . . 0rk


.
For F in G, we shall write F[A] = (σqF)AF−1 the result of the gauge transformation F on the matrix A.
Theorem 2.2 entails:
∀(Ui,j)1≤i< j≤k∈ ∏
1≤i< j≤k
Matri,r j (C({z})) ,∃! ˆF∈ G(C((z))) : ˆF[A0] = AU .
This ˆF will be written ˆFA (where A = AU). The blocks ˆFi,j are recursively computed as follows. For j < i,
ˆFi,j = 0. For j = i, ˆFi,j = Iri. Then, for j > i, one must solve the non homogeneous ﬁrst order equation:
(3) σq ˆFi,jzµ jA j− zµiAi ˆFi,j = ∑
i<k< j
Ui,k ˆFk,j +Ui,j.
Description of the Stokes group. To go further, we choose to ﬁx an arbitrary basepoint a∈ C∗ (see the
corollary to theorem 2.2) and we identify the Galois groups accordingly:
G(0)
1 =
de f
Gal(E (0)
1 ) = Aut⊗( ˆω (0)
a ).
Recall from the quoted papers the action of the pure componen t G(0)
p,1 = C∗× Homgr(C∗/qZ,C∗)× C. We
keep the notations above. For any A with graded part A0, an element (α,γ,λ)∈ G(0)
p,1 yields the automor-
phism of ˆω (0)
a (A) = ω (0)
a (A0) = Cn given by the matrix:


αµ1γ(As,1)Aλ
u,1 . . . . . . . . . . . .
. . . . . . . . . 0 . . .
0 . . . . . . . . . . . .
. . . 0 . . . . . . . . .
0 . . . 0 . . . αµk γ(As,k)Aλ
u,k


,
where we have written Ai = As,iAu,i the multiplicative Dunford decomposition (into a semi-sim ple and a
unipotent factor that commute) and γacts on a semi-simple matrix through its eigenvalues. These matrices
generate the group G(0)
p,1(A)⊂ GLn(C).
11
We then have a semi-direct decomposition:G(0)
1 = St ⋊G(0)
