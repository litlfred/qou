**Definition (Hecke curvature 2-cocycle).**
*The Hecke algebra $H_n(R, q)$ has free-algebra generators $\sigma_1,
\ldots, \sigma_{n-1}$ subject to two relations:*

$$
  R_H(i) \;:=\; \sigma_i^{\,2} - (q - q^{-1})\,\sigma_i - \mathbf{1}, \qquad
  R_{YB}(i) \;:=\; \sigma_i \sigma_{i+1} \sigma_i - \sigma_{i+1} \sigma_i \sigma_{i+1}.
$$

*The **Hecke curvature 2-cocycle** is the 2-form-valued bilinear
map $F \in C^2(H_n(R, q), H_n(R, q))$ defined on generator pairs by:*

$$
  F(\sigma_i, \sigma_j) \;=\;
  \begin{cases}
    R_H(i) & \text{if } i = j, \\
    R_{YB}(i) & \text{if } |i - j| = 1, \\
    [\sigma_i, \sigma_j] & \text{if } |i - j| \geq 2,
  \end{cases}
$$

*and extended to general elements by the Leibniz rule
$F(ab, c) = a F(b, c) + F(a, c) b$, $F(a, bc) = F(a, b) c + b F(a, c)$.
$F$ is a $2$-cochain in the Hochschild complex
([GB spectral sequence](#prop:gb-spectral-sequence)), and on the
free algebra $\mathbb{C}\langle \sigma_1, \ldots, \sigma_{n-1}\rangle$,
$F$ measures **failure of commutativity** at each generator pair
in the same way that the curvature $F_A = dA + A \wedge A$ of a
principal connection measures failure of flatness.*
