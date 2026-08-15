---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS"
section_id: sec-130-52-asymptotics-relative-to-a-divisor-77
section_title: "ASYMPTOTICS RELATIVE TO A DIVISOR 77"
section_number: 5.2
pages: 83-85
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symm"
---
Combining relations (5.10) and (5.12), we get decompositio n (5.9) of f,
thus achieving the proof of (i) ⇒ (ii).
Proof of (ii) ⇒ (i): It will rest on lemma 5.2.6.
Lemma 5.2.6 . — Let j∈ N, N ∈ N and write Rj,N the rational fraction
deﬁned by relation:
(5.13) 1
(1−t)j+1 =
N −1∑
n=0
(n +j
n
)
tn +Rj,N(t).
Letδ >0. If t∈ C satisﬁes|1−t|≥ δ, then:
(5.14) |Rj,N(t)|<C δ,r
j,N
|t|N
δj+1, C δ,r
j,N = 1
2−r
(1 +rδ
r− 1
) j (1 +rδ
1 +δ
) N
for all r∈ (1, 2).
Proof. — The relation (5.14) being trivially satisﬁed at point t = 0, we
assume that t ⁄= 0. Taking the j-th derivative for each side of relation
1
1−t =
N +j−1∑
n=0
tn + tN +j
1−t, one ﬁnds:
Rj,N(t) = 1
j!
(tN +j
1−t
) (j) = 1
2iπ
∮
C(t,ρ)
sN +j
1−s
ds
(s−t)j+1 ,
whereC(t,ρ ) denotes the positively oriented boundary of the circle cen tered
at s =t and with radius ρ|t|, with ρ<
⏐
⏐
⏐
⏐1− 1
t
⏐
⏐
⏐
⏐. One deduces that:
(5.15) |Rj,N(t)|≤ (1 +ρ)N +j |t|N
(
|1−t|− ρ|t|
)
ρj,
where ρ denotes a real number located between 0 and
⏐
⏐
⏐
⏐1− 1
t
⏐
⏐
⏐
⏐.
If|1−t|>δ , witht = 1+Reiα (α∈ R), one gets:
⏐
⏐
⏐
⏐1− 1
t
⏐
⏐
⏐
⏐≥ R
1 +R > δ
1 +δ .
Choose ρ := r′δ
1 +δ with r′∈ (0, 1), so that |1−t|− ρ|t|≥| 1−t| (1−r′) >
(1−r′) δ; relation (5.14) follows at once (along with lemma 5.2.6) wi th the
help of (5.15), with ρ := (r− 1) δ
1 +δ and r :=r′ + 1∈ (1, 2).
78 CHAPTER 5. SUMMATION AND ASYMPTOTIC THEORY
We shall now use lemma 5.2.6 to prove that (ii)⇒ (i); by linearity, it suﬃces
to check that a series of the form:
(5.16) S(z) :=
∑
n≥0
αn
(z−λq−n)j+1
deﬁnes a function in space AΛ
q , where λ = λi for some i ∈ {1, 2,...,m },
0≤j <νi and where (αn) denotes a q-Gevrey sequence of order (−ν): there
are C, A> 0 such that:
(5.17) ∀n∈ N ,|αn|≤ CA n|q|−νn(n−1)/2.
Let z ∈ C∗ such that dq(z, Λ) > ǫ; we have dq(z, [λ])νi > ǫ, hence⏐
⏐
⏐
⏐1− z
λq−n
⏐
⏐
⏐
⏐> ν i
√
ǫ. Let N ∈ N and apply to each term of the series S(z)
formula (5.13) with t = z
λq−n to obtain formally S(z) = SN(z) + RN(z),
where one puts:
SN(z) :=
∑
n≥0
N −1∑
k=0
αn
(k +j
k
)
(−λq−n)−j−1
( z
λq−n
) k
and:
RN(z) :=
∑
n≥0
αn (−λq−n)−j−1Rj,N( z
λq−n ).
Since (αn) has q-Gevrey decay of order ν (see (5.17)), we see that SN(z)
and RN(z) are normally convergent series on any domain Ω such that
inf
z∈Ω
dq(z, [λ])> 0.
Deﬁne:
(5.18) A(z) :=
∑
n≥0
αn zn, ˜A(z) :=
∑
n≥0
|αn| zn.
From relation (5.17), one gets:
|A(z)|≤ ˜A(|z|)≤C
∑
n≥0
|q|−νn(n−1)/2 |Az|n<C e(Az;|q|ν).
On the other hand, one can express the series SN(z) in the following way:
(5.19) SN(z) =
N −1∑
n=0
anzn, a n := (−λ)−j−1
(n +j
n
)
A(qj+1+n) λ−n ;
besides, the relation (5.14) implies that, putting δ := ν i
√
ǫ:
(5.20) |RN(z)|≤ K δ,r
j,N |z|N, K δ,r
j,N :=
C δ,r
j,N
|λ|j+1+N δj+1
˜A(|q|j+1+N) ,
