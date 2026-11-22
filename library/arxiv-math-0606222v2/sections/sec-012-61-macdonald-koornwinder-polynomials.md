---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-012-61-macdonald-koornwinder-polynomials
section_title: "Macdonald-Koornwinder polynomials"
section_number: 6.1
pages: 22-24
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
toc_source: outline
text_source: latex
latex_prose_ratio: 0.665
latex_coverage_ratio: 0.888
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
Recall our notation $\mathbb{E}=\mathbb{C}(a,b,c,d,q,t)$ for the field of rational functions in six indeterminates $a,b,c,d,q$ and $t$. Let $W=S_n\ltimes \{\pm 1\}^n$, acting on $\mathbb{Z}^n$ by permutations and sign-changes of the coordinates, and acting on the algebra $\mathbb{E}[z^{\pm 1}]=\mathbb{E}[z_1^{\pm 1},\ldots,z_n^{\pm 1}]$ by permutations and inversions of the independent variables $z_i$. The cone $\Lambda_n\subset \mathbb{Z}^n$ is a fundamental domain for the $W$-action on $\mathbb{Z}^n$. The dominance order on $\Lambda_n$ is the partial order $\leq$ defined by $\lambda\leq\mu$ if $\sum_{j=1}^{i}\lambda_j\leq\sum_{j=1}^i\mu_j$ for $1 \le i \le n$. An $\mathbb{E}$-basis of the algebra $\mathbb{E}[z^{\pm 1}]^W$ of $W$-invariant Laurent polynomials is given by the symmetric monomials $m_\lambda(z):=\sum_{\mu\in W\lambda}z^\mu$ ($\lambda\in
\Lambda_n$).

