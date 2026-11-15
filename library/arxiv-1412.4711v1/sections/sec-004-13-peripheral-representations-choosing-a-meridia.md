---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT"
section_id: sec-004-13-peripheral-representations-choosing-a-meridia
section_title: "Peripheral representations: choosing a meridian and a longitude"
section_number: 1.3
pages: 5-6
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.934
doc_brief: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
\label{ss:lm}
\newcommand{\Hol}{\mathrm{Hol}}\newcommand{\periph}{\mathrm{periph}}

By considering decorated versions of the representations, we also grant an easy parametrization 
for the \emph{peripheral representation}, that is the restriction of the representation to the fundamental group of the peripheral torus. This is more carefully studied in \cite[Section 1]{G}. Recall that $M$ is a $1$-cusped hyperbolic $3$-manifold. Let $\mathbb T$ be the peripheral torus.

First, let $\Gamma_\mathrm{para}$ be the set of parabolic elements of $\Gamma$ (the identity is not considered parabolic). 
Each element $\gamma$ of $\Gamma_\mathrm{para}$ stabilizes a unique cusp $p_\gamma\in\mathcal P$. 
Consider a decorated representation $(\rho,\phi)\in \DecHom(\Gamma,G)$. 
Let $D$ be the diagonal group of $G$. Then, in any basis adapted to the flag $\phi(p_\gamma)$,
$\rho(\gamma)$ is an upper-diagonal matrix. Moreover, the diagonal part of $\rho(\gamma)$ is invariant under the action of $G$ \cite{G}.
Hence we get a $G$-invariant map: 
$$\DecHom(\Gamma,G)  \to \{\Gamma_\mathrm{para}\to D\}.$$
\newcommand{\dec}{\mathrm{dec}}


In order to parametrize the peripheral representations, we fix, \emph{once for all}, the following choices: 
\begin{itemize}
\item $\pi_1(\mathbb T)\simeq \mathbb Z^2$, through the choice of a longitude $l$ and a meridian $m$ of $\mathbb T$.
\item An injection $\pi_1(\mathbb T)\to \Gamma=\pi_1(M)$.
\end{itemize}

A representation in $\Hom(\Gamma,G)$ may be restricted to $\pi_1(\mathbb T)$. This gives an algebraic map of \emph{restriction}:\newcommand{\restr}{\mathrm{restr}}
$$X(\Gamma,G)\xrightarrow{\restr}X(\mathbb Z^2,G).$$
Moreover, in the decorated case, as $\pi_1(\mathbb T)$ is composed of parabolic elements, we get a map, called \emph{peripheral holonomy map} and denoted by $\Hol_\periph$:
$$\DecX(\Gamma,G)\xrightarrow{\Hol_\periph}X(\mathbb Z^2,D)=:\DecX(\mathbb Z^2,G).$$
It consists, at the level of decorated representations, in sending a decorated representation to the diagonal part of the restriction restricted to $\pi_1(\mathbb T)$.

The last step of the parametrization is achieved by noting that $D$ is an affine algebraic group isomorphic to $(\bC^*)^{n-1}$ in the case $G=\PGL(n,\bC)$ or $\SL(n,\bC)$. We fix \emph{once for all} such an isomorphism. Using this, the space $\DecX(\mathbb Z^2,G)=X(\mathbb Z^2,D)$ is isomorphic to $(\bC^*)^{2(n-1)}$. This is the desired parametrization of the peripheral representations.

 In the case of $\PGL(3,\bC)$, we choose (for computational reasons, see section \ref{computations}) more precisely to use the isomorphism between $D$ and $(\bC^*)^2$ given by:
$$\begin{pmatrix} L^*&&\\&1&\\&&L\end{pmatrix}\quad \mapsto\quad (L,L^*).$$
 So the space $X(\mathbb Z^2,D)$ is isomorphic to $(\bC^*)^4$. A representation such that the diagonal part of the longitude and the meridian are:
 \[
\rho(l) = \left[ \begin{matrix}
  L^* & \ast & \ast\\
    0 & 1 & \ast\\
    0 & 0 & L
  \end{matrix} \right]\quad \textrm{and}\quad \rho(m) = \left[ \begin{matrix}
  M^* & \ast & \ast\\
    0 & 1 & \ast\\
    0 & 0 & M
  \end{matrix} \right]
 \]
will be represented by the coordinates $(L,L^*,M,M^*)$ (the choice is made to be compatible with the one 
we used in \cite{BFG}).



\begin{comment}
Denote by $\chi^{\dec}_{\rho,\phi}$ the map $\Gamma\to D\simeq \bC^{n-1}$ defined by: 
\begin{itemize}
\item if $\gamma$ is not parabolic, send it to $\frac1{n-1}(\tr^n(\rho(\gamma)),\ldots,\tr^n(\rho(\gamma)))\in\bC^{n-1}$.
\item $\gamma$ is parabolic, send it to $\Hol_\periph(\gamma)$.
\end{itemize}

Then a slight variation of the non-decorated case gives

\begin{pro}  The map 
$$ 
\DecX(  \Gamma, G)\rightarrow \{\textrm{decorated characters of }\Gamma\} 
$$
induced by $(\rho,\phi) \mapsto \chi^{\dec}_{\rho,\phi}$ is a bijection.
\end{pro}
\end{comment}
