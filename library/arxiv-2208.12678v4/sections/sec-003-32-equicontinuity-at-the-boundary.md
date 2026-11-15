---
doc_id: arxiv-2208.12678v4
doc_title: "STATIONARY CURVES UNDER THE MÖBIUS-PLATEAU ENERGY"
section_id: sec-003-32-equicontinuity-at-the-boundary
section_title: "Equicontinuity at the Boundary"
section_number: 3.2
pages: 4-5
source_pdf: 2208.12678v4.pdf
source_sha256: 406d36ff4968091d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.95
doc_brief: "STATIONARY CURVES UNDER THE MÖBIUS-PLATEAU ENERGY — Plateau problems with elastic boundary energies have been of recent theoretical and applied interest."
---
We first prove the following simple lemma,
\begin{lemma}\label{lemma:diameter-convergence}
    Suppose $\left\{\mu_k:[a,b]\rightarrow\RR^3\right\}$ is a sequence of continuous curves that converges uniformly to $\mu_\infty$. Then the diameters of the images converge: $\mathrm{diam}(\mu_k([a,b]))\rightarrow\mathrm{diam}(\mu_\infty([a,b]))$.
\end{lemma}
\begin{proof}
    Let $\varepsilon>0$ and choose $N$ large such that $\norm{\mu_k-\mu_\infty}_{C^0}<\frac{\varepsilon}{2}$ for $k>N$. Let $x,y\in[a,b]$ such that $\abs{\mu_\infty(x)-\mu_\infty(y)}=\mathrm{diam}(\mu_\infty([a,b]))$. From uniform convergence we have, for any $s,t\in[a,b]$ and $k > N$,
    \begin{align*}
        \abs{\mu_k(s)-\mu_\infty(s)},~\abs{\mu_k(t)-\mu_\infty(t)}<\frac{\varepsilon}{2}.
    \end{align*}
    We have the following lower-bound for $\mathrm{diam}(\mu_k([a,b]))$,
    \begin{align*}
        \mathrm{diam}(\mu_\infty([a,b]))&=\abs{\mu_\infty(x)-\mu_\infty(y)}\\
        &\leq\abs{\mu_\infty(x)-\mu_k(x)}+\abs{\mu_k(x)-\mu_k(y)}+\abs{\mu_k(y)-\mu_\infty(y)}\\
        &\leq\mathrm{diam}(\mu_k([a,b]))+\varepsilon.
    \end{align*}
    Let $s,t\in[a,b]$, then we have
    \begin{align*}
        \abs{\mu_k(s)-\mu_k(t)}&\leq \abs{\mu_k(s)-\mu_\infty(s)}+\abs{\mu_\infty(s)-\mu_\infty(t)}+\abs{\mu_\infty(t)-\mu_k(t)}\\
        &\leq \mathrm{diam}(\mu_\infty([a,b]))+\varepsilon.
    \end{align*}
    Taking a $\max$ over $s,t$ in the above inequality yields
    \begin{align*}
        \mathrm{diam}(\mu_k([a,b]))\leq \mathrm{diam}(\mu_\infty([a,b]))+\varepsilon.
    \end{align*}
\end{proof}

We also state the Courant-Lebesgue lemma which is essential for proving equicontinuity of our maps at the boundary. First, for $p\in \bar D$ and $\rho>0$, we define the circles
\begin{align*}
    C_\rho (p) = \{q\in\bar D:~\abs{p-q}=\rho\}.
\end{align*}

\begin{lemma}[Courant-Lebesgue]\label{lemma:courant-lebesgue}
    Let $u:D\rightarrow\RR^3$ with $u\in C^0(\bar D)\cap W^{1,2}(D)$ where $\mathrm{e}(u)\leq K/2$ for some $K>0$. Then, for all $0 < \delta \ll 1$, there exist $\rho\in[\delta,\sqrt{\delta}]$ such that for all $p\in\bar D$,
    \begin{align*}
        \left[\mathrm{diam}(u(C_\rho(p)))\right]^2\leq\frac{8\pi^2 K}{-\log\delta}.
    \end{align*}
\end{lemma}
\begin{proof}
    See~\cite{colding2011course} Lemma 4.11.
\end{proof}

