---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "arXiv:cond-mat/9811142v1 [cond-mat.mes-hall] 10 Nov 1998"
section_id: sec-004-311-the-thermodynamic-limit
section_title: "The thermodynamic limit"
section_number: 3.1.1
pages: 10-15
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.847
latex_coverage_ratio: 0.948
---
In the neighbourhood of the spectrum edge at the origin, we will show that after introducing the scaled coordinates and parameters $X$ and $t$ according to $$\begin{aligned}
x  = \frac{X}{4N} \, \quad \quad \tau = \frac{t}{2N} 
\label{3.9}
\end{aligned}$$ (the numerical factors $1/4$ and $1/2$ are chosen for convenience), the distribution functions have a well defined large $N$ limit. In particular, the scaled distribution function ([\[2.c\]](#2.c){reference-type="ref" reference="2.c"}), to be denoted $\rho_{(n+m)}^{\rm hard}$, is given by $$\begin{aligned}
\label{n.1}
\lefteqn{\rho_{(n+m)}^{\rm hard}(X_1^{(1)},\dots,X_n^{(1)};t^{(1)};
X_1^{(2)},\dots,X_m^{(2)};t^{(2)})} \nonumber \\ &&
= \lim_{N \to \infty} \Big ( {1 \over 4N} \Big )^{n+m}
\rho_{(n+m)}\Big ( {X_1^{(1)}\over 4N},\dots,{X_n^{(1)}\over 4N};
{t^{(1)} \over 4N};
{X_1^{(2)} \over 4N},\dots,{X_m^{(2)}\over 4N};{t^{(2)}\over 2N}\Big )
\end{aligned}$$ From the formula ([\[2.1b\]](#2.1b){reference-type="ref" reference="2.1b"}) for Tdet it follows that $\rho_{(n+m)}^{\rm hard}$ is given by the formula ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}) with the functions $S, \tilde{S}, \tilde{I}, D$ replaced by their scaled counterparts $$\begin{aligned}
S_1^{\rm hard}(X,Y;t_X,t_Y) & := & \lim_{N \to \infty} {1 \over 4N}
S \Big ({X \over 4N}, {Y \over 4N};{t_X \over 2N}, {t_Y \over 2N} \Big )
\label{n.2} \\
\tilde{S}_1^{\rm hard}(X,Y;t_X,t_Y) & := & \lim_{N \to \infty} {1 \over 4N}
\tilde{S} \Big ({X \over 4N}, {Y \over 4N};{t_X \over 2N}, {t_Y \over 2N} \Big )
\label{n.3} \\
\tilde{I}_1^{\rm hard}(X,Y;t_X,t_Y) & := & \lim_{N \to \infty}
\tilde{I} \Big ({X \over 4N}, {Y \over 4N};{t_X \over 2N}, {t_Y \over 2N} \Big )
\label{n.4} \\
D_1^{\rm hard}(X,Y;t_X,t_Y) & := & \lim_{N \to \infty} \Big (
{1 \over 4N} \Big )^2
D \Big ({X \over 4N}, {Y \over 4N};{t_X \over 2N}, {t_Y \over 2N} \Big )
\label{n.5}
\end{aligned}$$ where the subscripts 1 indicate $\beta = 1$ initial conditions.

Note that it was permissable to multiply ${1 \over 4N} \tilde{I}$ by $4N$ and divide ${1 \over 4N} D$ by $4N$ in the above definitions because of an invariance property of the Tdet formula ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}). Thus in general each $2 \times 2$ block $Q_{jk}$ can be replaced by the $2 \times 2$ block $$A^{-1} Q_{jk} A. \label{n.6'}$$ Choosing $$A = \left ( \begin{array}{cc} 1/\sqrt{4N} & 0 \\ 0 & \sqrt{4N} \end{array}
\right )$$ then transforms ${1 \over 4N} \tilde{I}$ and ${1 \over 4N} D$ as required.

### Asymptotics of $S(x, y; \tau_{x}, \tau_{y})$

Let us first compute the asymptotic behaviour of $\Phi_{2k-2}(x; \tau)$. This is required in the computation of $S_{2}$ (with $2k = N$), and also $\tilde{I}$. From the expansion ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}) and the explicit formulas ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}) and ([\[3.5\]](#3.5){reference-type="ref" reference="3.5"}) for the quantities $C_{\nu}(x)$, $h_{\nu}$ and $\beta_{\nu 2k-2}$ therein we have $$\begin{aligned}
\label{3.10}
\lefteqn{
\Phi_{2k - 2}(x;\tau) e^{\gamma_{2k-2} \tau} = \sqrt{w(x)}
r_{k-1}(0) \bigg ( - {L_{2k-1}^a (x) \over (2k - 1 + a)!} e^{-\gamma_{2k-1}
\tau}} \nonumber \\ &&
+ {(k + a/2)! (2k)! \over (2k - 1)! (2k + a)! k!}
\sum_{\nu = k}^\infty {\nu! \over (\nu + a/2)!}
\Big ( L_{2 \nu}^a(x) e^{-\gamma_{2 \nu} \tau} -
L_{2 \nu + 1}^a (x) e^{- \gamma_{2 \nu + 1} \tau} \Big ) \bigg ).
\end{aligned}$$ We now proceed to estimate the summand for large $\nu$.

From Stirling's formula $$\begin{aligned}
\frac{\nu !}{(\nu + a/2)!} \mathop{\sim}\limits_{\nu \to \infty}
\frac{1}{\nu^{a/2}} \,  .
\nonumber
\end{aligned}$$ For the second factor in the summand we write $$\begin{aligned}
\lefteqn{
L^{a}_{2\nu}(x) e^{-\gamma_{2\nu}\tau}  - 
L^{a}_{2\nu + 1}(x) e^{-\gamma_{2\nu + 1}\tau}} \nonumber \\
&& =  
 - e^{-\gamma_{2\nu + 1}\tau} \left( 
L^{a}_{2\nu + 1}(x) - L^{a}_{2\nu}(x) - L^{a}_{2\nu}(x)
(e^{-\tau(\gamma_{2\nu} - \gamma_{2\nu + 1})} - 1) \right) \,  .
\end{aligned}$$ Using the facts that $$\begin{aligned}
e^{\tau(\gamma_{2\nu} - \gamma_{2\nu + 1})} = e^{-2\tau}\, ,   \quad  \quad  
L^{a}_{2\nu + 1}(x) - L^{a}_{2\nu}(x) = L^{a-1}_{2\nu + 1}(x) \,  ,
\label{3.11}
\end{aligned}$$ and the asymptotic formula $$\begin{aligned}
\sqrt{w(x)}\,  L_{n}^{a}(x) 
\mathop{\sim}\limits_{n \to \infty}  n^{a/2} 
J_{a}\left(2\sqrt{nx}\right) 
\label{3.12}
\end{aligned}$$ where $J_{a}(z)$ denotes the Bessel function, we see that $$\begin{aligned}
\lefteqn{\left. \sqrt{w(x)}\, \frac{\nu !}{(\nu + a/2)!} 
 \left(L_{2\nu}^{a}(x) e^{-\gamma_{2\nu}\tau}  - 
L^{a}_{2\nu + 1}(x) e^{-\gamma_{2\nu + 1} \tau} \right)
\right|_{x = X/4N \atop \tau = t/2N}} \nonumber \\
 & \sim  &  -\nu^{-a/2} e^{-(2\nu /N)t} 
\bigg( \sqrt{\frac{X}{4N}}(2\nu)^{(a-1)/2} 
J_{a-1}\Big(\sqrt{\frac{2jX}{N}}\Big) + \frac{t}{N} (2\nu)^{a/2} 
J_{a}\Big(\sqrt{\frac{2jX}{N}}\Big)\bigg) 
\nonumber \\
& =  & -\frac{2^{a/2}}{N}u^{-a/2}\frac{d}{du}
\left(e^{-ut} u^{a/2} J_{a}\left(\sqrt{uX}\right) \right), \quad \quad 
u := 2\nu /N \,  .
\label{3.13}
\end{aligned}$$ (The equality is obtained by making use of a suitable differentiation formula for the Bessel function).

Substituting ([\[3.13\]](#3.13){reference-type="ref" reference="3.13"}) in ([\[3.10\]](#3.10){reference-type="ref" reference="3.10"}) gives the leading order behaviour of the sum over $\nu$ as a Riemann integral. Furthermore, use of ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) gives $$\begin{aligned}
\left. \sqrt{w(x)} \, \frac{L^{a}_{2k - 1}(x)}{(2k - 1 + a)!}\,
 e^{-\gamma_{2k-1}\tau}\right|_{x = X/4N \atop \tau = t/2N}
\sim  
\frac{N^{-a/2}}{(2k - 1)!} \, s^{-a/2} J_{a}\left(\sqrt{sX}\right)\, e^{-st},
\label{3.14} 
\end{aligned}$$ $s := 2k/N$, so in total we have $$\begin{aligned}
\Phi_{2k-2}\left(\frac{X}{4N}; \frac{t}{2N}\right) e^{\gamma_{2k-2}t/2N} & \sim &
r_{k-1}(0) \frac{N^{-a/2}}{(2k - 1)!} 
\bigg ( \frac{1}{2}\left( 1 - 2s^{-a/2}\right) J_{a}\left(\sqrt{sX}\right) 
e^{-st}  \nonumber \\
&  &   -  
\frac{a}{4} \int_{s}^{\infty} \frac{e^{-ut}}{u} J_{a}\left(\sqrt{uX}\right) 
du \bigg )  \,  .
\label{3.15}
\end{aligned}$$ The expansions ([\[3.14\]](#3.14){reference-type="ref" reference="3.14"}) and ([\[3.15\]](#3.15){reference-type="ref" reference="3.15"}) with $2k = N$ and thus $s = 1$ suffice to specify the $x$-dependent factor in ([\[3.8\]](#3.8){reference-type="ref" reference="3.8"}). Thus we have $$\begin{aligned}
\lefteqn{\left. 
\left(\frac{\Phi_{N-2}(x; \tau_{x})}{r_{N/2 - 1}(0)}  -  \sqrt{w(x)}\, 
\frac{C_{N-1}(x)e^{-\gamma_{N-1} \tau_{x}}}{h_{N-1}}\right) 
\right|_{x = X/4N \atop \tau_{x} = t_{X}/2N}}
\nonumber \\ 
& & \sim  \frac{N^{-a/2}}{2(N-1)!} \left( 
J_{a}\left(\sqrt{X}\right) e^{-t_{X}} - \frac{a}{2} \int_{1}^{\infty} 
\frac{e^{-ut_{X}}}{u} J_{a} \left( \sqrt{uX}\right) \, du \right)  \,  . 
\label{3.16}
\end{aligned}$$

Next we will compute the asymptotic form of $R_{2j}(y; \tau_{y})$. In the case $2j = N - 2$ this is required for the $y$-dependent factor in ([\[3.8\]](#3.8){reference-type="ref" reference="3.8"}). From ([\[2.i\]](#2.i){reference-type="ref" reference="2.i"}), ([\[3.2\]](#3.2){reference-type="ref" reference="3.2"}) and ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}) we see that $$\begin{aligned}
R_{2j}(y; \tau )\, e^{\gamma_{2j} \tau} = (2j)! \sum_{l=0}^{2j}L_{l}^{a}(y)\, 
e^{\gamma_{l}\tau} \,  . 
\label{3.16'}
\end{aligned}$$ The asymptotic form of this expression is deduced by using ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) to approximate the summand, which leads to the result $$\begin{aligned}
\left. \sqrt{w(y)} R_{2j}(y; \tau_{y}) e^{\gamma_{2j} \tau_{y}}
\right|_{y = Y/4N \atop \tau_{y} = t_{Y}/2N}
\sim (2j)! \, 
N^{1+a/2} \int_{0}^{s}v^{a/2}J_{a}\left(\sqrt{vY}\right)\, e^{vt_{Y}}\, dv 
\,  , 
\label{3.17}
\end{aligned}$$ where here $s = 2j/N$. Setting $s = 1$ and making further use of ([\[3.14\]](#3.14){reference-type="ref" reference="3.14"}) we see that $$\begin{aligned}
\lefteqn{\sqrt{w(y)} \left(C_{N-1}(y)e^{\gamma_{N-1}\tau_{y}} - 
(N-1) R_{N-2}(y; \tau_{y}) e^{\gamma_{N-2} \tau_{y}}\right)}
\nonumber \\ & & \hspace*{2cm} \sim  -(N-1)! N^{1+a/2} 
\int_{0}^{1}v^{a/2}J_{a}\left(\sqrt{vY}\right)\, e^{vt_{Y}}\, dv \,   .
\label{3.18}
\end{aligned}$$ Combining ([\[3.16\]](#3.16){reference-type="ref" reference="3.16"}) and ([\[3.18\]](#3.18){reference-type="ref" reference="3.18"}) in the formula ([\[3.8\]](#3.8){reference-type="ref" reference="3.8"}) for $S_{2}$ gives $$\begin{aligned}
S_{2}\left(\frac{X}{4N}, \frac{Y}{4N}; \frac{t_{X}}{2N}, \frac{t_{Y}}{2N} 
\right) 
& \sim  & 
\frac{N}{2}\left( - e^{-t_{X}} J_{a}\left(\sqrt{X}\right) + \frac{a}{2} 
\int_{1}^{\infty} \frac{e^{-ut_{X}}}{u}J_{a}\left(\sqrt{uX}\right)\, du\right) 
\nonumber \\  &  &  \times 
\left( \int_{0}^{1}v^{a/2}J_{a}\left(\sqrt{vY}\right)\, e^{vt_{Y}}\, 
dv \right)\,  .
\label{3.19}
\end{aligned}$$

The asymptotics of $S_{1}$ can be determined by using ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) and Stirling's formula to approximate the integrand. This gives $$\begin{aligned}
S_{1}\left(\frac{X}{4N}, \frac{Y}{4N}; \frac{t_{X}}{2N}, \frac{t_{Y}}{2N} 
\right) 
\sim  N \int_{0}^{1} J_{a}\left(\sqrt{uX}\right)\,J_{a}\left(\sqrt{uY}\right)\, 
e^{-u(t_{X} - t_{Y})}\, du \,  . 
\label{3.20}
\end{aligned}$$ Since $S$ is defined as the sum of $S_{1}$ and $S_{2}$, its asymptotic form is given by the sum of ([\[3.19\]](#3.19){reference-type="ref" reference="3.19"}) and ([\[3.20\]](#3.20){reference-type="ref" reference="3.20"}). Substituting into ([\[n.2\]](#n.2){reference-type="ref" reference="n.2"}) gives $$\begin{aligned}
\label{3.20'} \lefteqn{
S_1^{\rm hard}(X,Y;t_X,t_Y) = {1 \over 4} \int_0^1 J_a(\sqrt{uX})
J_a(\sqrt{uY}) e^{-u(t_X - t_Y)} \, du} \nonumber \\ &&
+ {1 \over 8} \Big ( - e^{-t_X} J_a(\sqrt{X}) + {a \over 2}
\int_1^\infty {e^{-u t_X} \over u} J_a(\sqrt{uX}) \, du \Big )
\int_0^1 dv \, J_a(\sqrt{vY}) e^{t_Y v} v^{a/2}.
\end{aligned}$$

### Asymptotics of $\tilde{I} (x, y; \tau_{x}, \tau_{y})$

So as to induce a cancellation at leading order, we first perform some minor manipulation to the definition ([\[2.p\]](#2.p){reference-type="ref" reference="2.p"}), by way of subtracting and adding $(2l + 1) e^{\gamma_{2l} (\tau_{x} + \tau_{y})} \Phi_{2l}(x; \tau_{x}) 
\Phi_{2l}(y; \tau_{y})$ to the summand, so that it reads $$\begin{aligned}
\tilde{I} (x, y; \tau_{x}, \tau_{y}) & = & \sum_{l = N/2}^{\infty} 
\frac{1}{r_{l}(0)} \left\{ e^{\gamma_{2l}\tau_{x}} \Phi_{2l}(x; \tau_{x})
\left( e^{\gamma_{2l+1}\tau_{y}} \Phi_{2l+1}(y; \tau_{y}) \right. \right. 
\nonumber \\
&  &  \left. \left. - (2l + 1) e^{\gamma_{2l}\tau_{y}} \Phi_{2l}(y; \tau_{y}) \right) - 
(x \leftrightarrow y) \right\} \,  . 
\label{3.21}
\end{aligned}$$ The asymptotics of $e^{\gamma_{2l} \tau_{x}} \Phi_{2l}(x; \tau_{x})$ can be read off from ([\[3.15\]](#3.15){reference-type="ref" reference="3.15"}). For the $y$-dependent factor of the first term of the summand we note from the definitions ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}) and the explicit formulas ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}) and ([\[3.5\]](#3.5){reference-type="ref" reference="3.5"}) that $$\begin{aligned}
\lefteqn{e^{\gamma_{2l+1}\tau} \Phi_{2l+1}(y; \tau) 
- (2l + 1) e^{\gamma_{2l}\tau} \Phi_{2l}(y; \tau)} \nonumber \\ 
& & = \sqrt{w(y)}\,  r_{l}(0) \left( (2l+1)
\frac{L_{2l+1}^{a}(y)e^{-\gamma_{2l+1}\tau}}{(2l+1+a)!} - 
\frac{L_{2l}^{a}(y)e^{-\gamma_{2l}\tau}}{(2l+a)!}\right) \,  . 
\nonumber
\end{aligned}$$ Thus, using ([\[3.3\]](#3.3){reference-type="ref" reference="3.3"}) and the asymptotic formula ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) we have $$\begin{aligned}
 \lefteqn{\Big( e^{\gamma_{2l+1}\tau} \Phi_{2l+1}(y; \tau) 
- (2l + 1) e^{\gamma_{2l}\tau} \Phi_{2l}(y; \tau) \Big)
\bigg|_{y = Y/4N \atop \tau = t/2N}} \nonumber \\
&  &  \sim 4(2l+1)! N^{-1 + a/2} \left\{ 
\frac{d}{ds}\left(e^{-st}J_{a}\left(\sqrt{sY}\right)\right) - 
as^{-1+a/2}J_{a}\left(\sqrt{sY}\right)e^{-st}\right\}\,  , \quad  s = 2l/N \,  . 
\nonumber
\end{aligned}$$ Substituting this result, together with ([\[3.15\]](#3.15){reference-type="ref" reference="3.15"}) (after replacing $k$ by $l + 1$) in ([\[3.21\]](#3.21){reference-type="ref" reference="3.21"}) shows that $$\begin{aligned}
\tilde{I}_1^{\rm hard}(X,Y;t_X,t_Y) =
 \int_{1}^{\infty}  ds \left\{ \left(1- \frac{2}{s^{a/2}}\right)
J_{a}\left(\sqrt{sX}\right) e^{-st_{X}} - \frac{a}{4}\int_{s}^{\infty} 
\frac{e^{-ut_{X}}}{u} J_{a}\left(\sqrt{uX}\right)\,du \right\} 
\nonumber \\   \times
\left\{ \frac{d}{ds}\left(e^{-st_{y}}J_{a}\left(\sqrt{sY}\right)\right) - 
as^{-1+a/2}J_{a}\left(\sqrt{sY}\right)
e^{-st_{Y}}\right\} - (X \leftrightarrow Y) \, .
\label{3.22}
\end{aligned}$$

### Asymptotics of $g(x, y; \tau)$

According to ([\[2.3\]](#2.3){reference-type="ref" reference="2.3"}) and ([\[2.5\]](#2.5){reference-type="ref" reference="2.5"}) $$\begin{aligned}
g(x, y; \tau) = (xy)^{a/2}e^{-(x+y)/2} \sum_{j=0}^{\infty} \frac{j!}{(j+a)!} 
L_{j}^{a}(x)L_{j}^{a}(y) e^{-2(j+(a+1)/2)\tau} \, . 
\label{3.22a}
\end{aligned}$$ This summation can be evaluated in closed form [@Er], giving $$\begin{aligned}
g(x, y; \tau) = e^{-(x+y)/2}e^{-(2a+1)\tau}\left(1 - e^{-2\tau}\right)^{-1} 
\exp \left( -\frac{e^{-2\tau}}{1 - e^{-2\tau}}(x+y) \right) 
I_{a}\left(2\frac{\sqrt{xy}\, e^{-\tau}}{1 - e^{-2\tau}}\right)\, ,
\nonumber
\end{aligned}$$ where $I_a$ denotes the Bessel function of pure imaginary argument. Consequently $$\begin{aligned}
g\left( \frac{X}{4N}, \frac{Y}{4N}; \frac{t_{X} - t_{Y}}{2N}\right) \sim 
\frac{N}{t_{X}-t_{Y}} 
\exp \left( -\frac{X+Y}{t_{X} - t_{Y}} \right) 
I_{a}\left(\frac{\sqrt{XY}}{2(t_{X} - t_{Y})}\right) \,  .
\label{3.22'}
\end{aligned}$$

Alternatively, proceeding as in the derivation of ([\[3.20\]](#3.20){reference-type="ref" reference="3.20"}) we can deduce from ([\[3.22a\]](#3.22a){reference-type="ref" reference="3.22a"}) that $$\label{m.1}
g\Big ({X \over 4N}, {Y \over 4N}; {t_X - t_Y \over 2N} \Big ) \sim
N \int_0^\infty J_a(\sqrt{uX})  J_a(\sqrt{uY}) e^{-u (t_X - t_Y)} \, du.$$ The immediate merit of this representation is that when substituted in ([\[2.r\]](#2.r){reference-type="ref" reference="2.r"}), partial cancellation occurs with ([\[3.20\]](#3.20){reference-type="ref" reference="3.20"}). Adding the result to ([\[3.19\]](#3.19){reference-type="ref" reference="3.19"}) and substituting in ([\[n.3\]](#n.3){reference-type="ref" reference="n.3"}) gives $$\begin{aligned}
\label{m.2} \lefteqn{
\tilde{S}_1^{\rm hard}(X,Y;t_X,t_Y) = - {1 \over 4} \int_1^\infty J_a(\sqrt{uX})
J_a(\sqrt{uY}) e^{-u(t_X - t_Y)} \, du} \nonumber \\ &&
+ {1 \over 8} \Big ( - e^{-t_X} J_a(\sqrt{X}) + {a \over 2}
\int_1^\infty {e^{-u t_X} \over u} J_a(\sqrt{uX}) \, du \Big )
+ \int_0^1 dv \, J_a(\sqrt{vY}) e^{t_Y v} v^{a/2}.
\end{aligned}$$

### Asymptotics of $D(x, y; \tau_{x}, \tau_{y})$

According to ([\[2.q\]](#2.q){reference-type="ref" reference="2.q"}) $D$ is defined in terms of $\{R_{j}(x; \tau)\}$. Now $R_{2j}(y; \tau)$ is specified by ([\[3.16\'\]](#3.16'){reference-type="ref" reference="3.16'"}). Deriving the analogous formula for $R_{2j+1}(x; \tau)$, which follows from ([\[3.2\]](#3.2){reference-type="ref" reference="3.2"}), ([\[2.i\]](#2.i){reference-type="ref" reference="2.i"}) and ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}), we see that $$\begin{aligned}
R_{2j+1}(x; \tau) e^{\gamma_{2j+1}\tau}
& =  &  -(2j+1)! L_{2j+1}^{a}(x) e^{\gamma_{2j+1}\tau} - 
(2j)! (2j+a + 1) L_{2j}^{a}(x) e^{\gamma_{2j}\tau} \nonumber \\  & & 
\quad \quad + (2j+a + 1) R_{2j}(x; \tau) e^{\gamma_{2j}\tau} \,  .
\nonumber
\end{aligned}$$ Hence $$\begin{aligned}
\lefteqn{\left( e^{\gamma_{2j+1}\tau_{x}} R_{2j+1}(x; \tau_{x}) 
e^{\gamma_{2j}\tau_{y}} R_{2j}(y; \tau_{y}) - (x \leftrightarrow y) \right) =} 
\nonumber \\ 
& & \left(-(2j+1)!  L_{2j+1}^{a}(x) e^{\gamma_{2j+1}\tau_{x}} - 
(2j)! (2j+a + 1) L_{2j}^{a}(x) e^{\gamma_{2j}\tau_{x}}\right) 
R_{2j}(y; \tau_{y}) e^{\gamma_{2j}\tau_{y}}  - (x \leftrightarrow y)  \,  .
\nonumber
\end{aligned}$$ Now the asymptotic form of $R_{2j}(y; \tau_{y})$ is specified by ([\[3.17\]](#3.17){reference-type="ref" reference="3.17"}) while we see from ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) that $$\begin{aligned}
\lefteqn{\sqrt{w(x)} \left(-(2j+1)!  
L_{2j+1}^{a}(x) e^{\gamma_{2j+1}\tau_{x}} - 
(2j)! (2j+a + 1) L_{2j}^{a}(x) e^{\gamma_{2j}\tau_{x}}\right)  
\bigg|_{x = X/4N \atop \tau_{x} = t_{X}/2N}} \nonumber \\ & & \quad \quad \quad 
\sim -2 (2j+1)! e^{st_{X}} (Ns)^{a/2} J_{a}\left( \sqrt{sX}\right) \, , \quad s = 2j/N \,  .
\nonumber
\end{aligned}$$ Making use also of the explicit form ([\[3.3\]](#3.3){reference-type="ref" reference="3.3"}) of $r_{n}(0)$ and using the definition ([\[n.5\]](#n.5){reference-type="ref" reference="n.5"}) we thus find $$\begin{aligned}
\lefteqn{
D_1^{\rm hard}(X,Y;t_X,t_Y) = - 4^{-3}  } \nonumber \\ && \times
\left\{ \int_{0}^{1}ds\, e^{st_{X}} s^{-a/2}  
J_{a}\left( \sqrt{sX}\right)  
\int_{0}^{s}dv \, e^{vt_{Y}}v^{a/2}J_{a}\left( \sqrt{vY}\right) 
- (X \leftrightarrow Y) \right\} \,  .
\label{3.23}
\end{aligned}$$

## $\beta = 4$ initial conditions

The method of evaluation of the quantities $S, \, \tilde{I}$, and $D$ for the Laguerre ensemble in the case of initial conditions with symplectic symmetry ($\beta = 4$) closely parallels that just given for $\beta = 1$ initial conditions. First, we note from previous work [@NW91] that the monic skew orthogonal polynomials at $\tau = 0$ have the explicit form $$\begin{aligned}
R_{2j}(x) &=& 2^{2j}j!\left(j + (a-1)/2\right)! \sum_{l=0}^{j} 
\frac{(2l)!}{l! \, 2^{2l}} \frac{1}{\left(l + (a-1)/2\right)!} L_{2l}^{a-1}(x) 
\nonumber \\
& = &  2^{2j}j!\left(j + (a-1)/2\right)! \sum_{l=0}^{j} 
\frac{1}{l! \, 2^{2l} \left(l + (a-1)/2\right)!} \left(C_{2l}(x) + 2lC_{2l-1}(x) \right) \,  , 
\nonumber \\
R_{2j+1}(x) &=& -(2j+1)! \,   L_{2j+1}^{a-1}(x) 
\nonumber \\
& = &  C_{2j+1}(x) + (2j+1)C_{2j}(x)  \,   , 
\label{3.24}
\end{aligned}$$ with corresponding normalization $$\begin{aligned}
r_{n}(0) = \Gamma(2n+2)\, \Gamma(a + 2n + 1) \,   . 
\label{3.25}
\end{aligned}$$

The inversion of these equations gives that the quantities $\beta_{n\, j}$ in ([\[2.l\]](#2.l){reference-type="ref" reference="2.l"}) have the explicit values $$\begin{aligned}
\beta_{2m\, 2m} &=& \beta_{2m+1\, 2m+1} = 1 \, , \quad \quad  
\beta_{2m+1\, 2m} = - (2m+1) \,   ,   \nonumber \\ 
\beta_{\nu\, 2j+1} &=& (-1)^{\nu + 1} \frac{\nu !}{(2j+1)!} \,  ,  \quad \quad 
\beta_{\nu\, 2j} = a \,  \beta_{\nu\, 2j+1} \,   , 
\label{3.26}
\end{aligned}$$ for $\nu > 2j + 1$. Thus the factorization formula ([\[3.6\]](#3.6){reference-type="ref" reference="3.6"}) again holds, which when substituted in ([\[2.1e\]](#2.1e){reference-type="ref" reference="2.1e"}) and after making use of the explicit value of $\beta_{N-1\, N-2}$ and $\beta_{p\, N-1}$, and ([\[2.l\]](#2.l){reference-type="ref" reference="2.l"}), implies $$\begin{aligned}
S_{2}(x, y; \tau_{x}, \tau_{y}) & = & \sqrt{w(x)w(y)} \sum_{p = N}^{\infty} 
\frac{C_{p}(x)}{h_{p}}\, e^{-\gamma_{p}\tau_{x}}\, \beta_{p\, N-1} 
\left\{ C_{N-1}(y) e^{\gamma_{N-1}\tau_{y}} \right. \nonumber \\
& & \quad \left. + (a + N-1) R_{N-2}(y; \tau_{y}) 
e^{\gamma_{N-2}\tau_{y}} \right\} \,  . 
\nonumber
\end{aligned}$$ The sum over $p$ is, after minor manipulation, formally identical to the sum over $p$ in ([\[3.7\]](#3.7){reference-type="ref" reference="3.7"}), so it can be summed using ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}). Thus $S_{2}$ has the explicit form $$\begin{aligned}
S_{2}(x, y; \tau_{x}, \tau_{y}) & = & \sqrt{w(y)} \left( 
\frac{\Phi_{N-2}(x; \tau_{x})}{r_{N/2 -1}(0)} e^{\gamma_{N-2}\tau_{x}} - 
\sqrt{w(x)} \frac{C_{N-1}(x)}{h_{N-1}} e^{-\gamma_{N-1}\tau_{x}} \right) 
\nonumber \\
& & \times 
\left(C_{N-1}(y) e^{\gamma_{N-1}\tau_{y}} + (a + N-1) R_{N-2}(y; \tau_{y}) 
e^{\gamma_{N-2}\tau_{y}} \right) \,  . 
\label{3.27}
\end{aligned}$$ As with ([\[3.8\]](#3.8){reference-type="ref" reference="3.8"}), in the limit $\tau_{x}, \tau_{y} \rightarrow 0$ this reduces down to the form of $S_{2}$ derived by Widom [@Wi98] in the static $\beta = 4$ theory. The details of the verification are given in Appendix A.

### The thermodynamic limit

Although the scaled distribution function is still given by ([\[n.1\]](#n.1){reference-type="ref" reference="n.1"}), the required scaling of the elements of the quaternion determinant ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}) differs slightly from the formulas ([\[n.2\]](#n.2){reference-type="ref" reference="n.2"})--([\[n.5\]](#n.5){reference-type="ref" reference="n.5"}) appropriate with $\beta = 1$ initial conditions. In particular ([\[n.4\]](#n.4){reference-type="ref" reference="n.4"}) and ([\[n.5\]](#n.5){reference-type="ref" reference="n.5"}) should now read $$\begin{aligned}
\tilde{I}_4^{\rm hard}(X,Y;t_X,t_Y) & := & \lim_{N \to \infty}
\Big ( {1 \over 4N} \Big )^2
\tilde{I} \Big ({X \over 4N}, {Y \over 4N};{t_X \over 2N}, {t_Y \over 2N} \Big )
\label{n.6} \\
D_4^{\rm hard}(X,Y;t_X,t_Y) & := & \lim_{N \to \infty} 
D \Big ({X \over 4N}, {Y \over 4N};{t_X \over 2N}, {t_Y \over 2N} \Big )
\label{n.7}
\end{aligned}$$ while ([\[n.2\]](#n.2){reference-type="ref" reference="n.2"}) and ([\[n.3\]](#n.3){reference-type="ref" reference="n.3"}) remain the same, except that the subscripts 1 on the right hand sides should be replaced by 4.

### Asymptotics of $S(x, y; \tau_{x}, \tau_{y})$

From the expansion ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}) and the explicit formulas ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}) and ([\[3.26\]](#3.26){reference-type="ref" reference="3.26"}) we have $$\begin{aligned}
\Phi_{2k-2}(x; \tau)e^{\gamma_{2k-2}\tau} 
= -\frac{r_{k-1}(0) \sqrt{w(x)}}{(2k-1)!} 
\sum_{\nu = 2k-1}^{\infty} \frac{L_{\nu}^{a}(x)\, \nu !}{(\nu + a)!} 
\, e^{-\gamma_{\nu}\tau}\, . 
\nonumber
\end{aligned}$$ Applying the asymptotic expansion ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) and Stirling's formula shows that $$\begin{aligned}
\Phi_{2k-2}\left(\frac{X}{4N}; \frac{t}{2N}\right)
e^{\gamma_{2k-2} t/2N}  \sim -\frac{r_{k-1}(0)}{(2k-1)!} N^{1 - a/2} 
\int_{u}^{\infty} dr \, r^{-a/2} e^{-rt} J_{a}\left(\sqrt{rX}\right)  \, , 
\label{3.28}
\end{aligned}$$ where $u := 2k/N$. Setting $u = 1$ gives the asymptotic form of $\Phi_{N-2}(x; \tau_{x})/r_{N/2 -1}(0)$ as required in ([\[3.27\]](#3.27){reference-type="ref" reference="3.27"}), and comparison with ([\[3.14\]](#3.14){reference-type="ref" reference="3.14"}) shows that this term dominates the one involving $C_{N-1}(x)$. Thus here the formula ([\[3.16\]](#3.16){reference-type="ref" reference="3.16"}) applies with the right hand side replaced by $$\begin{aligned}
- \frac{N^{1 - a/2}}{(N-1)!}  
\int_{u}^{\infty} dr \, r^{-a/2} e^{-rt} J_{a}\left(\sqrt{rX}\right) \,   .
\label{3.29}
\end{aligned}$$ For the $y$-dependent factor in ([\[3.27\]](#3.27){reference-type="ref" reference="3.27"}), we note from ([\[2.i\]](#2.i){reference-type="ref" reference="2.i"}), ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}), and ([\[3.16\'\]](#3.16'){reference-type="ref" reference="3.16'"}) that $$\begin{aligned}
\lefteqn{R_{2j}(y; \tau)  e^{\gamma_{2j}\tau} 
=} \nonumber \\
& &  2^{2j}j!  \left( j + (a-1)/2\right)! \sum_{l=0}^{j} 
\frac{(2l)!}{l!\, 2^{2l}} \frac{1}{(l + (a-1)/2)!} 
\left( L_{2l}^{a}(y) e^{\gamma_{2l}\tau} - L_{2l-1}^{a}(y) e^{\gamma_{2l-1}\tau}\right)  .
\nonumber 
\end{aligned}$$ Use of ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) and Stirling's formula gives for the corresponding asymptotic form $$\begin{aligned}
\lefteqn{\left. \frac{1}{(2j+1)!}\sqrt{w(y)} R_{2j}(y; \tau) e^{\gamma_{2j}\tau}
\right|_{y = Y/4N \atop \tau = t/2N}} \nonumber \\
& \sim & \frac{N^{a/2-1}}{2} s^{-1 + a/2} \int_{0}^{s} 
u^{-a/2} \frac{d}{du} \left( e^{ut} u^{a/2} J_{a}\left(\sqrt{uY}\right) \right) du \, , 
\quad s := 2j/N\,  . 
\label{3.30}
\end{aligned}$$ Adding this with $s = 1$ to the asymptotic form of $\sqrt{w(y)} 
C_{N-1}(y) e^{\gamma_{N-1} \tau_{y}}/(N-1)!$ deduced from ([\[3.14\]](#3.14){reference-type="ref" reference="3.14"}), and multiplying the result by ([\[3.29\]](#3.29){reference-type="ref" reference="3.29"}) gives that $$\begin{aligned}
\lefteqn{S_{2}\left(\frac{X}{4N}, 
\frac{Y}{4N}; \frac{t_{X}}{2N}, \frac{t_{Y}}{2N} \right) 
\sim  -N\int_{1}^{\infty} dr \, r^{-a/2} e^{-rt_{X}}J_{a}\left(\sqrt{rX}\right)}
\nonumber \\ &  & \times
\left( - J_{a}\left(\sqrt{Y}\right) e^{t_{Y}} + 
\frac{1}{2} \int_{0}^{1}u^{-a/2} \frac{d}{du}\left( e^{u t_{Y}} u^{a/2} 
J_{a}\left(\sqrt{uY}\right)\right) \,du \right)\,  .
\label{3.31}
\end{aligned}$$

The asymptotic form of $S_{1}$ can be read off from ([\[3.20\]](#3.20){reference-type="ref" reference="3.20"}) since according to its definition ([\[2.1d\]](#2.1d){reference-type="ref" reference="2.1d"}), its value is the same for $\beta = 1$ and 4. The asymptotic form of $S$ itself is thus given by the sum of ([\[3.20\]](#3.20){reference-type="ref" reference="3.20"}) and ([\[3.31\]](#3.31){reference-type="ref" reference="3.31"}). Thus we have $$\begin{aligned}
\lefteqn{
S_4^{\rm hard}(X,Y;t_X,t_Y) = } \nonumber \\ &  & {1 \over 4} \int_0^1
J_a(\sqrt{uX}) J_a(\sqrt{uY}) e^{-u(t_X - t_Y)} \, du
- {1 \over 4} \int_1^\infty dr \, r^{-a/2} e^{-r t_X}
J_a(\sqrt{rX}) \nonumber \\ &&
\times \bigg ( - J_a(\sqrt{Y}) e^{t_Y} + {1 \over 2}
\int_0^1 u^{-a/2} {d \over du} \Big ( e^{ut_Y} u^{a/2}
J_a(\sqrt{uY}) \Big ) du \bigg ) \label{m.3}
\end{aligned}$$

### Asymptotics of $\tilde{S}(x, y; \tau_{x}, \tau_{y})$

The single particle Green function $g$ as specified by ([\[2.3\]](#2.3){reference-type="ref" reference="2.3"}) is independent of the initial condition, so me can use the formula ([\[m.1\]](#m.1){reference-type="ref" reference="m.1"}). Dividing by $4N$ and subtracting from ([\[m.3\]](#m.3){reference-type="ref" reference="m.3"}) shows $$\begin{aligned}
\lefteqn{
\tilde{S}_4^{\rm hard}(X,Y;t_X,t_Y)} 
\nonumber \\ && =  - {1 \over 4} \int_1^\infty
J_a(\sqrt{uX}) J_a(\sqrt{uY}) e^{-u(t_X - t_Y)} \, du
- {1 \over 4} \int_1^\infty dr \, r^{-a/2} e^{-r t_X}
J_a(\sqrt{rX}) \nonumber \\ &&
\times \bigg ( - J_a(\sqrt{Y}) e^{t_Y} + {1 \over 2}
\int_0^1 u^{-a/2} {d \over du} \Big ( e^{ut_Y} u^{a/2}
J_a(\sqrt{uY}) \Big ) du \bigg ) \label{m.4}
\end{aligned}$$

### Asymptotics of $\tilde{I}(x, y; \tau_{x}, \tau_{y})$

The definition ([\[2.p\]](#2.p){reference-type="ref" reference="2.p"}) gives that $\tilde{I}$ is defined in terms of $\{\Phi_{l}(x; \tau)\}$. The asymptotic form of $\Phi_{2k-2}(x; \tau)$ is given by ([\[3.28\]](#3.28){reference-type="ref" reference="3.28"}). Instead of deriving an analogous expression for $\Phi_{2k-1}(y; \tau)$, we note from ([\[2.m\]](#2.m){reference-type="ref" reference="2.m"}), ([\[3.26\]](#3.26){reference-type="ref" reference="3.26"}), ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}) and the formula ([\[3.28\]](#3.28){reference-type="ref" reference="3.28"}) for $\Phi_{2k-2}$ that $$\begin{aligned}
\lefteqn{\Phi_{2k-1}(y; \tau)e^{\gamma_{2k-1}\tau} =} \nonumber \\ 
& - & \frac{\sqrt{w(y)}\, r_{k-1}(0)}{(2k-2 + a)!} 
\left( L_{2k-2}^{a}(y) 
e^{-\gamma_{2k-2}\tau} + L_{2k-1}^{a}(y) e^{-\gamma_{2k-1}\tau}
\right) - a \Phi_{2k-2}(y; \tau) \,  . 
\label{3.32}
\end{aligned}$$ Thus $$\begin{aligned}
\lefteqn{e^{\gamma_{2l}\tau_{x}}\Phi_{2l}(x; \tau_{x})
e^{\gamma_{2l+1}\tau_{y}}\Phi_{2l+1}(y; \tau_{y}) - (x \leftrightarrow y) 
=}  \nonumber \\ 
&  &  e^{\gamma_{2l}\tau_{x}}\Phi_{2l}(x; \tau_{x})
\left(-\frac{\sqrt{w(y)}\, r_{l}(0)}{(2l + a)!} \right)
\left( L_{2l}^{a}(y) 
e^{-\gamma_{2l}\tau_{y}} + L_{2l+1}^{a}(y) e^{-\gamma_{2l+1}\tau_{y}}
\right) - ( x \leftrightarrow y)   .  \nonumber \\
\label{3.33}
\end{aligned}$$ According to ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) and ([\[3.25\]](#3.25){reference-type="ref" reference="3.25"}), the product of the second and third factors in the first term have the same leading asymptotic behaviour $$\begin{aligned}
-(2l+1)! \, 
4(vN)^{a/2} J_{a}\left(\sqrt{vY}\right)\, 
e^{-v\tau} \,  , \quad  v = 2l/N \, .  
\label{3.34}
\end{aligned}$$ Multiplying this by ([\[3.28\]](#3.28){reference-type="ref" reference="3.28"}) (with $k \mapsto l + 1$) and substituting in ([\[2.p\]](#2.p){reference-type="ref" reference="2.p"}) gives that the desired asymptotic form is $$\begin{aligned}
\lefteqn{I_4^{\rm hard}(X,Y;t_X,t_Y)} \nonumber  \\
&& = 
{1 \over 4} \int_{1}^{\infty}\left\{
\int_{v}^{\infty}dr \, 
r^{-a/2}  e^{-r t_{X}} J_{a}\left(\sqrt{rX}\right)\right\}
v^{a/2} J_{a}\left(\sqrt{vY}\right) e^{-vt_{Y}} \, dv - (X \leftrightarrow Y)  .
\label{3.35}
\end{aligned}$$

### Asymptotics of $D(x, y; \tau_{x}, \tau_{y})$

Here we require the asymptotic form of $\{R_{l}(x; \tau)\}$. For $l$ even this is given by ([\[3.30\]](#3.30){reference-type="ref" reference="3.30"}). On the other hand, for $l$ odd we see from ([\[2.i\]](#2.i){reference-type="ref" reference="2.i"}), ([\[3.1\]](#3.1){reference-type="ref" reference="3.1"}) and ([\[3.24\]](#3.24){reference-type="ref" reference="3.24"}) that $$\begin{aligned}
R_{2j+1}(y; \tau)e^{\gamma_{2j+1}\tau} = -(2j+1)! 
\left( L_{2j+1}^{a}(y) 
e^{\gamma_{2j+1}\tau} - L_{2j}^{a}(y) e^{\gamma_{2j}\tau}
\right)  \,  . 
\label{3.36}
\end{aligned}$$ Use of ([\[3.12\]](#3.12){reference-type="ref" reference="3.12"}) shows $$\begin{aligned}
\left. \sqrt{w(y)} \,  R_{2j+1}(y; \tau) e^{\gamma_{2j+1}\tau}
\right|_{y = Y/4N \atop \tau = t/2N} 
\sim -(2j+1)! N^{a/2 - 1} \frac{d}{ds}\left( 
e^{st} s^{a/2} J_{a}\left(\sqrt{sY}\right) \right)  \, , 
\label{3.37}
\end{aligned}$$ $s := 2j/N$. Multiplying this by $(2j + 1)!$ times ([\[3.30\]](#3.30){reference-type="ref" reference="3.30"}) (with $Y$ replaced by $X$) and dividing by ([\[3.25\]](#3.25){reference-type="ref" reference="3.25"}) we thus have $$\begin{aligned}
D_4^{\rm hard}(X,Y;t_X,t_Y)
& \sim  &  -\frac{1}{4} \int_{0}^{1}ds\, s^{-a/2} \left\{
\int_{0}^{s} u^{-a/2}  \frac{d}{du}\left( 
e^{u t_{X}} u^{a/2} J_{a}\left(\sqrt{uX}\right) \right) du \right\} 
\nonumber \\  &  & \quad \times 
\frac{d}{ds}\left( e^{st_{Y}} s^{a/2} J_{a}\left(\sqrt{sY}\right) \right) 
 - (X \leftrightarrow Y) \,  .
\label{3.38}
\end{aligned}$$
