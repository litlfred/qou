---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-007-21-basic-examples-of-mod-convergence
section_title: "Basic examples of mod-convergence"
section_number: 2.1
pages: 9-12
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.964
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{subsec:basicexamples}
Let us give a few examples of mod-$\phi$ convergence, which will guide our intuition throughout the paper. In these examples, it will be useful sometimes to precise the speed of convergence in Definition \ref{def:modphi}.

\begin{definition}
We say that the sequence of random variables $(X_{n})_{n \in \N}$ converges mod-$\phi$ at speed $O((t_{n})^{-v})$ if the difference of the two sides of Equation \eqref{eq:modphi} can be bounded by $C_{K}\,(t_{n})^{-v}$ for any $z$ in a given compact subset $K$ of $\mathcal{S}_{(c,d)}$. We use the analogue definition with the $o(\cdot)$ notation.
\end{definition}\medskip

\begin{example}\label{ex:sumiid}
Let $(Y_{n})_{n \in \N}$ be a sequence of centered, independent and identically distributed real-valued random variables, with $\esper[\E^{zY}]=\esper[\E^{zY_{1}}]$ analytic and non-vani\-shing on a strip $\mathcal{S}_{(c,d)}$, possibly with $c=-\infty$ and/or $d=+\infty$. Set $S_{n}=Y_{1}+\cdots+Y_{n}$. If the distribution of $Y$ is infinitely divisible,

then $S_n$ converges mod-$Y$ towards the limiting function $\psi \equiv 1$ with parameter $t_n=n$.\medskip

But there is another mod-convergence hidden in this framework (we now drop the assumption of infinite divisibility of the law of $Y$). The cumulant generating series of $S_{n}$ is
$$\log \esper[\E^{zS_{n}}]=n \,\log \esper[\E^{zY}] = n \sum_{r = 2}^{\infty}\frac{\kappa^{(r)}(Y)}{r!}\,z^{r},$$
which is also analytic on $\mathcal{S}_{(c,d)}$ --- the coefficients $\kappa^{(r)}(Y)$ are the \emph{cumulants} of the variable $Y$. Let $v\geq 3$ be an integer such that $\kappa^{(r)}(Y)=0$ for each integer $r$ strictly between $3$ and $v-1$, and set $X_{n}=\frac{S_{n}}{n^{1/v}}$. It is always possible to take $v=3$, but sometimes we can also consider higher value of $v$, for instance $v=4$ as soon as $Y$ is a symmetric random random variable, and has therefore its odd moments and cumulants that vanish. One has
$$\log \varphi_{n}(z) = n^{\frac{v-2}{v}} \,\frac{\kappa^{(2)}(Y)}{2}\,z^{2} + \frac{\kappa^{(v)}(Y)}{v!}\,z^{v} + \sum_{r = v+1}^{\infty} \frac{\kappa^{(r)}(Y)}{r!\,n^{r/v-1}}\,z^{r},$$
and locally uniformly on $\C$ the right-most term is bounded by $\frac{C}{n^{1/v}}$. Consequently, 
$$\psi_{n}(z)=\exp\left(-n^{\frac{v-2}{v}}\,\frac{\sigma^{2}z^{2}}{2}\right)\,\varphi_{n}(z) \to \exp\left(\frac{\kappa^{(v)}(Y)}{v!}\,z^{v}\right) + O(n^{-1/v}),$$
that is, $(X_{n})_{n \in \N}$ converges in the mod-Gaussian sense with parameters $t_{n}=\sigma^{2}\,n^{\frac{v-2}{v}}$, speed $O(n^{-1/v})$ and limiting function $\psi(z)=\exp(\kappa^{(v)}(Y)\,z^{v}/v!)$.  Note that this first example was used in \cite{KNN13} to characterize the set of limiting functions in the setting of mod-$\phi$ convergence.
\bigskip

Through this article, we shall commonly rescale random variables in order to get estimates of fluctuations at different regimes. In order to avoid any confusion, we provide the reader with the following scheme, which details each possible scaling, and for each scaling, the regimes of fluctuations that can be deduced from the mod-$\phi$ convergence, as well as their scope. We also underline or frame the scalings and regimes that will be studied in this paper, and give references for the other kinds of fluctuations.

