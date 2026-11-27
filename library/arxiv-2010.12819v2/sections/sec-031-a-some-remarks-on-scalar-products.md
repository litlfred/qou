---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-031-a-some-remarks-on-scalar-products
section_title: "A Some remarks on scalar products"
section_number: null
pages: 36-38
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
It is interesting to discuss in more detail why the conformal scalar product (the one corresponding to the
conjugationL‡
n =L−n) is the one relevant for the calculation of correlation functions in the operator formalism,
and, in our case, is the one obtained by “treating q as a formal variable”. Due to the exploratory nature of this
36
Appendix, we shall use here the standard bra-ket notation ⟨−|−⟩, although the conformal scalar product will
eventually be denoted by (−,−) in the main text.
We start by discussing a simple example. Consider a very simple system of two spins 1 /2 coupled via the
Uqsl(2) invariant Hamiltonian, which reads (up to an irrelevant scalar factor)
H =−e =−


0 0 0 0
0 q−1 −1 0
0 −1 q 0
0 0 0 0

 (139)
in the basis{++, +−,−+,−−}. When q is real, the normalized ground state is given by
|Ω⟩ = 1√
q + q−1
(q−1/2| +−⟩− q1/2|− +⟩). (140)
When q is a complex number of modulus one—the case we are considering here— H is not hermitian . The
ground state|Ω⟩ as we have written here is not normalized any more, since its norm square obtained with the
usual scalar product is 2
q+q−1 .
However, since the eigenvalues (0, q + q−1) are real, we see that from
H†|EL⟩ =E|EL⟩ (141)
we get the left-eigenvalue problem
⟨EL|H =E⟨EL| (142)
to be compared with the right-eigenvalue problem initially considered
H|ER⟩ =E|ER⟩. (143)
In our case we have (where the unprimed states correspond to the singlet, i.e., the ground state, while the
primed states correspond to the triplet)
|ER⟩ = 1√
q + q−1
(
q−1/2| +−⟩− q1/2|− +⟩
)
, (144a)
|E′
R⟩ = 1√
q + q−1
(
q1/2| +−⟩ + q−1/2|− +⟩
)
, (144b)
and
|EL⟩ = 1√
q + q−1
(
q1/2| +−⟩− q−1/2|− +⟩
)
, (145)
|E′
L⟩ = 1√
q + q−1
(
q−1/2| +−⟩ + q1/2|− +⟩
)
, (146)
where we chose normalizations such that left and right eigenstates are orthonormal,
⟨EL|ER⟩ =⟨E′
L|E′
R⟩ = 1, ⟨EL|E′
R⟩ =⟨E′
L|ER⟩ = 0, (147)
and⟨−|−⟩ stands for the ordinary scalar product. We see now that |Ω⟩ remains properly normalized with these
conventions. Moreover, conjugating and switching L for R amounts to treating q as a formal parameter, by
which we mean that it does not undergo any complex conjugation in the process. We thus see that considering
scalar products of the form⟨EL|ER⟩ (with left and right eigenstates properly distinguished), instead of⟨ER|ER⟩
(with no such distinction), amounts to treating H as self-conjugate, i.e., q as a formal parameter indeed.
The second point is to establish what this has to do with physics. We start by demanding that calculations
in our quantum (ﬁeld theory or not) formalism describe well-deﬁned objects in two-dimensional statistical
physics. The mapping of the quantum system onto a statistical mechanics one proceeds via an imaginary-time
representation, which can be depicted by taking the direction of imaginary time to be upwards. The density
operator ρ introduces a horizontal cut in this time evolution, in the sense that its matrix elements ρxy are such
that x (resp. y) refers to the degrees of freedom on the lower (resp. upper) lip of this cut. We now argue that
one may write the density operator as ρ =|0R⟩⟨0L|, that is, in terms of the left and right ground states. Indeed,
its matrix elements are of the form
ρxy∝⟨ +∞|e−τH|y⟩⟨x|e−τH|−∞⟩ ,
37
where⟨+∞| and|−∞⟩ denote “generic states” (initial conditions that are not orthogonal to the left and right
ground states, respectively) introduced at imaginary times ±∞, that is, at the bottom and top of the time
evolution. Taking τ large projects onto the lowest-energy eigenstates of H for the bottom part and H† for the
top part, so
ρxy∝⟨ 0L|y⟩⟨x|0R⟩.
With proper normalizationsand it is therefore justiﬁed to write ρ =|0R⟩⟨0L|, as claimed. Correlation functions
in the quantum theory are then obtained by tracing ρ with various insertions, and thus correspond to
⟨0L|···| 0R⟩, (148)
with⟨−|−⟩ denoting the ordinary scalar product.
In CFT, we demand that
⟨φ| =|φ⟩†, (149)
which leads to (on the surface where ¯z =z∗, the complex conjugate)
[φ(z, ¯z)]†≡ ¯z−2hz−2¯hφ(1/¯z, 1/z), (150)
so that
⟨φ|φ⟩ = lim z,¯z,w, ¯w→0⟨0|φ(z, ¯z)†φ(w, ¯w)|0⟩
= lim ξ,¯ξ→∞ ¯ξ2hξ2¯h⟨0|φ(¯ξ,ξ )φ(0, 0)|0⟩
= 1 , (151)
where in the last step we would generally obtain the residue of the two-point function, if the latter were not
normalized. Using this for T (z) leads immediately to L†
n =L−n. In general, we see that this dagger operation
is the one that exchanges left and right eigenstates in the non-Hermitian case.
This conformal scalar product is the continuum limit of the loop scalar product, or the sl(2|1)-invariant
scalar product as well. It is not, in general, positive deﬁnite. As already mentioned, it will be denoted ( −,−)
in the main text.
