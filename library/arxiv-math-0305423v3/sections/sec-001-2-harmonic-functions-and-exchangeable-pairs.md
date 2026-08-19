---
doc_id: arxiv-math-0305423v3
doc_title: "Stein’s Method and Plancherel Measure of the Symmetric Group"
section_id: sec-001-2-harmonic-functions-and-exchangeable-pairs
section_title: "Harmonic functions and exchangeable pairs"
section_number: 2
pages: 5-8
source_pdf: 0305423v3.pdf
source_sha256: e4554f9084ba4935
doc_brief: "Stein’s Method and Plancherel Measure of the Symmetric Group — We initiate a Stein’s method approach to the study of the Plancherel measure of the symmetric group."
---
To begin we recall the theory of harmonic functions on Bratel li diagrams.
This is a beautiful subject with deep connections to probabi lity theory and
representation theory. Two excellent surveys are [K2] and [ BO].
The basic set-up is as follows. One starts with a Bratteli dia gram; that
is an oriented graded graph Γ = ∪n≥0Γ n such that
(1) Γ 0 is a single vertex ∅.
(2) If the starting vertex of an edge is in Γ i, then its end vertex is in
Γ i+1.
(3) Every vertex has at least one outgoing edge.
(4) All Γ i are ﬁnite.
For two vertices λ, Λ ∈ Γ, one writes λ ր Λ if there is an edge from λ
to Λ. Part of the underlying data is a multiplicity function κ(λ, Λ). Let-
ting the weight of a path in Γ be the product of the multiplicit ies of its
edges, one deﬁnes the dimension dim(Λ) of a vertex Λ to be the sum of the
weights over all maximal length paths from ∅ to Λ; dim(∅) is taken to be 1.
Given a Bratteli diagram with a multiplicity function, one c alls a function
φ harmonic if φ(∅) = 1, φ(λ) ≥ 0 for all λ ∈ Γ, and
φ(λ) =
∑
Λ: λ րΛ
κ(λ, Λ)φ(Λ).
An equivalent concept is that of coherent probability distr ibutions. Namely
a set {Mn} of probability distributions Mn on Γ n is called coherent if
Mn(λ) =
∑
Λ: λ րΛ
dim(λ)κ(λ, Λ)
dim(Λ) Mn+1(Λ).
The formula allowing one to move between the deﬁnitions is φ(λ) = Mn(λ )
dim(λ ) .
One reason the set-up is interesting from the viewpoint of pr obability
theory is the fact that every harmonic function can be writte n as a Poisson
integral over the set of extreme harmonic functions (i.e. th e boundary). For
the Pascal lattice (vertices of Γ n are pairs ( k,n ) with k = 0, 1, · · ·,n and
(k,n ) is connected to ( k,n + 1) and (k + 1,n + 1)), this fact is the simplest
instance of de Finetti’s theorem, which says that an inﬁnite exchangeable
sequence of 0 − 1 random variables is a mixture of coin toss sequences for
diﬀerent probabilities of heads. One of Kerov’s insights in [ K2] is that one
can prove Selberg type integral formulas by expressing inte resting harmonic
functions as integrals over the boundary. The paper [BO] car ries out this
program in many cases.
6
Before proceeding, let us indicate that Plancherel measure is a special case
of this set-up. Here the lattice which one uses is the Young la ttice, that is
Γ n consists of all partitions of size n, and a partition of size n is adjoined to
a partition of size n + 1 in Γ n+1 if the partition of size n + 1 can be obtained
from the partition of size n by adding a box. The multiplicity function
κ(λ, Λ) is equal to 1 on each edge. The dimension function dim(λ) is simply
n!∏
x h(x) , the dimension of the irreducible representation of the sym metric
group parameterized by the partition λ. Then one can show that if Mn is
the Plancherel measure, the family of measures {Mn} is coherent [K2]. More
generally it follows from Frobenius reciprocity that if H is a subgroup of G,
MH is Plancherel measure of H and MG is Plancherel measure of G, and
κ(λ, Λ) is the multiplicity of λ in the restriction of Λ from G to H, then
MH(λ) =
∑
Λ: λ րΛ
dim(λ)κ(λ, Λ)
dim(Λ) MG(Λ).
The relevance of these considerations is Proposition 2.1. P arts 1 and 2
are implicit in [K2]. Recall that a Markov chain J on a ﬁnite set X is said to
be reversible with respect to π ifπ(x)J(x,y ) = π(y)J(y,x ) for all x,y . It is
easy to see that if J is reversible with respect to π, then π is stationary for
J (i.e. that π(y) =∑
x∈Xπ(x)J(x,y )). Note that if W is any statistic on X
andW ∗ is obtained by evaluating the statistic after taking a step a ccording
to a Markov chain which is reversible with respect to π, then (W,W ∗) is an
exchangeable pair under the probability measure π.
Proposition 2.1. Suppose that the family of measures {Mn} is coherent
for the Bratelli diagram.
(1) If λ is chosen from the measure Mn, and one moves from λ to Λ
with probability dim(λ )Mn+1(Λ) κ (λ, Λ)
dim(Λ) Mn(λ ) , then Λ is distributed according
to the measure Mn+1.
(2) If Λ is chosen from the measure Mn+1, and one moves from Λ to
µ with probability dim(µ )κ (µ, Λ)
dim(Λ) , then µ is distributed according to the
measureMn.
(3) The Markov chain J on vertices in level Γ n of the Bratelli diagram
given by moving from λ to µ with probability
J(λ,µ ) = dim(λ)dim(µ)
Mn(λ)
∑
Λ ∈Γ n+1
Mn+1(Λ)κ(λ, Λ)κ(µ, Λ)
dim(Λ) 2
is reversible with stationary distribution Mn.
(4) The Markov chain J on vertices in level Γ n of the Bratelli diagram
given by moving from λ to µ with probability
J(λ,µ ) = Mn(µ)
dim(λ)dim(µ)
∑
τ∈Γ n− 1
dim(τ )2κ(τ,λ )κ(τ,µ )
Mn−1(τ )
is reversible with stationary distribution Mn.
7
Proof. For part 1, observe that
∑
λ ∈Γ n
Mn(λ)dim(λ)Mn+1(Λ)κ(λ, Λ)
dim(Λ)Mn(λ)
= Mn+1(Λ)
dim(Λ)
∑
λ ∈Γ n
dim(λ)κ(λ, Λ)
= Mn+1(Λ).
Note that the transition probabilities sum to 1 because the m easures {Mn}
are coherent. Part 2 is similar and also uses the fact that {Mn} is coherent.
For part 3 reversibility is immediate from the deﬁnitions, p rovided that the
transition probabilities for J sum to 1. But J is simply what one gets
by moving up one level in the Bratelli diagram according to th e transition
mechanism of part 1, and then moving down according to the tra nsition
mechanism of part 2. Part 4 is similar; one ﬁrst moves down the Bratelli
diagram and then up. □
One can investigate more general Markov chains where one mov es up or
down by an amount k. This is done in Section 5 where it is applied to tensor
products. However in the application of Stein’s method, we w ill only use
the chain J in part 3 of the proposition (the chain in part 4 would work as
well). This chain simpliﬁes in many cases of interest. We men tion two of
them.
Example 1: The ﬁrst example is the Plancherel measure of Sn. We
already indicated how it ﬁts in with harmonic functions on th e Young lat-
tice. Let parents(λ,µ ) denote the set of partitions above both λ,µ in the
Young lattice (this set has size 0 or 1 unless λ = µ). Then J(λ,µ ) =
dim(µ )|parents(λ,µ )|
(n+1)dim(λ ) . Lemma 3.6 in the next section will use representation
theory to derive a more complicated (but useful) expression forJ(λ,µ ) as a
sum over the symmetric group Sn.
Example 2: The second example concerns cycles of random permuta-
tions. As explained in [K2], the partitions of n index the conjugacy classes of
the symmetric group and the probability measure on partitio ns correspond-
ing to the conjugacy class of a random permutation is a cohere nt family of
measures with respect to the Kingman lattice. Here the under lying lattice
is the same as the Young lattice, but the multiplicity functi onκ(λ, Λ) is the
number of rows of length j in Λ, where λ is obtained from Λ by removing
a box from a row of length j. Also dim(λ) = n!
λ 1!···λ l! where l is the num-
ber of rows of λ and λi is the length of row i of λ. So the Markov chain
J amounts to the following. Letting mr(λ) denote the number of rows of
length r in λ, ﬁrst obtain Λ by adding a box to a row of length r with
chance rmr(λ )
n+1 , or to an empty row with probability 1
n+1 . Then remove a
box from a row of Λ of length s with probability sms(Λ)
n+1 . The cycle structure
of random permutations (and more generally the Ewens sampli ng formula)
8
is very well understood, but still in future work we intend to revisit them by
Stein’s method (using the exchangeable pairs in this sectio n) and to study
the spectral properties of the Markov chains of Proposition 2.1.
