---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT"
section_id: sec-009-21-triangulation
section_title: "Triangulation"
section_number: 2.1
pages: 9-10
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.741
latex_coverage_ratio: 0.776
doc_brief: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
It is a well-known fact, due to Riley and used by Thurston \cite{Thurston}, that the figure eight knot complement may be triangulated by two tetrahedra, with the combinatorics of face gluings displayed in figure \ref{fig:triang8}.
In order to simplify the notations, we denote by $u_{ij}$ and $v_{ij}$ be the coordinates associated to the edge $ij$ of the two tetrahedra as  shown in Figure \ref{fig:triang8}.

\begin{figure}[ht] \label{eight}
\begin{center}
\begin{asy}
   size(8cm);
  defaultpen(1);
  usepackage("amssymb");
  import geometry;
  
  point o = (8,0);
  point oo = (24,0);
  pair ph = (10,0);
  pair pv = (5,8);
 
  
  // 
  draw(o -- o+pv,Arrow(5bp,position=.4), Arrow(5bp,position=.5));
  draw(o+pv -- o+ph, Arrow(5bp,position=.6));
  draw(o+ph-pv-- o, Arrow(5bp,position=.6));
  draw(o+ph-pv-- o+ph, Arrow(5bp,position=.6));
  draw(o+ ph/2+(0,.2)--o+pv, Arrow(5bp,position=.4), Arrow(5bp,position=.5));
  draw(o+ph-pv -- o+ph/2+ (0,-.2));
  draw(o -- o+ph,Arrow(5bp,position=.3), Arrow(5bp,position=.4) );
  
  // 
  label("\small { $u_{34}$}", o, 3*dir(25));
  //
  //
  label("{\small  $3$}", o, 1*W);
  
  label("\small {$u_{43}$}", o+ph, 3*dir(180-25));
  //
  //
  label("{\small $4$}", o+ph, .6*E);
  
  //
  label(" \small $ u_{12}$", o+pv, 9*dir(-80));
  //
  label("{\small $1$}", o+pv, 1*N);
  
   //
  label(" \small $ u_{21}$", o+ph-pv, 9*dir(80));
  //
  label("{\small $2$}", o+ph -pv, 1*S);

  // 
  draw( oo+pv -- oo,Arrow(5bp,position=.6));
  draw( oo+pv -- oo+ph,Arrow(5bp,position=.6));
  draw( oo+ph-pv -- oo,Arrow(5bp,position=.6));
  draw(oo+ ph/2+(0,.2)--oo +pv,Arrow(5bp,position=.4), Arrow(5bp,position=.5));
  draw(oo+ph-pv -- oo+ ph/2-(0,.2));
  draw(oo+ph-pv -- oo+ ph,Arrow(5bp,position=.5),Arrow(5bp,position=.6));
  draw(oo -- oo+ph,Arrow(5bp,position=.3), Arrow(5bp,position=.4));
  
   // 
  label("\small { $v_{34}$}", oo, 3*dir(25));
  //
  //
  label("{ \small $3$}", oo, 1*W);
  
  label("\small {$v_{43}$}", oo+ph, 3*dir(180-25));
  //
  //
  label("{ \small $4$}", oo+ph, .6*E);
  
  //
  label(" \small $  v_{12}$", oo+pv, 9*dir(-77));
  //
  label("{ \small $1$}", oo+pv, 1*N);
  
   //
  label(" \small $ v_{21}$", oo+ph-pv, 9*dir(80));
  //
  label("{\small $2$}", oo+ph -pv, 1*S);

\end{asy}
\caption{ The figure eight knot represented by two tetrahedra.} \label{fig:triang8}
\end{center}
\end{figure}

From this triangulation, it is an elementary exercise to compute the equations defining $\mathrm{Defor}(M,\mathcal T)$ as explained in \S \ref{ss:deformationvariety}. These equations will actually be displayed in \S \ref{ss:equations}.
