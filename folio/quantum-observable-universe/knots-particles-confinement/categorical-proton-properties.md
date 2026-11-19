The proton definition establishes the $\mathcal{B}_3(\mathfrak{u},\mathfrak{u},\mathfrak{d})$ baryon. We derive its normal form, mass, Coulomb charge, and computational backing.

**Step 1: Borromean braid NF.**
The inverse relation $\sigma_1^{-1} = \sigma_1 - h_{\mathrm{A}} \mathbf{1}$ yields $\mathcal{B}_3 = (\sigma_0(\sigma_1 - h_{\mathrm{A}}))^3$. Expanding and reducing within $H_3(q)$ gives $\mathrm{net}(\mathcal{B}_3) = +1.0000$. The Hopf link terms $L_\pm$ manifest the gluon field.

**Step 2: Typed crossings.**
Quark flavor rigidly specifies the crossing eigenvalue. The $\mathfrak{u}$-$\mathfrak{u}$ crossing preserves the eigenvalue $+q$. The $\mathfrak{d}$-type crossings impose a full $-h_{\mathrm{A}}$ shift. Mixed $\mathfrak{u}$-$\mathfrak{d}$ crossings incur a half-shift $-\tfrac{1}{2}h_{\mathrm{A}}$.

**LP stability constraint.** *(Partly withdrawn 2026-08-24.)*

~~The bare 9-crossing element $\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$ violates Frobenius positivity. A single Hopf link $L_- = \sigma_1\sigma_0$ is the minimum additional structure capable of restoring stability. The gluon is strictly required by the LP dual.~~

Those three sentences rest on $\mathrm{tr}_M(e^-) = z^3$, a weight retired on 2026-05-19 in favour of the Markov-recursion value $h z^2 + z$. Under the live convention the bare element has $\mathrm{tr}_M = +0.544$, not $-0.006$, and so does every intermediate step of the typed build. There is no instability for a gluon to repair, and the bare nucleon lies inside the feasible set. Whether the gluon is required on some other ground is open; the [gluon ledger](#rem:gluon-stabiliser-ledger) carries the measurement.

What survives unchanged is the *scope* of the enumeration. The integer LP dual enumerates all feasible gluon combinations and selects the configuration minimizing $|\mathrm{tr}_M|$. That enumeration ranges over every non-trivial braid word inside the crossing cap, not over $L_\pm$ alone. The trefoil word $e^- = \sigma_0\sigma_1\sigma_0$ is inside the range and is admissible; it is not selected because it loses the minimisation, not because anything forbids it ([gluon ledger](#rem:gluon-stabiliser-ledger)).

**Step 3: Proton NF.**
Applying typed crossings and Hopf link stabilisation yields $\mathrm{net}(\mathfrak{p}) = +1.0065$. The dominant term is $e^- \approx +1.022$. The Hopf gluon link actively redistributes normal-form weight from $\sigma_1$ into the trefoil channel.

**Mass.**
The proton mass derives from the muon-anchored Hecke energy of the Borromean braid:

$$
  \mathfrak{m}_{\mathfrak{p}} =
  2\,\bigl(\mathfrak{m}_\mu F_{\mathrm{Bor}} - 6\, m_e\bigr)
  + \text{Skein corrections},
  \qquad
  \mathfrak{m}_\mu = m_e\,\frac{\mathrm{Vol}(4_1)}{\hbar_q^2},
  \quad
  F_{\mathrm{Bor}} = \lvert\mathrm{tr}_M(\beta_{\mathrm{Bor}})\rvert\,\frac{[3]_q!}{q^3}.
$$

The hyperbolic-volume dependence enters through the muon anchor $\mathrm{Vol}(4_1)$, dressed by the dimensionless Borromean factor $F_{\mathrm{Bor}}$.

The Skein corrections isolate the crossing asymmetry between the $\mathfrak{u}$ and $\mathfrak{d}$ components. The pair Skein formula dictates $\mathfrak{m}_{\mathfrak{p}} = \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q) + 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q)$.

**Gluon content and colour symmetry.** The Borromean braid $\mathcal{B}_3$ natively carries Hopf link content; this constitutes the intrinsic gluon field binding the components. The $S_3$ permutation symmetry of the color tubes guarantees the invariant structure across all color assignments.
