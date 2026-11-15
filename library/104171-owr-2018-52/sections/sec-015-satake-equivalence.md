---
doc_id: 104171-owr-2018-52
doc_title: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018)"
section_id: sec-015-satake-equivalence
section_title: "Satake equivalence"
section_number: null
pages: 46-50
source_pdf: 10.4171-owr-2018-52.pdf
source_sha256: b33ed36eaa470877
toc_source: inferred
doc_brief: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018) — The workshop brought together experts investigating algebraic Lie theory from the geometric and categorical"
---
Michael Finkelberg
(joint work with Vasily Krylov)
0.1. Let Λ = L
n Λn be the ring of symmetric functions equipped with the base
of Schur functions sλ. It also carries a natural coproduct. The classical Schubert
calculus is the based isomorphism of the bialgebra Λ with H•(Gr, Z) (doubling the
degrees) taking sλ to the fundamental class of the corresponding Schubert variety
σλ. Here Gr is the inﬁnite Grassmannian Gr = lim
→Gr(k, m) ≃BU(∞), and the
coproduct on H•(Gr, Z) comes from the H-space structure on the classifying space
BU(∞).
Enveloping Algebras and Geometric Representation Theory
3127
Here is a more algebraic geometric construction of the coproduct on H•(Gr, Z).
We have H2n(Gr, Z) = H2n(Schn, Z) = H2n
c (Schn, Z) = H2n
c (Schn, Z) where
Schn ⊂Gr (resp. Schn ⊂Gr) stands for the union of all n-dimensional (resp.
≤n-dimensional) Schubert cells (with respect to a ﬁxed ﬂag).
Recall the Calogero-Moser phase space Cn: the space of pairs of n × n-matrices
(X, Y ) such that [X, Y ] + Id has rank 1, modulo the simultaneous conjugation of
X, Y . The integrable system πn : Cn →A(n) takes (X, Y ) to the spectrum of X.
Wilson [10] has discovered the following two key properties of the Calogero-Moser
integrable system:
(a) for n1 + n2 = n, a factorization isomorphism
Cn ×A(n) (A(n1) × A(n2))disj
∼
−→(Cn1 × Cn2) ×(A(n1)×A(n2)) (A(n1) × A(n2))disj.
(b) For x ∈A1, an isomorphism π−1
n (n · x)
∼
−→Schn.
Now the desired coproduct
∆=
M
n1+n2=n
∆n1,n2 : H2n
c (Schn, Z) →
M
n1+n2=n
H2n1
c
(Schn1, Z) ⊗H2n2
c
(Schn2, Z)
is nothing but the cospecialization1 morphism for the compactly supported coho-
mology of the ﬁbers of πn restricted to the subfamily π−1
n (n1 · x + n2 · y) ⊂Cn
(from the ﬁbers over the diagonal x = y to the oﬀ-diagonal ﬁbers x̸ = y), cf. [5].
0.2. Given a reductive complex algebraic group G, Schieder [9] constructed a
bialgebra A playing the role of L
n H2n
c (Schn, C) for the aﬃne Grassmannian GrG
in place of Gr. In order to explain his construction, we set up the basic notations
for G and GrG.
We ﬁx a Borel and a Cartan subgroup G ⊃B ⊃T , and denote by W the Weyl
group of (G, T ). Let N denote the unipotent radical of the Borel B, and let N−
stand for the unipotent radical of the opposite Borel B−. Let Λ (resp. Λ∨) be
the coweight (resp. weight) lattice, and let Λ+ ⊂Λ (resp. Λ∨+ ⊂Λ∨) be the cone
of dominant coweights (resp. weights). Let also Λ+ ⊂Λ (resp. Λ∨
+ ⊂Λ∨) be the
submonoid spanned by the simple coroots (resp. roots) αi, i ∈I (resp. α∨
i, i ∈I).
We denote by G∨⊃T ∨the Langlands dual group, so that Λ (resp. Λ∨) is the
weight (resp. coweight) lattice of G∨.
Let O denote the formal power series ring C[[z]], and let K denote its fraction
ﬁeld C((z)). The aﬃne Grassmannian GrG = GK/GO is an ind-projective scheme,
the union F
λ∈Λ+ Grλ
G of GO-orbits. The closure of Grλ
G is a projective variety
Grλ
G = F
µ≤λ Grµ
G. The ﬁxed point set GrT
G is naturally identiﬁed with the coweight
lattice Λ; and µ ∈Λ lies in Grλ
G iﬀµ ∈Wλ.
For a coweight ν ∈Λ = GrT
G, we denote by Sν ⊂GrG (resp. Tν ⊂GrG) the orbit
of N(K) (resp. of N−(K)) through ν. The intersections Sν ∩Grλ
G (resp. Tν ∩Grλ
G)
are the attractors (resp. repellents) of C× acting via its homomorphism 2ρ to the
Cartan torus T acting on Grλ
G : Sν ∩Grλ
G = {x ∈Grλ
G : lim
c→0 2ρ(c) · x = ν} and
1terminology of [9, 6.2.7].
3128
Oberwolfach Report 52/2018
Tν ∩Grλ
G = {x ∈Grλ
G : lim
c→∞2ρ(c)·x = ν}. Going to the limit GrG = lim
λ∈Λ+ Grλ
G, Sν
(resp. Tν) is the attractor (resp. repellent) of ν in GrG. The closure Sν is the union
F
µ≤ν Sµ, while T ν = F
µ≥ν Tµ.
Deﬁnition 1. (a) For θ ∈Λ+ we denote by Schθ (resp. Schθ) the intersection
Sθ ∩T0 (resp. Sθ ∩T 0).2 It is equidimensional of dimension ⟨ρ∨, θ⟩.
(b) We set Aθ := H⟨2ρ∨,θ⟩
c
(Schθ, C) = H⟨2ρ∨,θ⟩
c
(Schθ, C), and A := L
θ∈Λ+ Aθ.
Given a smooth curve X and θ ∈Λ+, the open zastava space
◦
Zθ (see e.g. [2])
is equipped with the projection πθ :
◦
Zθ →Xθ to the degree θ conﬁguration space
of X. It enjoys the factorization property, and for any x ∈X, we have a canonical
isomorphism π−1
θ (θ · x)
∼
−→Schθ. Given θ1, θ2 ∈Λ+ such that θ1 + θ2 = θ, the
coproduct ∆θ1,θ2 : Aθ →Aθ1⊗Aθ2 is deﬁned just like in 0.1 via the cospecialization
morphism for the subfamily π−1
θ (θ1 · x + θ2 · y).
To construct the product m: L
θ1+θ2=θ Aθ1 ⊗Aθ2 →Aθ we need the Drinfeld-
Gaitsgory interpolation g
Schθ →A1 [4] constructed with respect to the C×-action
on Schθ arising from the cocharacter 2ρ of T . The key property of g
Schθ →A1 is
that the ﬁbers over a̸ = 0 are all isomorphic to Schθ, while the zero ﬁber (g
Schθ)0
is isomorphic to the disjoint union F
λ
Sch+,λ
θ
× Sch−,λ
θ
.
Here λ (a coweight in
Λ+ such that λ ≤θ) runs through the set of C×-ﬁxed points of Schθ, and Sch+,λ
θ
(resp. Sch−,λ
θ
) stands for the corresponding attractor (resp. repellent). It is easy to
see that H⟨2ρ∨,θ⟩
c
((g
Schθ)0, C) = L
θ1+θ2=θ H⟨2ρ∨,θ1⟩
c
(Schθ1, C)⊗H⟨2ρ∨,θ2⟩
c
(Schθ2, C),
and the desired product m is nothing but the cospecialization morphism for the
compactly supported cohomology of the ﬁbers of the Drinfeld-Gaitsgory family.
Schieder conjectured that the bialgebra A is isomorphic to the universal en-
veloping algebra U(n∨) of Lie(N ∨) where N ∨⊂B∨⊂G∨is the unipotent radical
of Borel subgroup of G∨. The goal of the present work is a proof of Schieder’s
conjecture.
0.3. In order to produce an isomorphism A
∼
−→U(n∨), we construct an action of
A on the geometric Satake ﬁber functor. More precisely, we denote by rν,+ (resp.
rν,−) the locally closed embedding Sν֒ →GrG (resp. Tν֒ →GrG). We also denote
by ιν,+ (resp. ιν,−) the closed embedding of the point ν into Sν (resp. into Tν).
According to [1, 4], there is a canonical isomorphism of functors ι∗
ν,−r!
ν,−≃
ι!
ν,+r∗
ν,+ : Db
GO(GrG) →Db(Vect).
For a sheaf P ∈Db
GO(GrG), its hyperbolic
stalk at ν is deﬁned as Φν(P) := ι∗
ν,−r!
ν,−P ≃ι!
ν,+r∗
ν,+P. According to [8], for
P ∈PervGO(GrG), the hyperbolic stalk Φν(P) is concentrated in degree ⟨2ρ∨, ν⟩,
and there is a canonical direct sum decomposition H•(GrG, P) = L
ν∈Λ Φν(P).
Moreover, the abelian category PervGO(GrG) is monoidal with respect to the con-
volution operation ⋆, and the functor H•(GrG, −): (PervGO(GrG), ⋆) →(Vect, ⊗)
2Here Sch stands for Schieder.
Enveloping Algebras and Geometric Representation Theory
3129
is a ﬁber functor identifying (PervGO(GrG), ⋆) with the tensor category Rep(G∨)
(geometric Satake equivalence).
We deﬁne a morphism of functors Aθ ⊗Φν →Φν+θ. To this end (and also in
order to check various tensor compatibilities) we consider the Drinfeld-Gaitsgory-
Vinberg interpolation Grassmannian: a relative compactiﬁcation VinGrprinc
G
of the
Drinfeld-Gaitsgory interpolation f
GrG →A1. We also consider an extended version
VinGrG →T +
ad := Spec C[Λ∨
+] and its version VinGrG,Xn for the Beilinson-Drinfeld
Grassmannian. It was implicit already in Schieder’s work, and it was made explicit
by D. Gaitsgory (private communication, cf. an earlier work [6]). We believe it
is a very interesting object in its own right.
For example, let ω ∈Λ+ be a
minuscule dominant coweight. Then the Schubert variety Grω
G is isomorphic to a
parabolic ﬂag variety G/Pω, and the corresponding subvariety VinGrω
G of VinGrG
is isomorphic to Brion’s degeneration of ∆G/Pω in Hilb(G/Pω × G/Pω) × T +
ad [3,
§3].
Remark.
(a) By the geometric Satake equivalence, for P ∈PervGO(GrG),
the cohomology H•(GrG, P) is equipped with an action of U(g∨).
For exam-
ple, the action of the Cartan subalgebra U(t∨) ⊂U(g∨) comes from the grading
H•(GrG, P) = L
ν∈Λ Φν(P). The action of U(n∨) comes from the geometric ac-
tion of the Schieder bialgebra A on the geometric Satake ﬁber functor, and the
isomorphism A
∼
−→U(n∨). Finally, the action of U(n∨
−) is conjugate to the action
of U(n∨) with respect to the Lefschetz bilinear form on H•(GrG, P).
(b) By construction, the Schieder algebra A comes equipped with a basis (fun-
damental classes of irreducible components of Schθ). On the other hand, U(n∨)
is equipped with the semicanonical basis [7].3
In the simplest example when
G = SL(2), A is N-graded, and each graded component An is one-dimensional
with the basis vector en; one can check enem =
 n+m
