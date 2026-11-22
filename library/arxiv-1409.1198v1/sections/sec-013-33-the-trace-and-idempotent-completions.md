---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-013-33-the-trace-and-idempotent-completions
section_title: "The trace and idempotent completions"
section_number: 3.3
pages: 15-16
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.943
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
A {\em projection} or {\em idempotent} in $\cat{Vect}_{\k}$ is an endomorphism $p \maps V \to V$ satisfying the relation $p^2=p$.  In this case, $(\Id_V-p )\maps V \to V$ is also an idempotent and together these two idempotents decompose the space $V$ into a direct sum of the image of the projection $p$ and the image of the projection $\Id_V-p$.

More generally, idempotents can be defined in any category $\modC$ as endomorphisms $e \maps x \to x$ satisfying $e^2=e$, but here we will always assume that $\modC$ is a linear category.
\[\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,1.5);
   
   
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,1.05) {$e$};
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,.45) {$e$};
        \node at (0.15,.1) { $\scs x$};
    \node at (.15,1.4) { $\scs x$};
\end{tikzpicture}} \;\; = \;\;
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,1.5);
   
   
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,.75) {$e$};
    \node at (0.15,.1) { $\scs x$};
    \node at (.15,1.4) { $\scs x$};
\end{tikzpicture}}
\]
An idempotent $e\col x\rightarrow x$ in $\modC $ is said to {\em split} if there is an object $y$ and morphisms $g\col x\rightarrow y$, $h\col y\rightarrow x$ such that $hg=e$ and $gh=1_y$.
\[\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,1.5);
   
   
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,1.05) {$h$};
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,.45) {$g$};
        \node at (0.15,.1) { $\scs x$};
    \node at (.15,1.4) { $\scs x$};
\end{tikzpicture}} \;\; = \;\;
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,1.5);
   
   
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,.75) {$e$};
    \node at (0.15,.1) { $\scs x$};
    \node at (.15,1.4) { $\scs x$};
\end{tikzpicture}}
\qquad \qquad
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,1.5);
   
   
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,1.05) {$g$};
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,.45) {$h$};
        \node at (0.15,.1) { $\scs y$};
    \node at (.15,1.4) { $\scs y$};
\end{tikzpicture}} \;\; = \;\;
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,1.5);
   
   
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,.75) {$1_y$};
    \node at (0.15,.1) { $\scs y$};
    \node at (.15,1.4) { $\scs y$};
\end{tikzpicture}}
\]





Unfortunately, even in an additive category $\modC$ it is not always possible to split idempotents.

Such phenomenon occurs quite often when studying additive categories $\modC$ defined diagrammatically by generators and relations~\cite{Kup,Mor,BNM-Kar}.  In this case, making sense out of the ``image" of a diagram is not usually possible.  A common solution is to enlarge the category $\modC$ by passing to the {\em Karoubi envelope} $\Kar(\mathcal C)$ (also called {\em idempotent}   or {\em Cauchy completion}) of $\modC $.  The Karoubi envelope can be thought of as a minimal enlargement of the category $\modC$ in which all idempotents split.



More formally, the Karoubi envelope $\Kar(\modC)$ is the category whose objects are pairs $(x,e)$ of objects $x\in \Ob(\C)$ and
an idempotent endomorphism $e : x\rightarrow x$ in $\mathcal
C$. The morphisms
$$f : (x,e)\rightarrow(y,e')$$
are morphisms $f\col x\rightarrow y$ in $\modC $ such that $f=e'fe$, or alternatively such that
\[
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,2);
   
   
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,1) {$f$};
    \node at (0.15,.1) { $\scs x$};
    \node at (.15,1.9) { $\scs y$};
\end{tikzpicture}} \;\; = \;\;
\hackcenter{\begin{tikzpicture}
    \draw[very thick] (0,0) -- (0,2.5);
   
   
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,1.25) {$f$};
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,.5) {$e$};
    \node[draw, thick, fill=blue!20,rounded corners=4pt,inner sep=3pt] () at (0,2) {$e'$};
        \node at (0.15,.1) { $\scs x$};
    \node at (.15,2.4) { $\scs y$};
\end{tikzpicture}} \; .
\]
Composition is induced by the composition in $\mathcal C$ and the identity morphism is
$e : (x,e)\rightarrow(x,e)$. $\Kar(\modC )$ is equipped with a linear category structure.

We can 
identify $(x,1_x)$ with the object $x$ of $\mathcal{C}$. This identification gives rise to a  natural embedding functor $\iota:\mathcal C\rightarrow
\Kar(\mathcal C)$ such that $\iota(x)=(x,1_x)$ for $x\in \Ob(\modC )$ and
$\iota(f\col x\rightarrow y)=f$.  The Karoubi envelope $\Kar(\modC )$ has
the universality property that if $F\col \modC \rightarrow \modD $ is
a linear functor to a linear category $\modD $ with split idempotents,
then $F$ extends to a functor from $\Kar(\modC)$ to $\modD$ uniquely
up to natural isomorphism \cite[Proposition 6.5.9]{Bor}.


\begin{example}
Consider the Temperley-Lieb category $\TL$ defined over $\mathbb{C}(q)$, where $q$ is an indeterminant with $q=-A^{2}$.   The Karoubi envelope $\Kar(\TL)$ is equivalent as a category to the category of finite-dimensional representations of quantum ${\fsl}_2$ (\cite{Kauffman} and \cite{Penrose}).

 The irreducible $N$-dimensional representation arises as the image of a certain idempotent  called {\em Jones-Wenzl} idempotent.
\end{example}


\begin{exercise}
Show that the Karoubi envelope of an additive category
is additive.
\end{exercise}

The following proposition illustrates one of the key advantages of the trace, namely its invariance under passing to the Karoubi envelope.

\begin{prop}
  \label{r1}
  The map $\Tr(\iota)\col \Tr(\modC )\longrightarrow \Tr(\Kar(\modC ))$ induced by $\iota$ is bijective.
\end{prop}

\begin{proof}
Recall that an endomorphism $f\maps (x,e) \to (x,e)$ in $\Kar(\modC)$ is just a morphism $f\maps x \to x$ in $\modC$ satisfying the condition that $f=efe$.  Define a map $u\col \Tr(\Kar(\modC ))\longrightarrow \Tr(\modC )$ sending $[f]\in \Tr(\Kar(\modC ))$ to $[f]\in \Tr(\modC )$.
Then one can check that $u$ is an inverse to $\Tr(\iota)$.
\end{proof}

\begin{example}
Adding Jones-Wenzl idempotents as  objects into $\TL$ does not affect  $\Tr(\TL)$.
\end{example}
