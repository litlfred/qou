---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL (2)"
section_id: sec-012-computation-of-hhna-n-3
section_title: "Computation of HHn(A), n 3"
section_number: null
pages: 11-15
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
toc_source: outline
doc_brief: "Twisted homology of quantum SL (2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra of the quan- tum SL(2) group"
---
n(A), n ≤3
All automorphisms arising from ﬁnite-dimensional calculi are of the form
σ = σλ,µ, and from now on we will only consider automorphisms of this
type.
In fact, they are of the form σ(x) = σ−1
mod(f ∗x), where f is a
functional in the dual Hopf algebra A◦acting on x by f∗x = P f(x(2))x(1)
(see Theorems 4.1, 4.3 and 4.8 in [12]). It is clear that such automorphisms
do not exchange b and c. By Corollary 3.2 we have HHσ
n(A) ∼= Hn(A, σA),
and the homologies H∗(A, σA) can be calculated via our noncommutative
Koszul resolution.
So let λ, µ ∈k× and σ = σλ,µ. We apply σA′ ⊗A · to our resolution
and obtain the complex (F∗, f) of vector spaces
0 →A →f3 A3 →f2 A3 →f1 A →0,
(34)
with morphisms fn given by
f1


x1
y1
z1

= x1 ◭a −x1 + y1 ◭b + z1 ◭c,
f2


x2
y2
z2

=


x2 ◭b + y2 ◭c
x2 −q−1x2 ◭a + z2 ◭c
y2 −q−1y2 ◭a −z2 ◭b

,
f3(x3) =


x3 ◭c
−x3 ◭b
q−2x3 ◭a −x3

.
(35)
11
Writing εi,j,k := qi+j+k+2λµ−1 we have
λqj+kei,j,k ◭a
=
ei,j,k + q−1−i−|i|(1 −ε|i|,j,k)ei,j+1,k+1,
λ−1ei,j,k ◭b
=
(1 −ε−1
i,j,k)ei+1,j+1,k
+
 0
: i ≥0
q−2i−1(1 −ε−1
−i,j,k)ei+1,j+2,k+1
: i < 0
,
λei,j,k ◭c
=
(1 −ε−i,j,k)ei−1,j,k+1
+

q−2i+1(1 −εi,j,k)ei−1,j+1,k+2
: i > 0
0
: i ≤0 (36)
For q = λ = µ = 1 we have fn = 0 and we recover the Hochschild-
Kostant-Rosenberg theorem for SL(2, k).
The cotangent bundle of an
algebraic group is trivial, so in the classical case HHn(A) = A ⊗Λnk3.
It is clear, however, that for q̸ = 1 there is no twisting automorphism for
which this happens.
The calculations lead to ﬁve distinct cases:
1. µ = 1, λ /∈{q−(N+2)}N≥0, and µ̸ = 1, λ = 1.
2. µ = 1, λ = q−(N+2), N ≥0.
3. µ = qM+1, λ = q−(N+1), M, N ≥0.
4. µ = q−(M+1), λ = q−(N+1), M, N ≥0.
5. µ = q±(M+1), M ≥0, λ /∈q−N, and µ /∈qZ, λ̸ = 1.
The computation of HHσ
0 (A) and HHσ
1 (A) is done most easily “by
hand” using the original Hochschild complex, but for HHσ
2 (A) and HHσ
3 (A)
the calculations are done via the Koszul resolution.
4.3
HHσ
0 (A)
We calculate from ﬁrst principles the twisted Hochschild homology HHσ
0 (A)
for all automorphism σ = σλ,µ. We start with the observation that:
b(a1, a2a3) = b(a1a2, a3) + b(σ(a3)a1, a2)
∀a1, a2, a3 ∈A
So for any a1, a2 ∈A, there exist xa, xb, xc, xc ∈A such that
b(a1, a2) = b[(xa, a) + (xb, b) + (xc, c) + (xd, d)]
Hence the image of the twisted Hochschild boundary is spanned by
Ai,j,k
:=
ei,j,ka −λaei,j,k
=
(q−(j+k) −λ)ei+1,j,k
+
 0
: i ≥0
(q−(j+k+1) −λq−2i−1)ei+1,j+1,k+1
: i < 0
Bi,j,k
:=
ei,j,kb −µbei,j,k = (1 −µq−i)ei,j+1,k,
Ci,j,k
:=
ei,j,kc −µ−1cei,j,k = (1 −µ−1q−i)ei,j,k+1,
Di,j,k
:=
ei,j,kd −λ−1dei,j,k
=
(qj+k −λ−1)ei−1,j,k
+
 0
