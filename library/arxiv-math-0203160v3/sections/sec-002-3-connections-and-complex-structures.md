---
doc_id: arxiv-math-0203160v3
doc_title: "arXiv:math/0203160v3 [math.QA] 28 Oct 2002"
section_id: sec-002-3-connections-and-complex-structures
section_title: "Connections and complex structures."
section_number: 3
pages: 6-8
source_pdf: 0203160v3.pdf
source_sha256: a84f478d72d40af2
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 1.0
doc_brief: "arXiv:math/0203160v3 [math.QA] 28 Oct 2002 — We analyze in detail projective modules over two-dimensional noncom- mutative tori and complex structures on these modules.We concentrate our attention on"
---
One can define a connection on a right $T_{\theta }^{d}$-module $E$ as a set of ${\mathbb C}$-linear operators $\nabla
_{1},...,\nabla _{d}$ obeying Leibniz rule: $$\nabla _{\alpha }(ea)=\nabla _{\alpha }e\cdot a+e\cdot \delta _{\alpha }a\label{con}$$

where $e\in E,a\in T_{\theta }^{d}$ and the derivatives $\delta _{\alpha }a$ are specified by the formula $\delta _{\alpha }U_{\overrightarrow{n}}=2\pi
niU_{\overrightarrow{n}}$ (see\[1\]). It will be convenient for us to generalize the notion of connection replacing $\delta _{\alpha }$ in ([\[con\]](#con){reference-type="ref" reference="con"}) by $\delta _{\alpha }^{\prime }=a_{\alpha }^{\beta }\delta _{\beta }$ where $a_{\alpha }^{\beta }$ is a non-degenerate matrix. A connection $\nabla
_{1},...,\nabla _{d}$ is a constant curvature connection if $$\left[ \nabla _{\alpha },\nabla _{\beta }\right]=i\,f_{\alpha \beta }\cdot 1$$ where $f_{\alpha \beta }$ are numbers and $1$ stands for identity operator. Similar definitions can be given for left modules. We always consider unitary connections (i.e. operators $\nabla _{\alpha }$ should be anti Hermitian). It is easy to check that operators $$\nabla _{1}=2\,\pi\,i\frac{m}{n+m\theta }x,\text{ \ \ }\nabla
_{2}=2\,\pi\,\frac{d}{dx}\label{conscon}$$

specify a constant curvature connection of right $T_{\theta }$-module $E_{m,n}.$ The same operators determine a connection (in generalized sense) on $E_{n,m}$ considered as a left $T_{\theta
^{\prime }}$-module. This follows from relations $[\nabla
_{i},\nabla_{j}]=\frac{2\pi\,i\,m}{n+m\theta}$. We see that $\nabla _{1}, \nabla _{2}$ can be considered as a constant curvature connection on $(T_{\theta ^{\prime }},T_{\theta
})$-bimodule.

If $\nabla _{1},\nabla _{2}$ is a constant curvature connection on a module $E$ we can introduce a complex structure on $E$ fixing $\overline{\partial \text{-}}$connection  $\overline{\nabla
}=\lambda_{1} \nabla _{1}+\lambda_{2} \nabla _{2},$where $\lambda_{1}$ and $\lambda_{2}$ are complex numbers and the quotient $\tau =\lambda_{1}/\lambda_{2}$ is not real [@Sc3]. This complex structure on a $T_{\theta }$-module corresponds to complex structure on $T_{\theta },$ specified by means of $\overline{\partial }$-derivative $\lambda_{1} \delta
_{1}+\lambda_{2} \delta _{2}$. By definition, vector $\Theta \in
E$ is holomorphic if: $$\overline{\nabla }\Theta =0$$

Notice that the notion of holomorphicity depends only on $\tau =\lambda_{1}/\lambda_{2}$, therefore we say that $\overline{\nabla }$ and $\rho \overline{\nabla }$ where $\rho
\neq 0$ determine the same complex structure on $E.$ Holomorphic vectors are closely related to theta-functions, hence we call  holomorphic vectors in basic modules theta-vectors.

Let us consider  holomorphic vectors in $T_{\theta }$-modules $E_{n,m},$ assuming that $n$ and $m$ are relatively prime. In this case all constant curvature connections have the form $\nabla _{\alpha }=\nabla _{\alpha
}^{0}+c_{\alpha }$, where $\nabla _{\alpha }^{0}$ stand for the connection ([\[conscon\]](#conscon){reference-type="ref" reference="conscon"}) and $c_{_{1}},c_{_{2}}$ are constants. The equation $\overline{\nabla }\Theta =0$ takes the form $$(i\tau \frac{m}{n+m\theta }x+\frac{\partial }{\partial x}+c)\varphi (x,\mu
)=0$$

If $\limfunc{Im}\tau <0$ it has $m$ linearly independent solutions $$\varphi _{\alpha }(x,\mu )=e^{-\frac{1}{2}\sigma x^{2}-cx}\delta _{\alpha
}^{\mu }\label{stdbasis}$$

where $$\sigma =i\tau \frac{m}{n+m\,\theta },\qquad \mu\in {\mathbb Z}_{m}$$

The functions ([\[stdbasis\]](#stdbasis){reference-type="ref" reference="stdbasis"}) belong to ${\cal S}$ only if $\limfunc{Re}\sigma >0$. We assumed that $n+m\theta >0$; in the case $n+m\theta <0$, the condition of existence of holomorphic vectors is that $\limfunc{Im}\tau >0$. We see that in the case when holomorphic vectors exist the space ${\cal H}_{n,m}$ of holomorphic vectors in $E_{n,m}$ is $m$-dimensional; the functions ([\[stdbasis\]](#stdbasis){reference-type="ref" reference="stdbasis"}) constitute a basis of ${\cal H}_{n,m}$. Considering $E_{n,m}$ as a $(T_{\theta ^{\prime }},T_{\theta })$-bimodule and taking into account that a constant curvature connection on $E_{n,m}$ is a constant curvature connection on the bimodule, one can define a notion of complex structure and of holomorphic vector for a bimodule. More precisely, complex structure on $T_{\theta }$-module $E_{n,m}$ induces a complex structure on same space considered as left $T_{\theta ^{\prime }}$-module in such a way that the notion of holomorphic vector remains the same. These two complex structures specify a complex structure on a bimodule; the notion of holomorphic vector in a bimodule coincides with corresponding notion for both modules. If ${\cal E}^{\prime }$ is a complex $(T_{\theta ^{\prime}},T_{\theta })$-bimodule, ${\cal E}^{\prime \prime }$ is a complex $(T_{\theta },T_{\theta ^{\prime \prime }})$-bimodule, then the $(T_{\theta
^{\prime }},T_{\theta ^{\prime \prime }})$-bimodule ${\cal E}={\cal E}^{\prime }\underset{T_{\theta }}{\otimes }{\cal E}^{\prime \prime }$ can be equipped with complex structure. We assume that complex structure on the right $T_{\theta }$-module ${\cal E}^{\prime }$ and on the left $T_{\theta }$ -module ${\cal E}^{\prime \prime }$ correspond to the same complex structure on $T_{\theta }$. One can prove [@Sc3] that tensor product of two  holomorphic vectors is again a holomorphic vector (i.e. we have a natural map ${\cal H}^{\prime }\otimes {\cal H}^{\prime \prime }$ into ${\cal H}$ where ${\cal H}^{\prime },{\cal H}^{\prime \prime }$ and ${\cal H}$ stand for spaces of holomorphic vectors in ${\cal E}^{\prime },{\cal E}^{\prime
\prime }$ and ${\cal E}$ correspondingly). Let the basis of ${\cal H}^{\prime }$ consist of:

$$\varphi^{\prime}_{\alpha}=e^{-\frac{1}{2}\sigma_{_{1}} x^{2}-c_{_{1}}x}\delta_{\alpha}^{\mu }$$

where

$$\sigma_{_{1}} =i\tau_{1} \frac{m}{n+m\,\theta },\qquad \mu\in {\mathbb Z}_{m},\qquad\alpha\in\left\{1,\ldots,m\right\}$$

and the basis of ${\cal H}^{\prime \prime }$ consist of:

$$\varphi^{\prime\prime}_{\beta}=e^{-\frac{1}{2}\sigma_{_{2}} y^{2}-c_{_{2}}x}\delta_{\beta}^{\nu }$$

where

$$\sigma_{_{2}} =i\tau_{2} \frac{l}{k-l\,\theta },\qquad \nu\in {\mathbb Z}_{l},\qquad\alpha\in\left\{1,\ldots,l\right\}$$ We assume that ${\cal E}^{\prime }$, considered as a right $T_{\theta }$--module, is isomorphic to $E_{n,m}$ , and that ${\cal E}^{\prime\prime }$, considered as a left $T_{\theta }$--module, is isomorphic to $E^{\prime}_{k,l}$. We can use ([\[prodbasis\]](#prodbasis){reference-type="ref" reference="prodbasis"}) to calculate $\varphi^{\prime}_{\alpha}\underset{T_{\theta }}{\otimes }\varphi^{\prime\prime}_{\beta}$. The condition that complex structures on ${\cal E}^{\prime }$ and ${\cal E}^{\prime\prime }$ correspond to the same complex structure on ${\cal E}$ implies $\tau_{1}=\tau_{2}$. Using this, we can check that the theta--functions that appear in ([\[prodbasis\]](#prodbasis){reference-type="ref" reference="prodbasis"}) do not depend on $z$ in our case. Applying ([\[prodbasis\]](#prodbasis){reference-type="ref" reference="prodbasis"}), we obtain that, $\varphi^{\prime}_{\alpha}\underset{T_{\theta }}{\otimes }\varphi^{\prime\prime}_{\beta}$ maps to $\Xi_{\alpha\,\beta}(z,\Delta)\in{\cal H}$ which is of the form:

$$\Xi_{\alpha\,\beta}(z,\Delta) = \sum_{\gamma} c_{\alpha\,\beta}^{\gamma}\,\varphi_{\gamma}(z,\Delta)$$

where

$$\begin{aligned}
\varphi_{\gamma}(z,\Delta)&=&\exp\left[\frac{\pi\,i\,\tau(n\,l+m\,k)(n+m\,\theta)}{k-l\,\theta}z^{2}-(c_{_{1}}+c_{_{2}})(n+m\,\theta)z\right]\,\delta_{\gamma}^{\Delta}
\end{aligned}$$

constitute a basis of ${\cal H}$ and the constants $c_{\alpha\,\beta}^{\gamma}$ are given by:

$$\begin{aligned}
c_{\alpha\,\beta}^{\gamma}=\Theta(s,t)\cdot e^{K}\nonumber
\end{aligned}$$

where $\Theta(s,t)$ a classical theta--function,

$$K=-\frac{\pi\,i\,\tau\,l}{m(n\,l+m\,k)}\,\gamma^{2}-\frac{\left(l(n+m\,\theta)c_{_{1}}-m(k-l\,\theta)c_{_{2}}\right)}{m(n\,l+m\,k)}\,\gamma+\pi\,i\,s\,q_{o}^{2}+2\,\pi\,i\,t\,q_{o}$$

and:

$$s=-m\,l\,(n\,l+m\,k)$$

$$t=\frac{l\,\tau\,\Delta-q_{o}(n\,l+m\,k)}{r} + \frac{c_{_{1}}\,l\,(n+m\,\theta)-c_{_{2}}\,m\,(k-l\,\theta)}{2\pi\,i\,r}$$
