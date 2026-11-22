---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES"
section_id: sec-007-24-the-linkage-principle-and-blocks
section_title: "The linkage principle and blocks"
section_number: 2.4
pages: 10-14
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.996
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on T."
---
\label{sub-blocks}
Consider the alcove $\mathcal A_0$ 
and its closure $\bar{\mathcal A}_0$ given by
\[
\mathcal A_0=\{k\in\bZ\mid -1<k<l-1\},\quad\quad\bar{\mathcal A}_0=\{k\in\bZ\mid -1\leq k \leq l-1\}.
\]
We call $\mathcal A_0$ the \textit{fundamental alcove}. 
Any other alcove in $\bZ_{\geq -1}$ is 
clearly of the form $\mathcal A_0+il$ for 
some $i\in\bN$. Moreover, we call 
$-1,l-1\in\bar{\mathcal A}_0-\mathcal A_0$ \textit{walls of $\mathcal A_0$}.




The \textit{affine Weyl group} is 
$W_l=\langle s_{r},t_{r}\mid r\in\bZ\rangle$ where $s_{r}$ and $t_r$ act on $\bZ$ via
\[
s_{r}.k=-k-2+(4r+2)l,\quad\quad t_{r}.k=-k-2+4rl,\quad k\in\bZ
\]
Note that $W_l$ is isomorphic 
to the infinite dihedral group $D_{\infty}$: 
we have $W_l\cong \bZ/2\bZ\ltimes l\bZ\cong D_{\infty}$ 
(with $\bZ/2\bZ$ being the Weyl group of $\mathfrak{sl}_2$) and we denote 
the two generators of $D_{\infty}$ by $s$ and $t$ (with the evident association). 
They act ``alcove-wise'' as indicated in~\eqref{eq-alcove}.

 
We denote by $W_l.x$ the orbits 
in $\bZ_{\geq -1}$ under the 
action of the affine Weyl 
group acting on $x\in\bZ_{\geq -1}$. 
For $l=3$ this can be visualized as
\begin{equation}\label{eq-alcove}
\xy
(0,0)*{\includegraphics[scale=0.75]{res/figs/tilt/alcove.eps}};
(-47,0)*{-1};
(-37.5,0)*{0};
(-28,0)*{1};
(-18.5,0)*{2};
(-9.75,0)*{3};
(0,0)*{4};
(9.5,0)*{5};
(18.5,0)*{6};
(28,0)*{7};
(37.5,0)*{8};
(47,0)*{9};
(-18.5,-7.5)*{s\text{-wall}};
(37.5,-7.5)*{s\text{-wall}};
(9.5,7.5)*{t\text{-wall}};
(-18.5,12)*{r=0};
(37.5,12)*{r=1};
(9.5,-12)*{r=1};
(-50,-7.5)*{\text{dead-end}};
\endxy
\end{equation}
with red (or top) action 
by $s$ and green (or bottom) 
action by $t$.



We say $i\in\bN$ is \textit{linked} to $i^{\prime}\in\bN$ 
if there exists $w\in W_l$ such that $w.i=i^{\prime}$. We, by 
convention, set all $\Uq$-modules indexed by negative numbers to be zero.


The following is known as the 
\textit{$\mathfrak{sl}_2$-linkage principle}. 
The more 
general (and highly non-trivial) 
statement can be found in~\cite[Corollaries~4.4 and~4.6]{an2}.



\begin{thm}(\textbf{The linkage principle})\label{thm-link}
All composition factors of $\Tn i$ have maximal weights $i^{\prime}$ linked to 
$i$. Moreover, $\Tn i$ is a simple $\Uq$-module if $i\in W_l.(\bar{\mathcal A}_0-\mathcal{A}_0)$.

In addition, if $i$ is linked to an element of $\mathcal{A}_0$, then 
$\Tn i$ is a simple $\Uq$-module iff $i\in\mathcal{A}_0$.\makeqed
\end{thm}



\begin{proof}
Use Propositions~\ref{prop-weyl} and~\ref{prop-tilt} and Corollary~\ref{cor-weyl}.
\end{proof}




