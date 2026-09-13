---
doc_id: arxiv-1108.1048v3
doc_title: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS"
section_id: sec-006-3-explicit-construction-of-irreducible-modules-f
section_title: "Explicit Construction of Irreducible Modules for Finite Classical Type"
section_number: 3
pages: 17-44
source_pdf: 1108.1048v3.pdf
source_sha256: 6f2b83450ba923d0
doc_brief: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS — We give an explicit construction of irreducible modules ove r Khovanov-Lauda- Rouquier algebras R and their"
---
In Sections 3 and 4, we assume that A is of ﬁnite classical type. We maintain the notation
from Sections 1 and 2. Our aim in this section is to present an e xplicit construction of
irreducible R-modules (resp. Rλ-modules) for ﬁnite classical type using a single induction
step. Let B be the crystal of the irreducible highest weight Uq(g)-module V (Λ n) if A is of
type An and of V (Λ 1) if A is of type Bn, Cn, Dn. We deﬁne the 1 or 2-dimensional irreducible
18 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
R-module ∆ (a,b) for a, b ∈ B with a ≻ b by using the structure of B. Combining Proposition
1.10 with some facts about the modules ∆ (a,b) and the descriptions of the adapted strings,
we deﬁne the outer tensor product ∆( a(v)) := ∆( a(v); 1) ⊠ · · · ⊠ ∆( a(v); n) of ∆ (a,b)’s for
v ∈ B(∞) (resp. v ∈ B(λ)). For v ∈ B(λ), the number η(v) of ∆ (a,b)’s in ∆( a(v)) has an
upper bound; i.e., η(v) ≤ nλ(h), where h is as in Lemma 3.4 below. Then, we construct a map
Ψ : B(∞) → B(∞) (resp. Ψ λ : B(λ) → B(λ)) by taking the head of Ind∆( a(v)) (Theorem
3.2). The proof that this map is indeed a crystal isomorphism , hence is compatible with the
Kashiwara operators, will be provided in the next section.
We ﬁrst give a detailed description of S and S λ for ﬁnite classical type with respect to
the expression of w0 = rs1 · · ·rsn in Table 1. Let △An be the triangle consisting of right
justiﬁed rows of boxes with 1 box in the ﬁrst (bottom) row, 2 bo xes in the second row, . . .,
and n boxes in the top row. Let △Bn (resp. △Dn) be the triangle consisting of centered
rows of boxes having 1 box (resp. 2 boxes) in the ﬁrst row, 3 box es (resp. 4 boxes) in the
second row, . . . , and (2 n − 1) boxes (resp. (2 n − 2) boxes) in the top row. Set △Cn = △Bn.
When it is not necessary to specify the type, we omit the subsc ript and simply write △. For
a ∈ S , let △(a) denote the ﬁlling of the triangle △ with entries of a from left to right in
each row, and from bottom to top. Let tij be the jth entry of the ith row in △(a) and let
△(a) = {tij}1≤i≤n′, p i≤j≤p′
i
, where
n′ =



n (An, Bn, Cn)
n − 1 ( Dn)
pi =



n + 1 − i (An, Bn, Cn),
n − i (Dn)
p′
i =



n (An),
n − 1 + i (Bn, Cn, Dn).
Set tij = 0 except when 1 ≤ i ≤ n′, p i ≤ j ≤ p′
i. For example, if a = (2, 3, 1, 0, 9, 8, 4, 2, 1) ∈ S
for type B3 and a′ = (5 , 2, 7, 4, 3, 1, 9, 6, 4, 5, 3, 2) ∈ S for type D4, then t1,3 = 2 in △(a),
t3,4 = 5 in △(a′) and
△(a) =
9 8 4 2 1
3 1 0
2
, △(a′) =
9 6 4 5 3 2
7 4 3 1
5 2
.
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 19
Let ˜c(ti,n−1) = ∑ n−1
k=i tk,n−1, ˜c(ti,n) = ∑ n−1
k=i tk,n, and
c(ti,j) =



∑ n
k=i tk,j if j ≤ n (An), j = n (Bn),∑ n
k=i(tk,j + tk,2n−j) if j < n (Bn, Cn),∑ n−1
k=i (tk,j + tk,2n−1−j) if j < n − 1 ( Dn),∑ n
k=i 2tk,j if j = n (Cn),∑ n−1
k=i (tk,n−1 + tk,n) if j = n − 1, n (Dn),
ti,j + ∑ n
k=i+1(tk,2n−j + tk,j ) if j > n (Bn, Cn),
ti,j + ∑ n−1
k=i+1(tk,2n−1−j + tk,j ) if j > n (Dn).
(3.1)
Proposition 3.1 ([24]). Let (A, P, Π , P∨, Π ∨) be a Cartan datum of ﬁnite classical type, and
let λ = λ1Λ 1 + · · · + λnΛ n ∈ P+. For a ∈ (Z≥0)ℓ, let △(a) = {tij}1≤i≤n′, p i≤j≤p′
i
be as above
and assume c(ti,j) is as in (3.1). Then
(An) : S = {a ∈ (Z≥0)ℓ | ti,n+1−i ≥ ti,n+2−i ≥ · · · ≥ ti,n for 1 ≤ i ≤ n},
S λ = {a ∈ S | ti,j ≤ λj + c(ti+1,j−1) − 2c(ti+1,j) + c(ti,j+1)
for 1 ≤ i ≤ n, n + 1 − i ≤ j ≤ n}
(Bn) : S = {a ∈ (Z≥0)ℓ | 2ti,n+1−i ≥ . . . ≥ 2ti,n−1 ≥ ti,n ≥ 2ti,n+1 ≥ . . . ≥ 2ti,n−1+i
for 1 ≤ i ≤ n},
S λ = {a ∈ S | ti,j ≤ λj + c(ti,j+1) − 2c(ti,2n−j) + c(ti,2n+1−j),
ti,2n−j ≤ λj + c(ti+1,j+1) − 2c(ti+1,j ) + c(ti,2n+1−j),
ti,n ≤ λn + 2c(ti,n+1) − 2c(ti+1,n) for 1 ≤ i ≤ n, n + 1 − i ≤ j < n }
(Cn) : S = {a ∈ (Z≥0)ℓ | ti,n+1−i ≥ . . . ≥ ti,n ≥ . . . ≥ ti,n−1+i for 1 ≤ i ≤ n}
S λ = {a ∈ S | ti,j ≤ λj + c(ti,j+1) − 2c(ti,2n−j) + c(ti,2n+1−j),
ti,2n−j ≤ λj + c(ti+1,j+1) − 2c(ti+1,j ) + c(ti,2n+1−j),
ti,n ≤ λn + c(ti,n+1) − c(ti+1,n) for 1 ≤ i ≤ n, n + 1 − i ≤ j < n }
(Dn) : S = {a ∈ (Z≥0)ℓ | ti,n−i ≥ . . . ≥ ti,n−2 ≥ ti,n−1, ti,n ≥ ti,n+1 ≥ . . . ≥ ti,n−1+i
for 1 ≤ i ≤ n − 1},
S λ = {a ∈ S | ti,j ≤ λj + c(ti,j+1) − 2c(ti,2n−1−j ) + c(ti,2n−j),
ti,2n−1−j ≤ λj + c(ti+1,j+1) − 2c(ti+1,j) + c(ti,2n−j),
ti,n−1 ≤ λn−1 + c(ti,n+1) − 2˜c(ti+1,n−1),
ti,n ≤ λn + c(ti,n+1) − 2˜c(ti+1,n) for 1 ≤ i ≤ n − 1, n − i ≤ j < n − 1}.
Let B be the crystal given by
20 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
(An) 1 2
1/d111/d111 · · ·
2/d111/d111 n
n−1/d111/d111 n + 1
n/d111/d111
(Bn) 1 · · ·
1/d111/d111 n
n−1/d111/d111 0
n/d111/d111 nn/d111/d111 · · ·
n−1/d111/d111 1
1/d111/d111
(Cn) 1 · · ·
1/d111/d111 n − 1
n−2/d111/d111 n
n−1/d111/d111 nn/d111/d111 n − 1
n−1/d111/d111 · · ·
n−2/d111/d111 1
1/d111/d111
(Dn)
n
n
/d125/d125⑤⑤⑤⑤⑤⑤⑤⑤⑤
1 · · ·
1/d111/d111 n − 1
n−2/d111/d111 n − 1
n−1
/d97/d97❇❇❇❇❇❇❇❇❇
n
/d125/d125⑤⑤⑤⑤⑤⑤⑤⑤⑤
· · ·
n−2/d111/d111 1
1/d111/d111
n
n−1
/d97/d97❇❇❇❇❇❇❇❇❇
with the entries ordered by
(An) 1 ≻ 2 ≻ · · · ≻ n + 1,
(Bn) 1 ≻ 2 ≻ · · · ≻ n ≻ 0 ≻ n ≻ · · · ≻ 2 ≻ 1,
(Cn) 1 ≻ 2 ≻ · · · ≻ n − 1 ≻ n ≻ n ≻ n − 1 ≻ · · · ≻ 1,
(Dn) 1 ≻ 2 ≻ · · · ≻ n − 1 ≻ n, n ≻ n − 1 ≻ · · · ≻ 1.
Let
ˆı =



