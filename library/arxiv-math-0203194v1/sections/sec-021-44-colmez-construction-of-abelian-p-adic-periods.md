---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-021-44-colmez-construction-of-abelian-p-adic-periods
section_title: "Colmez' construction of abelian $p$-adic periods."
section_number: 4.4
pages: 51-52
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.935
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
Let $A$ be an abelian variety defined over a $p$-adic local field
$K$. The Fontaine-Messing $p$-adic period pairing is a pairing

\begin{equation*}
\int^{(p)}\;:\;\mathrm{H}^1_{\mathrm{dR}}(A) \otimes T_p(A_{\ovl{K}})
 \longrightarrow \matheur{B}^+_{\mathrm{dR}}
\end{equation*}
where $T_p(A_{\ovl{K}}) = \varprojlim \Ker([p^n]: A_{\ovl{K}}\rightarrow
A_{\ovl{K}})$ is the Tate module (a ${\Z}_p$-module of rank $2\dim A$
with $\Gal({\ovl{K}}/K)$-action).

We present Colmez' construction, which is parallel to \ref{sub-complex-integ}.

Let $\omega$ be a differential form on $A$ of second kind, and
$F_{\omega}^3$ the function on $A^3$ determined as in
\ref{sub-complex-integ}.  Then:
\begin{pro}[{\cite[4.1]{ppdva}}]
There exists a locally meromorphic function $F_{\omega}$ on 
$A(\matheur{B}_{\mathrm{dR}})$, unique up to constant, such that:

\begin{enumerate}
 \renewcommand{\theenumi}{\arabic{enumi}}
 \item $dF_{\omega}=\omega$.
 \item $F_{\omega}(z_1+z_2+z_3)-F_{\omega}(z_1+z_2)-
       F_{\omega}(z_1+z_3)+F_{\omega}(z_1)=F^3_{\omega}(z_1,z_2,z_3)$.
 \item If $\omega=dF$, then $F_{\omega}=F$.
\end{enumerate}

\noindent
Moreover, if $\alpha\colon A_1\rightarrow A_2$ is a morphism of abelian 
varieties and $\omega$ is a differential form of second kind on
$A_2$, then $F_{\alpha^{\ast}\omega}=\alpha^{\ast}F_{\omega}$.
\end{pro}

Note that the function $F_{\omega}$ is \emph{not} multivalued; this
fact comes from the following lemma specific to the $p$-adic case:

\begin{lem}[{\cite[4.3]{ufdpplpdvaamc}}]
For any neighborhood $V$ of $0$ in $A(\matheur{B}_{\mathrm{dR}}^+)$, there
exists an open subgroup $U$ of $A(\matheur{B}_{\mathrm{dR}}^+)$ contained in 
$V$ such that $A(\matheur{B}_{\mathrm{dR}}^+)/U$ is a torsion group.
\end{lem}

Take a proper model $\mathscr{A}$ of $A$ over $\OO_{K}$.
Let $\gamma=(\cdots,u_n,\cdots,u_2,u_1=0)\in\mathrm{T}_p(A_{\ovl{K}})$ 
with each $u_n\in\mathscr{A}(\OO_{\C_p})$, and choose
$a_n\in\mathscr{A}(\matheur{B}^+_{\mathrm{dR}})$ so that neither
$a_n$ nor $a_n+_A\widehat{u}_n$ is close to a pole of $\omega$.
For suitable liftings 
$\widehat{u}_n\in\mathscr{A}(\matheur{B}^+_{\mathrm{dR}})$ of 
$u_n$ (\ie $\theta(\widehat{u}_n)=u_n$), the following holds. 

\begin{thm}[{\cite[5.2]{ufdpplpdvaamc}}]
The limit 
\begin{equation*}
 \oint^{(p)}_{\gamma}\omega \;:=\;
 \lim_{n\rightarrow\infty}p^n\bigl(F_{\omega}(a_n)-F_{\omega}
 (a_n+_A\widehat{u}_n)\bigr)
\end{equation*}
converges to an element in $\matheur{B}^+_{\mathrm{dR}}$, and it defines
a non degenerate bilinear pairing
\begin{equation*}
 \oint^{(p)}\;:\;
 \mathrm{H}^{1}_{\mathrm{dR}}(A)\otimes
 \mathrm{T}_p(A_{\ovl{K}})\longrightarrow\matheur{B}_{\mathrm{dR}}^+,
\end{equation*}
compatible with the Galois action and the filtrations.
\end{thm}

\begin{rem}
 On composing the period pairing $\int^{(p)}$ with $\theta$, one gets a
 bilinear map $\mathrm{H}^1_{\mathrm{dR}}(A) \otimes T_p(A_{\ovl{K}})
 \longrightarrow \C_p$ which sends $\Omega^1(A)\subset
 \mathrm{H}^1_{\mathrm{dR}}(A)$ to $0$.  This degenerate pairing
 describes ``half'' of the (Hodge)-Tate-Raynaud decomposition
 \begin{equation*}
  \mathrm{H}^1_{\mathrm{et}}(A_{\ovl{K}},{\Q}_p)\otimes {\C}_p \simeq
   \Omega^1(A)\otimes
   {\C}_p(-1) \oplus \mathrm{H}^1(\mathcal{O}(A))\otimes {\C}_p
 \end{equation*}
 of $\Gal({\ovl{K}}/K)$-modules.
\end{rem}
