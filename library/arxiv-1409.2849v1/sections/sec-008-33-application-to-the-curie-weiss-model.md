---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-008-33-application-to-the-curie-weiss-model
section_title: "Application to the Curie-Weiss model"
section_number: 3.3
pages: 15-17
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.95
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
\label{subsec:curieweiss}
Consider i.i.d.~Bernoulli random variables $(\sigma(i))_{i \geq 1}$ with $\proba[\sigma(i)=1]=1-\proba[\sigma(i)=-1]=\frac{\E^{\alpha}}{2\,\cosh\alpha}$ for some $\alpha \in\R$. We set $U_n=\sum_{i=1}^n \sigma(i)$, so that
\begin{align*}
\esper[\E^{zU_n}]&=\left(\frac{\cosh (z+\alpha)}{\cosh \alpha}\right)^n=\left(\cosh z + \sinh z \,\tanh \alpha\right)^n \\
\esper\!\left[\E^{z\,\frac{U_n-n\,\tanh\alpha}{n^{1/3}}}\right]&=\left(\frac{\cosh (zn^{-1/3}) + \sinh (zn^{-1/3}) \,\tanh \alpha}{\E^{zn^{-1/3}\,\tanh \alpha}}\right)^n\\
\log \esper\!\left[\E^{z\,\frac{U_n-n\,\tanh\alpha}{n^{1/3}}}\right] &=\frac{n^{1/3}}{2\,\cosh^2 \alpha}\,z^2-\frac{\sinh \alpha}{3 \cosh^3 \alpha}\,z^3+o(1)
\end{align*}
so one has complex mod-Gaussian convergence of $\frac{U_n-n\tanh \alpha}{n^{1/3}}$ with parameters $\frac{n^{1/3}}{\cosh^2\alpha}$ and limiting function $\exp(-\frac{\sinh \alpha}{3\cosh^3 \alpha}\,z^3)$. \bigskip

If $\alpha=0$, then the term of order $3$ disappears in the Taylor expansion of the characteristic function, and one obtains instead
$$\log \esper\!\left[\E^{z\,\frac{U_n}{n^{1/4}}}\right] =\frac{n^{1/2}\,z^2}{2}-\frac{z^4}{12}+o(1),$$
hence a complex mod-Gaussian convergence of $X_n=\frac{U_n}{n^{1/4}}$ with parameters $n^{1/2}$ and limiting function $\exp(-z^4/12)$. Since this function restricted to $\R$ is integrable, this leads us to the following result, which originally appeared in \cite{EN78} (without the mod-Gaussian interpretation):

\begin{theorem}\label{thm:ellnew}
Let $X_n=n^{-1/4}\sum_{i=1}^n \sigma(i)$ be a rescaled sum of centred $\pm 1$ independent Bernoulli random variables. It converges in the $\mathrm{L}^1$-mod-Gaussian sense, with parameters $n^{1/2}$ and limiting function $\exp(-\frac{z^4}{12})$. As a consequence, if $Y_n=n^{-1/4}M_n$ is the rescaled magnetization of a Curie-Weiss model $\CW_{0,1}$ of parameters $\alpha=0$ and $\beta=1$, then $Y_n/n^{1/2}$ converges in law to the distribution
$$\frac{\exp(-\frac{x^4}{12})\,dx}{\int_{\R}\exp(-\frac{x^4}{12})\,dx}.$$
\end{theorem}

\begin{proof}
The function $\psi_n(t)$ is in our case 
$$\psi_n(t)=\E^{-\frac{t^2n^{1/2}}{2}}\,\left(\cosh \frac{t}{n^{1/4}}\right)^n,$$
and we have seen that it converges locally uniformly to $\psi(t)=\exp(-\frac{t^4}{12})$. By Scheffe's lemma, to obtain the $\mathrm{L}^1$-mod-convergence, it is sufficient to prove that $\int_{\R} \psi_n(t)\,dt$ converges to $\int_{\R}\exp(-\frac{t^4}{12})\,dt$. This is a simple application of Laplace's method:
\begin{align*}
\int_{\R} \psi_n(t)\,dt &= \int_{\R}\E^{-\frac{t^2n^{1/2}}{2}}\,\left(\cosh \frac{t}{n^{1/4}}\right)^n\,dt = n^{1/4}\int_{\R} \left(\E^{-\frac{u^2}{2}}\,\cosh u\right)^n\,du
\end{align*}
and the function $u \mapsto \E^{-\frac{u^2}{2}}\,\cosh u$ attains its global maximum at $u=0$, with a Taylor expansion $1-\frac{u^4}{12}+o(u^4)$, see Figure \ref{fig:functionellnew}.
\begin{center}
\begin{figure}[ht]
\includegraphics[scale=0.5]{function.pdf}
\caption{The function $f(u)=\E^{-\frac{u^2}{2}}\,\cosh u$. \label{fig:functionellnew}}
\end{figure}
\end{center}
Then, the exponential change of measure \eqref{eq:exponchange} gives a probability measure on spin configurations proportional to
$$\exp\left(\frac{(Y_n)^2}{2n^{1/2}}\right)=\exp\left(\frac{1}{2n}\,(M_n)^2\right),$$
so it is indeed the Curie-Weiss model $\CW_{0,1}$.
\end{proof}
\bigskip

It is easily seen that the proof adapts readily to the case where Bernoulli variables are replaced by so-called pure measures, so we recover all the limit theorems stated in \cite{EN78,ENR80}. However, by choosing the setting of mod-Gaussian convergence, we also obtain new limit theorems for models that do not fall in the Curie-Weiss setting. The following result explains how it would work to replace the Bernoulli distribution by more general ones; \emph{cf.} \cite[Proposition 2.2]{KNN13}. 

\begin{proposition}
Let $k\geq2$ be an integer, and let $(B_n)_{n\geq1}$ be a sequence of i.i.d random variables in $\mathrm{L}^r$ for some $r>k+1$, such that the first $k$ moments of $B_1$ are the same as the corresponding moments of the Standard Gaussian distribution. Then the sequence of random variables 
$$\left(\frac{1}{n^{1/(k+1)}} \sum_{k=1}^n B_k\right)_{n\geq1}$$
converges in the mod-Gaussian sense with parameters $$t_n=n^{(k-1)/(k+1)},$$
and limiting function $$\theta(t)=\E^{(\I t)^{k+1}\frac{c_{k+1}}{(k+1)!}},$$
where $c_{k+1}$ denotes the $(k+1)$-th cumulant of $B_1$.
\end{proposition}

When the random variables $B_n$ have an entire moment generating function, then one can replace $t$ with $-\I t$ to obtain mod-Gaussian convergence with the Laplace transforms. If $B_1$ is  symmetric, then $k$ is necessarily an 
odd number of the form $2s-1$ and hence $$\psi(t)=\E^{(-1)^s t^{2s}\frac{c_{2s}}{(2s)!}}.$$In the case of the Bernoulli random variables, $s=2$ and $c_4=-1/12$. In order to have our theorem of $\mathrm{L}^1$-mod-Gaussian convergence to hold, we need to find conditions on the distribution of $B_1$ such that $c_{2s}$ is negative and that $\int_\R \psi_n$ converges to $\int_\R \psi$. The conditions in \cite{EN78} and \cite{ENR80} precisely imply these. But within our more general framework, following the discussion in Section \ref{subsec:methjoint}, we could well imagine a situation which fulfils the assumptions of Theorem \ref{thm:mainl1} but where the initial symmetric random variables are not necessarily i.i.d but simply independent or even weakly dependent. The following paragraph yields an example of such a setting.
\medskip
