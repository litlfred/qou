---
doc_id: cuspshapes
doc_title: "CUSP SHAPE AND TUNNEL NUMBER"
section_id: sec-006-5-cusp-shapes-of-tunnel-number-n-manifolds
section_title: "Cusp shapes of tunnel number n manifolds"
section_number: 5
pages: 10-12
source_pdf: CuspShapes.pdf
source_sha256: 01db19e63193e6ae
toc_source: outline
doc_brief: "CUSP SHAPE AND TUNNEL NUMBER — We show that the set of cusp shapes of hyperbolic tunnel number one manifolds is dense in the Teichm¨uller space of the torus."
---
In this section, we prove the main theorems.
Proof of Theorem 1.2. Let C0 be the compression body with the maximally pinched
structure of Lemma 3.9. Let H0 be a maximally pinched structure on a genus
n + 1 handlebody from Lemma 4.2. The convex cores of C0 and H0 have boundary
consisting of embedded, totally geodesic 3-punctured spheres. There is a unique
CUSP SHAPE AND TUNNEL NUMBER
11
hyperbolic structure on such a 3-punctured sphere (see [1]), hence the convex cores
of C0 and H0 can be glued along their 3-punctured sphere boundaries via isometry.
Since both C0 and H0 are geometrically ﬁnite, their convex cores have ﬁnite volume
and the resulting manifold c
M is a complete, ﬁnite volume hyperbolic manifold. The
manifold c
M has a system of n tunnels, as it is the result of gluing a (1; n + 1)-
compression body and a genus n + 1 handlebody along their genus n + 1 boundaries;
let S denote this surface of genus n + 1. Furthermore, c
M has (3n + 4) rank-2 cusps,
(3n + 3) of which come from gluing the rank-1 cusps on the boundaries of the convex
cores of C0 and H0. Denote these cusps by T1, T2, . . . , T3n+3. The remaining
cusp is the rank-2 cusp of C0 whose shape is [Tϵ/2], which is ϵ/2-close to [T] (from
Lemma 3.9).
For each i = 1, . . . 3n + 3, the cusp Ti meets the Heegard surface S of genus n + 1.
Choose a homology basis (µi, λi) for ∂Ti such that λi is parallel to the slope of S on
Ti, and µi is any curve with intersection number 1 with λi. Let si denote the slope
si = µi + kiλi, where ki is a positive integer. Let k = (k1, . . . , k3n+3). Let Mk denote
the manifold obtained by Dehn ﬁlling c
M along the slopes si on cusps Ti. Then Mk
has Heegaard surface S. On one side of S is a genus (n + 1) handlebody, and on the
other side is a (1; n + 1)-compression body. Thus Mk is manifold with a system of n
tunnels. Moreover, Mk has only one rank-2 cusp by construction.
Further, note that Dehn ﬁlling along slopes si ﬁxes the disk set of H0, but modiﬁes
the disk set of C0 by applying a multitwist along P. Assuming the second part of
Lemma 4.2, the Hempel distance of the resulting Heegaard splitting of Mk will be
larger than 2n + 2. Hence by work of Scharlemann and Tomova [33], this is the
minimal genus Heegaard splitting of Mk. (If we do not assume the second part of
Lemma 4.2, we only conclude that Mk has a system of n tunnels.)
Let ki →∞for each i. Then k →∞and by the hyperbolic Dehn surgery theorem,
the manifolds Mk form a sequence of complete, ﬁnite volume, hyperbolic manifolds
that converges geometrically to c
M. It follows that the rank 2 cusps of Mk converge
to the rank 2 cusp of c
M, which has shape [Tϵ/2]. Therefore, by choosing large enough
k, the manifold M = Mk has a system of n tunnels and cusp shape ϵ-close to [T].
Assuming the second part of Lemma 4.2, this manifold is tunnel number n.
□
We may actually complete the proof of Theorem 1.1 without using the work of
Maher and Schleimer [26] used in Lemma 4.2.
Proof of Theorem 1.1. Let n = 2. For any ϵ > 0, and any [T], by the proof of
Theorem 1.2 we obtain a hyperbolic 3-manifold M with a single tunnel and cusp
shape ϵ-close to [T]. Because there is a single tunnel, M has a genus 2 Heegaard
splitting. Since there are no hyperbolic manifolds with smaller genus Heegaard
splittings, M must have tunnel number one.
□
Corollary 5.1. For any integer n ≥1, there exist inﬁnitely many hyperbolic tunnel
number n manifolds with at most one exceptional Dehn ﬁlling.
Proof. For any R > 7 and 0 < ϵ < 1/2, let [T] be a ﬂat torus that is rectangular in
shape, normalized to have one side of length 1 and the perpendicular side of length
R. Let MR be a tunnel number one manifold whose cusp shape is within ϵ of [T],
provided by Theorem 1.2. In a maximal cusp neighborhood, the shortest curve on
the cusp has length at least 1. Thus the cusp embeds as a Euclidean torus with one
12
VINH DANG AND JESSICA S. PURCELL
Figure 4. The augmented minimally twisted 3-chain link La
3 is shown
on the left. It is hyperbolic, with each chain link component having
the cusp shape of a 1 × 2 rectangle, up to scale. One such cusp is
shown on the right.
slope length at least 1, and all other slope lengths at least R −ϵ > 7 −ϵ > 6. By the
6-Theorem [2, 23], there can be at most one exceptional Dehn ﬁlling of MR.
□
