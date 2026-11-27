---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-025-7-anomalies-and-the-convergence-of-the-koo-saleu
section_title: "Anomalies, and the convergence of the Koo-Saleur generators"
section_number: 7
pages: 27-28
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
The restriction to scaling states is crucial if one hopes to recover the Virasoro algebra relations (40) for the
generators Ln, obtained from the Temperley-Lieb algebra by the Koo-Saleur formulae (31). Otherwise—for
instance—since the Ln act on a ﬁnite-dimensional Hilbert space for N ﬁnite, we would necessarily have that
Tr [Ln, L−n] = 0 (by cyclicity of the trace), preventing the appearance of the central-charge “anomalous”
term in (40). The procedure to correct this is well known [54] in free-ﬁeld theory—e.g., for the Ising model or
the free boson—and involves ﬁrst restricting to excitations within a certain energy window, then calculating
commutators, and ﬁnally taking the limit where the energy window goes to inﬁnity.
In other words, the continuum limit of a commutator is not necessarily the commutator of the continuum
limit. The diﬀerence between these two objects arises because of what we will call “parasitic couplings”, that
is, couplings that converge to zero as N →∞ , but are non-zero at ﬁnite N. In computing, for instance, a
matrix element such as (112) we encounter, in principle, an inﬁnity of “unwanted terms” where L−2 acting on
|1⟩ couples weakly to, in particular, high-energy states, and L2 in turn couples these states back to ⟨1|. While
we expect each of these unwanted terms to vanish as N→∞ , it is in principle possible that their sum builds
up to a ﬁnite quantity [54,55].
This phenomenon was already observed by Koo and Saleur (KS 12) [1], whose observations are reproduced
and generalized in Figure 2. We have already discussed the evaluation of the corresponding matrix element
(112), by computing either full norms or projections (denoted “No cutoﬀ” and “Cutoﬀ” in the ﬁgure). Details
about precisely how the projected results were obtained will be given below, in section 7.1.
In KS (3.42) an analytical condition was given under which the central-charge term in (40) would be correctly
produced for the Ln generators, despite of the possibility of parasitic couplings. This condition turns out to
be satisﬁed precisely at the values x = 1, 2, 3, corresponding respectively to dense polymers, percolation and
the Ising model. Close inspection of ﬁgure 2 indeed reveals the perfect agreement between full norms and
projections for x = 1, 2, 3 (note that c = 0 at x = 2)—however, the agreement is not exact in-between these
integers, e.g., at x = 2.5.
12We henceforth refer to equation (x.y) of Koo and Saleur [1] in the form KS (x.y).
27
Although the non-generic cases of x integer are not within the scope of the present paper, we here make an
exception to brieﬂy comment on the fact that the exact results found in KS can be seen to match our knowledge
about the aﬃne TL modules W0,q±2 at x = 1, 2, 3. For instance, at x = 3 we observe numerically that there is
only one state V at the correct lattice momentum such that both ⟨V|ei|1⟩ and⟨1|ei|V⟩ are non-zero, while at,
e.g.,x = 4 there are several. At x generic, the number of such states is observed to be equal to the dimension of
the relevant momentum sector of W0,q±2, as it should. A more clear-cut example occurs at x = 2 (i.e., c = 0),
where the identity|1⟩ is the only state in the [0, q2] module (in that case, a simple Jones-Temperley-Lieb module
of dimension 1), so there clearly is nothing at level 2 to couple to at all. As a consequence, the determination
of c by the study of the matrix element (112) is exactly zero for any ﬁnite size N. Clearly there is much more
to be said about these non-generic cases, and this will be the subject of a separate publication [27].
