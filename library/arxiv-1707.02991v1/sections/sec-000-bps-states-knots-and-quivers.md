---
doc_id: arxiv-1707.02991v1
doc_title: "BPS states, knots and quivers"
section_id: sec-000-bps-states-knots-and-quivers
section_title: "BPS states, knots and quivers"
section_number: null
pages: 1-3
source_pdf: 1707.02991v1.pdf
source_sha256: f4f539f74403dd24
doc_brief: "BPS states, knots and quivers — 5 sections: BPS states, knots and quivers; Moduli of quiver representations; Knot invariants from quiver repres"
---
Piotr Kucharski 1, Markus Reineke 2, Marko Stoˇ si´ c3,4, and Piotr Su lkowski 1,5
1 Faculty of Physics, University of Warsaw,
ul. Pasteura 5, 02-093 Warsaw, Poland
2 Faculty of Mathematics, Ruhr-Universit¨ at Bochum,
Universit¨ atsstrasse 150, 44780 Bochum, Germany
3 CAMGSD, Departamento de Matem´ atica,
Instituto Superior T´ ecnico,
Av. Rovisco Pais, 1049-001 Lisboa, Portugal
4 Mathematical Institute SANU,
Knez Mihailova 36, 11000 Beograd, Serbia
5 Walter Burke Institute for Theoretical Physics,
California Institute of Technology,
Pasadena, CA 91125, USA
Dedicated to John Schwarz on his 75th birthday
We argue how to identify supersymmetric quiver quantum mechanics description of BPS states,
which arise in string theory in brane systems representing knots. This leads to a surprising relation
between knots and quivers: to a given knot we associate a quiver, so that various types of knot
invariants are expressed in terms of characteristics of a moduli space of representations of the
corresponding quiver. This statement can be regarded as a novel type of categoriﬁcation of knot
invariants, and among its various consequences we ﬁnd that Labastida-Mari˜ no-Ooguri-Vafa (LMOV)
invariants of a knot can be expressed in terms of motivic Donaldson-Thomas invariants of the
corresponding quiver; this proves integrality of LMOV invariants, conjectured originally based on
string theory and M-theory arguments.
In last few decades many intricate links between high
energy physics and contemporary mathematics have been
found. These links not only helped to solve some speciﬁc
problems, but also led to discovery of deep and earlier
unforeseen relations between diﬀerent branches of math-
ematics. In this letter we present a new chain of connec-
tions that in a similar vein relates a physical system – of
appropriately engineered branes in string theory – with
mathematical knot theory on one hand, and quiver rep-
resentation theory on the other hand, thereby revealing
deep links between these theories.
It is particularly interesting to determine exact results
in string theory. One source of such results are topo-
logical string amplitudes. Mathematically they encode
Gromov-Witten invariants, and from physics perspective
they capture degeneracies of BPS states formed by D-
branes. In case of closed string theory these degeneracies
are referred to as Gopakumar-Vafa invariants, and are
also conjecturally related to Donaldson-Thomas invari-
ants of underlying Calabi-Yau manifolds [1–3].
Analogous conjectures have been formulated for sys-
tems with additional branes. Mathematically they en-
code open Gromov-Witten invariants, and physically
they capture degeneracies of D-branes with boundaries.
Furthermore, it has been conjectured that in a sys-
tem with an appropriate choice of Calabi-Yau mani-
fold and brane conﬁguration, such open amplitudes en-
code knot invariants, in particular colored HOMFLY-PT
polynomials [4–6]. This relation is a non-trivial con-
sequence of famous relations between knot invariants,
Chern-Simons gauge theory, and topological string the-
ory [7, 8]. This relation also predicts, that – analo-
gously to the closed string case – colored HOMFLY-PT
polynomials are encoded in BPS invariants, referred to
as Labastida-Mari˜ no-Ooguri-Vafa (LMOV) invariants (or
Ooguri-Vafa invariants) [4–6]. Integrality of these invari-
ants is an important statement for both string theory and
knot theory, however it has been veriﬁed only in very spe-
ciﬁc cases e.g. in [4–6, 9, 10], and more recently for some
inﬁnite families of knots and representations [11, 12]. An
attempt to prove this conjecture – which however raised
some criticism – has been made in [13].
FIG. 1. Trefoil knot and the corresponding quiver.
arXiv:1707.02991v1  [hep-th]  10 Jul 2017
2
Knots Quivers
Homological degrees, framing Number of loops
Colored HOMFLY-PT Motivic generating series
LMOV invariants Motivic DT-invariants
Classical LMOV invariants Numerical DT-invariants
Algebra of BPS states Cohom. Hall Algebra
TABLE I. Identiﬁcation of quantities associated to knots and
quivers.
By standard arguments [4, 14, 15], BPS states in brane
systems – in particular those describing knots – should
have a description in terms of supersymmetric quantum
mechanics on their world-volume, which however has not
been identiﬁed to date. In this letter we argue that
such a description actually involves quiver quantum me-
chanics and identify relevant quivers. To this end we
also recall that, in another line of research, it was ar-
gued that BPS states in string theory form algebras [16].
More recently it has been postulated that such algebras
can be identiﬁed with Cohomological Hall Algebras [17],
and the associated theory of wall-crossing and motivic
Donaldson-Thomas invariants turned out to play an im-
portant role in supersymmetric gauge theories and string
theory. From mathematical perspective, these ideas can
be naturally implemented in the framework of quiver rep-
resentations and their moduli spaces [17–19].
In this letter we argue that BPS states enumerated
by motivic Donaldson-Thomas invariants of quiver mod-
uli spaces should be identiﬁed with those arising in the
supersymmetric quiver quantum mechanics description
of brane systems encoding knots. This observation has
far-reaching consequences: it leads to new ways of inter-
preting and computing BPS numbers, and to the (idea of
the) proof of the famous LMOV conjecture – and the ac-
tual proof for a large class of knots. From mathematical
perspective we ﬁnd direct, unexpected relations between
knots and quiver representation theory, which, in partic-
ular, lead to a novel categoriﬁcation of knot invariants.
In more detail, we claim that to each knot one can as-
sociate a quiver, whose moduli space of representations
encodes various types of knot invariants, including col-
ored HOMFLY-PT polynomials, homological invariants,
etc. In particular LMOV invariants of a given knot can
be expressed in terms of motivic Donaldson-Thomas in-
variants of the corresponding quiver, and integrality of
the latter implies integrality of the former ones, which is
how the proof of the LMOV conjecture follows. Identiﬁ-
cation of some quantities on both sides of “knots-quivers”
duality is summarized in table I. As an example, a quiver
corresponding to the trefoil knot is shown in ﬁg. 1.
Knot invariants, knot homologies, and LMOV
conjecture
Ever since its birth knot theory attracted attention
of physicists, and various knot invariants turned out to
have physical interpretation. In particular various knot
polynomials have been reinterpreted as expectation val-
ues in Chern-Simons theory in [7], and subsequently they
were expressed in terms of topological string theory am-
plitudes [8]. In [4] the topological string setup was related
to M-theory and it was argued, that colored HOMFLY-
PT polynomials are encoded in LMOV invariants, which
count bound states of open M2-branes with M5-branes.
In this work we show, among others, how – so far con-
jectural – integrality of these invariants can be proven.
Furthermore, more recently homological knot invari-
ants, such as Khovanov homology and its more involved
cousins [20–22], have been also realized in brane systems
in string theory, also revealing yet to be proved new prop-
erties of those invariants [23–25]. In what follows we show
that certain information about homological knot invari-
ants is also encoded in quiver moduli spaces.
Let us introduce ﬁrst the generating function of Sr-
colored HOMFLY-PT polynomials, which will be the
main object of the subsequent analysis, as well as cor-
responding LMOV invariants. To start with consider the
Ooguri-Vafa generating function [4–6, 26]
Z(U,V ) =
∑
R
TrRU TrRV = exp
( ∞∑
n=1
1
nTrUnTrVn
)
,
(1)
where U =P exp
∮
KA is the holonomy of U(N) Chern-
Simons gauge ﬁeld along a knot K, V plays a role of a
source, and the sum runs over all representations R, i.e.
all two-dimensional partitions. The LMOV conjecture
states that the expectation value of (1) takes form
⟨
Z(U,V )
⟩
=
∑
R
PR(a,q )TrRV =
= exp
( ∞∑
n=1
∑
R
1
nfR(an,qn)TrRVn
)
, (2)
where the expectation value of the holonomy is identiﬁed
with the unreduced HOMFLY-PT polynomial of a knot
K,⟨TrRU⟩ =PR(a,q ) = P 01
R PR(a,q ) (where P 01
R is the
unknot factor), and the functions
fR(a,q ) =
∑
i,j
NR,i,jaiqj
q−q−1 (3)
encode conjecturally integer LMOV (or Ooguri-Vafa) in-
variantsNR,i,j, counting bound states of M2-branes end-
ing on M5-branes. These functions take form of universal
polynomials in colored HOMFLY-PT polynomials.
In what follows we consider one-dimensional source
V =x. In this case Tr RV ⁄= 0 only for symmetric repre-
sentations R =Sr, so that TrSr(x) = xr. Let us denote
3
P (x) =⟨Z(U,x )⟩, and let Pr(a,q ) denote the Sr-colored
HOMFLY-PT polynomial of K, so that (2) takes form
P (x) =
∞∑
r=0
Pr(a,q )xr =e
∑
r,n≥1
1
nfr(an,qn)xnr
. (4)
In this case fr(a,q ) ≡ fSr(a,q ) = ∑
i,j
Nr,i,jaiqj
q−q−1 , for
Nr,i,j≡NSr,i,j, are polynomials inPd1(ad2,qd2) for some
d1 and d2 (such that d1d2≤r), e.g. f1(a,q ) =P 1(a,q ),
f2(a,q ) =P 2(a,q )− 1
2P 1(a,q )2− 1
2P 1(a2,q 2), (5)
etc. It follows that (4) can be rewritten in product form
P (x) =
∏
r≥1;i,j;k≥0
(
1−xraiqj+2k+1
)Nr,i,j
. (6)
Integrality of BPS degeneracies Nr,i,j encoded in this
product is one important outcome of our work.
Another outcome of our work is a surprising relation
of colored HOMFLY-PT polynomials, or their generat-
ing function (4), to superpolynomials, i.e. the Poincar´ e
polynomials of the uncolored HOMFLY-PT homologies
of knots [24]. More generally, one can consider colored
HOMFLY-PT homologyHSr
i,j,k that has not been deﬁned
rigorously by mathematicians, however its conjectural
(reduced) colored superpolynomial
Pr(a,q,t ) =
∑
i,j,k
aiqjtk dimHSr
i,j,k (7)
can be very eﬀectively computed for various families of
knots, using the formalism of diﬀerentials [24, 25, 27, 28].
Note that generalizations of the LMOV conjecture to the
case of superpolynomials have been considered in [11, 29].
For example, for trefoil knot 31, eq. (7) takes form [30]
Pr(a,q,t ) = a2r
q2r
r∑
k=0
[r
k
]
q2k(r+1)t2k
k∏
i=1
(1 +a2q2(i−2)t),
(8)
where
[r
k
]
= (q2;q2)r
(q2;q2)k(q2;q2)r−k
, and the q-Pochhammer
symbol is deﬁned as (z;q)n =∏n−1
i=0 (1−zqi). For t =−1
(8) specializes to the reduced colored HOMFLY-PT poly-
nomial, while in the uncolored (r = 1) case it reduces to
P1(a,q,t ) = a2
q2 +a2q2t2 +a4t3. (9)
The monomials in this expression correspond to genera-
tors of the HOMFLY-PT homology, and powers of t in
each monomial – in this example taking values (0, 2, 3) –
are referred to as homological degrees.
