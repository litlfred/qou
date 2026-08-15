---
doc_id: arxiv-hep-th-0001202v2
doc_title: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees"
section_id: sec-015-6-prospects
section_title: "Prospects"
section_number: 6
pages: 17-19
source_pdf: 0001202v2.pdf
source_sha256: b2e3e22ea3d51c0b
doc_brief: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees — The renormalization of quantum ﬁeld theory twists the antipode of a non- cocommutative Hopf algebra"
---
In this paper, we were content to study the bigrading of the Hopf a lgebra of undecorated [4,
8] rooted trees, by the number of nodes and a degree of primitivity analyzed by iterations
of the coproduct. The extension of this bigrading to the decorate d [3, 7] case is the
obvious next step, in our plan to decode the rich structure of matu re quantum ﬁeld
theory. The present work makes it clear that the key feature will b e the nontriviality
of C := B+ ◦ B− ⁄= B− ◦ B+ = id. In the undecorated case, we have shown that
the biﬁltration of the Hopf algebra is obtained by adjoining the single- node tree to the
biﬁltration of the kernel of C. The proof of this lies in the powerful generalization (67) of
the concept of natural growth, which diagonalizes (69). First res ults for the commutator
[B+, B−] = C −id of the decorated Hopf algebra of full quantum ﬁeld theory were r ecently
given in [9]. These increase our hopes that it will not take another 50 y ears to complete
the characterization of the intricate interrelation of combinatoric s and analysis that makes
16
quantum ﬁeld theory possible. We ﬁrmly believe that further elucidat ion of its structure
has much to oﬀer for wide areas of both physics and mathematics.
Acknowledgements: This study began during the workshop Number Theory and
Physics at the ESI in November 1999, where we enjoyed discussions with Pier re Cartier,
Werner Nahm, Ivan Todorov and Jean-Bernard Zuber. Work with A lain Connes at the
IHES supports the present paper. System management by Chris W igglesworth enabled
accumulation of crucial data, which Neil Sloane’s superseeker helped us to decode.
Appendix: asymptotic enumerations
Here we consider inequalities inferred from Tables 3 and 4 and show th at they persist at
large weights, thanks to the upper bound c < 3 on the Otter constant [17].
Asymptotically, the number of rooted trees is given by
rn = cnn−3/ 2(b + O(1/n)) (74)
with Otter constants that we evaluated in [4]:
b = 0.43992401257102530404090339143454476479808540794 011
98576534935450226354004204764605379862197779782334...
c = 2.95576528565199497471481752412319458837549230466 359
65953504724789059647331395749510866682836765813525...
The asymptotic fraction of trees assigned to primitivity k in the ﬁltration of Table 4 is
fk := limn→∞
Pn,k
rn
=
(
1 − 1
c
) k−1 1
c (75)
while the asymptotic fraction of forests in Table 3 is
gk := limn→∞
Hn,k
rn+1
= kfk
c =
(
1 − 1
c
) k−1 k
c2 . (76)
These follow by using [4] |1 − R(x)|2 = O(1 − cx), near x = 1/c. Numerically,
g1 = 0 .1144616788557279695 . . .
g2 = 0 .1514735822429146084 . . .
g3 = 0 .1503401379409753267 . . .
g4 = 0 .1326357110750687024 . . .
g5 = 0 .1097026887662558145 . . .
g6 = 0 .0871054456752243543 . . .
g7 = 0 .0672417311397409555 . . .
g8 = 0 .0508484386279160206 . . .
g9 = 0 .0378509630072558308 . . .
17
with k = 2 giving the largest fraction of forests at large n. This was not apparent until
n = 28, where we found that H28, 2 = 20 716 895 918 exceeds H28, 3 = 20 710 700 277.
The asymptotic results establish inequalities (53,54) at large n, where it is suﬃcient
that c < 3. Amusingly, this upper bound and the condition R(1/c) = 1 produce a rather
tight lower bound
c = exp

∑
k>0
R(c−k)
k

 > exp

1 +
∑
k>1
1
(3k − 1)k

 > 2.943 (77)
from the rather loose lower bound R(x) ≥ Rladder(x) = x/(1 − x).
