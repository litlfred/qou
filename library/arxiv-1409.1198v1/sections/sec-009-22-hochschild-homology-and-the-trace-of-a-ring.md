---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-009-22-hochschild-homology-and-the-trace-of-a-ring
section_title: "Hochschild homology and the trace of a ring"
section_number: 2.2
pages: 9-13
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.907
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
\label{subsec_HH0ring}



In this section we will explain how the Hochschild homology of a ring $R$ can be viewed as ``trace" of the ring $R$. Recall that for a ring $R$, the Hochschild homology $\HH_*(R)$ of $R$
can be defined as the homology of the Hochschild complex (see \cite{Mitchell,Loday}):
$$
C_{\bullet}=C_{\bullet}(R):\quad \quad \dots\longrightarrow C_n \xto{d_n} C_{n-1} \xto{d_{n-1}} \dots \xto{d_2} C_1 \xto{d_1} C_0 \longrightarrow 0,
$$
where $C_n(R)=R^{\otimes n+1}$ and
$$
d_n(a_0\otimes\dots\otimes
a_n):=\sum_{i=0}^{n-1}(-1)^ia_0\otimes\dots\otimes
a_ia_{i+1}\otimes\dots\otimes a_n+
(-1)^na_na_0\otimes a_1\otimes\dots\otimes a_{n-1}
$$
for $a_0,\ldots ,a_{n-1}\in R$.

\begin{exercise}
Show that the zeroth Hochschild homology of the ring $R$ is isomorphic to the quotient of $R$ by the commutator subgroup,
\[
\HH_0(R) \cong R/[R,R].
\]
In particular, $\HH_0(R) \cong R$ for any commutative ring $R$.
\end{exercise}


\begin{exercise}\label{mat}
If $\Mat_n(R)$ denotes the ring of $n \times n$ dimensional matrices with coefficients in $R$, show that
\[
\HH_0(\Mat_n(R) ) \cong \HH_0(R).
\] Hint: consider exercise~\ref{ex-1}.
\end{exercise}




\subsubsection{Diagrammatics for zeroth Hochschild homology}



Many interesting rings $R$ can be represented by diagrams in the plane modulo some local relations.  Multiplication in $R$ is represented by stacking diagrams on top of each other:
\[
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (-.55,0) -- (-.55,1.5);
    \draw[very thick] (0,0) -- (0,1.5);
    \draw[very thick] (.55,0) -- (.55,1.5);
    \draw[fill=red!20,] (-.8,.5) rectangle (.8,1);
    \node () at (0,.75) {$a$};
\end{tikzpicture}}
\;\;
\circ \;\;
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (-.55,0) -- (-.55,1.5);
    \draw[very thick] (0,0) -- (0,1.5);
    \draw[very thick] (.55,0) -- (.55,1.5);
    \draw[fill=red!20,] (-.8,.5) rectangle (.8,1);
    \node () at (0,.75) {$b$};
\end{tikzpicture}}
\;\; = \;\;
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (-.55,0) -- (-.55,2.5);
    \draw[very thick] (0,0) -- (0,2.5);
    \draw[very thick] (.55,0) -- (.55,2.5);
    \draw[fill=red!20,] (-.8,.5) rectangle (.8,1);
    \draw[fill=red!20,] (-.8,1.5) rectangle (.8,2);
    \node () at (0,.75) {$b$};
    \node () at (0,1.75) {$a$};
