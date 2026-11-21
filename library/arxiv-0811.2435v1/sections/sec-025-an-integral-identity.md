---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-025-an-integral-identity
section_title: "An integral identity"
section_number: null
pages: 69-73
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.991
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
In this section we are going to discuss the identity which will be crucial in the proof of the main theorem of Section 6.

Let $\k$ be a field of characteristic zero, and $V_1,V_2,V_3$ be finite-dimensional $\k$-vector spaces.

::: conj
Let $W$ be a formal series on the product $V_1\times V_2\times V_3$ of three vector spaces, depending in a constructible way on finitely many extra parameters, such that $W(0,0,0)=0$ and $W$ has degree zero with respect to the diagonal action of the multiplicative group ${\bf G}_m$ with the weights $(1,-1,0)$. We denote by $\widehat{W}$ the ${\bf G}_m$-equivariant extension of $W$ to the formal neighborhood $\widehat{V_1}$ of $V_1\times \{0\}\times \{0\}\subset V_1\times V_2\times V_3$. Then we have the following formula (where we denote the direct image by the integral): $$\int_{v_1\in V_1}(1-MF_{(v_1,0,0)}(\widehat{W}))={\mathbb L}^{\dim  V_1}(1-MF_{(0,0,0)}(W_{|(0,0,V_3)}))\,\,,$$ where in the RHS we consider the motivic Milnor fiber at $(0,0,0)$ of the restriction of $W$ to the subspace $(0,0,V_3)$.
:::

Using the obvious equality $\int_{V_1} 1={\mathbb L}^{\dim  V_1}$ we can rewrite the identity as $$\int_{v_1\in V_1}MF_{(v_1,0,0)}(\widehat{W})={\mathbb L}^{\dim  V_1}\cdot MF_{(0,0,0)}(W_{|(0,0,V_3)})\,\,.$$

Let us discuss the $l$-adic version of the Conjecture. For simplicity we assume that the vector spaces do not depend on extra parameters. Then we have a morphism of formal schemes $\pi: \widehat{V_1}\to Spf(\k[[w]])$ such that $w\mapsto \widehat{W}$ as well as an embedding $i_{V_1}:V_1\to \widehat{W}^{-1}(0)$. For any morphism $\pi: X\to Spf(\k[[w]])$ of formal schemes to we denote by $\R\psi_{\pi}$ the functor of nearby cycles. It acts from the bounded derived category of $l$-adic constructible sheaves on $X$ to the bounded derived category of $l$-adic constructible sheaves on $X_0=\pi^{-1}(0)$ endowed with the action of the inertia group (hence they can be informally thought of as $l$-adic constructible sheaves on $X_0\times_{Spec(\k)}\k((w))$).

::: prp
The complex $\R\Gamma_c(i^{\ast}_{V_1}\R\psi_{\pi}(\Q_l))$ is isomorphic (as a complex of $\op{Gal}(\overline{\k((w))}/\k((w)))$-modules) to the complex $\R\Gamma_c(V_1,\Q_l)\otimes j^{\ast}\R\psi_{\widehat{\pi}}(\Q_l)$, where $j:Spec(\k)\to V_3, j(0)=0$ is the natural embedding and $\widehat{\pi}$ is the morphism of the formal completion of $0\in \{0\}\times\{0\}\times V_3$ to $Spf(\k[[w]])$ given by the restriction $W_{|\,\{0\}\times\{0\}\times V_3}$.
:::

*Proof.* We will give a sketch of the proof based on the non-archimedean model for the Milnor fiber described in Section 4.3.

