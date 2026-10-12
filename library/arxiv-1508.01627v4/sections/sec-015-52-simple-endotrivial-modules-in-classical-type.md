---
doc_id: arxiv-1508.01627v4
doc_title: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS "
section_id: sec-015-52-simple-endotrivial-modules-in-classical-type
section_title: "Simple endotrivial modules in classical type groups"
section_number: 5.2
pages: 16-17
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.984
---
[]{#subsec:endoclass label="subsec:endoclass"}

We will use the fact shown in [@LMS13 Thm. 1.3] that any endotrivial module is liftable to a characteristic 0 representation. Therefore, we can investigate endotrivial modules by the ordinary character of their lift. These characters have the following properties:

-   they are irreducible modulo $\ell$,

-   their values on $\ell$-singular classes are of absolute value $1$,

-   their degree is congruent to $\pm 1$ modulo $|G|_\ell$.

Theorem 2 is now a consequence of:

::: thm
[]{#thm:BC label="thm:BC"} Let $G={\operatorname{Sp}}_{2n}(q)$ or $G={\operatorname{Spin}}_{2n+1}(q)$ with $n\ge2$, $(n,q)\ne(2,2)$, or $G={\operatorname{Spin}}_{2n}^\pm(q)$ with $n\ge4$, and $\ell$ a prime for which Sylow $\ell$-subgroups of $G$ are non-cyclic. Let $\rho$ be the character of a nontrivial simple endotrivial $kS$-module, for a central factor group $S$ of $G$. Then we have $G=S={\operatorname{Sp}}_8(2)\cong{\operatorname{O}}_9(2)$, $\ell=5$, and $\rho=\rho_{\mathcal{S}}$, with ${\mathcal{S}}=\binom{0\ 1}{4}$, is the unipotent character of degree $\rho_{\mathcal{S}}(1)=51$.
:::

::: proof
*Proof.* By [@LMS13 Thms. 6.7 and 5.2] there do not exist non-trivial simple endotrivial $kS$-modules if either $\ell=2$ or $\ell$ divides $q$. Now let $d=d_\ell(q)$. Since Sylow $\ell$-subgroups of $G$ are non-cyclic, the cyclotomic polynomial $\Phi_d(q)$ has to divide the group order at least twice. By Theorem [\[thm:non-unip\]](#thm:non-unip){reference-type="ref" reference="thm:non-unip"}, all non-unipotent characters of $G$ vanish on some $\ell$-singular element of $G$, so cannot come from simple endotrivial modules. The only candidates for endotrivial unipotent characters are those appearing in the conclusion of Theorem [\[thm:unip\]](#thm:unip){reference-type="ref" reference="thm:unip"}. Of those, we can discard the Steinberg character of $G$, because $G$ contains $\ell$-singular elements with non-trivial unipotent part, and on those classes the value of the Steinberg character is zero.

Now consider the other unipotent characters listed in Theorem [\[thm:unip\]](#thm:unip){reference-type="ref" reference="thm:unip"}. First assume that $G={\operatorname{Sp}}_{2n}(q)$ or $G={\operatorname{Spin}}_{2n+1}(q)$. Let $\rho=\rho_{\mathcal{S}}$ with ${\mathcal{S}}$ as in Theorem [\[thm:unip\]](#thm:unip){reference-type="ref" reference="thm:unip"}(1). So $d$ is odd and $n=2d+r$, $0\le r\le d-1$. Then $\rho$ lies in the principal series and is parameterised by the character of the Weyl group $W(B_n)$ labelled by the pair of partitions $((d+r,r+1,1^{d-r-1}),-)\vdash 2d+r$. By Proposition [\[prop:HeckeB\]](#prop:HeckeB){reference-type="ref" reference="prop:HeckeB"}(a), the corresponding character of the Hecke algebra ${\mathcal{H}}_n$ of type $B_n$ is reducible modulo $\ell$ for $r\ne d-1$. Since the decomposition matrix of the Hecke algebra of $W(B_n)$ embeds into that of $G$ (see e.g. [@GJ11 Thm. 4.1.14]), this shows that $\rho_{\mathcal{S}}$ is reducible modulo $\ell$, so does not give an example. The same argument applies to the Alvis--Curtis dual characters, since Alvis--Curtis duality on the side of Hecke algebras corresponds to tensoring with the sign character. In the case $r=d-1$ we have ${\mathcal{S}}=\binom{d\ 2d}{0}$ and the corresponding unipotent character does not satisfy the necessary degree congruence by Proposition [\[prop:babbage\]](#prop:babbage){reference-type="ref" reference="prop:babbage"}.

So now assume that $d=2e$ is even and write $n=2e+r$ with $0\le r\le e-1$. Let $\rho=\rho_{\mathcal{S}}$ as in Theorem [\[thm:unip\]](#thm:unip){reference-type="ref" reference="thm:unip"}(2). Again, $\rho$ lies in the principal series and is labelled by the pair of partitions $((r+1),(e+r,1^{e-r-1}))\vdash 2e+r$. Hence it is reducible modulo $\ell$ by Proposition [\[prop:HeckeB\]](#prop:HeckeB){reference-type="ref" reference="prop:HeckeB"}(b) if $e>1$. For $e=1$ we have $r=0$, $n=2$ and ${\mathcal{S}}=\binom{0\ 1}{2}$. Here $\rho_{\mathcal{S}}(1)=q(q^2+1)/2\equiv 2q+1\pmod{(q+1)^2}$ is not congruent to $\pm1$ modulo the $\ell$-part of the group order.

For $G={\operatorname{Sp}}_{2n}(q)$ or $G={\operatorname{Spin}}_{2n+1}(q)$ it remains to consider the unipotent characters listed in Theorem [\[thm:unip\]](#thm:unip){reference-type="ref" reference="thm:unip"}(8) and (9). (Note that the group ${\operatorname{Sp}}_4(2)$ was excluded.) In case (8) we have $q=d=2$, so $\ell=3$. The listed symbol parameterises a unipotent character of degree 7, its Alvis-Curtis dual has degree 56, both incongruent $\pm1\pmod{3^3}$. Finally in case (9), $\ell|(q^2+1)=5$. The second symbol belongs to a character of degree 119, its Alvis--Curtis dual has degree 30464, both incongruent to $\pm1\pmod{5^2}$, so this gives no example. But the 51-dimensional simple unipotent module for ${\operatorname{Sp}}_8(2)$ labelled by $\binom{0\ 1}{4}$ is irreducible and endotrivial in characteristic $\ell=5$. Indeed, the restriction of the corresponding irreducible character to the subgroup ${\operatorname{O}}_8^+(2)$ contains the trivial character once and all other constituents are of 5-defect zero, hence projective modulo 5. Its Alvis--Curtis dual has degree $13056\equiv6\pmod{5^2}$, so cannot lead to an example.

Next consider the case that $G={\operatorname{Spin}}_{2n}^+(q)$. Let $\rho=\rho_{\mathcal{S}}$ be unipotent with ${\mathcal{S}}$ as in Theorem [\[thm:unip\]](#thm:unip){reference-type="ref" reference="thm:unip"}(3). So $d$ is odd and $n=2d+r$ with $0\le r\le d-1$. Then $\rho$ lies in the principal series and is parameterised by the character of the Weyl group $W(D_n)$ labelled by the pair of partitions $(\la,\mu)=((d+r,r+1,1^{d-r-1}),-)\vdash 2d+r$. By Proposition [\[prop:HeckeD\]](#prop:HeckeD){reference-type="ref" reference="prop:HeckeD"}(a), the corresponding character $\chi_{\la,\mu}$ of the Hecke algebra ${\mathcal{H}}_n$ of type $B_n$ is reducible modulo $\ell$ for $r\ne d-1$. Since $\la\ne\mu$, $\chi_{\la,\mu}$ restricts irreducibly to the Hecke algebra ${\mathcal{H}}_n'$ of type $D_n$ (of index 2) and thus is also reducible as a character of ${\mathcal{H}}_n'$ modulo $\ell$. Using that the decomposition matrix of the Hecke algebra of $W(D_n)$ embeds into that of $G$, this shows that $\rho_{\mathcal{S}}$ is reducible modulo $\ell$, so does not give an example. The same argument applies to the Alvis--Curtis dual characters. In the remaining case $r=d-1$, Proposition [\[prop:babbage\]](#prop:babbage){reference-type="ref" reference="prop:babbage"} shows that the corresponding unipotent character does not satisfy the degree congruence.

Now assume that $\rho_{\mathcal{S}}$ is as in Theorem [\[thm:unip\]](#thm:unip){reference-type="ref" reference="thm:unip"}(4), so $d=2e$ is even and $n=2e+r$ with $0\le r\le e$. Again, $\rho$ lies in the principal series and is labelled by the pair of partitions $((e+r,1^{e-r}),(r))\vdash 2e+r$. By Proposition [\[prop:HeckeD\]](#prop:HeckeD){reference-type="ref" reference="prop:HeckeD"}(b) the corresponding character of the Hecke algebra of type $B_n$ is reducible modulo $\ell$ if $r<e$ and $e>1$, and so as before the same holds for the character of the Hecke subalgebra of type $D_n$, whence $\rho_{\mathcal{S}}$ is reducible modulo $\ell$ for $e>1$. Note that $e=1$ is excluded since then $n=2e=2$. The case when $r=e$ does not satisfy the degree congruence by Proposition [\[prop:babbage\]](#prop:babbage){reference-type="ref" reference="prop:babbage"}.

Similarly, in the case that $G={\operatorname{Spin}}_{2n}^-(q)$ the characters of the principal series Hecke algebra ${\mathcal{H}}_{n-1}(q,q^2)$ labelled by $(\la,\mu)$ as in Theorem [\[thm:unip\]](#thm:unip){reference-type="ref" reference="thm:unip"}(5) and (6) are reducible modulo $\ell$ by Proposition [\[prop:HeckeD\]](#prop:HeckeD){reference-type="ref" reference="prop:HeckeD"}(c) and (d), so the same holds for the unipotent characters parameterised by these pairs, unless $r=d$. The latter character again does not belong to an endotrivial module by Proposition [\[prop:babbage\]](#prop:babbage){reference-type="ref" reference="prop:babbage"}. In the exceptional case $(e,r)=(2,1)$ of Proposition [\[prop:HeckeD\]](#prop:HeckeD){reference-type="ref" reference="prop:HeckeD"}(d) we have $n=2e+r=5$ and $\rho_{\mathcal{S}}(1)+1\equiv 4(q^2+1)\pmod{(q^2+1)^2}$, hence the necessary degree congruence is not satisfied for $\rho_{\mathcal{S}}$.

Finally, the character listed in Theorem [\[thm:unip\]](#thm:unip){reference-type="ref" reference="thm:unip"}(10) takes value 2 on some $\ell$-singular classes, by the final statement in that result, so again cannot be endotrivial. ◻
:::

The endotrivial characters of ${\operatorname{Sp}}_4(2)\cong{\mathfrak{S}}_6$ and its covers have been described in [@LMS13 Thm. 4.9].

As pointed out before the simple endotrivial modules of linear and unitary groups have already been determined in [@LM15 Thm. 3.10 and 4.5].
