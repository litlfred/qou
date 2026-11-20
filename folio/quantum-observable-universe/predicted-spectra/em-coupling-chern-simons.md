### Chern--Simons level from existence of the quantum observable universe

The Chern--Simons level $k$ is not an independent input. The existence proof for a quantum observable universe ([QOU existence](#prop:quantum-observable-universe-exists)) sets $q = e^{\pi i/(k + h^{\vee})}$. This makes $\mathbf{C} = \mathbf{Rep}_{k}(\widehat{\mathfrak{g}})$ the modular tensor category. This category simultaneously fixes the braiding in the Skein relation and the Chern-Simons partition function on the brane. The index $k = \langle c_{2}(\mathrm{Ad}(P)), [M] \rangle$ determines the $q$-deformation of the $q$-dimensions $[m]_{q}, [n]_{q}$ and the functional $\mathrm{CS}(T_{m, n})$ through a single Reshetikhin-Turaev construction. The numerical prediction specialises this shared object. It does not combine two independent quantities.

**Conjecture (Chern-Simons :refterm[descent]{#descent} correction, $\kappa$ unproved).**
*The fine structure constant receives corrections from the Chern–Simons invariants of the force-carrier torus knots $T_{2,9}$ and $T_{3,5}$ on Bring's surface:*

$$
  \frac{1}{\alpha_{\mathrm{EM}}}
  = q \cdot [9]_q \cdot [10]_q \cdot
    \Bigl(1 + \frac{\delta_{\mathrm{CS}}}{1 - \delta_{\mathrm{CS}}\kappa}\Bigr)
$$

*The correction tower $\sum_{j\ge1}\delta_{\mathrm{CS}}^{\,j}\kappa^{\,j-1}$ is
geometric with ratio $\delta_{\mathrm{CS}}\kappa \approx 2.7\times10^{-3}$, so it
sums in closed form and has no truncation order to choose. The
order-$\delta_{\mathrm{CS}}^2$ form $1 + \delta_{\mathrm{CS}} +
\delta_{\mathrm{CS}}^2\kappa$, which this proposition previously displayed, is its
second-order truncation and costs $11.06$ ppb.*

*where:*

$$
  \delta_{\mathrm{CS}}
  = \frac{\bigl(\mathrm{CS}(T_{2,9}) + \mathrm{CS}(T_{3,5})\bigr)
              \cdot \tfrac{[2]_q}{2} \cdot \hbar_q^2}
             {q \cdot [9]_q \cdot [10]_q}
$$

*and $\kappa = \det G_{\mathrm{CS}}^{\mathrm{cl}} / \det G_{\mathrm{CS}}^{q}$ is the Gram determinant ratio of the classical and $q$-deformed Chern–Simons pairing on Bring's surface.*

*At the proton-pinned $q_0$ with the Witten-1988 value $\kappa \approx 1.722$, $1/\alpha$ evaluates to $137.0359351$ with the tower summed to all orders. The CODATA-2022 value is $137.035999177(21)$, so the residual is $-468$ ppb. The value $\kappa = 1.722$ derives from the sketched Gram-determinant computation but was admitted as `sorry` in the Lean formalisation. It was never closed. Exact matching at this pin requires $\kappa \approx 1.9153$, which differs from the Witten value by $11.2\%$.*

*Of the two candidate causes — a wrong Gram-determinant identification of $\kappa$, or an order-$\delta_{CS}^2$ truncation omitting higher-order contributions — the second is now excluded. The tower is geometric with ratio $\delta_{CS}\kappa \approx 2.7\times10^{-3}$, so it sums in closed form as $1 + \delta_{CS}/(1-\delta_{CS}\kappa)$, and the omitted orders are worth $11.06$ ppb against a $468$ ppb gap — roughly one part in forty. Summing them makes the residual smaller but leaves it the same size. The defect is therefore $\kappa$, the quantity still carried as a `sorry`.*

*Proof sketch (does not close $\kappa$).*
The bare coupling $\alpha = q^{-1}/([9]_q \cdot [10]_q)$ arises from the antisymmetric braiding eigenvalue. This is Layer 2 of [EM coupling projection](#prop:em-coupling-projection). It is normalized by the force-carrier $q$-dimensions from Layer 3.

The correction arises from the :refterm[descent]{#descent} decomposition of the coupling endomorphism $P_{\mathrm{anti}}$ on the force-carrier configuration. The torus knots $T_{2,9}$ and $T_{3,5}$ are non-hyperbolic. Their $\tau$-image geometric invariant is the Chern–Simons functional, not the hyperbolic volume:

$$
  \mathrm{CS}(T_{m,n})
  = \frac{\pi^2 (m^2-1)(n^2-1)}{12 m n}.
$$

The factor $[2]_q/2$ is the $q$-deformation of $\mathrm{Vol}(S^3)/\mathrm{Vol}(S^3_{\mathrm{classical}})$. It replaces $\mathrm{Vol}(S^3) = 2\pi^2$ with $\mathrm{Vol}(S^3_q) = \pi^2 [2]_q$.

At order $J^2$, the Gram matrix of the Chern-Simons pairing for the configuration $(T_{2,9}, T_{3,5})$ on Bring's surface gives:

$$
  G_{\mathrm{CS}} =
  \begin{pmatrix}
    \mathrm{CS}_1 + \pi^2 s_1^2 / c_1^2
    & \pi^2 \ell^2 / (c_1 c_2) \\
    \pi^2 \ell^2 / (c_1 c_2)
    & \mathrm{CS}_2 + \pi^2 s_2^2 / c_2^2
  \end{pmatrix}
$$

where $s_i = (m_i-1)(n_i-1)$ is the self-linking, $\ell = |m_1 n_2 - m_2 n_1| = 17$ is the linking number, and $c_i = m_i n_i$ is the crossing product. The $q$-deformed version replaces $m,n$ with $[m]_q, [n]_q$.

The determinant ratio $\kappa = \det G^{\mathrm{cl}}_{\mathrm{CS}} / \det G^{q}_{\mathrm{CS}}$ --- of the $2 \times 2$ Chern--Simons pairing displayed above, **not** of the $6 \times 6$ Markov--Gram $\mathrm{tr}_M(b_i b_j)$ of [Frobenius Gram matrix](#prop:frobenius-gram-matrix), which is a different matrix and is singular under the production trace convention --- is conjectured to capture the self-dual damping at the $J^2$ level, with numerical value $\kappa \approx 1.722$. This identification is unproved. The Gram matrix is dimensionally ambiguous. Two sources of freedom were named here: the choice of basis for the rank-$2$ sublattice, and the explicit form of $s_i, \ell, c_i$ in the $q$-deformed setting. Neither survives examination as an explanation of the residual.

The first is not a source of freedom at all. Write $B$ for the change of basis. A Gram matrix transforms by congruence, $G \mapsto B^{\top} G B$, so its determinant acquires $(\det B)^2$ --- the same factor on both sides of the ratio, where it cancels. Hence $\kappa$ is independent of the basis for every invertible $B$, unimodular or otherwise, so no choice of rank-$2$ sublattice can move it (`QOU.Archimedean.gramDetRatio_congr_invariant`; confirmed numerically to $60$ digits under unimodular, index-$2$ and irrational $B$).

The second is finite, and has been enumerated. Each of $s_i$, $\ell$, $c_i$ and $\mathrm{CS}$ admits two readings of the instruction *replace $m,n$ with $[m]_q,[n]_q$* --- deform the composite, or deform its constituents --- giving $16$ combinations, of which the shipped producer is one. Evaluated at the proton pin, $\kappa$ ranges over $[-10.92, 144.61]$ and **none** of the $16$ falls inside the window $[1.8739, 1.9567]$ that would bring $1/\alpha$ within $100$ ppb. The shipped reading is the closest of the $16$, which is what selecting for closeness would produce and is therefore not evidence that it is correct. Reproduce with [`alpha_em_kappa_qdeformation_family_probe.py`](../../../computations/alpha/alpha_em_kappa_qdeformation_family_probe.py).

This is a scope-limited negative: the $[m]_q$ substitution family, *alone*, does not supply the required $\kappa$. It does not exclude a Gram-determinant $\kappa$, because a different pairing --- different matrix entries, rather than a different reading of these ones --- is untouched by the enumeration. The resulting $\kappa$ is not computed end-to-end. A direct fit to CODATA gives $\kappa \approx 1.9153$ at the proton pin with the tower resummed. The same fit at the muon pin under the order-$\delta_{CS}^2$ truncation against CODATA-2018 gives $\kappa \approx 1.8878$. Of the three explanations this paragraph has offered for the residual, two are now closed: the missing higher-order term is excluded by the resummation above, and the two named ambiguities in $\kappa$ are excluded by the paragraphs above. What survives is the third --- that the ansatz uses the wrong decomposition, so that the pairing whose determinants are being compared is not the right one. Closing $\kappa$ structurally remains an open problem. See [open problems](#rem:alpha-em-derivation-open-problems).$\square$
