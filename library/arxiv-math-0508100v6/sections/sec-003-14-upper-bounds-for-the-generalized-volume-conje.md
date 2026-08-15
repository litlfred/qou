---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-003-14-upper-bounds-for-the-generalized-volume-conje
section_title: "Upper bounds for the generalized volume conjecture"
section_number: 1.4
pages: 5-7
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
the Generalized Volume Conjecture. Let ℜ(α) denote the real part of α.
Theorem 1.12. (Proof in Section 6.3) For every knot K with c + 2 crossings and every α ∈ C, we have
lim sup
n→∞
log |fK,n (α)|
n ≤ c log 4 + c + 2
2 |ℜ(α)|.
1.5. Relation with hyperbolic geometry , and asymptotically sha rp bounds. When α = 2 πi, the
upper bound in Theorem 1.12 is not optimal, and does not reveal any relationship between the lim su p and
hyperbolic geometry. Our next theorem ﬁlls this gap.
Theorem 1.13. (Proof in Section
8.5) For every knot K with c + 2 crossings we have
lim sup
n→∞
log |fK,n (2πi)|
n ≤ v8
2π c,
where
v8 = 8Λ( π/4) ≈ 3.6638623767088760602 . . .
is the volume of the regular ideal octahedron –see [Thu77].
6 STA VROS GAROUF ALIDIS AND THANG TQ L ˆE
Using an ideal decomposition of a knot complement by placing one octa hedron per crossing, it follows
that for every knot K with c + 2 crossings, we have
(9) vol(S3 − K) ≤ v8c,
where vol( S3 − K) is the hyperbolic volume of the knot complement. On the other hand , if the volume
conjecture holds for α = 2πi, then
lim
n→∞
log |fK,n (2πi)|
n = 1
2π vol(S3 − K) ≤ v8
2π c.
One may ask whether ( 9) (and therefore, whether the bound in Theorem 1.13) is optimal. This may be a
little surprising, since it involves all knots (and not just alternating o nes) and their number of crossings,
an invariant that carries little known geometric information. In conv ersations with I.Agol and D.Thurston,
it was communicated to us that the upper bound in ( 9) is indeed optimal. Moreover a class of knots that
achieves (in the limit) the optimal ratio of volume to number of crossin gs is obtained by taking a large chunk
of the following weave, and closing it up to a knot:
The complement of the weave has a complete hyperbolic structure a ssociated with the square tessellation of
the Euclidean plane:
Optimality follows along similar lines as the Appendix of [ Lac04], using a stronger estimate for the lower
bound of the volume of Haken manifolds, cut along an incompressible s urface: If M is a hyperbolic ﬁnite
volume 3-manifold containing a properly imbedded orientable, bounda ry incompressible, incompressible
surface S, then
vol(M ) ≥ vol(Guts(M − int(nbd(S))),
where vol stands for volume, and the Guts terminology are deﬁned in [ AST07a]. The proof of this stronger
statement (of Agol-Dunﬁeld-Storm-W.Thurston [ AST07b]) uses, among other things, work of Perelman.
The reader may compare ( 9) with the following result of Agol-Lackenby-D.Thurston [ Lac04]: If K is an
alternating knot with a planar projection having t twist, then
v3(t − 1)/2 < vol(S3 − K) < 10v3(t − 1),
where v3 = 2Λ( π/3) ≈ 1.01494 . . . is the volume of the regular ideal tetrahedron. Moreover, the clas s of
knots obtained by Dehn ﬁlling on the chain link has asymptotic ratio of volume by twist number equal to
10v3. The corresponding tessellation of the Euclidean plane is given by the star of David .
ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT 7
So far, we have formulated a Generalized Volume Conjecture for α near 0 and α near 2 πi, using repre-
sentations near the trivial or near the discrete faithful. How can w e connect these choices for other complex
angles α? A natural answer to this question requires analyzing asymptotics of solutions of diﬀerence equa-
tions with a parameter. This is a diﬀerent subject that we will not disc uss here; instead we will refer the
curious reader to [ GG06], and forthcoming work of the ﬁrst author. For a further discuss ion, see also Section
11.
