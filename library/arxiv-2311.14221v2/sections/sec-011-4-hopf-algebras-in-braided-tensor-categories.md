---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-011-4-hopf-algebras-in-braided-tensor-categories
section_title: "Hopf algebras in braided tensor categories"
section_number: 4
pages: 17-18
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 0.947
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
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
