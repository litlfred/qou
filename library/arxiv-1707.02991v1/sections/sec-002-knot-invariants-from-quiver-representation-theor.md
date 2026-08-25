---
doc_id: arxiv-1707.02991v1
doc_title: "BPS states, knots and quivers"
section_id: sec-002-knot-invariants-from-quiver-representation-theor
section_title: "Knot invariants from quiver representation theory"
section_number: null
pages: 3-4
source_pdf: 1707.02991v1.pdf
source_sha256: f4f539f74403dd24
doc_brief: "BPS states, knots and quivers — 5 sections: BPS states, knots and quivers; Moduli of quiver representations; Knot invariants from quiver repres"
---
We present now our main claim, which is the state-
ment that various types of knot invariants, for a given
knot, are encoded in the data of moduli spaces of quiver
representations of a certain quiver, assigned to this knot.
As explained in the introduction, from physical perspec-
tive this is a consequence of the supersymmetric quiver
quantum mechanics description of BPS states in brane
systems representing knots. Technically this statement
is a consequence of our observation – which we pose as a
general conjecture – that generating functions of colored
HOMFLY-PT polynomials (4) can be written in the form
P (x) =
∑
d1,...,dm≥0
q
∑
i,jCi,jdidj
∏m
i=1xdiqlidiaaidi(−1)tidi
∏m
i=1(q2;q2)di
(12)
4
where C is a symmetric m×m matrix, and li,ai and ti
are ﬁxed integers. Remarkably, this expression has the
same form as the motivic generating function (10) of a
certain quiver, up to q↦→−q and the specialization
xi =xaaiqli−1(−1)ti. (13)
In particular terms proportional to xr in (12), with ﬁxed
r, arise from sets of {di} such that r = d1 +... +dm.
Rewriting of (4) in the form (12) means that the matrix
C can be identiﬁed as a matrix representing a quiver with
m vertices, such that Ci,j denotes the number of arrows
from vertex i to j (and so Ci,i denotes the number of
loops at vertex i). Therefore, if colored HOMFLY-PT
polynomials for a given knot are known, after rewriting
the generating function (4) in the form (12), from the
form of C the corresponding quiver can be identiﬁed.
This also means that colored HOMFLY-PT polynomials
for a given knot are encoded in a ﬁnite number of pa-
rameters that determine (12): the matrix C and integers
li,ai andti. Furthermore, these parameters take speciﬁc
values, which are encoded in uncolored superpolynomial.
Recall that the uncolored, reduced superpolynomial for a
given knot (such as (9) for the trefoil), is a sum of mono-
mials of the form aaiqqitti, which correspond to genera-
tors of the HOMFLY-PT homology. We claim that the
size of the matrixC (and so the number of vertices in the
corresponding quiver) is equal to the number of such gen-
erators. Moreover, with appropriate ordering of vertices,
ti in (12) are to be identiﬁed with homological degrees of
generators of HOMFLY-PT homology, diagonal elements
ofC are also equal to homological degrees, i.e. Ci,i =ti,
coeﬃcients of linear powers of q take form li = qi−ti,
and ai are equal to a-degree of generators of uncolored
HOMFLY homology. An additional minus sign in (12)
comes with the power determined by ti, so that it is rel-
evant only for the generators with odd t-grading. Note
that it follows, that homological degrees ti can be read
oﬀ from the generating series (4) rewritten in the quiver-
like form, i.e. they are given by the numbers of loops
in the corresponding quiver; this means, that the uncol-
ored superpolynomial is encoded in the form of colored
HOMFLY-PT polynomials, which is a rather non-trivial
and previously unknown statement.
Note that the values of parameters li,ai and Ci,i de-
pend in fact on a choice of normalization ofPr(a,q ). The
values mentioned above, related to unreduced and uncol-
ored superpolynomial, arise when normalization includes
only the denominator of the colored HOMFLY-PT poly-
nomial of the unknot Pr(a,q ) = Pr(a,q )/(q2;q2)r. Per-
haps more familiar normalization by the full unknot poly-
nomial Pr(a,q ) = a−rqr (a2;q2)r
(q2;q2)r
Pr(a,q ) leads to identiﬁ-
cation with another version of HOMFLY-PT homology
and to twice larger quiver [34].
The above conjecture has very nontrivial consequences.
In general it implies that various knot invariants are spe-
cializations of certain quiver moduli invariants. In par-
ticular, under the above specialization the product de-
composition (11) is identiﬁed with the product decom-
position (6). It follows that LMOV invariants Nr,i,j can
be expressed as linear combinations (with integer coeﬃ-
cients) of motivic Donaldson-Thomas invariants Ω d,j≡
Ωd1,...,dm;j. As motivic Donaldson-Thomas invariants are
proven to be integer, it follows that corresponding LMOV
invariants are also integer, which proves the LMOV con-
jecture! We are able to prove this statement for many
speciﬁc knots (and arbitrary symmetric representations),
including some inﬁnite families of knots (e.g. twist knots,
certain classes of torus knots), analogously as in the case
of trefoil knot, which is analyzed in detail below. More-
over, the limitq→ 1 of the motivic generating series im-
mediately implies integrality of classical LMOV invari-
ants br,i = ∑
jNr,i,j (considered for example in [11]),
which are then expressed in terms of (integer) numerical
Donaldson-Thomas invariants. Moreover, the fact that
LMOV invariants and (generating functions of) colored
HOMFLY-PT polynomials are expressed in terms of mo-
tivic Donaldson-Thomas invariants – which arise as cer-
tain Betti numbers of quiver moduli spaces – provides a
novel categoriﬁcation of these knot invariants.
Some other relations between knots and quivers that
follow from our conjecture are listed in table I. For exam-
ple, the framing byf∈ Z changes the colored HOMFLY-
PT polynomial by a factor, that for Sr-symmetric rep-
resentation takes form a2frqr(r−1). The term with
quadratic power of q, i.e. qfr 2
=qf(∑
idi)2
=qf ∑
i,jdidj,
shifts all elements of C by f, which in the dual quiver
adds f loops at each vertex and f pairs of oppositely-
oriented arrows between all pairs of vertices. Moreover,
as predicted in [17], the Cohomological Hall Algebra as-
sociated to a quiver should be identiﬁed as the algebra
of BPS states [16], which deserves further studies in the
context of brane realization of knot invariants.