\begin{nota}\label{no-link}
We \textit{always} use $\lambda$ for 
elements in the fundamental alcove 
$\mathcal{A}_0$ and $\mu$ for elements 
on the walls of the fundamental alcove 
$\bar{\mathcal A}_0-\mathcal A_0$. Moreover, set 
\[
\mathcal A_i=\{i^{\prime}\mid il-1<i^{\prime}<(i+1)l-1\}=\mathcal A_0+il,\quad
\bar{\mathcal A}_i=\{i^{\prime}\mid il-1\leq i^{\prime}\leq (i+1)l-1\}=\bar{\mathcal A}_0+il,
\] 
for each $i\in\bN$. Suppose $\lambda\in\mathcal A_0$ 
and $\mu\in\bar{\mathcal A}_0-\mathcal A_0$. We write 
$\lambda_i$ and $\mu_i$ for the unique elements in 
$\mathcal A_i\cap W_l.\lambda$ and $\bar{\mathcal A}_i\cap W_l.\mu$. 
Note that, if $\mu=\mu_0=-1$, then $\mu_1=\mu_2$, $\mu_3=\mu_4$ and so 
forth, while for $\mu=\mu_0=l-1$ 
we have $\mu_0=\mu_1$, $\mu_2=\mu_3$ etc. See also~\eqref{eq-alcove}.
\end{nota}



We define the tilting generator $\Tn{\bbin}$ and 
its cut-off's $\Tn{\leq \bbm}$ that will play a 
crucial role in Section~\ref{sec-quiver}. By 
abuse of notation, we denote them in the same 
way for all $\lambda$ and $\mu$ and hope that 
it is clear from the context which ones we consider.


\begin{defn}(\textbf{The tilting generator})\label{defn-tiltgen}
Let $m\in\bN\cup\{\infty\}$. We call the $\Uq$-modules given by
\[
\Tn{\bbin}=\bigoplus_{i=0}^{\infty}\Tn{\lambda_i}\quad\text{and}\quad\Tn{\leq \bbm}=\bigoplus_{i=0}^m\Tn{\lambda_i}
\] 
the \textit{tilting generator} and its \textit{$m$-th cut-off}, respectively. 
Likewise for $\mu$'s instead of $\lambda$'s.
\end{defn}



Denote by $\T_{\lambda}$ for $\lambda\in\mathcal A_0$ 
the $\lambda$ \textit{block of} $\T$: all indecomposable summands of 
objects of $\T_{\lambda}$ should be of 
the form $\Tn i$ for $i\in W_l.\lambda$. Note that 
blocks are in general not indecomposable as categories.
We, using a similar notation on walls, note the following.



\begin{lem}\label{lem-block}
We have
\[
\T=\bigoplus_{\lambda\in\mathcal A_0}\T_{\lambda}\oplus \T_{-1}\oplus \T_{l-1}
\]
with semisimple categories 
$\T_{-1}$ and $\T_{l-1}$ equivalent 
to the corresponding $\Uv$-module categories. 
We have for all $\lambda\in\mathcal A_0$
(similar for $\T_{-1}$ and $\T_{l-1}$):
\begin{itemize}
\item[(a)] The categories $\T_{\lambda}$ 
are additive, closed under finite direct sums and under duals.
\item[(b)] The categories $\T_{\lambda}$ 
are full Krull-Schmidt subcategories of $\T$. 
Moreover, every indecomposable tilting 
in $\T_{\lambda}$ is of the form $\Tn i$ for some $i\in\bN$ and $i\in W_l.\lambda$.\makeqed
\end{itemize}
\end{lem}


\begin{proof}
This is now only a 
combination of Theorem~\ref{thm-link} and 
Lemma~\ref{lem-tiltcat}. Note that 
$\T_{-1}$ and $\T_{l-1}$ are equivalent 
to categories of $\Uv$-modules by Proposition~\ref{prop-tilt} part (a).
\end{proof}



