---
doc_id: arxiv-math-0108046v3
doc_title: "arXiv:math/0108046v3 [math.RT] 3 May 2002"
section_id: page-009
section_title: "Page 9"
section_number: null
pages: 9-9
source_pdf: 0108046v3.pdf
source_sha256: f47c1bd39c671cf3
toc_source: undetermined
doc_brief: "Presenting Schur algebras — Motivated by work of R.M. Green, we obtain a pre- sentation of Schur algebras (both the classical and quantized ver- sions) in terms of generators and relations."
---
PRESENTING SCHUR ALGEBRAS
9
has the advantage that upon specializing v to 1, we recover the classical
version given in Theorem 1.4.
Theorem 2.4. The algebra S(n, d) is the associative algebra (with 1)
given by generators 1λ (λ ∈Λ(n, d)), Ei, Fi (1 ≤i ≤n −1) subject to
the relations
1λ1µ = δλ,µ1λ,
X
λ∈Λ(n,d)
1λ = 1
(Q1′)
Ei1λ =
(
1λ+αiEi
if λ + αi ∈Λ(n, d)
0
otherwise
Fi1λ =
(
1λ−αiFi
if λ −αi ∈Λ(n, d)
0
otherwise
1λEi =
(
Ei1λ−αi
if λ −αi ∈Λ(n, d)
0
otherwise
1λFi =
(
Fi1λ+αi
if λ + αi ∈Λ(n, d)
0
otherwise
(Q2′)
EiFj −FjEi = δij
X
λ∈Λ(n,d)
[λj −λj+1]1λ
(Q3′)
along with the q-Serre relations (Q4), (Q5).
3. The algebra T
From now on we hold n and d ﬁxed, and set S = S(n, d).
We
deﬁne an algebra T = T(n, d) (over Q) by the generators and relations
of Theorem 1.1. Since U is the algebra on the same generators but
subject only to relations (R1)–(R5), we have a surjective quotient map
U →T (mapping generators onto generators). Eventually we shall
show that T ≃S, which will prove Theorem 1.1.
Lemma 3.1. Under the representation U →End(V ⊗d) the images of
the Hi satisfy the relations (R6) and (R7). Moreover, the relation (R7)
is the minimal polynomial of (the image of) Hi in End(V ⊗d).
Proof. Relation (R6) is trivial in the case d = 1, from which the general
case follows since each Hi acts as a derivation of V ⊗d. The relation (R7)
follows from the fact (which can be veriﬁed by induction on d) that the
eigenvalues of the diagonal operators Hi are 0, 1, . . . , d. The proof is
complete.
