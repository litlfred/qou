---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-017-53-taylor-series-expansion-at-u0
section_title: "Taylor series expansion at u=0"
section_number: 5.3
pages: 32-36
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.887
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
\label{sub.41near1}

The descendant state-integral is a meromophic function of $u$ which is
analytic at $u=0$ and factorizes in terms of descendant holomorphic
blocks~\eqref{41x-desc-fac}. In this section we compute the Taylor
series of the holomorphic blocks and of the state-integral at $u=0$
and show how the factorization of the descendant state-integral
\eqref{41x-desc-fac} reproduces~\eqref{410-desc-fac}.

We begin with some general comments valid for descendant holomorphic
blocks and state-integrals.  Since the descendant holomorphic blocks
are products of theta functions times $q$-hypergeometric sums, we need
to compute the Taylor expansion of each piece. For Taylor expansion of
the $q$-hypergeometric sums, we
\begin{subequations}
\begin{align}
  &\phi_n(u):=\frac{(q^{1+n}\re^u;q)_\infty}{(q^{1+n};q)_\infty}
    =\exp\left(-\sum_{l=1}^\infty \frac{1}{l!}E_l^{(n)}(q) u^l \right)
    \label{eq:phin}\\
  &\wt{\phi}_n(u):=\frac{(\tq;\tq)_\infty}{(\tq\re^u;\tq)_\infty}
    \frac{(\tq^{-1};\tq^{-1})_n}{(\tq^{-1}\re^u;\tq^{-1})_n}
    =\exp\left(\sum_{l=1}^\infty
    \frac{1}{l!}\wt{E}_l^{(n)}(\tq) u^l\right)
    \label{eq:tphin}
  \end{align}
\end{subequations}
from~\cite[Prop.2.2]{GK:qseries}, where
\begin{equation}
\label{En}
E_l^{(n)}(q)=\sum_{s=1}^\infty \frac{s^{l-1} q^{s(n+1)}}{1-q^s} 
\end{equation}
and
\begin{align}
  \wt{E}_l^{(n)}(\tq) =
  \begin{cases}
    -n+E_l^{(n)}(\tq) \quad &l=1\\
    E_l^{(n)}(\tq)\quad &l>1\;\text{odd}\\
    2E_l^{(0)}(\tq) - E_l^{(n)}(\tq)\quad &l>1\;\text{even} \,.
  \end{cases} 
