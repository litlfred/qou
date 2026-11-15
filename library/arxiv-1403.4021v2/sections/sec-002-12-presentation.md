---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-002-12-presentation
section_title: "Presentation"
section_number: 1.2
pages: 3-4
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.973
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
The origin of this work was the apparently innocent question to determine whether the `Kauffman trace', that is the
Markov trace affording the Kauffman polynomial, was indeed the only Markov
trace factoring through the BMW-algebra (in addition to the one factoring
to the smaller Hecke algebra quotient). When we tried to answer this question, we faced
another problem. First of all, it is well-known that there are two variations of
the Kauffman polynomial, one of them having been given the name of the
city of Dubrovnik. These two variations can be seen as Markov traces,
after specialization of the parameters $a,b,c$, subject to a polynomial relation
$a = bc$ or $a = -bc$. But they are not Markov trace on the same BMW-algebra ! More
precisely, although the two relevant BMW-algebras are isomorphic as algebras, they
are a priori not the same quotient of the group algebra of the braid group. Indeed, the additional
relation on 3 strands involves $a,b,c$ and depends on whether $a=bc$ or $a = -bc$.
Viewing the BMW-algebras as centralizer algebras for quantum groups actions, these two
specializations correspond to the difference between the orthogonal and symplectic
groups (see the end of \S \ref{secttwobmwagebras}). 

Because of this, we tried to dig deeper into the defining relations of the BMW-algebras. When
translated into braid words, the usual additional relation (in both cases), relating $e_i s_j e_i $ and $e_i$
for $|i-j| = 1$, involves 12 terms. We use another relation, that relates $s_j^{-1} e_i s_j^{-1}$ and $s_i e_j s_i$, involving only 6 terms when expanded into braid words, which holds inside both BMW-algebras, and which is enough to ensure
the finiteness of the dimension. Because of this, we can define
a finite-dimensional `cover' of the two BMW-algebras involved in the computation of the Kauffman polynomial,
as well as the ortho-symplectic quantum invariants, that we
call $\widetilde{BMW}_n$.  


From this we get a satisfying algebraic setup to explore the possible Markov traces for every single value
of the parameters. We prove that, for generic values of the parameters, this cover is actually isomorphic to
the usual BMW-algebras, thus providing in these cases an even simpler definition (as a quotient of the group algebra of $B_n$) of the BMW-algebras 
(see propositions \ref{propisomBMWtilde} and \ref{propisomBMWtilde2}). However, for generic
values satifying $a^2 = y$, we find that $\widetilde{BMW}_3$ has one dimension more than expected.


Concerning Markov traces we first get (proposition \ref{prop:MT3bmw}) that, when $a^2 \neq y^2$ and $a^2 \neq y$ (and actually : also when $a^2 = y$ and $a^2 \neq y^2$,
see proposition \ref{propmarkovypas1}), the only Markov trace factoring through $\widetilde{BMW}_n$ is the Ocneanu trace, defined
on the Hecke algebra quotient. 

We specialize to the situation $a^2 = y^2$. Then,
we have in addition the Kauffman trace.
When $y \neq 1$, we prove that the only Markov traces factoring through our algebra lead either to the Kauffman polynomial or to the Homfly polynomial,
and that this algebra is actually isomorphic to the usual BMW-algebra. When $y = 1$, that is when $a^2 = y^2$ and $a^2 = y$,
we have first to exclude a very degenerate case, $x = -2a$, for which there is an infinite number of Markov traces,
namely the ones factoring through the group algebra of the symmetric group (see proposition \ref{propTracesXm2a}) ; it is well-known that
these ones detect only the number of components of the links. In the general case $y=1$,
we get an additional Markov trace $t_n^{\dagger \dagger}$ that basically provides the parity of the number of
components of the link. These 3 Markov traces exhaust all possible traces, and are linearly independent one
from the other, for generic $x$. The special values for which this does not hold, besides $x = -2a$, are $x=a$ and $x=2a$.

In order to understand what happens in these two special cases, we provide a description of the algebra
$\widetilde{BMW}_n$ when specialized at $a^2=y=1$. For this we define by generators and relations an algebra over $\Q[a,x,x^{-1}]/(a^2-1)$ that we denote $F_n$.
It is a free module of rank 1 more than the dimension of $BMW_n$ (corollary \ref{cordimFn}) and it can be viewed
as a central extension of $BMW_n$ by a 1-dimensional ideal spanned by some element that we call $C$. This element squares to 0, and
therefore the extension cannot split, precisely when $x=a$ and $x=2a$. We prove that it is indeed the specialization
we want of $\widetilde{BMW}_n$, as soon as $x \neq -2a$ (theorem \ref{theoisomddaggerFn}),
while the specialization of $\widetilde{BMW}_n$ for the case $x=-2a$ provides a larger algebra, of which we provide a
partly conjectural description (see section \ref{subsectm2a}). Finally, we use the structure of $F_n$ to check that the space of Markov traces factoring through $F_n$ has dimension at most 3 : there is at most one way to find
an additional Markov trace in the special cases $x=a$ and $x=2a$.


In passing, we deduce from the existence of $F_n$ a similar central extension $\widetilde{TL}_n$ of the Temperley-Lieb algebra,
which is a subalgebra of $F_n$. We find natural (diagrammatic) interpretations of the two (potential) additional Markovs trace when restricted to this
subalgebra. Finally, we manage to construct the expected additional Markov trace in the case $x=2a$ by constructing a central
extension of the classical Hecke algebra.

More generally, we prove that, for an arbitrary Coxeter system $(W,S)$, the usual Iwahori-Hecke algebra at $q=-1$
has a natural non-split central extension, of dimension $1+\# W$ if $W$ is finite, and that there existes a Markov trace on this
algebra when $W= \mathfrak{S}_n$ (see theorems \ref{theoHeckeExt} and \ref{theoexistencetracedeltanul}). This Markov trace provides what we need.
The case $x= a$ remains conjectural, although we are confident that the corresponding invariant exists. We guess that an algebraic proof
of the existence of the Kauffman trace similar to the one that Jones provided for the Ocneanu trace should be easy to
generalize to our central extension. However it appears that no one provided such a proof yet, and finding such a proof seems to us to be quite
more tricky than the Hecke algebra case.
