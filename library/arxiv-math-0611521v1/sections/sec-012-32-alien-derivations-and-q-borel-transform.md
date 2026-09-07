---
doc_id: arxiv-math-0611521v1
doc_title: "THE q-ANALOGUE OF THE WILD FUNDAMENTAL GROUP"
section_id: sec-012-32-alien-derivations-and-q-borel-transform
section_title: "Alien derivations and q-Borel transform"
section_number: 3.2
pages: 16-19
source_pdf: 0611521v1.pdf
source_sha256: 65fcd77b7b0a208e
doc_brief: "THE q-ANALOGUE OF THE WILD FUNDAMENTAL GROUP — We describe an explicit construction of galoisian Stokes op erators for irregular linear q-difference equations."
---
Let δ∈ N∗ and assume that the matrix A of (1) has only null blocks Ui,j for µ j− µi < δ. Then, in the
computation (3), we ﬁnd the following equation for µ j− µi < δ: σq ˆFi,jzµ jA j− zµiAi ˆFi,j = 0. Likewise, the
upper diagonal blocks of any Sc ˆFA satisfy exactly the same equations. These have no non trivia l formal
solution, neither non trivial meromorphic wih less than (µ j− µi) poles modulo qZ (this follows from 2.3).
Hence, as well ˆFA as all the summations Sc ˆFA have null blocks Fi,j for 0 < µ j− µi < δ.
On level µ j− µi = δ, the equations to be solved are:
σqFi,jzµ jA j− zµiAiFi,j = Ui,j,
which is of the same type as those of 2.3. The properties of thi s ﬁrst non trivial level of ˆFA and Sc ˆFA will
play a crucial role in [20]. Indeed, the logarithm logF has, as ﬁrst non trivial level the same levelδ, and the
corresponding diagonal is equal to that of F. Therefore, after taking residues, on gets straightaway the ˙∆(δ)
c .
To study it in some detail, we therefore take again the light notations of 2.3.
Solving (8) with q-Borel transforms. We consider δ∈ N∗ as ﬁxed, to alleviate notations. Let the Laurent
series expansion:
θδ = ∑
n∈Z
tnzn.
Then, from the functional equation σqθδ = zδθδ, we draw the recurrence relations:
∀n∈ Z ,tn−δ = qntn.
¿From this, we get the useful estimation:
tn≈| q|−n2/2δ.
The notation un≈ vn for positive sequences here means “same order of magnitude u p to a polynomial
factor”, more precisely:
un≈ vn⇐⇒∃ R > 0 : un = O(Rnvn) and vn = O(Rnun).
Now, for any Laurent series F(z) = ∑ Fnzn∈ E⊗ C[[z,z−1]] with coefﬁcients Fn in some ﬁnite dimensional
C-vector space E, we deﬁne its q-Borel transform at level δ by the formula:
B (δ)
q F(ξ) = ∑ t−nFnξn∈ E⊗ C[[ξ,ξ−1]].
This transformation strongly increases the convergence pr operties; for instance, if F∈ E⊗ C{z}, then
B (δ)
q F∈ E⊗ O(C), etc. Since we are interested in analyticity of B (δ)
q F, we introduce conditions on the
order of growth of coefﬁcients, adapted from [14]. Let G∈ E⊗ C((ξ)) = E⊗ C[[ξ]][ξ−1]. We say that
16
G := ∑ Gnξn∈ E⊗ C({ξ})q,δ if‖ Gn‖= O(Rnq−n2/2d) for some R > 0. We say that G∈ E⊗ C({ξ})q,(δ)
if‖ Gn‖= O(Rnq−n2/2d) for all R > 0. In the case that, moreover, G has no pole at 0 ( G∈ C[[ξ]]), we
respectively say that G∈ E⊗ C{ξ}q,δ, resp. G∈ E⊗ C{ξ}q,(δ). Thus, we have the obvious equivalences:
F∈ E⊗ C{z} ⇐⇒ B (δ)
q F∈ E⊗ C{ξ}q,δ,
F∈ E⊗ C({z}) ⇐⇒ B (δ)
q F∈ E⊗ C({ξ})q,δ,
F∈ E⊗ O(C) ⇐⇒ B (δ)
q F∈ E⊗ C{ξ}q,(δ),
F∈ E⊗ O(C)[z−1] ⇐⇒ B (δ)
q F∈ E⊗ C({ξ})q,(δ).
With the notations of equation (8), write G = B (δ)
q F = ∑ Gnξn and V = B (δ)
q U = ∑ Gnξn (so that Gn =
t−nFn and Vn = t−nUn). Then, multiplying relation (9) by t−n and noting that qn−δt−n = t−(n−δ), we get:
∀n∈ Z ,Gn−δ− Λ(Gn) = Vn.
Multiplying by ξn and summing for n∈ Z yields:
(ξδId− Λ)B (δ)
q F(ξ) = B (δ)
q U(ξ).
Since U has a positive radius of convergence, B (δ)
q U(ξ) is an entire function. For F to be a convergent
solution, it is necessary that B (δ)
q F be an entire function. We shall now appeal to linear algebra. We ﬁrst
write A = AsAu and B = BsBu the multiplicative Dunford decompositions. Then A1/δ
u and B1/δ
u are well
deﬁned. In order to deﬁne A1/δ
s and B1/δ
s , it is enough to choose a mappingx↦→x1/δ on C∗ and to apply it to
the eigenvalues. We then putA1/δ = A1/δ
s A1/δ
u , B1/δ = B1/δ
s B1/δ
u and get a linear mapL : F↦→A1/δF(B1/δ)−1,
which is a δth root of Λ. Call µδ the set of δth roots of 1 in C.
Lemma 3.7 Let E be a ﬁnite dimensional C-vector space, A an endomorphism of E and R be any of the
following algebras of functions: O(C); O(C)[ξ−1]; C{ξ}q,δ; C({ξ})q,δ; C{ξ}q,(δ); C({ξ})q,(δ). Then the
linear operator (ξδ− Aδ) maps injectively E⊗ R into itself, its image has a ﬁnite codimension δdimE and
there is an explicit projection formula on the supplementary space E⊕···⊕ Eξδ−1 of the image:
V↦→∑
j∈µδ
d( jA)δ−1Pj(A,ξ)V ( jA),
where Pj(A,ξ) and V( jA) respectively are the following linear operator and vector:
Pj(A,ξ) =
δ−1
∑
i=0
( jA)i ξδ−1−i, V ( jA) = ∑ ( jA)nVn∈ E, (where V = ∑ Vnξn is entire).
Proof. - The algebraic part of the proof rests on the following computation:
1 = ∑
j∈µδ
δ( ja)δ−1Pj(a,X), where Pj(a,X) = X δ− aδ
X− a =
δ−1
∑
i=0
( ja)i X δ−1−i.
17
¿From this, we draw:
V (ξ) = ∑
j∈µδ
δ( jA)δ−1Pj(A,ξ)V (ξ)
= ∑
j∈µδ
δ( jA)δ−1Pj(A,ξ)
(
V (ξ)−V ( jA)
)
+ ∑
j∈µδ
δ( jA)δ−1Pj(A,ξ)V ( jA);
then we note that, sincePj(A,ξ)(ξ− jA) = ξδ−Aδ, the ﬁrst term of the last right hand side is in the image of
the linear operator (ξδ− Aδ). The second term plainly belongs to the supplementary space E⊕···⊕ Eξδ−1.
Then, there are growth conditions on the coefﬁcients to be ch ecked. In the case of O(C); O(C)[ξ−1], they
are standard. In the case of C{ξ}q,δ, C({ξ})q,δ, C{ξ}q,(δ) and C({ξ})q,(δ), they follow from the estimations
given in the proof of lemma 2.9 of [28]. □
Theorem 3.8 With the notations of section 2.3, equation (8) has a converg ent solution if, and only if,
B (δ)
q U( jL) = 0 for all j∈ µδ. More precisely, the family
(
B (δ)
q U( jL)
)
j∈µδ
∈ Matr,s(C)µδ≃ Matr,s(C)δ is a
complete set of invariants for analytic classiﬁcation within the formal class M0.
Solving (8) with θ functions and residue invariants. ¿From the computations in the one level case of
2.3, we see that the only solution of (8) such that condition (5) holds is given by the explicit formula:
Fc(z) = 1
θδc
∑
n∈Z
(cδqnId− Λ)−1Vn zn, where V = θδ
cU.
A short computation shows that V = ∑ tpc−pUnzn+p, so that, V0 = ∑ t−ncnUn = B (δ)
q U(c).
In order to compute explicitly the alien derivation in the on e level case, it is convenient to normalize the
setting, by requiring that all eigenvalues of A and B lie in the fundamental annulus 1 ≤| z| <|q| (up to
shearing transformation, this is always possible). We may f urther decompose the pure blocks zµA and zνB
into their corresponding characteristic subspaces. In oth er words, we may (and shall) assume here that A
and B are block diagonal, each block Aα (resp. Bβ) have the unique eigenvalue α (resp. β), this lying in the
fundamental annulus. We write Λ α,β, Lα,β, Uα,β, and compute the corresponding component ˙∆(δ,α,β)
ξ (M) of
˙∆(δ)
ξ (M). Let ξ∈ C∗ be a prohibited (polar) value of c. This means that one of the matrices (ξδqnId− Λ α,β)
is singular, so that ξδqn = α/β. From the normalisation condition, we see that this can occu r only for one
value of n. Since residues are actually deﬁned on Eq, one can choose ξ such that the bad value ofn is n = 0.
Then, we are to compute:
˙∆(δ,α,β)
ξ (M) = Resc=ξ
1
θδc(a) (cδId− Λ α,β)−1B (δ)
q Uα,β(c).
Note that the arbitrary basepoint a∈ C∗ (which provides us with the ﬁber functor ˆω (0)
a ) appears only in the
theta factor. As in the previous section, we introduce Lα,β such that Lδ
α,β = Λ α,β and get, from the same
formulas as before:
˙∆(δ,α,β)
ξ (M) = Resc=ξ
1
θδc(a) ∑
j∈µδ
δ( jα,βL)δ−1(c− jLα,β)−1B (δ)
q Uα,β(c).
18
Now, ξ is an eigenvalue of one and only one of the jLα,β, call it Lξα,β. From classical “holomorphic
functional calculus” (see e.g. [25]), we get:
˙∆(δ,α,β)
ξ (M) = θ−δ(L−1
ξα,β) δLδ−1
ξα,β B (δ)
q Uα,β(Lξα,β).
Recall that, as in loc. cit., the theta factor is the application of a holomorphic function to a linear operator.
Theorem 3.9 Call Φ a the automorphism of Matr,s(C)µδ, which, on the (α,β) component, is left multiplica-
tion by θ−δ(L−1
ξα,β). Then Φ a sends the q-Borel invariant
(
B (δ)
q U( jL)
)
j∈µδ
to the ˙∆ invariant: L
ξ
˙∆(δ)
ξ (M).
Here is an example similar to that at the end of section 2.1. We take M =
( α u
0 βz
)
, where α,β∈ C∗
and u∈ C{z}. The slopes are µ = 0 and ν = 1 and the only level isδ = 1. The associated non homogeneous
equation is βzσq f− α f = u, which, in the Borel plane, becomes(βξ− α)B (1)
q f = B (1)
q u, and the obstruction
to ﬁnding an analytical solution is the complex number B (1)
q u(α/β). This is also the invariant associated to
the analytical class of M within its formal class.
On the side of resolution with θ and residues, we ﬁrst get: fc(z) = 1
θc
∑ n∈Z(cqn− αβ−1)−1 vn zn, where
v = θcu, then the only non trivial alien derivation, given for ξ = α/β:
˙∆(δ)
ξ = Resc=ξfc(a) = Resc=ξ
1
θc(a) (c− ξ)−1B (1)
q u(c) = 1
θ(a/ξ) B (1)
q u(ξ).
