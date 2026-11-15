---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-042-102-higher-order-alexander-polynomials
section_title: "Higher order Alexander polynomials"
section_number: 10.2
pages: 32-33
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.985
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
We now recall the construction of what are arguably the most interesting examples of $\phi$--compatible homomorphisms from $\pi_1(N)$ to a non--commutative Laurent polynomial ring.
The ideas of this section are due to Cochran and Harvey.

\begin{theorem}\label{thm:tfa}
Let $\gamma$ be a torsion--free solvable group and let $\mathbb{F}$ be a commutative field. Then the
following hold.
\begin{enumerate}
\item  $\mathbb{F}[\Gamma]$  is an Ore domain, in particular it embeds in its classical right ring of
quotients $\mathbb{K}(\Gamma)$.
\item $\mathbb{K}(\Gamma)$ is flat over $\mathbb{F}[\Gamma]$.
\end{enumerate}
\end{theorem}

Indeed, it follows from \cite{KLM88}  that $\mathbb{F}[\Gamma]$ has no zero divisors. The first part now follows from
\cite[Corollary~6.3]{DLMSY03}. The second part is a well--known property of Ore
localizations. We call $ \mathbb{K}(\Gamma)$ the \emph{Ore localization} of
$\mathbb{F}[\Gamma]$. In \cite{COT03} the notion of a poly--torsion--free--abelian (PTFA) group is introduced,
it is well--known that these groups are torsion--free and solvable.

\begin{remark}
\begin{enumerate}
\item
It follows from Higman's theorem \cite{Hi40} that the above theorem also holds for groups which are locally indicable and amenable.
We will not make use of this, but note that throughout this section `torsion--free solvable' could be replaced by `locally indicable and amenable'.
\item  Note that the poly--torsion--free--abelian (PTFA) groups introduced in \cite{COT03} are solvable and torsion--free.
\end{enumerate}
\end{remark}

We need the following definition.

\begin{definition} Let $\pi$ be a group, $\phi:\pi \to \mathbb{Z}$ an epimorphism and
$\varphi:\pi\to \gamma$ an epimorphism to a torsion--free solvable group $\gamma$ such that there
exists a map $\phi_\Gamma:\Gamma\to \mathbb{Z}$ (which is necessarily unique) such that
 \[   \xymatrix {
 \pi \ar[dr]_{\phi} \ar[r]^{\varphi} &\Gamma \ar[d]^{\phi_\Gamma}\\& \mathbb{Z} }
     \]
 commutes. Following \cite[Definition~1.4]{Ha06} we call $(\varphi,\phi)$
an {\em admissible pair}.
\end{definition}

Now let $(\varphi:\pi_1(N)\to \Gamma,\phi)$ be an admissible pair for $\pi_1(N)$. In the following we
denote $\ker\{\phi:\Gamma\to \mathbb{Z}\}$ by $\Gamma'(\phi)$. When the homomorphism $\phi$ is understood we will
write $\Gamma'$ for $\Gamma'(\phi)$. Clearly $\Gamma'$ is still solvable and torsion--free. Let
$\mathbb{F}$ be any commutative field and $\mathbb{K}(\Gamma')$ the Ore localization of $\mathbb{F}[\Gamma']$. Pick an element $\mu
\in \gamma$ such that $\phi(\mu)=1$. Let $\gamma:\mathbb{K}(\Gamma')\to \mathbb{K}(\Gamma')$ be the homomorphism given by
$\gamma(a)=\mu a\mu^{-1}$. Then we get a ring homomorphism
\[ \begin{array}{rcl} \mathbb{Z}[\Gamma]&\to& \mathbb{K}(\Gamma')_\gamma[t^{\pm 1}]\\[1mm]
    g &\mapsto& (g\mu^{-\phi(g)}t^{\phi(g)}), \mbox{ for $g\in \gamma$.}\end{array} \]
    We denote this ring homomorphism again by $\varphi$.
    It is clear that $\varphi$ is $\phi$--compatible. Note that the ring $\mathbb{K}(\Gamma')[t^{\pm 1}]$ and hence the
above representation depends on the choice of $\mu$. We will nonetheless suppress $\mu$ in the
notation since different choices of splittings give isomorphic rings.
We will refer to a non--commutative Alexander polynomial corresponding to such a group homomorphism
as a \emph{higher order Alexander polynomial}.

An important example of admissible pairs is provided by Harvey's rational derived series of a group
$\gamma$ (cf. \cite[Section~3]{Ha05}). Let $\gamma_r^{(0)}=\gamma$ and define inductively
\[ \gamma_r^{(n)}=\big\{ g\in \gamma_r^{(n-1)} | \, g^k \in \big[\gamma_r^{(n-1)},\gamma_r^{(n-1)}\big] \mbox{ for some }k\in \mathbb{Z} \setminus \{0\} \big\}.\]
Note that $\gamma_r^{(n-1)}/\gamma_r^{(n)}\cong
\big(\gamma_r^{(n-1)}/\big[\gamma_r^{(n-1)},\gamma_r^{(n-1)}\big]\big)/\mbox{$\mathbb{Z}$--torsion}$.
 By \cite[Corollary~3.6]{Ha05} the quotients $\Gamma/\gamma_r^{(n)}$ are solvable and torsion--free
for any $\gamma$ and any $n$. If $\phi:\Gamma\to \mathbb{Z}$ is an epimorphism, then  $(\Gamma\to \Gamma/\gamma_r^{(n)},\phi)$ is
an admissible pair for $(\Gamma,\phi)$ for any $n>0$.

For example if $K$ is a knot, $\gamma=\pi_1(S^3\setminus \nu K)$, then it follows from \cite{St74} that
$\Gamma^{(n)}_r=\Gamma^{(n)}$, i.e. the rational derived series equals the ordinary derived series (cf. also
\cite{Co04} and \cite{Ha05}).

\begin{remark}
The Achilles heel of the higher order Alexander polynomials is that they are unfortunately difficult to compute
in practice. We refer to \cite{Sa07} for some ideas on how to compute higher order Alexander polynomials in some cases.
\end{remark}
