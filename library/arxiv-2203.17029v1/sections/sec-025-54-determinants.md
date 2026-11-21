---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-025-54-determinants
section_title: "Determinants"
section_number: 5.4
pages: 44-46
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.688
latex_coverage_ratio: 0.928
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
The functional equation \eqref{41x1} for $U,V$ defined in~\eqref{UVex41}
can be written in the form 
\be
U(qt,\lambda,q)
=
A(t;q)U(t,\lambda,q)
\quad\text{and}\quad
V(qt,q)
=
A(t;q)V(t,q)
\ee
where
\be\label{comp.mat.41.x1}
A(t,q)
=
\begin{pmatrix}
0 & 1\\
-q^{-2} & 2q^{-1}-q^{-2}t^{-1}
\end{pmatrix} \,.
\ee
Therefore, we see that
\be
\det(U(qt,\lambda,q))=\det(U(t,\lambda,q))q^{-2}
\quad\text{and}\quad
\det(V(qt,q))=\det(V(t,q))q^{-2}.
\ee

\begin{lemma}
\label{lem.41det}
  We have
\be
-\det(U(t,\lambda,q)) = \det(V(t,q)) = q^{-1}t^{-2} \,.
\ee
  \end{lemma}
  
\begin{proof}
Firstly notice that both $\det(U(t,\lambda,q))t^2$ and $\det(V(t,q))t^2$
are elliptic functions in $t$. Furthermore,
\be
\det(U(t,\lambda,q))
=
f^{(1)}(t,\lambda,q)f^{(-1)}(qt,q)-f^{(1)}(qt,\lambda,q)f^{(-1)}(t,q)
\ee
has potentially simple poles in $t$ at $\pm q^{-1/4-n/2}\lambda^{-1}$.
Lemma~\ref{lem.resf1} implies that

\begin{align*}
\Res_{t=\pm q^{-1/4-n}\lambda^{-1}}\det(U(t,\lambda,q)) =
&\frac{\theta(\pm q^{3/4}\lambda^{-1};q)\theta(\pm q^{-1/4};q)
  \theta(\pm q^{-3/4};q)\theta(\pm q^{-3/4}\lambda;q)}{2(q;q)_{\infty}^{6}
  \theta(q^{-1}\lambda;q)\theta(q^{-3/2}\lambda;q)} \\
& \times
f^{(-1)}(\pm q^{-1/4-n}
  \lambda^{-1},q)f^{(-1)}(\pm q^{3/4-n}\lambda^{-1},q)\\
&-\frac{\theta(\pm q^{3/4}\lambda^{-1};q)\theta(\pm q^{-1/4};q)
  \theta(\pm q^{-3/4};q)\theta(\pm q^{-3/4}\lambda;q)
}{2(q;q)_{\infty}^{6}
  \theta(q^{-1}\lambda;q)\theta(q^{-3/2}\lambda;q)}\\
& \times
f^{(-1)}(\pm q^{3/4-n}\lambda^{-1},q)f^{(-1)}(\pm q^{-1/4-n}\lambda^{-1},q) \\
  =&\; 0 \,.
\end{align*}

A similar calculation shows that

$\Res_{t=\pm q^{1/4-n}\lambda^{-1}}\det(U(t,\lambda,q))=0$.

