---
doc_id: arxiv-math-0501112v3
doc_title: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF"
section_id: sec-030-16-piotr-sniady
section_title: "PIOTR ´SNIADY"
section_number: 16
pages: 16-18
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
doc_brief: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
and with an explicit (but involved) covariance of free cumul ants. The ap-
propriate disjoint covariance is given by
lim
q →∞
Cov•
ρ ′q
(Σ l1 , Σ l2 )q− l1 +l2
2 =
(p(1))
l1 +l2
2 lim
q →∞
Cov•
ρ (1)
q
(Σ l1 , Σ l2 )q− l1 +l2
2 +
(p(2))
l1 +l2
2 lim
q →∞
Cov•
ρ (2)
q
(Σ l1 , Σ l2 )q− l1 +l2
2 .
Proof. By deﬁnition,
ρ ′
q =
(
ρ(1)
r(1)
q
× ρ(2)
r(2)
q
) ↑
Sq
S
r(1)
q
×S
r(2)
q
and we can use the Frobenius reciprocity between the inducti on and re-
striction of representations. It follows that the correspo nding normalized
characters fulﬁll for all l1, . . . , l n ≥ 1
χ ρ ′(Σ l1 •· · ·•Σ ln ) =
(
χ ρ (1) ⊗χ ρ (2)
)(
(Σ l1 ⊗1+1⊗Σ l1 )•· · ·•(Σ ln ⊗1+1⊗Σ ln )
)
.
We can treat the left-hand side as a mixed momentE(Σ l1 • · · · • Σ ln ) in the
algebra of conjugacy classes equipped with the disjoint product; analogous
interpretation is possible also for the right-hand side. Si nce equality holds
for all l1, . . . , l n ≥ 2 it follows that the joint distributions of the family
of random variables (Σ i)i≥2 coincides with the joint distribution of random
variables (Σ i ⊗ 1 + 1 ⊗ Σ i)i≥2; in particular their cumulants are equal:
(3.14)
k•
ρ ′(Σ l1 , . . . , Σ ln ) = k•
ρ (1)⊗ρ (2) (Σ l1 ⊗1+1⊗Σ l1 , . . . , Σ ln ⊗1+1⊗Σ ln ) =
k•
ρ (1) (Σ l1 , . . . , Σ ln ) + k•
ρ (2) (Σ l1 , . . . , Σ ln ).
In the last equality we used that the cumulant is linear with r espect to each
of the arguments and that the mixed cumulant of independent random vari-
ables vanishes.
It follows that
lim
q →∞
k•
ρ ′q
(Σ l1 , . . . , Σ ln )q− l1 +···+ln − n+2
2 =
(p(1))
l1 +···+ln − n+2
2 lim
q →∞
k•
ρ (1)
r(1)
q
(Σ l1 , . . . , Σ ln )(r(1)
q )− l1 +···+ln − n+2
2 +
(p(2))
l1 +···+ln − n+2
2 lim
q →∞
k•
ρ (2)
r(2)
q
(Σ l1 , . . . , Σ ln )(r(1)
q )− l1 +···+ln − n+2
2 .
It follows that if the representations ρ(i) fulﬁll condition (3.2) then repre-
sentations ρ ′
q fulﬁll (3.2) as well. Equation (3.13) results as a special ca se
of n = 1 and we leave it as a simple exercise to the Reader to study the
GAUSSIAN FLUCTUATIONS OF CHARACTERS OF SYMMETRIC GROUPS 17
case n = 2 and to ﬁnd the covariance of the free cumulants, analogous to
(3.11). □
Theorem 3.9 (Induction of representations). Suppose that the sequence of
representations (ρq ) has character factorization property. Let a sequence
of integers rq be given, such that rq ≤ q and the limit p = limq →∞
rq
q 
exists.
Let ρ ′
q = ρrq ↑Sq
Srq
denote the induced representation. Then the sequence
(ρ ′
q ) has the characters factorization property with
c ′
l+1 =
{
p
l+1
2 cl+1 for l ≥ 2,
1 for l = 1,
and with an explicit (but involved) covariance of free cumulants.
Proof. It is enough to adapt the proof of Theorem 3.8. □
Theorem 3.10 (Tensor product of representations) . Suppose that for i ∈
{1, 2 } the sequence of representations (ρ(i)
q ) has character factorization
property. Then the tensor product ρ ′
q = ρ(1)
q ⊗ ρ(2)
q has the property of
factorization of characters. Furthermore, the limit distribution and the ﬂuc-
tuations are the same as for the Plancherel measure(3.9) and (3.10).
Proof. Since the normalized characters fulﬁll for any π ∈ Sq 
χ ρ ′q (π ) =
(
χ ρ (1)
q
⊗ χ ρ (2)
q
)
(π ⊗ π )
hence also the corresponding cumulants are equal:
kρ ′q (σ 1, . . . , σ n) = kρ (1)
q ⊗ρ (2)
q
(σ 1 ⊗ σ 1, . . . , σ n ⊗ σ n).
Theorem 4.4 of Leonov and Sirjaev can be used to calculate the right-hand
side. Lemma 4.6 together with the condition (3.1) for ρ(i) show that the
right-hand side is of order O(q−( |σ 1 |+···+|σ n |+n− 1)) hence condition (3.1) is
fulﬁlled for ρ ′. It also follows that the limits in Theorem 3.2 are given by
cl+1 = lim
q →∞
E(σ )q
l− 1
2 =
{
1 if l = 1,
0 if l ≥ 2,
lim
q →∞
Cov(σ 1, σ 2)q
l1 +l2
2 = 0,
where σ, σ 1, σ 2 are disjoint cycles with lengths, respectively, l, l1, l2. □
