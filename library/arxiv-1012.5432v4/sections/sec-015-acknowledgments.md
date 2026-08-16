---
doc_id: arxiv-1012.5432v4
doc_title: ""
section_id: sec-015-acknowledgments
section_title: "Acknowledgments"
section_number: null
pages: 39-44
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
doc_brief: "quant-ph Towards Topological Quantum Computation? - — 19 sections: A Hamiltonian; Instantons; Dirac Monopoles"
---
The author would like to thank F. Wilczek for advising her thesis (the ﬂagstone for this
paper) and for subsequently suggesting she “condense a paper out of it”. In addition, she
would like to thank P. Shor for providing access to MAGMA and helping to debug part of
the MAGMA code.
[1] R. Feynman, “Simulating physics with computers,” International Journal of Theor. ,
vol. Physics 21, p. 467, 1982.
[2] P. Shor, “Polynomial-time algorithms for prime factorization and discrete logarithms on
a quantum computers,” SIAM J. Comput. , vol. 26(5):, pp. 1484–1509, 1997. preprint
arXiv:quant-ph/9508027v2.
[3] A. Steane, “Multiple-particle interference and quantum error correction,” Proceedings of the
Royal Society A .
39
[4] D. Aharonov and M. Ben-Or, “Fault-tolerant quantum computation with constant error rate,”
June 1999. preprint arXiv:quant-ph/9906129v1.
[5] A. Stern, “Anyons and the quantum hall eﬀect - a pedagogical review,” Nov. 1997. preprint
arXiv:0711.4697v1.
[6] F. Wilczek, “Quantum mechanics of fractional-spin particles,” Phys. Rev. Lett., vol. 49, p. 14,
1982. preprint arXiv:quant-ph/.
[7] J. Hoste, M. Thisthlethwaite, and J. Weeks, “The ﬁrst 1,701,936 knots,” The Mathematical
Intelligencer, vol. 20, p. 33.
[8] M. de Wild Propitius and F. A. Bais, “Discrete gauge theories,” Mar. 1996. preprint arxiv
hep-th/9511201 v2 .
[9] Y. Aharonov and D. Bohm, “Signiﬁcance of electromagnetic potentials in the quantum the-
ory,” The Physical Review , vol. 115, p. 485.
[10] A. van Oudenaarden, M. H. Devoret, Y. V. Nazarov, and J. E. Mooij, “Magnetoelectric
aharonov-bohm eﬀect in metal rings,” Nature, vol. 391, p. 768.
[11] Steven Weinberg, “The quantum theory of ﬁelds,” 1995.
[12] Sidney Coleman, “Aspects of symmetry: Selected erice lectures,” 1985.
[13] F. A. Bais, A. Morozov, and M. de Wild Propitius, “Charge screening in the higgs phase of
chern-simons electrodynamics,” Physical Review Letters , vol. 71, p. 2383.
[14] K. Druhl, R. Haag, and J. Roberts, “On parastatistics,” Commun. math. Phys. , vol. 18,
p. 204.
[15] T. Koornwinder, B. Schroers, J. Slingerland, and F. Bais, “Fourier transform and the verlinde
formula for the quantum double of a ﬁnite group,” jpa, vol. 32, p. 8539.
[16] A. Kitaev, “Fault-tolerant quantum computation by anyons,” Annals Phys. 303, 2-30 , May
2003. preprint arXiv:quant-ph/9707021v1.
[17] L. Duan, E. Demler, and M. Lukin, “Controlling spin exchange interactions of ultracold
atoms in optical lattices,” Physical Review Letters , vol. 91, p. 9, Aug. 2003. preprint
arXiv:cond-mat/0210564v2.
[18] B. Doucot, L. Ioﬀe, and J. Vidal, “Discrete non-abelian gauge theories in two-dimensional
lattices and their realizations in josephson-junction arrays,” Physical Review B , vol. 69, 2004.
[19] J. Preskill, “Chapter 9: Topological quantum computation,” online notes.
[20] R. W. Ogburn and J. Preskill, “Topological quantum computation,” in QCQC98 (C. Williams,
40
ed.), (Berlin), pp. 341–356, Springer Verlag, 1999.
[21] C. Mochon, “Anyons from nonsolvable ﬁnite groups are suﬃcient for universal quantum com-
putation,” Phys. Rev. A , vol. 67, p. 022315, 2003.
[22] M. Freedman, M. Larsen, and Z. Wang, “The two-eigenvalue problem and density of jones
representation of braid groups,” Commun. Math. Phys. 228, 177-199 , 2003.
[23] C. Mochon, “Anyon computers from smaller ﬁnite groups,” preprint
arXiv:quant-ph/0306063 v2 .
Appendix A: Appendix
function ComputeSMatrix(A, B, alpha, beta, Gp)
CC:=ConjugacyClasses(Gp);
Cent := [Centralizer(Gp,Gp!CC[i][3]) : i in [1..#CC]];
total:=0;
for j in [1..#RightTransversal(Gp,Cent[B])] do
for i in [1..#RightTransversal(Gp,Cent[A])] do
cj:= RightTransversal(Gp, Cent[B])[j];
ci:= RightTransversal(Gp, Cent[A])[i];
cj:=cj^-1;
ci:=ci^-1;
valpha := ci^-1 * cj * CC[B][3] * cj^-1 * ci;
valbeta := cj^-1 * ci * CC[A][3] * ci^-1 * cj;
if (Gp!cj * CC[B][3] * cj^-1)^-1 * (Gp! ci * CC[A][3] * ci^-1)^-1
*(Gp!cj * CC[B][3] * cj^-1) * (Gp! ci * CC[A][3] * ci^-1) eq Id(Gp)
then total:=total+ComplexConjugate((CharacterTable(Cent[A])[alpha])(valpha))*
ComplexConjugate((CharacterTable(Cent[B])[beta])(valbeta));
end if;
end for;
end for;
total:=total/#(Gp);
return(total);
end function;
41
function FusionCoefficientsviaSMatrix(A, alpha, B, beta, C, gamma, Gp)
CC:=ConjugacyClasses(Gp);
Cent := [Centralizer(Gp,Gp!CC[i][3]) : i in [1..#CC]];
fusionsum:=0;
//sum over all centralizers D and representations of those centralizers delta
for D in [1..#ConjugacyClasses(Gp)], delta in [1..#ConjugacyClasses(Cent[D])] do
//since the number of conjugacy classes = number of representations
//want delta up to # of repns of the centralizer corresponding to repn D Cent[D]
if(ComputeSMatrix(1,D,1,delta,Gp) ne 0)
then
fusionsum:=fusionsum+ComputeSMatrix(A, D, alpha, delta, Gp) *
ComputeSMatrix(B, D, beta, delta, Gp) *
ComplexConjugate(ComputeSMatrix(C, D, gamma, delta, Gp))/
ComputeSMatrix(1, D, 1, delta, Gp);
end if;
end for;
return fusionsum;
end function;
function FusionProb(A, alpha, B, beta, C, gamma, Gp)
CC:=ConjugacyClasses(Gp);
DA:=CharacterTable(Centralizer(Gp, Gp!CC[A][3]))[alpha][1];
dimA:= (CC[A][2])*DA;
DB:=CharacterTable(Centralizer(Gp, Gp!CC[B][3]))[beta][1];
dimB:= (CC[B][2])*DB;
DC:=CharacterTable(Centralizer(Gp, Gp!CC[C][3]))[gamma][1];
dimC:= (CC[C][2])*DC;
fus:=FusionCoefficientsviaSMatrix(A, alpha, B, beta, C, gamma, Gp);
prob:= ((fus) * (dimC))/(dimA *dimB);
return(prob);
end function;
42
function fusionprinter(Gp)
CC:=ConjugacyClasses(Gp);
Cent := [Centralizer(Gp,Gp!CC[i][3]) : i in [1..#CC]];
for i in [1..#ConjugacyClasses(Gp)],
i1 in [1..#ConjugacyClasses(Cent[i])] do
printf " \n";
for j in [1..#ConjugacyClasses(Gp)],
j1 in [1..#ConjugacyClasses(Cent[j])] do
printf ", ";
firstprint := 1;
particlenum := 0;
for k in [1..#ConjugacyClasses(Gp)], k1 in
[1..#ConjugacyClasses(Cent[k])] do
particlenum := particlenum + 1;
if (FusionCoefficientsviaSMatrix(i, i1, j, j1, k, k1,Gp) ne 0) then
if firstprint eq 0 then printf "+";
end if;
firstprint := 0;
if (FusionCoefficientsviaSMatrix(i, i1, j, j1, k, k1,Gp) ge 2) then
printf "\%o.", FusionCoefficientsviaSMatrix(i, i1, j, j1, k, k1,Gp);
end if;
printf "\%o", particlenum;
end if;
end for;
end for;
end for;
return 0;
end function;
43
function spinprinter(Gp, A, alpha) //returns spin mod 1
CC:=ConjugacyClasses(Gp);
CT:=CharacterTable(Centralizer(Gp, Gp!CC[A][3]))[alpha];
C := ComplexField();
z:=(C!CT(CC[A][3]))/(C!CT[1]);
s1:=Log(z)/(2*Pi(C)*C.1);
s:=(s1+ComplexConjugate(s1))/2;
return(s);
end function;
Appendix B: Other Interesting Quantum Doubles
1. Finite Subgroups of SO(3) and SU (2)
In this appendix, the tabulation of the quantum doubles of all non-dihedral ﬁnite sub-
groups ofSO(3) is completed. In the case of the inﬁnite family Dn, the quantum doubles for
the smallest order groups are tabulated. (These are most likely to be physically relevant.)
In addition to being potentially physically relevant, the tables for the remaining subgroups
of SO(3) provide a demonstration of the variety of properties that can be exhibited by a
