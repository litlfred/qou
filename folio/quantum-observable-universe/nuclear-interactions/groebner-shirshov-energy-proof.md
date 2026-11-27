*Part 1.*
The Yang--Baxter relation $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ has the same word length on both sides ($\ell = 3$) and coefficient $1$. Applying it to a term $c \cdot w$ produces $c \cdot w'$ where $|c| = |c|$ and $\ell(w') = \ell(w)$. The same holds for far commutativity, and for every rule of the Bokut--Shiao family $\sigma_i\sigma_{i-1}\cdots\sigma_j\sigma_i \mapsto \sigma_{i-1}\sigma_i\sigma_{i-1}\cdots\sigma_j$, whose two sides have equal length and coefficient $1$. Only the Hecke relation $\sigma_i^2 \mapsto (q - q^{-1})\sigma_i + 1$ changes the word length (from $\ell$ to $\ell - 1$ and $\ell - 2$) and splits one coefficient into two.

*Part 2.*
The Gröbner--Shirshov basis $G$ (the Hecke relation, far commutativity, and the Bokut--Shiao family; [Hecke normal form](#def:hecke-normal-form)) satisfies the Bergman diamond lemma (the main theorem of the Gröbner--Shirshov basis theory, [main theorem](#unital-groebner-bases:thm:main-theorem)). For any two overlapping reductions, the results reduce to the same normal form. Along a reduction path $\xi_0 \to \cdots \to \xi_m$ the step changes telescope: $\sum_{k} \bigl(E(\xi_{k+1}) - E(\xi_k)\bigr) = E(\xi_m) - E(\xi_0)$. Every path ends at the same normal form, so the total change depends only on $\xi_0$.

*Part 3.*
Let $c\,w$ with $w = u\,\sigma_i^2\,v$ of length $\ell$ be a reducible term, and suppose no other term of $\xi$ has word $u\,\sigma_i\,v$ or $u\,v$. Write $h = q - q^{-1}$. After applying the Hecke relation:
- one term has coefficient $c\,h$ and word length $\ell - 1$ (the $u\,\sigma_i\,v$ term);
- one term has coefficient $c$ and word length $\ell - 2$ (the $u\,v$ term).

The term $c\,w$ contributed $|c|\,\ell$, so by disjoint-support additivity of the finite-support sum and direct algebraic simplification the norm changes by

$$
  \bigl(|c|\,|h|\,(\ell - 1) + |c|\,(\ell - 2)\bigr) - |c|\,\ell \;=\; |c|\,\bigl(|h|\,(\ell - 1) - 2\bigr).
$$

For $c = 1$, $h = 1/5$, $\ell = 2$ this evaluates to $-9/5 < 0$, so a Hecke step can lower $E$. When a new term merges with an existing one, the change also depends on that term's coefficient.

*Part 4.*
Over any commutative ring $R$, let $\tau \colon M \to R$ be an $R$-linear map on an $R$-module $M$. Whenever $w_{\mathrm{sq}} = h \cdot w_{\mathrm{lin}} + w_{\mathrm{id}}$, $R$-linearity gives $\tau(w_{\mathrm{sq}}) = h\,\tau(w_{\mathrm{lin}}) + \tau(w_{\mathrm{id}})$. Substituting $\tau(1) = 1$, $\tau(\sigma_i) = z$, and $\tau(\sigma_1\sigma_2) = z^2$ yields $\tau(\sigma_i^2) = h\,z + 1$ and $\tau(\sigma_1^2\sigma_2) = h\,z^2 + z = z\,(1 + h\,z)$; by trace cyclicity $\tau(\sigma_1\sigma_2\sigma_1) = \tau(\sigma_1^2\sigma_2) = z\,(1 + h\,z)$.

**Substrate-internal: GS reduction over the Habiro embedding.**
*The reduction rules in $G$ (Hecke, far commutativity, and the Bokut--Shiao family, which contains Yang--Baxter) act strictly within the polynomial embedding $\mathbb{Z}[q^{\pm 1}] \hookrightarrow \widehat{\mathbb{Z}[q]}$ ([Habiro ring](#def:habiro-ring)). Confluence (the Bergman diamond lemma) and the skein trace invariance of Part 4 hold over any commutative ring where the Hecke relation $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$ applies, and in particular over the [motivic substrate](#def:motivic-substrate) before any place-realization. The word-length functional $E(\xi)$ is distinct: its absolute values $|c_w(q)|$ are taken over $\mathbb{R}$, so $E$ is defined only after the archimedean realization $\rho_\infty$ ([archimedean realization](#def:archimedean-realization-functor)) of the substrate.*
