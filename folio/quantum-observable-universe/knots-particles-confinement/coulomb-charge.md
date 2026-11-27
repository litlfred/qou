Let $\mathfrak{H}$ be a knot composite with braid word $\beta$. Let $n_+(\beta)$ and $n_-(\beta)$ denote the number of positive and negative crossings in $\beta$. One defines the **Coulomb charge** of $\mathfrak{H}$ as the halved writhe:

$$
  Q(\mathfrak{H}) =  \tfrac{1}{2}\bigl(n_+(\beta) - n_-(\beta)\bigr).
$$

The crossing energy of [the crossing-energy definition](#def:crossing-energy), $\mathfrak{E}_{\mathrm{cross}} = n_+ q - n_- q^{-1}$, splits as

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  =
  \underbrace{\tfrac{1}{2}(n_+ - n_-)(q + q^{-1})}_{\text{symmetric (strong)}} +
  \underbrace{\tfrac{1}{2}(n_+ + n_-)(q - q^{-1})}_{\text{antisymmetric (Coulomb)}}.
$$

The multiplicities are not interchangeable. The symmetric $\cosh$ weight carries the crossing sign, so reversing a crossing negates it and the symmetric total is governed by the **writhe** $n_+ - n_-$. The antisymmetric $\sinh$ weight is blind to the crossing sign, contributing $+\sinh\lambda$ for a negative crossing exactly as for a positive one, so the antisymmetric total is governed by the **crossing count** $n_+ + n_-$.

**Consequences, and what $Q$ is not.** $Q$ is the coefficient of the *symmetric* channel. Under the channel identification of [the crossing-energy definition](#def:crossing-energy) — symmetric with strong binding, antisymmetric with the electromagnetic correction — the halved writhe therefore governs the strong term, and the electromagnetic coefficient is $\tfrac{1}{2}(n_+ + n_-)$, which is non-negative for every composite. Two things follow that constrain any use of $Q$ as an electric charge:

- No composite carries a negative antisymmetric coefficient, so this decomposition supplies no attractive Coulomb channel and no negative charge.
- The vanishing locus $n_+ = n_-$ annihilates the *symmetric* term, not the antisymmetric one; the antisymmetric-to-symmetric ratio diverges there rather than vanishing.

The identification of $Q$ with an electromagnetic charge is therefore not established by this decomposition. The name is retained for continuity with the blocks that cite this label. The rest of this block records what is known beyond the decomposition: the halved writhe is not the electric charge, no braid element or invariant pair coupling produces a Coulomb pair term, and what such a term requires.

**The halved writhe is not the electric charge.**

- *Quarks.* The up quark is a single positive crossing $\sigma_i$ and the down quark a single negative crossing $\sigma_i^{-1}$, so their writhes are $+1$ and $-1$ while their charges are $+\tfrac{2}{3}$ and $-\tfrac{1}{3}$. No linear map $Q = c\,w$ fits both. Under charge conjugation, which negates the charge and mirrors the braid, the mirror of the up crossing is the down crossing; the anti-up and the down then share the writhe $-1$ but carry $-\tfrac{2}{3}$ and $-\tfrac{1}{3}$, so the charge is not a function of the writhe at all.
- *Nucleons.* The proton and the neutron carry the same nucleon word $V^3 = (\sigma_i\sigma_{i+1}^{-1})^3$, which has writhe $0$; they differ only in which strands are up and down. Their charges are $1$ and $0$, so the charge is not a function of the writhe of the nucleon word, and $Q = w/2$ gives the proton charge $0$.
- *Hypercharge.* If the charge $Q$ and the isospin $I_3$ are both functions of the writhe, then so is $Y = 2(Q - I_3)$. Reading $Q = w/2$ while also reading $I_3$ as a writhe coordinate therefore leaves no hypercharge independent of the writhe: at least one of the two readings has to be given up.

**No braid element or invariant pair coupling gives a Coulomb pair term.** Place two nucleon blocks on six strands, each carrying the core $V^3 = (\sigma_i\sigma_{i+1}^{-1})^3$ on its three strands, and let $\Pi_a$ project a block onto the sector with $a$ up strands. For an insertion $X$ set

$$
  T_X(a,b) = \mathrm{Tr}\bigl(K^{\otimes 6}\,(\Pi_a \otimes \Pi_b)\,V_A^3 V_B^3\,X\bigr),
  \qquad
  \Delta E_X(a,b) = \frac{T_X(a,b)}{T_1(a,b)},
$$

with $K = \mathrm{diag}(q, q^{-1})$ and block charge $Q = a - 1$. A *Coulomb pair term* is a shift of the form $\Delta E_X(a,b) = c + \kappa\,Q_a Q_b$ with $\kappa \neq 0$; on the four nucleon pairs it vanishes whenever a neutron is involved.

1. *A single crossing, to every order.* From $\sigma^2 = h\sigma + 1$ with $h = q - q^{-1}$, every power of $\sigma$, and every finite truncation of a power series in $\sigma$, equals $a + b\sigma$. If $a + b\,\Delta E_\sigma$ has the Coulomb form with $b \neq 0$, so does $\Delta E_\sigma$. At $q = 2$ the traces are integers and $\Delta E_X$ is not of Coulomb form for $X = \sigma_2^{\pm 1}, \sigma_1\sigma_2^{-1}, \sigma_2\sigma_3^{-1}$; an identity in $q$ would hold at $q = 2$, so none of these gives a Coulomb term, at any order in the crossing.
2. *Every element at $n = 6$.* Because $T_X$ is linear in $X$, the image of the six-strand Hecke algebra decides every insertion at once. Computed exactly over the field $\mathbb{Q}(q)$, the sector responses span ten dimensions, and the only reachable affine-bilinear pair terms are $c + \kappa\,(Q_a - \beta)(Q_b - \alpha)$ with $\alpha(q) + \beta(q) = 1$ identically and $\beta(q) = \alpha(q^{-1})$. The first identity is forced by a symmetry of the readout: flipping every strand ($u \leftrightarrow d$) and reversing their order, followed by conjugation by the half twist $\sigma_i\sigma_{i+1}\sigma_i$ in each block, fixes the core and sends $(Q_A, Q_B)$ to $(1 - Q_B, 1 - Q_A)$, which maps the ray with parameters $(\alpha, \beta)$ to the ray with $(1 - \beta, 1 - \alpha)$. The Coulomb form needs $\alpha = \beta = 0$, which the identity excludes at every $q$ where the computation is defined (all but finitely many). This symmetry holds at $n = 6$ only. With one or two spectator strands between the blocks, computed exactly over $\mathbb{Q}(q)$, the reachable pair terms are $c + \kappa\,(Q_a - \beta)(Q_b - \alpha)$ with $\alpha$ equal to its six-strand value and $\beta$ free. A second symmetry covers that case: transposition composed with the flip $u \leftrightarrow d$ and $q \mapsto q^{-1}$ reverses products, sends each $\sigma_i$ to $\sigma_i^{-1}$ and fixes $K^{\otimes n}$, so it maps the ray with parameters $(\alpha(q), \beta(q))$ to the ray with $(1 - \alpha(q^{-1}), 1 - \beta(q^{-1}))$. A pinned $\alpha$ therefore satisfies $\alpha(q) + \alpha(q^{-1}) = 1$, so it is not $0$, and the Coulomb form stays excluded; together with the first identity this gives $\beta(q) = \alpha(q^{-1})$ at $n = 6$. That $\alpha$ is pinned is computed for up to four spectators ($n \le 10$), not proved for general $n$. The side matters. Strands to the right of the pair change nothing for any $n$: the weighted partial trace over them carries the readout back to six strands. A single strand to the left of the pair makes the Coulomb form reachable. The reason is local: the readout traces each strand with the weight $K$, and closing the right strand of a crossing this way leaves the scalar $q^2$, while closing the left strand leaves $\mathrm{diag}(q^2 + 1 - q^{-2}, 1)$, which counts the weight of the strand it touches. A strand to the left of a block therefore makes that block's own charge readable, which frees its parameter. That exclusion depends on the weight $K^{\otimes n}$: with the plain trace, a spectator makes the Coulomb form reachable.
3. *Invariant couplings.* The charge factor of a Gaudin or Knizhnik–Zamolodchikov coupling between the blocks is an invariant symmetric form $\Omega_{AB}$. Its weight-changing part has zero sector trace for every $q$, and its Cartan part is symmetric under the reflection $u \leftrightarrow d$, which exchanges the proton–proton and neutron–neutron sectors. A Coulomb form with equal $pp$ and $nn$ values has $\kappa = 0$. The $q$-deformed pair Casimir compatible with the braiding, and the monodromy of the connection, also give equal $pp$ and $nn$ values, as identities over $\mathbb{Q}(q)$ at $n = 6$; both are fixed by the same symmetry, which exchanges the proton pair and the neutron pair. The pair Casimir with the opposite coproduct gives unequal values; that coproduct does not commute with the braiding.
4. *Distance.* Spectator strands placed between the two blocks leave every nucleon shift exactly unchanged (measured for up to three spectators). Strand counting carries no distance, so a $1/r$ law needs a metric input that the braid and the trace do not provide.

**What a Coulomb pair term requires.** Give each strand the charge $Q = T_3 + B/2$ with baryon number $B = \tfrac{1}{3}$, so that $u \mapsto \tfrac{2}{3}$, $d \mapsto -\tfrac{1}{3}$ and a block with $a$ up strands has charge $a - 1$. In $\mathfrak{gl}(2)$ this is $Q = \tfrac{1}{2}h + \tfrac{1}{6}\cdot 1$, so $Q \otimes Q$ contains the cross term $(h \otimes 1 + 1 \otimes h)/12$, which no invariant form contains, and it separates $pp$ from $nn$. The invariant form with this Cartan shape is the unbroken neutral exchange $g^2\,T_3T_3' + g'^2\,(Y/2)(Y'/2)$, and it splits identically as

$$
  g^2\,T_3T_3' + g'^2\,\tfrac{Y}{2}\tfrac{Y'}{2}
  = e^2\,QQ' + g_Z^2\,(T_3 - s^2 Q)(T_3' - s^2 Q'),
$$

with $e^2 = g^2g'^2/(g^2+g'^2)$, $s^2 = g'^2/(g^2+g'^2)$ and $g_Z^2 = g^2 + g'^2$. If a fraction $\lambda$ of the second term is kept, the pair term on nucleon blocks has the Coulomb form if and only if $\lambda = 0$ (for $g^2 \neq 0$); no value of $s^2$ makes the second term Coulomb-shaped. Then $\kappa = e^2$, which vanishes exactly when $g'^2 = 0$. A Coulomb pair term therefore needs two inputs that the braid, the Hecke algebra and the trace do not supply: the mixing $s^2$, with a nonzero hypercharge coupling, and a mechanism that removes the second term at nuclear distance, which in the Standard Model is the mass of the $Z$. Neither is derived in this framework; the mixing angle is the subject of the Weinberg-angle conjecture of the nuclear-interactions chapter.

**Ratio.** For a positive braid closure, $n_- = 0$ with $n_+ \geq 1$, the antisymmetric-to-symmetric ratio is $\tanh(\ln q) \approx 0.104$ at $q = q_0$, independent of $n_+$. For mixed crossing signs with $n_+ \neq n_-$ it acquires the multiplicity factor $\tfrac{n_+ + n_-}{n_+ - n_-}$ and is not a constant of the framework.
