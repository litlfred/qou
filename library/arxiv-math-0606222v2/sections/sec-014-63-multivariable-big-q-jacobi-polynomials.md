---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-014-63-multivariable-big-q-jacobi-polynomials
section_title: "Multivariable big q-Jacobi polynomials"
section_number: 6.3
pages: 27-29
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.9
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
We repeat the techniques and arguments of the previous subsection to derive evaluation formulas for multivariable big $q$-Jacobi polynomials. The monic multivariable big $q$-Jacobi polynomial $$P_\lambda^B(z)=P_\lambda^B(z;a,b,c,d;q,t)\in\ \mathbb{E}[z]^S$$ of degree $\lambda\in\Lambda_n$ is of the form $$\label{expansionB}
P_\lambda^B(z)=\widetilde{m}_\lambda(z)+\sum_{\mu\in\Lambda: \mu<\lambda}c_{\lambda,\mu}^B\widetilde{m}_{\mu}(z)$$ for certain coefficients $c_{\lambda,\mu}^B=c_{\lambda,\mu}^B(a,b,c,d;q,t)\in \mathbb{E}$. Similarly as for the Koornwinder polynomials and the multivariable little $q$-Jacobi polynomials, the multivariable big $q$-Jacobi polynomials can be characterized by a second-order difference equation they should satisfy, or in terms of suitable orthogonality properties, see [@S0]. The characterization as solution of a difference equation is $D_BP_\lambda^B=
E_\lambda^{qJ}P_\lambda^B$ with $$\begin{split}
D_B&=\sum_{j=1}^n\bigl(\phi_{B,j}^+(z)(T_j-\hbox{Id})+\phi_{B,j}^-(z)(T_j^{-1}-\hbox{Id})\bigr),\\
\phi_{B,j}^+(z)&=qt^{n-1}\bigl(a-\frac{c}{qz_j}\bigr)\bigl(b+\frac{d}{qz_j}\bigr)\prod_{l\not=j}\frac{z_l-tz_j}{z_l-z_j},\\
\phi_{B,j}^-(z)&=\bigl(1-\frac{c}{z_j}\bigr)\bigl(1+\frac{d}{z_j}\bigr)\prod_{l\not=j}\frac{z_j-tz_l}{z_j-z_l}.
\end{split}$$

