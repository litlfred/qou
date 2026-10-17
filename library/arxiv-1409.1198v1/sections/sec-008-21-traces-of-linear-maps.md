---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-008-21-traces-of-linear-maps
section_title: "Traces of linear maps"
section_number: 2.1
pages: 7-9
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.945
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
In this section we recall the definition and properties of the trace
for any linear endomorphism. Throughout this paper $\k$ is assumed to be a field.

The trace of an $n \times n$ matrix $M=\{M_{ij}\}_{1 \leq i,j,\leq n}$ is the sum of its diagonal entries $\sum_{i} M_{ii}$.
Given two square matrices
$A,B$, the trace satisfies the {\em trace property}
\begin{equation} \label{trace-property}\tr(AB)=\tr(BA)\, .
\end{equation}



\begin{exercise}\label{ex-1} Show that
 property \eqref{trace-property} uniquely characterize the trace
in the following sense:
Two linear functions on the space of matrices satisfying
\eqref{trace-property} are proportional. Hint: any non-diagonal elementary
matrix   can be written as a commutator, i.e. $E_{ij}=[E_{ii}, E_{ij}]$.
\end{exercise}


More generally, for any finite-dimensional $\k$-vector space $V$, trace is a linear map
 $$ \tr: \End_{\k}(V) \to \k$$
such that the {\it trace relation} holds:
$$
\tr (fg)=\tr (gf)\quad\text{for any}\quad f,g \in \End_{\k}(V)\, .$$


\begin{exercise}
Show that this (basis independent) definition of the trace coincides with the usual one, where
 the trace of a matrix representing $f$ in some basis is taken.
Hint: use Exercise \ref{ex-1}.
\end{exercise}


As a simple  invariant of any linear endomorphism, the trace has a variety of
important applications. Let us just mention few of them.
\begin{itemize}
 \item  For any representation $\phi: G\to {\rm Aut}_{\k}(V)$ of a group $G$,
the character $\chi_{\phi} \maps G \to \k$ of the representation $\phi$ is the function sending each group element $g\in G$ to the trace of $\phi(g)$.  The character of a representation carries much of the essential information about a representation.  In particular, for $G$ a finite group and $\k=\mathbb{C}$, the complex representations of $G$ are determined up to isomorphism by their characters.



 \item  A Lie algebra $\g$ defined over $\k$ acts on itself via the adjoint action sending $x \in \g$ to the endomorphism ${\rm ad}_x$ defined by ${\rm ad}_x(y)=[x,y]$ for all $y \in \g$.  When $\g$ is finite dimensional, there is a symmetric bilinear form (or Killing form) $B: \g \times \g \to \k$ defined by $B(x,y):= \tr({\rm ad}_x{\rm ad}_y)$.  The non-degeneracy of this form is used to determine if a Lie algebra is semisimple.


\item In topology Markov trace is used to construct link invariants out of
representations of braid groups.
\end{itemize}





\subsubsection{Diagrammatics for the trace}\label{tr-diag}





The category $\cat{Vect}_{\k}$ has the structure of a pivotal monoidal category.   What this means is that this category admits a surprisingly rich diagrammatic calculus.  In this calculus, edges are labelled by finite dimensional vector spaces and planar diagrams  represent linear maps between the tensor product of vector spaces labelling the bottom strands to the tensor product of vector spaces labelling the top strands.
\[
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (-1,1.75) [out=-90, in=150] to (0,.75);
    \draw[very thick] (1,1.75) [out=-90, in=30] to (0,.75);
    \draw[very thick] (-.5,-.25) [out=90, in=210] to (0,.75);
    \draw[very thick] (.5,-.25) [out=90, in=-30] to (0,.75);
    \draw[very thick] (0,1.75) -- (0,.75);
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,.75) {$f$};
    \node () at (.75,-.15) {$V_2$};
    \node () at (-.75,-.15) {$V_1$};
    \node () at (-1.25,1.6) {$W_1$};
    \node () at (1.25,1.6) {$W_2$};
    \node () at (.3,1.6) {$W_3$};
\end{tikzpicture}}
\qquad f \maps V_1 \otimes V_2 \longrightarrow W_1 \otimes W_2 \otimes W_3.
\]
In this graphical calculus the ground field $\k$ is depicted by the empty strand.  The ability to compose linear maps and to tensor linear maps is reflected in the graphical calculus by stacking the diagrams on top of each other and juxtaposing them side by side, respectively.

