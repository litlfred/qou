---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-012-62-multivariable-little-q-jacobi-polynomials
section_title: "Multivariable little q-Jacobi polynomials"
section_number: 6.2
pages: 24-27
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
littleq-Jacobi polynomials P L
λ (z) = P L
λ (z;a,b ;q,t ) from Section 2. We ﬁrst shortly discuss
evaluation formulas for one-variable little q-Jacobi polynomials ( n = 1), in which case
the evaluation formulas can be derived directly from the explicit expr essions of the little
q-Jacobi polynomials as basic hypergeometric series. In fact, the m onic one-variable little
q-Jacobi polynomial is independent of t and is given explicitly as
P L
m(z) =
(
qb;q
)
m
(
qm+1ab;q
)
m(qb)m 3φ2
(
q−m,q m+1ab,qbz
qb, 0 ;q,q
)
=
(
qa;q
)
m(
qm+1ab;q
)
m
(−1)mq
1
2 m(m−1)
2φ1
(
q−m,q m+1ab
qa ;q,qz
)(6.5)
for m ∈ Z+, see e.g. [14]. Here the second equality follows from [8, (III.7)]. From the
second equality in (6.5) we obtain
(6.6) P L
m(0) =
(
qa,qab ;q
)
m
(
qab;q
)
2m
(−1)mq
1
2 m(m−1).
From the ﬁrst equality in (6.5) and the q-Vandermonde sum
(6.7) 2φ1
(
q−m,a
c ;q,q
)
=
(
c/a;q
)
m(
c;q
)
m
am
for m ∈ Z+ (see [8, (II.6)]), we obtain
(6.8) P L
m(1) =
(
qb,qab ;q
)
m(
qab;q
)
2m
(
qma)m.
Finally, from the ﬁrst equality in (6.5) we obtain
(6.9) P L
m(q−1b−1) =
(
qb,qab ;q
)
m
(
qab;q
)
2m(qb)m.
In the following theorem we give the multivariable analogues of the eva luation formulas
(6.6), (6.8) and (6.9). Deﬁne ∆ λ = ∆ λ(a,b ;q,t ) by
(6.10) ∆ λ(a,b ;q,t ) =
∏
1≤j<k≤n
(
qabt2n−j−k+1;q
)
λj+λk
(
tk−j+1;q
)
λj−λk(
qabt2n−j−k;q
)
λj+λk
(
tk−j;q
)
λj−λk
, ∀λ ∈ Λ n.
Theorem 6.1. Forλ ∈ Λ n we have the evaluation formulas
(6.11) P L
λ (0) = ∆ λ
n∏
i=1
(
qatn−i,qabt n−i;q
)
λi(
qabt2(n−i);q
)
2λi
(−1)λiq
1
2 λi(λi−1),
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 25
(6.12) P L
λ (tρ) = ∆ λ
n∏
i=1
(
qbtn−i,qabt n−i;q
)
λi(
qabt2(n−i);q
)
2λi
(
aqλitn−i) λi
,
(6.13) P L
λ (q−1b−1t−ρ) = ∆ λ
n∏
i=1
(
qbtn−i,qabt n−i;q
)
λi(
qabt2(n−i);q
)
2λi
(
qbtn−i) λi
.
Proof. The evaluation formulas depend rationally on the parameters, henc e it suﬃces to
prove the theorem for a suitable choice of Zariski dense complex va lues of the parameters
a,b,q andt. The proof now uses the explicit limit transitions from Macdonald-Koo rnwinder
polynomials to multivariable little q-Jacobi polynomials from [29] and [27]. The key ingre-
dient is the following result from the proof of [27, Theorem 6.4]. Let λ,µ ∈ Λ n such that
µ<λ . Then
(6.14) lim
ǫ→0
(
q− 1
2ǫ
) |λ|−|µ|
cλ,µ(ǫ−1q
1
2, −aq
1
2,ǫbq
1
2, −q
1
2 ;q,t ) = cL
λ,µ(a,b ;q,t )
for the coeﬃcients cλ,µ (6.1) and cL
λ,µ (2.1) in the monomial expansions of Pλ andP L
λ , where
q
1
2 is an arbitrary choice of square root of q.
Proof of (6.11). Observe that
(6.15) lim
ǫ→0
ǫ|λ|mλ(z) = ~mλ(0), ∀λ ∈ Λ n,
since both sides are equal to zero if λ ∈ Λ n \ {0} and are equal to one if λ = 0. Combining
(6.1), (2.1), (6.14) and (6.15) now yields
(6.16) lim
ǫ→0
(
q− 1
2ǫ
) |λ|
Pλ
(
z;ǫ−1q
1
2, −aq
1
2,ǫbq
1
2, −q
1
2 ;q,t
)
=P L
λ (0;a,b ;q,t )
for λ ∈ Λ n. By the evaluation formula (6.2) for the Macdonald-Koornwinder po lynomial
Pλ and using that the Macdonald-Koornwinder polynomial is symmetric in a,b,c,d , we
have
(
q− 1
2ǫ
) |λ|
Pλ
(
−aq
1
2tρ;ǫ−1q
1
2, −aq
1
2,ǫbq
1
2, −q
1
2 ;q,t
)
= ∆ λ(a,b ;q,t )
n∏
i=1
(
qatn−i, −qabtn−iǫ,qabt n−i, −qatn−iǫ−1;q
)
λi
ǫλi
(
qabt2(n−i);q
)
2λi
(
−aqtn−i) λi
.
Combined with the limit transition (6.16), specialized to z = −aq
1
2tρ, we obtain the eval-
uation formula (6.11) for the multivariable little q-Jacobi polynomial P L
λ .
Proof of (6.12). Now we use the degeneration
(6.17) lim
ǫ→0
ǫ|λ|mλ(ǫ−1z) = ~mλ(z), ∀λ ∈ Λ n
for the monomial bases. Together with (6.14) this yields the limit tran sition
(6.18) lim
ǫ→0
(
q− 1
2ǫ
) |λ|
Pλ
(
q
1
2ǫ−1z;ǫ−1q
1
2, −aq
1
2,ǫbq
1
2, −q
1
2 ;q,t
)
=P L
λ (z;a,b ;q,t )
26 URI ONN AND JASPER V. STOKMAN
forλ ∈ Λ n, which is in accordance with [27, Theorem 6.4]. By the evaluation form ula (6.2)
for the Macdonald-Koornwinder polynomial Pλ we now have
(
q− 1
2ǫ
) |λ|
Pλ
(
q
1
2ǫ−1tρ;ǫ−1q
1
2, −aq
1
2,ǫbq
1
2, −q
1
2 ;q,t
)
= ∆ λ(a,b ;q,t )
n∏
i=1
(
−qatn−iǫ−1, −qtn−iǫ−1,qbt n−i,qabt n−i;q
)
λi
ǫ2λi
(
qabt2(n−i);q
)
2λi
(
qtn−i) λi
.
Combined with the limit transition (6.18), specialized to z =tρ, we obtain the evaluation
formula (6.12).
Proof of (6.13). We now use the limit transition
(6.19) lim
ǫ→0
ǫ|λ|mλ(ǫz) = ~mλ(z−1), ∀λ ∈ Λ n.
Together with (6.14) this yields
(6.20) lim
ǫ→0
(
q− 1
2ǫ
) |λ|
Pλ
(
q− 1
2ǫz;ǫ−1q
1
2, −aq
1
2,ǫbq
1
2, −q
1
2 ;q,t
)
=P L
λ (z−1;a,b ;q,t )
for λ ∈ Λ n. By the evaluation formula (6.2) for the Macdonald-Koornwinder po lynomial
Pλ we now have
(
q− 1
2ǫ
) |λ|
Pλ
(
ǫbq
1
2tρ;ǫ−1q
1
2, −aq
1
2,ǫbq
1
2, −q
1
2 ;q,t
)
= ∆ λ(a,b ;q,t )
n∏
i=1
(
qbtn−i,qabt n−i, −qbtn−iǫ, −qabtn−iǫ;q
)
λi(
qabt2(n−i);q
)
2λi
(
qbtn−i) −λi
.
Combined with the limit transition (6.20), specialized to z =qbtρ, we obtain (6.13). □
The quadratic norms NL(λ) = NL(λ;a,b ;q,t ) ∈ E of the multivariable little q-Jacobi
polynomials have been explicitly evaluated in [27]. It reads
NL(λ) = q(λ,λ)a|λ|t2(ρ,λ)N +
L (λ)N−
L (λ),
where the factors N±
L (λ) = N±
L (λ;a,b ;q,t ) ∈ E are given by
N +
L (λ) =
n∏
i=1
(
qatn−i,qabt n−i;q
)
λi(
qabt2(n−i);q
)
2λi
∏
1≤j<k≤n
(
qabt2n−j−k+1;q
)
λj+λk
(
tk−j+1;q
)
λj−λk
(
qabt2n−j−k;q
)
λj+λk
(
tk−j;q
)
λj−λk
,
N−
L (λ) =
n∏
i=1
(
qtn−i,qbt n−i;q
)
λi(
q2abt2(n−i);q
)
2λi
∏
1≤j<k≤n
(
q2abt2n−j−k−1;q
)
λj +λk
(
qtk−j−1;q
)
λj−λk
(
q2abt2n−j−k;q
)
λj +λk
(
qtk−j;q
)
λj−λk
.
We recall from [27] that
(6.21) lim
ǫ→0
(
q− 1
2ǫ
) 2|λ|
NK(λ;ǫ−1q
1
2, −aq
1
2,ǫbq
1
2, −q
1
2 ;q,t ) = NL(λ;a,b ;q,t ), ∀λ ∈ Λ n
for generic specialized parameters.
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 27