\begin{nota}\label{no-linkb}
If it is clear from the context 
which $\lambda$ we consider, then we, 
by abuse of notation, write 
$\Tn{\lambda_i}=\Tn{\bbi}$ for short. Similarly for simple and (dual) 
Weyl modules, and on walls.
\end{nota}



\begin{ex}\label{ex-block}
Take $l=3$ again. Then we only have to consider
$\lambda=0,1$ and $\mu=-1,2$.



The indecomposable tiltings in $\T_0$ are 
$\Tn{i}$ for $i=0,4,6,\dots$ as a look 
at~\eqref{eq-alcove} indicates. For $\T_1$ 
they are $\Tn{i}$ for $i=1,3,7,\dots$. The 
two blocks $\T_{-1}$ and $\T_2$ are semisimple 
and consist of direct sums of $\Ln i\cong\Tn{i}$ 
for $i=5,11,\dots$ and for $i=2,8,\dots$ respectively.
\end{ex}



\begin{rem}\label{rem-tria}
As in the usual case for an 
indeterminate $v$, we have a 
triangular decomposition
$\Uq=\Uq^-\Uq^0\Uq^+$, see for example~\cite[Section~1]{apw}. 
There is a character $\chi_i\colon \Uq^0\to\bC$ for any $i\in\bN$ 
(how the character is 
determined by $i$ can be found in~\cite[Lemma~1.1]{apw}).
We note that the Weyl module $\Vn{i}$ 
has the following \textit{universal property}: 
for any $\Uq$-module $M$ there is an isomorphism of vector spaces
\[
\Hom_{\Uq}(\Vn{i},M)\cong\{m\in M_i\mid E^{(j)}m=0\text{ for all }j\in\bN\},
\]
where $M_i=\{m\in M\mid um=\chi_i(u)m,\; u\in\Uq^0\}$ is the $i$ weight space 
of $M$.
This together with Definition~\ref{defn-weyl}, 
Proposition~\ref{prop-weyl} and Corollary~\ref{cor-weyl} imply that
\[
\Hom_{\Uq}(\Vn{i},\Ln{j})\cong\Hom_{\Uq}(\Vn{i},\dVn{j})\cong\delta_{ij}\bC
\]
for all $i,j\in\bN$. In particular,
\begin{equation}\label{eq-SchurLemma}
\Hom_{\Uq}(\Ln{i},\Ln{j})\cong\delta_{ij}\bC,
\end{equation}
i.e. Schur's Lemma holds in our set-up (although $\bC$ is not 
algebraically closed). Note that this is true for general quantum groups over 
arbitrary fields, see~\cite[Corollary~7.4]{apw}.
In addition\footnote{We point out that this fails in general. An explicit counterexample can be found for example in~\cite[Section~5]{ak}.}, we get
\[
\Hom_{\Uq}(\dVn{i},\Vn{i})\cong\bC.
\]
for all $i\in\bN$ (by using 
Proposition~\ref{prop-weyl} and Corollary~\ref{cor-weyl}).
\end{rem}



We call the following maps 
\textit{up} $u^{\lambda}_i$, 
\textit{down} $d^{\lambda}_i$ and 
\textit{loop} $\varepsilon^{\lambda}_i$ 
(\textit{or simply} $u_i,d_i$ and $\varepsilon_i$) respectively.



\begin{prop}\label{prop-link}
There exist up to scalars unique 
$\Uq$-intertwiners $u^{\lambda}_i,d^{\lambda}_i$ with
\begin{gather*}
u^{\lambda}_i\colon \Tn{\lambda_i}\to\Tn{\lambda_{i+1}},\; i=0,1,\dots,\quad\quad d^{\lambda}_i\colon \Tn{\lambda_i}\to\Tn{\lambda_{i-1}},\; i=1,2,\dots,
\\
u^{\lambda}_{i}\circ u^{\lambda}_{i-1}=0=d^{\lambda}_i\circ d^{\lambda}_{i+1},\; i=1,2,\dots,\quad\quad d^{\lambda}_{i+1}\circ u^{\lambda}_i=\varepsilon_i^{\lambda}=u^{\lambda}_{i-1}\circ d^{\lambda}_{i},\; i=1,2,\dots
\\
\varepsilon_i^{\lambda}\circ\varepsilon_i^{\lambda}=0,\; i=1,2,\dots
,\quad\quad d^{\lambda}_1\circ u^{\lambda}_0=0,
\end{gather*}
for $\lambda\in\mathcal A_0$. 
The equation on the bottom right is called 
the \textit{dead-end relation}.\makeqed
\end{prop}



