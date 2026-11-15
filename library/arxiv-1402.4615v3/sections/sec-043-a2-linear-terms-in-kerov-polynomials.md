---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-043-a2-linear-terms-in-kerov-polynomials
section_title: "A.2. Linear terms in Kerov polynomials"
section_number: null
pages: 60-62
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
top degree part of the coefﬁcients of linear terms in Kerov polynomials. This proves
a conjecture of Lassalle [Las09, page 31].
Proposition A.2. For any integers k > 0 and k −1 ≥i ≥0, we have
[Rk+1−i]K(k) =

k
k −i

γi + lower degree terms,
where

k
k −i

denotes the positive Stirling number of the ﬁrst kind.
Proof. We recall that
Chµ(λ) =
X
ρ
aµ
ρMρ(λ).
Thanks to the relation between moments and free cumulants – see Section 2.2 – it
is enough to prove that
a(k)
(k+1−i) =

k
k −i

γi + lower degree terms
for any positive integers k > 0 and k −1 ≥i ≥0. We will prove it by induction
over k. For k = 1 we have that K(1) = M2 = R2 and the inductive assertion holds
in this case.
Putting µ = (k) in Equation (B) we have that
X
ρ
a(k)
ρ



X
g,h≥0,
π⊢h
bρ
g,π(γ)Mπ∪(g+1)


= kLk−1,
LARGE DIAGRAMS AND STRUCTURE CONSTANTS
61
hence
X
ρ
a(k)
ρ bρ
k−1−i,0(γ) = ka(k−1)
(k−i)
for any integer 0 ≤i ≤k −1. From Lemma 3.6, bρ
k−1−i,0 vanishes for |ρ| <
k + 1 −i. Moreover, by Proposition 3.7 and by Lemma 3.9, we have that
degγ(a(k)
ρ bρ
k−1−i,0(γ)) ≤k +1−|ρ|+|ρ|−2ℓ(ρ)−(k −3−i) = i−2(ℓ(ρ)−1),
By inductive hypothesis one has
(55)
X
k+1≥r≥k+1−i
a(k)
(r)b(r)
k−1−i,0(γ) = k

k −1
k −1 −i

γi + lower degree terms
for any integer 0 ≤i ≤k −1. From Proposition 3.1 we know that
b(r)
k−1−i,0(γ) =

r −1
r −(k −i)

(−γ)r −(k −i + 1).
Putting it into Equation (55) we obtain that in order to ﬁnish the proof it is enough
to prove the following identity (set r = k + 1 −i + j in the summation index)
X
0≤j≤i
k −i + j
j + 1

(−1)j

k
k −i + j

= k

k −1
k −1 −i

for any integer 0 ≤i ≤k −1.
The following proof has been communicated to us by Goulden. It uses the fact
(see, e.g., [GJ04], Ex. 3.3.17) that Stirling numbers of the ﬁrst kind are deﬁned by
X
j≥0

k
j

xj = (x)(k),
k ≥0,
62
M. DOŁ ˛EGA AND V. FÉRAY
using the notation for rising factorials (a)(m) = a(a+1) · · · (a+m−1) for positive
integer m, and (a)(0) = 1. Thus we have
X
0≤j≤i
k −i + j
j + 1

(−1)j

k
k −i + j

= −
X
−1≤j≤i
k −i + j
k −i −1

(−1)j+1

k
k −i + j

+

k
k −i −1

= −
X
−1≤j≤i
[xk−i−1](x −1)k−i+j

k
k −i + j

+ [xk−i−1](x)(k)
= −[xk−i−1]

X
j≥0

k
j

(x −1)j −
X
0≤j≤k−i−2

k
j

(x −1)j

+ [xk−i−1](x)(k)
= −[xk−i−1](x −1)(k) + [xk−i−1](x)(k)
= [xk−i−1](x)(k−1)n
−(x −1) + (x + k −1)
o
= k

k −1
k −i −1

,
for all 0 ≤i ≤k −1, establishing the required identity.
□
