<!-- FILE_START: substrate-cohomology-calibration-story.md -->
## The substrate, its cohomology, and the three units

The categorical framework predicts all observables from a single substrate and one deformation parameter $q_0$. Bring's curve defines the geometry of this substrate. Its first cohomology $H^1$ is eight-dimensional. Under the curve's $S_5$ symmetry, it decomposes as two copies of one irreducible four-dimensional representation, $H^1 = 2W$. This cohomology is rigid. Fixing the curve determines $H^1$ and its polarised Hodge structure. The categorical data leaves a small set of units undetermined. Measurement enters here.

A polarised, weight-one Hodge structure $2W$ has exactly three real degrees of freedom invisible to the categorical chain. Crossing the substrate-to-archimedean wall (the realisation functor $\tau$) requires supplying these degrees of freedom as units: the **scale** of the rank-two $W$-Hodge plane, its **modulus**, and a third **scale** belonging to the meson sector. The meson sector has a Hopf-link topology with zero hyperbolic volume, meaning it carries no scale derivable from the other two. These match the three calibration inputs exactly:

* **CAL-1, $m_e$**: The scale of the $W$-plane. This is the unprolonged ($n=0$) Seiberg--Witten period, the electron period. It serves as the base of the mass tower, propagating into every higher mass by the recurrence, rather than acting as a pasted prefactor.
* **CAL-2, $q_0$**: The modulus of the $W$-plane. This is the trace $\tau = 2\cosh\theta$ of the Hodge monodromy. The monodromy lies in $\mathrm{SL}_2$ because it preserves the curve's polarisation. Its determinant is one, leaving the single number $\tau$ as the modulus.
* **CAL-3, $m_\pi$**: The scale of the meson sector. This is a cohomologically orthogonal class with no hyperbolic volume, independent of $(m_e, q_0)$.

Crossing the wall also fixes a parity. A crossing has two eigenvalues, $q$ and $-q^{-1}$. Setting $\lambda = \log q$, these split as $\cosh\lambda \pm \sinh\lambda$. The symmetric $\cosh$ part represents curvature-free transport. The antisymmetric $\sinh$ part represents the curvature defect. The bar-involution $q \mapsto q^{-1}$ identifies these as the even and odd parities of one element. The binding observables (masses and their averages) sit on the $\cosh$, bar-even side, alongside the modulus $\tau$. The $\beta$-decay observable $\mathfrak{Q}_\beta$ and its precision coefficients sit on the $\sinh$, bar-odd side. These are the two parities of a single substrate element. Pinning one constrains the other. That single element is the **complex volume** $\mathfrak{V}$ ([`conj:binding-qbeta-complex-volume`](../mass-endomorphism/binding-qbeta-complex-volume.md)). Its bar-even part is $\operatorname{Re}\mathfrak{V} = \mathfrak{E}_{\mathrm{bind}}$ (the mass/binding channel). Its bar-odd part is $\operatorname{Im}\mathfrak{V} = \mathfrak{Q}_\beta$ (the decay channel), forming the QOU analogue of the Neumann--Zagier $\operatorname{Vol} + i\,\mathrm{CS}$.

A rigid cohomology fixes the structure. Three units—a scale, a modulus, and an orthogonal scale—provide the only freedom, matching the three measured calibrations. The even/odd split at the wall sorts every observable into either the mass channel or the decay channel. The remaining open numbers, the binding modulus and the decay coefficients, represent the two parities of one object. Closing one closes the other.
<!-- FILE_END: substrate-cohomology-calibration-story.md -->

<!-- FILE_START: electron-period-base.md -->
**Proposition (the electron mass is the base period of the tower).**

