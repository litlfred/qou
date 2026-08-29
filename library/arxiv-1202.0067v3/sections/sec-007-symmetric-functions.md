---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN\u2013NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON"
section_id: sec-007-symmetric-functions
section_title: "Symmetric functions"
section_number: 7
pages: 30-33
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON — 8 sections: Introduction; Deflation by averaging; Skew characters"
---
Finally, we discuss the translation of our results into the language of
symmetric functions. The following well-known facts can be found in [12,
Chapter I]. Let Λ be the ring of symmetric functions with integer coefficients
L
in variables x1 , x2 , . . ., and let R =
n≥0 C(Sn ). There is a well-known
canonical ring isomorphism ch : R → Λ, where the ring structure on R is
given, for f ∈ C(Sm ) and g ∈ C(Sn ), by f g = IndSSmn
(f × g). Moreover,
m ×Sn
the map ch is an isometry with respect to the standard inner products h·, ·i
on R and Λ. If λ/µ is any skew-partition, then ch(χλ/µ ) = sλ/µ , the skew
Schur function corresponding to λ/µ. Furthermore, suppose that β and ν
are partitions, with |β| = m and |ν| = n. Denote by sν ◦ sβ the plethysm of
sν and sβ (see [12, §I.8]). Then


^
β )×n Inf Sm oSn χν ) = s ◦ s
(12)
ch IndSSmn
(
(χ
ν
β
Sn
m oSn
(see [12, §I.8 and §I.A.6]). By first using Frobenius reciprocity, then the
inflation-deflation reciprocity relation of Equation (11), we have
D
E D
E
β
^
β )×n Inf Sm oSn χν ), χλ/µ = χν , Defresχ χλ/µ
IndSSmn
(
(χ
S
S
oS
n
n
m n
for any skew-partition λ/µ with |λ/µ| = mn. Comparing with Equation (12)
shows that if λ/µ is such a skew-partition then
X
β
(13)
DefresχSn χλ/µ =
hsλ/µ , sν ◦ sβ iχν
ν

where the sum is over all partitions ν of n.
P
Let pl = i xli be the power-sum symmetric function, and write pγ =
pγ1 · · · pγd for any composition γ = (γ1 , . . . , γd ). If γ is a composition of n,


CHARACTER DEFLATIONS

31

then χν (gγ ) = hpγ , sν i (see [12, Equation (I.7.8)]). Using Equation (13), we
obtain
X
β
hsλ/µ , sν ◦ sβ iχν (gγ )
(DefresχSn χλ/µ )(gγ ) =
ν

(14)
=

X

hsλ/µ , sν ◦ sβ ihsν , pγ i = hsλ/µ , pγ ◦ sβ i

ν

where the sums are over all partitions of n.
In the case when β = (m), we have sβ = hm , where hm is the complete
symmetric function of degree m (see [12, Section I.2]). Thus Equation (14)
shows that Theorem 1.5 is equivalent to the identity
(15)

hsλ/µ , pγ ◦ hm i = aλ/µ,γ .

In [3, Section 9], Désarménien, Leclerc, and Thibon obtain a formula
which implies that
X
(16)
sµ (pn ◦ hm ) =
εn (λ/µ)aλ/µ,(n) ,
λ

where the sum is over the partitions λ of |µ| + mn such that λ ⊇ µ. (Our
definition of an m-border-strip tableau of type (n) is equivalent to the definition of a horizontal n-ribbon tableau of weight m in [3].) In fact, the formula
in [3] is more general, giving a combinatorial description of sµ (pn ◦ sκ ) for
any partition κ of n. Clearly, Equation (16) is equivalent to Equation (15)
in the case γ = (n); this leads, after some work, to an alternative proof of
Theorem 1.5.
Furthermore, in the special case when µ = ∅, a combinatorial description
of the left-hand side of Equation (15) is given by Macdonald in [12, §I.8,
Example 8]. Using Lemma 4.2, one can see that this description is equivalent
to the definition of aλ,γ .
Acknowledgements
The authors would like to thank Prof. Christine Bessenrodt for supplying
the reference to Farahat’s paper [5].
References
[1] Brion, M. Stable properties of plethysm: on two conjectures of Foulkes. Manuscripta
Math., 80 (1993) 347–371.
[2] Dent, S., and Siemons, J. On a conjecture of Foulkes. J. Algebra, 226(1):236–249,
2000.
[3] Désarménien, J., Leclerc, B., and Thibon, J. Y. Hall-Littlewood functions and
Kostka-Foulkes polynomials in representation theory. Sém. Lothar. de Combin., 32
(1994), Art. B32c, approx. 38 pp.
[4] Dixon, J. D., and Mortimer, B. Permutation Groups, vol. 163 of Graduate Texts
in Mathematics. Springer, 1996.


32

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

[5] Farahat, H. K. On the representations of the symmetric group. Proc. London Math.
Soc. (3) 4 (1954), 303–316.
[6] Giannelli, E. On the decomposition of the Foulkes module. Archiv der Mathematik
100 (2013) 201–214.
[7] Isaacs, I. M. Character theory of finite groups. Dover Publications Inc., New York,
1994. Corrected reprint of the 1976 original (Academic Press, New York).
[8] James, G., and Kerber, A. The representation theory of the symmetric group, vol. 16
of Encyclopedia of Mathematics and its Applications. Addison-Wesley Publishing Co.,
Reading, Mass., 1981.
[9] Kerber, A., Kohnert, A., and Lascoux, A. SYMMETRICA, an object oriented
computer-algebra system for the symmetric group Journal of Symbolic Computation
14 (1992) 195–203.
[10] Kerber, A., Sänger, F., and Wagner, B. Quotienten und Kerne von YoungDiagrammen, Brettspiele und Plethysmen gewhnlicher irreduzibler Darstellungen symmetrischer Gruppen. Mitt. Math. Sem. Giessen 149 (1981), 131–175.
[11] Littlewood, D. E. Modular representations of symmetric groups. Proc. Roy. Soc.
London. Ser. A, 209 (1951), 333–353.
[12] Macdonald, I. G. Symmetric functions and Hall polynomials, 2nd ed. Oxford University Press, Oxford, 1995.
[13] McKay, T. On plethysm conjectures of Stanley and Foulkes. J. Algebra, 319 (2011),
2050–2071.
[14] Müller, J., and Neunhöffer, M. Some computations regarding Foulkes’ conjecture. Experiment. Math., 14(3):277–283, 2005.
[15] Olsson, J. B. Combinatorics and representations of finite groups, vol. 20. Vorlesungen aus dem FB Mathematik der Univ. Essen, 1993. Available from http:
//www.math.ku.dk/~olsson/manus/comb_rep_all.pdf.
[16] Paget, R., and Wildon, M. Set families and Foulkes modules. J. Alg. Combinat.,
34 (2011), 525–544.
[17] Peyton-Jones, S. et al , The Haskell 98 Language and Libraries: The Revised Report. J. J. Funct. Programming, 13 (2003), 0–255.
[18] Robinson, G. de B. On the representations of the symmetric group. III. Amer. J.
Math. 70 (1948), 277–294.
[19] Stanley, R. P. Enumerative combinatorics. Vol. 2, vol. 62 of Cambridge Studies in
Advanced Mathematics. Cambridge University Press, Cambridge, 1999. With a foreword by Gian-Carlo Rota and appendix 1 by Sergey Fomin.
[20] Stanley, R. P. Positivity problems and conjectures in algebraic combinatorics. In
Mathematics: frontiers and perspectives. Amer. Math. Soc., Providence, RI, 2000,
pp. 295–319.
[21] Thrall, R. M., and Robinson, G. de B. Supplement to a paper of G. de B.
Robinson. Amer. J. Math. 73 (1951), 721–724.
[22] Zelevinsky, A. V. A generalization of the Littlewood–Richardson rule and the
Robinson–Schensted–Knuth correspondence. J. Algebra 69 (1981), 82–94.

Anton Evseev, School of Mathematics, University of Birmingham, Edgbaston, Birmingham B15 2TT, UK,
E-mail address: a.evseev@bham.ac.uk


CHARACTER DEFLATIONS

33

Rowena Paget, School of Mathematics, Statistics & Actuarial Science,
University of Kent, Canterbury, Kent CT2 7NF, UK,
E-mail address: r.e.paget@kent.ac.uk
Mark Wildon, Mathematics Department, Royal Holloway, University of
London, Egham TW20 0EX, UK,
E-mail address: mark.wildon@rhul.ac.uk
