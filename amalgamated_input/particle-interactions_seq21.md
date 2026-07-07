<!-- FILE_START: intro-magic-shells.md -->
The integer-linear-program (ILP) selection on stable nuclei identifies the categorical magic shells. These are closed nucleon configurations whose categorical-energy minimum is bounded below by the coupling constant $\kappa$. This section unwraps the ILP solution count. We extract the $\kappa$ coupling that controls the shell-closure pattern. We then connect the shell-closure spectrum to the empirical magic-number sequence ($2, 8, 20, 28, 50, 82, 126$).

The development proceeds in two layers. The first layer exhibits the ILP unwrap, the shell Schur-Weyl self-duality, and the compound-$\beta$ shell calibration. The second layer pins the $\kappa$ coupling constant from the substrate parameter. We conclude with a quantum-dilogarithm disambiguation required for the next section.
<!-- FILE_END: intro-magic-shells.md -->

<!-- FILE_START: ilp-solution-count-unwrap.md -->
**Remark.**
*The number of distinct ILP solutions at a given confinement level dictates the **unwrap depth** required to uniquely specify an atom-knot's normal form.*

*Let $K$ be an atom at substrate parameter $q$ with normal form currently expressed at level $\ell$. Let $N_\ell(K, q)$ be the number of integer solutions $x \in \mathbb{Z}_{\geq 0}^M$ to the Frobenius positivity ILP $\mathrm{G}(q)\, x \geq 0$ within the confinement filtration $J^\ell(q)$ ([stable atom](#def:stable-atom), [stable-atom-decidable](#prop:stable-atom-decidable)).*

*The **unwrap depth** at level $\ell$ is:*

$$
  d_\ell(K, q) = \max\bigl(0, N_\ell(K, q) - 1\bigr).
$$

*Interpretation:*

- *$N_\ell = 0$: **unstable** at level $\ell$ ([unstable atom](#def:unstable-atom)). The atom cannot exist in this shorthand. It must decay or fully unwrap.*
- *$N_\ell = 1$: **uniquely determined** at level $\ell$. The shorthand suffices; no unwrap is needed.*
- *$N_\ell = k \geq 2$: **$(k-1)$-fold ambiguous** at level $\ell$. One must unwrap $k-1$ levels to disambiguate via finer normal form structure.*

**Connection to confinement levels.**
*Each unwrap step expands a shorthand word at level $\ell$ into its normal form at level $\ell - 1$. The finer level accesses a larger filtration $J^{\ell-1}(q) \supsetneq J^\ell(q)$. This richer operator basis distinguishes previously tied ILP solutions. This process provides a categorical analog to renormalisation: when a coarse effective description exhibits multiple solutions, zooming to the next-finer scale resolves the ambiguity via operator content.*

**Computational benefit.**
*Non-magic atoms typically exhibit $N_\ell = 1$ at the coarsest useful level. A single inter-nucleon configuration suffices. Magic atoms exhibit $N_\ell \geq 2$ at the nucleon level. Shell closure permits multiple equivalent assemblies of the closed shell. Each corresponds to a distinct normal form at the quark level. Double-magic atoms exhibit $N_\ell \geq 3$ because both proton and neutron closures contribute degeneracy.*

**Formal statement.**
*Let $K$ be an atom-knot. Then:*

$$
  \boxed{\; \text{NF-depth}(K, q) = \text{coarsest level } \ell \text{ with } N_\ell(K, q) = 1 \;}
$$

*Computing the normal form at exactly this depth fully specifies the atom's categorical structure. Deeper computation is redundant; shallower computation leaves ambiguity.*

**Example (proton gluon derivation).**
*The proton's 9-crossing element $\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$ admits $N_\ell = 84$ feasible ILP solutions at the baryon level ([mass-endomorphism-tower](#prop:mass-endomorphism-tower)). Minimizing $|\mathrm{tr}_M|$ selects the unique $\sigma_0 \to \sigma_0$ solution. If a tie occurs (e.g., two solutions share identical $|\mathrm{tr}_M|$), the framework demands unwrapping to the quark level, where the ILP separates them.*

**Computational shortcut.**
*Adaptive unwrap yields dramatic savings:*

| Atom type | Typical $N_\ell$ at nucleon level | Unwrap depth | $n_{\text{strands}}$ used |
| :--- | :--- | :--- | :--- |
| Non-magic (e.g., $^6$Li) | 1 | 0 | $A$ (nucleon-words) |
| Single-magic (e.g., $^{14}$C) | 2 | 1 | $3A$ (quark-level) |
| Double-magic (e.g., $^4$He, $^{16}$O) | 3 | 2 | $3A$ + shell NF |

*Storage and Gröbner reduction scale with $n_{\text{strands}}^{\text{used}}$ rather than uniformly with $3A$.*
<!-- FILE_END: ilp-solution-count-unwrap.md -->

<!-- FILE_START: shell-schur-weyl-self-duality.md -->
**Proposition (Schur–Weyl justification of shell self-duality).**
*Let $\mathcal{U}_q(\mathfrak{gl}_k)$ denote the quantum enveloping
algebra and $H_n(R, q)$ the Iwahori–Hecke algebra.  Under Schur–Weyl
duality*

$$
  V^{\otimes n}
  \;=\;
  \bigoplus_{\lambda\,\vdash\,n}
    V_{\mathcal{U}_q(\mathfrak{gl}_k)}(\lambda)
    \;\otimes\;
    V_{H_n(R, q)}(\lambda),
$$

*the $S_n$-transpose involution $\lambda \leftrightarrow \lambda^*$
on Young diagrams is the image of the representation-duality
involution $V \leftrightarrow V^*$ on $\mathcal{U}_q(\mathfrak{gl}_k)$-
modules:*

$$
  V_{\mathcal{U}_q(\mathfrak{gl}_k)}(\lambda^*)
  \;\cong\;
  V_{\mathcal{U}_q(\mathfrak{gl}_k)}(\lambda)^*
$$

*(up to a twist by $\det^{n}$ when $\lambda$ has fewer than $k$ rows).
Equivalently, on the Hecke side:*

$$
  V_{H_n(R, q)}(\lambda) \,\otimes\, V_{H_n(R, q)}(1^n)
  \;\cong\;
  V_{H_n(R, q)}(\lambda^*),
$$

*where $V_{H_n(R, q)}(1^n)$ is the sign (alternating) representation.*

*Consequently, the **shell-operator self-duality constraint***

$$
  x_\lambda \;=\; x_{\lambda^*}
  \qquad\text{for all}\quad \lambda \vdash A_{\mathrm{magic}}
$$

*on the Wedderburn decomposition*

$$
  \sigma_{\mathrm{shell}}
  \;=\;
  \sum_{\lambda\,\vdash\, A_{\mathrm{magic}}}
    x_\lambda \cdot e_\lambda
  \;\in\; H_{A_{\mathrm{magic}}}(q)
$$

*is equivalent to $\mathrm{GL}_k$-charge-conjugate invariance of the
underlying quantum-group module structure under Schur–Weyl transport.*
<!-- FILE_END: shell-schur-weyl-self-duality.md -->

<!-- FILE_START: shell-schur-weyl-self-duality-interpretation.md -->
Shell closures in nuclei (magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$) correspond to charge-conjugate-invariant braid elements in $H_{A_{\mathrm{magic}}}(q)$. This categorical structure enforces three physical constraints:

- **Parity conservation.** The nuclear strong interaction conserves parity because shell closures respect charge conjugation.
- **Isospin doubling.** Proton-neutron interchange symmetry emerges at closed shells via isospin SU(2) doubling.
- **CP conservation.** Shell-level CP violation vanishes because parity-odd channels cancel between $\lambda$ and $\lambda^*$ contributions.

Parity-violating phenomena (such as $\beta$-decay) arise at level 3 (the inter-nucleon pair), where conjugate symmetry breaks via skein asymmetry ([skein crossing asymmetry](#prop:skein-crossing-asymmetry)). They do not appear at level 4 (the shell), where Schur–Weyl self-duality is exact.
<!-- FILE_END: shell-schur-weyl-self-duality-interpretation.md -->

<!-- FILE_START: compound-beta-shell-calibration.md -->
**Proposition (compound β-decay calibration across magic shells).**

*Let $E_0^{(2)} = \mathfrak{Q}_\beta = 0.782$ MeV be the free-neutron β-decay Q-value—the $H^2$ calibration of the [three-calibration discipline](#prop:three-calibration-discipline). Let a β-decay $(Z, N) \to (Z+1, N-1)$ cross a magic anchor $A_{\mathrm{magic}} \in \{2, 8, 20, 28, 50, 82, 126\}$. Assume the parent contains $\sigma_{\mathrm{shell}}$ (via [shell self-duality](#prop:shell-schur-weyl-self-duality)) and the daughter contains a different shell operator or a cross-shell transition ([shell-transition knot](#conj:shell-transition-knot)). Then the Q-value of the magic-crossing decay is:*

$$
  \mathfrak{Q}_\beta(A_{\mathrm{magic}}\text{-crossing})
  \;=\;
  E_0^{(2)} \cdot
  \Bigl(
    \bigl|\mathrm{tr}_M^{\mathrm{parent}}\bigr|
    \;-\;
    \bigl|\mathrm{tr}_M^{\mathrm{daughter}}\bigr|
    \;-\;
    \bigl|\mathrm{tr}_M^{\mathrm{e^- + \bar\nu}}\bigr|
  \Bigr).
$$

*Equivalently, the shell-binding target $y_{\mathrm{target}}(A_{\mathrm{magic}})$ correlates to the cumulative β-decay chain reaching the magic anchor via the categorical trace. To formalize the full binding scale, we combine multiple β-decay Q-values along the isobar chain through the magic anchor. (See [compound-beta-shell-calibration-probe](#audit:compound-beta-shell-calibration-probe) for empirical consistency checks.)*

A β-decay $(Z, N) \to (Z+1, N-1)$ in the Hecke algebra corresponds to the data in [Table 1](#tbl:compound-beta-shell-calibration-table1-data).
<!-- FILE_END: compound-beta-shell-calibration.md -->

<!-- FILE_START: compound-beta-shell-calibration-key-distinction.md -->
**Non-magic vs magic $\beta$-decays (key distinction).**

A $\beta$-decay $(Z, N) \to (Z+1, N-1)$ within the Hecke algebra maps to the operator transition shown in [Table 1](#tbl:compound-beta-shell-calibration-table1-data).

For magic-crossing decays, the $\mathcal{Q}_q$-value measures the strict difference in shell-operator contributions between parent and daughter, never the absolute shell magnitude itself. The parent intrinsically carries $\sigma_{\mathrm{shell}}$ via [shell self-duality](#prop:shell-schur-weyl-self-duality). The daughter realizes a distinct shell operator or a cross-shell transition ([shell-transition knot](#conj:shell-transition-knot)). The observable $\mathcal{Q}_q$-value isolates only this differential contribution.
<!-- FILE_END: compound-beta-shell-calibration-key-distinction.md -->

<!-- FILE_START: compound-beta-shell-calibration-interpretation.md -->
**Corollaries.**

1. *The shell $y_{\mathrm{target}}$ values are never independently calibrated. They follow strictly from $\beta$-decay $\mathcal{Q}_q$-values and level-3 shadow prices.*
2. *The shell sector introduces no new calibration. We retain $E_0 = \mathfrak{Q}_\beta$ as the pure $H^2$ input for the [three-calibration discipline](#prop:three-calibration-discipline) (alongside $H^0 = m_e$ and $H^1 = m_\mu/m_e$). Shell binding derives entirely from decay-chain $\mathcal{Q}_q$-values and level-3 shadow prices.*
3. *Predictions for all magic-anchor binding energies (${}^{4}\mathrm{He}$, ${}^{16}\mathrm{O}$, ${}^{40}\mathrm{Ca}$, ${}^{56}\mathrm{Ni}$, ${}^{208}\mathrm{Pb}$) are strictly parameter-free, contingent only on the $\beta$-decay table.*

**Open:** *The next step in tower binding requires full implementation of the chain-$\mathcal{Q}_q$-value derivation, enforcing correct separation of non-magic versus magic contributions at every intermediate step.*
<!-- FILE_END: compound-beta-shell-calibration-interpretation.md -->

<!-- FILE_START: magic-shell-coupling-kappa.md -->
**Proposition (Magic-shell coupling slope — categorical closed form).**
*The per-unit-excess magic-shell coupling slope $\kappa$, which controls the $(n_{pp} - n_{nn})$ excess contribution to atomic binding at single-magic anchors $(Z, N) = (2, 1)$ and $(1, 2)$, admits the closed categorical form*

$$
  \boxed{\,
  \kappa \;=\; -\,\frac{E_0 \cdot \log(1/h)}{[2]_q \cdot [3]_q}
  \,}
$$

*where $E_0 = m_e / (q(q-1))$ is the Hecke energy scale, $h = q - q^{-1}$ is the Hecke deformation parameter, and $[n]_q = (q^n - q^{-n}) / (q - q^{-1})$ is the q-bracket.*

## Numerical verification at $q_0$

Evaluating at the substrate parameter $q_0 = 1.109978595554181\ldots$ (50 dps):

See [Table](#tbl:magic-shell-coupling-kappa-table-data).

$$
  \kappa_{\mathrm{categorical}} = -\frac{4.1860 \cdot 1.5651}{6.1206}
  \approx -1.0704239\;\text{MeV}
$$

Against the observed physical value from v6 single-magic anchor data:

$$
  \kappa_{\mathrm{observed}} \approx -1.0707908\;\text{MeV}
$$

The ratio is $0.999657$ — within $0.034\%$ at the single-magic anchors. The numerical inputs are substrate parameters ($m_e$, $q_0$) and structural q-brackets. The form of the closed expression — the $E_0 \cdot \log(1/h)$ magic-shell quantum and the $[2]_q \cdot [3]_q$ normalization — was identified empirically against the $(2,2)$ doubly-magic anchor (an acknowledged CAL-4 shape selection; see §"Structural interpretation"). The $0.034\%$ agreement at the single-magic $(2,1)$ / $(1,2)$ anchors is therefore a near-match cross-check of that anchor-identified form, not a zero-parameter prediction.

## Structural interpretation

The closed form decomposes into two pieces:

1. **H7a energy quantum** $E_0 \cdot \log(1/h)$ — the per-shell magic-coupling magnitude, motivated structurally as the logarithm of the Hecke deformation and identified empirically against the doubly-magic anchor $(2, 2)$ (acknowledged CAL-4). This is the candidate "magic-shell energy unit" of the categorical substrate.
2. **q-deformed dimension product** $[2]_q \cdot [3]_q$ — the quantum dimension of the $V_2 \otimes V_3$ Schur–Weyl tensor product. This is the relevant LR fusion multiplicity for $A = 3$ single-magic anchors. The product normalizes the H7a quantum to the per-(n_{pp} - n_{nn}) excess slope.

Putting these together:

$$
  \kappa \;=\; \underbrace{-E_0 \cdot \log(1/h)}_{\text{H7a quantum}}
  \;\cdot\; \underbrace{\frac{1}{[2]_q \cdot [3]_q}}_{\text{LR-fusion normalization}}
$$

The negative sign tracks the orientation convention for the $(n_{pp} - n_{nn})$ excess in [`prop:compound-beta-shell-calibration`](#prop:compound-beta-shell-calibration).

## Closure of the κ derivation work-item

This proposition supplies a categorical form for the κ derivation requested in user work-list item #4. The observed $\kappa \approx -1.07\;\text{MeV}/\text{excess}$ from v6 is reproduced to $0.034\%$ at the single-magic anchors by a structurally-motivated expression. Its magic-shell quantum $E_0 \cdot \log(1/h)$ was identified at the $(2,2)$ doubly-magic anchor (acknowledged CAL-4). Full closure — a parameter-free derivation of that quantum purely from $q_0$, with a fresh verifying witness replacing the removed probe script — remains open.
<!-- FILE_END: magic-shell-coupling-kappa.md -->

<!-- FILE_START: quantum-dilogarithm-disambiguation.md -->
**Definition (Quantum dilogarithm disambiguation).**
*Two distinct functions appear in the QOU mass formulae. We must not conflate them:*

| Name | Symbol | Closed form | Behaviour near $z = 1$ |
|---|---|---|---|
| **Quantum dilogarithm product** | $\Phi_q(z)$ | $\prod_{k=1}^{\infty} (1 - q^{-k}z)^{-1}$ | Unbounded ($\Phi_q(0.989) \approx 6.7 \cdot 10^5$ at $q_0$) |
| **Symmetric q-dilogarithm (Kashaev limit)** | $\mathrm{Li}_2^q(z)$ | $\sum_{n \geq 1} \dfrac{z^n}{n \cdot [n]_q}$ | Bounded; $-\mathrm{Li}_2^q(-z) \in [0.1, 0.82]$ for $z \in (0,1)$ at $q_0$ |

*The historical paper-level identity:*
$$
  \Phi_q(z) \;\stackrel{?}{=}\; \int_0^z \frac{\ln_q(1+t)}{t}\,dt
       \;\stackrel{?}{=}\; \prod_{k\geq 1}(1 - q^{-k}z)^{-1}
$$
*is **false**. The integral evaluates to the bounded quantity $-\mathrm{Li}_2^q(-z)$, not the unbounded $\Phi_q(z)$. The two sides differ by six orders of magnitude at $z = 0.989$. We documented the resulting $-737$ MeV mirror-nucleus pathology in the [mass-endomorphism-tower audit](#prop:mass-endomorphism-tower).*

## Discipline

The canonical form of the mass-endomorphism tower uses $-\mathrm{Li}_2^q(-|V|)$, never $\Phi_q(|V|)$, for every per-generator amplitude.

The $\Phi_q$ product form explains the $\sim 10^5 \times$ amplification at $|V| \to 1$ that originally caused the $-737$ MeV pathology. The corrected canonical mass formula abandons it entirely.

## Lean anti-regression class

The Lean stub [`QOU.BraidKnot.QuantumDilogarithm`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/QuantumDilogarithm.lean) provides:

- `phi_q : ℝ → ℝ → ℝ`: Formal noncomputable definition of the product form.
- `li2_q : ℝ → ℝ → ℝ`: Formal noncomputable definition of the symmetric q-dilogarithm.
- `phi_q_ne_li2_q : ¬ (phi_q = fun q z => -li2_q q (-z))`: The two are not equal, breaking the historical identity.
- `towerTerm q V := -li2_q q (-|V|)`: The **corrected** per-generator tower term.
- `class HasCorrectedMassEndomorphismTower`: Type-level discipline. Any instance must use `towerTerm`, not `phi_q`, as the archimedean specialisation.

Combined with the production wiring, this class prevents the $\Phi_q$ pathology from re-entering the mass formula.
<!-- FILE_END: quantum-dilogarithm-disambiguation.md -->

