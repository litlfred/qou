---
doc_id: 0310280v4
doc_title: "Stabilization in the braid groups II: Transversal simplicity of knots"
section_id: sec-002-21-block-strand-diagrams-templates-and-the-mtws
section_title: "Block-strand diagrams, templates and the MTWS"
section_number: 2.1
pages: 4-8
source_pdf: 0310280v4.pdf
source_sha256: 1e146ee4ebc157f2
toc_source: outline
doc_brief: "Stabilization in the braid groups II: Transversal simplicity of knots — 10 sections: Front matter; Introduction and description of re; The MTWS and transversal isotopies"
---
Block-strand diagrams, templates and the MTWS
Let B be the collection of all braid isotopy classes of closed braid representatives of
oriented knot types in oriented R3. Among these, consider the sub-collection B(X) of
representatives of a ﬁxed knot type X . Among these, let Bmin(X) be the sub-collection
Geometry & Topology 10 (2006)
Stabilization in the braid groups II
1429
of representatives whose braid index is equal to the braid index of X . Choose any
X+ ∈B(X) and any X−∈Bmin(X). The classical Markov Theorem (see [5] for a
proof which is in the spirit of the work in this paper) asserts that there exists a sequence
of closed braids in B(X):
(1)
X+ = X1 →X2 →· · · →Xr = X−
such that, up to braid isotopy, each Xi+1 is obtained from Xi by a single stabilization or
destabilization. We call such a sequence a Markov tower. The existence of Markov
towers in the transversal setting was proved by Orevkov and Shevchisin in [15]. In
the transversal setting the stabilizations and destabilizations are all required to be
positive. That is, each Xi+1 is obtained from Xi by braid isotopy and a single positive
destabilization (see Figure 2) or stabilization, where stabilization and destabilization
are mutually inverse moves. The main result in [6] is to ﬁnd such a sequence of closed
braids, like the one in (1) relating X+ to X−, but not using stabilizations, so that the
braid index is non-increasing. This is done at the expense of introducing additional
moves which are non-increasing on braid index.
We are interested in pairs of ‘block-strand diagrams’ which we call ‘templates’ (see
Section 5.5, [6]). The concepts are intuitive and familiar, and the reader is referred to
Figures 2, 3 and 4 for examples.
w
w
w
w
P
P
P
P
1
1
1
1
A
A
A
A
positive destabilization template
negative destabilization template
+
−
Figure 2: The two destabilization templates. Each template is a pair of block-strand diagrams.
A block B in R3 −A is a 3–ball having the structure of a 2–disk ∆crossed with an
interval [0, 1] such that: (i) for any ﬁber Hθ ∈H the intersection Hθ ∩B is either ∅
or ∆× {θ} for some θ ∈[θ1, θ2] and, (ii) there exists some θ ∈[0, 2π) such that
Hθ ∩B = ∅. The disc t = B ∩Hθ1 is the top of B and the disc B = B ∩Hθ2 is the
bottom of B. A strand l is homeomorphic to an interval [0, 1] or a circle S1. It is
oriented and transverse to each ﬁber of H such that its orientation agrees with the
forward direction of H. When l is homeomorphic to an interval, ∂l = l0 ∪l1, where l0
is the beginning endpoint of l and l1 is the ending endpoint of l.
Geometry & Topology 10 (2006)
1430
Joan S Birman and William W Menasco
Q
Q
P
P
w
w
1
1
1
1
Figure 3: The exchange move template, w ≥2, braid index m ≥4
A block-strand diagram D is a collection of pairwise disjoint blocks {B1, · · · , Bk} and
pairwise disjoint strands {l1, · · · , ll} which together have the following structure:
(i) If li ∩Bj̸ = ∅then li ∩Bj = (li
1 ∩tj) ∪(li
0 ∩Bj) where tj is the top of Bj and Bj
is the bottom of Bj. (We allow for the possibility that either (li
1 ∩tj) or (li
0 ∩Bj)
is empty.)
(ii) For each li
0 (resp. li
1) there is some Bj ⊂Bj (resp. tj ⊂Bj) such that li
0 ⊂Bj
(resp. li
1 ⊂tj).
(iii) For each block Bj we have |tj ∩(∪1≤i≤lli
1)| = |Bj ∩(∪1≤i≤lli
0)| ≥2.
The fact that for each j = 1, . . . , k there is a ﬁber which misses Bj shows that, by
rescaling, we may ﬁnd a distinguished ﬁber Hθ0 which does not intersect any block. We
deﬁne the braid index b(D) of the block-strand diagram D to be the number of times
the strands of D intersect the distinguished ﬁber Hθ0 . Condition (iii) above makes b(D)
well deﬁned.
A braiding assignment to a block-strand diagram D is a choice of a braid on mj strands
for each Bj ∈D. That is, we replace Bj with the chosen braid, so that Bj with this
braiding assignment becomes a braided tangle with mj in-strands and mj out-strands.
In this way a block strand diagram with braiding assignments gives us a closed braid
representative X ⊂D of a link type X . We say that X is carried by D.
A template T
is a pair of block-strand diagrams (D+, D−), both with blocks
B1, . . . , Bk and an isotopy which takes D+ to D−. That is, the blocks of D+ are taken
onto the blocks of D−and the strands of D+ are taken onto the strands of D−. The
diagrams D+ and D−are the initial and ﬁnal block-strand diagrams in the pair. Thus,
for every ﬁxed choice of braiding assignments to the blocks B1, . . . , Bk the resulting
closed braids X+ ⊂D+ and X−⊂D−represent the same oriented link type X ; and
the isotopy from D+ to D−induces an isotopy from X+ to X−.
Geometry & Topology 10 (2006)
Stabilization in the braid groups II
1431
We use the notation T (m, n) for the collection of all topological templates whose D+
(resp. D−) has braid index m (resp. n), where m ≥n. Readers who are familiar with
[6] will note that we have changed the deﬁnition of T (m, n) slightly from the deﬁnition
given in Theorem 2 of [6], by including destabilizations, exchange moves and ﬂypes
in T(m, n). We did it because it makes the statement more concise; also we will not
be concerned here, as we were in [6], with the actual construction of the templates, so
there is no reason to single out some templates and treat them separately from others.
Examples of templates are the block-strand diagram pairs which make up the templates
in Figure 2, 3 and 4. The strands may carry positive integer weights, where weight w
means replace the strand by w parallel strands in the given projection.
R
R
R
R
P
P
P
P
Q
Q
Q
Q
w
w
w
w
w′
w′
w′
w′
k
k
k
k
k′
k′
k′
k′
+
+
−
−
positive destabilization template
negative destabilization template
Figure 4: The two ﬂype templates. The weights must satisfy k′ −w ≥0. Note that the device
of weighted strands may conceal half-twists introduced during the ﬂype. See Figure 4 of [6].
There are restrictions on the weights. The exchange move template of Figure 3 has
braid index m = w + 2, so that it appears in every T (m, n) with m ≥3. However, it
can be replaced by braid isotopy if m = n = 3 (except in the special case of composite
knots of braid index 3), so we assume that w ≥2. As for the ﬂype template of Figure 4
the restriction on the weights is needed to insure that the ﬂype is non-increasing on
braid index.
A braid X is said to be exchange equivalent to X′ if there exists an isotopy taking X to
X′ that is a sequence of braid isotopies and exchange moves. We say X is exchange
reducible to X′ if there exists an isotopy taking X to X′ that is a sequence of braid
isotopies, exchange moves and destabilizations.
We are now ready to state the main result in [6], the MTWS. We have simpliﬁed the
statement, because we do not need the full strength of the theorem proved in [6] for
present purposes.
Geometry & Topology 10 (2006)
1432
Joan S Birman and William W Menasco
Theorem 1 (Markov’s Theorem Without Stabilization [6]) Let X be an oriented knot
type and let (X+, X−) be a pair of closed braids such that X−∈Bmin(X) and X+ ∈B(X)
with b(X+) = m and b(X−) = n. Then there exist X′
+ ∈B(X), X′
−∈Bmin(X), and a
ﬁnite set of templates T (m, n) (whose membership is only dependent on (m, n)) such
that:
(1)
X+ is exchange reducible to X′
+ and X−is exchange equivalent to X′
−, and
(2) There is a template (D+, D−) in the ﬁnite set T (m, n) where, using the same
braiding assignment, on D+ and D−, the diagram D+ carries X′
+ and the
diagram D−carries X′
−.
