---
doc_id: arxiv-2401.04019v1
doc_title: "TRUNCA TED THET A SERIES RELA TED TO THE JACOBI TRIPLE PRODUCT IDENTITY"
section_id: sec-007-5-combinatorial-proof-of-an-identity-related-to
section_title: "Combinatorial proof of an identity related to the Jacobi Triple Product"
section_number: 5
pages: 13-16
source_pdf: 2401.04019v1.pdf
source_sha256: 1a29e52a81639640
doc_brief: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY — The work of Andrews and Merca on the truncated Euler’s pen- tagonal number theorem led to a resurgence in research on tru ncated"
---
Product
In this section we give both analytic and combinatorial proofs of an id entity
which includes as particular cases the conjectural identities (6.7), (6.10), (6.12),
(6.13) in [14].
14 CRISTINA BALLANTINE AND BROOKE FEIGON
First, we recall the Jacobi Triple Product identity in its general for m. See, for
example, [12] where a combinatorial proof is provided. For integers m and s such
that 0 <s<m , and complex numbers q and z with |q|< 1 and z ⁄= 0, we have
(18) ( zq s,z −1qm−s,q m;qm)∞ =
∞∑
i=−∞
(−z)iqm(i2−i)/2+si.
Theorem 5.1. Letm,s be positive integers such that m ≥ 2 and 0<s<m . Then,
(19) (qs,q 2m−s,q 2m;q2m)∞(q2m−2s,q 2m+2s;q4m)∞
(qs,q m−s;qm)∞
=
∞∑
n=−∞
qn(mn+s).
Corollary 5.2. If m = 5, then for s = 1, 2, 3, 4, we obtain the respective identities
(6.7), (6.10), (6.12), (6.13) in [14].
Remark 3. In [13], the authors point out that identities (6.7), (6.10), (6.12), ( 6.13)
in [14] follow from the Jacobi Triple Product identity.
Analytic proof. Since
(qs;qm)∞ = (qs;q2m)∞(qm+s;q2m)∞
(q2m+2s;q4m)∞ = (qm+s;q2m)∞(−qm+s;q2m)∞,
to prove identity (19), we need to show that
(−qm+s;q2m)∞(−qm−s;q2m)∞(q2m;q2m)∞ =
∞∑
n=−∞
qn(mn+s),(20)
which is precisely (18) with q replaced by q2 and z replaced by −qm−s. □
Combinatorial proof. To simplify the exposition, we ﬁrst deﬁne a sign reversing
involution to prove combinatorially the trivial cancellation
(q;q)∞
(q;q)∞
= 1.
We say that an involution deﬁned on a set of pairs (or tuples) of part itions is sign
reversing, if the involution changes the parity of the length of the ﬁ rst partition in
each pair (or tuple). Let QP(n) be the set of pairs of partitions ( λ,µ ) ⊢n withλ a
distinct partition and µ an unrestricted partition. The map F : QP(n) \ {(∅, ∅)} →
QP(n) \ {(∅, ∅)} deﬁned by
F (λ,µ ) =
{
(λ ∪ (µ1),µ \ (µ1)) if λ1 <µ 1
(λ \ (λ1),µ ∪ (λ1)) if λ1 ≥µ1
is a sign reversing involution. Recall that, following our convention, if ν = ∅, then
ν1 = 0. Since ( q;q)∞/(q;q)∞ is the generating function for
qpe−o(n) := |{(λ,µ ) ∈ QP (n),ℓ (λ) even }| − |{(λ,µ ) ∈ QP (n),ℓ (λ) odd }|,
this completes the argument.
We continue with the combinatorial proof of Theorem 5.1.
If m = 2, then (19) becomes
(21) (q,q 3,q 4;q4)∞(q2,q 6;q8)∞
(q;q2)2
∞
=
∞∑
n=−∞
qn(2n+1).
TRUNCATED THETA SERIES RELATED TO THE JTP IDENTITY 15
Using the transformation F above on pairs of partitions with odd parts, we have
that (21) is equivalent to
(22) (q2;q2)∞
(q;q2)∞
=
∞∑
n=0
qn(n+1)/2.
This is Gauss’s identity [2, Identity (1.3)] with q replaced by −q. However, since
ℓo(λ) ≡ |λ| mod 2, Andrews’ combinatorial proof of Gauss’ identity given in [2]
also proves (21) combinatorially.
For the remainder of the proof let m ≥ 3.
Denote by A(n) the set consisting of pairs of partitions ( λ,µ ) ⊢n such that
• λ is a partition with distinct parts congruent to 0, s or −s modulo 2m or
congruent to 2m + 2s or 2m − 2s modulo 4m;
• µ is a partition with parts congruent to s or −s modulo m. (Thus, µ has
parts congruent to s,m +s, −s or m −s modulo 2m.)
Deﬁne
Ae(n) := {(λ,µ ) ∈ A(n) |ℓ(λ) even }
and
Ao(n) := {(λ,µ ) ∈ A(n) |ℓ(λ) odd }.
The left hand side of (19) is the generating function for the sequen ceae−o(n) :=
|Ae(n)| − |Ao(n)|.
We deﬁne a sign reversing involution ϕ on a subset of A(n).
If (λ,µ ) ∈ A(n), we write
λ =λ0,2m ∪λ±s,2m ∪λ±(2m+2s),4m, µ =µ±s,2m ∪µ±(m+s),2m
and we consider several cases.
Case 1:
λ±s,2m ∪ µ±s,2m ⁄= ∅ (i.e., there is at least one part congruent to ±s
(mod 2m) in λ or in µ). Deﬁne ϕ(λ,µ ) := F (λ,µ ).
Hence,ϕ is a sign reversing involution on the subset of pairs ( λ,µ ) in A(n) with
λ±s,2m ∪µ±s,2m ⁄= ∅.
Case 2: λ±s,2m ∪µ±s,2m = ∅ and (λ±(2m+2s),4m ⁄= ∅ orµ±(m+s),2m has at least one
repeated part). In this case the involution is similar to that of [11]. Le t a be the
largest part in λ±(2m+2s),4m andb be the largest repeated part in µ±(m+s),2m (with
a = 0 or b = 0 if no such part exists).
(i) If a < 2b, remove two parts equal to b from µ±(m+s),2m and insert a part
equal to 2b intoλ±(2m+2s),4m, i.e.,
ϕ(λ,µ ) := (λ ∪ (2b),µ \ (b,b )).
(i) If a ≥ 2b, remove part a fromλ±(2m+2s),4m and insert two parts equal to a/2
intoµ±(m+s),2m, i.e.,
ϕ(λ,µ ) := (λ \ (a),µ ∪ (a/2,a/ 2)).
Again, ϕ is a sign reversing involution on the subset of pairs in A(n) satisfying
λ±s,2m ∪µ±s,2m = ∅ and (λ±(2m+2s),4m ⁄= ∅ orµ±(m+s),2m has at least one repeated
part).
Case 3:
λ±s,2m = µ±s,2m = λ±(2m+2s),4m = ∅ and µ±(m+s),2m is a partition with
distinct parts. Note that in this case λ = λ0,2m and µ = µ±(m+s),2m. Thus, to
complete the proof, we need a combinatorial proof of (20). Of cou rse, using 2m in
16 CRISTINA BALLANTINE AND BROOKE FEIGON
place of m and z = −qm in the proof of [12] also provides a combinatorial proof of
(20). However, the proof provided below is simpler.
We denote by C(n) the subset of pairs ( λ,µ ) ∈ A(n) satisfying the conditions of
Case 3. We deﬁne a sign reversing involution on the set
C∗(n) = C(n) \
(
{(∅,δ m−s,2m,k) |k ≥ 0} ∪ {(∅,δ m+s,2m,|k|) |k< 0}
)
.
Now we use a particular case of [8, Lemma 2.1]. Following the notation in [ 8] we
denote by Q2m,m−s(n) the set of distinct partitions of n with all parts congruent to
m ±s (mod 2m) and by W2m,m−s(n) the set of pairs ( ν,k (mk −s)), where ν is a
partition into parts divisible by 2 m,k ∈ Z, and |ν| +k(mk −s) = n. Then, the map
ξ2m,m−s : Q2m,m−s(n) → W 2m,m−s(n) deﬁned in [8, Lemma 2.1] is a bijection.
Let D(n) be the set of triples ( λ,ν,k (mk −s)), where λ andν have parts divisible
by 2m, λ has distinct parts, k ∈ Z, and |λ| + |µ| +k(mk −s) = n. The map
ζ : C(n) → D (n) deﬁned by ζ(λ,µ ) = (λ,ξ 2m,m−s(µ)) is a bijection.
We deﬁne a sign reversing involutionψ on D(n)\(∅, ∅,k (mk−s)). Let (λ,ν,k (mk−
s)) ∈ D (n) with λ ∪ν ⁄= ∅ and deﬁne ψ(λ,ν,k (mk −s)) = ( F (λ,ν ),k (mk −s)).
Then the proof of [8, Lemma 2.1] shows that the map ϕ(λ,µ ) := ζ−1 ◦ψ ◦ζ(λ,µ )
is a sign reversing involution on C∗(n).
Hence, the left hand side of (19) is the generating function for |C(n) \ C ∗(n)|.
This completes the combinatorial proof of Theorem 5.1. □
The combinatorial proof of Theorem 5.1 above also gives a combinato rial proof
of [13, Theorem 38].
Theorem 5.3 ([13], Theorem 38) . Let a be 1 or 3. Furthermore, let (an)n≥0 be
the sequence of non-negative integers j such that 16j +a2 is a square. Then
(23)
∞∑
n=0
qan = (q8;q8)∞(−q4+a;q8)∞(−q4−a;q8)∞.
Combinatorial Proof. First note that, if a ∈ {1, 3}, then 16j +a2 is a square if and
only if j = k(4k −a) for some k ∈ Z. Then, Case 3 in the proof of Theorem 5.1
with m = 4 and s =a proves the theorem. □
