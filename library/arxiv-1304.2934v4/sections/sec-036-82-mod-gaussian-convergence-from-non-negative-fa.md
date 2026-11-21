---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-036-82-mod-gaussian-convergence-from-non-negative-fa
section_title: "Mod-Gaussian convergence from non-negative factorizations"
section_number: 8.2
pages: 64-67
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.962
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
We will prove the following statement, which is stronger than what was announced.
\begin{theorem}
Let $(X_n)_{n \in \N}$ be a sequence of bounded random variables with non-negative integer values, with mean $\mu_n$, variance $\sigma_n^2$ and third cumulant $L_n^3$. Suppose that the probability generating function $P_n(t)$ of $X_n$ can be factorized as
\begin{equation}
    P_n(t) = \prod_{1 \le j \le k_n} P_{n,j}(t), 
    \label{eq:factorizationPGF}
\end{equation}
where \vspace{2mm}    
\begin{itemize}
    \item $(k_n)_{n \in \N}$ is a sequence of positive integers;\vspace{2mm}
    \item each $P_{n,j}$ is a polynomial with non-negative coefficients;\vspace{2mm}
    \item we assume $L_n=o(\sigma_n)$ and $M_n=o((L_n)^2/\sigma_n)$, where $M_n=\max_{1 \le j \le k_n} \deg(P_{n,j})$.\vspace{2mm}
\end{itemize}
Then, the sequence 
\[\widetilde{X_n}=\frac{X_n - \mu_n}{L_n}\]
converges in the mod-Gaussian sense with limiting function $\psi=\exp(z^3/6)$ and parameters $t_n=\sigma_n^2/L_n^2$.
The convergence takes place of the whole complex plane, with speed of convergence $O(M_n/|L_n|)$.
\label{thm:modgaussianfromzeros}
\end{theorem}

\noindent Notice that under the hypotheses of Theorem \ref{thm:modgaussianfromzeros}, $M_n = o(|L_n|)$: indeed,
$$M_n \ll \frac{(L_n)^2}{\sigma_n} = |L_n|\, \frac{|L_n|}{\sigma_n} \ll |L_n| $$
since $L_n  = o(\sigma_n)$. On the other hand, in the case where $P_n$ has only real negative roots $-r_{n,j}$, then 
\[P_n(t)= C \prod_{1 \le j \le n} (t+r_{n,j}).\] Therefore, we can then apply the above theorem with $k_n=n$ and $M_n=1$. Besides, our theorem also contains mod-Gaussian convergence of a sum of i.i.d. bounded variables with a non-zero third cumulant (see Example \ref{ex:sumiid}).

\begin{proof}
Since $P_n(1)= \prod_{1 \le j \le k_n} P_{n,j}(1)=1$, we have
    \[P_n(t) = \prod_{1 \le j \le k_n} \frac{P_{n,j}(t)}{P_{n,j}(1)}. \]
Therefore, we can assume without loss of generality that $P_{n,j}(1)=1$ (otherwise replace $P_{n,j}(t)$ by $P_{n,j}(t)/P_{n,j}(1)$). Since $P_{n,j}(t)$ has non-negative coefficients, $P_{n,j}(t)$ is the probability generating function of a variable $X_{n,j}$ (for $1 \le j \le k_n$), defined by $\proba[X_{n,j}=k]=[t^k] P_{n,j}(t)$.
\bigskip

The factorization \eqref{eq:factorizationPGF} implies that $X_n$ can be represented as the sum of independent copies of the variables $X_{n,j}$. In particular, 
\begin{align*}
\mu_n&=\sum_{1 \le j \le k_n} \mu_{n,j};\\
\sigma_n^2&=\sum_{1 \le j \le k_n} \sigma_{n,j}^2; \\
L_n^3&= \sum_{1 \le j \le k_n} L_{n,j}^3
\end{align*}
where $\mu_{n,j}$, $\sigma_{n,j}^2$ and $L_{n,j}^3$ are the three first cumulants of $X_{n,j}$. Notice that each $X_{n,j}$, and hence $|X_{n,j}-\mu_{n,j}|$ is bounded by $M_n$. We will use this repeatedly below. In particular one has: $\sigma_{n,j}^2 \le (M_n)^2$ and $|L_{n,j}^3| \le (M_n)^3$.
\bigskip

