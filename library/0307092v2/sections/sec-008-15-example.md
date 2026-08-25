---
doc_id: 0307092v2
doc_title: "Extended Bloch group and the Cheeger-Chern-Simons class"
section_id: sec-008-15-example
section_title: "Example"
section_number: 15
pages: 58-62
source_pdf: 0307092v2.pdf
source_sha256: de2f7ddec49b2ce6
doc_brief: "Extended Bloch group and the Cheeger-Chern-Simons class — We deﬁne an extended Bloch group and show it is naturally isom orphic to H3(PSL(2, C)δ; Z)."
---
We return to the ﬁgure 8 knot complement m004 of Example 14.4 to illustrate
the above formulae. Denote the cross-ratio parameters of th e two simplices in
Figure 8 by z and y , and choose ﬂattenings [ z; p, q] and [ y, r, s]. The consis-
tency condition about each edge can be read oﬀ from the ﬁgure. The condition
for the edge labeled with a single arrow is:
2 log z + log z′ − log y′ − 2 log y′′ = 2πi (18)
and the condition for the other edge turns out to be equivalen t to this. The
log-parameters for the ﬂattenings are
(log z + pπi, log z′ + qπi, log z′′ + (−1 − p − q)πi),
(log y + rπi, log y′ + sπi, log y′′ + (1 − r − s)πi) .
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 471
z
z
z´
z´´
z´
z´´
z´
z
z´
z´´
z´´
z
z´
z´
z´
z
z
z´ z´
z
y y
m(y´)
y
y
(y´)(y´)
y
(y´´) (y´´)
(y´)
−1
−1
−1
−1
−1
−1−1
−1
−1
−1 −1
−1
−1
−1
−1
l
z z
z´´z´´
(y´´)
(y´´) (y´´)
(y´´)
Figure 9: Fundamental domain of the cusp torus, triangulated as t he link of the 0–
simplex of the ideal triangulation of m004.
Thus the ﬂattening condition about the edge is
2p + q − s − 2(1 − r − s) = −2 . (19)
The log holonomy for a meridian and longitude can be read oﬀ fr om the fun-
damental domain of the cusp torus illustrated in Figure 9 (ta ken from [16]
but modiﬁed since orientation conventions diﬀer; in particu lar, w, w′, w′′ there
are our ( y′′)−1, (y′)−1, y−1 because of diﬀerent vertex-ordering for the second
simplex). They are:
u := log z′′ + log y′′ v := 2 log z − 2 log z′′ . (20)
Their vanishing thus gives ﬂattening conditions
(1 − r − s) + (−1 − p − q) = 0
2p − 2(−1 − p − q) = 0
which simplify to
−p − q − r − s = 0 (21)
2 + 4p + 2q = 0 . (22)
Solving equations (19), (21), (22) gives
q = −1 − 2p, (r, s) = −(p, q). (23)
Simultaneously solving the consistency condition (18) and the cusp conditions
u = v = 0 (see (20)) gives z = ω , y = ω−1 . Thus, as promised earlier, we see
Geometry & Topology, Volume 8 (2004)
472 Walter D Neumann
that ˆβ(m005) = [ ω; p, q] − [ω−1; −p, −q] with q = −1 − 2p. Choosing p = 0,
we get:
ˆβ(m005) = [ ω; 0, −1] − [ω−1; 0, 1].
Now suppose we deform our parameters to perform hyperbolic ( α, β) Dehn
ﬁlling on this manifold. Let z, y now denote the deformed values of the simplex
cross-ratios (they simultaneously satisfy the consistenc y condition (18) and the
Dehn ﬁlling condition αu + βv = 2πi ). Choose γ, δ ∈ Z so
⏐
⏐
⏐
⏐
α β
γ δ
⏐
⏐
⏐
⏐ = 1.
As described in [16], the complex length of the added geodesi c is λ := −(γu +
δv), so Theorem 14.5 gives the formulae
ˆβ(m004(α, β)) = −χ(e−γu−δv ) + [z; 0, −1] − [y; 0, 1]
(vol +i cs)(m004(α, β)) = π
2 (γu + δv) − i(R(z; 0, −1) − R(y; 0, 1)) ,
(24)
with u, v given by (20).
On the other hand, if we use Theorem 14.7, the Dehn ﬁlling cond ition αu+βv =
2πi gives the ﬂattening condition
α(−p − q − r − s) + β(2 + 4p + 2q) = −2
while the parity condition says p + q + r + s must be even. A simultaneous
solution of these and equation (19) is:
q = γ − 1 − 2p, r = −2δ − p, s = −γ + 4δ + 1 + 2p .
Choosing, eg, p = 0, we get
ˆβ(m004(α, β)) = [ z; 0, γ − 1] − [y; −2δ, −γ + 4δ + 1] ,
(vol +i cs)(m004(α, β)) = −i(R(z; 0, γ − 1) − R(y; −2δ, −γ + 4δ + 1)) .
(25)
It is not hard to verify directly the equivalence of (24) and ( 25).
16 Other ﬁelds
Although we have worked over C in this paper, most of what we have done
works for a subﬁeld K ⊂ C if we replace G = PSL(2, C) = PGL(2 , C) by G =
PGL(2, K). In Theorem 7.5 we must replace the group µ of roots of unity by the
group µK of roots of unity in K . The homomorphism λ : H3(PGL(2, K)) →
ˆB(K) is still deﬁned. For a hyperbolic 3–manifold H3/Γ with Γ ⊂ PGL(2, K)
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 473
the element ˆβ(M ) naturally lies in ˆB(K), but we have numerical evidence that
it lies in ˆB(k), where k is the invariant trace ﬁeld of M (k is always contained
in K and is generally smaller). The arguments of [15] show that ˆβ(M ) ∈ ˆB(k)
if M is non-compact, while some power of 2 times ˆβ(M ) lies in ˆB(k) in general.
References
[1] Stephane Baseilhac , Riccardo Benedetti , QHI Theory, II: Dilogarithmic
and Quantum Hyperbolic Invariants of 3–Manifolds with PSL(2, C)–Characters,
arXiv:math.GT/0211061
[2] P J Callahan , M V Hildebrand , J R Weeks, A census of cusped hyperbolic
3–manifolds, Mathematics of Computation 68 (1999) 321–332
[3] J Cheeger , J Simons , Diﬀerential characters and geometric invariants ,
Springer Lecture Notes in Math. 1167 (1985) 50–80
[4] D Coulson , O Goodman , C Hodgson , W D Neumann , Computing arith-
metic invariants of 3–manifolds , Experimental Mathematics 9 (2000) 127–152
[5] J L Dupont , The dilogarithm as a characteristic class for ﬂat bundles , J. Pure
and App. Algebra 44 (1987) 137–164
[6] J L Dupont , F L Kamber , Cheeger–Chern–Simons classes of transversally
symmetric foliations: dependance relations and eta-invar iants, Math. Ann. 295
(1993) 449–468
[7] J L Dupont , H Sah , Scissors congruences II , J. Pure and Appl. Algebra 25
(1982) 159–195
[8] J L Dupont, H Sah, Dilogarithm identities in conformal ﬁeld theory and group
homology, Comm. Math. Phys. 161 (1994) 265–282
[9] D B A Epstein , R Penner , Euclidean decompositions of non-compact hyper-
bolic manifolds, J. Diﬀ. Geom. 27 (1988) 67–80
[10] O Goodman , Snap, the program, http://ms.unimelb.edu.au/~snap
[11] R Meyerhoﬀ , Hyperbolic 3–manifolds with equal volumes but diﬀerent Chern–
Simons invariants , from: “Low-dimensional topology and Kleinian groups”,
(D B A Epstein, editor), London Math. Soc. Lecture notes 112 (19 86) 209–215
[12] R Meyerhoﬀ , W D Neumann , An asymptotic formula for the η –invariant
of hyperbolic 3–manifolds , Comment. Math. Helvetici 67 (1992) 28–46
[13] W D Neumann , Combinatorics of triangulations and the Chern–Simons in-
variant for hyperbolic 3–manifolds, from: “Topology 90, Proceedings of the
Research Semester in Low Dimensional Topology at Ohio State”, Walt er de
Gruyter Verlag, Berlin–New York (1992) 243–272
Geometry & Topology, Volume 8 (2004)
474 Walter D Neumann
[14] W D Neumann , Hilbert’s 3rd problem and invariants of 3–manifolds , from:
“The Epstein Birthday Schrift”, (Igor Rivin, Colin Rourke and Carolin e Series,
editors), Geom. Topol. Monogr. 1 (1998) 383–411
[15] W D Neumann , J Y ang, Bloch invariants of hyperbolic 3–manifolds, Duke
Math. J. 96 (1999) 29–59
[16] W D Neumann , D Zagier , Volumes of hyperbolic 3–manifolds, Topology 24
(1985) 307-332
[17] W D Neumann , Extended Bloch group and the Chern–Simons class , (Incom-
plete Working version), preprint (1998), arXiv:math.GT/0212147
[18] C Petronio, J R Weeks, Partially ﬂat ideal triangulations of cusped hyperbolic
3–manifolds, Osaka J. Math. 37 (2000) 453–466
[19] Udo Pachner , PL homeomorphic manifolds are equivalent by elementary
shellings, European J. Combin. 12 (1991) 129–145
[20] C S Sah , Scissors congruences, I, Gauss–Bonnet map , Math. Scand. 49 (1982)
181–210
[21] A A Suslin , Algebraic K –theory of ﬁelds , Proc. Int. Cong. Math. Berkeley
1986, 1 (1987) 222–244
[22] J Weeks, Snappea, the program,
http://www.geometrygames.org/SnapPea/index.html
[23] W P Thurston , The geometry and topology of 3–manifolds, Mimeographed
lecture notes, Princeton University (1977)
[24] T Y oshida , The η –invariant of hyperbolic 3–manifolds, Invent. Math. 81
(1985) 473–514
Geometry & Topology, Volume 8 (2004)
