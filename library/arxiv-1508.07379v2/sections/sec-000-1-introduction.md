---
doc_id: arxiv-1508.07379v2
doc_title: "Convergence of Mayer and Virial expansions and the Penrose t ree-graph identity"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1508.07379v2.pdf
source_sha256: c3dbf93d1cac198e
doc_brief: "Convergence of Mayer and Virial expansions and the Penrose t ree-graph identity — We establish new lower bounds for the convergence radius of the Ma yer series and the Virial series of a continuous"
---
Continuous particle systems are an important subject of inv estigation in rigorous statistical mechan-
ics. Since the thirties it was clear that the equation of stat e of a non ideal gas in thermodynamics
can be deduced from statistical mechanics via the Mayer seri es of the pressure in the grand canon-
ical ensemble. The Mayer series, proposed by Mayer (see, e.g ., [12] and references therein) is an
expansion in powers of the fugacity λ of the logarithm of the Grand Canonical partition function
of the the system under study, whose nth-order coeﬃcient is given by a sum of terms indexed by
the labeled connected graphs between n vertices. This series was at the time only formal and
the question about its convergence uniformly in the volume w here the gas is conﬁned, remained
an enigma during two decades. The diﬃculty in dealing with th is problem was basically due to
challenging combinatorial structure of the Mayer coeﬃcien ts.
In the sixties, Penrose [15] and independently Ruelle [19] p roved the convergence of the Mayer
series for a very large class of continuous particle systems . Namely those interacting via a stable
and tempered pair potential. The bound on the convergence ra dius R of the Mayer series obtained
in [15] and [19] still stands as the best available in the lite rature. It is worth to remind that the
ﬁrst singularity of Mayer series is in general not on the posi tive real fugacity axis (e.g. it is in the
negative axis at λ = −R for repulsive potentials, see [18]) so that the value λ = R for the fugacity is
not directly related to any physical phase transition point . However a lower bound for R as sharp as
possible is a physically relevant information since it allo ws to maximize the region of analyticity of
the pressure of the system, i.e. where the system is surely in the gas phase and no phase transitions
occur. In this respect, there have been only very few improve ments on the Penrose-Ruelle bound
for R by considering some restricted sub-classes of stable and te mpered potentials. Basically such
∗Departamento de Matem´ atica, Universidade Federal de Minas Gerais, Belo Horizonte-MG, Brazil - aldo@mat.ufmg.br
†Departamento de Matem´ atica, Universidad de Buenos Aires, Buenos Aires, Argentina - sergioyuhjtman@gmail.com
2010 Mathematics Subject Classiﬁcation. Primary 82B21; Secondary 05C05.
1
improvements can be summarized as follows. Brydges and coll aborators improved the Penrose-
Ruelle bound for absolutely summable pair potential (see e. g. [3] and references therein) and
Basuev gave in [2] an improvement for a signiﬁcant class of po tentials, introduced by himself in [1],
which is suﬃciently large to include Lennard-Jones type pot entials (see also recently [11]).
The method used to get the general bounds of 1963 were based on the so-called Kirkwood-Salzburg
equations (see [18] and references therein). It is an indire ct method which aims to control simulta-
neously all correlation functions of the systems by analyzi ng an inﬁnite set of equations involving
them. On the other hand, the methods used to get improvements cited above for subclasses of sta-
ble and tempered potentials are all based on trying to bound d irectly the Mayer coeﬃcients. The
main technical tools to obtain this task are the so-called tr ee-graph identities. Several alternative
identities have been proposed along the last four decades (s ee [3, 11] and references therein).
The very ﬁrst of these tree-graph identities, proposed by Pe nrose [16] in 1967, was based on the
existence of a map M (a so-called partition scheme ) from the set Tn of the labeled trees with n
vertices to the set Gn of the labeled connected graphs with n vertices. This map is able to induce a
partition of the set Gn into blocks indexed by the elements of set Tn (details in Section 3). Penrose
gave an explicit construction of such a map and used it to rewr ite the Mayer coeﬃcients as sum
of terms indexed by trees rather than by connected graphs. Us ing this alternative expression of
the Mayer coeﬃcients, Penrose was then able to bound them dir ectly, reobtaining the same bound
of 1963 but at the cost to impose a further condition on the pai r potential, beyond stability and
temperedness. Namely, the pair potential needed to have an h ard-core. This fact, we think, has
led researchers to believe that the identity proposed by Pen rose was useful only for systems with
hard-core and in fact in the literature it is mentioned only f or such kind of systems (see, e.g., [5, 20]
and reference therein).
In the present paper we disclaim this belief and show that the Penrose tree-graph identity can be
used to strongly improve the old Penrose-Ruelle bounds for g eneral stable and tempered potentials.
The main idea is based on the deﬁnition of a new map M , diﬀerent from the one originally proposed
by Penrose, which still is able to make a partition of the set o f connected graphs whose blocks are
indexed by minimum spanning trees, where the minimality is b asically on the energies of the edges
of the tree. Such new partition scheme, as we will see, allows to use in an optimal way the stability
condition of the pair potential.
The rest of the paper is organized as follows. In Section 2 we r emind the basic concepts for
continuous systems of classical particles, we give the deﬁn itions of stability and temperedness and
write down the Mayer series explicitly. We end the section by recalling the Penrose-Ruelle result
(Theorem 0) and by stating the main results of the paper. Name ly, in Theorem 1 we present
the new bound on the nth-order Mayer coeﬃcient and consequently the new lower bound on the
convergence radius of the Mayer series and in Proposition 1 w e give the main technical tool to proof
Theorem 1, id est a new tree graph inequality, deduced from the Penrose tree-g raph identity. In
Section 3 we prove Proposition 1. We start by recalling the Pe nrose identity for a generic partition
scheme M , we then introduce our new partition scheme and show how to us e it to obtain the
inequality given in Proposition 1. In Section 4 we conclude t he proof of Theorem 1. Finally, in
Section 5 we give a comparison with previous results and add s ome concluding remarks.
2
