---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-012-32-deviations-at-the-scale-otn
section_title: "Deviations at the scale O(tn)"
section_number: 3.2
pages: 16-21
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.959
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\begin{lemma}\label{lem:fourier}
Let $X$ be a $\Z$-valued random variable whose generating function $\varphi_{X}(z)=\esper[\E^{zX}]$ converges absolutely in the strip $\mathcal{S}_{(c,d)}$, with $c < 0 <d$. For $k \in \Z$,
\begin{align*}
\forall h \in (c,d),\,\,\,\proba[X=k]&=\frac{1}{2\pi}\int_{-\pi}^{\pi} \E^{-k(h+\I u)}\,\varphi_{X}(h + \I u)\,du;\\
\forall h \in (0,d),\,\,\,\proba[X\geq k]&=\frac{1}{2\pi}\int_{-\pi}^{\pi} \frac{\E^{-k(h+\I u)}}{1-\E^{-(h+ \I u)}}\,\varphi_{X}(h + \I u)\,du.
\end{align*}
\end{lemma}

\begin{proof}
Since $$\varphi_{X}(h+\I u )=\sum_{k \in \Z} \proba[X=k]\,\E^{k(h+\I u )},$$ $\proba[X=k]\,\E^{kh}$ is the $k$-th Fourier coefficient of the $2\pi$-periodic and smooth function $u \mapsto \varphi_{X}(h+\I u)$; this leads to the first formula. Then, assuming also $h >0$,
$$ \proba[X \geq k]=\sum_{l=k}^{\infty} \proba[X=l] = \sum_{l=k}^{\infty} \frac{1}{2\pi}\int_{-\pi}^{\pi} \E^{-l(h+\I u)}\,\varphi_{X}(h + \I u)\,du, $$
and the sum of the moduli of the functions on the right-hand side is dominated by the integrable function $\frac{\E^{-kh}}{1-\E^{-h}}\,\varphi_{X}(h)$; so by Lebesgue's dominated convergence theorem, one can exchange the integral and the summation symbol, which yields the second equation.
\end{proof}
\bigskip

We now work under the assumptions of Definition \ref{def:modphi}, with a lattice infinitely divisible distribution $\phi$. Furthermore, we assume that the convergence is at speed $O((t_{n})^{-v})$, on a strip $\mathcal{S}_{(c,d)}$ containing $0$. Note that necessarily $\eta(0)=0$ and $\psi(0)=1$. A simple computation gives also the following approximation formulas:
\begin{align*}
    \esper(X_n)&=\varphi'_n(0)=t_n \eta'(0) + \psi'(0) \sim t_n \eta'(0) = t_n \eta'(0) +O(1); \\
    \Var(X_n)&=\varphi''_n(0)-\varphi'_n(0)^2 = t_n \eta''(0) +O(1).
\end{align*}

