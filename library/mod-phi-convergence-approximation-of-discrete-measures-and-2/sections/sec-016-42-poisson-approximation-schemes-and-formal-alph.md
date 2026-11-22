---
doc_id: mod-phi-convergence-approximation-of-discrete-measures-and-2
doc_title: "ANNALES DE L’INSTITUT FOURIER"
section_id: sec-016-42-poisson-approximation-schemes-and-formal-alph
section_title: "Poisson approximation schemes and formal alphabets"
section_number: 4.2
pages: 41-45
source_pdf: mod-phi-convergence-approximation-of-discrete-measures-and-20yc5c6q3n.pdf
source_sha256: c563cc999000e75d
toc_source: outline
doc_brief: "ANNALES DE L’INSTITUT FOURIER — 27 sections: Front matter; Introduction; Poisson approximation of lattice-v"
---
The description of the approximation schemes and of the asymptotic es-
timates for the distances by means of the parameters pk and ek is actually
possible for many other examples of discrete random variables. Thus, the
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1155
combinatorics of approximation schemes can be encoded in the algebra of
symmetric functions Sym. From an algebraic point of view, the language
of λ-rings and formal alphabets make this description even more striking.
Denote Sym the algebra of symmetric functions, that is to say symmet-
ric polynomials in an inﬁnity of variables {x1, x2, x3, . . .}; we refer to [43,
Chapter 1] or [44, Chapter 2] for the whole discussion of this paragraph.
The algebra Sym admits for algebraic basis over C the power sums
pk⩾1 =
X
i
(xi)k
and the elementary functions
ek⩾1 =
X
i1<i2<···<ik
xi1xi2 · · · xik;
thus, Sym = C[p1, p2, . . .] = C[e1, e2, . . .]. The two bases are related by the
identity of formal series
1 =
 Y
i
(1 −txi)
!
exp
 X
i
log
1
1 −txi
!
=
 
1 +
∞
X
k=1
ek tk
!
exp
 ∞
X
k=1
pk
k tk
!
,
which leads to the formula
ek =
X
L∈Pk
(−1)|L|−ℓ(L)
zL
pL
where Pk is the set of integer partitions of size k, and pL = Qℓ(L)
i=1 pLi. This
is a particular case of the Frobenius–Schur formula for Schur functions [44,
Theorem 2.32].
A formal alphabet, or specialisation is a morphism of algebras ψ : Sym →
C. In particular, if A = {a1, a2, . . .} is a set of complex numbers with
P
i |ai| < +∞, then the map
pk 7→pk(A) =
X
i
(ai)k
can be extended to a morphism of algebras Sym →C, hence a specialisation
of Sym (in this case one can speak of a “true” alphabet for A). Beware
that some specialisations are not of this form: indeed, a formal alphabet
can send the power sums pk to an arbitrary set of values in C. Still, we
can agree to use the notation f 7→f(A) for any specialisation f 7→ψ(f)
of the algebra Sym. In particular, suppose that A = {a1, a2, . . .} is a set of
TOME 70 (2020), FASCICULE 3
1156
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
complex numbers, but this time with P
i |ai| = +∞and P
i |ai|2 < +∞.
We then denote f 7→f(A) the specialisation
p1(A) = 0 ;
pk⩾2(A) =
X
i
(ai)k.
This deﬁnition extends indeed to a unique morphism of algebras Sym →C,
although there is a priori no underlying “true” alphabet. Given two formal
alphabets A and B, one can deﬁne new formal alphabets ε(A) and A + B,
as follows:
pk(ε(A)) = (−1)k−1 pk(A) ;
pk(A + B) = pk(A) + pk(B).
As before, these deﬁnitions extend uniquely to new morphisms of algebras
Sym →C. If A and B were true alphabets, then A+B is the true alphabet
which is the disjoint union of A and B. On the other hand, ε is related to
a certain involution of the Hopf algebra of symmetric functions.
Let us now relate the theory of symmetric functions to the approximation
schemes of discrete distributions. Consider a sequence of random integer-
valued variables (Xn)n∈N, whose Fourier transforms write as:
E[eiξXn] = eλn(eiξ−1) exp
 ∞
X
k=2
ck,n
k! (eiξ −1)k
!
.
The coeﬃcients λn = c1,n and ck⩾2,n are called the factorial cumulants of
Xn, and the Poisson random variables are characterized by the vanishing of
their factorial cumulants of order k ⩾2 (see [21, Section 5.2]). We associate
to these coeﬃcients the following specialisation of Sym:
p1(An) = 0 ;
pk⩾2(An) = (−1)k−1 ck,n
(k −1)!
.
Then, the deconvolution residue ψn(ξ) = E[eiξXn] e−λn(eiξ−1) admits the
expansion:
ψn(ξ) =
∞
X
k=0
ek(An) (eiξ −1)k,
with e0(An) = 1 and e1(An) = 0. The approximation scheme of order r ⩾1
is given by the residue
χ(r)
n (ξ) =
r
X
k=0
ek(An) (eiξ −1)k.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1157
The reason why this formalism is convenient is that, for all the examples
that we shall look at in this section, the limiting residue
ψ(ξ) =
∞
X
k=0
ek(A) (eiξ −1)k,
corresponds to a formal alphabet A which is explicit and which expresses
in terms of “natural” parameters of the random model. These formal al-
phabets are given by Table 4.1.
Table 4.1. Formal alphabets associated to the mod-Poisson convergent
sequences.
Xn
formal alphabet A
sum of independent Bernoulli
{p1, p2, p3 . . .}
variables with parameters pj (Section 4.1)
number of cycles of a random
N∗−1
uniform permutation (Section 4.3)
number of cycles of a random Ewens
Θ
permutation with parameter θ (Section 4.3)
number of connected components
(2N + 1)−1
of a uniform random map (Section 4.4)
number of distinct irreducible factors
N∗−1 + (qdeg I)−1
of a random monic polynomial (Section 4.4)
number of irreducible factors of a
N∗−1 + ε((qdeg I −1)−1)
random monic polynomial (Section 4.4)
number of distinct prime divisors
N∗−1 + P−1
of a random integer (Section 4.5)
In this table we denote A−1 = { 1
a, a ∈A} if A is a true alphabet, and
Θ =

1,
θ
θ + 1,
θ
θ + 2, . . .

;
qdeg I =

qdeg P , P ∈I
	
;
(qdeg I −1) =

qdeg P −1, P ∈I
	
where I is the set of irreducible polynomials over the ﬁnite ﬁeld Fq. There-
fore, the asymptotic behavior of a sequence (Xn)n∈N in Table 4.1 is entirely
encoded in:
• a sequence of parameters (λn)n∈N,
• and a formal alphabet A which in some sense captures the geometric
and arithmetic properties of the model.
TOME 70 (2020), FASCICULE 3
1158
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
In particular, the reader should notice the appearance of two contributions
to the formal alphabet as soon as one studies the problem of factorization
of a random element in a factorial ring.
