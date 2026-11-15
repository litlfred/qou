---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-018-25-projective-tower-construction
section_title: "Projective tower construction"
section_number: 2.5
pages: 15-18
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.939
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:tower label="sub:tower"}

Let us consider the action: $$\mathbb{C}^* \times \mathbb{C}^* \curvearrowright \mathrm{FHilb}_n$$ which scales the matrices $X,Y$ independently. We denote the basic characters of this action by $q$ and $t$, so the $\mathbb{C}^{*} \times \mathbb{C}^*$ action is explicitly given by: $$(z_1,z_2) \cdot (X,Y) = (q(z_1) X ,t(z_2) Y), \qquad \forall \ (z_1,z_2) \in \mathbb{C}^* \times \mathbb{C}^*$$ In the matrix presentation, the tautological bundle $\mathcal{T}_n$ on $\mathrm{FHilb}_n$ has fibers consisting simply of the vector spaces $V$ on which the matrices $X,Y$ act. The fact that flag Hilbert schemes are defined as $B$--quotients means that this vector bundle need not be trivial. Therefore, the matrices $X,Y: V \rightarrow V$ give rise to endomorphisms of the tautological bundle on the whole of $\mathrm{FHilb}_n$, which we will denote by the same letters: $$q\mathcal{T}_n \stackrel{X}\longrightarrow \mathcal{T}_n, \qquad t\mathcal{T}_n \stackrel{Y}\longrightarrow \mathcal{T}_n$$ In the formulas above, one must twist the tautological bundle by the torus characters $q,t$ in order for the endomorphisms $X,Y$ to be $\mathbb{C}^* \times \mathbb{C}^*$ equivariant. Since a point of the flag Hilbert scheme entails the choice of a fixed flag of $V$, there is a full flag of tautological vector bundles: $$\mathcal{T}_n \twoheadrightarrow \mathcal{T}_{n-1} \twoheadrightarrow ... \twoheadrightarrow \mathcal{T}_1$$ on $\mathrm{FHilb}_n$. Flag Hilbert schemes are easier to work with than usual Hilbert schemes because they can be built inductively. Specifically, we have the maps: $$\label{eqn:tower}
\includegraphics{2_24.png}$$ for any $* \in \{\mathbb{C}^2, \mathbb{C}, \mathrm{point}\}$. When $* = \mathbb{C}$ we set $y_{n+1}=0$ and when $* = \mathrm{point}$ we further set $x_{n+1} = y_{n+1} = 0$. What makes [\[eqn:tower\]](#eqn:tower){reference-type="eqref" reference="eqn:tower"} manageable is that it is a **projective bundle**, so we conclude that flag Hilbert schemes are projective towers. Specifically, consider the complexes: $$\label{eqn:complex}
\includegraphics{2_25.png}$$ for any $* \in \{\mathbb{C}^2, \mathbb{C}, \mathrm{point}\}$, with the maps defined by: $$\label{eqn:psi}
\Psi(w) = \Big( - (Y-y_{n+1})w, (X-x_{n+1})w,0 \Big)$$ $$\label{eqn:phi}
\Phi(w_1,w_2,f) = (X-x_{n+1})w_1 + (Y-y_{n+1})w_2 + fv$$ Here, $x_{n+1},y_{n+1}$ are the coordinates on the second factor of $\mathrm{FHilb}_n(\mathbb{C}^2) \times \mathbb{C}^2$, which are specialized to $y_{n+1} = 0$ (resp. $x_{n+1} = y_{n+1} = 0$) when $* = \mathbb{C}$ (resp. $* = \mathrm{point}$). When $* = \mathrm{point}$, the leftmost bundle in the complex [\[eqn:complex\]](#eqn:complex){reference-type="eqref" reference="eqn:complex"} is $\mathcal{T}_{n-1}$. This implicitly uses the fact that the maps $X,Y:\mathcal{T}_n \rightarrow \mathcal{T}_n$ become nilpotent, hence they factor through $\mathcal{T}_{n} \twoheadrightarrow \mathcal{T}_{n-1}$. In the next Subsection, we will prove the following inductive description of flag Hilbert schemes ([@Negut]):

::: theorem
[]{#thm:complex label="thm:complex"} The maps $\pi$ of [\[eqn:tower\]](#eqn:tower){reference-type="eqref" reference="eqn:tower"} can be written as projectivizations: $$\label{eqn:towers}
\mathrm{FHilb}_{n+1} = \mathbb{P}\left( H^0(\mathcal{E}_n)^{\vee} \right) := \mathrm{Proj}_{\mathrm{FHilb}_n}\left(S^{\bullet} \left( H^0(\mathcal{E}_n) \right) \right)$$ This holds for each of the three variants $* \in \{\mathbb{C}^2, \mathbb{C}, \mathrm{point}\}$ of flag Hilbert schemes. The line bundle $\mathcal{L}_{n+1}$ on the left hand side coincides with the tautological sheaf $\mathcal{O}(1)$ on the right.
:::

::: example
[]{#n=1 label="n=1"}

Example [\[ex:hilb\]](#ex:hilb){reference-type="ref" reference="ex:hilb"} shows that the space $\mathrm{FHilb}_2$ can be obtained as $\mathrm{Proj}$ of an explicit algebra. Let us obtain the same result using Theorem [\[thm:complex\]](#thm:complex){reference-type="ref" reference="thm:complex"}. Since $\mathcal{T}_1=\mathcal{O}$, we have: $$\mathcal{E}_1(\mathbb{C}^2) = \left[qt \mathcal{O}\xrightarrow{(-y_1+y_2,x_1-x_2,0)} q\mathcal{O}\oplus t\mathcal{O}\oplus\mathcal{O}\xrightarrow{(x_1-x_2,y_1-y_2,1)}\mathcal{O}\right]\simeq$$ $$\simeq \left[qt \mathcal{O}\xrightarrow{(-y_1+y_2,x_1-x_2)}q\mathcal{O}\oplus t\mathcal{O}\right] \quad \Rightarrow \quad S^\bullet \left(\mathcal{E}_1 (\mathbb{C}^2)\right) = \frac{\mathbb{C}[x_1,x_2,y_1,y_2,z,w]}{(x_1-x_2)w-(y_1-y_2)z}$$ precisely as in [\[eqn:c2\]](#eqn:c2){reference-type="eqref" reference="eqn:c2"}. Here, $z$ and $w$ are the two basis vectors of $q \mathcal{O}\oplus t \mathcal{O}$. If we set $y_1 = y_2 = 0$ in the above computation, we obtain the case $* = \mathbb{C}$ of [\[eqn:c1\]](#eqn:c1){reference-type="eqref" reference="eqn:c1"}. Finally, we have: $$\mathcal{E}_1(\mathrm{point}) =\left[q\mathcal{O}\oplus t\mathcal{O}\oplus\mathcal{O}\xrightarrow{(0,0,1)}\mathcal{O}\right]\simeq \left[q \mathcal{O}\oplus t \mathcal{O}\right] \quad \Rightarrow \quad S^\bullet \left( \mathcal{E}_1(\mathrm{point}) \right) = \mathbb{C}[z,w]$$ as expected from [\[eqn:c0\]](#eqn:c0){reference-type="eqref" reference="eqn:c0"}.
:::

::: example
[]{#ex:n=2 label="ex:n=2"} Let us study Theorem [\[thm:complex\]](#thm:complex){reference-type="ref" reference="thm:complex"} in the case when $n=2$ and $* = \mathrm{point}$, in which case: $$\mathrm{FHilb}_2(\mathrm{point}) = \mathbb{P}^1$$ with respect to which we have $\mathcal{T}_1 = \mathcal{O}$ and $\mathcal{T}_2 = \mathcal{O}\oplus \mathcal{O}(1)$. With this in mind, the complex [\[eqn:complex\]](#eqn:complex){reference-type="eqref" reference="eqn:complex"} is explicitly given by: $$\mathcal{E}_2(\mathrm{point}) = \Big[ qt\mathcal{O}\stackrel{\Psi}\longrightarrow q\mathcal{O}\oplus t \mathcal{O}\oplus \mathcal{O}\oplus q \mathcal{O}(1) \oplus t\mathcal{O}(1) \stackrel{\Phi}\longrightarrow \mathcal{O}\oplus \mathcal{O}(1) \Big]$$ and the maps are given by: $$\Psi = \left( \begin{array}{c}
0 \\ 0 \\ 0 \\ -z_1 \\ z_0 \end{array} \right), \qquad \Phi = \left( \begin{array}{ccccc}
0 & 0 & 1 & 0 & 0 \\
z_0 & z_1 & 0 & 0 & 0 \end{array} \right)$$ It is clear from the above that the map $\Phi$ is surjective, which is a general phenomenon that follows from the cyclicity of triples $(X,Y,v)$. Therefore, we have: $$\mathcal{E}_2(\mathrm{point}) \stackrel{\text{q.i.s.}}\cong \Big[ qt\mathcal{O}\xrightarrow{(0,-z_1,z_0)} qt \mathcal{O}(-1) \oplus  q \mathcal{O}(1) \oplus t\mathcal{O}(1) \Big] \stackrel{\text{q.i.s.}}\cong qt\mathcal{O}(-1) \oplus \mathcal{O}(2)$$ Therefore, Theorem [\[thm:complex\]](#thm:complex){reference-type="ref" reference="thm:complex"} implies that: $$\label{eqn:pt 3}
\mathrm{FHilb}_3(\mathrm{point}) = \mathbb{P}_{\mathbb{P}^1} \left( \frac {\mathcal{O}(1)}{qt} \oplus \mathcal{O}(-2) \right)$$ which is a Hirzebruch surface. It is also the resolution of the singular cubic cone, which is nothing but the subvariety of the Hilbert scheme consisting of ideals supported at the origin.
:::

## Proving Theorem [\[thm:complex\]](#thm:complex){reference-type="ref" reference="thm:complex"} {#sub:proofcomplex}

Without loss of generality, we will treat the case $* = \mathbb{C}^2$. We will proceed by induction by $n$, by studying the fibers of the map [\[eqn:tower\]](#eqn:tower){reference-type="eqref" reference="eqn:tower"}: $$\label{eqn:mm}
\includegraphics{2_30.png}$$ Recall that points of $\mathrm{FHilb}_n(\mathbb{C}^2)$ are triples $(X,Y,v)$ consisting of two commuting lower triangular matrices (for simplicity, we fix the flag of vector spaces), together with a cyclic vector. Over such a triple, fibers of $\pi$ are completely determined by extending $X,Y,v$ by a bottom row: $$\bar{X} = \left( \begin{array}{cc}
X & 0 \\
w_1 & x_{n+1} \end{array} \right), \qquad \bar{Y} = \left( \begin{array}{cc}
Y & 0 \\
w_2 & y_{n+1} \end{array} \right), \qquad \bar{v} = \left( \begin{array}{cc}
v \\
f \end{array} \right)$$ where $w_1, w_2 \in \mathcal{T}_n^\vee$ and $f \in \mathcal{O}$. The triple $(w_1, w_2,f)$ must satisfy the following properties:

-   The closed condition $[\bar{X}, \bar{Y}] = 0$ is equivalent to: $$\label{eqn:enigma1}
    w_1 \cdot (Y - y_{n+1}) = w_2 \cdot (X - x_{n+1})$$

-   $(w_1, w_2,f)$ is only defined up to conjugation by: $$\
    V \rtimes \mathbb{C}^* = \text{Ker}(B_{n+1} \twoheadrightarrow B_n) = \left( \begin{array}{cc}
    \text{Id} & 0 \\
    w & c \end{array} \right) \qquad (w,c) \in V \rtimes \mathbb{C}^*$$ In other words, we do not consider the action of the group of $n \times n$ lower triangular matrices $B_n$ because it has already been trivialized locally on $\mathrm{FHilb}_n(\mathbb{C}^2)$. In formulas: $$\label{eqn:enigma2}
    (w_1, w_2,f) \sim \left( cw_1 + w \cdot (X-x_{n+1}),cw_2 + w \cdot (Y-y_{n+1}),cf + w \cdot v \right)$$

-   Since we already know that $(X,Y,v)$ is cyclic, the extra condition that $(\bar{X}, \bar{Y}, \bar{v})$ be cyclic is equivalent to the fact that: $$\label{eqn:equivalent}
    \mathbb{C}^{n+1} \text{ is generated by } \Big\{ \bar{v},\text{Im }(\bar{X}-x_{n+1}), \text{Im }(\bar{Y}-y_{n+1}) \Big\}$$ This fails precisely when there exists a linear functional $\lambda : \mathbb{C}^n \rightarrow \mathbb{C}$ such that: $$\lambda(v) = f, \quad \lambda \left((X-x_{n+1})w \right) = w_1 \cdot w, \quad \lambda \left((Y-y_{n+1})w \right) = w_2 \cdot w$$ for all $w \in V$. This is equivalent to $(w_1,w_2,f) \sim (0,0,0)$ with respect to [\[eqn:enigma2\]](#eqn:enigma2){reference-type="eqref" reference="eqn:enigma2"}.

::: proof
*Proof.* *of Theorem [\[thm:complex\]](#thm:complex){reference-type="ref" reference="thm:complex"}:* The three bullets above establish the fact that the triple $(w_1,w_2,f)$ that determines points in the fibers of $\mathrm{FHilb}_{n+1}(\mathbb{C}^2) \rightarrow \mathrm{FHilb}_n(\mathbb{C}^2) \times \mathbb{C}^2$ is a non-zero element in: $$\label{eqn:dualcomplex}
H^0\left( \frac {\mathcal{T}^\vee_{n}}{qt} \stackrel{\Psi^\vee}\longleftarrow \frac {\mathcal{T}^\vee_n}q \oplus \frac {\mathcal{T}_n^\vee}t \oplus \mathcal{O}\stackrel{\Phi^\vee}\longleftarrow \mathcal{T}_n^\vee \right)$$ modulo rescaling. Note that [\[eqn:dualcomplex\]](#eqn:dualcomplex){reference-type="eqref" reference="eqn:dualcomplex"} is the dual of [\[eqn:complex\]](#eqn:complex){reference-type="eqref" reference="eqn:complex"}, which completes the proof. ◻
:::

::: remark
[]{#rem:surjective label="rem:surjective"}

Note that the map $\Phi$ of [\[eqn:complex\]](#eqn:complex){reference-type="eqref" reference="eqn:complex"} is surjective, according to the equivalent description [\[eqn:equivalent\]](#eqn:equivalent){reference-type="eqref" reference="eqn:equivalent"} of a point being cyclic. This implies that $\mathcal{E}_n(*)$ is quasi-isomorphic to a complex: $$\label{eqn:two step}
\mathcal{E}_n(*) \stackrel{\mathrm{q.i.s.}}\cong \left[ qt \mathcal{T}_{n-\delta_\mathrm{point}^*} \stackrel{\Psi}\longrightarrow \text{Ker}\ \Phi \right]$$ of vector bundles on $\mathrm{FHilb}_n(*) \times *$, which lie in degrees $-1$ and $0$.
:::
