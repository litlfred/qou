---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-140-52-asymptotics-relative-to-a-divisor-81
section_title: "ASYMPTOTICS RELATIVE TO A DIVISOR 81"
section_number: 5.2
pages: 87-89
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
The function u can be analytically continuated at λq−n, because θλ has a
simple zero at each point of the q-spiral [λ]; formula (5.23) comes by diﬀeren-
tiating (ℓ +k) times the equality g(z) =u(z)(z−λq−n)k, while (5.24) follows
from a direct evaluation using Jacobi’s triple product form ula (1.2).
We now come to the proof of the direct implication; that is, we assume
condition (ii) of theorem 5.2.2. Since θΛh∈ EΛ
0 , by linearity, we just have to
check that the series S(z) deﬁned by relation (5.16) satisﬁes θΛS∈ EΛ
0 . To
that end, put T (z) := θΛ (z) S(z) for all t∈ C∗\λq−N; this clearly has an
analytic continuation to C∗. On the other hand, T (ℓ)(λi′q−n) = 0 for alli′⁄=i,
ℓ<ν i′ and n∈ Z.
In order to evaluate T (ℓ)(λq−n), put Λ ′ := Λ− (j + 1)[λ] and:
T0(z) :=
∑
n≥0
αn
(θλ(z))j+1
(z−λq−n)j+1 ;
one has T (z) = θΛ ′(z) T0(z), where T0 is analytic on C∗. First note that, if
ℓ<ν i−j− 1, one has T (ℓ)(λq−n) = 0 for all n∈ N; when νi−j− 1≤ℓ<ν i,
using relation (5.23), we get:
T (ℓ)(λq−n) =αn
ℓ−νi+j+1∑
k=0
(ℓ
k
)
θ(ℓ−k)
Λ ′ (λq−n) (k +j + 1)!
(j + 1)! g(k+j+1)(λq−n),
where n∈ N, g = (θλ)j+1. Taking in account assertions (1) and (2) of lemma
5.2.9, the sequences ( θ(ℓ−k)
Λ ′ (λq−n))n≥0 and (g(k+j+1)(λq−n))n≥0 respectively
haveq-Gevrey order (ν−j−1) and (j +1), which implies that (T (ℓ)(λq−n))n≥0
is bounded above by a geometric sequence, for ( αn)n≥0 has q-Gevrey order
(−ν).
Moreover, likeθΛ , the function T hasq-exponential growth of order ν at 0.
Indeed, let a∈ (1,|q|) and put δ := min
|z|=a
dq(z, [1]); one has δ >0, so that:
(5.25) max
|z|=a|λq−k|
|S(z)|≤ 1
δ |λ|
∑
n≥0
|αnqn|<∞.
This shows that S(z) stays uniformly bounded over the family of circles
centered at 0 and such that each one goes through a point of the q-spiral
with basis aλ. It follows ﬁrst that the restriction of function T to the circles
has q-exponential growth of order ν at 0; then that function T itself has such
growth. To summarize, we see that T∈ EΛ
0 , whence F∈ EΛ
0 .
82 CHAPTER 5. SUMMATION AND ASYMPTOTIC THEORY
Proof of F∈ EΛ
0⇒f∈ AΛ
q :
It will rest on lemma 5.2.10, which gives a mi-
noration on θ as in lemma 5.1.6.
Lemma 5.2.10 . — Leta> 0 and k∈ Z. Then:
(5.26) min
|z|=a|q|−k
|θ(z)|≥
⏐
⏐(q−1;q−1)∞
⏐
⏐
(|q|−1 ;|q|−1)∞
|θ(−a;|q|)| a−k |q|k(k−1)/2.
Proof. — Let z∈ C be such that |z| = a|q|−k. From a minoration of each
factor of the triple product formula (1.2), we get:
min
|z|=a|q|−k
|θ(z)| ≥
⏐
⏐(q−1;q−1)∞
⏐
⏐∏
n≥0
⏐
⏐
⏐1−a|q|−n−k
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐1−|q|−n−1
a|q|−k
⏐
⏐
⏐
⏐
⏐
=
⏐
⏐(q−1;q−1)∞
⏐
⏐
(|q|−1 ;|q|−1)∞
⏐
⏐
⏐θ(−a|q|−k ;|q|)
⏐
⏐
⏐,
yielding relation (5.26).
Now we assume F ∈ EΛ
0 . We put f := F
θΛ
and keep the notations R, N0
introduced at the beginning of the proof of the theorem (page 74); also, we
choose a∈ (|λm|,R ). According to relation (5.26), there is C >0 and µ >0
such that, if |z| = aq−k and k ≥ N0, then |f(z)| ≤C|z|µ; that is, f has
moderate growth at 0 on the circles |z| =a|q|−k, k≥N0.
Partial fraction decomposition of f at each point of Λ contained in the
punctured disk 0 <|z| < R, will produce an expression of the form (5.9), in
which the coeﬃcients αi,j,n haveq-Gevrey order (−ν). Indeed, let:
Fi,k,n := F (k)(λiq−n)
k! , Θi,k,n := θk+νi
Λ (λiq−n)
(k +νi)! ;
then:
αi,νi−1,n = Fi,0,n
Θi,0,n
, α i,νi−2,n = Fi,1,n−αi,νi−1,n Θi,1,n
Θi,0,n
, ...,
αi,0,n = Fi,νi−1,n−∑ νi−1
k=1 αi,νi−k,n Θi,νi−k,n
Θi,0,n
·
According to relation (5.24), one ﬁnds:
Θi,0,n = (q−1;q−1)3νi
∞ (−λiq−n)−νi θΛ ′
i
(λi)
m∏
j=1
(
−λj
λi
) nνj
qνn(n−1)/2.
Since ( Fi,0,n)n≥N0 has q-Gevrey order 0, it follows that the sequence
(αi,νi−1,n)n≥N0 has q-Gevrey order ( −ν). As for the other coeﬃcients
5.3. q-GEVREY THEOREM OF BOREL-RITT AND FLAT FUNCTIONS 83
αi,j,n, 0≤j <νi− 1, since the sequences (Θ i,j,n)n≥N0 all haveq-Gevrey order
ν (see lemma 5.2.9), one successively shows that the sequences (αi,νi−2,n)n≥N0,
... , (αi,0,n)n≥N0 all have q-Gevrey order (−ν).
Last, note that after (5.25), the function P deﬁned by:
P (z) :=
∑
n≥N0
∑
1≤i≤m
∑
0≤j<νi
αi,j,n
(z−λiq−n)j+1
is uniformly bounded over the family of circles |z| = a|q|−k, k∈ Z if a /∈⋃
1≤i≤m
[λi]. Since f ∈ BΛ , from proposition 5.1.5 we deduce that h(z) :=
f(z)−P (z) is analytic in some open disk 0 <|z| < Rand remains bounded
over these circles, which implies that h is holomorphic in a neighborhood of 0,
achieving the proof of the converse implication and of theor em 5.2.2.
5.3. q-Gevrey theorem of Borel-Ritt and ﬂat functions
The classical theorem of Borel-Ritt [ 26, chap. XI, §1] says that any formal
power series is the asymptotic expansion, in Poincar´ e’s sense, of some germ of
analytical function in a sector of the complex plane with ver tex 0 (the Gevrey
version for diﬀerential equations is to be found in §2 of the same chapter of
loc. cit. ). We are going to prove a q-Gevrey version of that theorem involving
the set of functions AΛ
q and then give a characterization of the corresponding
ﬂat functions.
