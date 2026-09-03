---
doc_id: arxiv-math-0203160v3
doc_title: "Differential and complex geometry of two-dimensional noncommutative tori Momar Dieng Albert Schwarz∗ Department of Mathematics University of California"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-8
source_pdf: 0203160v3.pdf
source_sha256: a84f478d72d40af2
doc_brief: "Differential and complex geometry of two-dimensional noncommutative tori Momar Dieng Albert Schwarz∗ Department of Mathematics University of California — We analyze in detail projective modules over"
---
of noncommutative spaces with simplest space of this kind th oroughly
analyzed as a basic example.
1 Introduction
Diﬀerential geometry of noncommutative spaces, in particular, of noncommuta-
tive tori was developed by A. Connes [1], [2]. More detailed analysis of d iﬀer-
ential geometry of noncommutative tori was performed in [3], [4],[14], [15], [16],
[17],[6].
Partly, the interest to this subject was motivated by the applicatio ns to
string/M-theory found in [4] (see [7] for review). Complex geometr y of non-
commutative tori and of projective modules over them was studied in [18] in
connection with noncommutative generalization of theta-function s.
The goal of present paper is to illustrate general results of [18] us ing the
example of two-dimensional noncommutative tori, where all calculat ions can be
performed explicitly. We repeat all basic deﬁnitions, starting with th e deﬁnition
of noncommutative torus. Therefore, the paper can be read inde pendently of
[18] and of other papers about noncommutative tori. However, in t he rest of
the introduction, we assume some knowledge of preceding work.
In Sec. 2 we describe projective modules over two-dimensional non commu-
tative torus and their tensor products. The results of this sectio n are closely
∗ Partially supported by NSF grant No. DMS 9971304
1
related to some results proved in multidimensional case in [18]. We will fo r-
mulate these general results restricting ourselves to basic Tθ- modules (modules
with constant curvature connection where the endomorphism alge bra is another
noncommutative torus Tθ′). Instead of basic modules we can work with cor-
responding ( Tθ′ , T θ)-bimodules. Tensor product of ( Tθ′, T θ)-bimodule E1 and
(Tθ, T θ′′ )-bimodule E2 is a ( Tθ′, T θ′′ )-bimodule E. We can ﬁnd the bimodule E
using the fact that basic bimodules E1 and E2 can be described by means of
elements g1, g 2 ∈ SO(d, d, Z) obeying θ′ = g1θ, θ ′′ = g2θ. Here g1, g 2 act on
the parameter of noncommutativity - antisymmetric matrix θ - by means of
fractional linear transformation. The description of E follows from the re-
lation θ′′ = g2g−1
1 θ′. In two-dimensional case all basic right Tθ–modules can
be represented as modules En,m (see Sec. 2) where m and n are relatively
prime. The space En,m can be considered also as a left Tθ′-module E′
a,m where
an − bm = 1 , a, b ∈ Z, θ ′ = ( aθ + b)(mθ + n)−1, or as ( Tθ′ , T θ)-bimodule that
will be denoted by E1. One can use general results to calculate the tensor
product E1 ⊗
Tθ
E2 where E2 is a ( Tθ, T θ′′ )-bimodule, corresponding to the basic
left Tθ-module E′
k,l. It follows from these results that this tensor product con-
sidered as a left Tθ′ -module is isomorphic to E′
ak+bl,nl+mk. We give a direct
proof of this relation constructing an explicit isomorphism. This cons truction is
used essentially in Sec. 3, devoted to complex geometry of project ive modules
over two-dimensional noncommutative tori. We calculate holomorph ic vectors
(theta-vectors) in basic modules and tensor products of these v ectors. The
relations we obtain generalize well known relations for theta-funct ions. The ap-
pendix contains a very detailed calculation of the tensor product (w e did not
include the appendix into the journal version). We did not try to ana lyze the
connection of our results to Manin’s version of the theory of nonco mmutative
theta–functions [8]–[10]. This is an interesting problem.
2 Projective modules and their tensor products.
One can deﬁne the algebra T d
θ of smooth functions on d-dimensional noncom-
mutative torus as an algebra of formal linear combinations f =∑ C− →n U− →n where− →n ∈ Zd and C− →n are complex numbers tending to zero at inﬁnity faster then
any power and the multiplication is governed by the rule
U− →n U− →m = eπi− →n θ− →mU− →n +− →m
where θ = θαβ is a real antisymmetric matrix. An antilinear involution on
T d
θ is deﬁned by the requirement U ∗− →n = U−− →n . These operations together with
the standard structure of vector space permit us to consider T d
θ as involutive
associative algebra with unit element 1 = U⃗0 and with trace Tr f = C− →0 . We
will ﬁx our attention on the case d = 2; in this case the matrix θαβ can be
speciﬁed by means of one number θ12 = θ and the multiplication is speciﬁed by
the relation
2
U1U2 = e2πiθU2U1
where Uα = U− →eα are elements U− →n corresponding to vectors of standard basis− →e 1 = (1, 0), − →e 2 = (0, 1).
In the case when θ is a natural number T 2
θ is isomorphic to the algebra of
smooth functions on the commutative two-dimensional torus. We w ill consider
projective modules over T 2
θ (we always assume that our modules are ﬁnitely
generated; a projective module is by deﬁnition a direct summand in a f ree
module ( T 2
θ )k). We assume that the number θ is irrational; in this case every
projective right module over T 2
θ is isomorphic to one of the modules En,m deﬁned
in the following way (see [2], [3], [7]). The elements of En,m are functions on
the Schwartz space S(R × Zm) and the action of the generators U1, U 2 of T 2
θ is
given by:
U1 f (x, µ ) = f (x − n + m θ
m , µ − 1)
U2 f (x, µ ) = e2 π i(x−µ n/m) f (x, µ )
We can deﬁne also left modules over T 2
θ replacing θ by −θ in the above formulas;
we will use the notation E′
n,m for left modules. If it is necessary to emphasize
that we consider En,m or E′
n,m as a Tθ–modules we will use the notation En,m(θ)
or E′
n,m(θ). We will assume that the numbers m and n are relatively prime.
Corresponding modules En,m are called basic modules. Every module over T 2
θ
can be represented as a direct sum of isomorphic basic modules. In t his case the
algebra of endomorphisms of the module E = En,m is again a noncommutative
torus Tθ′ generated by operators
Z1 f (x, µ ) = f (x − 1
m , µ − a)
Z2 f (x, µ ) = exp
[
2 π i
( x
n + mθ − µ
m
)]
f (x, µ )
where a, b are integers obeying an − bm = 1. This fact follows from relation
Z1Z2 = e−2πiθ′
Z2Z1
where θ′ = b+a θ
n+m θ . One can consider E as a left Tθ′ -module; this module is
isomorphic to E′
a,m.
We can regard E also as ( Tθ′ , T θ)-bimodule, since the action of Tθ′ commutes
with the action of Tθ. Notice that the bimodule E depends on the choice of
a and b. The tori Tθ and Tθ′ are Morita equivalent and the bimodule E is a
Morita equivalence bimodule ([2], [3], [7]).
Recall that two associative algebras A and B are Morita equivalent if cor-
responding categories of modules are equivalent. Having an ( A, B )-bimodule P
we can assign to every right A-module E a right B-module E′ = E ⊗
A
P where
tensor product over A is obtained from the standard tensor product over C by
3
means of identiﬁcation ea ⊗ p ∼ e ⊗ ap. If this correspondence is invertible we
say that P is a Morita equivalence bimodule.
Let us calculate now the tensor product En,m ⊗
Tθ
E′
k,l where En,m is a right
T 2
θ -module and E′
k,l is a left T 2
θ -module. We will see that this product can be
considered a vector space E = S(R × Znl+mk). Namely, the formula:
h(z, ∆) =
∑
q∈Z
[
f
(
(n + m θ)z − n + m θ
m q + l(n + m θ)
m(n l + m k) ∆ , −q + a ∆
)
·g
(
(n + m θ)z + k − l θ
l q − k − l θ
n l + m k ∆ , q
)]
(1)
where 0 ≤ ∆ ≤ nl + mk − 1, speciﬁes a map of tensor product over En,m ⊗
Tθ
E′
k,l
onto E, so that, with the usual notation, f ∈ En,m(θ) , g ∈ E′
k,l(θ) and h ∈
E′
a k+b l,n l+m k(θ′). This map is an isomorphism between the tensor product
and E. The formula (1) determines a bilinear map that is compatible with
identiﬁcation ea ⊗ p ∼ e ⊗ ap (see Appendix for details). We can consider
En,m as a ( Tθ′ , T θ)-bimodule where θ′ = b+aθ
n+mθ , an − bm = 1 and Ek,l as a
(Tθ, T θ′′ )-bimodule where θ′′ = − d−cθ
k−lθ , ck − dl = 1. Then E can be regarded as
(Tθ′ , T θ′′ )-bimodule. It follows from (1) that E considered as a left Tθ′-module
is isomorphic to E′
N ′,M where M = nl + mk, N ′ = ak + bl and E considered
as a right Tθ′′ -module is isomorphic to EN ′′,M where N ′′ = −(cn + md) for
ck − dl = 1. This result can be obtained also from general considerations (s ee
Introduction).
Let us apply (1) to the special case when:
f (x, µ ) = e− 1
2 σ1 x2−c1 xδµ
α
g(y, ν ) = e− 1
2 σ2 y2−c2 xδν
β
where
σ 1 = iτ1
m
n + m θ, µ ∈ Zm
σ 2 = iτ2
l
k − l θ, ν ∈ Zl
and δi
j is the usual Kronecker–delta. It is straightforward to check tha t in this
4
case:
hα β(z, ∆) =
∑
q∈Z
[
exp
{
− σ 1
2
(
(n + m θ)z − n + m θ
m q + l(n + m θ)
m(n l + m k) ∆
) 2
−c1
(
(n + m θ)z − n + m θ
m q + l(n + m θ)
m(n l + m k) ∆
)}
δ−q−a ∆
α
· exp
{
− σ 2
2
(
(n + m θ)z + k − l θ
l q − k − l θ
n l + m k ∆
) 2
−c2
(
(n + m θ)z + k − l θ
l q − k − l θ
n l + m k ∆
)}
δq
β
]
(2)
Notice that the right hand side of (2) can be expressed in terms of t heta–
functions; ﬁrst note that the set of solutions to the system of co ngruences:
{
q = a ∆ − α (mod m)
q = β (mod l)
can be written as qo + u m l
r for some integer qo, r = gcd(m, l ), and u ∈ Z. Hence
we can substitute qo + u m l
r in for q in (2), do away with Kronecker deltas, and
sum over u instead of q. We obtain:
hα β(z, ∆) = Θ( s, t ) · ξ(z, ∆)
where
ξα β(z, ∆) = exp
[
− σ 1
2
(
(n + m θ) z + l(n + m θ) ∆
m(n l + m k)
) 2
− σ 2
2
(
(n + m θ) z − (k − l θ) ∆
n l + m k
) 2
−(c1 + c2) (n + m θ) z −
(
c1
l(n + m θ)
m(n l + m k) − c2
k − l θ
n l + m k
)
∆
−
(
σ 1
(n + m θ
m
) 2
+ σ 2
(k − l θ
l
) 2)
q2
o
2
]
s = − σ 1 l2 (n + m θ)2 + σ 2 m2 (k − l θ)2
2 π i r2
t = σ 1 (n + m θ)2
2 π i m
(
z + l ∆
m (n l + m k) − l qo
r
)
+ c1
n + m θ
2 π i m − c2
k − l θ
2 π i l
+ σ 2 (k − l θ)2
2 π i l
(
− n + m θ
k − l θ z + ∆
n l + m k − m qo
r
)
and Θ( s, t ) a classical theta–function. We recall that classical–theta funct ions
are deﬁned as:
5
Θ( s, t ) =
∑
u∈Z
eπ i s u2+2π i t u , Im s > 0
3 Connections and complex structures.
One can deﬁne a connection on a right T d
θ -module E as a set of C-linear oper-
ators ∇1, ..., ∇d obeying Leibniz rule:
∇α(ea) = ∇αe · a + e · δαa (3)
where e ∈ E, a ∈ T d
θ and the derivatives δαa are speciﬁed by the formula
δαU− →n = 2 πniU − →n (see[1]). It will be convenient for us to generalize the notion
of connection replacing δα in (3) by δ′
α = aβ
αδβ where aβ
α is a non-degenerate
matrix. A connection ∇1, ..., ∇d is a constant curvature connection if
[∇α, ∇β] = i fαβ · 1
where fαβ are numbers and 1 stands for identity operator. Similar deﬁnitions
can be given for left modules. We always consider unitary connection s (i.e.
operators ∇α should be anti Hermitian). It is easy to check that operators
∇1 = 2 π i m
n + mθ x, ∇2 = 2 π d
dx (4)
specify a constant curvature connection of right Tθ-module Em,n. The same
operators determine a connection (in generalized sense) on En,m considered
as a left Tθ′-module. This follows from relations [ ∇i, ∇j] = 2π i m
n+mθ . We see
that ∇1, ∇2 can be considered as a constant curvature connection on ( Tθ′ , T θ)-
bimodule.
If ∇1, ∇2 is a constant curvature connection on a module E we can introduce
a complex structure on E ﬁxing ∂-connection ∇ = λ 1∇1+λ 2∇2, where λ 1 and λ 2
are complex numbers and the quotient τ = λ 1/λ 2 is not real [18]. This complex
structure on a Tθ-module corresponds to complex structure on Tθ, speciﬁed by
means of ∂-derivative λ 1δ1 + λ 2δ2. By deﬁnition, vector Θ ∈ E is holomorphic
if:
∇Θ = 0
Notice that the notion of holomorphicity depends only on τ = λ 1/λ 2, therefore
we say that ∇ and ρ∇ where ρ ⁄= 0 determine the same complex structure
on E. Holomorphic vectors are closely related to theta-functions, henc e we call
holomorphic vectors in basic modules theta-vectors.
Let us consider holomorphic vectors in Tθ-modules En,m, assuming that n
and m are relatively prime. In this case all constant curvature connectio ns have
the form ∇α = ∇0
α + cα, where ∇0
α stand for the connection (4) and c1, c 2 are
constants. The equation ∇Θ = 0 takes the form
(iτ m
n + mθ x + ∂
∂x + c)ϕ (x, µ ) = 0
6
If Im τ < 0 it has m linearly independent solutions
ϕ α(x, µ ) = e− 1
2 σx2−cxδµ
α (5)
where
σ = iτ m
n + m θ, µ ∈ Zm
The functions (5) belong to S only if Re σ > 0. We assumed that n + mθ > 0;
in the case n + mθ < 0, the condition of existence of holomorphic vectors is
that Im τ > 0. We see that in the case when holomorphic vectors exist the
space Hn,m of holomorphic vectors in En,m is m-dimensional; the functions
(5) constitute a basis of Hn,m. Considering En,m as a ( Tθ′ , T θ)-bimodule and
taking into account that a constant curvature connection on En,m is a con-
stant curvature connection on the bimodule, one can deﬁne a notio n of complex
structure and of holomorphic vector for a bimodule. More precisely , complex
structure on Tθ-module En,m induces a complex structure on same space con-
sidered as left Tθ′-module in such a way that the notion of holomorphic vector
remains the same. These two complex structures specify a complex structure
on a bimodule; the notion of holomorphic vector in a bimodule coincides w ith
corresponding notion for both modules. If E ′ is a complex ( Tθ′ , T θ)-bimodule,
E ′′ is a complex ( Tθ, T θ′′ )-bimodule, then the ( Tθ′ , T θ′′ )-bimodule E = E ′ ⊗
Tθ
E ′′
can be equipped with complex structure. We assume that complex st ructure on
the right Tθ-module E ′ and on the left Tθ-module E ′′ correspond to the same
complex structure on Tθ. One can prove [18] that tensor product of two holo-
morphic vectors is again a holomorphic vector (i.e. we have a natural map
H′ ⊗ H′′ into H where H′, H′′ and H stand for spaces of holomorphic vectors in
E ′, E ′′ and E correspondingly). Let the basis of H′ consist of:
ϕ ′
α = e− 1
2 σ1 x2−c1 xδµ
α
where
σ 1 = iτ1
m
n + m θ, µ ∈ Zm, α ∈ {1, . . . , m }
and the basis of H′′ consist of:
ϕ ′′
β = e− 1
2 σ2 y2−c2 xδν
β
where
σ 2 = iτ2
l
k − l θ, ν ∈ Zl, α ∈ {1, . . . , l }
We assume that E ′, considered as a right Tθ–module, is isomorphic to En,m ,
and that E ′′, considered as a left Tθ–module, is isomorphic to E′
k,l. We can use
(2) to calculate ϕ ′
α ⊗
Tθ
ϕ ′′
β. The condition that complex structures on E ′ and E ′′
correspond to the same complex structure on E implies τ1 = τ2. Using this, we
7
can check that the theta–functions that appear in (2) do not dep end on z in our
case. Applying (2), we obtain that, ϕ ′
α ⊗
Tθ
ϕ ′′
β maps to Ξ α β(z, ∆) ∈ H which is
of the form:
Ξ α β(z, ∆) =
∑
γ
cγ
α β ϕ γ(z, ∆)
where
ϕ γ(z, ∆) = exp
[ π i τ(n l + m k)(n + m θ)
k − l θ z2 − (c1 + c2)(n + m θ)z
]
δ∆
γ
constitute a basis of H and the constants cγ
α β are given by:
cγ
α β = Θ( s, t ) · eK
where Θ( s, t ) a classical theta–function,
K = − π i τ l
m(n l + m k) γ 2 − (l(n + m θ)c1 − m(k − l θ)c2 )
m(n l + m k) γ + π i s q2
o + 2 π i t qo
and:
s = −m l (n l + m k)
t = l τ ∆ − qo(n l + m k)
r + c1 l (n + m θ) − c2 m (k − l θ)
2π i r
