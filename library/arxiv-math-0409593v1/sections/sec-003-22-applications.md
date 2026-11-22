---
doc_id: arxiv-math-0409593v1
doc_title: "Categorification of sl_2 and braid groups"
section_id: sec-003-22-applications
section_title: "Applications"
section_number: 2.2
pages: 4-6
source_pdf: 0409593v1.pdf
source_sha256: ad965f5c80838824
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.989
doc_brief: "Categorification of sl_2 and braid groups — 20 sections: Front matter; Introduction; Self-equivalences"
---
###  {#P1}

We consider schemes of finite type type over an algebraic closure of a finite field ${\mathbf{F}}_q$ (the case of complex algebraic varieties is similar). Let $\pi:X\to Y$ be a smooth projective morphism already defined over ${\mathbf{F}}_q$. Assume the geometric fibers are projective lines.

Let $\Lambda$ be a field of coefficients (=an extension of ${\mathbf{Q}}_\ell$ for $\ell\!\not|\ q$ a prime number). Put ${\mathcal{C}}=D^b(Y)$ and ${\mathcal{D}}=D^b(X)$ (bounded derived categories of constructible sheaves of $\Lambda$-vector spaces). Take $F=\pi^*$, $G=R\pi_*$ and $\Phi=?(1)[2]$. We have a canonical isomorphism (projection formula) $?\otimes R\pi_*\Lambda_X\buildrel \sim\over\to R\pi_*\pi^*$. Via this isomorphism, $\eta'$ becomes $\operatorname{id}\nolimits\otimes\eta'(\Lambda_Y)$ and $\varepsilon$ becomes $\operatorname{id}\nolimits\otimes t$, where $t:R\pi_*\Lambda_X\to
\Lambda_Y(-1)[-2]$ is the trace map (an isomorphism on ${\mathcal{H}}^2$).