\end{tikzpicture}}
\]
for $a,b \in R$.  Then $\HH_0(R)$ can be described by diagrams on the annulus, modulo the same local relations
as those for $R$ and the map
\[
 R \longrightarrow R/[R,R]
\]
is given on diagrams by
\[
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (-.55,0) -- (-.55,1.5);
    \draw[very thick] (0,0) -- (0,1.5);
    \draw[very thick] (.55,0) -- (.55,1.5);
    \draw[fill=red!20,] (-.8,.5) rectangle (.8,1);
    \node () at (0,.75) {$a$};
\end{tikzpicture}}
\quad \mapsto
\quad
\hackcenter{\begin{tikzpicture}
      \path[draw,blue, very thick, fill=blue!10]
        (-2.3,-.6) to (-2.3,.6) .. controls ++(0,1.85) and ++(0,1.85) .. (2.3,.6)
         to (2.3,-.6)  .. controls ++(0,-1.85) and ++(0,-1.85) .. (-2.3,-.6);
        \path[draw, blue, very thick, fill=white]
            (-0.2,0) .. controls ++(0,.35) and ++(0,.35) .. (0.2,0)
            .. controls ++(0,-.35) and ++(0,-.35) .. (-0.2,0);
      
    \draw[very thick] (-1.65,-.7) -- (-1.65, .7).. controls ++(0,.95) and ++(0,.95) .. (1.65,.7)
        to (1.65,-.7) .. controls ++(0,-.95) and ++(0,-.95) .. (-1.65,-.7);
    \draw[very thick] (-1.1,-.55) -- (-1.1,.55) .. controls ++(0,.65) and ++(0,.65) .. (1.1,.55)
        to (1.1,-.55) .. controls ++(0,-.65) and ++(0,-.65) .. (-1.1, -.55);
    \draw[very thick] (-.55,-.4) -- (-.55,.4) .. controls ++(0,.35) and ++(0,.35) .. (.55,.4)
        to (.55, -.4) .. controls ++(0,-.35) and ++(0,-.35) .. (-.55,-.4);
    \draw[fill=red!20,] (-1.8,-.25) rectangle (-.4,.25);
    \node () at (-1,0) {$a$};
\end{tikzpicture}}
 \]

Notice that by sliding elements of $R$ around the annulus we see that $ab=ba$ in the quotient $\HH_0(R)$. Thus, the Hochschild homology of a ring $R$ exhibits similar properties to the trace of a linear map.

This method can be applied to Hecke algebras $H_{n,q}$ and their degenerations (0-Hecke algebras, nilCoxeter algebras) for a diagrammatic description of their Hochschild homology $\HH_0$~\cite{Brichard}.  In the next section we will use it to study $\HH_0$ of the nilHecke algebra.






\subsubsection{Example calculations} \label{sample}



The nilHecke ring $\NH_n$ is the graded unital associative ring generated by elements $x_1,\ldots,x_n$ of degree 2 and elements $\partial_1,\ldots,\partial_{n-1}$ of degree $-2$, subject to the relations
\begin{equation}\begin{split} \label{eq_rel_nilHecke}
&\partial_i^2=0,\qquad\partial_i\partial_{i+1}\partial_i=\partial_{i+1}\partial_i\partial_{i+1}\\
&x_i\partial_i-\partial_ix_{i+1}=1,\qquad\partial_ix_i-x_{i+1}\partial_i=1\\
&x_ix_j =x_jx_i \quad(i\neq j),\qquad\partial_i\partial_j =\partial_j\partial_i \quad(|i-j|>1),\\
&x_i\partial_j =\partial_jx_i  \quad(|i-j|>1).
\end{split}\end{equation}

The ring $\NH_n$ has graphical presentation via $n$-stranded planar diagrams, generated by dots and crossings, modulo planar isotopies and certain local relations.  In the graphical depiction of $\NH_n$ a dot on the $i$th strand corresponds to a generator $x_i$, while a crossing of the $i$ and $i+1$st strand represents $\partial_i$.  Then we impose local relations
\begin{equation}
\vcenter{
\xy 0;/r.17pc/:
	(-4,-4)*{};(4,4)*{} **\crv{(-4,-1) & (4,1)}?(1)*\dir{};
	(4,-4)*{};(-4,4)*{} **\crv{(4,-1) & (-4,1)}?(1)*\dir{};
	(-4,4)*{};(4,12)*{} **\crv{(-4,7) & (4,9)}?(1)*\dir{};
	(4,4)*{};(-4,12)*{} **\crv{(4,7) & (-4,9)}?(1)*\dir{};
	(-4,12); (-4,13) **\dir{-}?(1)*\dir{};
	(4,12); (4,13) **\dir{-}?(1)*\dir{};
	
\endxy}
 \;\; =\;\; 0, \qquad \quad
