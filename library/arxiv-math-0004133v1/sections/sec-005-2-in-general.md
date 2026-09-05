---
doc_id: arxiv-math-0004133v1
doc_title: "From Finite Sets to Feynman Diagrams"
section_id: sec-005-2-in-general
section_title: "In general,"
section_number: 2
pages: 14-17
source_pdf: 0004133v1.pdf
source_sha256: 687de8249639c7f2
doc_brief: "From Finite Sets to Feynman Diagrams — ‘Categoriﬁcation’ is the process of replacing equations by isomor- phisms."
---
|S/ /G | = |S|/ |G|
whenever G is a ﬁnite group acting on a ﬁnite set S. In fact, this formula
can be viewed as a simpliﬁed version of ‘Burnside’s lemma’, w hich gives
the cardinality of the ordinary quotient instead of the bett er-behaved weak
quotient [11].
The cardinality of a category C is a well-deﬁned nonnegative rational
number whenever C has ﬁnitely many isomorphism classes of objects and
each object has ﬁnitely many automorphisms. More generally , we can make
sense of |C| whenever the sum deﬁning it converges; we call categories fo r
which this is true tame.
Here are some easily checked and reassuring facts about thes e notions.
Any category equivalent to a tame category is tame, and equiv alent tame
categories have the same cardinality. Moreover, one can deﬁ ne the ‘coprod-
uct’ and ‘product’ of categories in the usual way; these oper ations preserve
tameness, and if C and D are tame categories we have
|C + D| = |C| + |D|, |C × D| = |C||D|.
Finally, there is a standard trick for thinking of sets as spe cial categories:
given a set S we form the discrete category whose objects are the elements
14
of S and whose morphisms are all identity morphisms. As one would hope,
applying this trick to a ﬁnite set gives a tame category with t he same cardi-
nality.
In the next section we describe a way to compute the cardinali ty of a large
class of tame categories — the tame categories whose objects are ﬁnite sets
equipped with extra structure. The simplest example is the c ategory of ﬁnite
sets itself! A simple computation gives the following marve lous formula:
|FinSet| =
∞∑
n=0
1
n! = e.
It would be nice to ﬁnd a natural category whose cardinality i nvolves π , but
so far our examples along these lines are rather artiﬁcial.
The cardinality of a category C equals that of its underlying groupoid C0.
This suggests that this notion really deserves the name groupoid cardinality.
It also suggests that we should generalize this notion to n-groupoids, or even
ω -groupoids. Luckily, we don’t need to understand ω -groupoids very well to
try our hand at this! Whatever ω -groupoids are, they are supposed to be an
algebraic way of thinking about topological spaces up to hom otopy. Thus we
just need to invent a concept of the ‘cardinality’ of a topolo gical space which
has nice formal properties and which agrees with the groupoi d cardinality in
the case of homotopy 1-types. In fact, this is not hard to do. T he key is to
use the homotopy groups π k(X) of the space X.
The homotopy cardinality of a topological space X is deﬁned as the al-
ternating product
|X| = |π 1(X)|−1 |π 2(X)| |π 3(X)|−1 · · ·
when X is connected and the product converges; if X is not connected, we
deﬁne its homotopy cardinality to be the sum of the homotopy c ardinalities
of its connected components, when the sum converges. We call spaces with
well-deﬁned homotopy cardinality tame. The product or coproduct of two
tame spaces is again tame, and we have
|X + Y | = |X| + |Y |, |X × Y | = |X||Y |,
just as one would hope.
15
Even better, homotopy cardinality gets along well with ﬁbra tions, which
we can think of as ‘twisted products’ of spaces. Namely, if
F → X → B
is a ﬁbration and the base space B is connected, we have
|X| = |F ||B|
whenever two of the three spaces in question are tame (which i mplies the
tameness of the third). This fact is an easy consequence of th e long exact
homotopy sequence
· · · → π n+1(B) → π n(F ) → π n(X) → π n(B) → π n−1(F ) → · · ·
As an application of this fact, recall that any topological g roup G has a
classifying space BG, meaning a space with a principal G-bundle over it
G → EG → BG
whose total space EG is contractible. Since EG is contractible it is tame,
and |EG| = 1. Thus G is tame if and only if BG is, and
|BG| = 1
|G| .
In other words, we can think of BG as a kind of ‘reciprocal’ of G.
This curious idea is already lurking in the usual approach to equivariant
cohomology. Suppose X is a space on which the topological group G acts.
When the action of G on X is free, it is fun to calculate cohomology groups
(and other invariants) of the quotient space X/G . When the action is not
free, this quotient can be very pathological, so people usua lly replace it by
the homotopy quotient
X/ /G = EG ×G X.
A careful examination of this construction shows that inste ad of identifying
points of X that lie in the same G-orbit, we are sewing in paths between
them — thus following the dictum of replacing equations by is omorphisms,
or more generally, equivalences. There is a ﬁbration
X → X/ /G → BG,
so when X and G are tame we have
|X/ /G | = |X| |BG| = |X|/ |G|
just as one would hope.
16
