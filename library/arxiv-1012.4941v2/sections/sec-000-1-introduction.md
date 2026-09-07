---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linea r and integer programming problems."
---
It is a known fact that many standard (integer) linear programming formulations of relevant
problems in optimization show a lot of symmetry. In this situation a sta ndard branch-and-
cut framework repeatedly enumerates symmetric solutions, and s ometimes this renders such
methods useless. To address these issues the last decade saw a nu mber of approaches to
devise algorithms specialized to symmetric optimization problems. We m ention a few: Mar-
got suggests to solve symmetric integer linear programs (ILPs) via a pruned branch-and-cut
approach involving techniques from computational group theory [ 14, 15]. A recent improve-
ment in this direction is “orbital branching” devised by Ostrowski et al. [17]. Friedman [5] as
well as Kaibel and Pfetsch [8] treat symmetric ILPs by shrinking the domain of feasibility
by cutting oﬀ symmetric solutions. Gatermann and Parrilo apply resu lts from represen-
tation theory and invariant theory to semideﬁnite programming [6], which includes linear
programming as a special case. Our approach is close in spirit to this p aper. See also the
survey of Margot [13] for a general overview of symmetric integer linear programming.
This is how our paper is organized: ﬁrst we analyze linear programs wit h an arbitrary
ﬁnite group of linear automorphisms. Most results in this section are known. A ﬁrst key
observation, Theorem 15, is that symmetric linear programming can be reduced to linear
programming over the ﬁxed space of the automorphism group. Sec tions 3 and 4 translate
these results to the context of integer linear programming. In the sequel we concentrate
on groups acting as signed permutations on the standard basis of Rn. Section 5 contains
our main contribution: our Core Point Algorithm B can solve an integer linear program in
Rn whose group of linear automorphisms contains the alternating grou p of degree n (acting
as signed permutations) in O(mn2) time, where m is the number of constraints. This is
in sharp contrast with the known NP-completeness of the general integer linear program-
ming feasibility problem. While our algorithm only works for ILPs with an e xceptionally
high degree of symmetry we believe that this is a ﬁrst step towards a n entire new class
Date: September 11, 2018.
Research by Herr is supported by Studienstiftung des deutsc hen Volkes. Research by Joswig is partially
supported by DFG Research Unit 565 “Polyhedral Surfaces” an d DFG Priority Program 1489 “Experimental
Methods in Algebra, Geometry, and Number Theory”.
1
2 RICHARD B ¨ODI, KATRIN HERR, AND MICHAEL JOSWIG
of algorithms dealing with symmetry in ILPs. Suitable generalizations a re the subject to
ongoing research. In Section 6 we discuss algorithms to determine g roups of automorphisms
of integer linear programs. This leads to algorithmic problems which tu rn out to be graph-
isomorphism-complete. The ﬁnal Section 8 contains experimental r esults. One of the ILP
classes that we investigated computationally is motivated by work of Pokutta and Stauﬀer
on lower bounds for Gomory-Chv´ atal ranks [19]. Section 7 explains the construction.
We are indebted to Tobias Achterberg, Leo Liberti, Marc Pfetsch, Sebastian Pokutta,
and Achill Sch¨ urmann for valuable discussions on the subject of th is paper.
