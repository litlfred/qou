---
doc_id: arxiv-2406.18369v2
doc_title: "112 years of listening to Riemannian manifolds"
section_id: sec-004-3-listening-to-flat-tori
section_title: "Listening to flat tori"
section_number: 3
pages: 12-15
source_pdf: 2406.18369v2.pdf
source_sha256: 20b3f8dbc40eacc3
toc_source: outline
doc_brief: "112 years of listening to Riemannian manifolds — In1910, HendrikAntoonLorentzdelvedintotheenigmaticLaplace eigenvalue equation, also known as the Helmholtz equation, pondering to what extent the"
---
Ann-dimensional flat torus is a smooth compact Riemannian manifold obtained
by taking the quotient of Euclidean spaceRn by a full-rank lattice. For inclusivity,
we recall that GLn(R) is the group of all invertiblen×n matrices with entries in
R with group operation given by matrix multiplication. The subgroup GLn(Z)⊂
GLn(R) consists of those matrices with entries inZ whose inverses also have entries
in Z. A full-rank lattice in Rn is a discrete additive subgroup of the additive
group Rn, that necessarily is a set of the formΓ =AZn for some invertible matrix
A∈ Rn×n called abasis matrix of Γ. We note that there are many basis matrices
for the same lattice because for anyB∈ GLn(Z), the sets AZn and ABZn are
identical. The lattice Γ defines an associatedflat torus TΓ = Rn/Γ. Such a torus
is “flat” because its Riemannian metric is induced by the Euclidean metric onRn.
Two flat tori areisometric if they are isometric as Riemannian manifolds.
Thanks to the structure of a flat torus as a quotient of Euclidean space, the
Laplace eigenvalue problem for a flat torus can be studied in Euclidean space by
searching for all twice weakly locally differentiable functionsf : Rn→ C andλ∈ C
112 YEARS OF LISTENING TO RIEMANNIAN MANIFOLDS 13
such that for allx∈ Rn and for allγ∈ Γ,
(14)



∆f(x) =λf(x),
f(x +γ) =f(x),
∇f(x +γ) =∇f(x).
The idea of two lattices being the same shape is captured by the notion of
congruence. Let On(R) be the group of all invertiblen×n matrices A with real
entriessuchthat A−1 =AT. Wesaythattwolattices A1Zn andA2Zn arecongruent
if A1 =A2B for someB∈On(R). By [14, p. 5], two flat tori are isometric if and
only if their associated lattices are congruent.
To find the spectrum of a flat torus, we need the notion of dual lattices. The
dual lattice Γ∗ of a latticeΓ is
Γ∗ ={γ∈ Γ :γ·δ∈ Z for allδ∈ Γ}.
Theorem 3.1([90], Thm. 2.8). The spectrum of a flat torusRn/Γ is the multi-set
(meaning counting multiplicity)
{4π2||γ||2 :γ∈ Γ∗}.
The multiplicity of4π2||γ||2 is the number of differentδ∈ Γ∗ such that||δ|| =||γ||.
In turns out that quadratic forms have a strong connection to flat tori. To
understand this, we need some more definitions. Recall that any quadratic formq
in n variables has anassociated matrix, that is, a symmetricn×n matrix Q such
that q(x) = xTQx for allx∈ Rn. Moreover, q is positive definite if q(x)≥ 0 for
all x∈ Rn with equality if and only ifx = 0. It is rational if all entries inQ are
rational, and it iseven if all entries inQ are integers, and the diagonal elements
are even.
Proposition 3.2 ([108], Thm. 11.2). If q(x) = xTQx is a positive definite qua-
dratic form inn variables, then there is an invertiblen×n matrix A such that
Q =ATA. This is called theCholesky factorizationof Q. The matrixA is unique
up to multiplication by matrices inOn(R).
If q is a positive definite quadratic form inn variables whose associated matrix
Q has Cholesky factorizationQ = ATA, thenAZn is called theunderlying lattice
ofQ andq. SinceAZn may not equalAOZn forO∈On(R), the underlying lattice
of a quadratic form is not unique. However, they are all congruent, and therefore
their associated flat tori are all isometric.
Two quadratic formsq(x) =xTQx andp(x) =xTPx are calledintegrally equiva-
lent ifBTQB =P for someB∈ GLn(Z). This defines an equivalence relation, and
two integrally equivalent quadratic forms have identicalrepresentation numbers.
That is,R(q,t ) =R(p,t ) for allt≥ 0, where
R(q,t ) = #{x∈ Zn :q(x) =t}.
Conversely, whilethetwoquadraticformswithassociatedmatrices ATAand (AB)T
AB may not be equal forB∈ GLn(Z), they are integrally equivalent and therefore
have identical representation numbers. This makes it reasonable to associate a flat
torus Rn/Γ, Γ =AZn, with the equivalence class of integrally equivalent quadratic
forms which contains the quadratic form with associated matrixATA. It follows,
then, that two flat tori are isometric if and only if their associated equivalence
classes of quadratic forms coincide. Moreover, we have the following result.
14 G. MÅRDBY AND J. ROWLETT
Theorem 3.3 ([90], Cor. 2.15). Two flat tori are isospectral if and only if their
representation numbers associated as above are identical.
We say that two quadratic forms areisospectral if they have identical repre-
sentation numbers. Thus, two quadratic forms are isospectral if and only if their
associated flat tori are isospectral. If two flat tori are isospectral, are they neces-
sarily isometric? In other words, if we are listening to flat tori, can we hear their
shapes?
This seems like a difficult question because verifying isospectrality directly from
the spectrum requires checking that all of the infinitely many eigenvalues are iden-
tical. Checking isometry - or non-isometry - is also not so simple since there are in-
finitely many isometries of Euclidean space. One simple way to check non-isometry
is to show that one lattice is reducible whereas the other lattice is not. A lattice
Γ⊂ Rn is adirect sumof two latticesΓ1, Γ2 if
Γ1 + Γ2 :={x +y :x∈ Γ1,y∈ Γ2} = Γ,
Γ1· Γ2 :={x·y :x∈ Γ1,y∈ Γ2} ={0}.
We write this asΓ = Γ1⊕Γ2. The latticeΓ is calledreducible if it is the direct sum
of two lattices of lower dimension. Otherwise it isirreducible. It is the case that
Γ̸={0} is reducible if and only if it is congruent toΓ1× Γ2, where both Γ1, Γ2
have dimension at least 1 [90, Lemma 2.26].
Proposition 3.4 ([90], Prop. 2.28). Suppose a latticeΓ∈ Rn can be decomposed
as
Γ = Γ1⊕···⊕ Γk.
Then, a latticeΛ is congruent toΓ if and only ifΛ is a direct sum ofk lattices Λi
congruent to Γi. In particular, ifΓ is reducible andΛ is irreducible, then they are
not congruent.
It follows that ifΓ1,..., Γk and Λ1,..., Λk′ are all irreducible, then the products
Γ1×···× Γk and Λ1×···× Λk′ are congruent if and only ifk =k′ and Γi, Λi are
congruent after possibly reordering. To show that two lattices (or quadratic forms)
are isospectral, we use the following result.
Theorem 3.5([90], Cor. 3.7). LetP andQ be the associated matrices of two even
positive definite quadratic forms in2k variables. Define forN≥ 1
µ0(N) :=N
Y
p prime
p|N

