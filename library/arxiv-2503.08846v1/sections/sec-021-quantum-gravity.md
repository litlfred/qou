---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-021-quantum-gravity
section_title: "Quantum Gravity"
section_number: null
pages: 44-51
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
Quantum Gravity
Knot theory explicitly appears in the construction of states of loop quantum gravity [101,110]. Quantum
states in this theory are similar to the Chern-Simons states used in this review, although they are based
on closed lines, or closed networks, which are analogs of conformal blocks mentioned here, but with no
open ends. Consequently, some questions addressed in this review, such as properties of multipartite
entanglement, can be studied in the context of loop quantum gravity, using similar techniques. See [111]
for a recent example.
In the string theory approach to quantum gravity the relevant framework appears in the context
of the AdS/CFT (or holographic) correspondence [112]. The AdS/CFT correspondence postulates the
equivalence, or duality, of two descriptions of the same quantum theory, valid for a large class of theories:
one is a gravitational theory in the bulk of some space and another is a theory without gravity defined
on the boundary of that space (see also [113,114]). The general idea of such a duality can be explained
in terms of a TQFT, and, in particular, Chern-Simons theory, which is a prototypical example of the
holographic correspondence.
Recall that in the Atiyah’s axioms, the boundary of the topological space encodes the Hilbert space.
The bulk cobordisms serve as one way of discriminating between different states in this Hilbert space,
but not a unique way. In the 3D Chern-Simons case the boundary theory can be described by a 2D Wess-
Zumino-Witten model, which is then a CFT-dual description of the 3D gauge theory. More abstractly,
the theory and the specific states of the boundary theory can be constructed in terms of representations
of the braid group action on the punctures on the boundary.
One can think of the construction in
section 2.4 as of an example of such a representation. In this case, braids themselves are emerging bulk
representations of the action of given operators in the Hilbert space.
The analogy between Chern-Simons states and gravity can be made even more precise if one observes
that three-dimensional gravity in anti de Sitter (AdS) space has a description in terms of a Chern-Simons
theory with a noncompact gauge group [115, 116]. Due to the noncompactness, the treatment of this
theory is more difficult than the SU(2) case considered here (see for example [117,118] for the discussion
of the main issues), but in principle, questions similar to the ones discussed in this review can be addressed
in this framework too.
We will close this discussion by giving the interpretation of the classical limit of the entanglement
entropy formula in terms of the famous result of Shinsei Ryu and Tadashi Takayanagi in holography [103].
44
The Ryu-Takayanagi formula expresses the entropy of a region of the boundary (subsystem A) in terms
of gravitational data in the bulk of the dual description. Namely, the entropy is proportional to the area
of the minimal-area surface in the bulk anchored at the boundary of the boundary region A:
SvN = min
{γ}
Area[γ]
4GN
.
(176)
Here γ is a surface in the bulk, whose area must be minimized, and GN is the Newton constant.
In section 4.3 we observed that for the connectome states, which are characteristic states of Chern-
Simons in the classical limit, the entropy is computed by the number of lines connecting the two parties.
In the limit of large number of Wilson lines the result is given by (156). We noted that the number of
connections is counted by a surface that encircles one of the subsystems and crosses the minimal number
of connections.
If one assumes that each line comes with a flux proportional to the inverse Newton
constant then the Ryu-Takayanagi formula follows [86]. Similar counting emerges in the tensor network
construction of holography [119] and in the “bit thread” models [120,121].
Chern-Simons, or TQFT states provide at least a heuristic picture of many concepts and results
discussed in the AdS/CFT over the past years.
Besides the correspondence itself, the emergence of
space from entanglement, the Ryu-Takayanagi formula, entropy inequalities, discussed here, one can also
mention Witten diagrams [114], bulk reconstruction [122], quantum error correcting codes [123], tensor
networks [124], replica wormholes and black hole information paradox [125–128] among the topics, where
the present “categorical” or “pictorial” approach may be of certain use. It should also be useful for
understanding quantum gravity itself.
Acknowledgments.
I would like to thank Julio Fabris and the Federal University of Espirito Santo in
Vitoria for hosting the IV Patricio Letelier School on Mathematical Physics, for which the first version
of these notes was prepared. I would also like to thank Jo˜ao Aires, Rafael Chaves, Andrei Mironov,
Sergey Mironov, Alexei Morozov, Andrey Morozov, Marcos Neves, Jefferson Oliveira, Luigy Pinto, Davide
Poderini and Vivek Singh for useful discussions and collaboration on related projects. This work was
supported by the Simons Foundation award number 1023171-RC, grants of the Brazilian National Council
for Scientific and Technological Development (CNPq) number 308580/2022-2 and 404274/2023-4, and
grant 1699/24 IIF-FINEP of the Brazilian Ministry of Science of Technology.
References
[1] W. Thomson, On vortex atoms, Proceedings of the Royal Society of Edinburgh 6 (1869) 94.
[2] L. D. Faddeev and A. J. Niemi, Knots and particles, Nature 387 (1997) 58 [hep-th/9610193].
[3] V. F. R. Jones, A polynomial invariant for knots via von Neumann algebras, Bull. Am. Math. Soc.
12 (1985) 103.
[4] A. A. Belavin, A. M. Polyakov, A. S. Schwartz and Y. S. Tyupkin, Pseudoparticle Solutions of the
Yang-Mills Equations, Phys. Lett. B 59 (1975) 85.
[5] A. S. Schwarz, The Partition Function of Degenerate Quadratic Functional and Ray-Singer
Invariants, Lett. Math. Phys. 2 (1978) 247.
[6] S. K. Donaldson, An application of gauge theory to four-dimensional topology, J. Diff. Geom. 18
(1983) 279.
[7] A. Floer, An instanton-invariant for 3-manifolds, Communications in mathematical physics 118
(1988) 215.
45
[8] A. M. Polyakov, Fermi-Bose Transmutations Induced by Gauge Fields, Mod. Phys. Lett. A 3
(1988) 325.
[9] L. H. Kauffman, State models and the jones polynomial, Topology 26 (1987) 395.
[10] V. G. Turaev, The Yang-Baxter equation and invariants of links, Invent. Math. 92 (1988) 527.
[11] A. Tsuchiya and Y. Kanie, Vertex Operators in the Conformal Field Theory on p1 and
Monodromy Representations of the Braid Group, Lett. Math. Phys. 13 (1987) 303.
[12] E. P. Verlinde, Fusion Rules and Modular Transformations in 2D Conformal Field Theory, Nucl.
Phys. B 300 (1988) 360.
[13] G. W. Moore and N. Seiberg, Polynomial Equations for Rational Conformal Field Theories, Phys.
Lett. B 212 (1988) 451.
[14] G. B. Segal, The definition of conformal field theory, in Differential geometrical methods in
theoretical physics, pp. 165–171. Springer, 1988.
[15] E. Witten, Quantum Field Theory and the Jones Polynomial, Commun. Math. Phys. 121 (1989)
351.
[16] V. O. Manturov, Knot theory. CRC press, 2018.
[17] J. H. Przytycki, R. P. Bakshi, D. Ibarra, G. Montoya-Vega and D. Weeks, Lectures in Knot
Theory: An Exploration of Contemporary Topics. Springer, 2024.
[18] L. H. Kauffman, Knots and physics, vol. 1. World scientific, 2001.
[19] M. Atiyah, Topological quantum field theories, Inst. Hautes Etudes Sci. Publ. Math. 68 (1989) 175.
[20] E. Witten, Topological Quantum Field Theory, Commun. Math. Phys. 117 (1988) 353.
[21] A. S. Schwarz, Topological quantum field theories, hep-th/0011260.
[22] A. Y. Kitaev, Fault tolerant quantum computation by anyons, Annals Phys. 303 (2003) 2
[quant-ph/9707021].
[23] C. Nayak, S. H. Simon, A. Stern, M. Freedman and S. Das Sarma, Non-Abelian anyons and
topological quantum computation, Rev. Mod. Phys. 80 (2008) 1083 [0707.1889].
[24] S. H. Simon, Topological quantum. Oxford University Press, 2023.
[25] S. Abramsky and B. Coecke, A categorical semantics of quantum protocols, quant-ph/0402130.
[26] G. M. Kelly and M. L. Laplaza, Coherence for compact closed categories, Journal of pure and
applied algebra 19 (1980) 193.
[27] A. Joyal and R. Street, The geometry of tensor calculus, i, Advances in mathematics 88 (1991) 55.
[28] A. Carboni and R. F. Walters, Cartesian bicategories i, Journal of pure and applied algebra 49
(1987) 11.
[29] S. Lack, Composing props, Theory and Applications of Categories 13 (2004) 147.
[30] B. Coecke, Kindergarten quantum mechanics: Lecture notes, in AIP Conference Proceedings,
vol. 810, pp. 81–98, American Institute of Physics, 2006.
46
[31] B. Coecke, Quantum picturalism, Contemp. Phys. 51 (2010) 59.
[32] S. D¨undar-Coecke, L. Yeh, C. Puca, S. M. L. Pfaendler, M. H. Waseem, T. Cervoni et al.,
Quantum Picturalism: Learning Quantum Theory in High School, in 2023 International
Conference on Quantum Computing and Engineering, 12, 2023, 2312.03653, DOI.
[33] B. Coecke and A. Kissinger, Picturing Quantum Processes: A First Course in Quantum Theory
and Diagrammatic Reasoning. Cambridge University Press, 2017.
[34] C. Heunen and J. Vicary, Categories for Quantum Theory: An Introduction. Oxford University
Press, 2019.
[35] L. H. Kauffman, Knot logic and topological quantum computing with Majorana fermions. 2016.
1301.6214. 10.1017/CBO9781139519687.012.
[36] L. H. Kauffman and S. J. Lomonaco, Quantum entanglement and topological entanglement, New
Journal of Physics 4 (2002) 73.
[37] L. H. Kauffman and S. J. Lomonaco Jr, Entanglement criteria: quantum and topological, in
Quantum Information and Computation, vol. 5105, pp. 51–58, SPIE, 2003.
[38] L. H. Kauffman and S. J. Lomonaco Jr, Quantum knots, in Quantum Information and
Computation II, vol. 5436, pp. 268–284, SPIE, 2004.
[39] L. H. Kauffman and S. J. Lomonaco, Braiding operators are universal quantum gates, New
Journal of Physics 6 (2004) 134.
[40] L. H. Kauffman and S. J. Lomonaco Jr, q-deformed spin networks, knot polynomials and anyonic
topological quantum computation, Journal of Knot Theory and Its Ramifications 16 (2007) 267.
[41] S. J. Lomonaco and L. H. Kauffman, Quantum knots and mosaics, Quantum Information
Processing 7 (2008) 85.
[42] C. Adams, Why Knot?: An Introduction to the Mathematical Theory of Knots, Key curriculum
press. Key College, 2004.
[43] A. B. Sossinsky, Knots, Links and Their Invariants: An Elementary Course in Contemporary
Knot Theory, vol. 101. American Mathematical Society, 2023.
[44] J. W. Alexander, Topological invariants of knots and links, Transactions of the American
Mathematical Society 30 (1928) 275.
[45] V. F. R. Jones, Hecke algebra representations of braid groups and link polynomials, Annals Math.
126 (1987) 335.
[46] P. Freyd, D. Yetter, J. Hoste, W. B. R. Lickorish, K. Millett and A. Ocneanu, A new polynomial
invariant of knots and links, Bull. Am. Math. Soc. 12 (1985) 239.
[47] J. H. Przytycki and P. Traczyk, Invariants of links of conway type, Kobe J. Math 4 (1987)
115–139 [1610.06679].
[48] H. N. V. Temperley and E. H. Lieb, Relations between the ’percolation’ and ’colouring’ problem
and other graph-theoretical problems associated with regular planar lattices: some exact results for
the ’percolation’ problem, Proc. Roy. Soc. Lond. A 322 (1971) 251.
47
[49] G. C˘alug˘areanu, L’int´egral de gauss et l’analyse des nœuds tridimensionnels, Rev. Math. Pures
Appl. 4 (1959) 5.
[50] G. C˘alug˘areanu, Sur les classes d’isotopie des noeuds tridimensionnels et leurs invariants,
Czechoslovak Mathematical Journal 11 (1961) 588.
[51] J. H. White, Self-linking and the gauss integral in higher dimensions, American Journal of
Mathematics 91 (1969) 693.
[52] F. B. Fuller, The writhing number of a space curve, Proceedings of the National Academy of
Sciences 68 (1971) 815.
[53] Y. Zhang, L. H. Kauffman and M.-L. Ge, Yang-Baxterizations, universal quantum gates and
Hamiltonians, Quant. Inf. Proc. 4 (2005) 159 [quant-ph/0502015].
[54] L. H. Kauffman and E. Mehrotra, Topological aspects of quantum entanglement, Quantum
Information Processing 18 (2019) 1.
[55] P. Padmanabhan, F. Sugino and D. Trancanelli, Braiding quantum gates from partition algebras,
Quantum 4 (2020) 311 [2003.00244].
[56] D. Melnikov, Jones polynomials from matrix elements of tangles in a pseudounitary
representation, 2403.17227.
[57] M. Jimbo, Quantum r Matrix for the Generalized Toda System, Commun. Math. Phys. 102 (1986)
537.
[58] H. Simmons, An introduction to category theory. Cambridge University Press, 2011.
[59] D. Melnikov, Entanglement classification from a topological perspective, Phys. Rev. D 107 (2023)
126005 [2208.13901].
[60] J. Lurie, On the Classification of Topological Field Theories, Int. Press (2009) 129 [0905.0465].
[61] D. S. Freed, The cobordism hypothesis, Bulletin of the American Mathematical Society 50 (2013)
57 [1210.5100].
[62] G. V. Dunne, Aspects of Chern-Simons theory, in Les Houches Summer School in Theoretical
Physics, Session 69: Topological Aspects of Low-dimensional Systems, 7, 1998, hep-th/9902115.
[63] J. Wess and B. Zumino, Consequences of anomalous Ward identities, Phys. Lett. B 37 (1971) 95.
[64] E. Witten, Global Aspects of Current Algebra, Nucl. Phys. B 223 (1983) 422.
[65] E. Witten, Nonabelian Bosonization in Two-Dimensions, Commun. Math. Phys. 92 (1984) 455.
[66] K. Gawedzki, Conformal field theory: A Case study, hep-th/9904145.
[67] A. Anokhina, E. Lanina and A. Morozov, Planar decomposition of the HOMFLY polynomial for
bipartite knots and links, Eur. Phys. J. C 84 (2024) 990 [2407.08724].
[68] A. Anokhina, E. Lanina and A. Morozov, Planar decomposition of bipartite HOMFLY polynomials
in symmetric representations, Phys. Rev. D 111 (2025) 046018 [2410.18525].
[69] G. Salton, B. Swingle and M. Walter, Entanglement from Topology in Chern-Simons Theory,
Phys. Rev. D 95 (2017) 105007 [1611.01516].
48
[70] V. Balasubramanian, J. R. Fliss, R. G. Leigh and O. Parrikar, Multi-Boundary Entanglement in
Chern-Simons Theory and Link Invariants, JHEP 04 (2017) 061 [1611.05460].
[71] V. Balasubramanian, M. DeCross, J. Fliss, A. Kar, R. G. Leigh and O. Parrikar, Entanglement
Entropy and the Colored Jones Polynomial, JHEP 05 (2018) 038 [1801.01131].
[72] S. Chun and N. Bao, Entanglement entropy from SU(2) Chern-Simons theory and symmetric
webs, 1707.03525.
[73] S. Dwivedi, V. K. Singh, S. Dhara, P. Ramadevi, Y. Zhou and L. K. Joshi, Entanglement on linked
boundaries in Chern-Simons theory with generic gauge groups, JHEP 02 (2018) 163 [1711.06474].
[74] G. Camilo, D. Melnikov, F. Novaes and A. Prudenziati, Circuit Complexity of Knot States in
Chern-Simons theory, JHEP 07 (2019) 163 [1903.10609].
[75] M. Buican and R. Radhakrishnan, Galois conjugation and multiboundary entanglement entropy,
JHEP 12 (2020) 045 [1912.04937].
[76] S. Dwivedi, V. K. Singh and A. Roy, Semiclassical limit of topological R´enyi entropy in 3d
Chern-Simons theory, JHEP 12 (2020) 132 [2007.07033].
[77] J. R. Fliss, Knots, links, and long-range magic, JHEP 04 (2021) 090 [2011.01962].
[78] R. G. Leigh and P.-C. Pai, Complexity for link complement states in Chern-Simons theory, Phys.
Rev. D 104 (2021) 065005 [2101.03443].
[79] A. Dwivedi, S. Dwivedi, B. P. Mandal, P. Ramadevi and V. K. Singh, Topological entanglement
and hyperbolic volume, JHEP 10 (2021) 172 [2106.03396].
[80] P. Caputa, S. Purkayastha, A. Saha and P. Su lkowski, Musings on SVD and pseudo entanglement
entropies, JHEP 11 (2024) 103 [2408.06791].
[81] C. J. Ram´ırez-Valdez, H. Garc´ıa-Compe´an and J. de-la Cruz-Moreno, Further Remarks on the
Entanglement Entropy of Hopf links, 2408.13439.
[82] S. Dwivedi, Topological entanglement and number theory, 2410.01492.
[83] V. Balasubramanian and C. Cummings, Multipartite Entanglement Structure of Fibered Link
States, 2502.19466.
[84] D. Melnikov, A. Mironov, S. Mironov, A. Morozov and A. Morozov, From Topological to Quantum
Entanglement, JHEP 05 (2019) 116 [1809.04574].
[85] S. Dwivedi, V. K. Singh, P. Ramadevi, Y. Zhou and S. Dhara, Entanglement on multiple S2
boundaries in Chern-Simons theory, JHEP 08 (2019) 034 [1906.11489].
[86] D. Melnikov, Connectomes as holographic states, Nucl. Phys. B 1010 (2025) 116757 [2312.16683].
[87] R. Chaves, D. Melnikov, M. Neves, L. Pinto and D. Poderini, Error-Correcting Codes in TQFT
on Multispheres, 2410.05404.
[88] P. Aravind, Borromean entanglement of the ghz state, Potentiality, Entanglement and
Passion-at-a-Distance: Quantum Mechanical Studies for Abner Shimony Volume Two (1997) 53.
[89] S. Dong, E. Fradkin, R. G. Leigh and S. Nowling, Topological Entanglement Entropy in
Chern-Simons Theories and Quantum Hall Fluids, JHEP 05 (2008) 016 [0802.3231].
49
[90] D. Bohm, Quantum theory. Courier Corporation, 1989.
[91] J. Maldacena and L. Susskind, Cool horizons for entangled black holes, Fortsch. Phys. 61 (2013)
781 [1306.0533].
[92] W. Israel, Thermo field dynamics of black holes, Phys. Lett. A 57 (1976) 107.
[93] J. M. Maldacena, Eternal black holes in anti-de Sitter, JHEP 04 (2003) 021 [hep-th/0106112].
[94] M. Van Raamsdonk, Building up spacetime with quantum entanglement, Gen. Rel. Grav. 42
(2010) 2323 [1005.3035].
[95] W. Dur, G. Vidal and J. I. Cirac, Three qubits can be entangled in two inequivalent ways, Phys.
Rev. A 62 (2000) 062314 [quant-ph/0005115].
[96] G. Vidal, Entanglement of pure states for a single copy, Phys. Rev. Lett. 83 (1999) 1046
[quant-ph/9902033].
[97] M. A. Nielsen, Conditions for a Class of Entanglement Transformations, Phys. Rev. Lett. 83
(1999) 436 [quant-ph/9811053].
[98] H. Wenzl, On sequences of projections, CR Math. Rep. Acad. Sci. Canada 9 (1987) 5.
[99] L. H. Kauffman, S. L. Lins and S. Lins, Temperley-Lieb recoupling theory and invariants of
3-manifolds, no. 134. Princeton University Press, 1994.
[100] R. Penrose, Angular momentum: an approach to combinatorial space-time, Quantum theory and
beyond 151 (1971) .
[101] C. Rovelli and L. Smolin, Spin networks and quantum gravity, Phys. Rev. D 52 (1995) 5743
[gr-qc/9505006].
[102] D. Melnikov, Connectomes and properties of quantum entanglement, JHEP 07 (2023) 015
[2302.08548].
[103] S. Ryu and T. Takayanagi, Holographic derivation of entanglement entropy from AdS/CFT, Phys.
Rev. Lett. 96 (2006) 181602 [hep-th/0603001].
[104] E. H. Lieb and M. B. Ruskai, Proof of the strong subadditivity of quantum-mechanical entropy, J.
Math. Phys. 14 (1973) 1938.
[105] C. H. Bennett, G. Brassard, C. Crepeau, R. Jozsa, A. Peres and W. K. Wootters, Teleporting an
unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels, Phys. Rev. Lett.
70 (1993) 1895.
[106] D. Melnikov, Toy gravizap for black hole redemption, Phys. Lett. B 851 (2024) 138554
[2211.01339].
[107] L. Kauffman, Teleportation topology, Optics and Spectroscopy 99 (2005) 227 [quant-ph/0407224].
[108] B. Coecke, The logic of entanglement, arXiv preprint quant-ph/0402014 (2004) .
[109] N. Bao, S. Nezami, H. Ooguri, B. Stoica, J. Sully and M. Walter, The Holographic Entropy Cone,
JHEP 09 (2015) 130 [1505.07839].
[110] R. Gambini and J. Pullin, Loops, Knots, Gauge Theories. Cambridge University Press, 2001.
50
[111] S. Cepollaro, G. Chirco, G. Cuffaro and V. D’Esposito, Curvature from multipartite entanglement
in quantum gravity states, Phys. Rev. D 108 (2023) 046010 [2305.02670].
[112] J. M. Maldacena, The Large N limit of superconformal field theories and supergravity, Adv. Theor.
Math. Phys. 2 (1998) 231 [hep-th/9711200].
[113] S. S. Gubser, I. R. Klebanov and A. M. Polyakov, Gauge theory correlators from noncritical string
theory, Phys. Lett. B 428 (1998) 105 [hep-th/9802109].
[114] E. Witten, Anti-de Sitter space and holography, Adv. Theor. Math. Phys. 2 (1998) 253
[hep-th/9802150].
[115] A. Achucarro and P. K. Townsend, A Chern-Simons Action for Three-Dimensional anti-De Sitter
Supergravity Theories, Phys. Lett. B 180 (1986) 89.
[116] E. Witten, (2+1)-Dimensional Gravity as an Exactly Soluble System, Nucl. Phys. B 311 (1988)
46.
[117] A. Maloney and E. Witten, Quantum Gravity Partition Functions in Three Dimensions, JHEP
02 (2010) 029 [0712.0155].
[118] A. Maloney and E. Witten, Averaging over Narain moduli space, JHEP 10 (2020) 187
[2006.04855].
[119] F. Pastawski, B. Yoshida, D. Harlow and J. Preskill, Holographic quantum error-correcting codes:
Toy models for the bulk/boundary correspondence, JHEP 06 (2015) 149 [1503.06237].
[120] M. Freedman and M. Headrick, Bit threads and holographic entanglement, Commun. Math. Phys.
352 (2017) 407 [1604.00354].
[121] M. Headrick and V. E. Hubeny, Covariant bit threads, JHEP 07 (2023) 180 [2208.10507].
[122] D. Harlow, TASI Lectures on the Emergence of Bulk Physics in AdS/CFT, PoS TASI2017
(2018) 002 [1802.01040].
[123] A. Almheiri, X. Dong and D. Harlow, Bulk Locality and Quantum Error Correction in AdS/CFT,
JHEP 04 (2015) 163 [1411.7041].
[124] A. Jahn and J. Eisert, Holographic tensor network models and quantum error correction: a topical
review, Quantum Sci. Technol. 6 (2021) 033002 [2102.02619].
[125] G. Penington, Entanglement Wedge Reconstruction and the Information Paradox, JHEP 09
(2020) 002 [1905.08255].
[126] A. Almheiri, N. Engelhardt, D. Marolf and H. Maxfield, The entropy of bulk quantum fields and
the entanglement wedge of an evaporating black hole, JHEP 12 (2019) 063 [1905.08762].
[127] G. Penington, S. H. Shenker, D. Stanford and Z. Yang, Replica wormholes and the black hole
interior, JHEP 03 (2022) 205 [1911.11977].
[128] A. Almheiri, T. Hartman, J. Maldacena, E. Shaghoulian and A. Tajdini, Replica Wormholes and
the Entropy of Hawking Radiation, JHEP 05 (2020) 013 [1911.12333].
51
