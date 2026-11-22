---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-037-57-jacobian-varieties
section_title: "Jacobian varieties"
section_number: 5.7
pages: 131-135
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
123
Proof. For a general ppav we know from theorem 4.2 that the Tannaka
group G(δΘ) is either a symplectic or a special orthogonal group and that
the perverse intersection cohomology sheaf δΘ corresponds to the standard
representation of this group. Now the symmetric and alternating square of
the standard representation are irreducible up to a trivial one-dimensional
representation, and this trivial representation corresponds to the skyscraper
sheaf δ0 of rank one supported in the origin. Furthermore, by corollary 2.9
each representation of the Tannaka group corresponds to a unique clean
perverse sheaf. Hence from lemma 5.22 we obtain that there exist clean
and simple perverse sheaves γ± ∈Perv(X,C) such that
δ+ =
(
γ+ ⊕δ0
γ+
and
δ−=
(
γ−
γ−⊕δ0
if g is
(
odd,
even,
and by lemma 5.21 the simplicity of γ± in particular implies that the local
systems V± are irreducible.
□
5.7. Jacobian varieties
Let us now see what happens if X = JC is the Jacobian variety of a
smooth complex projective curve C of genus g ≥2. To formulate our results
in this case we ﬁrst need to introduce some more notations. For n ∈N we
will denote by
Cn = (C ×···×C)/Sn
the n-fold symmetric product of the curve and by Wn ⊂X the image of Cn
under a suitable translate of the Abel-Jacobi map, normalized such that the
theta divisor Θ = Wg−1 becomes symmetric. We write fn : Cn −→Wn for
the Abel-Jacobi map and gn : Wn ×Wn −→X for the difference morphism
with gn(x,y) = y−x. Then the composite morphism
Cn ×Cn
(fn,fn)
/
dn
7
Wn ×Wn
gn
/ X ∼= Pic0(C)
does not depend on the chosen normalization of the Abel-Jacobi map, and it
sends a pair (D,E) ∈Cn ×Cn of effective divisors of degree n on the curve
to the isomorphism class of the line bundle OC(D−E).
In what follows we will be especially interested in non-hyperelliptic
curves of genus g = 4. For these we know from lemma 4.5 that the theta
divisor has only isolated singularities, so we can consider the variations of
Hodge structures V± from lemma 5.10 and the perverse sheaves δ± from
lemma 5.21. Here we have the following situation.
124
Chapter 5 – A family of surfaces
PROPOSITION 5.24. Let X = JC be the Jacobian variety of a smooth
non-hyperelliptic complex projective curve C of genus g = 4.
(a) The above semisimple perverse sheaves δ+ and δ−each contain
the negligible constituent δX precisely once.
(b) After shrinking the open dense subset U ⊂X in lemma 5.10 there
exists an isomorphism
V+ ∼= d2∗(CC2×C2)|U.
Proof. (a) We must check for the lowest hypercohomology degree that
dim(H−g(X,δ+)) = dim(H−g(X,δ−)) = 1. For this we can use the same
computation as in lemma 5.22, the only difference is that for a Jacobian
variety the hypercohomology H•(X,δΘ) is larger than the one for a general
ppav. Indeed it has been shown in [106, cor. 13(iii)] that if the curve C is
not hyperelliptic, then
Hi(X,δΘ) =
(
Hi+3(X,C)
for i ∈{−3,−2},
Hi+3(X,C)⊕Hi+1(X,C)
for i ∈{−1,0}.
Compared with the computation in lemma 5.22, for i = −1 the extra direct
summand H0(X,C) ⊂H−1(X,δΘ) gives a two-dimensional extra term
H0(X,C)⊗H−3(X,δΘ) ⊕H−3(X,δΘ)⊗H0(X,C) ⊂H−4(X,δΘ ∗δΘ).
This extra term splits into two one-dimensional contributions, one in the
symmetric and one in the alternating tensor square. Hence
H−4(X,S2(δΘ)) = H−4(X,L+)⊕C,
H−4(X,Λ2(δΘ)) = H−4(X,L−)⊕C,
and our claim follows because S2(δΘ) = L+ ⊕δ+ and Λ2(δΘ) = L−⊕δ−.
(b) This is most conveniently checked in the setting of Brill-Noether
sheaves and will be done after the proof of lemma 5.25 below.
□
Before we proceed further, let us recall from [106] some facts about
Brill-Noether sheaves. Here we are mainly interested in their Tannakian
description — more about their geometric construction can be found in the
brief survey in section 6.1 below. Let X = JC be the Jacobian variety of a
smooth non-hyperelliptic complex projective curve C of genus g ≥2, and
let C ,→X be a translate of the Abel-Jacobi map such that the corresponding
theta divisor Θ = Wg−1 is symmetric. Then by loc. cit. the convolutions of
the perverse intersection cohomology sheaf δC ∈Perv(X,C) are described
via corollary 2.14 by the Tannaka group
G(δC) = Sl2g−2(C).
5.7. Jacobian varieties
125
For partitions α = (α1,α2,...) such that 2g −2 ≥α1 ≥α2 ≥··· ≥0, one
can deﬁne the Brill-Noether sheaf
pδ α ∈Perv(X,C)
as the simple perverse sheaf corresponding to the irreducible representation
of Sl2g−2(C) whose highest weight is given by the conjugate partition αt
in the basis of the weights deﬁned by the diagonal entries of matrices. For
instance, the singleton partitions α = (α1) correspond to the fundamental
representations, and for these it has been shown in loc. cit. that
pδ i ∼= δWi
and
pδ 2g−2−i ∼= δ−Wi
for
0 ≤i ≤g−1,
where the second equality is due to the Riemann-Roch theorem. Now the
Tannakian formalism provides a means to decompose arbitrary convolution
products between these perverse intersection cohomology sheaves via the
combinatorial Littlewood-Richardson rule for the decomposition of tensor
products of irreducible representations of Sl2g−2(C), see [46, sect. 9.3.5]
and [106, sect. 5.4]. In the special case of fundamental representations this
gives the formula
pδ m ∗pδ n ∼= τm,n ⊕
n
M
i=0
pδ (m+i,n−i)
for
m ≥n,
where τm,n ∈Db
c (X,C) is a negligible sheaf complex in the sense that all
its perverse cohomology sheaves have Euler characteristic zero. In fact it
has been shown in lemma 27 of loc. cit. that τm,n (and more generally any
negligible direct summand of a convolution of Brill-Noether sheaves) is a
direct sum of degree shifts of δX = CX[g]. As an application we have the
following result concerning the difference morphism.
LEMMA 5.25. Let X = JC be the Jacobian variety of a non-hyperelliptic
smooth projective curve of even genus g = 2n. Then over some Zariski-open
dense subset U ⊂X there exists an irreducible local system LU of complex
vector spaces such that
dn∗(CCn×Cn)|U ∼= CU ⊕LU.
Proof. A Bertini-type argument like the one in lemma 5.3 shows that
over some Zariski-open dense subset U ⊂X the morphism dn restricts to a
ﬁnite ´etale cover. Furthermore, if S denotes the singular locus of Wn, then
for dimension reasons the closed subset (S ×Wn) ∪(Wn × S) ⊂Wn ×Wn is
mapped under the difference morphism
gn :
Wn ×Wn −→X
to a proper closed subset of X, so we can assume that g−1
n (U) is contained
in (Wn\S)×(Wn\S). The Riemann-Kempf singularity theorem [48, p. 348]
126
Chapter 5 – A family of surfaces
says that the Abel-Jacobi morphism fn :Cn −→Wn restricts over the smooth
locus to an isomorphism
f −1
n (Wn \S)
∼=
−→Wn \S.
Putting everything together and using the commutative diagram
Cn ×Cn
(fn,fn)
/
dn
.
Wn ×Wn
gn

 
(−in,in)
/ X ×X
a
p
X
for the closed embedding in : Wn ,→X, we therefore obtain by the deﬁnition
of convolution an isomorphism
dn∗(CCn×Cn[g])|U ∼= (δWn ∗δ−Wn)|U.
To control the convolution on the right hand side, we use the formalism of
Brill-Noether sheaves. Recall that δWn = pδ n and δ−Wn = pδ 3n−2, where the
second equality is due to the Riemann-Roch theorem. Hence we get from
the Littlewood-Richardson rule that
δWn ∗δ−Wn ∼= pδ n ∗pδ 3n−2 ∼= τ ⊕
n
M
i=0
pδ 3n−2+i,n−i
where τ is a direct sum of degree shifts of δX. In fact τ = δX as one may see
from the above isomorphism dn∗(CCn×Cn[g])|U ∼= (δWn ∗δ−Wn)|U and from
the fact that dn is generically ﬁnite. Therefore our claim will follow for the
cohomology sheaf
LU = H −g(pδ 3n−2,n)|U,
provided that for all i > 0 the perverse sheaves pδ 3n−2+i,n−i are supported
on a proper closed subset of X. But this is indeed the case because by the
Littlewood-Richardson rule the perverse sheaf
n
M
i=1
pδ 3n−2+i,n−i ∼= pδ n−1 ∗pδ 2g−(n−1) ∼= δWn−1 ∗δ−Wn−1
has the support dn−1(Cn−1 ×Cn−1) ⊂X of dimension 2(n−1) < g.
□
Proof of part (b) in proposition 5.24. For this we again use Brill-Noether
sheaves. The perverse sheaf δΘ = δW3 = pδ 3 corresponds by deﬁnition to
the third fundamental representation of the Tannaka group Sl6(C). One can
check that the alternating square of this representation decomposes into two
irreducible pieces of highest weight αt for α = (4,2) and α = (6). Hence
it follows that
δ−∼= pδ 4,2 ⊕pδ 6 ⊕τ
