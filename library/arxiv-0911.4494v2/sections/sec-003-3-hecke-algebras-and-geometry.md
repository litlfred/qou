---
doc_id: arxiv-0911.4494v2
doc_title: "The geometry of Markov traces"
section_id: sec-003-3-hecke-algebras-and-geometry
section_title: "Hecke algebras and geometry"
section_number: 3
pages: 4-5
source_pdf: 0911.4494v2.pdf
source_sha256: 1ba1c79686b12d98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.943
doc_brief: "The geometry of Markov traces — We give a geometric interpretation of the Jones-Ocneanu trace on the Hecke algebra, using the equivariant cohomology of sheaves on SLn."
---
\label{sec:hecke-algebr-geom}


Let $\FF_q$ denote a finite field with $q$ elements
and let $G$ denote a split semi-simple algebraic group over $\FF_q$
with fixed split maximal torus $T$ and Borel subgroup $B$. If $\Gamma$
denotes the Dynkin diagram of the root system of $G$, then we may
canonically identify $W_{\Gamma}$ with the Weyl group of $G$. Given any
$w \in W_{\Gamma}$ we denote by $\dot{w}$ a representative in $G$ for
$w \in W_{\Gamma}$. 







Consider the corresponding Bruhat decomposition
\[ G(\FF_q) = \bigsqcup_{w \in W_{\Gamma}} B(\FF_q) \cdot \dot{w} \cdot B(\FF_q). \] A classical
theorem of Iwahori identifies the convolution algebra of $B(\FF_q)
\times B(\FF_q)$-invariant $\C$-valued functions on $G(\FF_q)$ with $\Hec_{\Gamma}$, where
$q^{\nicefrac{1}{2}}$ is specialized at a fixed square root of $|\FF_q
| \in \C$. Under this identification the element $\si_i \in H_{\Gamma}$
corresponds to the characteristic function of the orbit $B(\FF_q)
\cdot \dot{s_i} \cdot B(\FF_q)$ multiplied by 
$q^{- \nicefrac{1}{2}}$.

The fact that the Hecke algebra arises as a convolution algebra
suggests a natural categorification using Grothendieck's
function-sheaf dictionary. Fix a prime $\ell$ different from the
characteristic of $\FF_q$ and let $\Qlb$ denote an algebraic
closure of the field of $\ell$-adic numbers.

We denote by $D^b_{B \times B}(G)$ the bounded $B \! \times \!B$-equivariant
derived category of mixed constructible $\Qlb$-sheaves
on $G$ (see, for example \cite{SGA4}, \cite{SGA4h}, \cite{BBD} and \cite{BL}), often referred to as the {\bf Hecke category}. There is a convolution product on $D^b_{B \times B}(G)$ which we denote by $\star$ (see \cite{SpIH}). We fix a square root
$q^{\nicefrac 12}$ of $q$ in $\Qlb$, which allows us to define a
square root $(\nicefrac 12)$ of the Tate twist $(1)$. 
We denote by $\langle m \rangle$ the shift-twist functor $[m](m/2)$ (note that $\langle m \rangle$ preserves weight).

\begin{defi} \label{def:ICnorm}
  Let $\IC_w$ denote the intersection cohomology complex corresponding
  to the $B \times B$ orbit $B\dot{w}B$, normalized so that the restriction
  of $\IC_w$ to $B\dot{w}B$ is $\underline{\Qlb}_{B\dot{w}B} \langle \ell(w)/2
  \rangle$.
\end{defi}

That is, we normalize intersection cohomology complexes so
  that the induced sheaf on $G/B$ is perverse and pure of weight 0.

Finally, let $D_{B \times B}(G)_0$ denote the subcategory of $D^b_{B
  \times B}(G)$ consisting of objects isomorphic to direct sums of
$\IC_w\langle m \rangle$ for $w \in W_{\Gamma}$ and $m \in \Z$ and
$\mathscr{K}_{B \times B}(G)_0$ its split Grothendieck group. We have:
\begin{itemize}
 \item The category $D_{B \times B}(G)_0$ is preserved under convolution (by the
   Decomposition theorem), and $\star$
  induces a ring structure on $\mathscr{K}_{B \times B}(G)_0$.
\item  The
  assignment $q^{1/2} \mapsto \langle {-1} \rangle $ makes
  $\mathscr{K}_{B \times B}(G)_0$ into an algebra over
  $\Z[q^{1/2},q^{-1/2}]$.
\end{itemize}
The following result is well-known:

\begin{thm}[See \cite{SpIH}]
\label{thm-heckeconv}
The Hecke algebra $\Hec_{\Gamma}$ can be identified with
$\mathscr{K}_{B \times B}(G)_0$. Under this identification the
Kazhdan-Lusztig basis element $C_w^{\prime}$ corresponds to the class of the
intersection cohomology complex $[ \IC_w ]$.
\end{thm}

For example, if $s$ is a simple reflection, then $C_s^{\prime} =
\sigma_s + q^{-\nicefrac 12}$ corresponds to
$\underline{\Qlb}_{P_s}\langle 1 \rangle$, the shift-twist of the
constant sheaf on the minimal parabolic subgroup $P_s = \overline{BsB}$.

The relationship between these sheaves and the Hecke algebra was an
important ingredient in the Kazhdan-Lusztig conjecture
\cite{KL79,KL80}.


Alternatively, one can consider the $B \! \times \! B$-equivariant cohomology of
$\IC_w$.  This is an indecomposable {\bf Soergel bimodule} 
$\hc_{\BB}(G;\IC_w)=S_w$ (for
more background on Soergel bimodules and their connections to
geometry, see the original paper
\cite{Soe92} of Soergel or authors' earlier paper \cite{WW}).
