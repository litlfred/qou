---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "arXiv:cond-mat/9811142v1 [cond-mat.mes-hall] 10 Nov 1998"
section_id: sec-006-4-gaussian-ensemble
section_title: "Gaussian ensemble"
section_number: 4
pages: 18-25
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.951
---
For the Gaussian ensemble, we see from ([\[2.4\]](#2.4){reference-type="ref" reference="2.4"}) that the corresponding monic orthogonal polynomials and normalization are $$\begin{aligned}
C_{n}(x) = 2^{-n}\, H_{n}(y), \quad \quad h_{n} = 2^{-n}\, \pi^{1/4}\, n! \, .
\label{4.1}
\end{aligned}$$ The skew orthogonal polynomials for both $\beta = 1$ and $\beta = 4$ initial conditions at $\tau = 0$ are known in terms of the $C_{n}(x)$ (see e.g. [@MM91]). Using these expansions, the general formula ([\[2.i\]](#2.i){reference-type="ref" reference="2.i"}) then gives $$\begin{aligned}
R_{2m}(x;\tau) e^{\gamma_{2m} \tau} & = & C_{2m}(x) e^{\gamma_{2m} \tau} 
\noindent \\
R_{2m+1}(x;\tau) e^{\gamma_{2m+1} \tau} & = & 
C_{2m+1}(x) e^{\gamma_{2m+1} \tau} - m C_{2m-1}(x)  e^{\gamma_{2m-1} \tau}
\noindent\\
r_{m}(0) & = & 2^{-2m+1} \sqrt{\pi} \Gamma(2m+1)
\label{4.2}
\end{aligned}$$ for $\beta = 1$ initial conditions, and $$\begin{aligned}
R_{2m}(x;\tau) e^{\gamma_{2m} \tau} & = & m! 
\sum_{l=0}^m e^{\gamma_{2l} \tau} {C_{2l}(x) \over l!} \nonumber \\
R_{2m+1}(x;\tau) e^{\gamma_{2m+1} \tau} & = & C_{2m+1}(x) e^{\gamma_{2m+1}
\tau} \\
r_m(0) & =  & 2^{-2m} \sqrt{\pi} \Gamma(2m+2)
\label{4.3}
\end{aligned}$$ for $\beta = 4$ initial conditions. Inverting these formulas for $\{R_{j}(x)\}$ in terms of $\{C_{l}(x)\}$ according to ([\[2.l\]](#2.l){reference-type="ref" reference="2.l"}) gives $$\begin{aligned}
\label{4.4}
\beta_{2m \, j} = \delta_{2m,j}, \qquad
\beta_{2m+1 \, j} = \left \{
\begin{array}{ll}m!/l!, & j=2l+1, \: l=0,1,\dots,m \\
0, & j=2l, \: l=0,1,\dots,m \end{array} \right.
\end{aligned}$$ for $\beta = 1$, while for $\beta =4$ we find $$\begin{aligned}
\label{4.5}
\beta_{2m \, j} = \left \{ \begin{array}{lll}1, & j=2m \\
-m, & j=2m-2 \\ 0, & {\rm otherwise} \end{array} \right. \qquad
\beta_{2m+1 \, j} = \delta_{2m+1, j}.
\end{aligned}$$

Here we will use these explicit values in the general formulas of Section 2 to compute the matrix elements in ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}). In particular, we will give their asymptotic form in the neighbourhood of the soft edge, which is specified by introducing the scaled variables $X$ and $t$ according to $$\begin{aligned}
x = \sqrt{2N} + 
\frac{X}{2^{1/2}N^{1/6}}\, , \quad \quad \tau = \frac{t}{N^{1/3}}\,   .
\label{4.6}
\end{aligned}$$ The corresponding scaled distribution function ([\[2.c\]](#2.c){reference-type="ref" reference="2.c"}), to be denoted $\rho_{(n+m)}^{\rm soft}$, is given by $$\begin{aligned}
\lefteqn{\rho_{(n+m)}^{\rm soft}(X_1^{(1)},\dots,X_n^{(1)};
t^{(1)};X_1^{(2)},\dots,X_m^{(2)};t^{(2)})} \nonumber \\ &&
= \lim_{N \to \infty}
\Big ( {1 \over 2^{1/2} N^{1/6}} \Big )^{n+m} \rho_{(n+m)}\Big ( \sqrt{2N} +
 {X_1^{(1)} \over 2^{1/2} N^{1/6}}, \dots,
\label{r.1}\nonumber \\ &&
\sqrt{2N} + {X_n^{(1)} \over 2^{1/2}N^{1/6}}; {t^{(1)} \over N^{1/3}};
\sqrt{2N} + {X_1^{(2)} \over 2^{1/2} N^{1/6}}, \dots,
\sqrt{2N} + {X_m^{(2)} \over 2^{1/2} N^{1/6}}; {t^{(2)} \over N^{1/3}} \Big )
\end{aligned}$$ Analogous to ([\[n.2\]](#n.2){reference-type="ref" reference="n.2"})--([\[n.5\]](#n.5){reference-type="ref" reference="n.5"}), the matrix elements of $\rho_{(n+m)}^{\rm soft}$ are computed from the formulas $$\begin{aligned}
\lefteqn{
S_1^{\rm soft}(X,Y;t_X,t_Y)} \nonumber \\ && =  \lim_{N \to \infty}
{e^{-N^{2/3}(t_Y - t_X)} \over 2^{1/2} N^{1/6}}
S \Big ( \sqrt{2N} + {X \over 2^{1/2} N^{1/6}},
 \sqrt{2N} + {Y \over 2^{1/2} N^{1/6}}; {t_X \over N^{1/3}},
 {t_Y \over N^{1/3}} \Big ) \label{r.2}
\end{aligned}$$ $$\begin{aligned}
\lefteqn{ 
\tilde{S}_1^{\rm soft}(X,Y;t_X,t_Y)} \nonumber \\ &&  =  \lim_{N \to \infty}
{e^{-N^{2/3}(t_Y - t_X)} \over 2^{1/2} N^{1/6}}
\tilde{S} \Big ( \sqrt{2N} + {X \over 2^{1/2} N^{1/6}},
 \sqrt{2N} + {Y \over 2^{1/2} N^{1/6}}; {t_X \over N^{1/3}},
  {t_Y \over N^{1/3}} \Big ) \label{r.3}
\end{aligned}$$ $$\begin{aligned}
\lefteqn{ 
\tilde{I}_1^{\rm soft}(X,Y;t_X,t_Y)} \nonumber \\ &&  =  \lim_{N \to \infty}
e^{N^{2/3}(t_Y + t_X)} \tilde{I} \Big ( \sqrt{2N} + {X \over 2^{1/2}
N^{1/6}},
 \sqrt{2N} + {Y \over 2^{1/2} N^{1/6}}; {t_X \over N^{1/3}},
   {t_Y \over N^{1/3}} \Big ) \label{r.4} 
\end{aligned}$$ $$\begin{aligned}
\lefteqn{
D_1^{\rm soft}(X,Y;t_X,t_Y)} \nonumber \\ & & = \lim_{N \to \infty}  
{e^{-N^{2/3}(t_Y + t_X)} 
 \over 2 N^{1/3}}
D \Big ( \sqrt{2N} + {X \over 2^{1/2}
N^{1/6}},
 \sqrt{2N} + {Y \over 2^{1/2} N^{1/6}}; {t_X \over N^{1/3}},
{t_Y \over N^{1/3}} \Big ). \label{r.5}
\end{aligned}$$ Here the scale factors in addition to $1/2^{1/2} N^{1/6}$ do not effect the value of ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}) because they result from a transformation of the form ([\[n.6\'\]](#n.6'){reference-type="ref" reference="n.6'"}).

## $\beta = 1$ initial conditions

We see from ([\[4.4\]](#4.4){reference-type="ref" reference="4.4"}) that for $N$ even and $p \geq N$ $$\begin{aligned}
\beta_{p l} = \beta_{p N-1}\, \beta_{N-1 l} \,  .
\label{4.7}
\end{aligned}$$ Substituting in the formula ([\[2.1e\]](#2.1e){reference-type="ref" reference="2.1e"}) for $S_{2}$ and using ([\[2.l\]](#2.l){reference-type="ref" reference="2.l"}) and ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}) we thus have $$\begin{aligned}
S_2(x,y;\tau_x,\tau_y) & = & \sqrt{w(y)} \Big (
{\Phi_{N-2}(x;\tau_x) \over r_{N/2 - 1}(0)} e^{\gamma_{N-2} \tau_x} -
\sqrt{w(x)} {C_{N-1}(x) e^{-\gamma_{N-1} \tau_x} \over h_{N-1}} \Big )
\nonumber \\
&& \times C_{N-1}(y) e^{\gamma_{N-1} \tau_y}.
\label{4.8}
\end{aligned}$$

To compute the scaled limit we make use of the asymptotic expansion [@Sz] $$\begin{aligned}
\label{4.9}
e^{-x^2/2} H_n(x) = \pi^{-3/4} 2^{n/2 + 1/4} (n!)^{1/2} n^{-1/12}
\Big ( \pi {\rm Ai}(-u) + {\rm O}(n^{-2/3}) \Big )
\end{aligned}$$ where $x = (2n)^{1/2} - u/2^{1/2}n^{1/6}$. This gives $$\begin{aligned}
\label{4.10}
\sqrt{w(y)} C_{N-1}(y) \Big |_{y = (2N)^{1/2} + Y/2^{1/2} N^{1/6}} 
\sim \pi^{1/4} 2^{-(N-1)/2 + 1/4}(N-1)!^{1/2} N^{-1/12}
{\rm Ai}(Y).
\end{aligned}$$ Also, from ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}), ([\[4.1\]](#4.1){reference-type="ref" reference="4.1"}) and ([\[4.4\]](#4.4){reference-type="ref" reference="4.4"}) $$\begin{aligned}
f(x;\tau_x) & := & {\Phi_{N-2}(x;\tau_x) \over r_{N/2 - 1}(0)}
e^{\gamma_{N-2} \tau_x} - \sqrt{w(x)} {C_{N-1}(x) e^{-\gamma_{N-1} \tau_x}
\over h_{N-1}} \\
& = & {e^{-x^2/2} \over (N/2 - 1)!} e^{-N \tau_x}
\sum_{p=0}^\infty {(N/2 + p)! \over \sqrt{\pi} (N + 2p + 1)!}
H_{N + 2p + 1}(x) e^{-(2p + 3/2) \tau_x}.
\nonumber
\end{aligned}$$ Noting that for large $N$ $$\begin{aligned}
\nonumber 
{(N/2 + p)! \over ((N + 2p + 1)!)^{1/2}}
{((N-1)!)^{1/2} \over (N/2 - 1)!} \sim 2^{-(p+1)}
\end{aligned}$$ and making use of ([\[4.10\]](#4.10){reference-type="ref" reference="4.10"}) with $n = N + 2p + 1$, $-u \sim X - 2p/N^{1/3}$ shows $$\begin{aligned}
\label{4.11}
\lefteqn{((N-1)!)^{1/2} f \Big ( (2N)^{1/2} + {X \over 2^{1/2} N^{1/6}};
{t_X \over N^{1/3}} \Big ) } \nonumber
\\ && \sim e^{-N^{2/3} t} 2^{(N-1)/2} 2^{1/4} \pi^{-1/4} N^{-1/12}
{N^{1/3} \over 2} \int_0^\infty {\rm Ai}(X - v) e^{-vt_X} \, dv.
\end{aligned}$$ Hence $$\begin{aligned}
 \lefteqn{
S_2 \Big (  (2N)^{1/2} + {X \over 2^{1/2} N^{1/6}},
 (2N)^{1/2} + {Y \over 2^{1/2} N^{1/6}}; {t_X \over N^{1/3}},
 {t_Y \over N^{1/3}} \Big )} \nonumber \\ && \sim
 e^{N^{2/3}(t_Y - t_X)} 2^{-1/2} N^{1/6} {\rm Ai}(Y)
 \int_0^\infty {\rm Ai}(X - v) e^{-vt_X} \, dv.
\label{4.12}
\end{aligned}$$

Now consider $S_{1}$ as defined by ([\[2.1d\]](#2.1d){reference-type="ref" reference="2.1d"}). Substituting ([\[4.1\]](#4.1){reference-type="ref" reference="4.1"}) we see that the asymptotics can be determined by writing the sum so that the sum index $p$ is replaced by $N-p$, and then using Stirling's formula and ([\[4.10\]](#4.10){reference-type="ref" reference="4.10"}). We thus find $$\begin{aligned}
 \lefteqn{
S_1 \Big (  (2N)^{1/2} + {X \over 2^{1/2} N^{1/6}},
(2N)^{1/2} + {Y \over 2^{1/2} N^{1/6}}; {t_X \over N^{1/3}},
{t_Y \over N^{1/3}} \Big )} \nonumber \\ && \sim
e^{N^{2/3}(t_Y - t_X)} 2^{1/2} N^{1/6} 
\int_0^\infty {\rm Ai}(X + v) {\rm Ai}(Y + v) e^{-v(t_Y - t_X)} \, dv.
\label{4.13}
\end{aligned}$$ Adding together ([\[4.12\]](#4.12){reference-type="ref" reference="4.12"}) and ([\[4.13\]](#4.13){reference-type="ref" reference="4.13"}) and substituting for $S$ in ([\[r.2\]](#r.2){reference-type="ref" reference="r.2"}) we thus have $$\label{4.13'}
S_1^{\rm soft}(X,Y;t_X,t_Y) = 
\int_0^\infty {\rm Ai}(X + v) {\rm Ai}(Y + v) e^{-v(t_Y - t_X)} \, dv
 + {1 \over 2}
 {\rm Ai}(Y)
  \int_0^\infty {\rm Ai}(X - v) e^{-vt_X} \, dv.$$

### Asymptotics of $\tilde{I}(x, y; \tau_{x}, \tau_{y})$

We know from ([\[2.p\]](#2.p){reference-type="ref" reference="2.p"}) that $\tilde{I}$ is defined in terms of $\{\Phi_{l}(\cdot ; \tau)\}$. The asymptotics of $\Phi_{2k-2}$ is calculated in an analogous fashion to the expansion ([\[4.11\]](#4.11){reference-type="ref" reference="4.11"}). Thus after noting $$\begin{aligned}
\lefteqn{\Phi_{N+2k-2}(x;\tau) e^{\gamma_{N+2k-2} \tau} } \\ &&
=
{r_{N/2 + k - 1}(0) \over (N/2 + k -1)!} e^{-N \tau}
\sum_{m=k-1}^\infty {H_{2m+N + 1}(x) (N/2 + m)! \over
\pi^{1/2} (N + 2m + 1)!} e^{-(2m+3/2) \tau}
\end{aligned}$$ we find $$\begin{aligned}
\Phi_{N+2k-2}\Big ( (2N)^{1/2} + {X \over 2^{1/2} N^{1/6}};
{t_X \over N^{1/3}} \Big ) e^{\gamma_{N+2k-2} t_X/N^{1/3}} \sim
{r_{N/2 + k -1}(0) \over ((N-1)!)^{1/2}}
{(N/2 - 1)! \over (N/2 + k - 1)!}
 \nonumber \\
\times  e^{-N^{2/3} t_X}
2^{(N-1)/2} 2^{1/4} \pi^{-1/4} N^{-1/12} {N^{1/3} \over 2}
\int_{2k/N^{1/3}}^\infty {\rm Ai}(X - v) e^{-v t_X} \, dv.
\label{4.14}
\end{aligned}$$

Consider now $\Phi _{2k-1}$. We note from ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}), ([\[4.1\]](#4.1){reference-type="ref" reference="4.1"}) and ([\[4.4\]](#4.4){reference-type="ref" reference="4.4"}) that $$\begin{aligned}
\Phi_{N+2k-1}(y;\tau) e^{\gamma_{N+2k-1} \tau} = - \sqrt{w(y)}
r_{N/2 + k -1}(0) {H_{N + 2k - 2}(y) \over \pi^{1/2}
(N + 2k - 2)!} e^{-N \tau} e^{- (2k - 3/2) \tau}
\nonumber
\end{aligned}$$ so use of ([\[4.9\]](#4.9){reference-type="ref" reference="4.9"}) gives $$\begin{aligned}
\label{4.15}
\Phi_{N+2k-1}\Big ( (2N)^{1/2} + {Y \over 2^{1/2} N^{1/6}};
{t_Y \over N^{1/3}} \Big ) e^{\gamma_{N+2k-1} \tau_Y/N^{1/3}} \sim
- r_{N/2 + k -1}(0) e^{-N^{2/3} t_Y} \nonumber \\
\times e^{-2k t_Y/N^{1/3}} 
\pi^{-1/4} 2^{(N + 2k - 2)/2 + 1/4} ((N + 2k - 2)!)^{1/2} N^{-1/12}
{\rm Ai} (Y - {2k \over N^{1/3}}).
\end{aligned}$$ Multiplying ([\[4.14\]](#4.14){reference-type="ref" reference="4.14"}) and ([\[4.15\]](#4.15){reference-type="ref" reference="4.15"}) together, substituting in ([\[2.p\]](#2.p){reference-type="ref" reference="2.p"}) and making use of the explicit value of $r_{m}(0)$ from ([\[4.2\]](#4.2){reference-type="ref" reference="4.2"}), we then find $$\begin{aligned}
\label{4.16}
\tilde{I}_1^{\rm soft}(X,Y;t_X,t_Y) =
\int_0^\infty ds \, {\rm Ai}(Y - s) e^{-s t_Y}
\int_s^\infty {\rm Ai}(X - v) e^{-vt_x} dv - ( X \leftrightarrow Y )
\end{aligned}$$

### Asymptotics of $D(x, y; \tau_{x}, \tau_{y})$

Here the asymptotics of $\{R_{m}(\cdot ; \tau)\}$ are required. Now, from ([\[2.i\]](#2.i){reference-type="ref" reference="2.i"}) and ([\[4.2\]](#4.2){reference-type="ref" reference="4.2"}) we have $$\begin{aligned}
\nonumber 
R_{N - 2l - 2}(x;\tau) e^{\gamma_{N - 2l - 2} \tau} = 2^{-(N - 2l - 2)}
H_{N - 2l - 2}(x) e^{\gamma_{N - 2l - 2} \tau}.
\end{aligned}$$ Use of ([\[4.9\]](#4.9){reference-type="ref" reference="4.9"}) then gives $$\begin{aligned}
\label{4.17}
\lefteqn{
\sqrt{w(x)} R_{N - 2l - 2}(x;\tau) e^{\gamma_{N - 2l - 2} \tau}
\bigg |_{\begin{array}{l} \scriptstyle x = (2N)^{1/2} + X/2^{1/2} N^{1/6}  \\ 
 \scriptstyle \tau = t_X / N^{1/3}\end{array}} \sim e^{N^{2/3} t_X}} \nonumber\\
&& \times  e^{-2l t_X /N^{1/3}} \pi^{1/4}
2^{-(N - 2l - 2)/2} 2^{1/4} ((N - 2l - 2)! )^{1/2} N^{-1/12}
{\rm Ai} \Big ( X + {2l \over N^{1/3}} \Big ).
\end{aligned}$$ Furthermore $$\begin{aligned}
\label{4.17'}
R_{2m+1}(x;\tau) e^{\gamma_{2m+1} \tau} & = &
2^{-(2m+1)} H_{2m+1}(x) e^{\gamma_{2m+1} \tau} - m
2^{-(2m-1)} H_{2m - 1}(x) e^{\gamma_{2m - 1} \tau} \nonumber
\\ & = &
- e^{\gamma_{2m + 1} \tau} e^{x^2 / 2}
{d \over dx} \Big ( e^{-x^2 / 2} 2^{-2m} H_{2m}(x) \Big ) \nonumber \\
&&
- m 2^{-(2m - 1)} H_{2m - 1}(x) e^{\gamma_{2m - 1} \tau}
( 1 - e^{2 \tau} ),
\end{aligned}$$ and use of ([\[4.9\]](#4.9){reference-type="ref" reference="4.9"}) gives for the asymptotics $$\begin{aligned}
\label{4.18}
\lefteqn{
\sqrt{w(x)} R_{N - 2l - 1}(y;\tau) e^{\gamma_{N - 2l - 1} \tau}
\bigg |_{\begin{array}{l} \scriptstyle
y = (2N)^{1/2} + Y/2^{1/2} N^{1/6}  \\ 
 \scriptstyle
\tau = t_Y / N^{1/3}\end{array}} \sim e^{N^{2/3}t_Y}} \nonumber \\
&& \times \pi^{1/4} 2^{-(N - 2l - 2)/2} 
2^{3/4} ((N - 2l - 2)!)^{1/2} N^{1/12}
{d \over ds} \Big ( e^{-s t_Y} {\rm Ai} (Y + s) \Big ), 
\end{aligned}$$ $s:= 2l / N$. Multiplying together ([\[4.17\]](#4.17){reference-type="ref" reference="4.17"}) and ([\[4.18\]](#4.18){reference-type="ref" reference="4.18"}), dividing by $r_{(N-2l-2)/2}$ and summing over $l$ (which is of the form of a Riemann integral) we thus obtain $$\begin{aligned}
\label{4.19}
D_1^{\rm soft}(X,Y;t_X,t_Y) = {1 \over 4} \int_0^\infty ds \,
e^{-st_X} {\rm Ai}(X + s) {d \over ds} \Big ( e^{-st_Y}
{\rm Ai}(Y + s) \Big ) - (X \leftrightarrow Y)
\end{aligned}$$

### Asymptotics of $g(x, y; \tau_{y} - \tau_{x})$

According to ([\[2.3\]](#2.3){reference-type="ref" reference="2.3"}) and ([\[2.4\]](#2.4){reference-type="ref" reference="2.4"}) $$\begin{aligned}
\label{4.19'}
g(x,y;\tau) = e^{-(x^2 + y^2)/2}
\sum_{j=0}^\infty {H_j(x) H_j(y) e^{ - (j + 1/2) \tau} \over 
\pi^{1/2} 2^j j!}
\end{aligned}$$ This summation can be evaluated in closed form [@Er] giving $$\begin{aligned}
\nonumber
g(x,y;\tau) = e^{-(x^2 + y^2)/2}
{e^{-\tau/2} \over (1 - e^{-2\tau})^{1/2}}
\exp \Big ( - {e^{-2 \tau} \over 1 - e^{-2 \tau} } (x - y)^2 \Big )
\exp \Big ( {2 e^{-\tau} \over 1 - e^{-2\tau} } xy \Big )
\end{aligned}$$ Hence $$\begin{aligned}
\nonumber
g \Big ( (2N)^{1/2} + {X \over \sqrt{2} N^{1/6}},
(2N)^{1/2} + {Y \over \sqrt{2} N^{1/6}}; {t \over N^{1/3}} \Big )
\sim {N^{1/6} \over (2t)^{1/2}}
e^{- t N^{2/3}} e^{-(X-Y)^2/4t - t(X+Y)/2}.
\end{aligned}$$ Alternatively, proceeding as in the derivation of ([\[4.13\]](#4.13){reference-type="ref" reference="4.13"}), we can deduce from ([\[4.19\'\]](#4.19'){reference-type="ref" reference="4.19'"}) that $$\begin{aligned}
\label{4.19''}\lefteqn{
g \Big ( (2N)^{1/2} + {X \over \sqrt{2} N^{1/6}},
(2N)^{1/2} + {Y \over \sqrt{2} N^{1/6}}; {t \over N^{1/3}} \Big )}
\nonumber \\ &&
\sim e^{- N^{2/3} t} 2^{1/2} N^{1/6} \int_{-\infty}^\infty
{\rm Ai}(X + v) {\rm Ai}(Y + v) e^{vt} \, dv
\end{aligned}$$ Dividing by $e^{- N^{2/3} t}
2^{1/2} N^{1/6}$, replacing $t$ by $t_X - t_Y$ and subtracting from ([\[4.13\'\]](#4.13'){reference-type="ref" reference="4.13'"}) shows $$\begin{aligned}
\tilde{S}_1^{\rm soft}(X,Y;t_X,t_Y) & = & -
 \int_{-\infty}^0 
 {\rm Ai}(X + v) {\rm Ai}(Y + v) e^{-v(t_Y - t_X) } \, dv \nonumber \\
&& +
 {1 \over 2} {\rm Ai}(Y) \int_0^\infty {\rm Ai} (X - v) e^{-vt_X} \, dv.
\end{aligned}$$

## $\beta = 4$ initial conditions

Here we want to again compute the scaled distribution ([\[r.1\]](#r.1){reference-type="ref" reference="r.1"}). As for $\beta = 4$ initial conditions in the Laguerre ensemble, we must modify the scale factor in ([\[r.4\]](#r.4){reference-type="ref" reference="r.4"}) and ([\[r.5\]](#r.5){reference-type="ref" reference="r.5"}) so that $$\begin{aligned}
\label{a.1}\lefteqn{
\tilde{I}_4^{\rm soft}(X,Y;t_X,t_Y)} \nonumber \\
&&
 = \lim_{N \to \infty}
{e^{N^{2/3}(t_X + t_Y)} \over 2 N^{1/3}}
\tilde{I} \Big ( (2N)^{1/2} + {X \over \sqrt{2} N^{1/6}},
(2N)^{1/2} + {Y \over \sqrt{2} N^{1/6}}; {t \over N^{1/3}} \Big ) 
\end{aligned}$$ $$\begin{aligned}
\lefteqn{
{D}_4^{\rm soft}(X,Y;t_X,t_Y)} \nonumber \\ &&  = \lim_{N \to \infty}
e^{-N^{2/3}(t_X + t_Y)} 
D \Big ( (2N)^{1/2} + {X \over \sqrt{2} N^{1/6}},
(2N)^{1/2} + {Y \over \sqrt{2} N^{1/6}}; {t \over N^{1/3}} \Big )
\label{a.2}
\end{aligned}$$

Substituting ([\[4.5\]](#4.5){reference-type="ref" reference="4.5"}) in ([\[2.1e\]](#2.1e){reference-type="ref" reference="2.1e"}) shows that in terms of $\{C_{l}(x)\}$, $S_{2}$ only consists of a single term, which reads explicitly $$\begin{aligned}
\label{4.2a}
S_2(x,y;\tau_x,\tau_y) = \sqrt{w(x) w(y)}
{C_N(x) e^{-\gamma_N \tau_x} \over h_N}
\Big ( - {N \over 2} \Big ) R_{N-2}(y;\tau_y) e^{\gamma_{N-2} \tau_y}.
\end{aligned}$$ The explicit form of $R_{N-2}(y; \tau_{y}) e^{\gamma_{N-2} \tau_{y}}$ is given by ([\[4.3\]](#4.3){reference-type="ref" reference="4.3"}). This expression however does not give a Riemann sum after substituting the asymptotic form of the integrand. Instead, we make use of the identity $$\begin{aligned}
\label{4.3a}
\sum_{l=0}^m {m! \over l!} 2^{-2l} H_{2l}(x) c^{-l} = - \alpha
(4c)^{-m} e^{\alpha x^2} \int_{-\infty}^x e^{-\alpha s^2}
H_{2m+1}(s) \, ds,
\end{aligned}$$ $c = (1 - \alpha)/\alpha$. This can be verified by multiplying both sides by $e^{-\alpha x^{2}}$ and differentiating (we also verify that both sides have the same $x \rightarrow \infty$ behaviour). Choosing $c = e^{-2\tau}$ and comparing with ([\[4.3\]](#4.3){reference-type="ref" reference="4.3"}) we see that $$\begin{aligned}
R_{2m}(y;\tau) e^{\gamma_{2m} \tau} & = &
- {e^{\tau/2} \over 1 + e^{-2 \tau} } (2 e^{-\tau})^{-2m}
e^{y^2/ (1 + e^{-2 \tau})} \int_{-\infty}^y
e^{-s^2/ (1 + e^{-2 \tau})} H_{2m+1}(s) \, ds \nonumber \\
& = &
 {e^{\tau/2} \over 1 + e^{-2 \tau} } (2 e^{-\tau})^{-2m}
 e^{y^2/ (1 + e^{-2 \tau})} \int_{y}^\infty
 e^{-s^2/ (1 + e^{-2 \tau})} H_{2m+1}(s) \, ds
\label{4.3b}
\end{aligned}$$ where to obtain the second equality the fact that the integrand is odd has been used.

With $x = (2N)^{1/2} + X/2^{1/2}N^{1/6}$, making the change of variables $s \mapsto (2N)^{1/2} + s$ and using the asymptotic expansion ([\[4.9\]](#4.9){reference-type="ref" reference="4.9"}) we see that $$\begin{aligned}
\sqrt{w(y)} R_{N - 2m}\Big ((2N)^{1/2} + {Y \over 2^{1/2} N^{1/6}};
{t \over N^{1/3}} \Big ) e^{\gamma_{N - 2m} t / N^{1/3}} \sim
2^{-3/4} N^{-1/4} \pi^{1/4} 2^{-(N - 2m)/2}  \nonumber
\\  
\times ((N - 2m + 1)!)^{1/2}
e^{N^{2/3} t} e^{Yt} \int_{Y+u}^\infty e^{-st} {\rm Ai}(s) \, ds,
\quad u := 2m/N^{1/3}
\label{4.3c}
\end{aligned}$$ For the $x$-dependent factor in ([\[4.2a\]](#4.2a){reference-type="ref" reference="4.2a"}), the asymptotic form of $\sqrt{w(x)} C_{N}(x)$ is given by ([\[4.10\]](#4.10){reference-type="ref" reference="4.10"}) with $N - 1$ replaced by $N$. Making use of the explicit value of $h_{N}$, we thus find $$\begin{aligned}
\label{4.3d}
\lefteqn{S_2 \Big ((2N)^{1/2} + {X \over 2^{1/2} N^{1/6}},
(2N)^{1/2} + {Y \over 2^{1/2} N^{1/6}};
{t_X \over N^{1/3}}, {t_Y \over N^{1/3}} \Big )} \nonumber \\ &&
 \sim
- {N^{1/6} \over 2^{1/2}} e^{-N^{2/3} (t_X - t_Y)}
{\rm Ai}(X) e^{Y t} \int_Y^\infty e^{-st} {\rm Ai}(s) \, ds.
\end{aligned}$$

The asymptotic form of the quantity $S_{1}$ as defined by ([\[2.1d\]](#2.1d){reference-type="ref" reference="2.1d"}) is given by ([\[4.13\]](#4.13){reference-type="ref" reference="4.13"}), since $S_{1}$ is the same for $\beta = 1$ and $\beta = 4$ initial conditions. Hence $$\begin{aligned}
\label{ls4}
S_4^{\rm soft}(X,Y;t_X,t_Y) & = &
\int_0^\infty {\rm Ai}(X + v) {\rm Ai}(Y + v) e^{-v(t_Y - t_X)} \,
dv \\ &&
- {1 \over 2} {\rm Ai}(X) e^{Yt} \int_Y^\infty e^{-st} {\rm Ai}(s) \, ds
\end{aligned}$$ Also, subtracting ([\[4.19\'\'\]](#4.19''){reference-type="ref" reference="4.19''"}) divided by $e^{-N^{2/3} t}2^{1/2}N^{1/6}$ (and with $t \mapsto t_X - t_Y$) gives $$\begin{aligned}
\tilde{S}_4^{\rm soft}(X,Y;t_X,t_Y) & = &
- \int_{-\infty}^0 {\rm Ai}(X + v) {\rm Ai}(Y + v) e^{-v(t_Y - t_X)} \,
dv \nonumber \\
&&- {1 \over 2} {\rm Ai}(X) e^{Yt} \int_Y^\infty e^{-st} {\rm Ai}(s) \, ds
\end{aligned}$$

### Asymptotics of $\tilde{I}(x, y; \tau_{x}, \tau_{y})$

First note from ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}), ([\[4.1\]](#4.1){reference-type="ref" reference="4.1"}), ([\[4.3\]](#4.3){reference-type="ref" reference="4.3"}) and ([\[4.5\]](#4.5){reference-type="ref" reference="4.5"}) that $$\begin{aligned}
\lefteqn{
\Phi_{2k-1}(x;\tau) e^{\gamma_{2k-1}\tau}} \\
 &  &
 = \sqrt{w(x)} e^{-\gamma_{2k-2} \tau} 2^{-2(k-1)} \Big (
{1 \over 2} H_{2k}(x) e^{-2\tau} - (2k-1) H_{2k-2}(x) \Big ) 
\\ &  & = -  e^{-\gamma_{2k-2} \tau} 2^{-2(k-1)} \bigg (
{d \over dx} \Big ( e^{-x^2/2} H_{2k-1}(x) \Big ) - {\sqrt{w(x)} \over 2}
H_{2k}(x) (e^{-2\tau} - 1) \Big )
\end{aligned}$$ (c.f. ([\[4.17\'\]](#4.17'){reference-type="ref" reference="4.17'"})). Use of ([\[4.9\]](#4.9){reference-type="ref" reference="4.9"}) gives for the asymptotics $$\begin{aligned}
\label{4.3e}
\lefteqn{ \Phi_{N - 2k - 1} \Big ( (2N)^{1/2} + {X \over 2^{1/2} N^{1/6}};
{t \over N^{1/3}} \Big ) e^{\gamma_{N-2k-1}t/N^{1/3}} \sim} \nonumber \\&&
- e^{-N^{2/3} t_X} \pi^{1/4} 2^{7/4} 2^{-(N-2k-1)/2} (N - 2k - 1)!^{1/2}
N^{1/12} {d \over ds} \Big ( e^{st_X} {\rm Ai}(X + s) \Big ),
\end{aligned}$$ $s : = 2 k/N$. Similarly $$\begin{aligned}
\nonumber
{1 \over r_{k-1}(0)} \Phi_{2k-2}(y;\tau) e^{\gamma_{2k-2}\tau} =
\sqrt{w(y)}  {H_{2k-1}(y) e^{-\gamma_{2k-1}\tau} \over \pi^{1/2}(2k-1)!}
\end{aligned}$$ and so $$\begin{aligned}
\label{4.3f}\lefteqn{
{1 \over r_{N/2 -k - 1}(0)} \Phi_{N-2k-2}\Big (
(2N)^{1/2} +  {Y \over 2^{1/2} N^{1/6}};
{t \over N^{1/3}} \Big ) e^{\gamma_{N-2k-2}t/N^{1/3}} \sim} \nonumber \\&&
e^{-N^{2/3} t_Y} e^{st_Y} \pi^{-1/4}
2^{(N-2k-1)/2 + 1/4} (N - 2k - 1)!^{-1/2} N^{-1/12}
{\rm Ai}(Y + s).
\end{aligned}$$ Multiplying together ([\[4.3e\]](#4.3e){reference-type="ref" reference="4.3e"}) and ([\[4.3f\]](#4.3f){reference-type="ref" reference="4.3f"}) and summing according to ([\[2.p\]](#2.p){reference-type="ref" reference="2.p"}) we see that $$\begin{aligned}
\label{4.3g}
\tilde{I}_4^{\rm soft}(X,Y;t_X,t_Y) =
\int_0^\infty ds \, e^{st_Y} {\rm Ai}(Y + s)
{d \over ds} \Big ( e^{st_X} {\rm Ai}(X + s) 
\Big ) - (X \leftrightarrow Y )
\end{aligned}$$

### Asymptotics of $D(x, y; \tau_{x}, \tau_{y})$

Here we require the asymptotics of $R_{2m}(\cdot ; \tau)$ and $R_{2m+1}(\cdot ; \tau)$. The former is given by ([\[4.3c\]](#4.3c){reference-type="ref" reference="4.3c"}). For the latter, we note from ([\[4.3\]](#4.3){reference-type="ref" reference="4.3"}) that $$\begin{aligned}
\nonumber
{1 \over r_m(0)} R_{2m+1}(x;\tau) e^{\gamma_{2m+1} \tau} =
{H_{2m+1}(y) \over 2 \sqrt{\pi} \Gamma(2m+2) } e^{\gamma_{2m+2}
\tau}
\end{aligned}$$ and thus according to ([\[4.9\]](#4.9){reference-type="ref" reference="4.9"}) $$\begin{aligned}
\label{4.4a}
\lefteqn{
{\sqrt{w(x)} \over r_{N/2 - m}(0)} R_{N - 2m+1} (x;\tau)
e^{\gamma_{N - 2m + 1} \tau} \bigg |_{\begin{array}{l}
\scriptstyle
x = (2N)^{1/2} + X/2^{1/2} N^{1/6} \\ 
\scriptstyle \tau = t/N^{1/3} \end{array}} }
\\ && \sim {e^{N \tau_x} \over 2 \sqrt{\pi} }
{e^{-u t_X} \over (\Gamma ( N - 2m + 2))^{1/2}} \pi^{1/4}
2^{(N - 2m + 1)/2 + 1/4} N^{-1/12} {\rm Ai}(X + u).
\end{aligned}$$ Multiplying ([\[4.4a\]](#4.4a){reference-type="ref" reference="4.4a"}) and ([\[4.3c\]](#4.3c){reference-type="ref" reference="4.3c"}) according to ([\[2.q\]](#2.q){reference-type="ref" reference="2.q"}) we see that $$\label{4.4b}
D(X,Y;t_X,t_Y) = {1 \over 4} e^{N^{2/3}(t_X + t_Y)}
\int_0^\infty e^{-u t_Y} {\rm Ai}(Y + u) e^{X t_X}
\int_{X + u}^\infty e^{-st} {\rm Ai}(s) \, ds - (X \leftrightarrow Y).$$
