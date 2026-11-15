---
doc_id: arxiv-1707.02991v1
doc_title: "BPS states, knots and quivers"
section_id: sec-000-bps-states-knots-and-quivers
section_title: "BPS states, knots and quivers"
section_number: null
pages: 1-2
source_pdf: 1707.02991v1.pdf
source_sha256: f4f539f74403dd24
toc_source: outline
doc_brief: "BPS states, knots and quivers — 7 sections: Front matter; BPS states, knots and quivers; Knot invariants, knot homologies"
---
Piotr Kucharski1, Markus Reineke2, Marko Stoˇsi´c3,4, and Piotr Su lkowski1,5
1 Faculty of Physics, University of Warsaw,
ul.
Pasteura 5, 02-093 Warsaw, Poland
2 Faculty of Mathematics, Ruhr-Universit¨at Bochum,
Universit¨atsstrasse 150, 44780 Bochum, Germany
3 CAMGSD, Departamento de Matem´atica,
Instituto Superior T´ecnico,
Av.
Rovisco Pais, 1049-001 Lisboa, Portugal
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
invariants, and among its various consequences we ﬁnd that Labastida-Mari˜no-Ooguri-Vafa (LMOV)
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
in string theory.
One source of such results are topo-
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
polynomials [4–6].
This relation is a non-trivial con-
sequence of famous relations between knot invariants,
Chern-Simons gauge theory, and topological string the-
ory [7, 8].
This relation also predicts, that – analo-
gously to the closed string case – colored HOMFLY-PT
polynomials are encoded in BPS invariants, referred to
as Labastida-Mari˜no-Ooguri-Vafa (LMOV) invariants (or
Ooguri-Vafa invariants) [4–6]. Integrality of these invari-
ants is an important statement for both string theory and
knot theory, however it has been veriﬁed only in very spe-
ciﬁc cases e.g. in [4–6, 9, 10], and more recently for some
inﬁnite families of knots and representations [11, 12]. An
attempt to prove this conjecture – which however raised
some criticism – has been made in [13].
FIG. 1. Trefoil knot and the corresponding quiver.
arXiv:1707.02991v1  [hep-th]  10 Jul 2017
Knots
Quivers
Homological degrees, framing
Number of loops
Colored HOMFLY-PT
Motivic generating series
LMOV invariants
Motivic DT-invariants
Classical LMOV invariants
Numerical DT-invariants
Algebra of BPS states
Cohom. Hall Algebra
TABLE I. Identiﬁcation of quantities associated to knots and
quivers.
By standard arguments [4, 14, 15], BPS states in brane
systems – in particular those describing knots – should
have a description in terms of supersymmetric quantum
mechanics on their world-volume, which however has not
been identiﬁed to date.
In this letter we argue that
such a description actually involves quiver quantum me-
chanics and identify relevant quivers.
To this end we
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
