---
doc_id: exploring-the-geometric-buchberger-algorithm-in-integer-prog
doc_title: "Exploring the Geometric Buchberger Algorithm in Integer Programming Gabriel Mattos Langeloh gmlangeloh@inf.ufrgs.br"
section_id: sec-003-3-the-binary-case
section_title: "THE BINARY CASE"
section_number: 3
pages: 3-4
source_pdf: Exploring the Geometric Buchberger Algorithm in Integer Programming.pdf
source_sha256: 73854bc5e3bcffb0
doc_brief: "Exploring the Geometric Buchberger Algorithm in Integer Programming Gabriel Mattos Langeloh gmlangeloh@inf.ufrgs.br — The Geometric Buchberger algorithm is a specialization of the clas- sical"
---
Many combinatorial optimization problems can be formulated as
integer programs with binary variables. Although the definition of
IP4-(b) does not explicitly allow the use of binary variables, one
can easily work with them by replacing the condition x; € {0, 1}
by a constraint of the form

xji+sj=1 (1)
with x;,s; € Z, where s; is an additional slack variable. In matrix
form, if A is the original constraint matrix involving binary vari-
ables and b is the original right-hand side vector, we need to solve
Par e(b’) with

>_ {A Omxn »_(% ri {e
ar=(i In ) v=(P), “= lon

where I, is the n X n identity matrix, 1, is a vector of n ones and
On; Omxn are respectively the zero vector and matrix of the specified
dimensions.

However, this turns a problem with n binary variables and m
constraints into a new problem with 2n variables and n + m con-
straints, and, as is well known, the size of a Grébner basis is very
sensitive to the number of variables of the problem. While it is pos-
sible to work with these n new slack variables implicitly, as shown
in [35], this does not affect the size of the output Grébner bases
and the amount of operations needed by the Geometric Buchberger
algorithm remains roughly the same, even though some memory is
saved. In this context, it is thus even more critical to use truncated
Grébner bases, as otherwise we allow arbitrary upper bounds for
each binary variable. This can be done even if multiple integer
programs in the family IP4,-(-) must be solved as long as an upper
bound of all the relevant right-hand sides b with respect to < is
available.

Interestingly, many steps of the Geometric Buchberger algorithm
can be specialized to binary variables. We start by showing an
efficient sufficient criterion for truncation in this context that can
be applied along the GCD and cancellation criteria for S-binomial
elimination.

THEOREM 3.1. If G is a partial Grébner basis obtained by the
Geometric Buchberger algorithm and g1, 92 € G, then h = S(g1, 92)
can be b’ -truncated whenever h; ¢ {-1, 0, 1}.

Proor. Suppose that h cannot be truncated, that is, deg 4, h < b’.
By definition, b’ — A’h* € Cyy, the set of feasible right-hand sides
for IP4/,¢’(-). Thus there exists a feasible solution x € Z2” such that
A’ (ht +x) =b.

From the form of A’ and b’, it follows that for all j = n+1,...,2n
(2)

+ + =
hj thin tx +Xj-n=1.
ISSAC 24, July 16-19, 2024, Raleigh, NC, USA

Because all terms in the left-hand side of Equation (2) are non-
negative, it follows that hy < 1 for all j € [2n]. The same argument
with deg, h = A’h” instead shows that hy < las well. a

Theorem 3.1 also leads to the following characterization of the
elements in a b’-truncated Grébner basis.

THEOREM 3.2. IfG is the reduced b’-truncated Grobner basis of
IP4’,01(b’) andg € G, then g; € {—1,0, 1} for alli € [2n].

Proor. Letg € Gand assume G was computed via the Geometric
Buchberger algorithm. Either g was in the input Markov basis for
the Geometric Buchberger algorithm and was not truncated, in
which case the proof of Theorem 3.1 shows that g € {—1,0, 1}2", or
g is the result of reducing some S-vector h. In this case, by Theorem
3.1, h € {-1,0,1}?".

Lemma 2.5 of [35] shows that the A’-degree keeps many prop-
erties of usual linear gradings of monomials. In particular, the A’-
degree is preserved by reductions, hence deg 4, h = deg 4, g.

Since g € kerzA’, gj = —9j4n for all j € [n], so either 9g; =
9j+n = 0 or exactly one of them is positive. Let j € [n] be any index
such that g; # 0. Then the (m + j)-th coordinate of deg 4, g is

(deg: 9)m+j = AnsjiG = Igjl
where A’, jis the (m + j)-th row of A’. A similar calculation for

deg 4, h shows that (deg 4, h)m+j = |hj|, thus |hj| = |g;|, proving
the theorem. a

Due to Theorem 3.2, we can represent the binary variables of
any g € G by a pair of bitsets, each representing one of the vec-
tors g*,g”. Furthermore, it is easy to detect whether S(g1, 92) €
{-1, 0, 1}2" via bitwise operations on these bitsets without actu-
ally computing S(g1, g2) in order to efficiently apply Theorem 3.1.
In fact, a direct calculation shows that supp gf M supp gz = 0 or
supp 9; supp g3 = 0 if and only if S(g1, 92) ¢ {-1,0, 1}?". Then,
the disjointness of these supports can be checked by a simple bitwise
AND of the corresponding bitsets. We summarize these conclusions
in Corollary 3.3 below.

CoROLLary 3.3 (BINARY TRUNCATION CRITERION). If G is a par-
tial b’ -truncated Grébner basis and g1, g2 € G then S(g1,g2) may be
truncated whenever supp a Nsupp gz # 9 orsupp g; Nsupp gq #0.

Proor. Assume without loss of generality that g; >¢ g2, that
supp 9} supp 9, # 9, and let i € supp a A supp 92 . By Theorem

3.2, the i-th coordinates of these elements are gi; = 1 and go; = —1.
It immediately follows that S(g1, 92); = 2 and so S(g1, g2) may be
eliminated by Theorem 3.1. a

It is possible that the representation of binary variables of G as
a pair of bitsets can be used to efficiently implement other basic
operations of the Geometric Buchberger algorithm, such as reduc-
tions, using bitwise logic. However, we have not implemented such
an approach yet.

The results above can be readily modified to apply only to the
binary variables whenever the integer program contains both inte-
ger and binary variables, since the proofs work variable by variable.
Note that in order to apply Theorems 3.1 and 3.2 it is necessary
to add the binary constraints (1) explicitly to the integer program,

337

Langeloh

even in cases where they would be otherwise unnecessary (such as
when they would be implied by other constraints).

Theorems 3.1 and 3.2 can also be generalized to arbitrary upper
bounds u; on each integer variable x;, so that h = $(g1, 92) can be
truncated whenever hj ¢ [—uj, uj] NZ and gj € [—uj, uj] NZ for all
G in the reduced b’-truncated Grébner basis. This generalization is
less useful for two reasons, however. First, there are fewer classical
combinatorial optimization problems where this hypothesis applies.
Second, and most importantly, the bitset representation of the sup-
ports leading to Corollary 3.3 cannot be used to efficiently check
whether the S-vector h can be truncated before it is computed. Thus,
checking this condition requires both computing h = g; — gz anda
further O(n) test and it is not clear whether this would lead to a
significant performance improvement in the Geometric Buchberger
algorithm.

Usually, the most costly part of the Geometric Buchberger algo-
rithm is the reducer search, that is, given u € kerz A and a partial
Grébner basis G, finding g € G such that gt < ut or proving
that no such g exists. We call support tree, following [25], the data
structure introduced in [22] to store G in order to make reducer
search efficient. A support tree is a binary tree where each internal
node has a label i with the interpretation that any vector g such
that i ¢ supp g* must be stored in the left subtree of the node, and
similarly, if i € supp g* then g must be stored in its right subtree.
Each leaf then contain the elements g € G with support given by
the sequence of labels found in the unique path from the root to
the leaf. Note that, in order to find a reducer for u, upon finding
an element g € G with supp g* C supp vu’, in general, one must
also check whether g* < u*, and backtrack to keep looking for a
reducer in case this condition is not satisfied. According to Theorem
3.1, this is unnecessary when working with binary variables, since
then supp g* € supp u* clearly implies g* < ut.

It is an open question whether other data structures that are
specialized for binary values, such as Zero-Suppressed Decision
Diagrams (ZDDs) [24] can be profitably used for more efficient
reducer search.