\end{align}
For the Taylor series of the theta functions, we use the well-known
identity that expresses them in terms of quasi-modular forms (see,
eg.~\cite[Sec.8, Eqn(76)]{Za:quasimod}, or alternatively observe that
the theta functions that appear in the bilinear expressions of the
holomorphic blocks are exponentials of quadratic and linear forms in
$u$; see for instance~\eqref{ebx2}--\eqref{ebx3}.  Yet alternatively
(and this is the method that we will use below), when $r$ and $s$ are
nonzero integers with $r$ odd and positive, we can use the identity
\begin{equation}
  \label{thrs}
  \th(-q^{\frac{r}{2}} x^s;q)
  =(-1)^{\frac{r+1}{2}}q^{\frac{r^2-1}{8}}x^{-\frac{s(r+1)}{2}}(1-x^s)
  \phi_0(su)\phi_0(-su)  
  
\end{equation}
whereas when $r$ is odd and negative, we can use the $q$-difference
equation~\eqref{recth} to bring it to the cass of $r$ odd and positive.

One last comment is that the descendant holomorphic blocks are in
general meromorphic functions of $u$. However, their bilinear
combination that appears in the descendant state-integrals is regular
at $u=0$.

We now give the details of the Taylor series expansion of
$Z_{\knot{4}_1,m,\mu}(u;\tau)$ and of the descendant holomorphic
blocks for the $\knot{4}_1$ knot.
Using the definition of $J(x,y;q)$ and~\eqref{eq:phin}--\eqref{eq:tphin},
we find
\begin{align}
  A_m(\re^u;q)
  
  &= (1-\re^{-u})^{-2}(q;q)_\infty^{-3}\phi_0(u)^{-2}\phi_0(-u)^{-2}
  \sum_{n=0}^\infty \frac{q^{nm}}{(q;q)_n(q^{-1};q^{-1})_n}
    \phi_n(u) \re^{(2n+2m)u} \nn
  &= u^{-2}(q;q)_\infty^{-3}
    \left(\alpha^{(m)}_0(q)+u\alpha^{(m)}_1(q)+\cO(u^2)\right)
\label{eq:A-uexp-41}
\end{align}
where
\begin{subequations}
\begin{align}
  &\alpha^{(m)}_0(q) = G_m^0(q),\label{eq:a0-41}\\
  &\alpha^{(m)}_1(q) =
    \sum_{n=0}^\infty \frac{q^{nm}}{(q;q)_n(q^{-1};q^{-1})_n}
    (1+2n+2m-E_1^{(n)}(q)),\label{eq:a1-41}
\end{align}
\end{subequations}
and
\begin{align}
  B_m(\re^u;q)
  
  &= (1-\re^u)(q;q)_\infty^3\phi_0(u)\phi_0(-u)
    \sum_{n=0}^\infty \frac{q^{nm}}
    {(q;q)_n(q^{-1};q^{-1})_n}
    \phi_n(-u) \re^{(n+m)u} \nn
  &= -u(q;q)_\infty^3
    \left(\beta^{(m)}_0(q)+u\beta^{(m)}_1(q)+\cO(u^2)\right)
    \label{eq:B-uexp-41}
\end{align}
where
\begin{subequations}
\begin{align}
  &\beta^{(m)}_0(q) = G_m^0(q),\label{eq:b0-41}\\
  &\beta^{(m)}_1(q) =
    \sum_{n=0}^\infty \frac{q^{nm}}{(q;q)_n(q^{-1};q^{-1})_n}
    \left(\frac{1}{2}+n+m+E_1^{(n)}(q)\right).\label{eq:b1-41}
\end{align}
\end{subequations}
We notice that
\begin{equation}
  \beta^{(m)}_1(q) -\alpha^{(m)}_1(q) =
  
  -\frac{1}{2} G_m^1(q).
\end{equation}
Similarly, using the definition of $J(x,y;q^{-1})$, we find
\begin{align}
  A_m(\re^u;q^{-1})
  &=

    (1-\re^u)(q;q)_\infty^3\phi_0(u)^2\phi_0(-u)^2
    \sum_{n=0}^\infty\frac{q^{-nm}}{(q;q)_n(q^{-1};q^{-1})_n}
    \wt{\phi}_n(u)\re^{(2n+2m)u} \nn
  &=
    -u(q;q)_\infty^3\left(\wt{\alpha}^{(m)}_0(q)+u
    \wt{\alpha}^{(m)}_1(q) + \cO(u^2)\right)
    \label{eq:tA-uexp-41}
\end{align}
where
\begin{subequations}
\begin{align}
  &\wt{\alpha}^{(m)}_0(q) = G_{-m}^0(q),\label{eq:ta0-41}\\
  &\wt{\alpha}^{(m)}_1(q) = \sum_{n=0}^\infty
    \frac{q^{-nm}}{(q;q)_n(q^{-1};q^{-1})_n}
    \left(\frac{1}{2}+n+2m+E_1^{(n)}(q)\right),\label{eq:ta1-41}
\end{align}
\end{subequations}
and
\begin{align}
  B_m(\re^u;q^{-1})
  &=

  \frac{\phi_0(u)^{-1}\phi_0(-u)^{-1}}{(1-\re^{-u})^2(q;q)_\infty^3}
    \sum_{n=0}^\infty\frac{q^{-nm}}{(q;q)_n(q^{-1};q^{-1})_n}
    \wt{\phi}_n(-u)\re^{(n+m)u} \nn
  &=
  u^{-2}(q;q)_\infty^{-3}\left(\wt{\beta}^{(m)}_0(q)+u
    \wt{\beta}^{(m)}_1(q) + \cO(u^2)\right)
    \label{eq:tB-uexp-41}
\end{align}
where
\begin{subequations}
\begin{align}
  &\wt{\beta}^{(m)}_0(q) = G_{-m}^0(q),\label{eq:tb0-41}\\
  &\wt{\beta}^{(m)}_1(q) = \sum_{n=0}^\infty
    \frac{q^{-nm}}{(q;q)_n(q^{-1};q^{-1})_n}
    (1+2n+m-E_1^{(n)}(q)).\label{eq:tb1-41}
\end{align}
\end{subequations}
We also notice
\begin{equation}
  \wt{\beta}_1^{(m)}(q) - \wt{\alpha}_1^{(m)}(q) =
  \frac{1}{2} G_{-m}^1(q).
\end{equation}
Applying these results to the right hand side of \eqref{41x-desc-fac},
we find the $O(1/u)$ contributions from~\eqref{eq:tA-uexp-41}
and~\eqref{eq:tB-uexp-41} cancel, and the $O(u^0)$ contributions
reproduce exactly~\eqref{410-desc-fac}. Notice that the $\sqrt{\tau}$
terms that appear in~\eqref{410-desc-fac} come from expanding in terms
of $2\pi\bb\,u$ and $2\pi\bb^{-1}\,u$ in~\eqref{41x-desc-fac}.
    
As an application of the above computations, we obtain proof of a
simplified formula for the $q$-series $G^1(q)$ from~\eqref{Gm0} which
was found experimentally in~\cite{GZ:qseries}.

\begin{proposition}
  \label{prop.G}
  For $|q|<1$, we have:
  \begin{equation}
  \label{GGformula}
  G^1(q) = \sum_{n=0}^\infty (-1)^n \frac{q^{n(n+1)/2}}{(q;q)_n^2}
  (6n+1) \,.
  \end{equation}
\end{proposition}

\begin{proof}
  We first show that the definition \eqref{Gm0} can equally be written
  as
  \begin{equation}
    G^1(q) = \sum_{n=0}^\infty (-1)^n \frac{q^{n(n+1)/2}}{(q;q)_n^2}
    \left(1+2n-4E_1^{(n)}(q)\right).\label{eq:G1-im}
  \end{equation}
  By definition
  \begin{equation}
    E_1^{(n)}(q) = \sum_{s=1}^\infty \frac{q^{s(n+1)}}{1-q^s},
  \end{equation}
  they satisfy the recursion relation
  \begin{equation}
    E_1^{(n)}(q) - E_1^{(n-1)}(q) = -\frac{q^n}{1-q^n},
  \end{equation}
  and therefore
  \begin{equation}
    E_1^{(n)}(q) = E_1^{(0)}(q) -\sum_{j=1}^n\frac{q^j}{1-q^j}.
  \end{equation}
  Using the identification $E_1(q) = 1-4E_1^{(0)}(q)$, one can then
  easily show that \eqref{eq:G1-im} is the same
  as \eqref{Gm0}.

  \eqref{GGformula} follows from \eqref{eq:G1-im} thanks to the
  non-trivial identity
  \begin{equation}
    \sum_{n=0}^\infty \frac{n+E_1^{(n)}(q)}{(q;q)_n(q^{-1};q^{-1})_n}
    = 0,\quad |q|<1,
    \label{eq:E1n-id}
  \end{equation}
  which now we prove.
  The crucial fact we use is that when $|q|<1$, $J(x,y;q)$ is
  symmetric between $x$ and $y$ (see a proof in \cite{Beem}).
  Let us consider the following expansion in small $u$
  \begin{align}
    J(\re^{-u},\re^u;q) =
    &\sum_{n=0}^\infty (q^{1+n}\re^u;q)_\infty\frac{\re^{-nu}}{(q^{-1};q^{-1})_n} =
    (q;q)_\infty\sum_{n=0}^\infty \frac{\phi_n(u)\re^{-nu}}{(q;q)_n(q^{-1};q^{-1})_n}\nn =
    &(q;q)_\infty\sum_{n=0}^\infty \frac{1-(n+E_1^{(n)}(q))u}{(q;q)_n(q^{-1};q^{-1})_n} +
    O(u^2). 
  \end{align}
  Since $J(\re^{-u},\re^u;q) = J(\re^{u},\re^{-u};q)$, the coefficient
  of $u$ (and in fact, of any odd power of $u$) in the expansion above
  vanishes, which leads to \eqref{eq:E1n-id}.
\end{proof}

As a second application, we demonstrate that Theorem~\ref{thm.410},
especially the identities \eqref{det41}, \eqref{WWT41}, as well as the
recursion relation \eqref{41qdiff}, can be proved by taking the $u=0$
limit of the analogue identities in Theorem~\ref{thm.41b}.

Using the expansion formulas of holomorphic blocks \eqref{eq:A-uexp-41},
\eqref{eq:B-uexp-41}, \eqref{eq:tA-uexp-41}, \eqref{eq:tB-uexp-41},
the Wronskians can be expanded as
\begin{align}
  W_m(\re^u;q) =
  &\begin{pmatrix}
    G_m^0(q)+u\alpha_1^{(m)}(q)&G_m^0(q)+u\beta_1^{(m)}(q)\\
    G_{m+1}^0(q)+u\alpha_1^{(m+1)}(q)&G_{m+1}^0(q)+u\beta_1^{(m+1)}(q)
  \end{pmatrix}
  \begin{pmatrix}
    u^{-2}(q;q)_\infty^{-3}&0\\
    0&-u(q;q)_\infty^3
  \end{pmatrix},
  \label{eq:Wp-uexp-41}\\
  W_m(\re^u;q^{-1}) =
  &\begin{pmatrix}
    G_{-m}^0(q)+u\wt{\alpha}_1^{(m)}(q)
    &G_{-m}^0(q)+u\wt{\beta}_1^{(m)}(q)\\
    G_{-m-1}^0(q)+u\wt{\alpha}_1^{(m+1)}(q)
    &G_{-m-1}^0(q)+u\wt{\beta}_1^{(m+1)}(q)
  \end{pmatrix}
  \begin{pmatrix}
    -u(q;q)_\infty^{3}&0\\
    0&u^{-2}(q;q)_\infty^{-3}
  \end{pmatrix}
  \label{eq:Wn-uexp-41}
\end{align}
Taking the determinant of \eqref{eq:Wp-uexp-41}, we find
\begin{equation}
  \det W_m(\re^u;q) = \frac{1}{2} \det W_m(q) + O(u)
\end{equation}
which together with the $u$-expansion of the right hand side of
\eqref{W410} leads to the determinant identity \eqref{det41}.
Furthermore, by substituting \eqref{eq:Wp-uexp-41},
\eqref{eq:Wn-uexp-41} into the Wronskian relation \eqref{WW41b}, the
latter also reduces in the leading order to the determinant identity
\eqref{det41}.  On the other hand, the Wronskian relation
\eqref{WWT41b} is equivalent to
\begin{equation}
  W_m(q) = 2
  \begin{pmatrix}
    0&-1\\1&0
  \end{pmatrix}\left(W_m(q)^{-1}\right)^T
  \begin{pmatrix}
    0&1\\-1&0
  \end{pmatrix}
\end{equation}
which can be proved directly by expressing the inverse matrix on the
right hand side by minors and determinant, using the explicit value of
the determinant given by the identity \eqref{det41}.

Finally, from the expression \eqref{eq:a0-41},\eqref{eq:b0-41} of the
leading order coefficients $\alpha_0^{(m)}(q)$, $\beta_0^{(m)}(q)$ of
$A_m(\re^u;q)$, $B_m(\re^u;q)$ in the expansion of $u$, one concludes
that the recursion relation \eqref{41qdiff} should be the $u=0$ limit
of the recursion relation \eqref{rec41m} in $m$, and one can easily
check it is indeed the case.