ı if 1 ≤ i ≤ n + 1 ( An), 1 ≤ i ≤ n (Bn, Cn, Dn),
0 if i = n + 1 ( Bn),
2n + 1 − i if n + 1 ≤ i ≤ 2n (Cn, Dn),
2n + 2 − i if n + 2 ≤ i ≤ 2n + 1 ( Bn).
(3.2)
For a, b ∈ B with a ≻ b, let i(a, b) be a sequence of elements in I such that a = ˜fi(a,b)b,
and deﬁne the irreducible graded R-module
∆ (a,b) = ˜fi(a,b)1.(3.3)
Note that ∆ (a,b) in general is not a cuspidal representation given in [7, 21].
Remark. The set of cuspidal representations is in one-to-one corresp ondence with the
set of positive roots, via correspondence given by the weigh ts of the cuspidal representations.
But there are some ∆( a, b)’s which do not correspond to positive roots. For example, in type
Bn, the module ∆ (1,1) ∈ R(∑ n
i=1 2αi)-fmod is not a cuspidal representation, since ∑ n
i=1 2αi
is not a positive root (see Example 3.5).
The action of the KLR algebra can be described explicitly as f ollows.
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 21
If one of the following holds: a ≻ b (An, Cn), either b ≽ 0 or 0 ≽ a (Bn), either b ≻ n − 1
or n − 1 ≻ a (Dn), then the module ∆ (a,b) is the 1-dimensional R-module Cv speciﬁed by
xiv = 0, τ jv = 0, e (i)v =
{
v if i = i(a, b),
0 otherwise.
If a ≻ 0 ≻ b for type Bn, then ∆ (a,b) is the 2-dimensional R-module Cu ⊕ Cv with R-action
xiu = 0, τ ju =
{
v if j = d,
0 otherwise, e(i)u =
{
u if i = i(a, b),
0 otherwise,
xiv =



−u if i = d,
u if i = d + 1,
0 otherwise
τjv = 0, e (i)v =
{
v if i = i(a, b),
0 otherwise,
where d is an integer such that σd(i(a, b)) = i(a, b).
If a ≽ n − 1 and n − 1 ≽ b for type Dn, then the module ∆ (a,b) is the 2-dimensional
R-module Cu ⊕ Cv given by
xiu = 0, τ ju =
{
Qn,n−1(xn, xn−1)v if j = d,
0 otherwise, e(i)u =
{
u if i = i(a, n) ∗ i(n, b),
0 otherwise,
xiv = 0, τ jv =
{
u if j = d,
0 otherwise, e(i)v =
{
v if i = i(a, n) ∗ i(n, b),
0 otherwise,
where d is an integer such that σd(i(a, n)∗i(n, b)) = i(a, n)∗i(n, b). Note that Qn,n−1(xn, xn−1) =
ζn,n−1 ∈ C \ {0}.
It follows from the description above that, for a, b ∈ B with a ≻ b,
ch∆ (a,b) =



i(a, n) ∗ i(n, b) + i(a, n) ∗ i(n, b) if a ≽ n − 1, n − 1 ≽ b (Dn),
2i(a, b) if a ≻ 0 ≻ b (Bn),
i(a, b) otherwise.
(3.4)
Remark. We see from the expression for the character in (3.4) that ∆ (a,b) can be identiﬁed
with the sequence i(a, b), or equivalently, with the segment of B between a and b, which is
another reason why we deﬁned the Kashiwara operators in the o pposite manner to [15, 19] .
Given a ∈ S (resp. a ∈ S λ) and i = 1, . . . , n, let
∆( a; i) =



ni
⊠
j=n+1−i
(
∆ ⊠ϑij
( ˆn+1−ı, ˆ+1)
)
if 1 ≤ i ≤ n (An, Bn, Cn),
∆ ⊠t1,n−1
(n−1, n ) if i = 1 ( Dn),
∆ ⊠t1,n
(n−1, n) if i = 2 ( Dn),
ni
⊠
j=n+1−i
(
∆ ⊠ϑi−1,j
( ˆn+1−ı, ˆ+1)
)
if 3 ≤ i ≤ n (Dn),
(3.5)
22 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
where ni = n for all i (An), ni = n + i (Bn), ni = n − 1 + i (Cn, Dn), △(a) = {ti,j}, and
ϑij =



ti,j − ti,j+1 if j ≤ ni (An, Cn), j ≤ n − 2 ( Bn), j ≤ n − 3 ( Dn),
ti,n−1 − ⌈ ti,n
2 ⌉ if j = n − 1 ( Bn),
⌈ ti,n
2 ⌉ − ⌊ ti,n
2 ⌋ if j = n (Bn),
⌊ ti,n
2 ⌋ − ti,n+1 if j = n + 1 ( Bn),
ti,n−2 − max{ti,n−1, ti,n} if j = n − 2 ( Dn),
max{0, ti,n − ti,n−1} if j = n − 1 ( Dn),
max{0, ti,n−1 − ti,n} if j = n (Dn),
min{ti,n−1, ti,n} − ti,n+1 if j = n + 1 ( Dn),
ti,j−1 − ti,j if j ≥ n + 2 ( Bn, Dn).
(3.6)
For v ∈ B(∞) (resp. v ∈ B(λ)), let a(v) be the adapted string of v with respect to the
expression w0 = rs1 · · ·rsn given in Table 1. Now we are ready to state the main theorem in
this section.
Theorem 3.2. Let (A, P, Π , P∨, Π ∨) be a Cartan datum of ﬁnite classical type. For v ∈
B(∞) (resp. v ∈ B(λ)), let a(v) be the adapted string of v with respect to the expression
w0 = rs1 · · ·rsn given in Table 1 and let ∆( a(v)) = ∆( a(v); 1) ⊠ · · · ⊠ ∆( a(v); n). Then
(1) hd Ind∆( a(v)) is irreducible.
(2) The map Ψ : B(∞) − →B(∞) deﬁned by
Ψ( v) = hd Ind∆( a(v)) for v ∈ B(∞)
is a crystal isomorphism.
(3) The map Ψ λ : B(λ) − →B(λ) deﬁned by
Ψ λ(v) = hd Ind∆( a(v)) for v ∈ B(λ)
is a crystal isomorphism.
Theorem 3.2 and Proposition 3.1 combine to give the followin g explicit description of the
irreducible graded modules over R and Rλ.
Corollary 3.3. Let (A, P, Π , P∨, Π ∨) be a Cartan datum of ﬁnite classical type. Then
(1) the set
A = {hdInd∆( a) | a ∈ S}
is the complete list of all irreducible graded R-modules up to isomorphism and grading
shift.
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 23
(2) For λ ∈ P+, the set
Aλ = {hd Ind∆( a) | a ∈ S λ}
is the complete list of all irreducible graded Rλ-modules up to isomorphism and grading
shift.
In the following proposition, we give an upper bound for the n umber of ∆ (a,b)’s that can
occur in ∆( a(v)) for v ∈ B(λ).
Proposition 3.4. For v ∈ B(λ), let η(v) be the number of ∆ (a,b)’s in the outer tensor product
∆( a(v)) = ∆( a(v); 1) ⊠ · · · ⊠ ∆( a(v); n). Then η(v) ≤ nλ(h), where
h =



h1 + · · · + hn (An),
2h1 + · · · + 2hn−1 + hn (Bn),
2(h1 + · · · + hn) ( Cn),
2h1 + · · · + 2hn−2 + hn−1 + hn (Dn).
Proof. Let a = a(v) and write a = a1 ∗ · · · ∗ an, where ak = ( ak,1, ak,2, . . . ,ak,lk) is the
subsequence of a deﬁned in (2.3). Since ak,1 = tk,n+1−k if A is of type An, Bn, Cn and
a1,1 = t1,n−1, a2,1 = t1,n, ak,1 = tk−1,n+1−k when n ≥ 3 for type Dn, it follows from (3.5) and
(3.6) that
η(v) ≤ a1,1 + · · · + an−1,1 + an,1.
Thus, it suﬃces to show that
a1,1 + · · · + an−1,1 + an,1 ≤ nλ(h).
Let λ = λ1Λ 1 + · · · + λnΛ n. If n > 1 for type An, Bn, Cn and n > 2 for type Dn, then using
the description in Proposition 3.1, we will obtain
an,1 ≤ λ(h)(3.7)
from the following inequalities:
24 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
(An) : an,1 = tn,1 ≤ λ1 + tn,2 ≤ λ1 + λ2 + tn,3 ≤ · · · ≤ λ1 + · · · + λn = λ(h),
(Bn) : an,1 = tn,1 ≤ λ1 + tn,2 + tn,2n−2 − 2tn,2n−1 ≤ λ1 + λ2 + tn,3 + tn,2n−3 − tn,2n−2 − tn,2n−1
≤ · · · ≤ λ1 + · · · + λn−1 + tn,n − tn,n+1 − tn,2n−1
≤ λ1 + · · · + λn + tn,n+1 − tn,2n−1 ≤ λ1 + · · · + λn + λn−1 + tn,n+2 − tn,2n−1
≤ · · · ≤ 2λ1 + 2λ2 + · · · + 2λn−1 + λn = λ(h),
(Cn) : an,1 = tn,1 ≤ λ1 + tn,2 + tn,2n−2 − 2tn,2n−1 ≤ λ1 + λ2 + tn,3 + tn,2n−3 − tn,2n−2 − tn,2n−1
≤ · · · ≤ λ1 + · · · + λn−1 + 2tn,n − tn,n+1 − tn,2n−1
≤ λ1 + · · · + λn−1 + 2λn + tn,n+1 − tn,2n−1
≤ · · · ≤ 2λ1 + 2λ2 + · · · + 2λn−1 + 2λn = λ(h),
(Dn) : an,1 = tn−1,1 ≤ λ1 + tn−1,2 + tn−1,2n−3 − 2tn−1,2n−2
≤ λ1 + λ2 + tn−1,3 + tn−1,2n−4 − tn−1,2n−3 − tn−1,2n−2
≤ · · · ≤ λ1 + · · · + λn−2 + tn−1,n−1 + tn−1,n − tn−1,n+1 − tn−1,2n−2
≤ λ1 + · · · + λn + tn−1,n+1 − tn−1,2n−2
≤ λ1 + · · · + λn + λn−2 + tn−1,n+2 − tn−1,2n−2
≤ · · · ≤ 2λ1 + 2λ2 + · · · + 2λn−2 + λn−1 + λn = λ(h).
We proceed by induction on n. If n = 2 for type An, Bn, Cn or n = 3 for type Dn, then
the assertion can be proved in the same manner as above. We ass ume that n > 2 for type
An, Bn, Cn and n > 3 for type Dn. Let Uq(gn−1) be the subalgebra of Uq(g) generated by ei, fi
(i ∈ I \ {1}) and qh (h ∈ P∨), and let B be the crystal obtained from B(λ) by forgetting the
1-arrows. Note that Uq(gn−1) is of type Xn−1 when Uq(g) is of type Xn (X = A, B, C, D). Let
u = ˜f an
sn bλ where sn is the sequence given in Table 1, and let C be the connected component
of B containing v. Then u is the highest weight vector of the Uq(gn−1)-crystal C with weight
wt(u) =



λ − tn,1α1 − · · · − tn,nαn (An),
λ − (tn,1 + tn,2n−1)α1 − · · · − (tn,n−1 + tn,n+1)αn−1 − (tn,n)αn (Bn, Cn),
λ − (tn−1,1 + tn−1,2n−2)α1 − · · · − (tn−1,n−2 + tn−1,n+1)αn−2
−tn−1,nαn−1 − tn−1,n−1αn (Dn).
Now suppose that h′ = h − h1 (An), and h′ = h − 2h1 (Bn, Cn, Dn). Then we see that
α1(h′) = −1, α 2(h′) = 1 , α i(h′) = 0 ( i = 3, . . . , n) ( An),
α1(h′) = −2, α 2(h′) = 2 , α i(h′) = 0 ( i = 3, . . . , n) ( Bn, Cn, Dn).
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 25
Proposition 3.1 implies
wt(u)(h′) ≤ λ(h)(3.8)
by the following calculations:
(An) : wt(u)(h′) = λ(h′) + tn,1 − tn,2 ≤ λ(h),
(Bn, Cn) : wt(u)(h′) = λ(h′) + 2(tn,1 + tn,2n−1) − 2(tn,2 + tn,2n−2)
= λ(h′) + 2(tn,1 − tn,2 − tn,2n−2 + 2tn,2n−1) − 2tn,2n−1 ≤ λ(h),
(Dn) : wt(u)(h′) = λ(h′) + 2(tn,1 + tn,2n−2) − 2(tn,2 + tn,2n−3)
= λ(h′) + 2(tn,1 − tn,2 − tn,2n−3 + 2tn,2n−2) − 2tn,2n−2 ≤ λ(h).
Since the adapted string of u is a1 ∗ · · · ∗ an−1, we obtain by the induction hypothesis that
a1,1 + · · · + an−1,1 ≤ (n − 1)wt(u)(h′),
which yields, by (3.7) and (3.8),
a1,1 + · · · + an−1,1 + an,1 ≤ (n − 1)λ(h) + λ(h) = nλ(h).
□
Example 3.5. Assume ( A, P, Π , P∨, Π ∨) is type B3 and λ = Λ 1 + Λ 2 + 3Λ 3 ∈ P+. In this
case, w0 = r3(r2r3r2)(r1r2r3r2r1) and
B = 1 2
1/d111/d111 3
2/d111/d111 0
3/d111/d111 3
3/d111/d111 2
2/d111/d111 1
1/d111/d111 .
Kashiwara and Nakashima [18] constructed combinatorial re alizations of highest weight crys-
tals for ﬁnite classical types using certain semistandard t ableaux, which are now referred to
as Kashiwara-Nakashima tableaux. We take this combinatorial model as a realization of the
crystal B(λ). Let T denote the following element in B(λ)
T =
13
1
3
0
3
1
3
2
.
Since w0 = r3(r2r3r2)(r1r2r3r2r1), using the crystal structure given in [18], we have
a(T ) = (3 , 3, 3, 0, 4, 3, 5, 2, 1) ∈ S λ, △(a(T )) =
4 3 5 2 1
3 3 0
3
,
26 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
T5 := ˜e4
1(T4) T6 := ˜e3
2(T5) T7 := ˜e5
3(T6) T8 := ˜e2
2(T7) T9 := ˜e1
1(T8)
21
2
1
3
0
1
2
3
31
3
1
2
0
1
2
3
31
3
1
2
3
1
2
3
21
2
1
2
3
1
2
3
11
2
1
2
3
1
2
3
T2 := ˜e3
2(T1) T3 := ˜e3
3(T2) T4 := ˜e0
2(T3)
12
1
2
0
3
1
2
3
12
1
2
3
0
1
2
3
12
1
2
3
0
1
2
3
T1 := ˜e3
3(T )
¯13
1
3
0
3
1
3
2
Note that εi(T9) = 0 ( i = 1, 2, 3), εi(T4) = 0 ( i = 2, 3) and εi(T1) = 0 ( i = 3). It follows from
(3.5) and (3.6) that
ϑ1,3 = 1, ϑ 1,4 = 1,
ϑ2,2 = 1, ϑ 2,3 = 1, ϑ 2,4 = 1, ϑ 2,5 = 0,
ϑ3,1 = 1, ϑ 3,2 = 0, ϑ 3,3 = 1, ϑ 3,4 = 0, ϑ 3,5 = 1, ϑ 3,6 = 1,
and using the deﬁnition of ˆı in (3.2), we have
∆( a(T ); 1) = ∆ ⊠ϑ1,3
(ˆ3,ˆ4) ⊠ ∆ ⊠ϑ1,4
(ˆ3,ˆ5)
= ∆ (3,0) ⊠ ∆ (3,3),
∆( a(T ); 2) = ∆ ⊠ϑ2,2
(ˆ2,ˆ3) ⊠ ∆ ⊠ϑ2,3
(ˆ2,ˆ4) ⊠ ∆ ⊠ϑ2,4
(ˆ2,ˆ5) ⊠ ∆ ⊠ϑ2,5
(ˆ2,ˆ6)
= ∆ (2,3) ⊠ ∆ (2,0) ⊠ ∆ (2,3),
∆( a(T ); 3) = ∆ ⊠ϑ3,1
(ˆ1,ˆ2) ⊠ ∆ ⊠ϑ3,2
(ˆ1,ˆ3) ⊠ ∆ ⊠ϑ3,3
(ˆ1,ˆ4) ⊠ ∆ ⊠ϑ3,4
(ˆ1,ˆ5) ⊠ ∆ ⊠ϑ3,5
(ˆ1,ˆ6) ⊠ ∆ ⊠ϑ3,6
(ˆ1,ˆ7)
= ∆ (1,2) ⊠ ∆ (1,0) ⊠ ∆ (1,2) ⊠ ∆ (1,1).
By Theorem 3.2, the Rλ-module M corresponding to T is given as follows:
M = Ψ λ(T )
= hd Ind
(
∆( a(T ); 1) ⊠ ∆( a(T ); 2) ⊠ ∆( a(T ); 3)
)
= hd Ind
(
∆ (3,0) ⊠ ∆ (3,3) ⊠ ∆ (2,3) ⊠ ∆ (2,0) ⊠ ∆ (2,3) ⊠ ∆ (1,2) ⊠ ∆ (1,0) ⊠ ∆ (1,2) ⊠ ∆ (1,1)
)
.
In this example, η(T ) = 9 < nλ(h) = 3(Λ 1 + Λ 2 + 3Λ 3)(2h1 + 2h2 + h3) = 21.
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 27
Recall the deﬁnition of Nk(T ) in (1.4) (here the element v in B(λ) is the tableau T ). Then
N1(T ) = hd Ind
(
∆( a(T ); 1)
)
, N2(T ) = hd Ind
(
∆( a(T ); 2)
)
, N3(T ) = hd Ind
(
∆( a(T ); 3)
)
.
We will prove that such a realization of these modules exists for all ﬁnite classical types in
the next section (Lemma 4.3). In this example, we give an intu itive picture for the case of
N3(T ). For a, b ∈ B with a ≻ b, by the deﬁnition of ∆ (a,b) in (3.3) we can identify ∆ (a,b) with
the segment of B between a and b. Then we have the following diagram.
∆ (1,2) 1 2
1/d111/d111
∆ (1,0) 1 2
1/d111/d111 3
2/d111/d111 0
3/d111/d111
∆ (1,2) 1 2
1/d111/d111 3
2/d111/d111 0
3/d111/d111 3
3/d111/d111 2
2/d111/d111
∆ (1,1) 1 2
1/d111/d111 3
2/d111/d111 0
3/d111/d111 3
3/d111/d111 2
2/d111/d111 1
1/d111/d111
4 × ˜f1 3 × ˜f2 5 × ˜f3 2 × ˜f2 1 × ˜f1
The Kashiwara operators at the bottom of the diagram are obta ined by adding up vertically
the number of i-colored arrows in the segments. By Proposition 2.3, we know
N3(T ) = ˜f 4
1 ˜f 3
2 ˜f 5
3 ˜f 2
2 ˜f 1
1 1.
Since N3(T ) = hd Ind
(
∆ (1,2) ⊠∆ (1,0) ⊠∆ (1,2) ⊠∆ (1,1)
)
, taking the head of Ind
(
∆ (1,2) ⊠∆ (1,0) ⊠
∆ (1,2) ⊠ ∆ (1,1)
)
can be understood as summing vertically the i-colored arrows in the segments
corresponding to the modules ∆ (1,2), ∆ (1,0), ∆ (1,2) and ∆ (1,1).
Now from the crystal structure in [18], we know that
˜f1T =
13
1
3
0
3
2
3
1
, ˜f2T =
13
1
3
0
2
1
3
2
, ˜f3T = 0,
which yield a( ˜f1T ) = (3 , 2, 1, 0, 5, 4, 7, 2, 1) ∈ S λ, a( ˜f2T ) = (3 , 4, 3, 0, 4, 3, 5, 2, 1) ∈ S λ and
△(a( ˜f1T )) =
5 4 7 2 1
2 1 0
3
, △(a( ˜f2T )) =
4 3 5 2 1
4 3 0
3
.
28 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
Therefore, by Theorem 3.2, the irreducible modules ˜f1(M ) = hd Ind (L(1) ⊠ M ) and ˜f2(M ) =
hd Ind (L(2) ⊠ M ) can be gotten as follows:
˜f1(M ) = ˜f1(Ψ λ(T )) = Ψ λ( ˜f1T )
= hd Ind
(
∆ (3,0) ⊠ ∆ (3,3) ⊠ ∆ (2,3) ⊠ ∆ (2,0) ⊠ ∆ (1,2) ⊠ ∆ (1,0) ⊠ ∆ (1,3) ⊠ ∆ (1,2) ⊠ ∆ (1,1)
)
,
˜f2(M ) = ˜f2(Ψ λ(T )) = Ψ λ( ˜f2T )
= hd Ind
(
∆ (3,0) ⊠ ∆ (3,3) ⊠ ∆ ⊠2
(2,3) ⊠ ∆ (2,0) ⊠ ∆ (2,3) ⊠ ∆ (1,2) ⊠ ∆ (1,0) ⊠ ∆ (1,2) ⊠ ∆ (1,1)
)
.
Note that by the same argument as above, one can compute the ac tion of Kashiwara
operators on B(∞) explicitly using the combinatorial realizations of B(∞) for ﬁnite classical
type in [5, 9].
4. Proof of Theorem 3.2
This section is devoted to a proof of Theorem 3.2. We ﬁrst give a suﬃcient condition for
Ind
(
∆ (a,b) ⊠ ∆ (c,d)
)
≃ Ind
(
∆ (c,d) ⊠ ∆ (a,b)
)
to hold (Lemma 4.1). Then we extend the result
in [15, Lem. 4.3] for type An to the other ﬁnite classical types in Lemma 4.2 below, and pro ve
Lemma 4.3 which yields Nn(v) = hd Ind∆( a(v); n) for v ∈ B(∞). From that we can deduce
Nk(v) = hd Ind∆( a(v); k) for all k. Using Lemma 1.8, Proposition 1.10, and Lemma 4.3, we
argue that the map Ψ : B(∞) − →B(∞) is a crystal isomorphism. It then follows from the
crystal embedding ιλ : B(λ) → B(∞) ⊗ Tλ ⊗ C in (1.1) that the map Ψ λ : B(λ) − →B(λ) is
a crystal isomorphism too.
Given i ∈ I α and j ∈ I β, a sequence k ∈ I α+β is called a shuﬄe of i and j if k is a
permutation of i ∗ j such that i and j are subsequences of k. For X = ∑ xi i and Y = ∑ yj j,
we deﬁne X ⋆ Y by
X ⋆ Y =
∑
k
xiyj k,
where k runs over all the shuﬄes of i and j. Suppose M ∈ R(α)-fmod and N ∈ R(β)-fmod,
and assume Q is a quotient (resp. L is a submodule) of Ind(M ⊠ N ). Then
ch
(
Ind(M ⊠ N )
)
= ch(M ) ⋆ ch(N ),(4.1)
any term of chQ (resp. chL) is a shuﬄe of some i ∈ ch(M ) and j ∈ ch(N ).(4.2)
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 29
The quantum Serre relations (1.3) imply that
dim(e(. . . , i, j, . . .)M ) = dim(e(. . . , j, i, . . .)M ) if aij = 0,(4.3)
2dim(e(. . . , i, j, i, . . .)M )(4.4)
= dim(e(. . . , i, i, j, . . .)M ) + dim(e(. . . , j, i, i, . . .)M ) if aij = −1,
dim(e(. . . , i, i, i, j, . . .)M ) + 3dim(e(. . . , i, j, i, i, . . .)M )(4.5)
= dim(e(. . . , j, i, i, i, . . .)M ) + 3dim(e(. . . , i, i, j, i, . . .)M ) if aij = −2,
for M ∈ R-fmod.
Using the description of ∆ (a,b) in Section 3, we obtain a surjective homomorphism
Ind
(
∆ (a,b) ⊠ ∆ (b,c)
)
։ ∆ (a,c)(4.6)
for a, b, c ∈ B with a ≻ b ≻ c.
Lemma 4.1. Let a, b, c, d ∈ B with a ≽ c ≻ d ≽ b. Suppose that one of the following
conditions hold:
(1) A is of type An,
(2) A is of type Bn and one of the following three holds:
(i) 0 ≽ a and c ⁄= 0,
(ii) b ≽ 0 and d ⁄= 0,
(iii) a ≽ n, n ≽ b and either c = 0 or d = 0,
(3) A is of type Cn and one of the following three holds:
(i) b ≽ n,
(ii) a = c = n,
(iii) a = 1 and c = n,
(4) A is of type Dn and one of the following three holds:
(i) b ≽ n − 1,
(ii) a = c = n − 1,
(iii) a = 1 and c = n − 1.
Then
Ind
(
∆ (a,b) ⊠ ∆ (c,d)
)
≃ Ind
(
∆ (c,d) ⊠ ∆ (a,b)
)
and these modules are irreducible.
Proof. Let
M = Ind
(
∆ (a,b) ⊠ ∆ (c,d)
)
, N = Ind
(
∆ (c,d) ⊠ ∆ (a,b)
)
,
and let Q (resp. L) be any nonzero quotient (resp. submodule) of M . We will assume that
k is a certain sequence of elements in I such that k ∈ chM , k ∈ chQ, and k ∈ chL. Let
30 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
ξM (resp. ξQ, ξL) be the multiplicity of k in chM (resp. chQ, chL). If we can show that
ξM = ξQ = ξL, we can conclude that M is irreducible and M ≃ N , since chM = chN .
For type An, the assertion follows from [15, Lem. 4.1]. We assume that A is of type Bn. If
either (i) or (ii) holds, the proof is identical to that for ty pe An. So suppose that (iii) holds.
Without loss of generality, we may assume that d = 0. Write i = i(a, b) = ( i, . . . , n, n, . . . , j),
j = i(c, d) = ( p, p + 1, . . . , n− 1, n), and let
k = (i, . . . , p, p, p+ 1, p + 1, . . . , n− 1, n − 1, n, n, n, n − 1, n − 2, . . . , j).
Note that k is a shuﬄe of i and j. Let l be the length of j. It follows from (3.4) and (4.1)
that the term k appears in chM with multiplicity ξM = 2 × 2l−13.
By Lemma 1.5 and (3.4), i∗j appears in the character chQ of any quotient module Q ⊆ M .
We claim that k also appears in chQ. Note that an,n−1 = −2 for type Bn.
We ﬁrst assume that p ⁄= n − 1, n. By the quantum Serre relations (1.3), if j > p + 1, then
i ∗ j =(i, . . . , n, n, . . . , j, p, p+ 1, . . . , n) ∈ chQ,
(4.3)
⇒ (i, . . . , p, p+ 1, p, . . . , n, n, . . . , j, p+ 1, . . . , n) ∈ chQ,
(4.2),(4.4)
=⇒ (i, . . . , p, p, p+ 1, . . . , n, n, . . . , j, p+ 1, . . . , n) ∈ chQ.
If j = p + 1, then
i ∗ j =(i, . . . , n, n, . . . , p+ 1, p, p + 1, . . . , n) ∈ chQ,
(4.2),(4.4)
=⇒ (i, . . . , n, n, . . . , p, p+ 1, p + 1, . . . , n) ∈ chQ,
(4.3)
⇒ (i, . . . , p, p+ 1, p, . . . , n, n, . . . , p+ 1, p + 1, . . . , n) ∈ chQ,
(4.2),(4.4)
=⇒ (i, . . . , p, p, p+ 1, . . . , n, n, . . . , p+ 1, p + 1, . . . , n) ∈ chQ.
If j = p, then
i ∗ j =(i, . . . , n, n, . . . , p+ 1, p, p, p + 1 . . . , n) ∈ chQ,
(4.4)
⇒ (i, . . . , n, n, . . . , p, p+ 1, p, p + 1, . . . , n) ∈ chQ,
(4.3)
⇒ (i, . . . , p, p+ 1, p, . . . , n, n, . . . , p, p+ 1, . . . , n) ∈ chQ,
(4.2),(4.4)
=⇒ (i, . . . , p, p, p+ 1, . . . , n, n, . . . , p, p+ 1, . . . , n) ∈ chQ.
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 31
If j < p , then
i ∗ j =(i, . . . , n, n, . . . , j, p, p+ 1 . . . , n) ∈ chQ,
(4.4)
⇒ (i, . . . , n, n, . . . , p+ 1, p, p − 1, p, . . . , j, p+ 1, . . . , n) ∈ chQ,
(4.2),(4.4)
=⇒ (i, . . . , n, n, . . . , p+ 1, p, p, p − 1, . . . , j, p+ 1, . . . , n) ∈ chQ,
(4.4)
⇒ (i, . . . , n, n, . . . , p, p+ 1, p, p − 1, . . . , j, p+ 1, . . . , n) ∈ chQ,
(4.3)
⇒ (i, . . . , p, p+ 1, p, . . . , n, n, . . . , , j, p+ 1, . . . , n) ∈ chQ,
(4.2),(4.4)
=⇒ (i, . . . , p, p, p+ 1, . . . , n, n, . . . , , j, p+ 1, . . . , n) ∈ chQ.
Applying this argument repeatedly, we determine that
(i, . . . , p, p, . . . , n− 2, n − 2, n − 1, n, n, . . . , j, n− 1, n) ∈ chQ
(4.2),(4.3),(4.4)
=⇒ (i, . . . , p, p, . . . , n− 1, n, n, n − 1, n − 1, . . . , j, n) ∈ chQ,
(4.2),(4.4)
=⇒ (i, . . . , p, p, . . . , n− 1, n, n − 1, n, n − 1, . . . , j, n) ∈ chQ
(4.2),(4.4)
=⇒ (i, . . . , p, p, . . . , n− 1, n − 1, n, n, n − 1, . . . , j, n) ∈ chQ,
(4.3)
⇒ (i, . . . , p, p, . . . , n− 1, n − 1, n, n, n − 1, n, . . . , j) ∈ chQ,
(4.2),(4.5)
=⇒ k = (i, . . . , p, p, . . . , n− 1, n − 1, n, n, n, n− 1, . . . , j) ∈ chQ.
We suppose that p = n − 1, n. Then, the same argument as above gives
k = (i, . . . , n− 1, n − 1, n, n, n, n − 1, . . . , j) ∈ chQ.
Now for any nonzero submodule L of M , chL contains j ∗ i by Lemma 1.5 and (3.4). If
a = c, then
j ∗ i = (i, i + 1, . . . , n, i, . . . , n, n, . . . , j) ∈ chL,
(4.3)
⇒ (i, i + 1, i, . . . , n, i+ 1, . . . , n, n, . . . , j) ∈ chL,
(4.2),(4.4)
=⇒ (i, i, i + 1, . . . , n, i+ 1, . . . , n, n, . . . , j) ∈ chL,
...
(4.2),(4.4)
=⇒ (i, i, i + 1, i + 1, . . . , n− 2, n − 2, n − 1, n, n − 1, n, n, . . . , j) ∈ chL,
(4.2),(4.4)
=⇒ k = (i, i, i + 1, i + 1, . . . , n− 2, n − 2, n − 1, n − 1, n, n, n, . . . , j) ∈ chL.
32 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
If a ≻ c, then
j ∗ i = (p, . . . , n− 1, n, i, . . . , n, n, . . . , j) ∈ chL,
(4.3)
⇒ (p, . . . , n− 1, i, . . . , n, n− 1, n, n, . . . , j) ∈ chL,
(4.2),(4.5)
=⇒ (p, . . . , n− 1, i, . . . , n− 1, n, n, n, . . . , j) ∈ chL,
...
(4.2),(4.4)
=⇒ k = (i, . . . , p, p, p+ 1, p + 1, . . . , n− 1, n − 1, n, n, n, . . . , j) ∈ chL.
Hence, chL contains k in either event. From the structure of k we see that it occurs in chQ
(resp. chL) with multiplicity ξQ ≥ 2l−13! (resp. ξL ≥ 2l−13!). Therefore, since ξM = 2 ×2l−13,
we have ξM = ξQ = ξL, which implies the result for type Bn.
Now assume that A is of type Cn. If either (i) or (ii) holds, the proof is identical to that
for type An. We assume that (iii) holds. Write i = i(a, b) = (1 , 2, . . . , n, . . . , j), j = i(c, d) =
(n, n − 1, . . . , q). Then
k := (1, 2, . . . , n− 1, n, n, n − 1, n − 1, . . . , q, q, . . . , j).
is a shuﬄe of i and j. Let l be the length of j. Then (3.4) and (4.1) imply that the term k
appears in chM with multiplicity ξM = 2 l.
For any nonzero quotient Q of M , chQ contains i ∗ j by (3.4) and Lemma 1.5. We claim
that k occurs in chQ as a term. Note that an−1,n = −2. The quantum Serre relations (1.3)
and (4.2) imply
i ∗ j = (1 , . . . , n, . . . , j, n, . . . , q) ∈ chQ,
(4.3)
⇒ (1, . . . , n− 1, n, n − 1, n, . . . , j, n− 1, . . . , q) ∈ chQ,
(4.2),(4.4)
=⇒ (1, . . . , n− 1, n, n, n − 1, . . . , j, n− 1, . . . , q) ∈ chQ.
Continuing this reasoning gives
k = (1, . . . , n, n, . . . , q, q, . . . , j) ∈ chQ.
For any nonzero submodule L of M , chL contains j ∗ i by Lemma 1.5 and (3.4). Then,
using a similar argument, we have
j ∗ i = ( n, . . . , q,1, 2, . . . , n, . . . , j) ∈ chL,
(4.2),(4.3),(4.4)
=⇒ (n, n − 1, 1, . . . , n− 1, n, n − 1, . . . , q, q, . . . , j) ∈ chL,
(4.2),(4.3),(4.4)
=⇒ (n, 1, . . . , n− 2, n − 1, n − 1, n, n − 1, . . . , q, q, . . . , j) ∈ chL,
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 33
(4.2),(4.5)
=⇒ (n, 1, . . . , n− 2, n − 1, n, n − 1, n − 1, . . . , q, q, . . . , j) ∈ chL,
(4.3)
⇒ (1, . . . , n, n− 1, n, n − 1, n − 1, . . . , q, q, . . . , j) ∈ chL,
(4.2),(4.4)
=⇒ k = (1, . . . , n, n, . . . , q, q, . . . , j) ∈ chL.
As k occurs in chQ (resp. chL) with multiplicity ξQ ≥ 2l (resp. ξL ≥ 2l), and since ξM = 2 l,
the assertion follows from ξM = ξQ = ξL.
Lastly, we assume that A is of type Dn. If (i) holds, then the proof is identical to that for
type An.
Suppose that (ii) holds. Write i = i(a, b) = ( n, n − 1, n − 2, . . . , j), j = i(c, d) = ( n, n −
1, n − 2, . . . , q). Then
k := (n, n, n − 1, n − 1, n − 2, n − 2, . . . , q, q, . . . , j).
is a shuﬄe of i and j. Let l be the length of j. The equations (3.4) and (4.1) imply that the
term k appears in chM with multiplicity ξM = 2 l.
By Lemma 1.5 and (3.4), i∗j appears in the character chQ of any quotient module Q ⊆ M .
We will show that k also appears in chQ. Note that an,n−2 = an−2,n = an−1,n−2 = an−2,n−1 =
−1 and an−1,n = an,n−1 = 0. The quantum Serre relations (1.3) imply
i ∗ j = ( n, n − 1, n − 2 . . . , j, n, n− 1, n − 2, . . . , q) ∈ chQ,
(4.3)
⇒ (n − 1, n, n − 2, n, . . . , j, n− 1, n − 2, . . . , q) ∈ chQ,
(4.2),(4.3),(4.4)
=⇒ (n, n, n − 1, n − 2, . . . , j, n− 1, n − 2, . . . , q) ∈ chQ,
(4.2),(4.4)
=⇒ (n, n, n − 1, n − 2, n − 1 . . . , j, n− 2, . . . , q) ∈ chQ,
(4.2),(4.5)
=⇒ (n, n, n − 1, n − 1, n − 2 . . . , j, n− 2, . . . , q) ∈ chQ.
Continuing this reasoning gives
k = (n, n, n − 1, n − 1, n − 2, n − 2, . . . , q, q, . . . , j) ∈ chQ.
For any nonzero submodule L, since chL contains j ∗ i by Lemma 1.5, the same argument
shows that chL contains k. Since k occurs in chQ (resp. chL) with multiplicity ξQ ≥ 2l (resp.
ξL ≥ 2l), the assertion follows from ξM = ξQ = ξL.
We now assume that (iii) holds. Since the proof is identical t o that for type An if b = n or
b = n, we may assume that n − 1 ≽ b. Write i = i(a, b) = (1 , . . . , n− 2, n, n − 1, n − 2, . . . , j),
j = i(c, d) = ( n, n − 1, n − 2, . . . , q) and
k := (1, . . . , n− 2, n, n, n − 1, n − 1, n − 2, n − 2, . . . , q, q, . . . , j).
34 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
Let l be the length of j. Then k is a shuﬄe of i and j and appears in chM with multiplicity
ξM = 2 l.
For any nonzero quotient Q of M , chQ contains i ∗ j by (3.4) and Lemma 1.5. Using the
same argument as in case (ii), we obtain
k = (1, . . . , n− 2, n, n, n − 1, n − 1, n − 2 . . . , j, n− 2, . . . , q) ∈ chQ.
For any nonzero submodule L of M , chL contains j ∗ i by Lemma 1.5 and (3.4). By the
same argument as in the Cn case, we have
j ∗ i = ( n, . . . , q− 1, q, 1, . . . , n− 2, n, n − 1, n − 2 . . . , j) ∈ chL,
(4.2),(4.3),(4.4)
=⇒ (n, n − 1, n − 2, 1, . . . , n− 2, n, n − 1, n − 2, . . . , q, q, . . . , j) ∈ chL,
(4.2),(4.4)
=⇒ (n, n − 1, 1, . . . , n− 2, n − 2, n, n − 1, n − 2, . . . , q, q, . . . , j) ∈ chL,
(4.4)
⇒ (n, n − 1, 1, . . . , n− 2, n, n − 2, n − 1, n − 2, . . . , q, q, . . . , j) ∈ chL,
(4.2),(4.4)
=⇒ (n, n − 1, 1, . . . , n− 2, n, n − 1, n − 2, n − 2, . . . , q, q, . . . , j) ∈ chL,
(4.3)
⇒ (n, 1, . . . , n− 1, n − 2, n − 1, n, n − 2, n − 2, . . . , q, q, . . . , j) ∈ chL,
(4.2),(4.4)
=⇒ (n, 1, . . . , n− 2, n, n − 1, n − 1, n − 2, n − 2, . . . , q, q, . . . , j) ∈ chL,
(4.3)
⇒ (1, . . . , n, n− 2, n, n − 1, n − 1, n − 2, n − 2, . . . , q, q, . . . , j) ∈ chL,
(4.2),(4.4)
=⇒ k = (1, . . . , n− 2, n, n, n − 1, n − 1, n − 2, n − 2, . . . , q, q, . . . , j) ∈ chL.
Since the sequence k occurs in chQ (resp. chL) with multiplicity ξQ ≥ 2l (resp. ξL ≥ 2l),
by ξM = 2 l, the assertion follows from ξM = ξQ = ξL. □
For a, b ∈ B, we deﬁne
(4.7) δ(a ≽ b) =
{
1 if a ≽ b,
0 otherwise .
In the An case, it follows from [15, Lem. 4.3] that, for dk ∈ Z≥0 and bk ∈ B with b1 ≻ b2 ≻
· · · ≻ bm,
˜f t1
1 ˜f t2
2 · · · ˜f tn
n 1 ≃ Ind
( m
⊠
k=1
∆ ⊠dk
(1,bk)
)
,(4.8)
where ti = ∑ m
j=1 djδ(ı ≻ bj) for i = 1 , . . . , n. Next we will extend this result to the other
ﬁnite classical types. We ﬁrst divide the crystal B for types Bn, Cn, Dn into two pieces so
that each part is almost the same as the crystal or the dual of t he crystal for type A. For
type Bn (resp. Cn, Dn), the crystal B is cut at the element 0 (resp. n, n − 1). In the next
result we give an analogue of (4.8) for each part.
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 35
Lemma 4.2. Let bk ∈ B, and dk ∈ Z≥0 for k = 1, . . . , m. Set
b• =



n + 1 ( An),
0 ( Bn),
n (Cn),
n − 1 ( Dn).
(1) If b1 ≻ b2 ≻ · · · ≻ bm ≽ b•, then
˜f t1
1 ˜f t2
2 · · · ˜f tl
l 1 ≃ Ind
( m
⊠
k=1
∆ ⊠dk
(1,bk)
)
,
where l = n (An, Bn), l = n − 1 ( Cn), l = n − 2 ( Dn) and ti := ∑ m
j=1 djδ(ı ≻ bj)
for i = 1, . . . , l.
(2) Let
ti =



∑ m
j=1 djδ(i ≽ bj) if i = 1, . . . , n (Bn, Cn), i = 1, . . . , n− 2 ( Dn),∑ m
j=1 djδ(n ≽ bj) if i = n − 1 ( Dn),∑ m
j=1 djδ(n ≽ bj) if i = n (Dn).
Then we have
(i) if b• ≻ b1 ≻ b2 ≻ · · · ≻ bm for type Bn, then
˜f s+tn
n ˜f tn−1
n−1 · · · ˜f t1
1 1 ≃ hd Ind
(
L(ns) ⊠
( m
⊠
k=1
∆ ⊠dk
(b•,bk)
) )
for all s ∈ Z≥0,
and the head occurs with multiplicity one as a composition fa ctor of
Ind
(
L(ns) ⊠
( m
⊠
k=1
∆ ⊠dk
(b•,bk)
) )
,
(ii) if b• ≻ bm ≻ bm−1 ≻ · · · ≻ b1 for type Cn, Dn, then
˜f tn
n · · · ˜f t2
2 ˜f t1
1 1 ≃ Ind
( m
⊠
k=1
∆ ⊠dk
(b•,bk)
)
.
Proof. For k1, . . . , kn ∈ Z≥0, it follows from Lemma 1.8 that
˜f k1
1 ˜f k2
2 · · · ˜f kn
n 1 ≃ hd Ind
(
L(1k1) ⊠ · · · ⊠ L(nkn)
)
,(4.9)
˜f kn
n ˜f kn−1
n−1 · · · ˜f k1
1 1 ≃ hd Ind
(
L(nkn) ⊠ · · · ⊠ L(1k1)
)
.(4.10)
(1) When A is of type An, Cn, Dn, this can be shown in the same way as for [15, Lem. 4.3].
Suppose that A is of type Bn. Note that ∆ (1,bk) is one of the cuspidal representations given
in [7, Sec. 6.2] and [21, Sec. 8.5]. By [21, Lem. 6.6], we have Nk := Ind∆ ⊠dk
(1,bk) is irreducible
for k = 1, . . . , m. We write i(1, bk) = (1 , 2, . . . , lk) and let
kk = (1, . . . ,1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
dk
, 2, . . . ,2/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
dk
, . . . , lk, . . . , lk/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
dk
)
36 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
for k = 1 , . . . , m. Then kk appears in chNk with multiplicity ( dk!)lk . Since b1 ≻ b2 ≻ · · · ≻
bm, the sequence k = km ∗ · · · ∗ k1 appears in ch(Ind(Nm ⊠ · · · ⊠ N1)) with multiplicity
(dm!)lm · · ·(d1!)l1 . Lemma 1.7 and Lemma 4.1 imply that Ind
( m
⊠
k=1
Nk
)
≃ Ind(Nm ⊠ · · ·⊠ N1)
is irreducible.
Now for t := (1 , . . . ,1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
t1
, 2, . . . ,2/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
t2
, . . . , n, . . . , n/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
tn
), we have e(t)
(
Ind
( m
⊠
k=1
Nk
) )
⁄= 0. Since
Ind
( m
⊠
k=1
Nk
)
is irreducible, it follows from Lemma 1.5 that there is a surj ective homomorphism
Ind(L(1t1 ) ⊠ · · · ⊠ L(ntn)) ։ Ind
( m
⊠
k=1
Nk
)
.
Therefore, ˜f t1
1 · · · ˜f tn
n 1 ≃ Ind
( m
⊠
k=1
Nk
)
by (4.9).
(2) For this part, note that since ∆ (b•,bk) is a cuspidal representation as in [7, Sec. 6] and
[21, Sec. 8], Nk := Ind∆ ⊠dk
(b•,bk) is irreducible by [21, Lem. 6.6]. We now separate considerat ions
according to the type.
(Case Bn) When A is of type Bn, let N = Ind
(
∆ ⊠dm
(n,bm) ⊠ · · · ⊠ ∆ ⊠d1
(n,b1)
)
. By [15, Lem. 4.3],
we have ˜f tn−1
n−1 · · · ˜f t1
1 1 ≃ N. By (4.6) and Lemma 4.1, for d ∈ Z≥0 we obtain
Ind
(
L(nd) ⊠ ∆ ⊠d
(n,bk)
)
≃ Ind
(
L(nd−1) ⊠ L(n) ⊠ ∆ (n,bk) ⊠ ∆ ⊠d−1
(n,bk)
)
։ Ind
(
L(nd−1) ⊠ ∆ (0,bk) ⊠ ∆ ⊠d−1
(n,bk)
)
≃ Ind
(
L(nd−1) ⊠ ∆ ⊠d−1
(n,bk) ⊠ ∆ (0,bk)
)
...
։ Ind
(
∆ ⊠d
(0,bk)
)
.
Since tn = d1 + · · · + dm, by the same argument as above, we have the following chain of
surjective homomorphisms
Ind
(
L(ns+tn) ⊠ N
)
։ Ind
(
L(ns+tn−dm) ⊠ ∆ ⊠dm
(b•,bm) ⊠ ∆ ⊠dm−1
(n,bm−1) ⊠ · · · ⊠ ∆ ⊠d1
(n,b1)
)
≃ Ind
(
L(ns+tn−dm) ⊠ ∆ ⊠dm−1
(n,bm−1) ⊠ · · · ⊠ ∆ ⊠d1
(n,b1) ⊠ ∆ ⊠dm
(b•,bm)
)
։ Ind
(
L(ns+tn−dm−dm−1) ⊠ ∆ ⊠dm−2
(n,bm−2) ⊠ · · · ⊠ ∆ ⊠d1
(n,b1) ⊠ ∆ ⊠dm−1
(b•,bm−1) ⊠ ∆ ⊠dm
(b•,bm)
)
...
։ Ind
(
L(ns) ⊠
( m
⊠
i=1
∆ ⊠di
(b•,bi)
) )
.
Therefore, by Lemma 1.8 and [19, Lem. 3.13], we obtain
˜f s+tn
n ˜f tn−1
n−1 · · · ˜f t1
1 1 ≃ hd Ind
(
L(ns+tn) ⊠ N
)
≃ hd Ind
(
L(ns) ⊠
( m
⊠
i=1
∆ ⊠di
(b•,bi)
))
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 37
and this module has multiplicity one as a composition factor of Ind
(
L(ns) ⊠
( m
⊠
i=1
∆ ⊠di
(b•,bi)
))
.
(Case Cn) For type Cn, we write i(b•, bj) = ( n, n − 1, . . . , n− lj + 1) and let
kk = (n, . . . , n/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
dk
, n − 1, . . . , n− 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
dk
, . . . , n− lk + 1, . . . , n− lk + 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
dk
)
for k = 1 , . . . , m. Then kk appears in chNk with multiplicity ( dk!)lk . Since b• ≻ bm ≻
bm−1 ≻ · · · ≻ b1, the sequence k := k1 ∗ · · · ∗ km appears in ch Ind
( m
⊠
k=1
Nk
)
with multiplicity
(d1!)l1 · · ·(dm!)lm . It follows from Lemma 1.7 and Lemma 4.1 that Ind
( m
⊠
k=1
Nk
)
is irreducible.
Let t = ( n, . . . , n/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
tn
, n − 1, . . . , n− 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
tn−1
, . . . ,1, . . . ,1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
t1
). Then we have e(t)
(
Ind
( m
⊠
k=1
Nk
))
⁄= 0.
Since Ind
( m
⊠
k=1
Nk
)
is irreducible, by Lemma 1.5 there exists a surjective homom orphism
Ind(L(ntn ) ⊠ · · · ⊠ L(1t1 )) ։ Ind
( m
⊠
k=1
Nk
)
.
Therefore, it follows from (4.10) that ˜f tn
n · · · ˜f t2
2 ˜f t1
1 1 ≃ Ind
( m
⊠
k=1
Nk
)
.
(Case Dn) For k = 1 , . . . , m, let lk be the length of i(n − 1, n) ∗ i(n, bk) if n ≻ bk, and
lk = 1 if bk = n or bk = n. We will show that Ind
( m
⊠
k=1
∆ ⊠dk
(b•,bk)
)
is irreducible for type Dn.
First suppose that bm−1 ⁄= n − 1. Let
kk =



(n − 1, . . . , n− 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
dk
) if bk = n,
(n, . . . , n/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
dk
, n − 1, . . . , n− 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
dk
, . . . , n− lk + 1, . . . , n− lk + 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
dk
) otherwise.
for k = 1 , . . . , m. Then kk appears in chNk with multiplicity ( dk!)lk . Since bm ≻ bm−1 ≻
· · · ≻ b1 and bm−1 ⁄= n − 1, the sequence k := k1 ∗ · · · ∗ km appears in ch Ind
( m
⊠
k=1
Nk
)
with
multiplicity (d1!)l1 · · ·(dm!)lm . It follows from Lemma 1.7 and Lemma 4.1 that Ind
( m
⊠
k=1
Nk
)
is irreducible.
We now assume that bm−1 = n − 1. Without loss of generality, we may suppose that
bm = n. Since Ind(L(n − 1) ⊠ L(n)) ≃ Ind(L(n) ⊠ L(n − 1)), we have
Ind∆ ⊠dm−1
(n−1,n−1) ⊠ ∆ ⊠dm
(n−1,n) ≃ Ind∆ ⊠dm
(n−1,n) ⊠ ∆ ⊠dm−1
(n−1,n−1) ≃ Ind
(
L
(
ndm−1
)
⊠ L
(
(n − 1)dm−1+dm
) )
and they are irreducible. Let Mk =
{
Ind∆ ⊠dk
(b•,bk) if k ≤ m − 2,
Ind∆ ⊠dm−1
(b•,bm−1) ⊠ ∆ ⊠dm
(b•,bm) if k = m − 1, and set
38 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
kk =



(n, . . . , n/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
dk
, n − 1, . . . , n− 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
dk
, . . . , n− ℓk + 1, . . . , n− ℓk + 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
dk
) if k ≤ m − 2,
(n, . . . , n/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
dm−1
, n − 1, . . . , n− 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
dm−1+dm
) if k = m − 1.
Then the multiplicity of kk in chMk is ( dk!)lk if k ≤ m − 2 and dm−1!(dm + dm−1)! if
k = m − 1. Since b• ≻ bm ≻ bm−1 ≻ · · · ≻ b1, the sequence k := k1 ∗ · · · ∗ km−1 appears in
ch (Ind(M1 ⊠ · · · ⊠ Mm−1)) with multiplicity ( d1!)l1 · · ·(dm−2!)lm−2 (dm−1!)((dm + dm−1)!). It
follows from Lemma 1.7 and Lemma 4.1 that Ind(M1 ⊠ · · · ⊠ Mm−1) is irreducible.
Now for t = (n, . . . , n/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
tn
, n − 1, . . . , n− 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
tn−1
, . . . ,1, . . . ,1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
t1
), we have e(t)
(
Ind
( m
⊠
i=1
∆ ⊠di
(b•,bi)
) )
⁄= 0.
Since Ind
( m
⊠
i=1
∆ ⊠di
(b•,bi)
)
is irreducible, Lemma 1.5 gives a surjective homomorphism
Ind(L(ntn ) ⊠ · · · ⊠ L(1t1 )) ։ Ind
( m
⊠
i=1
∆ ⊠di
(b•,bi)
)
,
which implies the desired conclusion ˜f tn
n · · · ˜f t2
2 ˜f t1
1 1 ≃ Ind
( m
⊠
i=1
∆ ⊠di
(b•,bi)
)
by (4.10). □
Recall the deﬁnition of ˆı ∈ B from (3.2). Using the surjective homomorphism in (4.6),
we can glue parts (1) and (2) of Lemma 4.2 together for types Bn, Cn, and Dn to get the
following result.
Lemma 4.3. Let ti ∈ Z≥0 be such that
t1 ≥ t2 ≥ · · · ≥ tn′−1 ≥ tn′ ≥ tn′+1 = 0 ( An, Cn),
2t1 ≥ 2t2 ≥ · · · ≥ 2tn−1 ≥ tn ≥ 2tn+1 ≥ · · · ≥ 2tn′−1 ≥ tn′ = 0 ( Bn),
t1 ≥ t2 ≥ · · · ≥ tn−2 ≥ tn−1, tn ≥ tn+1 ≥ · · · ≥ tn′−1 ≥ tn′ = 0 ( Dn),
where n′ = n (An), n′ = 2n (Bn), n′ = 2n − 1 ( Cn, Dn). Set
ϑi =



ti − ti+1 if i ≤ n′ (An, Cn), i ≤ n − 2 ( Bn), i ≤ n − 3 ( Dn),
tn−1 − ⌈ tn
2 ⌉ if i = n − 1 ( Bn),
⌈ tn
2 ⌉ − ⌊ tn
2 ⌋ if i = n (Bn),
⌊ tn
2 ⌋ − tn+1 if i = n + 1 ( Bn),
tn−2 − max{tn−1, tn} if i = n − 2 ( Dn),
max{0, tn − tn−1} if i = n − 1 ( Dn),
max{0, tn−1 − tn} if i = n (Dn),
min{tn−1, tn} − tn+1 if i = n + 1 ( Dn),
ti−1 − ti if i ≥ n + 2 ( Bn, Dn).
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 39
Then
(1) hd Ind
( n′
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆi+1)
)
is irreducible and has multiplicity one as a composition fac tor of
Ind
( n′
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆi+1)
)
,
(2) ˜fi1 ≃ hd Ind
( n′
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆi+1)
)
, where
i =



(1, . . . ,1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
t1
, 2, . . . ,2/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
t2
, . . . , n, . . . , n/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
tn
) (An),
(1, . . . ,1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
t1
, . . . , n− 1, . . . , n− 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
tn−1
, n, . . . , n/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
tn
, n − 1, . . . , n− 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
tn+1
, . . . ,1, . . . ,1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
t2n−1
) ( Bn, Cn),
(1, . . . ,1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
t1
, . . . , n− 2, . . . , n− 2/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
tn−2
, n, . . . , n/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
tn−1
, n − 1, . . . , n− 1/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
tn
, . . . ,1, . . . ,1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
t2n−2
) ( Dn).
Proof. By Lemma 4.1 and (4.6), for k ∈ Z≥0 we have
(4.11)
Ind
(
∆ ⊠k
(ˆ1,b) ⊠ ∆ ⊠k
(b,c)
)
≃ Ind
(
∆ ⊠k−1
(ˆ1,b) ⊠ ∆ (ˆ1,b) ⊠ ∆ (b,c) ⊠ ∆ ⊠k−1
(b,c)
)
։ Ind
(
∆ ⊠k−1
(ˆ1,b) ⊠ ∆ (ˆ1,c) ⊠ ∆ ⊠k−1
(b,c)
)
≃ Ind
(
∆ ⊠k−1
(ˆ1,b) ⊠ ∆ ⊠k−1
(b,c) ⊠ ∆ (ˆ1,c)
)
...
։ Ind
(
∆ ⊠k
(ˆ1,c)
)
,
where b ∈ B (An), b = ˆn + 1 ( Bn), b = ˆn (Cn), b = ˆn − 1 ( Dn) and c ∈ B with b ≻ c.
(Case An) The assertion in this case follows from Lemma 4.2.
(Case Bn) For type Bn, let
M (k) = Ind
((2n−k
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆı+1)
)
⊠ ∆ ⊠(ϑ2n+···+ϑ2n+1−k)
(ˆ1,ˆn+1)
)
, and
N (k) = Ind
(
∆ ⊠ϑ2n+1−k
(ˆn+1, ˆ2n+2−k)
⊠ ∆ ⊠ϑ2n+2−k
(ˆn+1, ˆ2n+3−k)
⊠ · · · ⊠ ∆ ⊠ϑ2n
(ˆn+1, ˆ2n+1)
)
for k = 1, . . . , n. Note that tn = ⌈ tn
2 ⌉ + ⌊ tn
2 ⌋, ⌈ tn
2 ⌉ = ϑn + · · ·ϑ2n and ⌊ tn
2 ⌋ = ϑn+1 + · · ·+ ϑ2n.
If follows from Lemma 4.2 that
M (n) ≃ ˜f t1
1 · · · ˜f tn−1
n−1 ˜f
⌈ tn
2 ⌉
n 1, hdN (n) ≃ ˜f
⌊ tn
2 ⌋
n ˜f tn+1
n−1 · · · ˜f t2n−1
1 1.
By Lemma 4.2 and [19, Lem. 3.13], there is a surjective homomo rphism
Ind
(
∆
⊠⌈ tn
2 ⌉
(1,n) ⊠ L(n⌈ tn
2 ⌉)
)
։ Ind∆
⊠⌈ tn
2 ⌉
(1,0) ,
40 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
which yields the following surjective homomorphism
Ind
(((n−1
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆı+1)
)
⊠ ∆
⊠⌈ tn
2 ⌉
(ˆ1,ˆn)
)
⊠
(
L(n⌈ tn
2 ⌉) ⊠ N (n)
) )
։ Ind
((n−1
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆi+1)
)
⊠ ∆
⊠⌈ tn
2 ⌉
(ˆ1,ˆn+1) ⊠ N (n)
)
≃ Ind
(( n
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆı+1)
)
⊠ ∆
⊠⌊ tn
2 ⌋
(ˆ1,ˆn+1) ⊠ N (n)
)
≃ Ind(M (n) ⊠ N (n)).
It follows from Lemma 4.2 that
˜f t1
1 · · · ˜f tn−1
n−1 1 ≃ Ind
((n−1
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆi+1)
)
⊠ ∆
⊠⌈ tn
2 ⌉
(ˆ1,ˆn)
)
,
˜f tn
n ˜f tn+1
n−1 · · · ˜f t2n−1
1 1 ≃ hd Ind
(
L(n⌈ tn
2 ⌉) ⊠ N (n)
)
.
Since εi
(
Ind
(
L(n⌈ tn
2 ⌉) ⊠ N (n)
) )
= 0 for i = 1, . . . , n− 1, by Lemma 1.8 we have
˜fi1 ≃ hd Ind
(
M (n) ⊠ N (n)
)
,
and this module has multiplicity one as a composition factor of Ind
(
M (n) ⊠ N (n)
)
.
Now by Lemma 4.1 and (4.11), we have the following chain of sur jective homomorphisms
Ind(M (n) ⊠ N (n))
≃ Ind
(( n
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆı+1)
)
⊠ ∆ ⊠(ϑ2n+···+ϑn+2)
(ˆ1,ˆn+1) ⊠
(
∆ ⊠ϑn+1
(ˆ1,ˆn+1) ⊠ ∆ ⊠ϑn+1
(ˆn+1,ˆn+2)
)
⊠ N (n − 1)
)
։ Ind
(( n
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆı+1)
)
⊠ ∆ ⊠(ϑ2n+···+ϑn+2)
(ˆ1,ˆn+1) ⊠ ∆ ⊠ϑn+1
(ˆ1,ˆn+2) ⊠ N (n − 1)
)
≃ Ind(M (n − 1) ⊠ N (n − 1))
...
։ Ind(M (1) ⊠ N (1)) ≃ Ind
((2n−1
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆı+1)
)
⊠ ∆ ⊠ϑ2n
(ˆ1,ˆn+1) ⊠ ∆ ⊠ϑ2n
(ˆn+1, ˆ2n+1)
)
։ Ind
( 2n
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆi+1)
)
,
which completes the proof for Bn.
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 41
(Case Cn) For type Cn, set
M (k) = Ind
((n−1
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆi+1)
)
⊠ ∆ ⊠(ϑn+···+ϑn−1+k)
(ˆ1,ˆn)
)
, and
N (k) = Ind
(
∆ ⊠ϑk+n−1
(ˆn,ˆk+n) ⊠ ∆ ⊠ϑk+n−2
(ˆn, ˆk+n−1) ⊠ · · · ⊠ ∆ ⊠ϑn
(ˆn,ˆn+1)
)
for 1 ≤ k ≤ n. It follows from Lemma 4.2 that
M (n) ≃ ˜f t1
1 ˜f t2
2 · · · ˜f tn−1
n−1 1, N (n) ≃ ˜f tn
n ˜f tn+1
n−1 · · · ˜f t2n−1
1 1.
Since εi(N (n)) = 0 for i = 1, . . . , n− 1, Lemma 1.8 implies
˜fi1 ≃ hd Ind(M (n) ⊠ N (n))
and this module has multiplicity one as a composition factor in Ind
(
M (n) ⊠ N (n)
)
.
By Lemma 4.1 and (4.11), we have a chain of surjective homomor phisms
Ind
(
M (n) ⊠ N (n)
)
≃ Ind
(
M (n − 1) ⊠ ∆ ⊠ϑ2n−1
(ˆ1,ˆn) ⊠ ∆ ⊠ϑ2n−1
(ˆn,ˆ2n) ⊠ N (n − 1)
)
։ Ind
(
M (n − 1) ⊠ ∆ ⊠ϑ2n−1
(ˆ1,ˆ2n) ⊠ N (n − 1)
)
≃ Ind
(
M (n − 1) ⊠ N (n − 1) ⊠ ∆ ⊠ϑ2n−1
(ˆ1,ˆ2n)
)
...
։ Ind
(
M (1) ⊠ N (1) ⊠ ∆ ⊠ϑn+1
(ˆ1,ˆn+2) ⊠ · · · ⊠ ∆ ⊠ϑ2n−1
(ˆ1,ˆ2n)
)
։ Ind
((n−1
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆı+1)
)
⊠ ∆ ⊠ϑn
(ˆ1,ˆn+1) ⊠ · · · ⊠ ∆ ⊠ϑ2n−1
(ˆ1,ˆ2n)
)
≃ Ind
(2n−1
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆı+1)
)
,
which yields ˜fi1 ≃ hd Ind
(2n−1
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆı+1)
)
.
(Case Dn) Without loss of generality, we may assume in the Dn case that tn−1 ≥ tn. Note
that ϑn−1 = 0 and ϑn = max{tn−1, tn} − min{tn−1, tn}. Let
M (k) = Ind
((n−2
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆi+1)
)
⊠ ∆ ⊠(ϑn+···+ϑn−1+k)
(ˆ1,ˆn−1)
)
,
N (k) = Ind
(
∆ ⊠ϑk+n−1
(ˆn−1,ˆk+n) ⊠ ∆ ⊠ϑk+n−2
(ˆn−1, ˆk+n−1) ⊠ · · · ⊠ ∆ ⊠ϑn
(ˆn−1,ˆn+1)
)
for k = 1, . . . , n. It follows from Lemma 4.2 that
M (n) ≃ ˜f t1
1 ˜f t2
2 · · · ˜f tn−2
n−2 1, N (n) ≃ ˜f tn−1
n ˜f tn
n−1 ˜f tn+1
n−2 · · · ˜f t2n−2
1 1.
42 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
Since εi(N (n)) = 0 for i = 1, . . . , n− 2, Lemma 1.8 gives
˜fi1 ≃ hd Ind(M (n) ⊠ N (n)),
and this module with multiplicity one in Ind(M (n) ⊠ N (n)).
Since ∆ ⊠ϑn−1
(ˆ1,ˆn) = C, Lemma 4.1 and (4.11) again give a string of surjective homom orphisms
Ind(M (n) ⊠ N (n)) ≃ Ind
(
M (n − 1) ⊠ ∆ ⊠ϑ2n−1
(ˆ1,ˆn−1) ⊠ ∆ ⊠ϑ2n−1
(ˆn−1,ˆ2n) ⊠ N (n − 1)
)
։ Ind
(
M (n − 1) ⊠ ∆ ⊠ϑ2n−1
(ˆ1,ˆ2n) ⊠ N (n − 1)
)
≃ Ind
(
M (n − 1) ⊠ N (n − 1) ⊠ ∆ ⊠ϑ2n−1
(ˆ1,ˆ2n)
)
...
։ Ind
(
M (1) ⊠ N (1) ⊠ ∆ ⊠ϑn+1
(ˆ1,ˆn+2) ⊠ · · · ⊠ ∆ ⊠ϑ2n−1
(ˆ1,ˆ2n)
)
։ Ind
((n−2
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆı+1)
)
⊠ ∆ ⊠ϑn
(ˆ1,ˆn+1) ⊠ · · · ⊠ ∆ ⊠ϑ2n−1
(ˆ1,ˆ2n)
)
≃ Ind
(2n−1
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆı+1)
)
,
which yields the desired result ˜fi1 ≃ hd Ind
(2n−1
⊠
i=1
∆ ⊠ϑi
(ˆ1,ˆı+1)
)
. □
As an immediate consequence of this lemma we have
Corollary 4.4. Nn(v) = hd Ind∆( a(v); n) for v ∈ B(∞), where Nn(v) is the irreducible
module given in Proposition 2.3.
We now are ready to prove Theorem 3.2.
Proof of Theorem 3.2. Let I(k) = {n − k + 1, n − k + 2, . . . , n} for k = 1 , . . . , n. Note that
I(k) ⊂ I(k+1) and |I(k)| = k. Let Uq(gk) be the subalgebra of Uq(g) generated by ei, f i (i ∈ I(k))
and qh (h ∈ P∨), and let Bk be the crystal obtained from B(∞) by forgetting the i-arrows
for i /∈ I(k). It follows from Table 1 that Uq(gk) is of type Xk when Uq(g) is of type Xn
(X = A, B, C, D). Recall the deﬁnition ai for a ∈ S and the sequences sk given in Section 2.
Take v ∈ B(∞) and let △(a(v)) = {tij}. If i = 1, . . . , n for type An, Bn, Cn, then
a(v)i = (ti,n+1−i, ti,n+2−i, . . . , ti,di),
where di = n for all i (An) and di = n − 1 + i (Bn, Cn). If i = 1, . . . , n for type Dn, then
a(v)i =