\begin{proof}
First let us assume that we are not in case of the 
dead-end relation (in fact, we leave it to 
the reader to verify this special case), 
that is, the indices $i$ are at least $1$. 
We want to use Proposition~\ref{prop-weyl} 
and Corollary~\ref{cor-weyl}. Moreover, we 
note that the $\Uq$-morphisms below will 
only be unique up to scalars and their 
precise form does not matter. We only 
assume that they are non-zero. In fact, 
by abuse of notation, we always use the 
same symbols, but the maps are of course different in general.




We consider
\[
\xymatrix{
    & \Ln{\lambda_i}\phantom{.} \ar@{^{(}->}[r] & \dVn{\lambda_i}\phantom{.} \ar@{->>}[r]^a & \Ln{\lambda_{i-1}}
                \ar@{->} `r/8pt[d] `/10pt[l] `^dl[ll]|b `^r/3pt[dll] [dll] \\
             & \Ln{\lambda_{i-1}} \ar@{^{(}->}[r]^c & \Vn{\lambda_{i}} \ar@{->>}[r]^d & \Ln{\lambda_{i}}
                \ar@{->} `r/8pt[d] `/10pt[l] `^dl[ll]|e `^r/3pt[dll] [dll] \\
             & \Ln{\lambda_{i}} \ar@{^{(}->}[r]^f & \dVn{\lambda_{i}} \ar@{->>}[r] & \Ln{\lambda_{i-1}}.
    }
\]
Hence, we see that $\Hom_{\Uq}(\dVn{\lambda_i},\Vn{\lambda_i})$ is 
one dimensional: as noted in Remark~\ref{rem-tria}, the 
hom-spaces between Weyl and dual Weyl modules are at 
most $1$-dimensional. The composite $cba$ ensures 
that the dimension is exactly $1$ since it spans the hom-space.




Likewise for $\Hom_{\Uq}(\Vn{\lambda_i},\dVn{\lambda_i})$ by 
using $fed$. Note that the composite $fedcba=0$ due to 
the fact that the middle row is exact. The same holds when the roles 
of $\Vn{\lambda_i}$ and $\dVn{\lambda_i}$ are exchanged. 
Moreover, note that the morphism from $\dVn{\lambda_i}$ to 
$\Vn{\lambda_i}$ uses only $\Ln{\lambda_{i-1}}$ while the 
other way around uses only $\Ln{\lambda_{i}}$. Thus, up 
to scalars, morphisms from $\dVn{\lambda_i}$ to $\Vn{\lambda_i}$ are 
the ``same'' as morphisms from $\Vn{\lambda_{i-1}}$ to $\dVn{\lambda_{i-1}}$.
We can now construct, by using Proposition~\ref{prop-tilt}, 
up $u_i^{\lambda}$ and 
down $d_i^{\lambda}$ 
as a composition of the following maps.
\[
\xymatrix{
    & \Vn{\lambda_i}\phantom{.} \ar@{^{(}->}[r] & \Tn{\lambda_i}\phantom{.} \ar@{->>}[r]^a & \Vn{\lambda_{i-1}}
                \ar@{->} `r/8pt[d] `/10pt[l] `^dl[ll]|b `^r/3pt[dll] [dll] \\
             & \Vn{\lambda_{i-1}} \ar@{^{(}->}[r]^c & \Tn{\lambda_{i-1}} \ar@{->>}[r]^d & \Vn{\lambda_{i-2}}
             \ar@{->} `r/8pt[d] `/10pt[l] `^dl[ll]|e `^r/3pt[dll] [dll] \\
             & \Vn{\lambda_{i-2}} \ar@{^{(}->}[r]^f & \Tn{\lambda_{i-2}} \ar@{->>}[r] & \Vn{\lambda_{i-3}}.
    }
\]
We define $d_i^{\lambda}$ to be the 
composite $cba$. Similar for $u_i^{\lambda}$, 
but using the right-hand side of part (b) of 
Proposition~\ref{prop-tilt}. By the same 
reasoning as above we see that they are unique up to scalars.




We have to check the relations between the 
various up $u_i^{\lambda}$ and down $d_i^{\lambda}$ maps 
now. To see that $u^{\lambda}_{i}\circ u^{\lambda}_{i-1}=0$ 
and $d^{\lambda}_i\circ d^{\lambda}_{i+1}=0$ we can simply 
use the second diagram above and its dual 
counterpart and the fact that the rows are exact. Now consider
\[
\xymatrix{
\Tn{\lambda_{i-1}}\ar@{<->}[d]|{\mathrm{id}} & \Vn{\lambda_{i-1}}\ar@{_{(}->}[l]\ar[d]|{\Ln{\lambda_{i-1}}\to\Ln{\lambda_{i-1}}} & \Tn{\lambda_{i}}\ar@{<->}[d]|{\mathrm{id}}\ar@{->>}[r]\ar@{->>}[l] & \dVn{\lambda_{i}}\ar@{^{(}->}[r]\ar[d]|{\Ln{\lambda_{i-1}}\to\Ln{\lambda_{i-1}}} & \Tn{\lambda_{i+1}}\ar@{<->}[d]|{\mathrm{id}}\\
\Tn{\lambda_{i-1}}\ar@{->>}[r] & \dVn{\lambda_{i-1}}\ar@{^{(}->}[r] & \Tn{\lambda_{i}} & \Vn{\lambda_{i}}\ar@{_{(}->}[l] & \Tn{\lambda_{i+1}}\ar@{->>}[l].
}
\]
Combining everything, we see that 
(up to scalars) $d^{\lambda}_{i+1}\circ u^{\lambda}_i=\varepsilon_i^{\lambda}=u^{\lambda}_{i-1}\circ d^{\lambda}_{i}\neq 0$. Moreover, by 
the reasoning above, the $\varepsilon_i^{\lambda}$ 
is an up to scalars unique non-zero 
$\Uq$-morphism $\Tn{\lambda_i}$ to $\Tn{\lambda_i}$ that squares to zero.
\end{proof}

\newpage

\begin{cor}\label{cor-homspaces}
Let $i,i^{\prime}\in\bN$. Then we have the following.
\begin{itemize}
\item[(a)] Outside of walls:
\[
\Hom_{\Uq}(\Tn{\lambda_i},\Tn{\lambda_{i^{\prime}}})\cong\begin{cases}\bC[\varepsilon],  & \text{if }|i-i^{\prime}|=0\text{ and }i=i^{\prime}\neq 0,\\
  \bC,  & \text{if }|i-i^{\prime}|=1 \text{ or }i=i^{\prime}=0,\\
  0,  & \text{if }|i-i^{\prime}|>1,\end{cases}
\]
where $\bC[\varepsilon]\cong \bC[X]/(X^2)$ denotes the $\bC$-algebra of dual numbers.
\item[(b)] On walls:
\[
\Hom_{\Uq}(\Tn{\mu_i},\Tn{\mu_{i^{\prime}}})\cong\begin{cases}\bC,  & \text{if }|i-i^{\prime}|=0,\\
  0,  & \text{if }|i-i^{\prime}|>0,\end{cases}
\]
where $\bC$ is the trivial $\Uq$-module.\makeqed
\end{itemize}
\end{cor}



\begin{proof}
Because of Proposition~\ref{prop-link}, we only 
need to verify (b). But since the $\Tn{\mu_i}$ 
are simple on walls (by Proposition~\ref{prop-tilt}), 
part (b) follows from ``Schur's Lemma''~\eqref{eq-SchurLemma}.
\end{proof}
