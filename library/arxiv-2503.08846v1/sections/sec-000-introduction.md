---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 2-4
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
Introduction
Physics contributed to the birth of knot theory in the 19th century, when Lord Kelvin hypothesized that
atoms are knotted vortices of aether [1]. Although the idea was doomed to fail,1 it is said to inspire the
first knot classification by Peter Guthrie Tait. Tait’s knot table had significant impact on developing
knot theory as a branch of pure mathematics, a subfield of topology. Until late 20th century advances in
knot theory were predominantly limited to math.
In 1980s new connections between knot theory and physics started to emerge. Vaughn Jones discovers
a new type of topological invariant of knots [3], now known as Jones polynomial, by studying operator
algebras relevant for quantum mechanical systems (von Neumann algebras). Connections between gauge
theories and various types of topological invariants are being unearthed, e.g. [4–7], including the one
between the oldest link invariant of Gauss and Chern-Simons theory [8]. General methods of constructing
knot invariants are emerging in integrable statistical physics models [9,10] and two-dimensional conformal
field theories (CFT) [11–14]. A benchmark achievement is the work of Edward Witten [15], which brings
together all the different types of evidence, tying CFT, Chern-Simons theories and the Jones polynomial,
and opening gates for a plethora of generalizations. (See the following reviews of modern topics in knot
theory [16,17] and its connections to physics [18].)
A notable feature of these manifestations of knot theory is their quantumness. At the technical level
this is explained by the observation that the relevant topological invariants, as defined in mathematics,
can be cast as path integrals (partition functions) of some physical theories. At a more abstract level,
topology is intrinsically discrete, as is the quantum theory. (See, for example, the discussion in [19].)
Physical theories in the path integral should satisfy certain conditions. To be topological, they should
be insensitive to smooth local variations of the geometry of the space they live in. In other words, they
should be metric independent. One way to achieve this is to have their Lagrangians constructed without
any explicit or implicit use of the metric tensor [20,21].
On the physics side, path integrals provide a convenient formal description of quantum mechanics.
They compute matrix elements of the evolution operator and, by construction, possess a natural concate-
nation, or composition, property, which expresses a big matrix element as a product of infinitesimal ones.
Path integrals are, essentially, matrices, or tensors, though commonly represented in an uncountably
infinite-dimensional space.
Yet, on the mathematical side, path integrals are ill-defined, what motivated Michael Atiyah to give
an alternative, axiomatic, definition of the topological quantum field theories (TQFTs), to somewhat
convince mathematicians about the legitimacy and merits of the physical approach [19]. Atiyah’s axioms
replace the path integral by topological spaces with boundaries (the cobordisms, a sort of fat Feynman
diagrams) that have a similar concatenation property, as well as other properties compatible with path
integrals. By construction, these topological spaces should also be viewed as relevant quantum mechanical
matrices, such as the evolution operator. In other words, Atiyah’s TQFTs construct quantum mechanics
from topological spaces, bypassing the definition of the path integral.
The purpose of this review is to use the Atiyah’s definition of TQFT and its relation to knot theory
in order to build some general intuition about quantum mechanics, and in particular, about quantum
correlations.
The basis for this intuition will be general manipulations we can apply to topological
spaces, such as twisting, braiding, knotting etc., besides the mentioned concatenation. We will use these
1The beauty of the concept continued to enchant physicists and led to a new reincarnation of the idea at the end of
the 20th century. In the new formulation, atomic nuclei were proposed to be viewed as knots of pion fields, extending the
Skyrme model [2].
2
manipulations to “visualize” quantum states and quantum correlations, explain quantum entanglement
and some of its properties, and demonstrate how topological manipulations can be used in construction
of quantum algorithms. Hopefully, this will help provide a useful complementary perspective on quantum
phenomena and quantum physics.
As such the review has overlaps with two particular subjects in quantum theory. One is Topological
Quantum Computation, a large modern and actively developing field, which started from the idea that
topological phases of matter provide an appealing setup for realization of the quantum computer. Unlike
bosons and fermions, anyons – the quasiparticles of quantum Hall systems – may possess an unusual
nonabelian statistics, which makes them simple low-dimensional quantum-mechanical systems with re-
spect to a permutation, a mesoscopic operation of exchanging two particle positions. Together with the
robustness of quantum Hall systems to local decoherence, the properties of anyons led Alexei Kitaev to
the idea to propose such systems as fault-tolerant quantum computers [22]. In this proposal world lines
of permuted anyons form braids, and their knotlike closures mathematically compute matrix elements of
the evolution operator, as we will also see in this review.
Mathematical foundations of anyon-based quantum computing stem from knot theory. As the name
of the field implies it should pursue the following two main goals: search for physical systems in which
suitable topological phases and quantum operations can be realized and design of protocols and algorithms
for given systems and sets of operations (gates). In some cases this approach becomes too “hardware-
oriented”, making the role of knots and topology more technical and obscure. The present review takes
a more abstract approach trying to explore the tools available in the topological features themselves,
though less concerning with important practical details. The reader may compare the approaches by
looking at standard references on Topological Quantum Computations, such as the classic review [23]
and a recent book [24].
The second overlap is with a recently-introduced subfield of mathematics referred as Categorical
Quantum Mechanics (CQM). The name means that in this field quantum mechanics is formulated in terms
of category theory – the axiomatic approach of Atiyah is another example of a categorical formulation.
CQM started in the works of Samson Abramsky and Bob Coecke [25], based on the mathematical studies
of category theory in [26–29]. One of the central tools of CQM is the diagrammatic presentation of
quantum states and processes. Unlike Atiyah’s TQFTs the diagrams do not depict topological spaces but
more abstract objects (categories). This makes the description more universal, but at the same time less
intuitive. One of the goals of this review is thus to advocate for the topological version of the categorical
approach as for more intuitive one. Hopefully this also contributes to the proposals spelled in [30–32] to
use the categorical approach, or Quantum Picturalism, as an early introduction of quantum mechanics.
The following books are recommended as general references for CQM: [33,34].
The purpose of this review can also be seen as filling some gaps between the Topological Quantum
Computation and CQM. It is based on some recent work, which will be introduced along the way. Some
earlier work that served as motivation for the description built here might not receive deserved attention,
so the reader is referred to [35] for additional information anf literature, such as works of Louis Kauffman,
Sam Lomonaco and others on the application of knot calculus in quantum mechanics and in the study
of quantum entanglement, e.g. [36–41].
These notes are organized as follows. Section 2 gives a short introduction into knot theory with a
minimal amount of necessary techniques to calculate topological invariants to be used in the remaining
parts. Section 2.3 introduces the Jones polynomial (and its “bracket” version due to Kauffman) and
section 2.4 – a useful matrix formalism for its evaluation.
In section 3 we will explain how braids and more general topological spaces can be understood as
quantum mechanical states. We use a minimal knowledge of category theory to review Atiyah’s definition
of TQFT in section 3.1. In section 3.2 we describe a one dimensional TQFT, to which we refer as topo-
logical quantum mechanics (TQM). This TQM is in fact more naturally formulated in three dimensions,
as a Chern-Simons theory, as we review in section 3.3.
Section 4 is dedicated to a study of quantum entanglement using the topological viewpoint. We explain
3
the general relation of space connectivity and topology with the entanglement in section 4.1. In section 4.2
we discuss a classification of entanglement using stochastic local operations and classical communication
and how this classification emerges in topological spaces describing bipartite entanglement. In section 4.3
we introduce the von Neumann entropy and explain its topological meaning. Some of the properties of
the entropy are discussed, including famous inequalities in section 4.4.
Section 5 reviews two quantum algorithms in the topological formulation: quantum teleportation in
section 5.1 and dense coding in section 5.2. The purpose is to illustrate the sense, in which entanglement
is a resource for quantum tasks.
We give concluding remarks in section 6, where we also review some open questions and possible
applications, focusing on multipartite entanglement and quantum gravity.
