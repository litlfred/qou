---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-012-labeled-classes
section_title: "Labeled classes"
section_number: null
pages: 69-78
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
51
Proof idea
The basic idea is to apply a sequence of blowups to a polynomial
annihilating f(z) to resolve any singularities it has at the origin, until we arrive
at a case where Proposition 2.36 applies. These changes of variable are mono-
mial substitutions of the form zi 7→zizj, which yields the unimodular matrix.
Full details can be found in [Saf00, Theorem 1].
□
Example 2.42. If f(x, y) = y
p
1 −x −y is the function from Example 2.38
then Safonov’s algorithm implies that f is the M-diagonal of
F(x, y, w) = wx +
2wx

w2 + w

2 + w + x + xy =
X
r,s,t≥0
ar,s,txsytwr,
where M =

1 0
1 1

. In particular, f(x, y) = P
s,t≥0 as+t,s+t,txsyt.
◁
2.5 Labeled classes
We end this chapter with additional constructions that produce a large variety
of combinatorial classes. Each combinatorial class that we have seen so far is
ultimately constructed from atomic pieces via constructions such as the disjoint
union and product, and we can enrich the objects in a class by adding labels
to their atoms. More formally, let the atomic class Z be the class containing a
single object of size 1 and no objects of other sizes, and let the neutral class E
be the class containing a single object of size 0 and no objects of other sizes. A
labeled combinatorial class is a univariate combinatorial class A constructed
from copies of the atomic and neutral classes, where the size of an object is the
number of atoms it contains and for any n ∈N and α ∈An the atoms in α are
given unique labels from the set [n]. The exponential generating function A(z)
of the labeled class A is the formal power series A(z) = P
n≥0
|An|
n! zn ∈C[[z]].
Example 2.43 (Basic labeled classes). The labeled atomic class Z =
n
1
o
is obtained from the atomic class by giving its single element of size one the
label 1. The labeled neutral class is the same as the neutral class, as an object
of size zero has no atoms.
◁
Example 2.44. By viewing a permutation of [n] in one-line notation, the class
of permutations can be constructed as the labeled class consisting of all ﬁnite
sequences of labeled atoms.
◁
We can construct labeled classes iteratively using labeled versions of the
constructions discussed above. If A and B are two labeled combinatorial classes
then, just like in the unlabeled case, the labeled disjoint union class C = A⊔B
52
Generating functions
is simply the class whose set of objects is the disjoint union of the elements in
A and B. The exponential generating function of the labeled disjoint union is
C(z) =
X
n≥0
|An| + |Bn|
n!
zn = A(z) + B(z) ,
where A and B are the exponential generating functions of A and B.
Creating a product for labeled classes is harder: when building tuples of
objects, relabeling must occur in order to achieve uniqueness of labels. The
labeled product A⋆B of labeled classes A and B is formed by ﬁrst taking the
product of the underlying unlabeled classes, and then labeling in all possible
ways that are consistent with the order of labels on the component pieces. More
formally, if α ∈A and β ∈B then we say that the pair (α, β) is pair labeled if
the sizes of α and β sum to n and the atoms appearing in both elements of the
pair are together given distinct labels from [n]. If ρ is the reduction map that
takes an object of size k whose atoms have distinct labels from any subset of
N and reduces the labels to lie in [k], then the labeled product of A and B is
A⋆B = (α′, β′) : α ∈A, β ∈B, ρ(α′) = α, ρ(β′) = β; (α′, β′) is pair labeled	.
As in the unlabeled case, the size of a labeled pair is the sum of the sizes of its
elements.
Example 2.45 (Labeled product). The labeled product of the atomic class with
itself is the labeled class
Z2 = Z ⋆Z =
n
1 , 2

,

2 , 1
o
=
n
1 −2 , 2 −1
o
containing two elements of size two, where we draw elements of a tuple sepa-
rated by dashes to simplify notation. If A = {σ} is the labeled class containing
a single object, which is the set σ =
n
1 , 2
o
, then the labeled class Z2 × A
contains the six elements

1 −2 ,
n
3 , 4
o
,

1 −3 ,
n
2 , 4
o
,

1 −4 ,
n
2 , 3
o
,

2 −3 ,
n
1 , 4
o
,

2 −4 ,
n
1 , 3
o
,

3 −4 ,
n
1 , 2
o
,
coming from pair labelings (α′, β′) whose components reduce to ρ(α′) = 1 −
2 and ρ(β′) = σ, together with another six elements whose ﬁrst component
reduces to 2 −1 .
◁
If α ∈A has size k and β ∈B has size n −k then there are
n
k

