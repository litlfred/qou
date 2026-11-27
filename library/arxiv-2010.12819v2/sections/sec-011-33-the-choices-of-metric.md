---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-011-33-the-choices-of-metric
section_title: "The choices of metric"
section_number: 3.3
pages: 15-16
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
We have just recovered the well-known result that the continuum limit of the XXZ spin chain is made up of
sectors of a twisted free-boson theory. The space of states in the continuum limit can be built out of vertex-
operator states Vα =:eiαϕ: (in this section we shall only consider the chiral part for notational brevity) and
derivatives∂ϕ,∂ 2ϕ, (∂ϕ)2,... .
From the free-boson current J(z) = 1
4∂zϕ, we deﬁne an as its modes, such that we have the Heisenberg
algebra
[an,am] =nδn+m,0. (71)
We can then equivalently consider the state space to be built from states of the form
(a−n1)N1··· (a−nk)NkVα. (72)
The vertex operator Vα is a highest-weight state for the Heisenberg algebra, with
anVα = 0 , ∀n> 0, (73a)
a0Vα =
√
2(α−α0)Vα. (73b)
In terms of an we have for the twisted boson theory
Ln =
∞∑
k=0
an−kak−
√
2α0nan, for n⁄= 0, (74a)
L0 =
∞∑
k=1
a−kak + 1
2a2
0−α2
0 (74b)
15
for which the Virasoro algebra relations (40) are readily shown to be satisﬁed with
c = 1− 24α2
0. (75)
Two possible scalar products can be introduced in the CFT. The one for which a†
n =a−n, denoted in what
follows by⟨−,−⟩, is positive deﬁnite and corresponds to the usual positive deﬁnite scalar product for the spin
chain, where the conjugation sending a ket to a bra is anti-linear. A crucial observation is that for this scalar
product L†
n⁄= L−n. This means that norm squares of descendants cannot be obtained using Virasoro algebra
commutation relations. Also, this scalar product must be used with great care when calculating correlation
functions; this point is discussed more in appendix A. Instead of using the Virasoro relations directly we shall
use the Heisenberg relations (71).
We shall in the following sections, especially when comparing to the numerical results, refer to theconjectured
values of various norms. What we refer to is then the value we obtain by considering the states to be given asVα
withα as in (66), writing any Virasoro generator in terms of an using (74), using the Heisenberg commutation
relations (71) to move an with n> 0 to the right and ﬁnally applying the highest-weight relation (73).
The second scalar product is denoted ( −,−) and corresponds to the conjugation ‡. Compared to the
conjugation†, where we write Ln in terms of an as in (74) and use a†
n = a−n to deﬁne the conjugate L†
n,
we instead deﬁne the conjugate L‡
n as simply L‡
n = L−n. This “conformal scalar product” ( −,−) is known
to correspond [9–11], on the lattice, to the “loop scalar product” deﬁned through the Markov trace, or to a
modiﬁed scalar product in the XXZ spin chain where q is treated as a formal, self-conjugate parameter [45].
It is not a positive deﬁnite scalar product, and we will not use it much here, as our main goal is to establish
whether various quantities are zero or not.
Of course, the relationship between the two scalar products is a question of great interest: for some recent
results about this, see [46].
