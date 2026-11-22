---
doc_id: arxiv-2601.07042v1
doc_title: "A Tannakian description of the local Kaletha gerbe"
section_id: sec-008-24-descent
section_title: "Descent"
section_number: 2.4
pages: 9-12
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.91
doc_brief: "A Tannakian description of the local Kaletha gerbe — We construct, for a p-adic field F, an explicit semisimple Tannakian category RigIsocF whose category of fiber functors recovers Kaletha’s Galois"
---
[]{#sec:Descent label="sec:Descent"} We want to descend the Tannakian category $RP_{E/F,s}$ to a Tannakian category over $F$. The first step is to define a canonical $\Gamma_{L_E/F}$-action on the ring $R_{E/F}$.

Note that $L_E/L$ is a totally ramified extension and that the sequence: $$1 \to \Gamma_{L_E/L} \to W_{L_E/F} \to W_{L/F} \to 1,$$ is split by any lift of the Frobenius element in $W_{L/F}$. Fix such a splitting and hence a lift which we denote $\mathfrak{f}_F$. Restriction gives an injection $\Gamma_{L_E/L} \hookrightarrow \Gamma_{E/F}$. We denote the image of this injection by $\Omega_E$.

We now define a $\Gamma_{L_E/F}$-semilinear action of $W_{L_E/F}$ on $R_{E/F}$ which we denote $\widetilde{\Phi}_{R_{E/F}}$. We define the action of $\Gamma_{L_E/L}$ such that $\gamma(\ell_{(b_{\sigma})_{\sigma}}) = \gamma(\ell)_{(b_{\overline{\gamma}^{-1}\sigma})_{\sigma}}$, where $\overline{\gamma}$ is the projection of $\gamma$ to $\Gamma_{E/F}$. We define the action of $\mathfrak{f}_F$ such that $$\mathfrak{f}_F(\ell_{(b_{\sigma})_{\sigma}}) = ({\mathfrak{f}_F(\ell)\prod\limits_{\sigma' \in \Omega_E} \sigma'(\varpi_E)^{b_{\overline{\mathfrak{f}_F}^{-1}\sigma'}}})_{(b_{\overline{\mathfrak{f}_F}^{-1}\sigma})_{\sigma}}.$$

In particular, this implies that $$\mathfrak{f}_F^{-1}(\ell_{(b_{\sigma})_{\sigma}}) = ({\mathfrak{f}_F^{-1}(\ell)\prod\limits_{\sigma' \in \Omega_E} \mathfrak{f}_{F}^{-1}\sigma'(\varpi_E)^{-b_{\sigma'}}})_{(b_{\overline{\mathfrak{f}_F}\sigma})_{\sigma}},$$ which can be verified easily by checking that $\mathfrak{f}_{F}^{-1} \circ \mathfrak{f}_{F} = \text{id}$.

We need to check that this indeed induces an action of $W_{L_E/F}$. To do so, we need to check that for $\gamma \in \Gamma_{L_E/L}$, the action of $\mathfrak{f}_F \circ \gamma \circ \mathfrak{f}^{-1}_F \in \Gamma_{L_E/L}$ agrees with the action induced by the composition. Since both actions are semilinear in the correct way, we need only understand the action on $1_{(b_{\sigma})_{\sigma}}$. We have $$\begin{aligned}
    (\mathfrak{f}_F \circ \gamma \circ \mathfrak{f}^{-1}_F)(1_{(b_{\sigma})_{\sigma}})  & =  (\mathfrak{f}_F \circ \gamma)(\prod\limits_{\sigma' \in \Omega_E} \mathfrak{f}^{-1}_F\sigma'(\varpi_E)^{-b_{\sigma'}})_{(b_{\overline{\mathfrak{f}_F} \sigma})_{\sigma}})\\
    &=\mathfrak{f}_F(\prod\limits_{\sigma' \in \Omega_E} \gamma\mathfrak{f}^{-1}_F\sigma'(\varpi_E)^{-b_{\sigma'}})_{(b_{\overline{\mathfrak{f}_F \gamma^{-1}} \sigma})_{\sigma}})\\
    &=(\prod\limits_{\sigma' \in \Omega_E} \mathfrak{f}_F\gamma\mathfrak{f}^{-1}_F\sigma'(\varpi_E)^{-b_{\sigma'}} \prod\limits_{\sigma'' \in \Omega_E} \sigma''(\varpi_E)^{b_{\overline{\mathfrak{f}_F \gamma^{-1}\mathfrak{f}^{-1}_F}\sigma''}}))_{(b_{\overline{\mathfrak{f}_F \gamma^{-1} \mathfrak{f}^{-1}_F} \sigma})_{\sigma}}\\
    &=1_{(b_{\overline{\mathfrak{f}_F\gamma^{-1}\mathfrak{f}^{-1}_F}\sigma})_{\sigma}},
\end{aligned}$$ as desired.

The action does not depend on the choice of $\mathfrak{f}_F$. Indeed, any other lift is of the form $\gamma \mathfrak{f}_F$ for $\gamma \in \Gamma_{L_E/L}$ and we have $$\gamma \mathfrak{f}_F(\ell_{(b_{\sigma})_{\sigma}}) = \gamma \mathfrak{f}_F(\ell) \prod\limits_{\sigma' \in \Omega_E} \gamma\sigma'(\varpi_E)^{b_{\overline{\mathfrak{f}^{-1}_F}\sigma'}}_{(b_{\overline{\mathfrak{f}^{-1}_F\gamma^{-1}}\sigma})_{\sigma}} = \gamma\mathfrak{f}_F(\ell) \prod\limits_{\sigma' \in \Omega_E} \sigma'(\varpi_E)^{b_{\overline{\mathfrak{f}^{-1}_F\gamma^{-1}}\sigma'}}_{(b_{\overline{\mathfrak{f}^{-1}_F\gamma^{-1}}\sigma})_{\sigma}},$$ which is the same action $\gamma\mathfrak{f}_F$ would have if we had chosen it as our lift of Frobenius.

Finally, we need to compute the action of the canonical generator $\mathfrak{f}_E$ of $W_{L_E/E} \subset W_{L_E/F}$. We can write $\mathfrak{f}_E = \gamma \mathfrak{f}^{f(E/F)}_F$ for some $\gamma \in \Gamma_{L_E/L}$. Then $$\begin{aligned}
    \gamma \mathfrak{f}^{f(E/F)}_F(1_{(b_{\sigma})_{\sigma}})&=\gamma \left(\prod\limits_{k=1}^{f(E/F)} \prod\limits_{\sigma' \in \Omega_E} \mathfrak{f}^{f(E/F) -k}_F\sigma'(\varpi_E)^{b_{\overline{\mathfrak{f}^{-k}_F}\sigma}}_{(b_{\overline{\mathfrak{f}^{-f(E/F)}_F}\sigma})_{\sigma}}\right)\\
    &=\gamma \left(\prod\limits^{f(E/F)}_{k=1} \prod\limits_{\sigma' \in \mathfrak{f}^{-k}_F(\Omega_E)} \mathfrak{f}^{f(E/F)}_F\sigma'(\varpi_E)^{b_{\sigma'}}_{(b_{\overline{\mathfrak{f}^{-f(E/F)}_F}\sigma'})_{\sigma}}\right)\\
    &=\gamma\left(\prod\limits_{\sigma' \in \Gamma_{E/F}} \mathfrak{f}^{f(E/F)}_F\sigma'(\varpi_E)^{b_{\sigma'}}_{(b_{\overline{\mathfrak{f}^{-f(E/F)}_F}\sigma})_{\sigma}}\right)=\prod\limits_{\sigma' \in \Gamma_{E/F}} \sigma'(\varpi_E)^{b_{\sigma'}}_{(b_{\sigma})_{\sigma}}.
\end{aligned}$$

With this action in hand, we are ready to define a descent datum for our category $RP_{E/F,s}$. Fix a section $s_{E} \colon \Gamma_{E/F} \to W_{L_{E}/F}$, which determines a 2-cocycle of $\Gamma_{E/F}$ valued in $\mathbb{Z}$, denoted by $c_{E}$. For a fixed $\gamma \in \Gamma_{E/F}$, we define the functor $\beta_{\gamma} \colon RP_{E/F,s} \to RP_{E/F,s}$ to send the triple $(V, \Phi, \mathcal{D})$ to the triple $(\beta_{\gamma}(V), \beta_{\gamma}(\Phi), \beta_{\gamma}(\mathcal{D}))$ such that

-   the underlying vector space $\beta_{\gamma}(V)$ is defined to be $V \otimes_{R_{E/F}} R_{E/F}$ where the map $R_{E/F} \to R_{E/F}$ is given by the action of $s_E(\gamma)$,

-   the endomorphism $\beta_{\gamma}(\Phi)$ is defined by $\Phi \otimes ( s_E(\gamma) \circ \Phi_R)$,

-   the grading $\beta_{\gamma}(\mathcal{D})$ on $\beta_{\gamma}(V)$ is such that $v_{(a_{\gamma \sigma}/s)_{\sigma})} \otimes r_{(b_{\sigma})_{\sigma}}$ is in the $((a_{\sigma} +sb_{\sigma})/s)_{\sigma}$ graded piece.

A morphism $f: (V, \Phi, \mathcal{D}) \to (V', \Phi', \mathcal{D}')$ is mapped by $\beta_{\gamma}$ to $\beta_{\gamma}(f) : = f \otimes \mathrm{id}$. This construction gives a $\gamma$-semilinear tensor equivalence from $RP_{E/F,s}$ to itself. For instance, for $e \in E$, we observe that $$\beta_{\gamma}(e)(v \otimes r) = ev \otimes r=v\otimes \gamma(e)r=\gamma(e)(v \otimes r).$$

To finish giving our descent datum, we need to provide an isomorphism of functors $\mu_{\gamma',\gamma} \colon \beta_{\gamma'\gamma} \to \beta_{\gamma'} \circ \beta_{\gamma}$ for all pairs $(\gamma',\gamma)$ which satisfies a cocycle condition (explained in more detail later). The morphism $\mu_{\gamma',\gamma}(X)$ will be defined for any object $(V, \Phi, \mathcal{D})=X \in RP_{E/F,s}$ by the map $$\mu_{\gamma', \gamma}(X): v \otimes r \mapsto \Phi^{-c_E(\gamma', \gamma)}(v) \otimes s_E(\gamma'\gamma')(r).$$

We check that this is a well-defined morphism in $RP_{E/F,s}$. First we note that for $v \in V$ and $r \in R_{E/F}$, we have $\mu_{\gamma', \gamma}(X)(v \otimes r)=\mu_{\gamma', \gamma}(rv \otimes 1)$. Indeed, $$\begin{aligned}
    \mu_{\gamma', \gamma}(X)(v \otimes r) & = \Phi^{-c_E(\gamma',\gamma)}(v) \otimes s_E(\gamma'\gamma)(r)  = \Phi^{-c_E(\gamma',\gamma)}(v) \otimes s_E(\gamma')s_E(\gamma) \Phi^{-c_E(\gamma', \gamma)}(r)\\
    & =  \Phi^{-c_E(\gamma', \gamma)}(rv) \otimes 1 =  \mu_{\gamma'\gamma}(X)(rv \otimes 1).
\end{aligned}$$

Now, evidently $\mu_{\gamma', \gamma}(X)$ is $\Phi$-equivariant and preserves gradings, so it remains to show $R_{E/F}$-linearity. For any $v \in V$ and $r \in R_{E/F}$, we compute that $$\mu_{\gamma', \gamma}(X)( v \otimes r) = \Phi^{-c_E(\gamma', \gamma)}(v) \otimes s_E(\gamma',\gamma)(r) = r\cdot \mu_{\gamma'\gamma}(v \otimes 1).$$

We claim that the family of isomorphisms of functors $\mu_{\gamma', \gamma}$ satisfies the "cocycle condition." Explicitly, for $\gamma'', \gamma', \gamma \in \Gamma_{E/F}$, we need to check that the following diagram commutes: $$\begin{tikzcd}
\beta_{\gamma''\gamma'\gamma}(V) \arrow["{(\mu_{{\gamma'',\gamma'\gamma}})_{V}}"]{rr} \arrow[swap, "{(\mu_{\gamma''\gamma',\gamma})_{V}}"]{dd} & & \beta_{\gamma''}(\beta_{\gamma'\gamma}(V)) \arrow["{\beta_{\gamma''}((\mu_{{\gamma',\gamma}})_{V})}"]{dd} \\
&&\\
\beta_{\gamma''\gamma'}(\beta_{\gamma}(V)) \arrow["{(\mu_{\gamma'',\gamma'})_{\beta_{\gamma}(V)}}"]{rr} && \beta_{\gamma''}(\beta_{\gamma'}(\beta_{\gamma}(V))).
\end{tikzcd}$$

We can write any element in the above spaces in the form $v \otimes 1$. Then we note that on elements of this form, the top arrow is given by $\Phi^{-c_{E}(\gamma'',\gamma'\gamma)}$, the right arrow by $\Phi^{-c_{E}(\gamma',\gamma)}$, the left by $\Phi^{-c_{E}(\gamma''\gamma', \gamma)}$, and the bottom by $\Phi^{-c_{E}(\gamma'',\gamma')}$. The desired commutativity then follows from the fact that $c_{E}$ is a $2$-cocycle (keeping in mind that the action of $\Gamma_{E/F}$ on $\mathbb{Z}= W_{L_{E}/E}$ is trivial).

With this setup in hand, we get a Tannakian category over $F$, denoted by $R\mathcal{W}_{E/F,s}$. Explicitly, the objects of $R\mathcal{W}_{E/F, s}$ are tuples $(X, f_{\gamma}: X \to \beta_{\gamma}(X))$ where $X$ is an object of $RP_{E/F, s}$ and $f_{\gamma}$ is a morphism such that $$\mu_{\gamma', \gamma}(X) \circ f_{\gamma'\gamma} = \beta_{\gamma'}(f_{\gamma}) \circ f_{\gamma'}.$$ Morphisms in $R\mathcal{W}_{E/F, s}$ are morphisms in $RP_{E/F,s}$ that commute with the $f_{\gamma}$ maps. The band of $R\mathcal{W}_{E/F, s}$ is an $F$-group scheme whose base-change to $E$ is $\prod_{\Gamma_{E/F}} \mu_{s}$. In fact, we have the following claim.

::: claim
The band of the gerbe associated to $R\mathcal{W}_{E/F,s}$ is $\mathrm{Res}_{E/F}(\mu_s)$.
:::

To make the verification of this claim easier, we note that we can define an analogous descent datum on the category $P_{E/F,s}$ defined in the identical way, except forgetting about any $R_{E/F}$-module structure (so for instance, $\beta_{\gamma}(V) = V \otimes_{L_E} L_E$ where the map $L_E \to L_E$ is the Galois action by $s_E(\gamma)$). This gives a Tannakian category $\mathcal{W}_{E/F,s}$ over $F$. Moreover, the quotient functor $q$ extends to a morphism $\tilde{q}$ of Tannakian categories with descent data; that is, for an object $(X, f_{\gamma})$ in $\mathcal{W}_{E/F,s}$, the object $(q(X), \tilde{q}(f_{\gamma}))$ lies in $R\mathcal{W}_{E/F,s}$. The map $\tilde{q}(f_{\gamma}): V \otimes R_{E/F} \to V \otimes R_{E/F} \otimes_{R_{E/F}} R_{E/F} =\beta_{\gamma}(V \otimes R_{E/F})$ is defined by $v \otimes r \mapsto f_{\gamma}(v) \otimes s_E(\gamma)^{-1}(r) \otimes 1$. This map is $R_{E/F}$-linear since for $r \in R_{E/F}$ and $v \in V$, we have $$v \otimes r \mapsto f_{\gamma}(v) \otimes s_E(\gamma)^{-1}(r) \otimes 1 = f_{\gamma}(v) \otimes 1 \otimes r = r \cdot q(f_{\gamma})(v \otimes 1).$$

This extension of $q$ is again a quotient functor, and the same argument as in §[\[sec:mod\]](#sec:mod){reference-type="ref" reference="sec:mod"} shows that the band of $R\mathcal{W}_{E/F,s}$ is given by the $s$-torsion subgroup-scheme of the $F$-group scheme giving the band of $\mathcal{W}_{E/F,s}$. It thus suffices to show that the latter band is the $F$-group scheme $\text{Res}_{E/F}(\mathbb{G}_{m})$.

Since we have identified the band of $P_{E/F,s}$ with the $F$-group scheme $\prod_{\Gamma_{E/F}} \mathbb{G}_{m}$ via the isomorphism of Tannakian categories over $E$ with the category $\text{Rep}_{E_{s}}(\mathcal{E}_{(c_{\sigma})_{\sigma}})$ constructed in §[\[sec:prod\]](#sec:prod){reference-type="ref" reference="sec:prod"}, we will work with this latter category. Conjugating the functors $\beta_{\gamma}$ with this ($E$-linear) identification gives a descent datum on $\text{Rep}_{E_{s}}(\mathcal{E}_{(c_{\sigma})_{\sigma}})$. For $\gamma \in \Gamma_{E/F}$, this is given by taking the representation $(V, \rho)$ to the representation $(V', \rho')$ where $V'=V \otimes_{E_s} E_s$ such that the map $E_s \to E_s$ is given by the action of $s_{E}(\gamma)$ restricted to $E_{s}$ and $V'_{(h_{\sigma})_{\sigma}} = V_{(h_{\gamma \sigma})_{\sigma}}$. We define $\rho'$ such that the element $((1),\mathfrak{f}_{E})$ acts by $\Phi \otimes \mathfrak{f}_E$ where the action on the right is the Galois action, and an element $(a_{\sigma})_{\sigma}$ of the torus acts on $V_{(h_{\sigma})}$ by the scalar $\prod_{\sigma \in \Gamma_{E/F}} a_{\sigma}^{h_{\gamma^{-1}\sigma}}$. With the descent functors $\beta'_{\gamma}$ on $\text{Rep}_{E_{s}}(\mathcal{E}_{(c_{\sigma})_{\sigma}})$ in hand, we are ready to compute the $\Gamma_{E/F}$-action giving the band the structure of an $F$-group scheme.

We know that the automorphisms of the canonical fiber functor $\omega$ are parametrized by $\prod_{\Gamma_{E/F}} \mathbb{G}_{m}(E_{s})$, where the tuple $(c_{\tau})$ acts on $V$ via scaling $V_{(h_{\sigma})}$ by $\prod\limits_{\tau \in \Gamma_{E/F}} c_{\tau}^{h_{\tau}}$. Starting with such an automorphism $\varphi$ and object $(V, \rho)$, we first apply $\beta_{\gamma^{-1}}$, obtaining $(V', \rho')$, and obtain an automorphism of $V'$ denoted $\varphi(\beta_{\gamma^{-1}}(V',\rho'))$. We then twist the $L_{E}$-action by $s(\gamma)^{-1}$, obtaining an automorphism $s(\gamma)^{-1}[\varphi(\beta_{\gamma^{-1}}(V',\rho'))]$ of the vector space $(V^{s(\gamma^{-1})^{-1}})^{s(\gamma)^{-1}}$, and then apply $\omega(\mu_{\gamma,\gamma^{-1}})$ to get an automorphism of $V = \omega((V,\rho))$, which we want to explicitly describe. The automorphism $\varphi(\beta_{\gamma^{-1}}(V',\rho'))$ scales $V_{(h_{\sigma})} = V'_{(h_{\gamma\sigma})}$ by $\prod_{\tau} c_{\tau}^{h_{\gamma \tau}}$ (using the twisted $L_{E}$-action), which means that $s(\gamma)^{-1}(\varphi(\beta_{\gamma^{-1}}(V',\rho')))$ scales $V_{(h_{\sigma})}$ by $s(\gamma) \cdot (\prod_{\tau} c_{\tau}^{h_{\gamma \tau}})$ (using the usual $L_{E}$-action), so that the new automorphism of our fiber functor is given by the tuple $(s(\gamma)\Phi^{c_{E}(\gamma,\gamma^{-1})}c_{\gamma^{-1}\tau})_{\tau}$. It follows that when $(c_{\tau})_{\tau} \in \prod_{\Gamma_{E/F}} \mathbb{G}_{m}(E)$, this action agrees with the usual $\Gamma_{E/F}$-action on $\text{Res}_{E/F}(\mathbb{G}_{m})(E)$. This implies that the $F$-group scheme structure of our band is given by $\text{Res}_{E/F}(\mathbb{G}_{m})$, as desired.

Finally, note that this identification of the bands of $\mathcal{W}_{E/F,s}$ and $R\mathcal{W}_{E/F,s}$ with these $F$-group schemes is compatible with our transition maps, in the sense that, at the level of bands, the functor $\iota_{s,s'}$ induces the $s'/s$-power map from $\text{Res}_{E/F}(\mathbb{G}_{m})$ to itself (and thus, the $s'/s$-power map from $\text{Res}_{E/F}(\mu_{s'})$ to $\text{Res}_{E/F}(\mu_{s})$). This fact follows from base-changing to $E$, where the analogous statement holds for the category $P_{E/F,s}$ (and thus for $RP_{E/F,s}$), as discussed in §[\[sec:prod\]](#sec:prod){reference-type="ref" reference="sec:prod"}). If $(X, f_{\gamma})$ is an object of $\mathcal{W}_{E/F,s}$, then $(\iota(X), \iota(f_{\gamma}))$ is an object of $\mathcal{W}_{E/F,s'}$, similarly for $R\mathcal{W}_{E/F,s}$, and we define $\mathcal{W}_{E/F}$ and $R\mathcal{W}_{E/F}$ to be their direct limits, whose bands have an explicit description via the above observation.
