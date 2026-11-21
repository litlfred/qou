---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-001-2-the-rt-invariant-for-surgeries-on-the-figure-8
section_title: "The RT-invariant for surgeries on the figure $8$ knot"
section_number: 2
pages: 10-12
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.978
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
\noindent This section is primarily intended to introduce
notation. Moreover, we present some preliminary formulas for
the colored Jones polynomial of the figure $8$ knot and for
the RT--invariants of the $3$--manifolds $M_{p/q}$.

Let $t=\exp(2\pi \I /(4r))$, $r$ an integer $\geq 2$, and let
$U_{t}$ be the modular Hopf algebra considered in
\cite[Sec.~8]{[27]}, i.e.\ $U_{t}$ is a finite-dimensional
factor of the quantum group $U_{\xi}(\frsl_{2}(\C))$,
$\xi=t^{4}$. (In \cite{[27]}, and in most literature on the
subject, $\xi$ is denoted $q$, but we use in this paper $q$
to mean something different.) For an integer $k$ we let
$$
[k] = \frac{t^{2k}-t^{-2k}}{t^{2}-t^{-2}} =
            \frac{\sin(\pi k /r)}{\sin(\pi/r)},
$$
sometimes called a quantum integer. For a knot $K$ in $S^{3}$
we denote by $K^{0}$ the knot $K$ considered as a framed knot
with framing zero. The colored Jones polynomial associated to
$U_{t}$ of a framed oriented knot $K$ with color
$\lambda \in \{1,2,\ldots,r\}$ is denoted $J_{K}(\lambda)$,
and for an oriented knot $K$ in $S^{3}$ we let $
J_{K}'(\lambda)=J_{K^{0}}(\lambda)/[\lambda]$. Here the
colors are the dimensions (as complex vector spaces) of
irreducible $U_{t}$--modules.

Let $N_{f}$ be the $3$--manifold obtained by surgery on
$S^{3}$ along $K$ with surgery coefficient $f \in \Z$. By
\cite{[16]} or \cite{[27]} the RT--invariant (at level $r-2$)
of $N_{f}$ is
\begin{equation}\label{eq:inv1}
\tau_{r}(N_{f}) =
  \alpha\sum_{k=1}^{r-1} \xi^{(k^{2}-1)f/4} [k]^{2}J_{K}'(k),
\end{equation}
where $K$ is given an arbitrary orientation. Here
$\alpha=C^{\sign(f)}\mD^{-2}$, where
\begin{eqnarray*}
\mD &=& \sqrt{\frac{r}{2}}\frac{1}{\sin(\pi/r)}, \\
C &=& \exp\left( \frac{\I\pi}{4} \frac{3(2-r)}{r} \right).
\end{eqnarray*}
We use here the normalization of \cite{[34]}. This is
$\mD^{-1}$ times the normalization of \cite{[16]} and
$C^{-b_{1}(N_{f})}\mD^{-1}$ times the normalization of
\cite{[27]}, where $b_{1}(N_{f})$ is the first Betti
number of $N_{f}$, see \cite[Appendix A]{[8]}. (In the
notation of \cite{[34]}, $C=\Delta \mD^{-1}$.)

Let us next generalize to arbitrary rational surgery. Let
$p,q$ be a pair of coprime integers with $q \neq 0$, and let
$N_{p/q}$ be the $3$--manifold obtained by surgery along $K$
with surgery coefficient $p/q$. Choose $c,d \in \Z$ such that
$B= \left( \begin{array}{ll}
                p & c \\
                q & d
                \end{array}
\right) \in \SL(2,\Z)$. Then (see e.g.\ \cite[Theorem 5.1 and
the proofs of Corollary 8.3 and Theorem 8.4]{[8]}),
$$
\tau_{r}(N_{p/q}) = \left( e^{\frac{i \pi}{4}}
 \exp \left( -\frac{i\pi}{2r} \right) \right)^{\Phi(B)
 -3\sign(pq) } \sqrt{\frac{2}{r}}\sin\left(\frac{\pi}{r}\right)
 \sum_{\lambda=1}^{r-1} [\lambda] J_{K}'(\lambda)
 \tilde{B}_{\lambda,1},
$$
where $\Phi$ is the Rademacher Phi function, see \cite{[26]},
and $\tilde{\cdot}$ is the unitary representation of
$P\SL(2,\Z)$ given by
\begin{eqnarray*}
&&\tilde{B}_{j,k} = \I \frac{\sign (q)}{\sqrt{2r|q|}}
      e^{-\frac{\I \pi}{4} \Phi(B)} \\*
 && \hspace{.5in} \times \sum_{\mu =
    \pm 1} \qsum \mu \exp \left( \frac{\I \pi}{2rq}
    [ p j^{2}- 2 \mu j (k +2rn \mu) + d (k + 2rn \mu)^{2} ]
    \right).
\end{eqnarray*}
By evaluating the sum over $\mu$ we get
\begin{eqnarray}\label{eq:rational}
&&\tau_{r}(N_{p/q}) = a(r)\qsum
       \exp\left( 2\pi ir \frac{dn^{2}}{q} \right) \\*