Let us consider the $\k((t))$-analytic space (in the sense of Berkovich) associated with the scheme $(V_1\times V_2\times V_3)\times_{Spec(\k)}Spec(\k((t)))$. Let us choose sufficiently small positive numbers $\varepsilon_1, \varepsilon_2,\varepsilon_3,\varepsilon_4$ (we will specify them later) and define an analytic subspace $Y=Y_{\varepsilon_1, \varepsilon_2,\varepsilon_3,\varepsilon_4}$ by the following inequalities: $$|v_1|\le 1+\varepsilon_1, \,\,|v_2|,|v_3|\le \varepsilon_2, \,\,\varepsilon_4\le |W(v_1,v_2,v_3)|\le \varepsilon_3\,\,.$$ Notice that the series $W(v_1,v_2,v_3)$ is convergent on $Y$ because of homogeneity property. We introduce another analytic space $Y^{\prime}=Y_{\varepsilon_1, \varepsilon_2,\varepsilon_3,\varepsilon_4 }^{\prime}\subset Y_{\varepsilon_1, \varepsilon_2,\varepsilon_3,\varepsilon_4 }$ by changing the inequality $|v_1|\le 1+\varepsilon_1$ to the equality $|v_1|=1+\varepsilon_1$ (all other inequalities remain unchanged). There is a natural projection $pr_{Y\to A}$ (resp. its restriction $pr_{Y'\to A}$) of $Y$ (resp. of $Y^{\prime}$) to the annulus $A=\{w|\,\varepsilon_4\le |w|\le \varepsilon_3\}$. Let us now consider the complex $$Cone((pr_{Y\to A})_\ast(\Q_l)\to  (pr_{Y'\to A})_\ast(\Q_l))[-1]\,.$$ This is a *lisse* sheaf on the annulus, i.e. a continuous $l$-adic representation of the fundamental group of the $\k((t))$-analytic space $A$. There is a tautological embedding $\k((w))\to {\cal O}^{an}(A)$. It induces the homomorphism of profinite groups $\pi_1(A)\to
\op{Gal}(\overline{\k((w))}/\k((w)))$. Then one can show that the complex $$Cone((pr_{Y\to A})_\ast(\Q_l)\to  (pr_{Y'\to A})_\ast(\Q_l))[-1]\simeq$$ $$\simeq (pr_{Y\to A})_\ast(Cone(\Q_l\to (i_{Y'\hookrightarrow Y})_*\Q_l))$$ on $A$ is quasi-isomorphic to the pull-back of the complex $\R\Gamma_c(i^{\ast}_{V_1}\R\psi_{\pi}(\Q_l))$ of $\op{Gal}(\overline{\k((w))}/\k((w)))$-modules.