\begin{center}
\begin{figure}[ht]
\begin{tikzpicture}
\draw (1,6) node {scaling};
\draw (1,4) node {$S_n$};
\draw (1,2) node {$\frac{S_n}{n^{1/v}}$};
\draw (5,6) node {mod-convergence};
\draw (3.75,5.4) node {$t_n$};
\draw (6.25,5.4) node {$\phi$};
\draw (3.75,4) node {$n$};
\draw (6.25,4) node {$Y$};
\draw (3.75,2) node {$\sigma^2 n^{1-\frac{2}{v}}$};
\draw (6.25,2) node {$\mathcal{N}_{\R}(0,1)$};
\draw[->,thick] (9.5,0) -- (9.5,5.5);
\draw[thick] (9.4,4) -- (9.6,4);
\draw (8.6,4) node {$\frac{S_n}{n}$};
\draw (8.6,3) node {$\frac{S_n}{n^{1-1/(v+1)}}$};
\draw (8.6,2) node {$\frac{S_n}{n^{1-1/v}}$};
\draw (8.6,1) node {$\frac{S_n}{n^{1/2}}$};
\draw (11.3,4) node {large deviations};
\draw (11.6,3.5) node {(\emph{cf.} \cite{BR60,DZ98})};
\draw (11.7,2.5) node {\underline{moderate deviations}};
\draw[thick,->] (9.4,2) -- (9.6,2) -- (9.6,2.95);
\draw[thick] (9.4,3) -- (9.6,3) ;
\draw (10,6) node {regime of fluctuations};
\draw[dashed,gray] (2.5,0) -- (2.5,6.5);
\draw[dashed,gray] (7.5,0) -- (7.5,6.5);
\draw[dashed,gray] (5,0) -- (5,5.7);
\draw[dashed,gray] (2.5,5.7) -- (7.5,5.7);
\draw[thick,->] (9.4,1) -- (9.6,1) -- (9.6,1.95);
\draw[thick,->] (9.6,0) -- (9.6,0.95) ;
\draw (11.22,1.5) node {\underline{normality zone}};
\draw (11.6,0.5) node {local limit theorem};
\draw (12.6,0.) node {(\emph{cf.} \cite{DKN11,KN12,FMN14})};
\draw (0,1) rectangle (7.5,3);
\end{tikzpicture}
\caption{Panorama of the fluctuations of a sum of $n$ i.i.d.~random variables.\label{fig:panoramaiid}}
\end{figure}
\end{center}
The content of this scheme will be fully explained in Section \ref{sec:nonlattice} (see in particular Section \ref{subsec:normalityzone}).
\end{example}\medskip


\begin{example}\label{ex:cycle}
Denote $X_{n}$ the number of disjoint cycles (including fixed points) of a random permutation chosen uniformly in the symmetric group $\mathfrak{S}(n)$. Feller's coupling (\emph{cf.} \cite[Chapter 1]{ABT03}) shows that $X_{n}=_{(\text{law})}\sum_{i=1}^{n}\mathcal{B}_{(1/i)},$
where $\mathcal{B}_{p}$ denotes a Bernoulli variable equal to $1$ with probability $p$ and to $0$ with probability $1-p$, and the Bernoulli variables are independent in the previous expansion. So,
$$\esper[\E^{zX_{n}}]=\prod_{i=1}^{n} \left(1+\frac{\E^{z}-1}{i}\right) = \E^{H_{n}(\E^{z}-1)}\,\prod_{i=1}^{n}\frac{1+\frac{\E^{z}-1}{i}}{\E^{\frac{\E^{z}-1}{i}}}$$
where $H_{n}=\sum_{i=1}^{n}\frac{1}{i}=\log n+\gamma+O(n^{-1})$. The Weierstrass infinite product in the right-hand side converges locally uniformly to an entire function, therefore (see \cite{WW27}),
$$\esper[\E^{zX_{n}}]\,\E^{-(\E^{z}-1)\log n} \to \E^{\gamma\,(\E^{z}-1)}\prod_{i=1}^{\infty}\frac{1+\frac{\E^{z}-1}{i}}{\E^{\frac{\E^{z}-1}{i}}}=\frac{1}{\Gamma(\E^{z})}$$
locally uniformly, \emph{i.e.}, one has mod-Poisson convergence with parameters $t_{n}=\log n$ and limiting function $1/\Gamma(\E^{z})$. Moreover, the speed of convergence is a $O(n^{-1})$, hence, a $o((t_{n})^{-v})$ for any integer $v$. We shall study generalizations of this example in Section \ref{subsec:cycles}.

