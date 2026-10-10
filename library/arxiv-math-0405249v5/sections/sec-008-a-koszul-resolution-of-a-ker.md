---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL(2)"
section_id: sec-008-a-koszul-resolution-of-a-ker
section_title: "a koszul resolution of A/ ker"
section_number: null
pages: 10-20
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
doc_brief: "Twisted homology of quantum SL(2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra o f the quan- tum SL(2) group"
---
Using the above facts it is easy to see that ker ε is generated as both a
left and right A-module by x1, 1 :=a− 1, x1, 2 :=b, x1, 3 :=c. For these
elements there exists a Koszul complex ( K∗,k ),Kn :=Kn(xi,j ,A), in the
sense of section 2.4 with the xi,j given by


a− 1 b c
q−1a− 1 b c
q−2a− 1 b c

. (30)
We check by explicit calculation that this Koszul complex is acyclic:
proposition 4.1 The leftA-moduleA/kerε possesses a resolution (K∗,k )
of the form
0→A→ k3A3→k2A3→k1A→A /kerε→ 0.
The augmentation map K0 =A→ k =A/kerε is given by the counit ε.
The left A-module morphisms kn :Kn→Kn−1, n = 1, 2, 3, are given by
k1 :


1
0
0

,


0
1
0

,


0
0
1

↦→a− 1,b,c
k2 :


1
0
0

,


0
1
0

,


0
0
1

↦→


b
1−q−1a
0

,


c
0
1−q−1a

,


0
c
−b

,
k3 : 1↦→


c
−b
q−2a− 1

.
Proof. It follows from Proposition 2.4 (or directly) that this is a c omplex.
Let (x,y,z )t∈ ker(k1), i.e. x(a− 1) +yb +zc = 0. Then πbc(x(a− 1)) = 0.
Using the Z-grading we have πbc(x) = 0, so x = x′b +x′′c. Subtracting
k2(x′,x ′′, 0)t from (x,y,z )t we get a new element of ker( k1) with x = 0.
Hence πc(y) = πb(z) = 0, so y = y′c, z =z′b, z′ =−y′ and this element
is a multiple of k2(0, 0, 1)t. In a similar manner
x


b
1−q−1a
0

 +y


c
0
1−q−1a

 +z


0
c
−b

 = 0
implies x =x′c, y =−x′b, x′(q−2a− 1) = z for some x′∈A . ✷
corollary 4.2 If n> 3, then HHσ
n (A) = 0 for all automorphisms σ.
The morphism between the resulting short complex σA′⊗AK∗ and the
standard complex for Tor A
n (σA′,k ) yielding an isomorphism in homology
is given explicitly by:
1. The map ϕ0 :A→ C0 =A is the identity.
10
2. The map ϕ1 :A3→C1 =A⊗2 is given by


x
y
z

↦→(x,a− 1) + (y,b ) + (z,c ). (31)
Since d(x, 1, 1) = ( x, 1) for any x, we have [( x,a− 1)] = [( x,a )] in
TorA
1 (σA′,k ).
3. The map ϕ2 :A3→C2 =A⊗3 is given by


x
y
z

