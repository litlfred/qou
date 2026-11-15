---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES"
section_id: sec-015-45-diagram-categories-for-endotgrl
section_title: "Diagram categories for Endo(Tgrl)"
section_number: 4.5
pages: 46-48
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.96
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on T."
---
\label{sub-projdia}



We denote by $\overline{\Mat}(\mathcal C)$ 
literally the same category as $\Mat(\mathcal C)$, 
but we allow \textit{countable} direct sums as 
objects and \textit{finitely supported} matrices as morphisms.
We carefully distinguish between 
red $r$ and green $g$ on one hand 
and $s,t\in W_l$ on the other. We 
think of an \textit{alternating} 
sequence (of length $i\geq 0$) of the 
former $x_{i-grg}$ to correspond (under 
Theorem~\ref{thm-diafortilt}) to $\Tn{\bbi}$ and 
of \textit{any} sequence of the latter $x=x_i\dots x_2x_1$ 
to correspond to $\Theta_x=\Theta_{x_i}\circ\cdots\circ\Theta_{x_1}$. 
Using this interpretation, we are going to make 
Proposition~\ref{prop-endograd2} explicit.
We define $\vec{\infty}$ to be the sequence of alternating $x_{i-grg}$ sequences
\[
\vec{\infty}=(\dots,rgrg,grg,rg,g,\emptyset),\;\vec{\infty}_i=x_{i-grg}\quad\text{for}\quad i=0,1,\dots,
\]
where we read the vector from right to left.





Moreover, given a finite sequence $x=x_i\dots x_2x_1$ with $x_i\in\{s,t\}$ we define
\[
x\cdot \vec{\infty}=(\dots,xrgrg,xgrg,xrg,xg,x),\;(x\cdot \vec{\infty})_i=xx_{i-grg}\quad\text{for}\quad i=0,1,\dots,
\]
where each entry is given by concatenation. In addition, we define
\[
xx_{i-grg}=\bigoplus_{i^{\prime}}x_{i^{\prime}-grg}^{m_{i^{\prime}}}\langle s_{i^{\prime}}\rangle
\]
where the multiplicity 
$m_{i^{\prime}}$ is the 
multiplicity of $\Tn{\bbi^{\prime}}$ in 
$\Theta_x(\Tn{\bbi})$ given inductively 
by part c of Corollary~\ref{cor-funcgrad3} 
(from where we also get the shifts $s_{i^{\prime}}$). 
Thus, we see $xx_{i-grg}$ as an object 
$\Ob(\overline{\Mat}(\QDk))$. Note that 
$xx_{0-grg}=0$ if $x$ starts with $r$ because of $\Theta_s(\Tn 0)=0$.




\begin{defn}\label{defn-diaforend1}
Denote by $\Mati(\QDk)$ the $\bC$-linear,
 graded category consisting of:
\begin{itemize}
\item Objects $\Ob(\Mati(\QDk))$ are 
finite sequences $x=x_i\dots x_2x_1$ 
with $x_i\in\{s,t\}$ (plus shifts). 
Moreover, the empty sequence $\emptyset$ is also an object.



\item The space of morphisms $\Hom_{\Mati(\QDk)}(x,x^{\prime})$ 
for $x,x^{\prime}\in\Ob(\Mati(\QDk))$ is the $\bC$-linear 
span of finitely supported (only a finite number of non-zero entries) matrices
\[
F=(F_{k^{\prime}k})_{k,k^{\prime}\in\bN}\in\Hom_{\overline{\Mat}(\QDk)}(x\cdot \vec{\infty},x^{\prime}\cdot \vec{\infty})
\]
of marked Soergel graphs $F_{k^{\prime}k}\colon (x\cdot \vec{\infty})_k\to (x^{\prime}\cdot \vec{\infty})_{k^{\prime}}$.



\item The diagonal part of $F$ consists 
of matrices $F^i\colon (x\cdot \vec{\infty})_i\to (x^{\prime}\cdot \vec{\infty})_i$.



\item Composition of morphisms is multiplication of matrices.


\end{itemize}
The spaces $\Hom_{\Mati(\QDk)}(x,x^{\prime})$ 
are graded $\bC$-vector spaces where the degree is 
given by $l(F_{k^{\prime}k})$ (the degree or length 
from Definition~\ref{defn-diacath}) for each entry of matrices $F$.
\end{defn}




