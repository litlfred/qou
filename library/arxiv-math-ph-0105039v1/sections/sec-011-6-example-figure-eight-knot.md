---
doc_id: arxiv-math-ph-0105039v1
doc_title: "Hyperbolic Structure Arising from a Knot Invariant"
section_id: sec-011-6-example-figure-eight-knot
section_title: "Example: Figure-Eight Knot"
section_number: 6
pages: 24-28
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.992
doc_brief: "Hyperbolic Structure Arising from a Knot Invariant — We study the knot invariant based on the quantum dilogarithm function."
---
\label{sec:eight}

We shall demonstrate
how to decompose the knot complement  into  tetrahedra in a
case of the  figure-eight knot.
The figure-eight knot is
given as $\sigma_1 \, \sigma_2^{~-1} \, \sigma_1
\, \sigma_2^{~-1}$ in the braid group, and is
depicted as Fig.~\ref{fig:fig_eight}.
To each crossing in the  figure-eight knot,  we assign the octahedron
(Fig.~\ref{fig:R_matrix}

or eq.~\eqref{attach_octa}),
and
give the numbering to each crossing  as in
Fig.~\ref{fig:fig_eight_tetra}.
We have  also named  each surface as  $D_i$.
We call the surface inside the octahedron as $S^a_{i,j}$;
a  surface  is  in  the octahedron of the $a$-th crossing,
and is a boundary
between $D_i$ and $D_j$.

\begin{figure}[htbp]
  \begin{center}
    \psfig{file=41.eps,scale=0.25}
    \caption{The figure-eight knot $4_1$.}
    \label{fig:fig_eight}
  \end{center}
\end{figure}

\begin{figure}[htbp]
  \begin{center}
    \begin{psfrags}
      \psfrag{A}{$D_0$}
      \psfrag{B}{$D_1$}
      \psfrag{C}{$D_2$}
      \psfrag{D}{$D_3$}
      \psfrag{E}{$D_4$}
      \psfrag{F}{$D_5$}

      \psfrag{1}{\ding{172}}
      \psfrag{2}{\ding{173}}
      \psfrag{3}{\ding{174}}
      \psfrag{4}{\ding{175}}

      \psfig{file=41withTetra.eps,scale=0.25}      
    \end{psfrags}
    \caption{We attach octahedra for each crossing of the figure-eight
      knot.}
    \label{fig:fig_eight_tetra}
  \end{center}
\end{figure}

In a surface $D_1$ there are 3 tetrahedra.
These three tetrahedra are glued to each other as shown in
Fig.~\ref{fig:41_glue_1}.
Due to the pentagon
relation we obtain  2 adjacent tetrahedra, whose common surface
(gray surface)  is named  $P_1$.

\begin{figure}[htbp]
  \begin{center}
    \parbox{8cm}{
      \begin{psfrags}
        \psfrag{A}{$S^1_{1,2}$}
        \psfrag{B}{\textcolor{red}{\reflectbox{$S^1_{1,4}$}}}
        \psfrag{C}{$S^3_{1,3}$}
        \psfrag{D}{$S^3_{1,2}$}
        \psfrag{E}{\textcolor{red}{\reflectbox{$S^2_{1,4}$}}}
        \psfrag{F}{$S^2_{1,3}$}
        \psfrag{X}{\ding{172}}
        \psfrag{Y}{\ding{173}}
        \psfrag{Z}{\ding{174}}
        \psfig{file=glue_tetra_1.eps,scale=0.32}
      \end{psfrags}
      }
    ~~~$\Longleftrightarrow$~~~
    \parbox{5cm}{
      \begin{psfrags}
        \psfrag{A}{\rotatebox{-30}{$S^1_{1,4}$}}
        \psfrag{B}{\rotatebox{30}{$S^2_{1,3}$}}
        \psfrag{C}{\textcolor{red}{\reflectbox{$S^3_{1,2}$}}}
        \psfrag{D}{\rotatebox{-30}{$S^1_{1,2}$}}
        \psfrag{E}{\rotatebox{30}{$S^2_{1,4}$}}
        \psfrag{F}{\textcolor{red}{\reflectbox{$S^3_{1,3}$}}}
        \psfig{file=glue_tetra_reg.eps,scale=0.36}
      \end{psfrags}
      }
    \caption{Gluing  3 tetrahedra in surface $D_1$ results in 2
      tetrahedra by the 2-3 Pachner move.
      The gray surface in the 2 adjacent tetrahedra is called $P_1$.
      }
    \label{fig:41_glue_1}
  \end{center}
