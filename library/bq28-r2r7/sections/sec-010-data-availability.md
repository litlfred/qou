---
doc_id: bq28-r2r7
doc_title: "Classical and Quantum Algorithms for Characters of the Symmetric Group"
section_id: sec-010-data-availability
section_title: ". DATA AVAILABILITY"
section_number: null
pages: 14-15
source_pdf: bq28-r2r7.pdf
source_sha256: 38419a88531ebce7
toc_source: outline
doc_brief: "Classical and Quantum Algorithms for Characters of the Symmetric Group — 12 sections: Front matter; I.. INTRODUCTION; II.. GROUP THEORY REFRESHER"
---
DATA AVAILABILITY
The data supporting the ﬁndings of this article and a
Python package to implement the MPS algorithms for
characters and Kostka numbers are openly available [33].
[1] Daniel Grier and Luke Schaeﬀer, in Proceedings of the
52nd Annual ACM SIGACT Symposium on Theory of Com-
puting (Association for Computing Machinery, Chicago,
USA, 2020), p. 875.
[2] David Lawrence Johnson, Minimal permutation represen-
tations of ﬁnite groups, Am. J. Math. 93, 857 (1971).
[3] Charles Thomas Hepler, On the complexity of com-
puting
characters
of
ﬁnite
groups.
Master’s
thesis.
https://prism.ucalgary.ca/items/0d83d63a-ec3b-47bd-
b5ca-18bf532eb49a, (1996).
[4] Christian Ikenmeyer, Igor Pak, and Greta Panova, Posi-
tivity of the symmetric group characters is as hard as the
polynomial time hierarchy, Int. Math. Res. Not. 2024, 8442
(2023).
[5] Gerald V. Dunne, Slater decomposition of Laughlin states,
Int. J. Mod. Phys. B 7, 4783 (1993).
[6] Andrea Di Gioacchino, Luca Guido Molinari, Vittorio
Erba, and Pietro Rotondo, Uniﬁed Fock space representa-
tion of fractional quantum Hall states, Phys. Rev. B 95,
245123 (2017).
[7] Di Gioacchino, Fock-space operator construction of Laugh-
lin fractional quantum Hall eﬀect states: http://pcteserver.mi.
infn.it/caraccio/Lauree/DiGioacchino_m.pdf, (2015).
[8] P. Di Francesco, M. Gaudin, C. Itzykson, and F. Lesage,
Laughlin’s wave functions, Coulomb gases and expansions
of the discriminant, Int. J. Mod. Phys. A 9, 4257 (1994).
[9] Benoît Collins and Piotr ´Sniady, Integration with respect
to the Haar measure on unitary, orthogonal and symplectic
group, Commun. Math. Phys. 264, 773 (2006).
[10] Imre Risi Kondor, Group Theoretical Methods in Machine
Learning (Columbia University, New York City, USA,
2008).
[11] Risi Kondor and Marconi S. Barbosa, in COLT (Asso-
ciation for Computing Machinery, Haifa, Israel, 2010),
p. 451.
[12] Guifré Vidal, Eﬃcient classical simulation of slightly
entangled quantum computations, Phys. Rev. Lett. 91,
147902 (2003).
[13] Marcos Crichigno and Anupam Prakash, Quantum spin
chains and symmetric functions, ArXiv:2404.04322.
[14] Sergey Fomin and Curtis Greene, Noncommutative Schur
functions and their applications, Discrete Math. 193, 179
(1998).
[15] F. G. Frobenius, in Sitz. Ber. Preuss. Akad. (Prussian
Academy of Sciences, Berlin, Germany, 1900), p. 516.
[16] Johnnie Gray, quimb: A python package for quantum infor-
mation and many-body calculations, J. Open Source Softw.
3, 819 (2018).
[17] Daniel Suess and Milan Holzäpfel, mpnum: A matrix prod-
uct representation library for python, J. Open Source Softw.
2, 465 (2017).
[18] Robert Beals, in Proceedings of the twenty-ninth annual
ACM symposium on Theory of computing (Associa-
tion for Computing Machinery, El Paso, USA, 1997),
p. 48.
[19] Scott Aaronson and Alex Arkhipov, in Proceedings of the
forty-third annual ACM symposium on Theory of com-
puting, (Association for Computing Machinery, San Jose,
USA, 2011), p. 333.
[20] Michael J. Bremner, Ashley Montanaro, and Dan J. Shep-
herd, Average-case complexity versus approximate simula-
tion of commuting quantum computations, Phys. Rev. Lett.
117, 080501 (2016).
[21] Dominik Hangleiter and Jens Eisert, Computational advan-
tage of quantum random sampling, Rev. Mod. Phys. 95,
035001 (2023).
[22] Francis D. Murnaghan, The characters of the symmetric
group, Am. J. Math. 59, 739 (1937).
[23] Tadasi Nakayama, in Japanese journal of mathematics:
transactions and abstracts (The Mathematical Society of
Japan, Tokyo, 1940), Vol. 17, p. 411.
[24] Ömer E˘gecio˘glu, in European Conference on Computer
Algebra, (Springer, Linz, Austria, 1985), p. 206.
[25] Stephen P. Jordan, Fast quantum algorithms for approx-
imating
some
irreducible
representations
of
groups,
(2009).
[26] Sergey Bravyi, Anirban Chowdhury, David Gosset, Vojtˇech
Havlíˇcek, and Guanyu Zhu, Quantum complexity of
the Kronecker coeﬃcients, PRX Quantum 5, 010329
(2024).
[27] Martin Larocca and Vojtech Havlicek, Quantum algorithms
for representation-theoretic multiplicities, Phys. Rev. Lett.
135, 010602 (2025).
[28] Pavel I. Etingof, Oleg Golberg, Sebastian Hensel, Tiankai
Liu, Alex Schwendner, Dmitry Vaintrob, and Elena Yudov-
ina, Introduction to Representation Theory (American
Mathematical Soc., Providence, USA, 2011), Vol. 59.
[29] It may be helpful to understand this binary encoding of a
partition as follows. If we start with the bit string xτ+λ and
then interpret each 1 as “up by one” and each 0 as “to the
right by one” and then trace out a picture according to these
instructions, we get a picture of the partition λ within a
bounding box of size n × n.
[30] Ulrich Schollwöck, The density-matrix renormalization
group in the age of matrix product states, Ann. Phys. 326,
96 (2011).
[31] The GAP Group, GAP – Groups, Algorithms, and Program-
ming, version 4.12.2, 2022.
[32] W. A. Stein et al., Sage Mathematics Software, version 9.8,
The Sage Development Team, 2023, http://www.sagemath.
org
[33] Sergey Bravyi, David Gosset, Vojtech Havlicek, and Louis
Schatzki,
https://github.com/sbravyi/symmetric_group_
characters.
[34] Alok Shukla and Prakash Vedula, An eﬃcient quantum
algorithm for preparation of uniform quantum superposi-
tion states, Quantum Inf. Process. 23, 38 (2024).
[35] Richard P. Stanley, Enumerative Combinatorics: Volume 2
(Cambridge University Press, 1999), Vol. 62.
[36] A Vershik and S Kerov, Asymptotics of the maximal and
typical dimension of irreducible representations of symmet-
ric group, Func. Anal. Appl. 19, 25 (1985).
[37] Greta Panova, Polynomial time classical versus quan-
tum algorithms for representation theoretic multiplicities,
ArXiv:2502.20253.
[38] Juan Bermejo-Vega and Kevin C. Zatloukal, Abelian
hypergroups and quantum computation, ArXiv:1509.05806.
[39] Michael J. Bremner, Richard Jozsa, and Dan J. Shepherd,
Classical simulation of commuting quantum computations
implies collapse of the polynomial hierarchy, Proc. R. Soc.
A: Math. Phys. Eng. Sci. 467, 459 (2011).
[40] Larry Stockmeyer, in Proceedings of the ﬁfteenth annual
ACM symposium on Theory of computing (Association
for Computing Machinery, New York City, USA, 1983),
p. 118.
[41] Kevin Ford, Cycle type of random permutations: A toolkit,
Discrete Analysis (2022).
[42] G. H. Hardy and S. Ramanujan, Asymptotic formulaæ in
combinatory analysis, Proc. London Math. Soc. s2-17, 75
(1918).
[43] Sergey Bravyi and Mikhail Vyalyi, Commutative version of
the k-local Hamiltonian problem and common eigenspace
problem, Quantum Inf. Comput. 5, 187 (2005).
[44] A. Yu Kitaev, Fault-tolerant quantum computation by
anyons, Ann. Phys. 303, 2 (2003).
[45] Norbert Schuch, Complexity of commuting Hamiltonians
on a square lattice of qubits, Quantum Inf. Comput. 11, 901
(2011).
[46] Dorit Aharonov and Lior Eldar, in 2011 IEEE 52nd Annual
Symposium on Foundations of Computer Science (IEEE,
Palm Springs, USA, 2011), p. 334.
[47] Matthew B. Hastings, Matrix product operators and central
elements: Classical description of a quantum state, Geom.
Topol. Monogr. 18, 276 (2012).
[48] Dorit Aharonov, Oded Kenneth, and Itamar Vigdorovich,
in Proceedings of the thirteenth conference on the Theory
of Quantum Computation, Communication and Cryptogra-
phy (Schloss Dagstuhl – Leibniz-Zentrum fur Informatik,
Sydney, Australia, 2018), p. 2.
[49] Dorit Aharonov and Lior Eldar, The commuting local
Hamiltonian problem on locally expanding graphs is
approximable in NP, Quantum Inf. Process. 14, 1 (2015).
[50] Sandy Irani and Jiaqing Jiang, Commuting local Hamilto-
nian problem on 2D beyond qubits, ArXiv:2309.04910.
[51] Paul Erdös and Joseph Lehner, The distribution of the num-
ber of summands in the partitions of a positive integer,
Duke Math. J. 8, 335 (1941).
