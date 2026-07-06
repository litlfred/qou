**Proposition (Golden quartet as Galois $\times$ bar orbit).**
The golden quartet

$$
  Q  :=  \bigl\{\,1/\varphi,\;-\varphi,\;\varphi,\;-1/\varphi\,\bigr\}
$$

is the complete root set of the quartic polynomial

$$
  P(x)  :=  x^4 - 3x^2 + 1
   =  (x^2 - x - 1)(x^2 + x - 1)
$$

over $\mathbb{Q}$. Under the Galois action of $\mathrm{Gal}(\mathbb{Q}(\sqrt{5})/\mathbb{Q}) = \langle \tau \rangle \cong \mathbb{Z}/2$ (with $\tau \colon \sqrt{5} \mapsto -\sqrt{5}$), the quartet splits into two orbits:

$$
  Q_+  :=  \{\,\varphi,\;-1/\varphi\,\}
  \;=\;\mathrm{Gal\text{-orbit}\ of\ }\varphi
  \;=\;\mathrm{roots\ of\ }x^2 - x - 1,
$$

$$
  Q_-  :=  \{\,1/\varphi,\;-\varphi\,\}
  \;=\;\mathrm{Gal\text{-orbit}\ of\ }1/\varphi
  \;=\;\mathrm{roots\ of\ }x^2 + x - 1.
$$

The bar involution $\iota \colon x \mapsto x^{-1}$ on $\mathbb{R}^\times$ exchanges these orbits:

$$
  \iota(Q_+) = Q_-,\qquad \iota(Q_-) = Q_+.
$$

The joint group $G := \mathrm{Gal}(\mathbb{Q}(\sqrt{5})/\mathbb{Q}) \times \langle\iota\rangle \cong \mathbb{Z}/2 \times \mathbb{Z}/2$ therefore acts transitively and faithfully on $Q$.
