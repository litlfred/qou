<!-- FILE_START: precision-tests-intro.md -->
Strangelets test the framework at extreme density. This section tests it at ordinary density but extreme precision. We first examine photonic and electromagnetic precision data.
- Photonic quantum Hall effect and $q$-deformed braiding matches the measured Hall conductance plateaux against $q$-deformed braiding amplitudes.
- Fine structure constant compares the predicted $\alpha$ to the CODATA value.

The confinement sector follows.
- Color confinement as $q$-chromaticity reads confinement as a positivity constraint on Feynman amplitudes.
- Curvature-rank as confinement layer supplies the categorical reformulation in terms of curvature rank.
- Physics names $\leftrightarrow$ categorical knot operations tabulates the dictionary between physics names and categorical knot operations at $q_0$.

The section closes with lepton anomalies.
- Electron--muon discrepancies and Lepton anomalies data record the discrepancies. The subsequent proton-radius and gravity-test section reads these as a single-substrate observable.
<!-- FILE_END: precision-tests-intro.md -->

<!-- FILE_START: photonic-hall.md -->
Experiments demonstrate a quantized Hall drift in photonic Chern insulators. In the QOU framework, bosons are purely horizontal $q$-harmonic forms ([boson](#def:fermion-boson-decomposition)). The Hall conductance arises from the Chern number of the bulk bundle restricted to the horizontal distribution. The $q$-deformation modifies the quantisation condition. It predicts fractional corrections of order $1 - q^{-1}$ to the Hall conductance.
<!-- FILE_END: photonic-hall.md -->

<!-- FILE_START: fine-structure-observation.md -->
The electromagnetic coupling ([EM coupling projection](#prop:em-coupling-projection)) predicts $\alpha_{\mathrm{EM}}$ directly from the substrate parameter $q$. It requires zero free parameters.

**Bare formula.**
$$
  \alpha_{\mathrm{EM}}^{-1}(q)
  = 
  q \cdot [9]_q \cdot [10]_q
  = 136.823.
$$

The force-carrier generators $T_{2,9}$ and $T_{3,5}$ ([force identification](#rem:force-knot-identification)) dictate the crossing numbers $9$ and $10$. The Descartes substrate parameter fixes the $q$-integers.

**Derived correction.**
The leading correction to the bare formula is additive. It derives from the photon infrared zero-mode on Bring's surface ([photon IR zero-mode](#prop:photon-ir-zero-mode-bring)):

$$
  \alpha_{\mathrm{EM}}^{-1}(q) = q \cdot [9]_q \cdot [10]_q + \frac{2}{3\pi},
  \qquad \frac{2}{3\pi} = \frac{b_1(M_{\mathrm{Bring}})}{\mathrm{Area}(M_{\mathrm{Bring}})}
  = \frac{2g}{4\pi(g-1)}\Big|_{g=4}.
$$

The genus-$4$ topology fixes $b_1 = 2g = 8$ and the Gauss–Bonnet area. The corrected value is $137.0354$. This leaves a $-4.2\;\mathrm{ppm}$ residual against the CODATA value of $137.035999$. This additive correction improves the bare form by a factor of $370$. Both the tree term and the additive zero-mode are Lean-formalised.

**Order of validity.**
The remaining $-4.2\;\mathrm{ppm}$ represents a next-order Schwinger-type effect $\sim \alpha/(4\pi)$. The denominator $8\pi = \pi\,b_1$ is derived. The exact coefficient is an $O(\alpha^2)$ Bloch-group normalisation in $B_3(\mathbb{C})$ over the ideal hyperbolic tetrahedra of Bring's surface. This coefficient is not yet closed ([α_EM derivation open problems](#rem:alpha-em-derivation-open-problems)). The parameter-free prediction holds to $\approx 4\;\mathrm{ppm}$ via the additive correction. The $O(\alpha)$ self-energy coefficient remains open.

**Numerical comparison.**
See [Table 1](#tbl:fine-structure-observation-table1-data).

**Inversion: $q$ from $\alpha_{\mathrm{EM}}$.**
Fixing $\alpha^{-1} \approx 137.036$ and solving for $q$ yields:

$$
  q_{\mathrm{CODATA}} = 1.11023.
$$

This value matches the substrate parameter extracted independently from mass predictions and half-life calculations ([half-life as $q$-probe](#rem:half-life-as-q-probe)). This provides a cross-check between the electromagnetic and strong sectors.

**Sensitivity.**
The coupling depends steeply on $q$:

$$
  \frac{\partial \ln \alpha_{\mathrm{EM}}}{\partial \ln q}
  =  -1 - 
  \frac{9  q^9 [10]_q + 10  q^{10} [9]_q}
       {[9]_q [10]_q (q - q^{-1})}.
$$

At $q = q_0$, this derivative is approximately $-20$. A $1\%$ shift in $q$ drives a $\sim 20\%$ shift in $\alpha_{\mathrm{EM}}$. The empirical agreement bounds $q$ around $q_0$.

**Comparison.**
See [Table 2](#tbl:fine-structure-observation-table2-data).

The substrate parameter $q_0$ is overdetermined. Three independent observables (electromagnetic coupling, mass ratios, decay rates) converge on the identical value.
<!-- FILE_END: fine-structure-observation.md -->

<!-- FILE_START: color-confinement-observation.md -->
Feynman noted \cite{feynman1963} that three color primaries cannot reproduce all visible spectral colors using strictly positive coefficients. The CIE chromaticity diagram formalizes this. The spectral locus is a curve that no inscribed triangle contains. Certain spectral colors require negative coefficients for at least one primary.

In the Descartes universe, this geometric constraint transplants to the Skein algebra. It provides a mechanism for color confinement.

**Analogy.**
See [Table](#tbl:color-confinement-observation-table-data).

**Why exactly three colors.**
The automorphism group $S_5$ of Bring's surface contains exactly three conjugate $S_3$ subgroups. Each subgroup is the quotient of the trefoil knot group restricted to one color fiber. The number three arises from geometric structure:
1. The degree of the Bring curve is $5$ (quintic in $\mathbb{P}^4$).
2. The resolvent structure factors as $5 = 1 + 1 + 3$ (one spacetime base, one longitudinal backbone, three chiral fibers).
3. The $S_5$ subgroup structure contains three $S_3$ subgroups permuted by the remaining generators.

In the CIE diagram, three primaries model human color vision. In this paper, the algebraic geometry of Bring's surface forces three color tubes.

**Confinement strength.**
The Skein asymmetry $q - q^{-1}$ controls the necessity of negative coefficients:
- At $q = 1$ (classical limit): the Skein relation simplifies to $[L_+] = [L_-]$. All coefficients can be made positive. Confinement vanishes. Individual colors are separately observable.
- At $q = q_0$ (Descartes value): $q - q^{-1} = 0.209$. This produces roughly $20\%$ negativity in Skein coefficients. Individual quarks have negative $\tau$-evaluations and remain confined.
- At $q \to \infty$: negativity saturates and confinement becomes absolute.

Confinement strength is finite and depends on $q$. This provides a geometric basis for asymptotic freedom. At short distances (high energies), the effective $q$ flows toward $1$ under Reeb dynamics. This reduces the Skein asymmetry. At the QCD scale, the running $q$ requires more energy for color extraction than pair creation. This reproduces the standard confinement mechanism via the $q$-chromaticity constraint.

**Quantitative prediction.**
The Skein negativity at a single crossing is $q^{-1} = 0.901$ (the antisymmetric $R$-matrix eigenvalue). For a baryon with $n$ internal crossings, the probability of isolating a single quark scales as

$$
  P_{\mathrm{isolation}} \sim (-q^{-1})^n \to 0
$$

This decays exponentially in the number of crossings. The proton consists of three trefoils linked by $T_{2,9}$, forming a Borromean structure. It requires $9$ binding crossings from the force carrier and $9$ matter crossings from the three trefoils, giving

$$
  P_{\mathrm{isolation}} \sim q^{-18} \approx 0.13
$$

at the bare level. Confinement is probabilistically suppressed rather than topologically absolute, as the knots embed freely. The fibre functor assigns exponentially small weight to single-color states.

A complete proof of confinement requires demonstrating that $\tau(\psi_{\mathrm{color}}) < 0$ for all single-color states $\psi_{\mathrm{color}}$ at $q = q_0$. This reduces to a positivity theorem for the $S_5$-invariant Skein submodule.
<!-- FILE_END: color-confinement-observation.md -->

<!-- FILE_START: confinement-curvature-rank.md -->
**Remark (curvature-rank as confinement layer).**
By [confinement-categorical](#prop:confinement-categorical), the collapse of the GB-filtration spectral sequence provides the categorical content of color confinement. Translating this algebraic statement into QCD vocabulary yields the following dictionary.

**Confinement layers.**
The GB filtration $J^0 \supset J^1 \supset \cdots$ stratifies $A = H_n(R, q)$ by curvature-rank $k = \mathrm{depth}(\lambda) - 1$. Each stratum $J^k / J^{k+1}$ acts as a confinement layer:
- $k = 0$ (centre): elements are gauge-invariant. This forms the observable hadron content.
- $k \geq 1$: extracting an element requires energy proportional to the curvature 2-cocycle $F$ (the combined Hecke and Yang-Baxter obstruction). This is categorically the **string tension**.

**String tension = curvature 2-cocycle.**
The Hecke relation $T^2 = (q - q^{-1}) T + 1$ and Yang-Baxter relations define a 2-cocycle $F$ on the GB filtration. $F$ obstructs the extraction of a non-central element along the filtration. It matches how QCD string tension obstructs the extraction of an isolated colored quark. The QCD "string" corresponds to the chain of commutators $[a, b]$ required to move an element through the layers $J^k$.

**Gluon condensate = chirality channel.**
The chirality cells $D_q^2 = 0$ in the q-Dirac cell scanner ($\lambda = (2, 1)$ for $H_3$ and higher-$n$ analogues) coincide with the S-fixed central elements of $A$. They produce a persistent gauge-invariant background. This is the categorical analogue of the **gluon condensate** in QCD. The volume match $\mathrm{Vol}(B_3) = 8 G$ with the gluon octet dimension $\dim \mathfrak{su}(3) = 8$ provides the operator-side identification.

**Hadron mass = sum of confinement layers.**
The unified mass formula ([unified mass formula](#prop:unified-curvature-rank-mass-formula)) reads physical hadron mass as a sum over confinement layers:

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\; \sum_{k = 0}^{n - 1} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(1).
$$

Each layer contributes its q-deformed Wedderburn-weighted log-character content (cf. $\tilde w_\lambda$ in [`prop:plancherel-term-7-formulation`](../braids-and-knots/plancherel-term-7-formulation.md)).

| Stratum | Confinement layer | Physical content |
|---|---|---|
| $k = 0$ | centre / vacuum | photon-like / unconfined |
| $k = 1, 2$ | low-tower | specific hyperbolic-knot ideals (named knots) |
| $k = 3$ | chirality layer | $D_q^2 = 0$, gluon-condensate background |
| $k \geq 4$ | universal residue | Frobenius co-Casimir tail (no specific knot) |

**Predictive consequence.**
Confinement is structurally built into the spectral-sequence collapse. Every prediction ([universal residue](#prop:plancherel-term-7-formulation), [$\mathfrak{Q}_\beta$ structural derivation](#)) is gauge-invariant because the spectral-sequence projection forces all results through $Z(A)$. The rank-3 chirality residue $\mathrm{Vol}(6_1) \cdot |(q;q)_3|$ in the $\mathfrak{Q}_\beta$ formula acts as a **gluon-condensate background term**. The rank-$\geq 4$ universal Pochhammer tail $|(q;q)_4|$ serves as the **Frobenius co-Casimir**. Both are necessary confinement residues, not free parameters.
<!-- FILE_END: confinement-curvature-rank.md -->

<!-- FILE_START: physics-names-knot-operations.md -->
**Remark (physics names are $q_0$-dependent labels for categorical knot operations).**
Physics names (alpha particle, gluon condensate, valence shell, isospin) are labels for recurring categorical structures in the Hecke algebra $H_n(R, q)$ at the substrate parameter $q_0$. The categorical structure is fundamental. The physics naming is a derived mapping that depends on the value of $q_0$.

This table records the current mapping at $q_0 = 1.109978595554181\ldots$ (50 dps). At a different substrate value, the categorical structures persist but their physics interpretations may differ. The recurring sub-blocks identified by the discovery cache acquire different macroscopic meaning when $q_0$ changes.

See [Table](#tbl:physics-names-knot-operations-table-data).

**Generation of the table.**
The discovery cache (`computations/knot-operation-cache.json`) is populated by SDP shadow-price analysis on Hecke Wedderburn blocks. It records each recurring categorical structure as a key. The lookup `physics-names.json` maps cache keys to physics names at the current $q_0$. The categorical cache keys are the source of truth. The physics names are the display layer.

**Substrate dependency.**
Several entries carry "Depends on $q_0$" annotations. These indicate:
- The $\dim_q V_\lambda$ factor evaluates to a $q_0$-dependent number.
- The recurring sub-block is identified at the algebraic level (categorical structure independent of $q_0$), but its numerical weight depends on $q_0$.
- At a different $q_0$, the same sub-block exists but may have a different Plancherel weight, possibly vanishing. If the weight vanishes, the physics name no longer applies.

The "alpha particle" identification requires $w_{(3,3,3,3)}(q_0)$ to dominate the depth-3 chirality cells of $H_{12}$. At $q_0 = 1.109978595554181\ldots$, this weight is $\sim 0.024$. It is the largest contribution at depth 3. At $q_0 = 1$ (classical limit), the weight becomes the symmetric-group Specht-module dimension squared over $12!$. The ranking changes. The "alpha particle" identification must be re-derived.

**Remark.** This table is the interface between the categorical machinery (`prop:em-spectral-completeness`, `prop:gauge-coupling-uniqueness`, `prop:chirality-residue-mass-term`) and the physics-language predictions in this chapter. Every physics name in this chapter that does not appear in this table is either an external empirical reference (CODATA, AME) or a forward reference to a later definition.
<!-- FILE_END: physics-names-knot-operations.md -->

<!-- FILE_START: lepton-discrepancies.md -->
Two structural criteria distinguish lepton generations. These are Reeb-vertical degree of knot localisation ([rem:archimedean-leptons](#rem:archimedean-leptons)), and whether the cyclic symmetry embeds in $S_5$ ([rem:symmetry-preserving-leptons](#rem:symmetry-preserving-leptons)). The electron and muon satisfy both. The tau satisfies only the first. Anomalous magnetic-moment tensions and lepton flavour universality violations observed at $B$-factories may reflect this structural asymmetry rather than new heavy-particle loops. This is likely where the discrepancy tracks specifically with the tau channel.
<!-- FILE_END: lepton-discrepancies.md -->
