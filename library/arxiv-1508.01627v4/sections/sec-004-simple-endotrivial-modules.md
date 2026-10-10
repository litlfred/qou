---
doc_id: arxiv-1508.01627v4
doc_title: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups"
section_id: sec-004-simple-endotrivial-modules
section_title: "Simple endotrivial modules"
section_number: 5
pages: 14-17
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.979
doc_brief: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups — 7 sections: Introduction; Maximal tori in classical groups; A Murnaghan–Nakayama rule"
---
[]{#sec:endotriv label="sec:endotriv"} In this section we prove Theorem 2 on the classification of simple endotrivial modules for finite classical groups. Note that the case of linear and unitary groups has already been treated in [@LM15], so we only need to consider symplectic groups and spin groups as in the previous section.

## On certain unipotent characters {#subsec:unip}

We first rule out some candidate characters. Let $\Phi_d\in{\mathbb{Z}}[x]$ denote the $d$th cyclotomic polynomial.

::: prop
[]{#prop:babbage label="prop:babbage"} Let $\chi$ be the unipotent character of $G = {\operatorname{SO}}_{6d-1}(q)$ or ${\operatorname{Sp}}_{6d-2}(q)$ (respectively of ${\operatorname{SO}}_{2(3d-1)}^+(q)$, ${\operatorname{SO}}_{6d}^-(q)$) parameterised by the symbol $$\binom{d\ 2d}{0}\quad \text{respectively }\ \binom{d\ 2d}{0\ 1},\
  \binom{d\ 2d}{},$$ with $d\ge3$ odd, or the unipotent character of ${\operatorname{SO}}_{6e}^+(q)$ parameterised by $$\binom{2e}{e}$$ for $d=2e$ even. Then $\chi(1)\not\equiv\pm1\pmod{|G|_\ell}$ for any prime $2<\ell$ with $d_\ell(q)=d$.
:::

::: proof
*Proof.* Since $\Phi_d(q)$ divides $|G|$ at least twice it is sufficient to show that $\chi(1)\not\equiv\pm1\pmod{\Phi_d(q)_\ell^2}$. We use a version of Babbage's congruence for quantum binomial coefficients $$\left[hd-1\atop d-1\right]_x
   \equiv x^{(h-1)\binom{d}{2}}\pmod{\Phi_d(x)^2}\quad\text{in }{\mathbb{Z}}[x]$$ for any $d,h\ge2$ (proved in [@LM15 Lemma 3.7]). If $\chi$ belongs to $\binom{d\ 2d}{0}$, we can express its degree using a quantum binomial coefficient evaluated at $q^2$, see [@Ca 13.8]: $$\chi(1) = \frac{(q^2-1)\cdots(q^{6d-2}-1)(q^{2d}-q^d)(q^{2d}+1)(q^d+1)}
  {2(q^2-1)\cdots(q^{4d}-1)(q^2-1)\cdots(q^{2d}-1)}
  =\frac{1}{2}\left[3d-1\atop d-1\right]_{q^2}q^d(q^{2d}+1).$$ Substituting $x = q^2$ in the Babbage congruence we get a congruence over the integers modulo $\Phi_d(q^2)^2$. Since $\Phi_d(x^2) =
\Phi_d(x)\Phi_d(-x)$ we also get a congruence modulo $\Phi_d(q)^2$: $$\chi(1) \equiv \frac{1}{2} q^{2d(d-1)+d}(q^{2d}+1) \pmod{\Phi_d(q)^2}.$$ It suffices to show that $2\chi(1) \not\equiv \pm 2\pmod{\Phi_d(q)_\ell^2}$. Since $\Phi_d(q) \mid (q^d-1)$ we get $$\begin{array}{rcl}
  2\chi(1) &\equiv& q^{2d(d-1)+d} \cdot 2 q^d
   = 2 (q^{2d})^d \equiv 2(q^{2d}-(q^d-1)^2)^d = 2(2(q^d-1)+1)^d \\
  &\equiv& 2 (2d(q^d-1)+1) \pmod{\Phi_d(q)^2}.
\end{array}$$ Since $\ell \neq 2$, $d < \ell$ and $\ell \mid (q^d-1)$ we conclude that $2\chi(1) + 2$ is not divisible by $\ell$ and that the highest power of $\ell$ dividing $2\chi(1)-2$ is $(q^d-1)_\ell = \Phi_d(q)_\ell$.

Now we turn to the unipotent character with symbol $\binom{d\ 2d}{0\ 1}$. Its degree differs from the previously considered $\chi(1)$ by the factor $$\frac{(q^{2d}+q)(q^{d-1}+1)}{(q^{3d-1}+1)(q+1)}
  =\frac{q^{3d-1}+3q^d+q-1+(q^d-1)^2}{q^{3d-1}+3q^d+q-1+(q^d+2)(q^d-1)^2}.$$ We argue that both degrees are equal modulo $\Phi_d(q)_\ell^2$.

For this, note that for integers $a,b,c,m$ with $a b/c \in {\mathbb{Z}}$, $b \equiv c
\pmod{m}$ and $(c,m) = 1$ there is an integer $\tilde{c}$ with $c\tilde{c}
\equiv b \tilde{c}
\equiv 1 \pmod{m}$ and so $a b/c \equiv ab/c\cdot c\tilde{c} \equiv a b
\tilde{c} \equiv a \pmod{m}$. This applies here because $(q^{3d-1}+1)(q+1)$ is not divisible by $\ell$ (since $d\geq 3$ is the order of $q$ modulo $\ell$ and $(q^{3d-1}+1)(q+1) (q^{3d-1}-1)(q-1) = (q^{6d-2}-1)(q^2-1)$ is not divisible by $\ell$).

The same argument works for the degree of the unipotent character with symbol $\binom{d\ 2d}{}$. Its degree differs from the previous $\chi(1)$ by the factor $$\frac{2(q^{2d}-q^d+1)}{q^{2d}+1}
  = \frac{2q^d +2(q^d-1)^2}{2q^d+(q^d-1)^2}$$ and $q^{2d}+1$ is not divisible by $\ell$.

Finally we consider for even $d=2e$ the unipotent character $\psi$ with symbol $\binom{2e}{e}$. Its degree is $$\psi(1) = \left[3e-1\atop e-1\right]_{q^2} (q^{2e}+q^e+1)q^e.$$ Evaluating Babbage's congruence at $q^2$ yields a congruence modulo $\Phi_e(q^2)^2$. But note that for odd $e$ we have $\Phi_e(x^2) = \Phi_e(x)
\Phi_e(-x)$ and $\Phi_e(-x) = \Phi_d(x)$, and for even $e$ we have $\Phi_e(x^2) = \Phi_d(x)$. So, we also get congruences modulo $\Phi_d(q)^2$. Using now $\Phi_d(q) \mid (q^e+1)$ we find with similar arguments as before that $\psi(1) \equiv -q^{2e^2} \pmod{\Phi_d(q)^2}$ and that $\psi(1)-1$ is not divisible by $\ell$, and that $\psi(1)+1$ is divisible by $\Phi_d(q)_\ell$ but no higher power of $\ell$. ◻
:::

In order to deal with certain unipotent characters, we recall some results of James and Mathas [@JM00] on reducibility of characters of Hecke algebras. Let ${\mathcal{H}}_n={\mathcal{H}}_n(q,Q)$ be the Iwahori--Hecke algebra of type $B_n$ with parameters $q$ and $Q$ over ${\mathbb{Z}}[q^{\pm1},Q^{\pm1}]$. Its irreducible characters are in natural bijection with those of the Weyl group $W(B_n)$ via the specialisation $q\mapsto1,Q\mapsto1$, and hence labelled by pairs of partitions $(\la,\mu)$ of $n$. We write $\chi_{\la,\mu}$ for the character of ${\mathcal{H}}_n$ labelled by $(\la,\mu)$. We consider certain specialisations of ${\mathcal{H}}_n$.

::: prop
[]{#prop:HeckeB label="prop:HeckeB"} Let $\ell$ be a prime and $q$ a prime power. Set $d=d_\ell(q)$.

1.  If $d$ is odd, $n=2d+r$ with $0\le r\le d-2$, and $(\la,\mu)=((d+r,r+1,1^{d-r-1}),-)$, then the character $\chi_{\la,\mu}$ of ${\mathcal{H}}_n(q,q)$ is reducible modulo $\ell$.

2.  If $d=2e>2$ is even, $n=2e+r$ with $0\le r\le e-1$, and $(\la,\mu)=((r),(e+r+1,1^{e-r-1}))$, then the character $\chi_{\la,\mu}$ of ${\mathcal{H}}_n(q,q)$ is reducible modulo $\ell$.
:::

::: proof
*Proof.* Let $\zeta_d$ denote a primitive complex $d$th root of unity. The reduction modulo $\ell$ of ${\mathcal{H}}_n(q,q)$ factors through the specialisation to ${\mathcal{H}}_n(\zeta_d,\zeta_d)$, thus a character which becomes reducible under the latter specialisation will a fortiori be reducible modulo $\ell$. James and Mathas [@JM00 Thms. 4.7(i) and 4.10] give a sufficient criterion for $\chi_{\la,\mu}$ to become reducible under the specialisation to ${\mathcal{H}}_n(\zeta_d,\zeta_d)$, if $(\la,\mu)$ is a Kleshchev bipartition. In case (a), $\chi_{\la,\mu}$ is reducible modulo $\Phi_d$ by [@JM00 Thm. 4.10(i)] since the character of the Hecke algebra of ${\mathfrak{S}}_n$ labelled by $\la=(d+r,r+1,1^{d-r-1})$ is reducible modulo $\Phi_d$, as the first column hook lengths are different.

In (b), $(\la,\mu)$ is Kleshchev, and for $r>0$ the last box of the Young diagram of $\la$ can be moved to the end of the first column of $\mu$ without changing its residue, so $\chi_{\la,\mu}$ is reducible by [@JM00 Thm. 4.10(ii)]. For $r=0$ the character $\chi_{\la,\mu}$ is reducible modulo $\Phi_{2e}$ by [@JM00 Thm. 4.10(i)] since the character of the Hecke algebra of ${\mathfrak{S}}_n$ labelled by the second part $\mu=(e+1,1^{e-1})$ is. ◻
:::

The next reducibility result for characters of specialisations of the Hecke algebra of type $B_n$ will be used in the investigation of unipotent characters of ${\operatorname{Spin}}_{2n}^\pm(q)$.

::: prop
[]{#prop:HeckeD label="prop:HeckeD"} Let $\ell$ be a prime and $q$ a prime power. Set $d=d_\ell(q)$.

1.  If $d$ is odd, $n=2d+r$ with $0\le r\le d-2$, and $(\la,\mu)=((d+r,r+1,1^{d-r-1}),-)$, then the character $\chi_{\la,\mu}$, of ${\mathcal{H}}_n(q,1)$ is reducible modulo $\ell$.

2.  If $d=2e>2$ is even, $n=2e+r$ with $0\le r\le e-1$, and $(\la,\mu)=((e+r,1^{e-r}),(r))$, then the character $\chi_{\la,\mu}$ of ${\mathcal{H}}_n(q,1)$ is reducible modulo $\ell$.

3.  If $d$ is odd, $n=2d+r$ with $1\le r\le d-1$, and $(\la,\mu)=(d+r-1,r,1^{d-r}),-$, then the character $\chi_{\la,\mu}$ of ${\mathcal{H}}_{n-1}(q,q^2)$ is reducible modulo $\ell$.

4.  If $d=2e>2$ is even, $n=2e+r$ with $1\le r\le e-1$, and $(\la,\mu)=((r-1),(e+r+1,1^{e-r-1}))$, then the character $\chi_{\la,\mu}$ of ${\mathcal{H}}_{n-1}(q,q^2)$ is reducible modulo $\ell$ unless $(e,r)=(2,1)$.
:::

::: proof
*Proof.* Parts (a) and (c) again follow from [@JM00 Thm. 4.10(i)] as the first column hook lengths of $\la$ are different. The characters $\chi_{\la,\mu}$ as in (b) and (d) are reducible since the first, respectively second part of $\la$ is a hook partition, of length $d=2e$, hence belonging to a reducible character of the Hecke algebra of type ${\mathfrak{S}}_{2e}$, unless this hook is either $(2e)$ or $(1^{2e})$. The latter case only occurs in (d) when $(e,r)=(2,1)$. ◻
:::

## Simple endotrivial modules in classical type groups {#subsec:endoclass}

We will use the fact shown in [@LMS13 Thm. 1.3] that any endotrivial module is liftable to a characteristic 0 representation. Therefore, we can investigate endotrivial modules by the ordinary character of their lift. These characters have the following properties:

- they are irreducible modulo $\ell$,

- their values on $\ell$-singular classes are of absolute value $1$,

- their degree is congruent to $\pm 1$ modulo $|G|_\ell$.

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