Call $\widetilde{\varphi_n}$ the Laplace transform of $\widetilde{X_n}$. We have
\[ \widetilde{\varphi_n}(z) = \esper\!\left[ \exp\left(\frac{z}{L_n}\, (X_n-\mu_n)\right) \right] = \prod_{j=1}^{k_n} \,\esper\!\left[ \exp \left(\frac{z}{L_n} (X_{n,j}-\mu_{n,j}) \right) \right]. \]
Fix $K>0$ and assume that $\frac{M_n |z| }{|L_n|} \le K$. From the Taylor expansion 
\[\E^w=1+w+\frac{w^2}{2}+\frac{w^3}{6} +O(w^4) \text{ (uniformly for $|w| \le K$),}\] 
we have that, uniformly for $\frac{M_n |z| }{|L_n|} \le K$,
 \begin{equation}
    \esper\!\left[\exp \left(\frac{z}{L_n} (X_{n,j}-\mu_{n,j}) \right) \right] = 1+\frac{\sigma_{n,j}^2\,z^2}{2\,(L_n)^2} + \frac{L_{n,j}^3\,z^3}{6\,(L_n)^3} +  O\!\left(\esper[(X_{n,j}-\mu_{n,j})^4] \left(\frac{|z|}{|L_n|}\right)^{\!4} \right).
    \label{eq:techniclaplace}
\end{equation}
Note that, since $M_n |z| /|L_n| \le K$, the two first terms are bounded. Besides, we have the following bounds:
    \begin{align*}
        \left| \left(\frac{\sigma_{n,j}^2\,z^2}{2\,(L_n)^2} \right)^2 \right| &\le \frac{\esper[(X_{n,j}-\mu_{n,j})^4]}{4} \left(\frac{|z|}{|L_n|}\right)^{\!4} ;\\
        \left| \frac{\sigma_{n,j}^2\,z^2}{2\,(L_n)^2}  \times \frac{L_{n,j}^3\,z^3}{6\,(L_n)^3} \right| & \le \frac{\esper[|X_{n,j}-\mu_{n,j}|^5]}{12} \left(\frac{|z|}{|L_n|}\right)^{\!5} \\
        &\le \frac{\esper[(X_{n,j}-\mu_{n,j})^4]}{12} \left(\frac{|z|}{|L_n|}\right)^{\!4}\, \frac{M_n |z|}{|L_n|};\\
        \left| \left(\frac{L_{n,j}^3\,z^3}{6\,(L_n)^3}\right)^2 \right| &\le \frac{\esper[(X_{n,j}-\mu_{n,j})^6]}{36} \left(\frac{|z|}{|L_n|}\right)^{\!6}\\
        & \le \frac{\esper[(X_{n,j}-\mu_{n,j})^4]}{36} \left(\frac{|z|}{|L_n|}\right)^{\!4} \,\left( \frac{M_n |z|}{|L_n|} \right)^2.
    \end{align*}
Taking the logarithm of Equation \eqref{eq:techniclaplace} and using $\log(1+t)=t+O(t^2)$, we get, thanks to the above bounds, that
$$\log \esper\!\left[ \exp \left(\frac{z}{L_n} (X_{n,j}-\mu_{n,j}) \right) \right] = \frac{\sigma_{n,j}^2\,z^2}{2\,(L_n)^2} + \frac{L_{n,j}^3\,z^3}{6\,(L_n)^3} +  O\!\left(\esper[(X_{n,j}-\mu_{n,j})^4] \left(\frac{|z|}{|L_n|}\right)^{\!4} \right).$$
Summing these identities, we obtain
\[\log \widetilde{\varphi_n}(z) = \left(\frac{\sigma_n}{L_n}\right)^2\,\frac{z^2}{2}+ \frac{z^3}{6} + O\!\left(\left(\frac{|z|}{|L_n|}\right)^{\!4} \,\sum_{j=1}^{k_n}\esper[(X_{n,j}-\mu_{n,j})^4] \right).\]
The error term can be bounded as follows:
$$\left(\frac{|z|}{|L_n|}\right)^{\!4} \,\sum_{j=1}^{k_n}\esper[(X_{n,j}-\mu_{n,j})^4] \leq \left(\frac{|z|}{|L_n|}\right)^{\!4} (M_n)^2\,\sum_{j=1}^{k_n}\esper[(X_{n,j}-\mu_{n,j})^2] \leq |z|^4\,\frac{(M_n)^2(\sigma_n)^2}{|L_n|^4}.$$
By the assumption made on $M_n$, this is a $o(|z|^4)$. Finally, we get
\[\log \widetilde{\varphi_n}(z) = \left(\frac{\sigma_n}{L_n}\right)^2\,\frac{z^2}{2} + \frac{z^3}{6} + o(|z|^4),\]
which can be rewritten as
\[ \widetilde{\varphi_n}(z)\, \E^{-\left(\frac{\sigma_n}{L_n}\right)^2\,\frac{z^2}{2}} = \exp\left(\frac{z^3}{6}\right)\, \big(1+o(|z|^4)\big), \]
this being uniform for $M_n |z| /|L_n| \le K$, thus on compacts of $\C$. This ends the proof of the theorem.
\end{proof}

\begin{remark}
Suppose for instance that $M_n=1$, \emph{i.e.}, the probability generating function of $X_n$ has non-negative real roots. Then, the conditions on the first cumulants of $X_n$ in order to apply Theorem \ref{thm:modgaussianfromzeros} are
$$\sqrt{\sigma_n} \ll L_n \ll \sigma_n,$$
which are usually easy to check.
\end{remark}
\bigskip
