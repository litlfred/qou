---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-014-41-identities-on-symmetric-functions
section_title: "Identities on symmetric functions"
section_number: 4.1
pages: 18-21
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
Lemma 4.1. The following abstract equalities hold:
(16)∑
µ ∪ρ=ν
mλ (µ) (l(µ) + 2g − 2)!
l(µ)! uµuρ = mλ (ν)
l(λ) + 2g − 1
(l(ν) + 2g − 2)!
l(ν)! uν;
(17)
∑
µ ∪ρ=ν
mλ (µ)(2g − 1)l(µ )z−1
µ z−1
ρ =
( 2g − 1
2g
) l(λ )
mλ (ν)(2g)l(ν)z−1
ν .
STRUCTURE OF KEROV CHARACTER POLYNOMIALS 19
Proof. From the deﬁnition of the monomial symmetric function we kno w
thatmλ (µ) = 0 for all partitionsµ such thatl(µ)<l (λ). We use an identity
that for every integern such thatl(λ) ≤n ≤l(ν) we have
(18)
( l(ν) −l(λ)
n −l(λ)
)
mλ (ν) =
∑
µ ∪ρ=ν,
l(µ )=n
mλ (µ)
( ∏
i≥1
mi(ν)!
mi(µ)!mi(ρ)!
)
.
Indeed,
∑
µ ∪ρ=ν,
l(µ )=n
mλ (µ)
( ∏
i≥1
mi(ν)!
mi(µ)!mi(ρ)!
)
=
∑
µ ⊂ν,
l(µ )=n
mλ (µ) =
∑
µ ′⊂µ ⊂ν,
l(µ )=n,l (µ ′)=l(λ )
mλ (µ′) =
∑
µ ′⊂ν,
l(µ ′)=l(λ )
∑
µ ′⊂µ ⊂ν,
l(µ )=n
mλ (µ′) =
( l(ν) −l(λ)
n −l(λ)
) ∑
µ ′⊂ν,
l(µ ′)=l(λ )
mλ (µ′) =
( l(ν) −l(λ)
n −l(λ)
)
mλ (ν),
where∑
µ ⊂ν,
l(µ )=n
means that µ = (νσ (1),...,ν σ (n)) for some σ ∈ S(l(ν))
such that σ(i) < σ(i + 1) for all i ∈ { 1,...,n − 1} and we are summing
over all such permutations σ. Now, we can write the left hand side of (16)
in the following way:
∑
l(λ )≤n≤l(ν)
(n + 2g − 2)!
n!
( ∑
µ ∪ρ=ν,
l(µ )=n
mλ (µ)
∏
i≥1
mi(ν)!
mi(µ) !mi(ρ)!
)
×
uν
n! (l(ν) −n)!
l(ν)! =
∑
l(λ )≤n≤l(ν)
(n + 2g − 2)!
n!
(l(ν) −l(λ))!
(l(ν) −n)!(n −l(λ))!mλ (ν)×
uν
n! (l(ν) −n)!
l(ν)! =
(l(ν) −l(λ))!
l(ν)!
∑
l(λ )≤n≤l(ν)
(n + 2g − 2)!
(n −l(λ))! mλ (ν)uν
and using the equality
∑
0≤i≤b
( a +i
i
)
=
( a +b + 1
b
)
20 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
we have
(l(ν) −l(λ))!
l(ν)!
∑
l(λ )≤n≤l(ν)
(n + 2g − 2)!
(n −l(λ))! =
(l(ν) −l(λ))!(l(λ) + 2g − 2)!
l(ν)!
∑
0≤n≤l(ν)−l(λ )
(n +l(λ) + 2g − 2)!
n!(l(λ) + 2g − 2)! =
(l(ν) −l(λ))!(l(λ) + 2g − 2)!
l(ν)!
∑
0≤n≤l(ν)−l(λ )
( l(λ) + 2g − 2 +n
n
)
=
(l(ν) −l(λ))! (l(λ) + 2g − 2)! (l(ν) + 2g − 1)!
l(ν)! (l(ν) −l(λ))! (l(λ) + 2g − 1)! = (l(ν) + 2g − 1)!
l(ν)!(l(λ) + 2g − 1)
which ﬁnishes the proof of (16).
Using (18) we can write the left hand side of (17) in the following form:
∑
l(λ )≤n≤l(ν)
(2g − 1)n
( ∑
µ ∪ρ=ν,
l(µ )=n
mλ (µ)
∏
i≥1
mi(ν)!
mi(µ) !mi(ρ)!
)
z−1
ν =
( ∑
l(λ )≤n≤l(ν)
(2g − 1)n
( l(ν) −l(λ)
n −l(λ)
) )
mλ (ν)z−1
ν =
(2g − 1)l(λ )
( ∑
0≤n≤l(ν)−l(λ )
( l(ν) −l(λ)
n
)
(2g − 1)n
)
mλ (ν)z−1
ν =
( 2g − 1
2g
) l(λ )
mλ (ν)(2g)l(ν)z−1
ν ,
where the last equality holds because of the binomial identity:
∑
0≤n≤m
( m
n
)
an = (a + 1)m,
which ﬁnishes the proof. □
4.2. Proof of Lemma 3.1.
Proof of Lemma 3.1. Let l be ﬁxed; we will use backward induction over
k. For k = l we know that f (µk) = 0 for inﬁnitely many choices of µk.
In other words, polynomial f has inﬁnitely many zeros hence f = 0 , as
claimed.
Let us assume that the inductive assertion holds for some k ≤l. We can
write
f (xk−1,...,x l) =
∑
0≤i≤N
xi
k−1fi(xk,...,x l)
STRUCTURE OF KEROV CHARACTER POLYNOMIALS 21
for some N. Let us ﬁx integers µk,...,µ l bigger than 1 which satisfy
(14) and (13). Then we can ﬁnd inﬁnitely many integer numbers µk−1 for
which the vector (µk−1,...,µ l) satisﬁes both (14) and (13); for each such
a number we have f (µk−1,...,µ l) = 0 therefore the polynomial xk−1 ↦→
f (xk−1,µ k,...,µ l) has inﬁnitely many zeros hence it is the zero polyno-
mial andfi(µk,...,µ l) = 0 . This shows that the inductive assertion can be
applied to the polynomial fi(xk,...,x l) and therefore fi(xk,...,x l) = 0 .
This ﬁnishes the proof. □
