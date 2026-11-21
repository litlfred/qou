---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-030-72-additive-arithmetic-functions-of-random-integ
section_title: "Additive arithmetic functions of random integers"
section_number: 7.2
pages: 50-55
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.982
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{subsec:arithmetic} In this paragraph, we sometimes write $\log(\log n) = \log_2 n$, which is negligible in comparison to $\log n$ as $n$ goes to infinity. 


\subsubsection{Number of prime divisors, counted without multiplicities}
Denote $\mathbb{P}$ the set of prime numbers, $\omega(k)$ the number of distinct prime divisors of an integer $k$, and $\omega_{n}$ the random variable $\omega(k)$ with $k$ random integer uniformly chosen in $[n]:=\{1,2,\ldots,n\}$. The random variable $\omega_{n}$ satisfies the Erd\"os-Kac central limit theorem (\emph{cf.} \cite{EK40}):
$$\frac{\omega_{n}-\log\log n}{\sqrt{\log\log n}} \to \mathcal{N}_{\R}(0,1).$$ 
In this section, we show that $\omega_{n}$ converges mod-Poisson and present precise deviation results for it. Such a result was established in \cite[Section 4]{KN10}. But in the latter article, mod-$\phi$ convergence is defined via convergence of the renormalized Fourier transform, while here we work with Laplace transform. Therefore, we need to justify that the convergence also holds for Laplace transforms.
\bigskip

We start from the {\em Dirichlet series} of $y^{\omega(k)}$, which is:
\[\sum_{k \ge 1} \frac{y^{\omega(k)}}{k^s} = \prod_{p \in \mathbb{P}} \left( 1 + \frac{y}{p^s-1} \right),\]
well-defined and absolutely convergent if $\Re(s)>1$. The Selberg-Delange method allows to extract from this formula precise estimates for the generating function of $\omega_{n}$; see \cite{Ten95} and references therein.

\begin{proposition}\cite[Section II.6, Theorem 1]{Ten95}
For any $A >0$, we have, for any $y$ in $\C$ with $|y| \le A$
\[ \sum_{k \le n} y^{\omega(k)} = n\, (\log n)^{y-1} \, (\lambda_0(y) +O(1/\log n)), \]
where
\[\lambda_0(y)= \frac{1}{\Gamma(y)} \, \prod_{p \in \mathbb{P}} \left( 1 + \frac{y}{p-1} \right)\left( 1- \frac{1}{p} \right)^y \]
and the constant hidden in the $O$ symbol depends only on $A$.
\label{prop:selbergdelange_omega}
\end{proposition}

\begin{remark}
In fact, \cite[Section II.6, Theorem 1]{Ten95} gives a complete asymptotic expansion of $\sum_{k \le n} y^{\omega(k)}$ in terms of powers of $1/\log(n)$. For our purpose, the first term is enough: we will see that it implies mod-Poisson convergence with a speed of convergence as precise as wanted.
\end{remark}
\bigskip

Setting $y=\E^z$, this can be rewritten as an asymptotic formula for the Laplace transform of $\omega_{n}$.
\begin{align*}
\esper[\E^{z\,\omega_{n}}] &= \frac{1}{n} \sum_{k=1}^n \E^{z\,\omega(k)} 
= (\log n)^{\E^z-1} \lambda_0(\E^z) \,(1+ O(1/\log n))\\
&= \E^{(\E^z-1) \log \log n}\, \lambda_0(\E^z) \,(1+ O(1/\log n)).
\end{align*}
Recall that the constant in the $O$ symbol is uniform on sets $\{w, |w| \le A\}$, that is on bands $\{z,\, \Re(z) \le \log(A)\}$. In particular the convergence is uniform on compact sets. Therefore, one has the following result.

\begin{proposition}
    The sequence of random variables $(\omega_n)_{ n \ge 1}$ converges mod-Poisson with parameter $t_n=\log_2 n$ and limiting function $\psi(z)=\lambda_0(\E^z)$ on the whole complex plane. This takes place with speed of convergence $O(1/\log n)$, that is $O((t_n)^{-\nu})$ for all $\nu >0$.
