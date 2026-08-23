---
doc_id: 0309214v3
doc_title: "The colored Jones function is q-holonomic"
section_id: sec-004-14-acknowledgements
section_title: "Acknowledgements"
section_number: 1.4
pages: 5-10
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
doc_brief: "The colored Jones function is q-holonomic — A function of several variables is called holonomic if, roug hly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many l inear"
---
The authors wish to express their gratitude to D Zeilberger w ho introduced
them to the wonderful world of holonomic functions and its re lation to discrete
mathematics. Zeilberger is a philosophical co-author of th e present paper.
Geometry & Topology, Volume 9 (2005)
1258 Stavros Garoufalidis and Thang T Q Lˆ e
In addition, the authors wish to thank A Bernstein, G Lusztig , and N Xie for
help in understanding quantum group theory, G Masbaum and K H abiro for
help in a formula of the cyclotomic expansion of the colored J ones polynomial,
and D Bar-Natan and A Riese for computer implementations.
The authors were supported in part by National Science Found ation.
2 q–holonomic and q–hypergeometric functions
Theorem 1 follows from the fact that the colored Jones functi on can be built
from elementary blocks that are q –holonomic, and the operations that patch
the blocks together to give the colored Jones function prese rve q –holonomicity.
IN Bernstein deﬁned the notion of holonomic functions f : Rr − →C, [2, 3].
For an excellent and complete account, see Bjork [4]. Zeilbe rger’s brilliant idea
was to link the abstract notion of holonomicity to the concre te problem of algo-
rithmically proving combinatorial identities among hyper geometric functions,
see [35, 33] and also [28]. This opened an entirely new view on combinatorial
identities.
Sabbah extended Bernstein’s approach to holonomic functio ns and deﬁned the
notion of a q –holonomic function, see [31] and also [6].
2.1 q–holonomicity in many variables
We brieﬂy review here the deﬁnition of q –holonomicity. First of all, we need an
r–dimensional version of the q –Weyl algebra. Consider the operators Ei and
Qj for 1 ≤ i, j ≤ r which act on discrete functions f : Nr − →Z[q±] by:
(Qif )(n1, . . . , nr) = qnif (n1, . . . , nr)
(Eif )(n1, . . . , nr) = f (n1, . . . , ni−1, ni + 1, ni+1, . . . , nr).
It is easy to see that the following relations hold:
QiQj = QjQi EiEj = EjEi
QiEj = EjQi for i ⁄= j E iQi = qQiEi
(Relq)
We deﬁne the q –Weyl algebra Ar to be a noncommutative algebra with pre-
sentation
Ar = Z[q±1]⟨Q1, . . . , Qr, E1, . . . , Er⟩
(Relq) .
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q –holonomic 1259
Given a discrete function f with domain Nr or Zr and target space a Z[q±1]–
module, one can deﬁne the left ideal If in Ar by
If := {P ∈ A r|P f = 0}.
If we want to determine a function f by a ﬁnite list of initial conditions, it does
not suﬃce to ensure that f satisﬁes one nontrivial recursion relation if r ≥ 2.
The key notion that we need instead is q –holonomicity.
Intuitively, a discrete function f : Nr − →Z[q±] is q –holonomic if it satisﬁes
a maximally overdetermined system of linear diﬀerence equations with polyno-
mial coeﬃcients. The exact deﬁnition of holonomicity is thr ough homological
dimension, as follows.
Suppose M = Ar/I , where I is a left Ar –module. Let Fm be the sub-space of
Ar spanned by polynomials in Qi, Ei of total degree ≤ m. Then the module
Ar/I can be approximated by the sequence Fm/(Fm ∩ I), m = 1 , 2, .... It
turns out that, for m >> 1, the dimension (over the fractional ﬁeld Q(q)) of
Fm/(Fm ∩ I) is a polynomial in m whose degree d(M ) is called the homological
dimension of M .
Bernstein’s famous inequality (proved by Sabbah in the q –case, [31]) states
that d(M ) ≥ r, if M ⁄= 0 and M has no monomial torsions , ie, any non-trivial
element of M cannot be annihilated by a monomial in Qi, Ei . Note that the
left Ar –module Mf := Ar · f ∼
= Ar/If does not have monomial torsion.
Deﬁnition 2.1 We say that a discrete function f is q –holonomic if d(Mf ) ≤ r.
Note that if d(Mf ) ≤ r, then by Bernstein’s inequality, either Mf = 0 or
d(Mf ) = r. The former can happen only if f = 0.
Although we will not use in this paper, let us point out an alte rnative cohomo-
logical deﬁnition of dimension for a ﬁnitely generated Ar module M . Let us
deﬁne
c(M ) := min {j ∈ N | Extj
Ar (M, Ar) ⁄= 0}.
Then the homological dimension d(M ) := 2 r − c(M ) equals to the dimension
d(M ) deﬁned above.
Closely related to Ar is the q –torus algebra Tr with presentation
Tr = Z[q±1]⟨Q±1
1 , . . . , Q±1
r , E±1
1 , . . . , E±1
r ⟩
(Relq) .
Elements of Tr acts on the set of functions with domain Zr , but not on the set
of functions with domain Nr . Note that Tr is simple, but Ar is not. If I is a
left ideal of Tr then the dimension of Tr/I is equal to that of Ar/(I ∩ Ar).
Geometry & Topology, Volume 9 (2005)
1260 Stavros Garoufalidis and Thang T Q Lˆ e
2.2 Assembling q–holonomic functions
Despite the unwelcoming deﬁnition of q –holonomic functions, in this paper we
will use not the deﬁnition itself, but rather the closure properties of the set of
q –holonomic functions under some natural operations.
F act 0
• Sums and products of q –holonomic functions are q –holonomic.
• Specializations and extensions of q –holonomic functions are q –holonomic.
In other words, if f (n1, . . . , nm) is q –holonomic, the so are the functions
g(n2, . . . , nm) :=f (a, n2, . . . , nm)
and h(n1, . . . , nm, nm+1) :=f (n1, . . . , nm).
• Diagonals of q –holonomic functions are q –holonomic. In other words, if
f (n1, . . . , nm) is q –holonomic, then so is the function
g(n2, . . . , nm) := f (n2, n2, n3, . . . , nm).
• Linear substitution. If f (n1, . . . , nm) is q –holonomic, then so is the func-
tion, g(n′
1, . . . , n′
m′), where each n′
j is a linear function of ni .
• Multisums of q –holonomic functions are q –holonomic. In other words, if
f (n1, . . . , nm) is q –holonomic, the so are the functions g and h, deﬁned
by
g(a, b, n2, . . . , nm) :=
b∑
n1=a
f (n1, n2, . . . , nm)
h(a, n2, . . . , nm) :=
∞∑
n1=a
f (n1, n2, . . . , nm)
(assuming that the latter sum is ﬁnite for each a).
For a user-friendly explanation of these facts and for many e xamples, see [35, 33]
and [28].
2.3 Examples of q–holonomic functions
Here are a few examples of q –holonomic functions. In fact, we will encounter
only sums, products, extensions, specializations, diagon als, and multisums of
these functions. In what follows we usually extend the groun d ring Z[q±1] to
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q –holonomic 1261
the fractional ﬁeld Q(q1/D), where D is a positive integer. We also use v to
denote a root of q , v2 = q .
For n, k ∈ Z, let
{n} := vn − v−n, [n] := {n}
{1} , [n]! :=
n∏
i=1
[i], {n}! :=
n∏
i=1
{i}
{n}k :=
{ ∏ k
i=1{n − i + 1}, if k ≥ 0
0 if k < 0
[ n
k
]
:=
{ {n}k
{k}k
if k ≥ 0
0 if k < 0
.
The ﬁrst four functions are q –holonomic in n, and the last two, as well as the
delta function δn,k , are q –holonomic in both n and k .
2.4 q–hypergeometric functions
Deﬁnition 2.2 A discrete function f : Zr − →Q(q) is q –hypergeometric iﬀ
Eif /f ∈ Q(q, qn1, . . . , qnr ) for all i = 1, . . . , r.
In that case, we know generators for the annihilation ideal o f f . Namely, let
Eif /f = ( Ri/Si)|Qi=qni for Ri, Si ∈ Z[q, Q1, . . . , Qr]. Then, the annihilation
ideal of f is generated by SiEi − Ri .
All the functions in the previous subsections are q –hypergeometric.
Unfortunately, q –hypergeometric functions are not always q –holonomic. For
example, ( n, k) − → 1/[n2 + k2]! is q –hypergeometric but not q –holonomic.
However, q –proper-hypergeometric functions are q –holonomic. The latter were
deﬁned by Wilf–Zeilberger as follows, [33, Sec.3.1]:
Deﬁnition 2.3 A proper q –hypergeometric discrete function is one of the form
F (n, k) =
∏
s(As; q)asn+bs.k+cs
∏
t(Bt; q)utn+vt.k+wt
qA(n,k)ξk (1)
where As, Bt ∈ K = Q(q), as, ut are integers, bs, ks are vectors of r integers,
A(n, k) is a quadratic form, cs, ws are variables and ξ is an r vector of elements
in K. Here, as usual
(A; q)n :=
n−1∏
i=0
(1 − Aqi).
Geometry & Topology, Volume 9 (2005)
1262 Stavros Garoufalidis and Thang T Q Lˆ e