\begin{center}
\begin{figure}[ht]
\begin{tikzpicture}
\draw (1,6) node {scaling};
\draw (1,4) node {$X_n$};
\draw (1,2) node {$\frac{X_n-H_n}{(H_n)^{1/3}}$};
\draw (5,6) node {mod-convergence};
\draw (3.75,5.4) node {$t_n$};
\draw (6.25,5.4) node {$\phi$};
\draw (3.75,4) node {$H_n$};
\draw (6.25,4) node {$\mathcal{P}(1)$};
\draw (3.75,2) node {$(H_n)^{1/3}$};
\draw (6.25,2) node {$\mathcal{N}_{\R}(0,1)$};
\draw[->,thick] (9.5,0) -- (9.5,5.5);
\draw[thick] (9.4,4) -- (9.6,4);
\draw (8.6,4) node {$\frac{X_n}{H_n}-1$};
\draw (8.6,3) node {$\frac{X_n-H_n}{(H_n)^{3/4}}$};
\draw (8.6,2) node {$\frac{X_n-H_n}{(H_n)^{2/3}}$};
\draw (8.6,1) node {$\frac{X_n-H_n}{(H_n)^{1/2}}$};
\draw (11.3,4) node {\underline{large deviations}};
\draw (11,3.5) node {(\emph{cf.} \cite{Rad09})};
\draw (11.7,2.5) node {\underline{moderate deviations}};
\draw[thick,->] (9.4,2) -- (9.6,2) -- (9.6,2.95);
\draw[thick] (9.4,3) -- (9.6,3) ;
\draw (10,6) node {regime of fluctuations};
\draw[dashed,gray] (2.5,0) -- (2.5,6.5);
\draw[dashed,gray] (7.5,0) -- (7.5,6.5);
\draw[dashed,gray] (5,0) -- (5,5.7);
\draw[dashed,gray] (2.5,5.7) -- (7.5,5.7);
\draw[thick,->] (9.4,1) -- (9.6,1) -- (9.6,1.95);
\draw[thick,->] (9.6,0) -- (9.6,0.95) ;
\draw (11.22,1.5) node {\underline{normality zone}};

\draw (11.6,0.3) node {local limit theorem};
\draw (0,1) rectangle (7.5,3);
\draw (0,3) rectangle (7.5,5);
\end{tikzpicture}
\caption{Panorama of the fluctuations of the number of cycles $X_n$ of a random permutation of size $n$.}
\end{figure}
\end{center}
Once again, there is another mod-convergence hidden in this example. Indeed, consider $Y_n=\frac{X_n-H_n}{(H_n)^{1/3}}$. Its generating function has asymptotics
$$\esper[\E^{zY_n}] = \E^{H_n\left(\E^{\frac{z}{(H_n)^{1/3}}}-1\right) - z(H_n)^{2/3}}\,(1+o(1)) = \E^{(H_n)^{1/3}\,\frac{z^2}{2}}\,\exp\left(\frac{z^3}{6}\right)\,(1+o(1)).$$
Therefore, one has mod-Gaussian convergence of $Y_n$ with parameters $t_n=(H_n)^{1/3}$ and limiting function $\exp(z^3/6)$.
\medskip

This is in fact a particular case of a more general phenomenon:
every sequence that converges mod-$\phi$
converges with a different rescaling in the mod-Gaussian sense.
\begin{proposition}
    Assume $X_n$ converges mod-$\phi$ with parameters $t_n$ and limiting function $\psi$,
    where $\phi$ is not the Gaussian distribution.
    Let 
    \[m = \min_{i \ge 3} \{i \mid \eta^{(i)}(0) \ne 0 \}.\]
    Then, the sequence of random variables $Y_n=(X_n-t_n \eta'(0))/(t_n)^{1/m}$ converges in the mod-Gaussian sense
    with parameters $(t_n)^{1-2/m} \eta''(0)$ towards the limiting function $\Psi(z)=\exp\big(\eta^{(m)}(0) z^m/m!)$.
\end{proposition}
\begin{proof}
    This follows from a simple computation
    \begin{align*}
    &\esper\! \left[  \exp \left( \frac{z (X_n-t_n \eta'(0))}{(t_n)^{1/m}}  \right)\right] \\
    &=\exp\!\left( \frac{-t_n \eta'(0))}{(t_n)^{1/m}} \right) \, \exp \!\left( t_n\, \eta\!\left(\frac{z}{(t_n)^{1/m}}\right) \right)\, \psi\!\left(\frac{z}{(t_n)^{1/m}}\right) (1+o(1)).
    \end{align*}
    The factor $\psi(\frac{z}{(t_n)^{1/m}})$ tends to $1$ and we do a Taylor expansion of $\eta(\frac{z}{(t_n)^{1/m}})$. We get
    \[\esper \!\left[  \exp \left( \frac{z (X_n-t_n \eta'(0))}{(t_n)^{1/m}}  \right)\right]             
        = \exp\!\left( (t_n)^{1-2/m} \eta''(0) \frac{z^2}{2} + \eta^{(m)}(0) \frac{z^m}{m!} + o(1) \right)( 1+o(1)). \qedhere\]
\end{proof}
Naturally, the mod-$\phi$ convergence gives more information than the implied mod-Gaussian convergence:
our deviation results --- Theorems \ref{thm:mainlattice} and \ref{thm:mainnonlattice} ---
for the former involve deviation probabilities of $X_n$ at scale $O(t_n)$,
while with the mod-Gaussian convergence, we get deviation probabilities of $Y_n$ at scale $O((t_n)^{1-2/m})$,
that is deviations of $X_n$ at scale $O((t_n)^{1-1/m})$.
\end{example}
\bigskip
