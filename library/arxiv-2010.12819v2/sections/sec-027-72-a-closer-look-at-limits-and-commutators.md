---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-027-72-a-closer-look-at-limits-and-commutators
section_title: "A closer look at limits and commutators"
section_number: 7.2
pages: 28-29
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
A priori, it looks like any product of Koo-Saleur generators might be strongly aﬀected by parasitic couplings.
We have, however, found serious evidence that only the central charge can come out wrong in calculations. In
particular we shall in this section consider commutators, and our belief is that the scaling limit of Koo-Saleur
commutators is the commutator of the scaling limit, except for the anomalous central charge term . This is
probably expected on general grounds. After all, the Virasoro algebra is just a mode reformulation of the
general stress-energy tensor OPE
T (z)T (w) = c
2(z−w)4 + 2T (w)
(z−w)2 + ∂T
z−w + reg. (115)
The second term is ﬁxed by the dimension of T (z), which—like for all conserved currents—is not renormalized,
and the third one by consistency under the exchange z↔w. Only the ﬁrst term is anomalous. Going back to
13This is an example of what is sometimes called “conditioned weak convergence”.
28
the original paper by Koo and Saleur [1], there were some initial checks of how the limit of [ H, P] behaves. In
this section we return to this question, exploring this kind of commutator in more detail. Our starting point is
KS (3.30), which leads to
[Lp+n + ¯L−p−n, L−p− ¯Lp] = 2
(N
2π
)2( γ
π sinγ
)3{
e2iπn/N sin
(3πp + 2πn
N
) N∑
j=1
e2iπnj/N [ej, [ej+1,ej+2]]
+e2iπn(1/2)/N sin
(πp +πn
N
) N∑
j=1
e2iπnj/N√
Q(ejej+1 +ej+1ej)− 2 sin
(πp
N
) N∑
j=1
e2iπnj/Nej
}
.
(116)
If we could exchange freely limits and commutators, the fact that Ln↦→ Ln (resp. ( ¯Ln↦→ ¯Ln) would imply
that the left-hand side of (116) converges to
[
Lp+n + ¯L−p−n,L−p− ¯Lp
]
= (2p +n)
(
Ln + ¯L−n
)
, for n⁄= 0, (117a)
[
Lp + ¯L−p,L−p− ¯Lp
]
= 2p
(
L0 + ¯L0− c
12
)
+p3c
6, for n = 0. (117b)
It is in fact known that (116) ↦→ (117) when x = 1 [22], or when x = 3 if one restricts to the Ising subspace of
the XXZ chain [1]. It is also known that (116) ⁄↦→ (117) for other values of x than these and the x = 2 case (see
KS (3.42)): our aim is to investigate in more detail what, exactly, fails.
General considerations
When studying the behaviour of (116) when acting on eigenstates of the lattice translation operator, it is
convenient to ﬁrst recall the discussion in Section 5.1, which yields two facts:
• Due to the relative phase e2iπnj/N , matrix elements of (116) between two states are only non-zero when
the lattice momentum p of the states diﬀers by precisely n.
• For such non-zero matrix elements, it suﬃces to evaluate a single summand, say at j = 0; the matrix
element corresponding to the entire sum is then obtained by multiplication with N.
We shall in the following use the word term to refer to the separate contributions for a single, ﬁxed value of j.
We note that any term that is constant will only contribute when considering matrix elements between a Bethe
state and itself, since the Bethe states form an orthonormal basis. In particular, this means that whenever
n⁄= 0 we can omit any constant terms, which will allow us to drop normal ordering symbols in the next section.
We note that by the deﬁnition in (22) ej will act on only two sites in the spin chain, and that the matrix
elements are given by q andeiφ/N—neither of which increases in norm asN→∞ . As such, the matrix elements
of a ﬁnite number of Temperley-Lieb generators can at most go towards a constant value as N→∞ . We shall
see that this occurs when matrix elements are between a state and itself—relevant for then = 0 case—while they
otherwise decrease with N. The numerical results for matrix elements between various states will be shown for
the generic example of x =π. Similar results were found for other generic and non-generic values of x. We shall
consider matrix elements where the various operators act on either the ground state or one of six low-energy
scaling states of various types—electric excitation, magnetic excitation, creating a “hole”, twisted boundary
conditions, and combinations of these. (One of these six excited states is excluded from certain ﬁgures, where
the matrix elements are exactly zero due to the indecomposability of W0,q±2.)
