---
doc_id: arxiv-2111.04763v2
doc_title: "RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION"
section_id: sec-001-11-resurgence-of-chernsimons-perturbation-theory
section_title: "Resurgence of Chern–Simons perturbation theory"
section_number: 1.1
pages: 1-4
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
doc_brief: "RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
1.2. A summary of our results 4
1.3. Challenges 5
1.4. Illustration with the two simplest hyperbolic knots 6
Acknowledgements 6
2. The4 1 knot 7
2.1. A2×2matrix ofq-series 7
2.2. A3×3matrix ofq-series 8
2.3. TheΦ (σ0)(τ)asymptotic series 10
2.4. Borel resummation and Stokes constants 12
2.5. The Andersen–Kashaev state-integral 18
2.6. A new state-integral 19
2.7. A3×3matrix of state-integrals 21
3. Thex-variable 23
3.1. TheΦ (σ0)(x,τ)series 24
3.2. A3×3matrix of(x,q)-series 25
3.3. Borel resummation and Stokes constants 27
Date: 5 November 2021.
Key words and phrases:Knots, Jones polynomial, colored Jones polynomial, Chern-Simons theory,
holomorphic blocks, state-integrals, Kashaev invariant, resurgence, perturbative series, Borel resummation,
Stokes automorphisms, Stokes constants,q-holonomic modules,q-difference equations, DT-invariants, BPS
states, peacocks, meromorphic quantum Jacobi forms,q-Stokes phenomenon.
1
arXiv:2111.04763v2  [math.GT]  18 Apr 2026
2 STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
3.4.(u,τ)state-integrals 33
3.5. An analytic extension of the colored Jones polynomial 35
4. The5 2-knot 36
4.1. A3×3matrix ofq-series 36
4.2. The Habiro polynomials and the descendant Kashaev invariants 37
4.3. A6×6matrix ofq-series 39
4.4. Borel resummation and Stokes constants 42
4.5.(x,q)-series 47
4.6.x-version of Borel resummation and Stokes constants 48
4.7. An analytic extension of the Kashaev invariant and the colored Jones polynomial 52
4.8. A new state-integral for the5 2 knot? 53
Appendix A.q-series identities 54
References 56
1.Introduction
1.1.Resurgence of Chern–Simons perturbation theory.Quantum Topology origi-
nated by Jones’s discovery of the famous polynomial invariant of a knot [Jon87], followed by
Witten’s 3-dimensional interpretation of the Jones polynomial by means of a gauge theory
with a topological (i.e., metric independent) Chern–Simons action [Wit89]. The connection
between this topological quantum field theory and the Jones polynomial appears both on the
level of the exact partition function and its perturbative expansion which both determine,
and are determined by, the (colored) Jones polynomial. Indeed, the exact partition func-
tion on the complement of a knot colored by the defining representation of the gauge group
SU(2)at levelkcoincides with the value of the Jones polynomial at the complex root of unity
e2πi/(k+2). On the other hand, the perturbative expansion along the trivial flat connection
σ0 is a formal power seriesΦ(σ0)(h)∈Q[[h]]whose coefficients are Vassiliev knot invariants
which are determined by the colored Jones polynomial of a knot expanded as a power series
inhwhereq=e h [BN95]. More generally, the loop expansion of the colored Jones poly-
nomial is a formal power seriesΦ(σ0)(x,h)∈Q(x)[[h]]introduced by Rozansky [Roz98] and
further studied by Kricker [Kri, GK04], wherex=qn plays the role of the monodromy of the
meridian. An important feature of the power seriesΦ(σ0)(x,h)is that it is determined by (but
also uniquely determines) the colored Jones polynomial. Likewise, the power seriesΦ(σ0)(h)
is determined by (and determines) the Kashaev invariant of a knot [Kas95], interpreted as
an element of the Habiro ring [Hab08].
In [Gar08a] the first author conjectured that the factorially divergent formal power series
Φ(σ0)(h)is resurgent, whose Borel transform has singularities arranged in a peacock pat-
tern, and can be re-expanded in terms of the perturbative seriesΦ(σ)(h)corresponding to
the remaining non-trivial flat connections of the Chern-Simons action. Although this is a
well-defined statement, resurgence was a bit of the surprise and a mystery. We should point
out that the above series are well-defined (forσ̸=σ0 via formal Gaussian integration using
as input an ideal triangulation of a 3-manifold [DG13], and forσ=σ0 using the Kashaev
invariant itself) and their coefficients are (up to multiplication by a power of2πi) algebraic
RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION 3
numbers. However a numerical computation of their coefficients is difficult (about 280 coef-
ficients can be obtained for the simplest hyperbolic knot), hence it is difficult to numerically
study them beyond the nearest to the origin singularity of their Borel transform.
The resurgence question has attracted a lot of attention in mathematics and mathematical
physics and some aspects of it were discussed by Jones [Jon09], Witten [Wit11], Gukov,
Putrov and the third author [GMnP], Costin and the first author [CG11] and Sauzin [Sau15].
Further aspects of resurgence in Chern–Simons theory were studied in [Mn14, GMnP, GH18,
GZa, GZb].
Whens̸=σ 0, theresurgencestructureoftheseriesΦ (σ)(h)wasgivenexplicitlyin[GGMn21],
where it was found that the location of the singularities was arranged in a peacock pattern,
and the Stokes constants were integers. The latter were fully described by anr×rma-
trixJ red(q). The passage from a vector(Φ (σ)(h))σ of power series to a matrixJ red(q)is
inevitable, and points out to the possibility that the non-perturbative partition function of a
theory yet-to-be defined and its corresponding perturbative expansion is matrix-valued and
notvector-valued, as was discussed in detail in [GZb] and [GZa]. Let us summarise some
key properties of the matrixJred(q).
Linearq-difference equation.The entries ofJ red(q)areq-series with integer coefficients
defined for|q|̸= 1. The matrixJ red(q)is a fundamental solution of a linearq-difference
equation of orderr, and its rows are labeled by the set of nontrivialσ.
Asymptotics in sectors:q-Stokes phenomenon.The functionJ red(e2πiτ )asτap-
proaches zero in a fixed cone, has a full asymptotic expansion as a sum of power series in
τ, times power series ine−2πi/τ. However, passing from one cone to an adjacent one changes
thee −2πi/τ-series. The dependence of the asymptotics on the cone is theq-Stokes phenom-
enon, analogous to the well-studied Stokes phenomenon in the theory of linear differential
equations with polynomial coefficients (see, e.g., [Sib90]). In our case, theq-Stokes phenom-
enon is a consequence of the fact thatJred(q)is a fundamental matrix solution to a linear
q-difference equation.
Analyticity.The productW(τ)ofJ red(˜q)with a diagonal automorphy factor and with
Jred(q), whenq=e 2πiτ and˜q=e −2πi/τ, although defined forτ∈C\R, equals to a matrix of
state-integrals and hence it analytically extends toτin the cut planeC ′ =C\(−∞,0]. A
distinguished(σ 1,σ 1)entry ofW(τ), whereσ 1 is the geometric representation of a hyperbolic
3-manifold, istheAndersen–Kashaevstate-integral[AK14]. Thelatterisoftenidentifiedwith
the unknown partition function of complex Chern–Simons theory. Thus, analyticity ofWis
interpreted as a factorisation property of state-integrals, or as a matrix-valued holomorphic
quantum modular form [GZb, Zagb].
Borel resummation.The matrixW(τ)coincides (in a suitable ray) to the Borel resum-
mation of the matrix of perturbative series. In particular, the Borel resummation of the
perturbative series isnotaq-series as has been claimed repeatedly in some physics litera-
ture, but rather a bilinear combination ofq-series and˜q-series.1
Relation with the 3D-index.The 3D-index of Dimofte–Gaiotto–Gukov can be expressed
bilinearly in terms ofJ red(q)andJ red(q−1). A detailed conjecture is given in see [GGMn,
Conj.4].
1A similar phenomenon was observed by Hatsuda–Okuyama [HO15].
4 STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
x-extension.There is an extension of the above invariants by a nonzero complex number
x, which measures the monodromy of the meridian in the case of a knot complement, and
extends theq-series to functions of(x,q), wherexbehaves like a Jacobi variable. This results
in a matrixJred(x,q)whose properties extend those of the matrixJred(q)and were studied
in detail in [GGMn].