The ``pivotal" structure on the category $\cat{Vect}_{\k}$ of finite-dimensional vector spaces indicates the existence of certain diagrams in the graphical calculus.  To be concrete, fix a basis $\{ e_1, \dots , e_n\}$ of the vector space $V$.  Denote by $\{e_1^{\ast}, \dots, e_n^{\ast} \}$ the basis for the dual space $V^{\ast} = \Hom(V, \k)$, with $e_i^{\ast}(e_j) = \delta_{ij}$. Then there are linear maps
\[
 \hackcenter{\begin{tikzpicture}
    \draw [very thick] (0,.5) to (0,1) .. controls ++(0,.35) and ++(0,.35) .. (1,1) to (1,.5);
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (.5,1.25) {$ev$};
      \node () at (-.35,.65) {$V^{\ast}$};
        \node () at (1.25,.65) {$V$};
\end{tikzpicture}}
\qquad
\begin{array}{c}
  ev \maps V^{\ast} \otimes V \to \k \\
  e_i^{\ast} \otimes e_j \mapsto e_i^{\ast}(e_j)
\end{array}
\qquad \qquad
 \hackcenter{\begin{tikzpicture}
    \draw [very thick] (0,.5) to (0,0) .. controls ++(0,-.35) and ++(0,-.35) .. (1,0) to (1,.5);
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (.5,-.25) {$coev$};
     \node () at (-.35,.35) {$V$};
        \node () at (1.25,.35) {$V^{\ast}$};
\end{tikzpicture}}
\qquad
\begin{array}{c}
  coev \maps \k \to V\otimes V^{\ast} . \\
  1  \mapsto \sum_i e_i \otimes e_i^{\ast}
\end{array}
\]


\begin{exercise}
Prove that the maps $ev$ and $coev$ satisfy the following identities
\[
 (\Id_V \otimes ev) \circ (coev \otimes \Id_V) = \Id_V, \quad \text{and} \quad
 (ev \otimes \Id_{V^{\ast}})\circ (\Id_{V^{\ast}} \otimes coev) = \Id_{V^{\ast}}
\]
and depict these relations in the graphical calculus described above.
\end{exercise}


It is common practice in this diagrammatic calculus to simplify these diagrams
\[
 \hackcenter{\begin{tikzpicture}
    \draw [very thick] (0,.5) to (0,1) .. controls ++(0,.35) and ++(0,.35) .. (1,1) to (1,.5);
      \node () at (-.35,.65) {$V^{\ast}$};
        \node () at (1.25,.65) {$V$};
\end{tikzpicture}} \;\; :=\;\;
 \hackcenter{\begin{tikzpicture}
    \draw [very thick] (0,.5) to (0,1) .. controls ++(0,.35) and ++(0,.35) .. (1,1) to (1,.5);
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (.5,1.25) {$ev$};
      \node () at (-.35,.65) {$V^{\ast}$};
        \node () at (1.25,.65) {$V$};
\end{tikzpicture}}
\qquad \qquad
 \hackcenter{\begin{tikzpicture}
    \draw [very thick] (0,.5) to (0,0) .. controls ++(0,-.35) and ++(0,-.35) .. (1,0) to (1,.5);
     \node () at (-.35,.35) {$V$};
        \node () at (1.25,.35) {$V^{\ast}$};
\end{tikzpicture}} \;\; := \;\;
 \hackcenter{\begin{tikzpicture}
    \draw [very thick] (0,.5) to (0,0) .. controls ++(0,-.35) and ++(0,-.35) .. (1,0) to (1,.5);
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (.5,-.25) {$coev$};
     \node () at (-.35,.35) {$V$};
        \node () at (1.25,.35) {$V^{\ast}$};
\end{tikzpicture}}
\]
used to represent $ev$ and $coev$. Using the flip map in $\cat{Vect}_{\k}$
\[
 \hackcenter{\begin{tikzpicture}
    \draw [very thick] (0,0) to (1,1);
    \draw [very thick] (1,0) to (0,1);
     \node () at (-.25,.05) {$V$};
        \node () at (1.25,.05) {$W$};
        \node () at (-.25,.95) {$W$};
        \node () at (1.25,.95) {$V$};
\end{tikzpicture}}
\qquad
\begin{array}{rcc}
  \tau \maps V \otimes W &\to &W\otimes V  \\
   v \otimes w  &\mapsto  &w \otimes v,
   \end{array}
\]
we can also define other caps and caps
\[
 \hackcenter{\begin{tikzpicture}
    \draw [very thick] (0,.5) to (0,1) .. controls ++(0,.35) and ++(0,.35) .. (1,1) to (1,.5);
      \node () at (-.25,.65) {$V$};
        \node () at (1.35,.65) {$V^{\ast}$};
\end{tikzpicture}} \;\; :=\;\;
 \hackcenter{\begin{tikzpicture}
    \draw [very thick] (1,0) [out=90, in=-90] to (0,.7) to (0,1) .. controls ++(0,.35) and ++(0,.35) .. (1,1) to (1,.7) [out=-90, in=90] to (0,0);
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (.5,1.25) {$ev$};
      \node () at (-.25,.65) {$V^{\ast}$};
        \node () at (1.35,.65) {$V$};
\end{tikzpicture}}
\qquad \qquad
 \hackcenter{\begin{tikzpicture}
    \draw [very thick] (0,.5) to (0,0) .. controls ++(0,-.35) and ++(0,-.35) .. (1,0) to (1,.5);
     \node () at (-.25,.35) {$V^{\ast}$};
        \node () at (1.35,.35) {$V$};
\end{tikzpicture}} \;\; := \;\;
 \hackcenter{\begin{tikzpicture}
    \draw [very thick] (1,1) [out=-90, in=90] to (0,.3) to (0,0) .. controls ++(0,-.35) and ++(0,-.35) .. (1,0) to (1,.3) [out=90, in=-90] to (0,1);
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (.5,-.25) {$coev$};
     \node () at (-.35,.35) {$V$};
        \node () at (1.25,.35) {$V^{\ast}$};
\end{tikzpicture}}
\]

