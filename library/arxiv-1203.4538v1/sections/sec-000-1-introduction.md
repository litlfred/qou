---
doc_id: arxiv-1203.4538v1
doc_title: "The exponential-logarithmic equivalence classes of surreal numbers"
section_id: sec-000-1-introduction
section_title: "Introduction."
section_number: 1
pages: 1-2
source_pdf: 1203.4538v1.pdf
source_sha256: 5e44909e355c78d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.986
doc_brief: "The exponential-logarithmic equivalence classes of surreal numbers — 9 sections: Front matter; Introduction.; Preliminaries on surreal numbers."
---
In his monograph [@gonshor_surreal], H. Gonshor showed that Conway's real closed field of surreal numbers carries an exponential and logarithmic map. Subsequently, L. van den Dries and P. Ehrlich showed in [@ehrlich-vdd:surreal-exp] that it is a model of the elementary theory of the field of real numbers with the exponential function. In this paper, we give a complete description of the exponential equivalence classes (see Theorem [\[theo:kappa-equivEL\]](#theo:kappa-equivEL){reference-type="ref" reference="theo:kappa-equivEL"}) in the spirit of the classical Archimedean and multiplicative equivalence classes (see Theorem [\[theo:NO-series-gene\]](#theo:NO-series-gene){reference-type="ref" reference="theo:NO-series-gene"} and Proposition [\[prop:N0-Hahn\]](#prop:N0-Hahn){reference-type="ref" reference="prop:N0-Hahn"}). This description is made in terms of a recursive formula as well as a sign sequence formula for the family of representatives *of minimal length* of these exponential classes.

This result can be seen as a step towards proving that the field of surreal numbers **No** can be described as an exponential-logarithmic series field $\mathds{K}^{\textrm{EL}}$ (for some subfield of generalized series $\mathds{K}$ of **No**) and a field of transseries $\mathds{T}$. Indeed, we conjecture that our representatives of the exponential classes are the fundamental monomials of $\mathds{K}$ - say the **initial fundamental monomials** - in the sense of [@matu-kuhlm:hardy-deriv-EL-series], or the **log-atomic elements** (i.e. the monomials which remains monomials by taking iterated log's) in the sense of [@vdh:transs_diff_alg; @schm01]. Such a description would allow us to exploit these representations to introduce derivations on the surreals. Indeed, we know how to define derivations on exponential-logarithmic series fields [@matu-kuhlm:hardy-deriv-gener-series; @matu-kuhlm:hardy-deriv-EL-series] and on transseries fields [@vdh:autom-asymp; @schm01].

In Section [\[sect:defi\]](#sect:defi){reference-type="ref" reference="sect:defi"}, we give a concise summary of the recursive definitions of the field operations on **No**, as well as the definition of the exponential $\exp$ and logarithmic $\log$ maps, and generalized epsilon numbers $\epsilon_{\mathrm{\mathbf{No}}}$. Our exposition is based on [@gonshor_surreal]. Of particular interest to us is the analysis of certain equivalence relations on the surreal numbers. Conway [@conway_numb-games p 31-32] introduced and studied the $\omega$-map to give a complete system $\omega^{\mathrm{\mathbf{No}}}$ (:= the image of **No** under this map) of representatives of the Archimedean additive equivalence relation. In [@gonshor_surreal Theorem 5.3], exploiting the convexity of the equivalence classes, Gonshor describes such a representative $\omega^a$ as the *unique* surreal of minimal length in a given class. By a simple modification of their arguments, we describe a complete system $\omega^{\omega^{\mathrm{\mathbf{No}}}}$ of representatives of the Archimedean multiplicative equivalence relation. In Section [\[sect:kappa\]](#sect:kappa){reference-type="ref" reference="sect:kappa"}, we introduce and study what we call the $\kappa$-map to give a complete system $\kappa_{\mathrm{\mathbf{No}}}$ (:= the image of **No** under this map) of representatives of the exponential equivalence relation (Definition [\[defi:equiv-exp\]](#defi:equiv-exp){reference-type="ref" reference="defi:equiv-exp"} and Theorem [\[theo:kappa-equivEL\]](#theo:kappa-equivEL){reference-type="ref" reference="theo:kappa-equivEL"}). We observe that:

::: center
$\epsilon_{\textbf{No}}\subsetneq\kappa_{\textbf{No}}\subsetneq \omega^{\omega^{\textbf{No}}} \subsetneq\omega^{\textbf{No}}\subsetneq\textbf{No}$.
:::

Section [\[sect:kappa-sign\]](#sect:kappa-sign){reference-type="ref" reference="sect:kappa-sign"} is devoted to establish the sign sequences of these representatives (see Theorem [\[theo:kappa-signe\]](#theo:kappa-signe){reference-type="ref" reference="theo:kappa-signe"}). Then, in Section [\[sect:TEL\]](#sect:TEL){reference-type="ref" reference="sect:TEL"}, we introduce the notion of Transserial-Exp-Log fields, which unifies the notion of transseries and exp-log series. We conjecture that **No** is such a TEL field (Conjecture [\[conj:TEL\]](#conj:TEL){reference-type="ref" reference="conj:TEL"}).

We thank Joris van der Hoeven : we started with him the project of endowing **NO** with a derivation, and since then had several valuable exchanges on this topic in connection with the fields of surreal numbers and of transseries. This helped to lead us to the results we present here.
