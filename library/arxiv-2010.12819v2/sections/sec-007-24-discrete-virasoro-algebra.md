---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-007-24-discrete-virasoro-algebra
section_title: "Discrete Virasoro algebra"
section_number: 2.4
pages: 10-11
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
Following (15) we deﬁne the Hamiltonian density as hj =− γ
π sinγej, from which we may construct a lattice
momentum density pj =i[hj, hj−1] = −i
( γ
π sinγ
)2
[ej−1,ej] by using energy conservation [3]. We then deﬁne
the corresponding momentum operator P as
P =−i
( γ
π sinγ
)2 N∑
j=1
[ej,ej+1]. (29)
From the densities hj and pj we may build components of a discretized stress tensor as
Tj = 1
2(hj + pj), (30a)
¯Tj = 1
2(hj− pj), (30b)
and use those to construct discretized versions of the Virasoro generators in the form of Fourier modes [3]. This
construction leads to the Koo-Saleur generators 5
Ln[N] = N
4π

− γ
π sinγ
N∑
j=1
einj2π/N
(
ej−e∞ + iγ
π sinγ [ej,ej+1]
)
 + c
24δn,0, (31a)
¯Ln[N] = N
4π

− γ
π sinγ
N∑
j=1
e−inj2π/N
(
ej−e∞− iγ
π sinγ [ej,ej+1]
)
 + c
24δn,0. (31b)
4Of course, the co-standard module would be formally obtained by reversing the arrows, which corresponds formally to prop-
agating “towards the past”, or acting with the transpose of the transfer matrix to build partition and correlation functions. It is
not clear what this means physically.
5In the present paper we consistently use calligraphic fonts for the lattice analogs of some key quantities: the HamiltonianH, the
momentum P—with their corresponding densities hj and pj—, the Virasoro generators Ln, ¯Ln and the stress-energy tensor T,
¯T. We denote the corresponding continuum quantities by Roman fonts: H,P andLn, ¯Ln, as well as T , ¯T . One of the paramount
questions is of course whether we have the convergence Ln, ¯Ln↦→ Ln, ¯Ln in the continuum limit N→∞ —and if we do, what
precisely is the nature of this convergence.
10
ﬁrst derived by other means in [1]. The crucial additional ingredient in these formulae is the central charge,
given by
c = 1− 6
x(x + 1), (32)
where we remind of the parametrisation (1). This choice (32) is known to apply to models with Hamiltonian
(15), such as the ferromagnetic Q-state Potts model with Q = m2. Note, however, that the identiﬁcation (32)
is actually a rather subtle question, since it may be aﬀected by boundary conditions. We discuss this aspect in
details in the next section, with some further discussion in Appendix G.
