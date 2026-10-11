---
doc_id: arxiv-2401.00636v2
doc_title: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS"
section_id: sec-019-51-kz-connections
section_title: "KZ connections"
section_number: 5.1
pages: 18-22
source_pdf: 2401.00636v2.pdf
source_sha256: 35e372d04cedf234
toc_source: outline
doc_brief: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS — We introduce a new notion of a periodic pencil of ﬂat connections on a smooth algebraic variety X."
---
5.1.1. KZ connections for ﬁnite dimensional simple Lie algebras. Let g be a ﬁnite dimen-
sional simple Lie algebra over C with triangular decomposition g = n−⊕h ⊕n+ and root
system R ⊂h∗, and let {hi} be the Chevalley basis of h. Let Ω∈(S2g)g be the Casimir
tensor of g corresponding to the invariant inner product (, ) on g∗under which short roots
of g have squared length 2:
Ω=
rank(g)
X
i=1
hi ⊗h∗
i +
X
α∈R
eα ⊗e−α,
where h∗
i is the dual basis of h under (, ) and eα are suitably normalized root elements of g.
Let V1, ..., Vr be representations of g from category O with rational weights. Then for any
rational weight µ ∈h∗the weight subspace (V1 ⊗... ⊗Vr)[µ] is ﬁnite dimensional. The KZ
connection on X = Cr \ diagonals with values in (V1 ⊗... ⊗Vr)[µ] has the form
(5.1)
∇(ℏ) := d −ℏ
r
X
i=1
 X
j̸=i
Ωij
xi −xj
!
dxi,
where Ωij is Ωacting in the i-th and j-th factor. It is easy to see that this connection has
regular singularities.
By the Drinfeld-Kohno theorem ([Dr],[EK])4, the monodromy of ∇(ℏ) for all ℏexcept
possibly a countable set is given by R-matrices of the quantum group Uq(g), where q = eπiℏ.
So, given that the weights of Vj are rational, the monodromy depends on eπiℏ/T, where T is
the common denominator of the weights of Vj.
Variants of this construction include restricting the KZ connection to singular vectors (i.e.,
n+-invariants in (V1 ⊗... ⊗Vr)[µ]) or, for µ = 0, g-invariants.
This example can be generalized in several directions described in the following subsections,
which gives many more examples of pencils of regular ﬂat connections that turn out to be
quasi-motivic.
4At the end of [Dr], Drinfeld claims this theorem for ﬁnite dimensional representations of g, but the proof
applies to the more general case of category O using the result of [EK] that the Etingof-Kazhdan functorial
quantization of a simple Lie algebra with its standard quasitriangular structure is isomorphic to the usual
Drinfeld-Jimbo quantization (for formal ℏ).
PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS
19
5.1.2. KZ connections for Kac-Moody algebras. In 5.1.1, the Lie algebra g may be replaced
with a symmetrizable Kac-Moody algebra g(A) for a generalized Cartan matrix A, or, more
generally, with the Lie algebra eg(A) without Serre relations attached to a rational matrix A
(see [V]). In this case, the relevant version of the Drinfeld-Kohno theorem is proved in [V]
(for Verma modules and integrable modules) and [EK] (in general).
5.1.3. Multiparameter KZ connections. We may consider a multiparameter version of the
pencil 5.1.1. For simplicity consider the case when Vi = M(λi) are Verma modules with
highest weights λi ∈h∗, and µ = Pr
i=1 λi −β, where β ∈Q+. In this case, we have a natural
identiﬁcation
(V1 ⊗... ⊗Vr)[µ] ∼=
M
β1,...,βr:Pr
i=1 βi=β
r
O
i=1
U(n−)[βi].
Realizing M(λ) ⊗M(µ) as U(n−) ⊗U(n−), we can write the operator Ωon M(λ) ⊗M(µ) as
Ω= (λ, µ) + Q +
X
k
λ(hk)P 12
k +
X
k
µ(hk)P 21
k ,
where Q, Pk do not depend on λ, µ and have rational coeﬃcients. It follows that the KZ
connection can be written as
∇= d −ℏ
r
X
i=1
 X
