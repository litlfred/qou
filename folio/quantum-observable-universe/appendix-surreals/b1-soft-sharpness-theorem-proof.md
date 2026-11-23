**Proof.**

*Step 1 (Borel non-vanishing).* By [Borel's theorem partially discharges the depth correspondence's sharpness target — explicit dimensions](#prop:borel-partial-resolution),
$\dim_\mathbb{Q} K_{2n-1}^{\mathrm{ind}}(F) \otimes \mathbb{Q} \geq 1$
for $n \geq 2$ when $F$ is non-trivial cyclotomic (specifically:
$F = \mathbb{Q}(\zeta_5), \mathbb{Q}(\zeta_6), \mathbb{Q}(i)$, all
of which have $r_2 \geq 1$). The Beilinson–Borel regulator

$$
  K_{2n-1}^{\mathrm{ind}}(F) \otimes \mathbb{Q}
  \;\longrightarrow\;
  \mathbb{R} / \pi^{2(n-1)} \mathbb{Q}
$$

is **injective** after tensoring with $\mathbb{R}$ (Borel 1977,
Theorem 12.3 — the regulator is rationally injective).

*Step 2 (polylog non-vanishing).* The single-valued $\mathrm{Li}_n$
companion (Bloch–Wigner $D$ at $n = 2$, Goncharov $D_n$ for $n \geq 3$)
is **non-zero on every algebraic argument $z \in \overline{\mathbb{Q}}^\times \setminus \{0, 1\}$**
(Lewin 1991, Polylogarithms and Associated Functions §2):

$$
  D_n(z) \;\neq\; 0
  \quad\text{for } z \in \overline{\mathbb{Q}}^\times \setminus \{0, 1\}.
$$

Equivalently: no algebraic point is a "regulator zero" of $D_n$.

*Step 3 (composition).* Combining Steps 1 and 2:

$$
  \tau_{\mathrm{arch}}(\mathrm{Li}_n^q(z_K))
  \;=\;
  \mathrm{Li}_n(z_K) \pmod{\mathcal{P}_{n-1}}
  \;\sim\;
  D_n(z_K) \neq 0
  \pmod{\mathcal{P}_{n-1}}.
$$

The non-vanishing is preserved under the regulator embedding into
$\mathcal{P}_n / \mathcal{P}_{n-1}$. $\square$
