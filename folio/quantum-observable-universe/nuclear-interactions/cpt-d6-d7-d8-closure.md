**Proposition (CPT Markov-trace closure).**
*Let $R$ be a commutative ring, let $\mathcal{B}_3 = \{u, d, \bar u, \bar d\}^3 \times B_3$ be the space of flavor-decorated 3-strand signed braid words $(F, w)$, and let $W \colon \{u, d, \bar u, \bar d\}^3 \to R$ be any flavor-conjugation-symmetric color-sheet weight satisfying $W(\bar F) = W(F)$. Define the discrete actions*

1. *Charge conjugation $C(F, w) = (\bar F, w)$, exchanging $u \leftrightarrow \bar u$ and $d \leftrightarrow \bar d$ on each color sheet (carrying $(u, u, d) \leftrightarrow (\bar u, \bar u, \bar d)$ and $(u, d, d) \leftrightarrow (\bar u, \bar d, \bar d)$);*
2. *Parity $P(F, w) = (F, w^{\mathrm{mirror}})$, reflecting every crossing sign $\sigma_i^\epsilon \mapsto \sigma_i^{-\epsilon}$;*
3. *Time reversal $T(F, w) = (F, w^{\mathrm{rev}})$, reversing the crossing order of $w$;*

*and let $\tau_M(z, h, (F, w)) = W(F)\,\mathrm{tr}_M(z, h, \mathrm{eval}_h(w))$ denote the $H_3(q)$ Markov trace functional on the 6-dimensional Gröbner normal-form algebra $(H_3, \mathrm{mulNF}_h)$. Then:*

1. *Commuting $\mathbb{Z}/2 \times \mathbb{Z}/2 \times \mathbb{Z}/2$ structure:* *$C$, $P$, $T$, and $\mathrm{CPT} := C \circ P \circ T$ are exact involutions and commute pairwise.*
2. *Time-reversal anti-automorphism and fixed-$(z, h)$ invariance:* *Word reversal induces an algebra anti-automorphism $\mathrm{wordRev}_{H_3}$ of $(H_3, \mathrm{mulNF}_h)$ fixing $1, \sigma_0, \sigma_1, \sigma_0\sigma_1\sigma_0$ and exchanging $\sigma_1\sigma_0 \leftrightarrow \sigma_0\sigma_1$. Consequently both $T$ and $C$ preserve $\tau_M(z, h, \cdot)$ identically at fixed $(z, h)$ (and $\mathrm{wordRev}_{H_3}$ likewise preserves both GPMT-completed Convention-D traces).*
3. *Kazhdan–Lusztig bar isomorphism and CPT trace closure:* *The upper-triangular $R$-polynomial map $\Phi_h \colon (H_3, \mathrm{mulNF}_h) \xrightarrow{\sim} (H_3, \mathrm{mulNF}_{-h})$ sending $\sigma_i \mapsto \sigma_i + h\cdot 1$ satisfies $\mathrm{eval}_{-h}(w^{\mathrm{mirror}}) = \Phi_h(\mathrm{eval}_h(w))$ and the universal ring identity $\mathrm{tr}_M(z - h, -h, \Phi_h(v)) = \mathrm{tr}_M(z, h, v)$. Hence:*
   - *Under the bar-covariant parameter involution $(z, h) \mapsto (z - h, -h)$ — which under Convention D ($z_D(q) = q^3/(q^2 + 1)$, $h(q) = q - q^{-1}$) equals $q \mapsto q^{-1}$ via $z_D(q^{-1}) = z_D(q) - (q - q^{-1})$ — the full chiral Markov trace is invariant on every closed braid:*
     $$
       \tau_M\bigl(z - h,\, -h,\, \mathrm{CPT}(b)\bigr) \;=\; \tau_M(z, h, b),
       \qquad
       \tau_M^D\bigl(q^{-1},\, \mathrm{CPT}(b)\bigr) \;=\; \tau_M^D(q, b).
     $$
   - *At fixed $(z, h)$, each individual factor $C$, $P$, $T$, and the composite $\mathrm{CPT}$ preserves the bar-symmetrized observable Markov trace $\tau_M^{\mathrm{sym}}(z, h, b) := \tau_M(z, h, b) + \tau_M(z - h, -h, b)$.*

