---
doc_id: s00453-026-01372-w
doc_title: "Concentration of Submodular Functions and Read-k Families Under Negative Dependence"
section_id: sec-010-acknowledgements
section_title: "Acknowledgements"
section_number: null
pages: 12-17
source_pdf: s00453-026-01372-w.pdf
source_sha256: 98b569eff84fb489
toc_source: outline
doc_brief: "Concentration of Submodular Functions and Read-k Families Under Negative Dependence — We study the question of whether submodular functions of random variables satisfying various notions of negative"
---
Author Contributions All ﬁve authors participated in discussion of the proofs, reviewed and approved the
ﬁnal version of the manuscript.
Funding All authors were supported in part by NSF award number CCF-1918749.
Data Availability No datasets were generated or analysed during the current study.
Declarations
Competing interests Funding: All authors were supported in part by NSF award number CCF-1918749.
Employment: Afﬁliation with University of Maryland, College Park, and Carnegie Mellon University
OpenAccess ThisarticleislicensedunderaCreativeCommonsAttribution4.0InternationalLicense,which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence,
and indicate if changes were made. The images or other third party material in this article are included
in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If
material is not included in the article’s Creative Commons licence and your intended use is not permitted
by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the
copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
Algorithmica (2026) 88:21 Page 130f19 21

A 1-Negative Association and Weak Negative Regression

In the following lemmata, we show that weak negative regression implies 1-negative
association in general. We then show that the reverse implication holds for binary
random variables, but give an example showing that it does not hold in general.

Claim A.1 Jf a collection of random variables X,,..., Xn satisfies weak negative
regression, then it satisfies 1-negative association.

Proof Assume X1,..., Xn satisfy weak negative regression; we will prove that it
also satisfies 1-negative association. Let f and g be monotone functions such that f
depends on X; for some subset J C [n] and g depends on X; fori ¢ J. Without loss
of generality, let us assume that f and g are non-decreasing.

First, define the function F(a) = E[ f(X)|X; = a]. Evaluating the expectation
E[ f (X7)g(X;)], we can express it via the law of total expectation as

EL f(X1)g(Xi))] = ElE[f (X1)|Xilg(Xi)] = EL F(X) g (Xi).

Next, we observe that by the definition of weak negative regression, F(a) is non-
increasing. Therefore, random variables F(X;) and g(X;) are negatively correlated,
yielding

ELF(X;)g@(Xi)] < ELF (X,)JElg(X3)].

Converting E[ F (X;)] back into the terms of f and g, we find
EL F(X) Ele (Xi)] = ELf(X)JELg(X)].

The overall inequality E[ f(X7)g(Xi)] < El f(X1)JE[g(X;)] thus holds, which estab-
lishes that X;,..., X, are 1-negatively associated, completing the proof. Oo

Claim A.2 If a collection of binary random variables X\,..., Xn satisfies 1-negative
association, then it satisfies weak negative regression.

Proof Recall that we wish to prove that for any non-decreasing function f depending
on some subset J C [n] and any i ¢ J, we have that

EL f(X7)|Xi = 0) = EL f(X7)|X; = U-

By the definition of 1-negative association, we obtain that for any monotone functions
g which depends on X;, the following inequality holds:

EL f(X)g(Xi)] Ss ELf(X))] - Elg(X)]- (10)

Without loss of generality, we may assume that E[ f (X7)|X; = 1] = 0 by shifting f
by aconstant. By choosing g to be the identity function, we can apply the law of total
probability to obtain

ELf(X7) - (XA) = PrlX; = 01 -ELf(XDIX; = 01 8)
+ Pr[X; = 1) -ELf (XIX; = 1]- g(1) =0.