j̸=i
(λi, λj) + Qij + P
k λi(hk)(P ij
k + P ji
k )
xi −xj
!
dxi.
Deﬁne the modiﬁed KZ connection by conjugating ∇by the multivalued analytic function
ψ0 = Q
i<j(xi −xj)ℏ(λi,λj):
∇∗= d −ℏ
r
X
i=1
 X
j̸=i
Qij + P
k λi(hk)(P ij
k + P ji
k )
xi −xj
!
dxi.
Now we can deﬁne s to be the vector with coordinates s0 := ℏand sjk := ℏλj(hk), and we
get a pencil of ﬂat connections ∇∗(s). Moreover, the Drinfeld-Kohno theorem ([Dr],[EK])
implies that the monodromy of this pencil depends on q = eπiℏand eπisjk = qλj(hk).
Example 5.1. Let g = sl2. In this case we have M(λ) = C[f]vλ ∼= C[z]. Thus, setting
∂= ∂z, we have Ω= 1
2h ⊗h + e ⊗f + f ⊗e, so by direct computation we obtain
Ω|M(λ)⊗M(µ) = 1
2λµ + λ(∂⊗z −1 ⊗z∂) + µ(z ⊗∂−z∂⊗1) −z∂2 ⊗1 −1 ⊗z∂2.
Thus
P = ∂⊗z −1 ⊗z∂, Q = −z∂2 ⊗1 −1 ⊗z∂2.
Example 5.2. Consider the multiparameter KZ pencil for g = sl2 in the vector space
(M(λ1) ⊗... ⊗M(λr))[Pr
j=1 λj −2] ∼= Cr. Let sj := ℏλj. Then from Example 5.1 we get
that the KZ equations for a ﬂat section I(s, x) = (I1(s, x), ..., Ir(s, x)) of ∇(s) (conjugated
by ψ0) have the form
(5.2)
∂Ij
∂xi
= si
Ii −Ij
xi −xj
, j̸ = i;
∂Ii
∂xi
= −
X
j̸=i
sj
Ii −Ij
xi −xj
.
(In this special case the KZ connection does not explicitly depend on ℏbut only depends
on sj, because Q = 0). We have a ∇(s)-invariant decomposition Cr = C1 ⊕Vs, where
20
PAVEL ETINGOF AND ALEXANDER VARCHENKO
1 = (1, ..., 1) and Vs is the orthogonal complement to s. Thus the shift operators Ak should
decompose accordingly as
Ak(s, x) = A0
k(s, x) ⊕ξk(s)(1 ⊗sT),
where ξk are scalar rational functions and
A0
k(s, x)1 = 0, A0
k(s, x)(Vs) ⊂Vs+ek.
Then A0
k is uniquely determined up to scaling by a rational function of s.
To compute A0
k, note that by deﬁnition A0
k(s, x) expresses ﬂat sections of ∇(s + ek) via
ﬂat sections of ∇(s). Now, ﬂat sections of ∇(s) are solutions of (5.2), so they have the form
Ii(x, s) =
Z
Φ(t, s, x)
dt
t −xi
,
where
Φ(t, s, x) :=
rY
j=1
(t −xj)−sj
is the master function, and integration is over a suitable twisted cycle (see e.g. [EFK], 4.3).
Thus for i̸ = k, we get by a direct computation
Ii(s + ek, x) =
Z
Φ(t, s, x)
1
(t −xk)(t −xi)dt = Ii(s, x) −Ik(s, x)
xi −xk
.
and
Ik(s + ek, x) =
Z
Φ(t, s, x)
1
(t −xk)2dt = −
X
i̸=k
si
sk + 1
Ii(s, x) −Ik(s, x)
xi −xk
.
This yields the following formula for A0
k:
A0
k(s, x) =
X
i̸=k
(sk + 1)(Eii −Eik) + si(Ekk −Eki)
xi −xk
,
where Eij are the elementary matrices.
Remark 5.3. The discussion of this subsection applies mutatis mutandis to the setting of
5.1.2. Moreover, one may consider the case of a generic complex matrix A and Lie algebra
eg(A) without Serre relations. In this case the entries aij of A multiplied by ℏshould become
parameters of the pencil (which can be done since the KZ connection is linear in aij).
Remark 5.4. The integral formulas for solutions of KZ equations given in [SV],[V] imply
that the pencils in 5.1.1, 5.1.2,5.1.3 are actually motivic (not just quasi-motivic).
5.1.4. KZ connections in the Deligne category. For t ∈C let Rep(GLt) be the (abelian)
Deligne category ([EGNO], Section 9.12), and let V = [1, 0] be the generating object (the
“vector representation”). Consider the space Hom(1, V ⊗m ⊗V ∗⊗m) = End(V ⊗m). By the
Schur-Weyl duality, this space is naturally identiﬁed with CSm. The Casimir operator Ω
acts on V ⊗V and V ∗⊗V ∗by the ﬂip and on V ⊗V ∗by −coev ◦ev, where ev : V ⊗V ∗→1,
PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS
21
coev : 1 →V ⊗V ∗are the evaluation and coevaluation maps. Thus the operators Ωij,
1 ≤i < j ≤2m on Hom(1, V ⊗m ⊗V ∗⊗m) = CSm act as follows: for σ ∈Sm,
Ωijσ =









