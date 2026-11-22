---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-020-41-identities-on-symmetric-functions
section_title: "Identities on symmetric functions"
section_number: 4.1
pages: 18-20
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
toc_source: outline
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
Lemma 4.1. The following abstract equalities hold:
(16)X
µ∪ρ=ν
mλ(µ)(l(µ) + 2g −2)!
l(µ)!
uµuρ =
mλ(ν)
l(λ) + 2g −1
(l(ν) + 2g −2)!
l(ν)!
uν;
(17)
X
µ∪ρ=ν
mλ(µ)(2g −1)l(µ)z−1
µ z−1
ρ
=
2g −1
2g
l(λ)
mλ(ν)(2g)l(ν)z−1
ν .
STRUCTURE OF KEROV CHARACTER POLYNOMIALS
19
Proof. From the deﬁnition of the monomial symmetric function we know
that mλ(µ) = 0 for all partitions µ such that l(µ) < l(λ). We use an identity
that for every integer n such that l(λ) ≤n ≤l(ν) we have
(18)
l(ν) −l(λ)
n −l(λ)

mλ(ν) =
X
µ∪ρ=ν,
l(µ)=n
mλ(µ)
 Y
i≥1
mi(ν)!
mi(µ)! mi(ρ)!
!
.
Indeed,
X
µ∪ρ=ν,
l(µ)=n
mλ(µ)
 Y
i≥1
mi(ν)!
mi(µ)! mi(ρ)!
!
=
X
µ⊂ν,
l(µ)=n
mλ(µ) =
X
µ′⊂µ⊂ν,
l(µ)=n,l(µ′)=l(λ)
mλ(µ′) =
X
µ′⊂ν,
l(µ′)=l(λ)
X
µ′⊂µ⊂ν,
l(µ)=n
mλ(µ′) =
l(ν) −l(λ)
n −l(λ)

X
µ′⊂ν,
l(µ′)=l(λ)
mλ(µ′) =
l(ν) −l(λ)
n −l(λ)

mλ(ν),
where P
µ⊂ν,
l(µ)=n means that µ = (νσ(1), . . . , νσ(n)) for some σ ∈S(l(ν))
such that σ(i) < σ(i + 1) for all i ∈{1, . . . , n −1} and we are summing
over all such permutations σ. Now, we can write the left hand side of (16)
in the following way:
X
l(λ)≤n≤l(ν)
(n + 2g −2)!
n!
 X
µ∪ρ=ν,
l(µ)=n
mλ(µ)
Y
i≥1
mi(ν)!
mi(µ) !mi(ρ)!
!
×
uν
n! (l(ν) −n)!
l(ν)!
=
X
l(λ)≤n≤l(ν)
(n + 2g −2)!
n!
(l(ν) −l(λ))!
(l(ν) −n)!(n −l(λ))!mλ(ν)×
uν
n! (l(ν) −n)!
l(ν)!
=
(l(ν) −l(λ))!
l(ν)!
X
l(λ)≤n≤l(ν)
(n + 2g −2)!
(n −l(λ))! mλ(ν)uν
and using the equality
X
0≤i≤b
a + i
i

=
a + b + 1
b

20
MACIEJ DOŁ ˛EGA AND PIOTR ´SNIADY
we have
(l(ν) −l(λ))!
l(ν)!
X
l(λ)≤n≤l(ν)
(n + 2g −2)!
(n −l(λ))!
=
(l(ν) −l(λ))!(l(λ) + 2g −2)!
l(ν)!
X
0≤n≤l(ν)−l(λ)
(n + l(λ) + 2g −2)!
n!(l(λ) + 2g −2)!
=
(l(ν) −l(λ))!(l(λ) + 2g −2)!
l(ν)!
X
0≤n≤l(ν)−l(λ)
l(λ) + 2g −2 + n
n

=
(l(ν) −l(λ))! (l(λ) + 2g −2)! (l(ν) + 2g −1)!
l(ν)! (l(ν) −l(λ))! (l(λ) + 2g −1)!
=
(l(ν) + 2g −1)!
l(ν)!(l(λ) + 2g −1)
which ﬁnishes the proof of (16).
Using (18) we can write the left hand side of (17) in the following form:
X
l(λ)≤n≤l(ν)
(2g −1)n
 X
µ∪ρ=ν,
l(µ)=n
mλ(µ)
Y
i≥1
mi(ν)!
mi(µ) !mi(ρ)!
!
z−1
ν
=
 
X
l(λ)≤n≤l(ν)
(2g −1)n
l(ν) −l(λ)
n −l(λ)
!
mλ(ν)z−1
ν
=
(2g −1)l(λ)
 
X
0≤n≤l(ν)−l(λ)
l(ν) −l(λ)
n

(2g −1)n
!
mλ(ν)z−1
ν
=
2g −1
2g
l(λ)
mλ(ν)(2g)l(ν)z−1
ν ,
where the last equality holds because of the binomial identity:
X
0≤n≤m
m
n

an = (a + 1)m,
which ﬁnishes the proof.
□
