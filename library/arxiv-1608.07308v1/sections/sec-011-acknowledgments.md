---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-011-acknowledgments
section_title: "Acknowledgments"
section_number: null
pages: 10-11
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.901
---
The authors would like to thank Michael Abel, Ben Elias and Matt Hogancamp for explaining to us their results [@AbHog; @EH; @Hog], and Mikhail Gorsky, Daniel Halpern-Leistner, Mikhail Khovanov, Ivan Losev, Davesh Maulik, Michael McBreen, Hugh Morton, Alexei Oblomkov, Andrei Okounkov, Claudiu Raicu, Sam Raskin, Raphael Rouquier, Lev Rozansky, Peter Samuelson, Peng Shan and Monica Vazirani for very useful discussions. Special thanks to Ian Grojnowski for explaining Example [\[ex:not lci\]](#ex:not lci){reference-type="ref" reference="ex:not lci"} to us. The work of E. G. was partially supported by the NSF grant DMS-1559338 and the Hellman fellowship. The work of A. N. was partially supported by the NSF grant DMS-1600375. The work of E.G. in sections 3, 5 and 6 was supported by the grant 16-11-10018 of the Russian Science Foundation.

# The flag Hilbert scheme {#sec:flag}

## Definition {#sub:defflag}

Let us recall the usual **Hilbert scheme** of $n$ points on $\mathbb{C}^2$: $$\mathrm{Hilb}_n = \{\text{ideal } I \subset \mathbb{C}[x,y], \text{ dim}_{\mathbb{C}} \ \mathbb{C}[x,y]/I = n \}$$ There is a **tautological bundle** of rank $n$ on the Hilbert scheme given by: $$\mathcal{T}_n|_I = \mathbb{C}[x,y]/I$$ Similarly, one can define the **flag Hilbert scheme** $\mathrm{FHilb}_n(\mathbb{C}^2)$ of $n$ points on $\mathbb{C}^2$ [@Cheah; @Tikh] as the moduli space of complete flags of ideals: $$\label{eqn:flagdef}
\mathrm{FHilb}_n(\mathbb{C}^2) = \{I_n \subset ... \subset I_1 \subset I_0 = \mathbb{C}[x,y], \text{ dim } I_{k-1}/I_k = 1, \ \forall k\}$$ Clearly, $\mathrm{FHilb}_n(\mathbb{C}^2)$ can be thought of as the closed subscheme of $\mathrm{Hilb}_n \times ... \times \mathrm{Hilb}_1 \times \mathrm{Hilb}_0$ cut out by the inclusions $I_k \subset I_{k-1}$ for all $k$. We will not pursue this description, and instead work with an alternative one given in the next Subsection. Meanwhile, let us point out several general features of the flag Hilbert scheme [\[eqn:flagdef\]](#eqn:flagdef){reference-type="eqref" reference="eqn:flagdef"}. We may pull $\mathcal{T}_n$ back to $\mathrm{FHilb}_n(\mathbb{C}^2)$, where we have a full flag of tautological bundles:

![image](tauto.png) of ranks $n,...,1$. For any $k \in \{1,...,n\}$, the fibers of $\mathcal{T}_k$ over flags $I_n \subset ... \subset I_0$ are precisely the quotients $\mathbb{C}[x,y]/I_k$. We define the tautological line bundles as the successive kernels: $$\label{eqn:taut line}
\mathcal{L}_k = \text{Ker} \left( \mathcal{T}_k \twoheadrightarrow \mathcal{T}_{k-1} \right)$$ Moreover, there is a morphism: $$\label{eqn:rho}
\rho: \mathrm{FHilb}_n(\mathbb{C}^2) \longrightarrow \mathbb{C}^{2n}=\mathbb{C}^n\times \mathbb{C}^n$$ $$(I_n \subset ... \subset I_0) \mapsto (x_1,\ldots, x_n, y_1,\ldots, y_n)$$ where $(x_k,y_k) = \mathrm{supp}\ I_{k-1}/I_k$. We may consider the various fibers of this map: $$\mathrm{FHilb}_n(\mathbb{C})=\rho^{-1}(\mathbb{C}^n\times \{0\}), \qquad \mathrm{FHilb}_n(\text{point}) = \rho^{-1}(\{0\}\times \{0\})$$ These will be the moduli spaces of flags of sheaves set-theoretically supported on the line $\{y=0\}$ and at the point $(0,0)$, respectively. The vector bundles $\mathcal{T}_k$ and $\mathcal{L}_k$ are defined as before. As a rule, we will write: $$\mathrm{FHilb}_n \quad \text{for any of} \quad \mathrm{FHilb}_n(\mathbb{C}^2), \mathrm{FHilb}_n(\mathbb{C}) \text{ or } \mathrm{FHilb}_n(\mathrm{point})$$ when we will make general statements that apply to all our flag Hilbert schemes.

::: example
[]{#ex:hilb label="ex:hilb"}

It is well-known that $\mathrm{Hilb}_2$ is the blow-up of the diagonal inside $(\mathbb{C}^2\times \mathbb{C}^2)/S_2$. It should be no surprise that: $$\label{eqn:c2}
\mathrm{FHilb}_2(\mathbb{C}^2) = \text{Bl}_\Delta\left( \mathbb{C}^2 \times \mathbb{C}^2 \right) = \text{Proj} \left( \frac {\mathbb{C}[x_1,x_2,y_1,y_2,z,w]}{(x_1-x_2)w - (y_1-y_2)z} \right)$$ where the variables $x_i,y_i$ sit in degree 0, while $z,w$ sit in degree 1 with respect to the Proj. Setting $y_1=y_2=0$, respectively $x_1=x_2=y_1=y_2=0$, we obtain: $$\label{eqn:c1}
\mathrm{FHilb}_2(\mathbb{C}) = \mathbb{P}^1 \times \mathbb{A}^1 \cup \mathbb{A}^1 \times \mathbb{A}^1 = \text{Proj} \left( \frac {\mathbb{C}[x_1,x_2,z,w]}{(x_1-x_2)w} \right)$$ $$\label{eqn:c0}
\mathrm{FHilb}_2(\mathrm{point}) = \mathbb{P}^1 = \text{Proj} \left( \mathbb{C}[z,w]\right)$$
:::