\vcenter{\xy 0;/r.17pc/:
    (-4,-4)*{};(4,4)*{} **\crv{(-4,-1) & (4,1)}?(1)*\dir{};
    (4,-4)*{};(-4,4)*{} **\crv{(4,-1) & (-4,1)}?(1)*\dir{};
    (4,4)*{};(12,12)*{} **\crv{(4,7) & (12,9)}?(1)*\dir{};
    (12,4)*{};(4,12)*{} **\crv{(12,7) & (4,9)}?(1)*\dir{};
    (-4,12)*{};(4,20)*{} **\crv{(-4,15) & (4,17)}?(1)*\dir{};
    (4,12)*{};(-4,20)*{} **\crv{(4,15) & (-4,17)}?(1)*\dir{};
    (-4,4)*{}; (-4,12) **\dir{-};
    (12,-4)*{}; (12,4) **\dir{-};
    (12,12)*{}; (12,20) **\dir{-};
    (4,20); (4,21) **\dir{-}?(1)*\dir{};
    (-4,20); (-4,21) **\dir{-}?(1)*\dir{};
    (12,20); (12,21) **\dir{-}?(1)*\dir{};
   
\endxy}
 \;\; =\;\;
\vcenter{\xy 0;/r.17pc/:
    (4,-4)*{};(-4,4)*{} **\crv{(4,-1) & (-4,1)}?(1)*\dir{};
    (-4,-4)*{};(4,4)*{} **\crv{(-4,-1) & (4,1)}?(1)*\dir{};
    (-4,4)*{};(-12,12)*{} **\crv{(-4,7) & (-12,9)}?(1)*\dir{};
    (-12,4)*{};(-4,12)*{} **\crv{(-12,7) & (-4,9)}?(1)*\dir{};
    (4,12)*{};(-4,20)*{} **\crv{(4,15) & (-4,17)}?(1)*\dir{};
    (-4,12)*{};(4,20)*{} **\crv{(-4,15) & (4,17)}?(1)*\dir{};
    (4,4)*{}; (4,12) **\dir{-};
    (-12,-4)*{}; (-12,4) **\dir{-};
    (-12,12)*{}; (-12,20) **\dir{-};
    (4,20); (4,21) **\dir{-}?(1)*\dir{};
    (-4,20); (-4,21) **\dir{-}?(1)*\dir{};
    (-12,20); (-12,21) **\dir{-}?(1)*\dir{};
  
\endxy}
 \label{eq_nil_rels}
  \end{equation}
\begin{equation}
 \xy 0;/r.18pc/:
  (4,6);(4,-4) **\dir{-}?(0)*\dir{}+(2.3,0)*{};
  (-4,6);(-4,-4) **\dir{-}?(0)*\dir{}+(2.3,0)*{};
  
 \endxy
 \quad =
\xy 0;/r.18pc/:
  (0,0)*{\xybox{
    (-4,-4)*{};(4,6)*{} **\crv{(-4,-1) & (4,1)}?(1)*\dir{}?(.25)*{\bullet};
    (4,-4)*{};(-4,6)*{} **\crv{(4,-1) & (-4,1)}?(1)*\dir{};
    
     (-10,0)*{};(10,0)*{};
     }};
  \endxy
 \;\; -
\xy 0;/r.18pc/:
  (0,0)*{\xybox{
    (-4,-4)*{};(4,6)*{} **\crv{(-4,-1) & (4,1)}?(1)*\dir{}?(.75)*{\bullet};
    (4,-4)*{};(-4,6)*{} **\crv{(4,-1) & (-4,1)}?(1)*\dir{};
   
     (-10,0)*{};(10,0)*{};
     }};
  \endxy
 \;\; =
\xy 0;/r.18pc/:
  (0,0)*{\xybox{
    (-4,-4)*{};(4,6)*{} **\crv{(-4,-1) & (4,1)}?(1)*\dir{};
    (4,-4)*{};(-4,6)*{} **\crv{(4,-1) & (-4,1)}?(1)*\dir{}?(.75)*{\bullet};
 
     (-10,0)*{};(10,0)*{};
     }};
  \endxy
 \;\; -
  \xy 0;/r.18pc/:
  (0,0)*{\xybox{
    (-4,-4)*{};(4,6)*{} **\crv{(-4,-1) & (4,1)}?(1)*\dir{} ;
    (4,-4)*{};(-4,6)*{} **\crv{(4,-1) & (-4,1)}?(1)*\dir{}?(.25)*{\bullet};
 
     (-10,0)*{};(10,0)*{};
     }};
  \endxy \label{eq_nil_dotslide}
\end{equation}



By \cite[Section 2.5]{KLMS}, the nilHecke ring
$\NH_n$ is isomorphic to the $n!\times n!$ matrix algebra ${\rm Mat}(n!,\sym_n)$
with coefficients in the ring $\sym_n$ of symmetric polynomials in $n$ variables,
\begin{equation}
  \sym_n \cong \Z[x_1, \dots, x_n]^{S_n}.