For the rest of this section, fix three distinct points $p_1,p_2,p_3\in\partial D$. For each $k$, we can find a unique conformal diffeomorphism $\phi_k:D\rightarrow D$ such that
\begin{align}\label{eqn:gauge-fixing}
    u_k\circ\phi_k(p_i)=\gamma_k(p_i)\text{ for }i=1,2,3.
\end{align}

\begin{proposition}\label{prop:equicontinuity}
    The maps $\tilde u_k:=u_k\circ\phi_k$ are equicontinuous on $\partial D$.
\end{proposition}
\begin{proof}
    Since $\{\tilde u_k\}$ is a minimizing sequence (and $\mathrm{e}[\cdot]$ is conformally invariant), we can assume that $\mathrm{e}(\tilde u_k)\leq K/2$ for some $K>0$. Let $\varepsilon>0$ and without loss of generality assume that
    \begin{align*}
        \varepsilon<\liminf_{k \to \infty}\left(\min_{i\neq j}\abs{\gamma_k(p_i)-\gamma_k(p_j)}\right),
    \end{align*}
    which exists since the $\gamma_k$ are all simple closed curves, along with $\gamma_\infty$. Since $\gamma_\infty$ is simple, closed and has finite arc-length, there is some $d_0>0$ such that for $p,q\in\partial D$ with $0<\abs{\gamma_\infty(p)-\gamma_\infty(q)}<d_0$, $\gamma_\infty(\partial D)\setminus\{p,q\}$ has exactly one component with diameter, $\mathrm{diam}_\infty\leq\frac{\varepsilon}{2}$~\cite[Proof of Lemma 4.14]{colding2011course}. Call the closure of this component $\Gamma$. Let $N>0$ such that $\norm{\gamma_k-\gamma_\infty}_{C^0}<\frac{\varepsilon}{4}$ for $k>N$. Then, from Lemma~\ref{lemma:diameter-convergence}, the sub-arc of $\gamma_k(\partial D)$ parametrized by the same part of $\partial D$ that parametrizes $\Gamma$ has diameter (denoted $\mathrm{diam}_k$) $\frac{\varepsilon}{2}$-close to the diameter of $\Gamma$, i.e. $\abs{\mathrm{diam}_k-\mathrm{diam}_\infty}<\frac\varepsilon 2$. Thus, $\mathrm{diam}_k<\varepsilon$. It follows that $\abs{\gamma_k(p)-\gamma_k(q)}<\frac{\varepsilon}{2}+d_0$. Henceforth, write $d:=\frac{\varepsilon}{2}+d_0$ and let $k>N$.
    
    Take $\delta<1$ small enough such that $\frac{8\pi^2 K}{-\log\delta}<d^2$ and not more than one of the $p_i$'s is in $B(p,\sqrt{\delta})$. Given any $p\in\partial D$, from Lemma~\ref{lemma:courant-lebesgue}, there exists $\rho\in[\delta,\sqrt{\delta}]$ such that
    \begin{align*}
        \textrm{diam}(\tilde u_k(C_\rho(p)))^2<\frac{8\pi^2 K}{-\log\delta}<d^2.
    \end{align*}
    In other words, $\textrm{diam}(\tilde u_k(C_\rho(p)))<d$. $C_\rho(p)$ divides $\partial D$ into two components, $A_1$ and $A_2$. Without loss of generality, let $A_1$ be the component that contains fewer than two of $p_1,p_2,p_3$. 
    
    Denote the images, $G_1= u(A_1)$ and $G_2= u(A_2)$. Due to monotonicity, $G_1$ will also contain fewer than two of $\gamma_k(p_1),\gamma_k(p_2),\gamma_k(p_3)$. Since $\textrm{diam}(\tilde u_k(C_\rho(p)))<d$, from Lemma~\ref{lemma:courant-lebesgue}, $\mathrm{diam}(G_i)<\varepsilon$ for at least one of $i=1,2$. However, from the chosen value of $\varepsilon$, this component cannot contain more than one of $\gamma_k(p_1),\gamma_k(p_2),$ or $\gamma_k(p_3)$. Thus, the component has to be $G_1$. 
    
    In conclusion, we have shown that there is $\rho>0$ such that $\abs{p-q}<\rho$ implies $\abs{\gamma_k(p)-\gamma_k(q)}<\varepsilon$.
\end{proof}