\end{proposition}

Using Theorem \ref{thm:mainlattice}, we get immediately the following deviation result.
\begin{theorem}
    Let $x>0$. Assume $x \log_2 n \in \N$. Then
    \begin{equation}
        \proba[\omega_n=x \log_2 n] =
        \frac{ \lambda_0(x)\,\,(1 +O(1/\log_2 n))}{(\log n)^{x \log(x)-x+1} \sqrt{2 \pi x\, \log_2 n}}.
    \label{eq:LLL_omega}
\end{equation}
    Furthermore, if $x>1$, then
    \begin{equation}
        \proba[\omega_n \ge x \log_2 n] =
        \frac{ \lambda_0(x)\,\,(1 +O(1/\log_2 n ))}{(\log n)^{x \log(x)-x+1} \sqrt{2 \pi x\, \log_2 n }} \,\frac{1}{1-\frac{1}{x}}.
    \label{eq:deviations_omega}
\end{equation}
\end{theorem}

\begin{remark}
The first equation \eqref{eq:LLL_omega} is not new: it is due to Selberg \cite{Selberg54} and presented in a slightly different form than here in \cite[Section II.6, Theorem 4]{Ten95}. Note also that, as the speed of mod-Poisson convergence of $\omega_n$ is $O\big(\big(t_n\big)^{-\nu}\big)$ for all $\nu >0$, Theorem \ref{thm:mainlattice} gives asymptotic expansions of the above probabilities, up to an arbitrarily large power of $1/\log\log n$. Theorem 4 in \cite[Section II.6]{Ten95} also gives such estimates. The second statement \eqref{eq:deviations_omega} follows from \cite[Theorem 2.8]{Rad09}; it is a nice feature of the theory of mod-$\phi$ convergence to allow to recover quickly such deep arithmetic results (though we still need Selberg-Delange asymptotics).
\end{remark}
\bigskip



\subsubsection{Number of prime divisors, counted with multiplicities}
In this section, we give similar results for the number of prime divisors $\Omega_n$ of a random integer in $\{1,2,\ldots,n\}$, {\em counted with multiplicities}. An important difference is that, here, the mod-Poisson convergence occurs only on a band and not on the whole complex plane $\C$. In this case the Dirichlet series is given by:
\[\sum_{k \ge 1} \frac{y^{\Omega(k)}}{k^s} = \prod_{p \in \mathbb{P}} \left( 1 - \frac{y}{p^s} \right)^{\!-1},\]
which again is well-defined and absolutely convergent for $\Re (s)>1$. Note that, unlike in the case of $\omega(k)$, the right-hand side has some pole, the smallest in modulus being for $y=2^s$. Again, a precise estimate for the generating function follows from the work of Selberg and Delange; see \cite{Ten95} and references therein.

\begin{proposition}\cite[Section II.6, Theorem 2]{Ten95}
For any $\delta$ with $0<\delta<1$, we have, for any $y$ in $\C$ with $|y| \le 2-\delta$
\[ \sum_{k \le n} y^{\Omega(k)} = n\, (\log n)^{y-1} \, (\nu_0(y) +O(1/\log n)), \]
where
\[\nu_0(y)= \frac{1}{\Gamma(y)} \, \prod_{p \in \mathbb{P}} \left(1 - \frac{y}{p} \right)^{-1}\left( 1- \frac{1}{p} \right)^y \]
and the constant hidden in the $O$ symbol depends only on $\delta$.
\label{prop:selbergdelange_Omega}
\end{proposition}

\noindent Note the difference with Proposition \ref{prop:selbergdelange_omega}: the function $\nu_0$ has a simple pole for $y=2$ (while $\lambda_0$ is an entire function) and the estimate in Proposition \ref{prop:selbergdelange_Omega} holds (uniformly on compacts) {\em only for $|y| < 2$}.\bigskip

