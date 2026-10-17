---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-002-12-an-application-concentration-of-negatively-de
section_title: "An application: Concentration of negatively dependent random variables"
section_number: 1.2
pages: 3-5
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.98
doc_brief: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube — It is well-known that measures whose density is the form e−V where V is a uniformly convex potential on Rn attain"
---
For a sequence of Bernoulli variables $X_1,...,X_n$, there are several notions of \emph{negative-dependence} between those variables (see e.g., \cite{BSS82,BK85,BF87,DR98}), some of which are known or conjectured to imply concentration of Lipschitz functions. Some notable first steps towards a theory unifying those notions appear in the work of Permantle \cite{pemantle04}, to which we also refer for a review of these notions.

The simplest notion of negative dependence is \textbf{pairwise negative-correlations}, hence the condition that $\EE[X_i X_j] \leq \EE X_i \EE X_j$ for all $i \neq j$. This condition, however, is too weak to imply any nontrivial concentration bounds. For example if $(X_1,...,X_n)$ are distributed as a uniformly chosen row of the $n \times n$ Hadamard matrix, then these variables are pairwise independent, and therefore have nonpositive correlations. However, if $A$ is the subset of combinations given by the first $n/2$ rows and $\varphi(x)$ is the Hamming distance of $x$ to the set $A$, then $\Var[ \varphi(X_1,\dots,X_n)] = \Omega \left (n^2 \right )$. 

A stronger notion which appears in the literature is \textbf{negative-association}: We say that $X_1,...,X_n$ are negatively associated if for all $I,J \subset [n]$ with $I \cap J = \emptyset$ and every monotone functions $f:\{0,1\}^I \to \RR$ and $g:\{0,1\}^J \to \RR$ one has $\EE [f(X_I) g(X_J)] \leq \EE f(X_I) \EE g(X_J)$. It was conjectured by E. Mossel that Lipschitz functions admit sub-Gaussian concentration with respect to such measures. 

To the best of our knowledge, there are two results in this direction in the literature: It was shown by Peres and Pemantle that sub-Gaussian concentration of Lipschitz functions hold for measures satisfying the \textbf{strong-Rayleigh} property (\cite{Peres-Pemantle}), which amounts to stability of the generating polynomial of the measure. More recently, Garbe and Vondrak (\cite{Garbe-Vondrak}) showed that concentration is implied by the \textbf{negative-regression} property. We also refer to their paper for a discussion of related bounds and questions. \\

Here, we consider the following notion of negative dependence suggested by Wagner \cite{Wa08}.
\begin{definition} (Rayleigh measures). 
We say that $X_1,\dots,X_n$ satisfy the \textbf{Rayleigh} property if for every $\theta \in \RR^n$ and for all $i,j \in [n]$, we have
\begin{equation}\label{eq:TNC}
\EE \left [X_i X_j e^{ \sum_i \theta_i X_i} \right ] \EE \left [ e^{ \sum_i \theta_i X_i} \right ] \leq \EE\left [X_i e^{ \sum_i \theta_i X_i} \right ] \EE\left [ X_j e^{ \sum_i \theta_i X_i} \right ]. 
\end{equation}
\end{definition} 

In other words, $X_1,...,X_n$ satisfies the Rayleigh property if the correlations between all pairs are negative even after reweighing the measure by an exponential tilt. Equivalently, this is the largest family that exhibits pairwise negative correlations and is closed under the operation of applying a magnetic field.\\

A corollary of our main theorem is the following concentration bound for measures with the Rayleigh property as well a lower bound for the entropy.
\begin{corollary} \label{cor:TNC}
If $X_1,...,X_n$ satisfy the Rayleigh property, then,
\begin{enumerate}
\item 
For any $1$-Hamming-Lipschitz function $\varphi$, we have 
$$
\Var[\varphi(X_1,\dots,X_n)] \leq C n^{2-c},
$$ 
for universal constants $C,c>0$.
\item 
One has,
$$
\sum_{i \in [n]} \mathcal{H}(X_i) \leq 2 \mathcal{H}(X_1,...,X_n).
$$	
\end{enumerate}
\end{corollary} 

\begin{proof}[Proof of corollary \ref{cor:TNC}]
Let $\nu$ be the law of $(2 X_1 - 1,\dots, 2 X_n - 1)$. Observe that the condition \eqref{eq:TNC} is equivalent to 
$$
\partial_i \partial_j \mathcal{L}[\nu](\theta) \leq 0,\quad\quad\forall{i\neq j}.
$$
Therefore, Rayleigh property is equivalent to the fact that $\nabla^2 \mathcal{L}[\nu](x)$ has non-positive off-diagonal entries for all $x \in \RR^n$. Let $u \in \RR^n$. Define $u = u_+ + u_-$ where $u_+ \in \RR_+^n$ and $u_- \in \RR_-^n$. Recall that $\nabla^2 \mathcal{L}[\nu](x)$ is positive semi-definite and that $\left (\nabla^2 \mathcal{L}[\nu](x) \right )_{i,i} \leq 1$ for all $i$ (see the identity \eqref{eq:momentgenerating} below), so by convexity,
\begin{align*}
\left \langle u, \nabla^2 \mathcal{L}[\nu](x) u \right \rangle & \leq 2 \left \langle u_+, \nabla^2 \mathcal{L}[\nu](x) u_+ \right \rangle + 2 \left \langle u_-, \nabla^2 \mathcal{L}[\nu](x) u_- \right \rangle \\
& \leq 2 \langle u_+, \mathrm{diag}\left ( \nabla^2 \mathcal{L}[\nu](x) \right ) u_+ \rangle + 2 \langle u_-, \mathrm{diag}\left ( \nabla^2 \mathcal{L}[\nu](x) \right ) u_- \rangle \\
& = 2 \langle u, \mathrm{diag}\left ( \nabla^2 \mathcal{L}[\nu](x) \right ) u \rangle.
\end{align*}
Thus, $\nu$ satisfies both \eqref{eq:semilc} and \eqref{eq:semilc2} with $\beta = 2$. An application of Theorem \ref{thm:main} implies the first part, and an application of Theorem \ref{thm:entropy}, the second.
\end{proof}

It was pointed out to us by P. Nuti and J. Vondrak, that in the special case that the measure $\nu$ is homogeneous (namely when $\sum_i X_i$ is deterministic), the Rayleigh property implies both the so-called stochastic covering property (see \cite{Peres-Pemantle}) and the negative regression property (\cite{Garbe-Vondrak}), which in turn (using either of the above references) implies a stronger version the above corollary (which gives sub-Gaussian concentration). In fact, the more recent paper \cite{anari2020spectral} gives spectral gap in this case (see discussion below). However, all of the above seem to rely on homogeneouity in a crucial way.
