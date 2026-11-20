**Theorem (conditional on the electroweak sector-selection postulate).**
*Let $R$ be a field with $\tfrac{1}{2} \in R$, and let $\sigma$ be the [spin involution](#def:spin-involution), acting on the two-dimensional sym/alt block of the [electroweak Hoefsmit cells](#thm:hoefsmit-ew-cell-content) as the swap $\sigma(x, y) = (y, x)$. Assume the sector-selection postulate: each electroweak carrier $c$ lies in the $\sigma$-even sector $A_+$ or the $\sigma$-odd sector $A_-$, with $H \in A_+$ (the [self-dual Higgs carrier](#prop:self-dual-higgs-real-volume)) and $W^\pm, Z \in A_-$; $c$ has carrier eigenvalue $a_c = q^{2k} \in R^\times$ with $a_c^2 \neq 1$; and $a_{W^-} = a_{W^+}^{-1}$, so that $W^-$ carries the $\sigma$-image of $W^+$. Let $v_c$ be the $\sigma$-even projection of $(a_c, a_c^{-1})$ if $c \in A_+$ and its $\sigma$-odd projection if $c \in A_-$. Define the sector label $2s(c) = 0$ if $\sigma v_c = v_c$ and $2s(c) = 2$ otherwise, and the charge $Q(c) = \mathrm{skew}(v_c)$, where $\mathrm{skew}(x, y) = x - y$ is the [$P_{\mathrm{skew}}$ functional](#prop:vdw-pskew-isolation). Then*

$$
  2s(H) = 0, \qquad 2s(W^\pm) = 2s(Z) = 2,
$$
$$
  Q(H) = 0, \qquad Q(W^+) \neq 0, \qquad Q(W^-) = -Q(W^+).
$$

*Both the sector label and the charge are computed from the action of $\sigma$ on the sector vectors $v_c$.*

The label $2s$ is a two-valued sector label of the model, named "spin" because $A_+$ is read as scalar and $A_-$ as vector; it is not a computation of Lorentz spin. The sectors $A_\pm$ are the two one-dimensional $\mathbb{Z}/2$-sectors of $\sigma$, not spin multiplets.

The theorem does not assign isospin. The paper's table $T_3(W^\pm) = \pm 1$, $T_3(Z) = T_3(H) = 0$ is recorded, not derived from $\sigma$, and it is not a function of $Q$ of the form $\lambda Q + \mu$: the row $H$ forces $\mu = 0$, the row $Z$ forces $\lambda = 0$ because $Q(Z) \neq 0$, and the row $W^+$ then fails. The normalised charge $Q(c)/Q(W^+)$ takes the values $1, -1, 0$ on $W^+, W^-, H$ and a nonzero value on $Z$. The rule of the [spin involution](#def:spin-involution), $2T_3 = 0$ on $A_+$ and $2T_3 = \pm 1$ on $A_-$, with the sign read as the sign of $Q$ over an ordered field with $a_{W^+}, a_Z > 1$, gives $2T_3(H) = 0$, $2T_3(W^\pm) = \pm 1$ and $2T_3(Z) = 1$. Each reading agrees with the table except at $Z$. In particular $T_3(H) = 0$ is a consequence of $H \in A_+$ under that rule, not an input of this theorem.

The $\sigma$-parity alone gives $Q(Z) \neq 0$, since $Z \in A_-$. Weinberg mixing does not repair this for a linear charge. Write $Z = cW^3 - sB$ and $\gamma = sW^3 + cB$ with $c^2 + s^2 = 1$, and extend $Q$ linearly from $x = Q(W^3)$ and $y = Q(B)$. Then $Q(Z)^2 + Q(\gamma)^2 = x^2 + y^2$, so $Q(Z) = Q(\gamma) = 0$ holds only if $x = y = 0$. If $W^3$ and $B$ are $\sigma$-odd sector vectors with non-degenerate eigenvalues, as the $\sigma_5^8$ grading places $B$, then $x \neq 0$ and no angle makes both $Z$ and $\gamma$ neutral. At the angle $c = \cot\theta_W \cdot s$ of the [Weinberg-angle conjecture](#conj:weinberg-angle-categorical), $Q(Z) = 0$ holds if and only if $\cot\theta_W \cdot x = y$.

*Interpretation.* In the Standard Model $W^3$ and $B$ both carry zero electric charge, and that is why $Z$ and $\gamma$ are both neutral; the rotation does not create neutrality. The model's $T_3(H) = 0$ differs from the Standard Model, where the neutral component of the Higgs doublet has $T_3 = -\tfrac{1}{2}$.
