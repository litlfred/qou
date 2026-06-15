*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The leading-order half-life formula
([hadron half-life](#prop:hadron-half-life)) evaluates the Skein
polynomial on the **nucleus alone**, treating the emitted electron as
a free particle.  But the electron (trefoil $T_{2,3}$,
[electron knot](#def:electron-knot)) passes through the Coulomb field
of $Z$ protons on its way out of the nucleus, and each
electron-proton crossing carries a Skein weight.  Evaluating the
Skein polynomial on the **full outgoing link**
$T_{2,3} \cup \mathcal{N}(Z, N)$ gives the Coulomb enhancement.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be a Descartes universe with substrate
parameter $q$.  In the beta decay
$\mathcal{N}(Z, N) \to \mathcal{N}(p\!+\!1, n\!-\!1) + T_{2,3} + \nu^{\sigma}$, the emitted electron $T_{2,3}$ crosses each of the
$Z = p + 1$ proton strands of the daughter nucleus as it exits the
Hopf link.  The $q$-deformed wedge product $\wedge_q$
([crossing asymmetry](#rem:skein-crossing-asymmetry)) assigns weight
$q$ to each positive electron-proton crossing, producing a coherent
product that multiplies the decay rate by the **Skein-Coulomb
enhancement factor**

$$
  F_q(Z, E)
  = 
  \frac{2\pi\eta_q}{1 - e^{-2\pi\eta_q}}
$$

where the $q$-deformed Sommerfeld parameter is

$$
  \eta_q
  = 
  \alpha_{\mathrm{EM}}(q)
  \cdot \frac{Z}{\beta_e}
$$

with $\alpha_{\mathrm{EM}}(q) = q^{-1}/([9]_q \cdot [10]_q)$
([EM coupling projection](#prop:em-coupling-projection)) and
$\beta_e = v_e / c$ the velocity of the emitted electron.

**Derivation.**
The canonical action $\mathfrak{S}_q$
([canonical action](#prop:qou-canonical-action)) evaluated on the
full outgoing state $\psi = T_{2,3} \cup \mathcal{N}(p\!+\!1, n\!-\!1)$
decomposes as

$$
  \mathfrak{S}_q\big|_\psi
  = 
  \mathfrak{S}_q\big|_{\mathcal{N}}
  + 
  \sum_{j=1}^{Z} \mathcal{S}_{e\text{-}p_j}
  + 
  \mathfrak{S}_q\big|_{T_{2,3}}
$$

where the middle sum runs over electron-proton crossings.  Each
crossing contributes a Skein weight $\mathcal{S}_{e\text{-}p_j}(q) = q$
(positive crossing between two like-charge constituents).  The
electron's radial wave function picks up a phase
$e^{i\delta_\ell}$ at each proton, where the phase shift is

$$
  \delta_\ell
  = 
  \arg \Gamma(\ell + 1 + i\eta_q).
$$

The coherent product of $Z$ such scattering amplitudes,
summed over partial waves $\ell$ and integrated over the
electron energy spectrum, gives

$$
  |\psi_e(0)|^2_{\text{Coulomb}}
  = 
  |\psi_e(0)|^2_{\text{free}}
   \times 
  F_q(Z, E).
$$

The decay rate is proportional to $|\psi_e(0)|^2$ (the electron
wave function at the nuclear origin), so $F_q$ multiplies the
leading-order rate.

**This is not a correction bolted on** — it is the same Skein
polynomial, evaluated on the complete outgoing link instead of
truncating at the weak vertex.

**Magnitude.**
The integrated Coulomb enhancement (averaged over the electron
energy spectrum) is a large, $Z$-dependent factor:

See [Table: Skein-Coulomb enhancement factors](#tbl:skein-coulomb-enhancement-table1-data).

These are **not** small corrections — they change decay rates by
factors of 1.4 to 5.  The leading-order predictions
([verification](#ex:hadron-half-life-verification)) already include
$F_q$ at leading order through the nucleus-specific matrix element
the leading-order computation.  The $\sim 10$--$17\%$ residual in the verification
table arises from nuclear structure effects (shell closures, pairing,
deformation) that modify the Gamow--Teller strength
$\sigma_{\mathrm{GT}}$ at the individual-nucleus level — discrete
structure (shell closures, pairing, deformation).

**Transition classes.**
The nuclear matrix element $|\mathcal{M}_q|^2$ varies by six orders
of magnitude across the verification set.  Measured $\log ft$ values
(NNDC/ENSDF) classify the transitions:

See [Table: Beta-decay classification](#tbl:skein-coulomb-enhancement-table2-data).

The QOU framework determines the $q$-dependent modulation of each
transition class (via $[2]_q$, $\tanh(\ln q)$, and $\sigma_{\mathrm{GT}}$)
but does not predict the absolute matrix element from the
leading-order Hecke computation alone.  Predicting $|\mathcal{M}_q|^2$
for individual nuclei requires resolving the discrete shell
structure — the quantum numbers of the specific parent and daughter
nuclear states.

**What the QOU does predict.**
Within a single transition class (fixed $\log ft$), the QOU
correctly determines:

1. **The $q$-dependent scale**: $(q + q^{-1})(q - q^{-1})^5$ sets
   the overall decay-rate scale from the single parameter $q$.
2. **The $A$-dependence**: $t_{1/2} \propto A^{5/3}$ at fixed
   $|\delta p|$ and fixed transition class.
3. **The $q$-sensitivity**: $\partial \ln \Gamma / \partial \ln q \approx 48$, a parameter-free prediction.
4. **The Coulomb enhancement structure**: $F_q(Z, E)$ emerges from
   the Skein crossing weights, unifying the electromagnetic and
   weak interactions through the single deformation parameter $q$.
5. **The self-deformation**: the differential $\Delta q_{\mathrm{eff}}$
   correction from the hadron's own linking structure.
