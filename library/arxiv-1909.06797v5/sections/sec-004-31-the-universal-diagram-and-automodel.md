---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-004-31-the-universal-diagram-and-automodel
section_title: "The Universal Diagram and Automodel"
section_number: 3.1
pages: 10-12
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
toc_source: outline
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 1.0
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
\label{sec:automodel}

Although we are using the ``English" notation for Young diagrams, but the limit shape of Young diagrams takes a simple form in rotated French notation. A typical shape of Young diagram in French notation is given in \cref{fig:YDFrench}. The centres of boxes are marked with $(X,Y)$ coordinates. The function $X(Y)$ specifies a particular shape of Young diagram in this notation.
\begin{figure}[h]
	\begin{center}
		\includegraphics[scale=0.2]{RegularYT.pdf}
		\caption{\footnotesize{Typical structure of a Young diagram in French notation.}}
		\label{fig:YDFrench}
	\end{center}
\end{figure}
However, it is more convenient to rotate this diagram anti-clock wise by $\pi/4$ and work in the redefined coordinates
\begin{equation}
u=\frac{1}{2}(Y-X) \qquad v=\frac{1}{2}(Y+X).
\end{equation}
A Young diagram in this notation\footnote{There is another advantage to draw the Young diagrams in rotated French notation. A transition from $\lambda_k$ to $\lambda_{k+1}$ occurs when one keeps a box at any of the minima of rotated diagram. Putting a box at different minima corresponds to different diagrams at $k+1$ level. Therefore the transition probabilities are denoted by $\mu_a$ where $a$ is the position of a minimum. To find $\mu_a$ we define two polynomials $P(x) = \prod_{a=1}^{n}(x-x_a)$ and $Q(x)= \prod_{a=1}^{n-1}(x-y_a)$, where $x_1,\cdots , x_n$ are positions of consecutive minima and $y_1,\cdots,y_{n-1}$ are consecutive maxima. The transition probability from $\lambda_k$ to $\lambda_{k+1}$ by adding a box at $a^{th}$ minima is given by decomposing the quotient into partial fraction

\ben
\sum_{a=1}^{n}\frac{\mu_a}{x-x_a} = \frac{Q(x)}{P(x)}.
\een

}
is depicted in figure \ref{fig:YDFrench-rotated}.
\begin{figure}[h]
	\begin{center}
		\includegraphics[scale=0.17]{RotatedYT.pdf}
		\caption{\footnotesize{Typical structure of a $45^{\circ}$ anti-clockwise rotated Young diagram.}}
		\label{fig:YDFrench-rotated}
	\end{center}
\end{figure}
Note that here the coordinate $u$ is different than the Young diagram density defined in (\ref{eq:uhdef}). For a finite number of boxes the function $v(u)$ is rough and zig-zag i.e. $v'(u)=\pm 1$. As the number of boxes goes very large we define a rescaled function 

\be\label{eq:vk}
\hat v_k(u) = \frac{v(u\sqrt{k})}{\sqrt{k}}
\ee

such that the area under the curve is finite and the boundary curve becomes smooth. It was observed by \cite{LogShe,VerKer77} that when the growth process follows Plancherel transition probability (\ref{eq:transmeasure}) the asymptotic shape of rescaled Young diagrams converges uniformly to a unique curve given by
\begin{equation}
\label{eq:kerovfunction}
\lim_{k \ra \infty}\hat v_k(u)\equiv\Omega(u)=
\begin{cases}
\frac{2}{\pi}(u \sin^{-1} \frac{u}{2}+\sqrt{4-u^2}) &\mbox{if} \quad |u| \leq 2\\
|u|& \mbox{if} \quad |u|>2.
\end{cases}
\end{equation}

In the continuum limit Kerov introduced \cite{Kerov1} \emph{charge} of a diagram, denoted by $\sigma(u)$ and is given by (we are using the notation that $\hat v(u) =\hat v_k(u)$ in the large $k$ limit)

\ben\label{eq:youngcharge}
\sigma(u) = \frac12 \lb\hat v(u)-|u|\rb.
\een

Therefore,

\ben\label{eq:chargeprime}
\sigma'(u) =\bigg\{ {\ \ \frac12 +\frac{\hat v'(u)}{2} \quad \for \quad u<0 \atop -\frac12 +\frac{\hat v'(u)}{2} \quad \for \quad u>0}.
\een

One can define moments of a diagram

\ben\label{eq:moments}
p_n = -n \int u^{n-1} d\sigma(u)
\een

such that area of a diagram (area covered under the curve $\hat v(h)$) is given by $A=(p_2-p_1^2)/2$. It is convenient to consider a moment generating function

\ben\label{eq:momgenfunc}
S(x) = \sum_{n=1}^{\infty}\frac{p_n}{n}x^{-n} = \int \frac{d\sigma(u)}{u-x}.
\een

The moment generating function as well as the sequence of moments determine the charge and hence the diagram ($\hat v(u)$) completely. The moment generating function plays an important role in our large $k$ analysis of partition function.

In \cite{Kerov1} Kerov introduced a dynamical model for the growth of Young diagrams. For every continuous Young diagram characterized by the function $\hat v(u)$, one can define the function $v(u,t)$, called the automodel tableaux which depends on two variables $u$ and $t$ as
\begin{equation}
\hat v(u,t)=\sqrt{t} \ \hat v(u/\sqrt{t}) \quad \mbox{for} \quad t>0\ .
\end{equation}
Kerov showed that the Young diagrams, following Plancherel growth, belong to \emph{automodel} class and satisfy the equation
\begin{equation}\label{eq:automodeleqnv}
{\partial_t \hat v(u,t)}=\frac{1}{2t}(\hat v(u,t)-u\partial_u \hat v(u,t)).
\end{equation}
In terms of charges the automodel equation is given by,

\ben\label{eq:automodeleqnsigma}
\dow_t \sigma'(u,t)+\frac{u}{2t} \sigma^{''}(u,t)=0.
\een
