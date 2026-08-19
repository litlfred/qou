---
doc_id: arxiv-math-0209324v1
doc_title: "CYCLOTOMIC COMPLETIONS OF POL YNOMIAL RINGS KAZUO HABIRO"
section_id: sec-013-6-v-alues-at-roots-of-unity
section_title: "V alues at roots of unity"
section_number: 6
pages: 12-14
source_pdf: 0209324v1.pdf
source_sha256: ae2ea5024a0a45e8
doc_brief: "CYCLOTOMIC COMPLETIONS OF POLYNOMIAL RINGS KAZUO HABIRO — The main object of study in this paper is the completion Z[q]N = lim←− n Z[q]/ ((1− q)(1− q2)···(1− qn)) of the polynomial ring Z[q], which"
---
Theorem 6.1. Let R be a subring of the ﬁeld ¯Q of algebraic numbers,
S⊂ N a⇔R-connected subset, and T⊂ S a subset. Suppose that for some
n∈ S there are inﬁnitely many elements m∈ T with m⇔R n. Then the
homomorphism τR
S,T : R[q]S→ PT (R) is injective.
In particular, if R is a subring of the ring of algebraic integers, then, for
any subset T⊂ N containing inﬁnitely many prime powers, τR
N,T : R[q]N→
PT (R) is injective.
Proof. Suppose for contradiction that there is a nonzero element a∈ R[q]S
with τR
S,T (a) = 0. By Theorem 4.2, ρR
S, {n} is injective, and therefore we have
ρR
S, {n}(a)⁄= 0. Hence we can write ρR
S, {n}(a) = ∑ ∞
j=l ajΦ n(q)j, where l≥ 0
and aj∈ R[q] for j≥ l with al⁄∈(Φ n(q)). There are inﬁnitely many elements
m1, m 2, . . . ∈ T with mi⇔R n and n|mi. For each i, mi/n is a power of a
prime pi such that R is pi-adically separated. It follows from τR
S,T (a) = 0 that
Φ mi(q)|a in R[q]S for each i. Since R is an integral domain of characteristic
0, we can show by induction that Φ m1(q)··· Φ mk (q)|a in R[q]S for each
k≥ 0, and hence we have Φ m1(q)··· Φ mk (q)|ρR
S, {n}(a) in R[q]{n}. By (6) we
have Φ mi(q)∈ (pi, Φ n(q)) for each i. Hence we have Φ m1(q)··· Φ mk (q)∈
(p1··· pk, Φ n(q)). In other words, for each k≥ 0, ¯al = al mod (Φ n(q))∈
R[q]/ (Φ n(q)) is divisible by p1··· pk. Note that R[q]/ (Φ n(q)) = R⊕ Rq⊕
···⊕ Rqd−1 with d = deg Φ n(q), and ¯al is expressed as a polynomial in q of
degree< d , each coeﬃcient of which is divisible by p1··· pk in R for k≥ 0.
CYCLOTOMIC COMPLETIONS OF POLYNOMIAL RINGS 13
Since R is a subring of ¯Q and each pi is a non-unit in R, it follows that the
coeﬃcients of ¯al are zero. Consequently, we have al∈ (Φ n(q)). □
Proposition 6.2. Let R be a subring of ¯Q, and S⊂ N an inﬁnite subset.
Then the completion R[q]S of R[q] is not an ideal-adic completion, i.e.,
there is no ideal I in R[q] such that idR[q] induces an isomorphism R[q]S≃
lim
←−j R[q]/I j.
Proof. Let I ⊂ R[q] is a nonzero ideal, and f (q)∈ I a nonzero element.
Then there are only ﬁnitely many elements n∈ S with Φ n(q)|f (q). For each
n∈ R the power f (q)j for j≥ 1 is divisible by Φ n(q) if and only if f (q) is
divisible by Φ n(q). It follows that f (q)j does not converge to 0 as j→ 0
in R[q] with the topology deﬁning the completion R[q]S. Hence we have
R[q]S⁄≃lim
←−j R[q]/I j. □
Let R be a subring of ¯Q, and let Z⊂ Z ¯Q be a subset. Set
PZ (R) =
∏
ζ∈Z
R[ζ],
which generalize the deﬁnition of PZ (Z). If S⊂ N is a subset and Z⊂ Z
¯Q
S ,
then let
τR
S,Z : R[q]S→ PZ (R)
denote the homomorphism induced by R[q]→ PZ (R), f (q)↦→(f (ζ))ζ∈Z.
Theorem 6.3. Let R be a subring of ¯Q, and let S⊂ N and Z⊂ Z
¯Q
S be
subsets. Suppose that there is an element n∈ S such that for inﬁnitely many
ζ∈ Z we have ord ζ⇔R n. Then the homomorphism τR
S,Z : R[q]S→ PZ (R)
is injective.
In particular, if R is a subring of the ring of algebraic integers, and Z⊂
Z ¯Q is a subset containing inﬁnitely many elements of prime powe r orders,
then τR
S,Z : R[q]S→ PZ (R) is injective.
Proof. Set NZ ={ord ζ| ζ∈ Z}⊂ N. Let γ : PNZ (R)→ PZ (R) be the ho-
momorphism deﬁned by γ((fn(q))n∈NZ ) = ( fnζ (ζ))ζ∈Z. Since γ is the direct
product of the injective homomorphisms R[q]/ (Φ n(q))→ ∏
ζ∈Z, ord ζ=n R[ζ],
f (q) ↦→(f (ζ))ζ, it follows that γ is injective. We have τR
S,Z = γτ R
S,N Z ,
where τR
S,N Z : R[q]S→ PNZ (R) is injective by Theorem 6.1. Hence τR
S,Z is
injective. □
Conjecture 6.4. For any inﬁnite subset Z ⊂ Z ¯Q, the homomorphism
τZ
N,Z : Z[q]N→ PZ (Z) is injective.
If Z ′⊂ Z⊂ Z R, then we have a homomorphism
τR
Z,Z ′ : R[q]Z→ PZ (R),
induced by R[q]→ PZ (R), f (q)↦→(f (ζ))ζ.
