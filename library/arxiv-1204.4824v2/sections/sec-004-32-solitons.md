---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-004-32-solitons
section_title: "Solitons"
section_number: 3.2
pages: 14-15
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
In the presence of the canonical surface defect Sz, there is a second kind of BPS state in
the story: we can consider BPS particles which are bound to the defect and interpolate
between distinct vacua. We call these particles solitons.
As described in [5], BPS solitons are also realized geometrically in terms of ﬁnite webs
of strings. The main diﬀerence is that now we consider webs in which one of the strings
ends on the point z, which we call ﬁnite open webs . See Figure 3.
(12)
12
23 31
(31)
(12)
12
(12)
12
23
(23)
31
(12)
32
21
43
41
42
Figure 3. Some possible topologies for ﬁnite open webs of BPS strings, representing BPS solitons
on the surface defect Sz. Each ﬁnite open web includes one string that ends on the point z∈ C.
An orange cross with label (ij) denotes an (ij)-branch point.
LetN denote a ﬁnite open web. As for the pure 4d case, the charge of the corresponding
BPS soliton is determined by the topology of the web, as follows. Let NΣ denote the union
of the lifts of all strings in N to Σ. Suppose the string of N ending on z is an ij-string
oriented out of z. Let z(i) and z(j) be the preimages of z on the i-th and j-th sheets of Σ.
NΣ is a 1-chain with boundary:
∂NΣ =z(j)−z(i). (3.3)
We let Γij(z,z ) denote the set of relative homology classes on Σ obeying (3.3), and
Γ(z,z ) =∪i,jΓij(z,z ). (3.4)
Thus the charges [ NΣ] of BPS solitons on Sz are elements of Γ( z,z ), and in fact of the
smaller set∪i,j,i⁄=jΓij(z,z ).
The central charges of BPS solitons are given by a formula analogous to (3.2): for any
¯a∈ Γ(z,z ) we have9
Z¯a = 1
π
∫
¯a
λ. (3.5)
There is a BPS index µ(¯a)∈ Z which counts 2d-4d BPS states of charge ¯a, deﬁned as a
trace over the Hilbert space of 1-particle BPS states [37, 38],
µ(¯a) = TrH1,BPS
Sz,¯a
Fe iπF, (3.6)
9In [5] we denoted elements of Γ ij(z,z ) by γij, but we are now deprecating that notation in favor of ¯a.
See Appendix C for a summary of conventions.
– 12 –
whereF is a fermion number operator. In principle,µ(¯a) could be determined by quantizing
the zero modes of the BPS strings. In practice, as with Ω( γ), we will take a more indirect
route in this paper.
We hasten to warn the reader that there are two important subtleties in the deﬁnition
(3.6). The ﬁrst subtlety is addressed in §3.5: to deﬁne F properly we will need to keep
track of slightly more information about the 2d-4d BPS states, by extending the charge
¯a to a new “charge” denoted a. It will turn out that µ really depends on a, not ¯a. The
second subtlety is that the space of 1-particle BPS states is only well deﬁned when the
parameters are not on a wall of marginal stability. At these walls, µ(a) can jump. In
particular, if ¯a∈ Γ(z,z ), then generically, if we move z holding all other parameters ﬁxed,
and apply the natural parallel transport to the relative homology cycle ¯ a, µ(a) remains
constant. However, there are walls on C across which µ(a) jumps, and in this case we
will need to deﬁne limits µ±(a) as z approaches the wall from either side. This will be
important in§6.
