---
doc_id: arxiv-2601.07906v2
doc_title: "March 2026 A universal sum over topologies in 3d gravity"
section_id: sec-002-kinematic-constraints
section_title: "Kinematic constraints"
section_number: null
pages: 11-13
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
doc_brief: "March 2026 A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS 3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
First, we state the constraints that we will impose on each member of the ensemble—
that is, not just on average. For eachi, we demand the spinJ i to be an integer, as
is appropriate for a bosonic CFT 2. Note that although this is a natural property to
demand, it was not imposed in the original ensemble of [3]. In our case, spin quan-
tization will follow as a special case of the stronger constraint of crossing symmetry
and modular invariance that we impose in section 2.2.
Next, the OPE coefficients must satisfy the following properties under complex
conjugation and permutation of the indices (hereσ∈S 3):
C∗
ijk =C kji, C σ(i)σ(j)σ(k) = sgn(σ)Ji+Jj+JkCijk.(2.3)
Combining these constraints implies thatC ijk is purely real when the sum of spins
is even, and purely imaginary when odd. When two operators coincide, the second
constraint also implies thatC jjk = (−1)JkCjjk , hence the OPE coefficientC jjk can
only be nonzero ifJ k is even (and moreoverC jjk is real). Lastly, we impose the
selection rule when one of the operators is the identity,C ij1 =δ ij,whereδ ij is the
Kronecker delta.
To account for the structure of descendant states, we can expand any genus-g
partition function into Virasoro conformal blocks [54]. Loosely speaking, the blocks
resum all contributions to the partition function from descendants, so that the re-
maining sums are only over primary states and OPE coefficients. More precisely, the
conformal block decomposition requires us to pick a channelC, so that
Z[Σg; Ω, ¯Ω] =
Z
d3g−3hd 3g−3¯h
Y
ei∈ΓC
ρ(hi, ¯hi)
Y
vijk∈ΓC
CijkFC
g (h; Ω) ¯FC
g (¯h; ¯Ω).(2.4)
Let us explain the notation used.F C
g denotes the genus-gVirasoro conformal block
in the channelC. The choice of channel involves a pair-of-pants decomposition of
the surface Σg, which gives a set of 3g−3 moduli, to which we collectively refer as
– 11 –
Ω. Similarly, the right-moving conformal block ¯FC
g depends on 3g−3 independent
right-moving moduli ¯Ω. The pair-of-pants decomposition defines a dual trivalent
graph ΓC, whose edges are labeled by the conformal weightsh= (h 1,...,h 3g−3) and
¯h= ( ¯h1,..., ¯h3g−3), and whose vertices are labeled by the OPE coefficientsCijk. This
graph specifies the products appearing in the average (2.4): each edgee i contributes
a factor of the density of states and each vertexvijk a factor ofCijk, where the pattern
of OPE indices is determined by the topology of the graph Γ C.
In equation (2.4), we used linearity to write the average ofZ[Σ g] in terms of
the average of the primary data encoded in theρ(h i, ¯hi)’s and the OPE coefficients.
Recall that this average is defined with respect to the measureµ({hi, ¯hi,Cijk}). After
averaging, we expect the momentQρQCto be a smooth function of the conformal
weightsh, ¯h, at least for the states above the black hole threshold—more generally, it
is a distribution, with discrete support on the light spectrum and continuous support
on the heavy spectrum. In section 3, we will see how these moments are related to
gravitational partition functions in the bulk.
As an example of the above formalism, let us draw the ‘sunset’ and ‘dumbbell’
channels for the genus-2 partition function, with the corresponding index structures:
i j k →C ijkCkji, i j k →C iijCjkk.(2.5)
We read the cyclic ordering of the indices of the structure constants in a counter-
clockwise sense of the three outgoing lines at each vertex. There are of course also
the same diagrams where some of the indices are permuted. At genus 3, we have the
following inequivalent graph topologies:
, , , , (2.6)
where the first diagram corresponds to the index structureC 112C234C345C566, the
second toC 123C124C345C566, and so forth. In general, at genusgwe get 2g−2 OPE
coefficients, giving (3(2g−2)−1)!! pairwise index contractions (many of which are
related by graph automorphisms).
Note that these are all diagrams that can be drawn on the level of index structures
of the OPE coefficients. However, the conformal blocks encode more data than just
the graph topology: they are fully specified by the pair-of-pants decomposition and
the braiding phases at each vertex of the dual graph (see the figures in [20] for the
complete graphical representations of the blocks). There are an infinite number of
such channels (where the trivalent graphs can be knotted), which are obtained from
the basic graphs in (2.5) and (2.6) by acting with crossing transformations, also called
Moore-Seiberg moves [55–57]. These crossing transformations will be the topic of the
next subsection.
– 12 –
FB S
Figure 4. The three basic Moore-Seiberg moves, acting on embedded bordered surfaces
in a given pair-of-pants decomposition of a Riemann surface. From left to right, these are
the braiding transformation, the fusion move and the modular S-transform.
