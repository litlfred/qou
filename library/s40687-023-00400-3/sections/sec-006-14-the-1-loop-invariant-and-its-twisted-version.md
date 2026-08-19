---
doc_id: s40687-023-00400-3
doc_title: "bonn.mpg.de/stavros 2MaxPlanckInstitutefor Mathematics,Bonn,Germany Fulllistofauthorinformationis availableattheendofthearticle DedicatedtoWalterNeumann andDonZagier,withadmiration"
section_id: sec-006-14-the-1-loop-invariant-and-its-twisted-version
section_title: "The 1-loop invariant and its twisted version"
section_number: 1.4
pages: 7-9
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
The adjoint Reidemeister torsion has a conjectural description in terms of the 1-loop
invariant of [6]. The latter depends on the NZ matrices of an ideal triangulation, its
shapes, their ﬂattenings and a peripheral curveγ. With the notation of Sect.1.3,t h e
1-loop invariant isdeﬁnedby
τCS
γ (T ): = det
(
Aγ diag(ζ) + Bγ diag(ζ′′)
)
2 ∏ N
j=1 ζ
fj
j ζ
′f ′
j
j ζ
′′f ′′
j
j
=
det
(
Gγ diag(ζ) + G′
γ diag(ζ′) + G′′
γ diag(ζ′′)
)
2 ∏ N
j=1 ζ
fj
j ζ
′f ′
j
j ζ
′′f ′′
j
j
∈ F/(±1)
(20)
where the last equality follows from Equation (8). In [6], it is conjectured that the 1-loop
invariant τCS
γ (T )isequaltotheadjointtorsion τγ(M)withrespectto γ
τCS
γ (T ) ?= τγ(M) ∈ F×/(±1). (21)
Given the above conjecture and the discussion of Sect.1.2,i ti sn a t u r a lt op r e d i c tt h e
existence of a twisted version of the 1-loop invariant, deﬁned in terms of the twisted NZ
matrices.WiththenotationofSect. 1.3,wedeﬁnethe twisted 1-loop invariant by
τ
CS(T ,t): = det
(
A(t)diag( ζ) + B(t)diag( ζ′′)
)
∏ N
j=1 ζ
fj
j ζ
′f ′
j
j ζ
′′f ′′
j
j
:= det
(
G(t)diag( ζ) + G′(t)diag( ζ′) + G′′(t)diag( ζ′′)
)
∏ N
j=1 ζ
fj
j ζ
′f ′
j
j ζ
′′f ′′
j
j
∈ F[t±1]/(±tZ)
(22)
wherethesecondequalityfollowsfromthefact(analogoustoEquation( 8))
G(t)diag( ζ) + G′(t)diag( ζ′) + G′′(t)diag( ζ′′) = A(t)diag( ζ) + B(t)diag( ζ′′). (23)
An elementary observation is thatτCS(T ,t) is well deﬁned up to multiplication by
an element in±tZ. Indeed, the computation in [6, Sec.3.5] shows that up to sign, the
twisted 1-loop invariant is independent of the choice of a combinatorial ﬂattening. It is
also manifestly independent of the choice of a quad type of/Delta1
j, as the deﬁnition (22)i s
symmetric with respect toζ ,ζ′, and ζ′′. Finally, a diﬀerent choice of lifts of the edges
and tetrahedra ofT results to left or right multiplication of all of the matricesG□ (t)
by the same diagonal matrix diag(tc1 ,t c2 ,... ,t cN ) for integers c1,c2,... ,c N,h e n c et h e
observationfollows.
37 Page 8 of 23 S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37
Bytheverydeﬁnitionof τCS(T ,t),itleadstoatwistedversionofConjecture( 21),namely
τCS(T ,t) ?= τ(M, t) ∈ F[t±1]/(±tZ). (24)
We now list some properties of the twisted 1-loop invariant. The ﬁrst concerns the
topologicalinvariance.
Theorem 1.6 τCS(T ,t) is invariant under Pachner 2–3 moves between ideal triangula-
tions that support the geometric representation.
CombiningtheabovetheoremwithProposition1.7of[ 6],weconcludethatthetwisted
1-loopinvariantdeﬁnesatopologicalinvariantofone-cuspedhyperbolic3-manifolds.
Thenexttwotheoremsconcerntheproperties( 3)and( 4)oftheadjointtwistedAlexan-
derpolynomial.
Theorem 1.7 For all n ≥ 1,w eh a v e
τCS(T (n),t n) =
∏
ωn=1
τCS(T ,ω t). (25)
Theorem 1.8 We have τCS(T ,1) = 0 and d
dt
⏐⏐
⏐
t=1
τCS(T ,t) = τCS
λ (T ) where λ is the
peripheral curve satisfying α(λ) = 0.
Acorollaryoftheabovetheoremsisarelationbetweenthetwisted1-loopinvariantand
the1-loopinvariantof[ 6]forcycliccovers,namely
τCS
μ (T (n))
τCSμ (T ) =
∏
ωn=1
ω⁄=1
τCS(T ,ω). (26)
Thenextresultconcernsthesymmetriesofthetwisted1-loopinvariant.Conjecture 1.4
impliesasymmetryofthetwisted1-loopinvariantwhichisknowntoholdfortheadjoint
twistedAlexanderpolynomial[ 18,19],namely τ(M, t) = τ(M,1/t).
Corollary 1.9 (assumingConjecture 1.4) We have
τ
CS(T ,t) = τCS(T ,1/t) ∈ F[t±1]/(±tZ). (27)
We end our discussion on the twisted 1-loop invariant with a remark which suggests
thatthe t-deformationvariableisindependentfromthevariable mwhichisaneigenvalue
ofthemeridianofanSL 2(C)-representationof π1(M).
Remark 1.10 By varying the representation, the adjoint Reidemeister torsion can be
extendedtoarationalfunctiononthegeometriccomponent XM oftheSL 2(C)-character
variety of a knot complementM [7], and consequently to a rational function of the geo-
metric component of theA-polynomial curve. The same holds for the 1-loop invariant;
see [6, Sec.4]. Likewise, we can extend the twisted 1-loop invariant to a twisted ratio-
nal function on the geometric component of the character variety, i.e., to an element of
the ringC(XM)[t±1]/(±tZ), whereC(XM) is the ﬁeld of rational functions onXM.T h e n ,
m ∈ C(XM)isavariableindependentof t.
S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37 Page 9 of 23 37
