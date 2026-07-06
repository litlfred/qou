The [proton definition](#def:categorical-proton) establishes the $\mathcal{B}_3(\mathfrak{u},\mathfrak{u},\mathfrak{d})$ baryon. We derive its normal form, mass, Coulomb charge, and computational backing.

**Step 1: Borromean braid NF.**
The inverse relation $\sigma_1^{-1} = \sigma_1 - H_A \mathbf{1}$ (derived from the Hecke relation $\sigma_i^2 = H_A \sigma_i + \mathbf{1}$ with $H_A = q - q^{-1}$) yields $\mathcal{B}_3 = (\sigma_0(\sigma_1 - H_A))^3$. Expanding and reducing within $H_3(q)$ at $q_0 \approx 1.1100$ produces:

See [Table 1](#tbl:categorical-proton-table1-data).

$$
  \mathrm{net}(\mathcal{B}_3) = +1.0000
$$

The Hopf link terms $L_\pm$ manifest the gluon field. The $\mathcal{B}_3$ braid supplies intrinsic binding without requiring an external Hopf link factor. (Witness: `breit-wheeler-nucleon-nf.witness.json`).

**Step 2: Typed crossings.**
Quark flavor rigidly specifies the crossing eigenvalue in $H_3(q)$. Each quark pair contributes a crossing on the generator connecting their strands:

See [Table 2](#tbl:categorical-proton-table2-data).

The $\mathfrak{u}$-$\mathfrak{u}$ crossing preserves the eigenvalue $+q$. The $\mathfrak{d}$-type crossings impose a full $-H_A$ shift (eigenvalue $-q^{-1}$). Mixed $\mathfrak{u}$-$\mathfrak{d}$ crossings incur a half-shift $-\tfrac{1}{2}H_A$.

The full proton assembly is $\mathfrak{p} = \mathcal{B}_3 \times \sigma_0 \times (\sigma_0 - \tfrac{1}{2}H_A) \times (\sigma_1 - \tfrac{1}{2}H_A) \times L_-$, evaluated step-by-step via Gröbner--Shirshov reduction.

**LP stability constraint.**
The bare 9-crossing element $\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$ (lacking the gluon) violates Frobenius positivity: $G x[\gamma] < 0$. A single Hopf link $L_- = \sigma_1\sigma_0$ is the minimum additional structure capable of restoring stability. The gluon is strictly required by the LP dual, not imposed by assumption.

The integer LP dual enumerates all feasible gluon combinations (up to 3 operations from $\{\sigma_0, \sigma_1, L_+, L_-\}$, enforcing Frobenius stability at every intermediate step) and selects the configuration minimizing $|\mathrm{tr}_M|$. Among 40 feasible solutions, the optimum is $\sigma_0 \to \sigma_0$: two bare $\sigma_0$ crossings, yielding 11 total crossings (6 from B$_{3}$, 3 from quarks, 2 from gluons) with $|\mathrm{tr}_M| = 0.027$.

**Step 3: Proton NF (with Hopf gluon).**
Applying typed crossings and Hopf link stabilisation at $q_0 \approx 1.1100$:

See [Table 3](#tbl:categorical-proton-table3-data).

$$
  \mathrm{net}(\mathfrak{p}) = +1.0065
$$

The dominant term is $e^- \approx +1.022$. The Hopf gluon link actively redistributes normal-form weight from $\sigma_1$ into the trefoil channel. The Hopf link content $L_\pm \approx \pm 0.11$ exceeds the bare B$_{3}$ value ($\pm 0.045$), reflecting the supplementary gluon binding. This construction maintains LP stability at every intermediate step.

**Mass.**
The proton mass derives from the hyperbolic volume of the Borromean link:

$$
  \mathfrak{m}_{\mathfrak{p}} =
  \frac{\mathrm{Vol}(S^3 \setminus \mathcal{B}_3)}{\hbar_q^2}
  \cdot \lambda_{\mathrm{scale}}
  + \text{Skein corrections}
$$

The Skein corrections isolate the crossing asymmetry between the $\mathfrak{u}$ and $\mathfrak{d}$ components. The pair Skein formula dictates:

$$
  \mathfrak{m}_{\mathfrak{p}} = \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q)
  + 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q)
$$

At the CODATA root $q_0$, the computed mass is $\mathfrak{m}_{\mathfrak{p}}(q_0) \approx :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV, constrained entirely by the local substrate parameter ([local substrate](#prop:local-substrate-q)).

**Coulomb charge.**
The proton sustains net positive crossing chirality. The two positive-orientation unknots ($\mathfrak{u}$) overpower the single negative unknot ($\mathfrak{d}$), forcing the net Coulomb charge:

$$
  Q(\mathfrak{p}) = 2 \cdot (+\tfrac{2}{3}) + 1 \cdot (-\tfrac{1}{3}) = +1.
$$

**Computational backing.** 
The Borromean architecture rests on numerical witnesses supplied with the text. The file `computations/borromean-axial-coupling.witness.json` verifies the axial-coupling $g_A$ from $H_3(q_0)$ against the PDG 2024 consensus $g_A = 1.2754$. The file `proton-braid-sweep-gg.witness.json` supplies the proton braid coefficients in the NF basis at $q_0$. The file `borromean-qvalue.py` documents the topological derivation of $q_0 = 1.109978595554181\ldots$ to 50 decimal places. These constitute numerical witnesses, not formal proofs (see the [Borromean-quark conjecture](#conj:borromean-quark) and the ground-ring annotation in `borromean-quark.lean`).
