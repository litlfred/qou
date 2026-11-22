---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-003-introduction
section_title: "Introduction"
section_number: null
pages: 21-23
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Introduction
Consider an array1 of complex numbers
n
ar : r ∈Ndo
:= ar1,...,rd : r1, . . . , rd ∈N	
where, as in the rest of this book, we include zero in the set N = {0, 1, 2, . . .}.
The numbers ar usually come with a story – a reason they are interesting.
Often, they count a class of objects parametrized by r. For example, it could
be that ar is the multinomial coeﬃcient ar =

|r|
r1 ··· rd

, in which case ar counts
sequences of elements in {1, . . . , d} with r1 occurrences of 1, r2 occurrences
of 2, and so forth up to rd occurrences of the symbol d. Another frequent
source of these arrays is probability theory, where the numbers ar ∈[0, 1]
are probabilities of events parametrized by r. For example, ars might be the
probability that a simple random walk of r steps in {−1, 1} ends at the integer
point s.
Deﬁnition 1.1 (running notation). Throughout this text we use d to denote
the dimension of an arbitrary array, and often employ r, s, and t as synonyms
for r1, r2, and r3, respectively, so as to avoid subscripts in low-dimensional
examples. We also use the notation |r| := Pd
j=1 |r j| for any vector r, which
helps us normalize in a way convenient for combinatorial examples.
How might one understand an array of numbers? In some cases there may
be a simple explicit formula, for instance the multinomial coeﬃcients are given
by a ratio of factorials. When a formula of such brevity exists, we don’t need
fancy techniques to describe the array. Unfortunately, this rarely happens. Of-
ten, if a formula exists at all, it will not be in closed form but will include in-
deﬁnite summation. As Stanley [Sta97, Ex.1.1.4] notes in his foundational text
on enumeration, “There are actually formulas in the literature (nameless here
1 To simplify our presentation in this introduction we consider arrays indexed by vectors of
natural numbers, while later in the text we generalize to arrays indexed by integer vectors.
3
4
Introduction
forevermore) for certain counting functions whose evaluation requires listing
all of the objects being counted! Such a ‘formula’ is completely worthless.”
Less egregious are the formulae containing functions that are rare or compli-
cated and whose properties are not immediately familiar to us. It is not clear
how much good comes from this kind of formula.
Another way of describing arrays of numbers is via recursions. The simplest
examples are ﬁnite linear recurrences, such as the recurrence ar,s = ar−1,s +
ar,s−1 for the binomial coeﬃcients ar,s =
r+s
r

. A recursion for ar in terms of
values {as : s ≺r} whose indices precede r in the coordinatewise partial order
may be unwieldy, perhaps requiring evaluation of a complicated function of all
as with s ≺r, but if the recursion is of bounded complexity then it can give an
eﬃcient algorithm for computing ar. Still, we will see that even in the case of
simple recursions the estimation of ar may not be straightforward. Thus, while
we look for recursions to help us understand number arrays, and for eﬃcient
methods of computation, they rarely provide deﬁnitive descriptions.
A third way of understanding an array of numbers is via an estimate. For
instance, Stirling’s formula, which approximates
n! ≈nn
en
√
2πn
for large n, yields an approximation
 r + s
r
!
≈
r + s
r
r r + s
s
s r
r + s
2πrs
(1.1)
for the binomial coeﬃcients when r and s are large. If number-theoretic prop-
erties of the binomial coeﬃcients are required then we are better oﬀsticking
with a ratio of factorials; when their approximate size is paramount, the esti-
mate (1.1) is better.
A fourth way to understand an array of numbers is to encode it algebraically.
The generating function (often abbreviated GF) of the array {ar} is the formal
series F(z) := P
r∈Nd arzr. Here z is a d-dimensional vector of indeterminates
(z1, . . . , zd) and we use the notation zr := zr1
1 · · · zrd
d . In our running example of
multinomial coeﬃcients, we have the generating function
F(z) =
X
r∈Nd
 
|r|
r1 · · · rd
!
zr1
1 · · · zrd
d =
1
1 −z1 −· · · −zd
,
where the ﬁnal expression can be viewed either as a multiplicative inverse
in a formal power series ring, or as an analytic function over an appropriate
domain of Cd. Stanley calls the generating function “the most useful but the
most diﬃcult to understand” method for describing a sequence or array.