The prolonged Seiberg--Witten periods satisfy the one-parameter recurrence $a_D^{(n+2)} = \tau\,a_D^{(n+1)} - a_D^{(n)}$ ([`prop:sl2-prolongation-recurrence`](#prop:sl2-prolongation-recurrence)). The $n=0$ term is the unprolonged period, defined as the **electron period** $a_D^{(e)}$ ([`prop:jet-sw-tau-decomposition`](#prop:jet-sw-tau-decomposition)). Identifying $a_D^{(e)}$ with the leptonic scale $m_e$ (CAL-1) establishes the first calibration as the base of the tower. Every period is generated from the triple $(m_e,\,a_D^{(1)},\,\tau)$. The scale $m_e$ propagates into every term through the recurrence. It is not an external multiplicative prefactor.

Concretely, the $n=2$ period is $a_D^{(2)} = \tau\,a_D^{(1)} - m_e$. The electron scale appears explicitly. This reflects the cohomological role of CAL-1: the scale of the rank-2 $W$-Hodge plane, the $h^0$ datum of the archimedean realisation. The proposition's `lean.ref`, [`QOU.Mass.electron_period_is_base`](#prop:electron-period-base), proves the base identity. Its companion `QOU.Mass.second_period_contains_me` proves the $n=2$ propagation.
<!-- FILE_END: electron-period-base.md -->

<!-- FILE_START: calibration-cohomology-alignment.md -->
**Proposition (the three calibrations are the three cohomological data).**

Bring's curve has first cohomology $H^1 = 2W$, consisting of rank $8$ organized as two copies of the irreducible $4$-dimensional $S_5$ representation $W$ ([`prop:prolonged-periods-fixed-depth`](#prop:prolonged-periods-fixed-depth)). Applying the archimedean functor $\tau$ leaves exactly three real degrees of freedom in its polarised Hodge structure:

| cohomological datum | calibration | channel |
|---|---|---|
| **scale** of the rank-2 $W$-Hodge plane $= a_D^{(e)}$ | CAL-1 $m_e$ ([`prop:electron-period-base`](#prop:electron-period-base)) | $h^0$ prefactor |
| **modulus** of that plane $=$ SL$_2$ trace $\tau = 2\cosh\theta$ | CAL-2 $q_0$ ([`prop:sl2-prolongation-recurrence`](#prop:sl2-prolongation-recurrence)) | cosh / bar-even |
| **scale** of the $\operatorname{Vol}(\mathrm{Hopf})=0$ meson sector | CAL-3 $m_\pi$ | orthogonal class |

The rank-2 $W$-Hodge plane carries a scale and a modulus. The meson sector, having no geometric scale derivable from $(m_e, q_0)$ due to its zero hyperbolic volume, contributes an orthogonal scale. The count $2 + 1 = 3$ matches the three calibrations. The three calibration inputs exactly match the three undetermined cohomological data of the Bring Hodge structure. These form the choice of units forced at the substrate-to-archimedean wall.

The Lean witnesses [`QOU.Mass.calibrations_eq_cohomology`](#prop:calibration-cohomology-alignment) and `cohomology_data_count` verify this correspondence.
<!-- FILE_END: calibration-cohomology-alignment.md -->

<!-- FILE_START: bar-parity-split.md -->
**Proposition (binding and $\beta$-decay are the two bar-parities of one element).**

The bar-involution $\sigma$ defined by $q \mapsto q^{-1}$ and $\sigma^2 = \mathrm{id}$ ([`def:bar-involution`](#def:bar-involution)) splits any element $x$ into a $\sigma$-fixed even part and a $\sigma$-anti odd part:
$$
\mathrm{even}(x) = x + \sigma x, \qquad
\mathrm{odd}(x) = x - \sigma x, \qquad
\mathrm{even}(x) + \mathrm{odd}(x) = 2x.
$$

Applying this to the fibre Habiro element $F$ that controls the substrate separates the two observables:

- **even ($\cosh$, bar-symmetric)**: The binding trace $\tau = \operatorname{tr} B$ from [`prop:sl2-prolongation-recurrence`](#prop:sl2-prolongation-recurrence). This is the curvature-free transport, $(q+q^{-1})/2 = \cosh\lambda$.
- **odd ($\sinh$, bar-antisymmetric)**: The $\mathfrak{Q}_\beta$ residue-A / $c_k$ ladder. This is the curvature defect, $(q-q^{-1})/2 = \sinh\lambda$, representing the bar-odd Habiro dual of $\alpha_{\mathrm{EM}}$.

Binding (mass-average) and $\beta$-decay ($\mathfrak{Q}_\beta$) represent the even and odd parities of a single bar-graded element. Pinning either parity constrains the other. The Lean witnesses [`QOU.Mass.evenPart_add_oddPart`](#prop:bar-parity-split), `evenPart_fixed`, and `oddPart_anti` prove this decomposition.

The bar-even/bar-odd split corresponds to the real/imaginary split of the complex volume $\mathfrak{V}$ ([`conj:binding-qbeta-complex-volume`](#conj:binding-qbeta-complex-volume)). The continuation $\lambda \mapsto i\theta$ sends $\cosh\lambda \mapsto \cos\theta$ and $\sinh\lambda \mapsto i\sin\theta$. The bar-even part becomes $\operatorname{Re}\mathfrak{V} = \mathfrak{E}_{\mathrm{bind}}$ and the bar-odd part becomes $\operatorname{Im}\mathfrak{V} = \mathfrak{Q}_\beta$. The additive projections $x \mapsto x \pm \sigma x$ permit a single identity on $\mathfrak{V}$ to descend to both channels simultaneously.

Mapping this algebraic decomposition to the physical dichotomy of binding and decay provides a rigorous interpretive framework for the Quantum Observable Universe.
<!-- FILE_END: bar-parity-split.md -->

<!-- FILE_START: deuteron-binding-dressing-proton-net.md -->
**Proposition (conditional on [`conj:borromean-quark`](../observations/borromean-quark.md)).**
*Let $h = q - q^{-1}$ and $\mathfrak{E}_0 = m_e/(q(q-1))$. Let $\mathrm{net}(p) = 1 - \tfrac{h}{2}$ and $\mathrm{net}(n) = 1 - \tfrac{3h}{2} + \tfrac{h^2}{2}$ be the single-wrap normal-form net coefficients of the proton $[u,u,d]$ and neutron $[u,d,d]$ in $H_3(q)$ (from [`conj:borromean-quark`](../observations/borromean-quark.md)). For any trace difference $\Delta\mathrm{tr}$,*

$$
\mathfrak{E}_0 \cdot \mathrm{net}(p) \cdot \Delta\mathrm{tr} \;=\; \mathfrak{Q}_\beta \cdot \frac{\Delta\mathrm{tr}}{h}.
$$

*The deuteron binding functional $\mathfrak{E}_0\,(1-\tfrac{h}{2})\,\Delta\mathrm{tr}$ dresses the energy scale $\mathfrak{E}_0$ by the proton net coefficient $\mathrm{net}(p)$. This is the bar-even partner of the $\beta$-decay $Q$-value $\mathfrak{Q}_\beta$ under the single Hecke factor $h$.*

We state the context. The trace-canonical deuteron binding on the $\mathfrak{E}_0$ route over-binds by $+11.99\%$. Dressing it by $(1-\tfrac{h}{2})$ corrects it to $+0.12\%$ of AME2020 without fitted constants. The term $(1-\tfrac{h}{2})$ is exactly $\mathrm{net}(p)$.

We establish the derivation exactly in the field. The key identity is division-free:

$$
\Delta(\mathrm{net}) \;=\; \mathrm{net}(n) - \mathrm{net}(p) \;=\; -\,h \cdot \mathrm{net}(p),
$$

which holds since $(1 - \tfrac{3h}{2} + \tfrac{h^2}{2}) - (1 - \tfrac{h}{2}) = -h + \tfrac{h^2}{2} = -h(1-\tfrac{h}{2})$.
In the substrate regime $0 < h < 2$, the proton coefficient $\mathrm{net}(p) > 0$. We have $|\Delta(\mathrm{net})| = h\,\mathrm{net}(p)$. The $Q$-value ansatz $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})|\,\mathfrak{E}_0$ from [`prop:neutron-qvalue-symbolic`](../particle-interactions/neutron-qvalue-symbolic.md) yields:

$$
\mathfrak{Q}_\beta \;=\; \mathfrak{E}_0 \, h \, \mathrm{net}(p).
$$

Dividing by $h \neq 0$ and multiplying by $\Delta\mathrm{tr}$ yields the proposition. The bar-even binding dressing $\mathrm{net}(p)$ and the bar-odd $Q$-value differ by the factor $h = q - q^{-1}$. The term $h$ is itself bar-odd. This implements the bar-parity split of [`prop:bar-parity-split`](../mass-theory/bar-parity-split.md) at the deuteron.

We limit the scope. The identities are exact and formalized in `QOU.Mass.DeuteronBindingDressing`. The magnitude claim $B_D \approx \mathfrak{E}_0\,\mathrm{net}(p)\,\Delta\mathrm{tr}$ remains an observation. It accurately models the deuteron ($+0.12\%$), but does not extend to $A \geq 3$ because the extensive deficit acts as a separate mechanism. This isolates the origin of $(1-\tfrac{h}{2})$ to the proton normal-form net coefficient, linking it to the $\beta$-decay sector. The $\Delta_\lambda$ gate remains the general binding law.
<!-- FILE_END: deuteron-binding-dressing-proton-net.md -->

<!-- FILE_START: lr-coefficient-hecke.md -->
**Proposition.**
*Let $\mu \vdash n_1$, $\nu \vdash n_2$, and $\lambda \vdash n_1 + n_2$ be partitions. The **Littlewood-Richardson coefficient** $c^\lambda_{\mu\nu}$ is the multiplicity of the irreducible Iwahori-Hecke module $V_\lambda$ in the restriction:*

$$
  V_\lambda \;\downarrow_{\mathbf{H}_{n_1}(q) \otimes \mathbf{H}_{n_2}(q)} \;=\; \bigoplus_{\substack{\mu \vdash n_1 \\ \nu \vdash n_2}} c^\lambda_{\mu\nu} \cdot (V_\mu \boxtimes V_\nu)
$$

*Equivalently, $c^\lambda_{\mu\nu} = |\mathrm{LR}(\lambda/\mu, \nu)|$ counts the Littlewood-Richardson skew tableaux of shape $\lambda/\mu$ and content $\nu$ whose reverse-reading word is Yamanouchi (every prefix has $\#i \geq \#(i{+}1)$).*

*The coefficient $c^\lambda_{\mu\nu}$ is a non-negative integer. It is zero if $\mu \not\subseteq \lambda$ or $|\lambda| - |\mu| \neq |\nu|$.*

The LR coefficient gives the multiplicity of $V_\lambda$ in the outer tensor product $V_\mu \boxtimes V_\nu$ pulled back through the standard inclusion $\mathbf{H}_{n_1}(q) \otimes \mathbf{H}_{n_2}(q) \hookrightarrow \mathbf{H}_{n_1 + n_2}(q)$. This constitutes the Hecke-deformed counterpart of the classical Littlewood-Richardson rule for symmetric groups.

The operator-valued Wenzl 1988 sub-lemma 2.1 ([`prop:crystal-r-matrix-sub-lemma`](crystal-r-matrix-sub-lemma.md)) sums per $(\mu, \nu)$ block with multiplicity $c^\lambda_{\mu\nu}$:

$$
  \chi^\lambda(W_{\mathrm{inner}} \cdot I \cdot \beta_{\mathrm{block}}) = \sum_{\substack{\mu \vdash n_1 \\ \nu \vdash n_2}} c^\lambda_{\mu\nu} \cdot \mathrm{Tr}\bigl(A^\lambda_{\mu\nu}(I) \cdot (\rho_\mu(W_{\mathrm{inner}}) \otimes \rho_\nu(\beta_{\mathrm{block}}))\bigr)
$$

The LR coefficient $c^\lambda_{\mu\nu}$ provides the integer multiplicity consumed by the operator-valued combiner. The operator $A^\lambda_{\mu\nu}(I)$ acts on the $c^\lambda_{\mu\nu}$-dimensional multiplicity space.

The canonical formalism computes $c^\lambda_{\mu\nu}$ by direct LR-tableau enumeration with Yamanouchi pruning. The canonical $A=2,3,4$ atomic decompositions rely on precomputed tables. The skew-SYT primitive $f^{\lambda/\mu}$ counts all standard Young tableaux of skew shape and weights all chains. The LR coefficient $c^\lambda_{\mu\nu}$ counts only the Yamanouchi-valid semistandard Young tableaux of content $\nu$.
<!-- FILE_END: lr-coefficient-hecke.md -->

<!-- FILE_START: hecke-1d-irrep-closed-form-character.md -->
**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark)).**

*Let $n \geq 2$. Let $\beta \in B_n$ be a typed braid encoded as a sequence of crossings in $\{\sigma_i,\, \sigma_i^{-1},\, \sigma_i - h/2\cdot\mathbf{1}\}$, with $h = q - q^{-1}$. The $q$-character on each 1-dimensional irreducible representation of $H_n(q)$ obeys the universal closed form:*

$$
\boxed{
  \chi^{(n)}_q(\beta) \;=\; q^{w(\beta)} \cdot \bigl(\tfrac{[2]_q}{2}\bigr)^{m(\beta)}
  \qquad\text{and}\qquad
  \chi^{(1^n)}_q(\beta) \;=\; \bigl(-q^{-1}\bigr)^{w(\beta)} \cdot \bigl(-\tfrac{[2]_q}{2}\bigr)^{m(\beta)},
}
$$

*where:*
* $w(\beta) = \#(\sigma_i) - \#(\sigma_i^{-1})$ is the **writhe**.
* $m(\beta)$ is the number of **averaged** (operator-valued $\sigma_i - h/2$) crossings.
* $[2]_q = q + q^{-1}$ is the quantum integer.

This form is independent of $n$. The choice of 1-d irrep ($V_{(n)}$ trivial or $V_{(1^n)}$ sign) dictates the eigenvalue $\lambda_\sigma \in \{+q,\, -q^{-1}\}$.

This block operates on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at the substrate parameter $q_0$.
<!-- FILE_END: hecke-1d-irrep-closed-form-character.md -->

<!-- FILE_START: hoefsmit-V21-cos-symmetrization.md -->
**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark)).**

The 1-d Hecke irreps use the universal closed form in [`prop:hecke-1d-irrep-closed-form-character`](#prop:hecke-1d-irrep-closed-form-character). The 2-d irrep $V_{(2,1)}$ of $H_3(q)$ requires the **Hoefsmit seminormal action**:

$$
  \rho_{(2,1)}(\sigma_0) \;=\; \begin{pmatrix} q & 0 \\ 0 & -q^{-1} \end{pmatrix},
  \quad
  \rho_{(2,1)}(\sigma_1) \;=\; \begin{pmatrix} d_1 & b \\ c & d_2 \end{pmatrix},
$$

where the matrix entries derive from Hoefsmit's standard Young tableau formulas:

$$
  d_1 = \frac{q^3}{q^2 + 1}, \qquad d_2 = -\frac{q^{-1}}{q^2 + 1}, \qquad b = c = \sqrt{d_1 \cdot d_2 + 1}.
$$

Both matrices satisfy the matrix-level Hecke quadratic $M^2 = (q - q^{-1}) \cdot M + I$. The trace equals $q - q^{-1}$ and the determinant equals $-1$. Cayley-Hamilton on $\mathbb{R}^{2 \times 2}$ verifies the off-diagonal identity.

For a typed braid $\beta$ on $V_{(2,1)}$, the Markov-traced character symmetrizes over the two eigenphases of $\rho_{(2,1)}$. At leading order, the single-wrap eigenphase is

$$
  \alpha \;=\; \frac{(z - 1) \, h}{2}, \qquad z = \tfrac{1}{\sqrt q + 1/\sqrt q}, \quad h = q - q^{-1}.
$$

The symmetrized character evaluates to $\chi^{(2,1),\mathrm{symm}}_q = \mathrm{tr}\,\rho_{(2,1)}(\beta) \cdot \cos\alpha$. This cos-resummation arises from the cyclic constraint $\tau_M(xy) = \tau_M(yx)$ combined with the bar involution.

At single wrap, for any $\beta \in B_n$ with writhe $w$ and averaged-count $m$, the full Markov trace decomposes as:

$$
\boxed{
  \tau_M(\beta) \;=\; y_{(n)} \cdot \chi^{(n)}_q(\beta) \;+\; \sum_{\substack{\lambda \vdash n \\ \dim V_\lambda \geq 2}} y_\lambda \cdot \chi^{\lambda,\mathrm{symm}}_q(\beta) \;+\; y_{(1^n)} \cdot \chi^{(1^n)}_q(\beta).
}
$$

For $H_3$, $V_{(2,1)}$ is the only 2-d irrep. For $H_5$ and beyond, additional irreps appear, each requiring its Hoefsmit matrix and Markov-symmetrized cos analog.

At $q_0$, the Hoefsmit $V_{(2,1)}$ matrix entries yield $\Delta \chi^{(2,1)}_q = +0.1068144700$. The symmetrized contribution combines with the 1-d forms to give $\mathfrak{Q}_\beta = \mathfrak{Q}_\beta^A \cdot \cos((z-1)h/2)$, matching CODATA to 305 ppm at the cos-resummation level.
<!-- FILE_END: hoefsmit-V21-cos-symmetrization.md -->