The monic Macdonald-Koornwinder polynomial $P_\lambda(z)=P_\lambda(z;a,b,c,d;q,t)\in \mathbb{E}[z^{\pm 1}]^W$ of degree $\lambda\in\Lambda_n$ is of the form $$\label{expansionK}
P_\lambda(z)=m_\lambda(z)+\sum_{\mu\in\Lambda_n: \mu<\lambda}c_{\lambda,\mu}m_{\mu}(z)$$ for certain coefficients $c_{\lambda,\mu}=c_{\lambda,\mu}(a,b,c,d;q,t)\in \mathbb{E}$. It can be characterized as solution of a particular second-order difference equation, or, for suitably specialized generic parameters $a,b,c,d,q,t$, in terms of suitable orthogonality properties, see Koornwinder [@K]. The characterizing difference equation for the Macdonald-Koornwinder polynomial $P_\lambda(z)$ of degree $\lambda$ is $DP_\lambda=E_\lambda P_\lambda$ where $$\begin{split}
D&=\sum_{j=1}^n\bigl(\phi_j(z)(T_j-\hbox{Id})+\phi_j(z^{-1})(T_j^{-1}-\hbox{Id})\bigr),\\
\phi_j(z)&=\frac{(1-az_j)(1-bz_j)(1-cz_j)(1-dz_j)}{(1-z_j^2)(1-qz_j^2)}
\prod_{l\not=j}\frac{(1-tz_lz_j)(1-tz_l^{-1}z_j)}{(1-z_lz_j)(1-z_l^{-1}z_j)}
\end{split}$$ and where the eigenvalue $E_\lambda\in \mathbb{E}$ is given by $$E_\lambda=\sum_{j=1}^n\bigl(q^{-1}abcdt^{2n-j-1}(q^{\lambda_j}-1)+t^{j-1}(q^{-\lambda_j}-1)\bigr).$$ Note that $P_\lambda(z;a,b,c,d;q,t)$ is symmetric in the four parameters $a,b,c,d$. The evaluation formulas for Macdonald-Koornwinder polynomials are given by $$\label{evalK}
\begin{split}
P_\lambda(at^\rho)&=\prod_{i=1}^n\frac{\bigl(abt^{n-i},act^{n-i},adt^{n-i},q^{-1}abcdt^{n-i};q\bigr)_{\lambda_i}}
{\bigl(q^{-1}abcdt^{2(n-i)};q\bigr)_{2\lambda_i}\bigl(at^{n-i}\bigr)^{\lambda_i}}\\
&\times\prod_{1\leq j<k\leq n}
\frac{\bigl(q^{-1}abcdt^{2n-j-k+1};q\bigr)_{\lambda_j+\lambda_k}
\bigl(t^{k-j+1};q\bigr)_{\lambda_j-\lambda_k}}
{\bigl(q^{-1}abcdt^{2n-j-k};q\bigr)_{\lambda_j+\lambda_k}
\bigl(t^{k-j};q\bigr)_{\lambda_j-\lambda_k}}
\end{split}$$ for $\lambda\in\Lambda_n$. The evaluation formulas [\[evalK\]](#evalK){reference-type="eqref" reference="evalK"} have been established by van Diejen [@vD] for a sub-family of Macdonald-Koornwinder polynomials. The general case follow from Sahi's [@Sa] results using double affine Hecke algebras, see also [@S2 Remark 9.5].

In the rank one case ($n=1$), the Macdonald-Koornwinder polynomials do not dependent on $t$ and reduce to the monic Askey-Wilson polynomials $$P_m(z) =\frac{\bigl(ab,ac,ad;q\bigr)_m}{a^m\bigl(q^{m-1}abcd;q\bigr)_m}
{}_4\phi_3\left(\begin{matrix} q^{-m}, q^{m-1}abcd, az, az^{-1}\\ ab, ac, ad \end{matrix};q,q\right)\in\mathbb{C}[z+z^{-1}],
\qquad m\in\mathbb{Z}_+.$$ In particular $$P_m(a)=\frac{\bigl(ab,ac,ad;q\bigr)_m}{a^m\bigl(q^{m-1}abcd;q\bigr)_m},\qquad m\in\mathbb{Z}_+,$$ which is in accordance to [\[evalK\]](#evalK){reference-type="eqref" reference="evalK"}.

We give here a purely algebraic formulation of the quadratic norm evaluations for the Macdonald-Koornwinder polynomials, which has the advantage that we do not need to specialize the parameters $a,b,c,d,q$ and $t$. We define an $\mathbb{E}$-linear functional $$h_K=h_K^{a,b,c,d;q,t}: \mathbb{E}[z^{\pm 1}]^W\rightarrow \mathbb{E}$$ by requiring $$h_K\bigl(P_\lambda\bigr)=
\begin{cases}
1,\qquad &\hbox{ if } \lambda=0,\\
0,\qquad &\hbox{ if } \lambda\not=0.
\end{cases}$$ An analytic definition of $h_K$ can be given (for specific Zariski dense choice of parameters) as an integral over a deformed compact $n$-torus with explicit weight function, see e.g. [@K]. We define now a sesqui-linear form $\langle \cdot,\cdot\rangle_K=
\langle \cdot,\cdot\rangle_K^{a,b,c,d;q,t}$ on $\mathbb{E}[z^{\pm 1}]^W$ by $$\label{Kpairing}
\langle
p_1,p_2\rangle_K=h_K\bigl(p_1(z)\overline{p_2(z)}\bigr),\qquad
p_1,p_2\in \mathbb{E}[z^{\pm 1}]^W,$$ where complex conjugation on $\mathbb{C}$ is extended to an anti-linear algebra involution on $\mathbb{E}[z^{\pm 1}]$ by requiring the six parameters $a,b,c,d,q,t$ to be formally real, e.g. $\overline{a}=a$, and by requiring the variables $z_j$ to be formally purely imaginary, $\overline{z_j}=z_j^{-1}$. The orthogonality relations for the Macdonald-Koornwinder polynomials are now given by $$\label{normKoorn}
\langle P_\lambda,P_\mu\rangle_K=N_K(\lambda)\delta_{\lambda,\mu},\qquad
\forall\,\lambda,\mu\in\Lambda_n,$$ with the quadratic norms $N_K(\lambda)=N_K(\lambda;a,b,c,d;q,t)$ given by $N_K(\lambda)=N_K^+(\lambda)N_K^-(\lambda)$, where $N_K^{\pm}(\lambda)=N_K^{\pm}(\lambda;a,b,c,d;q,t)\in \mathbb{E}$ are $$\begin{split}
N_K^+(\lambda)&=\prod_{i=1}^n\frac{\bigl(abt^{n-i},act^{n-i},adt^{n-i},q^{-1}abcdt^{n-i};q\bigr)_{\lambda_i}}
{\bigl(q^{-1}abcdt^{2(n-i)};q\bigr)_{2\lambda_i}}\\
&\times\prod_{1\leq j<k\leq
n}\frac{\bigl(q^{-1}abcdt^{2n-j-k+1};q\bigr)_{\lambda_j+\lambda_k}
\bigl(t^{k-j+1};q\bigr)_{\lambda_j-\lambda_k}}
{\bigl(q^{-1}abcdt^{2n-j-k};q\bigr)_{\lambda_j+\lambda_k}\bigl(
t^{k-j};q\bigr)_{\lambda_j-\lambda_k}},\\
N_K^-(\lambda)&=\prod_{i=1}^n\frac{\bigl(qt^{n-i},bct^{n-i},bdt^{n-i},cdt^{n-i};q\bigr)_{\lambda_i}}
{\bigl(abcdt^{2(n-i)};q\bigr)_{2\lambda_i}}\\
&\times\prod_{1\leq j<k\leq
n}\frac{\bigl(abcdt^{2n-j-k-1};q\bigr)_{\lambda_j+\lambda_k}
\bigl(qt^{k-j-1};q\bigr)_{\lambda_j-\lambda_k}}
{\bigl(abcdt^{2n-j-k};q\bigr)_{\lambda_j+\lambda_k}\bigl(
qt^{k-j};q\bigr)_{\lambda_j-\lambda_k}}.
\end{split}$$ The quadratic norm formulas have been established by van Diejen [@vD] for a sub-family of Macdonald-Koornwinder polynomials. The general case has been derived in [@Sa], see also [@S2].

## Multivariable little $q$-Jacobi polynomials {#little}

We now return to the multivariable little $q$-Jacobi polynomials $P_\lambda^L(z)=P_\lambda^L(z;a,b;q,t)$ from Section [\[qJsection\]](#qJsection){reference-type="ref" reference="qJsection"}. We first shortly discuss evaluation formulas for one-variable little $q$-Jacobi polynomials ($n=1$), in which case the evaluation formulas can be derived directly from the explicit expressions of the little $q$-Jacobi polynomials as basic hypergeometric series. In fact, the monic one-variable little $q$-Jacobi polynomial is independent of $t$ and is given explicitly as $$\label{Lone}
\begin{split}
P_m^L(z)&=\frac{\bigl(qb;q\bigr)_m}{\bigl(q^{m+1}ab;q\bigr)_m(qb)^m}{}_3\phi_2\left(\begin{matrix}
q^{-m},q^{m+1}ab,qbz\\ qb,0\end{matrix};q,q\right)\\
&=\frac{\bigl(qa;q\bigr)_m}{\bigl(q^{m+1}ab;q\bigr)_m}(-1)^mq^{\frac{1}{2}m(m-1)}{}_2\phi_1\left(\begin{matrix}
q^{-m}, q^{m+1}ab\\qa\end{matrix};q,qz\right)
\end{split}$$ for $m\in\mathbb{Z}_+$, see e.g. [@KS]. Here the second equality follows from [@GR (III.7)]. From the second equality in [\[Lone\]](#Lone){reference-type="eqref" reference="Lone"} we obtain $$\label{L11}
P_m^L(0)=\frac{\bigl(qa,qab;q\bigr)_m}{\bigl(qab;q\bigr)_{2m}}(-1)^mq^{\frac{1}{2}m(m-1)}.$$ From the first equality in [\[Lone\]](#Lone){reference-type="eqref" reference="Lone"} and the $q$-Vandermonde sum $$\label{qVandermonde}
{}_2\phi_1\left(\begin{matrix} q^{-m},a\\c\end{matrix};q,q\right)=\frac{\bigl(c/a;q\bigr)_m}{\bigl(c;q\bigr)_m}\,a^m$$ for $m\in\mathbb{Z}_+$ (see [@GR (II.6)]), we obtain $$\label{L21}
P_m^L(1)=\frac{\bigl(qb,qab;q\bigr)_m}{\bigl(qab;q\bigr)_{2m}}\bigl(q^ma)^m.$$ Finally, from the first equality in [\[Lone\]](#Lone){reference-type="eqref" reference="Lone"} we obtain $$\label{L31}
P_m^L(q^{-1}b^{-1})=\frac{\bigl(qb,qab;q\bigr)_m}{\bigl(qab;q\bigr)_{2m}(qb)^m}.$$ In the following theorem we give the multivariable analogues of the evaluation formulas [\[L11\]](#L11){reference-type="eqref" reference="L11"}, [\[L21\]](#L21){reference-type="eqref" reference="L21"} and [\[L31\]](#L31){reference-type="eqref" reference="L31"}. Define $\Delta_\lambda=\Delta_\lambda(a,b;q,t)$ by $$\label{Delta}
\Delta_\lambda(a,b;q,t)=\prod_{1\leq j<k\leq n}
\frac{\bigl(qabt^{2n-j-k+1};q\bigr)_{\lambda_j+\lambda_k}
\bigl(t^{k-j+1};q\bigr)_{\lambda_j-\lambda_k}}
{\bigl(qabt^{2n-j-k};q\bigr)_{\lambda_j+\lambda_k}
\bigl(t^{k-j};q\bigr)_{\lambda_j-\lambda_k}},
\qquad \forall\,\lambda\in\Lambda_n.$$

::: thm
[]{#thmL label="thmL"} For $\lambda\in\Lambda_n$ we have the evaluation formulas $$\label{L1}
P_\lambda^L(0)=\Delta_\lambda\prod_{i=1}^n\frac{\bigl(qat^{n-i},qabt^{n-i};q\bigr)_{\lambda_i}}{\bigl(qabt^{2(n-i)};q\bigr)_{2\lambda_i}}
(-1)^{\lambda_i}q^{\frac{1}{2}\lambda_i(\lambda_i-1)},$$ $$\label{L2}
P_\lambda^L(t^\rho)=\Delta_\lambda\prod_{i=1}^n\frac{\bigl(qbt^{n-i}, qabt^{n-i};q\bigr)_{\lambda_i}}
{\bigl(qabt^{2(n-i)};q\bigr)_{2\lambda_i}}\bigl(aq^{\lambda_i}t^{n-i}\bigr)^{\lambda_i},$$ $$\label{L3}
P_\lambda^L(q^{-1}b^{-1}t^{-\rho})=\Delta_\lambda\prod_{i=1}^n\frac{\bigl(qbt^{n-i},qabt^{n-i};q\bigr)_{\lambda_i}}
{\bigl(qabt^{2(n-i)};q\bigr)_{2\lambda_i}}\bigl(qbt^{n-i}\bigr)^{\lambda_i}.$$
:::

::: proof
*Proof.* The evaluation formulas depend rationally on the parameters, hence it suffices to prove the theorem for a suitable choice of Zariski dense complex values of the parameters $a,b,q$ and $t$. The proof now uses the explicit limit transitions from Macdonald-Koornwinder polynomials to multivariable little $q$-Jacobi polynomials from [@SK] and [@S]. The key ingredient is the following result from the proof of [@S Theorem 6.4]. Let $\lambda,\mu\in\Lambda_n$ such that $\mu<\lambda$. Then $$\label{coefflim}
\lim_{\epsilon\rightarrow 0}\bigl(q^{-\frac{1}{2}}\epsilon\bigr)^{|\lambda|-|\mu|}
c_{\lambda,\mu}(\epsilon^{-1}q^{\frac{1}{2}},-aq^{\frac{1}{2}},\epsilon bq^{\frac{1}{2}}, -q^{\frac{1}{2}};q,t)=
c_{\lambda,\mu}^L(a,b;q,t)$$ for the coefficients $c_{\lambda,\mu}$ [\[expansionK\]](#expansionK){reference-type="eqref" reference="expansionK"} and $c_{\lambda,\mu}^L$ [\[expansionL\]](#expansionL){reference-type="eqref" reference="expansionL"} in the monomial expansions of $P_\lambda$ and $P_\lambda^L$, where $q^{\frac{1}{2}}$ is an arbitrary choice of square root of $q$.

*Proof of [\[L1\]](#L1){reference-type="eqref" reference="L1"}.* Observe that $$\label{monlimit1}
\lim_{\epsilon\rightarrow 0}\epsilon^{|\lambda|}m_\lambda(z)=\widetilde{m}_\lambda(0),
\qquad \forall\,\lambda\in\Lambda_n,$$ since both sides are equal to zero if $\lambda\in\Lambda_n\setminus\{0\}$ and are equal to one if $\lambda=0$. Combining [\[expansionK\]](#expansionK){reference-type="eqref" reference="expansionK"}, [\[expansionL\]](#expansionL){reference-type="eqref" reference="expansionL"}, [\[coefflim\]](#coefflim){reference-type="eqref" reference="coefflim"} and [\[monlimit1\]](#monlimit1){reference-type="eqref" reference="monlimit1"} now yields $$\label{limpart1}
\lim_{\epsilon\rightarrow 0}\bigl(q^{-\frac{1}{2}}\epsilon\bigr)^{|\lambda|}
P_\lambda\bigl(z;\epsilon^{-1}q^{\frac{1}{2}},-aq^{\frac{1}{2}},\epsilon bq^{\frac{1}{2}}, -q^{\frac{1}{2}};q,t\bigr)=
P_\lambda^L(0;a,b;q,t)$$ for $\lambda\in\Lambda_n$. By the evaluation formula [\[evalK\]](#evalK){reference-type="eqref" reference="evalK"} for the Macdonald-Koornwinder polynomial $P_\lambda$ and using that the Macdonald-Koornwinder polynomial is symmetric in $a,b,c,d$, we have $$\begin{split}
\bigl(q^{-\frac{1}{2}}\epsilon\bigr)^{|\lambda|}
&P_\lambda\bigl(-aq^{\frac{1}{2}}t^\rho;\epsilon^{-1}q^{\frac{1}{2}},
-aq^{\frac{1}{2}},\epsilon bq^{\frac{1}{2}}, -q^{\frac{1}{2}};q,t\bigr)\\
&=\Delta_\lambda(a,b;q,t)
\prod_{i=1}^n\frac{\bigl(qat^{n-i},-qabt^{n-i}\epsilon, qabt^{n-i}, -qat^{n-i}\epsilon^{-1};q\bigr)_{\lambda_i}\epsilon^{\lambda_i}}
{\bigl(qabt^{2(n-i)};q\bigr)_{2\lambda_i}\bigl(-aqt^{n-i}\bigr)^{\lambda_i}}.
\end{split}$$ Combined with the limit transition [\[limpart1\]](#limpart1){reference-type="eqref" reference="limpart1"}, specialized to $z=-aq^{\frac{1}{2}}t^\rho$, we obtain the evaluation formula [\[L1\]](#L1){reference-type="eqref" reference="L1"} for the multivariable little $q$-Jacobi polynomial $P_\lambda^L$.

*Proof of [\[L2\]](#L2){reference-type="eqref" reference="L2"}.* Now we use the degeneration $$\label{monlimit2}
\lim_{\epsilon\rightarrow 0}\epsilon^{|\lambda|}
m_\lambda(\epsilon^{-1}z)=\widetilde{m}_\lambda(z),\qquad\forall\,\lambda\in\Lambda_n$$ for the monomial bases. Together with [\[coefflim\]](#coefflim){reference-type="eqref" reference="coefflim"} this yields the limit transition $$\label{limpart2}
\lim_{\epsilon\rightarrow 0}\bigl(q^{-\frac{1}{2}}\epsilon\bigr)^{|\lambda|}
P_\lambda\bigl(q^{\frac{1}{2}}\epsilon^{-1}z;\epsilon^{-1}q^{\frac{1}{2}},
-aq^{\frac{1}{2}},\epsilon bq^{\frac{1}{2}}, -q^{\frac{1}{2}};q,t\bigr)=
P_\lambda^L(z;a,b;q,t)$$ for $\lambda\in\Lambda_n$, which is in accordance with [@S Theorem 6.4]. By the evaluation formula [\[evalK\]](#evalK){reference-type="eqref" reference="evalK"} for the Macdonald-Koornwinder polynomial $P_\lambda$ we now have $$\begin{split}
\bigl(q^{-\frac{1}{2}}\epsilon\bigr)^{|\lambda|}
&P_\lambda\bigl(q^{\frac{1}{2}}\epsilon^{-1}t^\rho;
\epsilon^{-1}q^{\frac{1}{2}},-aq^{\frac{1}{2}},\epsilon bq^{\frac{1}{2}}, -q^{\frac{1}{2}};q,t\bigr)\\
&=\Delta_\lambda(a,b;q,t)\prod_{i=1}^n\frac{\bigl(-qat^{n-i}\epsilon^{-1},-qt^{n-i}\epsilon^{-1}, qbt^{n-i}, qabt^{n-i};q\bigr)_{\lambda_i}\epsilon^{2\lambda_i}}
{\bigl(qabt^{2(n-i)};q\bigr)_{2\lambda_i}\bigl(qt^{n-i}\bigr)^{\lambda_i}}.
\end{split}$$ Combined with the limit transition [\[limpart2\]](#limpart2){reference-type="eqref" reference="limpart2"}, specialized to $z=t^\rho$, we obtain the evaluation formula [\[L2\]](#L2){reference-type="eqref" reference="L2"}.

*Proof of [\[L3\]](#L3){reference-type="eqref" reference="L3"}.* We now use the limit transition $$\label{monlimit3}
\lim_{\epsilon\rightarrow 0}\epsilon^{|\lambda|}m_\lambda(\epsilon z)=\widetilde{m}_\lambda(z^{-1}),\qquad\forall\,
\lambda\in\Lambda_n.$$ Together with [\[coefflim\]](#coefflim){reference-type="eqref" reference="coefflim"} this yields $$\label{limpart3}
\lim_{\epsilon\rightarrow 0}\bigl(q^{-\frac{1}{2}}\epsilon\bigr)^{|\lambda|}
P_\lambda\bigl(q^{-\frac{1}{2}}\epsilon z;\epsilon^{-1}q^{\frac{1}{2}},
-aq^{\frac{1}{2}},\epsilon bq^{\frac{1}{2}}, -q^{\frac{1}{2}};q,t\bigr)=
P_\lambda^L(z^{-1};a,b;q,t)$$ for $\lambda\in\Lambda_n$. By the evaluation formula [\[evalK\]](#evalK){reference-type="eqref" reference="evalK"} for the Macdonald-Koornwinder polynomial $P_\lambda$ we now have $$\begin{split}
\bigl(q^{-\frac{1}{2}}\epsilon\bigr)^{|\lambda|}
&P_\lambda\bigl(\epsilon bq^{\frac{1}{2}}t^\rho;
\epsilon^{-1}q^{\frac{1}{2}},-aq^{\frac{1}{2}},\epsilon bq^{\frac{1}{2}}, -q^{\frac{1}{2}};q,t\bigr)\\
&=\Delta_\lambda(a,b;q,t)\prod_{i=1}^n\frac{\bigl(qbt^{n-i},qabt^{n-i},-qbt^{n-i}\epsilon,-qabt^{n-i}\epsilon;q\bigr)_{\lambda_i}}
{\bigl(qabt^{2(n-i)};q\bigr)_{2\lambda_i}}\bigl(qbt^{n-i}\bigr)^{-\lambda_i}.
\end{split}$$ Combined with the limit transition [\[limpart3\]](#limpart3){reference-type="eqref" reference="limpart3"}, specialized to $z=qbt^\rho$, we obtain [\[L3\]](#L3){reference-type="eqref" reference="L3"}. ◻
:::

The quadratic norms $N_L(\lambda)=N_L(\lambda;a,b;q,t)\in \mathbb{E}$ of the multivariable little $q$-Jacobi polynomials have been explicitly evaluated in [@S]. It reads $$N_L(\lambda)=q^{(\lambda,\lambda)}a^{|\lambda|}t^{2(\rho,\lambda)}
N_L^+(\lambda)N_L^-(\lambda),$$ where the factors $N_L^{\pm}(\lambda)=N_L^{\pm}(\lambda;a,b;q,t)\in
\mathbb{E}$ are given by $$\begin{split}
N_L^+(\lambda)&=\prod_{i=1}^n\frac{\bigl(qat^{n-i},qabt^{n-i};q\bigr)_{\lambda_i}}
{\bigl(qabt^{2(n-i)};q\bigr)_{2\lambda_i}}\prod_{1\leq j<k\leq
n}\frac{\bigl(qabt^{2n-j-k+1};q\bigr)_{\lambda_j+\lambda_k}
\bigl(t^{k-j+1};q\bigr)_{\lambda_j-\lambda_k}}
{\bigl(qabt^{2n-j-k};q\bigr)_{\lambda_j+\lambda_k}\bigl(
t^{k-j};q\bigr)_{\lambda_j-\lambda_k}},\\
N_L^-(\lambda)&=\prod_{i=1}^n\frac{\bigl(qt^{n-i},qbt^{n-i};q\bigr)_{\lambda_i}}
{\bigl(q^2abt^{2(n-i)};q\bigr)_{2\lambda_i}}
\prod_{1\leq j<k\leq n}\frac{\bigl(q^2abt^{2n-j-k-1};q\bigr)_{\lambda_j+\lambda_k}
\bigl(qt^{k-j-1};q\bigr)_{\lambda_j-\lambda_k}}
{\bigl(q^2abt^{2n-j-k};q\bigr)_{\lambda_j+\lambda_k}\bigl(
qt^{k-j};q\bigr)_{\lambda_j-\lambda_k}}.
\end{split}$$ We recall from [@S] that $$\label{limitLnorms}
\lim_{\epsilon\rightarrow
0}\bigl(q^{-\frac{1}{2}}\epsilon\bigr)^{2|\lambda|}N_K(\lambda;
\epsilon^{-1}q^{\frac{1}{2}},-aq^{\frac{1}{2}},\epsilon bq^{\frac{1}{2}},
-q^{\frac{1}{2}};q,t)=N_L(\lambda;a,b;q,t),\qquad
\forall\,\lambda\in\Lambda_n$$ for generic specialized parameters.
