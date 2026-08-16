---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-025-74-the-setting-sun
section_title: "The setting sun"
section_number: 7.4
pages: 46-48
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
Next we brieﬂy consider a more complicated example, in which several overlapping ﬁnite
webs appear simultaneously. Unlike the previous examples, we just draw the degenerate
network of interest, and not the nondegenerate ones at nearby phases (which would be
terribly cluttered in this example). See Figure 30.
Label the three two-way streets in this ﬁgure as p1, p2, p3 from top to bottom. Using
the rules of Appendix A, we can directly compute the soliton degeneracies µ(·,·) on all the
– 44 –
(jk)
(ij)
(ki)
Figure 30. The “setting sun”: a picture which could occur as part of a degenerate spectral network
at some ϑ = ϑc. We show the two-way streets slightly resolved, with the “American resolution”,
which would occur in the limit ϑ→ϑ−
c . Each street supports the charges indicated as well as their
shifts by positive multiples of γ = cl(¯a + ¯b + ¯c).
streets in the ﬁgure. The nonzero degeneracies on p1, p2, p3 come out to
µ(b,p 1) = 1, µ (c +a +n(b +c +a),p 1) = 1 for n≥ 0, (7.15)
µ(c,p 2) = 1, µ (a +b,p 2) = 1, (7.16)
µ(a +n(b +c +a),p 3) = 1 for n≥ 0, µ (b +c,p 3) = 1. (7.17)
(All other streets turn out to be one-way, as anticipated in Figure 30, and so do not
contribute to L below.) Deﬁne γ = cl(¯a + ¯b + ¯c), and let ˜γ be its preferred lift. Plugging
into (6.9) and keeping careful track of windings, we ﬁnd
Q(p1) =Q(p3) = (1−X˜γ)−1, (7.18)
Q(p2) = 1−X˜γ. (7.19)
This gives
L(γ) =−p1
Σ−p3
Σ +p2
Σ. (7.20)
This class is homologically trivial, [ L(γ)] = 0. (It could hardly be otherwise, since the
projection of L(γ) to C lies in a contractible region containing no branch points, which
means L(γ) itself lies in the disjoint union of three contractible open sets on Σ.) So in
particular this degenerate network does not contribute to the 4d BPS spectrum:
Ω(γ) = 0. (7.21)
Nevertheless the enhanced degeneraciesω(γ,·) are certainly not zero in this example: they
are given as usual by (6.14).
How should we understand the result (7.21)? First note that there is a 1-parameter
family of ﬁnite BPS webs here, parameterized by an interval, as indicated in Figure 31.
The two ends of the family are built from theS-walls appearing in the degenerate network
Wϑc, while the other ﬁnite webs involve a “bubble” made out of BPS strings which are
notS-walls. This is the same phenomenon we had in §7.2 above, where we considered a
cylinder swept out by BPS strings; the boundaries of the cylinder were S-walls, but the
generic BPS strings inside the cylinder were not.
– 45 –
(jk)
jk
ij
(ij)
ki
(ki)
(jk)
jk
ij
(ij)
ki
jk
ij
(ki)
(jk)
jk
ij
(ij)
ki
jk
ij
(ki)
ki
Figure 31. Three ﬁnite webs, belonging to a 1-parameter family of ﬁnite webs parameterized by
an interval: as we move along the interval, the “bubble” in the middle of the web expands from
zero size (left) to a ﬁnite maximum size (right).
In the present case one end of the family (at left) looks like the “three-string web” we
encountered in§7.3 above. If this three-string web occurred in isolation it would give rise to
a BPS hypermultiplet, with Ω(γ) = +1. However, when it sits in this 1-parameter family
its contribution cannot be evaluated in isolation: rather we must quantize the whole family
at once. What we have seen is that the contribution to Ω( γ) from this family vanishes.
