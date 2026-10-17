---
doc_id: arxiv-1205.1453v2
doc_title: "An asymptotic formula of the divergent bilateral basic hypergeometric series"
section_id: sec-002-3-an-asymptotic-formula-of-the-divergent-series
section_title: "An asymptotic formula of the divergent series 10(a;-;q,x)"
section_number: 3
pages: 7-8
source_pdf: 1205.1453v2.pdf
source_sha256: 29d1b1fd9466a3d8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.792
latex_coverage_ratio: 1.0
doc_brief: "An asymptotic formula of the divergent bilateral basic hypergeometric series — We show an asymptotic formula of the divergent bilateral basic hypergeometric series 1ψ0(a; −; q, ·) with using the"
---
In this section, we show an asymptotic formula of the divergent series ${}_1\psi_0(a;-;q,x)$. At first, we review Ramanujan's sum for ${}_1\psi_1(a;b;q,z)$ and its property. Ramanujan gives the following sum [@Hardy] $${}_1\psi_1(a;b;q,z)=\frac{(q,b/a,az,q/az;q)_\infty}{(b,q/a,z,b/az;q)_\infty},\qquad \left|b/a\right|<|z|<1.
\label{Rsum}$$ We can regard this sum as a $q$-analogue of the bilateral binomial theorem [@Horn] as follows;

**Theorem.** *(Horn [@Horn])* *If $z$ is a complex number such that $|z|=1$, we have*$${}_1H_1(\alpha ;\beta ;z)=\frac{\Gamma (\beta )\Gamma (1-\alpha )}{\Gamma (\beta -\alpha )}\frac{(1-z)^{\beta -\alpha -1}}{(-z)^{\beta -1}},
\label{bbt}$$ *provided that $\Re (\beta -\alpha )>1$.*

Let $z$ is a complex number such that $-\pi <\arg z <\pi$. The summation [\[Rsum\]](#Rsum){reference-type="eqref" reference="Rsum"} is rewritten by $$\frac{(q,b/a,az,q/az;q)_\infty}{(b,q/a,z,b/az;q)_\infty}
=\frac{(q,b/a;q)_\infty}{(b,q/a;q)_\infty}\frac{\theta (-az)}{\theta (-aqz/b)}\frac{(aqz/b;q)_\infty}{(z;q)_\infty}.
\label{bin3}$$ In [\[bin3\]](#bin3){reference-type="eqref" reference="bin3"}, we put $a=q^\alpha$ and $b=q^\beta$ (with $\Re (\beta -\alpha )>1$), we obtain $${}_1\psi_1 (q^\alpha ;q^\beta ;q,z)
=\frac{\Gamma_q(\beta )\Gamma_q (1-\alpha )}{\Gamma_q(\beta -\alpha )}
\frac{\theta (q^\alpha (-z))}{\theta (q^{\alpha +1-\beta }(-z))}
\frac{(q^{\alpha +1-\beta}z;q)_\infty}{(z;q)_\infty},
\label{qbb}$$ where $|q^{\beta -\alpha}|<|z|<1$. Combining [\[limgamma\]](#limgamma){reference-type="eqref" reference="limgamma"}, [\[limt1\]](#limt1){reference-type="eqref" reference="limt1"} and [\[limbin\]](#limbin){reference-type="eqref" reference="limbin"}, we can check out that the limit $q\to 1-0$ of [\[qbb\]](#qbb){reference-type="eqref" reference="qbb"} gives the bilateral binomial theorem [\[bbt\]](#bbt){reference-type="eqref" reference="bbt"}, provided that $-\pi <\arg z <\pi$.

The bilateral basic hypergeometric series ${}_1\psi_1(a;b;q,z)$ satisfies the $q$-difference equation $$\left(\frac{b}{q}-az\right)u(qz)+(z-1)u(z)=0.
\label{bqua}$$ We consider the degeneration of the equation [\[bqua\]](#bqua){reference-type="eqref" reference="bqua"} in the next section.
