---
doc_id: arxiv-math-0603444v2
doc_title: "QUASIHOMOGENEITY OF ISOLATED HYPERSURFACE SINGULARITIES AND LOGARITHMIC COHOMOLOGY"
section_id: sec-002-3-proof-of-the-theorem
section_title: "Proof of the theorem"
section_number: 3
pages: 2-5
source_pdf: 0603444v2.pdf
source_sha256: 46edfcddca963d08
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.931
doc_brief: "QUASIHOMOGENEITY OF ISOLATED HYPERSURFACE SINGULARITIES AND LOGARITHMIC COHOMOLOGY — We characterize quasihomogeneity of isolated hypersurface singu- larities by the injectivity of the map induced by"
---
We denote the $n$th local cohomology module of $\mathcal{O}$ supported at the origin by $$H:=H_0^n(\mathcal{O})
=H^{n-1}(\mathbb{C}^n\smallsetminus\{0\},\mathcal{O})
=\frac{\mathcal{O}[\frac{1}{x_1\cdots x_n}]}{\sum_{i=1}^n\mathcal{O}[\frac{1}{x_1\cdots\widehat{x_i}\cdots x_n}]}.$$ By right exactness of the tensor product $\otimes:=\otimes_\mathcal{O}$, this implies $$H_0^n(\Omega^1(\log D))=H^{n-1}(\mathbb{C}^n\smallsetminus\{0\},\Omega^1(\log D))=\Omega^1(\log D)\otimes H.$$ The total differential $d:\mathcal{O}\to\Omega^1(\log D)$ induces a natural map $$d_1:H=H_0^n(\mathcal{O})\to H_0^n(\Omega^1(\log D))=\Omega^1(\log D)\otimes H$$ in local cohomology. The perfect pairing $\mathop{\mathrm{Der}}(-\log D)\otimes\Omega^1(\log D)\to\mathcal{O}$ [@Sai80 Lem. 1.6] identifies $\Omega^1(\log D)$ to $\mathop{\mathrm{Hom}}(\mathop{\mathrm{Der}}(-\log D),\mathcal{O})$. Applying $\otimes H$, it induces a pairing $$\label{2}
\langle,\rangle:\mathop{\mathrm{Der}}(-\log D)\otimes H_0^n(\Omega^1(\log D))=\mathop{\mathrm{Der}}(-\log D)\otimes(\Omega^1(\log D)\otimes H)\to H.$$ such that $\langle\delta,(\omega\otimes[g])\rangle=\langle\delta,\omega\rangle [g]$. In particular, $d_1([g])=\sum_{i=1}^ndx_i\otimes[\partial_i(g)]$ for $g\in\mathcal{O}[\frac{1}{x_1\cdots x_n}]$ and hence $$\label{3}
\langle\delta,d_1([g])\rangle=\sum_{i=1}^n\langle\delta,dx_i\rangle[\partial_i(g)]=\delta([g]).$$ Denoting $\mathop{\mathrm{Hom}}=\mathop{\mathrm{Hom}}_\mathcal{O}$, the pairing ([\[2\]](#2){reference-type="ref" reference="2"}) corresponds to the natural map $$\label{5}
\SelectTips{cm}{}\xymatrix{
\mathop{\mathrm{Hom}}(\mathop{\mathrm{Der}}(-\log D),\mathcal{O})\otimes H=\Omega^1(\log D)\otimes H\ar[r]^-\pi&\mathop{\mathrm{Hom}}(\mathop{\mathrm{Der}}(-\log D),H).
}$$ According to [@HM98 Lem. 1.11], $\Omega^1(\log D)=\mathcal{O}\cdot\frac{df}{f}+\Omega ^1$ and there is an exact sequence $$\label{4}
\SelectTips{cm}{}\xymatrix{
0\ar[r]&\mathcal{O}\ar[r]^-{\alpha^t}&\mathcal{O}^{n+1}\cong\mathcal{O}\oplus\Omega^1\ar[r]^-\beta&\Omega^1(\log D)\ar[r]&0
}$$ where $\alpha=(f,f_1,\dots,f_n)$ and $\beta=(\frac{df}{f},-dx_1,\dots,-dx_n)$. Dualizing against $\mathcal{O}$ yields $$\SelectTips{cm}{}\xymatrix{
0\ar[r]&\mathop{\mathrm{Der}}(-\log D)\ar[r]^-{\beta^t}&\mathcal{O}^{n+1}\ar[r]^-\alpha&J\ar[r]&0,\quad J:=\langle f,f_1,\dots,f_n\rangle,
}$$ and $\mathop{\mathrm{Ext}}^1(\Omega^1(\log D),\mathcal{O})\cong\mathcal{O}/J$. Dualizing against $\mathcal{O}$ and $H$ yields the sequences $$\begin{gathered}
\label{6}
\xymat@C=22pt{
0\ar[r]&\mathop{\mathrm{Hom}}(J,\mathcal{O})\ar[r]&\mathcal{O}^{n+1}\ar[r]^-{(\beta^t)^t}&\mathop{\mathrm{Hom}}(\mathop{\mathrm{Der}}(-\log D),\mathcal{O})\ar[r]&0,
}\\
\label{7}
\xymat@C=14pt{
0\ar[r]&\mathop{\mathrm{Hom}}(J,H)\ar[r]&H^{n+1}\ar[r]&\mathop{\mathrm{Hom}}(\mathop{\mathrm{Der}}(-\log D),H)\ar[r]&\mathop{\mathrm{Ext}}^1(J,H)\ar[r]&0.
}
\end{gathered}$$ By reflexivity of $\mathop{\mathrm{Der}}(-\log D)$ [@Sai80 Cor. 1.7], the sequences ([\[4\]](#4){reference-type="ref" reference="4"}) and ([\[6\]](#6){reference-type="ref" reference="6"}) coincide. In particular, $(\beta^t)^t=\beta$ is surjective and $\mathop{\mathrm{Hom}}(J,\mathcal{O})=\mathcal{O}$ as the kernel of $\beta$ which is directly obvious. From sequences ([\[6\]](#6){reference-type="ref" reference="6"}) and ([\[7\]](#7){reference-type="ref" reference="7"}), we obtain the commutative diagram $$\label{8}
\SelectTips{cm}{}\xymatrix{
\mathop{\mathrm{Hom}}(J,\mathcal{O})\otimes H \ar[r]\ar[d]&H^{n+1} \ar@{->>}[r]^-{\beta\otimes1}\ar@{=}[d]&\mathop{\mathrm{Hom}}(\mathop{\mathrm{Der}}(-\log D),\mathcal{O})\otimes H\ar[d]^-\pi\\
\mathop{\mathrm{Hom}}(J,H)\ar@{^(->}[r]^-\iota&H^{n+1}\ar[r]^-\gamma&\mathop{\mathrm{Hom}}(\mathop{\mathrm{Der}}(-\log D),H)
}$$ involving the map $\pi$ in ([\[5\]](#5){reference-type="ref" reference="5"}).

::: lem
[]{#1 label="1"} If $D$ is not Euler homogeneous then $\mathop{\mathrm{tr}}\delta_0=0$ for all $\delta\in\mathop{\mathrm{Der}}(-\log D)$. In particular, $\pi(d_1([\frac{1}{x_1\dots x_n}]))(\delta)=\langle\delta,d_1([\frac{1}{x_1\dots x_n}])\rangle=0$ for all $\delta\in\mathop{\mathrm{Der}}(-\log D)$.
:::

::: proof
*Proof.* By the formal structure theorem [@GS06 Thm. 5.4], there is a system of generators $\mathcal S$ of the $\mathfrak{m}$-adic completion $\widehat\mathop{\mathrm{Der}}(-\log D)$ of $\mathop{\mathrm{Der}}(-\log D)$ such that, for $\delta\in\mathcal S$, either $\delta_0$ is nilpotent and hence $\mathop{\mathrm{tr}}\delta_0=0$ or $\delta=\delta_0$ is semisimple and $\delta(\hat f)\in\mathbb{Q}\cdot\hat f$ where $\hat f:=\hat u\cdot f$ for some unit $\hat u\in\widehat\mathcal{O}^\star$. In the second case, $\delta\in\mathop{\mathrm{Ann}}_{\widehat\mathop{\mathrm{Der}}}(\hat f)$ if $D$ and hence $\hat f$ is not Euler homogeneous. Since $D$ is an isolated singularity, $$\mathop{\mathrm{Ann}}_{\widehat\mathop{\mathrm{Der}}}(\hat f)=\langle\hat f_i\partial_j-\hat f_j\partial_i\mid 1\le i<j\le n\rangle,\quad\hat f_i:=\partial_i(\hat f).$$ By a formal coordinate change [@Arn73 Lem. 4.1], $\hat f=x_1^2+\cdots+x_k^2+g(x_{k+1},\dots,x_n)$ with $g\in\widehat\mathfrak{m}^3$ and $\mathop{\mathrm{tr}}\delta_0=0$ follows also in the second case from $$\delta_0\in\mathop{\mathrm{Ann}}_{\widehat\mathop{\mathrm{Der}}}(\hat f)_0=\langle x_i\partial_j-x_j\partial_i\mid 1\le i<j\le k\rangle.$$ Since $\mathop{\mathrm{Der}}(-\log D)_0=\widehat\mathop{\mathrm{Der}}(-\log D)_0$ and by additivity and coordinate invariance of $\mathop{\mathrm{tr}}\delta_0$, this proves the first claim. The second follows from ([\[3\]](#3){reference-type="ref" reference="3"}) and the obvious formula $\delta([\frac{1}{x_1\dots x_n}])=\mathop{\mathrm{tr}}(\delta_0)[\frac{1}{x_1\dots x_n}]$ for any $\delta\in\mathfrak{m}\cdot\mathop{\mathrm{Der}}$. ◻
:::

We continue our study of diagram ([\[8\]](#8){reference-type="ref" reference="8"}) under the assumption that $D$ is not Euler homogeneous. By Lemma [\[1\]](#1){reference-type="ref" reference="1"}, $\pi(d_1([\frac{1}{x_1\cdots x_n}]))=0$ and $d_1([\frac{1}{x_1\cdots x_n}])=(\beta\otimes1)(\psi)$ where $\psi=(0,u_1,\dots,u_n)\in H^{n+1}$ and $u_i=-\partial_i([\frac{1}{x_1\cdots x_n}])=[\frac{1}{x_1\cdots x_i^2\cdots x_n}]$. Then $\gamma(\psi)=0$ and hence $\psi=\iota(\varphi)$ where $\varphi\in\mathop{\mathrm{Hom}}(J,H)$ is characterised by $$\label{9}
\varphi(f_i)=\left[\frac{1}{x_1\cdots x_i^2\cdots x_n}\right],\quad\varphi(f)=0.$$ By injectivity of $\iota$, $d_1([\frac{1}{x_1\cdots x_n}])=0$ if and only if $\varphi$ extends to $\mathcal{O}$.

::: lem
[]{#10 label="10"} The map $\varphi\in\mathop{\mathrm{Hom}}(J,H)$ which fulfils ([\[9\]](#9){reference-type="ref" reference="9"}) extends to a $\tilde\varphi\in\mathop{\mathrm{Hom}}(\mathcal{O},H)$.
:::

::: proof
*Proof.* Denote by $A:=\mathbb{C}[x_1,\dots,x_n]\subseteq\mathcal{O}$ the polynomial ring and by $M^\star:=\mathop{\mathrm{Hom}}_\mathbb{C}(M,\mathbb{C})$ the algebraic dual of an $A$- or $\mathcal{O}$-module $M$. The residue pairing [@Ems78 Sect. B.1] $\langle,\rangle:H\otimes_\mathbb{C}\mathcal{O}\to\mathbb{C}$ is defined by $\langle[g],h\rangle:=\mathop{\mathrm{res}}([g\cdot h])$ where the residue map $\mathop{\mathrm{res}}:H\to\mathbb{C}$ sends $[g]\in H$ to the coefficient of $\frac{1}{x_1\cdots x_n}$ in $g$. More explicitly, $$\left\langle\left[\sum_{i\in\mathbb{N}^n}\frac{a_i}{x_1^{i_1+1}\cdots x_n^{i_n+1}}\right],\sum _{i\in\mathbb{N}^n}b_ix_1^{i_1}\cdots x_n^{i_n}\right\rangle=\sum_{i\in\mathbb{N}^n}a_ib_i.$$ The residue pairing defines an injection of $H$ into $\mathcal{O}^\star$. Restricted to $A$, the pairing injects $H$ into $A^\star=\mathbb{C}[[x_1^{-1},\dots,x_n^{-1}]]\cdot\frac{1}{x_1\cdots x_n}$. By ([\[9\]](#9){reference-type="ref" reference="9"}), $\varphi$ annihilates the ideal $K:=\langle f\rangle+\mathfrak{m}^2\cdot\langle f_1,\dots,f_n\rangle$ and induces a $\bar\varphi\in\mathop{\mathrm{Hom}}(J/K,H)$. Since $K$ has finite colength, $\mathfrak{m}^{N+1}\subseteq K$ for some $N>0$ and hence the finite vector space $$K^\perp\subseteq(\mathfrak{m}^{N+1})^\perp=\bigoplus_{|i|\le N}\frac{\mathbb{C}}{x_1^{i_1+1}\cdots x_n^{i_n+1}}$$ identifies to $(K\cap A)^{\perp}\subseteq A^\star$. Then the residue pairing induces an isomorphism $$\ell:K^{\perp}=(K\cap A)^{\perp}\to(A/K\cap A)^{\star}=(\mathcal{O}/K)^{\star}$$ defined by $\ell([g])([h])=\langle[g],h\rangle=\mathop{\mathrm{res}}([g\cdot h])$ for $[g]\in K^{\perp}$ and $[h]\in\mathcal{O}/K$. Thus, the linear form $\mathop{\mathrm{res}}\circ\bar\varphi\in(J/K)^\star$ extends to $\ell([g])$ for some $[g]\in K^{\perp}$ which means that $\mathop{\mathrm{res}}(\varphi(h))=\mathop{\mathrm{res}}([g\cdot h])$ for all $h\in J$. Now, define $\tilde\varphi\in\mathop{\mathrm{Hom}}(\mathcal{O},H)$ by $\tilde\varphi(h):=[g\cdot h]$ for all $h\in\mathcal{O}$. Then, for $h\in J$, $$\langle\tilde\varphi(h),x^\alpha\rangle=\langle[g\cdot h],x^\alpha\rangle=\mathop{\mathrm{res}}([g\cdot x^\alpha h])=\mathop{\mathrm{res}}(\varphi(x^\alpha h))=\langle\varphi(h),x^\alpha\rangle$$ for all $\alpha\in\mathbb{N}^n$ and hence $\tilde\varphi(h)=\varphi(h)$ which implies that $\tilde\varphi$ is an extension of $\varphi$. ◻
:::

::: proof
*Proof of Theorem [\[0\]](#0){reference-type="ref" reference="0"}.* For isolated singularities, Euler and quasihomogeneity are equivalent by [@Sai71] and $h^p(H^n_0(\Omega^\bullet(\log D)))=0$ for all $p$ by [@HM98 Cor. 1.8]. For non Euler homogeneous $D$, $0\ne[\frac{1}{x_1\cdots x_n}]\in\ker d_1$ by Lemma [\[10\]](#10){reference-type="ref" reference="10"}. ◻
:::
