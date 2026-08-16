---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Proceedings of Symposia in Pure Mathematics"
section_id: sec-007-12-ron-y-donagi
section_title: "RON Y. DONAGI"
section_number: 12
pages: 12-14
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
doc_brief: "Seiberg-Witten Integrable Systems Ron Y. Donagi Contents Introduction §1. Some physics background Electromagnetism Yang-Mills theory Quantization Supersymmetry N = 2 super Yang-Mills — 17 sections: RO"
---
which was mentioned above; and its K¨ ahler potential
K =K(a, ¯a) = Im
( ∑
i
aD
i ¯ai
)
= Im
( ∑
i
dF
dai
¯ai
)
.
The eﬀective Lagrangian itself is given as a sum of kinetic an d potential parts, each
a Berezin integral over an N = 1 SUSY aﬃne space of dimensions (4,4) and (4,2),
respectively:
Leﬀ = 1
4π
∫
K(Φ , ¯Φ) d4η + 1
8π Im
∫
τ (Φ) |W |2d2η.
Here Φ and W are the two N = 1 multiplets which together make up the N = 2
multiplet containing the Higgs ﬁeld ϕ. ( ϕ and a fermion ψ are the ﬁelds in the
“chiral multiplet” Φ. The “vector multiplet” W contains another fermion λ and
the gauge ﬁeld A. It can be thought of as the ﬁeld strength, N = 1 super analogue
of the curvature F in ordinary YM .) The integrands involve an analytic function
(τ ) or the real part of one ( K); this function is to be applied formally to the super
ﬁelds Φ, W and their conjugates. The integration over the four (or two) odd space
directionsη is interpreted via Berezin’s recipe as a derivative, or as th e reading oﬀ
of the relevant coeﬃcients. (The second term is actually wri tten as an integral over
a (4,2)-dimensional “chiral” quotient of the full (4,4)-di mensional SUSY space, in
which two of the odd directions have been reduced.
What is missing is an explicit expression for F. Traditionally, F was written as
an inﬁnite sum involving its classical (“tree level”) value , the one-loop correction
which is logarithmic in a (higher loop contributions were known to vanish), and an
inﬁnite sum of mysterious instanton corrections involving negative powers ofa. The
breakthrough came when Seiberg and Witten succeeded, in [ SW1], in computing
F (and hence Leﬀ , ds2, etc.) exactly, for the pure N = 2 theory with G = SU(2).
Their solution is based on the global properties of the theor y.
Duality
The original conjecture of Montonen and Olive [ MO] was that the low en-
ergy theory should be invariant under a duality exchanging e lectric and magnetic
charges, and also exchanging the coupling constant g with its inverse. In other
words: electric charge in the strongly coupled theory (larg e g) behaves like mag-
netic charge at weak coupling, and vice versa. Seiberg and Wi tten found that a
modiﬁed version of this duality holds in pure N = 2 SYM for SU(2). They applied
the super version of the Hodge ∗ operator to the Lagrangian Leﬀ , added some vari-
ables (Lagrange multipliers) and integrated out others, an d ended up with a new
Lagrangian LD
eﬀ which is equivalent to the original, and has the same form, bu t in
terms of a new quantity aD := dF
da :
LD
eﬀ (aD) = Leﬀ (a).
The same transformation sends aD to −a = − dF
daD . (This must be so, since the
ﬁrst term in Leﬀ changes sign when a, aD are simply exchanged.) The physical
meaning ofaD is therefore that of the dual, or magnetic, charge. As to the c oupling
constants, the deﬁning relations
τ = daD
da , τ D = d(−a)
daD
SEIBERG-WITTEN INTEGRABLE SYSTEMS 13
together with the chain rule, imply that the actual duality t ransformation is
τ D =τ D(aD) = −τ (a)−1.
This specializes to the Montonen-Olive transformation
gD =g−1
when θ = 0, but not otherwise.
There is another, more elementary, transformation which pr eserves the La-
grangian: the θ angle is deﬁned only modulo 2 πZ, so τ is deﬁned modulo Z. There
is therefore a transformation which ﬁxes a and sends τ ↦→τ + 1. Since τ = daD
da ,
this requires that aD goes to aD +a.
The two transformations can be represented by the matrices
S =
(
0 1
−1 0
)
T =
(
1 1
0 1
)
,
acting linearly on the 2-vector
(
aD
a
)
and fractional-linearly on τ . Since S and T
generate SL(2, Z),we see that the theory has an SL(2 , Z) action. (For other groups,
SL(2, Z) is replaced by a subgroup of ﬁnite index in Sp(2 r, Z).)
The Seiberg-Witten solution
The foregoing suggests that what lives intrinsically over a genericu ∈B is not
the electric charge a(u) but the unimodular lattice Za(u) + ZaD(u) of all charges
(electric, magnetic, and “dyonic”, or mixed). As u varies, we get a Z2 local system
V overB minus some singular locus, together with a homomorphism to ( the trivial
bundle with ﬁber) C. Dually, this homomorphism is equivalent to a holomorphic
section
(
aD
a
)
of the vector bundle VC (i.e. of the sheaf V ⊗ OB/integerdividesing). The plan
is to identify the local system (variation of Hodge structur e, really) V , and then
to ﬁx the section
(
aD
a
)
, which in turn will determine the prepotential F (up to
constant).
Seiberg and Witten identify V by ﬁnding its monodromy. Near u = ∞ we know
thatu ∼ 1
2a2, so the monodromy around ∞ sendsa ↦→ −a. The known non-trivial
logarithmic (one-loop) term in the perturbative expansion of F then ﬁxes the shift
in aD: the monodromy is
M∞ =
(
−1 2
0 −1
)
.
In particular, the local system is non trivial, so τ is a non-constant holomorphic
function on the universal cover ofB/integerdividesing, with values in H. The singular locus must
therefore contain at least two points (in addition to ∞). From a physical argument,
Seiberg and Witten deduce that the system is as simple as poss ible: exactly three
singularities, which can be relocated to u = ±1 and ∞ by an automorphism.
Duality instructs that the ﬁnite monodromies should be conj ugate to −M∞. Seiberg
and Witten label things so that aD vanishes at u = 1, yielding the monodromy
M1 =
(
1 0
−2 1
)
which then determines M−1.
