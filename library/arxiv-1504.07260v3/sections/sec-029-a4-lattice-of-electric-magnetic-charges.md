---
doc_id: arxiv-1504.07260v3
doc_title: "Fricke S-duality in CHL models"
section_id: sec-029-a4-lattice-of-electric-magnetic-charges
section_title: "A.4 Lattice of electric-magnetic charges"
section_number: null
pages: 44-47
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
toc_source: outline
doc_brief: "Fricke S-duality in CHL models — We consider four dimensional CHL models with sixteen spacetime supersym- metries obtained from orbifolds of type IIA superstring on K3×T 2 by a ZN symmetry acting"
---
Lattice of electric-magnetic charges
In this section, we determine the lattice of electric-magnetic charges in a CHL model with
λ > 1 under the assumption that string-string duality and heterotic S-duality (or, equiva-
lently, type IIA T-duality along S1 × ˜S1) hold. As stressed in section (A.1), one expects the
lattice of purely magnetic charges Λm to contain a summand of the form Γg
K3, correspond-
ing to the ˆg-invariant states of the original unorbifolded theory. By (A.5) and by the Dirac
quantization condition, this is the ﬁnest possible lattice of magnetic charges with respect
to the U(1)4+d gauge group associated with the gauge ﬁelds descending from the 4 + d six
dimensional vector multiplets.
Let us focus on the lattice of electric and magnetic charges with respect to the remaining
U(1)4 gauge ﬁelds, associated with the metric and B-ﬁeld along S1 × ˜S1.
As explained in section A.1, the analysis of the spectrum of perturbative heterotic
string leads to a lattice of purely electric charges of the form





m
˜m
w
˜w




∈{





λ −Eg 0 0
0
0
1 0
0 1/Nλ 0 0
0
0
0 1










a1
a2
a3
a4




, a1, a2, a3, a4 ∈Z} ,
(A.38)
with standard quadratic form (4.18). Here, Eg/Nλ mod
1
N Z is the level-mismatch (2.16)
for a heterotic string in the g-twisted sector, where g ∈O(ΓK3) is the pure rotational part
of ˆg = (δ, g). Without loss of generality, we can assume that Eg ∈Z/λZ and λ be coprime;
since λ is always a divisor of 24, this is equivalent to
gcd(Eg, λ) = 1
⇔
E2
g ≡1
mod λ .
(A.39)
Similarly, in type IIA, the momenta and winding along the torus S1 and ˜S1 are quantized
as follows





m′
˜m′
w′
˜w′




∈{





λ −E′
g 0 0
0
0
1 0
0 1/Nλ 0 0
0
0
0 1










a′
1
a′
2
a′
3
a′
4




, a′
1, a′
2, a′
3, a′
4 ∈Z}
(A.40)
where, E′
g/Nλ mod
1
N Z is the level-mismatch for a type IIA g-twisted sector in a non-linear
sigma model on K3. We do not assume, a priori, that E′
g and λ are coprime – we will derive
this property as a consequence of string-string duality, T-duality and S-duality.
Let m, ˜m, w, ˜w, M, ˜
M, W, ˜W denote, respectively, momentum around S1, and ˜S1,
winding around S1 and ˜S1, NS5 brane wrapping ˜S1 and S1 and KK monopole with asymp-
totic circle S1 and ˜S1 in the heterotic string frame. Let us impose the Dirac quantization
– 43 –
condition and assume that these charges be compatible with string-string duality and het-
erotic T-duality along S1 × ˜S1 (corresponding to S-duality in the type IIA frame). We
ﬁnd that the most general lattice of electric-magnetic charges satisfying these constraints
and correctly reproducing the perturbative spectra (A.38) and (A.40) has the following
structure
t 
m ˜m w ˜w M
˜
M W ˜W

∈
n
MN,λ,Eg,E′g,y v, v ∈Z8o
(A.41)
where MN,λ,Eg,E′g,y is the 8 × 8 matrix
MN,λ,Eg,E′g,y :=














λ −Eg 0 0
0
−E′
g
y
0
0
0
1 0
0
0
−EgE′
g/λ
0
0 1/Nλ 0 0
0
0
0
−E′
g/Nλ
0
0
0 1
0
0
−E′
g/λ
0
0
0
0 0 Nλ
0
EgN
0
0
0
0 0
0
1
0
0
0
0
0 0
0
0
1/λ
0
0
0
0 0
0
0
0
1














.
(A.42)
The constraints that we are imposing are not suﬃcient to ﬁx the parameter y ∈Z/λZ.
In order to determine its precise value a more detailed analysis of non-perturbative string
states is necessary.
The analogous type IIA lattice of winding, momenta, NS5 branes and KK monopoles
around S1 and ˜S1 has exactly the same form with Eg and E′
g exchanged:
t 
m′ ˜m′ w′ ˜w′
M′ ˜
M′ W ′ ˜W ′
∈
n
MN,λ,E′g,Eg,y v′, v′ ∈Z8o
.
(A.43)
The derivation of the matrix (A.42) is an easy but tedious exercise. We will skip the
details, but just show that, a posteriori, the lattice above is compatible with all expected
dualities. This can be checked by comparing the BPS mass formulas
M2 = | ˜mU + m
Nλ + T(NλUw −˜w) + S( ˜
MU + M
Nλ) + ST(NλUW −˜W)|2
4U2T2S2
(A.44)
for the heterotic and the type IIA frame.
The BPS mass formula is invariant under string-string duality acting on the moduli by
T ′ = S
S′ = T
U ′ = U ,
(A.45)
provided that the lattices (A.41) and (A.43) are identiﬁed via the GL(8, Z) transformation
v 7→v′ =














