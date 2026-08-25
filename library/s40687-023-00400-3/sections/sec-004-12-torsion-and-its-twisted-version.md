---
doc_id: s40687-023-00400-3
doc_title: "bonn.mpg.de/stavros 2MaxPlanckInstitutefor Mathematics,Bonn,Germany Fulllistofauthorinformationis availableattheendofthearticle DedicatedtoWalterNeumann andDonZagier,withadmiration"
section_id: sec-004-12-torsion-and-its-twisted-version
section_title: "Torsion and its twisted version"
section_number: 1.2
pages: 3-4
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
Beforediscussingtwistingmattersfurther,letusrecallakeymotivatingexample.Abasic
invariant of a compact 3-manifold is the order of the torsion of its ﬁrst homology. The
behavior of this invariant for all cyclic covers of a knot complement is determined by a
singleLaurentpolynomial,theAlexanderpolynomial.Explicitly,wehave⏐⏐
⏐tor(H
1(M(n); Z))
⏐⏐
⏐=
∏
ωn=1
/Delta1K(ω)( 1 )
where /Delta1K(t) ∈ Z[t±1] is the Alexander polynomial of a knotK ⊂ S3, M(n) is the n-
fold cyclic cover of M = S3 \ K, and the left-hand side is the order of the torsion
part of H1(M(n); Z). This classical result connecting the torsion of the ﬁrst homology
to the Alexander polynomial (see, e.g., [12, (6.3), p.417]) is deeply rooted in the idea that
the Alexander polynomial is the torsion of the inﬁnite cyclic cover ofM twisted by the
abelianizationmap α : π1(M) → H1(M; Z) = Z.Inotherwords,wehave
Thetwistedtorsiondeterminesthetorsionofthecycliccovers (2)
This idea has been extended in several directions. Among them, one can deﬁne the
torsion of a 3-manifold using interesting representations of its fundamental group. For
example, when M is a cusped hyperbolic 3-manifold, one can deﬁne a torsion using a
(lifted)geometricSL
2(C)-representationρofthefundamentalgroupofitscomplement,or
asymmetricpowerthereof.Therearesometechnicaldiﬃcultiesthatonemustovercome,
stemmingfromthefactthatsometimesthecorrespondingchaincomplexesarenotacyclic,
hencethetorsiondependsonachoiceofperipheralcurves,aswellasnormalizationissues,
since the torsion is usually well deﬁned up to a sign. These issues have been addressed
in detail by [5,11,23]. Among the several torsion nvariants, we will be interested in the
adjoint (Reidemeister) torsion τ
γ(M) of a one-cusped hyperbolic 3-manifold (such as a
knot complement) using the adjoint representation Adρ = Sym2(ρ): π1(M) → SL3(C),
where γ is a ﬁxed peripheral curve. The adjoint torsionτγ(M) ∈ F×/± i san o n z e r o
element of the trace ﬁeldF of M, well deﬁned up to a sign [23]. Just as in the case of
theAlexanderpolynomial,thereisaversionofthe adjoint twisted Alexander polynomial
τ(M,α,t) ∈ F[t±1]/(±tZ) (abbreviated byτ(M, t) whenα is clear) deﬁned in [5,11,27]
using an epimorphismα : π1(M) → Z. Here, the ambiguity is given by multiplication by
anelementof ±tZ :={ ±tr | r ∈ Z}.
TwokeypropertiesoftheadjointtwistedAlexanderpolynomialarethebehaviorunder
ﬁnitecycliccovers[ 11]
τ(M(n),t n) =
∏
ωn=1
τ(M,ω t)( 3 )
andtherelationwiththeadjointtorsion[ 28],namely
τ(M,1) = 0, d
dt
⏐⏐⏐
⏐
t=1
τ(M, t) = τλ(M)( 4 )
where λisthecanonicallongitude,i.e.,theperipheralcurvesatisfying α(λ) = 0.
37 Page 4 of 23 S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37
Fig. 1 Anidealtetrahedron
