---
doc_id: s0894-0347-00-00337-4
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4"
section_id: sec-023-41-results-and-strategy-of-proof-in-this-section
section_title: "Results and strategy of proof. In this section we prove Theorem 4 which"
section_number: 4.1
pages: 19-20
source_pdf: S0894-0347-00-00337-4.pdf
source_sha256: 1c6848281fc2804c
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4 — 35 sections: Introduction; Plancherel measures. Given a ﬁnite; Poissonization and correlation fun"
---
was stated in Section 1.4 of the Introduction. We refer the reader to Section 1.4 for
a discussion of the relation between Theorem 4 and the results obtained in [3, 4, 25].
Recall that the Airy kernel was deﬁned as
A(x, y) = A(x)A′(y) −A′(x)A(y)
x −y
,
where A(x) is the Airy function (1.15).
The Airy ensemble is, by deﬁnition, a
random point process on R, whose correlation functions are given by
ρAiry
k
(x1, . . . , xk) = det
h
A(xi, xj)
i
1≤i,j≤k .
This ensemble was studied in [36]. We denote by ζ1 > ζ2 > . . . a random con-
ﬁguration of the Airy ensemble. Theorem 4 says that after a proper scaling and
normalization, the rows λ1, λ2, . . . of a Plancherel random partition λ converge in
joint distribution to the Airy ensemble. Namely, the random variables eλ,
eλ =

eλ1 ≥eλ2 ≥. . .

,
eλi = n1/3
 λi
n1/2 −2

,
converge, in joint distribution, to the Airy ensemble as n →∞.
In the proof of Theorem 4, we shall follow the strategy explained in Section 1.5
of the Introduction. First, we shall prove that under the poissonized measure M θ
500
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
on the set of partitions λ, the random variables eλ converge, in joint distribution, to
the Airy ensemble as θ ≈n →∞. This result is stated below as Theorem 5. From
this, using certain monotonicity and Lemma 4.7 which is due to K. Johansson, we
shall conclude that the same is true for the measures Mn as n →∞.
The proof of Theorem 5 will be based on the analysis of the behavior of the
correlation functions of M θ, θ ≈n →∞, near the point 2√n. From the expression
for correlation functions of M θ given in Theorem 1 it is clear that this amounts to
the study of the asymptotics of J2√n(2
√
θ) when θ ≈n →∞. This asymptotics is
classically known and from it we shall derive the following
Proposition 4.1. Set r =
√
θ. We have
r
1
3 J

2r + xr
1
3 , 2r + yr
1
3 , r2
→A(x, y),
r →+∞,
uniformly in x and y on compact sets of R.
The prefactor r
1
3 corresponds to the fact that we change the local scale near 2r
to get nonvanishing limit correlations.
Using this and verifying certain tail estimates we obtain the following
Theorem 5. For any ﬁxed m = 1, 2, . . . and any a1, . . . , am ∈R we have
(4.1)
lim
θ→+∞M θ
 (
λ

λi −2
√
θ
θ
1
6
< ai , 1 ≤i ≤m
)!
= Prob{ζi < ai , 1 ≤i ≤m} ,
where ζ1 > ζ2 > . . . is the Airy ensemble.
Observe that the limit behavior of eλ is, obviously, identical with the limit be-
havior of similarly scaled 1st, 2nd, and so on maximal Frobenius coordinates.
Proofs of Proposition 4.1 and Theorem 5 are given Section 4.2. In Section 4.3,
using a depoissonization argument based on Lemma 4.7 we deduce Theorem 4.
Remark 4.2. We consider the behavior of any number of ﬁrst rows of λ, where λ is
a Plancherel random partition. By symmetry, same results describe the behavior
of any number of ﬁrst columns of λ.
