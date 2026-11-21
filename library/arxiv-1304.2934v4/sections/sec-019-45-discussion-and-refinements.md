---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-019-45-discussion-and-refinements
section_title: "Discussion and refinements"
section_number: 4.5
pages: 36-38
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 0.763
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\subsubsection{Bahadur-Rao theorem and Cramér-Petrov expansion}
We consider here the case of a sum $S_n=Y_1+\cdots+Y_n$ of i.i.d.~random variables
such that $Y=Y_1$ has an infinitely divisible distribution of Levy exponent $\eta$.
Then $S_n$ {\em converges mod-$Y$} with parameters $n$ and limiting function $\psi=1$;
see Example \ref{ex:sumiid}. In this case, Theorems \ref{thm:mainnonlattice} and \ref{thm:mainlattice}
correspond to Bahadur-Rao estimates   
$$\proba[S_n \geq n\,x] \simeq \begin{cases}\frac{\exp(-n\,F(x))}{(1-\E^{-h})\sqrt{2\pi n \,\eta''(h)}}
    &\!\!\!\text{in the lattice case (assume $\Z$ is the minimal lattice);} \\
\frac{\exp(-n\,F(x))}{h\sqrt{2\pi n \,\eta''(h)}}&\!\!\!\text{in the non-lattice case,}
 \end{cases}
$$
where $\eta(h)=\log \esper[\E^{hY}]$ and $F$ is the Legendre-Fenchel transform of $\eta$;
see Theorem 3.7.4 in \cite{DZ98}, and also the papers \cite{BR60,Ney83,Ilt95}.
\medskip

In the same setting,
 Theorems \ref{thm:cltnonlattice} and \ref{thm:cltlattice} correspond to 
 Cramér-Petrov expansion \cite{Petrov95} (in the non-lattice case,
 we assume in addition that the law of $Y$ is absolutely continuous with respect to Lebesgue measure).
 To the best of our knowledge, the link with the Legendre-Fenchel transform is new.\smallskip
\medskip



\subsubsection{On the infinite divisibility of $\phi$}
\label{subsect:OnInfDiv}
As above, consider the case of a sum $S_n=Y_1+\cdots+Y_n$ of i.i.d.~random variables,
but with the law of $Y_1$ not necessarily infinitely divisible.
In this case, $\esper[\E^{zS_n}]=\big(\esper[\E^{zY_1}] \big)^n$, 
but, if $\esper[\E^{zY_1}]$ vanishes for some complex value of $z$,
one cannot write this as $\exp(n \eta(z))$ as in Definition \ref{def:modphi}.

The proofs of our large deviation results --- Theorems \ref{thm:mainnonlattice} and \ref{thm:mainlattice} ---
can nevertheless be adapted to this setting.
For the extended central limit theorem --- Theorems \ref{thm:cltlattice} and \ref{thm:cltnonlattice} ---
we would need to assume the estimate given by
Lemma \ref{lem:technicqdelta_lattice} or Lemma \ref{lem:technicqdelta_nonlattice}.
This is satisfied in particular if:
\begin{itemize}
\item either $Y$ takes its values in $\Z$, and there are two consecutive integers $n,m=n-1$ such that $\proba[Y=n]\neq 0$ and $\proba[Y=m]\neq 0$;\vspace{2mm}
\item or, $Y$ has a component absolutely continuous w.r.t. Lebesgue measure.\vspace{2mm}
\end{itemize}
Since these are classical results and since our method are close to the usual ones,
we do not give details on how to adapt our proof to the non infinitely divisible setting.

\begin{remark}
For Bahadur-Rao theorem,
it should be noticed that the assumption that $\Z$ is the minimal lattice is necessary.
For instance, if one considers a sum $S_n$ of $n$ independent Bernoulli random variables with $\proba[B=1]=\proba[B=-1]=1/2$, then the estimate above is not true, because $S_n$ has always the same parity as $n$. This is related to the fact that $\esper[\E^{zB}]$ has modulus $1$ at $z=\I\pi$.
\end{remark}
\medskip