\end{figure}

Three  tetrahedra in a  surface $D_0$ also gives same adjacent  tetrahedra
with that in
Fig.~\ref{fig:41_glue_1}.
By the same method of gluing 3 tetrahedra in surfaces $D_2$ and $D_3$,
we obtain adjacent  tetrahedra as shown in Fig.~\ref{fig:41_glue_2}.
\begin{figure}[htbp]
  \begin{center}
    (a)
    \parbox{4.5cm}{
      \begin{psfrags}
        \psfrag{A}{\rotatebox{-30}{$S^4_{0,3}$}}
        \psfrag{B}{\rotatebox{30}{$S^2_{0,4}$}}
        \psfrag{C}{\textcolor{red}{\reflectbox{$S^1_{0,2}$}}}
        \psfrag{D}{\rotatebox{-30}{$S^4_{0,2}$}}
        \psfrag{E}{\rotatebox{30}{$S^2_{0,3}$}}
        \psfrag{F}{\textcolor{red}{\reflectbox{$S^1_{0,4}$}}}
        \psfig{file=glue_tetra_reg.eps,scale=0.36}
      \end{psfrags}
      }

    (b)~\parbox{4.5cm}{
      \begin{psfrags}
        \psfrag{A}{\rotatebox{-30}{$S^3_{1,2}$}}
        \psfrag{B}{\rotatebox{30}{$S^4_{2,5}$}}
        \psfrag{C}{\textcolor{red}{\reflectbox{$S^1_{0,2}$}}}
        \psfrag{D}{\rotatebox{-30}{$S^3_{2,5}$}}
        \psfrag{E}{\rotatebox{30}{$S^4_{0,2}$}}
        \psfrag{F}{\textcolor{red}{\reflectbox{$S^1_{1,2}$}}}
        \psfig{file=glue_tetra_res.eps,scale=0.36}
      \end{psfrags}
      }

    (c)~\parbox{4.5cm}{
      \begin{psfrags}
        \psfrag{A}{\rotatebox{-30}{$S^4_{0,3}$}}
        \psfrag{B}{\rotatebox{30}{$S^3_{3,5}$}}
        \psfrag{C}{\textcolor{red}{\reflectbox{$S^2_{1,3}$}}}
        \psfrag{D}{\rotatebox{-30}{$S^4_{3,5}$}}
        \psfrag{E}{\rotatebox{30}{$S^3_{1,3}$}}
        \psfrag{F}{\textcolor{red}{\reflectbox{$S^2_{0,3}$}}}
        \psfig{file=glue_tetra_res.eps,scale=0.36}
      \end{psfrags}
      }
    \caption{
      Gluing 3 tetrahedra in surfaces (a) $D_0$, (b) $D_2$,  and (c)
      $D_3$ gives the 2 adjacent tetrahedra.
      We call each gray
      surface  respectively $P_0$, $P_2$, and
      $P_3$.
      }
    \label{fig:41_glue_2}
  \end{center}
\end{figure}

In a surface $D_4$, we have 2 tetrahedra, which are glued to
each other
and result  in a suspension
as
shown in Fig.~\ref{fig:41_glue_sp}.
We also get a suspension from a surface $D_5$ as is shown in
Fig.~\ref{fig:41_glue_sp_2}.

\begin{figure}[htbp]
  \begin{center}
    \parbox{8.5cm}{
      \begin{psfrags}
        \psfrag{A}{$S^1_{1,4}$}
        \psfrag{B}{\textcolor{red}{\reflectbox{$S^1_{0,4}$}}}
        \psfrag{C}{$S^2_{1,4}$}
        \psfrag{D}{\textcolor{red}{\reflectbox{$S^2_{0,4}$}}}
        \psfrag{X}{\ding{172}}
        \psfrag{Y}{\ding{173}}
        \psfig{file=glue_tetra_sp.eps,scale=0.32}
      \end{psfrags}
      }
    ~~~$\Longleftrightarrow$~~~
    \parbox{4cm}{
      \begin{psfrags}
        \psfrag{A}{$S^2_{0,4}$}
        \psfrag{B}{\textcolor{red}{\reflectbox{$S^1_{1,4}$}}}
        \psfrag{C}{\textcolor{red}{\reflectbox{$S^1_{0,4}$}}}
        \psfrag{D}{$S^2_{1,4}$}
        \psfig{file=glue_susp_1.eps,scale=0.36}
      \end{psfrags}
      }
    \caption{Gluing 2 tetrahedra in a surface $D_4$ gives a suspension.}
    \label{fig:41_glue_sp}
  \end{center}
