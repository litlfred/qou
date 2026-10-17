---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-006-15-free-cumulants
section_title: "Free cumulants"
section_number: 1.5
pages: 3-5
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
toc_source: outline
---
of λ.
The original deﬁnition of free cumulants of λ given by Biane is quite
involved (free cumulants of a Young diagram are Speicher’s free cumulants
[NS06] — related to Voiculescu’s free probability theory [VDN92] — of
Kerov’s transition measure [Ker93] of the Young diagram λ), but it has an
advantage that it is very explicit and allows an algorithmic computation of
free cumulants in terms of the shape of a Young diagram.
From the results of Biane [Bia98] one can show the very surprising fact
that for any integer k ≥1 and any Young diagram λ the values of the
normalized character on dilations of λ
N ∋s 7→Σsλ
k
4
MACIEJ DOŁ ˛EGA AND PIOTR ´SNIADY
are given by a polynomial function of degree (at most) k + 1. Furthermore,
the leading coefﬁcient is equal to one of the free cumulants:
(2)
Rλ
k+1 = [sk+1]Σsλ
k = lim
s→∞
Σsλ
k
sk+1.
From the perspective of the Biane’s work [Bia98] this is a highly nontrivial
and very interesting result: it shows that free cumulants (which are viewed
as concrete, algorithmically computable quantities) describe the ﬁrst-order
asymptotics of characters. For the purposes of this article we can reverse the
optics and take (2) as a convenient (even if somewhat abstract) deﬁnition of
free cumulants.
1.5. Free cumulants. We deﬁne the free cumulants Rλ
2, Rλ
3, . . . as
Rλ
k = lim
s→∞
1
sk Σsλ
k−1,
in other words each free cumulant is asymptotically the dominant term of
the character on a cycle of appropriate length in the limit when the Young
diagram tends to inﬁnity.
One of the reasons why free cumulants are so useful in asymptotic rep-
resentation theory is that they are homogeneous with respect to dilations of
the Young diagrams, namely
Rsλ
k = skRλ
k.
1.6. Kerov character polynomials. It turns out that free cumulants can
be used not only to provide asymptotic approximations for the characters of
symmetric groups, but also for exact formulas. Kerov during a talk in Insti-
tut Henri Poincaré in January 2000 [Ker00] announced the following result
(the ﬁrst published proof was given by Biane [Bia03]): for each permutation
π there exists a unique universal polynomial Kπ with integer coefﬁcients,
called Kerov character polynomial, with a property that
Σλ
π = Kπ(Rλ
2, Rλ
3, . . . )
holds true for any Young diagram λ. We say that the Kerov polynomial is
universal because it does not depend on the choice of λ. In order to simplify
notation we suppress the λ-dependence of characters and free cumulants,
writing
Σπ = Kπ(R2, R3, . . . ).
As usual, we are mostly concerned with the values of the characters on
cycles, therefore we introduce special notation for such Kerov polynomials
Σk = Kk(R2, R3, . . . ).
STRUCTURE OF KEROV CHARACTER POLYNOMIALS
5
The ﬁrst few Kerov polynomials Kk are as follows [Bia01]:
Σ1 = R2,
Σ2 = R3,
Σ3 = R4 + R2,
Σ4 = R5 + 5R3,
Σ5 = R6 + 15R4 + 5R2
2 + 8R2,
Σ6 = R7 + 35R5 + 35R3R2 + 84R3.
The primary motivation for investigation of this subject is the asymp-
totic representation theory, namely a good understanding of Kerov character
polynomials might in the future shed some light on asymptotics of charac-
ters, also in the most difﬁcult scaling when the length of the permutation
on which we evaluate the character grows with the number of boxes of the
Young diagram, see [F´S11].
The second motivation — which is key for the purposes of this article —
is related to algebraic combinatorics. The last decade has seen a number
of research papers which stated (sometimes conjecturally) several very sur-
prising combinatorial properties of Kerov polynomials. For example, it was
conjectured by Kerov [Ker00] that the coefﬁcients of Kerov polynomials
are non-negative integers. These papers showed not only the richness of the
combinatorial and the analytic structures of the Kerov character polynomi-
als but also the difﬁculty in fully understanding these polynomials. Since
the results proved in most of these papers will be necessary for the purposes
of this article we decided to postpone the presentation of these papers until
they are needed. A more complete presentation of the history of the subject
and bibliography can be found in the paper [DF´S10].
