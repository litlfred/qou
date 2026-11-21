---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE"
section_id: sec-023-72-application-to-the-calculation-of-rz
section_title: "Application to the calculation of Rz"
section_number: 7.2
pages: 37-40
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.945
doc_brief: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn ="
---
[]{#sub.ag label="sub.ag"}

In this subsection, we apply Theorem [\[thm.nahmEM\]](#thm.nahmEM){reference-type="ref" reference="thm.nahmEM"} and its corollary to a specific Nahm sum to prove equation [\[CompRz\]](#CompRz){reference-type="eqref" reference="CompRz"} in the introduction.

::: theorem
[]{#thm.eta label="thm.eta"} Let $n$ be odd and $\eta_\zeta$ be the $n$-torsion element in $B(\mathbf Q(\zeta)^{+})$ defined by [\[eq.etaz\]](#eq.etaz){reference-type="eqref" reference="eq.etaz"}, where $\zeta$ is a primitive $n$th root of unity. Then $R_\zeta(\eta_\zeta) \;=\; \zeta^2\,$.
:::

::: proof
*Proof.* The case $n=1$ is trivial, so assume that $n\ge 3$. Set $A_n=\bigl(2\min(i,j)\bigr)_{1\le i,j\le r}$, where $r = (n- 3)/2$. If $n\ge 5$, let $f_n$ be the $r$-dimensional Nahm sum $f_{A_n,0}$. If $n= 3$, we let $f_{3} = 1$, which is also the natural interpretation of the corresponding $0$-dimensional Nahm sum. By a famous identity of Andrews and Gordon [@Andrews], which reduces to the first Ramanujan-Rogers identity when $n=5$, we have the product expansion $$\label{AGid}
f_n(q) \;=\; 
\prod_{\begin{subarray}{c}
  k>0\\2k\not\equiv0, \pm 1 \, (\;\text{\rm mod}\;n) \end{subarray}} \frac{1}{1-q^k}.$$ and this is modular up to a power of $q$ for the same reason as for $G(q)=f_5(q)$ (quotient of a theta series by the Dedekind eta-function). This modularity allows us to compute its asymptotics as $q\to\zeta_n$, and by comparing the result with the general asymptotics of Nahm sums as given in [\[thm.nahmEM\]](#thm.nahmEM){reference-type="ref" reference="thm.nahmEM"}, we will obtain the desired evaluation of $\eta_n$. We now give details.

It is easy to check that all solutions $X$ of the Nahm equation $1-X=X^{A_n}$ have the form $$X=(X_{r+1},\dots,X_2),
\qquad X_k  \;=\; \frac{(1-\zeta^{k-1})(1-\zeta^{k+1})}{(1-\zeta^{k})^2}$$ with $\zeta$ a primitive $n$ root of unity, and hence form a single Galois orbit. The distinguished solution $X^{A_n}\in(0,1)^r$ corresponds to $\zeta=\mathbf{e}(1/n)=\zeta_n$. From the equation $$\label{eq:comparetorsion}
1-X_k=\left(\frac{\zeta^{1/2}-\zeta^{-1/2}}{\zeta^{k/2}-\zeta^{-k/2}}\right)^2$$ and the functional equation $L(1-X)=\frac{\pi^2}6-L(X)$, we find $$\mathrm L({[X]}) \;=\;  {\sum_{k=2}^{r+1} L(X_k)  }
= \frac12\,\sum_{{k=2}}^{{n-2}}\biggl(\frac{\pi^2}6 
\,-\,\mathrm L\biggl(\frac{\sin^2(\pi/n)}{\sin^2(k \pi/n)}\biggr)\biggr) 
=  \frac{(n-3)\pi^2}{6n}\,,$$ the invoked equality being a well-known identity for the Rogers dilogarithm of which a proof can be found at the end of [@Zagier], §II.2C.

Denote the right-hand side of this by $-4\pi^2C_n$ and set $\widetilde f_n(\tau)=\widetilde f_{A_n,0,C_n}(\tau)=q^{C_n}f_n(q)$.

Using the Jacobi theta function and the Jacobi triple product formula $$\theta(\tau,z) \;=\; \sum_{-\infty}^{\infty} (-1)^{k} q^{(2k+1)^2/8} y^{(2k+1)/2} 
\;=\; q^{1/8}\,y^{1/2}\,\prod_{k=1}^\infty 
\bigl(1-q^k\bigr)\bigl(1-q^ky\bigr)\bigl(1-q^{k-1}y^{-1}\bigr)$$ (where $\Im(\tau)>0$, $z\in\mathbf C$, $q=\mathbf{e}(\tau)$, and $y=\mathbf{e}(z)$), together with the Dedekind eta-function $\eta(\tau)=q^{1/24}\prod_{n>0}(1-q^k)$, we can rewrite [\[AGid\]](#AGid){reference-type="eqref" reference="AGid"} as

$$\widetilde f_n(\tau) \;=\; q^{(r+1)^2/2n}\,\frac{\theta(n\tau,\,-(r+1)\tau)}{\eta(\tau)}\,,$$ which in conjunction with the standard transformation properties of $\theta$ and $\eta$ implies that $\widetilde f_n(\tau)$ is a modular function (with multiplier system) on the congruence subgroup $\Gamma_0(n)$ of $\mathrm{SL}(2,\mathbf Z)$. We need only the special case $\tau\mapsto\frac\tau{n\tau+1}$, where the transformation law is given by $$\label{WasLemma}
\widetilde f_n\Bigl(\frac\tau{n\tau+1}\Bigr) 
\;=\; \mathbf{e}\Bigl(\frac{n-3}{24}\Bigr)\,\widetilde f_n(\tau)\,.$$ We sketch the proof of this for completeness. The well-known modular transformation properties of $\theta$ and $\eta$ under the generators $T=\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix})$ and $S=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix})$ of $\mathrm{SL}(2,\mathbf Z)$ are given by $$\begin{aligned}
&\theta(\tau+1,z)\,=\, \mathbf{e}(1/8) \, \theta(\tau,z)\,, \quad
\theta(-1/\tau,\,z/\tau) \,=\, \sqrt{\tau/i} \; 
\mathbf{e}(z^2/2\tau)\,\theta(\tau,z)\, \\
& \eta(\tau+1)\,=\,\mathbf{e}(1/24) \,\eta(\tau)\,, \qquad\; \eta(-1/\tau) 
\,=\, \sqrt{\tau/i} \;\eta(\tau)\,. 
\end{aligned}$$ Hence, using$\;\stackrel T\sim\;$and$\;\stackrel S\sim\;$to denote an equality up to an elementary factor (the product of a power of $\tau$ with the exponential of a linear combination of 1, $\tau$ and $z^2/\tau$) that can be deduced from the $T$- or $S$-transformation behavior of the function in question, we have $$\theta\Bigl(\frac{n\tau}{n\tau+1}, \frac{(r+1)\tau}{n\tau+1}\Bigr) 
\;\stackrel T\sim\;\theta\Bigl(\frac{-1}{n\tau+1}, \frac{(r+1)\tau}{n\tau+1}\Bigr) 
\;\stackrel S\sim\;\theta\left(n\tau+1, (r+1)\tau \right)  
\;\stackrel T\sim\;\theta\left(n\tau, (r+1)\tau \right) \,,$$ $$\eta\Bigl(\frac{\tau}{n\tau+1}\Bigr) 
\;\stackrel S\sim\;\eta\Bigl(-n-\frac{1}{\tau}\Bigr) 
\;\stackrel T\sim\;\eta\Bigl(-\frac{1}{\tau}\Bigr) \;\stackrel S\sim\;\eta(\tau) \,.$$ Inserting all omitted factors and dividing the first equations by the second, we obtain [\[WasLemma\]](#WasLemma){reference-type="eqref" reference="WasLemma"}.

Now applying [\[WasLemma\]](#WasLemma){reference-type="eqref" reference="WasLemma"} to $\tau=\frac{-1+i/\hbar}{n}$, with $\hbar=\frac h{2\pi}$, where $h$ positive and small, we find $$\begin{aligned}
f_{A_n,0}\left(\zeta_ne^{-h/n}\right)
= & 
\ \mathbf{e}\left(-C_n\frac{1+i\hbar}n\right)
\  \widetilde f_n\left(\frac{1+i\hbar}n\right) \\
= & 
\ \mathbf{e}\left(-C_n\frac{1+i\hbar}n+\frac{n-3}{24}\right) 
\widetilde f_n\left(\frac{-1+i/\hbar}n\right) 
\\
\label{pfnc}










= & 
\  \mathbf{e}\left(\frac n{24}-\frac18+\frac1{12n}-\frac1{4n^2}\right)
  e^{\mathrm L(X^{A_n})/nh} (1+ O(\hbar)) \,.

\end{aligned}$$ Taking the $4n$-th power of this and combining with Theorem [\[thm.nahmEM\]](#thm.nahmEM){reference-type="ref" reference="thm.nahmEM"} and its Corollary [\[UnitCor\]](#UnitCor){reference-type="ref" reference="UnitCor"}, we have an equality $$\label{compareexpansions}
\mathbf{e}\left(\frac{n^2}{6} - \frac{n}{2} + \frac{1}{3} - \frac{1}{n} \right) (1 + \ldots)
= 
\mathbf{e}\left(\frac{r(n-1)(n-2)}{6} \right) \omega^{4n} 
(\Phi^{4n}_{\zeta}(h) + \ldots ).$$ Writing $\xi_{\zeta}$ for the Bloch element corresponding to $A_n$, we know from Theorem [\[thm.nahmEM\]](#thm.nahmEM){reference-type="ref" reference="thm.nahmEM"} that there is an inclusion $P_{\zeta}(\xi)^{1/n} D_{\zeta}(1)^{r/n} \Phi_{\zeta}(h) \in F_n[[h]]$, where in this case $F = \mathbf Q(\zeta+ \zeta^{-1})$ and $F_n = \mathbf Q(\zeta)$. Thus from equation ([\[compareexpansions\]](#compareexpansions){reference-type="ref" reference="compareexpansions"}) we deduce that $$R_{\zeta}(\xi)^4 D_{\zeta}(1)^{4r} \mathbf{e}\left(- \frac{r(n-1)(n-2)}{6} \right) 
 = \mathbf{e}\left(- \frac{n^2}{6} + \frac{n}{2} - \frac{1}{3} + \frac{1}{n} \right)  \;\text{\rm mod}\;F^{\times n}_n.$$ Since $r = (n-3)/2$ and $D_{\zeta}(1) = \mathbf{e}(n/3)$ by Lemma [\[lem.Rz\]](#lem.Rz){reference-type="ref" reference="lem.Rz"}[\[partb.Rz\]](#partb.Rz){reference-type="ref" reference="partb.Rz"}, we deduce that $$R_{\zeta}(\xi)^4  = 
   \mathbf{e}\left(- \frac{n^2}{6} + \frac{n}{2} - \frac{1}{3} + \frac{1}{n}  + \frac{r(n-1)(n-2)}{6}  - \frac{4rn}{3} \right)
   \;\text{\rm mod}\;F^{\times n}_n,$$ If $(3,n) = 1$, the only term which is non-trivial modulo $n$th powers is $\mathbf{e}(1/n)$. (Recall that $n$ is odd.) If $3|n$, then $3|r$, so the only terms which are non-trivial modulo $n$th powers are now $\mathbf{e}(1/n)$ and $\mathbf{e}(-1/3)$. Hence we deduce that $$\label{usedbelow}
   R_{\zeta}(\xi)^4 = \begin{cases} \mathbf{e}(1/n), & (n,3) = 1, \\
   \mathbf{e}(1/n)\mathbf{e}(-1/3), & 3|n. \end{cases}$$ From equation [\[eq:comparetorsion\]](#eq:comparetorsion){reference-type="eqref" reference="eq:comparetorsion"}, we find that $$\xi_\zeta= 
\sum_{k=2}^{(n-1)/2}
{\left[ 1 - \left(\frac{\zeta^{1/2}-\zeta^{-1/2}}{\zeta^{k/2}-\zeta^{-k/2}}\right)^2 \right]}.$$ Using the $k \mapsto -k$ symmetry in Equation [\[eq.etaz\]](#eq.etaz){reference-type="eqref" reference="eq.etaz"}, we deduce that $$\eta_\zeta= 
{[\infty] + 2 [0] + 
2 
\sum_{k=2}^{(n-1)/2}
\left[ 1 - \left(\frac{\zeta-\zeta^{-1}}{\zeta^{k}-\zeta^{-k}}\right)^2 \right]
},$$ and hence (using the identities $2[\infty] = [0]$ and $[\infty] = 2[0]$) we deduce that $$\label{quicker}
2 \xi_{\zeta} =  \eta_{\zeta^{1/2}} {- 4 [0] =\eta_{\zeta^{1/2}}  - [0]} \,.$$

It remains to show that $\eta_{\zeta^{1/2}} = \frac{1}{4} \cdot \eta_{\zeta}$ because then, by Equations [\[usedbelow\]](#usedbelow){reference-type="eqref" reference="usedbelow"} and [\[quicker\]](#quicker){reference-type="eqref" reference="quicker"}, and the fact that $R_{\zeta}([0])^{-2} = D_{\zeta}(1)^{2} = \mathbf{e}(2/3)$ if $3|n$ and $1$ otherwise, we will have $$R_{\zeta}(\eta_{\zeta}) = R_{\zeta}(\zeta_{\zeta^{1/2}})^4
=
{ R_{\zeta}(\xi)^8  R_{\zeta}([0])^{-2} = \mathbf{e}(2/n)}

= \zeta^2.$$ which is the desired conclusion. In fact, more generally, we show that $\eta_{\zeta^k} = k^2 \eta_{\zeta}$ for $k$ prime to $n$. Suppose that $R_{\zeta}(\eta_{\zeta}) = \zeta^{m}$. Since this does not depend on the choice of $\zeta$, it must also be true that $R_{\zeta^k}(\eta_{\zeta^k}) = \zeta^{km}$. By Lemma [\[lemma:compatibility\]](#lemma:compatibility){reference-type="ref" reference="lemma:compatibility"}([\[lemma:compatibilitytwo\]](#lemma:compatibilitytwo){reference-type="ref" reference="lemma:compatibilitytwo"}), we have $$R_{\zeta^k}(\eta_{\zeta}) = R_{\zeta}(\eta_{\zeta})^{1/k} = \zeta^{m/k} \,,$$ and thus $$\zeta^{mk} = R_{\zeta^k}(k^2 \eta_{\zeta}) = R_{\zeta^k}(\eta_{\zeta^k}) \,.$$ By Lemma [\[invertible\]](#invertible){reference-type="ref" reference="invertible"}, the map $R_{\zeta^k}$ is injective on the torsion subgroup of $B(\mathbf Q(\zeta)^{+})$, and thus $\eta_{\zeta^k} = k^2 \eta_{\zeta}$, as desired. As a consistency check, note that the Galois group $\mathrm{Gal}(\mathbf Q(\zeta)/\mathbf Q(\zeta)^{+})$ should act trivially on $B(\mathbf Q(\zeta)^{+})$, and we indeed see that the non-trivial element $\sigma: \zeta \mapsto \zeta^{-1}$ satisfies $$\sigma \eta_{\zeta} = \eta_{\zeta^{-1}} = (-1)^2 \eta_{\zeta} = \eta_{\zeta} \,.$$ ◻
:::
