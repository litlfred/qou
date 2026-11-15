---
doc_id: arxiv-math-0108046v3
doc_title: "arXiv:math/0108046v3 [math.RT] 3 May 2002"
section_id: page-011
section_title: "Page 11"
section_number: null
pages: 11-11
source_pdf: 0108046v3.pdf
source_sha256: f47c1bd39c671cf3
toc_source: undetermined
doc_brief: "Presenting Schur algebras — Motivated by work of R.M. Green, we obtain a pre- sentation of Schur algebras (both the classical and quantized ver- sions) in terms of generators and relations."
---
PRESENTING SCHUR ALGEBRAS
11
(b) The set {1λ | λ ∈Λ(n, d)} is a Q-basis for T 0 and a Z-basis for
T 0
Z; moreover, this set is a set of pairwise orthogonal idempotents which
add up to 1.
(c) HB = 0 for any B ∈Nn such that |B| > d.
Proof. Consider ﬁrst the algebra eT ′ deﬁned to be the quotient of U0
by the ideal generated only by the elements Hi(Hi −1) · · ·(Hi −d)
(1 ≤i ≤n). Since each of the relations in eT ′ is a polynomial in just
one of the variables, we have the factorization
eT ′ ∼= Q[H1]/(p(H1)) ⊗· · · ⊗Q[Hn]/(p(Hn))
where p(X) = X(X −1) · · ·(X −d). By the Chinese Remainder The-
orem applied to each tensor factor we obtain from the above isomor-
phisms (products denote direct products)
eT ′ ∼=
d
Y
i=0
(Q[H1]/(H1 −i)) ⊗· · · ⊗
d
Y
i=0
(Q[Hn]/(Hn −i))
and by rearranging the order of factors we obtain
∼=
Y
0≤µ1,... ,µn≤d
(Q[H1]/(H1 −µ1) ⊗· · · ⊗Q[Hn]/(Hn −µn))
∼=
Y
0≤µ1,... ,µn≤d
Q[H1, . . . , Hn]/(H1 −µ1, . . . , Hn −µn).
The isomorphism is realized by the map which sends a polynomial
f(H1, . . . , Hn) in eT ′ to the element (f(µ1, . . . , µn))0≤µ1,... ,µn≤d of the
direct product. Since T ′ is isomorphic with eT ′/(H1 + · · ·+ Hn −d), we
deduce from the above that
T ′ ∼=
Y
µ∈Λ(n,d)
Q[H1, . . . , Hn]/(H1 −µ1, . . . , Hn −µn)
and this isomorphism (which we denote by φ) is realized by the map
sending f(H1, . . . , Hn) to the element (f(µ1, . . . , µn))µ∈Λ(n,d).
Thus, given any λ ∈Λ(n, d), we have
φ(1λ) =
 µ1
λ1

· · ·
µn
λn
 
µ∈Λ(n,d)
= (δλµ)µ∈Λ(n,d)
Since the vector on the right of the above equality consists of zeros and
ones, with precisely one nonzero entry, and since φ is an isomorphism,
it follows that the various 1λ are orthogonal idempotents which add up
to the identity of T ′.
