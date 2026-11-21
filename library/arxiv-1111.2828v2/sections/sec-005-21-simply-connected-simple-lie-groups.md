---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-005-21-simply-connected-simple-lie-groups
section_title: "Simply connected, simple Lie groups"
section_number: 2.1
pages: 8-9
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.909
latex_coverage_ratio: 0.952
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{sub.simplelie}

If $G$ is simply connected and simple, $H^1(G;\Z)$ and $H^2(G;\Z)$ are 
trivial, and $H^3(G;\Z)\cong\Z$. Hence, by the Serre spectral sequence 
for the universal bundle, we have an isomorphism
\begin{equation}
S\colon H^{4}(BG;\Z)\cong H^{3}(G;\Z)\cong\Z
\end{equation}
called the \emph{suspension}.
The Killing form on $G$ defines an invariant polynomial $B\in I^2(G;\F)$, 
and since $B$ is real on the maximal compact subgroup $K$ of $G$, $W(B)$ 
is a real class. Hence, there exists a unique positive real number $\alpha$ 
such that $W(\alpha B)$ is a generator of $H^4(BG;4\pi^2\Z)$. We refer to 
$\alpha B$ as the \emph{renormalized Killing form}, and denote the 
Cheeger-Chern-Simons class $S_{\alpha B,W(\alpha B)}$ by $\widehat c$. 

Recall that every class in $H^3(G;\F)$ can be represented by a $G$-invariant 
$3$-form.
The following is well known (see e.g.~Kamber-Tondeur~\cite[(5.74) p.~116]{KamberTondeur}).

\begin{proposition} Let $P\in I^2(G;\F)$. The suspension of $W(P)$ is 
represented by the invariant $3$-form
\begin{equation}\lbl{sigmaPformula}
\sigma(P)=-\frac{1}{6}P(\omega\wedge[\omega,\omega])\in\Omega^3(G;\F)^G
\end{equation}
where $\omega$ is the Maurer-Cartan form on $G$.\qed
\end{proposition}

Let $E\to M$ be a $G$-bundle with flat connection $\theta$. We can view 
$\theta$ as a map $\mathfrak g^*\to\Omega^1(E;\F)$, so by taking exterior 
powers, $\theta$ induces a map
\begin{equation}
\theta\colon\Omega^3(G)^G=\wedge^3(\mathfrak g^*)\to\Omega^3(E;\F).
\end{equation}

Note that $\theta(\sigma(P))=-\frac{1}{6}P(\theta\wedge[\theta,\theta])$. 
In the following, $P$ denotes the renormalized Killing form.

\begin{proposition}[{\cite[Proposition~2.8]{CheegerSimons}}]
Let $E\to M$ be a $G$-bundle, with flat connection $\theta$, over a closed 
$3$-manifold $M$.
The cohomology class $\widehat c(E)\in H^3(M;\F/4\pi^2\Z)$ satisfies 
\begin{equation}
\lbl{CSintegral}
\widehat c(E)([M])=\int_{M} s^*\big(\theta(\sigma(P))\big)\in \F/4\pi^2\Z,
\end{equation}
where $s$ is a section of $E$ (which exists since $G$ is $2$-connected).\qed
\end{proposition}

\begin{remark}
Since $\sigma(P)\in H^3(G;4\pi^2\Z)$ is a generator, it follows that a 
change of section changes the integral by a multiple of $4\pi^2\Z$.
\end{remark}

\begin{example}
\lbl{SLnExample}
For $G=\SL(n,\C)$, the renormalized killing form $P$ equals $\frac{1}{2}\Tr$, 
where $\Tr$ is the trace form $(A,B)\mapsto \Tr(AB)$. For a flat connection, $d\theta=-\frac{1}{2}[\theta,\theta]=-\theta\wedge\theta$, so~\eqref{CSintegral} yields
\begin{equation}
\widehat c(E)([M])=\frac{1}{2}\int_{M} 
s^*\big(\Tr(\theta\wedge d\theta+\frac{2}{3}\theta\wedge\theta\wedge\theta)\big)\in 
\C/4\pi^2\Z
\end{equation}
recovering the Chern-Simons integral~\eqref{ChernSimonsintegral}. Note that $P$ also equals the (renormalized) second Chern-polynomial $c_2$. 
It thus follows that $\widehat c=\widehat c_2$. 
\end{example}
