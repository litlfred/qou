---
doc_id: arxiv-math-0209324v1
doc_title: "CYCLOTOMIC COMPLETIONS OF POL YNOMIAL RINGS KAZUO HABIRO"
section_id: sec-020-8-kazuo-habiro
section_title: "KAZUO HABIRO"
section_number: 8
pages: 8-10
source_pdf: 0209324v1.pdf
source_sha256: ae2ea5024a0a45e8
---
where vertical arrows are induced by the inclusion R ⊂ RI , and hence
are injective. Let ¯I denote the closure of I in RI . Since RI is ¯I-adically
complete and clearly f
¯I⇒RI g, the above-proved case implies that ρRI
(f g), (f )
is an isomorphism. Hence ρR
(f g), (f ) is injective. □
For two subsets M, M ′⊂M R, we write M ′≺ M if M ′⊂ M and for each
f∈ M there is a sequence M ′∋ f0⇒ f1⇒···⇒ fr = f in M .
Suppose that M0≺ M⊂M R. Set
F(M, M 0) ={M ′⊂ M| M0⊂ M ′, |M ′\ M0| <∞},
and
F ≺(M, M 0) ={M ′∈F (M, M 0)| M0≺ M ′}⊂F (M, M 0).
We will regardF(M, M 0) as a directed set with respect to⊂, andF ≺(M, M 0)
as a partially-ordered subset ofF(M, M 0). Note that if M ′, M ′′∈F ≺(M, M 0)
and M ′′⊂ M ′, then we have M ′′≺ M ′.
Lemma 3.3. If M0 ≺ M ⊂M R, then F ≺(M, M 0) is a coﬁnal directed
subset of F(M, M 0).
Proof. It suﬃces to show that if M ′ ∈ F(M, M 0), then there is M ′′ ∈
F ≺(M, M 0) with M ′ ⊂ M ′′. For each g ∈ M ′\ M0 choose a sequence
M0 ∋ g0 ⇒ ··· ⇒gr = g in M and set Ug ={g1, . . . , g r}. Set M ′′ =
M0∪ ⋃
g∈M ′\M0 Ug. Then we have M ′′∈F ≺(M, M 0) and M ′⊂ M ′′. □
Theorem 3.4. If R is a ring and M0≺ M⊂M R, then the homomorphism
ρR
M,M 0 : R[q]M→ R[q]M0 is injective.
Proof. By (5) and Lemma 3.3 we have
R[q]M≃ lim
←−
M ′∈F(M,M 0)
R[q]M ′
≃ lim
←−
M ′∈F ≺(M,M 0)
R[q]M ′
.
Hence it suﬃces to prove the theorem assuming that M\ M0 is ﬁnite. We
can further assume that |M\ M0| = 1. Let g∈ M\ M0 be the unique
element.
First we assume that M0 ={f1, . . . , f n} (n≥ 1) is ﬁnite. Set f = f1··· fn.
Since fi⇒ g for some i∈{ 1, . . . , n }, we have f⇒ g. By Proposition 3.2,
ρR
(f g), (f ) is injective. Since R[q]M0 = R[q](f ) and R[q]M = R[q](f g), it follows
that ρR
M,M 0 is injective.
Now assume that M0 is inﬁnite. Choose an element g0∈ M0 with g0⇒ g.
We have R[q]M0≃ lim
←−U ∈F(M0, {g0}) R[q]U and R[q]M≃ lim
←−U ∈F(M0, {g0}) R[q]U ∪{g}.
For each U∈F (M0,{g0}) we have U≺ U∪{ g}. Hence it follows from the
above-proved case that the homomorphism ρR
U ∪{g},U : R[q]U ∪{g}→ R[q]U is
injective. Since ρR
M,M 0 is the inverse limit of the ρR
U ∪{g},U for U∈F (M0,{g0}),
it is injective. □
CYCLOTOMIC COMPLETIONS OF POLYNOMIAL RINGS 9
A subset M⊂M R is said to be ⇒R-connected if M is not empty and
for each f, f ′∈ M there is a sequence f = f0⇒R f1⇒R···⇒ R fr = f ′
(r≥ 0) in M . Note that if M is⇒R-connected, then for any nonempty
subset M ′⊂ M we have M ′≺ M . The following follows immediately from
Theorem 3.4.
Corollary 3.5. If R is a ring, and M ⊂M R is a ⇒R-connected subset,
then for any nonempty subset M ′⊂ M the homomorphism ρR
M,M ′ : R[q]M→
R[q]M ′
is injective.
4. Injectivity of ρR
S,S ′
If R a ring, and S ⊂ N is a subset, then we have R[q]S = R[q]Φ S . If
S′⊂ S, then we have
ρR
S,S ′ = ρR
Φ S, Φ S′ : R[q]S→ R[q]S′
.
We will use the following well-known properties of cyclotom ic polynomi-
als.
Lemma 4.1. (1) Let n∈ N, p a prime, and e≥ 1. Then we have
(6) Φ pen(q)≡ Φ n(q)d (mod ( p)),
in Z[q], where d = deg Φ pen(q)/ deg Φ n(q). (We have d = ( p− 1)pe−1 if
(n, p ) = 1 and d = pe if p|n.)
(2) If m, n ∈ N, and n/m ∈ Q is not an integer power of a prime, then
we have (Φ n(q), Φ m(q)) = (1) in Z[q].
For m, n ∈ N, we deﬁne cm,n ∈{ 0, 1}∪{ p| prime} by
(1) cn,n = 0,
(2) cm,n = p if p is a prime and n/m = pj for some j∈ Z\{ 0}, and
(3) cm,n = 1 if n/m is not an integer power of a prime.
Note that cm,n = cn,m for all m, n ∈ N. It is straightforward to see that
m⇔R n if and only if R is ( cm,n )-adically separated.
Lemma 4.1 implies that for each m, n ∈ N we have Φ m(q)∈
√
(Φ n(q), c m,n )
in R[q], i.e., Φ m(q)
(cm,n )
⇒ R Φ n(q). It follows that if m⇔R n, then we have
Φ m(q)⇒R Φ n(q). Note also that if S⊂ N is⇔R-connected, then Φ S is
⇒R-connected. The following follows immediately from Theore m 3.4 and
Corollary 3.5.
Theorem 4.2. Let R be a ring and let S′⊂ S⊂ N. Suppose that each
connected component of the graph Γ R(S) contains at least one vertex of
Γ R(S′). (In other words, for each element n∈ S, there is a sequence S′∋
n′⇔R···⇔ R n in S.) Then the homomorphism ρR
S,S ′ is injective.
In particular, if S⊂ N is⇔R-connected, then for any nonempty subset
S′⊂ S the homomorphism ρR
S,S ′ : R[q]S→ R[q]S′
is injective. More partic-
ularly, for any nonempty subset S′⊂ N the homomorphism ρZ
N,S ′ : Z[q]N→
Z[q]S′
is injective.
