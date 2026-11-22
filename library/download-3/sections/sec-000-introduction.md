---
doc_id: download-3
doc_title: "Algebraic index theorem"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-6
source_pdf: Download (3).pdf
source_sha256: 7c2b83ba9f9baad7
toc_source: inferred
doc_brief: "Algebraic index theorem — We prove the Atiyah-Singer index theorem where the algebra of pseudo- differential operators is replaced by an arbitrary deformation quantization of the algebra of functions"
---
This paper is the first in a series aimed at providing an algebraic insight to various
Atiyah-Singer type index theorems.
In recent years much research was devoted to finding explicit local proofs of
Atiyah-Singer and Riemann-Roch theorems. In the works of Bismut, Gillet, Soule,
Getzler, Witten and Fedosov, the index of an operator (usually Dirac operator) was
expressed as the trace of a certain infinite dimensional operator; the asymptotic ex-
pansion of this trace provided a local formula. OΈrian, Toledo and Tong [TT, BTT]
developed an explicit method of computing a certain cohomology class in the Cech
complex. The integral of that class over a complex manifold is known to be the
Euler characteristic of the analytic sheaf; thus the computation yields the ex-
plicit proof of the Riemann-Roch theorem. Arbarello, de Concini, Kac and Procesi
[ACKP] suggested a method of proving the Riemann-Roch-Grothendieck 
theorem
(inspired by string theory). One of the crucial steps of that method was the passage
to a certain infinite dimensional manifold. The De Rham complex of that mani-
fold is closely related to Gelfand-Fuks cohomology of the Lie algebra of vector
fields; the computation was finally reduced to an explicit computation in Lie algebra
cohomology. This method was further developed by Feigin and Tsygan [FT].
One of the useful tools in proving the index theorems is cyclic cohomology.
This cohomology was independently introduced by Connes and Tsygan. In Connes'
approach, it was intimately related to the index theory. The idea, going back partly
to Helton and Howe [HH], is, roughly speaking, that the cyclic cocyles, being
higher analogues of the traces, provide a natural algebraic framework for trace
Partially supported by NSF Grant DMS-9101817.
224 
R. Nest, B. Tsygan
computations. This facilitates the explicit computation of the index as the trace of
a certain operator.
Such a computation of the index of the Dirac operator is due ot Connes.
Another proof of the Atiyah-Singer theorem, for the case when the manifold is
a linear space, was given by Elliot, Natsume and Nest. This proof was more
directly in line with the work of Helton and Howe. We will outline this
proof later.
In this paper, we will state and prove a purely algebraic theorem which is parallel
to the index theorem. It works in a much more general framework. Instead of the
ring of pseudodifferential operators on a manifold we will consider any deformation
of the algebra of functions on a sympletic manifold, (cf. [BFFLS]; it is well known
that the ring of pseudodifferential operators can be viewed as a deformed algebra
of functions on the cotangent bundle).
A similar theorem was proved by B. Fedosov (by completely different methods);
cf. [F].
Note that the approach of this paper, though quite different, is closely related to
the recent paper by Connes, Flato and Sternheimer [CFS].
The Atiyah-Singer theorem does not follow directly from the algebraic state-
ment. But it can be proved along the same algebraic lines. We will do that in a
separate paper. Here we will concentrate on the algebraic case.
First, to give an example (and also to explain why our algebraic theorem is
indeed the algebraic form of the index theorem), let us recall the proof of the index
theorem for IR" due to Elliot, Natsume and Nest. Let D be an elliptic differential
operator on C°°(R
W); assume that D = 1 outside some compact. Let e^ be the
orthogonal projection onto the graph of D in Z,2(IR'
7) θ Z,2(1R
A?). This is a pseudo-
differential operator in the trivial bundle (C
2 over IRΛ One can construct an explicit
homotopy e(t\ 0 ^ t ^ 1, such that e(\) = eD and e(0) = K \-Q)> where P
(resp. Q) is the orthogonal projection onto the kernel (resp. cokernel) of D. One
has, obviously,
index D = Tr (e(0 - (^ 
^ J J . 
(0.1)
The operator CD — ({j ?) *
s not trace class. This suggests that, in order to compute
the trace in (0.1) in terms of ep, one should replace the trace with a suitable higher
trace, or a cyclic cocycle. Let UQ, a\, #2,... be integral operators with compactly
supported kernels. Put
Θ(aQ9...,a2n) = -T Σ sgn(σ) 
Ύr(aQ[yσ\, a\] - 
- [yσ(2n), a2n]) , 
(0.2)
nl^Σ2π
where (y\,...,y2n) = (3*,, *ι,...,d r, l 5 χn).
One checks that
(1) Θ is a cyclic cocyle cohomologous to the cocyle Tr(αo 
«2/?) From this
one deduces that
(2) 0(e(0),...,e(0)) = 6>(<?(l ),..., e(l)) 
(0.3)
Algebraic Index Theorem 
225
Note that the above formula of Connes is true for any cyclic cocyle Θ on an
algebra A and for any two homotopic idempotents e(0), e(l) in A. The problem is
that Θ is not defined on an algebra containing β(l). So one has to check that:
i) the right-hand side of (0.3) makes sense;
ii) Connes' explicit calculation proving (0.3) makes sense for the explicit
homotopy e(t).
Now let us compute Θ(eD, 
,eo\ Let h be a non-zero parameter. Let D =
D(x, 3Y); D(h) = D(x, hdx). Then index D = index D(h) for any h\ therefore, be-
cause of the well known formula for the trace,
index D = — lim ΣsgΆ(σ)ΊreD(h)[yσ\,eD(h)] 
- yσ(2n^eD(h}]
n\ h^o σ
= — lim ^Tr / σ(eD){yσ\,σ(eD)} 
{yσ(2n),σ(eD)}dξ\ 
dxn .
n. n —»0 σ 
^2/ί
But σ(eo)(x, c) = eσ(D^x^ - the orthogonal projection onto the graph of the 2 x 2
matrix σ(D)(x, ξ). Clearly the last limit is equal to ^f^2n^σ(D)deσ(D) 
- -deσ(D).
Now, let X be a compact C°° manifold. Let D be an elliptic differential operator
on X. Let eo be the projection onto the graph of D in L2(X) ΘZ^C-Ό There exists
a homotopy between βo and e(Q) as above. To compute the index of D one has to
construct the analogue of the fundamental cocyle Θ. Then, rescaling the cotangent
bundle by the transformation ξ ι—> ^c, one passes to a one-parameter family of
projectors eD(h). Using the explicit formula for 6>, one has to show that
index/) = lim indexD(h) = f ch eσ(D) 
td(Tχ 0 C) ,
Λ-*O 
τ*x
where σ(D) is the symbol of D, σ(D) is the projection onto its graph and td is the
Todd class.
In this paper we will prove the parallel algebraic theorem. Let (M, ω) be any
symplectic manifold (instead fo T*X). Let us define, following [BFFLS],
f*9 = fg + hφ\(f, 9} + h
2φ2(f, g}λ— ,
a formal deformation of the ring C°°(M). We assume that lim^oi/ * (] — 9 * /) =
{/, g}, that φ/(/, g ) are differential expressions in /, g and that !*/ = / * ! = / .
Consider the algebras A*(M) = (C°°(M)[[n]],*) and Ag(M) - (^(MX^]],*).
If ^ is an algebra over a ring & then #~ — B + Λ: is the algebra 5 with adjoined unit.
One can construct the canonical trace Tr : Aj(M) —» (Cfft""
1, fe]] such that for
/ G Cf°°(M),
Tr(/) - ^ f -ί// 
ω
n + ftτ,(/) + ^
2τ2(/) +
n \n\M
and Tr(/ * g - cj * /) — 0, where τ/(/) are local expressions in /. Also, consider
an idempotent e in the matrix algebra MW(AQ(M)~).
Let e(oo) be the constant value of e at infinity of M; βo = β | h = 0; βo(cχo) =
e(oo) ft = 0.
In our idealized approach, A
tl(M) stands for all pseudodifferential operators;
AQ(M) stands for pseudodifferential operators of negative order; Tr stands for the
226 
R. Nest, B. Tsygan
operator trace; e stands for the projection CD onto the graph of an elliptic differential
operator D; e$ stands for eσ(£>); βo and βo(oo) stand for (|j
Let ch(βQ) = 5^Ai^tr e§(de§)
n G Ω
ev(M). Aslo, let td(ω) be the Todd class of
the reduction of the bundle of symplectic frames on M from Sp(2n) to ί/(«); let
c,(ω) be the Chern classes of that reduction.
For any deformation one can define a characteristic class θ G //
2(M, C[[fe]]).
(We do this in Sect. 5). One has θ = ω + MI 
-\ 
h A'θ/ H 
, θ, e //
2(M, <C).
Theorem 1.1.1.
Tr(e - e(oo)) = J(c/z(β0) - tr β0(oo)) td(ω) 
e~
C}(ω^
2e°
/fi .
M
For the special deformations this was proved by B. Fedosov [F].
The purpose of this paper is to prove this theorem using the method outlined
above. In fact the paper is mainly devoted to constructing the analogue of the
fundamental cyclic cocycle Θ.
First, in Sect. 2, we construct a Poincare duality map in cyclic homology. Let
AQ be an algebra over commutative ring k, g a Lie subalgebra of Der(^o). Let
τ: AQ/^AQ —» k be a trace. We construct a map
where C* is the standard Lie algebra complex and CC*er is the periodic cyclic
cochain complex.
Now, let A be an algebra over a ring k and v4o an ideal in A\ let τ: AQ/[A, AQ] —»
& be a trace. Passing to the matrix algebras and using the well known connection
between Lie algebra and cyclic homologies, we construct the map
χτ:~CC*-\(A)—> CC~G*(AQ) , 
(0-5)
where CC* is the reduced cyclic complex. Note that, to some extent, all known
characteristic classes with values in periodic cyclic cohomology account for partic-
ular cases of the maps (0.4) and (0.5) (Sect. 2.4). We prove the crucial property
of the map (0.5): there exists a map CC*_2(&) —» CC~Q*(AQ), making the diagram
CC-r (/lo)
(0.6)
commute up to homotopy. Here d is the boundary operator.
Apply the construction above to A = A^(M), AQ = AQ(M), τ = Tr. The dia-
gram (0.6) is in fact a diagram of complexes of sheaves. We show in Sect. 3 that
this diagram can be extended to the diagram
(0.7)
where C* is the Cech complex.
Algebraic Index Theorem 
227
Let J^*(M, A [ft 
]) be the hyperhomology of the double complex C*(M, CC*_ i
( A
f l ) ) [ h ~
] ] . We show that ffiιn-\ is canonically isomoφhic to k = (Cfft^^ft]]. Let
Ω be the generator of J^2/?-ι
In the case when M = IR
2'
7, Ω is represented by the cochain ^-ζ\ /\x\ Λ 
Λ
ζn /\xn (of course there is no need to involve Cech complexes). The fundamental
cocycle Ω is equal to χτι(Ω). The fact that Ω and Tr(#o... a^n) are cohomologous
follows from the commutativity of (0.6).
Now, note that the (2n - 2)
th hyperhomology group of C*(M, CC*(&)) is iso-
moφhic to H
ev(M,k\ In Sect. 4 we show that Theorem 1.1.1 follows from the
equality
dΩ — ε(td(ct}) 
e~
Cχ^
ω'^ + /
? ) ~ 
9 
(0.8)
where ε H
n(M) = (-1)
A'. Put 6) = χTl(ίd(ω)U Ω).
Then
Tr(β — e(oo)) = (Θ,ch(e)) ,
where c/?(e) is the Chern character in periodic cyclic homology. An explicit calcu-
lation shows that for any periodic cyclic α of Aj
7(M),
lim((9,o( 
e~
0 / f l) = Jα 
td(ω) 
e~
Γι
(ω)/2 .
On the other hand, there is a rigidity property: if α is a periodic cyclic cycle of
AQ(Λ/) 0ί;£r C (that is, if one considers C, not C[[ft]], as the ring of scalars), then
Tr(α 
e ~
0 / f l ) does not depend on ft. The theorem follows.
It remains to prove (0.8). The proof occupies Sects. 5,6. We reduce the prob-
lem to the local computation. Let A/* be the standard deformation of the ring of
power series < E [ [ x \ , . . . , x n , ξ \ 9 . . . , ξ n ] ] . Let g be the Lie algebra A^/C[[ft]] with the
bracket [/, g] = |(/ * g - g * /). Let I) be the subalgebra {^aljx!ξ/ \ at/ G C}. Let
Jf*(g,ί); A
f 7[ft~']) be the hyperhomology of the double complex C*(g,i); CC*(A*)).
Then rJ#2n-\ is one-dimensional; let Ω be the generator. There is the boundary map
d : C*(g,ί);CC*(A
f7)) -» C*(&fyCC*-\(k)). 
This provides the canonical element
dΩ of //^(g, ly,k) and
cΩ = ε(td(c\,...,cn) 
- e-
c\!
2+
0<
l1}y\ . 
(0.9)
Here ε | H
u = (-1)
A; c/ are the algebraic Chern classes in //
2/(g,ί); (C); (9 is the
2-cocycle coming from the central extension 0 —* C[[ft]] —^ A
f? —» g —^ 0.
To reduce (0.8) to (0.9) (and to define the element 0 of//
2(M,(Γ[[ft]])), we re-
place M by a certain infinite dimensional manifold of "non-linear frames" (compare
with [ACKP,FT].
Finally, the local formula (0.9) is proved by a computation. This completes the
proof of Theorem 1.1.1. In Sect. 1 we prove a conjecture of B. Feigin (from which
the Riemann-Roch theorem can be easily deduced). Let M be an ^-dimensional
complex manifold; let £% be the sheaf of holomoφhic differential operators on M.
Let C*(M,CC*(^M)) be the Cech hypercomplex; let HC*(^M) be its hyperho-
mology. It was shown by Brylinski [B] that HCo(^M) -^//
2/7(M, C).
On the other hand, the trivial cocycle 1 G C°(M, CCo) provides an element of
HC0(^/v/) and therefore an element [1] of//
2/7(M,C). We prove that [1] = td(M)2n.
This is an easy consequence of (0.8) (with A^(Γ*M) replaced by @M)
228 
R. Nest, B. Tsygaπ
There is also a holomorphic version of Theorem 1.1.1. We will discuss it in
another paper.
To construct the maps (0.4)-(0.7) and to prove (0.9), we use the operations on
the cyclic complex. Let us discuss them in some more detail.
First, let X be a C°° manifold. Let g be the algebra of vector fields on X.
For D G g, the operations LD\ Ωχ —» Ωχ and 
/£>: Ωχ —> Ωχ~
l 
are defined, sub-
ject to standard relations (like [io,d] = LD). Let ε be an odd formal parameter,
ε
2 = 0; g[ε] = g ® C[ε]. Let δ = d/dε: g[ε] -» g[ε], δφ + Eε) = £. Then the set
of standard relations for L/>, /# is equivalent to the following:
the differential graded Lie algebra (g[ε],<5) acts on the complex Ωχ via D +
Eε^ LD + iE.
This algebra can be extended. Let A — C°°(X); put //(ω) = / 
ω, Lf(co) =
df /\ω for / eA. Let 4 be the g-module A concentrated in the odd degree; let
QxAbε the semi-direct product. Then
the differential ^-graded algebra (g><4)[^] acts on the ^-graded complex Ωx
via D -f Eε H^ Lβ -f- /£•; Z),£ £ 0 xA.
Now, let ^ be an arbitrary algebra; g = Der(^). For D £ g, a £ A one
can define the operations LD, ia: CCl
