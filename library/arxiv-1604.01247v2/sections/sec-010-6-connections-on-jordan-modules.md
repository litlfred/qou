---
doc_id: arxiv-1604.01247v2
doc_title: "Exceptional quantum geometry and particle physics"
section_id: sec-010-6-connections-on-jordan-modules
section_title: "Connections on Jordan modules"
section_number: 6
pages: 30-32
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
text_source: latex
latex_prose_ratio: 0.758
latex_coverage_ratio: 1.0
doc_brief: "Exceptional quantum geometry and particle physics — Based on an interpretation of the quark-lepton symmetry in t erms of the unimodularity of the color group SU (3) and on the existence of 3"
---
## Derivation-based connections. First definition

Let $J$ be a unital Jordan algebra with center (= centroid) $Z(J)$ and let ${\mbox{Der}}(J)$ be the Lie algebra and $Z(J)$-module of derivations of $J$. A *(derivation-based) connection* $\nabla$ on a unital $J$-module $M$ is a linear mapping $X\mapsto \nabla_X$ of ${\mbox{Der}}(J)$ into the linear endomorphisms of $M$ such that $$\begin{equation}
 \left\{
 \begin{array}{l}
 \nabla_X(xm)=X(x)m +x\nabla_X(m)\\
 \\
 \nabla_{zX}(m)=z\nabla_X(m)
 \end{array}
 \right.
  \label{covder}
\end{equation}$$ for any $m\in M$, $x\in J$ and $z\in Z(J)$.\
It follows from this definition that the difference $\nabla-\nabla'$ between 2 connections on $M$ is a $Z(J)$-linear mapping of ${\mbox{Der}}(J)$ into the $Z(J)$-module of all the $J$-module endomorphisms of $M$.\
It also follows that $$\begin{equation}
R_{X,Y}=[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}
\end{equation}$$ satisfies $$\begin{equation}
 \left\{
 \begin{array}{l}
 R_{X,Y}(xm)=x R_{X,Y}(m)\\
 \\
 R_{zX,Y}(m)=z R_{X,Y}(m)
 \end{array}
 \right.
 \label{curv}
\end{equation}$$ in other words that $R$ is a $Z(J)$-linear mapping of $\wedge^2_{Z(J)}{\mbox{Der}}(J)$ into the $Z(J)$-module of all the $J$-module endomorphism of $M$ which will be referred to as the *curvature* of $\nabla$.\
It is clear that if ${\mathfrak g}$ is a Lie subalgebra and a $Z(J)$-submodule of ${\mbox{Der}}(J)$, the restriction of ([\[covder\]](#covder){reference-type="ref" reference="covder"}) to ${\mathfrak g}$, i.e. for $X\in{\mathfrak g}$, makes sense and the corresponding notion will be referred to as a *derivation-based ${\mathfrak g}$-connection* on $M$.

## Derivation-based connections. Second definition

Let $J$, $Z(J)$, ${\mbox{Der}}(J)$ and $M$ be as in §6.1 and let $\Omega^n_{{\mbox{\tiny Der}}}(M)$ be the $J$-module of all $n$-$Z(J)$-linear antisymmetric mapping of ${\mbox{Der}}(J)$ into $M$, which means that $\Phi\in \Omega^n_{{\mbox{\tiny Der}}}(M)$ is a $Z(J)$-linear mapping $$\Phi: \wedge^n_{Z(J)}{\mbox{Der}}(J)\rightarrow M$$ with the notations of §5.4. The graded $J$-module $\Omega_{\mbox{\tiny Der}}(M)=\oplus_{n\geq 0}\Omega^n_{\mbox{\tiny Der}}(M)$ in naturally a graded Jordan module over the graded Jordan algebra $\Omega_{\mbox{\tiny Der}}(J)$: The product of $\omega\in \Omega^m_{\mbox{\tiny Der}}(J)$ with $\Phi\in\Omega^n_{\mbox{\tiny Der}}(M)$ is the element $\omega\Phi\in\Omega^{m+n}_{\mbox{\tiny Der}}(M)$ obtained by product of evaluations on derivations followed by antisymmetrization in the derivations. A *(derivation-based) connection* on $M$ is a linear endomorphism $\nabla$ of $\Omega_{\mbox{\tiny Der}}(M)$ such that $$\begin{equation}
 \left\{
 \begin{array}{l}
 \nabla(\Omega^n_{\mbox{\tiny Der}}(M))\subset \Omega^{n+1}_{\mbox{\tiny Der}}(M)\\
 \\
 \nabla(\omega \Phi)=d(\omega) \Phi + (-1)^m\omega\nabla (\Phi)
 \label{covdiff}
 \end{array}\right.
\end{equation}$$ for any $m, n\in \mathbb N$, $\omega\in \Omega^m_{\mbox{\tiny Der}}(J)$ and $\Phi\in \Omega_{\mbox{\tiny Der}}(M)$. Let $\nabla$ be such a connection and define $\nabla_Xm$ by $$\begin{equation}
 \nabla(m)(X)
 \label{cocod}
\end{equation}$$ for $m\in M=\Omega^0_{\mbox{\tiny Der}}(M)$ and $X\in {\mbox{Der}}(J)$. Then $X\mapsto \nabla_X$ is a connection on $M$ in the sense of §6.1. Conversely if $X\mapsto \nabla_X$ is a connection in the sense of §6.1 one defines $\nabla$ on $\Omega^n_{\mbox{\tiny Der}}(M)$ by $$\begin{equation}
 \begin{array}{ll}
 \nabla(\Phi)(X_0,\cdots,X_n) & = \sum^n_{p=0}(-1)^p\nabla_{X_p}(\Phi(X_0,\stackrel{p\atop \vee}{\cdots\cdots}, X_n))\\
 &+ \sum_{0\leq r<s\leq n}(-1)^{r+s}\ \Phi([X_r,X_s],X_0,\stackrel{r\atop \vee}{\cdots} \stackrel{s\atop \vee}{\cdots},X_n)
 \end{array}
 \label{evcov}
\end{equation}$$ for $\Phi\in \Omega^n_{\mbox{\tiny Der}}(M)$, $X_p\in{\mbox{Der}}(J)$. This $\nabla$ satisfies the axioms ([\[covdiff\]](#covdiff){reference-type="ref" reference="covdiff"}). We shall refer to $\nabla$ as the *covariant differential* while $\nabla_X$ for $X\in {\mbox{Der}}(J)$ will be refered to as the covariant *derivative along* $X$.\
From the axioms ([\[covdiff\]](#covdiff){reference-type="ref" reference="covdiff"}), it follows that one has $$\begin{equation}
 \nabla^2(\omega\Phi)=\omega\nabla^2(\Phi)
 \label{covcurv}
\end{equation}$$ for any $\omega\in \Omega_{\mbox{\tiny Der}}(J)$ and $\Phi\in\Omega_{\mbox{\tiny Der}}(M)$ furthermore $$\nabla^2(m)(X,Y)=R_{X,Y}(m)$$ for $m\in M$. Thus $\nabla^2$ is an homomorphism of $\Omega_{\mbox{\tiny Der}}(J)$-module which is also called *the curvature* of $\nabla$ since it is expressible in terms of the $R_{X,Y}$ and conversely.

## General connections

Let $\Omega=\oplus_{n\geq 0}\Omega^n$ be a differential graded Jordan algebra and let $\Gamma=\oplus_{n\geq 0}\Gamma^n$ be a graded Jordan module over the graded Jordan algebra $\Omega$, (the axioms for this notion are easy to guess). A *connection* on $\Gamma$ will be defined to be a linear endomorphism $\nabla$ of $\Gamma$ satisfying $$\begin{equation}
 \left\{
\begin{array}{l}
\nabla(\Gamma^n)\subset \Gamma^{n+1}\\
\nabla(\omega\Phi)=d(\omega)\Phi+(-1)^m\omega\nabla(\Phi)
\label{gcovd}
\end{array}
\right.
\end{equation}$$ for $m, n\in \mathbb N$, $\omega\in\Omega^m$ and $\Phi\in \Gamma$.\
The axioms ([\[gcovd\]](#gcovd){reference-type="ref" reference="gcovd"}) imply that one has $$\begin{equation}
\nabla^2(\omega\Phi)=\omega\nabla^2(\Phi)
\label{gcurv}
\end{equation}$$ for any $\omega\in\Omega$ and $\Phi\in \Gamma$, so $\nabla^2$ is an homogeneous $\Omega$-module homomorphism of degree 2 which will be refereed to as the *curvature* of the connnection $\nabla$.\
Notice that the formalism of 6.2 is a particular case of this formalism and that within it, the Bianchi identity reduces to the trivial identity $$\nabla\nabla^2=\nabla^2\nabla$$ that is to the associativity of the composition of the endomorphism $\nabla$.
