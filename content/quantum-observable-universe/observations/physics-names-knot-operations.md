**Remark (physics names are q₀-dependent labels for categorical knot operations).**

*The names that physicists give to phenomena (alpha particle, gluon
condensate, valence shell, isospin, etc.) are convenient labels for
recurring **categorical structures** in the Hecke algebra
$H_n(R, q)$ at the substrate parameter $q_0$.  The categorical structure
is fundamental; the physics naming is a derived mapping that depends on
which value of $q_0$ instantiates the substrate.*

*This table records the current mapping at $q_0 \approx 1.10998$.  At
a different substrate value the categorical structures persist but
their physics interpretations may differ — the recurring sub-blocks
identified by the discovery cache
([cite knot-operation-cache.json](#))
acquire different macroscopic meaning when $q_0$ changes.*

| Physics name | Categorical structure | Block kind | Depends on $q_0$? | Reference |
|---|---|---|---|---|
| Quark (up, down) | Strand of the canonical Borromean baryon $T_p, T_n \in H_3(R, q)$ | NF basis element | Definition only | [borromean-baryon](#def:borromean-baryon) |
| Proton / neutron | Closed 3-strand Borromean braid in $H_3(R, q)$ at curvature-rank 0 | $\Lambda_0$ Wedderburn block | Through $\dim_q V_{(3)}$ | [borromean-baryon-interpretation](#rem:borromean-baryon-interpretation) |
| Alpha particle ($^4$He) | Closed-shell sub-block: $\beta_\alpha = $ tensor of 4 baryon NFs in $H_{12}(R, q)$ at curvature-rank 3 | $\Lambda_3$ chirality cell | Through Plancherel weight $w_{(3,3,3,3)}$ | [chirality-residue-mass-term](#prop:chirality-residue-mass-term) |
| Gluon octet | Curvature 2-cocycle at depth 2 with $S$-eigenvalue $+1$ in symmetric channel | $\Lambda_2$ symmetric channel | Through $\dim \mathfrak{su}(3) \cdot q$ | [gauge-coupling-uniqueness](#cor:gauge-coupling-uniqueness) |
| Photon (force-carrier sector) | $T_{2,9} \oplus T_{3,5}$ — the unique pair of genus-4 torus knots | $\Lambda_4$ singlet sub-block | Through $[9]_q \cdot [10]_q$ | [force-carrier-bring-uniqueness](#prop:force-carrier-bring-uniqueness) |
| Electron | $\sigma_1^{-1}$ insertion on the atomic braid at the leading strand | $\Lambda_1$ correction | Through $1/q$ Hecke eigenvalue | [electron-shell](#def:electron-shell) |
| Pauli weight (sym vs alt) | Ratio of trivial-block ($\Lambda_0$) to alternating-block ($\Lambda_{n-1}$) traces | Cross-stratum ratio | Through $q^n$ vs $q^{-n}$ Markov scaling | [pauli-factor-wedderburn](#prop:pauli-factor-wedderburn) |
| Wigner $np$-pairing | Self-conjugate restricted weight at $\Lambda_3$ chirality cell | Chirality sub-stratum | Through Wedderburn projection on $c_\lambda = 0$ | [mass-tower-coefficient-stratification](#prop:mass-tower-coefficient-stratification), [chirality-residue-mass-term](#prop:chirality-residue-mass-term) |
| Color confinement | Spectral-sequence collapse to centre $Z(H_n(R, q))$ — chirality channel = gauge-invariant background | $D_q^2 = 0$ kernel | Through $D_q^2(\lambda) = (q^{c_\lambda} - q^{-c_\lambda})^2 / (q - q^{-1})^2$ | [confinement-categorical](#prop:confinement-categorical), [rem:confinement-curvature-rank](#rem:confinement-curvature-rank) |
| CP-violation discriminant | Imaginary part of alternating/symmetric character ratio under complex substrate $q$ | Cross-channel imaginary part | Through analytic continuation $q \to q e^{i\theta}$ | [cp-violation-spectral-form](#conj:cp-violation-spectral-form) |
| Newton's constant $G$ | Universal-residue prefactor $m_e \cdot 8 G$ at the deep-tower mass stratum $\mathfrak{m}^{\geq 4}$ | $\Lambda_{\geq 4}$ universal tail prefactor | Through Plancherel-weighted asymptotic | [gravity-spectral-prefactor](#prop:gravity-spectral-prefactor) |

**How the table is generated.**

*The discovery cache (`folio-assistant/computations/knot-operation-cache.json`,
populated by SDP / shadow-price analysis on Hecke Wedderburn blocks)
records each recurring categorical structure as a key.  The lookup
`physics-names.json` maps cache keys to physics names at the current
$q_0$.  Both are version-controlled artifacts; the categorical cache
keys are the source of truth, the physics names are the human-facing
display layer.*

**Substrate dependency.**

*Several entries above carry "Depends on $q_0$" annotations.  These
indicate that:*

- *the `dim_q V_λ` factor evaluates to a $q_0$-dependent number;*
- *the recurring sub-block is identified at the **algebraic level**
  (categorical structure independent of $q_0$) but its **numerical
  weight** depends on $q_0$;*
- *at a different $q_0$, the same sub-block exists but may have
  different Plancherel weight, possibly even vanishing weight (in
  which case the corresponding "physics name" no longer applies).*

*The "alpha particle" identification, for instance, requires
$w_{(3,3,3,3)}(q_0)$ to dominate the depth-3 chirality cells of $H_{12}$
— at $q_0 \approx 1.10998$ this weight is $\sim 0.024$, the largest
contribution at depth 3.  At $q_0 = 1$ (classical limit), the weight
becomes the symmetric-group Specht-module dimension squared over
$12!$, with different ranking — the "alpha particle" identification
must be re-derived.*

*Remark.* This table is the **interface** between the categorical machinery
(`prop:em-spectral-completeness`, `prop:gauge-coupling-uniqueness`,
`prop:chirality-residue-mass-term`, etc.) and the physics-language
predictions in this chapter.  It will grow as the discovery cache
identifies further recurring structures.  Every physics name in this
chapter that does **not** appear in this table is either an external
empirical reference (CODATA, AME) or a forward reference to a
later definition.*
