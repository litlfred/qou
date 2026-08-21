---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-001-02-acknowledgements
section_title: "Acknowledgements"
section_number: 0.2
pages: 3-8
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? — 57 sections: Abstract; Acknowledgements; Introduction"
---
This research was supported by NSERC, the University of Waterloo, the Templeton Foun-
dation, and by the Perimeter Institute for Theoretical Physics. Research at Perimeter
Institute is supported by the Government of Canada through Industry Canada and by the
Province of Ontario through the Ministry of Research and Innovation.
A special thanks to my committee members: L. Boyle, F. Cachazo, F. Girelli, A. Kempf,
R. Mann, and P. Ramond. I am especially grateful to L. Boyle, A. Kempf, and R. Mann
for giving me a hand when I needed one, and feel very fortunate to have had A. Kempf as
a supervisor during these ﬁnal stages of my degree. He has been an outstanding mentor.
My time in Waterloo has been both wonderful and trying, and I will be forever indebted
to those who were there with me through the days that were diﬃcult. Alex, Carey, Calida,
Deb, Steve, Luke, Sheri, Hilary, Gaetano, George, Vito, Steph, Josh, and of course, Mike,
Dianna, Shona, and Kelly: please know how much I value your friendship.
iii
And I want to know the same thing. We all want to know, how’s it going to end?
- Brennan and Waits
iv
Table of Contents
0.1 Abstract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ii
0.2 Acknowledgements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . iii
1 Introduction 1
1.1 Towards conceptual parsimony . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2 What lies in an algebra? 3
2.1 Causality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.2 Irreversible time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.3 Particles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.4 Summary and outlook . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3 Complex quaternions 8
3.1 Preamble . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.2 Introduction to C⊗ H . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.3 Conjugation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.4 Generalized ideals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.5 Complex invariant-action, mc . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.5.1 Preliminaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.5.2 Weyl and Dirac spinors as generalized ideals . . . . . . . . . . . . . 12
v
3.5.3 A seamless new way to conjugate Weyl spinors . . . . . . . . . . . 13
3.5.4 Majorana spinors as generalized ideals . . . . . . . . . . . . . . . . 14
3.6 Hermitian invariant-action, mh . . . . . . . . . . . . . . . . . . . . . . . . 15
3.7 Quaternionic invariant-action, mq . . . . . . . . . . . . . . . . . . . . . . . 16
3.8 Bilinears . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.9 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.10 Outlook . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
4 Cliﬀord algebras 19
4.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
4.2 Deﬁnition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
4.3 Examples of Cliﬀord algebras from C⊗ H . . . . . . . . . . . . . . . . . . 21
4.4 Minimal left ideals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
4.5 How to identify minimal left ideals . . . . . . . . . . . . . . . . . . . . . . 23
4.5.1 Some deﬁnitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4.5.2 Procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
4.6 Minimal left ideals in C⊗ H . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.6.1 Fock space structure . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.7 The Dirac algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.8 Right action required . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.9 Parity and the ﬁeld strength tensor . . . . . . . . . . . . . . . . . . . . . . 28
5 Standard model of particle physics 32
5.1 What it is . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
5.2 What it is not . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5.3 What it should be . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
vi
6 One generation of quarks and leptons from C⊗ O 37
6.1 A summary of the results to come . . . . . . . . . . . . . . . . . . . . . . 38
6.2 Introduction to C⊗ O . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
6.3 Octonionic chain algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
6.4 A system of ladder operators . . . . . . . . . . . . . . . . . . . . . . . . . 45
6.5 Complex conjugation’s analogue . . . . . . . . . . . . . . . . . . . . . . . 46
6.6 Minimal left ideals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
6.7 MTIS symmetries: su(3)c and u(1)em . . . . . . . . . . . . . . . . . . . . . 49
6.8 Ladders to su(3)c and u(1)em . . . . . . . . . . . . . . . . . . . . . . . . . 50
6.9 Towards the weak force . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
6.10 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
7 Why does SU (2)L act on only left-handed fermions? 55
7.1 A spotlight on right multiplication . . . . . . . . . . . . . . . . . . . . . . 55
7.2 Leptonic subspace of Cl(4) . . . . . . . . . . . . . . . . . . . . . . . . . . 56
7.3 MTIS symmetries: su(2)L and u(1)Y . . . . . . . . . . . . . . . . . . . . . 57
7.4 Summary and outlook . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
8 Group representation structure of some grand uniﬁed theories 59
8.1 SU (5) uniﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
8.1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
8.1.2 GSM inside SU (5) . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
8.1.3 Some notes on symmetry breaking . . . . . . . . . . . . . . . . . . 62
8.2 A fermionic binary code . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
8.3 Spin(10) uniﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
8.4 Pati-Salam model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
vii
9 Towards a three-generation model 71
