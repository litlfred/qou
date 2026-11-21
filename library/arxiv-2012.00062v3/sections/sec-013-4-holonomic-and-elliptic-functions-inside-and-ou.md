---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-013-4-holonomic-and-elliptic-functions-inside-and-ou
section_title: "Holonomic and elliptic functions inside and outside the unit disk"
section_number: 4
pages: 24-25
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.935
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
\label{sec.elliptic}

An important property for the functions of a complex variable $q$ in
our paper (such as the holomorphic blocks considered below) is that
they can be defined both inside ($|q|<1$) and outside ($|q|>1$) the unit
disk, in such a way that they have the same annihilator ideal. Recall
that if $L$ and $M$ denote the operators that act on functions
$f(x;q)$ by $(L f)(x;q)=f(qx;q)$ and $(M f)(x;q)=x f(x;q)$, then
$LM=q ML$, hence $L^{-1}M=q^{-1}ML^{-1}$. It follows that if
$P(L,M,q)f(x;q)=0$, then $P(L^{-1},M,q^{-1}) f(x;q^{-1})=0$ where
$P(L,M,q)$ denotes a polynomial in $L$ with coefficients polynomials
in $M$ and $q$.

A first example of a function to consider is
$(x;q)_\infty=\prod_{j=0}^\infty (1-q^j x)$, which is well-defined for
$|q|<1$ and $x \in \BC$ and satisfies the linear $q$-difference
equation
\begin{equation}
\label{recxq}
(1-x)(qx;q)_\infty = (x;q)_\infty \qquad (|q|<1) \,.
\end{equation}
We can extend it to a meromorphic function of $x$ when $|q|>1$ (by a
slight abuse of notation) by defining
\begin{equation}
\label{xqout}
(x;q^{-1})_\infty := (qx;q)_\infty^{-1} \qquad (|q|<1)\,,
\end{equation}
so that Equation~\eqref{recxq} holds for $|q| \neq 1$. Our second
example is the theta function
\begin{equation}
\th(x;q)=(-q^{\frac{1}{2}}x;q)_\infty (-q^{\frac{1}{2}}x^{-1};q)_\infty \qquad (|q|<1)  
\end{equation}
which satisfies the linear $q$-difference equation
\begin{equation}
\label{recth}
\th(qx;q)=q^{-\frac{1}{2}} x^{-1}\th(x;q) \qquad (|q|<1) \,
\end{equation}
and can be extended to $\th(x;q^{-1})=\th(x;q)^{-1}$ when $|q|> 1$ so
that Equation~\eqref{recth} holds for $|q| \neq 1$. $\th(x;q)$ is a
meromorphic function of $x \in \BC^*$ with the following (simple)
zeros and (simple) poles

\begin{align}
  \label{thetap}
  |q| < 1 & & \text{zeros}(\th)& =-q^{\frac{1}{2}+\BZ}
  &  \text{poles}(\th) & =\emptyset \\
  \notag
  |q| > 1 & & \text{zeros}(\th)& = \emptyset
  &  \text{poles}(\th) & =-q^{\frac{1}{2}+\BZ} \,.
\end{align}

An important property of the theta functions is that they factorize
the exponentials of a quadratic and linear form of $u$. This
fact is a consequence of the modular invariance of the theta function
and was used extensively in the study of holomorphic
blocks~\cite{Beem}.

\begin{lemma}
  \label{lem.thetaf}
  For integers $r$ and $s$ we have:
  \begin{subequations}
    \begin{align}
      \label{ebx2}
      \re^{\pi \ri (u + r c_\bb)^2}
      
      & = \re^{-\frac{\pi \ri}{12}(\tau+\tau^{-1})} \th((-q^{\frac{1}{2}})^r x;q)
        \th((-\tq^{-\frac{1}{2}})^r\tx;\tq^{-1}) \\
      \label{ebx3}
      \re^{\pi \ri r u^2 + 2 \pi \ri s c_\bb u}
      &= \ri^s
        \re^{\frac{\pi \ri}{12}(3s-r)(\tau+\tau^{-1})}
        
        \th(x;q)^{r-s} \th(-q^{\frac{1}{2}} x;q)^s
        \times \th(\tx;\tq^{-1})^{r-s} \th(-\tq^{-\frac{1}{2}}\tx;\tq^{-1})^s
    \end{align}
  \end{subequations}
  for integers $r$ and $s$.
\end{lemma}

Note that we the above factorization formulas are by no means unique,
and this is a reflection of the dependence of the above formulas on a
theta divisor.

\begin{proof}
  When $x=\re^{2\pi \bb u}$, $q=e(\tau)$, $\tq=e(-1/\tau)$ and
  $|q|<1$, then we claim
  \begin{equation}
    \label{ebx}
    \re^{-\frac{1}{4\pi \ri \tau} (\log x)^2} = \re^{\pi \ri u^2}
    = \Phi_\bb(0)^{-2} \Phi_\bb(u) \Phi_\bb(-u)
    = \re^{-\frac{\pi \ri}{12}(\tau+\tau^{-1})} \th(x;q)\th(\tx;\tq^{-1}) \,.
  \end{equation}
  The first equality is easy, the second one follows from the
  inversion formula of Faddeev's quantum dilogarithm, and the third one
  follows from the product expansion of Faddeev's quantum dilogarithm
  or from the modular invariance of the theta function. Note also that
  $\Phi_\bb(0)^2=(q/\tq)^{\frac{1}{24}}=\re^{\frac{\pi
      \ri}{12}(\tau+\tau^{-1})}$.  Equation~\eqref{ebx2} follows
  easily from the above and Equation~\eqref{ebx3} follows from the
  above using for example,
  $ \re^{\pi \ri r u^2 + 2 \pi \ri s c_\bb u} = \re^{(r-s)\pi \ri
    u^2}\re^{s\pi i(u+c_\bb)^2}\re^{-s\pi \ri c_\bb^2}$.
\end{proof}





\section{The $\knot{4}_1$ knot}
\label{sec.41}