## Proof

Pairwise commutation and involutivity of $C$, $P$, $T$ follow from $\overline{\overline{f}} = f$, $(\sigma_i^{-\epsilon})^{-1} = \sigma_i^\epsilon$, $(w^{\mathrm{rev}})^{\mathrm{rev}} = w$, and $(w^{\mathrm{rev}})^{\mathrm{mirror}} = (w^{\mathrm{mirror}})^{\mathrm{rev}}$. Direct expansion on the six normal-form basis elements $[1, \sigma_0, \sigma_1, \sigma_1\sigma_0, \sigma_0\sigma_1, \sigma_0\sigma_1\sigma_0]$ verifies $\mathrm{wordRev}_{H_3}(\mathrm{mulNF}_h(u, v)) = \mathrm{mulNF}_h(\mathrm{wordRev}_{H_3}(v), \mathrm{wordRev}_{H_3}(u))$, and because $\mathrm{TRM}(z, h) = [1, z, z, z^2, z^2, h z^2 + z]$ assigns equal weight $z^2$ to coordinates $3$ and $4$, $\mathrm{tr}_M(z, h, \mathrm{wordRev}_{H_3}(v)) = \mathrm{tr}_M(z, h, v)$.

In $(H_3, \mathrm{mulNF}_{-h})$, the elements $\tau_i = \sigma_i + h\cdot 1$ satisfy $\tau_i^2 = (-h\sigma_i + 1) + 2h\sigma_i + h^2 = h\tau_i + 1$ and $\tau_0\tau_1\tau_0 = \tau_1\tau_0\tau_1$, giving the upper-triangular Kazhdan–Lusztig isomorphism $\Phi_h$ with columns $1$, $[h, 1, 0, 0, 0, 0]$, $[h, 0, 1, 0, 0, 0]$, $[h^2, h, h, 1, 0, 0]$, $[h^2, h, h, 0, 1, 0]$, and $[h^3 + h, h^2, h^2, h, h, 1]$. Contracting $\Phi_h(v)$ against $\mathrm{TRM}(z - h, -h)$ cancels every power of $h$ identically to yield $\mathrm{tr}_M(z, h, v)$. Under Convention D,
$$
  z_D(q) - \bigl(q - q^{-1}\bigr)
  \;=\;
  \frac{q^3 - (q - q^{-1})(q^2 + 1)}{q^2 + 1}
  \;=\;
  \frac{q^{-1}}{q^2 + 1}
  \;=\;
  z_D(q^{-1}),
$$
which gives both the bar-covariant identity $\tau_M^D(q^{-1}, \mathrm{CPT}(b)) = \tau_M^D(q, b)$ and fixed-$(z, h)$ invariance of $\tau_M^{\mathrm{sym}}(z, h, \cdot)$ under each of $C$, $P$, $T$, and $\mathrm{CPT}$. On an un-symmetrized chiral crossing $\sigma_0$ at fixed $(z, h)$, $\mathrm{tr}_M(z, h, \sigma_0 - h) - \mathrm{tr}_M(z, h, \sigma_0) = -h$, isolating the exact chiral writhe sign flip carried by $P$. $\square$

## Scope of external color-tube inputs

All Hecke-algebraic, Markov-trace, and flavor-involution statements above hold unconditionally over any commutative ring $R$ (and over any field $K$ with $q \ne 0$, $q^2 + 1 \ne 0$ for Convention D) for every conjugation-even weight $W(\bar F) = W(F)$, including the uniform projection $W \equiv 1/9$. Exhibiting the canonical geometric color-tube tensor $W_{c_1 c_2}(F_1, F_2)$ from Bring's surface fibers remains the subject of [inter-nucleon channel color tube](#conj:inter-nucleon-channel-color-tube).
