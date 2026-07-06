The leading-order half-life formula ([hadron half-life](#prop:hadron-half-life)) evaluates the Skein polynomial strictly on the **nucleus alone**, treating the emitted electron as a free particle. However, the electron (trefoil $T_{2,3}$, [electron knot](#def:electron-knot)) traverses the Coulomb field of $Z$ protons as it exits the nucleus. Each electron-proton crossing carries a Skein weight. Evaluating the Skein polynomial on the **full outgoing link** $T_{2,3} \cup \mathcal{N}(Z, N)$ naturally generates the Coulomb enhancement.

**This does not constitute an ad hoc correction.** It is precisely the same Skein polynomial, evaluated on the complete outgoing link rather than truncating at the weak vertex.

**Magnitude.**
The integrated Coulomb enhancement (averaged over the electron energy spectrum) is a large, $Z$-dependent factor.

See [Table: Skein-Coulomb enhancement factors](#tbl:skein-coulomb-enhancement-table1-data).

These are **not** small perturbative corrections. They change decay rates by factors of 1.4 to 5. The leading-order predictions ([verification](#ex:hadron-half-life-verification)) inherently include $F_q$ at leading order through the nucleus-specific matrix element. The $\sim 10$--$17\%$ residual in the verification table stems entirely from discrete nuclear structure effects. Shell closures, pairing, and deformation modify the Gamow--Teller strength $\sigma_{\mathrm{GT}}$ at the individual-nucleus level.

**Transition classes.**
The nuclear matrix element $|\mathcal{M}_q|^2$ varies by six orders of magnitude across the verification set. Measured $\log ft$ values (NNDC/ENSDF) classify the transitions.

See [Table: Beta-decay classification](#tbl:skein-coulomb-enhancement-table2-data).

The QOU framework dictates the $q$-dependent modulation of each transition class (via $[2]_q$, $\tanh(\ln q)$, and $\sigma_{\mathrm{GT}}$). It does not, however, predict the absolute matrix element from the leading-order Hecke computation alone. Predicting $|\mathcal{M}_q|^2$ for individual nuclei necessitates resolving the discrete shell structure, specifically the precise quantum numbers of the parent and daughter nuclear states.

**Predictions of the QOU.**
Within a single transition class (fixed $\log ft$), the QOU correctly predicts:

1. **The $q$-dependent scale**: The factor $(q + q^{-1})(q - q^{-1})^5$ sets the overall decay-rate scale entirely from the single parameter $q$.
2. **The $A$-dependence**: We find $t_{1/2} \propto A^{5/3}$ at fixed $|\delta p|$ and fixed transition class.
3. **The $q$-sensitivity**: We predict $\partial \ln \Gamma / \partial \ln q \approx 48$ without free parameters.
4. **The Coulomb enhancement structure**: The term $F_q(Z, E)$ emerges directly from the Skein crossing weights. This unifies the electromagnetic and weak interactions through the single deformation parameter $q$.
5. **The self-deformation**: We observe a differential $\Delta q_{\mathrm{eff}}$ correction induced by the hadron's own linking structure.
