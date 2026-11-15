---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-013-5-monoidal-module-categories
section_title: "Monoidal module categories"
section_number: 5
pages: 20-22
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.82
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
Given $\vc$, $\Bc$ tensor categories. We shall  define what means that a tensor category $\vc$ \textit{acts} on $\Bc$.

\begin{defi}\label{definition:monoidal-mod} We call $\Bc$ a \emph{monoidal left $\vc$-module category} if $\Bc$ is a left  $\vc$-module category, with action given by $\triangleright:\vc\times \Bc\to \Bc, $ such that
 $\uno\triangleright\uno\simeq \uno,$
and there are natural isomorphisms
$l_{X,B}: X \triangleright B\xrightarrow{\;\simeq\; } (X\triangleright \uno)\ot B,$
for any $X\in \vc$, $B\in \Bc$, such that


\begin{equation}\label{tens-acting0}  l_{\uno, B}=\id_B, \quad l_{X,\uno}=\id_{X\triangleright \uno},
\end{equation}
\begin{equation}\label{tens-acting}  
            \begin{tikzpicture}[commutative diagrams/every diagram]
            \node (P1) at (180:5cm) 
            {${X\triangleright(Y \triangleright B)}$};
            \node (P2) at (180-51:5cm) 
            {${(X\triangleright\uno)\otimes (Y \triangleright B)}$};
            \node (P3) at (180-51*2:5cm) 
            {$(X\triangleright\uno)\otimes ((Y \triangleright \uno)\otimes B)$};
            \node (P4) at (180-51*3:5cm) 
            {$((X\triangleright \uno)\otimes (Y \triangleright \uno))\otimes B$};
            
            \node (P5) at (180-51*4:5cm) 
            {$(X\triangleright (Y \triangleright \uno))\otimes B$};
            \node (P6) at (180-51*5:5cm)
            {${((X\otimes Y) \triangleright \uno)\otimes B}$};
            \node (P7) at (180-51*6:5cm) 
            {$(X\otimes Y) \triangleright B$};
\path[commutative diagrams/.cd, every arrow, every label]
            (P1) edge node [swap] {$l_{X,Y\triangleright B}$} (P2)
            (P2) edge node [swap] {$\mathrm{id}_{X\triangleright \uno}\ot  l_{Y,B}$} (P3)
            (P3) edge node [swap] {\rotatebox{-31}{$\sim$}} (P4)
            
            (P1) edge node {$m_{X,Y,B}^{-1}$} (P7)
            (P7) edge node {$l_{X\ot Y,B}$} (P6)
            (P6) edge node {$m_{X,Y,\uno}\otimes \mathrm{id}_B$} (P5)
            (P5) edge node {$l_{X,Y\triangleright  \uno}\ot\id_B$} (P4); 
            \end{tikzpicture}
\end{equation}

for any $X, Y\in \vc$, $B\in \Bc$. Similarly, we shall say that $\Bc$ is a monoidal right $\vc$-module category, with action $\triangleleft:\Bc\times  \vc\to \Bc, $ such that
$$\uno\triangleleft \uno\simeq \uno,$$
and there are natural isomorphisms
$l_{B,X}: B \triangleleft X\to B\ot (\uno \triangleleft X),$
such that for any $X, Y\in \vc$, $B\in \Bc$


\begin{equation}\label{tens-acting0r}  l_{ B,\uno}=\id_B, \quad l_{\uno, X}=\id_{\uno \triangleleft X },
\end{equation}
\begin{equation}\label{tens-acting2}  
            \begin{tikzpicture}[commutative diagrams/every diagram]
            \node (P1) at (180:5cm) 
            {$(B\triangleleft X)\triangleleft Y$};
            \node (P2) at (180-51:5cm) 
            {$(B\triangleleft X)\otimes (\uno\triangleleft Y)$};
            \node (P3) at (180-51*2:5cm) 
            {$(B\otimes (\uno\triangleleft X))\otimes (\uno\triangleleft Y)$};
            \node (P4) at (180-51*3:5cm) 
            {$B\otimes ((\uno\triangleleft X)\otimes (\uno\triangleleft Y))$};
            
            \node (P5) at (180-51*4:5cm) 
            {$B\otimes ((\uno\triangleleft X)\triangleleft Y))$};
            \node (P6) at (180-51*5:5cm)
            {$B\otimes (\uno\triangleleft (X\otimes Y))$};
            \node (P7) at (180-51*6:5cm) 
            {$B\triangleleft (X\otimes Y)$};
\path[commutative diagrams/.cd, every arrow, every label]
            (P1) edge node [swap] {$l_{B\triangleleft X,Y}$} (P2)
            (P2) edge node [swap] {$l_{B,X}\ot \mathrm{id}_{\uno \triangleleft Y}$} (P3)
            (P3) edge node [swap] {\rotatebox{-31}{$\sim$}} (P4)
            
            (P1) edge node {$\tilde{m}_{B,X,Y}^{-1}$} (P7)
            (P7) edge node {$l_{B, X\ot Y}$} (P6)
            (P6) edge node {$\mathrm{id}_B\otimes\tilde{m}_{\uno,X,Y}$} (P5)
            (P5) edge node {$\id_B\ot l_{\uno \triangleleft X, Y}$} (P4); 
            \end{tikzpicture}
\end{equation}
\end{defi}


\begin{exa}\begin{itemize}
\item[(i)]  Any tensor category $\vc$ is a monoidal $\vect_\ku$-module category, with the canonical action
\begin{equation*}
 \bullet: \vect_\ku \times \vc\to \vc.
\end{equation*}

\item[(ii)] Let $\vc$ be a tensor category. Any tensor subcategory $\Do$ acts on  $\vc$ by
$$X \triangleright Y=X\ot Y.$$
In particular any tensor category acts on itself.
\item[(iii)] Let $(\vc, \sigma)$ be a braided tensor category and $\Do\subseteq \vc$ be a tensor subcategory. Then $\Do^{\rev}$ acts on  $\vc$ as
$$X \triangleright Y=Y\ot X.$$
In this case $l_{X,B}=\sigma_{B,X}$.

\item[(iv)] Let $\vc$ be a tensor category and $C\in\vc$ be a coalgebra. Then the category ${}^C\vc$, of left $C$-comodules in $\vc$, is a right $\vc$-module category. The action is given as follows. If $(W,\rho)\in {}^C\vc$, then $W \triangleleft Y=W\ot Y$, where the coaction on $W\ot Y$ is given by $\rho\ot \id_Y.$

\end{itemize} 
\end{exa} 


\begin{defi} If $\Bc$, $\Bc'$ are right monoidal $\vc$-module categories,   a \textit{monoidal module functor} is a collection  $(F,c,\xi):\Bc\to \Bc'$ where $(F,c)$ is a $\ca$-module functor, $(F, \xi)$ is a monoidal functor and equation \begin{equation}\label{monoidal-mod-functor} l_{F(B),V}\, c_{B,V}= (\id_{F(B)}\ot c_{\uno, V}) \xi^{-1}_{B, \uno \triangleleft V} F(l_{B,V}),
\end{equation}
is fulfilled, for any $B\in \Bc$, $V\in \ca$.
\end{defi}