\subsubsection{Quasi powers}
\label{Subsect:QP}

Mod-$\phi$ convergent is reminiscent of the quasi-power theory
developed by Hwang \cite{Hwa96,Hwa98} --- see also \cite[Chapter IX]{FSe09}.
\begin{definition}\cite{Hwa96}
    A sequence $(X_n)$ of random variables satisfy the quasi-power hypothesis if
    \begin{equation}
        \esper[\E^{zX_n}] = \E^{\phi(n)u(z)+v(z)} \big( 1 +O(\ka_n^{-1}) \big),
        \label{EqHwangQP}
    \end{equation}
    where $\phi(n),\ka_n \to \infty$, $u(z)$ and $v(z)$ are analytic functions for $|s| < \rho$
    (with $u''(0) \ne 0$)
    and the $O$ symbol is uniform in the disk $D(0,\rho)$.    
\end{definition}
Clearly, any sequence converging mod-$\phi$ satisfies this hypothesis,
taking $\phi(n)=t_n$, $v(z)=\ln(\psi(z))$, $u(z)=\eta(z)$
(since $\psi(0)=1$, a determination of the $\ln$ always exists on a sufficiently small neighbourhood of the origin).

A major difference between mod-convergence and the quasi-power framework
is that we assume that $\eta(z)$ is the L\'evy exponent of an infinitely divisible distribution,
while Hwang does not have any hypothesis on $u(z)$ (except $u''(0) \ne 0$).
The fact that $\exp(\eta(z)) = \int_{\R} \E^{zx}\, \phi(dx)$ is important
to study deviations at scale $O(t_n)$,
since we used the inequality $|\exp(\eta(z))| \le 1$ for $z=i\xi$
in the proof of Theorem \ref{thm:mainlattice} and Proposition \ref{prop:berryesseen}.
\bigskip


At the scale $o(t_n)$, our results --- Theorems \ref{thm:cltnonlattice} and \ref{thm:cltlattice} ---
coincide with the ones of Hwang.
Note, however, that our hypotheses are slightly different.
We need $\eta(z)$ to be the Levy exponent of an infinitely divisible distribution,
while Hwang uses an hypothesis
on the speed of convergence in Equation \eqref{EqHwangQP}.
In most examples, $\eta$ is a Poisson or Gaussian Lévy exponent,
so that our hypothesis is automatically verified.
It can thus be considered as a slight improvement that 
we do not require any hypothesis on the speed of convergence
(but such an hypothesis allows us to refine our results at scale $O(t_n)$
in the lattice case, see Theorem \ref{thm:mainlattice}).

\begin{remark}[The disk or the strip?]
    In the quasi-power framework, we assume convergence of the renormalized 
    Laplace transform on a disk, while mod-$\phi$ convergence is defined
    as such convergence on the strip.
    It is thus natural to wonder which hypothesis is more natural. To this purpose, let us mention an old result of Lukacs and Szász \cite[Theorem 2]{LS52}: if $X$ is a random variable with an analytic moment generating function $\esper[\E^{zX}]$ defined on the open disk $\mathcal{D}_{(0,c)}$, then this function is automatically defined and analytic on the strip $\mathcal{S}_{(-c,c)}$. This implies that the left-hand side of Eq.~\eqref{eq:modphi} is automatically defined on a strip, as soon as it is defined on a disk. Of course it could converge on a disk and not on a strip, but we shall see throughout this paper that, in many examples, the convergence on the strip indeed occurs. Actually, in most of our examples, $c=-\infty$ and $d=+\infty$, and the distinction between disk and strip disappears as $\mathcal{D}_{(0,+\infty)}=\mathcal{S}_{(-\infty,+\infty)}=\C$.
\label{rem:diskorstrip}
\end{remark}\medskip
