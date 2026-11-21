---
doc_id: bq28-r2r7
doc_title: "Classical and Quantum Algorithms for Characters of the Symmetric Group"
section_id: sec-006-a-granularity-and-quantum-advantage
section_title: "A.. Granularity and quantum advantage"
section_number: null
pages: 10-11
source_pdf: bq28-r2r7.pdf
source_sha256: 38419a88531ebce7
toc_source: outline
doc_brief: "Classical and Quantum Algorithms for Characters of the Symmetric Group — 12 sections: Front matter; I.. INTRODUCTION; II.. GROUP THEORY REFRESHER"
---
Let us ﬁrst consider a general setting in which a sam-
pling problem is deﬁned by a probability distribution P
over some ﬁnite set  called the sample space and an
error tolerance ϵ. We consider inﬁnite families of prob-
lem instances labeled by an integer n called the problem
size. It is required that each point x ∈ can be speci-
ﬁed by poly(n) bits. Likewise, the probability distribution
P should admit a succinct classical description of size
poly(n). We also assume that the error tolerance obeys
ϵ ≥poly(1/n). A classical or quantum algorithm solves
the sampling problem if it outputs a sample x ∈ from
some probability distribution P′ that is ϵ close to P
in the total variation distance, such that ∥P −P′∥1 ≡

x∈ |P(x) −P′(x)| ≤ϵ. Such an algorithm is eﬃcient if
its runtime is at most poly(n).
We are speciﬁcally interested in sampling problems
that can be solved eﬃciently by a quantum computer. To
provide evidence for classical hardness of such a sam-
pling problem, one can follow the complexity-theoretic
argument pioneered in Refs. [19,39]. Roughly speaking,
this argument gives a reduction from average-case strong
simulation—computing output probabilities of a quantum
circuit in the average case over a suitable ensemble—to
the sampling problem of interest. Here the reduction uses
polynomial time classical resources as well as access to an
NP oracle (i.e., it is a BPPNP algorithm). If the average-
case strong simulation problem is so hard that it cannot
be solved using resources within the polynomial hierarchy
then this implies that no eﬃcient classical algorithm can
solve the sampling problem of interest.
Here we describe a variant of this argument for sampling
problems with a certain granularity structure, described
below.
Deﬁnition 1 (Granularity). A probability distribution P
over a ﬁnite set  is called granular if there exists a real
number γ ≥1 such that P(x) is an integer multiple of
γ/|| for all points x ∈. We refer to the number γ as
the granularity of P.
For example, distribution (29) deﬁned by columns of
the character table has granularity γ = 1 since the sample
space has size || = |Sn| = n! and characters of the sym-
metric group are integer valued. Distribution (28) deﬁned
by rows of the character table may or may not be gran-
ular depending on the choice of the permutation g ∈Sn,
as detailed below. If the input of a sampling problem is a
granular distribution P, the granularity γ and the size of
the sample space || have to be included in the classical
description of P.
Lemma 4. Suppose that P0 and P1 are probability distri-
butions over a ﬁnite set  such that P0 is granular, P1 can
be sampled by a BPP algorithm and ∥P0 −P1∥1 ≤ϵ for a
given ϵ that is at least inverse polynomial in n. Let γ ≥1
be the granularity of P0. There exists a BPPNP algorithm
that takes as input a point x ∈ and outputs an integer
k(x) such that
P0(x) = γ k(x)
||
(36)
for at least a max {0, 1 −20ϵ} fraction of points x ∈.
Proof. Let N = ||. Deﬁne the sets
S =

x ∈: P0(x) ≤
1
10Nϵ

and
T =

x ∈: |P0(x) −P1(x)| ≤
1
10N

.
Markov’s inequality gives |S| ≥(1 −10ϵ)N and |T| ≥
(1 −10ϵ)N. By the union bound,
|S ∩T| ≥(1 −20ϵ)N.
(37)
The assumption that P1 can be sampled by a BPP algorithm
and Stockmeyer’s approximate counting theorem [40]
imply that there exists a BPPNP algorithm that takes as
input a point x ∈ and outputs a real number P2(x) such
that
|P2(x) −P1(x)| ≤ϵP1(x).
For any x ∈S ∩T, one has P1(x) ≤P0(x) + 1/(10N) ≤
1/(10Nϵ) + 1/(10N) ≤1/(5Nϵ),
which
implies
that
|P2(x) −P1(x)| ≤1/(5N). Thus, for any x ∈S ∩T, one
has
|P2(x) −P0(x)| ≤|P2(x) −P1(x)| + |P0(x) −P1(x)|
≤1
5N +
1
10N ≤1
3N .
(38)
By assumption, P0(x) is an integer multiple of γ/N for
a given γ ≥1. Let P3(x) be an integer multiple of γ/N
closest to P2(x). Using Eq. (38), one gets P3(x) = P0(x)
whenever x ∈S ∩T. The above shows that P3(x) can be
computed by a BPPNP algorithm and Eq. (37) implies that
P3(x) = P0(x) for at least a 1 −20ϵ fraction of points x ∈
. Finally, set k(x) = (N/γ )P3(x).
■
A central challenge in quantum complexity theory is
to prove the quantum advantage conjecture [19] in the
following form.
Conjecture 1. Assume that the polynomial hierarchy
does not collapse. Then there exists a sampling problem
that can be solved eﬃciently on a quantum computer and
that is provably hard for classical randomized algorithms.
Lemma 4 implies that the conjecture is true if there
exists a sampling problem satisfying the following prop-
erties.
(1) Granularity: the sampling problem is based on a
family of granular probability distributions P.
(2) Quantum algorithm: the sampling problem can be
solved eﬃciently on a quantum computer.
(3) Average-case hardness: the problem of computing
P(x) exactly on a point x ∈ picked uniformly at
random with a suﬃciently high success probabil-
ity is not contained in the polynomial hierarchy.
Here the success probability must be at least 1 −
poly(1/n) for problem instances of size n.
We see that, for granular distributions, the hardness of
classical sampling follows from the average-case hard-
ness property (3) and the assumption that the polynomial
hierarchy does not collapse. This diﬀers from the usual
argument in that we do not need to establish the so-called
anticoncentration property for the family of distributions
P; moreover, the average-case hardness property (3) con-
cerns exact computation of output probabilities rather than
approximate computation.
Note that a dummy algorithm for computing P(x) that
outputs zero for all x ∈ has success probability at
least 1 −1/γ . Indeed, the dummy algorithm succeeds
with probability |S|/||, where S = {x ∈: P(x) = 0}.
Granularity gives P(x) ≥γ/|| for x /∈S. Thus, 1 =

x∈ P(x) ≥γ (|| −|S|)/||, that is, |S|/|| ≥1 −
1/γ , as claimed. This shows that the average-case hard-
ness property (3) can only be achieved if the granularity γ
is at most polynomial in n.