\end{equation}
Hence, by exercise~\ref{mat} it follows that $\Tr(\NH_n) \cong \sym_n$. The isomorphism between $\NH_n$ and the matrix algebra holds in the graded case, with $n!$ replaced by the non-symmetric quantum factorial $(n)^!_{q^2}:=(n)_{q^2} (n-1)_{q^2} \dots (1)_{q^2}$ where $(n)_{q^2}=(1-q^{2n})/(1-q^2)$, and with each variable of $\sym_n$ assigned degree $2$.


Let us illustrate the isomorphism
$\Tr(\NH_n) \cong \sym_n$ of graded abelian groups by some computations:
  \begin{enumerate}
  \item The diagram $ \xy 0;/r.18pc/:
   (8,0)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.4,-.6) to (-1.4,.6) .. controls ++(0,1.15) and ++(0,1.15) ..
   (1.4,.6)
   to (1.4,-.6)  .. controls ++(0,-1.15) and ++(0,-1.15) ..
   (-1.4,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
\end{tikzpicture}}
 };
 
  (8,8)*{\lcap};
 (8,6)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};
 (12,0)*{\sline}; (20,0)*{\sline}; (8,-10)*{\lcup};

 \endxy\;$
 has degree $-2$.  $\sym_n$ is non-negatively
  graded, so this diagram should be 0 in $\Tr$.  Indeed, we have
\begin{align}
 \xy 0;/r.16pc/:
   (8,0)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.2,-.6) to (-1.2,.6) .. controls ++(0,1) and ++(0,1) ..
   (1.2,.6)
   to (1.2,-.6)  .. controls ++(0,-1) and ++(0,-1) ..
   (-1.2,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
  \end{tikzpicture}}
 };

  (8,8)*{\lcap};
 (8,6)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};
 (12,0)*{\sline};
 (20,0)*{\sline};
 (8,-10)*{\lcup};
 

 \endxy
  \;\;
 =
  \;\;
 \vcenter{ \xy 0;/r.16pc/:
    (8,4)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.4,-.6) to (-1.4,.6) .. controls ++(0,1.15) and ++(0,1.15) ..
   (1.4,.6)
   to (1.4,-.6)  .. controls ++(0,-1.15) and ++(0,-1.15) ..
   (-1.4,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
  \end{tikzpicture}}
 };

  (8,16)*{\lcap};
 (8,14)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};(0,8)*{\naecross};
 (12,4)*{\mline};
 (20,4)*{\mline};
 (8,-10)*{\lcup};
 (-2.8,6)*{\bullet};
 
 
 \endxy}
  \;\; = \;\;
  \vcenter{ \xy 0;/r.16pc/:
   (8,0)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.2,-.6) to (-1.2,.6) .. controls ++(0,1) and ++(0,1) ..
   (1.2,.6)
   to (1.2,-.6)  .. controls ++(0,-1) and ++(0,-1) ..
   (-1.2,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (8,8)*{\lcap};
 (8,6)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};(16,0)*{\naecross};
 (8,-10)*{\lcup};
(-2.5,1.5)*{\bullet};


 \endxy}   \;\; = \;
\vcenter{ \xy 0;/r.16pc/:
    (8,4)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.4,-.6) to (-1.4,.6) .. controls ++(0,1.15) and ++(0,1.15) ..
   (1.4,.6)
   to (1.4,-.6)  .. controls ++(0,-1.15) and ++(0,-1.15) ..
   (-1.4,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (8,16)*{\lcap};
 (8,14)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};(0,8)*{\naecross};
 (12,4)*{\mline};
 (20,4)*{\mline};
 (8,-10)*{\lcup};
 (-2.5,9.5)*{\bullet};
 

 \endxy}   \;\;\refequal{\eqref{eq_nil_rels}} \;
  0, \label{eq_bubble_rel_zero}
\end{align}
where the first equality follows from a combination of \eqref{eq_nil_dotslide} and the first equality in \eqref{eq_nil_rels}.

 \item The degree 0 part of $\Tr(\NH_2)$ is spanned by $ \xy 0;/r.16pc/:
   (8,0)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.2,-.6) to (-1.2,.6) .. controls ++(0,1) and ++(0,1) ..
   (1.2,.6)
   to (1.2,-.6)  .. controls ++(0,-1) and ++(0,-1) ..
   (-1.2,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (8,8)*{\lcap};
 (8,6)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};
 (12,0)*{\sline};
 (20,0)*{\sline};
 (8,-10)*{\lcup};
 (-3.3,6)*{\bullet};
 
 \endxy\;$.
 We have
