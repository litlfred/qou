---
doc_id: arxiv-2509.04267v3
doc_title: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology"
section_id: sec-006-4-quantum-cocycle-invariants-via-traces
section_title: "Quantum cocycle invariants via traces"
section_number: 4
pages: 8-12
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.978
doc_brief: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
[]{#sec:inf_def label="sec:inf_def"}

Let $S = (R, \alpha, \beta, \mu)$ be an EYBO. Suppose that there is an infinitesimal deformation $$\tilde R=\phi_0 + \hbar \phi_1=R + \hbar \phi
\quad {\rm on} \quad 
\tilde V={\mathbb k} [[ \hbar ]] / (\hbar^2 )  \otimes V .$$ Suppose further that there is $\tilde \mu = \mu + \hbar \mu_1 : \tilde V \rightarrow \tilde V$ such that $\tilde S = (\tilde R, \alpha, \beta, \tilde \mu )$ is an EYBO on $\tilde V$. Then we say that $\tilde S$ is an *infinitesimal deformation* of an EYBO $S$, or $S$ is deformed to $\tilde S$. In this situation we also denote the deformation by the pair $(\phi,\mu_1)$, and call it an *enhanced* Yang-Baxter $2$-cocycle, or EYB $2$-cocycle for short. We also simply say that $\phi$ is an EYB $2$-cocycle when $\mu_1$ is understood from context.

::: definition
[]{#def:deg1_operator label="def:deg1_operator"}

Let $R$ be a YB operator with inverse $R^{-1}$, and let $\phi$ be a YB $2$-cocycle. Let $b_m$ be an $m$-braid. Then, we associate an operator $\Psi_\phi(b_m)$ to the braid as follows. We consider the operator $\tilde R = \phi_0 + \hbar \phi_1$ with $\phi_0=R$ on $\tilde V = {\mathbb k} [[ \hbar ]] / (\hbar^2 ) \otimes V$ as above. Observe that $\tilde R$ is invertible with inverse $\tilde R^{-1} = \hat \phi_0 + \hbar \hat \phi_1$, where $\hat \phi_0 = R^{-1}$ and $\hat \phi_1 = -R^{-1}\phi_1R^{-1}$. For $R$ and/or $R^{-1}$ we use the notation $R^{\pm}$, and similarly for $\tilde R^{\pm}$.

To each standard generator (and its inverse) $\sigma^{\pm}_i$, $i=1,\ldots, m-1$, of the braid group $\mathbb  B_m$, we associate the operator $\sigma_i^{\pm}  \mapsto \mathbb 1^{\otimes ( i-1)}\otimes \tilde R^\pm \otimes \mathbb 1^{\otimes (m-i-1)}$. Then, from a presentation of $b_m$ as a product of $\sigma_i^{\pm}$'s we obtain an operator obtained as composition of terms of type $\mathbb 1^{\otimes (i-1)}\otimes \tilde R^\pm \otimes \mathbb 1^{\otimes (m-i-1)}$, which we denote $\Psi_\phi(b_m)$. We let $\Psi^i_\phi(b_m)$, $i=0,1$, be defined by $$\Psi_\phi(b_m) = \Psi^0_\phi(b_m) + \hbar \Psi^1_\phi(b_m) \in 
             {\rm Hom}(\tilde{V}^{\otimes m},\tilde{V}^{\otimes m}).$$
:::

We use the following notation.

::: definition
[]{#def:gamma label="def:gamma"} For given non-negative integers $k$ and $n$, set $$\begin{aligned}
                    \Gamma_n^m &=& \{(j_1,\ldots,j_m )\ |\  j_1+\cdots +j_m = n, \  j_\ell \geq 0 \}, \\
                    \hat\Gamma_n^m  &=& \{(j_1,\ldots,j_m )\ |\  j_1+\cdots +j_m= n, \  j_\ell \geq 0\ {\rm and}\  j_\ell \neq n,\ {\rm for\ all}\ \ell=1,\ldots,m \}.
\end{aligned}$$ When $m$ is apparent, we also use $\Gamma_n=\Gamma_n^m$ and $\hat\Gamma_n=\hat\Gamma_n^m$. For $n=1$ we may also omit the subscript.
:::

::: theorem
[]{#thm:inf_YB_inv label="thm:inf_YB_inv"} Let $S = (R, \alpha, \beta, \mu)$ be an EYBO on $V$. Let $\Gamma=\Gamma^3_1$. Then there exists an infinitesimal deformation $\tilde R=\phi_0 + \hbar \phi_1=R + \hbar \phi$ and $\tilde \mu = \mu + \hbar \mu_1$ on $\tilde V= {\mathbb k} [[ \hbar ]] / (\hbar^2 )  \otimes V$ such that $\tilde S = (\tilde R, \alpha, \beta, \tilde \mu )$ is an EYBO on $\tilde V$ if and only if the following equations hold: $$\begin{aligned}
            \sum_{(i,j,k)\in \Gamma} (\mu_i\otimes \mu_j)\phi_k &=& \sum_{(i,j,k)\in \Gamma} \phi_i (\mu_j\otimes \mu_k),\label{eqn:inf_mu_comm}\\
            \sum_{(i,j,k)\in \Gamma}\mathop{\mathrm{Tr}}_2(\phi_i(\mu_j\otimes \mu_k)) &=& \alpha\beta \mu_1,\label{eqn:inf_partial_tr+}\\
            \sum_{(i,j,k)\in \Gamma}\mathop{\mathrm{Tr}}_2(\hat \phi_i(\mu_j\otimes \mu_k)) &=& \alpha^{-1}\beta \mu_1,\label{eqn:inf_partial_tr-}
    
\end{aligned}$$ where $\hat \phi_0 = \phi_0^{-1}$, and $\hat \phi_1 = -\phi_0^{-1}\phi_1\phi_0^{-1}$.

Moreover, if $\tilde S$ is an EYBO and $b_m$ is an $m$-braid representing a knot $K$, the quantity $$\begin{aligned}
        \Psi^{1 }_{\tilde S}(b_m) =             \sum_{(i,j_1,\ldots,j_m)\in \Gamma^{m+1}} \alpha^{-w(b_m)}\beta^{-n}\mathop{\mathrm{Tr}}(\Psi^i_\phi(b_m)( \mu_{j_1}\otimes \cdots \otimes \mu_{j_m})) \label{eqn:inv_deg1}
    
\end{aligned}$$ does not depend on the choice of $b_m$ used, and it is invariant under Markov moves. It is therefore a knot invariant.
:::

::: proof
*Proof.* We prove the first statement. Observe that given $\tilde R = \phi_0 + \hbar \phi_1$, its inverse is given by $\tilde R^{-1} =  \hat \phi_0 + \hbar \hat \phi_1$, up to quadratic terms in $\hbar$, as one might verify directly. The characterization of the conditions on $\tilde S$ being an EYBO module up to degree 2 gives, quotienting out higher degrees in $\hbar$, Equation [\[eqn:mu_comm\]](#eqn:mu_comm){reference-type="eqref" reference="eqn:mu_comm"} and Equation [\[eqn:partial_tr\]](#eqn:partial_tr){reference-type="eqref" reference="eqn:partial_tr"}.

For the second statement, since $\tilde S$ is an EYBO on $\tilde V= \mathbb k[[\hbar]]/(\hbar^2) \otimes  V$, using classical results of Turaev in [@Tur], it follows that the trace of $\alpha^{-w(D)}\beta^{-n}\Psi_\phi(b_m)$ is a knot invariant. Since the summation $\sum_{(i,j_1,\ldots,j_m)\in \Gamma^{m+1}}$ collects degree 1 terms with respect to $\hbar$, one sees that it gives precisely the term in [\[eqn:inv_deg1\]](#eqn:inv_deg1){reference-type="eqref" reference="eqn:inv_deg1"}. ◻
:::

::: definition
[]{#def:qcocy label="def:qcocy"} From the second statement of this theorem, we denote the Expression ([\[eqn:inv_deg1\]](#eqn:inv_deg1){reference-type="ref" reference="eqn:inv_deg1"}) by $\Phi^1_{\tilde S}( K)$, or $\Phi^1_\phi (K)$ when other data for $\tilde S$ are understood, without an explicit reference to the braid $b_m$ used to obtain the operator $\Psi^1_{\tilde S} (b_m)$, as the trace is independent of this choice. We also denote the Turaev's invariant for the undeformed $S=(R,  \alpha, \beta, \mu )$ by $\Phi^0_\phi( K)$, and combine both by the expression $\Phi_\phi(K) = \Phi^0_\phi(K) + \hbar \Phi^1_\phi(K)$.
:::

We now consider the effect of deforming an EYBO by a YB coboundary.

::: lemma
[]{#lem:cob_EYBO label="lem:cob_EYBO"} Let $(R,\alpha,\beta,\mu)$ denote an EYBO, and let $\phi = \delta^1_{\rm YB}(f)$ be a cobounded YB $2$-cocycle. Then, $(\tilde R, \alpha, \beta, \tilde \mu)$ is an EYBO, where $\tilde R = R + \hbar \phi$, and $\tilde \mu = \mu + \hbar \mu_1$, with $\mu_1 = \mu f - f\mu$.
:::

::: proof
*Proof.* We first show [\[eqn:inf_mu_comm\]](#eqn:inf_mu_comm){reference-type="eqref" reference="eqn:inf_mu_comm"}, i.e. $\tilde R(\tilde \mu\otimes \tilde \mu) = (\tilde \mu\otimes \tilde \mu)\tilde R$. We need to show that the following equation holds $$\begin{aligned}
                            \phi(\mu\otimes \mu) + R(\mu_1\otimes \mu) + R(\mu\otimes \mu_1) &=& (\mu\otimes \mu)\phi + (\mu_1\otimes \mu)R + (\mu\otimes \mu_1)R. 
                    
\end{aligned}$$ For the left-hand side, using the defining formula of $\phi = \delta^1_{\rm YB}(f)$ and the fact that $R$ and $(\mu\otimes \mu)$ commute by assumption, we compute $$\begin{aligned}
                \phi(\mu\otimes \mu) + R(\mu_1\otimes \mu) + R(\mu\otimes \mu_1) &=& R(f\mu\otimes \mu) + R(\mu\otimes f\mu) - (f\mu\otimes \mu)R - (\mu\otimes f\mu)R \\
                && + R(\mu f\otimes \mu)  - R(f\mu \otimes \mu) + R(\mu\otimes \mu f) - R(\mu\otimes f\mu).
        
\end{aligned}$$ Similarly, for the right-hand side we obtain $$\begin{aligned}
                (\mu\otimes \mu)\phi + (\mu_1\otimes \mu)R + (\mu\otimes \mu_1)R &=& R(\mu f\otimes \mu) + R(\mu\otimes \mu f) - (\mu f\otimes \mu)R - (\mu\otimes \mu f)R\\
                && + (\mu f\otimes \mu)R - (f\mu \otimes \mu)R + (\mu \otimes \mu f)R - (\mu\otimes f\mu)R. 
        
\end{aligned}$$ The required equality is therefore seen to hold.

We now consider [\[eqn:inf_partial_tr+\]](#eqn:inf_partial_tr+){reference-type="eqref" reference="eqn:inf_partial_tr+"} and [\[eqn:inf_partial_tr-\]](#eqn:inf_partial_tr-){reference-type="eqref" reference="eqn:inf_partial_tr-"}, i.e. we need to show the equalities $$\begin{aligned}
                \mathop{\mathrm{Tr}}_2(\phi(\mu\otimes \mu)) + \mathop{\mathrm{Tr}}_2(R(\mu_1\otimes \mu)) + \mathop{\mathrm{Tr}}_2(R(\mu\otimes \mu_1)) &=& \alpha\beta \mu_1 , \\
                \mathop{\mathrm{Tr}}_2(\hat\phi(\mu\otimes \mu)) + \mathop{\mathrm{Tr}}_2(R^{-1}(\mu_1\otimes \mu)) + \mathop{\mathrm{Tr}}_2(R^{-1}(\mu\otimes \mu_1)) &=& \alpha^{-1}\beta \mu_1,
        
\end{aligned}$$ where $\hat\phi := -R^{-1}\phi R^{-1}$ is the infinitesimal component of the inverse of $\tilde R$. Observe that $$\begin{aligned}
                R^{-1}\phi R^{-1} 
                &=& R^{-1}\delta^1_{\rm YB}(f) R^{-1}   \\
                &=& R^{-1}R(f\otimes \mathbb 1)R^{-1} + R^{-1}R(\mathbb 1\otimes f)R^{-1} - R^{-1}(f\otimes \mathbb 1)RR^{-1} + R^{-1}R(\mathbb 1\otimes f)RR^{-1}\\
                &=& (f\otimes \mathbb 1)R^{-1} + (\mathbb 1\otimes f)R^{-1} - R^{-1}(f\otimes \mathbb 1)+ R^{-1}R(\mathbb 1\otimes f)\\
                &=& - \delta^1_{  R^{-1} } (f),  
        
\end{aligned}$$ where $\delta^1_{ R^{-1}}(f)$ is the first YB differential of the operator $R^{-1}$ applied to $f$.

Therefore, if $(R,\alpha, \beta,\mu)$ is an EYBO, then we have that $(R^{-1},\alpha^{-1},\beta,\mu)$ is also an EYBO. Hence it is sufficient to prove [\[eqn:inf_partial_tr+\]](#eqn:inf_partial_tr+){reference-type="eqref" reference="eqn:inf_partial_tr+"}, since [\[eqn:inf_partial_tr-\]](#eqn:inf_partial_tr-){reference-type="eqref" reference="eqn:inf_partial_tr-"} is equivalent to [\[eqn:inf_partial_tr+\]](#eqn:inf_partial_tr+){reference-type="eqref" reference="eqn:inf_partial_tr+"} for the EYBO $(R^{-1},\alpha^{-1},\beta,\mu)$, with $\hat \phi =  \hbar \delta^1_{ R^{-1}}(f)$ and $\tilde \mu= \mu +\hbar\mu_1$. For the left-hand side of [\[eqn:inf_partial_tr+\]](#eqn:inf_partial_tr+){reference-type="eqref" reference="eqn:inf_partial_tr+"} we have $$\begin{aligned}
                \lefteqn{\mathop{\mathrm{Tr}}_2(\phi(\mu\otimes \mu)) + \mathop{\mathrm{Tr}}_2(R(\mu_1\otimes \mu)) + \mathop{\mathrm{Tr}}_2(R(\mu\otimes \mu_1))}\\ 
                &=& \mathop{\mathrm{Tr}}_2[R(f\otimes \mathbb 1)(\mu\otimes \mu) + R(\mathbb 1\otimes f)(\mu\otimes \mu)
                 - (f\otimes \mathbb 1)R(\mu\otimes \mu) - (\mathbb 1\otimes f)R(\mu\otimes \mu)\\
                 && \hspace{1cm} + R(\mu f\otimes \mu) - R(f\mu \otimes \mu) + R(\mu\otimes \mu f) - R(\mu\otimes f\mu)]\\
                 &=& \mathop{\mathrm{Tr}}_2[R(f\otimes \mathbb 1)(\mu\otimes \mu) + R(\mathbb 1\otimes f)(\mu\otimes \mu)
                 - (f\otimes \mathbb 1)(\mu\otimes \mu)R - (\mathbb 1\otimes f)(\mu\otimes \mu)R\\
                 && \hspace{1cm} + R(\mu f\otimes \mu) - R(f\mu \otimes \mu) + R(\mu\otimes \mu f) - R(\mu\otimes f\mu)]\\
                 &=& -\mathop{\mathrm{Tr}}_2[(f\otimes \mathbb 1)(\mu\otimes \mu)R] 
                 + \mathop{\mathrm{Tr}}_2[R(\mu\otimes \mu)(f\otimes \mathbb 1)]\\
                 && - \mathop{\mathrm{Tr}}_2[(\mathbb 1\otimes f)(\mu\otimes \mu)R] 
                 + \mathop{\mathrm{Tr}}_2[R(\mu\otimes \mu)(\mathbb 1\otimes f)]\\
                 &=& -f\mathop{\mathrm{Tr}}_2[(\mu\otimes \mu)R] 
                     + \mathop{\mathrm{Tr}}_2[R(\mu\otimes \mu)]f - \mathop{\mathrm{Tr}}_2[(\mathbb 1\otimes f)(\mu\otimes \mu)R] 
            + \mathop{\mathrm{Tr}}_2[R(\mu\otimes \mu)(\mathbb 1\otimes f)]\\
                &=& -f\alpha\beta \mu
                + \alpha\beta\mu f\\
                 &=& \alpha\beta[\mu f-f\mu]\\
                 &=& \alpha\beta\mu_1,   
        
\end{aligned}$$ where we have used [\[eqn:mu_comm\]](#eqn:mu_comm){reference-type="eqref" reference="eqn:mu_comm"} and [\[eqn:partial_tr\]](#eqn:partial_tr){reference-type="eqref" reference="eqn:partial_tr"} for $R$ and $\mu$, along with $$\begin{aligned}
                - \mathop{\mathrm{Tr}}_2[(\mathbb 1\otimes f)(\mu\otimes \mu)R] + \mathop{\mathrm{Tr}}_2[R(\mu\otimes \mu)(\mathbb 1\otimes f)]=0,
        
\end{aligned}$$ by the cyclic property of the partial trace with respect to maps that factor as $\mathbb 1\otimes f$, and $$\begin{aligned}
                \mathop{\mathrm{Tr}}_2[(f\otimes 1)(\mu\otimes \mu)R] &=& f\mathop{\mathrm{Tr}}_2((\mu\otimes \mu)R), \\
                \mathop{\mathrm{Tr}}_2[R(\mu\otimes \mu)(f\otimes 1)] &=& \mathop{\mathrm{Tr}}_2[R(\mu\otimes \mu)]f.
         
\end{aligned}$$ This completes the proof. ◻
:::

The following is an analogue, in our setting, of the result for quandle invariants that states that the invariant of a coboundary is the number of quandle colorings, see [@CJKLS].

::: proposition
[]{#prop:cob label="prop:cob"} Let $K$ be a knot. Let $(R,\alpha,\beta,\mu)$ be an EYBO, let $\phi := \delta^2_{\rm YB}(f)$ be a coboundary for some $1$-cochain $f$, and set $\mu_1 = \mu f - f\mu$. Then, we have $\Phi_\phi(K) = \Phi_\phi^0(K)$. In other words, the infinitesimal part of the quantum cocycle invariant vanishes, $\Phi_\phi^1(K)=0$.
:::

::: proof
*Proof.* Applying Lemma [\[lem:cob_EYBO\]](#lem:cob_EYBO){reference-type="ref" reference="lem:cob_EYBO"}, it follows that $\Phi_\phi(K)$ is well defined. Let $b_m$ denote a braid on $m$-string whose closure is $K$. We show that $$\alpha^{w(b_m)}\beta^m\Phi_\phi^1(K) = \sum_{(i,j_1,\ldots, j_m)\in \Gamma^{m+1}} \mathop{\mathrm{Tr}}(\Psi_\phi^i(b_m)(\mu_{j_1}\otimes \cdots \otimes \mu_{j_m})) =0.$$

In this proof, we will refer to the arcs of $b_m$ that are bounded by crossings (regardless of whether the arc in question is an over or under arc at the end crossings), and *external* otherwise. External arcs have at least one end at the top or bottom of the braid, and internal arcs do not. We claim that the only terms in the operator $\Psi_\phi^1(b_m)$ that do not vanish are those where $\phi$ appears in a position such that it has either external incoming arcs, or external outgoing arcs. In fact, if an arc is internal, then it takes part in two consecutive crossings. The term $\Psi_\phi^1$ consists of the braid $b_m$ where each crossing is replaced by $R^\pm$, except for one of the crossings where $\phi$ appears. Moreover, $\phi$ appears exactly once in each position. If we consider an internal arc, then there are two terms in the sum defining $\Psi_\phi^1$ where $\phi$ appears, once in the top crossing and once in the bottom crossing. There are three different types of configurations associated to this situation. Namely, we can have $b_m = b'_m\sigma_i^\pm\sigma_i^\pm b''_m$, or $b_m = b'_m \sigma_i^\pm\sigma_{i+1}^\pm b''_m$, or $b_m = b'_m\sigma_{i+1}^\pm\sigma^\pm_ib''_m$.

<figure id="cancel">
<div class="center">
<img src="cancel" style="width:3.8in" />
</div>
<figcaption></figcaption>
</figure>

First, we consider the case where all crossings are positive. We consider only the case $b_m = b'_m\sigma_i\sigma_{i+1}b''_m$, as the other two are substantially the same, and we show the fact that the contribution to $\Psi^1_\phi(b_m)$ vanishes for the terms where $\phi$ appears in the position of $\sigma_i$, or $\sigma_{i+1}$. These terms correspond to the sum $$\begin{aligned}
                    \Psi_\phi^0(b'_m)\circ (\phi\otimes \mathbb 1)(\mathbb 1\otimes R)\circ  \Psi_\phi^0(b''_m) + \Psi_\phi^0(b'_m)\circ (R\otimes \mathbb 1)(\mathbb 1\otimes \phi)\circ  \Psi_\phi^0(b''_m),
            
\end{aligned}$$ which is part of the sum defining $\Psi_\phi^1(b_m)$. In the left-hand side of Figure [1](#cancel){reference-type="ref" reference="cancel"}, these two terms are depicted. Since $$\phi = \delta^2_{\rm YB}(f) = R(f\otimes \mathbb 1) + R(\mathbb 1\otimes f) - (f\otimes \mathbb 1)R - (\mathbb 1\otimes f)R,$$ we can pair the elements corresponding to $R(f\otimes \mathbb 1)$ associated to $\Psi_\phi^0(b'_m)\circ (\phi\otimes \mathbb 1)(\mathbb 1\otimes R)\circ  \Psi_\phi^0(b''_m),$ and $- (\mathbb 1\otimes f)R$ in $\Psi_\phi^0(b'_m)\circ (R\otimes \mathbb 1)(\mathbb 1\otimes \phi)\circ  \Psi_\phi^0(b''_m).$ These terms are seen to cancel. In the right-hand side of Figure [1](#cancel){reference-type="ref" reference="cancel"} these 1-cochains are depicted as circles on the corresponding edges. The two terms represented by circles on the middle edge are the canceling pair. The cancelations of 1-cocycles on arcs are also seen in diagrams of Figure [\[YBdiff1\]](#YBdiff1){reference-type="ref" reference="YBdiff1"}, where circles from a single YB 2-cocycle are distributed to each adjacent edge, and two circles coming from crossings that bound each internal arc represent canceling terms. This diagrammatic interpretation was also used in [@CJKLS] for quandle cocycle invariants.

Since, as shown in Lemma [\[lem:cob_EYBO\]](#lem:cob_EYBO){reference-type="ref" reference="lem:cob_EYBO"}, $\phi^{-1} = \delta^2_{R^{-1}}(f)$, it follows that the computation is substantially the same when $\sigma_i$ is replaced by $\sigma_i^{-1}$, upon changing $R$ with $R^{-1}$. So, the same calculation as above can be applied to the cases where a negative crossing appears, and we see that the terms all cancel. We proceed in the same manner for each internal arc, therefore pairing all the terms arising from each instance of $\phi$ appearing in the positions of the crossings of $b_m$, and cancel all the terms where $f$ appears on internal arcs. The only terms that are potentially nonzero in $\Psi^1_\phi(b_m)$ are therefore those in which $f$ appears on external arcs.

By adding canceling pairs $\sigma_i \sigma_i^{-1}$ if necessary, we may assume that all strings cross at least another string of the braid. Further, observe that all instances where $f$ appears as a top arc have positive sign, while all instances where $f$ appears on a bottom arc have negative sign. Therefore, we have $$\begin{aligned}
                    \lefteqn{\sum_{(i,j_1,\ldots, j_m)\in \Gamma^{m+1}} \mathop{\mathrm{Tr}}(\Psi_\phi(b_m)(\mu_{j_1}\otimes \cdots \otimes \mu_{j_m}))}\\
                    &=& \mathop{\mathrm{Tr}}(\Psi^1_\phi(b_m)(\mu_0\otimes \cdots \otimes \mu_0)) + \sum_{(j_1,\ldots, j_m)\in \Gamma^m} \mathop{\mathrm{Tr}}(\Psi^0_\phi(b_m)(\mu_{j_1}\otimes \cdots \otimes \mu_{j_m}))\\
                    &=& \sum_{i=1}^m \mathop{\mathrm{Tr}}[\Psi^0_\phi(b_m)(\mu_0^{\otimes (i-1)  }\otimes f\mu_0\otimes \mu_0^{\otimes (m-i-1) }) - (\mathbb 1^{\otimes (i-1) }\otimes f\otimes \mathbb 1^{\otimes ( m-i-1) })\Psi^0_\phi(b_m)(\mu_0 \otimes \cdots \otimes \mu_0)]\\
                    && + \sum_{i=1}^m \mathop{\mathrm{Tr}}(\Psi^0_\phi(b_m)(\mu_0^{\otimes (i-1) }\otimes \mu_1\otimes \mu_0^{\otimes (m-i-1) })) 
                    
\end{aligned}$$ $$\begin{aligned}
                    &\stackrel{(A)}{=} & \sum_{i=1}^m \mathop{\mathrm{Tr}}[\Psi^0_\phi(b_m)(\mu_0^{\otimes (i-1)}\otimes f\mu_0\otimes \mu_0^{\otimes (m-i-1)}) - \Psi^0_\phi(b_m)(\mu_0^{\otimes (i-1) }\otimes \mu_0f\otimes \mu_0^{\otimes (m-i-1) })]\\
                    && + \sum_{i=1}^m \mathop{\mathrm{Tr}}(\Psi^0_\phi(b_m)(\mu_0^{\otimes (i-1)}\otimes \mu_1\otimes \mu_0^{\otimes (m-i-1)  }))\\
                    &=& - \sum_{i=1}^m \mathop{\mathrm{Tr}}(\Psi^0_\phi(b_m)(\mu_0^{\otimes (i-1)}\otimes \mu_1\otimes \mu_0^{\otimes (m-i-1) })) + \sum_{i=1}^m \mathop{\mathrm{Tr}}(\Psi^0_\phi(b_m)(\mu_0^{\otimes (i-1)}\otimes \mu_1\otimes \mu_0^{\otimes (m-i-1)}))\\
                    &=& 0
            
\end{aligned}$$ where the equality $(A)$ follows from the cyclic property of the partial trace. ◻
:::
