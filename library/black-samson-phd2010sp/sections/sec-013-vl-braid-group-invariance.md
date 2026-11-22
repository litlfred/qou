---
doc_id: black-samson-phd2010sp
doc_title: "REPRESENTATIONS OF HECKE"
section_id: sec-013-vl-braid-group-invariance
section_title: "V.l. Braid Group Invariance"
section_number: null
pages: 49-51
source_pdf: Black_Samson_phd2010sp.pdf
source_sha256: c16799b0bd54ff29
toc_source: inferred
doc_brief: "REPRESENTATIONS OF HECKE — 16 sections: Front matter; INTRODUCTION; ILL Links and Braids"
---
Braid Group Invariance
For a permutation diagram x, let 7r(x) E Sd denote the underlying permutation.
Let
pT,(a) = {x permutation diagram satisfying (PI) /7r(x) = 7r}.
Notice that P1(a) = P(a), the
admissible diagrams. 'vVe have immediately:
P(afJ)
IT {xy I x E P,,(a) and y E P,,-l (fJ)}
"ESd
IT P,,(a) x P,,-1(fJ)
"ESd
(V.l)
\iVith signs attached to the strands in the diagrams, we have the analogous definition of S,,(a) and
the decomposition:
S(afJ) ~ IT S,,(a) x S,,-1 (fJ)·
"ESd
(V.2)
\iVe prove a Lemma now that shows that the function A is invariant under concatenation
for certain pairs of braid words. For 7r E Sd, define
A,,(a) =
I.: (c:)M(a,x,c:)
(x,c)ES,,(ex)
(V.3)
Lemma V.l.l. Suppose that fJ, fJl E ~j satisfy A,,(fJ) = A,,(fJ') faT' all 7r E Sd.
Then, A(afJ) =
A(afJ') and A(fJa) = A(fJ'o:) for any 0: E ~j.
42
P7'Oof. Let Srr(a,f3) = S7T(a) x SCI ({3).
L (cv)M(a{3, xy, EV)
S, (ex,(3)
1
A(a(3) = 1dJ L
7TE S d
1
= 1dJ L
L
(E)M(a, x, E) L
(v)M({3, y, v)
7TES" (x.E)ES,,(a)
(Y,l/)ES,,-I ((3)
1
= [d] L
L
(E)l\1(a, x, E) A 7T-I ({3)
7TES" (x,E)ES,,(a)
(VA)
(V.5)
(V.6)
This last expression is equal to A(a{3'), using the fact that A7T ((3)
A({3a) = A({3'a) is completely analogous and is omitted.
A7T ({3').
The proof that
o
Proposition V.1.2. If a, (3 E I:d represent the same group element in 3 d , then A(a) = A({3).
Proof. Identity. A(1a) = A(a) = A(a1).
This is clear since A is defined by resolving crossings in the braid diagram. For the remainder of
the proof, we use Lemma V.l.1, checking cases according to permutations 7f.
Inverse.
A((J;!=I(J~I) = A(0).
Let (x,c) E S7T((J,.(J,~I), where 7r = 7r(x). We must show that A7T ((Jr(J;I) = 1 when 7r = 1 and 0
otherwise.
(Case 7r = 1). If the signs on strands rand r + 1 match, then the only available diagrams
have the crossings (Jr(J;1 resolved straight through. If (cr,Er+d = (+,+), then M((Jr(J;I,X,c) =
v· V-I = 1. And with (-, -),
M((Jr(J,~l,x,E) = (_V-I). (-V) = 1. If Er i- Er+l, then there are
two possible resolutions that form states, as illustrated.
I \
+ -
or Q
+ -
With (cr, cr+d = (+, -), we calculate the contribution of the two states is
_v- r
-v r
[r+1]
[r-1]
--.-+--.--
IT]
[r]
[r]
[r]'
which equals 1, using Lemma V.2.3.
With (cr' Er+d = (-, +), a similar calculation establishes
equality.
43
then there are two possible resolutions that form states, as illustrated.
~
+ -
or ><
+ -
'With (cTlcr+Jl = (+, -), we calculate the contribution from the two states is
[1'-1]
-vr
v r
[1'-1]
--·-+-·--=0.
[1']
[1']
[1']
[1']
The calculation with (cr,cr+Jl = (+, -) is analogous and is omitted.
Braid relations. A((Jr(Js) = A((Js(Jr) when IT - sl > 1. This is a simple calculation only
using the commutativity of the ring C(v).
A((Jr(Jr+)tJr)
=
A((Jr+l(Jr(Jr+l).
Let x (resp., y) denote a permutation diagram for
(Jr(Jr+l(Jr (resp., (Jr+l(Jr(Jr+l)'
Again, we organize by cases -rr = -rr(x) = -rr(y).
In Figure V.2,
the possible permutation diagrams are shown with labels suggesting the possible signs on those
strands.
For example, the label (a, b, b) indicates that possible signs are (+, +, -), (+, -, +),
(-, +, -), or (-, -, +). Permutations are named by how they act on strands 1', l' + 1, and l' + 2.
Notice that for -rr = (3 2 1), there are no ways to assign signs, as each pair of strands crosses.
,Ve illustrate one calculation (of twenty):
-rr = 1 and (cr' Cr+l, Cr+2) = (-, -, +). These
signs match each of the patterns except (a, a, c), so it suffices to verify that the following equation
holds:
This is equivalent to showing that vr~l[T + 1] = ~_v2r+l + Vr[T + 2], which follows from Lemma
V.2.3.
0
V.2.
