---
doc_id: arxiv-math-0611941v3
doc_title: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 0611941v3.pdf
source_sha256: bf6f2d55c7adee51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.979
doc_brief: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR — Let H be the one-parameter Hecke algebra associated to a ﬁnite Weyl group W, deﬁned over a ground ring in which “bad” primes for W are invertible."
---
[]{#sec:intro label="sec:intro"}

The concept of "cellular algebras" was introduced by Graham and Lehrer [@GrLe]. It provides a systematic framework for studying the representation theory of non-semisimple algebras which are deformations of semisimple ones. The original definition was modeled on properties of the Kazhdan--Lusztig basis [@KaLu] in Hecke algebras of type $A_n$. There is now a significant literature on the subject, and many classes of algebras have been shown to admit a "cellular" structure, including Ariki-Koiki algebras, $q$-Schur algebras, Temperley--Lieb algebras, and a variety of other algebras with geometric connections; see, e.g., [@GrLe], [@GrLe2], [@DJMa], [@CKoe] and the references there. However, the question of whether all Hecke algebras of finite type (i.e., the originally motivating examples) are cellular remained open. A positive answer to this question would provide a general theory of "Specht modules" which so far has only been established in types $A_n$, $B_n$ (see [@DJ0], [@Mu2], [@DJM3], [@GrLe]) and, with some restrictions on the ground ring, in type $D_n$ with $n$ odd (see [@pall1], [@kor2]). In these cases, the constructions heavily rely on the underlying combinatorics of Young tableaux.

The purpose of this paper is to solve this problem in general. We prove:

::: theorem
[]{#thmb label="thmb"} Let ${\mathcal{H}}$ be the one-parameter Hecke algebra associated with a finite Weyl group $W$, defined over an integral domain in which all "bad" primes for $W$ are invertible. Then ${\mathcal{H}}$ admits a natural "cellular" structure, where the elements in the "cellular basis" are integral linear combinations of Kazhdan--Lusztig basis elements $C_w$ with constant value ${\mathbf{a}}(w)$ (Lusztig's ${\mathbf{a}}$-function [@Lu1]).
:::

If we apply this in type $A_n$, the linear combinations will have only one non-zero term and we recover the Kazhdan--Lusztig basis in this case. In type $B_n$, we obtain a cellular structure which is different from the one by Dipper--James--Murphy [@DJM3] or Graham--Lehrer [@GrLe]. Our construction works in the general setting of multi-parameter Hecke algebras, assuming that Lusztig's conjectures on Hecke algebras with unequal parameters in [@Lusztig03 Chapter 14] hold. We can also formulate a similar result for Hecke algebras associated to non-crystallographic finite Coxeter groups $W$; some additional care is needed since ${\mathbb{Q}}$ is not a splitting field for such a group $W$.

Thus, if "bad" primes are invertible in the ground ring, then all Hecke algebras of finite type are "cellular". The general theory of cellular algebras then produces "cell representations" and a natural parametrisation of the irreducible representations for non-semisimple versions of ${\mathcal{H}}$, in terms of properties of certain bilinear forms on the cell representations; see [@GrLe §3]. We show that this parametrization is precisely given by the "canonical basic sets" introduced by Rouquier and the author [@mykl], [@GeRo2], [@mylaus].

This paper is organised as follows. In Section 2 we recall the fundamental facts from Kazhdan--Lusztig theory, including Lusztig's construction of the "asymptotic ring" $J$. We also establish a basic result about the representations of $J$ in Proposition [\[lem1\]](#lem1){reference-type="ref" reference="lem1"}. In Section 3, we prove Theorem [\[thmb\]](#thmb){reference-type="ref" reference="thmb"} and briefly discuss non-crystallographic Coxeter groups in Remark [\[noncryst\]](#noncryst){reference-type="ref" reference="noncryst"}. The cellular basis that we construct turns out to be unique up to integral equivalence of the representations of $J$. Finally, in Section 4, we consider examples and discuss the applications to non-semisimple specialisations. For types $A_n$ and $B_n$, we explain the relation of our cellular bases with the previously known ones.
