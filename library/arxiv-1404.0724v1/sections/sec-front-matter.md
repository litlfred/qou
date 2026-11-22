---
doc_id: arxiv-1404.0724v1
doc_title: "Introduction to representations of braid groups"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-2
source_pdf: 1404.0724v1.pdf
source_sha256: ea40edaad77c1617
toc_source: outline
doc_brief: "Introduction to representations of braid groups — These are lecture notes prepared for a minicourse given at the Cimpa Research School Algebraic and geometric aspects of representation the- ory, held"
duplicate_of: "ariasabad2015-revcolmat"
---
Introduction to representations of braid groups
Camilo Arias Abad∗
April 4, 2014
Abstract
These are lecture notes prepared for a minicourse given at the Cimpa Research School
Algebraic and geometric aspects of representation theory, held in Curitiba, Brazil in March
2013. The purpose of the course is to provide an introduction to the study of representations
of braid groups. Three general classes of representations of braid groups are considered:
homological representations via mapping class groups, monodromy representations via the
Knizhnik-Zamolodchikov connection, and solutions of the Yang-Baxter equation via braided
bialgebras. Some of the remarkable relations between these three diﬀerent constructions are
described.
Contents
Introduction
2
2
Braid groups
2
2.1
Artin’s presentation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
2.2
Conﬁguration spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2.3
Mapping class groups
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2.4
Pure braids . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
3
Homological representations
7
3.1
The Burau representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
3.2
Homological interpretation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
3.3
Braids, knots and the Alexander Conway polynomial . . . . . . . . . . . . . . . .
10
3.4
The Lawrence-Krammer-Bigelow representation . . . . . . . . . . . . . . . . . . .
13
4
The Knizhnik-Zamolodchikov connection
15
4.1
Cohomology of conﬁguration spaces and the KZ connection . . . . . . . . . . . .
16
4.2
Representations of sl2(C) and Lawrence-Krammer-Bigelow
. . . . . . . . . . . .
20
5
The Yang-Baxter equation and the Drinfeld-Kohno theorem
22
5.1
The Yang-Baxter equation and quasi-triangular bialgebras
. . . . . . . . . . . .
22
5.2
The Drinfeld-Kohno theorem
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
∗Max Planck Institut f¨ur Mathematik, Vivatgasse 7, Bonn, camiloariasabad@gmail.com. Supported by SNF
Grant 200020-131813/1 and a Humboldt fellowship.
1
arXiv:1404.0724v1  [math.AT]  2 Apr 2014
Acknowledgements. I would like to thank Florian Sch¨atz and David Martinez Torres for their
comments on an earlier version, and Bernardo Uribe, for his help with some of the references.
I would also like to thank the organizers of the Cimpa School for the invitation to teach this
