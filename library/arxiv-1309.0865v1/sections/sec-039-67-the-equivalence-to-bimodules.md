---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-039-67-the-equivalence-to-bimodules
section_title: "The equivalence to bimodules"
section_number: 6.7
pages: 69-69
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 1.0
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
In this section we assume that $\hg$ is a Soergel realization over a field $\Bbbk$. In this section we prove that our diagrammatic category is equivalent to Soergel bimodules.

By Corollary \ref{cor:homto[B]} the map $\HB \to [\DC] : \un{H}_s \mapsto [B_s]$ is a homomorphism. By taking the graded ranks of Hom spaces in $\DC$ we obtain a pairing on $[\DC]$ which induces a semi-linear pairing $( - , - )_{\DC}$ on $\HB$ by pull-back. It is obvious from the diagrammatic description of $\DC$ that $B_s$ is self-biadjoint in $\DC$, so $\un{H}_s$ is self-biadjoint in this pairing. It follows that $( -, - )_{\DC}$ is determined by the trace $\e_\DC : \HB \to \Zvv : h \mapsto ( h, 1 )_{\DC}$. Because the degree of any light leaves map is given by the defect of the corresponding subexpression, it follows from Proposition \ref{homspaceprop} and Corollary \ref{cor:defects} that $\e_{\DC}$ agrees with the standard trace on objects of the form $\un{H}_{\un{w}}$ for all expressions $\un{w}$. As these elements generate $\HB$ we conclude that $\e$ and $\e_{\DC}$, and hence $( - , - )_{\DC}$ and the standard form $( -, - )$, agree.

In section \ref{subsec-functor} we constructed a monoidal functor $\FC : \DC \to \BSBim$. It induces a monoidal functor on the idempotent completions $\FC : \Kar(\DC) \to \SBim$.

\begin{thm} Under the above assumptions $\FC : \Kar(\DC) \to \SBim$ is an equivalence of monoidal categories. \label{thm-equiv}
\end{thm}

\begin{proof} Because idempotent completion preserves equivalences, it is enough to show that $\FC : \DC \to \BSBim$ is an equivalence. Clearly this functor is essentially surjective, so it is enough to show that it is fully-faithful. It is a theorem due to Libedinsky \cite{Lib} that images under $\FC$ of the dots, trivalent vertices and $2m_{st}$-valent vertices generate all moprhisms between Bott-Samelson bimodules. It follows that $\FC$ is full. Now by the above discussion and the fact that our realization is a Soergel realization, the graded dimensions of the homomorphism spaces in $\DC$ and $\BSBim$ conincide. We conclude that $\FC$ induces an isomorphism on Hom spaces, being a surjection between graded vector spaces of the same (finite) dimension in each graded component. Hence $\FC$ is fully-faithful.\end{proof}

\begin{remark} One can avoid the appeal to Libedinsky's result as follows. By adjunction, it is enough to prove that the images of dots, trivalent vertices and $2m_{st}$-valent vertices generate $\Hom(B_{\un{w}}, R)$ for any expression $\un{w}$. Now a fixed choice of light leaves maps $\LL_{\un{w},e}$ is obviously mapped to a composition of such maps, and is mapped to a linearly independent subset of $\Hom(B_{\un{w}}, R)$ by the same localisation argument as in the proof of Corollary \ref{LLalocalbasis}, this time carrried out in the localized category of Soergel bimodules. By comparing the degrees of $\LL_{{\un{w}},\eb}$ and the graded rank of $\Hom(B_{\un{w}}, R)$ one concludes that $\LL_{\un{w},e}$ spans $\Hom(B_{\un{w}}, R)$ as a graded $R$-module. Hence the result. (This is basically an adaption of Libedinsky's argument.)
\end{remark}
