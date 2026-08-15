---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3–manifolds"
section_id: sec-002-definition-of-topological-volume-and-its-spectru
section_title: "Definition of topological volume and its spectrum"
section_number: null
pages: 4-5
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
LetMbe a closed, orientable 3–manifold. AlinkinMis a (possibly empty, possibly dis-
connected) closed 1–submanifoldLofM.We consider links up to (not necessarily orientation
preserving) diffeomorphisms of their complementM\L. This is motivated by the fact that
none of the invariants we consider in this article differ on non-isotopic links with diffeomorphic
complement.
A linkLinMishyperbolicif its complement admits a complete hyperbolic structure of finite
volume. In this case, let vol H(M\L) denote the hyperbolic volume ofM\L.We often write
volH(L) = volH(M\L).Following [ BBB+10BBB+10,§1.3.2], let
volt(M) = inf

volH(M\L)|L⊂Mis a hyperbolic link
	
.(2.1)
It follows from Mostow–Prasad rigidity that volt(M) is a topological invariant ofM, and we
term it thetopological volumeofM.The invariant volt(M) is indeed finite since every closed,
orientable 3–manifold contains a hyperbolic knot [ Mye82Mye82, Mye93Mye93].22 IfMadmits a complete
hyperbolic structure, then volt(M) = vol H(M), since volume decreases under Dehn filling.
Example 2.1As our first example, we observe that volt(S 3) = 2v 0≈2.02988, wherev 0 is
the volume of the ideal regular tetrahedron in hyperbolic 3-space, and with the figure eight
knot as unique minimiser. To see this, recall that [ CM01CM01] showed that the complement of the
figure eight knot, calledK4a1 in the Hoste–Thistlethwaite–Weeks knot table [ HTW98HTW98], and
m004 in SnapPy’s [ CDGW21CDGW21]OrientableCuspedCensus, 33 is a cusped hyperbolic 3–manifold
of minimum volume. Indeed, the cusped hyperbolic 3–manifolds of minimum volume are the
once-punctured torus bundlesm003 andm004 and they are related by a change in monodromy.
However,m003 admits no filling toS 3 and thus does not represent a knot complement inS 3.
All exceptional fillings of these two manifolds have the same topological volume.
According to Jørgensen and Thurston (see [Thu78Thu78,Gro81Gro81,Mai10Mai10]), the set of volumes of complete
orientable hyperbolic 3–manifolds of finite volume is a closed, non-discrete, well-ordered subset of
the positive reals of order typeωω.Throughout this article, we refer to this fact, as well as related
results, as Jørgensen–Thurston theory. In particular, there is always at least one hyperbolic link
L⊂Mwith volt(M) = vol H(M\L). We term such a link avolume minimiser. We say that
two minimising links are equivalent if they have diffeomorphic complements. Occasionally we
refer to the least volume hyperbolic link complement inMas a volume minimiser ofMas well.
Question 2.2LetMbe a closed, orientable 3–manifoldM. SupposeL 1 andL 2 are links
realising volt(M). IsM\L 1 diffeomorphic withM\L 2?
The manifoldm003 appears as complement of a minimiser inL(5,1) in two different ways—
through the fillingsm003(−1,1) andm003(0,1).However, there is a diffeomorphism ofm003
that sends one surgery slope to the other. In particular, the minimising hyperbolic knot in
L(5,1) is the same. Hence this is not a counterexample to the following question, which is
equivalent to the previous one if the cosmetic surgery conjecture is true.
Question 2.3LetMbe a closed, orientable 3–manifoldM. SupposeL 1 andL 2 are links
realising volt(M). Is there a diffeomorphismM→MtakingL 1 toL 2?
2[Mye93Mye93] in fact established that all compact 3–manifolds, including non-orientable 3–manifolds, con-
tain hyperbolic knots. However we restrict ourselves to the closed and orientable case.
3The naming convention throughout this paper follows that of the SnapPy census manifolds. Hence the
symbolmmeans that the corresponding manifolds can be triangulated with at most 5 ideal tetrahedra.
4
It is shown in [ Ada94Ada94] that the set of volumes of hyperbolic knots in any 3–manifold is un-
bounded. Hence not only determining the minimum but also the study of the spectrum of volt
is interesting. LetVbe the set of volumes of all cusped hyperbolic 3–manifolds, andNbe the
set of all closed, non-hyperbolic, orientable 3–manifolds.
Question 2.4Is volt:N→Vsurjective?
