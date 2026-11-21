---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-005-1-introduction
section_title: "Introduction"
section_number: 1
pages: 10-14
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
Introduction
The idea of concentration of measure was ﬁrst introduced by Milman in the asymp-
totic theory of Banach spaces [Milman and Schechtman, 1986]. The phenomenon
occurs geometrically only in high dimensions, or probabilistically for a large number
of random variables with suﬃcient independence between them. For an overview of
the history and some standard results, see [Ledoux, 2005].
A illustrative geometric example of concentration of measure occurs for the stan-
dard n-sphere Sn in Rn+1. If we let µn denote the uniform measure on Sn, then for
large enough n, µn is highly concentrated around the equator.
To see exactly what we mean by ”highly concentrated”, let us consider any mea-
surable set A on Sn such that µn(A) ≥1/2. Then, if we let d(x, A) be the geodesic
distance between x ∈Sn and A, we deﬁne the expanded set
At = {x ∈Sn ; d(x, A) < r}
At contains all points of A in addition to any points on Sn with a geodesic distance
less than r from A. The precise inequality that can be obtained says that
µn(Ar) ≥1 −e−(n−1)r2/2
In other words ”almost” all points of the sphere are within distance of
1
√n from our
set A. Obviously as n →∞, this quantity because inﬁnitesimal. This example is due
to Gromov, and more discussion can be found in [Gromov, 1980].
Gromov’s work on concentration on the sphere was inspired by L´evy’s work [L´evy
and Pellegrino, 1951] on concentration of functions. Suppose we have a function F,
which is continuous on Sn with a modulus of continuity given by ωF(t) = sup{|F(x)−
F(y)| : d(x, y) ≤t}. Let mF be a median for F, which by deﬁnition means that
µn(F ≥mF) ≥1/2 and µn(F ≤m) ≥1/2. Then we have
µn({|F −mF| ≥ωF(t)}) ≤2e−(n−1)t2
While these geometric examples give a nice introduction to the phenomenon, in
this work we will mainly be interested in concentration of measure in a probabilis-
tic setting. Let us give a simple example that will give some intuition about how
concentration of measure comes up in probability.
Suppose we have independent
random variables X1, X2, . . . , Xn. Suppose that they take the values 1 and −1, each
with probability 1/2. For each n ≥1, let Sn = Pn
i=1 Xi. Since E(Xi) < ∞(in fact
E(Xi) = 0), the strong law of large numbers tells us that Sn/n converges almost
surely to E(Xi) as n →∞. Remember that this means that
P

lim
n→∞
Sn
n = E(Xi)

= 1
Moreover, by the central limit theorem, we know that
 Sn
√n

d−→N(0, σ2)
where σ2 is the variance of each Xi, which in this case is 1. This shows us that the
ﬂuctuations of Sn are of order n. However, notice that |Sn| can take values as large
as n. If we measure Sn using this scale, then Sn
n is essentially zero. The actual bound
looks like
P
|Sn|
n
≥r

≤2e−nr2/2
for r > 0. See [Talagrand, 1996] for a proof. As Talagrand points out, concentration
of measure appears in a probabilistic setting by showing that one random variable
that depends in a smooth enough way on many other independent random variables
is close to constant, provided that it does not depend too much on any one of the
independent random variables. As we will see later in this work, it turns out that this
idea still holds true if we have a random variable that depends on a large number of
”almost” independent random variables. We will later see an instance of a random
variable that depends on many weakly correlated random variables. It requires a
little more work to prove concentration of measure, but often, it is still possible.
This work is divided into chapters. Chapter 2 introduces Talagrand’s Gaussian
concentration of measure inequality, Talagrand’s isoperimetric inequality, Ledoux’s
concentration of measure on Markov chains, and the Euler-Maclaurin formula. A
statement and proof of each theorem (with the exception of the Euler-Maclaurin for-
mula) is also given, to make this work as self-contained as possible. In later chapters,
we will see new applications of each of these results. Chapter 3 introduces several
new results using Ledoux’s concentration of measure inequality on reversible Markov
chains. We are able to generalize a method ﬁrst used by Chatterjee and Ledoux [Chat-
terjee and Ledoux, 2009] to prove concentration of measure for two diﬀerent random
operator compressions. We also show how to use this method to obtain concentration
of measure bounds for the length of the longest increasing subsequence of a random
walk evolving under the asymmetric exclusion process. To give more meaning to our
ﬂuctuation bounds, we also derive a lower bound for the length of this longest increas-
ing subsequence. It turns out that we can use Talagrand’s isoperimetric inequality
to do this, even though our random variables have weak correlations. In Chapter
4, we discuss a method for calculating the mixed matrix moments in the Ginibre
random matrix ensemble using techniques from spin glasses. In addition, we use the
mixed matrix moments to compute asymptotics of the overlap functions (introduced
by Chalker and Mehlig [Chalker and Mehlig, 1998]) for eigenvectors corresponding
to eigenvalues near the edge of the unit circle.
We propose an adiabatic method
for computing explicit formulas for the eigenvector overlap functions. In Chapter 5,
we use the Euler-Maclaurin formula to prove a q-deformed Stirling’s formula. We
demonstrate a use of the q-Stirling’s formula to obtain asymptotics for point counts
in a four square problem. We also discuss techniques and algorithms to simulate a
Mallows random permutation.
2
