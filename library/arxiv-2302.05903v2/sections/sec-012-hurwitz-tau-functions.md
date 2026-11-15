---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-012-hurwitz-tau-functions
section_title: "Hurwitz tau-functions"
section_number: null
pages: 12-13
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.993
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
The combinatorial Borel transform allows one to enrich the set of the Hurwitz $\tau$-functions [@MMN; @AMMN] $$\begin{aligned}
\tau^{(n)}\{p^{(1)},\ldots,p^{(n)}\}:=\sum_R q^{|R|} d_R^{2-n} S_R\{p^{(1)}\}\ldots S_R\{p^{(n)}\}
\end{aligned}$$ to make the power of $d_R$ and the number of Schur functions independent: suppose $m>n$, then $$\begin{aligned}
\sum_R d_R^{2-m} S_R\{p^{(1)}\}\ldots S_R\{p^{(n)}\}
= \left<\tau^{(m)}\{p^{(1)},\ldots,p^{(n)},p^{(n+1)}, \ldots, p^{(m)}\}\right>_{p^{(n+1)}, \ldots , p^{(m)}}
\end{aligned}$$ Averaging here is performed over the $m-n$ sets of time variables. For example, a direct counterpart of ([\[factorialelimination\]](#factorialelimination){reference-type="ref" reference="factorialelimination"}) would be $$\begin{aligned}
\sum_R \frac{q^{|R|}}{d_R}
= \sum_R  \frac{q^{|R|}}{d_R}\underbrace{\left<S_R\{p^{(1)}\right>}_{1}\underbrace{\left<S_R\{p^{(2)}\right>}_{1}
\underbrace{\left<S_R\{p^{(3)}\right>}_{1}
 = \left< \tau^{(3)}\{p^{(1)},p^{(2)},p^{(3)}\}\right>_{p^{(1)},p^{(2)},p^{(3)}}
\end{aligned}$$ At the same time, from what we know about the spectrum of dimensions, $$\begin{aligned}
\sum_R \frac{q^{|R|}}{d_R} = \sum_R q^{|R|}\frac{|R|! }{{\rm dim}_R} =
 \sum_{r=0}^\infty r! \cdot q^{r}\left\{2 + 2\cdot\frac{1}{r-1}
 + 2\cdot \left( \frac{1}{\frac{r(r-3)}{2}} +  \frac{1}{\frac{(r-1)(r-2)}{2}}\right) +
\right.\nonumber\\ \left.
+  2\cdot \left( \frac{1}{\frac{r(r-1)(r-5)}{6}} +  \frac{1}{\frac{r(r-2)(r-4)}{3}}
+ \frac{1}{\frac{(r-1)(r-2)(r-3)}{6}}\right)
  + O(r^{-4})  \right\}
\label{dinvsum}
\end{aligned}$$ This first item corresponds to representations $[r]$ and $[1^{r}]$, the second, to $[r-1,1]$ and $[2,1^{r-2}]$ and so on: $$\begin{aligned}
{\rm dim}_{[r-1,1]}=  r-1\nonumber\\ \nonumber\\
{\rm dim}_{[r-2,2]}={r(r-3)\over 2}\nonumber\\
{\rm dim}_{[r-2,1,1]}={(r-1)(r-2)\over 2}\nonumber\\ \nonumber\\
{\rm dim}_{[r-3,3]}={r(r-1)(r-5)\over 6}\nonumber\\
{\rm dim}_{[r-3,2,1]}={r(r-2)(r-4)\over 3}\nonumber\\
{\rm dim}_{[r-3,1,1,1]}={(r-1)(r-2)(r-3)\over 6 } \nonumber\\ \nonumber\\
\ldots
\label{listdims}
\end{aligned}$$ It is important that this is a discrete spectrum and multiplicities stabilize at large $r$. The smallest dimensions, like listed in ([\[listdims\]](#listdims){reference-type="ref" reference="listdims"}) are made from polynomials like $\frac{r^m}{m!}\Big(1+O(r^{-1})\Big)$, but at another end of the spectrum the growth is already factorial. In particular, the biggest dimension $D_r$ of all ${\rm dim}_R$ at the given level $|R|=r$ is restricted at large $r$ by [@McKay]: $$\begin{aligned}
\sqrt{r!}e^{-\alpha_1\sqrt{r}(1+o(1))}\le D_r\le \sqrt{r!}e^{-\alpha_2\sqrt{r}(1+o(1))}
\end{aligned}$$ where $\alpha_{1,2}$ are some constants. Still this growth is much weaker than $r!$ in the numerator of ([\[dinvsum\]](#dinvsum){reference-type="ref" reference="dinvsum"}). Thus contributions with all $m$ are divergent at large $r=|R|$, and one can expect the whole series to be ambiguous. The same is true for any particular term in the expansion ([\[dinvsum\]](#dinvsum){reference-type="ref" reference="dinvsum"}).

We will deal with the divergent sums $\xi_{-\nu} =\sum_R \frac{q^{|R|}}{d_R^\nu}$ with negative powers of $d_R$ as with formal power series. Note that they have *integer*-valued coefficients, provided by inverse powers of representation dimensions $d_R =\frac{|R|!}{{\rm dim}_R}$ with multiplicities read from ([\[xim\]](#xim){reference-type="ref" reference="xim"}). Their plethystic logarithms $\Psi_\nu(k)$ also have an interesting interpretation. Indeed, consider $$\begin{aligned}
\xi_{-\nu} =
\sum_R \frac{q^{|R|}}{d_R^\nu} =\exp\left(\sum_{k=1}^\infty{\Psi_\nu(k)q^k\over k}\right)
\end{aligned}$$ Remarkably, all the coefficients $\Psi_\nu(k)$ are positive integers, and they can be interpreted as the numbers of subgroups of index $k$ in the fundamental group of a certain fiber space [@LM]. They are a little more complicated (multi-linear) combinations of powers of above-mentioned integers $d_R =\frac{|R|!}{{\rm dim}_R}$ so that in the decomposition $$\begin{aligned}
\label{Psi}
\Psi_\nu(k) = \sum_{n=1}^\infty c_n(k)\eta_n^\nu
\end{aligned}$$ the spectrum $\eta_n$ of $\Psi_\nu(k)$ is more complicated than the spectrum $d_R^{-1}$ of $\xi_{-\nu}$, with some of elements $\eta_n$ coming from products of $d_R^{-1}$, and the coefficients $c_n(k)$ are not obligatory positive (despite $\Psi_\nu(k)$ *is* positive), and, hence, they can not play a role of multiplicities.

One can compare the spectrum of $\xi_{-\nu}$ (the values of $d_R^{-1}$),

$$\begin{aligned}
\begin{array}{c||c|c|cc|ccc|cccc|ccccc|cccc}
|R| & 1 & 2 & 3 && 4 &&& 5 &&&& 6 &&&&&   \ldots
\\ \hline
d_R^{-1} &1 &2    & 3 & 6   & 8& 12 & 24 & 20 &24 & 30&  120
& 45 & 72 & 80 & 144 & 720 &
\end{array}
\label{primaryspectrum}
\end{aligned}$$ with the spectrum of $\Psi_\nu(k)$ appearing in ([\[Psi\]](#Psi){reference-type="ref" reference="Psi"}) (see Table 3 of [@LM], note that $\Psi_\nu(k)$ are denoted as $R_\nu(k)$ in [@LM]):

$$\begin{aligned}
\hspace{-1cm}\begin{array}{c||ccccccccccccccccccccccc}
\Psi_\nu(k)\Big({\rm Table}\ 3\Big) &\eta_1&\eta_2&\eta_3&\eta_4&\eta_5&\eta_6&\ldots&&&&&&&&&&&&
\\ \hline
\Psi_\nu(1) & 1 &&&&&&&&&&&&&&&&&
\\ \hline
\Psi_\nu(2) & 1&2 &&&&&&&&&&&&&&&&&&
\\ \hline
\Psi_\nu(3) & 1&2&3&&6&&&&&&&&&&&&&&&&
\\ \hline
\Psi_\nu(4) & 1&2&3&\boxed{4}&6&8&&12&24&&&&&&&&&&&
\\ \hline
\Psi_\nu(5) & 1&2&3&\boxed{4}&&8&&12&&&&20&&30&&&&&&120&
\\ \hline
 \Psi_\nu(6)& 1&2&3&\boxed{4}&6&8&\boxed{9}&12&&\boxed{16}&\boxed{18}&20&24&30&\boxed{36}&45&\boxed{48}&72&80&120&144&720
\\ \hline
\ldots
\end{array}
\nonumber
\end{aligned}$$

where the quantities in the boxes are the products of the powers of the primary elements of the spectrum from ([\[primaryspectrum\]](#primaryspectrum){reference-type="ref" reference="primaryspectrum"}), and for each $\Psi_\nu(k)$ only $\eta_n$ corresponding to non-zero $c_n$ in ([\[Psi\]](#Psi){reference-type="ref" reference="Psi"}) are specified.
