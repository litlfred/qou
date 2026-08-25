**Proof.**

*Part 1.*
The Yang--Baxter relation $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ has the same word length on both sides ($\ell = 3$) and coefficient $1$. Applying it to a term $c \cdot w$ produces $c \cdot w'$ where $|c| = |c|$ and $\ell(w') = \ell(w)$. The same holds for far commutativity. Only the Hecke relation $\sigma_i^2 \mapsto (q - q^{-1})\sigma_i + 1$ changes the word length (from $\ell$ to $\ell - 1$) and splits one coefficient into two.

*Part 2.*
The Gröbner--Shirshov basis $G$ satisfies the Bergman diamond lemma (the main theorem of the Gröbner--Shirshov basis theory, [main theorem](#unital-groebner-bases:thm:main-theorem)). For any two overlapping reductions, the results can be further reduced to the same normal form. Because the energy is computed from the unique normal form, the energy is path-independent.

*Part 3.*
Let $c \cdot \sigma_i^2 \cdot (\text{suffix})$ be a reducible term. After applying the Hecke relation:
- One term has coefficient $c(q - q^{-1})$ and word length $\ell - 1$ (the $\sigma_i$ term).
- One term has coefficient $c$ and word length $\ell - 2$ (the identity term).
The total weight changes by $|c(q-q^{-1})| + |c| - |c| = |c| \cdot |q - q^{-1}|$.

**Substrate-internal: GS reduction over the Habiro embedding.**
*The reduction rules in $G$ (Hecke, Yang–Baxter, far commutativity) act strictly within the polynomial embedding $\mathbb{Z}[q^{\pm 1}] \hookrightarrow \widehat{\mathbb{Z}[q]}$ ([Habiro ring](#def:habiro-ring)). Confluence (the Bergman diamond lemma) is an exact algebraic consequence of the foundational triple $(\mathbf{C}, A, \tau)$. It holds in any base ring where the Hecke relation $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$ applies. In particular, it holds over the [motivic substrate](#def:motivic-substrate) before any place-realization. The energy functional $E(\xi)$ takes values in $\mathbb{Z}_{\geq 0}[q^{\pm 1}]$ as a formal Laurent polynomial. Its evaluation as a real-valued physical quantity (Skein binding energy) requires the archimedean realization $\rho_\infty$ ([archimedean realization](#def:archimedean-realization-functor)) of the substrate. This occurs downstream of the reduction itself.*

