---
doc_id: arxiv-2402.08782v1
doc_title: "Hecke–Farey coordinates for Bring’s surface Doha Kattan 1 and David Singerman 2"
section_id: sec-006-8-poles
section_title: "Poles"
section_number: 8
pages: 9-11
source_pdf: 2402.08782v1.pdf
source_sha256: 30311f0bd815f93f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.973
doc_brief: "Hecke–Farey coordinates for Bring’s surface Doha Kattan 1 and David Singerman 2 — The modular group Γ (which is the Hecke group H3) can be used to study triangular maps, Here we use the Hecke group"
---
In a Farey map (the case $q=3$) a {\it pole} is a vertex with a Farey coordinate of the form $\frac{a}{0}$, where $a\not =0.$ For example, in the icosahedron $\mathscr{M}_{3}(5)$ the poles are $\frac{1}{0}$ and $\frac{2}{0}.$ which from Figure \ref{f9} are the north and south poles of the icosahedron.  Also, in \cite{ISS} Farey fractions were used to construct the fundamental region for the Klein quartic.  We found that $\frac{1}{0}$ was at the centre whilst $\frac{2}{0}$ and $\frac{3}{0}$ lie on the boundary. This is a typical situation. The pole $\frac{1}{0}$ always lies at the centre and the other poles lie on the boundary. In a rough sense these other poles lie at "infinity". The poles of $\mathscr{M}_{4}(5)$ are
$$A_1= \frac{1}{0\sqrt 2},  \, B_1=\frac{2}{0\sqrt 2},  \,  C_2=\frac{\sqrt 2}{0}, \, H_2=\frac{2\sqrt 2}{0}.$$

   
   

   \begin{figure}[H] 
    \centering

    \includegraphics[width=0.9\textwidth]{art23v4}
    \caption{}     
    \label{art123}
\end{figure}



  

  
  
 

    
   
   
   
