---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-010-4-cocommutative-algebraic-quantum-groups-vs-comp
section_title: "Cocommutative Algebraic Quantum Groups vs. Compact Groups"
section_number: 4
pages: 20-25
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.972
doc_brief: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002 — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups which are related to the Tannaka-Krein"
---
::: defin
[]{#d-intrins label="d-intrins"} Let $(A,\Delta)$ be an aqg. The intrinsic group $G$ of $(A,\Delta)$ is the following subgroup of the unitaries in the multiplier algebra $M(A)$: $$G=\{g\in M(A)\ |\ \Delta g=g\otimes g,\ g^* g =gg^* =1\}.$$
:::

Since the extended comultiplication $\Delta:M(A)\rightarrow M(A\otimes A)$ is a unital $*$-homomorphism and the algebra $M(A)$ is associative, the set $G$ is indeed a group. It is easy to see that $\varepsilon(g)=1$ and $S(g)=g^{-1}=g^*$, for any $g\in G$.

::: rema
It can be shown that any bounded group-like element of $M(A)$ is automatically unitary with $S(g)=g^*$. A proof of this may be found in [@KD] and [@ES], but the above definition suffices for our purposes.
:::

::: lem
[]{#l-loc_cp label="l-loc_cp"} Let $(A,\Delta)$ be a discrete aqg. Equipped with the product topology, $M(A)=\prod_{i\in I} B(H_i )$ is a complete locally convex topological vector space and $A$ is dense in $M(A)$.
:::

*Proof. *Since the blocks $B(H_i)$ are Banach spaces, the functions $\| p_i(\cdot)\|$ form a separating family of seminorms which induces the product topology. Completeness is obvious by semisimplicity of the $B(H_i),\ i\in I$. To see that $A$ is dense in $M(A)$, let $x\in M(A)$ and consider the net $(x_{\lambda})_{\lambda\in\Lambda}$ in $A$ given by $x_{\lambda}=\oplus_{i\in\lambda}p_i (x)$, where $\Lambda$ is the collection of finite subsets of $I$ directed by inclusions. Then clearly $x_{\lambda}\rightarrow x$.

::: prop
If $(A,\Delta)$ is a discrete aqg, its intrinsic group $G$ is a compact topological group w.r.t. the product topology on $M(A)$.
:::

*Proof. * Note that a net $(g_{\lambda})$ converges to $g$ in $G$ iff $p_i (g_{\lambda})\rightarrow p_i (g)$ in norm, for all $i\in I$. By Tychonov's theorem it suffices to show that $G$ is closed in $\prod_{i\in I} U(B(H_i ))$. Given a net $(g_{\lambda})$ in $G$ which converges to $a\in M(A)$, we must show that $\Delta a=a\otimes a$. Let $i,j\in I$ and consider the finite dimensional non-degenerate $*$-representation $(p_i\otimes p_j )\Delta:A\rightarrow B(H_i\otimes H_j )$. By Proposition [\[Berkeley\]](#Berkeley){reference-type="ref" reference="Berkeley"}, we may write $$(p_i\otimes p_j )\Delta\simeq\bigoplus_{k\in I}\ N_{ij}^k\, p_k.$$ Since both these expressions are non-degenerate $*$-representations, they extend to equivalent unital $*$-representations of $M(A)$, which we now identify. Therefore $$(p_i\otimes p_j )\Delta a =\bigoplus_{k\in I}\ N_{ij}^k\, p_k (a)
=\lim_{\lambda}\bigoplus_{k\in I}\ N_{ij}^k\, p_k (g_{\lambda})
=\lim_{\lambda}(p_i\otimes p_j )\Delta g_{\lambda}$$ $$=\lim_{\lambda}p_i (g_{\lambda})\otimes p_j (g_{\lambda})
=p_i (a)\otimes p_j (a)=(p_i\otimes p_j )(a\otimes a),$$ thus $\Delta a =a\otimes a$ and $G$ is closed.

::: rema
Note furthermore that in the proof of the proposition we have shown that $$\Delta:M(A)=\prod_{i\in I}B(H_i )\rightarrow M(A\otimes A)=\prod_{i,j\in I}B(H_i\otimes H_j )$$ is continuous w.r.t. the product topologies.
:::

::: prop
[]{#p-functor_D label="p-functor_D"} Suppose $(A,\Delta)$ is a discrete aqg with intrinsic group $G$. Let $\pi$ be a non-degenerate $*$-representation of $A$ on a finite dimensional Hilbert space $K$. Define a map $u_{\pi} :G\rightarrow B(K)$ by $$u_{\pi} : g\mapsto \pi (g),$$ where the extension of $\pi$ to $M(A)$ is understood. Then $u_{\pi}$ is strongly continuous and $D: (K,\pi) \mapsto (K,u_{\pi})$ together with the identity map on the morphisms is a faithful and tensor functor from $\mathrm{Rep}_f(A,\Delta)$ to the category $\mathrm{Rep}_f\,G$ of finite dimensional continuous representations of $G$.
:::

*Proof. *Continuity of $u_\pi$ w.r.t. the topology on $G$ is obvious. As $\pi :M(A)\rightarrow B(K)$ is a unital $*$-homomorphism, clearly $(K, u_{\pi})\in\mathrm{Rep}\,G$. Functoriality and faithfulness of $D$ are obvious. Monoidality follows from the calculation $$D(\pi_1\times\pi_2)(g)=(\pi_1\otimes\pi_2 )\Delta g=\pi_1 (g)\otimes\pi_2 (g)
=u_{\pi_1}(g)\otimes u_{\pi_2 }(g)=(u_{\pi_1}\times u_{\pi_2 })(g)$$ for all $g\in G$ and $\pi_i\in \mathrm{Rep}(A,\Delta)$. Every $\pi\in \mathrm{Rep}(A,\Delta)$ is equivalent to a direct sum of the representations $p_i$ by Proposition [\[Berkeley\]](#Berkeley){reference-type="ref" reference="Berkeley"}. Each $u_{p_i}$ is (strongly) continuous and therefore the direct sum is strongly continuous.

Thus far we have not assumed $(A,\Delta)$ to be cocommutative. The following characterization of cocommutativity will be crucial for proving that $D$ gives rise to an equivalence of categories.

::: thm
[]{#t-cocomm1 label="t-cocomm1"} A discrete aqg $(A,\Delta)$ is cocommutative iff $$\overline{\mathrm{span}_{\mathbb C} \{ g\ |\ g\in G \}}=M(A).$$
:::

::: rema
This theorem implies that $$\mathrm{span}_{\mathbb C} \{ p_i(g)\ |\ g\in G \}=B(H_i)$$ for every $i\in I$ and in particular that $A=\mathrm{span}_{\mathbb C} \{ gI_i \ |\ i\in I, g\in G \}$. These results are rigorous formulations of the heuristic idea that a cocommutative aqg is 'spanned by its grouplike elements'. Before we give the proof of Theorem [\[t-cocomm1\]](#t-cocomm1){reference-type="ref" reference="t-cocomm1"} we show that it leads to the desired equivalence of categories.
:::

In what follows we fix a cocommutative discrete aqg $(A,\Delta)$ where $A=\oplus_{i\in I} B(H_i)$ and let $G$ denote its intrinsic group. For every $i\in I$, $u_i : g\mapsto p_i(g)\in B(H_i)$ is a continuous unitary representation of $G$. By Theorem [\[t-cocomm1\]](#t-cocomm1){reference-type="ref" reference="t-cocomm1"}, the span of $p_i(g),\ g\in G$ is dense in $B(H_i)$, thus $u_i$ is irreducible. This defines a map $\gamma: I\rightarrow I_G$.

::: prop
[]{#p-biject label="p-biject"} The map $\gamma$ is a bijection.
:::

*Proof. * If there is a unitary $V: H_i\rightarrow H_j$ such that $Vp_i(g)=p_j(g)V$ for all $g\in G$ then $Vp_i(x)=p_j(x)V$ for all $x\in \mathrm{span}_{\mathbb C} \{ g\ |\ g\in G \}$. Since these $x$ are dense in $M(A)$ by Theorem [\[t-cocomm1\]](#t-cocomm1){reference-type="ref" reference="t-cocomm1"} and the $p_i$ are continuous we conclude that $Vp_i(x)=p_j(x)V$ for all $x\in M(A)$, thus $i=j$ so that $\gamma: I\rightarrow I_G$ is injective.

Obviously if $g\ne e$ there is an $i\in I$ such that $p_i(g)\ne 1_{B(H_i)}$. Since the category $\mathrm{Rep}_f(A,\Delta)$ is monoidal and has conjugates, $\gamma(I)\subset I_G$ is closed w.r.t. conjugation and tensor products and reduction. The surjectivity of $\gamma$ now follows from the following well known group theoretical fact.

::: lem
[]{#l-surj label="l-surj"} Let $G$ be a compact group and let $J\subset I_G$ be closed w.r.t. conjugation and tensor products and reduction. If $J$ separates points on $G$ then $J=I_G$.
:::

*Proof. *For every equivalence class $i\in I_G$ pick a representative $u_i$. The assumptions on $J$ imply that the span of the matrix elements $(u_j)_{nm},\ j\in J$ is a unital $*$-subalgebra of $C(G)$. Since it separates the points of $G$ it is dense in $C(G)$ by the Stone-Weierstrass theorem and therefore dense in $L^2(G,\mu)$, where $\mu$ is the Haar measure. If there were a $k\in I_G\backslash J$ then by the Peter-Weyl theorem the matrix elements of $u_k$ would be orthogonal to the dense subspace of $L^2(G,\mu)$ generated by the $(u_j)_{nm},\ j\in J$, which is a contradiction.

::: thm
[]{#t-cocomm2 label="t-cocomm2"} Let $(A,\Delta)$ be a cocommutative discrete aqg and $G$ its intrinsic group. Then the functor $D :\mathrm{Rep}(A,\Delta)\rightarrow\mathrm{Rep}\,G$ induces a canonical equivalence of tensor $*$-categories: $$\begin{aligned}

  \mathrm{Rep}_f(A,\Delta) & \stackrel{\otimes}{\simeq} & \mathrm{Rep}_f\,G.
\end{aligned}$$
:::

*Proof. *In view of Proposition [\[p-functor_D\]](#p-functor_D){reference-type="ref" reference="p-functor_D"} it only remains to prove that the functor $D$ is full and essentially surjective. By Proposition [\[Berkeley\]](#Berkeley){reference-type="ref" reference="Berkeley"} the category $\mathrm{Rep}_f(A,\Delta)$ is semisimple, and for a compact group $G$ the semisimplicity of $\mathrm{Rep}_f G$ is well known. Recall from Section [\[ss-categ\]](#ss-categ){reference-type="ref" reference="ss-categ"} that a faithful functor between semisimple categories is full if and only if it maps simple objects to simple objects and non-isomorphic simple objects have non-isomorphic images. The first property was used to define the map $\gamma$ of Proposition [\[p-biject\]](#p-biject){reference-type="ref" reference="p-biject"}, and the second is the injectivity of $\gamma$. Finally, essential surjectivity of $D$ is expressed by surjectivity of $\gamma$. Since $D$ is monoidal it gives rise to an equivalence of tensor categories by [@SR].

Now we prove the characterization of cocommutative discrete aqg used above.\
*Proof of Theorem [\[t-cocomm1\]](#t-cocomm1){reference-type="ref" reference="t-cocomm1"}.* Clearly, if the closure of $\mathrm{span}_{\mathbb C}\{g\, |\, g\in G\}$ is $M(A)$, then by linearity and continuity of $\Delta:M(A)\rightarrow M(A\otimes A)$, we see that $(A,\Delta)$ is cocommutative. We prove the converse direction. By Lemma [\[l-loc_cp\]](#l-loc_cp){reference-type="ref" reference="l-loc_cp"} it suffices to show that any $x\in A$ is the limit of linear combinations of elements of $G$. Fix $x\in A$. For any aqg $(A,\Delta)$ there exists a linear inclusion $Q:A\hookrightarrow \hat{A}_r^*$ determined by $$Q(b)\hat{\pi}_r (\hat{a})=\hat{a}(b)=\varphi (ba)$$ for all $a,b\in A$. To see this, to any $a,b\in A$ we can choose an element $c\in A$ such that $\hat{c}\hat{b^*}^* =\hat{b^*}^*$. (Such $c$ can be obtained as inverse Fourier transform of a local unit for $\hat{b^*}^*$ in $\hat{A}$.) Now we observe that $$Q(b)\hat{\pi}_r (\hat{a})=\varphi((b^*)^*a)
   =\hat{\psi}(\hat{b^*}^*\hat{a})=\hat{\psi}(\hat{c}\hat{b^*}^*\hat{a}) 
   =\hat{\psi}(\hat{b^*}^*\hat{a}\hat{\rho}(\hat{c}))
   =(\hat{\pi}_r (\hat{a})\hat{\Lambda}(\hat{\rho}(\hat{c})),\hat{\Lambda}(\hat{b^*} )),$$ so $Q(b)=(\cdot\hat{\Lambda}(\hat{\rho}(\hat{c})),\hat{\Lambda}(\hat{b^*} ))$. Now $\hat{A}_r$ is a unital commutative $C^*$-algebra. Let $Y$ be the set of $*$-characters on $\hat{A}_r$. Gelfand's theorem tells us that $Y$ is a compact Hausdorff space and that the map ${\Gamma}:\hat{A}_r\rightarrow C(Y)$ given by ${\Gamma}(a)(y)=y(a)$, for all $a\in\hat{A}_r$ and $y\in Y$, is a unital $*$-isomorphism from $\hat{A}_r$ to the $C^*$-algebra $C(Y)$ of continuous functions on $Y$. Thus $Q(x){\Gamma}^{-1}\in C(Y)^*$. By the Krein-Milman theorem for probability measures [@ped Theorem 2.5.4] any element of $C(Y)^*$ is a $w^*$-limit of linear combinations of Dirac measures $\delta_y\in C(Y)^*$. Hence we may write $$Q(x){\Gamma}^{-1}=\lim_\lambda\sum_k c_{\lambda k}\delta_{y_{\lambda k}}$$ for some $c_{\lambda k}\in {\mathbb C}$ and $y_{\lambda k}\in Y$. Thus we get $$\begin{aligned}
\hat{a}(x) &=& Q(x)\hat{\pi}_r (\hat{a})=Q(x){\Gamma}^{-1}{\Gamma}\hat{\pi}_r (\hat{a})
=\lim_\lambda\sum_k c_{\lambda k}\delta_{y_{\lambda k}}{\Gamma}\hat{\pi}_r (\hat{a}) \\
 &=& \lim_\lambda\sum_k c_{\lambda k}{\Gamma}\hat{\pi}_r (\hat{a})(y_{\lambda k})
=\lim_\lambda\sum_k c_{\lambda k}\, y_{\lambda k}\hat{\pi}_r(\hat{a})
\end{aligned}$$ for all $a\in A$. Now the $y_{\lambda k}\hat{\pi}_r :\hat{A}\rightarrow{\mathbb C}$ are unital $*$-homomorphisms, so we may define $g_{\lambda k}\in M(A)$ by $$g_{\lambda k}=(\iota\otimes y_{\lambda k}\, \hat{\pi}_r )U,$$ where $U\in M(A\otimes\hat{A})$ is the universal corepresentation of $(A,\Delta)$. Since $U$ is unitary, so are the elements $g_{\lambda k}$ and moreover, $$\begin{aligned}
\Delta g_{\lambda k} &=&\Delta(\iota\otimes y_{\lambda k}\, \hat{\pi}_r )U
=(\iota\otimes\iota\otimes y_{\lambda k}\, \hat{\pi}_r)(\Delta\otimes\iota )U
=(\iota\otimes y_{\lambda k}\, \hat{\pi}_r)(U_{13}U_{23}) \\
 &=& (\iota\otimes y_{\lambda k}\, \hat{\pi}_r)U\otimes(\iota\otimes y_{\lambda k}\, \hat{\pi}_r)U
=g_{\lambda k}\otimes g_{\lambda k},
\end{aligned}$$ thus all $g_{\lambda k}\in G$.

Now for any $\xi\in B(H_i)'$ and $i\in I$ observe that $\xi p_i\in \hat{A}$ since $\varphi$ is, up to a factor $d_i$, the trace on $B(H_i)$. Thus by Theorem [\[t-univ-corep\]](#t-univ-corep){reference-type="ref" reference="t-univ-corep"} we have $(\xi p_i\otimes\iota )U =\xi p_i$. Hence by the previous formulae we get $$\begin{aligned}
\xi p_i (x) &=& \lim_\lambda\sum_k c_{\lambda k}\, y_{\lambda k}\hat{\pi}_r(\xi p_i )
=\lim_\lambda\sum_k c_{\lambda k}\, y_{\lambda k}\hat{\pi}_r(\xi p_i\otimes\iota )U \\
 &=& \lim_\lambda\sum_k c_{\lambda k}\, \xi p_i (\iota\otimes y_{\lambda k}\, \hat{\pi}_r )U
=\lim_\lambda\sum_k c_{\lambda k}\, \xi p_i (g_{\lambda k})
=\lim_\lambda\xi p_i(\sum_k c_{\lambda k}\,  g_{\lambda k}).
\end{aligned}$$ Since this is true for all $i\in I$ and $\xi\in B(H_i)'$, we thus get $$x=\lim_\lambda\sum_k c_{\lambda k}\,  g_{\lambda k}$$ as desired.

This concludes the proof of Theorem [\[t-cocomm1\]](#t-cocomm1){reference-type="ref" reference="t-cocomm1"}.

::: cor
[]{#c-span label="c-span"} For every $i\in I$ we have $\ \mathrm{span}_{\mathbb C} \{ p_i(g)\ |\ g\in G \}=B(H_i)$.
:::

*Proof. *First we show that for $0\ne a\in A$, there exist $g\in G$ such that $\varphi (ga)\neq 0$. Thus let $0\ne a\in A$. Then there exists $x\in A$ such that $\hat{a}(x)=\varphi(xa)\ne 0$, thus $\hat{a}=\varphi(\cdot a)\ne 0$. Furthermore, there exists a finite set $\Lambda\subset I$ such that $$\hat{a}(b)=\varphi (ba)=\sum_{i\in\Lambda} d_i Tr_i (p_i (ba)),$$ for all $b\in M(A)$. Since the product in $M(A)$ is continuous, we thus see that $\hat{a}: M(A)\rightarrow{\mathbb C}$ is continuous. Thus by Theorem [\[t-cocomm1\]](#t-cocomm1){reference-type="ref" reference="t-cocomm1"} there exists $g\in G$ such that $\varphi(ga)\ne 0$.

Assume now that $\mathrm{span}_{\mathbb C} \{p_i(g) \ | \ g\in G\}\ne B(H_i)$. Then there exists a non-zero $a\in B(H_i)$ such that $Tr_{B(H_i)}(p_i(g)a)=0$ for all $g\in G$. Since $\varphi\upharpoonright B(H_i)=d_i Tr_{B(H_i)}$, this is a contradiction.

Let $G$ be a compact group and consider a unitary representation $u:G\rightarrow B(K)$ of $G$ on some finite dimensional Hilbert space $K$. Since $u$ is continuous (here with respect to the norm), we have $u\in C(G,B(K))$. Since $C(G,B(K))\cong C(G)\otimes B(K)$, we may thus regard $u$ as a unitary element $\tilde{V}$ of the unital $*$-algebra $C(G)\otimes B(K)$. Now $u:G\rightarrow B(K)$ being a representation simply means that $(\Delta\otimes\iota )\tilde{V} =\tilde{V}_{13}\tilde{V}_{23}$, where $\Delta:C(G)\rightarrow C(G\times G)\cong C(G)\otimes C(G)$ is given by $\Delta(a)(g,g')=a(gg' )$, for all $a\in C(G)$ and $g,g'\in G$. Thus $\tilde{V}$ is a unitary corepresentation of the commutative compact quantum group $(C(G),\Delta)$ in the sense of Woronowicz. It is easy to see that one may recover $u$ from $\tilde{V}$ by $u(g)=(\delta_g\otimes\iota )\tilde{V}$, for $g\in G$.

::: thm
Let $(A,\Delta)$ be a cocommutative discrete aqg, so $(\hat{A},\hat{\Delta})$ is a commutative compact aqg. Let $G$ be the compact group such that $(C(G),\Delta)\cong (\hat{A}_r, \hat{\Delta}_r )$. For any $V\in\mathrm{Corep}_f (\hat{A},\hat{\Delta})$, let $\tilde{V}\in C(G)\otimes B(K)$ be the unitary corepresentation of $(C(G),\Delta)$ given by $\tilde{V} =(\hat{\pi}_r\otimes\iota )V$. Then there exists an isomorphism from $G$ to the intrinsic group of $(A,\Delta)$ given by $$g\mapsto\tilde{g}=(\iota\otimes\delta_g\hat{\pi}_r )U \in M(A),$$ where $U$ is the universal corepresentation of $(A,\Delta)$. Moreover, the equivalence $$\mathrm{Corep}_f (\hat{A},\hat{\Delta})\stackrel{P}{\longrightarrow}\mathrm{Rep}_f (A,\Delta)\stackrel{D_f}{\longrightarrow}\mathrm{Rep}_f G$$ given by the composition $$V\mapsto \pi_V\mapsto u_{\pi_V}=:u_V,$$ with $P$ and $D_f$ established in Theorem [\[t-dualcor\]](#t-dualcor){reference-type="ref" reference="t-dualcor"} and Theorem [\[t-cocomm2\]](#t-cocomm2){reference-type="ref" reference="t-cocomm2"}, is described more directly by $$u_V (\tilde{g})=(\delta_g\otimes\iota )\tilde{V},$$ for all $g\in G$.
:::

*Proof. * From the proof of Theorem [\[t-cocomm1\]](#t-cocomm1){reference-type="ref" reference="t-cocomm1"}, it is easily seen that $g\mapsto\tilde{g}$ is indeed a homeomorphism from $G$ to the intrinsic group of $(A,\Delta)$ which also preserves the products. Let $g\in G$. We proceed to show that $u_V (\tilde{g})=(\delta_g\otimes\iota )\tilde{V}$. Since $V\in\hat{A}\otimes B(K)$ we may write $V=\sum_k \omega_k\otimes x_k$ for $\omega_k\in\hat{A}$ and $x_k\in B(K)$. Then $$\begin{aligned}
 \lefteqn{ 
u_V (\tilde{g}) = u_V((\iota\otimes\delta_g\hat{\pi}_r )U)
=\pi_V ((\iota\otimes\delta_g\hat{\pi}_r )U) } \\
&=& ([(\iota\otimes\delta_g\hat{\pi}_r )U]\otimes\iota )V
=\sum_k [(\iota\otimes\delta_g\hat{\pi}_r )U](\omega_k )x_k
=\sum_k (\omega_k\otimes\delta_g\hat{\pi}_r )U x_k \\
&=& \sum_k \delta_g\hat{\pi}_r ((\omega_k\otimes\iota )U) x_k
=\sum_k \delta_g\hat{\pi}_r (\omega_k ) x_k 
=(\delta_g\hat{\pi}_r\otimes\iota )(\sum_k \omega_k \otimes x_k ) 
=(\delta_g\hat{\pi}_r\otimes\iota )V =(\delta_g\otimes\iota )\tilde{V},
\end{aligned}$$ as claimed.
