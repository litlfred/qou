---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-000-preface
section_title: "Preface"
section_number: null
pages: 1-5
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
toc_source: inferred
---
The workshop and seminars on “Invariants of knots and 3-manifolds” was held at
Research Institute for Mathematical Sciences, Kyoto University in September 2001.
There were 25 talks in the workshop in September 17–21, and there were 27 talks in the
seminars in the other weeks of September. Each speaker was requested to give his/her
open problems in a short problem session after his/her talk, and many interesting open
problems were given and discussed by the speakers and participants in the workshop
and the seminars. Contributors of the open problems were also requested to give kind
expositions of history, background, signiﬁcance, and/or importance of the problems.
This problem list was made by editing these open problems and such expositions.1
Since the interaction between geometry and mathematical physics in the 1980s, many
invariants of knots and 3-manifolds have been discovered and studied. The discovery
and analysis of the enormous number of these invariants yielded a new area: the
study of invariants of knots and 3-manifolds (from another viewpoint, the study of the
sets of knots and 3-manifolds). Recent works have almost completed the topological
reconstruction of the invariants derived from the Chern-Simons ﬁeld theory, which was
one of main problems of this area.
Further, relations among these invariants have
been studied enough well, and these invariants are now well-organized. For the future
developments of this area, it might be important to consider various streams of new
directions;2 this is a reason why the editor tried to make the problem list expository.
The editor hopes this problem list will clarify the present frontier of this area and assist
readers when considering future directions.
The editor will try to keep up-to-date information on this problem list at his web site.3
If the reader knows a (partial) solution of any problem in this list, please let him4 know
it.
February, 2003
T. Ohtsuki
The logo for the workshop and the seminars was designed by N. Okuda.
1Open problems on the Rozansky-Witten invariant were written in a separate manuscript
[349]. Some fundamental problems are quoted from other problem lists such as [188], [220],
[262], [285], [286], [388, Pages 571–572].
2For example, directions related to other areas such as hyperbolic geometry via the volume
conjecture and the theory of operator algebras via invariants arising from 6j-symbols.
3http://www.kurims.kyoto-u.ac.jp/~tomotada/proj01/
4Email address of the editor is: tomotada@kurims.kyoto-u.ac.jp
Geometry & Topology Monographs, Volume 4 (2002)
ii
Contents
Preface
1
0
Introduction
377
1
Polynomial invariants of knots
380
1.1
The Jones polynomial
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 380
1.1.1
Does the Jones polynomial distinguish the trivial knot?
. . . . . 381
1.1.2
Characterization and interpretation of the Jones polynomial . . . 382
1.1.3
Numerical experiments . . . . . . . . . . . . . . . . . . . . . . . . 386
1.1.4
Categoriﬁcation of the Jones polynomial . . . . . . . . . . . . . . 388
1.2
The HOMFLY, Q, and Kauﬀman polynomials . . . . . . . . . . . . . . . 390
1.3
The volume conjecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . 393
2
Finite type invariants of knots
398
2.1
Torsion and Vassiliev invariants . . . . . . . . . . . . . . . . . . . . . . . 399
2.2
Do Vassiliev invariants distinguish knots?
. . . . . . . . . . . . . . . . . 401
2.3
Can Vassiliev invariants detect other invariants?
. . . . . . . . . . . . . 402
2.4
Vassiliev invariants and crossing numbers
. . . . . . . . . . . . . . . . . 403
2.5
Dimensions of spaces of Vassiliev invariants . . . . . . . . . . . . . . . . 405
2.6
Milnor invariants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 408
2.7
Finite type invariants of virtual knots
. . . . . . . . . . . . . . . . . . . 409
2.8
Finite type invariants derived from local moves . . . . . . . . . . . . . . 412
2.9
Loop ﬁnite type invariants . . . . . . . . . . . . . . . . . . . . . . . . . . 415
2.10 Goussarov-Habiro theory for knots . . . . . . . . . . . . . . . . . . . . . 418
2.11 Other problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 422
3
The Kontsevich invariant
424
3.1
Calculation of the Kontsevich invariant
. . . . . . . . . . . . . . . . . . 424
3.2
Does the Kontsevich invariant distinguish knots? . . . . . . . . . . . . . 425
3.3
Characterization and interpretation of the Kontsevich invariant . . . . . 425
3.4
The Kontsevich invariant in a ﬁnite ﬁeld . . . . . . . . . . . . . . . . . . 426
3.5
The Kontsevich invariant in arrow diagrams . . . . . . . . . . . . . . . . 427
3.6
The Chern-Simons series of conﬁguration space integrals . . . . . . . . . 429
3.7
Associators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 432
3.8
Graph cohomology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 435
3.9
The loop expansion of the Kontsevich invariant . . . . . . . . . . . . . . 437
3.10 The Kontsevich invariant of links in Σ × [0, 1] . . . . . . . . . . . . . . . 443
Geometry & Topology Monographs, Volume 4 (2002)
iii
4
Skein modules
445
4.1
The Kauﬀman bracket skein module . . . . . . . . . . . . . . . . . . . . 446
4.2
The Homﬂypt skein module . . . . . . . . . . . . . . . . . . . . . . . . . 447
4.3
The Kauﬀman skein module . . . . . . . . . . . . . . . . . . . . . . . . . 448
4.4
The q-homotopy skein module
. . . . . . . . . . . . . . . . . . . . . . . 449
4.5
The (4, ∞) skein module . . . . . . . . . . . . . . . . . . . . . . . . . . . 450
4.6
Other problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 453
5
Quandles
455
5.1
Classiﬁcation of quandles
. . . . . . . . . . . . . . . . . . . . . . . . . . 455
5.2
Representations of knot quandles . . . . . . . . . . . . . . . . . . . . . . 458
5.3
(Co)homology of quandles . . . . . . . . . . . . . . . . . . . . . . . . . . 459
5.4
Quandle cocycle invariant . . . . . . . . . . . . . . . . . . . . . . . . . . 461
5.5
Quantum quandles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 464
5.6
Rack (co)homology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 464
6
Braid group representations
466
6.1
The Temperley-Lieb algebra . . . . . . . . . . . . . . . . . . . . . . . . . 466
6.2
The Burau representation . . . . . . . . . . . . . . . . . . . . . . . . . . 467
6.3
The Hecke and BMW algebras
. . . . . . . . . . . . . . . . . . . . . . . 468
6.4
Other problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 469
7
Quantum and perturbative invariants of 3-manifolds
471
7.1
Witten-Reshetikhin-Turaev invariants and quantum invariants
. . . . . 471
7.2
The asymptotic expansion conjecture . . . . . . . . . . . . . . . . . . . . 474
7.3
The volume conjecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . 481
7.4
Quantum hyperbolic invariants of 3-manifolds . . . . . . . . . . . . . . . 485
7.5
Perturbative invariants . . . . . . . . . . . . . . . . . . . . . . . . . . . . 488
8
Topological quantum ﬁeld theory
493
8.1
Classiﬁcation and characterization of TQFT’s . . . . . . . . . . . . . . . 494
8.2
Spin TQFT’s . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 495
8.3
Homotopy QFT’s . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 496
8.4
Geometric construction of TQFT’s . . . . . . . . . . . . . . . . . . . . . 496
8.5
Half-projective and homological TQFT’s . . . . . . . . . . . . . . . . . . 498
9
The state-sum invariants of 3-manifolds derived from 6j-symbols
506
9.1
Monoidal categories, 6j-symbols, and subfactors
. . . . . . . . . . . . . 506
Geometry & Topology Monographs, Volume 4 (2002)
iv
9.2
Turaev-Viro invariants and the state-sum invariants derived from monoidal
categories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 508
9.3
The state-sum invariants derived from ribbon categories . . . . . . . . . 511
9.4
Turaev-Viro-Ocneanu invariants . . . . . . . . . . . . . . . . . . . . . . . 512
10 Casson invariant and ﬁnite type invariants of 3-manifolds
514
10.1 Casson and Rokhlin invariants
. . . . . . . . . . . . . . . . . . . . . . . 514
10.2 Finite type invariants
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 517
10.2.1 Torsion and ﬁnite type invariants . . . . . . . . . . . . . . . . . . 518
10.2.2 Do ﬁnite type invariants distinguish homology 3-spheres?
. . . . 518
10.2.3 Dimensions of spaces of ﬁnite type invariants . . . . . . . . . . . 518
10.2.4 Vogel’s algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . 520
10.2.5 Other problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . 522
10.3 Goussarov-Habiro theory . . . . . . . . . . . . . . . . . . . . . . . . . . . 523
10.3.1 Goussarov-Habiro theory for 3-manifolds . . . . . . . . . . . . . . 523
10.3.2 Goussarov-Habiro theory for spin and spinc 3-manifolds . . . . . 525
11 The LMO invariant
527
11.1 Calculation of the LMO invariant . . . . . . . . . . . . . . . . . . . . . . 527
11.2 Does the LMO invariant distinguish integral homology 3-spheres? . . . . 527
11.3 Characterization of the image of the LMO invariant
. . . . . . . . . . . 528
11.4 Variations of the LMO invariant
. . . . . . . . . . . . . . . . . . . . . . 528
11.5 Reﬁnements of the LMO invariant
. . . . . . . . . . . . . . . . . . . . . 528
11.6 Other problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 529
12 Other problems
530
12.1 (Pseudo) Legendrian knot invariants . . . . . . . . . . . . . . . . . . . . 530
12.2 Knots and ﬁnite groups
. . . . . . . . . . . . . . . . . . . . . . . . . . . 531
12.3 The numbers of 3-, 5-colorings and some local moves . . . . . . . . . . . 532
12.4 Knotted trivalent graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . 533
12.5 Quantum groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 537
12.6 Other problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 538
Bibliography
543
Index of contributors
567
Index
568
Geometry & Topology Monographs, Volume 4 (2002)
ISSN 1464-8997 (on line) 1464-8989 (printed)
377
Geometry & Topology Monographs
Volume 4: Invariants of knots and 3-manifolds (Kyoto 2001)
Pages 377–572
Problems on invariants of knots and 3-manifolds
Edited by T. Ohtsuki
Abstract
This is a list of open problems on invariants of knots and 3-
manifolds with expositions of their history, background, signiﬁcance, or
importance. This list was made by editing open problems given in prob-
lem sessions in the workshop and seminars on “Invariants of Knots and
3-Manifolds” held at Kyoto in 2001.
AMS Classiﬁcation 20F36, 57M25, 57M27, 57R56; 13B25, 17B10, 17B37,
18D10, 20C08, 20G42, 22E99, 41A60, 46L37, 57M05, 57M50, 57N10, 57Q10,
81T18, 81T45
Keywords
Invariant, knot, 3-manifold, Jones polynomial, Vassiliev in-
variant, Kontsevich invariant, skein module, quandle, braid group, quantum
invariant, perturbative invariant, topological quantum ﬁeld theory, state-
sum invariant, Casson invariant, ﬁnite type invariant, LMO invariant
0