\begin{center}
\makebox[0pt]{$
 \xy 0;/r.16pc/:
   (8,0)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.2,-.6) to (-1.2,.6) .. controls ++(0,1) and ++(0,1) ..
   (1.2,.6)
   to (1.2,-.6)  .. controls ++(0,-1) and ++(0,-1) ..
   (-1.2,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (8,8)*{\lcap};
 (8,6)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};
 (12,0)*{\sline};
 (20,0)*{\sline};
 (8,-10)*{\lcup};
 (-3.3,6)*{\bullet};
 
 
 \endxy
  \; \refequal{\eqref{eq_nil_dotslide}}  -
  \vcenter{ \xy 0;/r.16pc/:
    (8,4)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.4,-.6) to (-1.4,.6) .. controls ++(0,1.15) and ++(0,1.15) ..
   (1.4,.6)
   to (1.4,-.6)  .. controls ++(0,-1.15) and ++(0,-1.15) ..
   (-1.4,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (8,16)*{\lcap};
 (8,14)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};(0,8)*{\naecross};
 (12,4)*{\mline};
 (20,4)*{\mline};
 (8,-10)*{\lcup};
 (-3.3,14)*{\bullet};(3.2,6)*{\bullet};
 
  
 \endxy}
  \;=
\; - \vcenter{ \xy 0;/r.16pc/:
   (8,0)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.2,-.6) to (-1.2,.6) .. controls ++(0,1) and ++(0,1) ..
   (1.2,.6)
   to (1.2,-.6)  .. controls ++(0,-1) and ++(0,-1) ..
   (-1.2,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (8,8)*{\lcap};
 (8,6)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};(16,0)*{\naecross};
 (8,-10)*{\lcup};
 (18.3,-1.5)*{\bullet};(2.7,1.5)*{\bullet};
 
 \endxy}   \; =
\; - \vcenter{ \xy 0;/r.18pc/:
    (8,4)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.4,-.6) to (-1.4,.6) .. controls ++(0,1.15) and ++(0,1.15) ..
   (1.4,.6)
   to (1.4,-.6)  .. controls ++(0,-1.15) and ++(0,-1.15) ..
   (-1.4,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (8,16)*{\lcap};
 (8,14)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};(0,8)*{\naecross};
 (12,4)*{\mline};
 (20,4)*{\mline};
 (8,-10)*{\lcup};
 (2.8,9.5)*{\bullet};(-2.8,6)*{\bullet};
 
 \endxy}   \; =
  -\;\xy 0;/r.16pc/:
   (8,0)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.2,-.6) to (-1.2,.6) .. controls ++(0,1) and ++(0,1) ..
   (1.2,.6)
   to (1.2,-.6)  .. controls ++(0,-1) and ++(0,-1) ..
   (-1.2,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (8,8)*{\lcap};
 (8,6)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};
 (12,0)*{\sline};
 (20,0)*{\sline};
 (8,-10)*{\lcup};
 (2.8,1.5)*{\bullet};
 
 \endxy
$ }
\end{center}
\begin{equation}
 \label{eq_bubble_rel}
\end{equation}
 which implies