Denote by $\Endo_{\Theta}^{\mathrm{fs}}(\Tgrl)$ the full 
subcategory of $\Endo(\Tgrl)$ consisting of 
only compositions of $\Theta_s$ and $\Theta_t$ (together with the 
condition of being finitely supported). 
Note that, by Proposition~\ref{prop-profunc}, 
we have
\[
\Kar(\Endo_{\Theta}^{\mathrm{fs}}(\Tgrl))\cong\Endo^{\mathrm{fs}}(\Tgrl).
\] 
Moreover, we denote by $\Mati(\QDk)_c$ the 
subcategory of $\Mati(\QDk)$ whose hom-spaces are
\begin{equation}\label{eq-homfunctors}
\Hom_{\Mati(\QDk)_c}(x,x^{\prime})=\{F\in\Hom_{\Mati(\QDk)}(x,x^{\prime})\mid FG=G^{\prime}F\},
\end{equation}
for $G\in\Hom_{\Mati(\QDk)}(x,x)$ and 
$G^{\prime}\in\Hom_{\Mati(\QDk)}(x^{\prime},x^{\prime})$ 
such that entry-wise there exists an $\Uq$-intertwiner 
$f\colon M\to M^{\prime}$ with 
$\mathcal{D}_{\infty}(G_{i^{\prime}i})=\Theta_x(f)$ and $\mathcal{D}_{\infty}(G^{\prime}_{i^{\prime}i})=\Theta_{x^{\prime}}(f)$. 
The reader may check that $\Mati(\QDk)_c$ is really a subcategory.




\begin{defn}\label{defn-diaforend2}
We define a functor
\[
\mathcal{D}^{\infty}\colon\Endo_{\Theta}^{\mathrm{fs}}(\Tgrl)\to\Mati(\QDk)_c
\]
on objects (we treat shifts again in the evident way) and morphisms as
\[
\Theta_x\mapsto x,\quad\text{and}\quad\eta\colon\Theta_x\to\Theta_{x^{\prime}},\,\eta_{\Tn{\bbi}}\colon\Theta_x\Tn{\bbi}\to\Theta_{x^{\prime}}\Tn{\bbi} \mapsto \mathrm{diag}(F)=(F^i)_{i\in\bN}\colon x\to x^{\prime},
\]
where $\mathrm{diag}(F)$ is a diagonal matrix 
consisting of the various $F^i$'s and, for 
each $\bbi$, the matrix of marked Soergel 
diagrams $F^i$ is component-wise given by 
$\bbi\mapsto\bbi$, $u_i\mapsto u_i$, 
$d_i\mapsto d_i$ and $\varepsilon_i\mapsto\varepsilon_i$ 
for all suitable indices $i$ and marked Soergel diagrams as in Corollary~\ref{cor-homspaces2}.
\end{defn}




\begin{lem}\label{lem-welldefagain}
The functor $\mathcal{D}^{\infty}\colon\Endo_{\Theta}^{\mathrm{fs}}(\Tgrl)\to\Mati(\QDk)_c$ 
is a well-defined functor between $\bC$-linear, graded categories.\makeqed
\end{lem}



\begin{proof}
The $\bC$-linearity is clear. 
In addition, the assignment is clearly degree preserving 
and well-defined component-wise (since the quiver relations are satisfied, 
see Proposition~\ref{prop-quiverrel}).




To see that it is well-defined note that 
$\eta_{\Tn{\bbi}}$ is a matrix consisting 
of $\Uq$-intertwiners between the direct 
summands of $\Theta_x\Tn{\bbi}$ and 
$\Theta_{x^{\prime}}\Tn{\bbi}$ (for each $\Tn{\bbi}$). 
These are sums of $\bbi,u_i,d_i$ and $\varepsilon_i$ 
by the isomorphism of Proposition~\ref{prop-isoofalg2}. 
To see that the relations are satisfied, note that, 
given any $\Uq$-intertwiner $f\colon M\to M^{\prime}$, 
the naturality of a transformation $\eta\colon \Theta_x\to \Theta_{x^{\prime}}$ says that
\begin{equation}\label{eq-natural}
\raisebox{0.9cm}{\begin{xy}
  \xymatrix{
      \Theta_x M \ar[r]^{\Theta_x f} \ar[d]_{\eta_M}    &   \Theta_x M^{\prime} \ar[d]^{\eta_{M^{\prime}}}  \\
      \Theta_{x^{\prime}} M \ar[r]_{\Theta_{x^{\prime}} f}             &   \Theta_{x^{\prime}} M^{\prime}  
  }
\end{xy}}
\end{equation}
commutes. Thus, the matrices coming from our assignment 
satisfy the condition~\eqref{eq-homfunctors}.
\end{proof}

