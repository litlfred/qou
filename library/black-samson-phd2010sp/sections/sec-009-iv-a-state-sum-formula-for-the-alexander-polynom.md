---
doc_id: black-samson-phd2010sp
doc_title: "REPRESENTATIONS OF HECKE"
section_id: sec-009-iv-a-state-sum-formula-for-the-alexander-polynom
section_title: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL"
section_number: IV
pages: 42-45
source_pdf: Black_Samson_phd2010sp.pdf
source_sha256: c16799b0bd54ff29
toc_source: inferred
doc_brief: "REPRESENTATIONS OF HECKE — 16 sections: Front matter; INTRODUCTION; ILL Links and Braids"
---
IV.I.
Semi-normal Representations of the Heeke Algebra
Much of the following is standard (see e.g. [11] or [25, chapters 4 and 5]). We collect some
of the definitions here and fix some notation. In what follows, [r] E Z[v, V-I] denotes the quantum
integer
(IV.1)
for any T E Z.
IV.i.i.
Serninormal RepTesentations
This exposition follows [35, section 3], although the results were originally worked out in
[19]. For a new point of view and substantial generalization, see [8, section 5].
Let Tab(A) denote the set of A-tableaux.
These are fillings of the boxes in the Young
diagram A by the numbers 1, ... ,d.
Let Std(A) denote the set of standard A-tableaux, namely
those that increase across rows and down columns. The symmetric group Sel acts on Tab(A) via
its natural action on the entries, although Std(A) is not stable under this action. For a tableau
T E Tab(A), its residue seq'uence (il, ... ,iel) E Zel is defined by setting iT' = b - a where the box
labeled T in T appears in row a and column b.
T = ffiillJ
T - [I[]JiJ
82 -~
Figure
IV.!: The partition A = (3,1) E Par(4) and standard tableaux T and 52T. Here, T has
residue sequence (0,1, -1, 2).
Fix a partition A E Par(n) and let S(A) be the C(v)-vector space on basis {XI IT E Std(A)}.
35
Let (i j , ... ,id) be the residue sequence ofT and define ar(T),br(T) E C(v) to be
(IV,2)
Define actions of the generators H j ,.", Hd- j of Hd on S(A) by
Hrxr = ar(T)xr + br(T)xs,r,
where we interpret xs,.r = 0 if SrT is not a standard tableau,
(IV.3)
Theorem IV.lol (Semi-normal representations). This action extends to make S(A) into a well-
defined Hd-module.
Furthermore, the modules {S(A) I A E Par(d)} constitute a complete set of
pairwise non-isomorphic irreducible modules for Hd.
IV 1.2.
Sign Sequences and Hook Partitions
For 0 :::; g:::; d -1, let A£ be the hook partition (d - g, If). We refer to g as leg length,
Lemma IV.lo2. Standard tableaux of shape A£ are in bijeci'ion with sign sequences C = (cl' .. , ,Cd) E
{±}d such that C j = + and g entries equal -.
Proof. Beginning with a standard Af-tableau, define C =
(Cj"
.. ,ceL) by
if r appears on the first row
otherwise
(IVA)
Notice that the box labeled 1 has to be in the corner of the hook, so Cj = +. Also, g numbers are
on the leg of the hook, so there are g entries equal to -,
For the inverse, starting with a sign sequence C = (cj,' .. , cd) with Cj = + and g other
entries equal to -, construct a standard tableau recursively, as follows. Place 1 in the corner of
the diagram. Now, for each l' > 1, suppose that the numbers 1, ' . , ,r - 1 have been placed. Either
add r to the end of the first row or at the bottom of the first column, according to whether Cr is
+ or -, respectively.
o
Using this bijection, we can adapt the semi-normal representation to the combinatorics of
sign sequences,
36
Theorem IV.1.3. The irreducible module S(Ae) has basis {x,,,}, where C 'rUns over sign sequences
ha'uing C1 = + and £ other entTies equal to -. The generators H1, ... , Hk-1 of Hd act by
(IV.5)
where SrC denotes the sign sequence obtained from C by permuting Cr and cr+ 1,
Xc is interpreted
as zero if C1 = -, and
if (croCr+1) = (+,+)
if (cr,cr+d =
(~,-)
'i!(Cro Cr+1) = (-,+)
if (cr,cr+d = (+,-),
'if (cr,cr+d = (-,+)
if (cr,cr+d = (+,-)
otherwise.
The inverse generators H j 1 , ... , Hd~ 1 act by
where ar (c) is obtained from ar (c) by replacing v by v- 1 .
(IV.6)
(IV.7)
(IV.S)
Proof. This is just a translation of Theorem IV.I.1 using the bijection from Lemma IV.I.2. Given a
sign sequence C E {±}k having C1 = + and £ other entries equal to -, construct the corresponding
standard tableau, and let (i 1 , ... , i d ) be its residue sequence. We have i 1 = 0, and for 1 S; r < d,
ir + 1
if (cr,cr+1) = (+,+)
ir -1
if (cr,Cr+1) = (-,-)
(IV.9)
ir+1 =
i r +r
if (C.r,cr+1) = (-,+)
i r
- r
if (cr, cr+d = (+, -).
Given this, the formulae (IV.6)-(IV.7) are easily deduced from (IV.2). Finally the formula (IV.S)
is easily deduced from (IV..S) since H;l = Hr
-
(v - v- 1 ).
o
37