n

en+m. Hence the two bases
match under the isomorphism A
∼
−→U(n∨). However, J. Kamnitzer has checked
recently that for G = SL(6) the two bases do not match. Thus the Higgs branch
realization [7] of U(n∨) is diﬀerent from the Coulomb branch realization [9] of
U(n∨).
References
[1] T. Braden, Hyperbolic localization of intersection cohomology, Transform. Groups 8 (2003),
209–216.
[2] A. Braverman, M. Finkelberg, D. Gaitsgory and I. Mirkovi´c, Intersection cohomology of
Drinfeld’s compactiﬁcations, Selecta Math. 8 (2002), no. 3, 381–418. Erratum: Selecta Math.
10 (2004), no. 3, 429–430.
[3] M. Brion, Group completions via Hilbert schemes, J. Algebraic Geom. 12 (2003), no. 4,
605–626.
[4] V. Drinfeld, D. Gaitsgory, On a theorem of Braden, Transform. Groups 19 (2014), 313–358.
[5] M. Finkelberg, V. Ginzburg, Calogero-Moser space and Kostka polynomials, Adv. Math.
172 (2002), no. 1, 137–150.
[6] D. Gaitsgory, D. Nadler, Spherical varieties and Langlands duality, Mosc. Math. J. 10
(2010), no. 1, 65–137.
3constructed under the assumption that G is simply laced.
3130
Oberwolfach Report 52/2018
[7] G. Lusztig, Semicanonical bases arising from enveloping algebras, Adv. Math. 151 (2000),
no. 2, 129–139.
[8] I. Mirkovi´c, K. Vilonen, Geometric Langlands duality and representations of algebraic groups
over commutative rings, Ann. of Math. (2) 166 (2007), no. 1, 95–143.
[9] S. Schieder, Monodromy and Vinberg fusion for the principal degeneration of the space of
G-bundles, arXiv:1701.01898.
[10] G. Wilson, Collisions of Calogero-Moser particles and an adelic Grassmannian, Invent.
Math. 133 (1998), 1–41.