elements
(α′, β′) ∈A ⋆B with ρ(α′) = α and ρ(β′) = β, since choosing the k labels
from [n] to give to the elements of α′ uniquely determines (α′, β′). Thus, the
2.5 Labeled classes
53
exponential generating function of C = A ⋆B is
C(z) =
X
n≥0
n
X
k=0
 n
k
!
|Ak| |Bn−k| zn
n!
=
X
n≥0
n
X
k=0
|Ak|
k! zk · |Bn−k|
(n −k)!zn−k
= A(z)B(z) ,
where A and B are the exponential generating functions of A and B. This
nice behavior is one reason why exponential generating functions are used for
labeled classes.
A labeled sequence construction is deﬁned analogously to the unlabeled
case. Because sequences can be represented in terms of disjoint union and
product, and the exponential generating functions of labeled classes behave the
same under these operations as ordinary generating functions do in the unla-
beled case, the exponential generating function of the sequence class SEQ(A)
for any labeled class A with no objects of size zero is still 1/(1 −A(z)).
Example 2.46 (permutations as labeled sequences). As discussed in Exam-
ple 2.44, the class of permutations has the labeled construction P = SEQ(Z),
so that P(z) = 1/(1−z). As a sanity check, we note that there are n![zn]P(z) = n!
permutations of size n.
◁
Finally, we introduce two new constructions, which can be used in the unla-
beled case but are much easier when dealing with labeled objects. Let A be a
labeled class with no objects of size zero and exponential generating function
A(z). The set class SET(A) is the labeled class containing all sets of objects in
A, which can be viewed as SEQ(A) after identifying tuples whose elements
diﬀer only by a permutation. Because there are k! ways to permute the elements
in a tuple of length k, the exponential generating function of B = SET(A) is
B(z) =
X
k≥0
A(z)k
k!
= eA(z) ,
where ez = exp(z) denotes the formal power series P
n≥1
zn
n!. Similarly, the cycle
class CYC(A) is the labeled class containing the elements of SEQ(A) after
identifying tuples whose elements diﬀer only by a cyclic shift. By convention,
we do not add an element of size zero to the cycle class. Because there are
k ways to cyclically shift the elements in a tuple of length k, the exponential
54
Generating functions
generating function of C = CYC(A) is
C(z) =
X
k≥1
A(z)k
k
= log
 
1
1 −A(z)
!
,
where log is the formal power series deﬁned by log
 1
1−z

= P
n≥1
zn
n .
Example 2.47 (permutations as labeled cycles). Viewing a permutation as a
set of disjoint cycles, the class of permutations has the labeled construction P =
SET(CYC(Z)), so that P(z) = exp
h
log
 1
1−z
i
. Comparing this to Example 2.46
gives a combinatorial proof that
exp
"
log
 
1
1 −z
!#
=
1
1 −z
as formal power series.
◁
Exercise 2.12. Prove the following statements for formal power series using
algebraic arguments.
• If A(0) = B(0) = 0 then eA(z)+B(z) = eA(z)eB(z).
• If A(0) = B(0) = 1 then log(A(z)B(z)) = log A(z) + log B(z).
• If A(0) = 0 then log(exp(A(z))) = A(z).
• If A(0) = 0 then exp(log(1 −A(z))) = 1 −A(z).
Often, we wish to track the size of the tuple that deﬁnes an element in a
sequence, set, or cycle class. If A is a labeled class with no objects of size
zero and exponential generating function A(z) then the semi-exponential gen-
erating function tracking the elements of SEQ(A) by size and tuple length
is
X
k≥0
ykA(z)k =
1
1 −yA(z) .
The term semi-exponential refers to the fact that the coeﬃcient of ykzn is di-
vided by n! but not by k!. Similarly, the semi-exponential generating function
for SET(A) is
X
k≥0
yk A(z)k
k!
= exp(yA(z))
and the semi-exponential generating function for CYC(A) is
X
k≥0
yk A(z)k
k
= log
1
1 −yA(z) .
We end by listing several examples of (semi-)exponential generating functions
that we return to in Chapter 3 when deriving asymptotics.
2.5 Labeled classes
55
Example 2.48 (permutations by number of cycles). Continuing Example 2.47,
the semi-exponential generating function for permutations enumerated by size
and number of cycles is
f(z, y) = exp
 