: i ≤0
(qj+k+1 −λ−1q−2i+1)ei−1,j+1,k+1
: i > 0
.
12
For given (i, j, k), the elements Bi,j,k and Ci,j,k both vanish if and only if
i = 0 and µ = 1. Therefore, for all λ, µ, im b contains the basis elements
ei,j,k,
i̸ = 0, j, k > 0.
(37)
Omitting the span of these terms from the above list of generators we see
that im b is spanned by (37) together with
A−1,j,k = (q−(j+k) −λ)e0,j,k + (q−(j+k+1) −λq)e0,j+1,k+1
˜Ai,j,k = (q−(j+k) −λ)ei+1,j,k,
i̸ = −1
Bi,j,0 = (1 −µq−i)ei,j+1,0,
B0,j,k = (1 −µ)e0,j+1,k,
Ci,0,k = (1 −µ−1q−i)ei,0,k+1,
C0,j,k = (1 −µ−1)e0,j,k+1,
D1,j,k = (qj+k −λ−1)e0,j,k + (qj+k+1 −λ−1q−1)e0,j+1,k+1
˜Di,j,k = (qj+k −λ−1)ei−1,j,k,
i̸ = 1.
Since ˜Di+2,j,k is proportional to ˜Ai,j,k and both vanish if and only if
λ = q−(j+k), we can omit ˜Di,j,k from this list. We also have
A−1,j,k = −λq−(j+k)D1,j,k,
so the D1,j,k can be omitted as well. Finally, C0,j,k is for j > 0 a nonzero
multiple of B0,j−1,k+1 and can be omitted. Thus the degree 0 part (with
respect to the Z-grading) of im b is spanned by
(1 −λqj+k)e0,j,k + (q−1 −λqj+k+1)e0,j+1,k+1,
(1 −µ)e0,r,s,
r + s > 0
and the nonzero degrees by (37) together with
(1 −λqj+k)ei,j,k,
(1 −µq−i)ei,j+1,0,
(1 −µ−1q−i)ei,0,k+1.
where i̸ = 0, and j, k ≥0. Dually,
HH0
σ(A) = { linear h : A →k : h(a1a2) = h(σ(a2)a1) }
For λ /∈q−N we have h(ei,j,k) = 0 for i̸ = 0, and
h(bjck) =





(−q)−k f(j−k)
f(j+k)h(bj−k) :
j ≥k
(−q)−j f(k−j)
f(j+k)h(ck−j) :
j ≤k
(38)
where f(n) = λ −q−n.
We now present the generating twisted 0-cycles, together with dual
twisted 0-cocycles. Our calculations now break down into ﬁve cases:
Case 1: µ = 1, λ /∈{q−(N+2)}N≥0 and µ̸ = 1, λ = 1. Then
HHσ
0 (A) = k[1] ⊕
M
x∈{a,b,c,d}, σ(x)=x
(
⊕
X
r≥0
k[xr+1] )
(39)
For µ = 1 = λ (i.e. σ = id) this agrees with [15]. The dual σ-twisted 0-
cocycles are deﬁned on basis elements x = ei,j,k with σ(x) = x as follows:
h[1](x) =



1
: x = 1
(−q)s+1
f(0)
f(2j+2)
: x = (bc)j+1
0
: otherwise
(40)
13
(if λ = 1, obviously f(0) = 0). For y = [ar+1], [dr+1] deﬁne
h[y](x) =
 1
: x = y
0
: otherwise
(41)
For y = [bs+1], [ct+1] deﬁne
h[bs+1](x) =
(
(−q)k
f(s+1)
f(s+1+2k)
: x = bs+1(bc)k
0
: otherwise
(42)
h[ct+1](x) =
(
(−q)j
f(t+1)
f(t+1+2j)
: x = (bc)jct+1
0
: otherwise
(43)
These all satisfy (38). For any [x], [y] in (39), we have h[y](x) = δ[x],[y],
so the 0-cycles given in (39) are linearly independent, hence a basis.
Case 2: µ = 1, λ = q−(N+2), N ≥0. We have
HHσ
0 (A) = (
⊕
X
s∈S
k[bs]) ⊕(
⊕
X
t∈S
k[ct]) ⊕(
⊕
X
0≤i≤N+2
k[bicN+2−i])
(44)
where S = {integers ≥N + 3} ∪{N + 1, N −1, N −3, . . . ≥0}, with the
convention that if 0 ∈S, we include only one copy of k[1]. Dual 0-cocycles
are h[y], deﬁned for [y] = [bicN+2−i] on the basis ei,j,k by
h[y](x) =
 1
: x = y
0
: otherwise
(45)
and for [y] = [bs], [ct], s, t ∈S by
h[bs](x) =
(
(−q)k
f(s)
f(s+2k)
: x = bs(bc)k
0
: otherwise
h[ct](x) =
(
(−q)j
f(t)
f(t+2j)
: x = (bc)jct
0
: otherwise
(46)
So for each pair [x], [y] appearing in (44), we have h[y](x) = δ[x],[y].
Case 3: µ = qM+1, λ = q−(N+1), M, N ≥0.
HHσ
0 (A) ∼= k2 = k[dM+1cN+1] ⊕k[aM+1bN+1]
(47)
Also HH0
σ(A) ∼= k2, with basis the twisted 0-cocycles h[y], [y] = [dM+1cN+1],
[aM+1bN+1], deﬁned on elements x = ei,j,k, with σ(x) = x by
h[y](x) =
 1
: x = y
0
: otherwise
(48)
Case 4: µ = q−(M+1), λ = q−(N+1), M, N ≥0. We have
HHσ
0 (A) ∼= k2 = k[dM+1bN+1] ⊕k[aM+1cN+1]
(49)
with HH0
σ(A) ∼= k2 with basis h[y], [y] = [dM+1bN+1], [aM+1cN+1], de-
ﬁned as in (48).
Case 5: µ = q±(M+1), M ≥0, λ /∈q−N, and µ /∈qZ, λ̸ = 1. Then
HHσ
0 (A) = 0 = HH0
σ(A)
14
