---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-010-32-uniqueness-of-minimal-genus-seifert-surfaces
section_title: "Uniqueness of minimal genus Seifert surfaces"
section_number: 3.2
pages: 12-13
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Uniqueness of minimal genus Seifert surfaces
The discussion here came about from the desire to complete Xu’s uniqueness theorem for Seifert surfaces of 3-braid
links. While our result will be further improved later using work to follow, we need to introduce some notation and
basic tools. We will use the work of Kobayashi [Ko], implying that the property a surface to be a unique minimal
genus surface is invariant under Hopf (de)plumbing.
Subsequently Mikami Hirasawa advised me about a subtlety concerning the notion of ‘uniqueness’ which must be
explained. Xu’s work considers Seifert surfaces unique in the sense isotopic to each other, if we may move the link
by the isotopy. In particular, such isotopy may interchange link components. However, we demand the isotopy to
preserve component orientation. (For unoriented isotopy Xu’s result is complete.) Contrarily, Kobayashi’s setting
assumes uniqueness in the sense that Seifert surfaces are isotopic to each other ﬁxing the link. Hirasawa explained
that the deﬁnitions are not equivalent, and that a unique (if we may move the link) minimal genus surface may get
not unique when one (de)plumbs a single Hopf band. To account for this discrepancy, we should establish proper
language.
Deﬁnition 3.1 Let us use the term unique for Kobayashi’s notion of uniqueness (up to isotopy ﬁxing the link), and
let us call Xu’s notion of uniqueness (up to isotopy which may move the link or permute components, but preserves
orientation) weakly unique.
Here we state the following extension of Xu’s uniqueness theorem.
Theorem 3.1 Every 3-braid link has a weakly unique minimal genus Seifert surface.
Proof. Birman-Menasco showed that any minimal genus Seifert surface of a 3-braid link is isotopic to a Bennequin
surface. Then, Xu showed that every conjugacy class of 3-braids carries a canonical (up to oriented isotopy) Bennequin
surface. The conjugacy classes of 3-braids with given closure link were classiﬁed in [BM]. Most links admit a single
conjugacy class, and we are done, as in [Xu]. The exceptional cases are easy to deal with, except the “ﬂype admitting”
braids
σ±p
1 σ±q
2 σ±r
1 σ±1
2 .
(19)
The ﬂype interchanges ±q and ±1, and (in general) gives a different conjugacy class, which differs from the original
one by orientation. So we have (as in [Xu]), two Bennequin surfaces isotopic only up to orientation. We will settle
this case now also for oriented isotopy, that is, show that these surfaces are isotopic to themselves with the opposite
orientation.
Recall that for a ﬁbered link, a minimal genus surface is the same as a ﬁber surface, and such a surface is unique
(Neuwirth-Stallings theorem). Moreover, by work of Gabai [Ga, Ga2, Ga3] and Kobayashi [Ko] the properties of a
surface to ba a minimal genus surface, a unique minimal genus surface or a ﬁber surface are invariant under Murasugi
(de)sum with a ﬁber surface. In particular, this invariance holds for (de)plumbing a Hopf band (which is understood to
be an unknotted annulus with one full, positive or negative, twist). Now we note that in the cases in (19) where p = r,
the ﬂype is trivial (i.e. realized by a conjugacy), so that the surface is weakly unique. However, since Kobayashi’s the-
orem may fail for weakly unique surfaces, we cannot reduce our surfaces to this case. We will use Hopf (de)plumbings
to recur all cases to ﬁber surfaces or a 2-full twisted annulus. Then we understand that our surfaces are unique, and in
particular weakly unique. The type of Hopf (de)plumbings we will apply is to interconvert all powers of a given band
generator of given sign (for example σk
3 is equivalent to σ−1
3
for each k < 0).
W.l.o.g. assume in (19) that we have −in ±1 and that none of p,q,r is 0 (the other cases are easy). We assume
p,q,r > 0 and vary the signs before p,q,r properly. Also, since the ﬂype interchanges ±p and ±r, we may assume
±p ≥±r. So we exclude the sign choice (−p,+r).
Case 1. p,q,r > 0. We can write (19) up to cyclic permutation as (σ−1
2 σ1σ2)pσq−1
2
σr
1, and conjugating with σ2σ1σ2
we have σp
3σq−1
1
σr
2. Since p,r > 0, this is Hopf plumbing equivalent to σ3σ1σ2 or σ3σ2. These cases are a disk and a
2-full twisted annulus for the reverse (2,4)-torus link, and we are done.
Case 2. p,r > 0, −q < 0. We have an alternating braid, which is ﬁbered.
