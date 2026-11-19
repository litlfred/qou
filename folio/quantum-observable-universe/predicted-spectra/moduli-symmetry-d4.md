The two natural involutions on the aether moduli line $\mathbb{C}^\times$,

$$
  \sigma\colon q \mapsto iq
  \qquad\text{(complex rotation by $\pi/2$)},
  \qquad
  \tau\colon q \mapsto q^{-1}
  \qquad\text{(Hecke bar involution)},
$$

generate a faithful action of the dihedral group of order 8:

$$
  D_4
   =  \langle\,\sigma,\,\tau \;\mid\; \sigma^4 = \tau^2 = (\sigma\tau)^2 = 1\,\rangle.
$$

The relation $(\sigma\tau)^2 = 1$ enforces the dihedral commutation $\tau\sigma\tau = \sigma^{-1}$. Verification:

$$
  \tau\sigma\tau(q)
   =  \tau(\sigma(q^{-1}))
   =  \tau(iq^{-1})
   =  (iq^{-1})^{-1}
   =  -iq
   =  \sigma^{-1}(q).
$$

**The golden octet.**

The $D_4$-orbit of $\varphi$ in $\mathbb{C}^\times$ forms the golden octet:

$$
  G_8
   :=  D_4 \cdot \varphi
   =  \bigl\{\,\varphi,\;i\varphi,\;-\varphi,\;-i\varphi,\;
              1/\varphi,\;i/\varphi,\;-1/\varphi,\;-i/\varphi\,\bigr\}.
$$

The eight elements partition by stabilizer into two cosets:

| Coset | Elements | Generator | Real / imaginary |
|-------|----------|-----------|------------------|
| $\sigma\langle 1\rangle$-orbit through $\varphi$ | $\{\varphi, i\varphi, -\varphi, -i\varphi\}$ | $\sigma^k \cdot \varphi$ | real (golden quartet $Q_+$) plus imaginary axis |
| $\sigma\langle 1\rangle$-orbit through $1/\varphi$ | $\{1/\varphi, i/\varphi, -1/\varphi, -i/\varphi\}$ | $\sigma^k \cdot 1/\varphi$ | bar-image of $Q_+$, by $\tau$ |

The intersection $G_8 \cap \mathbb{R}$ recovers the golden quartet
$Q = \{\,\varphi,\,-\varphi,\,1/\varphi,\,-1/\varphi\,\}$
([golden-quartet Galois orbit](#prop:golden-quartet-galois)).
The intersection $G_8 \cap i\mathbb{R}$ recovers its $\pi/2$-rotation
$iQ = \{\,i\varphi,\,-i\varphi,\,i/\varphi,\,-i/\varphi\,\}$.

Equivalently, the octet contains the eight roots of

$$
  P_{\mathbb{C}}(z)  :=  P(z) \cdot P(z/i)
   =  (z^4 - 3z^2 + 1)(z^4 + 3z^2 + 1)
   =  z^8 - 7z^4 + 1
$$

over $\mathbb{Q}(i)$, where $P(z) = z^4 - 3z^2 + 1$ is the quartic of the golden quartet.