(t1,n−1) if i = 1,
(t1,n) if i = 2,
(ti−1,n+1−i, ti−1,n+2−i, . . . , ti−1,n−2+i) if i = 3, . . . , n.
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 43
Let Mk = Ind∆( a(v); k) for k = 1 , . . . , n. Then, by Proposition 2.3, Lemma 4.3, and the
choice of I(k), we obtain
Nk(v) = hdMk for k = 1, . . . , n.
By the construction of ∆( a(v); k) and Lemma 4.3, we know
(i) εi(Mk) = 0 for i ∈ I(k−1),
(ii) hdMk is irreducible and occurs with multiplicity one as a composi tion factor of Mk.
Therefore, by Lemma 1.8 and Proposition 1.10,
Φ( v) = hd Ind ((hdM1) ⊠ (hdM2) ⊠ · · · ⊠ (hdMn))
= hd Ind(M1 ⊠ M2 ⊠ · · · ⊠ Mn)
= hd Ind
(
∆( a(v); 1) ⊠ · · · ⊠ ∆( a(v); n)
)
,
which completes the proofs of (1) and (2).
Let Ψ λ : B(λ) → B(λ) be the canonical crystal isomorphism given by Ψ λ( ˜fibλ) = ˜fi1 for
any sequence i of elements in I. Then the following diagram commutes:
B(λ)/d95/d127
ıλ
/d15/d15
∼
Ψ λ
/d47/d47 B(λ)/d95/d127
λ
/d15/d15
B(∞) ⊗ Tλ ⊗ C
∼
Ψ ⊗id⊗id
/d47/d47 B(∞) ⊗ Tλ ⊗ C
Here, ıλ (resp. λ) is the crystal embedding (1.1) from B(λ) (resp. B(λ)) to B(∞) ⊗ Tλ ⊗ C
(resp. B(∞) ⊗ Tλ ⊗ C). Assume for v ∈ B(λ) that ιλ(v) = v′ ⊗ tλ ⊗ c for some v′ ∈ B(∞),
and recall that a(v) = a(v′). Let −1
λ be the inverse from im(λ) to B(λ). Then
Ψ λ = −1
λ ◦ (Ψ ⊗ id ⊗ id) ◦ ıλ,
which yields
Ψ λ(v) = −1
λ ◦ (Ψ ⊗ id ⊗ id) ◦ ıλ(v)
= −1
λ ◦ (Ψ ⊗ id ⊗ id)(v′ ⊗ tλ ⊗ c)
= −1
λ (hd Ind(∆( a(v′); 1) ⊠ · · · ⊠ ∆( a(v′); n)) ⊗ tλ ⊗ c)
= −1
λ (hd Ind(∆( a(v); 1) ⊠ · · · ⊠ ∆( a(v); n)) ⊗ tλ ⊗ c)
= hd Ind(∆( a(v); 1) ⊠ · · · ⊠ ∆( a(v); n)).
This proves assertion (3) and concludes the proof of the main theorem (Theorem 3.2). □
44 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
Acknowledgments
Work on this paper was facilitated by a visit by S.-J. Kang, S. -j. Oh, and E. Park to the
University of Wisconsin-Madison and by a visit by G. Benkart to the Korea Institute for
Advanced Study. We express our gratitude to these instituti ons for their hospitality.
