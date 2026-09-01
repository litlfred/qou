---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-013-a-stringy-deformation
section_title: "A Stringy Deformation"
section_number: null
pages: 17-19
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
---
We start from the undeformed partition function (4.1) and study the implementation of the
deformation into the structure of the genus expansion of the string theory. Consider first
17An interesting observation is that the product of the filtered Hurwitz theory – see e.g. [28] – does preserve
the Riemann-Hurwitz formula.
16
the deformation by transpositions. The exponential can be expanded inside the correlation
functions to write
Z+
G(U1,...,U k) =
X
d
g(2G−2+k)d
s qd
X
r
(−1)r (gst)r
r! ⟨Cr
2
kY
i=1
Cαi⟩d (4.12)
The Riemann-Hurwitz equation may be leveraged to write this expression as a correlator in
a string theory. The method consists again in introducing a redundant sum over all genera
together with a constrained correlator ⟨·⟩g,d:
Z+
G(U1,...,U k) =
X
g
g(2G−2+k)d+r
s
X
d
qd
X
r
(−1)rtr
r!⟨Cr
2
kY
i=1
Cαi⟩g,d. (4.13)
The correlator is non-vanishing when the genusg takes the value determined by the Riemann-
Hurwitz formula
2g− 2 = (2G− 2 +k)d−
X
i
ℓ(αi) +r. (4.14)
One then identifies the power of the string couplinggs with the genusg of the covering surface,
up to the appropriate normalization factor for the vertex operators. We write:
Z+
G(U1,...,U k) =
X
g
g2g−2
s
X
d
qd⟨e−tC2
kY
i=1
gℓ(αi)
s Cαi⟩g,d. (4.15)
The genus expansion has absorbed the factor of the string couplinggs featured in the deforma-
tion. The deformation by transpositions thus preserves the stringy structure of the correlators.
In general, a deformation by conjugacy classes Cη preserves the stringy structure of the cor-
relators if each insertion comes with a factor of the string coupling raised to the power of the
charge of the conjugacy class g|η|
s . For transpositions, |C2| = 1, and each insertion C2 comes
indeed with a single factor gs. Importantly, this means that we interpret the power expansion
of the exponential as insertions of distinct observables: ⟨Cr
2Cα⟩g,d denotes the correlator
⟨C2,...,C 2| {z }
r times
,Cα⟩g,d, (4.16)
as indicated in the previous section.
We move on to study the effect of Ω deformations. We recall the definition of the expo-
nential distance operator Ω:
Ωgsu :=
X
η⊢d
(gsu)|η|Cη. (4.17)
The criterion just stated is manifestly satisfied and we deduce that the gs factor in Ω gsu is
absorbed by the genus expansion. Furthermore, the inverse Ω −1
gsu can be defined by a series
expansion, in which each term Cη1...C ηs is again accompanied by a factor g|η1|+···+|ηs|
s . As
a result, the genus expansion soaks up the factors of the string coupling contained in the
operator Ω−1
gsu as well.
17
In conclusion, the observables of chiral Yang-Mills theory admit a string theoretic expan-
sion
Z+
G(U1,...,U k) =
X
g
g2g−2
s
X
d
qd⟨
kY
i=1
 X
αik
pα(U)gℓ(αi)
s ˆCαi
!
⟩def
g,d, (4.18)
where the correlation functions of the deformed theory are defined by
⟨ ˆCα1··· ˆCαk⟩def
g,d =⟨Cα1··· Cαk·e−tC2Ω2−2G−k
u ⟩g,d. (4.19)
We stress that by the explicit criterion we laid out, generic deformations do not preserve
the string theoretic structure of correlation functions. We thus view the preservation of the
structure as further new and strong evidence that chiral Yang-Mills theory in two dimensions
admits a string dual.
