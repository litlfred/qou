The leading-order half-life formula
([hadron half-life](#prop:hadron-half-life)) evaluates the Skein
polynomial on the **nucleus alone**, treating the emitted electron as
a free particle.  But the electron (trefoil $T_{2,3}$,
[electron knot](#def:electron-knot)) passes through the Coulomb field
of $Z$ protons on its way out of the nucleus, and each
electron-proton crossing carries a Skein weight.  Evaluating the
Skein polynomial on the **full outgoing link**
$T_{2,3} \cup \mathcal{N}(Z, N)$ gives the Coulomb enhancement.

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

**Predictions of the QOU.**
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