\begin{equation}
 \xy 0;/r.16pc/:
   (8,0)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.2,-.6) to (-1.2,.6) .. controls ++(0,1) and ++(0,1) ..
   (1.2,.6)
   to (1.2,-.6)  .. controls ++(0,-1) and ++(0,-1) ..
   (-1.2,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (8,8)*{\lcap};
 (8,6)*{\scap};
 (8,-6)*{\scup};
(-4,0)*{\sline};
 (4,0)*{\sline};
 (12,0)*{\sline};
 (20,0)*{\sline};
 (8,-10)*{\lcup};
 (-3.3,6)*{};
 
 \endxy
  \;\; = \;\; \vcenter{
    \xy 0;/r.16pc/:
   (0,-4)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.2,-.6) to (-1.2,.6) .. controls ++(0,1) and ++(0,1) ..
   (1.2,.6)
   to (1.2,-.6)  .. controls ++(0,-1) and ++(0,-1) ..
   (-1.2,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (-8,-4)*{\naecross};(4,-4)*{\sline};(12,-4)*{\sline};
  (0,2)*{\scap};(0,4)*{\lcap};
  (0,-10)*{\scup};(0,-14)*{\lcup};
  (-9.8,-3)*{\bullet};
  \endxy}
  \;\; - \;\;
  \vcenter{
    \xy 0;/r.16pc/:
   (0,-4)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.2,-.6) to (-1.2,.6) .. controls ++(0,1) and ++(0,1) ..
   (1.2,.6)
   to (1.2,-.6)  .. controls ++(0,-1) and ++(0,-1) ..
   (-1.2,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (-8,-4)*{\naecross};(4,-4)*{\sline};(12,-4)*{\sline};
  (0,2)*{\scap};(0,4)*{\lcap};
  (0,-10)*{\scup};(0,-14)*{\lcup};
  (-4.8,-6)*{\bullet};
  \endxy}
  \;\;\refequal{\eqref{eq_bubble_rel}}\;\;
  2  \;   \vcenter{\xy 0;/r.16pc/:
    (0,-4)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-1.2,-.6) to (-1.2,.6) .. controls ++(0,1) and ++(0,1) ..
   (1.2,.6)
   to (1.2,-.6)  .. controls ++(0,-1) and ++(0,-1) ..
   (-1.2,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.3) and ++(0,.3) .. (0.15,0)
            .. controls ++(0,-.3) and ++(0,-.3) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (-8,-4)*{\naecross};(4,-4)*{\sline};(12,-4)*{\sline};
  (0,2)*{\scap};(0,4)*{\lcap};
  (0,-10)*{\scup};(0,-14)*{\lcup};
  (-9.8,-3)*{\bullet};
  \endxy}
\end{equation}
  \end{enumerate}


More generally, the element
\begin{equation}
  e_n = \xy 0;/r.15pc/:
 (-12,-20)*{}; (12,20) **\crv{(-12,-8) & (12,8)}?(1)*\dir{>};
 (-4,-20)*{}; (4,20) **\crv{(-4,-13) & (12,2) & (12,8)&(4,13)}?(1)*\dir{>};?(.88)*\dir{}+(0.1,0)*{\bullet};
 (4,-20)*{}; (-4,20) **\crv{(4,-13) & (12,-8) & (12,-2)&(-4,13)}?(1)*\dir{>}?(.86)*\dir{}+(0.1,0)*{\bullet};
 ?(.92)*\dir{}+(0.1,0)*{\bullet};
 (12,-20)*{}; (-12,20) **\crv{(12,-8) & (-12,8)}?(1)*\dir{>}?(.70)*\dir{}+(0.1,0)*{\bullet};
 ?(.90)*\dir{}+(0.1,0)*{\bullet};?(.80)*\dir{}+(0.1,0)*{\bullet};
 \endxy
