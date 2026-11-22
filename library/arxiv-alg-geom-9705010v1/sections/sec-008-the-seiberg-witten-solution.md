---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-008-the-seiberg-witten-solution
section_title: "The Seiberg-Witten solution"
section_number: null
pages: 13-14
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
The foregoing suggests that what lives intrinsically over a generic u ∈B is not
the electric charge a(u) but the unimodular lattice Za(u) + ZaD(u) of all charges
(electric, magnetic, and “dyonic”, or mixed). As u varies, we get a Z2 local system
V over B minus some singular locus, together with a homomorphism to (the trivial
bundle with ﬁber) C. Dually, this homomorphism is equivalent to a holomorphic
section

aD
a

of the vector bundle VC (i.e. of the sheaf V ⊗OB∖sing). The plan
is to identify the local system (variation of Hodge structure, really) V , and then
to ﬁx the section

aD
a

, which in turn will determine the prepotential F (up to
constant).
Seiberg and Witten identify V by ﬁnding its monodromy. Near u = ∞we know
that u ∼1
2 a2, so the monodromy around ∞sends a 7→−a. The known non-trivial
logarithmic (one-loop) term in the perturbative expansion of F then ﬁxes the shift
in aD: the monodromy is
M∞=

−1
2
0
−1

.
In particular, the local system is non trivial, so τ is a non-constant holomorphic
function on the universal cover of B∖sing, with values in H. The singular locus must
therefore contain at least two points (in addition to ∞). From a physical argument,
Seiberg and Witten deduce that the system is as simple as possible: exactly three
singularities, which can be relocated to u = ±1 and ∞by an automorphism.
Duality instructs that the ﬁnite monodromies should be conjugate to −M∞. Seiberg
and Witten label things so that aD vanishes at u = 1, yielding the monodromy
M1 =

1
0
−2
1

which then determines M−1.
14
RON Y. DONAGI
The monodromies generate the level-2 congruence subgroup Γ(2) ⊂SL(2, Z),
and the local system itself can now be identiﬁed with the ﬁber cohomology of the
universal level-2 elliptic curve
Eu: y2 = (x + 1)(x −1)(x −u)
over the u-line C ∖{±1}.
The complexiﬁcation VC has a global trivialization in terms of the holomorphic
1-form λ1 = dx
y and the residueless meromorphic form λ2 = xdx
y . We can also ﬁx an
integral homology basis, say γ = loop around the branch points 0, 1, and γD = loop
around 1, u. To determine a(u) and aD(u), we use the condition that Im(τ) > 0,
where τ(u) := daD/du
da/du . One geometric solution is to take τ(u) as the period
τu :=
H
γD λ1
H
γ λ1
of the elliptic curve Eu; rigidity implies that this is in fact the only solution. We
then ﬁnd that, up to a multiplicative constant, a and aD are the periods over γ,
γD of the meromorphic 1-form
λ =
y dx
x2 −1 = (x −u)dx
y
= λ2 −uλ1.
