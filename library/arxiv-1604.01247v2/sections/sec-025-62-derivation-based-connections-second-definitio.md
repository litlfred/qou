---
doc_id: arxiv-1604.01247v2
doc_title: "Exceptional quantum geometry and particle physics"
section_id: sec-025-62-derivation-based-connections-second-definitio
section_title: "Derivation-based connections. Second definition"
section_number: 6.2
pages: 30-32
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.949
doc_brief: "Exceptional quantum geometry and particle physics — Based on an interpretation of the quark-lepton symmetry in terms of the unimodularity of the color group SU(3) and on the existence of 3"
---
Let $J$, $Z(J)$, ${\mbox{Der}}(J)$ and $M$ be as in §6.1 and let $\Omega^n_{{\mbox{\tiny Der}}}(M)$ be the $J$-module of all $n$-$Z(J)$-linear antisymmetric mapping of ${\mbox{Der}}(J)$ into $M$, which means that $\Phi\in \Omega^n_{{\mbox{\tiny Der}}}(M)$ is a $Z(J)$-linear mapping $$\Phi: \wedge^n_{Z(J)}{\mbox{Der}}(J)\rightarrow M$$ with the notations of §5.4. The graded $J$-module $\Omega_{\mbox{\tiny Der}}(M)=\oplus_{n\geq 0}\Omega^n_{\mbox{\tiny Der}}(M)$ in naturally a graded Jordan module over the graded Jordan algebra $\Omega_{\mbox{\tiny Der}}(J)$: The product of $\omega\in \Omega^m_{\mbox{\tiny Der}}(J)$ with $\Phi\in\Omega^n_{\mbox{\tiny Der}}(M)$ is the element $\omega\Phi\in\Omega^{m+n}_{\mbox{\tiny Der}}(M)$ obtained by product of evaluations on derivations followed by antisymmetrization in the derivations. A *(derivation-based) connection* on $M$ is a linear endomorphism $\nabla$ of $\Omega_{\mbox{\tiny Der}}(M)$ such that $$\left\{
 \begin{array}{l}
 \nabla(\Omega^n_{\mbox{\tiny Der}}(M))\subset \Omega^{n+1}_{\mbox{\tiny Der}}(M)\\
 \\
 \nabla(\omega \Phi)=d(\omega) \Phi + (-1)^m\omega\nabla (\Phi)
 \label{covdiff}
 \end{array}\right.$$ for any $m, n\in \mathbb N$, $\omega\in \Omega^m_{\mbox{\tiny Der}}(J)$ and $\Phi\in \Omega_{\mbox{\tiny Der}}(M)$. Let $\nabla$ be such a connection and define $\nabla_Xm$ by $$\nabla(m)(X)
 \label{cocod}$$ for $m\in M=\Omega^0_{\mbox{\tiny Der}}(M)$ and $X\in {\mbox{Der}}(J)$. Then $X\mapsto \nabla_X$ is a connection on $M$ in the sense of §6.1. Conversely if $X\mapsto \nabla_X$ is a connection in the sense of §6.1 one defines $\nabla$ on $\Omega^n_{\mbox{\tiny Der}}(M)$ by $$\begin{array}{ll}
 \nabla(\Phi)(X_0,\cdots,X_n) & = \sum^n_{p=0}(-1)^p\nabla_{X_p}(\Phi(X_0,\stackrel{p\atop \vee}{\cdots\cdots}, X_n))\\
 &+ \sum_{0\leq r<s\leq n}(-1)^{r+s}\ \Phi([X_r,X_s],X_0,\stackrel{r\atop \vee}{\cdots} \stackrel{s\atop \vee}{\cdots},X_n)
 \end{array}
 \label{evcov}$$ for $\Phi\in \Omega^n_{\mbox{\tiny Der}}(M)$, $X_p\in{\mbox{Der}}(J)$. This $\nabla$ satisfies the axioms ([\[covdiff\]](#covdiff){reference-type="ref" reference="covdiff"}). We shall refer to $\nabla$ as the *covariant differential* while $\nabla_X$ for $X\in {\mbox{Der}}(J)$ will be refered to as the covariant *derivative along* $X$.\
From the axioms ([\[covdiff\]](#covdiff){reference-type="ref" reference="covdiff"}), it follows that one has $$\nabla^2(\omega\Phi)=\omega\nabla^2(\Phi)
 \label{covcurv}$$ for any $\omega\in \Omega_{\mbox{\tiny Der}}(J)$ and $\Phi\in\Omega_{\mbox{\tiny Der}}(M)$ furthermore $$\nabla^2(m)(X,Y)=R_{X,Y}(m)$$ for $m\in M$. Thus $\nabla^2$ is an homomorphism of $\Omega_{\mbox{\tiny Der}}(J)$-module which is also called *the curvature* of $\nabla$ since it is expressible in terms of the $R_{X,Y}$ and conversely.
