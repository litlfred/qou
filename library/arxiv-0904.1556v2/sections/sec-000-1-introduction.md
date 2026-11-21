---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 1.0
doc_brief: "The Algebra of Grand Uniﬁed Theories — The Standard Model is the best tested and most widely accepted theory of elementary particles we have today."
---
[]{#sec:introduction label="sec:introduction"}

The Standard Model of particle physics is one of the greatest triumphs of physics. This theory is our best attempt to describe all the particles and all the forces of nature\... *except* gravity. It does a great job of fitting experiments we can do in the lab. But physicists are dissatisfied with it. There are three main reasons. First, it leaves out gravity: that force is described by Einstein's theory of general relativity, which has not yet been reconciled with the Standard Model. Second, astronomical observations suggest that there may be forms of matter not covered by the Standard Model---most notably, 'dark matter'. And third, the Standard Model is complicated and seemingly arbitrary. This goes against the cherished notion that the laws of nature, when deeply understood, are simple and beautiful.

For the modern theoretical physicist, looking beyond the Standard Model has been an endeavor both exciting and frustrating. Most modern attempts are based on string theory. There are also other interesting approaches, such as loop quantum gravity and theories based on noncommutative geometry. But back in the mid 1970's, before any of the currently popular approaches rose to prominence, physicists pursued a program called 'grand unification'. This sought to unify the forces and particles of the Standard Model using the mathematics of Lie groups, Lie algebras, and their representations. Ideas from this era remain influential, because grand unification is still one of the most fascinating attempts to find order and beauty lurking within the Standard Model.

This paper is a gentle introduction to the group representations that describe particles in the Standard Model and the most famous grand unified theories. To make the material more approachable for mathematicians, we limit our scope by not discussing particle interactions or 'symmetry breaking'---the way a theory with a large symmetry group can mimic one with a smaller group at low energies. These topics lie at the very heart of particle physics. But by omitting them, we can focus on ideas from algebra that many mathematicians will find familiar, while introducing the unfamiliar ways that physicists use these ideas.

In fact, the essential simplicity of the representation theory involved in the Standard Model and grand unified theories is quite striking. The usual textbook approach to particle physics proceeds through quantum field theory and gauge theory. While these subjects are very important to modern mathematics, learning them is a major undertaking. We have chosen to focus on the algebra of grand unified theories because many mathematicians have the prerequisites to understand it with only a little work.

A full-fledged treatment of particle physics requires quantum field theory, which uses representations of a noncompact Lie group called the Poincaré group on *infinite-dimensional* Hilbert spaces. This brings in a lot of analytical subtleties, which make it hard to formulate theories of particle physics in a mathematically rigorous way. In fact, no one has yet succeeded in doing this for the Standard Model. But by neglecting the all-important topic of particle interactions, we can restrict attention to *finite-dimensional* Hilbert spaces: that is, finite-dimensional complex inner product spaces. This makes our discussion purely algebraic in flavor.

Every theory we consider has an 'internal symmetry group' or 'gauge group'. This is a compact Lie group, say $G$. Particles then live in representations of $G$ on a finite-dimensional Hilbert space $V$. More precisely: $V$ can always be decomposed as a direct sum of irreducible representations, or **irreps**---and for our limited purposes, *particles are basis vectors of irreps*. This provides a way to organize particles, which physicists have been exploiting since the 1960s.

The idea of 'unification' has a clear meaning in these terms. Suppose $V$ is a representation, not only of $G$, but also some larger group $H$ having $G$ as a subgroup. Then we expect $V$ to decompose into fewer irreps as a representation of $H$ than as a representation of $G$, because elements of $H$ can mix different irreps of $G$. So: by introducing a larger symmetry group, particles can be unified into larger irreps.

'Grand unification' occurs when the compact Lie group $G$ is simple, and thus not a product of other groups. A gauge theory based on $G$ requires an invariant inner product on its Lie algebra. When $G$ is simple, this form is unique up to a scale factor, which physicists call a 'coupling constant': this measures the strength of the force corresponding to $G$. When $G$ is the product of simple factors, there is one coupling constant for each factor of $G$. So, by using a simple Lie group as gauge group, we minimize the number of coupling constants.

In this paper, we give an account of the algebra behind the Standard Model and three attempts at unification: Georgi and Glashow's ${\rm SU}(5)$ theory, Georgi's theory based on the group ${\rm Spin}(10)$ (physicists call this the ${\rm SO}(10)$ theory), and the Pati--Salam model. All three date to around 1974. The first two are known as grand unified theories, or GUTs, because they are based on simple Lie groups. The Pati--Salam model is different: while it is called a GUT by some authors, and does indeed involve unification, it is based on the Lie group ${\rm SU}(2) \times {\rm SU}(2) \times {\rm SU}(4)$, which is merely semisimple.

It is important to note that these theories have their problems. The ${\rm SU}(5)$ theory predicts that protons will decay more quickly than they do, and it requires certain trends to hold among the relative strengths of forces at high energies---trends which the data do not support. The ${\rm SO}(10)$ theory may still be viable, especially if at low enough energies it reduces to the Pati--Salam model. However, the issues involved are complex. For details, see the paper by Bertolini *et al* and the many references therein [@BLM].

Nonetheless, it is still very much worthwhile for mathematicians to study the algebra of grand unified theories. First, even apart from their physical significance, these theories are intrinsically beautiful mathematical structures. Second, they provide a nice way for mathematicians to get some sense of the jigsaw puzzle that physicists are struggling to solve. It is certainly hopeless trying to understand what physicists are trying to accomplish with string theory without taking a look at grand unified theories. Finally, grand unified theories can be generalized by adding 'supersymmetry'---and the resulting generalizations are considered serious contenders for describing the real world. For some recent overviews of their prospects, see Pati [@pati:decay; @pati:probing] and Peskin [@Peskin].

This is how we shall proceed. In Section [\[sec:sm\]](#sec:sm){reference-type="ref" reference="sec:sm"} we start by describing the Standard Model. After a brief nod to the electron and photon, we explain some nuclear physics in Section [\[sec:isospin\]](#sec:isospin){reference-type="ref" reference="sec:isospin"}. We start with Heisenberg's old attempt to think of the proton and neutron as two states of a single particle, the 'nucleon', described by a 2-dimensional representation of ${\rm SU}(2)$. The idea of unification through representation theory traces its origins back to this notion.

After this warmup we tour the Standard Model in its current form. In Section [\[sec:fermions\]](#sec:fermions){reference-type="ref" reference="sec:fermions"} we describe the particles called 'fundamental fermions', which constitute matter. In Section [\[sec:forces\]](#sec:forces){reference-type="ref" reference="sec:forces"} we describe the particles called 'gauge bosons', which carry forces. Apart from the elusive Higgs boson, all particles in the Standard Model are of these two kinds. In Section [\[sec:smrep\]](#sec:smrep){reference-type="ref" reference="sec:smrep"} we give a more mathematical treatment of these ideas: the gauge bosons are determined by the Standard Model gauge group $${G_{\mbox{\rm SM}}}= {\rm U}(1) \times {\rm SU}(2) \times {\rm SU}(3) ,$$ while the fundamental fermions and their antiparticles are basis vectors of a highly reducible representation of this group, which we call $F \oplus F^*$. Here $F$ describes the fermions, while $F^*$ describes their antiparticles.

Amazingly, using the ideas of gauge theory and quantum field theory, plus the 'Higgs mechanism' for symmetry breaking, we can recover the dynamical laws obeyed by these particles from the representation of ${G_{\mbox{\rm SM}}}$ on $F
\oplus F^*$. This information is enough to decode the physics of these particles and make predictions about what is seen in the gigantic accelerators that experimental physicists use to probe the natural world at high energies. Unfortunately, to explain all this would go far beyond the modest goals of this paper. For a guide to further study, see Section [\[subsec:reading\]](#subsec:reading){reference-type="ref" reference="subsec:reading"}.

Having acquainted the reader with the Standard Model of particle physics in Section [\[sec:sm\]](#sec:sm){reference-type="ref" reference="sec:sm"}, we then go on to talk about grand unified theories in Section [\[sec:guts\]](#sec:guts){reference-type="ref" reference="sec:guts"}. These theories go beyond the Standard Model by 'extending' the gauge group. That is, we pick a way to include ${G_{\mbox{\rm SM}}}$ in some larger group $G$, and choose a representation $V$ of $G$ which reduces to the Standard Model representation $F \oplus F^*$ when we restrict it to ${G_{\mbox{\rm SM}}}$. We describe how this works for the ${\rm SU}(5)$ theory (Section [\[sec:su(5)\]](#sec:su(5)){reference-type="ref" reference="sec:su(5)"}), the ${\rm SO}(10)$ theory (Section [\[sec:so(10)\]](#sec:so(10)){reference-type="ref" reference="sec:so(10)"}), and the Pati--Salam model (Section [\[sec:g(2,2,4)\]](#sec:g(2,2,4)){reference-type="ref" reference="sec:g(2,2,4)"}). Of course, since we do not discuss the dynamics, a lot will go unsaid about these GUTs.

As we proceed, we explain how the ${\rm SU}(5)$ theory and the Pati--Salam model are based on two distinct visions about how to extend the Standard Model. However, we will see that the ${\rm SO}(10)$ theory is an extension of both the ${\rm SU}(5)$ theory (Section [\[sec:so(10)\]](#sec:so(10)){reference-type="ref" reference="sec:so(10)"}) and the Pati--Salam model (Section [\[sec:route\]](#sec:route){reference-type="ref" reference="sec:route"}). Moreover, these two routes to the ${\rm SO}(10)$ theory are compatible in a precise sense: we get a commuting square of groups, and a commuting square of representations, which fit together to form a commuting cube (Section [\[sec:compatibility\]](#sec:compatibility){reference-type="ref" reference="sec:compatibility"}).

In Section [\[sec:conclusion\]](#sec:conclusion){reference-type="ref" reference="sec:conclusion"}, we conclude by discussing what this means for physics: namely, how the Standard Model reconciles the two visions of physics lying behind the ${\rm SU}(5)$ theory and the Pati--Salam model. In a sense, it is the intersection of the ${\rm SU}(5)$ theory and the Pati--Salam model within their common unification, ${\rm SO}(10)$.

Throughout the course of the paper, we occasionally summarize our progress in theorems, most phrased in terms of commutative diagrams:

-   Section 3.1, Theorem [\[thm:su(5)\]](#thm:su(5)){reference-type="ref" reference="thm:su(5)"}: the ${\rm SU}(5)$ theory extends the Standard Model.

-   Section 3.2, Theorem [\[thm:spinor\]](#thm:spinor){reference-type="ref" reference="thm:spinor"}: the ${\rm Spin}(10)$ theory extends the ${\rm SU}(5)$ theory.

-   Section 3.3, Theorem [\[thm:Pati\--Salam\]](#thm:Pati--Salam){reference-type="ref" reference="thm:Pati--Salam"}: the Pati--Salam model extends the Standard Model.

-   Section 3.4, Theorem [\[thm:Pati\--Salam2\]](#thm:Pati--Salam2){reference-type="ref" reference="thm:Pati--Salam2"}: the Pati--Salam model is isomorphic to a theory involving ${\rm Spin}(4) \times {\rm Spin}(6)$.

-   Section 3.4, Theorem [\[thm:Pati\--Salam3\]](#thm:Pati--Salam3){reference-type="ref" reference="thm:Pati--Salam3"}: the ${\rm Spin}(4) \times 
    {\rm Spin}(6)$ theory extends the Standard Model.

-   Section 3.4, Theorem [\[thm:Spin(10)\]](#thm:Spin(10)){reference-type="ref" reference="thm:Spin(10)"}: the ${\rm Spin}(10)$ theory extends the ${\rm Spin}(4) \times {\rm Spin}(6)$ theory.

-   Section 3.5, Theorem [\[thm:cube\]](#thm:cube){reference-type="ref" reference="thm:cube"}: the Standard Model, the ${\rm SU}(5)$ theory, the ${\rm Spin}(4) \times {\rm Spin}(6)$ theory and the ${\rm Spin}(10)$ theory fit together in a commutative cube.

-   Section 4, Theorem [\[thm:pullbackSO(10)\]](#thm:pullbackSO(10)){reference-type="ref" reference="thm:pullbackSO(10)"}: The true gauge group of the Standard Model is the intersection of ${\rm SU}(5)$ and ${\rm SO}(4) \times
    {\rm SO}(6)$ in ${\rm SO}(10)$.

-   Section 4, Theorem [\[thm:pullbackSpin(10)\]](#thm:pullbackSpin(10)){reference-type="ref" reference="thm:pullbackSpin(10)"}: The true gauge group of the Standard Model is the intersection of ${\rm SU}(5)$ and $({\rm Spin}(4) \times
    {\rm Spin}(6))/\mathbb{Z}_2$ in ${\rm Spin}(10)$.
