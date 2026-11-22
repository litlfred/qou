---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-019-41-the-q-pochhammer-symbol
section_title: "The q-Pochhammer symbol"
section_number: 4.1
pages: 30-32
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.845
latex_coverage_ratio: 0.92
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
\label{sub.ex1}

This section is devoted to the proof of Theorem~\ref{thm.ex1}. 
The $q$-difference equation~\eqref{ex1} can be written in operator form
as $((1-qt)\sigma-1)f=0$, with the Newton polygon shown in Figure~\ref{f.ex1}.

\begin{figure}[!htpb]
\begin{center}
\begin{tikzpicture}[scale=0.8,baseline=-3]
\draw[thick,<->] (0,-1.5) -- (0,3);
\draw[thick,<->] (-1.5,0) -- (3,0);
\foreach \y in {2}
\draw[thick] (2pt,\y) -- (-2pt,\y);
\filldraw (0,0) circle (2pt);
\filldraw (2,2) circle (2pt);
\filldraw (2,0) circle (2pt);
\draw (0,0) -- (2,2);
\draw (2,2) -- (2,0);
\fill[blue,opacity=0.2] (0,0) -- (2,2) -- (2,0) -- cycle;
\node at (1,1.5) {$g^{(1)}$};
\node at (1,-0.3) {$f^{(0)}$};
\end{tikzpicture}
\caption{The Newton polygon of Equation~\eqref{ex1}.}
\label{f.ex1}
\end{center}
\end{figure}

\noindent
The lower Newton polygon has one edge of slope zero. Applying the
Frobenius method, we seek a formal power series solution of the form
\be
f^{(0)}(t,q)
=
\sum_{k=0}^{\infty}\alpha_{k}(q)t^{k}\frac{\theta(\rind^{-1}t;q)}{\theta(t;q)}
\quad\text{ where }\quad
q^{k}\rind\alpha_{k}(q)-q^{k}\rind\alpha_{k-1}(q)-\alpha_{k}(q)=0.
\ee
Since $\alpha_{k}(q)=0$ for $k<0$, setting $k=0$ in the above equation
implies the vanishing of the indicial polynomial
\be
(\rind-1)\alpha_{0}(q)=0,
\ee
giving $\rind=1$. Then we have
\be
\frac{\alpha_{k}(q)}{\alpha_{k-1}(q)}
=
-\frac{q^{k}}{1-q^{k}}.
\ee
Therefore, normalising so that $\alpha_{0}(q)=1$,
\be
\label{ex1.f0}
f^{(0)}(t,q)
=
\sum_{k=0}^{\infty}(-1)^{k}\frac{q^{k(k+1)/2}}{(q;q)_{k}}t^{k}
=
(qt;q)_{\infty} \,.
\ee
This solution is convergent at $t=0$, in fact it is an entire function of $t$.

The upper Newton polygon has one edge of slope of one. Therefore, we must multiply
by a $\theta$-function to get a slope zero, \emph{i.e.} a power series solution.
The new Newton polygon is as follows.
\begin{center}
\begin{tikzpicture}[scale=1]
\draw[thick,<->] (0,-1.5) -- (0,3);
\draw[thick,<->] (-1.5,0) -- (3,0);
\foreach \y in {2}
\draw[thick] (0.1,\y) -- (-0.1,\y);
\filldraw (0,0) circle (2pt);
\filldraw (2,2) circle (2pt);
\filldraw (2,0) circle (2pt);
\draw (0,0) -- (2,2);
\draw (2,2) -- (2,0);
\fill[blue,opacity=0.2] (0,0) -- (2,2) -- (2,0) -- cycle;
\node at (0.8,1.5) {$g^{(1)}$};
\draw[ultra thick, ->] (3.5,0) -- (5,0);
\node at (4.25,0.5) {$\theta(t;q)$};
\draw[thick,<->] (0+7,-3) -- (0+7,1.5);
\draw[thick,<->] (-1.5+7,0) -- (3+7,0);
\draw[thick] {(0.1+7,-2)} -- (-0.1+7,-2);
\filldraw (0+7,0) circle (2pt);
\filldraw (2+7,-2) circle (2pt);
\filldraw (2+7,0) circle (2pt);
\draw (0+7,0) -- (2+7,-2);
\draw (2+7,-2) -- (2+7,0);
\fill[blue,opacity=0.2] (0+7,0) -- (2+7,-2) -- (2+7,0) -- cycle;
\node at (1+7,0.4) {$\hat{g}^{(1)}$};
\end{tikzpicture}
\end{center}
Therefore, the top edge has solution of the form
\be
g^{(1)}(t,q)
=
\theta(t;q)\hat{g}^{(1)}(t,q), \qquad \hat{g}^{(1)}(t,q)
=
\theta(t;q)
\sum_{k=0}^{\infty}\beta_{k}(q)t^{-k}\frac{\theta(\rind^{-1}t;q)}{\theta(t;q)}
\ee
where
\be
-q^{-k}\rind\beta_{k-1}(q)+q^{-k}\rind\beta_{k}(q)-\beta_{k}(q)=0.
\ee
As $\beta_{k}(q)=0$ for $k<0$, we get indicial polynomial
\be
(\rind-1)\beta_{0}(q)=0
\ee
and so $\rind=1$. Then we have
\be
\frac{\beta_{k}}{\beta_{k-1}}
=
\frac{1}{1-q^{k}}.
\ee
Therefore, normalising so that $\beta_{0}(q)=\frac{1}{(q;q)_{\infty}}$,
we obtain that
\be
\label{ex1.g1}
g^{(1)}(t,q)
=
\frac{\theta(t;q)}{(q;q)_{\infty}}\sum_{k=0}^{\infty}\frac{t^{-k}}{(q;q)_{k}}
=
\frac{\theta(t;q)}{(t^{-1};q)_{\infty}(q;q)_{\infty}} \,.
\ee
It follows that the monodromy is given by
\be
\vM(t,q)
=
V(t,q)^{-1}U(t,q)
=
\frac{(qt;q)_{\infty}(t^{-1};q)_{\infty}(q;q)_{\infty}}{\theta(t;q)}
=
1 
\ee
and the cocycles are equal and given by 
\be
\Om_{U}(z,\tau)
=
(U|_{0}S)(z,\tau) U(z,\tau)^{-1}
=
\Om_{U}(z,\tau)
=
(V|_{0}S)(z,\tau) V(z,\tau)^{-1}
=
\frac{(\ti q\ti t;\ti q)_{\infty}}{(qt;q)_{\infty}} \,.
\ee
Notice that
\be
\frac{(\ti q\ti t;\ti q)_{\infty}}{(qt;q)_{\infty}}
=
\Phi_{\sfb}\left(\frac{iz}{\sfb}
  +\frac{i\sfb}{2}+\frac{1}{2i\sfb}\right)^{-1}
\ee
where $\Phi$ is the Faddeev quantum dilogarithm function~\cite{Faddeev,
FK-QDL}. This function extends to a meromorphic function of $(z,\tau)\in
\BC \times \BC'$, with poles at $z\in \BZ_{\geq0}+\BZ_{\geq0}\tau$. Noting that $\Omega_{T}=1$,
it then follows from Theorem~\ref{thm.ST} that
$\Om_{U,\gamma}$ also extends. This is discussed in detail in upcoming
work~\cite{GKZ:cocycle}. This proves that this is a modular
$q$-holonomic module.