Setting again $y=\E^z$, this can be rewritten as an asymptotic formula for the Laplace transform of $\Omega_{n}$
 on the band $\mathcal{S}_{(-\infty,\log 2)}=\{z, \, \Re(z) < \log 2\}$.
\[
    \esper[\E^{z\,\Omega_{n}}] = \frac{1}{n} \sum_{k=1}^n \E^{z\,\Omega(k)} 
= \E^{(\E^z-1) \log \log n}\, \nu_0(\E^z) \,(1+ O(1/\log n)).
\]
Recall that the constant in the $O$ symbol is uniform on sets $\{y, |y| \le 2-\delta\}$, that is on bands $\{z,\, \Re(z) < \log(2-\delta)\}$. In particular the convergence is uniform on compact sets. Therefore, one has the following result.
\begin{proposition}
The sequence of random variables $(\Omega_n)_{ n \ge 1}$ converges mod-Poisson with parameter $t_n=\log_2 n$ and limiting function $\psi(z)=\nu_0(\E^z)$, on the band $\mathcal{S}_{(-\infty,\log 2)}$. This takes place with speed of convergence $O(1/\log(n))$, that is $O((t_n)^{-\nu})$, for all $\nu >0$.
\end{proposition}
\bigskip

As for $\omega_n$, this implies precise deviation results. However, as the convergence only takes place on a band,
the range of these results is limited (note the condition $x<2$ in the theorem below).
\begin{theorem}
    Fix $x$ with $0<x<2$. Assume $x \log_2 n \in \N$. Then
    \begin{equation}
        \proba[\Omega_n=x \log_2 n] =
        \frac{ \nu_0(x)\,\,(1 +O(1/\log_2 n))}{(\log n)^{x \log(x)-x+1} \sqrt{2 \pi x \,\log_2 n}}.
    \label{eq:LLL_Omega}
\end{equation}
    Furthermore, if $1<x<2$,
    \begin{equation}
        \proba[\Omega_n \ge x \log_2 n ] =
        \frac{ \nu_0(x)\,\,(1 +O(1/\log_2 n))}{(\log n )^{x \log(x)-x+1} \sqrt{2 \pi x \,\log_2 n}}\, \frac{1}{1-\frac{1}{x}}.
    \label{eq:deviations_Omega}
\end{equation}
\end{theorem}
\noindent Again, the fist equation was discovered by Selberg \cite{Selberg54} and can be found in a slightly different form in \cite[Section II.6, Theorem 5]{Ten95}.

\begin{remark}
An extension of Equation \eqref{eq:LLL_Omega} for $x>2$ is given in \cite[Section II.6, Theorem 6]{Ten95}. This involves the type of singularity of the limiting function $\nu_0(\E^z)$ at the edge of the convergence domain. Here, $\nu_0(y)$ has only a simple pole in $y=2$, and the residue appears in the deviation results. It would be interesting to see if this kind of idea can be used in the general framework of mod-$\phi$ convergence, but this is outside the scope of this already quite long paper.
\end{remark}
\bigskip



\subsubsection{Other arithmetic functions}
In this paragraph, we generalize the two examples $\omega_n$ and $\Omega_n$ above. The goal is to understand the phase transition between the convergence on a band and the convergence on the complex plane.
\medskip

