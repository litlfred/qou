---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-026-52-the-current-algebra-for-sln
section_title: "The current algebra for sln"
section_number: 5.2
pages: 35-43
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.887
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
\label{current-sln}





We expect to be able to generalize Theorem~\ref{qqq} to $\fsl_n$.


Let us define the current algebra
${\bf U}(\fsl_n[t])={\bf U}(\fsl_n\otimes\Q[t])$. This algebra is generated over $\k$ by
$x^+_{i,r}$, $x^-_{i,s}$ and $\xi_{i,k}$ for $r,s,k\in \N\cup\{0\}$ and $1\leq i<n$
modulo the following relations:
\begin{description}
  \item[C1] For $i,j$ in $I$ and $r,s \in \N\cup\{0\}$
\[
[ \xi_{i,r}, \xi_{j,s} ] = 0
\]

  \item[C2] For any $i,j \in I$ and $k \in \N\cup\{0\}$,
\[
 [ \xi_{i,0}, x^{\pm}_{j,k} ] = \pm a_{ij}x^{\pm}_{j,k}
\]

  \item[C3] For any $i,j \in I$ and $r,k \in \N\cup\{0\}$,
\[
 [\xi_{i,r}, x^{\pm}_{j,k} ] = \pm a_{ij} x^{\pm}_{j, r+k}
\]

  \item[C4] For $i,j \in I$ and $k, \ell \in \N\cup\{0\}$
\[
[x^\pm_{i, k+1}, x^\pm_{j,\ell}]=[x^\pm_{i,k}, x^\pm_{j,\ell+1}]
\]
  \item[C5] For $i,j \in I$ and $k,\ell \in \N\cup\{0\}$
\[
 [x^+_{i,k}, x^-_{j,\ell}] = \delta_{i,j} \xi_{i, k+\ell}
\]
  \item[C6] Let $i \neq j$ and set $m=1-a_{ij}$.  For every $k_1, \dots, k_m \in \N\cup\{0\}$ and $\ell \in \N\cup\{0\}$
\[
 \sum_{\pi \in S_m} \sum_{s=0}^{m} (-1)^s
 \binom{m}{s} x^{\pm}_{i, k_{\pi(1)}} \dots x^{\pm}_{i, k_{\pi(s)}}
 x^{\pm}_{j, \ell} x^{\pm}_{i, k_{\pi(s+1)}} \dots x^{\pm}_{i, k_{\pi(m)}} = 0.
\]
\end{description}
For more on the relationship between the current algebra and specializations of the Yangian see \cite{Bag}.
Recall that we denote by $\dot{\bfU}(\fsl_n[t])$ the idempotented form of the current algebra.

\begin{exercise}
Show for $t=1$ that the current algebra relations restrict to the defining relations
for ${\bf U}(\fsl_n)$.
\end{exercise}

The next proposition is
 a step towards generalizing Theorem~\ref{qqq}.

\begin{proposition}\label{prop-cur}
Let \(\mathsf{E}_{i,r}, \mathsf{F}_{j,s}, \mathsf{H}_{i,r}\) denote  the generators of \(\Tr(\U^\ast(\fsl_n))\):
\[\mathsf{E}_{i,r}1_{\lambda}:=  \left[
\xy 0;/r.18pc/:
  (10,6)*{\lambda};
  (0,0)*{\bbe{}};
  (0,2)*{\bullet}+(3,1)*{r};
  (-8,6)*{ }; (12,-7)*{}; (2,-7)*{\scs i};
 \endxy
\right],  \quad \quad
\mathsf{F}_{j,s}1_{\lambda}:=  \left[
\xy 0;/r.18pc/:
  (10,6)*{\lambda};
  (0,0)*{\bbf{}};
  (2,-7)*{\scs j};
  (0,4)*{\bullet}+(3,1)*{s};
   (-8,6)*{ }; (12,-7)*{};
 \endxy
\right],\quad \quad
  \mathsf{H}_{i,r}1_{\lambda}:= \left[
 p_{i,r}(\lambda)\; \Id_{\onel}
\right],\]where $p_{i,r}(\l)$ was defined in equation~\ref{eq_defpil}.
For any choice of scalars $Q$ with $t_{ij}^2=t_{ji}^2=t_ij^{-1}t_{ji}=1$ for $i \neq j$, there is a well defined homomorphism
\begin{equation} \label{eq_sln-homo}
 h \maps \dot{\bfU}(\fsl_n[t]) \longrightarrow \Tr(\U^\ast(\fsl_n)),
\end{equation}
given by
\begin{equation} \label{homomorp}
x^{+}_{i, r} 1_{\lambda} \mapsto
(-1)^{(i+1)r}\,\mathsf{E}_{i,r}1_{\lambda}


 
  
 
 
 

 ,\quad \quad
x^{-}_{j, s} 1_{\lambda}\mapsto
(-1)^{(j+1)s}\,\mathsf{F}_{j,s}1_{\lambda}



  
  
  
   
 

,\quad \quad
\xi_{i, r} 1_{\lambda}\mapsto
  (-1)^{(i+1)r}\,\mathsf{H}_{i,r}1_{\lambda}.
 
 

\end{equation}

\end{proposition}

\begin{proof}
To prove this proposition we verify the current algebra relations  using the relations in the 2-category $\U^\ast(\fsl_n)$. We only need
to consider the case \(i\neq j\), since the relations in $\U^\ast(\fsl_2)$ have been proven in \cite{BHLZ}.
\textbf{C1} is clear, since multiplication by a bubble is a commutative operation. We prove  the equality \textbf{C3} for the case \(j=i\pm1\).
For convenience we will only depict the interior of the annulus for diagrams on the annulus in our calculation below where $v_{ij}:= t_{ij}^{-1}t_{ji}$.
\[ \mathsf{H}_{i,a}\mathsf{E}_{j,b} 1_\lambda\;\;= \;\;
\sum^a_{k=0} k \; \;
 \xy
   (-12,-2)*{\icbub{\spadesuit+k}{i}};
   (0,-2)*{\iccbub{\spadesuit+a-k}{i}};
  (12,-2)*{\icbub{b}{j}};
    (12,1)*{\lambda}; (12,-3)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
 \endxy
 \]