We again consider the evaluation formulas for the one-variable big $q$-Jacobi polynomials ($n=1$) first. The one-variable monic big $q$-Jacobi polynomial is independent of $t$ and is given explicitly as $$\label{Bone}
P_m^B(z)=\frac{\bigl(qa,-qad/c;q\bigr)_m}{\bigl(q^{m+1}ab;q\bigr)_m\bigl(qa/c\bigr)^m}
{}_3\phi_2\left(\begin{matrix} q^{-m},q^{m+1}ab,qaz/c\\ qa,-qad/c \end{matrix};q,q\right)$$ for $m\in\mathbb{Z}_+$, see e.g. [@KS]. We immediately obtain from [\[Bone\]](#Bone){reference-type="eqref" reference="Bone"} the evaluation formula $$\label{B11}
P_m^B(c/qa)=\frac{\bigl(qa,-qad/c;q\bigr)_m}{\bigl(q^{m+1}ab;q\bigr)_m}\bigl(c/qa\bigr)^m$$ for $m\in\mathbb{Z}_+$. A straightforward computation using [\[Bone\]](#Bone){reference-type="eqref" reference="Bone"} and the $q$-Vandermonde formula [\[qVandermonde\]](#qVandermonde){reference-type="eqref" reference="qVandermonde"} yields the two evaluation formulas $$\label{B21}
\begin{split}
P_m^B(c)&=\frac{\bigl(qa,qab,-qbc/d;q\bigr)_m}{\bigl(qab;q\bigr)_{2m}}d^mq^{\frac{1}{2}m(m-1)},\\
P_m^B(-d)&=\frac{\bigl(-qad/c,qb,qab;q\bigr)_m}{\bigl(qab;q\bigr)_{2m}}(-1)^mc^mq^{\frac{1}{2}m(m-1)}
\end{split}$$ for $m\in\mathbb{Z}_+$. Finally, by the $q$-Saalschütz sum $$\label{qSaalschutz}
{}_3\phi_2\left(\begin{matrix}
q^{-m},a,b\\ abq^{1-m}/c,c\end{matrix};
q,q\right)=\frac{\bigl(c/a,c/b;q\bigr)_m}{\bigl(c,c/ab;q\bigr)_m},\qquad
m\in\mathbb{Z}_+$$ (see [@GR (II.12)]) we obtain the evaluation formula $$\label{B31}
P_m^B(-d/qb)=\frac{\bigl(qb,-qbc/d,qab;q\bigr)_m}
{\bigl(qab;q\bigr)_{2m}}\bigl(-d/qb\bigr)^m$$ for $m\in\mathbb{Z}_+$. In the following theorem we give the multivariable analogues of the evaluation formulas [\[B11\]](#B11){reference-type="eqref" reference="B11"}, [\[B21\]](#B21){reference-type="eqref" reference="B21"} and [\[B31\]](#B31){reference-type="eqref" reference="B31"}. Recall the explicit expression $\Delta_\lambda$, defined by [\[Delta\]](#Delta){reference-type="eqref" reference="Delta"}.

::: thm
[]{#thmB label="thmB"} For $\lambda\in\Lambda_n$ we have the evaluation formulas $$\label{B1}
P_\lambda^B(ct^\rho)=\Delta_\lambda\prod_{i=1}^n\frac{\bigl(qat^{n-i},qabt^{n-i},
-\frac{qbc}{d}t^{n-i};q\bigr)_{\lambda_i}}{\bigl(qabt^{2(n-i)};q\bigr)_{2\lambda_i}}
d^{\lambda_i}q^{\frac{1}{2}\lambda_i(\lambda_i-1)},$$ $$\label{B2}
P_\lambda^B(-dt^\rho)=\Delta_\lambda\prod_{i=1}^n\frac{\bigl(qbt^{n-i},qabt^{n-i},
-\frac{qad}{c}t^{n-i};q\bigr)_{\lambda_i}}
{\bigl(qabt^{2(n-i)};q\bigr)_{2\lambda_i}}(-c)^{\lambda_i}q^{\frac{1}{2}\lambda_i(\lambda_i-1)},$$ $$\label{B3}
P_\lambda^B\bigl(\frac{c}{qa}\,t^{-\rho}\bigr)=\Delta_\lambda
\prod_{i=1}^n\frac{\bigl(qat^{n-i},qabt^{n-i},-\frac{qad}{c}t^{n-i};q\bigr)_{\lambda_i}}
{\bigl(qabt^{2(n-i)};q\bigr)_{2\lambda_i}}\bigl(\frac{c}{qa}t^{i-n}\bigr)^{\lambda_i},$$ $$\label{B4}
P_\lambda^B\bigl(-\frac{d}{qb}\,t^{-\rho}\bigr)=\Delta_\lambda
\prod_{i=1}^n\frac{\bigl(qbt^{n-i},qabt^{n-i},-\frac{qbc}{d}t^{n-i};q\bigr)_{\lambda_i}}
{\bigl(qabt^{2(n-i)};q\bigr)_{2\lambda_i}}\bigl(-\frac{d}{qb}t^{i-n}\bigr)^{\lambda_i}.$$
:::

::: proof
*Proof.* The proof is analogous to the proof of Theorem [\[thmB\]](#thmB){reference-type="ref" reference="thmB"}, so we only indicate the main steps. From (the proof of) [@S Theorem 7.5] (replacing the role of the limiting parameter $\epsilon$ in [@S Theorem 7.5] by $\bigl(cd/q\bigr)^{\frac{1}{2}}\epsilon$), we obtain the two limit transitions $$\label{limitB1}
\lim_{\epsilon\rightarrow 0}\epsilon^{|\lambda|}P_\lambda\Bigl(\epsilon^{-1}z;
\frac{qa\epsilon}{c}, -\frac{qb\epsilon}{d}, c\epsilon^{-1},
-d\epsilon^{-1};q,t\Bigr)=P_\lambda^B(z;a,b,c,d;q,t),$$ $$\label{limitB2}
\lim_{\epsilon\rightarrow 0}\epsilon^{|\lambda|}P_\lambda\Bigl(\epsilon z;
\frac{qa\epsilon}{c}, -\frac{qb\epsilon}{d}, c\epsilon^{-1},
-d\epsilon^{-1};q,t\Bigr)=P_\lambda^B(z^{-1};a,b,c,d;q,t)$$ for $\lambda\in\Lambda_n$ and for a specific Zariski-dense subset of specialized parameters $a,b,c,d,q$ and $t$. If we set $z=\epsilon^{-1}ct^\rho$ (respectively $z=-\epsilon^{-1}dt^\rho$) in [\[limitB1\]](#limitB1){reference-type="eqref" reference="limitB1"} and use the evaluation formula [\[evalK\]](#evalK){reference-type="eqref" reference="evalK"} for the Macdonald-Koornwinder polynomial $P_\lambda$, then we arrive at the evaluation formula [\[B1\]](#B1){reference-type="eqref" reference="B1"} (respectively [\[B2\]](#B2){reference-type="eqref" reference="B2"}). The evaluation formulas [\[B3\]](#B3){reference-type="eqref" reference="B3"} and [\[B4\]](#B4){reference-type="eqref" reference="B4"} follow from [\[evalK\]](#evalK){reference-type="eqref" reference="evalK"} and the limit transition [\[limitB2\]](#limitB2){reference-type="eqref" reference="limitB2"} specialized to $z=\frac{qa}{c}\,t^\rho$ and $z=-\frac{qb}{d}\,t^\rho$, respectively. ◻
:::

We end this section by recalling the quadratic norm evaluations of the multivariable big $q$-Jacobi polynomials from [@S]. We define an $\mathbb{E}$-linear functional $$h_B=h_B^{a,b,c,d;q,t}: \mathbb{E}[z]^S\rightarrow \mathbb{E}$$ by requiring $$h_B\bigl(P_\lambda^B\bigr)=
\begin{cases}
1,\qquad &\hbox{ if } \lambda=0,\\
0,\qquad &\hbox{ if } \lambda\not=0.
\end{cases}$$ An analytic definition of $h_B$ can be given for specific Zariski dense choice of specialized parameters as a multidimensional $q$-integral with explicit weight function, see e.g. [@S]. We define a sesqui-linear form $\langle \cdot,\cdot\rangle_B= \langle
\cdot,\cdot\rangle_B^{a,b,c,d;q,t}$ on $\mathbb{E}[z]^S$ by $$\label{Bpairing}
\langle
p_1,p_2\rangle_B=h_B\bigl(p_1(z)\overline{p_2(z)}\bigr),\qquad
p_1,p_2\in \mathbb{E}[z]^S,$$ with the same convention on the complex conjugation as for the multivariable little $q$-Jacobi polynomials. The orthogonality relations for the multivariable big $q$-Jacobi polynomials are now given by $$\langle P_\lambda^B,P_\mu^B\rangle_B=N_B(\lambda)\delta_{\lambda,\mu},\qquad
\forall\,\lambda,\mu\in\Lambda_n$$ with the quadratic norms $N_B(\lambda)=N_B(\lambda;a,b,c,d;q,t)\in \mathbb{E}$ given by $$N_B(\lambda)=(cd)^{|\lambda|}t^{(\rho,\lambda)}
\left(\prod_{i=1}^nq^{{\lambda_i\choose
2}}\Bigl(-\frac{qbc}{d}t^{n-i},-\frac{qad}{c}t^{n-i};q\Bigr)_{\lambda_i}\right)N_L^+(\lambda)N_L^-(\lambda),$$ with $N_L^{\pm}=N_L^{\pm}(a,b;q,t)$ the same factors as for the multivariable little $q$-Jacobi polynomials. We recall from [@S] that $$\label{limitBnorms}
\lim_{\epsilon\rightarrow 0}\epsilon^{2|\lambda|}N_K
\bigl(\lambda;\frac{qa\epsilon}{c}, -\frac{qb\epsilon}{d}, c\epsilon^{-1},
-d\epsilon^{-1};q,t\bigr)=N_B(\lambda;a,b,c,d;q,t),\qquad
\lambda\in\Lambda_n,$$ for generic specialized parameters.
