**Proof.**

*Part 1.*
The Yang--Baxter relation $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ has the same word length on both sides ($\ell = 3$) and coefficient $1$. Applying it to a term $c \cdot w$ produces $c \cdot w'$ where $|c| = |c|$ and $\ell(w') = \ell(w)$. The same holds for far commutativity. Only the Hecke relation $\sigma_i^2 \mapsto (q - q^{-1})\sigma_i + 1$ changes the word length (from $\ell$ to $\ell - 1$) and splits one coefficient into two.

*Part 2.*
The Gröbner--Shirshov basis $G$ satisfies the Bergman diamond lemma (the main theorem of the Gröbner--Shirshov basis theory, [main theorem](#unital-groebner-bases:thm:main-theorem)). For any two overlapping reductions, the results can be further reduced to the same normal form. Along a reduction path $\xi_0 \to \cdots \to \xi_m$ the step changes telescope: $\sum_{k} \bigl(E(\xi_{k+1}) - E(\xi_k)\bigr) = E(\xi_m) - E(\xi_0)$. Every path ends at the same normal form, so the total change depends only on $\xi_0$.

*Part 3.*
Let $c\,w$ with $w = u\,\sigma_i^2\,v$ of length $\ell$ be a reducible term, and suppose no other term of $\xi$ has word $u\,\sigma_i\,v$ or $u\,v$. Write $h = q - q^{-1}$. After applying the Hecke relation:
- one term has coefficient $c\,h$ and word length $\ell - 1$ (the $\sigma_i$ term);
- one term has coefficient $c$ and word length $\ell - 2$ (the identity term).

The term $c\,w$ contributed $|c|\,\ell$, so the energy changes by

$$
  |c|\,|h|\,(\ell - 1) + |c|\,(\ell - 2) - |c|\,\ell \;=\; |c|\,\bigl(|h|\,(\ell - 1) - 2\bigr).
$$

For $c = 1$, $h = 1/5$, $\ell = 2$ this is $-9/5$, so a Hecke step can lower the energy. When a new term merges with an existing one, the change also depends on that term's coefficient.

**Substrate-internal: GS reduction over the Habiro embedding.**
*The reduction rules in $G$ (Hecke, Yang–Baxter, far commutativity) act strictly within the polynomial embedding $\mathbb{Z}[q^{\pm 1}] \hookrightarrow \widehat{\mathbb{Z}[q]}$ ([Habiro ring](#def:habiro-ring)). Confluence (the Bergman diamond lemma) is an exact algebraic consequence of the foundational triple $(\mathbf{C}, A, \tau)$. It holds in any base ring where the Hecke relation $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$ applies. In particular, it holds over the [motivic substrate](#def:motivic-substrate) before any place-realization. The energy functional $E(\xi)$ is not part of this: its absolute values $|c_w(q)|$ are taken over $\mathbb{R}$, so $E$ is defined only after the archimedean realization $\rho_\infty$ ([archimedean realization](#def:archimedean-realization-functor)) of the substrate. This occurs downstream of the reduction itself.*