\newpage


\begin{thm}(\textbf{Diagram categories for $\Endo(\Tgrl)$})\label{thm-diafortilt1}
The functor $\mathcal{D}^{\infty}$ is a graded equivalence.\makeqed
\end{thm}



\begin{proof}
As in Theorem~\ref{thm-diafortilt}, we have to show that $\mathcal{D}^{\infty}$ is 
essentially surjective, full and faithful.



That $\mathcal{D}^{\infty}$ is essentially surjective 
follows from the definition of the objects in 
$\Mati(\QDk)_d$. That it is faithful is a 
direct consequence of Proposition~\ref{prop-endograd2} 
combined with Theorem~\ref{thm-diafortilt}. 
That $\mathcal{D}^{\infty}$ is full is just a 
direct comparison of~\eqref{eq-homfunctors} and~\eqref{eq-natural}. 
\end{proof}




\begin{rem}\label{rem-possibleextension}
A possible 
generalization of our diagrammatic categories could follow from work of 
Elias and Libedinsky on Coxeter groups, 
see~\cite{el2}. The
underlying Coxeter group $W$ will for $A_n$ be the affine Weyl group, that is, the one given by the cyclic Dynkin diagram with $n+1$-nodes
\[
\xy 0;/r.17pc/:
(-5,8.66)*+{\bullet}="1";
(-5,-8.66)*+{\bullet}="2";
(10,0)*+{{\color{green}\bullet}}="3";
{\ar@{-} "1";"2" };
{\ar@{-} "2";"3" };
{\ar@{-} "3";"1" };
(0,-12.5)*{n=2};
\endxy\hspace*{1.5cm}
\xy 0;/r.17pc/:
(0,10)*+{\bullet}="1";
(-10,0)*+{\bullet}="2";
(0,-10)*+{\bullet}="3";
(10,0)*+{{\color{green}\bullet}}="4";
{\ar@{-} "1";"2" };
{\ar@{-} "2";"3" };
{\ar@{-} "3";"4" };
{\ar@{-} "4";"1" };
(0,-12.5)*{n=3};
\endxy\hspace*{1.5cm}
\xy 0;/r.17pc/:
(3.09,9.51)*+{\bullet}="1";
(-8.09,5.88)*+{\bullet}="2";
(-8.09,-5.88)*+{\bullet}="3";
(3.09,-9.51)*+{\bullet}="4";
(10,0)*+{{\color{green}\bullet}}="5";
{\ar@{-} "1";"2" };
{\ar@{-} "2";"3" };
{\ar@{-} "3";"4" };
{\ar@{-} "4";"5" };
{\ar@{-} "1";"5" };
(0,-12.5)*{n=4};
\endxy\hspace*{1.5cm}
\xy 0;/r.17pc/:
(5,8.66)*+{\bullet}="1";
(-5,8.66)*+{\bullet}="2";
(-10,0)*+{\bullet}="3";
(-5,-8.66)*+{\bullet}="4";
(5,-8.66)*+{\bullet}="5";
(10,0)*+{{\color{green}\bullet}}="6";
{\ar@{-} "1";"2" };
{\ar@{-} "2";"3" };
{\ar@{-} "3";"4" };
{\ar@{-} "4";"5" };
{\ar@{-} "5";"6" };
{\ar@{-} "1";"6" };
(0,-12.5)*{n=5};
\endxy\hspace*{1.5cm}\cdots
\]
where the green (rightmost) nodes indicate the affine nodes.
\end{rem}


\bibliographystyle{plainurl}
