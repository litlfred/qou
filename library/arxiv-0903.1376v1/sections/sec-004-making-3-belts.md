---
doc_id: arxiv-0903.1376v1
doc_title: "Particle Topology, Braids and Braided Belts"
section_id: sec-004-making-3-belts
section_title: "Making 3-belts"
section_number: null
pages: 8-16
source_pdf: 0903.1376v1.pdf
source_sha256: c106071c1a3110e8
toc_source: outline
doc_brief: "Particle Topology, Braids and Braided Belts — Recent work [1, 2] suggests that topological features of certain quantum gravity theories can be interpreted as particles, matching the known fermions"
---
Making 3-belts
Consider a braided belt (or framed braid) on three strands. In the particular
(trivial) case where the strands do not cross each other, the associated braid
word is clearly the identity, I. In the case where the strands are untwisted,
the associated twist-word is also the identity. Such an untwisted trivial braid -
the identity braid on three strands - can be made by cutting two parallel slits
in a strip of leather, as shown on the left of Fig. 5. The resulting surface is
topologically equivalent to three parallel strips capped at the top and bottom
by an attached disk. We will refer to three strands (not necessarily unbraided)
attached to disks in this manner as a 3-belt. In Fig. 5, we show the consequence
of trinion ﬂips in the making of a braided leather belt.
Recall that σ1 ≡[ 1
2, 1
2, −1
2], and so we may write I = [−1
2, −1
2, 1
2]σ1. The
right-hand side of Fig. 5 illustrates that the strands are now crossed and twisted,
but still the 3-belt we have obtained is isotopic to the trivial 3-belt. Figure 6
shows the result of six consecutive repetitions of this process (alternately to the
ﬁrst two strands and the last two strands) of a 3-belt. The reader will note
by direct observation that along each of the three ribbon strands, all the twists
cancel. Thus when we isotop all the twists to the top of the braid we obtain a ﬂat
(untwisted) braided belt, with braid-word (σ−1
2 σ1)3. Iteration of the procedure
that yields Fig. 6 is actually used by belt-makers.
8
Figure 6: Braiding a Belt
Since the same physical structure can be isotoped to have the braid word
I or (σ−1
2 σ1)3, it is clear that the braid word is not a topological invariant.
However, as noted above, the pure twist-word is a topological invariant. If any
two braids [a, b, c]B1 and [x, y, z]B2 have the same pure twist-word, then they
are isotopic. For the remainder of this paper we shall be mostly interested in
classifying braided, twisted 3-belts by their pure twist numbers, rather than
inducing twists and crossings on an initially trivial 3-belt. We are therefore
primarily interested in the procedure illustrated in Eqn. (4). We now apply
this procedure to the braid word (σ−1
2 σ1)3, and conﬁrm that its pure twist-
word is I = [0, 0, 0]. This corresponds with reversing the procedure (used by
belt-makers) described in the previous paragraph.
Firstly we consider the braid word σ−1
2 σ1
σ−1
2 σ1
→
1
2, −1
2, −1
2

σ1
→
P1,2
1
2, −1
2, −1
2
 1
2, 1
2, −1
2

→

−1
2, 1
2, −1
2
 1
2, 1
2, −1
2

→
[0, 1, −1]
(6)
9
Figure 7: A braided belt can be embedded within a larger network, represented
by the box.
To consider the full braid with six crossings we need to multiply this result with
itself three times, but also keep track of the permutations induced by the braid
word σ−1
2 σ1. This permutation will be P1,2(P2,3) = P(123), that is, the cyclic
permutation which sends [a, b, c] →[c, a, b]. Hence,
(σ−1
2 σ1)3
→
[0, 1, −1](σ−1
2 σ1)2
→
P(123)([0, 1, −1])[0, 1, −1]σ−1
2 σ1
→
[−1, 0, 1][0, 1, −1]σ−1
2 σ1
→
[−1, 1, 0]σ−1
2 σ1
→
P(123)([−1, 1, 0])[0, 1, −1]
→
[0, −1, 1][0, 1, −1]
→
[0, 0, 0]
(7)
as expected.
The reader will notice that it is unnecessary to keep track of the permutation
induced by the ﬁrst generator in a braid word (or the ﬁrst braid word in a
product, when the corresponding pure twist-word is known), as there is nothing
for this permutation to act upon.
The braided belts we consider in this paper are of interest not only from a
purely topological basis, but also due to a possible connection with theoretical
physics. In [2] it was shown that braided belts attached at one end to a larger
network of ribbons could be used to represent the elementary quarks and leptons.
In order to keep the discussion in this paper relevant to the work in [2], we shall
henceforth treat the ordering of generators in a braid word as indicative of a “top
end” which is free to be trinion-ﬂipped, and a “bottom end” which is attached
to a larger network (which for all practical purposes is ﬁxed and static). The
10
Figure 8: Finding the pure twist-word for a braid [ 1
2, 3
2, −1
2]σ1σ2σ−1
1 σ−1
1 σ−1
2
left-most generator in a product is equated with the top end, and this is why
we shall always work from left to right when we resolve a braid word to ﬁnd the
associated pure twist-word. In diagrams of braided belts we shall henceforth
include a box on the boundary of the belt at the bottom end, to represent the
presence of a larger network to which the braided belt is attached, as shown in
Fig. 7
There is a simple schematic technique for ﬁnding the pure twist-word asso-
ciated with a braid word, as follows:
• Replace each generator in the braid word by one of the following triples
of symbols;
σ1
→
+ + −
σ−1
1
→
−−+
σ2
→
−+ +
σ−1
2
→
+ −−
(8)
such that they form a vertical stack, leftmost generator at the top.
• Beneath each pair of similar symbols, place a cross, ×, connecting each
symbol to the diagonally opposite symbol in the pair below.
Beneath
each dissimilar symbol, place a vertical bar, |, connecting it directly to the
symbol below it. The lines below the bottom row of symbols will end on
three blank spaces.
• Sum up the symbols along each vertical path, starting at the top of the
symbol stack, and ending on the blank spaces at the bottom. Each +
stands in for 1
2. Each −stands in for −1
2. The resulting triplet of numbers
is the pure twist-word.
In the case where the braid is written in standard form [a, b, c]B we construct
the symbol stack for the braid word as described above, and then place the twist
word at the top, with three vertical lines descending to the top of the symbol
stack.
11
Figure 9: The Positron, in fully-braided form (left), resolved in stages to its
pure twist form (right).
In Fig. 8 we give an example of using this process to ﬁnd the pure twist-word
corresponding to the braid [ 1
2, 3
2, −1
2]σ1σ2σ−1
1 σ−1
1 σ−1
2 . The three diagrams in the
ﬁgure correspond with the addition of twists along each of the three strands.
The resulting pure twist-word is found to be [1, 2, −1].
A further example is given by the braid e+
L = [1, 1, 1]σ1σ−1
2 . This is the braid
structure assigned to the left-handed positron in [1]. We ﬁnd that
e+
L
→
[1, 1, 1]σ1σ−1
2
→
[1, 1, 1]
1
2, 1
2, −1
2

