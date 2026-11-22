---
doc_id: oberwolfachreports1223-v20120708-9-40
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by"
section_id: sec-013-yokonumahecke-algebras
section_title: "Yokonuma–Hecke algebras"
section_number: null
pages: 28-31
source_pdf: OberwolfachReports1223_v20120708_9_40.pdf
source_sha256: 94f82cfc185955ba
toc_source: inferred
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by — This meeting concentrated on topological invariants in low di"
---
Sofia Lambropoulou
(joint work with Maria Chlouveraki)
We compare the knot invariant deﬁned using the Juyumaya trace on the
Yokonuma-Hecke algebras with the 2-variable Jones polynomial, and we show that
they do not coincide except in a few trivial cases.
1. The 2-variable Jones or HOMFLYPT polynomial
Let Bn denote the Artin braid group of type A. Closing a geometric braid
β with simple arcs gives rise to an oriented knot or link ,β and, by the classical
Markov theorem, oriented knot or link types are in bijective correspondence with
equivalence classes of braids in ∪nBn under the moves:
(i) Conjugation in each Bn: αβ ∼βα;
(ii) Positive and negative stabilization: α ∼ασn±1, α ∈Bn.
Let q ∈C \ {0}. The Iwahori-Hecke algebra Hn(q) of type A is a C-associative
algebra with generators G1, G2, . . ., Gn−1, which can be deﬁned as the quotient
of the algebra CBn over the quadratic relations G2
i = (q −1)Gi + q for all i. The
algebras Hn(q) support the Ocneanu trace with parameter ζ [3, Theorem 5.1], a
unique linear Markov trace τ : -
n≥0 Hn(q) −→C[ζ]. Another characterization of
the Ocneanu trace can be given by its values on the basis elements Gwµ, τ(Gwµ) =
ζℓ(wµ), where wµ is a minimal length representative of the conjugacy class of Sn
parametrized by the partition µ of n [2], and ℓ(wµ) denotes the length of wµ. After
re-scaling and normalizing the Ocneanu trace according to the Markov theorem,
Jones constructed the 2-variable Jones or HOMFLYPT polynomial [3], an isotopy
invariant of oriented links:
P(,α) = (DH)n−1(√λH)ϵ(α) (τ ◦π) (α)
where α ∈Bn, for any n ∈N, π : CBn −→Hn(q) is the natural algebra epi-
morphism that maps the braid generator σi to the algebra generator Gi, ϵ(α) is
the algebraic sum of the exponents of the braid generators in the braid word α,
λH := ζ+(1−q)
qζ
and DH := −
1−λHq
√λH(1−q) =
1
ζ√λH .
2. Link invariants from the Yokonuma-Hecke algebras
The Yokonuma-Hecke algebra [7], Yd,n(u), for d ∈N and u ∈C\{0}, is a C-
associative algebra with generators g1, . . . , gn−1, t1, . . . , tn, satisfying: the braid
relations for the gi’s, the relations titj = tjti for all i, j, the modular relations
td
j = 1 for all j, the mixed relations tjgi = gitsi(j) for all i, j, where si denotes the
transposition (i, i + 1), and the quadratic relations:
g2
i
=
1 + (u −1) ei + (u −1) ei gi
for all i
where ei := 1
d
.d−1
s=0 ts
it−s
i+1, idempotents in Yd,n(u).
Invariants in Low-Dimensional Topology and Knot Theory
29
The algebras Yd,n(u) support the Juyumaya trace with parameters z, x1, . . . ,
xd−1 in C\{0} [4, Theorem 12], a unique linear Markov trace tr : -
n≥0 Yd,n(u) −→
C[z, x1, . . . , xd−1]. Trying to normalize and re-scale the Juyumaya trace according
to the Markov braid equivalence, in order to obtain a link invariant, turns out to be
impossible, basically because tr(αen)̸ = tr(en)tr(α), unless the trace parameters
x1, . . . , xd−1 satisfy the so-called E-system [5, 6]:
.d−1
s=0 xm+sxd−s = xm
.d−1
s=0 xsxd−s
(m = 1, . . . , d −1)
where the sub-indices on the xj’s are regarded modulo d and x0 := 1. As it is
shown in [5] (in the Appendix by Paul G´erardin), the solutions of the E-system are
parametrized by the non-empty subsets S of Z/dZ. The case E := tr (ei) = 1 leads
to the “trivial” solution: x1 a d-th root of unity and xm = xm
1 (m = 1, . . . , d −1).
Given a solution XS = {x1, . . . , xd−1} of the E-system, a link isotopy invariant
∆S was deﬁned in [6], depending on the variables u, z:
∆S(,α) = Dn−1
Y
(√λY)ϵ(α) (tr ◦δ) (α),
where α ∈Bn, for any n ∈N, δ : CBn −→Yd,n(u) is the natural algebra
homomorphism that maps the braid generator σi to the algebra generator gi,
ϵ(α) is the sum of the exponents of the braid generators in the braid word α,
λY := z+(1−u)E
uz
, and DY :=
1−λYu
√λY(1−u)E =
1
z√λY .
3. Comparing P and ∆S
It is natural to ask how the invariants P and ∆S compare. Computational data
so far do not indicate that one invariant is stronger than the other. Thus, it is
possible that the two invariants are topologically equivalent. For comparing the
two invariants we would like to introduce a given solution of the E-system as early
in the construction as possible. Therefore, in [1] we ﬁrst consider the specialization
map θ : C[z, x1, . . . , xd−1] −→C[z], given by z 2→z and xm 2→xm (m = 1, . . . , d −
1), for x1, . . . , xd−1 ∈C \ {0}. Then we consider the specialized Juyumaya trace
θ ◦tr with parameter z and we show that, as in the case of the Ocneanu trace,
this is uniquely determined by its values on the elements gwµ, tr(gwµ) = zℓ(wµ).
We show this by considering the linear map ϕ : -
n≥0 Yd,n(u) −→-
n≥0 Yd,n(u)
deﬁned inductively on Yd,n(u), for all n ∈N, by the following rules:
ϕ(1)
=
1
ϕ(wngngn−1 . . . gitk
i )
=
gnϕ(wngn−1 . . . gitk
i )
ϕ(wntk
n+1)
=
xkϕ(wn)
where wn ∈Yd,n(u), x1, . . . , xd−1 ∈C \ {0}, x0 = 1 and k ∈Z/dZ. Then we show
that tr◦ϕ = θ◦tr and that ϕ(Yd,n(u)) is the C-linear subspace of Yd,n(u) spanned
by the elements gwµ.
Mapping now gi 2→Gi and tm
i
2→xm
(m = 1, . . . , d −1) does not deﬁne an
algebra homomorphism between Yd,n(u) and Hn(u), unless we are in the case
E = 1. In this case we can then show that P and ∆S coincide.
30
Oberwolfach Report 28/2012
The map ϕ provides us with the earliest possible specialization to a solution
of the E-system during the construction of ∆S. So, we proceed in [1] with com-
paring the invariants P and ∆S as maps on isotopy classes of knots and links.
Forcing P = ∆S on the identity braid 1 in each Bn we deduce DH = DY.
Then, taking α = σ2
1, α = σ3
1 and α = σ1σ2
2σ1σ2
2 we ﬁnd necessary condi-
tions for the maps P and ∆S to coincide.
Namely, when u = 1 or q = 1 or
E = tr(ei) = 1.
Then we prove that these are also suﬃcient conditions for
the maps P and ∆S to coincide on any braid α. Our proof is by induction on
ν(α) := | sum of all negative exponents of the braid generators in α |. For the ﬁrst
step (ν(α) = 0), we proceed by induction on n on the braid monoid B+
n , see [1]
for details. To recapitulate, in [1] we prove the following.
Theorem 1. Let XS be a solution of the E-system. Let tr be the Juyumaya trace
on Yd,n(u) with parameters z, XS, and let τ be the Ocneanu trace on Hn(q) with
parameter ζ. Let E = tr(ei) for all i = 1, . . . , n −1. Then P = ∆S or, more
generally, P is a scalar multiple of ∆S if and only if we are in one of the cases
portrayed in the following tables:
Case
q
ζ
u
z
E
1
1
z
1
C∗
any
2
1
−z
1
C∗
any
3
C∗
q
1
1
any
4
C∗
q
1
−1
any
5
C∗
−1
1
1
any
6
C∗
−1
1
−1
any
7
1
E
C∗
−E
any
Case
q
ζ
u
z
E
8
1
−E
C∗
−E
any
9
C∗
q
C∗
−1
1
10
C∗
q
C∗
u
1
11
C∗
−1
C∗
−1
1
12
C∗
−1
C∗
u
1
13
u
z
C∗
C∗
1
14
1/u
−z/u
C∗
C∗
1
Acknowledgements. The research project is implemented within the framework of
the Action “Supporting Postdoctoral Researchers” of the Operational Program “Edu-
cation and Lifelong Learning” (Action’s Beneﬁciary: General Secretariat for Research
and Technology), and is co-ﬁnanced by the European Social Fund (ESF) and the Greek
State.
References
[1] M. Chlouveraki, S. Lambropoulou, The Yokonuma-Hecke algebras and the HOMFLYPT
polynomial, submitted for publication. See arXiv:1204.1871.
[2] M. Geck, G. Pfeiﬀer, Characters of ﬁnite Coxeter groups and Iwahori-Hecke algebras, Lon-
don Math. Soc. Monographs, New Series 21, Oxford University Press, New York, 2000.
[3] V. F. R. Jones, Hecke algebra representations of braid groups and link polynomials, Annals
of Math. 126 (1987), no. 2, 335–388.
[4] J. Juyumaya, Markov trace on the Yokonuma-Hecke algebra, J. Knot Theory and its Ram-
iﬁcations 13 (2004) 25–39.
[5] J. Juyumaya, S. Lambropoulou, p-adic framed braids II, submitted for publication. See
arXiv:0905.3626.
[6] J. Juyumaya, S. Lambropoulou, An adelic extension of the Jones polynomial, M. Banagl,
D. Vogel (eds.) The mathematics of knots, Contributions in the Mathematical and Compu-
tational Sciences, Vol. 1, Springer.
[7] T. Yokonuma, Sur la structure des anneaux de Hecke d’un groupe de Chevallley ﬁni, C.R.
Acad. Sc. Paris, 264, 344–347 (1967).
Invariants in Low-Dimensional Topology and Knot Theory
