---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-042-a1-comments-on-hamiltonian-locality-and-gate-sim
section_title: "A.1 Comments on Hamiltonian locality and gate simplicity"
section_number: null
pages: 57-59
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
Comments on Hamiltonian locality and gate simplicity
In the previous section, it was mentioned that the elements of the gate set {Gα} are
taken to be close to the identity Gα = I + iδHα, with the Hα taken to be simple
Hermitian operators. Here, we will elaborate a bit on what is meant by simple in this
context, and whether it is reasonable to have a bound on complexity.18
18We thank Douglas Stanford for questions and discussions leading to the creation of this section.
56
An individual Hα will be a product of operators at neighboring points, with the
number of such operators deﬁning the size or weight of the Hα. We will call a gate set
k-local if all elements of {Hα} have a size less than or equal to k. When we say that
the Hα should be simple, what we mean is that k should be small.
In this paper, we are mostly interested in estimating the complexity of Hamiltonian
time evolution. Thus, our gate set should be adept at approximating U(t) = e−iHt.
In the limit of small δ, we can suggestively write a gate as Gα = eiδHα. This suggests
a reasonable choice for the {Hα} could be the individual terms in the Hamiltonian.
Certainly this makes it clear how this gate set can approximate Hamiltonian time
evolution.
Even with a more general gate set, this also suggests a reasonable value for k. If the
Hamiltonian is k-local, then we should at least choose a gate set that is also only k-local.
There’s some reasonable intuition behind this: a Hamiltonian with locality k means
that interactions are roughly spread over at most k degrees of freedom. Presumably
in a circuit approximation of Hamiltonian evolution, one should only be able to use
gates that mix together at most k degrees of freedom per gate. However, by measuring
the complexity with a gate set that either depends directly on the H (by explicitly
choosing the Hα to be the terms in H) or by picking the k-locality of the Hα to equal
the k-locality of the Hamiltonian, we see that the complexity C will be a function of
both the Hamiltonian and the state. By changing the properties of H, we have to
change the way in which we measure C.19
Instead, let’s consider the more general case, where we choose a j-local gate set,
but have a k-local Hamiltonian. In that case, C has the desirable property of being a
function of j and the state |ψ⟩, but no longer a function of H. Now, it’s easy to see
that the bound discussed in this paper
dC
dt ≤2
πℏ⟨ψ|H|ψ⟩,
(A.5)
cannot hold without modiﬁcation. As a simple example, consider the case of k ≫j.
(For instance if the system has N degrees of freedom, H is a random 2N ×2N Hermitian
matrix, and j is O(1).) For k ∼N, a small amount of time evolution will lead to near
exponential complexity as measured by the j-local gate set and violate the bound.
Therefore, we need to consider the dependence on both j and k explicitly
dC
dt ≤g(k)
f(j)
2
πℏ⟨ψ|H|ψ⟩,
(A.6)
where the monotonically increasing functions f(j), g(k) capture the dependence of
the complexity on the locality of the gate set and the Hamiltonian.
A reasonable
19In particular, we thank Douglas Stanford for emphasizing this point.
57
assumption is that these are the same functions of their argument (since they’re trying
to account for the same type of dependence). Thus, for the natural choice discussed
above j = k, these factors cancel, and Eq. A.6 reduces to Eq. A.5.
For the case
considered previously k ≫j, we see that the bound becomes harder and harder to
violate, compensating for the large increase of complexity under time evolution as
measured by the j-local gate set. In the other limit of k ≪j, the rate of complexity
growth is vanishing. This is because the gate set is so large that the reference system
is never more than O(1) gates away from the time-evolved state; the complexity will
always stay small.
A comment on the relevance of the ground state
The complexiﬁcation bound we propose has the unusual property of depending on the
energy of the ground state of the Hamiltonian H. Given the ground state, |0⟩, and a
state of interest, |ψ⟩, one might think that it could be possible to change the energy
of the ground state ⟨0|H|0⟩without altering the complexodynamics of ⟨ψ|H|ψ⟩. By
arbitrarily lowering the ground state, it appears we could make the diﬀerence ⟨ψ|H|ψ⟩−
⟨0|H|0⟩arbitrarily large.
Let’s explore this idea a bit further. We can lower the ground state by an amount
∆> 0 by adding a term to the Hamiltonian
H′ = H −∆|0⟩⟨0|.
(A.7)
The ground state of the perturbed Hamiltonian H′ has ground state energy ⟨0|H|0⟩−
∆< ⟨0|H|0⟩. Additionally, if the ground state has negligible support on |ψ⟩such that
⟨0|ψ⟩≪1, then the complexodynamics remain unchanged ⟨ψ|H′|ψ⟩≈⟨ψ|H|ψ⟩. This
appears to let us shift the complexiﬁcation bound by an arbitrary amount. However,
the catch is that the ground state projector |0⟩⟨0| is a high-weight operator of O(N)
and will destroy the locality of the Hamiltonian.
If instead we take ∆< 0 and try to make the complexiﬁcation bound tighter, the
ground state will quickly cross the gap and become an excited state. Since the gap is
O(N −1), this would only be a 1/N correction to the bound.
