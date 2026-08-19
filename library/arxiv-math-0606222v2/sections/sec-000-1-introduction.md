---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
Let F be a local ﬁeld and let KF be the maximal compact subgroup of GL d(F). That is,
(1.1) KF =





O(d) if F = R,
U(d) if F = C,
GLd(O) if F non-Archimedean,
where in the latter case O denotes the ring of integers of F. Let G(n,d ; F) be the Grassman-
nian of n-dimensional subspaces of a ﬁxed d-dimensional vector space over F. Throughout
we assume that n ≤ d/2. The group KF acts transitively on G(n,d ; F). Letting MF be
a stabilizer of a point we may identify G(n,d ; F) with KF/MF. The pair ( KF, MF) is a
Gelfand pair, in the sense that each (continuous, complex) irreduc ible KF-representation
has a subspace of MF-ﬁxed vectors which is at most one-dimensional. The irreducible
representations having a one-dimensional subspace of MF-ﬁxed vectors are called MF-
spherical. In this paper we derive explicit dimension formulas for the ir reducible MF-
spherical KF-representations.
For all local ﬁelds F the equivalence classes of the irreducible MF-spherical KF-repre-
sentations are naturally parameterized by the set Λ n of partitions of at most n parts
2000 Mathematics Subject Classiﬁcation. 33D52, 33D80.
The ﬁrst author is supported by the Israel Science Foundation, I SF grant no. 555104, and by the
Edmund Landau Minerva Center for Research in Mathematical Analy sis and Related Areas, sponsored by
the Minerva Foundation (Germany). The second author is support ed by the Netherlands Organization for
Scientiﬁc Research (NWO) in the VIDI-project ‘Symmetry and modu larity in exactly solvable models’.
1
2 URI ONN AND JASPER V. STOKMAN
(see e.g. [12] and [5] for F Archimedean, and [2] for F non-Archimedean). This is quite
remarkable, taking into consideration that the representation th eory of KF for F non-
Archimedean is of a completely diﬀerent nature compared to the rep resentation theory for
F Archimedean. In each case there is a natural explicit labeling of the ir reducible MF-
spherical KF-representationsV F
λ by partitions λ ∈ Λ n which we shall describe in detail.
The zonal spherical functions ϕF
λ associated to V F
λ (λ ∈ Λ n) form a linear basis of the
Hecke algebra of MF-biinvariant representative functions on KF. The starting point for
the derivation of the explicit dimension formulas for the irreducible MF-spherical KF-
representations is the representation theoretic dimension formu la
(1.2) Dim C
(
V F
λ
)
=
(
ϕF
λ(e)
) 2
∫
KF
|ϕF
λ(g)|2dg, λ ∈ Λ n
where e ∈ K F is the unit element and integration is with respect to the normalized Ha ar
measure on KF. The second key ingredient is the fact that the zonal spherical fu nctions
ϕF
λ for the diﬀerent local ﬁelds F relate to various degenerations of the multivariable little
q-Jacobi polynomials from [26], see [12], [5] and [23]. As a result, we are led to consider
generalized dimensions deﬁned in terms of evaluations and quadratic norms of multivariable
little q-Jacobi polynomials, which interpolate between the various classica l dimensions.
The multivariable littleq-Jacobi polynomials P L
λ (z) (λ ∈ Λ n) are symmetric polynomials
in n variables z = (z1,...,z n) depending on four auxiliary parameters, which arise as
degenerations of the Macdonald-Koornwinder polynomials [15]. They form an orthogonal
system with respect to an explicit discrete probability orthogonality measure deﬁned in
terms of an iterated Jackson integral (see [26]), which induces a no rm ‖·‖L on the symmetric
polynomials in z. The generalized dimensions referred to in the previous paragraph are
(1.3) d(λ) = P L
λ (0)2
‖P L
λ ‖2
L
, λ ∈ Λ n,
compare with the representation theoretic dimension formula (1.2) .
We show that the dimension of V F
λ can be obtained as a classical ( q = 1) degener-
ation of d(λ) for F Archimedean, and as a p-adic (q = 0) degeneration of d(λ) for F
non-Archimedean. For special values of the four auxiliary paramet ers of the multivari-
able little q-Jacobi polynomials we show that the generalized dimensions d(λ) (λ ∈ Λ n)
themselves have a representation theoretic interpretation as th e quantum dimensions of
irreducible spherical quantum representations associated to the one-parameter family of
quantum complex Grassmannians from [20] and [5]. In this case the ke y ingredient is
the identiﬁcation in [20] and [5] of the associated quantum zonal sph erical functions with
Macdonald-Koornwinder polynomials, as well as with degenerations o f the Macdonald-
Koornwinder polynomials known as multivariable big and little q-Jacobi polynomials.
Cherednik’s double aﬃne Hecke algebra techniques have led to explicit evaluation for-
mulas and to explicit quadratic norm evaluations for the Macdonald-K oornwinder poly-
nomials in [24] (see also [3] and [28]). The quadratic norms ‖Pλ‖2
L of the multivariable
little q-Jacobi polynomials (as well as for multivariable big q-Jacobi polynomials) have
been explicitly evaluated in [27] by degenerating the quadratic norm e valuations of the
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 3
Macdonald-Koornwinder polynomials. In exactly the same way we der ive in this paper
evaluation formulas for the multivariable big and little q-Jacobi polynomials. This leads to
explicit expressions for the interpolating, generalized dimensions d(λ) (λ ∈ Λ n). Explicit
(quantum) dimension formulas for the irreducible spherical (quant um) representations as-
sociated to the various (quantum) Grassmannians are subsequen tly derived by degenerating
the explicit expression for d(λ) (λ ∈ Λ n).
The contents of the paper is as follows. In Section 2 we introduce th e multivariable little
q-Jacobi polynomials and the associated generalized dimensions. In S ection 3 we discuss
the representation theory of general Compact Quantum Group ( CQG) algebras from [4]
and [7]. CQG algebras form the natural setting to capture the harmonic analyt ic structures
of the various (quantum) Grassmannians under consideration in th is paper.
In Section 4 we specialize the general representation theoretic se tup from Section 3
to the classical CQG algebra of representative functions on the compact group KF. We
discuss the harmonic analytic implications for the associated Grassm annian KF/MF. We
pay close attention to the speciﬁc parametrization of the irreducib le MF-spherical KF-
representations by Λ n. We state the explicit dimension formulas, which are new in case
of non-Archimedean local ﬁelds F (see Theorem 4.5). Although the results are essentially
classical for Archimedean local ﬁelds F (see e.g. [12], [5], [30] and [23]), we have decided
to give a detailed exposition in case of F = C in order to highlight the similarities and
diﬀerences to the results for the Grassmannians over non-Archim edean local ﬁelds F, as
well as to the results for the quantum complex Grassmannians in the subsequent sections.
In Section 5 we specialize the setup from Section 3 to the CQG algebra of quantized
representative functions on KC = U(n), and we discuss the associated harmonic analysis
on the standard quantum complex Grassmannian. In particular, we state explicit quantum
dimension formulas for the associated irreducible spherical quantu m representations.
In Section 6 we introduce the Macdonald-Koornwinder polynomials an d the multivari-
able big and little q-Jacobi polynomials. We derive explicit evaluation formulas for the
multivariable big and little q-Jacobi polynomials. Subsequently we derive in Section 7
explicit expressions for the generalized dimensions as well as for the ir p-adic (q = 0) de-
generations.
In Section 8 we discuss the present approach for the one-parame ter family of quantum
complex Grassmannians from [20] and [5]. Following closely the analysis of Noumi [19]
for other examples of quantum symmetric spaces, we express the quantum dimensions
of the associated irreducible spherical quantum representations in terms of evaluations
and quadratic norms of Macdonald-Koornwinder polynomials, as well as of multivariable
big and little q-Jacobi polynomials. In particular, we obtain the representation t heoretic
interpretation of the generalized dimensions for special paramete rs as quantum dimensions
of irreducible spherical quantum representations. In this contex t we remark that a similar
approach can be followed for quantum real Grassmannians using th e harmonic analytic
results from [30] and [17], but we do not pursue it in this paper.
4 URI ONN AND JASPER V. STOKMAN
Notations and conventions. Representations of topological groups are complex and are
required to be continuous. We set
(1.4) E = C(a,b,c,d,q,t )
for the ﬁeld of rational functions in six indeterminates a,b,c,d,q and t. We set Λ n for the
partitions of at most n parts. It is the cone
Λ n =
n⨁
r=1
Z+ωr
in Zn, where ωr = (1 r, 0n−r) ∈ Λ n is the fundamental partition consisting of r ones and
n −r zeros. We write ω0 = (0 n) ∈ Λ n for the zero partition. For a partition λ ∈ Λ n we
denote λ′ for the conjugate partition and we set λ′
0 = n. In addition we write |λ| for the
weight of λ,l(λ) = λ′
1 for the length of λ, and ∂λ′ = (λ′
j −λ′
j+1)j≥0 for the positive integral
diﬀerences of the conjugate partition (whose sum equals n). For n-vectors u,v,w we set
uvw = (u1vw1
1 ,...,u nvwn
n ). We occasionally use this notation when u or v are scalars, in
which we use the corresponding n-vectors having all entries equal to the given scalar. We
recall some standard notations from basic hypergeometric series (see e.g. [8]). For j ∈ Z+
we set
(
a;q
)
j = (1 −a)(1 −aq) · · · (1 −aqj−1) (empty product is one) for the q-shifted
factorial. We write
(
a1,...,a m;q
)
j =∏ m
s=1
(
as;q
)
j for products of q-shifted factorials. For
m,l,l 1,...,l k ∈ Z+ with l ≤m, we use the notations
[m] = 1 −qm
1 −q , [m]q! =
m∏
j=1
[j]q,
[ m
l1 l2 · · · lk
]
q
= [m]q!
[l1]q! · · ·[lk]q!,
(m
l
)
q
=
[ m
l m−l
]
q
.
In terms of q-shifted factorials, the q-factorial can be expressed as
(1.5) [ m]q! = q
1
2 m(m−1)
(
q−1;q−1)
m
(1 −q−1)m.
We use standard notations for the basic hypergeometric series r+1φr, see e.g. [8].