Let $f: \N \to \Z$ be a function with the following properties:\vspace{2mm}
\begin{enumerate}[(i)]
\item\label{hyp:additivefunction1} $f$ is additive, that is $f(mn)=f(m)+f(n)$ if $m \wedge n =1$;\vspace{2mm}
\item\label{hyp:additivefunction2} for every prime $p$, one has $f(p)=1$.\vspace{2mm}
\end{enumerate}
We necessarily have $f(1)=0$. For $C>0$, we say that such a function {\em has a $C$-linear growth} if there exists $B$ such that
$$|f(p^k)| \le B+C\, k \quad\text{for any }p\in \mathbb{P} \text{ and any }k>0.$$
If $f$ has a $C$-linear growth for any $C>0$, we say that $f$ has a {\em sublinear growth}. In particular, since $\Omega(p^k)=k$ (for all $p$ and $k$), the function $\Omega$ has a $1$-linear growth, while $\omega$ has a sublinear growth (for all $p$ and $k$, $\omega(p^k)=1$). We are interested in the random variable $f_n$, which is equal to the value $f(k)$ of $f$ on a random integer $k$ chosen uniformly between $1$ and $n$. Note that the additivity condition ensures that the following Dirichlet series factorizes:
\[F(y,s):= \sum_{k=1}^\infty \frac{y^{f(k)}}{k^s} = \prod_{p\in \mathbb{P}} \left( 1+\frac{y^{f(p)}}{p^s}+\frac{y^{f(p^2)}}{p^{2s}}+\cdots \right). \]
Again, one can use the Selberg-Delange method to get precise estimates for the Laplace transform.
\begin{proposition}
\label{prop:selbergdelange_general}
Suppose that $f$ fulfills \eqref{hyp:additivefunction1} and \eqref{hyp:additivefunction2} and has a $C$-linear groth for some $C>0$. For any $\delta$ with $0<\delta<\frac{1}{2}$, we have, for any $y$ in $\C$ with $(2-2\delta)^{-1/C} \le |y| \le (2-2\delta)^{1/C}$,
\begin{equation}
 \sum_{k \le n} y^{f(k)} = n\, (\log n)^{y-1} \, (\tau_0(y) +O(1/\log n)),
\label{eq:asymptotics_generaladditivefunction}
\end{equation}
where the constant hidden in the $O$ symbol depends on $\delta$, $B$ and $C$ (but not on $y$), and
\[\tau_0(y)= \frac{1}{\Gamma(y)} \, \prod_{p \in \mathbb{P}}
\left( 1 + \frac{y^{f(p)}}{p}+\frac{y^{f(p^2)}}{p^2} + \cdots \right)\left( 1- \frac{1}{p} \right)^y. \]
\end{proposition}

\begin{proof}
The proof is an easy adaptation of the proof of \cite[Section II.6, Theorems 1 and 2]{Ten95}. We will only indicate the necessary modifications, assuming that the reader can consult Tenenbaum's book.\medskip

Fix $\delta\in(0,\frac{1}{2})$, and $y$ in $\C$ with $(2-2\delta)^{-1/C} \le |y| \le (2-2\delta)^{1/C}$. We set $Y = \max(|y|,|y|^{-1})$; by assumption, $1\leq Y\leq (2-2\delta)^{1/C}$, and on the other hand,
$$|y^{f(p^k)}| \leq Y^{B+Ck}
$$
as $f$ has a $C$-linear growth. We have, for any prime $p$ and $|\xi|<Y^{-C}$, the bound
\[\sum_{k \ge 0} |y^{f(p^k)}\, \xi^k| < 1+\sum_{k \ge 1} Y^{B+Ck} |\xi|^k \leq 1+ Y^B \frac{Y^C |\xi|}{1-Y^C |\xi|}.
\]
Therefore, for each prime $p$, the following formula defines a holomorphic function for $|\xi|<Y^{-C}\leq 1$:
\[h_{y,p}(\xi)= \left( 1+ y^{f(p)} \xi+ y^{f(p^2)} \xi^2 +\dots \right) \left( 1- \xi \right)^y. \]
Moreover, we have
\[|h_{y,p}(\xi)| < \left(1+ Y^B \frac{Y^C |\xi|}{1-Y^C |\xi|} \right)\,\E^{Y\,|\log(1-\xi)|}.\]
Consider now the coefficients of the power series expansion of $h_{y,p}$ around the origin,
{\em i.e.} the numbers $b_y(p^k)$ such that
\[h_{y,p}(\xi)= 1 + \sum_{k \ge 1} b_y(p^k) \xi^k.\]
Note that $b_y(p)=0$ for any $p \in \mathbb{P}$. With the previous hypotheses, 
$$\frac{1}{2-\delta}< Y^{-C}\leq |y|^{-C}.$$
By Cauchy's formula applied to the circle of radius $1/(2-\delta)$, one has, for any prime $p$, any complex number $y$ such that $(2-2\delta)^{1/C}\le |y| \le (2-2\delta)^{1/C}$, and any $k \ge 1$:
\[ |b_w(p^k)| \le M(\delta,B,C)\, (2-\delta)^k, \]
where 
\[M(\delta,B,C) = \sup_{\substack{|\xi| = 1/(2-\delta) \\  1 \leq Y \leq  (2-2\delta)^{1/C} }}
\left(1+ Y^B \frac{Y^C |\xi|}{1-Y^C |\xi|} \right)\,\E^{Y\,|\log(1-\xi)|} < +\infty. \]