1 0 0 0
0 0 0
0
0 0 0 0
0 1 0 Eg
0 0 1 0
0 0 0
0
0 0 0 0 −1 0 0
0
0 0 0 −1 0 0 0
0
0 1 0 0
0 0 0 −E′
g
0 0 0 0
0 0 1
0
0 0 0 0
0 0 0
1














v .
(A.46)
– 44 –
The mass formula is also compatible with heterotic T-duality (type IIA S-duality). In order
to preserve the spectrum of perturbative heterotic states, the action of T-duality on the
Kähler and complex moduli of S1 × ˜S1 must be
T →−
1
NλT
U →−
1
NλU
S →S .
(A.47)
This transformation must be accompanied by an automorphism of the electric magnetic
lattice such that the mass formula is invariant:
v →















Eg
1−E2
g
λ
0 0 −y 0
0
0
λ −Eg 0 0
0
0
y
0
0
0
0 1 EgE′
g 0
−E′
g(1−E2
g )
λ
0
0
0
1 0
E′
g
0
0
0
0
0
0 0 −Eg 0
1−E2
g
λ
0
0
0
0 0
0
0
0
1
0
0
0 0
λ
0
Eg
0
0
0
0 0
0
1
0
0















v .
(A.48)
This is a GL(8, Z) transformation, thanks to (A.39).
The assumptions of string-string duality and heterotic T-duality are suﬃcient to ﬁx the
form of the electric-magnetic lattice as a functions of the three parameters Eg, E′
g, y, with
the constraint E2
g ≡1 mod λ. Let us now impose heterotic S-duality (or, equivalently, type
IIA T-duality). One can check that, in order to preserve the BPS mass formula, one needs
to act on the moduli via
T →T
U →−
1
NλU
S →−
1
NλS .
(A.49)
and on the charges by
v →
















E′
g
0
0
y
0
1−E′
g
2
λ
0
−Eg(E′
g
2−1)
λ
0
E′
g
0
0
0
0
0
1 −E′
g
2
0
0
0 −EgE′
g −1
0
−Eg(1−E′
g
2)
λ
0
0
0
0
−E′
g
0
0
E′
g
2−1
λ
0
0
0
−1
Eg
0
0
0
0
λ −Eg
0
0
0
−E′
g
y
0
0
0
0
−λ
0
0
E′
g
0
0
1
0
0
0
0
0
−E′
g
















v .
(A.50)
This is a GL(8, Z) transformation if and only if
E′
g
2 ≡1
mod λ .
(A.51)
We conclude that, upon imposing string-string duality, T-duality and S-duality, the level
mismatch in the g-twisted sector in the heterotic and type IIA frames must be related
gcd(Eg, λ) = 1
⇔
gcd(E′
g, λ) = 1 .
(A.52)
– 45 –
The physical interpretation of the lattice (A.42) is not obvious. The form of the upper
right block in (A.42) suggests that (in the heterotic frame) each unit of NS5 brane wrapping
S1 (respectively, ˜S1), must carry E′
g units of momentum along S1 (respectively, E′
g/Nλ units
of momentum along ˜S1). Furthermore (and compatibly with T-duality), each unit of KK
monopole with asymptotic circle S1 (respectively, ˜S1), carries also E′
g units of winding
along ˜S1 (respectively, E′
g/Nλ units of winding along S1). A similar observation holds in
the type IIA picture, with E′
g replaced by Eg. In general, it is known that, in type IIA, a
NS5-brane wrapping a non-trivial 4-manifold (such as K3) times a circles S1, must carry
also a ‘geometrically induced’ momentum charge along S1 (by a chain of dualities, this is
related to the D1-brane charge geometrically induced on a type IIB D5 brane wrapping K3).
In this case, the four manifold is an asymmetric orbifold of a K3 sigma model (or, in the
heterotic picture, an asymmetric orbifold of a compactiﬁcation on T 4), so that the precise
computation of the induced charges is more complicated. This interpretation suggests that
the parameter y should vanish.
Let us now consider the electric and magnetic charges under the full U(1)8+d gauge
group. From (A.42), it follows that the sublattice Λm of purely magnetic charges is
Λm = Γg
K3 ⊕⟨Nλu∗, u + NλEgu∗⟩⊕⟨λ˜u∗, ˜u + Eg˜u∗⟩,
(A.53)
where each vector u, u∗, ˜u, ˜u∗represent, respectively, one unit of magnetic charges W, M, ˜W, ˜
M.
This is a proper sublattice of the lattice Λ∗
e thus showing that, as anticipated in section A.1,
the naive guess (A.6) is incompatible with all expected dualities. As a consequence, the full
lattice Λem is ﬁner than the direct sum Λe ⊕Λm, i.e. that there are dyonic charges that
cannot be written as sums of purely electric and purely magnetic. The last three columns
of (A.42) are examples of such charges. The full lattice of electric magnetic charges is given
by
Λem = MN,λ,Eg,E′g,yZ8 ⊕(Γg
K3)∗⊕Γg
K3 ⊂Λ∗
e ⊕Λ∗
m ,
(A.54)
where Γg
K3 ⊂Λm is purely magnetic and its dual (Γg
K3)∗⊂Λe is purely electric. The
summand MN,λ,Eg,E′g,yZ8 ⊂Λem is invariant under heterotic S-duality by construction.
Notice that all g such that λ > 1 have balanced Frame shape, with balancing number
ˆN = Nλ. Therefore, the corresponding CHL models are self-dual under S-duality and the
lattice Γg
K3 must be ˆN-modular
Γg
K3 ∼= (Γg
K3)∗( ˆN) .
(A.55)
As announced in section 4.3, this prediction of S-duality can be veriﬁed for all possible
Frame shapes with λ > 1 (see table 1 in appendix C).