So, the triangle ([\[GF\]](#GF){reference-type="ref" reference="GF"}) is obtained from the triangle $\Lambda_Y\xrightarrow{\eta'(\Lambda_Y)}R\pi_*\Lambda_X
\xrightarrow{t}\Lambda_Y(-1)[-2]\rightsquigarrow$ by applying $?\otimes$. This is indeed a distinguished triangle, for it is so at geometric fibers.

Let ${\mathcal{L}}$ be a relative ample sheaf for $\pi$ and $c\in H^2(X,\Lambda(1))$ be its first Chern class. The hard Lefschetz Theorem states that the composition $\Lambda_Y\xrightarrow{\eta'(\Lambda_Y)}R\pi_*\Lambda_X\xrightarrow{c}
R\pi_*\Lambda_X(1)[2]\xrightarrow{t(1)[2]}\Lambda_Y$ is an isomorphism. It follows that the connecting map in the triangle above is zero.

Thus, we are in the setting of §[\[constrequiv\]](#constrequiv){reference-type="ref" reference="constrequiv"} and we get a self-equivalence of $D^b(X)$.

This can be also constructed as a kernel transform. Let $\alpha,\beta:X\times_YX\to X$ be the first and second projections. Let $i:\Delta X\to X\times_Y X$ be the closed immersion of the diagonal and $j:Z\to X\times_Y X$ be the open immersion of the complement of $\Delta X$. Denote by ${\tilde{\varepsilon}}:1_{D^b(X\times_Y X)}\to i_*i^*$ and ${\tilde{\eta}}:Rj_!j^*\to 1_{D^b(X\times_Y X)}$ the adjunction morphisms. One checks easily that there is a commutative diagram where the rows are distinguished triangles $$\xymatrix{
\Upsilon\ar[r] & \pi^*R\pi_*\ar[r]^-{\varepsilon'}\ar[d]^\sim & 
 1_{{\mathcal{D}}}\ar[d]^\sim \ar@{~>}[r] & \\
R\beta_*Rj_!j^*\alpha^*\ar[r]_-{R\beta_*{\tilde{\eta}}\alpha^*} &
 R\beta_*\alpha^*\ar[r]_-{R\beta_*{\tilde{\varepsilon}}\alpha^*}&
 R\beta_*i_*i^*\alpha^*\ar@{~>}[r] & 
}$$ where the middle vertical map is the base change isomorphism.

Denote by $p,q:Z\to X$ the first and second projections. Then, $\Upsilon\simeq Rp_!q^*$ and $\Upsilon'\simeq Rp_*q^!$.

###  {#section}

Assume we are in the setting of §[\[constrequiv\]](#constrequiv){reference-type="ref" reference="constrequiv"} with ${\mathcal{C}}=D^b(k\operatorname{\!-mod}\nolimits)$ where $k$ is a field and the categories and functors involved are $k$-linear. There is an integer $n$ such that $\Phi=?[n]$. Let $E=F(k)$. Then, $F\simeq E\otimes_k ?$ and $G\simeq R\operatorname{Hom}\nolimits(E,?)$. The morphism $\varepsilon$ comes from $t:\operatorname{Hom}\nolimits(E,E[n])\to k$.

The morphism $\varepsilon$ is the counit of an adjoint pair $(G,F\Phi)$ if and only if $\dim_k\bigoplus_i\operatorname{Hom}\nolimits(E,M[i])<\infty$ for all $M\in{\mathcal{D}}$ and $\operatorname{Hom}\nolimits(E,M)\times\operatorname{Hom}\nolimits(M,E[n])\to k,\ (f,g)\mapsto t(gf)$ is a perfect pairing for all $M\in{\mathcal{D}}$.

The triangle ([\[GF\]](#GF){reference-type="ref" reference="GF"}) is distinguished if and only if $0\to k\cdot \operatorname{id}\nolimits\to \bigoplus_i \operatorname{Hom}\nolimits(E,E[i]) \xrightarrow{t} k\to 0$ is an exact sequence.

In other words, $E$ is an $n$-spherical object and $\Upsilon$, $\Upsilon'$ are the corresponding twist functors of Seidel and Thomas [@SeiTho §2b]. So, the framework above corresponds exactly to the twist functor theory when ${\mathcal{C}}\simeq D^b(k\operatorname{\!-mod}\nolimits)$.

::: rem
The case ${\mathcal{C}}=D^b(k^d\operatorname{\!-mod}\nolimits)$ also leads to interesting examples.
:::

::: rem
It would be interesting to see if the construction of §[\[constrequiv\]](#constrequiv){reference-type="ref" reference="constrequiv"} can be used to construct automorphisms of derived categories of Calabi-Yau varieties corresponding, via Kontsevich's homological mirror symmetry conjecture, to graded symplectic automorphisms on the mirror associated to Lagrangian submanifolds more complicated than spheres.
:::

###  {#invRi}

Let us consider here two abelian categories ${\mathcal{A}}$ and ${\mathcal{B}}$ and ${\tilde{F}}:{\mathcal{A}}\to{\mathcal{B}}$, ${\tilde{G}}:{\mathcal{B}}\to{\mathcal{A}}$ and ${\tilde{\Phi}}$ a self-equivalence of ${\mathcal{A}}$. We assume we have two adjoint pairs $({\tilde{F}},{\tilde{G}})$ and $({\tilde{G}},{\tilde{F}}{\tilde{\Phi}})$. So, we have four morphisms (units and counits of the two adjunctions) $${\tilde{\eta}}:1_{\mathcal{B}}\to {\tilde{F}}{\tilde{\Phi}}{\tilde{G}},\ \ \ {\tilde{\varepsilon}}:{\tilde{G}}{\tilde{F}}{\tilde{\Phi}}\to 1_{\mathcal{A}}$$ $${\tilde{\eta}}':1_{\mathcal{A}}\to {\tilde{G}}{\tilde{F}},\ \ \ {\tilde{\varepsilon}}':{\tilde{F}}{\tilde{G}}\to 1_{\mathcal{B}}.$$

Let ${\tilde{\Upsilon}}$ be the complex $0\to {\tilde{F}}{\tilde{G}}\buildrel {\tilde{\varepsilon}}'\over \longrightarrow 1_{\mathcal{B}}\to 0$ and ${\tilde{\Upsilon}}'$ the complex $0\to 1_{\mathcal{B}}\buildrel {\tilde{\eta}}\over \longrightarrow {\tilde{F}}{\tilde{\Phi}}{\tilde{G}}\to 0$ (with ${\tilde{F}}{\tilde{G}}$ and ${\tilde{F}}{\tilde{\Phi}}{\tilde{G}}$ in degree $0$). We put ${\mathcal{C}}=K({\mathcal{A}})$ and ${\mathcal{D}}=K({\mathcal{B}})$ and we denote by $F$, $G$, etc\... the extensions of ${\tilde{F}}$, ${\tilde{G}}$, etc\... to ${\mathcal{C}}$ and ${\mathcal{D}}$.

Assume ${\mathcal{B}}$ is artinian and noetherian (every object is a finite extension of simple objects). If we have the equality $[{\tilde{G}}{\tilde{F}}]=[\operatorname{id}\nolimits]+[{\tilde{\Phi}}^{-1}]$ as endomorphisms of $K_0({\mathcal{A}})$ (or more generally, if $[{\tilde{F}}{\tilde{\Phi}}{\tilde{G}}{\tilde{F}}{\tilde{G}}]=[{\tilde{F}}{\tilde{G}}{\tilde{F}}{\tilde{\Phi}}{\tilde{G}}]=[{\tilde{F}}{\tilde{G}}]+[{\tilde{F}}{\tilde{\Phi}}{\tilde{G}}]$ in $\operatorname{End}\nolimits(K_0({\mathcal{B}}))$), then, the conclusion of Proposition [\[inversibilitetriang\]](#inversibilitetriang){reference-type="ref" reference="inversibilitetriang"} remains valid.

Let us justify this, following ideas of Rickard [@Ri §3]. There is an adjoint pair $(\Upsilon',\Upsilon)$, hence there is a map $u:\operatorname{id}\nolimits\to \Upsilon\Upsilon'$ that doesn't vanish on a non-zero object of ${\mathcal{B}}$. One shows that $\Upsilon\Upsilon'$ is homotopy equivalent to a complex of functors with only one non-zero term, $R$, in degree $0$ and $R$ is an exact functor. The assumption on classes shows that $[R]=[\operatorname{id}\nolimits]$. So, $R$ sends a simple object to itself, for a simple object is characterized amongst objects of ${\mathcal{B}}$ by its class in $K_0({\mathcal{B}})$. In particular, $u:\operatorname{id}\nolimits\to R$ is an isomorphism on simple objects. So, $u$ is an isomorphism.