y log
1
1 −z
!
.
The entries of the bivariate sequence counting permutations of size n with k
cycles are called the Stirling numbers of the second kind.
◁
Example 2.49 (involutions). An involution is a permutation whose square is
the identity. Equivalently, an involution is a permutation with cycles of length
one or two. The exponential generating function for the class of cycles of
length one or two is z + z2/2, so the exponential generating function for the
class of involutions is exp(z + z2/2).
◁
Example 2.50 (set partitions). Let B = SEQ>0(Z) be the labeled class with a
single object of all sizes n ≥1 and no object of size zero, with exponential gen-
erating function g(z) = exp(z) −1. The labeled class exp(B), with exponential
generating function exp(ez −1), can be interpreted as the partitions of [n] into
nonempty sets. Tracking both the size and number of sets in these set partitions
gives the semi-exponential generating function exp(yg(z)) = exp(y(ez−1)). The
entries of the bivariate sequence counting partitions of [n] into k nonempty sets
are called the Stirling numbers of the ﬁrst kind.
◁
Example 2.51 (set partitions into tuples). If P>0 is the labeled class of nonempty
permutations, then SET(P>0) is the class of set partitions into tuples, contain-
ing sets {(x11, . . . , x1n1), . . . , (xk1, . . . , xknk)}, where each element of [n] appears
exactly once. The semi-exponential generating function F(y, z) for partitions
into tuples by size and number of sets is thus
F(y, z) = exp

y
z
1 −z

.
(2.12)
◁
Example 2.52 (2-regular graphs). A 2-regular graph is a simple graph (with
no loops or multiple edges) in which every vertex has degree 2. A labeled
2-regular graph is the union of labeled undirected cycles and, because we con-
sider simple graphs, every cycle has length at least three. The exponential gen-
erating function for undirected cycles of length at least three is
u(z) = 1
2
 
log
1
1 −z −z −z2
2
!
,
derived by taking the expression for all cycles and removing the terms for
56
Generating functions
cycles of length one and two, then dividing by 2 to account for orientation.
The exponential generating function for labeled 2-regular graphs is thus
eu(z) =
exp

