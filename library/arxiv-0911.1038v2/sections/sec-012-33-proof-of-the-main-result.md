---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-012-33-proof-of-the-main-result
section_title: "Proof of the main result"
section_number: 3.3
pages: 16-18
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
STRUCTURE OF KEROV CHARACTER POLYNOMIALS 17
Proof of Theorem 1.1. We know by Proposition 1.2 that for any integerg ≥
1 there exist inhomogeneous symmetric functions ˜fg and ˜hg, having maxi-
mal degree 4g, such that
Lk :=L′
k :=kK k,k +1−2g =
∑
|µ |=k+1−2g
(
l(µ) + 2g − 2
)
! ˜fg(µ)Rµ
=
∑
|µ |=k+1−2g
(2g − 1)l(µ ) ˜hg(µ)Qµ.
By applying Lemma 3.2 for ∆ = 0 we obtain that
kK k,k +1−2g =k
∑
|µ |=k+1−2g
(
l(µ) + 2g − 2
)
! ˜f ′
g(µ)Rµ
=k
∑
|µ |=k+1−2g
(2g − 1)l(µ ) ˜h′g(µ)Qµ,
where ˜f ′
g, ˜h′
g are symmetric functions of degree at most 4g − 1.
Let
Lk :=L′
k :=Kk,k +1−2g =
∑
|µ |=k+1−2g
(
l(µ) + 2g − 2
)
! ˜f ′
g(µ)Rµ
=
∑
|µ |=k+1−2g
(2g − 1)l(µ ) ˜h′
g(µ)Qµ.
Lemma 3.3(a) shows that Lemma 3.2 can be applied for ∆ = 0 , thus
Kk,k +1−2g =k
∑
|µ |=k+1−2g
(
l(µ) + 2g − 2
)
! ˜f ′′
g (µ)Rµ
=k
∑
|µ |=k+1−2g
(2g − 1)l(µ ) ˜h′′
g(µ)Qµ,
where ˜f ′′
g, ˜h′′
g are symmetric functions of degree at most 4g − 2.
Let
Lk :=L′
k := AKk,k +1−2g
k =
∑
|µ |=k+1−2g
(
l(µ) + 2g − 2
)
!A ˜f ′′
g (µ)Rµ
=
∑
|µ |=k+1−2g
(2g − 1)l(µ )A ˜h′′
g(µ)Qµ,
whereA is the common multiple of the denominators of coefﬁcients of ˜h′′
g
and ˜f ′′
g . We know that Lp−1 = L′
p−1 has integer coefﬁcients as polynomial
in R2,R 3,... and we know, thanks to Lemma 3.3(b), that for inﬁnitely
many prime numbers p the coefﬁcients of (p − 1)Lp−1 = (p − 1)L′
p−1 are
divisible by p, hence coefﬁcients of Lp−1 = L′
p−1 are also divisible by p,
18 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
becausep−1 andp are coprime. Then we can apply Lemma 3.2 for∆ = −1
and we obtain that there exist symmetric functions ˜f ′′′
g , ˜h′′′
g of degree at most
4g − 3 such that
Kk,k +1−2g =k (k + 1)
∑
|µ |=k+1−2g
(
l(µ) + 2g − 2
)
! ˜f ′′′
g (µ)Rµ
=k (k + 1)
∑
|µ |=k+1−2g
(2g − 1)l(µ ) ˜h′′′
g (µ)Qµ,
where ˜f ′′
g, ˜h′′
g are symmetric functions of degree at most 4g − 3.
Similarly as before, thanks to Lemma 3.3(c) and thanks to thefact that for
prime numberp> 2 the numbersp andp + 1 are coprime and the numbers
p + 2 andp are coprime, we can apply Lemma 3.2 for ∆ = 1 for
Lk :=L′
k := BKk,k +1−2g
k(k + 1) =
∑
|µ |=k+1−2g
(
l(µ) + 2g − 2
)
!B ˜f ′′′
g (µ)Rµ
=
∑
|µ |=k+1−2g
(2g − 1)l(µ )B ˜h′′′
g (µ)Qµ,
where B is the common multiple of the denominators of coefﬁcients of
˜h′′′
g and ˜f ′′′
g and we obtain that there exist symmetric functions ˜f ′′′′
g , ˜h′′′′
g of
degree at most 4g − 4 such that
Kk,k +1−2g = (k − 1)k (k + 1)
∑
|µ |=k+1−2g
(
l(µ) + 2g − 2
)
! ˜f ′′′′
g (µ)Rµ
= (k − 1)k (k + 1)
∑
|µ |=k+1−2g
(2g − 1)l(µ ) ˜h′′′′
g (µ)Qµ,
which ﬁnishes the proof. □
4. T ECHNICAL LEMMAS
