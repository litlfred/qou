---
doc_id: arxiv-math-0409593v1
doc_title: "Categorification of sl_2 and braid groups"
section_id: sec-017-62-kernel-transforms
section_title: "Kernel transforms"
section_number: 6.2
pages: 16-21
source_pdf: 0409593v1.pdf
source_sha256: ad965f5c80838824
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.642
doc_brief: "Categorification of sl_2 and braid groups — 20 sections: Front matter; Introduction; Self-equivalences"
---
[]{#noyaux label="noyaux"}

### 

Let us define a $2$-category ${\mathcal{K}}$.

-   The $0$-arrows are the varieties.

-   $1$-arrows : $\operatorname{Hom}\nolimits(X,Y)$ is the family of $(K,U)$ where $U$ is a variety over $Y\times X$ and $K\in D^b(U)$.

-   $2$-arrows : $\operatorname{Hom}\nolimits((K,U),(K',U'))$ is the set of $(\phi,f)$ where $f:U\buildrel \sim\over\to U'$ is an isomorphism of $(Y\times X)$-varieties and $\phi:K\buildrel \sim\over\to f^*K'$.

We define the composition of $1$-arrows. Consider the following diagram where the square is cartesian $$\label{diag3}
\xymatrix{
& & V\times_Y U \ar[dl]_{\beta}\ar[dr]^{\alpha}\\
& V \ar[dl]_{p_4}\ar[dr]^{p_3} & & U \ar[dl]_{p_2} \ar[dr]^{p_1}\\
Z & & Y & & X
}$$ Let $K\in D^b(U)$ and $L\in D^b(V)$. We put $L\boxtimes K=\beta^*L\otimes \alpha^*K$. The composition $(L,V)(K,U)$ is defined to be $(L\boxtimes K,V\times_Y U)$.

Let us consider now the diagram with all squares cartesian $$\xymatrix{
& & & W\times_Z V\times_Y U \ar[dl]_{b}\ar[dr]^{a} \\
& & W\times_Z V \ar[dl]_{\delta}\ar[dr]^{\gamma} & &
    V\times_Y U \ar[dl]_{\beta}\ar[dr]^{\alpha}\\
& W \ar[dl]_{p_6}\ar[dr]^{p_5} & & V \ar[dl]_{p_4}\ar[dr]^{p_3} & &
   U \ar[dl]_{p_2} \ar[dr]^{p_1}\\
T & & Z & & Y & & X
}$$ and take $M\in D^b(W)$. We have $$(M\boxtimes L)\boxtimes K=b^*(\delta^*M\otimes\gamma^*L)\otimes
(\alpha a)^*K\buildrel \sim\over\to(\delta b)^* M\otimes a^*(\beta^*L\otimes \alpha^*K)=
M\boxtimes (L\boxtimes K).$$ This provides the associativity isomorphisms for ${\mathcal{K}}$. With our conventions, we will write $M\boxtimes L\boxtimes K$ for the objects in the isomorphism above. It is straightforward to check that ${\mathcal{K}}$ is indeed a $2$-category.

### 

We put $\Phi_K=\Phi_K^{p_2,p_1}={p_2}_!(K\otimes p_1^* -): D^b(X)\to D^b(Y).$

Let $c_{L,K}:\Phi_L\Phi_K\buildrel \sim\over\to\Phi_{L\boxtimes K}$ be defined as the composition

$$\begin{aligned}
{p_4}_!(L\otimes p_3^* {p_2}_!(K\otimes p_1^* -)) &\to 
{p_4}_!(L\otimes \beta_!\alpha^*(K\otimes p_1^* -))\\
& \to
{p_4}_!\beta_!(\beta^*L\otimes \alpha^*(K\otimes p_1^* -)) \\
&\to (p_4\beta)_!((\beta^*L\otimes \alpha^*K)\otimes \alpha^*p_1^* -)\\
&\to
(p_4\beta)_!((\beta^*L\otimes \alpha^*K)\otimes (p_1\alpha)^* -).
\end{aligned}$$

Let $(\phi,f)\in\operatorname{Hom}\nolimits_{\mathcal{K}}((K,U),(K',U'))$. We have a commutative diagram $$\xymatrix{
& U\ar[ddl]_{p_2}\ar[ddr]^{p_1}\ar[d]_{f}^{\sim} \\
& U'\ar[dl]^{p'_2}\ar[dr]_{p'_1} \\
Y && X
}$$ and we define $\Phi(\phi,f)$ as the composition $$p_{2!}(K\otimes p_1^* -)\buildrel \sim\over\to
p_{2!}'f_!(f^*K'\otimes f^*p_1^{'*} -)\buildrel \sim\over\to
p_{2!}'(K'\otimes p_1^{'*} -).$$

::: thm
[]{#cocycle label="cocycle"} $\Phi$ is a $2$-functor from ${\mathcal{K}}$ to the $2$-category of triangulated categories.

We have $c_{M\boxtimes L,K}\circ(c_{M,L}\Phi_K)=
c_{M,L\boxtimes K}\circ(\Phi_M c_{L,K})$, *i.e.*, the following diagram commutes : $$\xymatrix{
\Phi_M\Phi_L\Phi_K \ar[r] \ar[d] & \Phi_{M\boxtimes L}\Phi_K \ar[d] \\
\Phi_M \Phi_{L\boxtimes K} \ar[r] & \Phi_{M\boxtimes L\boxtimes K}
}$$
:::

### 

The next two Lemmas deal with composition of base change isomorphisms.

For the first Lemma, see [@De1 Lemme 5.2.5] :

::: lemma
[]{#compoh label="compoh"} Let $\xymatrix{
X_2 \ar[r]^{f_2}\ar[d]_{h_2} & X_1\ar[r]^{f_1}\ar[d]_{h_1} & X \ar[d]_h\\
S_2 \ar[r]_{g_2} & S_1\ar[r]_{g_1} & S
}$ be a diagram with all squares cartesian. Then, the following diagram commutes $$\xymatrix{
(g_1g_2)^*h_!\ar[rr]\ar[d] & & {h_2}_! (f_1f_2)^* \\
g_2^*g_1^*h_! \ar[r] & g_2^* {h_1}_!f_1^* \ar[r]& {h_2}_!f_2^*f_1^*\ar[u]
}$$
:::

The second Lemma is [@De1 Lemme 5.2.4] :

::: lemma
[]{#compov label="compov"} Let $\xymatrix{
X'_2\ar[d]_{f'_2}\ar[r]^{g_2} & X_2 \ar[d]^{f_2} \\
X'_1\ar[d]_{f'_1}\ar[r]^{g_1} & X_1 \ar[d]^{f_1} \\
S' \ar[r]_{g}            & S
}$ be a diagram with all squares cartesian. Let $A\in D^b(S')$. Then, the following diagram commutes $$\xymatrix{
A\otimes g^* (f_1f_2)_!- \ar[d]\ar[r] & A\otimes (f'_1f'_2)_! g_2^* -
\ar[r] & (f'_1f'_2)_!((f'_1f'_2)^*A\otimes g_2^* -)\\
A\otimes g^* {f_1}_!{f_2}_!- \ar[d]&& 
 {f'_1}_!{f'_2}_!({f'_2}^*{f'_1}^*A\otimes g_2^*-) \ar[u]\\
A\otimes {f'_1}_!g_1^*{f_2}_!- \ar[r]&
{f'_1}_!({f'_1}^*A\otimes g_1^*{f_2}_!-) \ar[r]&
{f'_1}_!({f'_1}^*A\otimes {f'_2}_!g_2^*-) \ar[u]\\
}$$
:::

::: lemma
[]{#corKunneth label="corKunneth"} Let $f:Y\to X$ and $A,B\in D^b(X)$ and $C\in D^b(Y)$. Then, the following diagram commutes $$\xymatrix{
A\otimes B\otimes f_!C \ar[r]\ar[d] & f_!(f^*(A\otimes B)\otimes C)\ar[d] \\
A\otimes f_!(f^*B\otimes C)\ar[r] & f_!(f^*A\otimes f^*B\otimes C)
}$$
:::

::: proof
*Proof.* The corresponding statement for $f_!$ replaced by $f_*$ is easy, the key point is that the composition $f^*\xrightarrow{f^*\eta}
f^*f_*f^*\xrightarrow{\varepsilon f^*} f^*$ is the identity of $f^*$, where $\eta$ and $\varepsilon$ are the unit and counit of the adjoint pair $(f^*,f_*)$. The Lemma follows easily from this (in the algebraic case, we have only to check in addition the trivial case where $f$ is an open immersion thanks to the transitivity of Lemma [\[compov\]](#compov){reference-type="ref" reference="compov"}, whereas in the topological case we use the embedding $f_!C\subset f_*C$ for $C$ injective). ◻
:::

::: lemma
[]{#triple label="triple"} Let $\xymatrix{
X'\ar[d]_{f'}\ar[r]^{g'} & X \ar[d]^f \\
S' \ar[r]_{g}            & S
}$ be a cartesian square. Let $A\in D^b(S)$ and $B\in D^b(X)$. Then, the following diagram commutes $$\xymatrix{
g^*A\otimes g^*f_!B \ar[r]\ar[d] & g^*A\otimes f'_!{g'}^*B \ar[r] &
 f'_! ({f'}^*g^*A\otimes {g'}^*B)\ar[r] &
 f'_!({g'}^*f^*A\otimes {g'}^*B)\ar[d]\\
g^*(A\otimes f_!B)\ar[rr] && g^*f_!(f^*A\otimes B)\ar[r] & 
 f'_!{g'}^*(f^*A\otimes B)
}$$
:::

::: proof
*Proof.* As in the previous Lemma, one reduces to proving the analog of the Lemma with $?_!$ replaced by $?_*$. This follows then from the easily checked commutativity of the two diagrams $$\xymatrix{
{f'}^*g^*f_*\ar[r]\ar[d]& {f'}^*f'_*{g'}^*\ar[d] & & 
  g^*\ar[r]\ar[d] & g^*f_*f^*\ar[d] \\
{g'}^*f^*f_*\ar[r]& {g'}^* &&
  f'_*{f'}^* g^* \ar[r] & f'_*{g'}^* f^*
}$$ where we have used the units and counits of the adjoint pairs $(f^*,f_*)$ and $({f'}^*,f'_*)$. ◻
:::

::: proof
*Proof of the Theorem.* We will show the commutativity of the following diagram $$\xymatrix{
& & \Phi_M^{p_6,p_5}\Phi_{L\boxtimes K}^{p_4\beta,p_1\alpha}\ar[d]_\zeta
  \ar[drr]^{c_{M,L\boxtimes K}}\\
\Phi_M\Phi_L\Phi_K\ar[urr]^{\Phi_M c_{L,K}}\ar[drr]_{c_{M,L}\Phi_K}
 & & \Phi_{\delta^*M}^{p_6\delta,\gamma} \Phi_{L\boxtimes K}^{\beta,p_1\alpha}
\ar[rr]^{c_{\delta^*M,L\boxtimes K}} & & \Phi_{M\boxtimes L\boxtimes K}\\
& & \Phi_{M\boxtimes L}^{p_6\delta,p_3\gamma}\Phi_K^{p_2,p_1}
  \ar[u]^\xi \ar[urr]_{c_{M\boxtimes L,K}}
}$$ where $\zeta$ is the composition $$\begin{aligned}
{p_6}_!\left(M\otimes p_5^*(p_4\beta)_!(\beta^*L\otimes \alpha^* K\otimes
   (p_1\alpha)^*-)\right)&\to
{p_6}_!\left(M\otimes p_5^*{p_4}_!\beta_!(\beta^*L\otimes \alpha^* K\otimes
   (p_1\alpha)^*-)\right)\\
&\to {p_6}_!\left(M\otimes \delta_!\gamma^*\beta_!(\beta^*L\otimes \alpha^* K
   \otimes (p_1\alpha)^*-)\right)\\
&\to {p_6}_!\delta_!\left(\delta^*M\otimes \gamma^*\beta_!(\beta^*L\otimes
   \alpha^* K \otimes (p_1\alpha)^*-)\right)\\
&\to (p_6\delta)_!\left(\delta^*M\otimes\gamma^*\beta_!(\beta^*L\otimes
   \alpha^* K\otimes (p_1\alpha)^*-)\right)
\end{aligned}$$ and $\xi$ the composition

$$\begin{aligned}
(p_6\delta)_!\left(\delta^*M\otimes\gamma^*L\otimes (p_3\gamma)^*{p_2}_!
  (K\otimes p_1^*-)\right)&\to
(p_6\delta)_!\left(\delta^*M\otimes\gamma^*L\otimes \gamma^*p_3^*{p_2}_!
  (K\otimes p_1^*-)\right)\\
&\to (p_6\delta)_!\left(\delta^*M\otimes\gamma^*(L\otimes p_3^*{p_2}_!
  (K\otimes p_1^*-))\right)\\
&\to (p_6\delta)_!\left(\delta^*M\otimes\gamma^*(L\otimes \beta_!\alpha^*
  (K\otimes p_1^*-))\right)\\
&\to (p_6\delta)_!\left(\delta^*M\otimes\gamma^*(L\otimes
   \beta_!(\alpha^* K\otimes \alpha^*p_1^*-))\right)\\
&\to (p_6\delta)_!\left(\delta^*M\otimes\gamma^*(L\otimes
   \beta_!(\alpha^* K\otimes (p_1\alpha)^*-))\right)\\
&\to(p_6\delta)_!\left(\delta^*M\otimes\gamma^*\beta_!(\beta^*L\otimes
   \alpha^* K\otimes (p_1\alpha)^*-)\right)
\end{aligned}$$

Let $u$ and $v$ be the compositions $$u:{p_6}_!(M\otimes p_5^*{p_4}_!-)\to
{p_6}_!(M\otimes \delta_!\gamma^*-)\to
{p_6}_!\delta_!(\delta^*M\otimes \gamma^*-)\to
(p_6\delta)_! (\delta^*M\otimes \gamma^*-)$$ and $$v:L\otimes p_3^*{p_2}_! (K\otimes p_1^* -)\to
L\otimes \beta_!\alpha^* (K\otimes p_1^* -)\to
\beta_!(\beta^*L\otimes \alpha^* (K\otimes p_1^* -))\to
   \beta_! (\beta^*L\otimes \alpha^*K\otimes (p_1\alpha)^* -).$$

Then, one has trivially $$\zeta(\Phi_M c_{L,K})=u(L\otimes p_3^*{p_2}_! (K\otimes p_1^* -))\circ
{p_6}_!(M\otimes p_5^*{p_4}_!v)=\xi(c_{M,L}\Phi_K).$$

The equality $c_{M,L\boxtimes K}=c_{\delta^*M,L\boxtimes K}\zeta$ follows from Lemma [\[compov\]](#compov){reference-type="ref" reference="compov"} applied to $g=p_5$, $g_1=\gamma$, $g_2=a$, $f_1=p_4$, $f_2=\beta$, $f'_1=\delta$, $f'_2=b$ and $A=M$ and from Lemma [\[comp!\]](#comp!){reference-type="ref" reference="comp!"} applied to $u=p_6$, $v=\delta$ and $w=b$.

The equality $c_{M\boxtimes L,K}=c_{\delta^*M,L\boxtimes K}\xi$ follows from Lemma [\[compoh\]](#compoh){reference-type="ref" reference="compoh"} applied to $f_1=\alpha$, $f_2=a$, $g_1=p_3$, $g_2=\gamma$, $h=p_2$, $h_1=\beta$ and $h_2=b$, from Lemma [\[corKunneth\]](#corKunneth){reference-type="ref" reference="corKunneth"} applied to $f=b$, $A=\delta^*M$, $B=\gamma^*L$ and $C=(\alpha a)^*(K\otimes p_1^*-)$ and from Lemma [\[triple\]](#triple){reference-type="ref" reference="triple"} applied to $f=\beta$, $g=\gamma$, $f'=b$, $g'=a$, $A=L$ and $B=\alpha^*(K\otimes p_1^*-)$. ◻
:::