−1
2z −1
4z2
√
1 −z
.
◁
Example 2.53 (surjections). A surjection of size n is any mapping from [n]
to a set [k] for any positive integer k. Because a surjection of size n onto [k]
can be viewed as the sequence ( f −1(1), . . . , f −1(k)) of nonempty sets, and the
exponential generating function of nonempty sets is ez −1, the exponential
generating function of surjections is 1/(2 −ez).
◁
A wide variety of additional combinatorial constructions, for labeled and
unlabeled classes, can be found in [FS09].
Notes
The transfer matrix method is classical, and discussed in [Sta97, Section 4.7]
and [GJ04, Chapter 2], among many other places. Our discussion of the ker-
nel method borrows liberally from [BP00]. The method itself, which appears
to have been re-discovered several times, has been taken much further; a his-
torical account and survey of recent results can be found in [Mel21, Section
4.2.1].
Several of our proofs in Section 2.4 are taken from [Sta99]. An earlier deﬁni-
tion of P-recursiveness appeared in the literature but it was discarded, due to its
failure to be equivalent to D-ﬁniteness; counterexamples are given in [Lip89].
Lipshitz’s Theorem replaced two earlier proofs [Ges81; Zei82] with gaps and
solved a problem of Stanley [Sta80, Question 4e]. Algorithms for ﬁnding a
diﬀerential equation satisﬁed by an algebraic function go back at least to Abel,
and work on eﬃcient algorithms for this purpose is still ongoing [Bos+07].
The approach of Exercise 2.14 is due to Comtet [Com64].
The method of Denef and Lipshitz [DL87] for expressing a d-variate alge-
braic function as the diagonal of a 2d-variate rational function is not, to our
knowledge, computationally eﬀective, as it relies on the existence of a gener-
ator for a certain type of ring extension. Further discussion can be found in
[AB13], which gives a diﬀerent, computationally eﬀective, embedding proce-
dure. Denef and Lipshitz also give an embedding as an M-diagonal in dimen-
sion d + 1, and they allow a wider range of substitutions than do the other
methods.
2.5 Labeled classes
57
By Theorem 2.30, the main diagonal of every rational function is a D-ﬁnite
univariate generating function. The converse is not true, but Christol conjec-
tured that every D-ﬁnite univariate function that satisﬁes a mild condition
called global boundedness is the main diagonal of some rational function (see
[Chr15] for a recent survey of progress). Rational diagonals occur very often
in applications: see, for instance, [Mel21, Ch. 3.4] for a list of interesting ex-
amples.
There are several methods for computing asymptotics of P-recursive se-
quences, which can be used to compute asymptotics for rational diagonal se-
quences, including the method of Frobenius for D-ﬁnite series and methods
arising from the work of Birkhoﬀand Trjitzinsky [WZ85]. The diﬃculty in
such work is typically expressing the sequence of interest as a linear combina-
tion of certain known series expansions, which is a type of connection problem.
In Chapter 8 we discuss how to combine methods for D-ﬁnite series and mul-
tivariate asymptotics to resolve the connection problem, and how to eﬀectively
compute with algebraic and D-ﬁnite series.
Moving on from D-ﬁnite series, one might consider the even larger class
of diﬀerentially algebraic series, deﬁned to be those that satisfy an equation
P(z, f, f ′, . . . , f (m)) = 0 for some positive integer m and some polynomial P.
The question of possible behaviors of the coeﬃcient sequence of such a func-
tion is wide open; some of the few known results are summarized in [Rub83;
Rub92]. Some negative results using model theory can be found in [MM08].
In the other direction, the theory of hypergeometric sequences is well de-
veloped. These are the coeﬃcients of univariate formal power series satisfying
a ﬁrst order linear recurrence with polynomial coeﬃcients (equivalently, they
are sequences where the ratio of successive coeﬃcients an+1/an is some ﬁxed
rational function of n), and hence correspond to a special subclass of D-ﬁnite
generating functions. A substantial algorithmic theory exists, well described at
an elementary level in the book [PWZ96].
Additional exercises
Exercise 2.13. A domino or dimer is a union of two unit squares along a
common edge. Let ank be the number of ways of placing k non-overlapping
dominoes on a 2 × n grid. Find the generating function enumerating {ank}.
Exercise 2.14. From the deﬁning algebraic equation for the Catalan number
generating function C(z) = P
n≥0 cnzn, derive a ﬁrst order linear diﬀerential
equation with polynomial coeﬃcients for C(z), and then a ﬁrst order linear
recurrence for cn. Use this to deduce an explicit formula for cn in terms of
58
Generating functions
factorials. Hint: After expressing C′ as a rational function A/B, use the fact
that B and the minimal polynomial P of C are relatively prime, and apply the
Euclidean algorithm to eventually express B−1(z) modulo P(z).
Exercise 2.15. Given a generating function F(x, y) in dimension d, consider
the monomial change of variables F(xayb, xcyd), where a, b, c, d ∈N. How
does the main diagonal of F relate to the r-diagonal for other values of r?
Exercise 2.16. Using the method shown in this chapter, obtain the generat-
ing function T(z) for the (2, 1)-diagonal {a2n,n} of the Delannoy numbers and
compare the algebraic complexity of T to the diagonal generating function in
Example 2.33.
Exercise 2.17. Let α ∈Nd represent a direction (with all coeﬃcients non-
zero and relatively prime). Show how to express the α-diagonal of the GF
F(z) = P
r∈Nd arzr as the main diagonal of a function related to F in a simple
way. Hint: Consider roots of unity.
Exercise 2.18. (a D-ﬁnite generating function) Let p0 = 1 and deﬁne {pn : n ≥
1} recursively by
pn =
1
3n + 1
2pn−1 +
n
X
j=2
p j−2pn−j
.
This sequence from [LP04] gives the probability that a genome in a certain
model due to Kaufmann and Levin cannot be improved by changing one al-
lele. Find a diﬀerential equation satisﬁed by the generating function f(z) =
P∞
N=0 pnzn, then use a computer algebra system to solve the resulting Riccati
equation explicitly in terms of Bessel functions. Among the solutions, ﬁnd the
only one that is analytic in a neighborhood of the origin.
Exercise 2.19. A left-to-right maximum (respectively right-to-left maximum)
of a permutation π of size n is a position i for which πi > π j for all j <
i (respectively all j > i). Derive an explicit formula for the bivariate semi-
exponential generating function that enumerates permutations by length and
number of left-to-right maxima. Then derive the trivariate generating function
that also counts right-to-left maxima.
Exercise 2.20. The Catalan generating function f(x) = (1 −
√
1 −4x)/(2x)
does not satisfy the hypotheses of Proposition 2.34. We can get around this by
multiplying by x, as in Example 2.35. Find another simple change to f that
allows Proposition 2.34 to be applied, and compare results.
Exercise 2.21. The Narayana numbers can be further reﬁned by considering
2.5 Labeled classes
59
diﬀerent types of leaves in a rooted ordered tree. Following [CDE06], we say
that the leaf of a tree is old if it is the leftmost child of its parent, and young oth-
erwise. The authors of [CDE06] enumerate such trees according to the number
of old leaves, number of young leaves and number of edges, ﬁnding the alge-
braic equation
G(x, y, z) = 1 +
z(G(x, y, z) −1 + x)
1 −z(G(x, y, z) −1 + y).
Use the embedding procedure above to express this as a diagonal of a 4-
variable rational function R. How exactly do we obtain the Narayana gen-
erating function from G? Does the embedding procedure commute with this
operation?
