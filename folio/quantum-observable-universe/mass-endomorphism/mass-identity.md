Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe ([quantum observable universe](#def:quantum-observable-universe)) and let $\{A_n\}_{n \geq 0}$ be its recursive brane tower ([recursive brane tower](#def:recursive-brane-tower)). Let $\mu$, $\eta$ be the multiplication and unit of the Frobenius--Hopf object $A$, let $\Delta \colon A \to A \otimes A$ be the comultiplication and let $\int_A \colon A \to \mathbf{1}$ be the Frobenius form. The **mass integrand** is the endomorphism

$$
  \Psi = (\textstyle\int_A \otimes \mathrm{id}) \circ \Delta \colon A \to A .
$$

The **inertial mass** of a morphism $\varrho \colon \mathbf{1} \to A$ (a "closed cycle" in the Frobenius--Hopf object) is the norm of the composite $\mathbf{1} \xrightarrow{\varrho} A \xrightarrow{\Psi} A \xrightarrow{\int_A} \mathbf{1}$:

$$
  \mathfrak{m}(\varrho)
  = 
  \bigl\lVert
    \textstyle\int_A \circ\, \Psi \circ \varrho
  \bigr\rVert,
$$

where $\lVert \cdot \rVert$ is the norm on $R$ induced by the Frobenius pairing ([Frobenius pairing](#def:frobenius-pairing)). The mass measures the resistance of the Frobenius--Hopf structure to transporting the cycle $\varrho$ through the comultiplication.

The composite is an element of $\mathrm{End}(\mathbf{1}) = R$, so no trace is applied. Two facts fix its value. First, $\Psi$ is left multiplication by the fixed element $u = \Psi \circ \eta$, so $\mathfrak{m}(\varrho) = \lVert \int_A (u \cdot \varrho) \rVert$. Second, when the Frobenius form is the counit $\varepsilon$, as it is for the coalgebra a Frobenius form induces, $u = \eta$ and $\Psi = \mathrm{id}_A$, so $\mathfrak{m}(\varrho) = \lVert \int_A \varrho \rVert$.

The categorical trace of the endomorphism $L_\varrho \circ \Psi$, where $L_\varrho$ is left multiplication by $\varrho$, is a different quantity. It equals $\int_A (u \cdot \varrho \cdot c)$, with $c = \mu \circ \mathrm{coev}$ the Casimir element of the self-duality of $A$. Under a fibre functor to free $R$-modules this is the regular trace of $A$, which is not a Markov trace.

**Non-abelian holonomy and Temperley–Lieb state sum.** For a word $w = [g_1, \dots, g_k]$ of segment transports $g_i \colon \mathbf{1} \to A$, the cycle is the non-abelian multiplicative integral $\varrho = \mathrm{hol}(w) = g_1 * \cdots * g_k$ in the convolution monoid $(\mathrm{Hom}(\mathbf{1}, A), *, \eta)$, satisfying $\mathrm{hol}(w_1 \mathbin{+\!+} w_2) = \mathrm{hol}(w_1) * \mathrm{hol}(w_2)$. Multiplication takes place in $\mathrm{Hom}(\mathbf{1}, A)$ before applying the linear functional $\int_A \circ \Psi$ (giving $\int_A (u \cdot \mathrm{hol}(w))$) or the categorical trace $\mathrm{tr}(L_{\mathrm{hol}(w)} \circ \Psi) = \int_A (u \cdot \mathrm{hol}(w) \cdot c)$. When $A$ acts on $V^{\otimes n}$ ($V = R^2$) via Jimbo's R-matrix $\check R$, each signed crossing transport $T(\sigma_a^{\pm 1})$ decomposes over $R$ into the identity channel and the Temperley–Lieb cup-cap generator $e_a = q \cdot 1 - \check R_a$ ($e_a^2 = (q + q^{-1}) e_a$): $T(\sigma_a) = q \cdot 1 - e_a$ and $T(\sigma_a^{-1}) = q^{-1} \cdot 1 - e_a$. Expanding the ordered holonomy product $\mathrm{Hol}(\ell_1 \cdots \ell_k) = T(\ell_1) \cdots T(\ell_k)$ over binary states $s \in \{0, 1\}^k$ expresses the Markov trace on $B_n$ as the state sum

$$
  \textstyle\int_A \rho(\beta_\ell)
  = \sum_{s \in \{0, 1\}^k} w_{\mathrm{TL}}(\ell, s) \, \textstyle\int_A \mathrm{TL}(\ell, s),
$$

where $w_{\mathrm{TL}}(\ell, s) = \bigl(\prod_{j : s_j = 0} c(\ell_j)\bigr) (-1)^{|s|}$ ($c(\sigma_a) = q$, $c(\sigma_a^{-1}) = q^{-1}$) and $\mathrm{TL}(\ell, s) = \prod_{j : s_j = 1}^{\longrightarrow} e_{a_j}$. The all-zero state $s \equiv 0$ contributes the per-crossing scalar product $\prod_{j=1}^k c(\ell_j)$, while the states $s \neq 0$ collect the Temperley–Lieb loop contractions.

**Braid classes.** When the cycle is the image $\varrho = \rho(\beta)$ of a braid $\beta$ on $n$ strands and $\int_A$ is the Jones–Markov trace, the mass is read on braid classes: braids on any number of strands modulo conjugation and positive or negative stabilisation. The trace is cyclic and is multiplied by fixed units under the two stabilisations, so its framing-corrected form

$$
  (1 + q^2)^{n} \, q^{-n - 2 w(\beta)} \textstyle\int_A \rho(\beta),
$$

with $w(\beta)$ the writhe of $\beta$, is constant on each class. This form, not the raw trace, defines the mass of a braid class. That braid classes correspond to isotopy classes of oriented links is the theorem of Alexander and Markov \cite{alexander1923, markov1936}, which names the classes and enters no statement here.

**Archimedean specialisation.** What follows spans the substrate wall. The pre-archimedean Frobenius mass is valued in the generic ground ring $R$ (the Frobenius norm $\lVert x\rVert_F = \langle x, x\rangle_F$ stays in $R$). The post-$\tau$ scalar mass is the archimedean realisation $R \to \mathbb{R}$, $x \mapsto \lVert x\rVert$, obtained by evaluating the Frobenius norm at the substrate parameter $q = q_0$. The $R \to \mathbb{R}$ realisation map inherently crosses the wall and cannot be made $\mathbb{R}$-free or generic-only. It is acknowledged here rather than splitting it off.
