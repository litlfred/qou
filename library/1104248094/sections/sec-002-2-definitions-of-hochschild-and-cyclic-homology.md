---
doc_id: 1104248094
doc_title: "Hochschild and cyclic homology of quantum groups"
section_id: sec-002-2-definitions-of-hochschild-and-cyclic-homology
section_title: "Definitions of Hochschild and Cyclic Homology"
section_number: 2
pages: 4-8
source_pdf: 1104248094.pdf
source_sha256: c1fdb4791afcad3b
toc_source: inferred
doc_brief: "Hochschild and cyclic homology of quantum groups — For an arbitrary complex linear semisimple Lie group G, we consider Hopf algebras of the deformations of the formal and algebraic functions on G."
---
Here we recall the definitions and basic properties of Hochschild and cyclic
homology [8, 44, 14, 27]. Let A be an associative algebra over a commutative unital
ring fe, fccA In this paper /c = C, or C((/ι)), the ring of Laurent series. The
Hochschild homology of A, denoted by HH^(A\ is defined to be the homology of
the following complex
-., 
(2.1)
where Cn(A) = A®
n + l, and b\Cn(A)-+Cn-ι(A) such that
n-l
= Σ (-iy«
i = 0
4-(-l)Xα0®α1(x)...(x)αn_1. 
(2.2)
The cyclic homology of A, denoted by HC+(A)9 is defined to be the total
homology of the following double complex
(2.3)
where B\Cn(A)^Cn + 1(A) such that
n
~ 
$'-®an®aQ® '®ai_1
If k = C((h)) and A is h-adically complete, then by the tensor product we will
always mean fc-adically completed tensor product.
Let X be a non-singular affine variety, A = C[X], Ω
n(X) the n-forms on X,
H^R(X) the n
th de Rham cohomology of X. The following result is well-known.
Lemma (2.1).
1) (Hochschild-Kostant-Rosenberg) HHn(A) = Ω
n(X\
2) HCn(A) = Ω
n(X)/dΩ
n~
 
l(X)φ^DR
2(X)® #
n
DR
4® 
-.
This shows that in the commutative case the cyclic homology measures the de
Rham cohomology of the space, thus the name "non-commutative differential
geometry."
We are especially interested in certain Hopf algebras. Let us recall
Hochschild and Cyclic Homology of Quantum Groups
485
Definition (2.2). A Hopf algebra A over k is a k-bimodule A together with morphisms
m, i, Δ, ε, S,
A® A—-+A
ε 
i
A — » k — + A,
s
(2.5)
such that they satisfy the following axioms:
1. Associativity:
w (m® 1) =
2. ί/mί:
A® A® A
A® A
k®A
A® A
A®k 
>A®A
(2.6)
(2.7)
3. Coassociativity:
A®A
\®Δ 
*
A® A 
>A®A®A
(2.8)
4. Counit:
A®A
A® A 
>k®A
(2.9)
486
5. Connection Axiom:
P. Feng and B. Tsygan
A® A
[
Δ®
Δ
\ m = (m®m)'σ2ι (Δ®Δ), A® A® A® A
<T23
(2.10)
A® A® A® A 
>A®A
where σ23 means the permutation between the second and the third variables;
6. Antipode:
= (S®S)-σ Δ, 
A® A
A® A
A® A
|S<8>S
• m σ (S®S), 
A®A
A®A 
-
A®A
m-
-Δ = i-ε,
A®A
A® A
+ A
-> A
s®\
(2.11)
(2.12)
(2.13)
•A® A
We will call m, i, A, ε, S, respectively, the product, unit, coproduct, counit, antipode
of Hopf algebra A. We usually omit the symbol m,ί when there is no confusion.
Example (2.3). Let G be complex algebraic group, g its Lie algebra, (7(g) the
universal enveloping algebra, C[G] the algebraic functions on G.
U(g) is made into a Hopf algebra by
Vxeg, 
Δ(x)= l®x
ε(x) - 0,
S(χ)= -x.
(2.14)
Hochschild and Cyclic Homology of Quantum Groups 
487
C[G] is made into a Hopf algebra by
V/eC[G], 
0,/zeG, 
(Δ(f))(g,h) = f(gh\
\ 
(2.15)
where e is the identity of G.
The formal functions on G in the vicinity of identity, C^G), can be viewed as
a Hopf algebra dual to the universal enveloping algebra (7(g).
We now give a new complex for Hochschild homology of Hopf algebras.
1 Let
mr9ml denote respectively the natural right, left multiplications of A on A, i.e.,
mr(a)b = ba, m^cήb = ab. Define a right action of A on A by
p(a) = (mr ® m,)(l ® S)Δ(a). 
(2.16)
This obviously defines a right action since A is algebra homomorphism and S is
antihomomorphism. To be more specific,
p(a)x = £a;xaj9 
(2.17)
where Δ(a) = £ a{ ® aί? and ά
s — S(ά).
ί
Consider the following complex (C.(A\d}\
c ^ c ^ . . . , 
(2.18)
where d:Cn(A)-*Cn-ι(A\ such that
n-l
-f X (-I)
ία0®-(g)αίflί+1(
®α,J_1. 
(2.19)
It is straightforward to check that d
2 = 0, thus it indeed defines a complex. Note
that in this paper we also use d to denote the exterior derivative on G. We hope
there is no confusion as to which d we are referring to.
ξ(x®a®b(S) 
®c)= 
X 
c
s
ί 
l
s
ja
s
ίx®ai®bj® ~®ck9 
(2.20)
i,j,...,k
where Δ(a) = £ α (x) δt , etc.
1 This complex might have been known to other people, but we are unable to locate it in the
literature other than [13]
488 
P. Feng and B. Tsygan
Proposition (2.4).
1) 
ξ:CH(A)^Ca(A)9
2) ξd = bξ, i.e., the following diagram is commutative,
Cΐ(A)
Proof. 1) We define £': Cn(Λ) -+ Cn(,4), by
We claim that £•£' = ξ' ξ = 1. Let us check it for rc = 1, the general case can be
shown similarly. Denote Δ(a) = YJAi®Bi9 Δ
2(a) = (1 ® A)(a) = (4® l)(α) = £0,-®
fcyφcy, then, 
'
 
j
j 
j
where we have used m-(S® l) 4 = ε, and (ε® l) Λ= 1. Thus ξ-ξ
f = 1. Similarly,
2) Again we only check the n = 1 case.
/ 
\
ξ - d(x (x) α) = α Y J5*.χy4 — ε(α)x = Y JB* xA.. — ε(α)x,
\ j 
J 
j
and
/ 
s 
\ 
s 
ί 
\
Wegetξ-d = d'ξ.
Note that (2.16, 2.17) is the standard complex for the functor Tor,,.. We have
Corollary (2.5).
HH+(A) = H+(C.(A\ d) = Tor£μ, /c),
where A is considered as a right A-module via p defined in (2.15), and k is considered
as a left A-module via the counit ε.
It is this new complex that we are going to use for computing the Hochschild
