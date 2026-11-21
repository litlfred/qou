---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-016-33-state-integral
section_title: "State integral"
section_number: 3.3
pages: 28-29
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.969
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
\label{subsec.heine.stateint}

Consider the following state integral

\be
\label{heine.stateint}
I(z,\alpha,\beta,\tau) = 
\int_{\calC} \frac{\Phi_{\sfb}(x)
  \prod_{j=1}^{r-1} \Phi_{\sfb}(x+i\sfb^{-1}\beta_{j}+i\sfb^{-1}-i\sfb)}{
\prod_{j=1}^{r} \Phi_{\sfb}(x+i\sfb^{-1}\alpha_{j}+i\sfb^{-1}-i\sfb)}




\exp\left(-2\pi\frac{zx}{\sfb}\right)
dx \,.







\ee
where $\calC$ is a contour in the complex plane asymptotic to
$\BR+i\ve$ that separates the poles of the numerator from the zeros of the
denominator of the integrand, $a_{i}=\e(\alpha_{i})$,
$\tilde{a}_{i}=\e(\alpha_{i}/\tau)$, $b_{i}=\e(\beta_{i})$ and
$\tilde{b}_{i}=\e(\beta_{i}/\tau)$, and $\Phi_\sfb$ is the Faddeev quantum
dilogarithm function ~\cite{Faddeev, FK-QDL} and $\sfb=\sqrt{\tau}$.



















We first discuss convergence of the above integral for
$\tau=\sfb^2$ in the upper half-plane. Using the asymptotic behavior
$\Phi_{\sfb}(x) \sim e^{2 \pi i x^2}$ (resp., $1$) when $\Re(x) \gg 0$
(resp., $\Re(x) \ll 0$) (see for example, ~\cite[Eqn.(46)]{AK}), it follows that
when $\Re(x)\gg 0$, the integrand of~\eqref{heine.stateint} is given by a constant
times $e^{-2\pi x \sfb^{-1} (\gamma+z)}$ where
$\gamma=\sum_{j=0}^{r-1}\beta_j-\sum_{j=1}^r \alpha_j$, and setting $x=x_0+i t$
with $t \gg 0$, it follows that the absolute value of the integrand is a constant
times $e^{-2\pi t \Im(\sfb^{-1}(\gamma+z))}$, which is exponentially decaying when
$\Im( \sfb^{-1}(\gamma+z))<0$. Likewise, when $\Re(x) \ll 0$, the integrand is
exponentially decaying when $\Im(\sfb^{-1} z)>0$. 

Finally, the state integral satisfies difference equations when we shift $\alpha,\beta,z$ by either $1$ or $\tau$. This can be used to analytically extend to a meromorphic function for $\tau\in\BC'$ and $\alpha\in\BC^{r}$, $\beta\in\BC^{r-1}$, and $z\in\BC$.
































From its very definition, the state integral is a well-defined holomorphic
function of $\tau \in \BC'$. Moreover, after moving the contour of integration
upwards and using the residue theorem (see eg.~\cite{GK:qseries}), the
state integral in Equation~\eqref{heine.stateint} can be written in the
factorised form
\be
\label{heine.II}
I(z,\alpha,\beta,\tau)=-t^{1/2}\tilde{t}^{1/2}\frac{\tau}{2\pi i}
\calI(z,\alpha,\beta,\tau)
\ee
where
\be
\label{heine.stateint.fac}
\calI(z,\alpha,\beta,\tau)
=f^{(1)}(t,a,b,q)f^{(1)}(\tilde{t},\tilde{a},\tilde{b},\tq^{-1})
-\tau\sum_{j=1}^{r}f^{(qb_{j}^{-1})}(t,a,b,q)
f^{(qb_{j}^{-1})}(\tilde{t},\tilde{a},\tilde{b},
\tq^{-1})\,.
\ee
Now $\calI(z+k+j\tau,\alpha,\beta,\tau)$ is nothing but the $(j+1,k+1)$ entry
of the matrix
\be
  U(t,a,b,q)
  \begin{pmatrix}
    1 & 0 & \dots & 0\\
    0 & -\tau & \dots & 0\\
    : & : & \dots & :\\
    0 & 0 & \dots & -\tau\\
  \end{pmatrix}
  U(\tilde{t},\tilde{a},\tilde{b},\tq^{-1})^{T}\,,
\ee
and therefore, by Equation~\eqref{heine.selfdual.Ueq}, the $(j+1,k+1)$ entry of
\be
  U(t,a,b,q)
  \begin{pmatrix}
    1 & 0 & \dots & 0\\
    0 & \tau & \dots & 0\\
    : & : & \dots & :\\
    0 & 0 & \dots & \tau\\
  \end{pmatrix}
  U(\tilde{t},\tilde{a},\tilde{b},\tq)^{-1}Q(\tilde{t},\tilde{a},\tilde{b},\tq)^{-T}
  \,.
\ee
Therefore, inverting $Q$, we see that the cocycle
\be
  \Om(z,\alpha,\beta,\tau)
  =
  U(\tilde{t},\tilde{a},\tilde{b},\tq)
  \begin{pmatrix}
    1 & 0 & \dots & 0\\
    0 & \tau & \dots & 0\\
    : & : & \dots & :\\
    0 & 0 & \dots & \tau\\
  \end{pmatrix}^{-1}
  U(t,a,b,q)^{-1}
\ee
extends to a meromorphic function for $\tau\in\BC'$. This complete the proof of
Theorem~\ref{thm.heine}.

\begin{remark}
\label{rem.updown}
Note that the state integral ~\eqref{heine.stateint} is absolutely convergent
and its contour of integration can be pushed either upwards or downwards. Doing
so, the integral factorises in two different ways, one giving the $U$-cocycle
and another giving the $V$-cocycle. This explains the equality of the two
cocycles from first principles.
\end{remark}
