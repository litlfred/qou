---
doc_id: arxiv-0903.1376v1
doc_title: "Particle Topology, Braids and Braided Belts"
section_id: sec-003-framed-braid-multiplication
section_title: "Framed braid multiplication"
section_number: null
pages: 6-8
source_pdf: 0903.1376v1.pdf
source_sha256: c106071c1a3110e8
toc_source: outline
doc_brief: "Particle Topology, Braids and Braided Belts — Recent work [1, 2] suggests that topological features of certain quantum gravity theories can be interpreted as particles, matching the known fermions"
---
Framed braid multiplication
As mentioned above, a braid with several crossings is speciﬁed by its braid word,
which corresponds with several generators multiplied together. Unframed braids
are multiplied together by joining the tops of the strands of the second braid to
the bottoms of the strands of the ﬁrst braid. Framed braids are multiplied in an
analogous way, however there are extra complications introduced by the presence
of twists. Therefore when forming the product of two (or more) framed braids,
we shall ﬁrstly join the bottom of the ribbons in the ﬁrst braid to the tops of
the ribbons in the second braid, and so on (in the case of braided belts, we must
eliminate the intervening nodes ﬁrst, while retaining the nodes at the “top” of
the ﬁrst belt in the product, and the “bottom” of the last belt). Secondly we
shall isotop the twists from each of the component braids upwards to render
the product into standard form (as described above). They will get permuted
in the process, according to the permutation PB associated with the braid B
that they pass through.
Given a permutation PB and a twist-word [x, y, z],
6
we shall write the permuted twist-word as PB ([x, y, z]). Thus given two braids
[r, s, t]B1 and [u, v, w]B2, we can form their product by joining strands to form
[r, s, t]B1[u, v, w]B2, and then move the twists [u, v, w] upward along the strands
of the braid B1. Thus
[r, s, t]B1[u, v, w]B2 = [r, s, t]PB1 ([u, v, w]) B1B2
(2)
where [r, s, t][x, y, z] = [r +x, s+y, t+z] and B1B2 denotes the usual product of
braid words. In general the twists will be permuted by all the braids they pass
through. For example, remembering that Pσi = Pi,(i+1),
[r, s, t]σ1σ2[x, y, z]
=
[r, s, t]σ1[x, z, y]σ2
=
[r, s, t][z, x, y]σ1σ2
=
[r + z, s + x, t + y]σ1σ2.
(3)
It should also be clear to the reader that since crossings can be exchanged for
twists, in the case of braided belts - which we shall be discussing exclusively from
this point onwards, we may go a step further and entirely eliminate the crossings
from a 3-braid. When we do so we uncross the strands (hence permuting them
by the permutation associated with the crossing being eliminated) and introduce
the twists indicated in eqn. (1). In general, this means that we iterate the process
[a1, a2, a3][b1, b2, b3]σiσj . . . σm →[a1 + b1, a2 + b2, a3 + b3]σiσj . . . σm
→Pσi([a1 + b1, a2 + b2, a3 + b3])[x, y, z]σj . . . σm
(4)
where [x, y, z] is the twist-word associated to σi (as listed in Eqn. 1, when i is
speciﬁed). We iterate this procedure until the braid word becomes the identity.
Hence continuing the example above, from Eqn. (3),
[r + z, s + x, t + y]σ1σ2
→
Pσ1([r + z, s + x, t + y])
1
2, 1
2, −1
2

σ2
→
[s + x, r + z, t + y]
1
2, 1
2, −1
2

σ2
→

s + x + 1
2, r + z + 1
2, t + y −1
2

σ2
→
Pσ2

s + x + 1
2, r + z + 1
2, t + y −1
2

×

−1
2, 1
2, 1
2

→

s + x + 1
2, t + y −1
2, r + z + 1
2

×

−1
2, 1
2, 1
2

→
[s + x, t + y, r + z + 1].
(5)
7
Figure 5: A Trip performed on a closed 3-Belt
We shall refer to the form of a braid in which all the crossings have been ex-
changed for twists as the pure twist form.
The list of three numbers which
characterise the twists on the strands in the pure twist form will be referred to
as the pure twist-word. The pure twist-word is of interest because it is a topo-
logical invariant (since it is obtained when a braid is reduced to a particularly
simple form i.e. all crossings removed).
