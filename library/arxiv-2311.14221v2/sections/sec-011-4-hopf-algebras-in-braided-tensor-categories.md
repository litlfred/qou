---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-011-4-hopf-algebras-in-braided-tensor-categories
section_title: "Hopf algebras in braided tensor categories"
section_number: 4
pages: 17-18
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
text_source: latex
latex_prose_ratio: 0.702
latex_coverage_ratio: 0.951
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
\label{Section_Hopf}


\subsection{Hopf algebras in braided tensor categories}
Let us briefly recall the notion of Hopf algebras in braided tensor categories, and how their corepresentation categories are again tensor categories. For more details, the reader is referred to \cite{Majid},  \cite{Majid2}, \cite{Ta} and references therein. 

\medbreak


A \textit{braided tensor category} is a pair $(\vc,\sigma)$ where $\vc$ is a tensor category and $\sigma_{V,W}:V\ot W\to W\ot V$ is a \textit{braiding}, that is, a family of natural isomorphisms satisfying
\begin{equation}\label{braiding1}\begin{split} \sigma_{V,U\ot W}=(\id_U\ot \sigma_{V,W})(\sigma_{V,U}\ot\id_W),\\
\sigma_{V\ot U, W}=(\sigma_{V,W}\ot\id_U) (\id_V\ot \sigma_{U,W}).
\end{split}
\end{equation}
\begin{rmk} Note that in the above axioms we are assuming that $\vc$ is a strict tensor category. 
\end{rmk}
The braiding fulfills the braid relation, whence the name. We illustrate this identity in terms of string diagrams, which we read bottom to top
\begin{center}
        \begin{grform}
           \begin{scope}[scale = 1]
           
                \def\y{-0.3}\def\yn{-0.3+1}
                \draw (0 , \y) node {$U$};
                \draw (1 , \y) node {$V$};
                \draw (2 , \y) node {$W$};

                
                \def\y{0}\def\yn{1}
                \vLine{0}{\y}{0}{\yn}{\grau};
                \vLine{2}{\y}{1}{\yn}{\grau};
                \vLineO{1}{\y}{2}{\yn}{\grau};

                
                \def\y{1}\def\yn{2}
                \vLine{1}{\y}{0}{\yn}{\grau};
                \vLineO{0}{\y}{1}{\yn}{\grau};
                \vLine{2}{\y}{2}{\yn}{\grau};

                
                \def\y{2}\def\yn{3}
                \vLine{0}{\y}{0}{\yn}{\grau};
                \vLine{2}{\y}{1}{\yn}{\grau};
                \vLineO{1}{\y}{2}{\yn}{\grau};

                \def\y{3.3}\def\yn{4.3}
                \draw (0 , \y) node {$W$};
                \draw (1 , \y) node {$V$};
                \draw (2 , \y) node {$U$};
            \end{scope}  
        \end{grform}
                \quad=\quad
        \begin{grform}
            \begin{scope}[scale = 1]
           
                \def\y{-0.3}\def\yn{-0.3+1}
                \draw (0 , \y) node {$U$};
                \draw (1 , \y) node {$V$};
                \draw (2 , \y) node {$W$};

               
                \def\y{0}\def\yn{1}
                \vLine{1}{\y}{0}{\yn}{\grau};
                \vLineO{0}{\y}{1}{\yn}{\grau};
                \vLine{2}{\y}{2}{\yn}{\grau};

                
                \def\y{1}\def\yn{2}
                 \vLine{0}{\y}{0}{\yn}{\grau};
                \vLine{2}{\y}{1}{\yn}{\grau};
                \vLineO{1}{\y}{2}{\yn}{\grau};

                
                \def\y{2}\def\yn{3}
                \vLine{1}{\y}{0}{\yn}{\grau};
                \vLineO{0}{\y}{1}{\yn}{\grau};
                \vLine{2}{\y}{2}{\yn}{\grau};

                \def\y{3.3}\def\yn{4.3}
                \draw (0 , \y) node {$W$};
                \draw (1 , \y) node {$V$};
                \draw (2 , \y) node {$U$};
            \end{scope}
        \end{grform}
\end{center}


