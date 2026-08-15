---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-019-53-a-technical-lemma-obtained-by-polynomial-inte
section_title: "A technical lemma obtained by polynomial interpolation"
section_number: 5.3
pages: 37-38
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
asymptotics of large Young diagrams we need to understand some special cases of
structure constants. Here, we present some technical, but useful lemma about them:
Lemma 5.6. We have the following identities:
(1) gµ,ν;ρ = δρ,µ∪ν for |ρ| + ℓ(ρ) ≥ |µ| + ℓ(µ) + |ν| + ℓ(ν);
(2) gµ,ν;1k = 0 for ˜µ ⁄= ˜ν and 2k ≥ |µ| + ℓ(µ) + |ν| + ℓ(ν) − 2;
(3) g(k),(k);1k = k;
(4) g(k),(l);ρ = 0 for |ρ| + ℓ(ρ) = k + l + 1.
Proof. Let x(µ, ν; ρ) := |µ| + ℓ(µ) + |ν| + ℓ(ν) − (|ρ| + ℓ(ρ)).
By Theorem 1.4 we know that gµ,ν;ρ is a polynomial in γ of degree at most
x(µ, ν; ρ) and of the same parity as x(µ, ν; ρ). Hence, if one wants to prove that
for some particular partitions, gµ,ν;ρ is identically equal to some constant c, it is
enough to prove that:
• g(1)
µ,ν;ρ = c in the case x(µ, ν; ρ) = 0 ;
• g(2)
µ,ν;ρ = c in the case x(µ, ν; ρ) = 1 (necessarily, c = 0 in this case);
• g(1)
µ,ν;ρ = g(2)
µ,ν;ρ = c in the case x(µ, ν; ρ) = 2 .
Applying this idea, we see that the ﬁrst item holds true, sinc e this is true for
α = 1 [IO02, Proposition 4.9.].
Consider now the second item. In this case, x(µ, ν; ρ) ≤ 2, hence we need to
prove that g(1)
µ,ν;1k = g(2)
µ,ν;1k = 0. We know from Lemma 5.2 (1) thatc(1)
π,ρ;1n = 0 for
any pair of different partitions π, ρ ⊢ n. It means that for n large enough, thanks
to (19), we have the following equation:
0 =
∑
0≤i≤k+1
g(1)
˜π, ˜ρ;(1i) · i! ·
(n
i
)
,
hence
g(1)
˜π, ˜ρ;(1i) = 0 for each 0 ≤ i ≤ k + 1.
The same holds for g(2) using Lemma 5.5. This ﬁnishes the case where µ and ν
have no parts equal to 1.
The general case follows, since for any λ ⊢ n one has
Chµ(λ) = ( n − |˜µ|)m1(µ) Ch˜µ(λ).
In order to prove the third item, we need to prove the equalities
g(1)
(k),(k);1k = k = g(2)
(k),(k);1k (as x((k), (k); 1k )) = 2 ).
Here, we use Equation (19) again. We have that
c(1)
(k1n),(k1n);(1k+n) = 1
k2
∑
0≤i≤k+n
g(1)
(k),(k);(1i)i!
(k + n
i
)
.
38 M. DOŁ ˛ EGA AND V . FÉRAY
Moreover, the summation index can be restricted to i ≤ k as g(1)
(k),(k);(1i) = 0 for
i > k . By Lemma 5.2 (2) one has that
c(1)
(k1n),(k1n);(1k+n) =
(k + n
k
)
(k − 1)!.
It gives us
(k + n
k
)
(k − 1)! = 1
k2
∑
0≤i≤k
g(1)
(k),(k);(1i)i!
(k + n
i
)
and since both sides of the equation are polynomials inn, the equationg(1)
(k),(k);(1k ) =
k follows (all others g(1)
(k),(k);(1i) vanish). The same proof works for α = 2 , using
Lemma 5.5 (2).
Finally, let us prove the last item. As x((k), (l), ρ) = 1 in this case, it is enough
to prove that g(2)
(k),(l);ρ = 0. Here, we shall use a different approach. It is proved in
[F´S11, Theorem 5.3] that the coefﬁcient of
(
R(2)
2
) s2(
R(2)
3
) s3
· · ·
in Kerov’s expansion of Ch(2)
(k) Ch(2)
(l) − Ch(2)
(k,l) is, up to some constant factor, the
number of maps with 2 faces, k + l edges, 2s2 + 3s3 + · · · vertices and some
additional properties (the details of which is irrelevant here). But, using the theory
of Euler characteristic, such maps may exist only if
2 − (k + l) + 2s2 + 3s3 + · · · ≤ 2,
that is
2s2 + 3s3 + · · · ≤ k + l.
This implies that
deg1
(
Ch(2)
(k) Ch(2)
(l) − Ch(2)
(k,l)
)
= k + l.
Expanding it in the Jack characters basis one has
Ch(2)
(k) Ch(2)
(l) = Ch (2)
(k,l) +
∑
|ρ|+ℓ(ρ)≤k+l
g(2)
(k),(l);ρ Ch(2)
ρ ,
which ﬁnishes the proof. □
Remark. The equality g(1)
(k),(k);(1k) = k was also established by Kerov, Ivanov and
Olshanski [IO02, Proposition 4.12.], using their combinat orial interpretation for
g(1)
µ,ν;ρ.
6. J ACK MEASURE : LAW OF LARGE NUMBERS
The purpose of this Section is to prove Theorem 1.1. As in [IO02], the key point
