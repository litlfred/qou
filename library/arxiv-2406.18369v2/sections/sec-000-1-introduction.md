---
doc_id: arxiv-2406.18369v2
doc_title: "112 years of listening to Riemannian manifolds"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2406.18369v2.pdf
source_sha256: 20b3f8dbc40eacc3
toc_source: outline
doc_brief: "112 years of listening to Riemannian manifolds — In1910, HendrikAntoonLorentzdelvedintotheenigmaticLaplace eigenvalue equation, also known as the Helmholtz equation, pondering to what extent the"
---
In 1910 the Dutch physicist Hendrik Antoon Lorentz gave five lectures under the
title “Old and new problems in physics” at the University of Göttingen. One of the
central topics of his lectures is the Helmholtz equation, the eigenvalue equation for
the Laplace operator:
(1) ∆f =λf, together with boundary conditions in case of boundary.
Here, ∆ is the Laplace operator, which inn-dimensional Euclidean spaceRn is
(2) ∆ =−
nX
i=1
∂2
∂x2
i
.
Solving the Helmholtz equation amounts to finding all eigenvaluesλ such that there
exists a solutionf to (1). When one solves this problem on a bounded domain in
Euclidean space, a boundary condition must also be imposed. Perhaps the most
common is the Dirichlet boundary condition, that requires the solutionf to vanish
on the boundary of the domain. At the time of Lorentz’s lectures, experts could
solve this equation in only a few types of domains: boxes (products of intervals),
spheres, disks, wedges, and products of these. For a more general bounded domain
in Euclidean space, the form of the solution and the collection of eigenvalues was
still a mystery.
Nonetheless, using reasoning from physics, Lorentz made a famous conjecture at
the end of his fourth lecture:
lim
Λ→∞
#{λ≤ Λ}
|Ω|Λn/2 =C >0.(3)
1
arXiv:2406.18369v2  [math.SP]  19 Sep 2024
2 G. MÅRDBY AND J. ROWLETT
In this equation, #{λ ≤ Λ} is the number of Laplace eigenvalues less than or
equal toΛ, considered in a bounded domainΩ⊂ Rn taking the Dirichlet boundary
condition. Here, |Ω| is then-dimensional volume of Ω, andC is a constant that
depends only on the dimensionn. Lorentz had the following physical - and musical
- explanation for this conjecture. Consider an enclosure with a perfectly reflecting
surface, which produces electromagnetic waves analogous to tones of an organ pipe.
To compute the energy in a frequency intervaldv, one may calculate the number
of overtones which lie between the frequenciesv andv +dv and then multiply this
by the energy at the frequencyv. Now, if the conjecture is true, then the number
of sufficiently high overtones betweenv and v +dv should be independent of the
shape of the enclosure and only proportional to its volume [70, p. 4].
Lorentz could rigorously prove that the conjecture is true if the domain were an
n-dimensional Euclidean box. So, he reasoned based on the physical interpretation
that the same asymptotic relationship should hold for any bounded domain. This
problem had already been formulated a month eariler by Arnold Sommerfeld at a
lecture in Köningsberg. David Hilbert, who was present at Lorentz’s lecture, was
convinced that (3) would not be proven in his lifetime. However, using techniques
developed by Hilbert himself, Hermann Weyl, who was also present at the lecture
and was a student of Hilbert, proved Lorentz’s conjecture less than two years later
in1912 [118]! Thus, Weylprovedthatthe eigenvaluesofthe Laplaceoperatoracting
on a bounded Euclidean domain with the Dirichlet boundary condition detect both
the dimensionn as well as then-dimensional volume of the domain. Inspired by
Lorentz’sorganpipe, onecouldsaythattheseeigenvaluescanbe heard,anddescribe
their study aslistening to them. In this way we could also describe those quantities
that are specified by knowing the eigenvalues can also beheard. The title of this
article refers to 112 years of investigating the interplay between the eigenvalues
and the geometric setting in which one is solving the Helmholtz equation, because
one can in general study the Helmholtz equation on ann-dimensional Riemannian
manifold (M,g ).
In this case, the Laplace operator is
(4) ∆ =−
X
i,j
1
det(g)∂igijp
det(g)∂j.
To further connect the Helmholtz equation to our listening analogy, note that
sounds are caused by vibration which is mathematically described by the wave
equation. A common way to solve the wave equation is to use separation of the
time and space variables. When one does this, the equation for the space variables
turns into the eigenvalue problem (1). The spectrum of (M,g ) is the set of all
eigenvalues. From a physical point of view, the spectrum represents the frequencies
thatM can produce. Therefore, it is indeed reasonable to say that a quantity may
be “heard” if it is determined by the eigenvalues. In other words, the quantity can be
heard precisely if it is a spectral invariant. In the 112 years since Weyl’s discovery,
mathematicians and physicists have investigated what geometric properties can
be ‘heard.’ In other words, we have been listening to Riemannian manifolds to
understand to what extent their geometry, or more colloquially, theirshape can be
heard. We do not take credit for this language, as it was inspired by Lorentz and
later popularized by Kac [70]. Interestingly, Kac’s description and language came
from Bochner, for whom the Bochner Laplacian is named [88].
112 YEARS OF LISTENING TO RIEMANNIAN MANIFOLDS 3
The intended audience of this article ranges from experts to those who are new
to the field. For the beginners, we will give an introduction to this rich field of
mathematics. For the experts, we will give a survey which presents numerous works
from different niches of the field, some of which even experts might not be aware.
Therefore, not only do we give a thorough overview of the major results of the past
112 years, but we also convey essential techniques by explaining the proofs of some
of these results. We start in §2 with the proof of Lorentz’s conjecture (3), a fact that
is now known as Weyl’s law. We show how one can prove this fact using variational
principles and bracketing arguments, as Weyl did 112 years ago. Although several
other proofs are now available [65], [66], [24], [23], Weyl’s original proof remains
instructive and robustly applicable to settings in which similar variational principles
are known to hold.
Weyl’s law shows that the dimension and the volume are spectral invariants,
in other words one can hear the dimension and volume of a bounded domain. It
took over 40 years to discover the next geometric spectral invariant. In 1954 the
SwedishmathematicianÅkePleijelshowedthatonecanhearthe (n−1)-dimensional
volume of the boundary of such a domain [98]. Of course, the field was not dormant
during these decades, so what were people working on, and what results were they
obtaining? Sinceonecannotcomputetheeigenvaluesofarbitrarilyshapeddomains,
it is natural to turn to more computationally accessible examples. One large class
of examples is flat tori, compact smooth Riemannian manifolds obtained by taking
the quotient ofRn by a full-rank lattice with Riemannian metric inherited from the
flat Euclidean metric. For these examples, one can show that the eigenvalues are
equal to the representation numbers of certain naturally associated quadratic forms.
In the years from 1912 to 1954, the theory of quadratic forms and representation
numbers developed rapidly and therewith our understanding of the spectra of flat
tori. In §3 we explain these connections and how they were used to construct
Milnor’s example of 16 dimensional isospectral non-isometric flat tori. Milnor’s
example helped to inspire Kac’s famous articleCan one hear the shape of a drum?
In the aforementioned article Kac focused on the Helmholtz equation in the
special context of bounded, two-dimensional domains, so these domains could be
seen as the heads of drums. Then, one can ask, if these drumssound identicalin
the mathematical sense that their Laplace spectra are identical, then are the drums
also the same shape? In other words, is the entire geometry of a two-dimensional
domain a spectral invariant? Although Kac did not answer this question, he gave
heuristic physical arguments to show that one would expect to be able to hear
the Euler characteristic of a smoothly bounded domain. Kac was forthright in
explaining that his arguments were not fully rigorous. Interestingly, his intuition
was entirely correct, and we will show in §4 that all of Kac’s arguments can be made
rigorous. Kac’s paper has inspired a wealth of research in the field, an overview of
which we give in §5 and §6. In §7, we leave the reader with a brief look towards
the future of the field and what one may expect or hope can be achieved.
