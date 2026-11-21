---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-022-45-some-computations-of-elliptic-p-adic-periods
section_title: "Some computations of elliptic $p$-adic periods."
section_number: 4.5
pages: 52-53
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.946
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub-computation}

\begin{para}{\itshape Tate elliptic curves.\ }
In this case, $T_p(A_{\ovl{K}})$ sits in an exact sequence 
\begin{equation*}
 0\rightarrow {\Z}_p(1)\rightarrow T_p(A_{\ovl{K}}) \rightarrow
  {\Z}_p \rightarrow 0.
\end{equation*}
Let us take for $\gamma_1$ the image of $(2i\pi)_p \in {\Z}_p(1)$ in
$T_p(A_{\ovl{K}})$, and for $\gamma_2$ any lifting of $1 \in {\Z}_p$.
For concreteness, let $A=X_z$ be in Legendre form as in
\ref{para-padic-int-1}.  Let $\eta \in \mathrm{H}^1_{\mathrm{dR}}$
satisfy $\an{\omega,\eta}=1$ (\eg $\frac{xdx}{4y}$).  We set
$\omega^{(p)}_i=\int^{(p)}_{\gamma_i}\omega,
\eta^{(p)}_i=\int^{(p)}_{\gamma_i}\eta$.  Then one has the ``Legendre
relation''
\begin{equation*}
\omega^{(p)}_1\eta^{(p)}_2-\eta^{(p)}_1\omega^{(p)}_2=(2i\pi)_p
\end{equation*}
and the formulas (\cf \cite{pbl}, \cite{get})
\begin{equation*}
\frac{\omega^{(p)}_1}{(2i\pi)_p} = \sqrt{-1}F\Bigl(\frac{1}{2},
\frac{1}{2},1;z\Bigr) = 1/\Theta(z), \;\; \omega^{(p)}_2 =
\sqrt{-1}F\Bigl(\frac{1}{2},\frac{1}{2},1;z\Bigr) \Log q
\end{equation*}
(compare with the complex case in \ref{para-tate-para}, and also
\cite[p.406]{f2}).  Note that the ``period'' we found in
\ref{para-padic-int-1} by integration along the Berkovich loop is
 \emph{not} a Fontaine-Messing period (there is a $\log$ instead of
 $\Log$).
\end{para}

\begin{para}{\itshape Elliptic curves with ordinary reduction.\ }
We now assume that $z\in {\Z}_p^{\mathrm{ur}}$ and that $A=X_z$ has good
ordinary reduction (with the notation of \subsecref{sub-dwork-hyper},
this means that $z(1-z)h_p(z)\neq 0$).  Again, $T_p(A_{{\ovl{\Q}}_p})$
sits in an exact sequence (\cite[A.2.4]{alraec})
\begin{equation*}
0\rightarrow {\Z}_p \gamma_1\rightarrow
T_p(A_{{\ovl{\Q}}_p}) \rightarrow T_p(A\;\mathrm{mod}\, p) \rightarrow 0.
\end{equation*}
 Then one still has the formula $\Theta(z)=
\frac{(2i\pi)_p}{\omega^{(p)}_1}$, where $\Theta(z)\in
\widehat{{\Z}_p^{\mathrm{ur}}}$ is the Tate constant discussed in
\ref{para-tate-para} (compare \cite{pbl}, \cite[4.3]{itoecwcm}).  In
particular, $\frac{\omega^{(p)}_1}{(2i\pi)_p}$ is given by the
evaluation at $z$ of ``the'' extension of
$F(\frac{1}{2},\frac{1}{2},1;?)$ discussed in \subsecref{sub-serre-tate-para}.

\noindent On the other hand, let $\gamma_2 \in T_p(A_{{\ovl{\Q}}_p})$ be
such that the Weil pairing $\an{\gamma_1,\gamma_2}\in {\Z}_p(1)={\Z}_p
(2i\pi)_p$ is the chosen generator $(2i\pi)_p$. Then one has the
``Legendre relation'', and $\omega^{(p)}_2 = \omega^{(p)}_1\cdot\frac{{\Log
\;q}}{{(2i\pi)_p}}$, where $q\in \widehat{{\Z}_p^{\mathrm{ur}}}$ denotes
here the so-called {\it Dwork(-Serre-Tate) parameter} of $A$ introduced
in \ref{para-dwork-para}.  If $q=1$, \ie when $A$ is the \emph{canonical
lifting} of $A\pmod{p}$, then one can choose $\gamma_2\;$ such the
corresponding value of ${\Log 1}$ is $0$, and then $\omega^{(p)}_2 =0.$
\end{para}
