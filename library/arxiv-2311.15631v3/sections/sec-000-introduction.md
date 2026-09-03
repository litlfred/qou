---
doc_id: arxiv-2311.15631v3
doc_title: "Classification of connected étale algebras in pre-modular fusion categories up to rank three Ken KIKUCHI"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-5
source_pdf: 2311.15631v3.pdf
source_sha256: a3cc6d51cd04fc07
doc_brief: "Classification of connected étale algebras in pre-modular fusion categories up to rank three Ken KIKUCHI — We classify connected ´ etale algebras A’s in pre-modular fusion categories B with rank(B) ≤"
---
Throughout the paper, C denotes a fusion category (FC) over the ﬁeld C of complex numbers
(see [1] for deﬁnitions). Its simple objects are denoted ci’s withi = 1, . . . ,rank(C). We denote
its fusion ring by K(C). A pivotal structure a : idC ∼= (−)∗∗ deﬁnes left and right quantum
(or categorical) traces tr L/R (a) : 1 → 1. A pivotal structure is called spherical if ∀c ∈ C ,
trL(ac) = tr R(ac∗). In an FC C with a spherical structure a, a (quantum) dimension of an
object c ∈ C is deﬁned as dc := tr L(ac). Its squared sum deﬁnes categorical (or global)
dimension
D2(C) :=
rank(C)∑
i=1
d2
ci. (1.1)
Note that for a given categorical dimension, there are two D(C)’s, one positive and one
negative. If an FC is equipped with a braiding c, in order to avoid confusion, we especially
write the braided fusion category (BFC) B and simple objects bi’s. A spherical BFC is called
pre-modular fusion category (pre-MFC). This is our ambient categ ory. If the braiding in
a pre-MFC is non-degenerate, the category is called modular or mod ular fusion category
(MFC).
With a braiding, we can study commutative algebras. An algebra in an F C C is a triple
(A, µ, u) of an object A ∈ C , multiplication morphism µ : A ⊗ A → A, and unit morphism
u : 1 → A obeying associativity and unit axioms. A category CA of right A-modules consists
1
of pairs ( m, p) where m ∈ C and p : m ⊗ A → m subject to coherence conditions. (A
category AC of left A-modules is deﬁned analogously.) An algebra is called separable if CA is
semisimple. An algebra A ∈ B in a BFC is called commutative if
µ · cA,A = µ. (1.2)
A commutative separable algebra is called ´ etale. Any ´ etale algebraA decomposes to a direct
sum of connected ones [2] where A ∈ C is called connected if dim C C(1, A) = 1. An example
of connected ´ etale algebra is the unitA ∼= 1 ∈ B giving BA ≃ B . A BFC B without nontrivial
connected ´ etale algebra is called completely anisotropic. The goal o f this paper is to classify
connected ´ etale algebras1 in pre-MFCs. Our main results are summarized as the
Theorem. Connected ´ etale algebras in pre-modular fusion categories B’s up to rank three
are given as follows:
Rank B Results Completely anisotropic?
1 VectC Table 2 Yes
2 Vecα
Z/ 2Z Tables 3,4 No (two with (2.6))/ Yes (the other 14)
Fib Table 5 Yes
3 Vec1
Z/ 3Z Table 6 No ( hX = hY = 0)/ Yes ( hX = hY = ± 1
3)
Ising Table 7 Yes
Rep(S3) Tables 8,9 No (the other six)/ Yes (two symmetric with dY = −1)
psu(2)5 Table 10 Yes
.
T able 1: Connected ´ etale algebras in pre-MFC B with rank( B) ≤ 3
What is central in our classiﬁcation method [3] is the Frobenius-Perr on dimensions. They
are deﬁned as follows. An FC C has Grothendieck ring Gr(C). It admits a non-negative integer
matrix representation (NIM-rep). The matrix ( Ni)jk := Nij
k consists of N-coeﬃcients
ci ⊗ cj ∼=
rank(C)⨁
k=1
Nij
kck. (1.3)
Since they have non-negative entries, we can apply the Perron-Fr obenius theorem to get the
largest positive eigenvalue FPdim C(ci) called Frobenius-Perron dimension of ci (or Ni). Its
squared sum deﬁnes Frobenius-Perron dimension of an FC
FPdim(C) :=
rank(C)∑
i=1
(FPdimC(ci))2. (1.4)
1They are also called quantum subgroup, consensable algebra, or no rmal algebra depending on contexts.
2
An FC C with D2(C) = FPdim( C) is called pseudo-unitary, and unitary if ∀c ∈ C , dc =
FPdimC(c). The Frobenius-Perron dimension deﬁnes a Lagrangian algebra. A connected
´ etale algebraA in a BFC B is called Lagrangian if (FPdim B(A))2 = FPdim( B). With the
Frobenius-Perron dimension at hand, our classiﬁcation method [3] c onsists of three steps:
1. Find a maximal rank rmax on rank( BA),
2. List up candidate fusion categories for BA,
3. Check which of them satisfy axioms.
A maximal rank on BA is given by rmax = ⌊FPdim(B)⌋ [3]. This is because ∀c ∈ C ,
FPdimC(c) ≥ 1 [4, 1], and for a BFC B and a connected ´ etale algebraA ∈ B , Frobenius-Perron
dimensions obey [5, 4, 2]
FPdimB(A) = FPdim(B)
FPdim(BA) . (1.5)
Since FPdim B(A) ≥ 1, we obtain
1 ≤ FPdim(BA) ≤ FPdim(B), (1.6)
and
rank(BA) ≤ rmax = ⌊FPdim(B)⌋. (1.7)
In our setup, BA is known to be a fusion category. 2 Hence, we list up candidate fu-
sion categories C’s for BA in the second step. The candidates should satisfy three con-
ditions: i) rank( C) ≤ rmax = ⌊FPdim(B)⌋, ii) (1 ≤)FPdim(C) ≤ FPdim(B), and iii)
FPdimB(A) = FPdim( B)/FPdim(C). The ﬁrst two conditions are coming from (1.7,1.6).
The third condition is coming from (1.5). Since A is a direct sum of simple objects in
B, its Frobenius-Perron dimension is given by a linear sum of those of sim ple objects with
N-coeﬃcients
FPdimB(A) =
rank(B)∑
i=1
niFPdimB(bi) ( ni ∈ N). (1.8)
It turns out that these conditions are strong enough to rule out m any fusion categories. In
the third step, we check which candidate fusion categories satisfy axioms of connected ´ etale
algebras. In particular, we have to check (1.2). For that purpose , we check a necessary
condition
µ · cA,A · cA,A = µ (1.9)
2Here is the reason. Let C be a multitensor category and A ∈ C be a connected separable algebra. Then,
CA is a semisimple tensor category with simple unit A ∈ C A. If C is ﬁnite, CA is ﬁnite. Thus, for a ﬁnite
multitensor category C and connected separable algebra A ∈ C , CA is a fusion category. (Recall a fusion
category is deﬁned as ﬁnite semisimple tensor category.)
3
for an algebra to be commutative. With conformal dimension hi of bi, the double braiding is
given by
cA,A · cA,A ∼=
n∑
i,j =1
(ιi ⊗ ιj) · caj ,a i · cai,a j · (pi ⊗ pj), (1.10)
where pi : A → ai and ιi : ai → A are product projections and coproduct injections of a
direct sum A ∼= a1 ⊕ a2 ⊕ · · · ⊕ an, respectively. The double braiding caj ,a i · cai,a j of simple
objects ai, aj can be computed from the formula 3
caj ,a i · cai,a j =
rank(B)∑
k=1
Nij
k e2πih k
e2πi (hi+hj) idk. (1.14)
If one ﬁnds A does not satisfy (1.9), one can drop it from the list of candidates. I f a candidate
does pass the necessary condition, we need to check the axiom µ · cA,A = µ seriously. Just
like a double braiding, the half-braiding is given by
cA,A ∼=
n∑
i,j =1
(ιj ⊗ ιi) · cai,a j · (pi ⊗ pj). (1.15)
To ﬁnd cai,a j , in principle, we have to solve hexagon equations, but ‘diagonal’ ones cb,b ’s for
self-dual simple objects b ∼= b∗ can be computed from the formula [6]
cb,b ∼= e−2πih bν2(b)idb⊗b, (1.16)
where ν2(b) is the Frobenius-Schur indicator [7]. 4
3The quantum trace of double braidings deﬁnes S-matrix
~Si,j := tr(cbj ,b i · cbi,b j ) =
rank(B)∑
k=1
Nij
k e2πih k
e2πi (hi+hj ) dk. (1.11)
A normalized S-matrix is deﬁned by
Si,j :=
~Si,j
D(B) .
Another modular matrix T is deﬁned by
Ti,j = e2πih i δi,j . (1.12)
When B is modular, the matrices deﬁne (additive) central charge c(B) mod 8 by
(ST )3 = e2πic (B)/ 8S2. (1.13)
4When B is modular, it can be computed with the formula
ν2(bk) := 1
D2(B)
rank(B)∑
i,j =1
Nij
kdidj
(e2πih i
e2πih j
) 2
. (1.17)
4
Another fact we use to check an existence of connected ´ etale alg ebra A ∈ B is that
BA is a left B-module category [8]. A left C-module category (or module category over
C) is a quadruple ( M, ⊲, m, l) of a category M, an action (or module product) bifunctor
⊲ : C × M → M , and natural isomorphisms m−, −, − : ( − ⊗ − ) ⊲ − ∼= − ⊲ (− ⊲ −) and
l : 1 ⊲ M ≃ M called module associativity constraint and unit constraint, respect ively.
They are subject to associativity and unit axioms as usual. An essen tial fact about module
categories is that since c⊲m is an object of M, it can be decomposed to a direct sum of simple
objects with N-coeﬃcients. Thus, actions of (left) C-module categories form NIM-reps. If one
ﬁnds no r-dimensional NIM-rep, one can rule out candidates A ∈ B giving BA’s with rank
r. On the other hand, if one ﬁnds r-dimensional NIM-reps, we can use it to constrain forms
of A’s. In order to get additional constraints, we use the internal Hom [8]. For m1, m2 ∈ M
over C, the internal Hom Hom (m1, m2) ∈ C is deﬁned, if exists, by a natural isomorphism
∀c ∈ C , M(c ⊲ m1, m2) ∼= C(c, Hom(m1, m2)). (1.18)
It has a natural isomorphism
∀c ∈ C , ∀m1, m2 ∈ M, Hom(m1, c ⊲ m2) ∼= c ⊗ Hom(m1, m2). (1.19)
We will use this fact to translate actions ⊲ of C on M to monoidal products ⊗ in C. For
every m ∈ M , Hom (m, m) has a canonical structure of an algebra in C. Furthermore, it is
known [8, 1] that the functor
F := Hom(m, −) : M → C Hom(m,m ) (m ∈ M) (1.20)
sending m′ ∈ M to Hom (m, m′) ∈ C gives M ≃ C Hom(m,m ).
2 Classiﬁcation
