---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-020-52-computation-of-covariances
section_title: "Computation of covariances"
section_number: 5.2
pages: 21-22
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
rescaled deviations of the Σk. First, note that if l and m are two positive integers, then:
k•(Σl, Σm) = /BX [Σl • Σm] − /BX [Σl] /BX [Σm] = /BX [Σl,m] − /BX [Σl] /BX [Σm]
= (1 − q)l+m
1 − ql,m
(
n↓l+m − n↓l n↓m)
= −lm (1 − q)l+m
1 − ql,m nl+m−1 + O(nl+m−2)
The last identity follows from the development of the fallin g factorial:
n↓k = nk − k(k − 1)
2 nk−1 + O(nk−2)
Now, we can compute the higher term of the standard cumulant k(Σl, Σm) if we use the graded develop-
ment of Σl Σm − Σl,m in the algebra of observables:
k(Σl, Σm) = kid(Σl, Σm) + k•(Σl, Σm) = /BX [Σl Σm − Σl,m] + k•(Σl, Σm)
= /BX [lm Σl+m−1] − lm (1 − q)l+m
1 − ql,m nl+m−1 + O(nl+m−2)
= lm (1 − q)l+m
( 1
1 − ql+m−1,1 − 1
1 − ql,m
)
nl+m−1 + O(nl+m−2)
We have therefore proved:
Proposition 20 (Fluctuations of Σk). If we denote Zn,q,k = √
n (Σk/nk − (1 − q)k/(1 − qk)), then
(Zn,q,k)k≥2 converges in ﬁnite-dimensional laws towards a gaussian vec tor (Zq,k )k≥2, with the following
covariance matrix:
k(Zq,l, Zq,m) = lm (1 − q)l+m
( 1
1 − ql+m−1,1 − 1
1 − ql,m
)
End of the proof of Proposition 16. It turns out that the sequence (Wn,q,k )k≥2 of the rescaled deviations
of power sums has the same limit law (Zq,k)k≥2. Indeed, we have already shown that the limit of the
rescaled deviations of power sums is a gaussian vector, and i t suﬃces then to show that k(pl, pm) has the
same higher term as k(Σl, Σm). According to the proposition 7, each symbol Σk is a rational polynomial
in the pl≤k with higher term pk. So, we can use the multi-linearity of joint cumulants to wri te:
k(Σl, Σm) = k(pl, pm) + (cumulants of observables ai, bj with deg ai + deg bj < l + m).
But if a and b are two observables of degree A and B, then we have seen that k(a, b) is a O(nA+B−1).
As a consequence, the remaining terms are all O(nl+m−2). This ends the proof of Proposition 16. □
Remark 5. Lemma 17 also implies that the rescaled q-characters converge towards a gaussian vector. For
these q-characters, it can be shown that if Sn,q,k = √n (Σk,q /nk) ≃ √n χλ(k1n−k, q), then (Sn,q,k)k≥2
converges in ﬁnite-dimensional laws towards a gaussian vec tor (Sq,k)k≥2, with the following covariance
matrix:
k(Sq,l, Sq,m) = ( q − q2)l+m−3 (1 − q2) {l − 1}q {m − 1}q
{l + m − 1}q {l + m − 2}q {l + m − 3}q
Hence, one has a q-analogue of Kerov’s central limit theorem (see [ IO02, Theorem 6.1]) for the q-characters
of the Hecke algebras under q-Plancherel measures. However, notice that the ﬂuctuation s of the q-
characters are always some O(n−1/2), in contrast to the case of the characters χλ(k1n−k) under Plancherel
measures, whose ﬂuctuations are O(n−k/2). The proof of the formula given above involves a generalizat ion
22 V ALENTIN FÉRAY AND PIERRE-LOÏC MÉLIOT
of Proposition 20 to the case of arbitrary central characters Σµ, and a Möbius inversion formula that
allows to simplify the expression of the covariances; we ref er to a future paper of the second author
([Mél10]) for details on these computations.