\begin{theorem}\label{thm:mainlattice}
Let $x$ be a real number in the interval $(\eta'(c),\eta'(d))$, and $h$ defined by the implicit equation $\eta'(h)=x$. We assume $t_{n}x \in \N$. \vspace{2mm}
\begin{enumerate}
\item The following expansion holds:
\begin{align*}
\proba[X_{n}=t_{n}x]&=\frac{\exp(-t_{n}F(x))}{\sqrt{2\pi t_{n}\eta''(h)}} \left(\psi(h)+\frac{a_{1}}{t_{n}}+\frac{a_{2}}{(t_{n})^{2}}+\cdots+\frac{a_{v-1}}{(t_{n})^{v-1}}+O\!\left(\frac{1}{(t_{n})^{v}}\right)\!\right)\\
&= \exp(-t_{n}F(x))\, \sqrt{\frac{F''(x)}{2\pi t_{n}}} \left(\psi(F'(x))+\frac{a_{1}}{t_{n}}+\cdots+\frac{a_{v-1}}{(t_{n})^{v-1}}+O\!\left(\frac{1}{(t_{n})^{v}}\right)\!\right),
\end{align*}
for some numbers $a_k$.\vspace{2mm}
\item Similarly, if $x$ is a real number in the range of $\eta'_{|(0,d)}$, then
$$\proba[X_{n}\geq t_{n}x]= \frac{\exp(-t_{n}F(x))}{\sqrt{2\pi t_{n}\eta''(h)}}\, \frac{1}{1-\E^{-h}}\left(\psi(h)+\frac{b_{1}}{t_{n}}+\cdots+\frac{b_{v-1}}{(t_{n})^{v-1}}+O\!\left(\frac{1}{(t_{n})^{v}}\right)\right),$$
for some numbers $b_k$.\vspace{2mm}
\end{enumerate}
Both $a_k$ and $b_k$ are rational fractions in the derivatives of $\eta$ and $\psi$ at $h$, that can be computed explicitly --- see Remark \ref{rem:computation_ak_bk}.
\end{theorem}\medskip 

\begin{proof}
With the notations of Definition \ref{def:modphi}, the first equation of Lemma \ref{lem:fourier} becomes
\begin{align}\proba[X_{n}=t_{n}x]&=\frac{1}{2\pi}\int_{-\pi}^{\pi} \E^{-t_{n}x\, (h+\I u)}\,\varphi_{n}(h + \I u)\,du\nonumber\\
&=\frac{1}{2\pi}\int_{-\pi}^{\pi} \E^{-t_{n}xh}\,\E^{t_{n}(\eta(h+\I u) - \I u x)}\,\psi_{n}(h + \I u)\,du \nonumber\\
&=\frac{ \E^{-t_{n}F(x)}}{2\pi}\int_{-\pi}^{\pi}\,\E^{t_{n}(\eta(h+\I u) - \eta(h)- \I u \eta'(h))}\,\psi_{n}(h + \I u)\,du.\label{eq:tobesplit}
\end{align}
The last equality uses the facts that $x h=F(x)+\eta(h)$ and $x=\eta'(h)$. We perform the Laplace method on \eqref{eq:tobesplit}, and to this purpose we split the integral in two parts. Fix $\delta >0$, and denote $q_{\delta}=\max_{u \in (-\pi,\pi)\setminus (-\delta,\delta)} |\exp(\eta(h+\I u)-\eta(h))|$. This is strictly smaller than $1$, since
$$\exp(\eta(h+\I u)-\eta(h))=\frac{\esper[\E^{(h+\I u)X}]}{\esper[\E^{hX}]} = \esper_{\mathbb{Q}}[\E^{\I u X}]$$
is the characteristic function of $X$ under the new probability $d\mathbb{Q}(\omega)=\frac{\E^{hX(\omega)}}{\esper[\E^{hX}]}d\mathbb{P}(\omega)$
(and $X$ has minimum lattice $\Z$). Note that Lemma \ref{lem:technicqdelta_lattice} hereafter is a more precise version of this inequality.
\bigskip

As a consequence, if $I_{(-\delta,\delta)}$ and $I_{(-\delta,\delta)^{\mathrm{c}}}$ denote the two parts of \eqref{eq:tobesplit} corresponding to $\int_{-\delta}^{\delta}$ and $\int_{-\pi}^{-\delta}+\int_{\delta}^{\pi}$, then
$$
|I_{(-\delta,\delta)^{\mathrm{c}}}|\leq \frac{ \E^{-t_{n}F(x)}}{2\pi} \int_{(-\delta,\delta)^{\mathrm{c}}} (q_{\delta})^{t_{n}} \,|\psi_{n}(h + \I u)|\,du \leq 2\,(\E^{-F(x)}\,q_{\delta})^{t_{n}} \max_{u \in (-\pi,\pi)} |\psi(h+\I u)|
$$
for $n$ big enough, since $\psi_{n}$ converges uniformly towards $\psi$ on the compact set $K=h+\I[-\pi,\pi]$. Since $q_{\delta}<1$, for any $\delta>0$ fixed, $I_{(-\delta,\delta)^{\mathrm{c}}}\,\E^{t_{n}F(x)}$ goes  to $0$ faster than any negative power of $t_{n}$, so $I_{(-\delta,\delta)^{\mathrm{c}}}$ is negligible in the asymptotics
(recall that $F(x)$ is non-negative by definition, as $\eta(0)=0$).\bigskip

As for the other part, we can first replace $\psi_{n}$ by $\psi$ up to a $(1+O((t_{n})^{-v}))$, since the integral is taken on a compact subset of $\mathcal{S}_{(c,d)}$.
We then set $u=\frac{w}{\sqrt{t_{n}\eta''(h)}}$:
\begin{equation}
I_{(-\delta,\delta)}=\frac{\E^{-t_{n}F(x)}\left(1+O\!\left(\frac{1}{(t_{n})^{v}}\right)\right)}{2\pi \sqrt{t_{n}\eta''(h)}}\int_{-\delta \sqrt{t_{n}\eta''(h)}}^{\delta  \sqrt{t_{n}\eta''(h)}} \psi\!\left(h+\frac{\I w}{ \sqrt{t_{n}\eta''(h)}}\right) \,\E^{t_{n}\Delta_n(w)-\frac{w^{2}}{2}}\,dw,
\label{eq:principal}
\end{equation}
where $\Delta_n(w)$ is the Taylor expansion
\begin{align*}
\eta\left(h+\I u\right)&-\eta(h)-\eta'(h) \left(\I u \right)-\frac{\eta''(h)}{2} \left(\I u \right)^{2}\\
&=\sum_{k=3}^{2v+1} \frac{\eta^{(k)}(h)}{k!}\left(\frac{\I w}{ \sqrt{t_{n}\eta''(h)}}\right)^{\!k}+O\!\left(\frac{1}{(t_{n})^{v+1}}\right)\\
&=\frac{1}{t_{n}} \left(-\frac{w^{2}}{\eta''(h)}\sum_{k=1}^{2v-1} \frac{\eta^{(k+2)}(h)}{(k+2)!}\left(\frac{\I w}{ \sqrt{t_{n}\eta''(h)}}\right)^{\!k}+O\!\left(\frac{1}{(t_{n})^{v}}\right)\right).
\end{align*}
We also replace $\psi$ by its Taylor expansion
$$\psi\!\left(h+\frac{\I w}{ \sqrt{t_{n}\eta''(h)}}\right)=\sum_{k=0}^{2v-1} \frac{\psi^{(k)}(h)}{k!}\left(\frac{\I w}{ \sqrt{t_{n}\eta''(h)}}\right)^{\!k}+O\!\left(\frac{1}{(t_{n})^{v}}\right).$$
Thus, if one defines $\alpha_k$ by the equation
\begin{align*}
f_{n}(w)&:=\left(\sum_{k=0}^{2v-1} \frac{\psi^{(k)}(h)}{k!}\left(\frac{\I w}{ \sqrt{t_{n}\eta''(h)}}\right)^{\!k}\right)\,\exp\!\left(-\frac{w^{2}}{\eta''(h)}\sum_{k=1}^{2v-1} \frac{\eta^{(k+2)}(h)}{(k+2)!}\left(\frac{\I w}{ \sqrt{t_{n}\eta''(h)}} \right)^{\!k}\right)\\
&=\sum_{k=0}^{2v-1} \frac{\alpha_{k}(w)}{(t_{n})^{k/2}}+O\!\left(\frac{1}{(t_{n})^{v}}\right),
\end{align*}
then one can replace $\psi(h+\I u) \,\E^{t_{n}\Delta_n(w)}$ by $f_{n}(w)$ in Equation \eqref{eq:principal}. Moreover, observe that each coefficient $\alpha_{k}(w)$ writes as
$$\alpha_{k}(w)=\alpha_{k,0}(h)\left(\frac{w}{\sqrt{\eta''(h)}}\right)^{k}+\alpha_{k,1}(h)\left(\frac{w}{\sqrt{\eta''(h)}}\right)^{k+2}+\cdots+\alpha_{k,r}(h)\left(\frac{w}{\sqrt{\eta''(h)}}\right)^{k+2r}$$
with the $\alpha_{k,r}(h)$'s polynomials in the derivatives of $\psi$ and $\eta$ at point $h$. So,
$$I_{(-\delta,\delta)}=\left(1+O\!\left(\frac{1}{(t_{n})^{v}}\right)\right)\frac{\E^{-t_{n}F(x)}}{\sqrt{2\pi t_{n}\eta''(h)}} \left(\sum_{k=0}^{2v-1} \int_{-\delta \sqrt{t_{n}\eta''(h)}}^{\delta  \sqrt{t_{n}\eta''(h)}} \frac{\alpha_{k}(w)}{(t_{n})^{k/2}}\,\frac{\E^{-\frac{w^{2}}{2}}}{\sqrt{2\pi}}\,dw\right).$$
For any power $w^{m}$,  
$$\left|\int_{-\infty}^{\infty} w^{m} \,\frac{\E^{-\frac{w^{2}}{2}}}{\sqrt{2\pi}}\,dw-\int_{-\delta\sqrt{t_{n}\eta''(h)}}^{\delta\sqrt{t_{n}\eta''(h)}} w^{m}\, \frac{\E^{-\frac{w^{2}}{2}}}{\sqrt{2\pi}}\,dw\right|$$ is smaller than any negative power of $t_{n}$ as $n$ goes to infinity (see Lemma \ref{lem:gaussintegral}, \eqref{item:gausstail} for the case $m=0$): indeed, by integration by parts, one can expand the difference as 
$\E^{-\delta^{2}\,t_{n}\eta''(h)/2}\,R_{m}(\sqrt{t_{n}}),$
where $R_{m}$ is a rational fraction that depends on $m,h,\delta$ and on the order of the expansion needed. Therefore, one can take the full integrals in the previous formula. On the other hand, the odd moments of the Gaussian distribution vanish. One concludes that
$$
\proba[X_{n}=t_{n}x]=\frac{\E^{-t_{n}F(x)}}{\sqrt{2\pi t_{n}\eta''(h)}} \left(\sum_{k=0}^{v-1} \frac{1}{(t_{n})^{k}} \left(\int_{\R} \alpha_{2k}(w)\,\frac{\E^{-\frac{w^{2}}{2}}}{\sqrt{2\pi}}\,dw\right)+O\!\left(\frac{1}{(t_{n})^{v}}\right)\right),$$
and each integral $\int_{\R} \alpha_{2k}(w)\,\frac{\E^{-\frac{w^{2}}{2}}}{\sqrt{2\pi}}\,dw$ is equal to 
$$
\frac{\alpha_{2k,0}(h) \,(2k-1)!!}{(\eta''(h))^{k}}+\cdots+\frac{\alpha_{2k,r}(h) \,(2k+2r-1)!!}{(\eta''(h))^{k+r}}
$$
where $(2m-1)!!$ is the $2m$-th moment of the Gaussian distribution (\emph{cf.} Lemma \ref{lem:gaussintegral}, \eqref{item:gaussmoment}). This ends the proof of the first part of our Theorem, the second formula coming from the identities $h=F'(x)$ and $\eta''(h)=\frac{1}{F''(x)}$. The second part is exactly the same, up to the factor
$$\frac{1}{1-\E^{-h-\I u}}=\frac{1}{1-\E^{-h}}\,\left(\frac{1-\E^{-h}}{1-\E^{-h-\frac{\I w}{\sqrt{t_{n}\eta''(h)}}}}\right)$$
in the integrals.
\end{proof}\medskip

\begin{remark}\label{rem:deviation}
For $x > \eta'(0)$, the first term of the expansion
$$\frac{\exp(-t_{n}F(x))}{\sqrt{2\pi t_{n}\eta''(h)}}$$ 
is the leading term in the asymptotics of $\proba[Y_{t_{n}}=t_{n}x]$, where $(Y_{t})_{t \in \R_{+}}$ is the L\'evy process associated to the analytic function $\eta(z)$. Thus, the residue $\psi$ measures the difference between the distribution of $X_{n}$ and the distribution of $Y_{t_{n}}$ in the interval $(t_{n}\eta'(0),t_{n}\eta'(d))$. 
\end{remark}

\begin{remark}
If the convergence is faster than any negative power of $t_{n}$, then one can simplify the statement of the theorem as follows: as formal power series in $t_{n}$,
$$ \sqrt{2\pi t_{n}\eta''(h)}\,\exp(t_{n}F(x))\,\proba[X_{n}=t_{n}x]=\int_{\R} f_{n}(w)\,\E^{-\frac{w^{2}}{2}}\,dw,$$
\emph{i.e.}, the expansions of both sides up to any given power $O\!\left(\frac{1}{(t_{n})^{v}}\right)$ agree.
\end{remark}

\begin{remark}\label{rem:computation_ak_bk}
As mentioned in the statement of the theorem, the proof also gives an algorithm to obtain formulas for $a_k$ and $b_k$. More precisely, denote  
\begin{align*}\Delta_{n}(w)&=t_{n}\left(\eta\!\left(h+\frac{\I w}{\sqrt{t_{n}\eta''(h)}}\right)-\eta(h)-\eta'(h)\,\frac{\I w}{\sqrt{t_{n}\eta''(h)}}+\frac{w^{2}}{2t_{n}}\right)\\
f_{n}(w)&=\psi \!\left(h+\frac{\I w}{\sqrt{t_{n}\eta''(h)}}\right)\,\exp(t_n \Delta_{n}(w))=\sum_{k=0}^{\infty} \frac{\alpha_{k}(w)}{(t_{n})^{k/2}},
\end{align*}
the last expansion holding in a neighborhood of zero. The coefficient $\alpha_{2k}(w)$ is an even polynomial in $w$ with valuation $2k$ and coefficients which are polynomials in the derivatives of $\psi$ and $\eta$ at $h$, and in $\frac{1}{\eta''(h)}$. Then, 
$$a_{k}=\int_{\R}\alpha_{2k}(w) \,\frac{\E^{-\frac{w^{2}}{2}}}{\sqrt{2\pi}}\,dw,$$
and in particular,
\begin{align*}
a_{0}&= \psi(h);\\ 
a_{1}&= -\frac{1}{2}\,\frac{\psi''(h)}{\eta''(h)}+\frac{1}{24}\,\frac{\psi(h)\,\eta^{(4)}(h)+4\,\psi'(h)\,\eta^{(3)}(h)}{(\eta''(h))^{2}}-\frac{15}{72}\,\frac{\psi(h)\,(\eta^{(3)}(h))^{2}}{(\eta''(h))^{3}}.
\end{align*}
the $b_{k}$'s are obtained by the same recipe as the $a_{k}$'s, but starting from the power series
$$g_{n}(w)=\frac{1-\exp(-h)}{1-\exp\!\left(-h- \frac{\I w}{\sqrt{t_{n}\eta''(h)}}\right)}\,f_{n}(w).$$
\end{remark}
\medskip










\begin{example}\label{ex:randomcycle}
Suppose that $(X_{n})_{n \in \N}$ is mod-Poisson convergent, that is to say that $\eta(z)=\E^{z}-1$. The expansion of Theorem \ref{thm:mainlattice} reads then as follows:
$$\proba[X_{n}=t_{n}x]=\frac{\E^{t_{n} (x-1-x\log x)}}{\sqrt{2\pi x t_{n} }}\left(\psi(h)+\frac{\psi'(h)-3\psi''(h)-\psi(h)}{6xt_{n}}+O\!\left(\frac{1}{(t_{n})^{2}}\right)\right) $$
with $h = \log x$. For instance, if $X_{n}$ is the number of cycles of a random permutation in $\mathfrak{S}(n)$, then the discussion of Example \ref{ex:cycle} shows that for $x > 0$ such that $x\log n \in \N$, 
$$\proba[X_{n}= x(\log n)] = \frac{n^{-(x\log x-x+1)}}{\sqrt{2\pi x\,\log n}}\,\frac{1}{\Gamma(x)}\big(1+O(1/\log n)\big).$$
Similarly, for $x > 1$ such that $x\log n \in \N$, one has 
$$\proba[X_{n}\geq x(\log n)] = \frac{n^{-(x\log x-x+1)}}{\sqrt{2\pi x\,\log n}}\,\frac{x}{x-1}\,\frac{1}{\Gamma(x)}\big(1+O(1/\log n)\big).$$
As the speed of convergence is very good in this case, precise expansions in $1/\log n$ to any order could  also be given.
\end{example}
\bigskip