↦→(x,b,a − 1)− (x,q −1a− 1,b )+
+ (y,c,a − 1)− (y,q −1a− 1,c ) + (z,c,b )− (z,b,c ) (32)
4. Finally, the map ϕ3 :A→ C3 =A⊗4 in the complex for the Tor-
groups is given by x↦→x⊗v, where
v =−(q−2a− 1,b,c ) + (q−2a− 1,c,b )− (c,q −1a− 1,b )+
+ (c,b,a − 1)− (b,c,a − 1) + (b,q −1a− 1,c ). (33)
One sees by direct computation that this is a morphism of comp lexes,
and by the comparison theorem (see [23], Theorem 2.2.6) this is a quasi-
isomorphism.
4.2 Computation of HH σ
n (A), n ≤ 3
All automorphisms arising from ﬁnite-dimensional calculi are of the form
σ = σλ,µ , and from now on we will only consider automorphisms of this
type. In fact, they are of the form σ(x) = σ−1
mod(f∗x), where f is a
functional in the dual Hopf algebraA◦ acting onx byf∗x = ∑ f (x(2))x(1)
(see Theorems 4.1, 4.3 and 4.8 in [12]). It is clear that such a utomorphisms
do not exchangeb andc. By Corollary 3.2 we have HHσ
n (A)∼=Hn(A,σA),
and the homologies H∗(A,σA) can be calculated via our noncommutative
Koszul resolution.
So let λ,µ ∈ k× and σ = σλ,µ . We apply σA′⊗A· to our resolution
and obtain the complex ( F∗,f ) of vector spaces
0→A→ f3A3→f2A3→f1A→ 0, (34)
with morphisms fn given by
f1


x1
y1
z1

 =x1 ◭a−x1 +y1 ◭b +z1 ◭c,
f2


x2
y2
z2

 =


x2 ◭b +y2 ◭c
x2−q−1x2 ◭a +z2 ◭c
y2−q−1y2 ◭a−z2 ◭b

,
f3(x3) =


x3 ◭c
−x3 ◭b
q−2x3 ◭a−x3

