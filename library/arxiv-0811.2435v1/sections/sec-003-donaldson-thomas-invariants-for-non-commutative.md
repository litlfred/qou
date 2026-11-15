---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-003-donaldson-thomas-invariants-for-non-commutative
section_title: "Donaldson-Thomas invariants for non-commutative 3d Calabi-Yau varieties"
section_number: null
pages: 9-10
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.993
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
Recall that a non-commutative Calabi-Yau variety of dimension $d$ (a.k.a Calabi-Yau category of dimension $d$) is given by an $Ext$-finite triangulated $\A$-category ${\cal C}$ which carries a functorial non-degenerate pairing $$(\bullet, \bullet): \op{Hom}^\bullet_{\CC}(E,F)\otimes \op{Hom}^\bullet_{\CC}(F,E)\to \k[-d]$$ (see e.g. [@KoSo3], [@So1], [@Laz]), such that the polylinear forms $(m_n(f_0,\dots,f_n),f_{n+1})$ defined on $\otimes_{0\le i\le n+1}\op{Hom}^\bullet_{\CC}(E_i,E_{i+1})$ by higher compositions $m_n$ are cyclically invariant. We will discuss mainly the case $d=3$ and assume that our non-commutative $3d$ Calabi-Yau variety is ind-constructible and endowed with polarization.

Under these assumptions we define *motivic Donaldson-Thomas invariants* which take values in certain Grothendieck groups of algebraic varieties (more details are given in Sections 4 and 6). Assuming some "absence of poles\" conjectures, which we discuss in detail in Section 7 one can pass to the "quasi-classical limit\" which corresponds to the taking of Euler characteristic of all relevant motives. In this way we obtain the putative *numerical DT-invariants* $\Omega(\gamma)\in \Q, \gamma\in \Gamma\setminus \{0\}$. Morally, $\Omega(\gamma)$ counts semistable objects of $\CC$ with a given class $\gamma\in \Gamma\setminus \{0\}$.

There is a special case when our formulas can be compared with those from [@B] (see Section 7.1). Namely, let us define a *Schur object* $E\in Ob(\CC)$ as such that $$\op{Ext}^{<0}(E,E)=0, \op{Ext}^0(E,E)=\k\cdot Id_E\,\,.$$ By the Calabi-Yau property in the dimension $d=3$ we know that the only possibly non-trivial groups $\op{Ext}^i(E,E), i=0,1,2,3$ are $$\op{Ext}^0(E,E)\simeq \op{Ext}^3(E,E)\simeq \k\,,\,\,\,\op{Ext}^1(E,E)\simeq (\op{Ext}^2(E,E))^{\ast}\,\,.$$ In other words the ranks are $(1,a,a,1),\, a\in \Z_{\geqslant 0}$. Recall (see [@KoSo2], [@KoSo3]) that the deformation theory of any object $E\in Ob(\CC)$ is controlled by a differential-graded Lie algebra (DGLA for short) $\g_E$ such that $H^i(\g_E)\simeq \op{Ext}^i(E,E), i\in \Z$. For a given Schur object $E$ instead of $\g_E$ we can use a DGLA $\widehat{\g}_E=\tau_{\le 2}(\g_E)/\tau_{\le 0}(\g_E)$ where $\tau_{\le i}$ is the truncation functor. This makes sense since $\tau_{\le 0}(\g_E)$ is an ideal (in the homotopy sense) in $\g_E$. The modified deformation theory gives rise to a perfect obstruction theory in the sense of [@B], [@BF]. The corresponding moduli space is the same as the original one, although controlling DGLAs are not quasi-isomorphic. The contribution of Schur objects to $\Omega(\gamma)$ can be identified with the Behrend microlocal formula for DT-invariants. From this point of view objects of the category $\CC$ should be interpreted as critical points of the function (called the potential), which is obtained from the solution to the so-called classical master equation. The latter has a very natural interpretation in terms of the non-commutative formal symplectic dg-scheme defined by the $\A$-category $\CC$ endowed with a Calabi-Yau structure (see [@KoSo3]).
