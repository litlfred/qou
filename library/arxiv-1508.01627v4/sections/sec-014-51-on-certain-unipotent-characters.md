---
doc_id: arxiv-1508.01627v4
doc_title: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS "
section_id: sec-014-51-on-certain-unipotent-characters
section_title: "On certain unipotent characters"
section_number: 5.1
pages: 14-16
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.958
doc_brief: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS IN CLASSICAL GROUPS"
---
[]{#subsec:unip label="subsec:unip"}

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
