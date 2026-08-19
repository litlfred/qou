---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3–manifolds"
section_id: sec-009-lower-bounds
section_title: "Lower bounds"
section_number: null
pages: 11-11
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
In Proposition 2.13Proposition 2.13 (2) we have shown that a sequence of manifolds with unbounded rank of first
homology has unbounded topological volume. In the next theorem, we develop a lower bound
which quantifies this.
Theorem 1.21.2 LetMbe a closed, orientable 3–manifold andpbe a prime. Then
rk(H1(M;Z p))
168.602 <volt(M).
Moreover, we havevolt(M)>3.08,3.69,3.77forrk(H 1(M;Z 2))>5,7,10, respectively.
ProofA result by Guzman–Shalen [ GS25GS25] states that for every finite-volume, orientable, hy-
perbolic 3-manifoldN, and every primep, we have rk(H 1(N;Z p))<168.602·vol H(N). Now let
L⊂Mbe a volume minimiser ofM, and setN=M\L. Since the rank of the first homology
cannot increase under filling, the first inequality follows, i.e.
rk(H1(M;Z p))
168.602 ≤ rk(H1(M\L;Z p))
168.602 <vol H(M\L) = volt(M).
For the other inequalities we use the main results of [ CS11CS11, CS12CS12, GS24GS24] stating that for every
closed, finite-volume, orientable, hyperbolic 3–manifoldNwith rk(H 1(N;Z 2))>5, 7 or 10 we
have volH(N)>3.08, 3.69 or 3.77 respectively. LetLbe a volume minimiser forM. For every
cuspc i ofM\Lwe choose a sequence of slopesp ci
n/qci
n whose lengths converge to∞and such
that fillingM\Lwith these slopes yield manifoldsN n with rk(H 1(Nn;Z 2)) = rk(H1(M;Z 2)).
Note that the latter is satisfied if allp ci
n are even. Since the lengths of the slopes converge to
infinity it follows that(a)the manifoldsN n are hyperbolic fornsufficiently large, and(b)the
volumes ofN n converge to the volume ofM\L. Thus, applying the results of [ CS11CS11,CS12CS12,GS24GS24]
to theN n yields the claimed inequalities for volt(M).
Example 3.7Although our general upper and lower bounds are far from sharp, we claim that
their asymptotic behaviour is the same. LetMbe the Seifert fibered space of genusgandnsin-
gular fibresSFS(g;p,...,p) for a primep. From the standard surgery description (see Figure 1Figure 1)
ofMwe compute rk(H 1(M;Z p)) = 2g+nand thus Proposition 1.2Proposition 1.2 and Proposition 3.3Proposition 3.3 yield
2g+n
168.602 <volt(M)<37g+ 22n−28.
We observe that the quotient of the upper bound divided by the lower bound is bounded.
