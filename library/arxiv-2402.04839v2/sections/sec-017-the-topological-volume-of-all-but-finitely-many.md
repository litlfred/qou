---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3–manifolds"
section_id: sec-017-the-topological-volume-of-all-but-finitely-many
section_title: "The topological volume of all but finitely many lens spaces"
section_number: null
pages: 19-21
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
Agol [Ago10Ago10] showed thatWandPare the minimal volume orientable hyperbolic 3-manifolds
with two cusps. This property is key for the following:
Theorem 1.31.3 For all but finitely many homeomorphism types of lens spacesL(p,q)(p>q≥1
coprime), the volume minimising link inL(p,q)has complement one ofW( p′
q′,∞)orP( p′′
q′′,∞),
where the filling slopes p′
q′ and p′′
q′′ can be determined from an efficiently computable finite set.
ForPthis means that we fill along the unknotted component.
Throughout, the surgery coefficient 1
0 is the filling with the infinity slope, while we do not write
any slope if we leave one boundary component unfilled.
19
ProofFirst note that, by Proposition 4.3Proposition 4.3, we can assume without loss of generality that we
fill along the first cusp of bothWandP. Since the first cusp is an unknot (inS 3), it follows
from the classification of lens spaces, that all Dehn fillings ofWorPyielding a knot inL(p,q)
must have filling coefficients obtained from the following operations
(p,q)7→(p,q+np),∀n∈Z(5.3)
(p,q)7→(p,q ∗), q ∗q≡1 modp(5.4)
(p,q)7→(−p,q),(p,−q).(5.5)
The volume functions (vol W−∆ volW (p,q), for vol W (p,q) from Equation 5.25.2 and the corre-
spondingly forP) derived by Hodgson and Masai in [ HM13HM13] exclude all but finitely many
fillings slopes satisfying Equations (5.3)Equations (5.3) to (5.5)(5.5) from being volume minimising. Since these
functions are strictly monotonically increasing with respect to their near-elliptical level sets (cf.
Section 5.1Section 5.1), this is a straightforward calculation.
With this setup, suppose to the contrary that there are infinitely many homeomorphism types
of lens spacesL(p i,qi),p i > qi ≥1, with the property that some volume minimising link
complementM i ⊂L(p i,qi) is not homeomorphic with a Dehn filling onPorW.We may
assume thatp 2
i +q 2
i is sufficiently large, such thatWandPhave filling slopes resulting in
hyperbolic knots inL(p,q).
Hence for all p′
i
q′
i
obtained from pi
qi
by Equations (5.3)Equations (5.3) to (5.5)(5.5) and withW( p′
i
q′
i
),P( p′
i
q′
i
) hyperbolic,
we have volH(Mi)≤vol H(W(p′
i
q′
i
)),vol H(P(p′
i
q′
i
))<vol H(W) = vol H(P). According to [ Ago10Ago10],W
andPare the minimal volume orientable hyperbolic 3-manifolds with two cusps. Hence each
Mi has exactly one cusp. Then{vol H(Mi)}is a set of volumes of hyperbolic manifolds with one
cusp and bounded above by vol H(W) = vol H(P).
If this is a finite set, then there isv 0∈{vol H(Mi)}with the property that infinitely many of
the manifoldsM i have volume equal tov 0.But then infinitely many lens spaces have the same
volume, contradicting Proposition 2.6Proposition 2.6.
Hence{vol H(Mi)}is an infinite set. But the first accumulation point for volumes of hyperbolic
manifolds with one cusp is vol H(W).However, a manifold with volume arbitrarily close to this
value is obtained by Dehn surgery on eitherPorW, a contradiction to our assumption.
This proves that all but finitely many lens spacesL(p,q) have volume minimiser a Dehn filling
onPorW.
Corollary 5.2The sequence( volt(L(p,q)) ) (p,q) converges, asp 2 +q 2→∞, to the volume of
the Whitehead link complement.
Corollary 5.3The topological volume of the lens spaceL(p,q)is realised by a knot, i.e.
h(L(p,q)) = 1. Moreover, for|p|sufficiently large, the minimiser ofL(p,1)is unique and the
complement is a tunnel number one once-punctured torus bundle.
ProofEvery lens spaceL(p,q) is obtained as a (−p/q)-filling of the first component of (say)
P. By performing ann-fold Rolfsen twist on that component we can change the surgery
coefficient to−p/(q+np). Thus we can assume that the filling slope is sufficiently large so
that by Thurston’s hyperbolic Dehn surgery theorem [ Thu97Thu97] the other component ofPyields
a hyperbolic knot inL(p,q). But this implies that volt(L(p,q))<vol(P). By Agol [ Ago10Ago10] any
hyperbolic manifold with volume less than vol(P) has at most one cusp and thus the minimiser
is a knot inL(p,q).
For the second statement, observe thatqmust be within±1 of a multiple ofp(see Equations (5.3)Equations (5.3)
to (5.5)(5.5)). Inserting this into the first terms of Equations (5.1)Equations (5.1) and (5.2)(5.2), we can see that—forp
20
sufficiently large—the minimiser must be obtained by filling slope (p,−1) onW(settingp≥0
without loss): For (p,±1), the function ∆ vol P (p,q) converges to π2
2p2 plus lower order terms,
while ∆ volW (p,q) converges to 2π2
p2 plus lower order terms; and we have ∆ vol W (p,−1) =
2π2
p2−4p+1 while ∆ volW (p,1) = 2π2
p2+4p+1 . And thus, the unique minimiser is given by an integer
filling of the Whitehead link. These are known to be once-punctured torus bundles with tunnel
number 1 [ BJK09BJK09, Theorem 1.3].
Corollary 5.4The lens spaceL(4,1)has as a minimiser a one-cusped manifold of volume at
mostvol H(m034)≈3.166and which is not obtained by Dehn fillingWorP.
ProofThe filling coefficients forWandPto obtain a knot in lens spaceL(4,1) are precisely
(±4,2m+ 1), form∈Z. Of those, onlyW((4,−1)) andP((4,1)) are not hyperbolic: The
former contains a splitting Klein bottle, the latter is a solid torus. The other cases can be
verified to be hyperbolic using the 6-theorem [ Ago00Ago00,Lac00Lac00] together with Snappy.
Using the volume bounds from [FKP08FKP08] for sufficiently large slopes together with direct compu-
tations using SnapPy for short slopes, we see that of the hyperbolic filling slopes, the smallest
volume ones areW((4,1)) andW((4,−3)) with a volume of≈3.17729. On the other hand, we
have volt(L(4,1))≤vol H(m034)≈3.166.
Remark 5.5It is important to note that we require both the Whitehead linkWand its sister
Pfor Proposition 1.3Proposition 1.3 to hold: The volume minimiser forL(p,1),psufficiently large, is uniquely
realised as fillingW(p,−1), as shown in Proposition 5.3Proposition 5.3. On the other hand, it can be deduced
from Table 1Table 1 thatL(13,3) has minimiserm011 andL(19,7) andL(18,5) both have minimiser
m016. But according to Table 2Table 2, these can only be obtained by Dehn fillings ofP, but not of
W.
We conclude this section with a question that is analogous to the third question in [ HM13HM13,§9].
Question 5.6What is the largest volume less than vol H(W) of a one-cusped hyperbolic 3–
manifold that does not arise from Dehn filling onW=m129 orP=m125?
An answer to Proposition 5.6Proposition 5.6 would allow us to give a quantitative version of Proposition 1.3Proposition 1.3.
