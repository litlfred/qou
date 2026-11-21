---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-006-22-stochastic-localization
section_title: "Stochastic localization"
section_number: 2.2
pages: 7-9
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.976
doc_brief: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube — It is well-known that measures whose density is the form e−V where V is a uniformly convex potential on Rn attain"
---
\label{sec:stochastic}
We construct a stochastic process driven by a Brownian motion, which we refer to as \emph{stochastic localization}. A somewhat similar process was originally used in \cite{Eldan-thin-KLS} to establish concentration properties for log-concave measures on $\RR^n$. Here we use a discrete version, similar to the construction which appears in \cite{Eldan-taming, eldan2020spectral}. In this section we occasionally allow ourselves to omit some of the details of the proofs, and the reader is referred to \cite{Eldan-taming} for more rigorous derivations. \\

Let $B_t$ be a standard Brownian motion on $\RR^n$ adapted to a filtration $\FF_t$. Consider the system of equations,
\begin{equation}\label{eq:localization}
F_0(x) = 0, ~~ d F_t (x) = F_t(x) \langle x - a_t,  d B_t \rangle, ~~ \forall x \in \DC,
\end{equation}
where $a_t := \int x d \nu_t(x) := \int x F_t(x) d \nu(x)$. \\

We think of this process $(\nu_t)_t$ as an evolution of measures on $\DC$, which starts with the measure $\nu_0 = \nu$, and as seen below, ends up with a Dirac measure whose support is $\nu$-distributed. Let us first summarize some useful properties of this process.
\begin{proposition} \label{prop:basicprops}
The process defined above satisfies the following properties.
\begin{enumerate}
\item 
Almost surely, for all $t$, $\nu_t$ is a probability measure.
\item
For all $A \subset \DC$, the process $\nu_t(A)$ is a martingale.
\item 
The process $a_t$ almost surely converges to a point in $\DC$, and $a_\infty := \lim_{t \to \infty} a_t$ is distributed according to the law $\nu$. Moreover, the measure $\nu_t$ almost-surely weakly converges to a Dirac measure at $a_\infty$.
\end{enumerate}
\end{proposition}
\begin{proof}
We have
$$
d \nu_t(\DC) = d \int_{\DC} F_t(x) \nu(x) = \int_{\DC} (x - a_t) d \nu_t(x) d B_t = 0,
$$
which proves the first part. The second part is evident from the definition. For the third part, a calculation gives,
\begin{align}
da_t ~& = d \int_{\DC} x \nu_t(x)  \nonumber \\
& = \left (\int_{\DC} x \otimes (x - a_t)\nu_t(dx) \right ) dB_t \nonumber \\
& = \left (\int_{\RR^d} (x - a_t)^{\otimes 2} \nu_t(dx) \right ) dB_t \nonumber \\ 
& = \COV(\nu_t) dB_t. \label{eq:dat}
\end{align}
Therefore, $a_t$ is a martingale, and 
\begin{equation}\label{eq:atfast}
d [\langle a_t, e_i \rangle]_t = \sum_{j \in [n]} \COV(\nu_t)_{i,j}^2 \geq \COV(\nu_t)_{i,i}^2 = (1 - \langle a_t, e_i \rangle^2)^2 dt,
\end{equation}
implying that $\langle a_t, e_i \rangle$ converges to $\{\pm 1\}$ almost surely and that $\nu_t$ converges weakly to to $\delta_{a_\infty}$, which also implies that
$$
\lim_{t \to \infty} a_t \in A \Leftrightarrow \lim_{t \to \infty} \nu_t(A) = 1,
$$
for all $A \subset \DC$. Since $\nu_t(A)$ is a martingale, we have that 
$$
\PP \left ( \lim_{t \to \infty} a_t \in A \right ) = \lim_{t \to \infty} \EE \nu_t(A) = \nu(A),
$$
implying the third part.
\end{proof}

Next, we have by It\^o's formula, for all $x \in \DC$,
\begin{align}
d \log F_t(x) & = \frac{d F_t(x)}{F_t(x)} - \frac{d[F(x)]_t}{2 F_t(x)^2} \nonumber \\
& = \langle x-a_t, d B_t \rangle - \frac{1}{2}  |x-a_t|^2 dt \nonumber \\
& = \langle x, d B_t + a_t dt \rangle + d Z_t
\end{align}
where $Z_t$ is an It\^o process that does not depend on $x$ (here we used the fact that $|x|^2$ is constant on $\DC$). Therefore,
$$
\log F_t(x) = \left \langle x, w_t  \right \rangle + c_t
$$
where $c_t$ is some It\^o process and $w_t = B_t + \int_0^t a_s ds$. The above display and the fact that $\nu_t$ is a probability measure, implies that
\begin{equation}\label{eq:tilts}
\nu_t = \tau_{w_t} \nu,
\end{equation}
and therefore also 
$$
a_t = \int_{\DC} x d \nu_t(x) = \int_{\DC} x d \tau_{w_t} \nu(x) = a_\nu(w_t).
$$ 
The process $w_t$ thus satisfies the equation
\begin{equation}\label{eq:dvt}
w_0 = 0, ~~ d w_t = d B_t + a_\nu(w_t) dt.
\end{equation}
The above equation gives an alternative construction for the process defined in \eqref{eq:localization}. Due to the Markov property of the measure-valued process $\nu_t$, the above discussion leads to the following result.
\begin{proposition} \label{prop:alt}
Given a measure $\nu$ and a vector $v \in \RR^n$, consider the process defined by the equation
$$
u_0 = v, ~~~ d u_t = d B_t + a_\nu(u_t) dt.
$$
Then $X = \lim_{t \to \infty} a_\nu(u_t)$ exists and is a point in $\DC$ almost surely, and has the law $\tau_{v} \nu$. 
\end{proposition}
\begin{proof}
Consider the measure $\tilde \nu = \tau_{v} \nu$ and let $w_t$ be the process constructed as above with $\nu$ replaced by $\tilde \nu$ in equation \eqref{eq:localization}. Observe that by definition 
$$
a_{\tilde \nu}(x) = a_\nu(x + v), ~~ \forall x \in \RR^n.
$$	
In light of \eqref{eq:dvt} and by the uniqueness of the solution to the above SDE, we have that $w_t + v = u_t$ almost surely, for all $t$. The result now follows from part 3 of Proposition \ref{prop:basicprops} and the fact that 
$$
a_t = a_{\tilde \nu}(w_t) = a_\nu(u_t).
$$
\end{proof}


\section{Proof of Theorem \ref{thm:main}}
