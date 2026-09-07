---
doc_id: amc-2730
doc_title: "(Also available at http://amc-journal.eu) Braid representatives minimizing the number of simple walks* Hans U. Boden † , Matthew Shimoda ‡"
section_id: sec-001-the-colored-jones-polynomial-and-walks-along-bra
section_title: "The colored Jones polynomial and walks along braids"
section_number: null
pages: 3-6
source_pdf: amc_2730.pdf
source_sha256: 65730074a2925c6e
doc_brief: "(Also available at http://amc-journal.eu) Braid representatives minimizing the number of simple walks* Hans U. Boden † , Matthew Shimoda ‡ — Given a knot, we develop methods for finding a braid"
---
Given a knot K and integer N ě 2, the colored Jones polynomial JN,Kpqq is a Laurent
polynomial in the variableq1{2. It is normalized so that JN,⃝pqq“ 1, where⃝ is the un-
knot. WhenN“ 2, the colored Jones polynomial agrees with the usual Jones polynomial.
In general, the N-th colored Jones polynomial of a knot K can be expressed in terms of
the usual Jones polynomial of thepN´ 1q strand cable ofK. However, since the crossing
number of thepN´ 1q strand cable of a knot ispN´ 1q2 times the crossing number of the
knot, this does not lead to a practical method for computing the colored Jones polynomial.
One approach for computing the colored Jones polynomial is presented by Huynh and
Lê [15]. Starting with a braid β whose closure is the given knot, Huynh and Lê use meth-
ods from quantum algebra to express the colored Jones polynomial as the inverse of the
quantum determinant of an almost quantum matrix. The matrix is constructed through the
product of Burau matrices, which we obtain from the crossing and orientation properties of
β.
A second approach is presented by Armond [2]. It is based on a probabilistic inter-
pretation of the colored Jones polynomial and involves counting walks along braids. This
method is closely related to the previous one, and in fact it provides a visual representation
of the quantum algebra approach. The idea is to view walks along the braid as traversing
the strands of the braid from the bottom to the top and to record information about the
crossings and their orientations as a product of operators. The end result is the same as
that obtained by taking the quantum determinant of the deformation of Burau matrices, but
Armond’s approach is more accessible and requires less background material on operator
theory. One interesting aspect is that the complexity of the computation is sensitive to the
choice of braid word, and this will be explored further in Section 4. For now, we focus on
describing Armond’s approach and the special role played by the simple walks.
We begin by introducing a little terminology from braid theory.
Definition 2.1. A braid is a set ofm strands running from top to bottom with no reversals
in vertical direction. The strands may cross each other, but only two strands can participate
at each crossing.
Given a braidβ, a braid word is an expression of the form
β“σε1
i1σε2
i2 ...σ εℓ
iℓ,
whereεi“˘ 1 andσi is a symbol. Braid words are read from left to right, and braids are
drawn from top to bottom. For 1ď iď m´ 1,σi represents the braid with one crossing
where thepi`1q-st strand crosses over thei-th strand. The inverseσ´1
i represents the braid
where thei-th strand crosses over thepi` 1q-st strand.
4 Ars Math. Contemp. 23 (2023) #P1.10
The braid word β “ σε1
i1σε2
i2 ...σ εℓ
iℓ hasℓ crossings, and we say it has braid length ℓ.
Ifβ is a braid on m strands, we say it has braid width m. Note that braid words are not
uniquely determined by the braid. Applying a braid relation (see below) will alter the word
without changing the braid. The writhe of a braid is defined to be the sum of the signs on
all its crossings. For example, the braid word above has writhewpβq“ řℓ
i“1εi.
The braid group onm strands is denotedBm. Abstractly, it is the group with generators
σ1,...,σ m´1 and relations
(i) σiσj“σjσi for 1ďi,j ďm´ 1 with|i´j|ą 1 and
(ii) σiσi`1σi“σi`1σiσi`1 for 1ďiďm´ 2.
Relation (i) is called far commutativity and (ii) is called the Yang-Baxter relation (or braid
relation). The group operation is given by concatenation of words or, equivalently, by
stacking geometric braids, one on top of the other.
Next, we introduce the notions of paths and walks along braids. Apath starts at the bot-
tom of the braid and traverses arcs of the braid, sometimes jumping down, until it reaches
the top of the braid. If the path starts at strand i on the bottom and ends at strand j at the
top, we say it is a path fromi toj. Whenever the path encounters a crossing, if it is on the
overstrand, it is allowed to jump down to the undercrossing arc. If it is on the understrand,
then it must stay on that strand. At each crossing the path encounters, a weight from the
settai,εi,bi,εi,ci,εi | i“ 1,...,ℓ u is assigned. The weight will depend on the crossing,
its sign, and the arcs traversed by the path at that crossing. For example, if the path jumps
down at thei-th crossing, it is assigned the weightai,εi. Otherwise, it is assigned the weight
bi,εi if the path traverses the understrand and ci,εi if it traverses the overstrand. Note that,
at a given crossing, the path will follow the braid unless it jumps down there. The total
weight of the path is the product of the weights of the crossings.
A walk W along β consists of a set J Ď t1,...,m u, a permutation π of J, and a
collection of paths with exactly one path in the collection from j toπpjq for each j P J.
The weight of a walk isp´1qp´qq|J|`invpπq times the product of the weights of the paths,
where|J| is the cardinality of J and invpπq is the number of inversions in π, i.e., the
number of pairs of elements inJ withiăj andπpiqą πpjq.
The paths in a walk are ordered from left to right, using their starting strand at the
bottom of the braid. This induces an ordering on the weights. The order of the weights is
important, and that is because the operators associated to the weights are non-commuting.
Operators based at different crossings do commute, but operators at the same crossing do
not. Thus, the effect of non-commutativity can be computed locally at each crossing of
the braid. Given a walk W and a crossing i of the braid, we use Wpiq to denote the local
weight of paths ofW through crossingi in the given order. If no path ofW passes through
crossingi, then we set the local weightWpiq“ 1.
A stack of walks is any ordered collection W1¨¨¨ Wk of walks. Visually, this can be
viewed as stacking the walks on top of one another with W1 at the top and Wk on the
bottom. The weight of the stack is the product of the weights of the paths in the appropriate
order. If two paths belong to different walks, then the path in the higher walk is multiplied
to the left of the path in the lower walk. If two paths belong to the same walk, then the path
which begins to the left of the other path is said to be above and is multiplied to the left
of the other path. Given a stack S “ W1¨¨¨ Wk and a crossing i of the braid, we letSpiq
be the local weight of the stack at i; it is equal to the product pW1qpiq¨¨¨p Wkqpiq of local
weights of the walks of the stack ati in the given order.
H. U. Boden and M. Shimoda: Braid representatives minimizing the number of simple walks 5
With walks along braids established, we now show how they can be used to com-
pute the colored Jones polynomial. Let R “ Zrq,q´1s. Let ˆx and τx be operators on
the ring Rrx˘1,y˘1,u˘1s given by ˆxfpx,y,... q “xfpx,y,... q and τxfpx,y,... q “
fpqx,y,... q. The operators ˆy, ˆu,τy,τu are defined similarly. We associate operators to
each of the crossing weights using the formulas:
a`“p ˆu´ ˆyτx´1qτy
´1, b `“ ˆu2, c `“ ˆxτy
´2τu
´1,
a´“pτy´ ˆx´1qτx
´1τu, b ´“ ˆu2, c ´“ ˆy´1τy
´1τu.
By taking the summation of all walks on the braid and writing their weights in terms of
the above operators, we obtain the operatorP . LettingP act on the constant 1 and making
the substitutions x “ z, y “ z and u “ 1, we obtain a polynomial EpPq. Let ENpPq
denote the polynomial obtained by making the substitutionz“qN´1 toEpPq.
The next result shows how to compute the colored Jones polynomial of a knot from its
braid representative. It was proved by Huynh and Lê in [15] and appears as Theorem 2.3
in [2].
Theorem 2.2. Let K be a knot obtained as the closure of a braid β P Bm. Its colored
Jones polynomial is given by
JN,Kpqq“ qpN´1qpwpβq´m`1q{2
8ÿ
n“0
ENpPnq, (1)
where the operatorP is the sum of the weights of the walks onβ withJĎt 2,...,m u.
Stacks of walks are produced when we take the product of the weights of walks. This
occurs in the step when we expand the operatorP to the power ofn.
Huynh and Lê also gave a useful method for evaluating the termsENpPnq which avoids
operator theory. The key result is the following lemma from [15] which computesENpPnq
directly from the weights once they have been put in a preferred order. In the following,
we suppress the dependence of the weights on the crossing and writea˘,b˘,c˘ instead of
ai,˘,bi,˘,ci,˘.
Lemma 2.3.
ENpbs
`cr
`ad
`q“ qrpN´1´dq
d´1ź
i“0
p1´qN´1´r´iq
ENpbs
´cr
´ad
´q“ q´rpN´1q
d´1ź
i“0
p1´qr`i`1´Nq
We will apply this lemma to the local weights Spiq of each stack at each crossing.
However, before we can apply Lemma 2.3, we must first put the local weights at a crossing
into the preferred order. This can always be achieved using the following relations:
a`b`“b`a`, a `c`“qc`a`, b `c`“q2c`b`
a´b´“q2b´a´, a ´c´“q´1c´a´, b ´c´“q´2c´b´
6 Ars Math. Contemp. 23 (2023) #P1.10
Once the local weights have been put into the preferred order at each crossing, The-
orem 2.2 and Lemma 2.3 can be applied locally at each crossing to compute the colored
Jones polynomial.
The computation is simplified by the observation that only simple walks contribute to
the colored Jones polynomial [2, Lemma 2.5(a)]. Here, a walk is said to besimple if no two
paths intersect in the walk, otherwise it is non-simple. It turns out that non-simple walks
occur in cancelling pairs, so for the purpose of computingJN,Kpqq, it is enough to consider
only simple walks.
The computation is further simplified by the fact that, for any stack of walks, the evalu-
ation of its weights will vanish if the walks in the stack traverse the same arc onN or more
different levels [2, Lemma 2.5(b)]. This is extremely useful because it reduces the com-
plexity of the computation and guarantees that only finitely many terms of ř8
n“0ENpPnq
contribute to the N-th colored Jones polynomial. In particular, for a fixed N, there will
always be an upper bound to the integersn which need to be considered in the infinite sum
of Equation (1). In practice, this bound can be determined by comparing the arcs traversed
by the set of all simple walks for a given braid word.
