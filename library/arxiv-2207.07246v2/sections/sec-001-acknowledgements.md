---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-001-acknowledgements
section_title: "ACKNOWLEDGEMENTS"
section_number: null
pages: 4-8
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
I am grateful to my advisor prof. Kevin E. Schmidt not only for his transcendental
tolerance, extraordinary patience, sagacious guidance, but also for his kindly accepting
me at the stage I was at and assigning me an awesome PhD project which enlightened
my life. From him I learned not only delicate and creative physics ideas, but more
importantly, the hardcore independent American spirit. To me he is the high seas
Caesar who always tries to train me to be like captain Jack Sparrow who adventures
on the seven seas under any whimsical conditions with the Black Pearl. It was destiny
that lead me overseas from Shanghai to Tempe, and eventually brought me the honor
to work with prof. Schmidt doing nuclear physics in an ab initio way using state of
the art quantum Monte Carlo methods. I thank the United States and prof. Ralph V.
Chamberlin for bringing me the Bifr¨ost. I thank prof. Francesco Pederiva, too.
I am honored to have profs. Alarc´on, Beckstein, Comfort and Shovkovy as my
PhD committee. I also thank profs. Quan Qin, Kong-Thon Tsen, Peter Rez, Cecilia
Lunardini, Tanmay Vachaspati, Maulik Parikh, and Damien A. Easson. I thank Drs.
Darya Dolenko and Iwonna Rzanek for teaching assistant instructions. I thank Lucas
Madeira, Cody L. Petrie, and Jie Zhang for discussions. I thank Zhi-Yu Huang, too.
I am indebted to my MS degree advisor prof. Lie-Wen Chen for laying me a crucial
foundation and beyond. I thank prof. Bao-An Li for collaborations and help. I thank
prof. Dean Lee for beneﬁcial suggestions and kindness. I thank Bao-Jun Cai, Jing-Jing
Yang, Yi-Hua Huang, Bo-Wen Lian, Jie Gu and Jia-Xin Li for long friendship.
Ultimately, I thank my parents for their unmatched love and unconditional support
all those years. These are truly in extra dimensions beyond the Standard Model.
This work was supported by the National Science Foundation Grant No. PHY-
1404405. The High-Performance Computing and storage resources were provided by
Research Computing at Arizona State University.
iii
TABLE OF CONTENTS
Page
LIST OF TABLES . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . vii
LIST OF FIGURES. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . viii
CHAPTER
1
INTRODUCTION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
1.1
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
1.1.1
Evolution of the Nucleon-Nucleon Interaction . . . . . . . . . . . . . .
1
1.1.2
Methods of Solving the Many-Body Problem . . . . . . . . . . . . . . .
5
1.2
Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
1.3
Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2
PATH INTEGRAL QUANTUM MONTE CARLO. . . . . . . . . . . . . . . . . . . . . 14
2.1
Theoretical Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.2
Hamiltonian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.3
Model Space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.4
Wave Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
2.5
Propagator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
2.6
Time Step Error Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
2.7
Computational Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
2.7.1
Recast . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
2.7.2
Path Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
2.7.3
Calculating the Path . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
2.7.4
Calculating the Samples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
47
2.8
Sign Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
3
MONTE CARLO ALGORITHMS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
51
3.1
Metropolis Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
51
iv
CHAPTER
Page
3.2
Methods of Sampling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
3.2.1
Single-Bead Sampling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
3.2.2
Multi-level Sampling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
3.2.3
Regular Sampling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
67
3.2.4
Directional Importance Sampling . . . . . . . . . . . . . . . . . . . . . . . . . 70
3.3
Path Updating Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
77
3.4
Sampling Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
4
GROUND STATE CALCULATIONS OF LIGHT NUCLEI . . . . . . . . . . . . . 80
4.1
Ground State Energies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
4.1.1
Preparations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
4.1.2
Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
81
4.1.3
Veriﬁcations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
4.2
Radii . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
4.3
Density Distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
4.4
Euclidean Response Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
4.5
Parallel Scalability of the Code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
5
CONCLUSION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
5.1
Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
5.2
Outlook . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
REFERENCES . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
APPENDIX
A VARIATIONAL MONTE CARLO BRIEF . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
B DIFFUSION MONTE CARLO BRIEF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
B.1
Time-Dependent Green’s Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
v
CHAPTER
Page
B.2 Diﬀusion Monte Carlo. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
B.3
Diﬀusion Monte Carlo with Importance Sampling . . . . . . . . . . . . . . . . 127
B.4
Diﬀusion Monte Carlo Algorithm. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
C AUXILIARY FIELD DIFFUSION MONTE CARLO BRIEF . . . . . . . . . . . 133
C.1 Formalism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
C.2 Hubbard-Stratonovich Transformation. . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
C.3 AFDMC and the Standard DMC with Importance Sampling . . . . . . . 137
C.4 Quadratic Form of the AV6’ Interaction . . . . . . . . . . . . . . . . . . . . . . . . . . 138
C.5 Trial Wave Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
D AV6’ LINEARIZING TRICK. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
E
ADDITIONAL CALCULATIONS OF THE RESPONSE FUNCTIONS . 143
E.1
Angle Averaged Euclidean Response Functions. . . . . . . . . . . . . . . . . . . . 144
E.2
Euclidean Response Functions in Diﬀerent Coordinates . . . . . . . . . . . . 153
BIOGRAPHICAL SKETCH . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
vi
