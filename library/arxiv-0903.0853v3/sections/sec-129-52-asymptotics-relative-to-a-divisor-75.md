---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-129-52-asymptotics-relative-to-a-divisor-75
section_title: "ASYMPTOTICS RELATIVE TO A DIVISOR 75"
section_number: 5.2
pages: 81-83
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
deﬁnition 5.2.1, one ﬁnds:
|f(z)|< 2C⏐
⏐
⏐1− z
zi,n
⏐
⏐
⏐
νi,
which allows one to conclude.
WritePi,n the polar part of f at point λiq−n:
(5.10) Pi,n(z) =
∑
0≤j<νi
αi,j,n
(z−λiq−n)j+1·
We are going to study the growth of coeﬃcients with respect toindexn whenn
goes to inﬁnity. For that, we choose some smallη∈
(
0, |q|
1+|q|
)
so that, putting
ri,n :=|λiq−n|η, all the open disks Dη
i,n :={z ∈ C| |z−λiq−n| < ri,n}
(1≤ i≤ m, n≥ N0) are pairwise disjoint. Also write Cη
i,n = ∂+Dη
i,n the
boundary of disk Dη
i,n, with positive orientation.
Lemma 5.2.4 . — LetRN :=f(z)−
N −1∑
k=0
anzn, the N -th remainder of f . For
all z∈C η
i,n, one has:
(5.11) |RN(z)|< 2C
ην
(
2A
⏐
⏐λiq−n⏐
⏐) N|q|N 2/(2ν) ,
whereC and A are the constants in relation (5.8) of deﬁnition 5.2.1.
Proof. — Since η < |q|
1+|q|, one has dq(z, [λi]) =η and dq(z, [λj])≥η forj⁄=i.
One deduces that dq(z, Λ)≥ ηmax(ν1,...,νm)≥ ην, which allows one to write,
taking ǫ := ην
2 in (5.8):
|RN(z)|< 2C
ην AN |q|N 2/(2ν) |z|N.
Relation (5.11) follows, using the fact that|z|≤ (1+η)|λiq−n|< 2|λiq−n|.
We now express the coeﬃcients αi,j,n in (5.10) with the help of Cauchy
formula in the following way:
αi,j,n = 1
2iπ
∮
Cη
i,n
f(z) (z−λiq−n)j dz,
that is, for any integer N≥ 0:
αi,j,n = 1
2iπ
∮
Cη
i,n
RN(z) (z−λiq−n)j dz.
76 CHAPTER 5. SUMMATION AND ASYMPTOTIC THEORY
Taking in account estimation (5.11) above entails:
|αi,j,n|≤ 2C ηj+1−ν ⏐
⏐λiq−n⏐
⏐j+1 X N QN 2/2,
where X := 2A|λiq−n| and Q :=|q|1/ν. Relation (5.6) implies that, if X <1,
then:
min
N ∈N
(
X N QN 2/2)
≤ Q1/8 e− ln2 X
2 ln Q,
which implies that:
|αi,j,n|≤ 2Cη j+1−ν|λi|j+1|q|1/(8ν)−(j+1)n e− ν ln2(2A|λ iq−n|)
2 ln |q| ,
so that all the sequences ( αi,j,n)n≥N0 are q-Gevrey of level (−ν). Thus, for
each pair (i,j ) of indexes, the series:
Si,j(z) :=
∑
n≥N0
αi,j,n
(z−λiq−n)j+1
converges normally on each compact subset of the sector S(Λ, 0).
Last, if 0 <|z|<R and if z /∈ ⋃
1≤i≤m
λiq−N0+N, let us put:
h(z) :=f(z)−
∑
1≤i≤m
∑
0≤j<νi
Si,j(z).
From normal convergence of the series Si,j(z) on every compact subset of
S(Λ, 0), we draw:
(5.12) h(z) =f(z)−
∑
n≥N0
∑
1≤i≤m
Pi,n(z).
Lemma 5.2.5 . — The function h represents the germ of an analytic function
at z = 0.
Proof. — Since all non zero singularities of f in the disk |z| < Rare neces-
sarily situated on the union of half q-spirals ⋃
1≤i≤m
λiq−N0+N and each Pi,n(z)
represents its polar part at each point λiq−n of the latter, the function h has
an analytic continuation to the punctured disk 0 <|z| < R. Moreover, if
Ω := ⋃
n>N0
C(0;R|q|−n) denotes the union of the circles centered at z = 0 and
with respective radii R|q|−n with n > N0, all the series Si,j(z) converge nor-
mally over Ω, and therefore remain bounded on that family of circles. Besides,
from proposition 5.1.5,f is also bounded on Ω because f∈ BΛ . It follows that
h is bounded on Ω, which entails the analyticity of h at z = 0.