\section{Hecke--Farey coordinates for Bring's surface}
There are two important papers where Bring's surface is drawn as a 20-sided polygon with side identifications. The first of these is by G.~Riera and R.~E.~Rodriguez \cite{RR92} from 1992.  The second is by H.~W.~Braden and T.~P.~Northover \cite{BN12}, who just used the Riera--Rodriguez diagram. 
   This diagram is slightly clearer so we use this. This is given in Figure \ref{art123}, but without the Hecke--Farey coordinates $G_1, J_2$ etc. In the diagram we also use their notation for the poles, So $P1 = H2,\;P2 = B2, \;P3 = C2$. Otherwise we use the original notation.
   
Riera and Rodriguez  did not give a proof that that their polygon represents Bring's surface. They write that the consider a Cayley diagram for $S_5$ and embed it into the surface but no details are given, nor did  they  justify the side pairings. Our aim is to give Hecke--Farey coordinates for the vertices of the 20-sided polygon.  This will tell us how to draw the polygon and also how to find the side-pairings. We start with a simple observation.


\begin{lemma} The map $z\mapsto z+\sqrt 2$ of the Hecke-Farey coordinates induces a rotation of $\mathscr{M}_4(5)$ through $2\pi/5$ about the centre $\frac{1}{0}.$
 
\end{lemma}

\begin{proof} As we are working modulo 5 in in $\mathscr{M}_4(5)$ the transformation has order 5 and fixes the centre $\frac{1}{0}.$ (Here we are identifying  the Hecke-Farey coordinate with its corresponding vertex.) 
\end{proof} 



For example, consider the pole $H_2=\frac{2\sqrt 2}{0}$, which we regard as the top vertex of our 20-sided polygon (See Figure \ref{art123}).  As $H_2+\sqrt 2=H_2$ we find that there are 5 vertices of our polygon, labelled $H_2.$  
The same applies to the pole $C_2$. There are 5 poles with label $C_2.$ However,  as we now see, there are 10 poles with label $B_1$.

\begin{definition} A  {\it Farey circuit}  is a collection of points $v_0, v_1,\cdots v_n$ each with a Hecke-Farey coordinate such that $v_i$ is adjacent to $v_{i+1}$ and $v_0=v_n.$

\end{definition}



A Farey circuit on $\mathscr{M}_4(5)$ is given by $H_2,  E_1, F_2, B_1, J_2, K_1, C_2, L_1, E_2, B_1,\\ F_2, D_1, H_2$ (12 vertices). For example $H_2=\frac{2\sqrt 2}{0}$ is adjacent to $E_1=\frac{2}{\sqrt 2}$ and $E_1$ is adjacent to $F_2=\frac{\sqrt 2}{3}$, etc.  We continue this Farey sequence  just by adding multiples of  $\sqrt 2.$ For example, if we add  $\sqrt 2$ to our circuit  we get $H_2+\sqrt 2=H_2$,  $E_1+\sqrt 2=G_1$, $F_2+\sqrt 2=E_2$ etc., and we  get another 12 vertices. We get 12 more vertices each by adding $2\sqrt 2, \;3\sqrt 2$ and $4\sqrt 2$. In  this way we find Hecke-Farey  coordinates for all of the  60 boundary vertices as illustrated in Figure \ref{art123}.  Now in the first 12 vertices we found that there was one pole labelled $H_2=P_1$, one pole labelled $C_2=P_3$  and two poles labelled $B_2=P_2$.  Thus in total there are 5 poles of the form $P_1$, 5 poles labelled $ P_3$ and 10 poles labelled $P_2$. Thus in total there are 20 poles on the boundary and we regard these as the vertices of a 20-sided hyperbolic polygon. We use the diagram in \cite{BN12}, where the edges are labelled $1,2,\cdots , 20.$

In the diagram of Bring's surface with its  Hecke-Farey coordinates, each at the 20 edges has one vertex of valency 5 in its interior.
 For example, edge 1 has $K2$ as the vertex of valency 5 in its interior. In Table \ref{table:ds} we just list the edges together with these vertices.
 
 \begin{table}[h!]   
\begin{center}
\begin{tabular}{ | c | c | } 
\hline
 $1 \leftrightarrow  K_2$ &  $2 \leftrightarrow B_2$   \\ \hline
 $3 \leftrightarrow  L_1$ &  $4 \leftrightarrow I_1$  \\ \hline
 $5 \leftrightarrow  B_2$ &  $6 \leftrightarrow J_2$ \\ \hline
$7 \leftrightarrow  J_1$ &  $8 \leftrightarrow H_1$\\ \hline
$9 \leftrightarrow  J_2$ &  $10 \leftrightarrow F_2$ \\ \hline
$11 \leftrightarrow  K_1$ &  $12 \leftrightarrow L_1$ \\ \hline
$13 \leftrightarrow  F_2$ &  $14 \leftrightarrow E_2$ \\ \hline
$15 \leftrightarrow  I_1$ &  $16 \leftrightarrow J_1$ \\ \hline
$17 \leftrightarrow  E_2$ &  $18 \leftrightarrow K_2$ \\ \hline
$19 \leftrightarrow  H_1$ &  $20 \leftrightarrow K_1$ \\ \hline

\end{tabular}
    \end{center}
    \caption{}
    \label{table:ds}

\end{table}   

 We now just pair the sides of the polygon which have the same Hecke-Farey coordinate.  For example both side 1 and side 18 have the vertex $K_2$ so we pair them.
 
 We give all the side pairings in Table \ref{table:c}.
 \begin{table}[h!]   
\begin{center}
\begin{tabular}{ | c | c | } 
\hline
 $2 \leftrightarrow  5$ &  $6 \leftrightarrow 9$   \\ \hline
 $10 \leftrightarrow  13$ &  $14 \leftrightarrow 17$  \\ \hline
 $18 \leftrightarrow  1$ &  $3 \leftrightarrow 12$ \\ \hline
$7 \leftrightarrow  16$ &  $11 \leftrightarrow 20$\\ \hline
$15 \leftrightarrow  4$ &  $19 \leftrightarrow 8$ \\ \hline

\end{tabular}
    \end{center}
    \caption{}
    \label{table:c}

\end{table}   

We notice that if $k\equiv 2\,
\; \text{mod}\; 4$ then we pair $k$ with $k+3$, while if $k\equiv  3\; \text{mod}\; 4$ then we pair $k$ with $k+9$.  This is similar, but not exactly the same as in \cite{RR92} or \cite{BN12} where they give their answers without  proof.

\newpage
