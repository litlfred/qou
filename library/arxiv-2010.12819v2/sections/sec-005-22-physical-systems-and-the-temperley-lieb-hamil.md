---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-005-22-physical-systems-and-the-temperley-lieb-hamil
section_title: "Physical systems and the Temperley-Lieb Hamiltonian"
section_number: 2.2
pages: 8-9
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
Following the original work in [1] we now consider systems with Hamiltonians
H =− γ
π sinγ
N∑
j=1
(ej−e∞). (15)
Here, the prefactor is chosen to ensure relativistic invariance at low energy (see the next section), and we recall
that γ∈ [0,π ] is deﬁned through q =eiγ, so m∈ [−2, 2]. e∞ is a constant energy density added to cancel out
extensive contributions to the ground state. Its value (as discussed below) is given by
e∞ = sinγI 0, (16)
with I0 being given by the integral
I0 =
∫ ∞
−∞
sinh(π−γ)t
sinh(πt) cosh(γt)dt. (17)
In (15), the ej can be taken to act in diﬀerent representations of the Ta
N(m) algebra.
We will consider in this paper the XXZ representation, in which the ej act on CN with
ej =−σ−
j σ+
j+1−σ+
j σ−
j+1− cosγ
2 σz
jσz
j+1− i sinγ
2 (σz
j−σz
j+1) + cosγ
2 , (18)
where the σj are the usual Pauli matrices, so the Hamiltonian is the familiar XXZ spin chain
H = γ
2π sinγ
N∑
j=1
[
σx
jσx
j+1 +σy
jσy
j+1 + ∆(σz
jσz
j+1− 1) + 2e∞
]
(19)
with anisotropy parameter
∆ = cosγ. (20)
In the usual basis where [ 1
0 ] corresponds to spin up in the z-direction at a given site, the Temperley-Lieb
generator ej acts on spins j,j + 1 (with periodic boundary conditions) as
ej =···⊗ 1⊗


0 0 0 0
0 q−1 −1 0
0 −1 q 0
0 0 0 0

⊗ 1⊗··· . (21)
It is also possible to introduce a twist in the spin chain without changing the expression (15), by modifying
the expression of the Temperley-Lieb generator acting between ﬁrst and last spin with a twist parametrized by
φ. In terms of the Pauli matrices, this twist imposes the boundary conditions σz
N+1 =σz
1 and σ±
N+1 =e∓iφσ±
1 .
For technical reasons, we will later on “smear out” the twist by taking φ/N for each Temperley Lieb generator:
ej =···⊗ 1⊗


0 0 0 0
0 q−1 −eiφ/N 0
0 −e−iφ/N q 0
0 0 0 0

⊗ 1⊗··· . (22)
This is equivalent, and is done in order to preserve invariance under the usual translation operator, which will be
useful in the sections below. Note that the value of the energy density e∞ is independent ofφ and remains given
by (16). In the generic case, the XXZ model with magnetization Sz =j and twisteiφ provides a representation
of the module Wj,eiφ. This is not true in the non-generic case—see below.
Instead of the XXZ representation, one could also consider the so-called loop representation, which is simply
the representation in terms of aﬃne diagrams introduced in section 2.1, or equivalently in terms of the corre-
sponding link states. This loop representation is useful for describing geometrical problems such as percolation
or dense polymers. It is also strictly equivalent to the cluster representation familiar from the study of the Q-
state Potts model with Q = m2 [19]. Other representations are possible—such as the one involving alternating
3, ¯3 representations of sl(2|1) discussed in [28] to study percolation.
There are many common features of the XXZ and the loop representations. In particular, they have the same
ground-state energy and the same “velocity of sound” determining the correct multiplicative normalization of
the Hamiltonian in (15). This reason is that the ground state is found in the same moduleWj,eiφ for both models,
or in closely related modules for which the extensive part of the ground-state energy (and hence the constant
e∞) is identical. However, the XXZ and loop representations generally involve mostly diﬀerent modules. The
8
modules appearing in the XXZ chain depend on the twist angle φ, while for the loop model the modules depend
on the rules one wishes to adopt to treat non-contractible loops, or lines winding around the system. For a
generic and non-degenerate situation, studying the physics in each irreducible module Wj,eiφ would suﬃce to
answer all questions about all Ta
N(m) models as well as the related Virasoro modules obtained in the scaling
limit. But it turns out, importantly, that degenerate cases are always of relevance to the problems at hand. In
such cases, a crucial issue that we will be interested in is how the modules “break up” or “get glued”. This
issue is highly model-dependent, and is central to the understanding of logarithmic CFT in particular.
The loop representation is studied in [2], with a main focus on the continuum limit of the various standard
modules and the build-up of indecomposable structures. Meanwhile, this paper will focus instead on the XXZ
spin chain representation. One goal will be to again establish the continuum limit of standard modules—which
will turn out diﬀerent than in the loop case—and another will be to investigate more closely the nature of the
convergence of Koo-Saleur generators towards the Virasoro generators. An important point is that the diﬀerence
between the loop and XXZ spin chain representations is manifest already at the smallest possible ﬁnite size. To
see this, we start by a detailed discussion of the module W0,q±2 at N = 2 sites.