Denote $\zeta$ is the Riemann zeta function. The same arguments as in the proof of \cite[Section II.6, Theorem 1]{Ten95} shows that
\[G(y,s):=F(y,s)\, \zeta(s)^{-y} = \prod_{p \in \mathbb{P}} \left (1 + \sum_{k \ge 2} \frac{b_y(p^k)}{p^{ks}} \right)\]
is convergent and uniformly bounded for $\Re(s)>3/4$ and $y $ such that $(2-2\delta)^{-1/C}\le |y| \le (2-2\delta)^{1/C}$.
Therefore, we can apply \cite[Section II.5, Theorem 3]{Ten95}, which gives the asymptotic formula \eqref{eq:asymptotics_generaladditivefunction}.












\end{proof}

Setting $y=\E^z$, Proposition \ref{prop:selbergdelange_general} can be rewritten as an asymptotic formula for the Laplace transform of $f_{n}$:
\[
    \esper[\E^{z\,f_{n}}] = \frac{1}{n} \sum_{k=1}^n \E^{z\,f(k)} 
= \E^{(\E^z-1) \log \log n)} \,(\tau_0(\E^z) + O(1/\log n)),
\]
where the constant hidden in $O$ depends on $\delta$, $B$ and $C$, but is uniform on $|\Re(z)| \le (\log(2-2\delta))/C$. This yields the following mod-convergence result:

\begin{proposition}
Assume $f$ is an arithmetic function that fulfills \eqref{hyp:additivefunction1} and \eqref{hyp:additivefunction2} and has a $C$-linear growth for some constant $C>0$. Then, the sequence of random variables $(f_n)_{ n \ge 1}$
converges mod-Poisson with parameter $t_n=\log_2 n$ and limiting function $\psi(z)=\tau_0(\E^z)$ on the band $$\mathcal{S}_{(-\frac{\log 2}{C},\frac{\log 2}{C})}.$$ 
This takes place with speed of convergence $O(1/\log n)$, that is $O((t_n)^{-\nu})$ for all $\nu >0$.
\medskip

\noindent As a consequence, if $f$ has a sublinear growth, then the convergence takes place on the whole complex plane.
\end{proposition}

\noindent It is then straightforward to write deviation results, analog to Equations \eqref{eq:deviations_omega} and \eqref{eq:deviations_Omega}, for a generic function $f$ as above.
\medskip

\begin{remark}
If the additive function $f$ is non-negative, as is the case for $\omega(n)$ and $\Omega(n)$, then it is easily seen that one can perform the whole proof of Proposition \ref{prop:selbergdelange_general} assuming only $|y| \leq (2-2\delta)^{1/C}$ (but not $|y| \geq (2-2\delta)^{-1/C}$). Therefore, one has in this case a mod-Poisson convergence on the band $$\mathcal{S}_{(-\infty,\frac{\log 2}{C})}\quad \text{instead of}\quad \mathcal{S}_{(-\frac{\log 2}{C},\frac{\log 2}{C})}.$$
\end{remark}
\bigskip
