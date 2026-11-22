---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-013-33-central-limit-theorem-at-the-scales-otn-and-o
section_title: "Central limit theorem at the scales o(tn) and o(tn23)"
section_number: 3.3
pages: 21-25
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 0.969
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
The previous paragraph has described in the lattice case the fluctuations of $(X_n)_{n \in \N}$ in the regime $O(t_n)$, with a result akin to large deviations. In this section, we establish in the same setting an extended central limit theorem, for fluctuations of order up to $o(t_n)$. In particular, for fluctuations of order $o((t_n)^{2/3})$, we obtain the usual central limit theorem. Hence, we describe the panorama of fluctuations drawn on Figure \ref{fig:panoramalattice}.

\begin{center}
\begin{figure}[ht]
\begin{tikzpicture}
\draw (-0.5,1.5) node {order of fluctuations};
\draw (2.3,0) node {large deviations ($\eta'(0)<x$):};
\draw (1.75,-1) node {extended central limit};
\draw (3,-3) node {central limit theorem ($y \ll (t_n)^{1/6}$):};
\draw (2.7,-1.4) node {theorem ($(t_n)^{1/6}\lesssim y \ll (t_n)^{1/2}$):};
\draw (9.2,-0.05) node {$\proba[\frac{X_n}{t_n} \geq x] \simeq \frac{\exp(-t_n\,F(x))}{\sqrt{2\pi t_n\eta'(x)}}\,\frac{1}{1-\E^{-F'(x)}}\,\psi(F'(x));$};
\draw (9.2,-1.5) node {$\proba[\frac{X_n-t_n\eta'(0)}{\sqrt{t_n\,\eta''(0)}} \geq y] \simeq \frac{\exp(-t_n\,F(x))}{F'(x)\,\sqrt{2\pi t_n \eta'(x)}};$};
\draw (9.23,-3.8) node {$\proba[\frac{X_n-t_n\eta'(0)}{\sqrt{t_n\,\eta''(0)}} \geq y] \simeq \proba[\mathcal{N}_{\R}(0,1)\geq y].$};
\draw[->,thick] (-2,-5) -- (-2,1) ;
\draw[thick] (-2.1,0) -- (-1.9,0);
\draw (-1.25,0) node {$O(t_n)$} ;
\draw[->,thick] (-2.1,-2) -- (-1.9,-2) -- (-1.9,-0.1);
\draw (-0.85,-2) node {$O((t_n)^{2/3})$} ;
\draw[->,thick] (-2.1,-4) -- (-1.9,-4) -- (-1.9,-2.1) ;
\draw (-0.85,-4) node {$O((t_n)^{1/2})$} ;
\end{tikzpicture}
\caption{Panorama of the fluctuations of a sequence of random variables $(X_n)_{n\in\N}$ that converges modulo a lattice distribution (with $x=\eta'(0) + \sqrt{\eta''(0)/t_n}\,y$).}\label{fig:panoramalattice}
\end{figure}
\end{center}

\begin{theorem}\label{thm:cltlattice}
Consider a sequence $(X_n)_{n \in \N}$ that converges mod-$\phi$, with a reference infinitely divisible law $\phi$ that is a lattice distribution. Assume $y=o((t_{n})^{1/6})$. Then,
$$\proba\!\left[X_{n}\geq t_{n}\eta'(0)+\sqrt{t_{n}\eta''(0)}\,y\right]=\proba[\mathcal{N}_{\R}(0,1)\geq y]\left(1+o(1)\right).$$
On the other hand, assuming $y \gg 1$ and $y=o((t_n)^{1/2})$, if $x=\eta'(0)+\sqrt{\eta''(0)/t_n}\,y$ and $h$ is the solution of $\eta'(h)=x$, then
\begin{align}
    \proba\!\left[X_{n}\geq t_{n}\eta'(0)+\sqrt{t_{n}\eta''(0)}\,y\right]
& = \frac{\E^{-t_n F(x)}}{h \sqrt{2\pi t_{n}\,\eta''(h)}}(1+o(1)) ; \nonumber\\
& = \frac{\E^{-t_n F(x)}}{y \sqrt{2\pi}} (1+o(1)).
\label{EqGaussianTailY}
\end{align}
\end{theorem}
\medskip

\begin{remark}
The case $y=O(1)$, which is the classical central limit theorem, follows immediately from the assumptions of Definition \ref{def:modphi}, since by a Taylor expansion around $0$ of $\eta$ the characteristic functions of the rescaled r.v. 
\[Y_{n}=\frac{X_{n}-t_{n}\eta'(0)}{\sqrt{t_{n}\eta''(0)}}\] 
converge pointwise to $\E^{-\frac{\zeta^{2}}{2}}$, the characteristic function of the standard Gaussian distribution.
In the first statement, the improvement here is the weaker assumption $y=o((t_{n})^{1/6})$.
\end{remark}\medskip

As we shall see, the ingredients of the proof are very similar to the ones in the previous paragraph. We start with a technical lemma of control of the module of the Fourier transform of the reference law $\phi$. 

\begin{lemma}\label{lem:technicqdelta_lattice}
Consider a non-constant infinitely divisible law $\phi$, of type lattice, and with convergent moment generating function $\int \E^{zx}\,\phi(dx) = \E^{\eta(z)}$ on a strip $\mathcal{S}_{(c,d)}$ with $c<0<d$. We assume without loss of generality that $\phi$ has minimal lattice $\Z$. Then, there exists a constant $D>0$ only depending on $\phi$, and an interval $(-\eps,\eps)\subset (c,d)$, such that for all $h \in (-\eps,\eps)$ and all $\delta$ small enough,
$$q_{\delta}= \max_{u \in [-\pi,\pi]\setminus (-\delta,\delta)} |\exp(\eta(h+\I u)-\eta(h))|$$ 
is smaller than $1-D\,\delta^{2}$.
\end{lemma}

\begin{proof}
Denote $X$ a random variable under the infinitely divisible distribution $\phi$. We claim that there exist two consecutive integers $n$ and $m=n-1$ with $\proba[X=n]\neq 0$ and $\proba[X=m]\neq 0$. Indeed, under our hypotheses, if $\Pi$ is the L\'evy measure of $\phi$, then 
$$\Z=\Z[\supp(\Pi)]=\N[\supp(\Pi)]-\N[\supp(\Pi)],$$ 
so there exist $a$ and $b$ in $\N[\supp(\Pi)]$ such that $b-a=1$. However, $\supp(\phi)=\gamma+\N[\supp(\Pi)]$ for some $\gamma \in \Z$, so $n=\gamma+b$ and $m=\gamma+a$ satisfy the claim.\bigskip

Now, we have seen that $\exp(\eta(h+\I u)-\eta(h))$ can be interpreted as the characteristic function of $X$ under the new probability measure $d\mathbb{Q}=\frac{\E^{hX}}{\esper[\E^{hX}]}\,d\proba$. So, for any $u$,
\begin{align*}
|\exp(\eta(h+\I u)-\eta(h))|^{2}&=\left|\esper_{\mathbb{Q}}[\E^{\I u X}]\right|^{2} = \sum_{n,m \in \Z} \mathbb{Q}[X=n]\,\mathbb{Q}[X=m]\,\E^{\I u (n-m)} \\
&= \sum_{k \in \Z}  \left(\sum_{n-m=k} \mathbb{Q}[X=n]\,\mathbb{Q}[X=m] \right)\cos ku.
\end{align*}
Fix two integers $n$ and $m=n-1$ such that $\proba[X=n]\neq 0$ and $\proba[X=m]\neq 0$. Then one also has $\mathbb{Q}[X=n]\neq 0$, $\mathbb{Q}[X=m]\neq 0$, and there exists
$D >0$ such that
$$\mathbb{Q}[X=n]\,\mathbb{Q}[X=m] \geq 15\,D>0$$
for $h$ small enough ($\mathbb{Q}$ tends to $\mathbb{P}$ for $h\to 0$).
As $\cos u \leq 1-\frac{u^{2}}{5}$ for all $u \in (-\pi,\pi)$, 
\begin{align*}
&|\exp(\eta(h+\I u)-\eta(h))|^{2} \leq 1+15\,D\,(\cos u-1) \leq 1-3\,D\,u^{2};\\ 
&q_{\delta} \leq \sqrt{1-3\,D\,\delta^{2}} \leq 1-D\,\delta^{2} \text{ for $\delta$ small enough}.
\end{align*}
This concludes the proof of the Lemma.\end{proof}
\medskip

\begin{proof}[Proof of Theorem \ref{thm:cltlattice}]
Notice that $\eta''(0)\neq 0$ since this is the variance of the law $\phi$, 
assumed to be non-trivial.
Set $x=\eta'(0)+s$, and assume $s =o(1)$. The analogue of Equation \eqref{eq:tobesplit} reads in our setting
\begin{equation}\proba[X_{n}\geq t_{n}x]=\frac{ \E^{-t_{n}F(x)}}{2\pi}\int_{-\pi}^{\pi}\,\frac{\E^{t_{n}(\eta(h+\I u) - \eta(h)- \I u \eta'(h))}}{1-\E^{-h-\I u}}\,\psi_{n}(h + \I u)\,du.\label{eq:tobesplit2}\end{equation}
Since $h'(x)=\frac{1}{\eta''(x)}$, one has $h=\frac{s}{\eta''(0)}+O(s^{2})$.
The same argument as in the proof of Theorem \ref{thm:mainlattice} shows that the integral over $(-\delta,\delta)^{\mathrm{c}}$ is bounded by $C\,\delta\,(q_{\delta})^{t_{n}},$ where $q_{\delta} <1$, and $C\,\delta$ (with $C$ a constant independent from $s$ and $\delta$) comes from the computation of 
$$\max_{u \in (-\delta,\delta)^{\mathrm{c}}}\left|\frac{\psi(h+\I u)}{1-\E^{-h-\I u}}\right|.$$
In the following we shall need to make $\delta$ go to zero sufficiently fast, but with $\delta\sqrt{t_{n}\eta''(0)}$ still going to infinity. Thus, set $\delta=(t_{n})^{-2/5}$, so that in particular $(t_{n})^{-1/2}\ll \delta \ll (t_{n})^{-1/3}$.
Notice that $I_{(-\delta,\delta)^\mathrm{c}}\,\,\E^{t_{n}F(x)}$ still goes to zero faster than any power of $t_{n}$; indeed, 
$$(q_{\delta})^{t_{n}}\leq \left(1-\frac{D}{(t_{n})^{4/5}}\right)^{t_{n}} \leq \E^{-D\,(t_{n})^{1/5}}$$
by Lemma \ref{lem:technicqdelta_lattice}. The other part of \eqref{eq:tobesplit2} is 
$$\frac{\E^{-t_{n}F(x)}}{2\pi \sqrt{t_{n}\eta''(h)}}\int_{-\delta \sqrt{t_{n}\eta''(h)}}^{\delta  \sqrt{t_{n}\eta''(h)}} \psi\!\left(h+\frac{\I w}{ \sqrt{t_{n}\eta''(h)}}\right) \,\E^{t_{n}\Delta_n(w)}\,\frac{\E^{-\frac{w^{2}}{2}}}{1-\E^{-h-\frac{\I w}{\sqrt{t_{n}\eta''(h)}}}}\,dw,$$
up to a factor $(1+o(1))$. Let us analyze each part of the integral:\vspace{2mm}
\begin{itemize}
\item The difference between $\psi\left(h+\frac{\I w}{ \sqrt{t_{n}\eta''(h)}}\right)$ and $\psi(0)$ is bounded by
$$\max_{z \in [-s,s]+\I[-\delta,\delta]}|\psi(z)-\psi(0)|=o(1)$$
by continuity of $\psi$, so one can replace the term with $\psi$ by the constant $\psi(0)=1$, up to factor $(1+o(1))$.\vspace{2mm}
\item The term $\Delta_n(w)$ has for Taylor expansion
$$\frac{\eta^{(3)}(h)}{6}\,\left(\frac{\I w}{\sqrt{t_{n}\eta''(h)}}\right)^{\!3}+O\left(\frac{1}{(t_{n})^{2}}\right),$$
so $t_{n}\,\Delta_n(w)$ is bounded by a $O(t_{n}\,\delta^{3})$, which is a $o(1)$ since $\delta\ll(t_{n})^{-1/3}$. So again one can replace $\E^{t_{n}\Delta_n(w)}$ by the constant $1$.\vspace{2mm}
\item The Taylor expansion of $\left(1-\E^{-h-\frac{\I w}{\sqrt{t_{n}\eta''(h)}}}\right)^{-1}$ is $\frac{1}{h+\frac{\I w}{\sqrt{t_{n}\eta''(h)}}}\,(1+o(1))$. Hence,
\begin{align*}\proba\left[X_{n}\geq t_{n}(\eta'(0)+s)\right]&= \frac{\E^{-t_{n}F(x)}}{2\pi} \left(\int_{\R} \frac{\E^{-\frac{w^{2}}{2}}}{\sqrt{t_{n}\eta''(h)} \,h+\I w} \,dw\right)\big(1+o(1)\big)\\
&=\E^{-t_{n}F(x)+\frac{h^{2}\,t_{n}\,\eta''(h)}{2}}\,\,\proba\!\left[\mathcal{N}_{\R}(0,1)\geq h\,\sqrt{t_{n}\eta''(h)}\right]\big(1+o(1)\big).
\end{align*}
Indeed, setting $\beta=h\sqrt{t_{n}\,\eta''(h)}$, this leads directly to the computation done in Lemma \ref{lem:gaussintegral}, \eqref{item:gausscomplex}.
\end{itemize}
Hence, we have shown so far that
\begin{equation}
\proba\left[X_{n}\geq t_{n}(\eta'(0)+s)\right]=\E^{-t_{n}F(\eta'(0)+s)}\,\E^{\frac{\beta^{2}}{2}}\,\proba[\mathcal{N}_{\R}(0,1)\geq \beta]\big(1+o(1)\big),\label{eq:forcomparisionwithradziwill}
\end{equation}
with $\beta=h\sqrt{t_{n}\,\eta''(h)}$.
\medskip

We now set $y=s\sqrt{t_{n}/\eta''(0)}=o(t_n^{1/2})$, and we consider the following regimes. If $y \gg 1$ (and \emph{a fortiori} if $y$ is of order bigger than $O(t_n)^{1/6}$), then  $s\gg (t_n)^{-1/2}$, so $h \gg (t_n)^{-1/2}$ and $\beta \gg 1$. We can then use Lemma \ref{lem:gaussintegral}, \eqref{item:gausstail} to replace in Equation \eqref{eq:forcomparisionwithradziwill} the function of $\beta$ by the tail-estimate of the Gaussian:
\begin{equation}
    \proba\left[X_n \geq t_n\eta'(0) + \sqrt{t_n\,\eta''(0)}y\right] 
= \frac{\E^{-t_n\,F(x)}}{h\,\sqrt{2\pi t_n\, \eta''(h)}}(1+o(1)).
\label{EqGaussianTail}
\end{equation}
Recall that $h=\frac{s}{\eta''(0)}\,(1+O(s))$, so that the denominator above can be approximated as follows:
\[h \sqrt{t_n\, \eta''(h)} =\frac{s}{\eta''(0)}\,(1+O(s))\, \sqrt{t_{n}\,(\eta''(0)+O(s))}= y\,(1+O(s))=y(1+o(1)).\]
This completes the proof of the second part of the theorem.
\medskip

Suppose on the opposite that $y=o((t_{n})^{1/6})$, or, equivalently, $s=o((t_{n})^{-1/3})$. Let us then see how everything is transformed.\vspace{2mm}
\begin{itemize}
\item By making a Taylor expansion around $\eta'(0)$ of the Legendre-Fenchel transform, we get (recall that $x=\eta'(0)$ implies $h=0$)
    \begin{equation}
        F(x)=F(\eta'(0))+F'(\eta'(0))\,s+\frac{F''(\eta'(0))}{2}\,s^{2}+O(s^{3})=\frac{y^{2}}{2t_{n}}+o((t_{n})^{-1}),
        \label{EqTaylorF}
    \end{equation}
so $\E^{-t_{n}F(\eta'(0)+s)}\simeq \E^{-\frac{y^{2}}{2}}$.  \vspace{2mm}
\item As above,
\[
\beta=h\sqrt{t_{n}\,\eta''(h)} = y\,(1+O(s))= y\,(1+o((t_{n})^{-1/3}))
\]
Consequently, $\beta^{2}=y^{2}(1+o((t_{n})^{-1/3}))=y^{2}+o(1)$, so $\E^{\frac{\beta^{2}}{2}}$ can be replaced safely by $\E^{\frac{y^{2}}{2}}$, which compensates the previous term.
\vspace{2mm}
\item Finally, fix $y$, and denote $F_{y}(\lambda)=\proba[\mathcal{N}_{\R}(0,1)\geq \lambda y]$. Then, for $|\lambda|$ say between $\frac{1}{2}$ and $2$,
$$|F_{y}'(\lambda)|=\left|\frac{y}{\sqrt{2\pi}}\,\E^{-\frac{\lambda^{2}y^{2}}{2}}\right|\leq \max_{y \in \R} \left|\frac{y}{\sqrt{2\pi}}\,\E^{-\frac{y^{2}}{8}}\right|=C<+\infty;$$
as a consequence,
\begin{align*}
\left|\proba[\mathcal{N}_{\R}(0,1)\geq \beta]-\proba[\mathcal{N}_{\R}(0,1)\geq y]\right|&=\left|F_{y}(1+o((t_{n})^{-1/3}))-F_{y}(1)\right|\\
&\leq \frac{C}{(t_{n})^{1/3}}=o(1).
\end{align*}
\end{itemize}
This ends the proof of Theorem \ref{thm:cltlattice}.
\end{proof}
\medskip

\begin{remark}
Equation \eqref{eq:forcomparisionwithradziwill} is the probabilistic counterpart of the number-theoretic results of \cite{Kub72,Rad09}, see in particular Theorems 2.1 and 2.2 in \cite{Rad09}. In Section \ref{subsec:arithmetic}, we shall explain how to recover the precise large deviation results of \cite{Rad09} for arithmetic functions whose Dirichlet series can be studied with the Selberg-Delange method.
\end{remark}\bigskip

The following corollary gives
a more explicit form of Theorem \ref{thm:cltlattice},
depending on the order of magnitude of $y$.
\begin{corollary}
    If $y=o((t_n)^{1/4})$, then one has
\begin{equation}
    \proba\!\big[X_n \ge t_n \eta'(0) + \sqrt{t_n \eta''(0)}\, y\big] 
    =\frac{ (1+o(1))}{y\sqrt{2\pi}} \,\E^{-\frac{y^2}{2}}\, \exp\left( \frac{\eta'''(0)}{6\,(\eta''(0))^{3/2}}\,\frac{y^3}{\sqrt{t_n}}
    \right) .
\label{EqCramerOrdre3}
\end{equation}
More generally, if $y=o((t_n)^{1/2-1/m})$, then one has
\begin{equation}
    \proba\!\big[X_n \ge t_n \eta'(0) + \sqrt{t_n \eta''(0)}\, y\big] 
    =\frac{(1+o(1))}{y\sqrt{2\pi}} \exp\left( - \sum_{i=2}^{m-1} \frac{F^{(i)}(\eta'(0))}{i!}\,\frac{(\eta''(0))^{i/2}\, y^i}{(t_n)^{(i-2)/2}}
    \right).
\label{EqCramerOrdreM}
\end{equation}
\end{corollary}
\begin{proof}
    As above in Equation \eqref{EqTaylorF}, we write $s=y\sqrt{\eta''(0)/t_{n}}$
    and $x=\eta'(0)+s$ and do a Taylor expansion of $F$ around $\eta'(0)$:
    \[F(x) = \sum_{i=0}^{m-1} \frac{F^{(i)}(\eta'(0))}{i!} \left( y\sqrt{\frac{\eta''(0)}{t_{n}}} \right)^i +O(s^{m}).\]
    Note that $F(\eta(0))=F'(\eta'(0))=0$.
    Because of the hypothesis $y=o((t_n)^{1/2-1/m})$, we have $t_n O(s^{m})=o(1)$.
    Therefore, plugging the equation above in Equation \eqref{EqGaussianTailY},
    we get \eqref{EqCramerOrdreM}.\medskip

    Observing that $F''(\eta'(0))=1/\eta''(0)$ and $F'''(\eta'(0))=\frac{-\eta'''(0)}{\eta''(0)^3}$,
    we get the first equation.
\end{proof}

To summarize, in the lattice case, mod-$\phi$ convergence implies a large deviation principle (Theorem \ref{thm:mainlattice}) and a precised central limit theorem (Theorem \ref{thm:cltlattice}), and these two results cover a whole interval of possible scalings for the fluctuations of the sequence $(X_n)_{n \in \N}$. As we shall see in the next Section \ref{sec:nonlattice}, the same holds for non-lattice reference distributions.
\bigskip
\bigskip
