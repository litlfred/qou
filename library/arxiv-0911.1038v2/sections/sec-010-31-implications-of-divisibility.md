---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-010-31-implications-of-divisibility
section_title: "Implications of divisibility"
section_number: 3.1
pages: 12-16
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
In order to prove Theorem 1.1 we would like to show that for eac h integer
g ≥ 1, functions ˜fg and ˜hg are divisible by the symmetric function
(p1 + 2g − 1) (p1 + 2g)(p1 + 2g − 1)(p1 + 2g − 2)
3! ,
STRUCTURE OF KEROV CHARACTER POLYNOMIALS 13
where p1 denotes the power symmetric function. By word divisible we
mean that there exist symmetric functionsfg andhµ such that
˜fg = (p1 + 2g − 1) (p1 + 2g)(p1 + 2g − 1)(p1 + 2g − 2)
3! fg
and
˜hg = (p1 + 2g − 1) (p1 + 2g)(p1 + 2g − 1)(p1 + 2g − 2)
3! hg.
Observe that for ﬁxed g ≥ 1 and for any partition µ there exists number k
such that |µ| =k + 1 − 2g and then
˜fg(µ) = k
( k + 1
3
)
fg(µ),
˜hg(µ) = k
( k + 1
3
)
hg(µ)(µ).
The idea of showing divisibility of symmetric function by symmetric func-
tion of degree 1 is similar to the case of showing divisibility of some poly-
nomial by some monomial. The main idea is dividing with a remainder and
using a fact that if some integer is divisible by inﬁnite numb er of primes
then it has to be equal to zero. The remainning of this section is a formali-
sation of this idea.
The ﬁrst difﬁculty is that we have to deal with polynomials in several
variables. Hence, in order to show some generalisation of th e “dividing
with remainder” technique, we need the following technical lemma:
Lemma 3.1. Let m be a ﬁxed integer and f be a polynomial in vari-
ables xk,...,x l with the property that f (µk,...,µ l) = 0 for all integers
µk,...,µ l ≥ 1 which fulﬁll the following equations:
(13)
∑
k≤j≤l
µj >m,
(14) µi>µ i+1 + · · · +µl
for all values ofi for which it makes sense. Thenf = 0.
The proof of this lemma can be found in Section 4.
The next lemma is key for this section: it allows to translate information
about arithmetic properties of Kerov polynomials into info rmation about
the polynomials governing the coefﬁcients.
Lemma 3.2. Let f, respectively h, be a symmetric function of degree at
mostd with rational coefﬁcients,g ≥ 1 be an integer; we deﬁne
Lk =
∑
|µ |=k+1−2g
(
l(µ) + 2g − 2
)
!f (µ) Rµ,
14 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
respectively,
L′
k =
∑
|µ |=k+1−2g
(
2g − 1
) l(µ )
h(µ) Qµ
and view it as a polynomial inR2,R 3,... .
Assume that an integer ∆ has a property that all coefﬁcients of Lp+∆
(respectively, all coefﬁcients of L′
p+∆ ) are integers divisible by p for an
inﬁnite number of prime numbersp. Then there exists a symmetric function
˜f (respectively, ˜h) with rational coefﬁcients of degree at most d − 1 such
that
Lk = (k − ∆)
∑
|µ |=k+1−2g
(
l(µ) + 2g − 2
)
! ˜f (µ) Rµ,
respectively,
L′
k = (k − ∆)
∑
|µ |=k+1−2g
(
2g − 1
) l(µ ) ˜h(µ) Qµ.
Proof. For simplicity assume that the coefﬁcients of f (respectively,h) are
integer numbers; if this is not the case we multiply Lk andf (respectively,
L′
k andh) by some common multiple of the denominators.
Letµ = (µ1,µ 2,... ) be a sequence of indeterminates. We use the nota-
tion |µ| =µ1+µ2+· · · and deﬁne variablez = |µ|+2g−1−∆ . The family
of indeterminates µ can be alternatively parametrized by z,µ 2,µ 3,... ; we
just use the substitutionµ1 =z + ∆ + 1 − 2g −µ2 −µ3 − · · ·. Now we can
considerf,h ∈ Λ[z] as polynomials in one variable z with coefﬁcients in
the ring Λ of symmetric functions in variablesµ2,µ 3,... and we can divide
f andh byz with a remainder. Hence
f (µ) = ( |µ| + 2g − 1 − ∆) ˜f (µ) +r(µ2,µ 3,... ),
h(µ) = ( |µ| + 2g − 1 − ∆) ˜h(µ) +s(µ2,µ 3,... )
for some ˜f, ˜h ∈ Λ[z] and for some r,s ∈ Λ . Below we will show that
r =s = 0. This would imply that
f (µ) = ( |µ| + 2g − 1 − ∆) ˜f (µ),
h(µ) = ( |µ| + 2g − 1 − ∆) ˜h(µ),
where by substitution z = |µ| + 2g − 1 − ∆ we view ˜f, ˜h ∈ Λ[µ1] as
polynomials in one variableµ1 with coefﬁcients in Λ . For any permutation
π of the set of positive integers which moves only ﬁnitely many elements
STRUCTURE OF KEROV CHARACTER POLYNOMIALS 15
we have
(|µ| + 2g − 1 − ∆) ˜f (µ1,µ 2,... ) = f (µ1,µ 2,... ) =
f (µπ (1),µ π (2),... ) = ( |µ| + 2g − 1 − ∆) ˜f (µπ (1),µ π (2),... )
hence from the cancellation property
˜f (µ1,µ 2,... ) = ˜f (µπ (1),µ π (2),... )
is a symmetric function. In an analogous way we show that˜h is a symmetric
function. The lemma follows now immediately.
It remains now to show that r = s = 0 . From the following on let
µ2 > · · ·> µl be ﬁxed integers bigger than 1 which fulﬁll Equations (14)
and (13) withm = ∆ −2g. Deﬁneµ1 =p + ∆ + 1 −2g −µ2−µ3 − · · ·−µl,
wherep is a prime number. Notice that µ1 − 1 < p, because we required
that ∆ + 1 − 2g −µ2 −µ3 − · · · −µl < 1. We consider the integral vector
µ = (µ1,...,µ l).
Ifp is large enough, the parts ofµ are all distinct and it follows that
[Rµ 1Rµ 2 · · ·Rµ l]Lp+∆ = (l + 2g − 2)!f (µ) (µ1 − 1)(µ2 − 1) · · ·(µl − 1).
Also, if prime number p is big enough then it does not divide (l + 2g −
2)! (µ1 − 1)(µ2 − 1) · · ·(µl − 1). It follows that for inﬁnitely many prime
numbersp the number
f (µ) = p ˜f (µ) +r(µ2,...,µ l)
is divisible byp. We proved in this way thatr(µ2,...,µ l, 0,... ) is an inte-
ger which is divisible by an inﬁnite number of primes hencer(µ2,...,µ l, 0,... ) =
0. Finaly Lemma 3.1 shows thatr = 0.
Ifp is big enough then condition (14) holds true for all 1 ≤ i ≤ l − 1
therefore every partition resulting from µ by gluing together some of its
parts cannot be obtained by gluing the parts ofµ in some other way (in fact,
this property is the main reason of introducing Equation (14 )). From (3) it
follows that
[Rµ 1Rµ 2 · · ·]L′
p+∆ =
∑
ν≥µ
(2g − 1)l(ν)(
l(ν) − 1
)
!h(ν),
whereν ≥µ means that partitionν can be obtained from partitionµ by glu-
ing some parts of µ. We also know that for inﬁnitely many prime numbers
16 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
p the following number
∑
ν≥µ
(2g − 1)l(ν)(
l(ν) − 1
)
!h(ν) =
p
[ ∑
ν≥µ
(2g − 1)l(ν)(
l(ν) − 1
)
! ˜h(ν)
]
+
∑
ν≥µ
(2g − 1)l(ν)(
l(ν) − 1
)
!s(ν′)
is divisible by p, where for ν = (ν1,ν 2,... ) we denote ν′ = (ν2,ν 3,... ).
Notice that the set of values of ν′ which contribute to the right hand side
does not depend on the choice of p, because onlyν1 depends on the choice
ofp. Thus we proved that for inﬁnitely many prime numbers p the second
summand on the right hand side does not depend on the choice of p and is
a ﬁxed integer divisible by all these prime numbers, hence
(15)
∑
ν≥µ
(2g − 1)l(ν)(
l(ν) − 1
)
!s(ν′) = 0.
We will use induction over k to show that s(x2,...,x k, 0,... ) is equal
to the zero polynomial for any k > 1, which proves that s = 0 . Indeed,
assume, thats(x2,...,x k, 0,... ) is equal to the zero polynomial fork <l.
From the induction hypothesis it follows that all summands on the left-hand
side of (15) vanish, except forν =µ, which shows thats(µ′) = 0 . We use
Lemma 3.1 to show thats = 0 as claimed. □