(i, j) ◦σ if i, j ≤m;
σ ◦(i −m, j −m) if i, j > m;
−tσ if σ(j −m) = i, i ≤m < j;
−(i, σ(j −m)) ◦σ = −σ ◦(σ−1(i), j −m) if σ(j −m)̸ = i, i ≤m < j,
where (i, j) is the transposition of i and j. In other words, Ωij = Ωij
0 + tΩij
1 , where Ωij
0 , Ωij
1
are independent on t.
We may now set s0 = ℏ, s1 = ℏt and consider the pencil of ﬂat connections ∇KZ,m(s)
with ﬁber CSm given by (5.1).
Note that if t = n ≥m is a positive integer then this
connection coincides with the usual KZ connection for gln on (V ⊗m ⊗V ∗⊗m)gln.
Thus,
repeating the arguments of [Dr] in the Deligne category (which can be done since they are
based on diagrammatic tensor calculus), we can interpolate the Drinfeld-Kohno theorem to
non-integer t. This implies that the monodromy of ∇KZ,m is given by the braiding operators
of the tensor category Repq(GLt), also called the oriented skein category (see e.g. [B]). These
operators are rational functions in q := eπis0 and a := qt = eπis1.
5.1.5. KZ connections for Lie superalgebras. The results of 5.1.1 can be generalized to the
case when g is a Lie superalgebra of type A-G, and V1, ..., Vr are ﬁnite dimensional g-modules.
In this case the relevant version of the Drinfeld-Kohno theorem is proved in [G]: again it
turns out that the monodromy representation depends on q := eπiℏ.
This can be generalized in several directions:
1. V1, ..., Vr can be taken from category O for some Borel subalgebra of g (with ratio-
nal weights), as in 5.1.1. Note that for Lie superalgebras there are several types of Borel
subalgebras up to conjugation.
2. The setup can be generalized to Kac-Moody Lie superalgebras, as in 5.1.2 (for basic
results on their structure and representation theory we refer the reader to [S]).
3. V1, ..., Vr can be taken to be Verma modules with complex highest weights for some
Borel subalgebra, and their highest weights multiplied by ℏcan be made parameters of a
multiparameter pencil, as in 5.1.3.
Remark 5.5. To be more precise, the Lie superalgebras of type A-G contain a unique
continuous family D(2, 1, α), α ∈C. So the above discussion applies literally when α ∈Q.
For more general α ∈C, we should make it a parameter of the pencil, similarly to Remark
5.3 (as the entries aij of the Cartan matrix of D(2, 1, α) depend linearly on α).
5.1.6. Trigonomeric KZ connections. Let g be a simple Lie algebra as in 5.1.1 and r ∈g ⊗g
a quasitriangular structure (classical r-matrix) such that r + r21 = Ω. Such structures were
classiﬁed by Belavin and Drinfeld, [BD1] and are labeled (up to abelian twists) by Belavin-
Drinfeld triples. Given r, we may deﬁne the aﬃne r-matrix (with spectral parameter)
br(z) := r21z + r
z −1 .
We may assume that the centralizer of r in g is a Lie subalgebra hr ⊂h (this can always
be achieved by conjugation). Let s ∈hr, let V1, ..., Vr be ﬁnite dimensional g-modules, and
22
PAVEL ETINGOF AND ALEXANDER VARCHENKO
consider the connection on the trivial bundle with ﬁber (V1 ⊗... ⊗Vr)[µ], µ ∈h∗
r on Cr with
ﬁrst order poles at xi = 0 and xi = xj, given by
(5.3)
∇(ℏ, s) := d −
r
X
i=1
 
