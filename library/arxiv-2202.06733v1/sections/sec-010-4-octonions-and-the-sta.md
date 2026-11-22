---
doc_id: arxiv-2202.06733v1
doc_title: "Received <day> <Month>, <year>"
section_id: sec-010-4-octonions-and-the-sta
section_title: "Octonions and the STA"
section_number: 4
pages: 8-9
source_pdf: 2202.06733v1.pdf
source_sha256: e670632090447f14
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 1.0
doc_brief: "Received <day> <Month>, <year> — Diﬀerent ways of representing the group 푆푈(3) within a Geometric Algebra approach are explored."
---
There are still several further aspects that are relevant for representing the $SU(3)$ aspect of strong forces, and in particular something we have not discussed here is that the $\psi=\psi(B)$ recipe for allowing the spacetime Dirac wavefunction to respond to the internal colour forces needs to be `self-dual', i.e.\ we need $\psi(IB)=I\psi(B)$, where $I$ is the spacetime pseudoscalar. Nevertheless, it seems very likely overall that what we need can be done wholly with STA entities. 
However, such an approach deals only with one generation of particles and only with $SU(3)$ and not the other groups involved in the standard model (SM). What do we need to do to enlarge the opportunities for representing particles and forces in the SM, whilst still staying in the STA?

A clue to this comes from an increase of interest over the last few years in how {\em Octonions} could be relevant to the Standard Model. Octonions are of general interest mathematically of course, but to most people seem rather mysterious. What we wish to do here is show how they can be instantiated quite simply in the STA. This has the double benefit of making them more accessible to a lot of people (e.g.\ they can then be computed with mathematically by anyone who has access to a program able to do the STA), and also provide a new approach to using octonions in the SM, as we will see.

The octonions were first introduced as a generalisation of quaternions, by Graves in 1843 and Cayley in 1845. (The first actual paper by Graves concerning them\cite{graves1845xlvi} was published shortly after Cayley's paper\cite{cayley1845xxviii}, in 1845.) They are commonly written as 8 `units', $e_0$, $e_1$, \ldots , $e_7$, with 

\be
e_0^2=1, \quad e_i^2=-1, \quad i=1,\ldots,7
\ee

Their key feature is that they form a `normed division algebra'. Any product of octonions has a norm which is the product of the individual norms, and two non-zero octonions always multiply to produce a further non-zero octonion. As is well known, the only normed division algebras are the real numbers, complex numbers, quaternions and octonions. Among these, the complex numbers are commutative and associative, the quaternions are non-commutative but still associative, while famously the octonions are neither commutative nor associative. The doubling process which can produce a higher grade algebra from a lower one (e.g.\ the complex numbers from the reals, or the quaternions from the complex numbers), is formalised in the {\em Cayley-Dickson construction}\cite{dickson1919quaternions}. If we attempt to apply this process to the octonions themselves, we get a 16 dimensional algebra called the Sedenions, but this fails to be a normed division algebra since it contains non-zero elements which when multiplied together produce 0. The Sedenions may still be useful in particle physics, however, see e.g.\ \cite{masi2021exceptional}.

We now discuss how we can represent octonions in the STA.The key is that (in the STA) the Dirac spinors $\psi$ can be divided into parts that commute or anticommute with the unit timelike vector $\gamma_0$, and we can use these two parts (the `Pauli' and `non-Pauli' parts of the Dirac spinor), in a Cayley-Dickson type doubling procedure in a way which defines the octonionic product of two Dirac spinors in terms of these sub-parts.

An STA spinor has 8 real degrees of freedom, so we are able to identify an octonion directly with a spinor. For an `octonion' $\psi$, we define

\be
\psi_+ = \half\left(\psi + \go \psi \go\right), \quad \psi_- = \half\left(\psi -\go \psi \go\right)
\ee

as the two sub-parts of $\psi$. These will correspond to the even and odd parts of the full 3d Pauli algebra, in the usual `spacetime split' correspondence between the Pauli and Dirac geometric algebras, given by multiplication by $\gamma_0$. (See the discussion concerning Fig.~\ref{fig:sta-split} below.)

Then given two octonions, $\psi$ and $\phi$, the octonionic product between them, which we will denote `$\star$', is the Dirac spinor $\theta$ given by

\be
\boxed{
\theta=\psi \star \phi = \psi_+\phi_++\phirev_-\psi_-+\phi_-\psi_++\psi_-\phirev_+
}
\label{eqn:oct-prod}
\ee

\medskip

\noindent (We have put a box around this equation, since it is a central result of this paper.) Note carefully that the four individual products on the right hand side of this equation are all usual {\em geometric products} taking place within the ordinary STA, and the spinors involved are just ordinary STA spinors, hence our claim about being able to compute everything entirely within the STA. 

From the form of this we can see that such a product is highly unlikely to be associative, and indeed in general it is not. The property it {\em does} have, however, comes from the (essentially) defining property of the octonions, already discussed, that they form a {\em normed division algebra}.

To define the norm, we need to define a \alert{conjugate} element. For us this is (using $^*$ to denote conjugation)

\be
\boxed{
\psi^*=\psirev_+-\psi_-
}
\label{eqn:conj-def}
\ee

where the tilde over the first term on the r.h.s.\ denotes the usual GA reversion.

This yields the following norm:

\be
\boxed{
||\psi|| \equiv \psi \star  \psi^* = \half\left(\go\psi\go\psirev+\psi\go\psirev\go\right) = J\dt\go
}
\label{eqn:norm-res}
\ee

where $J=\psi\go\psirev$ is the Dirac current! (We have put boxes around the last two equations, since they are also central results of this paper.)

We know from its interpretation as a probability current, that $J$ is always non-zero and future pointing as long as $\psi$ is non-zero. This, along with its scalar nature (in the sense of grades present) coincides perfectly with properties a norm should have.

The other property we need for our product and norm to be representing a normed division algebra is the fundamental relation that the norm respects multiplication, so we require

\be
||\psi\star\phi || = ||\psi|| \, ||\phi||
\ee

for \alert{all} Dirac spinors $\psi$ and $\phi$. Given our definitions so far, this is a matter of computation, and one can find that this does indeed work. Moreover, given our reinterpretation of the octonionic norm in terms of the Dirac current, we see that with $\theta=\psi \star \phi$ it corresponds to the (ordinary STA) result

\be
||\theta||=\left(\theta \go \tilde{\theta}\right)\dt\go = \left[ \left(\psi \go \tilde{\psi}\right)\dt\go \right] \left[ \left(\phi \go \tilde{\phi}\right)\dt\go \right]
\ee

(Note the square brackets are just to separate out the two scalar quantities on the r.h.s.) It is worth noting that it is the requirement for this property which means that taking just the ordinary Clifford product between spinors in e.g.\ the STA, or Euclidean $Cl(4,0)$, does not work in terms of providing a representation of octonionic multiplication. This is because in this case we can have non-zero states with zero norm, or which multiply together to give the zero state. For example, in the STA the states $\half(1+\sigma_3)$ and $\half(1-\sigma_3)$ are clearly non-zero, but multiply together, under ordinary GA multiplication, to give 0, whilst in Euclidean $Cl(4,0)$ the states $\half(1+I)$  and $\half(1-I)$ have the same problem, which as discussed in \cite{lasenby20201d} is relevant to (necessarily) false claims to have found an associative version of the Octonions\cite{christian2018quantum}.
