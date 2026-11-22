---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-041-a-further-comments-on-the-complexification-bound
section_title: "A Further comments on the complexification bound"
section_number: null
pages: 56-57
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
Further comments on the complexiﬁcation bound
If we want a notion of complexity such that local Hamiltonian evolution leads to com-
plexity growth linear in t and the number n of active degrees of freedom, then the
Hamiltonian should ﬁrst be normalized so that the energy is extensive in n. The com-
plexity can then be preliminarily deﬁned by a limiting procedure where we take the
gate set {Gα} to consist of elements which are close to the identity, Gα = I + iδHα,
with the Hα taken to be simple Hermitian operators. As δ →0 the number of gates
diverges as 1/δ, so the complexity may be deﬁned as
C ∝lim
δ→0 δNgates.
(A.1)
The above deﬁnition is roughly equivalent to saying the complexity is deﬁned as
an L1-norm (with a high penalty for nonsimple directions) of a tangent vector to
the manifold U(2n) of many-body unitaries.
Two comments are necessary.
First,
the limiting procedure is important because with a ﬁxed noninﬁnitesimal gate set the
number of gates grows like
t log( t
ϵ)
log(log( t
ϵ)), i.e. not quite linearly in t [70]. Second, our
deﬁnition is inspired by Nielsen’s complexity geometry [71] where the complexity grows
linearly in t. However, [71] uses an L2-norm so the complexity growth is proportional
to √n instead of n in that formulation.
We might further hope that the necessary notion of approximation and other details
in the deﬁnition of the complexity can be swept up into the overall prefactor which is
not ﬁxed by the considerations in this appendix. In the main text we assumed that the
prefactor could be chosen so that the stated complexity growth bound holds. While
not proven, this seems reasonable given that there are special information theoretic
properties [72] (such as concentration of eigenvalues) of ﬁeld theories with semiclassical
holographic duals.
A rough argument for the complexiﬁcation bound proceeds as follows. Decompose
e−iHt as
e−iHt = UHe−ihtU †
H
(A.2)
where UH is a unitary which maps from the energy basis to a tensor-product basis and
h is a diagonal matrix whose entries are the energy eigenvalues. Provided we only care
about energies up to roughly E = ⟨ψ|H|ψ⟩one can argue using adiabatic evolution that
55
the complexity of UH is of order eS where S is the microcanonical entropy at energy
E. From this perspective we may conceptualize the action of e−iHt as a dephasing
process in which the eS complexity of UH is slowly revealed as the diagonal term e−iht
increasingly inhibits the cancellation of UH and U †
H. Assuming the input state has
maximum energy E we would again expect the rate of “increasing failure to cancel” to
be bounded by E.
The above argument sketch has at least one major problem: it is violated by
“cat states”, that is by states which are superpositions of macroscopically diﬀerent
states. The simplest example contains a noncomputing branch and a rapidly comput-
ing branch,
|θ⟩= cos θ|0⟩+ sin θ|E⟩,
(A.3)
where |0⟩is the ground state and |E⟩is a highly excited state. If θ ≪1 then the
average energy of |θ⟩is approximately sin2 θE ≪E but the rate of complexiﬁcation of
|θ⟩is likely given by E (without any sin2 θ factor). This is an arbitrarily bad violation
of the complexity growth bound.
Another very serious objection comes from considering superpositions of multiple
computers. Suppose the system is a composite of i = 1, . . . , m computing systems and
suppose the Hamiltonian is H = P
i Hi where each Hi acts only on the ith computer.
Then a state of the form
|cat⟩=
1
√m
m
X
i=1
|0⟩1 . . . |E⟩i . . . |0⟩m
(A.4)
has average energy E but likely complexiﬁes at a rate mE. Again, we appear to have
an arbitrarily bad violation of the complexity growth bound.
However, both of these states correspond, on the gravity side, to superpositions of
black holes and ground states. Such energy cat states are certainly not semiclassical,
so it remains possible that among semiclassical states the complexity growth bound
could be obeyed. As for more general quantum computers, bearing in mind the “cat
computer” examples, it is at present unclear to us if there is any general bound on the
rate of computation.