s(i) + ℏ
X
j̸=i
br(xi/xj)
!
dxi
xi
.
This connection is ﬂat and called the trigonometric KZ connection; it is a pencil with
parameters s = (ℏ, s) ∈C ⊕hr (i.e., ℏ= s0, s = (s1, ..., sn)). The monodromy of the trigono-
metric KZ connection is computed in [EG] in terms of the Etingof-Kazhdan quantization
of the quasitriangular Lie bialgebra (g, r), using its relationship to the usual KZ connec-
tion. This quantization is described explicitly in [ESS], and this description implies that the
monodromy of the trigonometric KZ connection depends on q = eπiℏand qs.
Remark 5.6. 1. In the case when r is the standard classical r-matrix of g, the trigonometric
KZ connection can be easily obtained from the rational one, as explained for example in
[EFK], Subsection 3.8, or [MV]. In particular, the integral representations of solutions of
the KZ equations from [SV] give integral representations of solutions of the trigonometric
KZ equations. Hence the trigonometric KZ connection for the standard r-matrix is motivic.
2. Moreover, in this case the shift operators Aj(s) in the parameters sj, j ≥1 are the
dynamical diﬀerence operators introduced in [TV] and studied further in [EV1] (the lattice
part of the dynamical Weyl group for the aﬃne Lie algebra bg). However, the shift operator
A0(s) in s0 = ℏis more complicated, and its explicit expression is not known in general.
As before, this can be generalized to category O modules and to Lie superalgebras.
Another generalization arises if the trigonometric r-matrix br(z) corresponding to r is
replaced by an arbitrary trigonometric r-matrix br(z) from [BD2] (i.e., corresponding to a
Belavin-Drinfeld triple for a possibly twisted aﬃne Lie algebra). This deﬁnes a pencil of ﬂat
connections (5.3) (where s ∈h preserves br) whose monodromy can be computed using the
trace interpretation of ﬂat sections given in [ES], and shown to depend on q = eπiℏand qs.
5.1.7. Elliptic KZ connections. Let τ ∈C+ and E = C×/e2πiτZ be an elliptic curve. Let
g = sln and r(z, τ) be the Belavin elliptic r-matrix associated to some integer 1 ≤k ≤n −1
coprime to n ([BD2]); it has simple poles at points of order n on E. Let V1, ..., Vr be ﬁnite
dimensional representations of sln. The elliptic KZ connection is the connection on the
trivial bundle on Er with ﬁber V1 ⊗... ⊗Vr and ﬁrst order poles at xi = ζxj, where ζ ∈E,
ζn = 1, given by the formula
∇(ℏ) = d −ℏ
r
X
i=1
X
j̸=i
r(xi/xj, τ)dxi
xi
.
This is a pencil of ﬂat connections on its regular locus X ⊂Er. The monodromy of this
pencil was computed in [E1] and shown to depend on q = eπiℏ.
