---
doc_id: arxiv-1804.10084v1
doc_title: "Concentration of Lipschitz Functions of Negatively Dependent Variables"
section_id: sec-002-2-notions-of-negative-dependence
section_title: "Notions of negative dependence"
section_number: 2
pages: 1-3
source_pdf: 1804.10084v1.pdf
source_sha256: 716da9708f06d930
---
tionships. In particular, he posed the question whether there is a r obust notion of negative depen-
dence, closed under natural operations, and allowing one to replica te some of the theory enjoyed
by independent random variables or positively dependent variables ( such as the FKG inequality).
Meanwhile, Dubhashi and Ranjan [5] studied in depth the scenario of balls and bins , and proved
that the respective random variables satisfy several notions of n egative dependence. Among other
1A function f : {0,1}n → R is c-Lipschitz, if each variable can aﬀect the value additively by at most c.
1
results, they stated a concentration bound for any Lipschitz fun ction of random variables satisfy-
ing the property of negative regression. This was a rare example of a concentration inequality for
non-linear functions of negatively dependent variables that can be found in the literature — unfor-
tunately, it turns out that their proof was erroneous (see Appen dix A for details). Later, Farcomeni
[6] studied concentration bounds under a weaker notion of negativ e dependence (which reduces to
negative cylinder dependence in the case of {0, 1} random variables) and claimed a concentration
inequality for Lipschitz functions of such variables. Unfortunately , his proof again turned out to be
incorrect, as reported by [13]. In that work, Pemantle and Peres [13] proved a concentration bound
for Lipschitz functions under strong Rayleigh measures , a strong notion of negative dependence
which implies all the other notions discussed in this paper. Their proof relies on the theory of
stable polynomials [2].
Let us mention that special-purpose tail inequalities have been prov ed for submodular functions
and matrix norms under a particular randomized rounding scheme on matroid polytopes [4, 8].
While this is a natural setting where negatively dependent variables a rise, it is not known how to
generalize these concentration bounds to any general notion of n egative dependence.
Organization. In Section 2, we survey several notions of negative dependence a nd their relation-
ships. In Section 3, we provide a corrected proof of the concentr ation bound for Lipschitz functions
of random variables under the assumption of negative regression. This is the main contribution of
this paper. In Appendix A, we explain where the proof of [5] fails and discuss a counterexample
that motivated our proof.
2 Notions of negative dependence
Let us survey here several notions of negative dependence and t heir known relationships. In this
paper, we restrict attention to (correlated) Bernoulli random va riables, i.e. probability measures on
{0, 1}n.
Pairwise Negative Correlation. This is the weakest notion of negative dependence consid-
ered here. Variables X1, . . . , X n are pairwise negatively correlated, if
Cov[Xi, X j] = E[XiXj] − E[Xi]E[Xj] ≤ 0
for all i, j ∈ [n]. Pairwise negative correlation allows one to use Chebyshev’s inequalit y, but it is
too weak to imply exponential tail bounds. For example, n pairwise independent variables deﬁned
by the n × n Hadamard matrix have probability Ω(1 /n ) of being all equal to 1.
Negative Cylinder Dependence. X1, . . . , X n are negative cylinder dependent, if for every
S ⊆ [n],
E[
∏
i∈S
Xi] ≤
∏
i∈S
E[Xi]
and
E[
∏
i∈S
(1 − Xi)] ≤
∏
i∈S
E[1 − Xi].
Negative cylinder dependence is strictly stronger than pairwise neg ative correlation. It is known to
imply exponential concentration bounds for linear functions of X1, . . . , X n.
Negative Association. X1, . . . , X n are negatively associated if for any I, J ⊂ [n], I ∩ J = ∅
and any pair of non-decreasing functions f : {0, 1}I → R, g : {0, 1}J → R,
E[f (XI )g(XJ )] ≤ E[f (XI )]E[g(XJ )].
2
(Here and in the following, XS ∈ {0, 1}S denotes the |S|-tuple of random variables indexed by S.)
Negative association is strictly stronger than negative cylinder dep endence. Whether nega-
tive association implies exponential concentration bounds for Lipsc hitz functions is an interesting
question (posed by Elchanan Mossel [13] and still open as far as we k now).
Negative Regression. X1, . . . , X n satisfy negative regression, if for any I, J ⊂ [n], I ∩ J = ∅,
any non-decreasing function f : {0, 1}I → R and a ≤ b ∈ {0, 1}J,
E[f (XI ) | XJ = a] ≥ E[f (XI ) | XJ = b].
Negative regression is the main subject of this paper; we prove a co ncentration bound for Lipschitz
functions under negative regression here. The relationship of neg ative association and negative
regression is not completely understood. It is known that negative association does not imply
negative regression [5] but the status of the opposite implication is u nknown. Negative regression
is preserved under conditioning of variables, while negative associat ion is not. It is easy to see that
both properties are implied by the following.
Conditional Negative Association. X1, . . . , X n are conditionally negatively associated, if
for any I ⊂ [n] and a ∈ {0, 1}I, ( Xj : j ∈ [n] \ I) conditioned on XI = a are negatively associated.
Pemantle [12] conjectured that conditional negative association is equivalent to negative re-
gression. He also deﬁned several related notions that entail the “ negative lattice condition” (log-
submodularity) and “external ﬁelds”. We will not discuss these her e.
Stochastic Covering. X1, . . . , X n satisfy the stochastic covering property, if for any I ⊂ [n]
and a ≥ a′ ∈ { 0, 1}I such that ‖a′ − a‖1 = 1, there is a coupling ν of the distributions µ, µ ′ of
(Xj : j ∈ [n] \ I) conditioned on XI = a or XI = a′, respectively, such that ν(x, y ) = 0 unless x ≤ y
and ‖x − y‖1 ≤ 1.
This property is discussed in [13]. It is stronger than negative regr ession (which is equivalent
to a similar coupling condition, without the requirement that the coup ling is supported on pairs of
distance at most 1; this follows from Strassen’s theorem as we discu ss further).
The Strong Rayleigh Property . X1, . . . , X n satisfy the strong Rayleigh property if the
generating function F (z1, . . . , z n) = E[∏ n
j=1 zXj
j ] is a real stable polynomial, which means it has no
root ( z1, . . . , z n) ∈ Cn with all imaginary components strictly positive.
The strong Rayleigh property is intimately tied to the theory of stab le polynomials, and it was
shown in [2] to imply all the other forms of negative dependence discu ssed above. Hence, it can
be viewed as a very strong and robust notion of negative dependen ce — it is closed under several
natural operations, and exhibits a number of other desirable prop erties. Particularly relevant to this
paper is the result of [13] that any Lipschitz function of random var iables under a strong Rayleigh
measure satisﬁes concentration bounds similar to independent ran dom variables. Furthermore,
[13] also proves a concentration bound for Lipschitz functions for homogeneous random variables
(∑ n
i=1 Xi = k for some constant k, with probability 1) satisfying the stochastic covering property.