\end{figure}


\begin{figure}[htbp]
  \begin{center}
    \begin{psfrags}
      \psfrag{A}{$S^4_{2,5}$}
      \psfrag{B}{\textcolor{red}{\reflectbox{$S^3_{3,5}$}}}
      \psfrag{C}{\textcolor{red}{\reflectbox{$S^3_{2,5}$}}}
      \psfrag{D}{$S^4_{3,5}$}
      \psfig{file=glue_susp_2.eps,scale=0.36}
    \end{psfrags}
    \caption{Gluing 2 tetrahedra  in a surface $D_5$.}
    \label{fig:41_glue_sp_2}
  \end{center}
\end{figure}

We next glue these polyhedra,
4 2-adjacent-tetrahedra (Fig.~\ref{fig:41_glue_1}
and Fig.~\ref{fig:41_glue_2}) and 2 suspensions
(Fig.~\ref{fig:41_glue_sp} and Fig.~\ref{fig:41_glue_sp_2}).
We first cut those polyhedra in the plane which was painted  gray in
figures, and separate them into ``upper'' and ``lower'' polyhedra
(tetrahedra or cones).
In this procedure, we should remember  which vertices
in the gray faces
were  glued to each other.
We then glue these polygons to each other
which have  same surfaces $S^a_{i,j}$,
and we finally obtain 2 tetrahedra
(Fig.~\ref{fig:comple_41}) which come from   upper and lower polyhedra.
Faces in these tetrahedra present  gray faces
in Figs.~\ref{fig:41_glue_1}--\ref{fig:41_glue_2} which separates
upper and lower polyhedra.
It is a well known result by Thurston~\cite{WPThurs80Lecture} that the
complement of
the figure-eight knot is decomposed into these 2 tetrahedra.
Note that,  in order to have upper and lower polyhedra, we have used the so-called
1-4 Pachner move which shows that
neighborhood of  vertex inside the tetrahedron  constitute sphere
as was pointed out in Ref.~\citen{YYokot00b}.

\begin{figure}[htbp]
  \begin{center}
    \begin{psfrags}
      \psfrag{A}{\textcolor{red}{\reflectbox{$P_0$}}}
      \psfrag{B}{\rotatebox{30}{$P_1$}}
      \psfrag{C}{\textcolor{red}{\reflectbox{$P_2$}}}
      \psfrag{D}{\rotatebox{-20}{$P_3$}}
      \psfrag{E}{\textcolor{red}{\reflectbox{$P_0$}}}
      \psfrag{F}{\textcolor{red}{\reflectbox{$P_1$}}}
      \psfrag{G}{\rotatebox{-20}{$P_2$}}
      \psfrag{H}{\rotatebox{30}{$P_3$}}
      \psfig{file=comple_41.eps,scale=0.5} 
    \end{psfrags}
    \caption{Complement of the figure-eight knot.}
    \label{fig:comple_41}
  \end{center}
\end{figure}


The partition function of the complement of the figure-eight knot is
then computed from Fig.~\eqref{fig:comple_41} as
\begin{align}
  {\tau}_1({4_1})
  & =
  \int \mathrm{d} \vec{p} \
  \langle p_1 = 0, p_2 \  | \  S \  | \  p_3, p_4 \rangle \,
  \langle p_4, p_3 \ | \  S^{-1} \  | \  p_2 , p_1=0\rangle
  \nonumber
  \\

  & \sim
  \int \mathrm{d} p \
  \exp \frac{1}{2 \, \mathrm{i} \, \gamma} \,
  \Bigl(
    \Li (\mathrm{e}^{-p}) - \Li (\mathrm{e}^p)
  \Bigr) .
\end{align}
Here we have introduced a restriction $p_1=0$ which comes from a
computation of the knot invariant for a ($1,1$)-tangle.
The integral in the partition function can be evaluated at the saddle
point,
\begin{equation*}
  (1- \mathrm{e}^p) \, ( 1 - \mathrm{e}^{-p})=1 ,
\end{equation*}
which, with a root of $\omega^2 - \omega + 1=0$, gives
\begin{equation}
  \Tilde{\tau}_1(4_1)
  =
  \lim_{\gamma \to 0}
  \left(
    2 \, \mathrm{i} \, \gamma \log {\tau}_1(4_1)
  \right)
  =
  2.02988 \, \mathrm{i} .
\end{equation}
The imaginary part is nothing but the hyperbolic volume of the
complement of the figure-eight knot.
