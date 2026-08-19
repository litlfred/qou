---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-031-93-soliton-content
section_title: "Soliton content"
section_number: 9.3
pages: 56-59
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
To a spectral network we can associate some additional data having to do with solitons,
which we now deﬁne.
A soliton s(z), where z∈ pc, is an immersion of [0 , 1] into Σ, which begins and ends
on preimages of z, and such that its projection to C lies in the spectral network W (or
more precisely in a very small neighborhood of W; this correction is necessary because at
joints we smooth out the sharp corners.) If pc carries the label (o,ij ), then we say s(z) is
compatible witho if it begins onz(i) and ends onz(j), and the projection ofs(z) toC begins
with orientation−o and ends with orientation o. The soliton content is, for each street pc
and each point z∈ pc, a pair of sets of solitons So
c (z),S−o
c (z), such that the solitons in
So
c (z) are compatible with o and those inS−o
c (z) are compatible with −o.
– 54 –
The soliton sets must satisfy some rules, which we will refer to as solitonic traﬃc rules.
Actually the rules come in two variants: either American or British. In order to state the
rules we introduce a resolution of the streets of the spectral network, regarding each street
as resolved into two oriented “lanes” inﬁnitesimally displaced from one another, either in
the “American” or the “British” fashion. See Figure 39. Note that this deﬁnition uses the
Figure 39. The American (left) and British (right) resolutions of a street.
orientation of C. The American and British traﬃc rules are thus related to one another
by a reﬂection in the plane. In what follows we show the British rules only; to get the
American rules simply requires a little reﬂection.
ST1. Asz moves continuously along a streetpc, the soliton setsS±o
c (z) evolve continuously,
by the natural parallel transport; in other words, the soliton sets do not “jump.” With
this in mind, we abuse notation by writing the soliton sets simply asS±o
c , suppressing
the trivial z dependence.
Figure 40. A spectral network in the vicinity of a branch point.
ST2. Let b be a branch point. The network W then looks like Figure 40 in the vicinity
of b. There are three streets pc emerging from b. We denote the set of orientations
of each street by {in, out}. For each c, deﬁne the light soliton sc as follows: if pc
carries the label (out ,ij ), then sc(z) begins on z(i), travels along p(i)
c back to the
ramiﬁcation point on Σ covering b, and returns along p(j)
c to z(j). Then, the soliton
sets are related by
Sout
1 =Sin
3 ∪{s1}, Sout
2 =Sin
1 ∪{s2}, Sout
3 =Sin
2 ∪{s3}. (9.2)
(In this equation the solitons are understood to be evolved continuously from one
street to the other. Since there is a branch point at b, this continuous evolution
depends on which path we follow to go from one street to the next; we follow the
short path, i.e. we go around an arc of length 2 π/3, not 4π/3.)
ST3. In a suﬃciently small neighborhood of a joint of the “four-way junction” type shown
in Figure 9 (where ij and kl walls meet), the soliton sets vary continuously, i.e.
– 55 –
jkij
ik
ik
ijkj
ij
ik
jijk
jk
ki
ji
jikj
ki
ki
kj
Figure 41. The rule for constructing outgoing solitons from a six-way junction, with the British
resolution. We show six allowed types of junction, one in each “Weyl chamber” around the joint.
The most general outgoing soliton is constructed by a diagrammatic prescription as follows. We
ﬁx any set of incoming solitons; for each one we draw an incoming line on the diagram, coming
in along the appropriate direction, and on the left side of the median. We then combine these
incoming solitons with junctions of the allowed types, to make a single outgoing line. Every diagram
so obtained determines an outgoing soliton in a natural way, by concatenation of the incoming
solitons.
Figure 42 . Some examples of diagrams representing outgoing solitons. Incoming solitons are
represented by black lines, the outgoing path by a red line. (The ﬁrst example is exceptional in
that the incoming line is the same as the outgoing one.)
the outgoing soliton sets are equal to the incoming ones. In a suﬃciently small
neighborhood of a joint of the “six-way junction” type (where ij, jk and ki walls
meet), the outgoing soliton sets are determined by the incoming ones according to
the rules shown in Figures 41, 42. (A motivation for this peculiar-looking rule is
explained in Appendix A.)
– 56 –
Importantly, for any spectral networkW, the solitonic traﬃc rules (including the choice
of American or British) uniquely determine the soliton content. To prove this claim one can
consider a discrete version of the mass ﬁltration of the spectral networks Wϑ: just deﬁne
the length of a soliton to be the number of walls in its projection to C, and construct the
soliton content by induction on length using the solitonic traﬃc rules.
It is convenient to distinguish two diﬀerent possibilities for the soliton content. Con-
sider the two soliton setsSo
c ,S−o
c on a street pc. If both are nonempty, we refer to pc as a
two-way street. If exactly one is empty, pc is a one-way street, and in that case we writeSc
for the single nonempty soliton set. (It never happens that both are empty.) If there are
no two-way streets we say that W is a nondegenerate spectral network; otherwise we say
it is degenerate.
IfW is nondegenerate, the solitonic traﬃc rules simplify considerably, to the following.
Consider the joint of Figure 10. We continue theij andjk soliton sets continuously through
the joint. For the ik wall, after passing through the joint we add to the set of ik solitons
all new solitons of the following description: the new soliton begins at z(i), projects on C
to the path going back to the joint, then follows one of the the ij solitons from sheet i to
sheetj above the joint, then follows one of thejk solitons from sheetj to sheetk above the
joint, then returns on sheet k on the trajectory projecting to the ik wall ending at z(k). In
particular, these simpliﬁed rules do not depend on whether we started out with American
or British traﬃc rules (as we should expect since we are considering the case where there
are no two-way streets.)
So for nondegenerate spectral networks the soliton content is unique, while for degen-
erate ones there are two possible soliton contents, one following American traﬃc rules and
one British.
In previous sections we considered integers µ(p,a ) attached to the spectral networks
Wϑ. These integers are determined by the soliton content ofWϑ — indeed they are simply
counts of the solitons with appropriate signs: µ(pc,a )Xa = ∑
ν∈ScX[˜sν]. So the soliton
content is a slight extension of the µ(p,a ) to keep track of the actual solitons, not only
their number. This extension will actually not be used for anything in this paper (all of
our constructions really depend only on µ) but we believe it may be useful in the future.
