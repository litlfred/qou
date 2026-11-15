---
doc_id: black-samson-phd2010sp
doc_title: "REPRESENTATIONS OF HECKE"
section_id: sec-010-iv-2-construction-of-the-state-sum
section_title: "2. Construction of the State-sum"
section_number: IV
pages: 45-48
source_pdf: Black_Samson_phd2010sp.pdf
source_sha256: c16799b0bd54ff29
toc_source: inferred
doc_brief: "REPRESENTATIONS OF HECKE — 16 sections: Front matter; INTRODUCTION; ILL Links and Braids"
---
Construction of the State-sum
Begin with a word a E I;d in the braid generators 0"1, ... ,0"d-I and their inverses, which
we picture as a diagram drawn up the page as the word is read from right to left.
O"r = I ... I X I .. · I
r r+1
0",-:-1 = I ... I X I .. · I
r r+1
Construct permutation diagrams from the braid diagram by replacing each crossing by one
of two resolutions:
x
x
I
I
I
I
or
or x
x
Definition IV.2.1. A permutation diagram x is admissible if
(PI) the first (leftmost) strand goes straight through without crossing any other strands, and
(P2) the underlying permutation is the identity.
A state is a pair (X,E), where x is an admissible permutation diagram and E is an assignment of a
sign ± to each strand such that
(SI) the first (leftmost) sign is +, and
(S2) no two strands of the same sign cross.
Let Sea) denote the set of states for a. To a state (x, E) E Sea), we associate a weight
M(a, x. E) E C(v) defined by multiplying together certain scalars, one for each resolved crossing.
The scalar associated to a positive crossing of strands in positions rand r + 1 is given in (IV.I0).
For a negative crossing, replace v by V-I in each expression.
38
+
+
x
r
r+1
[1'] I
I
+
I
I
+
(IV.IO)
Define A(a) E C(v) by
[1'+1] X
[1']
+
[1'-1] X
-[1']-
+
1
A(a) =
[d]
L
(c)M(a, x, c)
(x,E)ES(a)
where (c) E {±I} is the product of the signs CI, ... ,Cd attached to the strands.
(IV.H)
Theorem IV.2.2. Let L be an oriented link, and let a E Ed represent a braid in Ed such that
0: = L. Then, A(a) is a polynomial in v - V-I, and
A(a) = \1(L),
where \7(L) is the Conway-normalized Alexander polynomial with z = v - V-I.
Proof. To avoid confusion when switching between the generators Hr and Tr = vHr of H d , let us
write'P : Ed -» H: for the group homomorphism given by 'P(o-r) = Hr and ¢ : Ed -» H~ for the
one with ¢(o-r) = Tr. Formula (7.2) in [24] gives the Alexander polynomial for a link L as
(IV.I2)
where:(£ = tr OPe is the character of Hd arising from the irreducible representation Pe : Hd
-'I
End(S(Ae)) indexed by the hook partition (d - e, Ie), and e is the exponent sum of a. Put q = v2
39
and Tr = uH" for each r, so that ¢ira) = ve(Cllip(a). Reindex the sum over £ = d - 1 - j to get
\7(L)
d-I
[~] 2:)-I)£X£(ip(a)).
£=0
(IV.13)
Now we compute x£ by using the semi-normal form for S(>,£). The action of the generators
Hr. H,-:I on Xc from Theorem IV.1.3 are pictured in (IV.14).
r
r+1
Cr
Cr+l
C,'+I
Cr
a,,(c) I
+
br(c) X
Cr
cr+l
Cr
cr+l
(IV.14)
Cr
c,'+1
cr+1
C"
ar(c) I
+
br(c) X
Cr
C,'+I
Cr
Cr+l
Moreover, if r
=
1, the second term on the right hand side should be omitted.
Only diagonal
entries of the matrix p£(ip(a)) contribute to the trace. Hence, for each £ we need only consider
those permutation diagrams that represent the identity permutation and whose first strand goes
straight through. The theorem follows 011 comparing formulas (IV.6) and (IV.7) with (IV.I0).
0
40