Therefore, $U(t,\lambda;q)t^2$ is elliptic and holomorphic in
$t\in\BC^{\times}$, hence it is constant in $t$. Now considering the limit as
$t\rightarrow0$, using the definition of $f^{(\pm1)}$ and their asymptotic
expansions (given by their formal power series expansions, by a $q$-version of
Watson's lemma), it follows that
\be
\begin{aligned}
\det(U(t,\lambda,q))t^2
&=
\lim_{t\rightarrow 0}\det(U(t,\lambda,q))t^2
=
\lim_{t\rightarrow 0}\frac{\theta(t;q)}{\theta(t;q)}t^2
-\lim_{t\rightarrow 0}\frac{\theta(qt;q)}{\theta(q^{-1}t;q)}t^2\\
&=
-\lim_{t\rightarrow 0}q^{-1}\frac{\theta(t;q)}{\theta(t;q)}
=
-q^{-1} \,.
\end{aligned}
\ee

For $V$ notice that
\be
\det(V(t,q))t^{2}
=
g^{(0,0)}(t,q)g^{(0,1)}(qt,q)t^{2}-g^{(0,0)}(qt,q)g^{(0,1)}(t,q)t^{2}.
\ee
This has potentially simple poles at $t\in q^{\BZ}$. There is no non-constant
elliptic function that satisfies this~\cite{Akhiezer}.
Therefore, $\det(V(t,q))t^{2}$ is constant. Then notice that
\be
\det(V(t,q))t^{2}
=
\lim_{t\rightarrow\infty}\det(V(t,q))t^{2}
=
q^{-1}.
\ee
\end{proof}

\begin{corollary}
  \label{cor:41holsol}
  If $h(t,q)$ is holomorphic for $t\in\BC^{\times}$
  and satisfies the $q$-difference equation~\eqref{41x1} then
\be
h(t,q)=C_{0}(q)g^{(0,0)}(t,q) \,.
\ee
\end{corollary}

\begin{proof}
Every solution to equation~\eqref{41x1} can be written in the form
\be
h(t,q)=C_{0}(t,q)g^{(0,0)}(t,q)+C_{1}(t,q)g^{(0,1)}(t,q)
\ee
for some elliptic functions $C_0$ and $C_1$. Now we see that
\be
\det
\begin{pmatrix}
g^{(0,0)}(t,q) & h(t,q)\\
g^{(0,0)}(qt,q) & h(qt,q)\\
\end{pmatrix}
=
C_{1}(t,q)q^{-1}t^{-2}
\ee
is holomorphic and therefore $C_{1}(t,q)=C_{1}(q)$ is independent of $t$. Now
notice that if $g(t_{0},q)=0$ then $g(qt_{0},q)\neq0$ as otherwise this would imply
$\det(V(t_{0},q))=0$. This means that if $C_{1}(q)\neq0$ then $C_{0}(t,q)$ has
simple poles at $t\in q^{\BZ}$ and no other poles for $t\in\BC^{\times}$ which
contradicts the fact that $C_{0}(t,q)$ is elliptic as this would give an isomorphism
from the elliptic curve to $\mathbb{CP}^{1}$. Therefore
$C_{1}(q)=0$. Then again noting that if $g(t_{0},q)=0$ then $g(qt_{0},q)\neq0$
we see that $C_{0}(t,q)$ must be constant in $t$.

We remark that an alternative proof can be given using the fact that all holomorphic
solutions on $\BC^{\times}$ have a convergent Laurent/Fourier series expansion
\be
\sum_{k\in\BZ}\alpha_{k}(q)t^{k} \,.
\ee
This is a consequence of Cauchy's theorem and a detailed discussion of this
can be found, for example, in~\cite{Ahlfors}. In our case, the functional equations
imply this expansion is divergent if $\alpha_{-1}\neq0$. This forces
$\alpha_{-1}=0$, and the functional equation then implies that $\alpha_{k}=0$
  for $k<0$ and that $\alpha_{k}$ are
uniquely determined by $C_{0}(q)=\alpha_{0}(q)$ for $k \geq 0$ which implies
that our function is equal to $C_{0}(q)g^{(0,0)}(t,q)$.
\end{proof}


\subsection{State integral}
\label{sub.state}

In this section we discuss the second part of Theorem~\ref{thm.41} concerning
the extension of the cocycle to the cut plane. The main idea is to use
descendant state integrals, following~\cite[Eqn.(41)]{GGM}, defined by







\be
\mathcal{I}_{A,B}(z,\tau)
=
\int_{\BR+i\ve}
\Phi_{\sfb}(x)^B
\exp\left(-A\pi i x^{2}-2\pi\frac{zx}{\sfb}\right)dx.
\ee
Using the holomorphic extension of the quantum dilogarithm $\Phi$ from
Theorem~\ref{thm.ex1}, this integral can be shown to extend to a holomorphic
function in for $(z,\tau)\in\BC\times\BC'$. We are interested in the integrals
$\mathcal{I}_{1,2}(z,\tau)$ which, using the residue theorem, factorise as an
elementary function holomorphic for $\tau\in\BC'$ times the following bilinear
combination, see~\cite[Thm.3]{GGM},
\be
\label{gs.fac.int}
\begin{aligned}
\calI(z,\tau)
&=\tau^{1/2} g^{(0,0)}(\tilde{t},\tq)g^{(0,1)}(t,q)
-\tau^{-1/2}g^{(0,1)}(\tilde{t},\tq)g^{(0,0)}(t,q)\\
&\quad+\tau^{-1/2}\left(\tau\frac{\theta'(t^{-1};q)}{\theta(t^{-1};q)}
  -\frac{\theta'(\tilde{t}^{-1};\tq)}{\theta(\tilde{t}^{-1};\tq)}
  -\frac{1}{2}+\frac{\tau}{2}-z\right)g^{(0,0)}(\tilde{t},\tq)g^{(0,0)}(t,q)\\
&=\tau^{1/2} g^{(0,0)}(\tilde{t},\tq)g^{(0,1)}(t,q)
-\tau^{-1/2} g^{(0,1)}(\tilde{t},\tq)g^{(0,0)}(t,q) \,.
\end{aligned}
\ee
where the equality follows from Equation~\eqref{S.mod.thd}. Therefore,
$\calI(z,\tau)$ extends to a holomorphic function for $(z,\tau)\in\BC\times\BC'$.
Now, we see that 
{\small
\be
\begin{aligned}
\Om_{V,S}(z,\tau)
&=
(V|_{\kappa}S)(z,\tau)V(z,\tau)^{-1}\\
&=
qt^2
\begin{pmatrix}
  g^{(0,0)}(\tilde{t},\tq) & g^{(0,1)}(\tilde{t},\tq)\\
  g^{(0,0)}(\tq\tilde{t},\tq) & g^{(0,1)}(\tq\tilde{t},\tq)\\
\end{pmatrix}
\begin{pmatrix}
  \tau^{1/2} & 0\\
  0 & \tau^{-1/2}
\end{pmatrix}
\begin{pmatrix}
  g^{(0,1)}(qt,q) & -g^{(0,1)}(t,q)\\
  -g^{(0,0)}(qt,q) & g^{(0,0)}(t,q)
\end{pmatrix}
.
\end{aligned}
\ee
}
The entries of $\Om_{V,S}$ are then elementary functions holomorphic for
$\tau\in\BC'$ times $\calI(z+n+m\tau,\tau)$ for some $n,m\in\{-1,0,1\}$.
This shows that the cocycle $\Om_{V,S}$ extends to a holomorphic function for
$(z,\tau)\in\BC\times\BC'$; see~\cite[Thm.14]{GGM:peacock} following the proof
of~\cite[Thm.1.1]{GK:qseries}. Now noting that
\be
\Av(\vM) = \Delta_{\kappa,\gamma} (\Av(\vM)|_{\kappa} \gamma)
\ee
and $\Om_{\Av(U),T}=I$, part (c) of Theorem~\ref{thm.ST} proves part \rm{(b)}
of Theorem~\ref{thm.41}.
