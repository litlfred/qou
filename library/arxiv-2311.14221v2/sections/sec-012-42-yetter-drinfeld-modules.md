---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-012-42-yetter-drinfeld-modules
section_title: "Yetter-Drinfeld modules"
section_number: 4.2
pages: 18-20
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.916
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
\label{Section_YD}

Let $H$ be a finite dimensional Hopf algebra in $\vect_\ku$. Then we shall denote by ${}^H_H\YD$ the category of finite-dimensional \textit{Yetter-Drinfeld modules.}  An object $V\in {}^H_H\YD(\vect_\ku)$ is a left $H$-module $\cdot:H\otk V\to V$, and a left $H$-comodule $\lambda:V\to H\otk V$ such that
\begin{equation}\label{yd-module} \lambda(h\cdot v)=h\_1 v\_{-1} \Sc(h\_3)\ot h\_2\cdot v\_0,
\end{equation}
for any $h\in H, v\in V$.  If $V\in {}^H_H\YD(\vect_\ku)$, the map
$\sigma_X: V\otk X\to X\otk V$, given by $\sigma_X(v\ot x)=v\_{-1}\cdot x\ot v\_0$ is a half-braiding for $V$.\\


This notion had been generalized in \cite{Besp95} to Hopf algebras $H$ inside a braided tensor category $\vc$:

\begin{defi}\label{def_YD}
Let $H$ be a Hopf algebra in a braided tensor category $\vc$. Then an $H$-$H$-\emph{Yetter-Drinfeld module} $V$ is an object $V\in\vc$, together with a structure of  $H$-module $m:H\otimes V\to V$  and  structure of  $H$-comodule in $\rho:V\to H\otimes V$ in the tensor category $\vc$, compatible in the following way
\begin{center}
                \begin{grform}
                    \begin{scope}[scale = 1]
                        \dMult{0.5}{1.5}{1}{-1.5}{\grau}
                        \dMult{0.5}{2.5}{1}{1.5}{\grau}
                        \dAction{2.5}{1.5}{0.5}{-1.5}{\grau}{black}
                        \dAction{2.5}{2.5}{0.5}{1.5}{\grau}{black}
                        \vLine{0.5}{1.5}{0.5}{2.5}{\grau}
                        \vLine{2.5}{1.5}{1.5}{2.5}{\grau}
                        \vLineO{1.5}{1.5}{2.5}{2.5}{\grau}
                        \vLine{3}{1.5}{3}{2.5}{black}
                        \draw (1 , -0.3) node {$H$};
                        \draw (1 , 4.3) node {$H$};
                        \draw (3 , -0.3) node {$V$};
                        \draw (3 , 4.3) node {$V$};
                    \end{scope}
                \end{grform}
                
                =
                
                \begin{grform}
                    \begin{scope}[scale = 1]
                       \vLine{2}{0}{1}{1}{black}
                       \dMultO{0}{1}{1.5}{-1}{\grau}
                       \dAction{0}{1}{1}{1}{\grau}{black}
                       \dAction{0}{3}{1}{-1}{\grau}{black}
                       \dMult{0}{3}{1.5}{1}{\grau}
                       \vLineO{2}{4}{1}{3}{black}
                       \vLine{1.5}{1}{1.5}{3}{\grau}
                        \draw (0.9 , -0.3) node {$H$};
                        \draw (0.9 , 4.3) node {$H$};
                        \draw (2 , -0.3) node {$V$};
                        \draw (2 , 4.3) node {$V$};
                    \end{scope} 
                \end{grform}
\end{center}
\end{defi}

The category ${^H_H}\YD(\vc)$ consists of  Yetter-Drinfeld modules and of $H$-linear and $H$-colinear morphisms. It becomes a tensor category with the usual tensor product of $H$-modules and $H$-comodules $V\otimes W$. An useful feature of this tensor category is that, it admits, by construction, a braiding
\begin{align*}
     c_{(V, m_V, \rho_V), (W, m_W, \rho_W)} 
    &: V \otimes W \rightarrow W \otimes V \\
\intertext{which is given on objects $(V, m_V, \rho_V)$ and $(W, m_W, \rho_W)$ by}
     c_{(V, m_V, \rho_V), (W, m_W, \rho_W)} 
    &:= (\rho_W \otimes \id_V ) \circ (\id_H \otimes
    c_{V,W} ) \circ (\rho_V \otimes \id_W )\,\, \\
\end{align*}
and is invertible if $H$ has a bijective antipode
\begin{align*}
(c_{(V, m_V, \rho_V), (W, m_W, \rho_W)} )^{-1} 
&:= c^{-1}_{V,W} 
\circ (m_W \otimes \id_V ) \circ (c^{-1}_{H,W} \otimes \id_V ) \\
&\circ (\id_W \otimes S^{-1} \otimes \id_V ) \circ (\id_W \otimes \rho_V ).
\end{align*}
 If $\vc$ is rigid, then the dual object in $\vc$ with the standard dual action and coaction  gives a dual object in ${^H_H}\YD(\vc)$. The structure is summarized in the following statement proven in \cite{Besp95}:
\begin{teo}
Let $H$ be a Hopf algebra in $\vc$. 
The Yetter-Drinfeld modules over $H$ in $\vc$ have
a natural structure of a
braided tensor category ${^H_H}\YD(\vc)$. If $\vc$ is rigid, then so is ${^H_H}\YD(\vc)$.
\end{teo}

Recall that the \emph{Drinfeld center}  
$\mathcal{Z}(\mathcal{B})$ is a braided tensor category associated to any tensor category $\mathcal{B}$.
The construction of Yetter-Drinfeld modules gives a realization of a special case of the construction of a \emph{relative Drinfeld center}  
$\mathcal{Z}_\vc(\mathcal{B})$, a braided tensor category associated to any tensor category $\mathcal{B}$ with a braided subcategory $\vc\hookrightarrow \mathcal{Z}(\mathcal{B})$. More precisely we have 
$${^H_H}\YD(\vc)=\mathcal{Z}_\vc({^H}\vc)$$
