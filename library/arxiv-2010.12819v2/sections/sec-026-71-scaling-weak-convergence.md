---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-026-71-scaling-weak-convergence
section_title: "``Scaling-weak'' convergence"
section_number: 7.1
pages: 28-28
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
The precise mathematical status of the convergence of the Koo-Saleur generators to the Virasoro generators
is clearly a problem beyond the scope of this article. A very conservative statement, which we believe to hold
true, is that 1) matrix elements of lattice Virasoro generators converge, when evaluated between scaling states,
to their expected continuum limit and 2) matrix elements of products of lattice Virasoro generators converge,
when evaluated between scaling states, to their expected continuum limit when the products are calculated
using only such intermediate states which are scaling states, and using a double-limit procedure. While the
meaning of statement 1) is obvious, the meaning of 2) will be explained in more detail below. We remind the
reader that a sequencefn in a Hilbert space is said to converge weakly tof, if the inner products⟨fn|g⟩ converge
to⟨f|g⟩ for all states g in the space. Accordingly we shall refer to the above phenomenon as scaling-weak
convergence.13 It is indeed a weak convergence, as the statement is only for matrix elements, but it is weaker
than what is usually called weak convergence because of the restriction to scaling states, in particular in the
intermediate states encountered when forming products of operators. In practice, this scaling-weak convergence
can be implemented by the double limit procedure familiar to physicists, as discussed already in [1]. We can
illustrate it more technically by writing some simple equations.
As we saw in Figure 2, computing ⟨1|L2L−2|1⟩ via the full norm (“No cutoﬀ”) of the matrix element does
not quite give the conjectured result c
2. We can write
⟨1|L2L−2|1⟩ =
S∑
j=1
⟨1|L2|v(j)⟩⟨v(j)|L−2|1⟩, (113)
where S denotes the number of states (in the relevant momentum sector). We see that even if matrix elements
of single Koo-Saleur generators converge towards those of the Virasoro generators, this does not guarantee weak
convergence overall. As discussed at the end of Section 5.2, even if each parasitic matrix element ⟨v(j)|L−2|1⟩
in (113) converges to zero as N→∞ , the simultaneous rapid growth of S can destroy the convergence of the
product of generators. To deal with this issue we can consider some ﬁxed cutoﬀ,
Smax∑
j=1
⟨1|L2|v(j)⟩⟨v(j)|L−2|1⟩ (114)
(where the intermediate states are supposed to be conveniently ordered), sending the cutoﬀ Smax→∞ after
taking the scaling limit N→∞ . The right-hand side of Figure 2 illustrates the most extreme cutoﬀ, where we
do not include any parasitic matrix elements at all, that is to say, “Cutoﬀ” means that the intermediate states
are just the Smax = 2 states existing at chiral level 2.