cay Springer
21
Page 14 of 19
Algorithmica (2026) 88 :21
Plugging this into Equation 10, we obtain
0 ≤E[ f (X I)] · E[g(Xi)] = E[ f (X I)|Xi = 0] Pr[Xi = 0] · E[Xi],
again by the law of total probability. Since E[Xi] > 0 and Pr[Xi = 0] > 0, this
implies that
E[ f (X I)|Xi = 0] ≥0,
which concludes the proof since E[ f (X I)|Xi = 1] = 0.
⊓⊔
Claim A.3 There exists (non-binary) distributions over 2 random variables which sat-
isfy1-negativeassociationbut not weaknegativeregression. Inother words, 1-negative
association is strictly more general than weak negative regression for non-binary ran-
dom variables.
Proof Let’s ﬁrst discuss the intuition for the construction of the counterexample. One
can show via algebra that E[ f (X I)g(Xi)] −E[ f (X I)]E[g(Xi)] can be expanded as
the following expression:

x<y Pr[Xi = x] Pr[Xi = y]·

E[ f (X I)|Xi = x]−E[ f (X I)|Xi = y]

g(x)−g(y)

,
where the summation is over the values that Xi takes with non-zero probability.
Now, suppose that for some values x < y we have that
E[ f (X1, . . . , Xn)|Xi = x] −E[ f (X1, . . . , Xn)|Xi = y] < 0,
violating the weak negative regression property. This would imply that some of the
summands are positive (since g(x) < g(y) by monotonicity). In the case of binary ran-
dom variables, the summation would only consist of a single summand so 1-negative
association would be violated. For general random variables, the summation consists
of multiple terms so the summation may still be negative even when a single summand
is positive. Consequently, the random variables may still satisfy 1-negative association.
We now give the example. Consider the random variables (X1, X2) which are uni-
formly distributed on their support set {(0, 3), (1, 1), (2, 2), (3, 0)}. By considering an
identity function 1x : {0, 1, 2, 3} →{0, 1, 2, 3}, we can show that that the distribution
of (X1, X2) does not satisfy weak negative regression:
E[1x(X2)|X1 = 1] = 1x(1) = 1 < 2 = 1x(2) = E[1x(X2)|X1 = 2].
However, for any pair of non-decreasing functions f , g : {0, 1, 2, 3} →R, we have
E[ f (X1)]E[g(X2)] −E[ f (X1)g(X2)]
= f (1) + f (2) + f (3)
4
· g(1) + g(2) + g(3)
4
−f (1)g(1) + f (2)g(2)
4
,
where we have again assumed without loss of generality that f (0) = g(0) = 0.
Algorithmica (2026) 88 :21
Page 15 of 19
21
We claim that the quantity on the right hand side is always non-negative. In order
to see this, observe that f (2)g(2) ≤f (i)g( j) for any i, j ≥2 by monotonicity. As a
result, we have
f (2)g(2)
4
≤( f (2) + f (3))(g(2) + g(3))
16
.
Further, we observe that f (1)g(1) ≤f (i)g( j) for any i, j ≥1 by monotonicity. As
a result, we have
f (1)g(1)
4
≤f (1)(g(2) + g(3)) + g(1)( f (2) + f (3))
16
.
Combining these two inequalities immediately and observing that f (1)g(1) ≥0
by monotonicity implies our desired result. Hence, the distribution is 1-negatively
associated.
⊓⊔
Since 1-negative association and weak negative regression are equivalent for binary
random variables and weak negative regression has been shown to be strictly stronger
than cylinder negative dependence [1, Proposition 2.4], we also have that 1-negative
association is strictly stronger than cylinder negative dependence. Additionally, since
weak negative regression is strictly stronger than 1-negative association for general
random variables and weak negative regression has been shown to be strictly weaker
than negative association and negative regression [1, Proposition 2.4], we have that
1-negative association is strictly weaker than negative association and negative regres-
sion. We summarize these in the following corollaries.
Corollary A.4 1-negative association is a strictly weaker condition than negative asso-
ciation.
Corollary A.5 1-negative association is a strictly weaker condition than negative
regression.
Corollary A.6 1-negative association is a strictly stronger condition than negative
cylinder dependence.
B Concentration of Read-k Families
We will give a new simpler proof of the results of Gavinsky et al. [4] using exponential
moments for f j for independent random variables X1, . . . , Xn. Our proof will use the
following lemma
Lemma B.1 For an arbitrary read-k family F1, . . . , Fn, we have
E

n
j=1 Fj

≤
n
j=1 E

Fk
j

	1/k
