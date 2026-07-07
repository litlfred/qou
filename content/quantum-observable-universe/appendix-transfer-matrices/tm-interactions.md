This appendix collects the transfer-matrix changes induced by elementary processes. An interaction changing the crossing type from $(K_1, K_2)$ to $(K_1', K_2')$ is encoded by the $\Delta$ operator:

$$
  \Delta_{K_1 K_2 \to K_1' K_2'}(q) = T_{K_1', K_2'}(q) - T_{K_1, K_2}(q)
$$

## 1. The universal beta decay matrix

The step from any nuclear crossing type to the next is always the same matrix:

$$
  \Delta_\beta(q) = T_{\mathrm{mix}}(q) - T_{nn}(q) = T_{pp}(q) - T_{\mathrm{mix}}(q) = \tfrac{1}{2}(q - q^{-1}) \mathbb{I}
$$

In explicit entries:

$$
  \Delta_\beta(q) = \begin{pmatrix} \frac{q - q^{-1}}{2} & 0 \\ 0 & \frac{q - q^{-1}}{2} \end{pmatrix}
$$

See [Table 1](#tbl:tm-interactions-table1-data). $\Delta_\beta$ is scalar, so it commutes with every transfer matrix. At $q = 1$, $\Delta_\beta = 0$ (no classical parity violation). It is universally applicable to every nucleus and converting nucleon.

## 2. Reverse beta decay ($\beta^+$)

Positron emission runs $\beta^-$ backwards, undoing the crossing-type change. Its transfer-matrix difference is the negated operator:

$$
  \Delta_{\beta^+}(q) = -\Delta_\beta(q)
$$

## 3. Photon absorption (Reidemeister I move)

Photon absorption appends a new transfer matrix factor $T_{\gamma e}$ to the chain at the absorbing generator:

$$
  M_i^{(n+1)}(q) = T_{\gamma e}(q) \cdot M_i^{(n)}(q) = T_{pp}(q) \cdot M_i^{(n)}(q)
$$

The energy change for shell $n \to n+1$ is $\Delta E_{n \to n+1} = \hat{V}(M_i^{(n+1)}) - \hat{V}(M_i^{(n)})$. For hydrogen, the transfer matrix at shell $n$ is $T_{pp}^n$, and the energy scales as $\lambda_+^n$.

## 4. Pair creation ($\gamma\gamma \to e^- e^+$)

Pair creation is a chirality-changing crossing replacement of the same form as $\beta^+$. Its transfer-matrix difference is:

$$
  \Delta_{\mathrm{pair}}(q) = T_{e^- e^+}(q) - T_{\gamma\gamma}(q) = T_{\mathrm{mix}}(q) - T_{pp}(q) = -\Delta_\beta(q)
$$

It consumes a two-photon crossing and produces a particle–antiparticle crossing. A single photon cannot pair-produce in vacuum. The matrix change equals $\beta^+$ decay.

## 5. Double beta decay ($2\beta$)

At a generator $\sigma_i$ affected by converting nucleons at positions $p_1$ and $p_2$:

$$
  \Delta M_i^{(2\beta)} = L_i \cdot \Delta_\beta \cdot C_i \cdot \Delta_\beta \cdot R_i + L_i \cdot \Delta_\beta \cdot R_i' + L_i' \cdot \Delta_\beta \cdot R_i
$$

where $C_i$ is the product of unchanged transfer matrices between the converting positions, and $L_i, R_i$ are the products to the left and right. The quadratic term is the nuclear matrix element.

## 6. Toffoli transfer matrix (information-theoretic)

On $3$ strands with nucleon types $[\mathfrak{p}, \mathfrak{p}, \mathfrak{n}]$, the Toffoli gate selects the target strand whose control--control pair has unit crossing coefficient ($c = 1$). The target-flip amplitude factors as $P_{\mathrm{flip}}(q; k_1, k_2) = c_{k_1 k_2}(q) \cdot \Phi(q)$, where $c_{k_1 k_2}$ is the control--control crossing coefficient and

$$
  \Phi(q) = \frac{(q-1)(q^{3/2} + q^{1/2} - 1)(q^{3/2} + q + 1)}{2(q+1)^2}
$$

The full $2 \times 2$ Toffoli transfer matrix $\mathbf{M}(q)$ is in [Table 2](#tbl:tm-interactions-table2-data). At generator $\sigma_1$ (one crossing), $\hat{V}_1 = z$ regardless of crossing type.

## 7. Catalogue of all $\Delta$ operators

See [Table 3](#tbl:tm-interactions-table3-data).