\[ \refequal{\eqref{c_slide_right}} \;\;
\sum^a_{k=0} k \; \;
 \xy
   (-18,-2)*{\iccbub{\spadesuit+a-k}{i}};
   (-1,-2)*{\icbub{\spadesuit+k}{i}};
  (0,6.5)*{\lambda};(5,3)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
    (-10,0)*{}="t1";  (10,0)*{}="t2";
  "t2";"t1" **\crv{(10,14) & (-10,14)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(10,-14) & (-10,-14)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(1,-3)*{\scs b};
   \endxy
   \;\;+\;\; v_{ij} \; \sum^a_{k=0} k \;
 \xy
   (-18,-2)*{\iccbub{\spadesuit+a-k}{i}};
   (-1,-1)*{\icbub{\spadesuit+k-1}{i}};
  (1,6.5)*{\lambda};(5,3)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
    (-10,0)*{}="t1";  (10,0)*{}="t2";
  "t2";"t1" **\crv{(10,14) & (-10,14)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(10,-14) & (-10,-14)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(1,-3)*{\scs b+1};
   \endxy
 \]
\[\refequal{\eqref{cc_slide_right}}
\sum^a_{k=0}\;\sum^{a-k}_{\ell=0} k \; (-v_{ij})^{\ell}\;
 \xy
   (-6,-2)*{\icbub{\spadesuit+k}{i}};
   (8,-2)*{\iccbub{\spadesuit+a-k-\ell}{i}};
  (8,8)*{\lambda};(4,8)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
    (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs \ell+b};
   \endxy \;\; +\;\;v_{ij}\;\sum^a_{k=0}\;\sum^{a-k}_{\ell=0} k \; (-v_{ij})^{\ell}\;
 \xy
   (-6,-2)*{\icbub{\spadesuit+k-1}{i}};
   (8,-2)*{\iccbub{\spadesuit+a-k-\ell}{i}};
  (8,8)*{\lambda}; (4,8)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
    (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs \ell+b+1};
   \endxy
\]
\[  =\;\; \sum^a_{\ell=0}\;\sum^{a-\ell}_{k=0} k \; (-v_{ij})^{\ell}\;
 \xy
   (-9,-2)*{\icbub{\spadesuit+k}{i}};
   (5,-2)*{\iccbub{\spadesuit+a-k-\ell}{i}};
  (8,8)*{\lambda};(4,8)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
    (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(1,-3)*{\scs \ell+b};
   \endxy \;\; +\;v_{ij}\;\sum^a_{\ell=0}\;\sum^{a-\ell-1}_{k=0} (k+1) \; (-v_{ij})^{\ell}\;
 \xy
   (-9,-2)*{\icbub{\spadesuit+k}{i}};
   (6,-2)*{\iccbub{\spadesuit+a-k-\ell-1}{i}};
  (8,8)*{\lambda};(4,8)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
    (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs \ell+b+1};
   \endxy
\]
\[ \refequal{\eqref{eq_defpil}}
\;\; \sum^a_{\ell=0} \; (-v_{ij})^{\ell}\; \;
 \xy
  (5,5)*{\lambda}; (1,5)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
  (0,0)*{\mathsf{H}_{i,a-\ell}};
(-10,0)*{}="t1";  (10,0)*{}="t2";
  "t2";"t1" **\crv{(10,14) & (-10,14)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(10,-14) & (-10,-14)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(1,-3)*{\scs \ell+b};
   \endxy \;\; -\;\;\sum^{a+1}_{\ell=1}\;\sum^{a-\ell}_{k=0} (k+1) \; (-v_{ij})^{\ell}\;
 \xy
   (-6,-2)*{\icbub{\spadesuit+k}{i}};
   (10,-2)*{\iccbub{\spadesuit+a-k-\ell}{i}};
  (8,8)*{\lambda}; (4,8)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
    (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(1,-3)*{\scs \ell+b};
   \endxy
\]
Pulling off $k$ of the summands in the second term and observing that the $\ell=a+1$ term vanishes we have
\[
=\;\; \sum^a_{\ell=0} \; (-v_{ij})^{\ell}\; \;
 \xy
  (5,5)*{\lambda}; (1,5)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
  (0,0)*{\mathsf{H}_{i,a-\ell}};
(-10,0)*{}="t1";  (10,0)*{}="t2";
  "t2";"t1" **\crv{(10,14) & (-10,14)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(10,-14) & (-10,-14)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(1,-3)*{\scs \ell+b};
   \endxy \;\;  -\;\; \sum^a_{\ell=1} \; (-v_{ij})^{\ell}\; \;
 \xy
  (5,5)*{\lambda}; (1,5)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
  (0,0)*{\mathsf{H}_{i,a-\ell}};
(-10,0)*{}="t1";  (10,0)*{}="t2";
  "t2";"t1" **\crv{(10,14) & (-10,14)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(10,-14) & (-10,-14)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(1,-3)*{\scs \ell+b};
   \endxy \;-\;\sum^{a}_{\ell=1}\;\sum^{a-\ell}_{k=0}  \; (-v_{ij})^{\ell}\;
 \xy
   (-6,-2)*{\icbub{\spadesuit+k}{i}};
   (10,-2)*{\iccbub{\spadesuit+a-k-\ell}{i}};
  (8,8)*{\lambda};(4,8)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
    (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(1,-3)*{\scs \ell+b};
   \endxy
  \]
\[=\; \;
 \xy
  (5,5)*{\lambda}; (1,5)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
  (0,0)*{\mathsf{H}_{i,a}};
(-10,0)*{}="t1";  (10,0)*{}="t2";
  "t2";"t1" **\crv{(10,14) & (-10,14)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(10,-14) & (-10,-14)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(1,-3)*{\scs b};
   \endxy \;\; -\;\; \sum^a_{\ell=1} \; (-v_{ij})^{\ell}\; \;
 \xy
  (5,5)*{\lambda};(1,5)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
   (0,0)*{\delta_{a-\ell,0}};
(-10,0)*{}="t1";  (10,0)*{}="t2";
  "t2";"t1" **\crv{(10,14) & (-10,14)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(10,-14) & (-10,-14)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(1,-3)*{\scs \ell+b};
   \endxy \;\; =\;\; \xy
  (5,5)*{\lambda};
  (1,5)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};(0,0)*{\mathsf{H}_{i,a}};
(-10,0)*{}="t1";  (10,0)*{}="t2";
  "t2";"t1" **\crv{(10,14) & (-10,14)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(10,-14) & (-10,-14)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(1,-3)*{\scs b};
   \endxy \;\; -\;\; (-v_{ij})^a\; \;
 \xy
  (3,3)*{\lambda}; (0,0)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(-10,0)*{}="t1";  (10,0)*{}="t2";
  "t2";"t1" **\crv{(10,14) & (-10,14)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(10,-14) & (-10,-14)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(1,-3)*{\scs a+b};
   \endxy
\]
\[=\;\;\mathsf{E}_{j,b} \mathsf{H}_{i,a} 1_\lambda - (-v_{ij})^a\;\mathsf{E}_{j,a+b}  1_\lambda. \]
By choosing \(v_{ij}=1\), we get
\[[ \mathsf{H}_{i,a}, \mathsf{E}_{j,b}] 1_\lambda = -(-1)^a \mathsf{E}_{j,a+b}1_\lambda .\]
The relation
\[[ \mathsf{H}_{i,a}, \mathsf{F}_{j,b}] 1_\lambda = (-1)^a \mathsf{F}_{j,a+b}1_\lambda .\]
can be proven in a similar way.
\textbf{C4} follows from the relations
\eqref{eq_r2_ij-gen} and \eqref{eq_dot_slide_ij-gen}:
\[
  t_{ij}\;\; \xy
 (-6,0)*{};
  (6,0)*{};
  (0,2)*{\lambda};(0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
  (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs b};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs a+1};
  \endxy \; + t_{ji}\;\;  \xy
 (-6,0)*{};
  (6,0)*{};
   (0,2)*{\lambda};(0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
  (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs b+1};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs a};
  \endxy
  
  \;\; \refequal{\eqref{eq_r2_ij-gen}}\;\;
  
    \xy 0;/r.18pc/:
     (0,-1)*{
 };
 (0,6)*{\lambda};(0,0)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
 (-8,-4)*{\ecross};(-8,4)*{\naecross};
  (4,0)*{\mline};(12,0)*{\mline};(0,10)*{\scap};(0,12)*{\lcap};
  (0,-10)*{\scupef};(0,-14)*{\lcupef};
  (6,-3)*{\scs j};(15,-3)*{\scs i};
   (-12,8)*{\bullet}+(-2.5,1)*{\scs a};
 (-4,8)*{\bullet}+(-2.5,1)*{\scs b};
  \endxy

\;\; \refequal{\eqref{eq_dot_slide_ij-gen}} \;\;

    \xy 0;/r.18pc/:
     (0,-1)*{
 };
(0,6)*{\lambda};(0,0)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
 (-8,-4)*{\ecross};(-8,4)*{\naecross};
  (4,0)*{\mline};(12,0)*{\mline};(0,10)*{\scap};(0,12)*{\lcap};
  (0,-10)*{\scupef};(0,-14)*{\lcupef};
  (6,-3)*{\scs i};(15,-3)*{\scs j};
   (-12,8)*{\bullet}+(-2.5,1)*{\scs b};
 (-4,8)*{\bullet}+(-2.5,1)*{\scs a};
  \endxy
\]
\[\; \refequal{\eqref{eq_r2_ij-gen}} \;
  t_{ji}\;\; \xy
 (-6,0)*{};
  (6,0)*{};
   (0,2)*{\lambda};(0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};  (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs a};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs b+1};
  \endxy \; + t_{ij}\;\;  \xy
 (-6,0)*{};
  (6,0)*{};
   (0,2)*{\lambda};(0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
  (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs a+1};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs b};
  \endxy \; \; .\]
  Dividing both sides of this equation by \(t_{ij}\), and by choosing \(v_{ij}=1\), we get
  \[ [ \mathsf{E}_{i,a+1},\mathsf{E}_{j,b} ]1_\lambda=-[\mathsf{E}_{i,a},\mathsf{E}_{j,b+1} ]1_\lambda .\]
  If we reverse the arrows in the preceding equation, they still hold:
   \[ [ \mathsf{F}_{i,a+1},\mathsf{F}_{j,b} ]1_\lambda=-[\mathsf{F}_{i,a},\mathsf{F}_{j,b+1} ]1_\lambda .\]
The choice of signs  in \eqref{homomorp} correspond to
  \[ [x^\pm_{i, a+1}, x^\pm_{j,b}]=[x^\pm_{i,a}, x^\pm_{j,b+1}].\]
The relation \textbf{C5} for the case \(i\neq j\) can be checked the following way:  \[
\mathsf{E}_{i,a}\mathsf{F}_{j,b} 1_\lambda
 \;\; = \;\;
  \xy
 (-6,0)*{};
  (6,0)*{};
  (0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(0,2)*{\lambda};
  (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{>}
   ?(1)*\dir{>} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs b};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs a};
  \endxy
  \;\; \refequal{\eqref{mixed_rel}} \;
   t^{-1}_{ji}\;  \xy 0;/r.18pc/:
     (0,-1)*{
 };(0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(0,6)*{\lambda};
(-8,-4)*{\fecross};(-8,4)*{\naecross};
  (4,0)*{\mline};(12,0)*{\mline};(0,10)*{\scap};(0,12)*{\lcap};
  (0,-10)*{\scupfe};(0,-14)*{\lcupef};
  (6,-3)*{\scs j};(15,-3)*{\scs i};
   (-12,8)*{\bullet}+(-2.5,1)*{\scs a};
 (-4,8)*{\bullet}+(-2.5,1)*{\scs b};
  \endxy
  \;\; \refequal{\eqref{eq_dot_slide_ij-gen}} \;
\]  \[
\;\; \refequal{\eqref{eq_dot_slide_ij-gen}} \;
  t^{-1}_{ji}\;  \xy 0;/r.18pc/:
     (0,-1)*{ };
(0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(0,6)*{\lambda};     (-8,-4)*{\efcross};(-8,4)*{\naecross};
  (4,0)*{\mline};(12,0)*{\mline};(0,10)*{\scap};(0,12)*{\lcap};
  (0,-10)*{\scupef};(0,-14)*{\lcupfe};
  (6,-3)*{\scs i};(15,-3)*{\scs j};
   (-12,8)*{\bullet}+(-2.5,1)*{\scs b};
 (-4,8)*{\bullet}+(-2.5,1)*{\scs a};
  \endxy
 \;\; \;\; \refequal{\eqref{mixed_rel}} \;
   \xy
 (-6,0)*{};
  (6,0)*{};
(0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(0,2)*{\lambda};
  (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs a};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{>} ?(1)*\dir{>} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs b};
  \endxy  \;\; \;\; = \;
\mathsf{F}_{j,b} \mathsf{E}_{i,a}1_\lambda.
\]
 




We now prove the Serre relation \textbf{C6} in the case when $i \cdot j = -1$.
Let us prove the identity $$\mathsf{E}_{i,a}\mathsf{E}_{j,b}\mathsf{E}_{i,c}1_{\lambda} +\mathsf{E}_{i,c}\mathsf{E}_{j,b}\mathsf{E}_{i,a}1_{\lambda} = \mathsf{E}_{i,a}\mathsf{E}_{i,c}\mathsf{E}_{j,b} 1_{\lambda}+\mathsf{E}_{j,b}\mathsf{E}_{i,a}\mathsf{E}_{i,c} 1_{\lambda}.$$
\begin{equation} \label{eq_vv1}
\mathsf{E}_{i,a}\mathsf{E}_{j,b}\mathsf{E}_{i,c}1_{\lambda}  =\;\;
 \xy
 (-6,0)*{};
  (6,0)*{};
  (0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(0,2)*{\lambda};
  (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs c};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs b};
   (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs a};
  \endxy
\;\; \refequal{\eqref{eq_r3_hard-gen}}\;\;
  t^{-1}_{ij} \vcenter{
 \xy 0;/r.18pc/:
    (-4,-4)*{};(4,4)*{} **\crv{(-4,-1) & (4,1)}?(1)*\dir{>};
    (4,-4)*{};(-4,4)*{} **\crv{(4,-1) & (-4,1)}?(1)*\dir{>};
    (4,4)*{};(12,12)*{} **\crv{(4,7) & (12,9)}?(1)*\dir{>};
    (12,4)*{};(4,12)*{} **\crv{(12,7) & (4,9)}?(1)*\dir{>};
    (-4,12)*{};(4,20)*{} **\crv{(-4,15) & (4,17)}?(1)*\dir{>};
    (4,12)*{};(-4,20)*{} **\crv{(4,15) & (-4,17)}?(1)*\dir{>};
    (-4,4)*{}; (-4,12) **\dir{-};
    (12,-4)*{}; (12,4) **\dir{-};
    (12,12)*{}; (12,20) **\dir{-};
 (16,4)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(16,12)*{\lambda};
  (-6,-3)*{\scs i}; (6,-3)*{\scs j};(15,-3)*{\scs i};  (20,5)*{\bullet}+(3,3)*{\scs c};(28,5)*{\bullet}+(3,3)*{\scs b}; (36,5)*{\bullet}+(3,3)*{\scs a};
  (20,8)*{\lfline};(28,8)*{\lfline};(36,8)*{\lfline};
  (16,22)*{\scap};(16,24)*{\lcap};(16,30)*{\xlcap};
  (16,-6)*{\scupef};(16,-10)*{\lcupef};(16,-15)*{\xlcupef};
\endxy}\;
 \;\; -\;  t^{-1}_{ij} \;
 \vcenter{
 \xy 0;/r.18pc/:
    (12,-4)*{};(4,4)*{} **\crv{(12,-1) & (4,1)}?(1)*\dir{>};
    (4,-4)*{};(12,4)*{} **\crv{(4,-1) & (12,1)}?(1)*\dir{>};
    (4,4)*{};(-4,12)*{} **\crv{(-,7) & (-4,9)}?(1)*\dir{>};
    (-4,4)*{};(4,12)*{} **\crv{(-4,7) & (4,9)}?(1)*\dir{>};
    (12,12)*{};(4,20)*{} **\crv{(12,15) & (4,17)}?(1)*\dir{>};
    (4,12)*{};(12,20)*{} **\crv{(4,15) & (12,17)}?(1)*\dir{>};
    (12,4)*{}; (12,12) **\dir{-};
    (-4,-4)*{}; (-4,4) **\dir{-};
    (-4,12)*{}; (-4,20) **\dir{-};
   (16,4)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(16,12)*{\lambda};
  (15,-3)*{\scs i};
  (2,-3)*{\scs j};
  (-6,-3)*{\scs i};(20,5)*{\bullet}+(3,3)*{\scs c};(28,5)*{\bullet}+(3,3)*{\scs b}; (36,5)*{\bullet}+(3,3)*{\scs a};
   (20,8)*{\lfline};(28,8)*{\lfline};(36,8)*{\lfline};
  (16,22)*{\scap};(16,24)*{\lcap};(16,30)*{\xlcap};
  (16,-6)*{\scupef};(16,-10)*{\lcupef};(16,-15)*{\xlcupef};
\endxy}\;\;.
\end{equation}
The first term on the right-hand-side of \eqref{eq_vv1} can be simplified
\begin{eqnarray}
t^{-1}_{ij} \vcenter{
 \xy 0;/r.18pc/:
    (-4,-4)*{};(4,4)*{} **\crv{(-4,-1) & (4,1)}?(1)*\dir{>};
    (4,-4)*{};(-4,4)*{} **\crv{(4,-1) & (-4,1)}?(1)*\dir{>};
    (4,4)*{};(12,12)*{} **\crv{(4,7) & (12,9)}?(1)*\dir{>};
    (12,4)*{};(4,12)*{} **\crv{(12,7) & (4,9)}?(1)*\dir{>};
    (-4,12)*{};(4,20)*{} **\crv{(-4,15) & (4,17)}?(1)*\dir{>};
    (4,12)*{};(-4,20)*{} **\crv{(4,15) & (-4,17)}?(1)*\dir{>};
    (-4,4)*{}; (-4,12) **\dir{-};
    (12,-4)*{}; (12,4) **\dir{-};
    (12,12)*{}; (12,20) **\dir{-};
   (16,4)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(16,12)*{\lambda};
  (-6,-3)*{\scs i}; (6,-3)*{\scs j};(15,-3)*{\scs i};  (20,5)*{\bullet}+(3,3)*{\scs c};(28,5)*{\bullet}+(3,3)*{\scs b}; (36,5)*{\bullet}+(3,3)*{\scs a};
  (20,8)*{\lfline};(28,8)*{\lfline};(36,8)*{\lfline};
  (16,22)*{\scap};(16,24)*{\lcap};(16,30)*{\xlcap};
  (16,-6)*{\scupef};(16,-10)*{\lcupef};(16,-15)*{\xlcupef};
\endxy}\;
\;\; = \;\; t_{ij} \; \vcenter{ \xy 0;/r.18pc/:
 (8,4)*{ \hackcenter{\begin{tikzpicture}





    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,12)*{\lambda};
  (8,16)*{\lcap};
  (8,22)*{\xlcap};
 (8,14)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (0,0)*{\ecross};(-4,8)*{\seline};(4,8)*{\seline};
 (-12,4)*{\meline};
 (24,8)*{\fcross};
 (24,0)*{\fcross};
 (12,4)*{\mfline};
 (8,-10)*{\lcupef};
 (-6,-3)*{\scs i}; (6,-3)*{\scs i};(-15,-3)*{\scs j}; (12,5)*{\bullet}+(3,3)*{\scs c};(-12,5)*{\bullet}+(3,3)*{\scs b}; (-4,5)*{\bullet}+(3,3)*{\scs a};
 \endxy} \;.
\end{eqnarray}
using the biadjoint relations and equations~\eqref{eq_crossl-gen} and \eqref{eq_crossr-gen} to slide crossings around the annulus.  This diagram can be further simplified using the KLR relations
\begin{equation}
   \;\; \refequal{\eqref{eq_r2_ij-gen}}\;\;
   t_{ji}^3 \; \vcenter{ \xy 0;/r.18pc/:
 (8,4)*{ \hackcenter{\begin{tikzpicture}





    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,12)*{\lambda}; (8,16)*{\lcap};  (8,22)*{\xlcap}; (8,14)*{\scap};  (8,-6)*{\scupef};
  (8,-14)*{\xlcupef}; (0,0)*{\ecross}; (-4,8)*{\seline}; (4,8)*{\seline}; (-12,4)*{\meline};
 (28,4)*{\mfline}; (20,4)*{\mfline}; (12,4)*{\mfline}; (8,-10)*{\lcupef}; (-6,-3)*{\scs i};
  (6,-3)*{\scs i};  (-15,-3)*{\scs j}; (12,5)*{\bullet}+(3,3)*{\scs c};(-12,5)*{\bullet}+(4,3)*{\scs {b+1}}; (-4,5)*{\bullet}+(3,3)*{\scs a};
 \endxy}
 + \; t_{ji}^2 t_{ij} \;
\vcenter{ \xy 0;/r.18pc/:
 (8,4)*{ \hackcenter{\begin{tikzpicture}





    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,12)*{\lambda};
  (8,16)*{\lcap};
  (8,22)*{\xlcap};
 (8,14)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (0,0)*{\ecross};(-4,8)*{\seline};(4,8)*{\seline};
 (-12,4)*{\meline};
 (28,4)*{\mfline};
 (20,4)*{\mfline};
 (12,4)*{\mfline};
 (8,-10)*{\lcupef};
 (-6,-3)*{\scs i}; (6,-3)*{\scs i};(-15,-3)*{\scs j};
(12,5)*{\bullet}+(3,3)*{\scs c};(-12,5)*{\bullet}+(3,3)*{\scs b}; (-4,5)*{\bullet}+(4,3)*{\scs {a+1}};
 \endxy}
\end{equation}
where we freely slide dots through caps and cups using the dot cyclicity relation~\eqref{eq_cyclic_dot}.
The second term on the right-hand-side of \eqref{eq_vv1} can also be simplified
\[t^{-1}_{ij} \;
 \vcenter{
 \xy 0;/r.18pc/:
    (12,-4)*{};(4,4)*{} **\crv{(12,-1) & (4,1)}?(1)*\dir{>};
    (4,-4)*{};(12,4)*{} **\crv{(4,-1) & (12,1)}?(1)*\dir{>};
    (4,4)*{};(-4,12)*{} **\crv{(-,7) & (-4,9)}?(1)*\dir{>};
    (-4,4)*{};(4,12)*{} **\crv{(-4,7) & (4,9)}?(1)*\dir{>};
    (12,12)*{};(4,20)*{} **\crv{(12,15) & (4,17)}?(1)*\dir{>};
    (4,12)*{};(12,20)*{} **\crv{(4,15) & (12,17)}?(1)*\dir{>};
    (12,4)*{}; (12,12) **\dir{-};
    (-4,-4)*{}; (-4,4) **\dir{-};
    (-4,12)*{}; (-4,20) **\dir{-};
    (16,4)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(16,12)*{\lambda};
  (15,-3)*{\scs i};
  (2,-3)*{\scs j};
  (-6,-3)*{\scs i};(20,5)*{\bullet}+(3,3)*{\scs c};(28,5)*{\bullet}+(3,3)*{\scs b}; (36,5)*{\bullet}+(3,3)*{\scs a};
   (20,8)*{\lfline};(28,8)*{\lfline};(36,8)*{\lfline};
  (16,22)*{\scap};(16,24)*{\lcap};(16,30)*{\xlcap};
  (16,-6)*{\scupef};(16,-10)*{\lcupef};(16,-15)*{\xlcupef};
\endxy} \;
 = \;  t_{ij} \;\vcenter{ \xy 0;/r.18pc/:
 (8,4)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,12)*{\lambda};
  (8,16)*{\lcap};
  (8,22)*{\xlcap};
 (8,14)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (-8,0)*{\ecross};(-12,8)*{\seline};(-4,8)*{\seline};
 (4,4)*{\meline};
 (16,8)*{\fcross};
 (16,0)*{\fcross};
 (28,4)*{\mfline};
 (8,-10)*{\lcupef};
 (-2,-3)*{\scs i}; (6,-3)*{\scs j};(-15,-3)*{\scs i};(12,5)*{\bullet}+(3,1)*{\scs c};(20,5)*{\bullet}+(3,2)*{\scs b}; (28,5)*{\bullet}+(3,2)*{\scs a};
 \endxy}
=\]\[
   \refequal{\eqref{eq_r2_ij-gen}} \;\;
   t_{ij}^2  \;\; \vcenter{ \xy 0;/r.18pc/:
 (8,-3)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,4)*{\lambda};
  (8,8)*{\lcap};
  (8,14)*{\xlcap};
 (8,6)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (-8,0)*{\ecross};
 (4,0)*{\seline};
 (12,0)*{\sfline};
 (20,0)*{\sfline};
 (28,0)*{\sfline};
 (8,-10)*{\lcupef};
 (-2,-3)*{\scs i}; (15,-3)*{\scs j};(-15,-3)*{\scs i};
  (12,0)*{\bullet}+(4,3)*{\scs b+1};(20,0)*{\bullet}+(3,3)*{\scs c}; (28,0)*{\bullet}+(3,3)*{\scs a};
  \endxy}
 \;\; + \;\;t_{ij}t_{ji}
\vcenter{ \xy 0;/r.18pc/:
 (8,-3)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,4)*{\lambda};  (8,8)*{\lcap};
  (8,14)*{\xlcap};
 (8,6)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (-8,0)*{\ecross};
 (4,0)*{\seline};
 (12,0)*{\sfline};
 (20,0)*{\sfline};
 (28,0)*{\sfline};
 (8,-10)*{\lcupef};
 (-2,-3)*{\scs i}; (15,-3)*{\scs j};(-15,-3)*{\scs i};
   (12,0)*{\bullet}+(3,3)*{\scs b};(20,0)*{\bullet}+(4,3)*{\scs c+1}; (28,0)*{\bullet}+(3,3)*{\scs a};
 \endxy} \nn
\]
Combining terms and simplifying using that $t_{ij}^2=t_{ji}^2=1, \, v_{ij}=1$ for our choice of scalars, we have
\begin{equation} \label{fin_eq}
 \xy
 (-6,0)*{};
  (6,0)*{};
 (0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(0,2)*{\lambda};  (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs c};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs b};
   (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs a};
  \endxy
 \;\; = \;\;
   \vcenter{ \xy 0;/r.18pc/:
 (8,4)*{ \hackcenter{\begin{tikzpicture}





    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,12)*{\lambda}; (8,16)*{\lcap};  (8,22)*{\xlcap}; (8,14)*{\scap};  (8,-6)*{\scupef};
  (8,-14)*{\xlcupef}; (0,0)*{\ecross}; (-4,8)*{\seline}; (4,8)*{\seline}; (-12,4)*{\meline};
 (28,4)*{\mfline}; (20,4)*{\mfline}; (12,4)*{\mfline}; (8,-10)*{\lcupef}; (-6,-3)*{\scs i};
  (6,-3)*{\scs i};  (-15,-3)*{\scs j}; (12,5)*{\bullet}+(3,3)*{\scs c};(-12,5)*{\bullet}+(4,3)*{\scs {b+1}}; (-4,5)*{\bullet}+(3,3)*{\scs a};
 \endxy}\;
 + \;
\vcenter{ \xy 0;/r.18pc/:
 (8,4)*{ \hackcenter{\begin{tikzpicture}





    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,12)*{\lambda};
  (8,16)*{\lcap};
  (8,22)*{\xlcap};
 (8,14)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (0,0)*{\ecross};(-4,8)*{\seline};(4,8)*{\seline};
 (-12,4)*{\meline};
 (28,4)*{\mfline};
 (20,4)*{\mfline};
 (12,4)*{\mfline};
 (8,-10)*{\lcupef};
 (-6,-3)*{\scs i}; (6,-3)*{\scs i};(-15,-3)*{\scs j};
(12,5)*{\bullet}+(3,3)*{\scs c};(-12,5)*{\bullet}+(3,3)*{\scs b}; (-4,5)*{\bullet}+(4,3)*{\scs {a+1}};
 \endxy}
   \end{equation}
   \[ - \;\; \vcenter{ \xy 0;/r.18pc/:
 (8,-3)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,4)*{\lambda};
  (8,8)*{\lcap};
  (8,14)*{\xlcap};
 (8,6)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (-8,0)*{\ecross};
 (4,0)*{\seline};
 (12,0)*{\sfline};
 (20,0)*{\sfline};
 (28,0)*{\sfline};
 (8,-10)*{\lcupef};
 (-2,-3)*{\scs i}; (15,-3)*{\scs j};(-15,-3)*{\scs i};
  (12,0)*{\bullet}+(4,3)*{\scs b+1};(20,0)*{\bullet}+(3,3)*{\scs c}; (28,0)*{\bullet}+(3,3)*{\scs a};
  \endxy}
 \;\; - \;\;
\vcenter{ \xy 0;/r.18pc/:
 (8,-3)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,4)*{\lambda};  (8,8)*{\lcap};
  (8,14)*{\xlcap};
 (8,6)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (-8,0)*{\ecross};
 (4,0)*{\seline};
 (12,0)*{\sfline};
 (20,0)*{\sfline};
 (28,0)*{\sfline};
 (8,-10)*{\lcupef};
 (-2,-3)*{\scs i}; (15,-3)*{\scs j};(-15,-3)*{\scs i};
   (12,0)*{\bullet}+(3,3)*{\scs b};(20,0)*{\bullet}+(4,3)*{\scs c+1}; (28,0)*{\bullet}+(3,3)*{\scs a};
 \endxy} \nn.\]
By interchanging \(a\) and \(c\) in the equation  \eqref{fin_eq}, we get
 \begin{equation} \label{fin_eq2}
 \xy
 (-6,0)*{};
  (6,0)*{};
 (0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(0,2)*{\lambda};  (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs a};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs b};
   (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs c};
  \endxy
 \;\; = \;\;
   \vcenter{ \xy 0;/r.18pc/:
 (8,4)*{ \hackcenter{\begin{tikzpicture}





    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,12)*{\lambda}; (8,16)*{\lcap};  (8,22)*{\xlcap}; (8,14)*{\scap};  (8,-6)*{\scupef};
  (8,-14)*{\xlcupef}; (0,0)*{\ecross}; (-4,8)*{\seline}; (4,8)*{\seline}; (-12,4)*{\meline};
 (28,4)*{\mfline}; (20,4)*{\mfline}; (12,4)*{\mfline}; (8,-10)*{\lcupef}; (-6,-3)*{\scs i};
  (6,-3)*{\scs i};  (-15,-3)*{\scs j}; (12,5)*{\bullet}+(3,3)*{\scs a};(-12,5)*{\bullet}+(4,3)*{\scs {b+1}}; (-4,5)*{\bullet}+(3,3)*{\scs c};
 \endxy}\;
 + \;
\vcenter{ \xy 0;/r.18pc/:
 (8,4)*{ \hackcenter{\begin{tikzpicture}





    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,12)*{\lambda};
  (8,16)*{\lcap};
  (8,22)*{\xlcap};
 (8,14)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (0,0)*{\ecross};(-4,8)*{\seline};(4,8)*{\seline};
 (-12,4)*{\meline};
 (28,4)*{\mfline};
 (20,4)*{\mfline};
 (12,4)*{\mfline};
 (8,-10)*{\lcupef};
 (-6,-3)*{\scs i}; (6,-3)*{\scs i};(-15,-3)*{\scs j};
(12,5)*{\bullet}+(3,3)*{\scs a};(-12,5)*{\bullet}+(3,3)*{\scs b}; (-4,5)*{\bullet}+(4,3)*{\scs {c+1}};
 \endxy}
   \end{equation}
   \[ - \;\; \vcenter{ \xy 0;/r.18pc/:
 (8,-3)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,4)*{\lambda};
  (8,8)*{\lcap};
  (8,14)*{\xlcap};
 (8,6)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (-8,0)*{\ecross};
 (4,0)*{\seline};
 (12,0)*{\sfline};
 (20,0)*{\sfline};
 (28,0)*{\sfline};
 (8,-10)*{\lcupef};
 (-2,-3)*{\scs i}; (15,-3)*{\scs j};(-15,-3)*{\scs i};
  (12,0)*{\bullet}+(4,3)*{\scs b+1};(20,0)*{\bullet}+(3,3)*{\scs a}; (28,0)*{\bullet}+(3,3)*{\scs c};
  \endxy}
 \;\; - \;\;
\vcenter{ \xy 0;/r.18pc/:
 (8,-3)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,4)*{\lambda};
  (8,8)*{\lcap};
  (8,14)*{\xlcap};
 (8,6)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (-8,0)*{\ecross};
 (4,0)*{\seline};
 (12,0)*{\sfline};
 (20,0)*{\sfline};
 (28,0)*{\sfline};
 (8,-10)*{\lcupef};
 (-2,-3)*{\scs i}; (15,-3)*{\scs j};(-15,-3)*{\scs i};
   (12,0)*{\bullet}+(3,3)*{\scs b};(20,0)*{\bullet}+(4,3)*{\scs a+1}; (28,0)*{\bullet}+(3,3)*{\scs c};
 \endxy} \nn.\]
 Using the relation \eqref{eq_bubble_rel} and induction, one can easily prove the following equation:
 \begin{equation} \label{ac}
  \xy 0;/r.16pc/:
   (8,-3)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (8,8)*{\lcap};
 (8,6)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};
 (12,0)*{\sline};
 (20,0)*{\sline};
 (8,-10)*{\lcup};
  (-3.3,6)*{\bullet}+(-4,0)*{\scs a}; (4.7,6)*{\bullet}+(-2.7,0)*{\scs c};
  (22,0)*{\scs i};
 (8,3)*{\lambda};
 \endxy\; \; = - \;\;
 \xy 0;/r.16pc/:
   (8,-3)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (8,8)*{\lcap};
 (8,6)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};
 (12,0)*{\sline};
 (20,0)*{\sline};
 (8,-10)*{\lcup};
 (-3.3,6)*{\bullet}+(-4,0)*{\scs c}; (4.7,6)*{\bullet}+(-2.7,0)*{\scs a};
  (22,0)*{\scs i}; (8,3)*{\lambda};
 \endxy.
 \end{equation}
 Also, the following equation directly follows from \eqref{eq_nil_dotslide} and \eqref{ac}
 \begin{equation} \label{ac2}
 \xy
 (-6,0)*{};
  (6,0)*{};
   (0,2)*{\lambda};(0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
  (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs c};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs a};
  \endxy \;\;=\;\;
 \xy 0;/r.16pc/:
   (8,-3)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (8,8)*{\lcap};
 (8,6)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};
 (12,0)*{\sline};
 (20,0)*{\sline};
 (8,-10)*{\lcup};
 (-3.3,6)*{\bullet}+(-5,0)*{\scs a+1}; (4.7,6)*{\bullet}+(-2.7,0)*{\scs c};
  (22,0)*{\scs i}; (8,3)*{\lambda};
 \endxy\;\; + \;\;
 \xy 0;/r.16pc/:
   (8,-3)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
  \end{tikzpicture}}
 };
  (8,8)*{\lcap};
 (8,6)*{\scap};
 (8,-6)*{\scup};
 (0,0)*{\naecross};
 (12,0)*{\sline};
 (20,0)*{\sline};
 (8,-10)*{\lcup};
 (-3.3,6)*{\bullet}+(-5,0)*{\scs c+1}; (4.7,6)*{\bullet}+(-3.5,0)*{\scs a};
  (22,0)*{\scs i}; (8,3)*{\lambda};
 \endxy.
 \end{equation}
We add  the right and left hand sides of the equations \eqref{fin_eq} and \eqref{fin_eq2}, and after eliminating terms using \eqref{ac}, we get
\begin{equation}\label{fin_eq3}
 \xy
 (-6,0)*{};
  (6,0)*{};
(0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(0,2)*{\lambda};   (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs a};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs b};
   (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs c};
  \endxy
 \;\; +\;\;
 \xy
 (-6,0)*{};
  (6,0)*{};
(0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(0,2)*{\lambda};   (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs c};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs b};
   (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs a};
  \endxy
 \;\; =
   \end{equation}
   \[ =\; \;
\vcenter{ \xy 0;/r.18pc/:
 (8,4)*{ \hackcenter{\begin{tikzpicture}





    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,12)*{\lambda};
  (8,16)*{\lcap};
  (8,22)*{\xlcap};
 (8,14)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (0,0)*{\ecross};(-4,8)*{\seline};(4,8)*{\seline};
 (-12,4)*{\meline};
 (28,4)*{\mfline};
 (20,4)*{\mfline};
 (12,4)*{\mfline};
 (8,-10)*{\lcupef};
 (-6,-3)*{\scs i}; (6,-3)*{\scs i};(-15,-3)*{\scs j};
(12,5)*{\bullet}+(3,3)*{\scs c};(-12,5)*{\bullet}+(3,3)*{\scs b}; (-4,5)*{\bullet}+(4,3)*{\scs {a+1}};
 \endxy} - \;\;
\vcenter{ \xy 0;/r.18pc/:
(8,-3)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,4)*{\lambda};  (8,8)*{\lcap};
  (8,14)*{\xlcap};
 (8,6)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (-8,0)*{\ecross};
 (4,0)*{\seline};
 (12,0)*{\sfline};
 (20,0)*{\sfline};
 (28,0)*{\sfline};
 (8,-10)*{\lcupef};
 (-2,-3)*{\scs i}; (15,-3)*{\scs j};(-15,-3)*{\scs i};
   (12,0)*{\bullet}+(3,3)*{\scs b};(20,0)*{\bullet}+(4,3)*{\scs c+1}; (28,0)*{\bullet}+(3,3)*{\scs a};
 \endxy} \nn \;\;+
\]
\[+\;\;
\vcenter{ \xy 0;/r.18pc/:
 (8,4)*{ \hackcenter{\begin{tikzpicture}





    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,12)*{\lambda};
  (8,16)*{\lcap};
  (8,22)*{\xlcap};
 (8,14)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (0,0)*{\ecross};(-4,8)*{\seline};(4,8)*{\seline};
 (-12,4)*{\meline};
 (28,4)*{\mfline};
 (20,4)*{\mfline};
 (12,4)*{\mfline};
 (8,-10)*{\lcupef};
 (-6,-3)*{\scs i}; (6,-3)*{\scs i};(-15,-3)*{\scs j};
(12,5)*{\bullet}+(3,3)*{\scs a};(-12,5)*{\bullet}+(3,3)*{\scs b}; (-4,5)*{\bullet}+(4,3)*{\scs {c+1}};
 \endxy} \;\; - \;\;
\vcenter{ \xy 0;/r.18pc/:
(8,-3)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(8,4)*{\lambda};  (8,8)*{\lcap};
  (8,14)*{\xlcap};
 (8,6)*{\scap};
 (8,-6)*{\scupef};(8,-14)*{\xlcupef};
 (-8,0)*{\ecross};
 (4,0)*{\seline};
 (12,0)*{\sfline};
 (20,0)*{\sfline};
 (28,0)*{\sfline};
 (8,-10)*{\lcupef};
 (-2,-3)*{\scs i}; (15,-3)*{\scs j};(-15,-3)*{\scs i};
   (12,0)*{\bullet}+(3,3)*{\scs b};(20,0)*{\bullet}+(4,3)*{\scs a+1}; (28,0)*{\bullet}+(3,3)*{\scs c};
 \endxy} \nn.\]
 Combining the respective terms using the relation \eqref{ac2} in the equation \eqref{fin_eq3}, we have
 \begin{equation}
 \xy
 (-6,0)*{};
  (6,0)*{};
(0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(0,2)*{\lambda};   (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs a};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs b};
   (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs c};
  \endxy
 \;\; +\;\;
 \xy
 (-6,0)*{};
  (6,0)*{};
(0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(0,2)*{\lambda};   (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs c};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs b};
   (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs a};
  \endxy
 \;\; =
 \end{equation}
 \[=\;\;\xy
 (-6,0)*{};
  (6,0)*{};
(0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(0,2)*{\lambda};   (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs c};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs a};
   (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs b};
  \endxy
 \;\; +\;\;
 \xy
 (-6,0)*{};
  (6,0)*{};
(0,-2)*{ \hackcenter{\begin{tikzpicture}
    \path[draw, blue, very thick, fill=white]
    (-0.15,0) .. controls ++(0,.2) and ++(0,.2) .. (0.15,0)
            .. controls ++(0,-.2) and ++(0,-.2) .. (-0.15,0);
\end{tikzpicture}}};
(0,2)*{\lambda};   (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{<}
   ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs j};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs b};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs c};
   (-20,0)*{}="t1";  (20,0)*{}="t2";
  "t2";"t1" **\crv{(20,24) & (-20,24)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(20,-24) & (-20,-24)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs a};
  \endxy\;\;=
 \]
 \[= \mathsf{E}_{j,b}\mathsf{E}_{i,a}\mathsf{E}_{i,c} 1_{\lambda}+  \mathsf{E}_{i,a}\mathsf{E}_{i,c}\mathsf{E}_{j,b} 1_{\lambda}.
 \]
 Reversing the orientation of the arrows, we get the identity $$ \mathsf{F}_{i,a}\mathsf{F}_{j,b}\mathsf{F}_{i,c}1_{\lambda} +\mathsf{F}_{i,c}\mathsf{F}_{j,b}\mathsf{F}_{i,a}1_{\lambda} = \mathsf{F}_{i,a}\mathsf{F}_{i,c}\mathsf{F}_{j,b} 1_{\lambda}+\mathsf{F}_{j,b}\mathsf{F}_{i,a}\mathsf{F}_{i,c} 1_{\lambda}.$$
\end{proof}