We decompose the space $Y$ into a disjoint union $Y_0\sqcup Y_1$ where for $Y_0$ we have $|v_1||v_2|=0$ while for $Y_1$ we have $|v_1||v_2|\ne 0$. Similarly, we have a decomposition $Y^{\prime}=Y_0^{\prime}\sqcup Y_1^{\prime}$. We claim that the complex $$(pr_{Y_0\to A})_\ast(Cone(\Q_l\to (i_{Y'_0\hookrightarrow Y_0})_*\Q_l))$$ is quasi-isomorphic to the pull-back of the complex $\R\Gamma_c(V_1,\Q_l)\otimes j^{\ast}\R\psi_{\widehat{\pi}}(\Q_l)$ of $\op{Gal}(\overline{\k((w))}/\k((w)))$-modules. Notice that $W_{|Y_0}$ depends on $v_3$ only. Furthermore, $Y_0$ and $Y_0^{\prime}$ can be decomposed as the products $$Y_0=Y_3\times Z_0,\,\,Y_0^\prime=Y_3\times Z_0^{\prime}\,\,,$$ where $$\begin{array}{l}
Z_0:=\{(v_1,v_2)\in V_1^{an}\times V_2^{an}\,|\,\,v_1=0\, \,\mbox{or}\, \,v_2=0,\, |v_1|\le 1+\varepsilon_1, \,|v_2|\le\varepsilon_2\}\,\,,\\
Z_0^{\prime}:=\{(v_1,v_2)\in V_1^{an}\times V_2^{an}\,|\,\,v_2=0,\,|v_1|= 1+\varepsilon_1\}\,\,,\\
Y_3:=\{v_3\in V_3^{an}\,|\,\,|v_3|\le \varepsilon_2,\,\,\varepsilon_4\le |W(0,0,v_3)|\le \varepsilon_3\}\,\,.
\end{array}$$ Here we denote by $V_i^{an}, i=1,2,3$ the $\k((t))$-analytic space associated with the scheme $V_i\times_{Spec(\k)}Spec(\k((t)), i=1,2,3$. Notice that $Z_0$ is the bouquet of two (non-archimedean) balls. It follows that the inclusion of the ball $$Z_0^{\prime\prime}=\{(v_1,0)\,|\,|v_1|\le 1+\varepsilon_1\}$$ into $Z_0$ induces isomorphisms of the Berkovich étale cohomology groups of the $l$-adic sheaves on the analytic spaces. Therefore the cohomology groups of the pair $(Z_0,Z_0^{\prime})$ coincide with the cohomology groups of the pair $(Z_0^{\prime\prime},Z_0^{\prime})$. The latter are equal to $\R\Gamma_c(V_1^{an},\Q_l)$ (which corresponds to the image of ${\mathbb L}^{\dim V_1}$ in $K_0(\op{Gal}(\overline{\k((t))}/\k((t)))-mod)$).

We have an obvious morphism of complexes of sheaves on $Y$: $$f:Cone(\Q_l\to (i_{Y'\hookrightarrow Y})_*\Q_l) \to 
Cone ((i_{Y_0\hookrightarrow Y})_*\Q_l\to (i_{Y'_0\hookrightarrow Y})_*\Q_l)\,\,.$$ In order to prove the Proposition we have to prove that the $(pr_{Y\to A})_*f$ is a quasi-isomorphism, i.e. $(pr_{Y\to A})_*(Cone(f))$ is zero. The compactness of spaces $Y,Y',Y_0,Y_0'$ implies that $$(pr_{Y\to A})_*(Cone(f))\simeq (pr_{Y_1\to A})_!(Cone(\Q_l\to (i_{Y_1'\to Y_1})_\ast \Q_l ))\,\,.$$

The (partially defined) actions of the group ${\bf G}_m$ on $Y_1$ and $Y_1^{\prime}$ are free, and the value of $W$ does not change under the action. More precisely, one can define easily analytic "spaces of orbits" $\widetilde{Y}_1\supset \widetilde{Y}_1^{\prime}$ of ${\bf G}_m$ acting on $Y_1$ and $Y_1^{\prime}$ respectively. The projections $$Y_1\to \widetilde{Y}_1,\,\,\, Y_1'\to \widetilde{Y}_1^{\prime}$$ are proper maps, and the map $W$ factors through them. Hence it is enough to check that $$(pr_{Y_1\to \widetilde{Y}_1})_*(Cone(\Q_l\to (i_{Y_1'\hookrightarrow Y_1})_*\Q_l))\simeq 0\,\,.$$ This follows from the fact that every orbit in $Y_1$ is a closed annulus, its intersection with $Y_1^{\prime}$ is a circle, and the inclusion of a circle into an annulus induces an isomorphism of étale cohomology groups.

This concludes the sketch of the proof. $\blacksquare$

::: rmk
1\) In the proof we did not specify the values of $\varepsilon_i, i=1,2,3,4$. We can take $\varepsilon_4=O(\varepsilon_3)$ (e.g. take $\varepsilon_4=\frac{1}{2}\varepsilon_3$), $\varepsilon_2=o(1)$ and $\varepsilon_3=O(\varepsilon_2^N),\varepsilon_1=O(\varepsilon_3^M)$ for some integers $N,M>0$.

2\) In the proof we used the comparison of the cohomology of the sheaf of nearby cycles with the étale cohomology of subvarieties of $\k((t))$-analytic spaces (see [@NicS]).
:::

We strongly believe that the analog of the Proposition holds at the level of motivic rings in the case $char\,\k=0$.