\begin{defi}
A \emph{bialgebra} in $\vc$ is a collection $(H,m,u,\Delta,\varepsilon)$, where $(H,m,u)$ is an algebra, $(H,\Delta,\varepsilon)$ is a coalgebra, and $\Delta, \varepsilon$ are algebra morphisms. I.e.
\begin{align}\label{definition:bialgebra} 
\Delta\circ m&=(m\ot m) (\id\ot \sigma_{H,H}\ot \id)  (\Delta\ot \Delta),\\
\Delta\circ u&= (u\ot u)\\
\varepsilon \circ m &= (\varepsilon\ot\varepsilon) \\
\varepsilon \circ u &= \id_\uno
\end{align}
We illustrate the first identity
\begin{center}
            \begin{grform}
                    \begin{scope}[scale = .8]
                       \dMult{1}{4}{2}{-1.5}{\grau}
                       \dMult{1}{0}{2}{1.5}{\grau}
                       \vLine{2}{1}{2}{3}{\grau}
                        
                        \draw (1 , -0.3) node {$H$};
                        \draw (1 , 4.3) node {$H$};
                        \draw (3 , -0.3) node {$H$};
                        \draw (3 , 4.3) node {$H$};
                    \end{scope}
                \end{grform}
                
                = \hspace{.2cm}
                
                \begin{grform}
                    \begin{scope}[scale = .8]
                       \dMult{0.5}{1.5}{1}{-1.5}{\grau}
                       \dMult{0.5}{2.5}{1}{1.5}{\grau}
                       \dMult{2.5}{1.5}{1}{-1.5}{\grau}{black}
                       \dMult{2.5}{2.5}{1}{1.5}{\grau}{black}
                       \vLine{0.5}{1.5}{0.5}{2.5}{\grau}
                       \vLine{2.5}{1.5}{1.5}{2.5}{\grau}
                       \vLineO{1.5}{1.5}{2.5}{2.5}{\grau}
                       \vLine{3.5}{1.5}{3.5}{2.5}{\grau}
                        
                        \draw (1 , -0.3) node {$H$};
                        \draw (1 , 4.3) node {$H$};
                        \draw (3 , -0.3) node {$H$};
                        \draw (3 , 4.3) node {$H$};
                   \end{scope}
                \end{grform}
\end{center}
    
\end{defi}
If $H$ is a bialgebra, then the space $\Hom_\vc(H,H)$ has a a convolution product with unit given by $u\circ \varepsilon$. If the identity $\id_H$ has an inverse $S$ under the convolution product, then $H$ is a \textit{Hopf algebra}, and $S$ is called the \textit{antipode}. The next Theorem is  well known, see for example \cite{Majid}.
\begin{teo}
If $H$ is a Hopf algebra in a braided tensor category $\vc$, then the category of left $H$-comodules ${}^H\vc$ is a  tensor category. Moreover, if $\vc$ is a finite tensor category, then ${}^H\vc$  is also  a finite tensor category, and the forgetful functor $\uc:{}^H\vc\to \vc$ is an exact faithful monoidal functor.\qed
\end{teo}


The tensor product of two left $H$-comodules is given as follows: If $(V,\rho_V)$, $(W, \rho_W)$ are objects in ${}^H\vc$, then the tensor product $V\ot W$ in $\vc$ has a left $H$-comodule structure given by
\begin{equation}\label{comodule-tensor-prod}\rho_{V\ot W}= (m\ot \id_{V\ot W})(\id_H\ot \sigma_{V,H}\ot \id_W)(\rho_V\ot \rho_W).
\end{equation}
\begin{center}
            \begin{grform}
                        \begin{scope}[scale = 1]
                                \dMult{-0.5}{2}{1}{1}{\grau}
                                \dAction{-0.5}{1}{2}{-1}{\grau}{black}
                                \dAction{0.5}{2}{2}{-1}{\grau}{black}
                                
                                \vLine{-0.5}{1}{-0.5}{2}{\grau}
                                \vLineO{1.5}{0}{1.5}{3}{black}
                                \vLine{2.5}{0}{2.5}{3}{black}

                                \draw (0 , 3.3) node {$H$};
                                \draw (1.5 , -0.3) node {$V$};
                                \draw (2.5 , -0.3) node {$W$};
                                \draw (1.5 , 3.3) node {$V$};
                                \draw (2.5 , 3.3) node {$W$};
                        \end{scope}
                        
                \end{grform}
    \end{center}



If $(V, \rho_V)\in {}^H\vc$ then ${}^*V\in  {}^H\vc$. The coaction is given by 
\begin{equation}\label{antipode-com} 
\rho_{{}^*V}=\big((S\ot \id)\sigma_{{}^*V,H}\ot \ev_V\big)\big(\id_{{}^*V}\ot \rho_V\ot \id_{{}^*V}\big)\big(\coev_V\ot\id_{{}^*V}\big).
\end{equation}
The coaction of the right dual $V^*$ is defined similarly.

\medbreak

For any $V\in \vc$ we can endow $V$ with a trivial $H$-comodule structure, given by
$$\rho^t_V:V\to H\ot V, \quad \rho^t_V=u\ot \id_V.$$



\subsection{Yetter-Drinfeld modules}\label{Section_YD}

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
