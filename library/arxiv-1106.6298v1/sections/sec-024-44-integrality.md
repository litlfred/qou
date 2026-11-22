---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS"
section_id: sec-024-44-integrality
section_title: "Integrality"
section_number: 4.4
pages: 17-17
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariants."
---
The proof of integrality of the SO(3) WRT invariants for
all  roots of unity and for all 3--manifolds is given in \cite{BL}.
Note that even restricted to rational homology 3--spheres,
this fact requires a separate proof, since
 the existence
of $I_M \in \R_b$ does not imply  integrality of the WRT invariants,
unless $b= 1$. In this subsection
we define a subring $\Gamma_b \subset \R_b$, such that
for any $f\in \Gamma_b$, $\ev_\xi(f)\in \Z[\xi]$.


The fact that $I_{M,1}$ belongs
to this subring was proved in \cite{BL}. We conjecture that
this holds in general.

For any divisor $c$ of $b$, let us decompose
$\N=\cup_{c|b}\; c\; \N_{b/c}$. Then
$$\Z[1/b][q]^\N=\prod_{c|b} \Z[1/b][q]^{c\,\N_{b/c}}\, .$$
Analogously, we have
$\Gamma_b=\prod_{c|b} \Gamma_{b,c}$, where
$\Gamma_{b,c} \subset \Z[1/b][q]^{c\, \N_{b/c}}$ is defined as follows.

Let $A_{b,c}=\Z[e_c][q^{\pm 1}, q^{\pm c/b}]$.
Put $t=q^{c/b}$ and let $A^{(m)}_{b,c}$ be the algebra generated over  $A_{b,c}$
by
$$\frac{(t;t)_m}{(q^c;q^c)_{m}}\;
 \frac{(e_c;e_c)_{(c-1)/2}}{\widetilde {(q;q)_m}}\; $$
where $$\widetilde{(q;q)_m}=\prod^m_{i=1, c\, \nmid\,  i}(1-q^i)\, .$$
Then
every element $f\in \Gamma_{b,c}$ has a presentation
$$f=\sum^\infty_{m=0} f_m \; \frac{(q^{m+1};q)_{m+1}}{1-q}
$$
with $f_m\in A^{(m)}_{b,c}$.
For any root of unity $\xi$ of odd order $r$ with $(r,b)=c$
and $f\in \Gamma_{b,c}$, we have
$$ \ev_\xi (f)= \ev_\xi \left(\sum^{(r-3)/2}_{m=0} f_m \frac{(q^{m+1};q)_{m+1}}{1-q}
\right)\; .$$








Observe that for $m<(r-1)/2$,
$$
\ev_\xi (\widetilde {(q;q)_{m}}) \; \mid\;
(e_c;e_c)_{(c-1)/2}
\;\;\text{and}\;\;
\ev_\xi \left(\frac{(t;t)_m}{(q^c;q^c)_{m}}
\right) \in \Z[\xi]\, .$$



\begin{conjecture}
For any $M\in \M_b$,
there exists an invariant $I'_M \in \Gamma_b$, such that
for any root of unity $\xi$ of odd order
$\ev_\xi(I'_M)=\tau_M(\xi)$.
\end{conjecture}

We also expect that $\Gamma_{b,b}$ is determined by its Taylor
expansion at $e_b$.
