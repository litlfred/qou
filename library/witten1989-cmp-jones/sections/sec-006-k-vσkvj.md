---
doc_id: witten1989-cmp-jones
doc_title: "Commun. Math. Phys. 121, 351-399 (1989) Mathematical Physics © Springer-Verlag 1989 Quantum Field Theory and the Jones Polynomial Edward Witten **"
section_id: sec-006-k-vσkvj
section_title: "V^ΣK/VJ."
section_number: K
pages: 35-38
source_pdf: witten1989-cmp-jones.pdf
source_sha256: 32f98ed8f7b23588
toc_source: inferred
doc_brief: "Quantum field theory and the Jones polynomial (Witten, Commun. Math. Phys. 121 (1989) 351–399) — Chern–Simons gauge theory gives the Jones polynomial; framing dependence of Wilson loops"
---
(4.25)
j
In the space spanned by the ι;ί5 there is a natural inner product, defined by the
tensor gtj which is one if Rt is the dual oΐRj and zero otherwise. We may sometimes
use this metric to raise and lower indices, letting Ktj = ΣgmjKi™-
m
We can now get a much more concrete description of the behavior of the
quantum field theory partition function under surgery. In discussing surgery, we
began with a three manifold M and a knot C. Cutting out a tubular neighborhood
of this knot, whose boundary we call Σ, we separated M into ML and MR, with MR
being a solid torus. The path integrals on ML and MR gave vectors ψ and χ in the
Hubert spaces #fL and 3CR. As we have just noted, χ is the same as u 0, so the
partition function on M is (ψ, v0). Now we want to make a diffeomorphism K on
the boundary of MR, and then glue together ML and MR to make a new three
manifold M. The partition function of Mis Z (M) = (ψ, KvQ), as we saw in the last
section. To say that Z(M) is computable from a surgery presentation means that
the evaluation of this invariant of Mean be reduced to tractable calculation on M.
We will now show this. From (4.25), we can write
Z(M) = Σ
κo
j(ψ>Vj) 
(4-26)
j
But each term ((//, Vj) has an interpretation in terms of path integrals on M! Indeed,
it is the very definition of the Vj that Vj differs from vQ just by an insertion of an
extra Wilson line in the Rj representation at the center of MR. So just as (ψ, v0)
represents the original partition function of M, (ψ, ΌJ} represents a modified
partition function with an extra Wilson line in the Rj representation placed on C.
So we rewrite (4.26) in the form
Z(M) = £V Z(M;^.), 
(4.27)
j
where Z (M; Rj) is the partition function of M with an extra Wilson line in the Rj
representation included on the circle C (in addition to whatever Wilson lines are
already present on M). This is indicated in Fig. 12c. To use (4.27), one needs to
know the matrix Kt
j, which is precisely the matrix by which the diffeomorphism K
of the torus is represented on the characters of the irreducible level k represen-
tations of LG; these matrices appear in [37] and have remarkable properties
' The b cycle on the boundary of U gives a framing of this Wilson line
386 
E. Wittcn
recently investigated in [12,13]. Given a knowledge of the Kt
j , (4.27) is a
completely explicit formula expressing computations on M in terms of computa-
tions on M. By repeated use of this formula, computations on any three manifold
can be reduced to computations on S
3,
 13 with appropriate Wilson lines. Of
course, the surgery will generate Wilson lines on S
 3 in representations of G
corresponding to arbitrary integrable representations of LG.
Generalized Surgery. The surgery law (4.27) has a useful generalization. While so
far we have only considered surgery on a purely imaginary circle C, as in Fig. 12,
there is no reason not to generalize this to a situation in which before the surgery a
Wilson line in the R{ representation was already present on C. Surgery amounts to
cutting out a neighborhood of C and then gluing it back in, and after this process
the Rt Wilson line will still be present in M. So the left-hand side of (4.27) is
replaced by Z(M; T^ ), where the notation schematically indicates the presence of
the Rt Wilson line. What about the right-hand side of (4.27)? Before surgery, with a
Wilson line Ri on C, the path integral on a tubular neighborhood U of C gives on
the boundary a state/' = vt\ this is the generalization of (4.24). If we cut out Cand
glue it back in with a diffeomorphism K of the boundary, then υt is replaced
according to (4.25) with K * vj . If we remember that ΌJ could have been obtained by
putting a Wilson line on C in the Rj representation, we see that the right-hand side
of (4.27) becomes ^K/ Z(M;Rj), so we get the generalized surgery formula
j). 
(4.28)
j
This formula will be used later in a new proof of Verlinde's conjecture.
Cabling of Knots; Satellites. Finally, let us note that similar methods can be used
to determine the behavior of the knot invariants under "cabling", and more
generally to relate the invariants of the "satellites" of a knot to invariants of the
original knot. Any knot C in any three manifold Mhas a neighborhood that looks
like a solid torus U. If we replace Cby an arbitrary satellite C of itself (an arbitrary
knot that can be placed in [/), with representations Rσ associated with the
connected components of C, then the path integral on U will define a vector ψ in
the physical Hubert space 3fΣ associated with the boundary Σ of U. Like any
vector in jjfΣ, ψ can be expanded in the Verlinde basis,
v = Σ«i"i 
(
4 29)
The αf are complex numbers that depend on the choice of satellite C and on the
choice of representations Rσ, but they do not depend on what three manifold M
the solid torus [/has been extracted from or on what other knots are present on M.
The vectors vt e <tffΣ are the vectors that would be produced by the path integral on
U with a Wilson line in the Rt representation placed on the original knot C (and
not a satellite of C). Thus, a knowledge of the invariants of C in arbitrary
representations together with a knowledge of the universal coefficients αf is
enough to determine the invariants of arbitrary satellites of C.
* Or on any desired three manifold; we will see that S
2 x S
l is more tractable than
Quantum Field Theory and the Jones Polynomial
387
a 
X 
b 
S2 
(
Fig. 14a-c. Beginning with Xxl, shown in a, one makes XxS
1 by identifying Xx {0} with
Xx {!}. If X is S
2 with some marked points Ph then this construction gives the picture of b. If
S
2 x {0} is joined to S
2 x {1} via a non-trivial diffeomorphism B, one makes in this way a braid, as
4.4. Path Integrals on S
1 x X
In this subsection we will describe a few facts which are useful in their own right
and will enable us to carry out some concrete surgeries.
First of all, we have not so far determined the partition function of S
3 without
Wilson lines. It may come as a surprise to topologists that we cannot trivially
assert that this is 1 . In quantum field theory there is no particularly strong axiom
governing the partition function of -S
3. The three manifolds whose partition
functions can be computed in a particularly simple way, from the axioms of
quantum field theory, are those of the form Xx S
1, for various X. Xx S
1 can
conveniently be studied in a "Hamiltonian" formalism, as indicated in Fig. 14a.
One constructs the Hubert space J4fx of X. Then one introduces a "time" direction,
represented by a unit interval 7 = [0, 1], and one propagates the vectors in jΊfx from
"time" 0 to "time" 1. This operation is trivial, since the Chern-Simons theory, like
any generally covariant theory, has a vanishing Hamiltonian. Finally, one forms
Xx S
1 by gluing Xx {0} to A'x {!}; this identifies the initial and final states, giving
a trace:
Z(Xx S
1) = Tι>x(l) - dim«#V 
(4.30)
For example, the physical Hubert space of S
2 is one dimensional, for any G and k,
so one has
Z(S
2x5
1) = 1. 
(4.31)
It is possible to generalize (4.30) as follows. If we are given a diffeomorphism
K: X->X, then one can form the mapping cylinder X xκ S
 l by identifying x x { 1 }
with K(x) x {0} for every xeX. At the level of quantum field theory, when one
goes from X x / to X x KS
l, the initial and final states are identified via K, so the
generalization of (4.30) is
κS
ΐ) = ττ^x(K). 
(4.32)
The situation that we actually wish to apply this to is the case in which Xis S
2
with some marked points Pa,a=\ ... sio which representations Ri(a) are assigned.
388 
E.Witten
[For a=\ ... s , ί ( a ) i s one of the values 0 ... t — 1 corresponding to integrable level
k representations of the loop group.] In this case, the simple product Xx S
1 is just
S
2 x S
1 with some Wilson lines which are unknotted, parallel circles of the form
{Pa} x S
1, as sketched in Fig. 14b. To determine the path integral on S
2 x S
1 in
the presence of these Wilson lines, which we will denote as Z(S
2 x S
1; C^)λ one
needs to study the Hubert space of S
2 with charges in the representations Rttι\ we
will denote this as ^S2;<R>. The analog of (4.31) is then
Z(S
2xS
l; <^»-dimJf s 2 ; < κ >. 
(4.33)
The dimensions of these spaces were discussed at the end of Sect. 3. Thus, if the
collection of representations <J^> consists of a single representation Ra, we get
Z(S
2xS
1;/? e) = ^ 0 9 
(4-34)
since the physical Hubert space with a single charge in the Ra representation is one
dimensional if Ra is the trivial representation (a — 0) and zero dimensional
otherwise.
14 For two charges in the representations Ra and Rb, we get
Z(S
2xS
ί',Ra9Rb) = gab, 
(4.35)
where gab, introduced earlier, is 1 if Rb is the dual of Ra and zero otherwise. The
formula (4.35) follows from the result of Sect. (4.4) for the Hubert space on S
2
with two charges. Finally, if there are three charges in the representations Ra, Rb,
Rc, we get
xS
ί\R0,Rb,Rc) = Nabc, 
(4.36)
with Nabc the trilinear "coupling" of Verlinde, since this is the dimension of the
physical Hubert space.
4.5. Some Concrete Surgeries
Now we would like to describe some useful results that can be obtained from
concrete surgeries. The first goal is compute the partition function of S