. (35)
11
Writingεi,j,k :=qi+j+k+2λµ−1 we have
λqj+kei,j,k ◭a = ei,j,k +q−1−i−|i|(1−ε|i|,j,k )ei,j +1,k +1,
λ−1ei,j,k ◭b = (1 −ε−1
i,j,k )ei+1,j +1,k
+
{ 0 : i≥ 0
q−2i−1(1−ε−1
−i,j,k )ei+1,j +2,k +1 :i< 0 ,
λei,j,k ◭c = (1 −ε−i,j,k )ei−1,j,k +1
+
{
q−2i+1(1−εi,j,k )ei−1,j +1,k +2 :i> 0
0 : i≤ 0 (36)
For q = λ = µ = 1 we have fn = 0 and we recover the Hochschild-
Kostant-Rosenberg theorem for SL(2,k ). The cotangent bundle of an
algebraic group is trivial, so in the classical case HHn(A) = A⊗ Λnk3.
It is clear, however, that for q⁄= 1 there is no twisting automorphism for
which this happens.
The calculations lead to ﬁve distinct cases:
1. µ = 1, λ /∈{q−(N+2)}N≥0, and µ⁄= 1, λ = 1.
2. µ = 1, λ =q−(N+2), N≥ 0.
3. µ =qM +1, λ =q−(N+1), M , N≥ 0.
4. µ =q−(M +1), λ =q−(N+1), M , N≥ 0.
5. µ =q±(M +1), M≥ 0, λ /∈q−N, and µ /∈qZ, λ⁄= 1.
The computation of HHσ
0 (A) and HHσ
1 (A) is done most easily “by
hand” using the original Hochschild complex, but for HHσ
2 (A) andHHσ
3 (A)
the calculations are done via the Koszul resolution.
4.3 HH σ
0 (A)
We calculate from ﬁrst principles the twisted Hochschild ho mologyHHσ
0 (A)
for all automorphism σ =σλ,µ . We start with the observation that:
b(a1,a 2a3) = b(a1a2,a 3) +b(σ(a3)a1,a 2) ∀a1, a2, a3∈A
So for any a1, a2∈A , there exist xa, xb, xc, xc∈A such that
b(a1,a 2) = b[(xa,a ) + (xb,b ) + (xc,c ) + (xd,d )]
Hence the image of the twisted Hochschild boundary is spanne d by
Ai,j,k := ei,j,k a−λaei,j,k
= ( q−(j+k)−λ)ei+1,j,k
+
{ 0 : i≥ 0
(q−(j+k+1)−λq−2i−1)ei+1,j +1,k +1 :i< 0
Bi,j,k := ei,j,k b−µbei,j,k = (1−µq−i)ei,j +1,k,
Ci,j,k := ei,j,k c−µ−1cei,j,k = (1−µ−1q−i)ei,j,k +1,
Di,j,k := ei,j,k d−λ−1dei,j,k
= ( qj+k−λ−1)ei−1,j,k
+
{ 0 :i≤ 0
(qj+k+1−λ−1q−2i+1)ei−1,j +1,k +1 :i> 0 .
12
For given (i,j,k ), the elements Bi,j,k andCi,j,k both vanish if and only if
i = 0 and µ = 1. Therefore, for all λ,µ, imb contains the basis elements
ei,j,k , i ⁄= 0, j,k> 0. (37)
Omitting the span of these terms from the above list of genera tors we see
that imb is spanned by (37) together with
A−1,j,k = (q−(j+k)−λ)e0,j,k + (q−(j+k+1)−λq)e0,j +1,k +1
˜Ai,j,k = (q−(j+k)−λ)ei+1,j,k , i ⁄=−1
Bi,j, 0 = (1−µq−i)ei,j +1, 0, B 0,j,k = (1−µ)e0,j +1,k,
Ci, 0,k = (1−µ−1q−i)ei, 0,k +1, C 0,j,k = (1−µ−1)e0,j,k +1,
D1,j,k = (qj+k−λ−1)e0,j,k + (qj+k+1−λ−1q−1)e0,j +1,k +1
˜Di,j,k = (qj+k−λ−1)ei−1,j,k , i ⁄= 1.
Since ˜Di+2,j,k is proportional to ˜Ai,j,k and both vanish if and only if
λ =q−(j+k), we can omit ˜Di,j,k from this list. We also have
A−1,j,k =−λq−(j+k)D1,j,k ,
so the D1,j,k can be omitted as well. Finally, C0,j,k is for j >0 a nonzero
multiple of B0,j −1,k +1 and can be omitted. Thus the degree 0 part (with
respect to the Z-grading) of im b is spanned by
(1−λqj+k)e0,j,k + (q−1−λqj+k+1)e0,j +1,k +1,
(1−µ)e0,r,s , r +s> 0
and the nonzero degrees by (37) together with
(1−λqj+k)ei,j,k , (1−µq−i)ei,j +1, 0, (1−µ−1q−i)ei, 0,k +1.
where i⁄= 0, and j, k≥ 0. Dually,
HH 0
σ (A) ={ linearh :A→ k : h(a1a2) = h(σ(a2)a1)}
Forλ /∈q−N we have h(ei,j,k ) = 0 for i⁄= 0, and
h(bjck) =



(−q)−kf (j−k)
f (j+k)h(bj−k) : j≥k
(−q)−jf (k−j)
f (j+k)h(ck−j ) : j≤k
(38)
where f (n) = λ−q−n.
We now present the generating twisted 0-cycles, together wi th dual
twisted 0-cocycles. Our calculations now break down into ﬁv e cases:
Case 1: µ = 1, λ /∈{q−(N+2)}N≥0 and µ⁄= 1, λ = 1. Then
HHσ
0 (A) = k[1]⊕
⨁
x∈{a,b,c,d },σ (x)=x
(
⊕∑
r≥0
k[xr+1] ) (39)
Forµ = 1 = λ (i.e. σ = id) this agrees with [15]. The dual σ-twisted 0-
cocycles are deﬁned on basis elements x =ei,j,k withσ(x) = x as follows:
h[1](x) =



1 : x = 1
(−q)s+1 f (0)
f (2j+2) :x = (bc)j+1
0 : otherwise
(40)
13
(if λ = 1, obviously f (0) = 0). For y = [ar+1], [dr+1] deﬁne
h[y](x) =
{ 1 : x =y
0 : otherwise (41)
Fory = [bs+1], [ct+1] deﬁne
h[bs+1](x) =
{
(−q)k f (s+1)
f (s+1+2k) :x =bs+1(bc)k
0 : otherwise (42)
h[ct+1](x) =
{
(−q)j f (t+1)
f (t+1+2j) :x = (bc)jct+1
0 : otherwise (43)
These all satisfy (38). For any [ x], [y] in (39), we have h[y](x) = δ[x], [y],
so the 0-cycles given in (39) are linearly independent, henc e a basis.
Case 2: µ = 1, λ =q−(N+2), N≥ 0. We have
HHσ
0 (A) = (
⊕∑
s∈S
k[bs])⊕ (
⊕∑
t∈S
k[ct])⊕ (
⊕∑
0≤i≤N+2
k[bicN+2−i]) (44)
where S ={integers≥N + 3}∪{ N + 1,N− 1,N− 3,... ≥ 0}, with the
convention that if 0∈S, we include only one copy of k[1]. Dual 0-cocycles
are h[y], deﬁned for [ y] = [bicN+2−i] on the basis ei,j,k by
h[y](x) =
{ 1 : x =y
0 : otherwise (45)
and for [y] = [bs], [ct], s, t∈S by
h[bs](x) =
{
(−q)k f (s)
f (s+2k) :x =bs(bc)k
0 : otherwise
h[ct](x) =
{
(−q)j f (t)
f (t+2j) :x = (bc)jct
0 : otherwise (46)
So for each pair [ x], [y] appearing in (44), we have h[y](x) = δ[x], [y].
Case 3: µ =qM +1, λ =q−(N+1), M , N≥ 0.
HHσ
0 (A)∼=k2 =k[dM +1cN+1]⊕k[aM +1bN+1] (47)
AlsoHH 0
σ (A)∼=k2, with basis the twisted 0-cocycles h[y], [y] = [dM +1cN+1],
[aM +1bN+1], deﬁned on elements x =ei,j,k , with σ(x) = x by
h[y](x) =
{ 1 : x =y
0 : otherwise (48)
Case 4: µ =q−(M +1), λ =q−(N+1), M , N≥ 0. We have
HHσ
0 (A)∼=k2 =k[dM +1bN+1]⊕k[aM +1cN+1] (49)
with HH 0
σ (A)∼= k2 with basis h[y], [y] = [ dM +1bN+1], [aM +1cN+1], de-
ﬁned as in (48).
Case 5: µ =q±(M +1), M≥ 0, λ /∈q−N, and µ /∈qZ, λ⁄= 1. Then
HHσ
0 (A) = 0 = HH 0
σ (A)
14
4.4 Twisted cocycles deﬁned by derivations
Before proceeding with HHσ
1 (A), we present a general construction of
σ-twisted Hochschild n-cocycles. It is essentially a variant of the charac-
teristic map of [4, 10].
LetA be a k-algebra and σ be an automorphism. A σ-derivation ofA
is a k-linear map ∂ :A→A , such that ∂(a0a1) = a0∂(a1) +∂(a0)σ(a1).
The following is straightforward:
proposition 4.3 If h is a σ1-twisted 0-cocycle, ∂1, ..., ∂n−1 derivations
ofA, and ∂n is a σ2-derivation, then
φn(a0,a 1,...,a n) = h(a0∂1(a1)...∂ n(an)) (50)
is a σ1◦σ2-twisted Hochschild n-cocycle
In general there is no reason for such a cocycle to represent a nontrivial
element of Hochschild cohomology, nor for it also to be cycli c. However:
lemma 4.4 SupposeA is a unital algebra, h a σ1-twisted 0-cocycle and ∂
a σ2-derivation of A. Deﬁning φ1 by φ1(x,y ) = h(x∂(y)), then φ1 is a
σ1◦σ2-twisted cyclic cocycle if and only if h(∂(a)) = 0 for all a∈A .
ForA =A(SLq(2)) there are obvious derivations ∂a, ∂b deﬁned by
∂a(a) = a, ∂ a(b) = 0, ∂ a(c) = 0, ∂ a(d) =−d
∂b(a) = 0, ∂ b(b) = b, ∂ b(c) =−c, ∂ b(d) = 0 (51)
and extended via the Leibniz rule. For any x∈A deﬁne an inner deriva-
tion∂′
x by∂′
x(y) = [x,y ] = xy−yx. The following is straightforward:
proposition 4.5 The vector space of all derivations of A(SLq(2)) is spanned
by ∂a, ∂b together with the inner derivations.
In the sequel we will use the derivation ∂0 =∂a +∂b, which satisﬁes
∂0(a) = a, ∂ 0(b) = b, ∂ 0(c) =−c, ∂ 0(d) =−d (52)
and also the σλ, 1-derivation deﬁned by
∂(a) = a, ∂ (b) = 0 = ∂(c), ∂ (d) =−λ−1d. (53)
4.5 HH σ
1 (A)
The second twisted Hochschild boundary is given by
b(a1,a 2,a 3) = (a1a2,a 3)− (a1,a 2a3) + (σ(a3)a1,a 2).
In particular (take a2 = a3 = 1) the image of b contains all elementary
tensors of the form ( a1, 1), and the residue classes of
(ei,j,k ,a ), (ei,j,k ,b ), (ei,j,k ,c ), (ei,j,k ,d )
generateA⊗A/imb. Now, HHσ
1 (A) is the kernel of the mapA⊗A/imb→
A induced by the ﬁrst twisted Hochschild boundary. This sends the classes
of the above elements to Ai,j,k ,Bi,j,k ,Ci,j,k ,Di,j,k from the previous sec-
tion. It is straightforward to check for triviality and line ar dependence.
We now present generators of HHσ
1 (A) and dual twisted 1-cocycles.
From Proposition 4.3, for any σ-twisted 0-cocycle h and derivation ∂,
deﬁning φ1(x,y ) = h(x∂(y)) gives a σ-twisted Hochschild 1-cocycle. For
15
A(SLq(2)) all automorphisms σλ,µ commute with the derivations ∂a, ∂b
(51), and the ei,j,k are eigenvectors for these derivations. By Lemma 4.4,
φ1 is cyclic if and only if h◦∂ = 0. We take ∂0 =∂a +∂b deﬁned by (52).
Case 1: µ = 1, λ /∈{q−(N+2)}N≥0 and µ⁄= 1, λ = 1. Then
HHσ
1 (A) = k[ω1] ⊕
⨁
x∈{a,b,c,d },σ (x)=x
(
⊕∑
r≥0
k[(xr,x )]) (54)
whereω1 = (µ−1−1)(d,a ) + (q−q−1)(b,c ). We note that, for all µ and for
λ⁄=q−2, we have [( c,b )] =−µ[(b,c )], [(d,a )] =−λ[(a,d )]. For µ = 1 = λ
this is in agreement with [15], apart from the sign change in ω1. Now
recall the 0-cocycles h[x] deﬁned in (40)-(43). Given such an x, deﬁne a
Hochschild 1-cocycle φ[x] by
φ[x](y,z ) = h[x](y∂0(z)) (55)
Then the Hochschild 1-cocycles dual to the generators of HHσ
1 (A) are:
φ[xr+1]↔ (xr,x ), x ∈{a,b,c,d }, σ (x) = x.
Dual to ω1 we have
φω 1 (x,y ) = h[1](x∂0(y)) (56)
with h[1] deﬁned in (40) and ∂0 deﬁned in (52). Then for λ = 1 we
have φω 1 (d,a ) = 1, and for λ⁄= q−2 we have φω 1 (b,c ) = q(1−λ )
λq 2−1 . Since
h[1]◦∂0 = 0, by Lemma 4.4 φω 1 is in fact a σ-twisted cyclic 1-cocycle.
Case 2. µ = 1, λ =q−(N+2), N≥ 0. Then
HHσ
1 (A) = (
⊕∑
s∈S′
k[(bs,b )])⊕ (
⊕∑
t∈S′
k[(ct,c )])⊕
(
⊕∑
0≤i≤N
k[(bicN+1−i,b )])⊕ (
⊕∑
0≤i≤N
k[(bi+1cN−i,c )])⊕k[ω1] (57)
HereS′ ={integers≥N}∪{N−2,N−4,... ≥ 0}, and for N≥ 1 we have
[ω1] = [( b,c )] = −[(c,b )] for N odd, [ω1] = 0 for N even. For λ = q−2,
[(b,c )] and [(c,b )] are linearly independent.
Recall the 0-cocycles h[x], with [ x] = [ bs], [ct], deﬁned in (42), (43).
The dual Hochschild 1-cocycles (55) are
φ[bs+1]↔ (bs,b ), φ [ct+1]↔ (ct,c )
together with the twisted cyclic 1-cocycle φω 1 (56) dual to ω1. To deﬁne
twisted 1-cocycles dual to [(bicN+1−i,b )], [(bi+1cN−i,c )] we need to work a
little harder. It is straightforward to show that any σ-twisted Hochschild
1-cocycle is uniquely deﬁned by its values φ(y,t ), for t =a,b,c,d and basis
elementsy =ei,j,k .
lemma 4.6 For λ = q−(N+2), µ = 1 deﬁning φ1, φ2 on basis elements
y =ei,j,k by
φ1(bicN+1−i,b ) = βN,i , φ 1(dbicN−i,a ) = q−(N+1)βN,i,
φ1(y,b ) = 0 = φ1(y,a ) otherwise , φ 1(y,c ) = 0 = φ1(y,d ) ∀y
φ2(abicN−i,d ) = qN+1γN,i , φ 2(bi+1cN−i,c ) = γN,i
φ2(y,d ) = 0 = φ2(y,c ) otherwise , φ 2(y,a ) = 0 = φ1(y,b ) ∀y
16
for arbitraryβN,i ,γN,i , 0≤i≤N , gives well-deﬁned σ-twisted Hochschild
1-cocycles.
Setting each βN,i ,γN,i to 1 in turn, and all others to zero, we see that
the twisted Hochschild 1-cycles [(bicN+1−i,b )], [(bi+1cN−i,c )] are nontriv-
ial and linearly independent. This extends to N + 1 linearly independent
twisted cyclic 1-cocycles. Deﬁne φ =φ1 +φ2. Cyclicity requires
φ(xc,b ) =−φ(b,xc ) =−iφ(xc,b )− (N + 1−i)φ(bx,c )
where x =bicN−i. Hence for φ to be cyclic, we need
(i + 1)βN,i =−(N + 1−i)γN,i 0≤i≤N
i.e. γN,i = −(i+1)
N+1−iβN,i for 0≤i≤N . Then:
lemma 4.7 For each 0≤i≤N , deﬁning φN,i =φ1 +φ2 with
βN,i =N + 1−i, γ N,i =−(i + 1)
gives a well-deﬁned twisted cyclic 1-cocycle satisfying
φN,i (xc,b ) = N + 1−i, φ N,i (bx,c ) =−(i + 1)
φN,i (ax,d ) =−qN+1(i + 1), φ N,i (dx,a ) = q−(N+1)(N + 1−i)
forx =bicN−i, and φN,i (y,t ) = 0 for all basis elements y andt =a,b,c,d
otherwise.
Case 3. µ = qM +1, λ = q−(N+1), M , N≥ 0. Then HHσ
1 (A)∼= k4,
with basis given by the Hochschild cycles
(aMbN+1,a ), (aM +1bN,b ), (dM +1cN,c ), (dMcN+1,d ) (58)
The dual basis for HH 1
σ (A)∼= k4 is given by the 1-cocycles φ[x],t , for
[x] = [aM +1bN+1], [dM +1cN+1], and t =a,b deﬁned by
φ[x],t (y,z ) = h[x](y∂t(z)) (59)
where the h[x] were deﬁned in (48) and ∂a, ∂b in (51). We have
φ[aM +1bN +1],a (aMbN+1,a ) = q−(N+1)
φ[aM +1bN +1],b (aM +1bN,b ) = 1
φ[dM +1cN +1],b (dM +1cN,c ) =−1
φ[dM +1cN +1],a (dMcN+1,d ) =−qN+1
with all other pairings being zero.
Case 4. µ =q−(M +1), λ =q−(N+1), M , N≥ 0. HHσ
1 (A)∼=k4, with
basis given by the Hochschild cycles
(aMcN+1,a ), (dM +1bN,b ), (aM +1cN,c ), (dMbN+1,d ) (60)
Analogously to Case 3, the dual basis for HH 1
σ (A)∼= k4 is given by the
1-cocycles φ[x],t , (59) for [ x] = [aM +1cN+1], [dM +1bN+1], and t =a, b.
Case 5. For µ = q±(M +1), M ≥ 0, λ /∈ q−N, and µ /∈ qZ, λ⁄= 1,
HHσ
1 (A) = 0 and HH 1
σ (A) = 0.
17
4.6 HH σ
2 (A)
We now compute HHσ
2 (A). The ﬁrst step is to describe the kernel of
ψ :A2→A, (x,y )↦→ψ+(x) +ψ−(y)
If kerψc
±⊂A are ﬁxed complements to ker ψ± and
φ± : imψ±→ kerψc
±
are the inverses of ψ±|kerψ c
± , then the linear map
kerψ+⊕ (imψ+∩ imψ−)⊕ kerψ−→ kerψ,
(x,y,z )↦→(x +φ+(y),z−φ−(y))
is an isomorphism of vector spaces. Using (36) one determine s a basis of
imψ+∩ imψ− and obtains:
proposition 4.8 The set
Bkerψ :={(x+, 0), (0,x −)|x±∈B kerψ ±}
∪{(−λ−2( 1−ε−i,j,k
1−ε−1
i−2,j,k
ei−2,j −1,k +1−ε−i,j,k +1ei−2,j,k +2),ei,j,k ),
(e−i,k,j ,−λ2(
1−ε−1
−i,j,k
1−εi−2,j,k
e−i+2,k +1,j −1−ε−1
−i,j,k +1e−i+2,k +2,j ))|
i≥ 2,j≥ 1,k≥ 0,εi−2,j,k ⁄= 1}
∪{(λ−2qei−2, 0,j +2,ei, 0,j ), (e−i,j, 0,λ 2q−1e−i+2,j +2, 0)|i≥ 2,j≥ 0,ε −i, 0,j = 1}
∪{(e−1,j,k ,λ 2ε−1
−1,j,k e1,j +1,k −1)|j≥ 0,k≥ 1}.
is a vector space basis of kerψ.
Now we can compute which of these remain nontrivial and linea rly
independent modulo the image of the map ϕ :x↦→(ψ−(x),−ψ+(x)).
proposition 4.9 The classes of
{(ei,j, 0, 0), (0,e −i, 0,j )|i≥ 0, j≥ 0, εi, 0,j = 1}
∪{ (λ−2qei−2, 0,k +2, ei, 0,k )|i≥ 2, k≥ 0, ε−i, 0,k = 1}
∪{ (ei,j, 0, λ2q−1ei+2,j +2, 0)|i≤− 2, j≥ 0, εi,j, 0 = 1}
∪{ (e−1jk,λ 2e1,j +1,k −1)|j≥ 0, k≥ 1,ε −1,j,k = 1}
form a vector space basis of kerψ/imϕ.
Next we check for which linear combinations ( x,y )⁄= (0, 0) of these
there exists z with (x,y,z )∈ kerf2, and determine those z with (0, 0,z )∈
kerf2, giving a generating set for HHσ
2 (A):
proposition 4.10 The classes of
{ (0, 0,e 0,j,k )|j,k≥ 0, ε0,j,k = 1}
∪{ (ei,j, 0, 0, 0), (0,e −i, 0,j , 0)|i≥ 0, j≥ 0, λ=q−j−1, µ=qi+1}
∪{(λ−2qei−2, 0,k +2,ei, 0,k ,λ −1q−1ei−1, 0,k +1)|i≥ 2,k≥ 0,λ =q−k−1,µ =q−i+1}
∪{(ei,j, 0, λ2q−1ei+2,j +2, 0,λq −1ei+1,j +1, 0)|i≤− 2,j ≥ 0,λ =q−j−1,µ =qi+1}
∪{ (e−1,j,k , λ2e1,j +1,k −1,λq −1e0,j +1,k )|j≥ 0, k≥ 1, λ=q−j−k−1, µ= 1}
generateHHσ
2 (A).
18
The classes of the elements in the ﬁrst line are trivial for µ⁄= 1, and for
µ = 1 they contain those from the last line. It follows directly from the
deﬁnition of f3 that the remaining classes are independent. Hence:
HHσ
2 (A)∼=



kN+1 :λ =q−(N+2),N ≥ 0, µ= 1,
k2 :λ =q−(N+1), µ=q±(M +1),M,N ≥ 0,
0 : otherwise .
(61)
To calculate HCσ
∗ (A) we need generators in the original Hochschild
complex. In Case 2 we compute generators from the above using ϕ2 (32)
and ξ (18). In Cases 3 and 4 we use simpler generators that are direc tly
veriﬁed to be homologous to those obtained from the above one s:
Case 2. µ = 1, λ =q−(N+2),N≥ 0. Then HHσ
2 (A)∼=kN+1. Taking
x =bicN−i (0≤i≤N ), a basis is given by
ω2(N,i ) = (bcx,a,d )− (bcx,d,a )−q(dbx,a,c ) +q(bdx,c,a )
+ (dax,b,c )− (adx,c,b )−q−1(cax,b,d ) +q−1(acx,d,b ) (62)
Case 3. µ = qM +1, λ = q−(N+1), M , N≥ 0. Then HHσ
2 (A)∼= k2,
with basis given by the Hochschild cycles
ω2 = ( aMbN,b,a )−q−1(aMbN,a,b )
ω
′
2 = ( dMcN,c,d )−q(dMcN,d,c ) (63)
Case 4. µ =q−(M +1), λ =q−(N+1), M , N≥ 0. HHσ
2 (A)∼=k2, with
basis given by the Hochschild cycles
ω2 = ( aMcN,c,a )−q−1(aMcN,a,c )
ω
′
2 = ( dMbN,b,d )−q(dMbN,d,b ) (64)
Finally,HHσ
2 (A) = 0 for all other σ =σλ,µ .
4.7 HH σ
3 (A)
The third homology HHσ
3 (A) can be determined easily using the Koszul
resolution. We abbreviate:
ψ+ :A→A , x ↦→x ◭b, ψ − :A→A , x ↦→x ◭c.
From (36) we obtain in a straightforward way:
proposition 4.11 The sets
Bkerψ ± :={ei,j,k | ±i≥ 0, ε±i,j,k = 1}
are vector space bases of kerψ±. Hence the sets
Bimψ ± :={E±
i,j,k |ei,j,k /∈ kerψ±}, E ±
i,j,k :=ψ±(ei,j,k )
are vector space bases of imψ±.
19
If x∈ HHσ
3 (A) = ker f3, then x∈ kerψ+∩ kerψ−, so by Proposi-
tion 4.11, πi,j,k (x)⁄= 0 implies i = 0. Insertion in q−2x ◭a =x gives
x∈
{
span{bicN−i}i=0,...,N :λ =q−N−2,µ = 1,
0 : otherwise .
Conversely, all these monomials are elements of ker f3. Hence:
