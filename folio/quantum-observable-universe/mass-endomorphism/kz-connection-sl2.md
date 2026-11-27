Let $V = \mathbb{C}^2$ be the fundamental representation of $\mathfrak{sl}_2$ with basis $e, f, h$, and let $\Omega = e \otimes f + f \otimes e + \tfrac{1}{2}\, h \otimes h$ be the split Casimir. For $n \geq 2$ let $X_n = \{(z_1, \dots, z_n) \in \mathbb{C}^n : z_i \neq z_j \text{ for } i \neq j\}$ be the configuration space of $n$ distinct points, and for $i < j$ let $\Omega_{ij}$ be $\Omega$ acting in tensor slots $i$ and $j$ of $V^{\otimes n}$.

The **Knizhnik--Zamolodchikov connection** with coupling $\lambda \in \mathbb{C}$ is the connection on the trivial bundle $X_n \times V^{\otimes n}$ given by

$$
  \nabla = d - \lambda\, \omega,
  \qquad
  \omega = \sum_{i<j} \Omega_{ij}\, d\log(z_i - z_j).
$$

A logarithmic connection $\omega = \sum_{i<j} M_{ij}\, d\log(z_i - z_j)$ is **flat** if $d\omega - \omega \wedge \omega = 0$.
