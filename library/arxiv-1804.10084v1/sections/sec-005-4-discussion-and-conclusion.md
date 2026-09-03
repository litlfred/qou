---
doc_id: arxiv-1804.10084v1
doc_title: "Concentration of Lipschitz Functions of Negatively Dependent Variables"
section_id: sec-005-4-discussion-and-conclusion
section_title: "Discussion and conclusion"
section_number: 4
pages: 8-10
source_pdf: 1804.10084v1.pdf
source_sha256: 716da9708f06d930
---
Let us discuss brieﬂy the notion of negative regression and how it re lates to other notions of negative
dependence. It is fair to say that most known examples that satisf y negative association or nega-
tive regression actually satisfy the strong Rayleigh property as we ll. For example, random variables
arising in the context of random spanning trees, determinantal po int processes and exclusion dy-
namics processes are in this category. However, there are ensem bles of random variables satisfying
negative regression and not stronger notions of negative depend ence. We want to mention a few
examples here.
Random variables conditioned on their sum. It is known that if X1, . . . , X n are in-
dependent, then the probability measure of ( X1, . . . , X n) conditioned on ∑ n
i=1 Xi = k is strongly
Rayleigh, for any ﬁxed k. The probability measure conditioned on ∑ n
i=1 Xi ∈ { k, k + 1} is still
strongly Rayleigh. Conditioning on ∑ n
i=1 Xi ∈ [a, b ] does not preserve the strong Rayleigh condi-
tion in general [2]. However, such ensembles still satisfy negative re gression [12]. More generally,
ensembles produced from independent random variables by taking p roducts, “external ﬁelds” and
“rank rescaling” satisfy negative regression; we refer the reade r to [12] for a precise statement and
proof.
V ariables of large inﬂuence. As we remarked, [13] also handles the case of random variables
satisfying the stochastic covering property and homogeneity, i.e. the condition ∑ n
i=1 Xi = k. The
case of conditioning on ∑ n
i=1 Xi ∈ [a, b ] is not covered by their theorem, although we believe that
their method would still apply. However, what seems signiﬁcantly bey ond the scope of stochastic
covering is the case of random variables where one variable can have a large eﬀect on the remaining
variables. (Under stochastic covering, conditioning on one variable can change the expected sum
of the remaining variables by at most 1.) An example of such a measure is our counterexample in
Appendix A; this counterexample illustrates what the issue was in the previously claimed proof,
and also this is the main hurdle that our proof had to overcome.
The main question that this paper leaves open is whether similar conce ntration bounds still
hold for Lipschitz functions of negatively associated variables.
References
[1] Alexander Ageev and Maxim Sviridenko. Pipage Rounding: A new met hod of constructing
algorithms with proven performance guarantee. J. Comb. Optim. 8:3, 307–328, 2004.
[2] Julius Borcea, Petter Br¨ and´ en and Thomas M. Liggett. Negative dependence and the geometry
of polynomials. J. AMS 22, 521–567, 2009.
[3] Chandra Chekuri, Jan Vondr´ ak and Rico Zenklusen. Dependent randomized rounding via
exchange properties of combinatorial structures. In FOCS, 575–584, 2010.
8
[4] Chandra Chekuri, Jan Vondr´ ak and Rico Zenklusen. Dependent randomized rounding for
matroid polytopes and applications. arXiv:0909.4348, 2009.
[5] Devdatt Dubhashi and Desh Ranjan. Balls and bins: a study in neg ative dependence. Random
Structures Algorithms 13:2, 99–124, 1998.
[6] Alessio Farcomeni. Some ﬁnite sample properties of negatively dep endent random variables.
Theory Prob. Math. Statist. 77, 155–163, 2008.
[7] Rajiv Gandhi, Samir Khuller, Srinivasan Parthasarathy and Aravin d Srinivasan. Dependent
rounding and its applications to approximation algorithms. J. ACM 53:3, 324–360, 2006.
[8] Nicholas J. A. Harvey and Neil Olver. Pipage rounding, pessimistic e stimators and matrix
concentration. In SODA, 926–945, 2014.
[9] Colin McDiarmid. On the method of bounded diﬀerences. In Surveys in Combinatorics ,
London Mathematical Society Lecture Note Series , Vol. 141, 148–188. Cambridge University
Press, 1989.
[10] Charles M. Newman. Asymptotic independence and limit theorems for positively and nega-
tively dependent random variables. Inequalities in statistics and probability , Y. L. Tong, Editor.
I. M. S. Lecture notes-monograph series , Vol. 5, 127–140, 1984.
[11] Alessandro Panconesi and Aravind Srinivasan. Randomized dist ributed edge coloring via an
extension of the Chernoﬀ-Hoeﬀding bounds. SIAM J. Comput. 26:2, 350–368, 1997.
[12] Robin Pemantle. Towards a theory of negative dependence. J. Math. Phys. 41, 1371–1390,
2000.
[13] Robin Pemantle and Yuval Peres. Concentration of Lipschitz fu nctionals of determinantal and
other strong Rayleigh measures. Combin. Probab. Comput. 23:1, 140–160, 2014.
[14] Yuval Peres, Mohit Singh and Nisheeth Vishnoi. Random walks in po lytopes and negative
dependence. In ITCS 2017 .
A The failure of a ﬁxed ordering
Here we review brieﬂy the argument presented in [5] and why it is ﬂawe d. In Proposition 31, [5]
states Theorem 1 under the assumption of f being monotone and Lipschitz with constant ci in
variable Xi; here let us assume ci = 1. The proof proceeds by deﬁning Yk = E[f (X) | X1, . . . , X k]
(using our notation) and claiming that this martingale has bounded diﬀ erences. In the last line of
the proof, it is claimed that “Similarly it follows that . . . ”. However, th e desired inequality does
not follow by the same argument, and can be false.
Example. Consider the following random variables X1, . . . , X n: X2, . . . , X n are independent and
uniformly random in {0, 1}. X1 is the NAND function of X2, . . . , X n, i.e., X1 = 1 − ∏ n
i=2 Xi. Note
that Pr[ X1 = 1] = 1 − 1/ 2n−1. We claim that X1, . . . , X n satisfy negative regression:
Let I, J ⊂ [n] be disjoint and a ≤ b ∈ {0, 1}J. We consider the following cases:
• If 1 /∈ I ∪ J, then there is no dependence between XI and XJ .
• If 1 ∈ I, then the distribution of XI diﬀers under XJ = a, b only if a ⁄= 1 J and b = 1 J . In
this case, the XJ = b is consistent with Xi = 0 or Xi = 1, while XJ = a implies X1 = 1.
The other variables in I are independent of XJ . Hence, conditioning on XJ = a as opposed
to XJ = b can only increase the expectation of any monotone function f (XI).
• If 1 ∈ J, then the distribution of XI diﬀers under XJ = a, b only if a1 = 0 and b1 = 1. In this
case, XI = a implies that all the other variables are equal to 1, while XI = b is consistent
with any assignment to the other variables except all 1’s. Therefor e, conditioning on XJ = a
as opposed to XJ = b can only increase the expectation of any monotone function f (XI).
9
Now consider the martingale Y0, Y 1, . . . , Y n, where Yk = E[f (X) | X1, . . . , X k] for f (X) =∑ n
i=1 Xi.
Y0 = E[f (X)] =
n∑
i=1
E[Xi] = (1 − 1
2n−1 ) + 1
2 (n − 1) = 1
2 (n + 1) − 1
2n−1 .
If X1 = 0 (which happens with probability 1 / 2n−1), this implies that all the remaining variables
are equal to 1, which means that Y1 = n − 1. Therefore, the diﬀerence between Y0 and Y1 can be
Ω( n). Clearly, the issue here is the enormous inﬂuence of X1 via its correlation with the remaining
variables, and this is what motivates our adaptive ordering of variab les.
10
