---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum"
section_id: sec-005-3-the-quantum-dilogarithm
section_title: "The quantum dilogarithm"
section_number: 3
pages: 16-19
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual ˆA as a von Neumann algebra."
---
We recall the deﬁnition of the quantum dilogarithm given in [14] (see als o [2]), an
important special function that will be used throughout the paper .
3.1 Deﬁnition and properties
Throughout this section, we let q =eπib2
whereb2∈ R\ Q and 0 <b 2< 1, so that
|q| = 1. We also denote Q =b +b−1.
Let ω := (w1,w 2)∈ C2.
Deﬁnition 3.1. The Double Zeta function is deﬁned as
ζ2(s,z|ω) :=
∑
m1,m2∈Z≥0
(z +m1w1 +m2w2)−s. (3.1)
16
The Double Gamma function is deﬁned as
Γ 2(z|ω) := exp
( ∂
∂sζ2(s,z|ω)|s=0
)
. (3.2)
Let
Γ b(x) := Γ 2(x|b,b −1). (3.3)
The Quantum Dilogarithm is deﬁned as the function:
Sb(x) := Γ b(x)
Γ b(Q−x). (3.4)
The following form is often useful, and will be used througho ut this paper:
Gb(x) := e
πi
2 x(x−Q)Sb(x). (3.5)
Let us also relate Gb to another well-known expression by Ruijsenaars [36]
Lemma 3.2.
Gb(z) = G(b,b −1;iz− iQ
2 )e
πi
2 z(z−Q), (3.6)
where
G(a+,a −;z) := exp
(
i
∫ ∞
0
dy
y
( sin 2yz
2 sinh(a+y) sinh(a−y)− z
a+a−y
))
(3.7)
with|Im(z)| < (a+ +a−)/2 and extends meromorphically to the whole complex
plane.
The quantum dilogarithm satisﬁes the following properties:
Proposition 3.3. Self-Duality:
Sb(x) = Sb−1(x), G b(x) = Gb−1 (x); (3.8)
Functional equations:
Sb(x +b±1) = 2 sin(πb±1x)Sb(x), G b(x +b±1) = (1−e2πib±1x)Gb(x); (3.9)
Reﬂection property:
Sb(x)Sb(Q−x) = 1, G b(x)Gb(Q−x) = eπix(x−Q); (3.10)
Complex Conjugation:
Sb(x) = 1
Sb(Q−x), Gb(x) = 1
Gb(Q− ¯x), (3.11)
17
in particular
⏐
⏐
⏐
⏐Sb(Q
2 +ix)
⏐
⏐
⏐
⏐ =
⏐
⏐
⏐
⏐Gb(Q
2 +ix)
⏐
⏐
⏐
⏐ = 1 for x∈ R; (3.12)
Analyticity:
Sb(x) and Gb(x) are meromorphic functions with poles at x =−nb−mb−1 and
zeros at x =Q +nb +mb−1, for n,m∈ Z≥0;
Asymptotic Properties:
Gb(x)∼
{ ¯ζb Im(x)−→ +∞
ζbeπix(x−Q) Im(x)−→−∞ , (3.13)
where
ζb =e
πi
4 + πi
12 (b2+b−2); (3.14)
Residues:
lim
x− →0
xGb(x) = 1
2π, (3.15)
or more generally,
Res 1
Gb(Q +z) =− 1
2π
n∏
k=1
(1−q2k)−1
m∏
l=1
(1−~q2l)−1 (3.16)
at z =nb +mb−1,n,m ∈ Z≥0 and ~q =eπib−2
.
From the asymptotic properties, we have the following useful coro llary that is
needed when we deal with interchanging of order of integrations:
Corollary 3.4. For s,t ∈ C,x ∈ R, the asymptotic behavior of the ratio is given
by
⏐
⏐
⏐
⏐
Gb(s +ix)
Gb(t +ix)
⏐
⏐
⏐
⏐∼
{ 1 x−→ +∞
e2πxRe(t−s) x−→−∞ . (3.17)
By analytic continuation in b, there exists a classical limit for Gb(x) given in
[14]:
Theorem 3.5. Forq =eπib2
, by letting b2−→i0+ we have
lim
b− →0
Gb(bx)
√−i|b|(1−q2)x−1 = Γ(x), (3.18)
where√−i =e− πi
4 and− π
2 < arg(1−q2)< π
2 . The limit converges uniformly for
any compact set in C.
18
We will also need another important variant of the quantum dilogarith m func-
tion:
gb(x) :=
¯ζb
Gb( Q
2 + 1
2πib logx)
, (3.19)
where|gb(x)| = 1 when x∈ R>0 due to (3.12).
Lemma 3.6. Letu,v be self-adjoint operators with uv =q2vu, q =eπib2
. Then
gb(u)gb(v) = gb(u +v), (3.20)
gb(v)gb(u) = gb(u)gb(q−1uv)gb(v). (3.21)
(3.20) and (3.21) are often referred to as the quantum exponent ial and the
quantum pentagon relations, which follows from the other propert ies:
gb(u)∗vgb(u) = q−1uv +v, (3.22)
gb(v)ugb(v)∗ =u +q−1uv. (3.23)