σ−1
2
→
3
2, 3
2, 1
2

σ−1
2
→
Pσ−1
2
3
2, 3
2, 1
2
 1
2, −1
2, −1
2

→
3
2, 1
2, 3
2
 1
2, −1
2, −1
2

→
[2, 0, 1].
(9)
Thus [2, 0, 1] gives the framings on the equivalent parallel ﬂat strip belt. See
Fig. 9 for a graphical version of this calculation, and a depiction of the boundary
of the surface that corresponds to e+
L . We denote the boundary of this surface
by ∂e+
L . Note that ∂e+
L is independent (topologically) of the deformation that
we have applied to straighten out the braiding from the original deﬁnition of
e+
L . Thus our algebraic reduction gives us an algorithm for ﬁnding the boundary
link for each particle in Bilson-Thompson’s tables.
In Fig. 11 - Fig. 14 we illustrate the correspondence between the braids
proposed in [1] to match the ﬁrst-generation fermions of the Standard Model,
and their pure twist form. Notice that the pure twist forms are distinct in each
12
Figure 10: By assuming that the outer edge of the braided belt is closed (when
we trace it through the rest of the network), we can equate a link (right) to
the pure twist form (left) of any braid, in this case the left-handed positron as
illustrated in Fig 9
illustrated case, except for the neutrino and anti-neutrino. In this case, the
left-handed “negative” neutrino is isomorphic to the right-handed “positive”
anti-neutrino. Likewise the left-handed “positive” anti-neutrino is isomorphic
to the right-handed “negative” neutrino. In other words, there are half as many
topologically distinct states for neutral particles as one would expect for charged
particles. This is in agreement with the Standard Model, where neutrinos are
purely left-handed, and anti-neutrinos are purely right-handed. The pure twist
numbers in each case are listed with the corresponding particles in the table
below;
left-handed
right-handed
e−
[0,-2,-1]
e−
[-1,0,-2]
¯uB
[0,-1,-1]
¯uB
[-1,1,-2]
¯uG
[1,-2,-1]
¯uG
[-1,0,-1]
¯uR
[0,-2,0]
¯uR
[0,0,-2]
dB
[1,-2,0]
dB
[0,0,-1]
dG
[0,-1,0]
dG
[0,1,-2]
dR
[1,-1,-1]
dR
[-1,1,-1]
νL
[1,-1,0]
νR
[0,1,-1]
¯dB
[1,0,0]
¯dB
[0,2,-1]
¯dG
[2,-1,0]
¯dG
[0,1,0]
¯dR
[1,-1,1]
¯dR
[1,1,-1]
uB
[2,-1,1]
uB
[1,1,0]
uG
[1,0,1]
uG
[1,2,-1]
uR
[2,0,0]
uR
[0,2,0]
e+
[2,0,1]
e+
[1,2,0]
13
Figure 11: Left-handed negatively-charged fermions, as per the structure pro-
posed by Bilson-Thompson, and their associated pure twist form
Figure 12: Right-handed negatively-charged fermions, as per the structure pro-
posed by Bilson-Thompson, and their associated pure twist form
14
Figure 13: Left-handed positively-charged fermions, as per the structure pro-
posed by Bilson-Thompson, and their associated pure twist form
Figure 14: Right-handed positively-charged fermions, as per the structure pro-
posed by Bilson-Thompson, and their associated pure twist form
15
