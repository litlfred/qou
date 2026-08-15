---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS"
section_id: sec-157-54-relative-divisors-and-multisummable-functions
section_title: "RELATIVE DIVISORS AND MULTISUMMABLE FUNCTIONS 91"
section_number: 5.4
pages: 97-99
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symm"
---
Fori from 1 to m + 1, put
Λ≥i :=
∑
j≥i
Λj
and Λ≤i :=
∑
j≤i
Λj.
Also, we will write Λ ≥m+1 = Λ≤0 = O, where O stands for the null divisor,
and Λ ≥0 = Λ ≤m = Λ. For short, we shall call (Λ 1, Λ2,..., Λm) an ordered
partition of Λ.
Theorem 5.4.3. — Let (Λ1, Λ2,..., Λm) be an ordered partition of Λ and
deﬁne EΛ
(Λ 1,Λ 2,...,Λ m) as the set of functions that are analytic in a punctured
neighborhood of 0, have q-Gevrey order|Λ| at 0 and, for i from 1 tom, having
q-Gevrey order|Λ≥i+1| over Λ≥i/Λ≥i+1 at 0. Then, one has:
EΛ
(Λ 1,Λ 2,...,Λ m) = EΛ m
0 +θΛ ≥mEΛ m−1
0 +··· +θΛ ≥2EΛ 1
0 .
In other words, writing OΛ
(Λ 1,Λ 2,...,Λ m) :=
( 1
θΛ
EΛ
(Λ 1,Λ 2,...,Λ m)
)
∩ BΛ , one has:
OΛ
(Λ 1,Λ 2,...,Λ m) = AΛ 1
q + 1
θΛ ≤1
AΛ 2
q +··· + 1
θΛ ≤m−1
AΛ m
q ·
Proof. — One proceeds by induction on the lengthm of the partition of divisor
Λ: the cass m = 1 is theorem 5.2.8 while the case m = 2 is dealt with in
proposition 5.4.2. The other cases follow directly from the next lemma.
Lemma 5.4.4 . — Letm≥ 2. Then:
EΛ
(Λ 1,Λ 2,...,Λ m) = EΛ m
0 +θΛ mE
Λ ≤m−1
(Λ 1,Λ 2,...,Λ m−1) .
Proof. — Let F ∈ EΛ
(Λ 1,Λ 2,...,Λ m). As in equation (5.36) in the course of the
proof of proposition 5.4.2, one considers the Taylor expans ion of F along the
divisor Λm, thereby ﬁnding that F∈ EΛ m
0 +θΛ mE
Λ ≤m−1
(Λ 1,Λ 2,...,Λ m−1).
Deﬁnition 5.4.5 . — We call OΛ
(Λ 1,Λ 2,...,Λ m) the set of multisummable func-
tions at 0 with respect to partition (Λ1, Λ2,..., Λm) of divisor Λ.
By convention, we will set OO
(O) := C{z}, the ring of all germs of analytic
functions at z = 0.
Proposition 5.4.6. — The sets EΛ
(Λ 1,Λ 2,...,Λ m) and OΛ
(Λ 1,Λ 2,...,Λ m) have a
structure of module over C{z} and are stable under the q-diﬀerence operator
σq.
92 CHAPTER 5. SUMMATION AND ASYMPTOTIC THEORY
Proof. — Immediate.
Ifm≥ 2, an element f∈ OΛ
(Λ 1,Λ 2,...,Λ m) generally has no asymptotic expan-
sion in the sense of deﬁnition 5.2.1. Nonetheless, accordin g to theorem 5.4.3,
there exists a f1∈ AΛ 1
q such thatf(z)−f1(z) =O
( 1
θΛ 1(z)
)
asz→ 0 outside
of Λ, which allows one to prove the following.
Theorem 5.4.7. — To each f ∈ OΛ
(Λ 1,Λ 2,...,Λ m) there corresponds a unique
power series ˆf = ∑
n≥0
an zn∈ C[[z]]q;1/|Λ 1| satisfying the following property:
for all R >0 near enough 0, there are constants C, A >0 such that, for all
ǫ> 0 and all z∈S(Λ,ǫ ;R):
(5.37)
⏐
⏐
⏐
⏐
⏐f(z)−
n−1∑
ℓ=0
aℓ zℓ
⏐
⏐
⏐
⏐
⏐< C
ǫ An |q|n2/(2|Λ 1|) |z|n .
Proof. — Applying theorem 5.4.3 to the function f, one gets:
f =f1 + f2
θΛ 1
+··· + fm
θΛ ≤m−1
,
wherefi∈ AΛ i
q for all indexesi from 1 tom. Choose R> 0 in such a way that
the fi θΛ i have an analytic continuation to the punctured disk 0 <|z|< 2R;
from the deﬁnition of each space AΛ i
q , one has:
dq(z, Λi)>ǫ =⇒|fi(z)|< Ci
ǫ
for all z such that 0 <|z| < R, where Ci is some positive constant. On the
other hand, from lemma 5.1.6 and relation (5.35), one has, fo r any divisor
Λ′ = Λ1,..., Λ≤m−1:
dq(z, Λ′)>ǫ =⇒
⏐
⏐
⏐
⏐
1
θΛ ′(z)
⏐
⏐
⏐
⏐< C ′
ǫ A′n |q|n2/(2|Λ ′|) |z|n
for all integersn≥ 0, whereC ′ andA′ are positive constants depending only on
the divisor Λ ′. Noting that dq(z, Λ)≤dq(z, Λi) dq(z, Λ≤i−1) for i = 2,...,m ,
one gets that, for all integers n≥ 0:
(5.38) dq(z, Λ>ǫ =⇒|f(z)−f1(z)|< C1
ǫ A1n |q|n2/(2|Λ 1|) |z|n
as long as 0 <|z|<R .
Relation (5.38) implies that both f andf1 have ˆf as an asymptotic expan-
sion in the classical sense (Poincar´ e) at 0, outside of divi sor Λ. Since f1 is
asymptotic to ˆf in the frame of space AΛ 1
q , one has ˆf ∈ C[[z]]q;1/|Λ 1|. The