&& \hspace{.7in} \times \sum_{k=1}^{r-1}
    \sin\left(\frac{\pi}{q}\left[2nd-\frac{k}{r}\right]\right)
    \exp\left( \frac{\pi ir}{2q}
        \left[ p\left(\frac{k}{r}\right)^{2}
               - 4n\frac{k}{r}\right]
      \right) [k]J_{K}'(k), \nonumber
\end{eqnarray}
where
$$
a(r) = -\frac{2\sign(q)}{r\sqrt{|q|}}
        \sin\left(\frac{\pi}{r}\right)
    e^{-\frac{3\pi i}{4}\sign(pq)}\exp\left(\frac{\pi i}{2r}
               \left[ 3\sign(pq) - \frac{p}{q}
          + \dS \left(\frac{p}{q}\right)\right]\right).
$$
Here $\dS$ is the Dedekind symbol, see e.g.\ \cite{[17]}.
We note that the quantum invariant $\tau_{r}$ is independent
of the colored Jones polynomial $J_{K}'(k)$ for the top-color
$k=r$.

In the remaining part of this paper $K$ will denote the
figure $8$ knot unless explicitly stated otherwise. Recall
that $M_{p/q}$ denotes the $3$--manifold obtained by surgery
on $S^{3}$ along $K$ with surgery coefficient $p/q \in \Q$.
By an $R$--matrix calculation (see e.g.\ \cite{[11]}) we find
that
\begin{equation}\label{eq:figure8Le}
J_{K}'(\lambda) = \sum_{m=0}^{\lambda-1} \xi^{-m\lambda}
 \prod_{l=1}^{m}(1-\xi^{\lambda-l}) (1-\xi^{\lambda+l})
\end{equation}
for $\lambda=1,2,\ldots,r$, where
$\prod_{l=1}^{m} (1-\xi^{k-l}) (1-\xi^{k+l})=1$ for $m=0$. Le
and Habiro have obtained a similar formula, cf.\ \cite{[20]}.


\begin{remark}
Unitarity of the TQFT associated to $U_t$ implies that
\begin{equation}\label{eq:unitarity}
{\tau}_{r}(-M)=\overline{\tau_{r}(M)}
\end{equation}
for any $3$--manifold $M$, where $\overline{\cdot}$ means
complex conjugation. This formula also follows directly from
\cite{[16]} and the remarks concerning normalization
following (\ref{eq:inv1}).
\end{remark}


Since the figure $8$ knot is amphicheiral, $M_{-p/q}$ and
$M_{p/q}$ are orientation reversing homeomorphic. By
(\ref{eq:unitarity}) we therefore have
\begin{equation}\label{eq:mirror2}
\overline{\tau_{r}(M_{p/q})} = \tau_{r}(M_{-p/q}).
\end{equation}
This formula also follows directly by (\ref{eq:rational}) and
the facts that $J_{K}'(\lambda)$ is real and $S(-p/q)=-S(p/q)$.
That $J_{K}'(\lambda)$ is real follows by amphicheirality of
$K$ but can also be seen directly from (\ref{eq:figure8Le}) by
\begin{eqnarray*}
J_{K}'(\lambda) &=& \sum_{m=0}^{\lambda-1} \prod_{l=1}^{m}
   \xi^{-\lambda/2}\xi^{l/2}(1-\xi^{\lambda-l})
   \xi^{-\lambda/2}\xi^{-l/2}(1-\xi^{\lambda+l}) \\
 &=& \sum_{m=0}^{\lambda-1} \prod_{l=1}^{m}
       (\xi^{(\lambda-l)/2}-\xi^{-(\lambda-l)/2})
       (\xi^{(\lambda+l)/2}-\xi^{-(\lambda+l)/2}) \\
 &=& \sum_{m=0}^{\lambda-1} (-4)^{m} \prod_{l=1}^{m}
       \sin(\pi(\lambda-l)/r)\sin(\pi(\lambda+l)/r).
\end{eqnarray*}
By (\ref{eq:rational}) and (\ref{eq:figure8Le}) we get the
following preliminary formula for the RT--invariants of the
manifolds $M_{p/q}$:
\begin{eqnarray}\label{eq:inv2}
\tau_{r}(M_{p/q}) &=& \frac{ia(r)}{2\sin(\pi/r)}\qsum
   \exp\left( 2\pi ir \frac{dn^{2}}{q} \right) \nonumber \\*
&& \times \sum_{k=1}^{r-1} \exp\left( \frac{\pi ir}{2q}
\left[p\left(\frac{k}{r}\right)^{2}-4n\frac{k}{r}\right]
                   \right) \sin\left(\frac{\pi}{q}
         \left[2nd-\frac{k}{r}\right]\right) \nonumber \\*
&& \times \sum_{m=0}^{r-1}
         \frac{\xi^{-(m+1/2)k}}{(1-\xi^{k})}
         \prod_{l=0}^{m} (1-\xi^{k-l}) (1-\xi^{k+l}).
\end{eqnarray}
