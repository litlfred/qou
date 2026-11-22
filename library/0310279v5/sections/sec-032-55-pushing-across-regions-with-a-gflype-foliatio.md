---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-032-55-pushing-across-regions-with-a-gflype-foliatio
section_title: "Pushing across regions with a G–flype foliation"
section_number: 5.5
pages: 92-94
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
toc_source: outline
doc_brief: "Stabilization in the braid groups I: MTWS — 41 sections: Front matter; Introduction; The problem"
---
Pushing across regions with a G–ﬂype foliation
We have seen that if PA contains a long clasp arc, then there is a family of thin annuli
S1 ⊂PA having ∂S1 = X0 ∪X1, where X0 = X+, also X0 can be pushed across
S1 to X1 using a sequence of ﬂypes. The complement of S1 in PA will be a new
family of annuli which has boundary X1 ∪X−. It may happen that we can then apply
Proposition 5.1.1 to simplify S1 via (ab)⋆exchange moves; or it may happen that
PA \ S1 has long clasp arcs, in which case we can iterate the construction. Putting the
two cases together we can construct a second annulus S2 with ∂S2 = X1 ∪X2 such
that the movement across S2 is either an (ab)⋆exchange move or a sequence of ﬂypes.
This procedure can be iterated until either we produce thin annuli that have X−as a
boundary component, or there are no more (ab)⋆exchange moves, or there are no more
long clasp arcs. If we do have thin annuli with X−in the boundary then we will have
decomposed CA into a sequence of thin annuli. And, we have moved across CA using
ﬂypes and ab or ab⋆exchange moves. The difﬁculty in moving across PA this way is
that it may happen that we needed to use inadmissible ﬂypes.
With that difﬁculty in mind, we say that a family of thin annuli Sk ∪Sk+1 ∪· · · ∪Sk+l
supports a G–ﬂype foliation if (i) it is possible to cross the region using only ﬂypes and
ab or (ab)⋆exchange moves, and (ii) there exist integers k, q such that b(Xk+i) ≥b(Xk)
for 1 ≤i ≤(q −1) and b(Xk+q) ≤b(Xk). In this situation the combined ﬂyping and
ab or (ab)⋆motion across the region Sk ∪Sk+1 ∪· · · ∪Sk+q is a G–ﬂype. It is readily
seen that if (B, B) is a pair of related amalgamating blocks for the pair (X+, X−) then
B maintains its integrity through successive ﬂypes and is isotopied to B.
Example 5.5.1 The template in Figure 56 is an illustration of a G–ﬂype.
It shows the foliated annulus PA which was used to construct the template which we
saw in Section 1 in the boxed sketches at the bottom of Figure 9. The labels ‘block Y ’
and ‘block Z’ refer to the blocks in Figure 9. In the interest of keeping the foliation
as simple and understandable as possible, we decided to position the clasp arcs only
in tab neighborhoods, and not in normal neighborhoods. Thus, the clasp arcs are not
contained in the ﬁnite union of leaves. (The addition of 12 vertices and 12 singularities
would be needed in order to position the clasps in normal neighborhoods.) In order
to remove distracting details from the picture, we have eliminated inessential b–arcs,
collapsing the normal neighborhoods of the clasp arcs γ1
+ and γ2
+. This is always
possible, and we did it to save space. The arcs γ1 and γ2 in sketch (d) are the clasp arcs
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
505
(a) from strand 3 of block
Y to strand 1 of block Z
(b) from strand 2 of block
Z to strand 2 of block Y
(c) from strand 3 of block
Z to strand 3 of block Y
(d) from strand 2 of block
Y to strand 2 of block Z
1
3
4
5
13
14
γ3
γ4
+
+
+
+
1
2
4
7
7
8
10
12
14
15
17
18
γ3
γ1
+
+
+
+
+
+
+
3
5
6
6
8
9
9
11
11
16
17
18
γ4
γ2
+
+
+
+
+
+
+
2
10
12
13
15
16
γ1
γ2
+
+
+
+
+
Figure 56: The foliation of PA, in the situation of the 6–braid template of Figure 9
used to construct the ﬁrst thinly foliated annuli that are split off by the dotted curves
in sketches (b) and (c). After we have ﬂyped across this initial thin annulus (the ﬁrst
negative ﬂype of Figure 9) we will have four resulting vertices where we can perform
(ab) exchange move. These are the two double-strand exchange moves in the isotopy
sequence of Figure 9. Finally, the remaining portion of CA will just be the region in
sketch (a) and tab neighborhoods around clasp arcs γ3 and γ4 in sketches (b) and (c).
All of these individual motions were across thin annuli, giving us a decomposition of
CA into thin annuli. Since the braid index starts at b(X+) = 6, goes to 7 after the ﬁrst
ﬂype, remains at 7 for all of the exchange moves and only returns to 6 = b(X−) after
the last ﬂype, all of the thin annuli in this decomposition go to make up the motion
across PA. The combination of all of these isotopies is the 6–braid G–ﬂype which we
illustrated in Figure 9 and Figure 56.
Notice that there are no moving blocks in Figure 9 because there are no doubly long
clasp arcs in Figure 56. The following features of the template in Figure 9 are outside
the support of the isotopy: the four blocks X, Y, Z, W and the following strands that
join them: all strands that enter and leave W and X, also strand 1 entering Y, strand
1 leaving Y, strands 3 and 4 entering Z and strands 1 and 4 leaving Z. We need to
account for the changes in strands 2 and 3 entering Y , strands 2 and 3 leaving Y , strands
1 and 2 entering Z and strands 2 and 3 leaving Z. These are all described completely
by the data in the foliated annulus.
Geometry & Topology 10 (2006)
506
Joan S Birman and William W Menasco
