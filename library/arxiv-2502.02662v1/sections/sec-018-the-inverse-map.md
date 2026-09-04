---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-018-the-inverse-map
section_title: "The Inverse Map"
section_number: null
pages: 23-24
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
The duality map (5.19) we have uncovered is a rather complicated one, and it would be
interesting to identify new Yang-Mills variables in terms of which which this map simplifies.
To that effect, we shall invert the duality map (5.19). We consider the correlation functions
of standard vertex operators on the string theory side and derive their expression in terms of
Yang-Mills observables. We start by inverting the relation (3.11). This yields an expression
for the symmetric group characters in terms of the unitary group characters:
χλ(α) =
Z
dUsλ(U)pα(U−1). (5.21)
The observables of the deformed Hurwitz theory at fixed degree thus read:
⟨
kY
i=1
ˆCσi⟩def
d = 1Qk
i=1zσi
Z  kY
i=1
dUi
!
pσ1(U−1
1 )··· pσk(U−1
k )·Z+
d (U1,...,U k). (5.22)
The equation (5.22) suggests that the basis most natural for comparing operators on both
sides is that of the complex-conjugated power sum polynomials p∗
α:
⟨
kY
i=1
p∗
αi⟩+ =
Z
dU1··· dUkp∗
α1(U)··· p∗
αk(U)Z+(U1,...,U k), (5.23)
as first argued in [4]. We note that the insertions must be associated with Young diagrams
of the same order to get non-vanishing correlators. In particular, one may replace the full
partition function of Yang-Mills in equation (5.23) with the fixed-degree partition function,
up to a factor of the chemical potential. We may then write
qdg2g(d)−2
s ⟨
kY
i=1
gℓ(σi)
s ˆCσi⟩def
d =⟨
kY
i=1
p∗
σi
zσi
⟩+, (5.24)
whereg(d) is the covering surface genus determined by the Riemann-Hurwitz formula for the
ramification profiles σi. Expressing the correlators of the deformed Gromov-Witten theory in
terms of Yang-Mills observables is then a basis change in the algebra of partial permutations.18.
We write
⟨
kY
i=1
ˆτki⟩def =⟨˜Ω−k
gsu
kY
i=1
¯Aki+1
ki! ⟩def.
18We note that a basis of the family of Yang-Mills observables encoded by the string theory at fixed-degree
is given by the correlators ⟨Qk
i=1p∗
σi⟩d.
22
Writing out the completed cycles explicitly, rearranging the sum and taking out the combina-
torial factors arising from the correlators of partial permutations, we obtain
⟨
kY
i=1
ˆτki⟩def =
X
s1,...,sk
X
d
g2g(d)−2
s qd
 kY
i=1
m1(σi)
m1(si)
ρki+1,si
ki!
!
⟨
kY
i=1
ˆCσi⟩def
d . (5.25)
Substituting in equation (5.24), we find
⟨
kY
i=1
ˆτki⟩def =
X
d
X
s1,...,sk
 kY
i=1
g−ℓ(σi)
s
ki!zσi
m1(σi)
m1(si)

ρki+1,si
!
⟨
kY
i=1
p∗
σi⟩+. (5.26)
This equation is the inverse of (5.19): it describes the Yang-Mills observables naturally com-
puted by standard string theory correlators. These observables are a completed version of
the power sum polynomials. It is interesting to manipulate the expression a little further to
uncover the role of the trivial sheets:
⟨
kY
i=1
ˆτki⟩def =
* X
s1,...,sk
 kY
i=1
ρki+1,si
ki!
g−ℓ(si)
s
zsi
p∗
si
!X
d
 kY
i=1
g
−(d−|dsi|)
s
(d−|dsi|)!
!
(p∗
1)d−|dsi|
+
+
. (5.27)
They give rise both to operator insertions p∗
1 as well as combinatorial factors.
