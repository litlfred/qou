---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-019-4-abelian-periods-as-algebraic-integrals
section_title: "Abelian periods as algebraic integrals."
section_number: 4
pages: 47-47
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.978
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\begin{abst}
 We discuss periods of abelian varieties. Their $p$-adic counterparts 
 live naturally in Fontaine's ring $\matheur{B}_{\mathrm{dR}}$. We present 
 Colmez' construction of abelian $p$-adic periods, which relies on 
 $p$-adic integration and reflects as closely as possible the complex
 picture.
 




 We also deal with the concrete evaluation of elliptic $p$-adic periods.
\end{abst}


\subsection{Over $\C$.}\label{sub-complex-integ}

Let $A$ be an abelian variety over $\C$ of dimension $g$, 
and $\omega_1,\ldots,\omega_g$ a basis of invariant differential forms.






Let $\Lambda$ be the image of the map
\begin{equation*}
 \iota:\mathrm{H}_1(A(\C),\Z)\rightarrow \C^g\; ;\;\; \gamma\mapsto
 \left(\int_{\gamma}\omega_i\right)_i.
\end{equation*}
One has a canonical isomorphism 
\begin{equation*}
\C^g/\Lambda\stackrel{\sim}{\longrightarrow}A(\C).
\end{equation*}
Let us denote the projection $\C^g\rightarrow A(\C)$ by $\mathrm{pr}$.
For any differential one-form $\omega$ of the second kind, one can 
consider a primitive function $f_{\omega}$
of $\mathrm{pr}^{\ast}\omega$; it is meromorphic (univalued) on 
$\C^g$, because all residues of $\omega$ are $0$ by definition, and
it is unique up to addition of an arbitrary constant.
Then $f_{\omega}(z_1+z_2+z_3)-f_{\omega}(z_1+z_2)-f_{\omega}(z_1+z_3)
+f_{\omega}(z_1)$ defines a periodic function on $(\C^g)^3$, hence
induces a meromorphic function on $A(\C)^3$, which we denote by
$F^3_{\omega}$.
Note that the function $F^3_{\omega}$ can also be defined purely
algebraically by the following conditions:
\begin{itemize}
\item $F^3_{\omega}(z_1,0,z_3)=F^3_{\omega}(z_1,z_2,0)=0$.
\item $dF^3_{\omega}=m^{\ast}_{123}\omega-m^{\ast}_{12}\omega
-m^{\ast}_{13}\omega+m^{\ast}_1\omega,$
\end{itemize}
where $m_{123}$ is the addition $A^3\rightarrow A$ sending 
$(z_1,z_2,z_3)$ to $z_1+z_2+z_3$, etc.
For $\gamma\in\mathrm{H}_1(A(\C),\Z)$ the value
$f_{\omega}\bigl(i(\gamma)+a\bigr)-f_{\omega}(a)$ 
does not depend on $a\in\C^g$ ($a$ being chosen so that
$i(\gamma)+a$ and $a$ are not poles of $f_{\omega}$),
and one has the equality
\begin{equation*}
f_{\omega}\bigl(i(\gamma)+a\bigr)-f_{\omega}(a)=
\int_{\gamma}\omega,
\end{equation*}
which describes the period pairing 
\begin{equation*}
\mathrm{H}^1_{\mathrm{dR}}(A)
\times\mathrm{H}_1(A(\C),\Z)\longrightarrow\C
\end{equation*}
(or equivalently, the isomorphism
$\mathrm{H}^1_{\mathrm{dR}}(A)\otimes\C
\stackrel{\sim}{\rightarrow}
\mathrm{H}^1_{\mathrm{B}}(A(\C),\Z)\otimes\C$.)
Here $\mathrm{H}^1_{\mathrm{dR}}(A)$ denotes the first \emph{algebraic}
de Rham cohomology group of $A$, which coincides with the group of 
differential forms of the second kind modulo exact forms.