1 + 1
p

,
and letNP and NQ be the smallest positive integers such thatNPP−1 and NQQ−1
are even, respectively. Then the quadratic forms are isospectral if and only if
det(P ) = det(Q), NP = NQ, and their representation numbersR(p,t ) and R(q,t )
for t∈ [0, µ0(NP )k
12 + 1] are identical.
We now describe Milnor’s example of two isospectral non-isometric Riemann-
ian manifolds. Let e1,...,e n denote the standard basis vectors ofRn, write 1 =Pn
i=1ei, and define the lattice
En =

x∈ Zn∪
1
2 1 + Z

:
nX
i=1
xi∈ 2Z

.
112 YEARS OF LISTENING TO RIEMANNIAN MANIFOLDS 15
A basis matrix forE4n is given by the4n× 4n matrix
(A4n)ij =



2, if i =j = 1,
1, if i =j, 2≤i≤ 4n− 1,
−1, if j =i + 1, 1≤i≤ 4n− 2,
1
2, if j = 4n, 1≤i≤ 4n,
0, otherwise.
Indeed, the column vectors ofA4n are linearly independent and are all inE4n.
Explicitly,
A4n =


2 −1 0 0 ··· 0 0 0 1
2
0 1 −1 0 ··· 0 0 0 1
2
0 0 1 −1 ··· 0 0 0 1
2
0 0 0 1 ··· 0 0 0 1
2
... ... ... ... ... ... ... ... ...
0 0 0 0 ··· 1 −1 0 1
2
0 0 0 0 ··· 0 1 −1 1
2
0 0 0 0 ··· 0 0 1 1
2
0 0 0 0 ··· 0 0 0 1
2


.
By [37],E8n is irreducible and even for everyn≥ 1. Here, even means that the
square of the norm of any lattice vector is an even number. Now, Milnor’s example
consists of the flat tori associated to the latticesE16 and E8×E8. Since E16 is
irreducible andE8×E8 is reducible, it follows from Proposition 3.4 that the flat
tori are not isometric. It remains to show that they are isospectral. The latticeE16
has basis matrixA16, andE8×E8 has
A8×8 =
A8 0
0 A8

.
Two quadratic formsP andQ associated toE16 andE8×E8 are those with associ-
ated matricesAT
16A16 andAT
8×8A8×8, respectively. These are even, positive definite,
and have determinant 1, as the reader may verify. In fact, the inverses(AT
16A16)−1
and (AT
8×8A8×8)−1 are also even, which gives that NAT
16A16 = NAT
8×8A8×8 = 1.
Since µ0(1) = 1, Theorem 3.5 gives that it is enough to show thatP and Q have
the same multiplicity over 1. That is, we need to show that the equationsP (x) = 1
and Q(x) = 1 have as many distinct solutions inZ16. SinceE8 and E16 are even,
P (x) = (A16x)T (A16x) =||A16x||2,
Q(x) = (A8×8x)T (A8×8x) =||A8×8x||2
are always even. So, they both have multiplicity 0 over 1. This completes the
proof that the flat tori are isospectral, and we conclude that the spectrum of a
Riemannian manifold in general does not determine all of its geometry.
