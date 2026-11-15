---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-9
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
INAUGURAL-DISSERTATION
zur
Erlangung der Doktorw¨urde
an der
Naturwissenschaftlich-Mathematischen Gesamtfakult¨at
der Ruprecht-Karls-Universit¨at Heidelberg
TANNAKIAN CATEGORIES OF PERVERSE SHEAVES
ON ABELIAN VARIETIES
vorgelegt von
Dipl.-Math. Thomas Kr¨amer
aus Frankenberg (Eder)
Tag der m¨undlichen Pr¨ufung:
Betreuer: Prof. Dr. Rainer Weissauer
Zusammenfassung. Die vorliegende Dissertation besch¨aftigt sich mit
Tannaka-Kategorien, welche durch Faltung perverser Garben auf abelschen
Variet¨aten entstehen. Die Konstruktion dieser Kategorien ist eng verbunden
mit einem kohomologischen Verschwindungssatz, der ein Analogon zum
Satz von Artin-Grothendieck darstellt und als Spezialfall die generischen
Verschwindungss¨atze von Green und Lazarsfeld enth¨alt. Die erhaltenen
Tannaka-Gruppen bilden interessante geometrische Invarianten, welche in
vielen Situationen eine Rolle spielen — nachdem die Grundlagen f¨ur das
Studium dieser Gruppen bereitgestellt sind, wird als ein wichtiges Beispiel
der Thetadivisor einer prinzipal polarisierten komplexen abelschen Variet¨at
behandelt. Durch Entartungsargumente wird die Tannaka-Gruppe f¨ur eine
generische abelsche Variet¨at bestimmt, welche wenigstens in Dimension 4
eine neue Antwort auf das Schottky-Problem liefert. Das Faltungsquadrat
des Thetadivisors in Dimension 4 h¨angt eng zusammen mit einer Familie
glatter Fl¨achen vom allgemeinen Typ, und ein Studium dieser Familie f¨uhrt
auf eine Variation von Hodge-Strukturen mit Monodromiegruppe W(E6),
die mit der Prym-Abbildung verbunden ist. Die Dissertation schließt ab mit
einer Rekursionsformel f¨ur den generischen Rang der durch Faltungen von
Kurven entstehenden Brill-Noether-Garben auf Jacobischen Variet¨aten.
Abstract. We study Tannakian categories that arise from convolutions of
perverse sheaves on abelian varieties. The construction of these categories
is closely intertwined with a cohomological vanishing theorem which is an
analog of the Artin-Grothendieck theorem and contains as a special case the
generic vanishing theorems of Green and Lazarsfeld. The arising Tannaka
groups form a powerful new tool applicable in many different geometric
contexts — after providing the framework for the study of these groups, we
consider as an important example the theta divisor of a complex principally
polarized abelian variety. Using degeneration techniques we determine the
associated Tannaka group for a generic abelian variety, and we show that in
dimension 4 this yields a Tannakian solution to the Schottky problem. The
convolution square of the theta divisor in dimension 4 is closely related to a
family of surfaces of general type, and a detailed study of this family leads
to a variation of Hodge structures with monodromy group W(E6) which is
connected with the Prym map. To conclude the dissertation, we provide a
recursive formula for the generic rank of Brill-Noether sheaves which arise
from the convolution of curves on Jacobian varieties.
Acknowledgements
It is a pleasure for me to thank my advisor, Professor R. Weissauer, for
sharing his beautiful ideas in many productive mathematical discussions,
for his general open-mindedness in all occuring questions, for his careful
reading of the manuscript and for various helpful suggestions concerning
the exposition. I am also grateful to my roommates Johannes Schmidt,
Thorsten Heidersdorf and Uwe Weselmann and to the other members of the
Mathematical Institute at Heidelberg for the pleasant environment which
they created during the past years. Furthermore I would like to thank several
people outside Heidelberg who enlivened the atmosphere on conferences
and expressed their interest in my work, among them Anders Lundman,
Bashar Dudin, Christian Schnell, Dan Petersen, Dmitry Zakharov, Giovanni
Mongardi, Katharina Heinrich, Nicola Tarasca and Paul Hacking. I am also
indebted to the Studienstiftung des deutschen Volkes and to all members
of its staff for their ﬂexibility and for the ﬁnancial and ideal support from
which I proﬁted a lot. Finally, my most special thanks go to my family and
friends for their encouragement and patience during my work, but perhaps
even more for the multifarious, pleasant and interesting distractions from it
without which I would not have been able to think freely.
Contents
Introduction
1
Some commonly used notations
7
Chapter 1.
Vanishing theorems on abelian varieties
9
1.1.
The main result
9
1.2.
A relative generic vanishing theorem
11
1.3.
Kodaira-Nakano-type vanishing theorems
12
1.4.
Negligible perverse sheaves
15
1.5.
The spectrum of a perverse sheaf
17
Chapter 2.
Proof of the vanishing theorem(s)
23
2.1.
The setting
23
2.2.
Character twists and convolution
26
2.3.
An axiomatic framework
30
2.4.
The Andr´e-Kahn quotient
32
2.5.
Super Tannakian categories
35
2.6.
Perverse multiplier
36
2.7.
The main argument
38
Chapter 3.
Perverse sheaves on semiabelian varieties
41
3.1.
Vanishing theorems revisited
42
3.2.
Some properties of convolution
46
3.3.
The thick subcategory of negligible objects
47
3.4.
Tannakian categories
51
3.5.
Nearby cycles
54
3.6.
Specialization of characters
58
3.7.
Variation of Tannaka groups in families
61
Chapter 4.
The Tannaka group of the theta divisor
69
4.1.
The Schottky problem in genus 4
71
4.2.
Nondegenerate bilinear forms
73
4.3.
Local monodromy
74
4.4.
Degenerations of abelian varieties
79
4.5.
Proof of the main theorem
85
4.6.
Singularities of type Ak
88
v
vi
Contents
Chapter 5.
A family of surfaces with monodromy W(E6)
93
5.1.
Intersections of theta divisors
95
5.2.
Variations of Hodge structures
102
5.3.
Integral cohomology
106
5.4.
N´eron-Severi lattices
109
5.5.
The upper bound W(E6)
115
5.6.
Negligible constituents
119
5.7.
Jacobian varieties
123
5.8.
The difference morphism
127
5.9.
A smooth global family
131
Chapter 6.
The generic rank of Brill-Noether sheaves
135
6.1.
Brill-Noether sheaves
135
6.2.
A formula for the generic rank
137
6.3.
Computations in the symmetric product
139
6.4.
The ﬁbres of multiple Abel-Jacobi maps
142
6.5.
Betti polynomials
144
6.6.
Some numerical values
146
Appendix A.
Reductive super groups
151
Appendix B.
Irreducible subgroups with bounded determinant
157
Appendix C.
An irreducible subgroup of W(E6)
163
Appendix D.
Doubly transitive permutation groups
165
Bibliography
169
