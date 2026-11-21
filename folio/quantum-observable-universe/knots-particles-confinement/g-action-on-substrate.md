The proposal is that the Frobenius–Hopf substrate $A$ in $\mathbf{Rep}(\mathrm{SU}_q(2))$ admits a unique $G$-equivariant structure under $G = \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$. This structure is governed by four constraints linking the categorical data to the electroweak sector. The constraints are intended to give the symmetric-channel Frobenius trace $\mathcal{N}_{\rm sym}(q) = \mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$ in closed form. The closed form depends on how the trace composes across the hosts, which is not yet fixed (see below).

### The four constraints

**Constraint (G-1) — $G$-isotypic decomposition.**
The substrate $A$ decomposes as a direct sum of $G$-isotypic components:

$$
  A \;=\; A^{(\gamma)} \;\oplus\; A^{(W^+)} \;\oplus\; A^{(W^-)}
  \;\oplus\; A^{(Z)} \;\oplus\; A^{(H)} \;\oplus\; A^{(\rm matter)}
$$

where each $A^{(X)}$ carries a unique irreducible representation of $G$. See [Table 1](#tbl:g-action-on-substrate-table1-data).

**Constraint (G-2) — Per-host $q$-dimension assignment.**
The categorical $q$-dimension of each component is determined by its torus-link host:

$$
  \dim_q\bigl(A^{(W^\pm)}\bigr) \;=\; [4]_q,
  \qquad
  \dim_q\bigl(A^{(Z)}\bigr) \;=\; [6]_q,
  \qquad
  \dim_q\bigl(A^{(H)}\bigr) \;=\; [2]_q.
$$

The $W$-host scale $[4]_q$ reflects the $T(2,4)$ crossing count, and the $Z$-host scale $[6]_q$ reflects $T(2,6)$. The Higgs scale $[2]_q$ is the $q$-dimension of the fundamental representation, restricted to the neutral component.

**Constraint (G-3) — Higgs vacuum vortex morphism.**
The Higgs vacuum value $\langle\Phi\rangle \in A$ is a non-zero vortex morphism $\varrho_\Phi \colon \mathbf{1} \to A^{(H)}$, unique up to a non-zero scalar, satisfying

$$
  Q \cdot \varrho_\Phi = 0, \qquad
  \mathrm{tr}_F(\varrho_\Phi^* \cdot \varrho_\Phi) = v^2 / m_e^2,
$$

where $Q = T_3 + Y$ is the unbroken charge generator and $v \approx 246\,\mathrm{GeV}$ is the weak vacuum expectation value. The first condition forces neutrality under the unbroken $\mathrm{U}(1)_{\text{em}}$ and, when the neutral subspace of $A^{(H)}$ is one-dimensional, fixes $\varrho_\Phi$ up to a non-zero scalar. The second fixes the modulus of that scalar to the empirical Higgs VEV and leaves its phase free, so $\varrho_\Phi$ is unique only up to a phase. The idempotent $e_H$ of (G-4) does not depend on that phase.

**Constraint (G-4) — Higgs idempotent.**
The categorical Higgs idempotent $e_H$ is defined from $\varrho_\Phi$ by:

$$
  e_H \;=\; \frac{\varrho_\Phi \cdot \varrho_\Phi^*}{\mathrm{tr}_F(\varrho_\Phi^* \cdot \varrho_\Phi)}.
$$

This rank-1 projector isolates the unbroken 1-dimensional subspace of $A^{(H)}$. Its trace is

$$
  \mathrm{tr}_F(e_H) \;=\; 1.
$$

The idempotent factors through the monoidal unit: $e_H = \varrho_\Phi \circ \bigl(t^{-1}\varrho_\Phi^*\bigr)$ with $t = \mathrm{tr}_F(\varrho_\Phi^* \cdot \varrho_\Phi)$, and $\varrho_\Phi^* \cdot \varrho_\Phi = t \cdot \mathrm{id}_{\mathbf{1}}$. Cyclicity of the trace gives $\mathrm{tr}_F(e_H) = \mathrm{tr}_F(\mathrm{id}_{\mathbf{1}})$, which is $1$ for a unit-normalised cyclic trace. The value $[2]_q$ of (G-2) is the $q$-dimension of all of $A^{(H)}$, not the trace of its rank-one image.

### The closed form for $\mathcal{N}_{\rm sym}(q)$

Writing
$\mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$ as $\dim_q$ of the image of $e_{\rm sym}^{\rm EW}$ on $A^{(W^+)} \oplus A^{(W^-)} \oplus A^{(Z)}$ times $\dim_q(e_H \cdot A^{(H)})$, and then multiplying the per-host dimensions, is not justified, for two reasons.

1. *$q$-dimension is additive over direct sums and multiplicative over tensor products.* (G-1) makes $A^{(W^+)}$, $A^{(W^-)}$, $A^{(Z)}$ and $A^{(H)}$ direct summands of $A$, so the $q$-dimension of their direct sum is the sum of the per-host values, not their product.
2. *The trace of a composite of idempotents is not in general a product of traces.* If $e_{\rm sym}^{\rm EW}$ and $e_H$ are idempotents of $A$ supported on the orthogonal summands of (G-1), then $e_{\rm sym}^{\rm EW} \cdot e_H = 0$. A non-zero value of $\mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$ therefore needs the two idempotents to act on different tensor factors, which (G-1) does not supply.

The corpus does not settle which object is meant. Two readings are recorded, and neither is selected.

- **Reading (a), tensor product.** The electroweak host is $A^{(W^+)} \otimes A^{(W^-)} \otimes A^{(Z)}$, the Higgs host $A^{(H)}$ is a further tensor factor, and $\mathrm{tr}_F$ is multiplicative on $e_{\rm sym}^{\rm EW} \otimes e_H$. Then, with (G-2) and (G-4),

$$
  \mathcal{N}_{\rm sym}^{(a)}(q)
  \;=\;
  [4]_q \cdot [4]_q \cdot [6]_q \cdot 1
  \;=\;
  [4]_q^2 \, [6]_q.
$$

This reading needs a tensor structure on the hosts that (G-1) does not state.

- **Reading (b), direct sum, as (G-1) states.** The $q$-dimension of the symmetric-channel image is additive over the summands:

$$
  \dim_q\!\bigl(e_{\rm sym}^{\rm EW}\bigl[A^{(W^+)} \oplus A^{(W^-)} \oplus A^{(Z)}\bigr]\bigr)
  \;=\;
  2\,[4]_q + [6]_q,
$$

taking $e_{\rm sym}^{\rm EW}$ to act as the identity on each host, as (G-2) assumes. Keeping the outer factor $\dim_q(e_H \cdot A^{(H)}) = \mathrm{tr}_F(e_H) = 1$ gives $\mathcal{N}_{\rm sym}^{(b)}(q) = 2\,[4]_q + [6]_q$. By point 2 this is not $\mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$. It is the $q$-dimension of the symmetric-channel image, and the composition rule that would turn it into the trace is not specified.

- **What the trace algebra decides.** For any additive, cyclic, unit-normalised trace, the composite reading of $\mathrm{tr}_F(e_{\rm sym}^{\rm EW}\cdot e_H)$ is a vacuum expectation value. Because $e_H$ factors through $\mathbf{1}$, $\mathrm{tr}_F(f\circ e_H) = t^{-1}\langle\varrho_\Phi^*, f\,\varrho_\Phi\rangle$ for every endomorphism $f$ of the host of $e_H$. When $f$ is an idempotent commuting with $e_H$ this value is $0$ or $1$, and it is $0$ when $f$ and $e_H$ live on different summands. The dimension of the electroweak host never enters. A $q$-dimension-valued $\mathcal{N}_{\rm sym}$ therefore needs the product to be the tensor product $e_{\rm sym}^{\rm EW}\otimes e_H$, on a tensor power of $A$ rather than on $A$, and then $\mathcal{N}_{\rm sym} = \mathrm{tr}_F(e_{\rm sym}^{\rm EW})$. The trace is additive on direct sums and multiplicative on tensor products, so it cannot decide between (a) and (b): that is a question about the host object.
- **What the rest of the corpus fixes.** Neither reading matches the host structure used elsewhere. In the [Hoefsmit realisation](#thm:hoefsmit-ew-cell-content) and in [weak spectral completeness](#prop:weak-spectral-completeness), distinct carriers are tensor factors: $W$, $Z$ and $T(2,8)$ act on disjoint strand pairs, in $H_2(q)^{\otimes 3} \subset H_6(q)$. There is a single $W$ slot. The [charge–spin theorem](#thm:ew-triplet-charge-spin-from-involution) gives $W^-$ the swap-image $a_{W^-} = a_{W^+}^{-1}$, so the two sector vectors are negatives of each other and span one line. $W^+$ and $W^-$ are therefore neither two tensor factors, as (a) assumes, nor two independent summands, as (b) counts. [Table 1](#tbl:g-action-on-substrate-table1-data) agrees, listing them as the $T^\pm$ weight spaces of one adjoint. Taking (G-2) and (G-4) as given, this structure gives $[4]_q\,[6]_q \approx 26.25$ at $q_0$, conditional on [the torus-link identification](#conj:electroweak-higgs-torus-link-triplet). It does not justify (G-2) itself: the slot object is $V \otimes V$ with $\dim_q = [2]_q^2 = [3]_q + 1$, while $[4]_q$ and $[6]_q$ are $\dim_q V_{3/2}$ and $\dim_q V_{5/2}$, which are not among the representations of Table 1. They come from crossing counts, not from a $q$-dimension the corpus derives.

The factor $1$ in both readings is (G-4): $e_H$ factors through $\mathbf{1}$ ([the Higgs vacuum-residual idempotent](#prop:higgs-vacuum-residual-idempotent)). The host labels $T(2,4)$ and $T(2,6)$ of (G-2) come from [the electroweak/Higgs torus-link identification](#conj:electroweak-higgs-torus-link-triplet), which is itself a conjecture. See [Table 2](#tbl:g-action-on-substrate-table2-data).

### The value on the strand-pair slots

Suppose the hosts of (G-1) are the strand pairs of the [Hoefsmit realisation](#thm:hoefsmit-ew-cell-content): $W$, $Z$ and $H$ act on the strand pairs $(1,2)$, $(3,4)$, $(5,6)$ of $V^{\otimes 6}$, with carriers $\sigma_1^4$, $\sigma_3^6$, $\sigma_5^8$. Call this hypothesis (H1). The labels $W$, $Z$, $H$ come from [the torus-link identification](#conj:electroweak-higgs-torus-link-triplet), so (H1) is conditional on that conjecture, and (G-1) as stated, a direct sum, does not imply it. Under (H1) and a choice of trace, stated in step 3, the value of $\mathcal{N}_{\rm sym}$ is forced:

1. Each carrier $\sigma_i^{2k}$ has exactly the two eigenvalues $q^{2k}$ and $q^{-2k}$, and its spectral projectors are the projectors $e^{+}$, $e^{-}$ of $\sigma_i$ itself, for every $k$. So $e_{\rm sym}^{\rm EW}$ is $e^{+}$ on the $W$ and $Z$ slots.
2. By (G-3), $e_H$ factors through $\mathbf{1}$. On a slot $V \otimes V$ the invariant line is the $-q^{-1}$ eigenline of $\sigma_5$, which is one-dimensional, so $e_H = e^{-}(\sigma_5)$, with $\mathrm{tr}_F(e_H) = 1$ as (G-4) requires. The identification of the invariants with that eigenline is quantum Schur–Weyl duality \cite{jimbo1986}.
3. Take $\mathrm{tr}_F$ to be a multiple of the pivotal trace; call this (H4). A general cyclic trace takes independent values on $e^{+}$ and $e^{-}$, and $\mathrm{tr}_F(e_H) = 1$ fixes only the value on $e^{-}$. Under (H4) that condition selects the unnormalised pivotal trace, whose Markov parameter is $q^3/(q^2+1)$.
4. On $V^{\otimes 6}$ the composite $e_{\rm sym}^{\rm EW} \cdot e_H$ is the tensor product $e^{+} \otimes e^{+} \otimes e^{-}$, and the trace is multiplicative over slots.

Since $\mathrm{tr}_F(e^{+}) = [3]_q$ on each slot,

$$
  \mathcal{N}_{\rm sym}(q) \;=\; [3]_q^2, \qquad \mathcal{N}_{\rm sym}(q_0) \approx 9.2641 .
$$

This is none of readings (a) and (b) and differs from the slot value $[4]_q\,[6]_q$ above, which took (G-2) as given. Under (H1), (G-2) does not hold: the symmetric image of every carrier is the adjoint $V_1$, of $q$-dimension $[3]_q$ for each $k$, which is the adjoint of [Table 1](#tbl:g-action-on-substrate-table1-data), and not $V_{k-1/2}$ of $q$-dimension $[2k]_q$. The idempotent $e_H = e^{-}(\sigma_5)$ is the alternating eigenprojector, whereas [the torus-link identification](#conj:electroweak-higgs-torus-link-triplet) places $H$ in the bar-even part $A_+$ of $\sigma_5^8$, a grading component rather than a spectral projector; the two descriptions are not reconciled.

### The anchor value is not a host trace

The anchor value $\mathcal{N}_{\rm sym}(q_0) \approx 213.11$ is defined as $N_v / \prod_{k=2,3,4} [2k]_q^2/[2]_q$, with $N_v = v/(E_\times \mu_0)$. Since the electron [trefoil](#rem:building-block-knots) has three crossings, $m_e = 3\,E_\times \mu_0$, so this $N_v$ is $v$ counted in crossings, $3v/m_e$. Writing it through the weak scale $v/m_p$ of [the torus-link identification](#conj:electroweak-higgs-torus-link-triplet) gives the identity

$$
  \mathcal{N}_{\rm sym}^{\rm anchor} \;=\; 3\,\frac{m_p}{m_e}\cdot\frac{v}{m_p}\cdot\frac{[2]_q^3}{\bigl([4]_q\,[6]_q\,[8]_q\bigr)^2}.
$$

The factor $3\,m_p/m_e \approx 5508$ is the proton mass counted in crossings; the remaining factor is $\approx 0.03869$. When $m_p/m_e$ is the model function of the proton pin, $2\,\mathrm{Vol}(4_1)\,F_{\rm Bor}/\hbar_q^2 - 12$, it has a double pole at $q = 1$, and so does $\mathcal{N}_{\rm sym}^{\rm anchor}$. Every $q$-dimension in $\mathbf{Rep}_q(\mathrm{SU}(2))$ is a non-negative integer combination of $q$-integers and is finite at $q = 1$. So no host trace equals the anchor as a function of $q$, and agreement at the single point $q_0$ would be a coincidence of evaluation, not an identification. If $m_p/m_e$ is instead treated as a constant, the weaker statement remains: the anchor carries a factor that is not a weak-sector quantity. The comparison of host values with $213.11$ is therefore not a test of any reading, including the value $[2]_q\,[4]_q^2\,[6]_q \approx 216.96$, which uses the $q$-dimension of $A^{(H)}$ in place of $\mathrm{tr}_F(e_H)$. [Table 2](#tbl:g-action-on-substrate-table2-data) lists the host values.
