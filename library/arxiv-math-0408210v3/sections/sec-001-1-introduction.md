---
doc_id: arxiv-math-0408210v3
doc_title: "A SIMPLE ALGEBRAIC PROOF OF THE ALGEBRAIC INDEX THEOREM"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0408210v3.pdf
source_sha256: 16d5ccb83a86954f
doc_brief: "A SIMPLE ALGEBRAIC PROOF OF THE ALGEBRAIC INDEX THEOREM — In math.QA/0311303 B. Feigin, G. Felder, and B."
---
The famous Atiyah-Singer index theorem [2] relates the index of an e lliptic pseudo-diﬀerential
operator on a compact manifold X to the Todd class of X and the Chern character of the
bundle naturally associated with the symbol of the pseudo-diﬀeren tial operator. It is well-
known that the algebra of pseudo-diﬀerential operators can be v iewed as a “quantization”
of the cotangent bundle T ∗X. Starting from this point B. Fedosov [9] proposed a natural
analogue of the Atiyah-Singer index theorem for the deformation q uantization of an arbitrary
symplectic manifold. This theorem expresses the index of a compact ly supported element in
K-theory of the quantum algebra of functions on a symplectic manifo ld M via the ˆA-genus
of M, the Deligne-Fedosov class of the quantum algebra, and the Chern character of the
principal symbol of the K-theory element. While the original index theorem of Atiyah and
1On leave of absence from: ITEP (Moscow)
1
Singer relates two integers, the Fedosov index theorem relates tw o formal power series with
complex coeﬃcients.
In paper [16] R. Nest and B. Tsygan proposed a completely diﬀerent proof of the algebraic
index theorem based on the relations between Hochschild (co)homo logy, cyclic (co)homology,
and Lie algebra (co)homology. In their next paper [18] they also sho wed that the analytic
index theorem for a compact manifold (without a boundary) could be derived from the
algebraic one. In order to generalize this result to manifolds with a bo undary (or more
generally, with corners) one is in great need of a local version of the algebraic index theorem
which relates De Rham cohomology classes, rather than formal pow er series of complex
numbers.
The aim of this paper is to give such a version (see theorem 4 in section 3) using the trace
density map proposed in paper [10] by B. Feigin, G. Felder, and B. Sho ikhet. Namely, we
show that the Feigin-Felder-Shoikhet (FFS) trace density map sen ds an arbitrary element of
K-theory of the algebra of quantum functions on M to the top component of the cup product
of the ˆA-genus of M, the exponent of the Deligne-Fedosov class of the quantum algebr a, and
the Chern character of the principal symbol of the element. Thus , we generalize the result
of [10], in which the trace density map was evaluated at the trivial elem ent of K-theory. For
the case of the cotangent bundle this computation of [10] was perf ormed in [7].
We have to mention that in [6] another version of the trace density m ap was proposed.
This map sends a cohomology class of the sheaf of the periodic cyclic c omplexCC per
• (Oquant
X )
of the structure sheaf Oquant
X of quantum functions on a holomorphic symplectic manifold X
to the cohomology of the constant sheaf on X. In [6] it was proven that the evaluation of this
map on an arbitrary cohomology class of the sheaf of periodic cyclic c omplexCC per
• (Oquant
X )
can be expressed in terms of the principal symbol of the class, ˆA-genus ofX and the Deligne-
Fedosov class of the quantum deformation. In [6] the authors ref er to this result as a
Riemann-Roch theorem for deformation quantizations. It is not ha rd to see that the local
version of the algebraic index theorem proven in our paper follows fr om the results of P.
Bressler, R. Nest and B. Tsygan [6]. However, our proof is more exp licit and straightforward.
For this reason we expect that our technique is more powerful for exploring the parallel
analytic results.
We would like to mention an alternative deformation quantization proc edure due to L.
Boutet de Monvel and V. Guillemin [4]. This procedure allows us to quant ize an arbi-
trary compact symplectic manifold with an integral symplectic form. Recently R. Melrose
proposed in [15] a beautiful idea on how one can relax the integrality c ondition in the quan-
tization of L. Boutet de Monvel and V. Guillemin. R. Melrose suggests that using this
procedure one could derive the algebraic index theorem from the an alytic one.
The organization of the paper is as follows. In section two, we give a r eminder of Fedosov’s
construction [9] of the deformation quantization with twisted coeﬃ cients on a symplectic
manifold. In this section we also recall the necessary results of Feig in, Felder, and Shoikhet
about their trace density map proposed in [10]. In section three, we prove the local version
of the algebraic index theorem (see theorem 4), using the FFS trac e density map. In the
concluding section we make a few remarks about the local algebraic in dex theorem for
symplectic Lie algebroids and the versions of the local Riemann-Roch -Hirzebruch theorem.
Throughout the paper we assume the summation over repeated ind ices. We assume that
M is either a smooth real symplectic manifold of dimension 2 n or a smooth aﬃne algebraic
variety (over C) of the complex dimension 2 n, endowed with an algebraic symplectic form.
2
C(M) stands, respectively, for the algebra of smooth function or for the algebra of regular
functions on M. The notation Sk is reserved for the group of permutations of k elements.
We omit the symbol ∧ referring to a local basis of exterior forms, as if we thought of dxi’s as
anti-commuting variables. For a vector space h we denote by Sjh the subspace of monomials
of degree j in the symmetric algebra Sh of h . Finally, we always assume that a nilpotent
linear operator is the one whose second power is vanishing.
Acknowledgments. This work was done while the ﬁrst author was a student and the
second author was a mentor in the Summer Program for Undergrad uate Research. We
both express sincere thanks to Hartley Rogers who organizes this remarkable program at
M.I.T. We thank Richard Melrose and all participants of his Spring analy sis seminar for
their interest and stimulating discussions. The second author also t hanks Alberto Cattaneo
and Giovanni Felder for useful conversations. We are grateful t o Teal Guidici for criticisms
concerning our English. This work is partially supported by the NSF gr ant DMS-9988796,
the Grant for Support of Scientiﬁc Schools NSh-1999.2003.2, the g rant INTAS 00-561 and
the grant CRDF RM1-2545-MO-03.