\end{equation}
(shown for $n=4$) is a minimal idempotent in $\NH_n$.  The composition
\begin{equation}
 \xymatrix{
 \sym_n  \ar@{^{(}->}[r] & \NH_n  \ar[r]& \Tr(\NH_n) \\ a \ar@{|->}[r] & a e_n &}
\end{equation}
is a grading-preserving isomorphism of abelian groups.
In particular, any basis of $\sym_n$ gives a basis of $\Tr(\NH_n)$.
Taking the basis $\{\epsilon_{\lambda}\}_{\lambda}$ of $\sym_n$, over all partitions with at
most $n$ parts, $\lambda=(\lambda_1,\dots, \lambda_n)$, $\lambda_1 \geq \dots
\geq \lambda_n$, $\epsilon_{\lambda} = \epsilon_{\lambda_1}\dots
\epsilon_{\lambda_n}$, $\epsilon_k$ the $k$-th elementary symmetric function,
gives us a basis of $\Tr(\NH_n)$.

Let $x^{\lambda}=x_1^{\lambda_1}\dots x_n^{\lambda_n} \in \NH_n$.

\begin{prop}[\cite{BHLZ}]
The image of $\{ x^{\lambda} e_n \}_{\lambda}$ with $\lambda$ as above is a basis
of $\Tr(\NH_n)$.
\end{prop}


We call this basis the standard basis of $\Tr(\NH_n)$.

\begin{problem}
 Determine the coefficients of inclusions $\xymatrix{\NH_{n_1} \otimes \NH_{n_2} \ar@{^{(}->}[r]^{i} &
\Tr(\NH_{n_1+n_2})  }$ in the standard basis.
\end{problem}





\subsubsection{Zeroth Hochschild cohomology} \label{subsec_HHco}




The zeroth Hochschild cohomology $\HH^0(R)$ of a ring $R$ can be identified with the center of $R$,
\[
 \HH^0(R) \cong Z(R) .
\]
The Hochschild cohomology is naturally a module over the Hochschild homology.  This action has a nice graphical interpretation as well.  The action of $Z(R)$ on $\HH_0(R)$ can be graphically understood by cutting the diagram of an element $b \in \HH_0(R)$ along any ray emanating from the origin and inserting the diagram of $a\in Z(R)$ there:
\[ a\quad\rhd\quad
\hackcenter{\begin{tikzpicture}
      \path[draw,blue, very thick, fill=blue!10]
        (-2.3,-.6) to (-2.3,1.1) .. controls ++(0,1.85) and ++(0,1.85) .. (2.3,1.1)
         to (2.3,-.6)  .. controls ++(0,-1.85) and ++(0,-1.85) .. (-2.3,-.6);
      
    \draw[very thick] (-1.65,-.7) -- (-1.65, 1.2).. controls ++(0,.95) and ++(0,.95) .. (1.65,1.2)
        to (1.65,-.7) .. controls ++(0,-.95) and ++(0,-.95) .. (-1.65,-.7);
    \draw[very thick] (-1.1,-.55) -- (-1.1,1.05) .. controls ++(0,.65) and ++(0,.65) .. (1.1,1.05)
        to (1.1,-.55) .. controls ++(0,-.65) and ++(0,-.65) .. (-1.1, -.55);
    \draw[very thick] (-.55,-.4) -- (-.55,.9) .. controls ++(0,.35) and ++(0,.35) .. (.55,.9)
        to (.55, -.4) .. controls ++(0,-.35) and ++(0,-.35) .. (-.55,-.4);
    \draw[fill=red!20,] (-1.8,-.25) rectangle (-.4,.25);
    \node () at (-1,0) {$b$};
    
   \draw[very thick, red, dashed] (0,.25) -- (-2.3,2.3);
            \path[draw, blue, very thick, fill=white]
            (-0.2,.25) .. controls ++(0,.35) and ++(0,.35) .. (0.2,.25)
            .. controls ++(0,-.35) and ++(0,-.35) .. (-0.2,.25);
\end{tikzpicture}}
\qquad  =\qquad
\hackcenter{\begin{tikzpicture}
      \path[draw,blue, very thick, fill=blue!10]
        (-2.3,-.6) to (-2.3,1.1) .. controls ++(0,1.85) and ++(0,1.85) .. (2.3,1.1)
         to (2.3,-.6)  .. controls ++(0,-1.85) and ++(0,-1.85) .. (-2.3,-.6);
      
    \draw[very thick] (-1.65,-.7) -- (-1.65, 1.2).. controls ++(0,.95) and ++(0,.95) .. (1.65,1.2)
        to (1.65,-.7) .. controls ++(0,-.95) and ++(0,-.95) .. (-1.65,-.7);
    \draw[very thick] (-1.1,-.55) -- (-1.1,1.05) .. controls ++(0,.65) and ++(0,.65) .. (1.1,1.05)
        to (1.1,-.55) .. controls ++(0,-.65) and ++(0,-.65) .. (-1.1, -.55);
    \draw[very thick] (-.55,-.4) -- (-.55,.9) .. controls ++(0,.35) and ++(0,.35) .. (.55,.9)
        to (.55, -.4) .. controls ++(0,-.35) and ++(0,-.35) .. (-.55,-.4);
    \draw[fill=red!20,] (-1.8,-.25) rectangle (-.4,.25);
    \node () at (-1,0) {$b$};
      \draw[fill=red!20,] (-1.8,.5) rectangle (-.4,1);
    \node () at (-1,0) {$b$};\node () at (-1,.75) {$a$};
    
            \path[draw, blue, very thick, fill=white]
            (-0.2,.25) .. controls ++(0,.35) and ++(0,.35) .. (0.2,.25)
            .. controls ++(0,-.35) and ++(0,-.35) .. (-0.2,.25);
\end{tikzpicture}}
\]

In section~\ref{action} we study an extension of this relationship between Hochschild homology and cohomology.
