---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-014-46-summarising
section_title: "Summarising"
section_number: 4.6
pages: 27-30
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.902
latex_coverage_ratio: 0.981
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
[]{#subsec: summarising quotients label="subsec: summarising quotients"} We can collect the information of the quotients we have seen into the following diagram. Solid arrows represent a covering map coming from a quotient, whereas 'squiggly' arrows indicate isomorphisms that are unexplained by group theory alone.

::: center
<figure id="eq: structure of quotient curves">

<figcaption>Quotient structure of Bring’s curve.</figcaption>
</figure>
:::

This corresponds to the quotients by the following groups, where an arrow now indicates that a source group is normal in the target, whereas a dashed line just indicates that a group is a subgroup. The label used corresponds to the list in §[\[subsec: relations between quotients\]](#subsec: relations between quotients){reference-type="ref" reference="subsec: relations between quotients"}, except where that label is ambiguous and the exact group must be specified.

::: center
<figure id="eq: structure of quotient groups">

<figcaption>Subgroup structre of <span class="math inline"><em>S</em><sub>5</sub></span> corresponding to the quotients of Bring’s curve.</figcaption>
</figure>
:::

Finally, we recall from a Riemann-Hurwitz argument that each elliptic curves that comes a quotient from a genus-2 curve with $V_4$ symmetry has 2 marked points which are the branch points of the covering map, equivalently the images of the fixed points of the involution being quotiented by. We have shown that the preimages of these on Bring's curve are geometric points. In Figure [3](#eq: tracking fixed points){reference-type="ref" reference="eq: tracking fixed points"} we illustrate the quotient structure highlighting these points. (We do not decorate the curve $\mathcal{B}/A_4 \cong \mathcal{E}_{3\tau_0}$, but include it so as to show every quotient with genus greater than 0.) Note the nodes of this diagram do not correspond directly to the placements of those above.

::: center
<figure id="eq: tracking fixed points">

<figcaption>Quotient structure including marked points. The points <span class="math inline">$\textcolor{red}{\times}$</span> correspond to the Weierstrass points <span class="math inline">[1:1:<em>α</em>:<em>β</em>:<em>γ</em>]</span> (and permutations of <span class="math inline"><em>α</em>, <em>β</em>, <em>γ</em></span>), the points <span class="math inline">$\textcolor{blue}{\otimes}$</span> to the vertices <span class="math inline">[1:−1:0:±<em>i</em>:∓<em>i</em>]</span> and <span class="math inline">[1:−1:±<em>i</em>:0:∓<em>i</em>]</span>, the points <span class="math inline">$\textcolor{blue}{\ocircle}$</span> to the vertices <span class="math inline">[1:−1:±<em>i</em>:∓<em>i</em>:0]</span>, and the points <span class="math inline">$\textcolor{blue}{{\square}}$</span> correspond to the vertices <span class="math inline">[1:±<em>i</em>:∓<em>i</em>:−1:0]</span> and <span class="math inline">[1:±<em>i</em>:−1:∓:0]</span>.</figcaption>
</figure>
:::

With the information of the quotients, we can now discuss the isogeny class and isomorphism class of the Jacobian of Bring's curve with the following results.

::: prop
[]{#prop: CC-isogeny class of Bring's Jacobian label="prop: CC-isogeny class of Bring's Jacobian"} The $\mathbb{C}$-isogeny class of the Jacobian of Bring's curve is $\mathcal{E}_3^4$.
:::

::: proof
*Proof.* As we will later want to strengthen this result, we will use methods which relate subvarieties of the Jacobian to idempotents, and thus to subgroups of the automorphism group. Namely we will use [@Lange2001 §4.2], which gives the isogeny decomposition in terms of Prym varieties of the Jacobian of a curve with $A_5$ action. Note, because of comments made before, Bring's curve is the unique genus-4 curve for which we could apply this argument. The result follows as, using the notation of Lange, $X_{A_4} = \mathcal{E}_3$, $X_{D_5} = X_{Z_5} = Y = \mathbb{P}^1$.

This proof also follows from [@Lange2001 Proposition 5.1], which uses only the action of $S_4$ on the curve. Moreover, one could use [@Kani1989 Theorem C] taking the subgroups to be $\left\langle (12) \right\rangle, \left\langle (34) \right\rangle$, $C_4$ and $A_4$. Alternatively, using the isomorphism $A_5 \cong PSL_2(\mathbb{F}_5)$ and [@Kani1989 Example 2] on can find $\mathop{\mathrm{Jac}}\mathcal{B} \sim \mathop{\mathrm{Jac}}\mathcal{C}_1 \times \mathop{\mathrm{Jac}}\mathcal{C}_2$ and proceed from there. These proof strategies all follow the same approach of looking for idempotents.

One may also obtain the result following the same method as R&R. We use that fact that isogenies act on the period matrix by right multiplication by matrices $R \in M_{4}(\mathbb{Z})$, and so we have the required isogeny by taking $\lambda=1$ in the identity $$\begin{pmatrix} \lambda\sp{-1}\mathop{\mathrm{Id}}\end{pmatrix} \begin{pmatrix} 1 & \tau M \end{pmatrix}  \begin{pmatrix} \lambda\mathop{\mathrm{Id}}& 0 \\ 0 & M^\prime \end{pmatrix} = \begin{pmatrix}\mathop{\mathrm{Id}}& \dfrac{5}{\lambda}\tau \mathop{\mathrm{Id}}\end{pmatrix}  ,$$ where $$M':= 5 M^{-1} = \begin{pmatrix} 2 & -1 & 1 & -1 \\ -1 & 2 & -1 & 1 \\ 1 & -1 & 2 & -1 \\ -1 & 1 & -1 & 2 \end{pmatrix}  .$$ ◻
:::

Note that we are able to construct the quotient $\mathcal{B}/A_4$ directly from the $\mathbb{P}^4$-model using transformations with coefficients in $\mathbb{Q}$, and the resulting curve is defined over $\mathbb{Q}$, so by [@Kani1989 Remark 6] the above proposition can be strengthened to a statement about the $\mathbb{Q}$-isogeny class of the Jacobian of Bring's curve. Calculating using Sage we find that the $\mathbb{Q}$-isogeny class of $\mathcal{B}/A_4$ is 50a using the Cremona labels for elliptic curve $\mathbb{Q}$-isogeny classes. Hence the following result holds.

::: prop
[]{#prop: JB Q-isogeny class label="prop: JB Q-isogeny class"} The $\mathbb{Q}$-isogeny class of the Jacobian of the $\mathbb{P}^4$-model of Bring's curve is $(50a)^4$.
:::

Note in the above proposition we had to be careful to specify the Jacobian of the $\mathbb{P}^4$-model of Bring's curve, as we have seen that HC-model is not birationally equivalent over a field that doesn't contain $\mathbb{Q}[\zeta]$. The $\mathbb{Q}$-isogeny class of the elliptic curve $\mathcal{B}/\left\langle (12)(34), (13)(24) \right\rangle$ calculated via the HC-model is 50b. Similarly, the $\mathbb{Q}$-isogeny class of the two elliptic curves covered by $\mathcal{C}_2$ is 450b, and the computation of the quotient required the coefficient field to be $\mathbb{Q}[\rho]$. In order to not have a contradiction with Proposition [\[prop: JB Q-isogeny class\]](#prop: JB Q-isogeny class){reference-type="ref" reference="prop: JB Q-isogeny class"}, we must have that the $\mathbb{Q}$-isogeny classes 50b and 50a merge over $\mathbb{Q}[\sqrt{5}]$, and that the isogeny classes 450b and 50a merge over $\mathbb{Q}[\rho]$, which is indeed the case.[^1]

One could use computational tools such as those in [@Booker2016; @Lombardo2018][^2] to numerically find the $\mathbb{Q}$-isogeny class of the Jacobian of the HC-model of Bring's curve, as we did in the notebooks. Such computational results using idempotents can be helpful for developing our understanding, for example one can use computer algebra to search for relations between the characters $\operatorname{Ind}_H^{S_5}(1_H)$, that is the characters of $S_5$ induced from the trivial representation of $H \leq S_5$. Doing so gives relations between subvarieties of the Jacobian of Bring's curve following [@Kani1989 Theorem 3], for example $$\begin{aligned}\label{isogenies}
    J_{\left\langle (12) \right\rangle} \times J_{\left\langle (12)(34), (13)(24) \right\rangle} & \sim J_{\left\langle (12)(34) \right\rangle} \times J_{\left\langle (12), (34) \right\rangle} , \\
    J_{\left\langle (12)(34), (13)(24) \right\rangle} \times J_{S_3} &\sim J_{\left\langle (12), (34) \right\rangle} \times J_{S_3^\prime} .
\end{aligned}$$ Using Riemann-Hurwitz arguments these would let us say that $\mathcal{B}/\left\langle (12) \right\rangle \sim \mathcal{B}/C_4$ and $\mathcal{B}/\left\langle (12)(34), (13)(24) \right\rangle \sim \mathcal{B}/S_3^\prime$ without having to do any calculation, entirely from group theory. The reason why these isogenies are actually isomorphisms is not clear.

Proposition [\[prop: CC-isogeny class of Bring\'s Jacobian\]](#prop: CC-isogeny class of Bring's Jacobian){reference-type="ref" reference="prop: CC-isogeny class of Bring's Jacobian"} can also be strengthened in a different direction.

::: prop
The Jacobian of Bring's curve is isomorphic as a complex torus to $\mathcal{E}_2^3 \times \mathcal{E}_1$.
:::

::: proof
*Proof.* The proof in [@Gonzalez2000] is very general, considering Jacobians whose period matrix is invariant under $S_n$ for any $n$. The isomorphism from the period matrix given in [@Riera1992] is $$C \begin{pmatrix}
1 & \tau M
\end{pmatrix} \begin{pmatrix}
D & 0 \\ 0 & E
\end{pmatrix} = \begin{pmatrix}1, \tau \operatorname{diag}(5, 5, 5, 1) \end{pmatrix}$$ where $$C = \begin{pmatrix}
-1 & 1 & -1 & 2 \\ 1 & 0 & 0 & 1 \\ 0 & -1 & 0 & 1 \\ 0 & 0 & 0 & 1
\end{pmatrix},  D = \begin{pmatrix}
0 & 1 & 0 & -1 \\ 0 & 0 & -1 & 1 \\ -1 & -1 & -1 & 4 \\ 0 & 0 & 0 & 1
\end{pmatrix},  E = \begin{pmatrix}
-1 & 1 & 0 & 0 \\ 1 & 0 & -1 & 0 \\ -2 & -1 & -1 & 1 \\ 1 & 0 & 0 & 0
\end{pmatrix}  .$$ ◻
:::

Note it would not be possible that the Jacobian is isomorphic to the product of the elliptic curves as a principally polarised abelian variety, as it is well know that the Jacobian of any smooth compact Riemann surface with canonical principal polarisation is irreducible. In particular this means the matrix $\begin{pmatrix}
D & 0 \\ 0 & E
\end{pmatrix}$ of the proposition is not symplectic.

[^1]: The isogeny classes 450b and 50b merge over $\mathbb{Q}[\sqrt{-15}]$.

[^2]: To make the reconstruction process of Lombardo more accessible, we recreated in Sage some of the functions implemented by Lombardo in Magma.
