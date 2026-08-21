---
doc_id: descendants-colored-jones
doc_title: "The descendant colored Jones polynomials"
section_id: sec-007-proof-of-the-gauge-symmetry-equations
section_title: "Proof of the gauge symmetry equations"
section_number: null
pages: 15-19
source_pdf: descendants_colored_jones.pdf
source_sha256: f00693a5926c074f
doc_brief: "The descendant colored Jones polynomials — We discuss two realizations of the colored Jones polyno- mials of a knot, one appearing in an unnoticed work of the second author in 1994 on quantum"
---
In this section we give the proofs of equations (26)a n d(27)w h i c hw e r es t a t e d
in [Kas96], but proofs were ommitted.
We begin with Equation ( 26). Writing out its left hand side in matrix
coeﬃcients (indexed by i, j ∈{ 0,...,N − 1}), we have
⟨i|h(x, m)h(y,m )|j⟩=
N−1∑
k=0
⟨i|h(x, m)|k⟩⟨k|h(y,m )|j⟩(32)
= ζ(j−i)m
N−1∑
k=0
⟨⟨xζk−i⟩⟩N ⟨⟨yζj−k⟩⟩N
so that Equation ( 26)i se q u i v a l e n tt o
N−1∑
k=0
⟨⟨xζk−i⟩⟩N ⟨⟨yζj−k⟩⟩N = ⟨⟨xyζj−i⟩⟩N ⇔
N−1∑
k=0
⟨⟨xζk⟩⟩N ⟨⟨yζj−k⟩⟩N = ⟨⟨xyζj⟩⟩N .
(33)
2322 Stavros Garoufalidis and Rinat Kashaev
The deﬁnition ( 18)g i v e s⟨⟨x⟩⟩N = N−1 ∑ N−1
a=0 xa. Using this equality, we ob-
tain
N−1∑
k=0
⟨⟨xζk⟩⟩N ⟨⟨yζj−k⟩⟩N(34)
= N−2
N−1∑
k,a,b=0
(xζk)a(yζj−k)b = N−1
N−1∑
a,b=0
xaybζjbδ0,{a−b}N
= N−1
N−1∑
b=0
(xyζj)b = ⟨⟨xyζj⟩⟩N .
We can diagonalize the matrices h(x, m) by conjugating them by the
(discrete) Fourier transformation operator ⟨i|F|j⟩ = ζij. Indeed, assuming
i, j ∈{ 0,...,N − 1},w eh a v e
⟨i|Fh(x, m)F−1|j⟩
(35)
= N−1 ∑
i′,j′
ζii′−jj′
⟨i′|h(x, m)|j′⟩= N−1 ∑
i′,j′
ζii′−jj′+(j′−i′)m⟨⟨xζj′−i′
⟩⟩N
= N−1 ∑
i′,j′
ζii′−j(j′+i′)+j′m⟨⟨xζj′
⟩⟩N = δi,j
∑
j′
ζ(m−j)j′
⟨⟨xζj′
⟩⟩N
= N−1δi,j
∑
j′
ζ(m−j)j′
N−1∑
a=0
xaζaj′
= δi,j
N−1∑
a=0
δ0,{m−j+a}N xa = δi,jx{j−m}N .
Thus, conjugating the r-matrix ( 23)b y F,w ec a np r o v eE q u a t i o n s(27)b y
explicit computation. Indeed, assuming that i, j, k, l ∈{ 0,...,N − 1},w e
have
⟨i, j|(F ⊗ F)r(x; m, n)(F−1 ⊗ F−1)|k, l⟩(36)
= N−2 ∑
i′,j′,k′,l′
ζii′+jj′−kk′−ll′
⟨i′,j ′|r(x; m, n)|k′,l ′⟩
= ⟨⟨x⟩⟩N
N 2
∑
i′,j′,k′,l′
ζii′+jj′−kk′−ll′+(i′−k′+n)(l′−j′)
× w(x/ζ|j′− i′− m)w(x|l′− k′+ n)
w(x/ζ|j′− k′+ n − m)w(x/ζ|l′− i′)
= ⟨⟨x⟩⟩N
N 2
∑
i′,j′,k′,l′
ζi(i′+k′)+j(j′+k′)−kk′−l(l′+k′)+(i′+n)(l′−j′)
The descendant colored Jones polynomials 2323
× w(x/ζ|j′− i′− m)w(x|l′+ n)
w(x/ζ|j′+ n − m)w(x/ζ|l′− i′)
= ⟨⟨x⟩⟩N δ0,{i+j−k−l}N
N
∑
i′,j′,l′
ζii′+jj′−ll′+(i′+n)(l′−j′)
× w(x/ζ|j′− i′− m)w(x|l′+ n)
w(x/ζ|j′+ n − m)w(x/ζ|l′− i′),
where, in third equality, we have shifted the summation variables i′,j ′,l ′ by
k′ and, in the last equality, performed the k′-summation by using the formula
(37)
N−1∑
a=0
ζab = Nδ 0,{b}N .
We continue the calculation in (36) by shifting the summation variables l′ ↦→
l′+ i′ and j′ ↦→ j′+ m − n followed by the shift i′ ↦→ i′− n:
(36)= ⟨⟨x⟩⟩N δ0,{i+j−k−l}N
N
∑
i′,j′,l′
ζi(i′−n)+j(j′+m−n)−l(l′+i′−n)+i′(l′+i′−j′−m)
(38)
× w(x/ζ|j′− i′)w(x|l′+ i′)
w(x/ζ|j′)w(x/ζ|l′)
= ⟨⟨x⟩⟩N δ0,{i+j−k−l}N
Nζ kn−jm
∑
i′,j′,l′
ζ(i−l−m+i′)i′+(j−i′)j′+(i′−l)l′
× w(x/ζ|j′− i′)w(x|l′+ i′)
w(x/ζ|j′)w(x/ζ|l′)
= ⟨⟨x⟩⟩N δ0,{i+j−k−l}N
Nζ kn−jm
N−1∑
i′=0
w(x/ζ|− i′)w(x|i′)
ζ(l+m−i−i′)i′
×
∑
j′,l′
ζ(j−i′)j′+(i′−l)l′ w(xζ−i′−1|j′)w(xζi′
|l′)
w(x/ζ|j′)w(x/ζ|l′)
= ⟨⟨x⟩⟩N δ0,{i+j−k−l}N
Nζ kn−jm
×
N−1∑
i′=0
w(x/ζ|− i′)w(x|i′)
ζ(l+m−i−i′)i′ f(xζ−i′−1,x / ζ|ζj−i′
)f(xζi′
,x / ζ|ζi′−l)
where, in third equality, we used the addition formula ( 20), and in the last
2324 Stavros Garoufalidis and Rinat Kashaev
equality, we use function f(x, y|z) deﬁned by
(39) f(x, y|z): =
∑
a
w(x|a)
w(y|a)za, (1 − yN )zN =1 − xN ,
whose automorphic properties are described in [ KMS93]. In particular, we
have the equality
(40) f(xζa,x / ζ|ζ−b)= x{b}N
⟨⟨x⟩⟩N w(x|{a}N )
(ζ){a}N +{b}N
(ζ){a}N (ζ){b}N
(a, b ∈ Z)
which we can use to proceed in ( 38) as follows:
(38)= ⟨⟨x⟩⟩N δ0,{i+j−k−l}N
ζkn−jm
N−1∑
i′=j
w(x|i′)xi′−j
ζ(l+m−i−i′)i′
(ζ)N−1−j
(ζ)N−1−i′(ζ)i′−j
f(xζi′
,x / ζ|ζi′−l)
= ⟨⟨x⟩⟩N δ0,{i+j−k−l}N
ζkn−jm
N−1∑
i′=j
w(x|i′)xi′−j
ζ(l+m−i−i′)i′
(¯ζ)i′
(¯ζ)j(ζ)i′−j
f(xζi′
,x / ζ|ζi′−l)
(41)
where, in ﬁrst equality, we used the addition formula ( 20) for simpliﬁcation,
and in the last equality, the property
(42) ( ζ)k(¯ζ)N−1−k = N (k ∈ Z, 0 ≤ k ≤ N − 1).
Continuing with the second f-function in (41), we have
= δ0,{i+j−k−l}N
ζkn−jm
l∑
i′=j
xl−j
ζ(l+m−i−i′)i′
(¯ζ)i′
(¯ζ)j(ζ)i′−j
(ζ)l
(ζ)i′(ζ)l−i′
= δ0,{i+j−k−l}N (ζ)lxl
ζ(n−j)k(ζ)jxj
l−j∑
i′=0
(−1)i′
ζ(i′−1)i′/2
ζ(l+m−i−j)i′
(ζ)i′(ζ)l−j−i′
= δ0,{i+j−k−l}N (ζ)lxl(ζk−m; ζ)l−j
ζ(n−j)k(ζ)jxj(ζ)l−j
= δ0,{i+j−k−l}N (ζ)lxl(ζ){k−m−1}N +l−j
ζ(n−j)k(ζ)jxj(ζ)l−j(ζ){k−m−1}N
= δ{i−m−1}N +j,{k−m−1}N +l ζ(j−n)kxl−j (ζ)l(ζ){i−m−1}N
(ζ)j(ζ)l−j(ζ){k−m−1}N
(43)
The descendant colored Jones polynomials 2325
where, in third equality, we used the well-known q-binomial formula
(44) ( z; q)s =
s∑
t=0
(−z)tq(t−1)t/2 (q)s
(q)t(q)s−t
, (s ∈ N),
with q = ζ, s = l − j and z = ζk−m; in fourth equality, the identity
(45) ( ζa; ζ)b = (ζ){a−1}N +b
(ζ){a−1}N
(a ∈ Z,b ∈ N),
and, in the last equality, the equivalence
{
i + j ≡ k + l (mod N)
0≤{k−m−1}N + l − j ≤N − 1 ⇔{ i−m−1}N + j = {k − m − 1}N + l.
(46)
Equation (43), combined with (35), straightforwardly implies relations (27).
We remark that the R-matrix coeﬃcients in ( 43), when specialized to
m = n = −1, coincide with the standard colored Jones R-matrix coeﬃcients.
This means that in this case, the associated knot invariant is the N-colored
Jones polynomial specialized to a primitive N-th root of unity.