\begin{exercise}
Given a linear endomorphism $f:V\to V$ the following diagram
\[
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,1.5);
    \draw [very thick] (0,1.5) .. controls ++(0,.35) and ++(0,.35) .. (1,1.5) to (1,0)
    .. controls ++(0,-.35) and ++(0,-.35) .. (0,0);
     \node () at (-.25,.05) {$V$};
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,.75) {$f$};
\end{tikzpicture}}
\]
is multiplication by an element of the ground field $\k$.  Show that this element is exactly the trace of $f$.
\end{exercise}

Utilizing the evaluation and coevaluation map it is possible to dualize any map $f \maps V \to W$ to get a map $f^{\ast} \maps W^{\ast} \to V^{\ast}$.  Using these dual morphisms it is possible to slide linear maps through caps and cups
\[
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,1.5);
    \draw [very thick]  (1,1.5) to (1,0) .. controls ++(0,-.35) and ++(0,-.35) .. (0,0);
     \node () at (-.25,.05) {$V$};
       \node () at (-.35,1.25) {$W$};
       \node () at (1.35,1.25) {$V^{\ast}$};
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,.75) {$f$};
\end{tikzpicture}}
\;\; = \;\;
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,1.5);
    \draw [very thick]  (1,1.5) to (1,0) .. controls ++(0,-.35) and ++(0,-.35) .. (0,0);
     \node () at (1.35,.05) {$W^{\ast}$};
       \node () at (-.35,1.25) {$W$};
        \node () at (1.35,1.25) {$V^{\ast}$};
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (1,.75) {$f^{\ast}$};
\end{tikzpicture}}
\qquad \qquad
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,1.5);
    \draw [very thick] (0,1.5) .. controls ++(0,.35) and ++(0,.35) .. (1,1.5) to (1,0);
     \node () at (1.25,.1) {$V$};
     \node () at (-.35,1.25) {$W^{\ast}$};
     \node () at (1.25,1.25) {$W$};
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (1,.75) {$f$};
\end{tikzpicture}}
\;\; = \;\;
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,1.5);
    \draw [very thick] (0,1.5) .. controls ++(0,.35) and ++(0,.35) .. (1,1.5) to (1,0);
     \node () at (-.35,.1) {$W^{\ast}$};
     \node () at (-.35,1.25) {$V^{\ast}$};
     \node () at (1.35,1.25) {$V$};
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,.75) {$f^{\ast}$};
\end{tikzpicture}}
\]
Using these facts and the identification of $(V^{\ast})^{\ast}$ with $V$, it is not hard to verify the trace property:
\[
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,1.5);
    \draw [very thick] (0,1.5) .. controls ++(0,.35) and ++(0,.35) .. (1,1.5) to (1,0)
    .. controls ++(0,-.35) and ++(0,-.35) .. (0,0);
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,1.15) {$f$};
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,.35) {$g$};
\end{tikzpicture}}
\;\; = \;\;
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,1.5);
    \draw [very thick] (0,1.5) .. controls ++(0,.35) and ++(0,.35) .. (1,1.5) to (1,0)
    .. controls ++(0,-.35) and ++(0,-.35) .. (0,0);
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,1.15) {$g$};
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,.35) {$f$};
\end{tikzpicture}}
\]
In particular, for $f=1_V$, the identity endomorphism of $V$,
 $\tr(1_V)=\dim (V)$.  Here we are using the ``right" trace.  In a pivotal category one could also take the ``left" trace and these two traces need not coincide.

This pictorial presentation was extended to  the category
of colored ribbon graphs, graphically describing arbitrary ribbon categories such as the category of finite dimensional representation of quantum groups \cite{RT, Tur}.


This graphical calculus can also be seen as a specific instance of string diagrams in a 2-category~\cite{Street,js2,Lau3}.
