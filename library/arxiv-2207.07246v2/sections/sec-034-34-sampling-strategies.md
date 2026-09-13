---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-034-34-sampling-strategies
section_title: "Sampling Strategies"
section_number: 3.4
pages: 88-90
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
We have tested all the algorithms described in this chapter. We have also tested
the bisection method (Ceperley (1995)), as well as the reptation Monte Carlo method
(Baroni and Moroni (1999); Carleo et al. (2010)) for our calculation. For our light
nuclei PIMC calculation, as pointed out in section 3.2.2, we did not ﬁnd any advantage
for bisection over the multi-level sampling method. The reptation method basically
samples the spatial conﬁguration of the path by adding some beads at one end of the
path, and removing some beads to the other end of the path. However, since we have
spin and isospin sums in the path, the removing and adding of beads, even if just one
bead is involved, requires the recalculation of the whole path fV
l′r′(R′). Therefore it is
not economical to perform reptation moves. After initial testing we did not pursue
reptation moves further.
The multi-level sampling is eﬃcient so we do not do regular sampling described
in section 3.2.3 very often. The importance sampling also does not make much
diﬀerence. Considering that the importance sampling at least needs to calculate the
two possibilitiesπ(s′
1) andπ(s′
2) and an additionalπ(s2), we did not ﬁnd it particularly
78
increase the eﬃciency. Again we turned oﬀ the importance sampling in our calculations.
So when performing our calculations, about 90% moves are proposed by multi-level
sampling described in section 3.2.2, and the other 10% are proposed by diﬀerent kinds
of regular sampling described in section 3.2.3.
For multi-level sampling, for the total N + 1 beads along the path, we pick two
lengths, n1≈N/3 and n2≈N/6. And, 80% of the moves are proposed for n1 beads
and the others are for n2 beads. The acceptance rate for sampling n1 beads is about
20%, forn2 beads is about 40%. The reason for sampling n2 beads is mainly to include
the 0th and the N th beads. For example, if we have a total of 400 beads, we can pick
n1 = 27 = 128 and n2 = 26 = 64. 80% moves are proposed for the n1 = 128 beads
with acceptance rate around 20%, and the other 20% of the moves among the total
multi-level samplings are for n2 = 64 beads with an acceptance rate around 40%.
For the diﬀerent kinds of regular sampling which make the samples more uncorre-
lated than applying multi-level sampling alone, we include moving beads one by one,
moving all the beads at the same time, and shifting all the beads at the same time,
according to section 3.2.3. By moving beads one by one, we randomly pick a direction,
either propose moves from bead N to bead 0, or propose moves from bead 0 to bead
N. For each bead, we move each particle in it and we choose the step parameter α to
make the acceptance rate around 50%. By moving all the beads at the same time, we
move all the particles in each bead, the step parameter α needs to be smaller than
when moving beads one by one, in order to make the acceptance rate of moving all
the beads at the same time around 50% again. By shifting all the beads at the same
time, we propose to move each of the beads by using Eq.(3.64). The step parameter in
the common Λ vector is again adjusted to make the acceptance rate of shifting all the
beads around 50%. The overall eﬃciency of the algorithm is not substantially aﬀected
by these acceptance rates as long as they are in the 20% to 80% range.
79
Chapter 4