.
(11)
Using this lemma, if we deﬁne
Fj = exp(λ · f j(X1, . . . , Xm)),
21
Page 16 of 19
Algorithmica (2026) 88 :21
it is easy to see that F1, . . . , Fn are a read-k family since f1, . . . , fn are read-k. We
will show later that after applying inequality (11) on F1, . . . , Fm, we can adapt the
standard Chernoff bound proof to our case.
Proof We will prove inequality (11) via induction on the number of independent
variables m. For the base case m = 1, observe that there are at most k non-constant
functions Fj by deﬁnition. If there are fewer than k functions Fj, we can also add
identity functions without changing the product. As a result, we can without loss of
generality assume that there are exactly k functions Fj. The inequality then follows
directly by the Generalized Hölder’s Inequality.
Now assume we have proven the statement for m independent variables; we will
try to prove it for m + 1. Again, let S = S1 denote the set of functions Fj which are
inﬂuenced by X1. We have
E

n
j=1 Fj

= E


j∈S Fj · 
j /∈S Fj

= E

E


j∈S Fj · 
j /∈S Fj

X2, . . . , Xm+1

= E

E


j∈S Fj

X2, . . . , Xm+1

· 
j /∈S Fj

(12)
Here, the ﬁrst equality is obvious, the second equality follows by the law of total expec-
tation, and the third equality follows since Fj for j /∈S only depends on X2, . . . , Xm+1
and is independent of X1.
After taking the conditional expectation, observe that E[
j∈S Fj|X2, . . . , Xm+1]
is a random variable which only depends on X2, . . . , Xm+1. In particular, these form
a read-k family over m random variables, so we can apply the inductive hypothesis to
claim that
E


j∈S Fj|X2, . . . , Xm+1

≤

j∈S E

Fk
j |X2, . . . , Xm+1

	1/k
After combining this with equation (12), we have
E

n
j=1 Fj

≤E


j∈S E

Fk
j |X2, . . . , Xm+1

1/k
· 
j /∈S Fj

=: A
For j /∈S, let G j = Fj and for j ∈S, deﬁne
G j = E

Fk
j |X2, . . . , Xm+1

1/k
so that A
=
E

n
j=1 G j

. Observe that G j are again a read-k family on
X2, . . . , Xm+1, so we can again apply the induction hypothesis to claim that
A = E

n
j=1 G j

≤n
j=1 E

Gk
j

1/k
= n
j=1 E

Fk
j

1/k
,
Algorithmica (2026) 88 :21
Page 17 of 19
21
where the ﬁnal equality follows directly by deﬁnition of G j. This completes the proof.
⊓⊔
Using the lemma, we can follow the standard Chernoff bound techniques to com-
plete the proof. Let X = n
j=1 f j(X1, . . . , Xm); we can apply Markov’s inequality
for any λ < 0 to obtain
Pr[X ≤qn] = Pr[exp(λX) ≥exp(λqn)] ≤exp(−λqn) · E

exp(λX)

As mentioned before, we can take Fj = exp(λ· f j(X1, . . . , Xm)) and apply inequality
(11) to obtain that
exp(λX) = E

n
j=1 Fj

≤n
j=1 E[Fk
j ]1/k.
Combining this inequality with the previous inequality, we now have that
Pr[X ≤qn] ≤exp(−λqn) · n
j=1 E[Fk
j ]1/k =
n
j=1 E

[Fj/ exp(λq)]k	1/k
.
Writing out the deﬁnition of Fj, we have
[Fj/ exp(λq)]k = exp(λk · f j(X1, . . . , Xm))/ exp(λkq).
Deﬁne λ′ = λk; since λ was arbitrary, we will abuse notation and let λ = λ′. Com-
bining the two previous inequalities, we have that
Pr[X ≤qn] ≤
n
j=1 E[exp(λ · f j)/ exp(λq)]
	1/k
.
Here, the right-hand side is in exactly the same form as in the proof of the Chernoff-
Hoeffding theorem under independence, except with an additional exponent 1/k. As
a result, we can follow the Chernoff-Hoeffding proof and take q = p −ϵ to obtain
Pr[X ≤(p −ϵ)n] ≤exp(−D(p −ϵ||p) · n/k),
which was our desired result.
