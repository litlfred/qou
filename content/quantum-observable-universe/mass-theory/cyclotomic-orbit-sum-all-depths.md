**Proposition (general orbit-sum identity at every depth $n$).**

[`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general)
established the orbit sum at $n = 3$. *This proposition extends to
all depths $n \geq 2$:*

$$
  \boxed{\;
    \sum_{k = 1}^{N - 1} \mathrm{Cl}_n\!\left(\tfrac{2\pi k}{N}\right)
    \;=\;
    \begin{cases}
      \bigl(N^{1 - n} - 1\bigr)\, \zeta(n) & \text{$n$ odd}, \\[4pt]
      0 & \text{$n$ even},
    \end{cases}
  \;}
$$

*where $\mathrm{Cl}_n$ is the Glaisher Clausen function*:

- *$\mathrm{Cl}_n(\theta) = \mathrm{Re}\,\mathrm{Li}_n(e^{i\theta})$
 for $n$ odd*
- *$\mathrm{Cl}_n(\theta) = \mathrm{Im}\,\mathrm{Li}_n(e^{i\theta})$
 for $n$ even.*
