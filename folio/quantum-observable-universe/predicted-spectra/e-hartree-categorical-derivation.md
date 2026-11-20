> **Superseded.** The scalar substrate density $\rho_q = 1/\hbar_q^2$ used below is
> the structurally-wrong leading-order ansatz; the operator-valued form supersedes
> it ([`mass-endomorphism-tower`](../mass-theory/mass-endomorphism-tower.md)). The canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$ graded expansion [`prop:rho-k-graded-expansion`](../mass-endomorphism/rho-k-graded-expansion.md).

The molecular-binding framework uses the Hartree energy $E_h = m_e c_q^{2}\,\alpha_{EM}^{2}$ as a conversion scale. The question is whether the $\alpha_{EM}^{2}$ factor arises from QOU/Hecke structure rather than as an empirical input. The result is a **clean conditional theorem**.

**Conjecture (corrected headline form).** *For a covalent diatomic with definite-parity ground state, the bound-state contribution on the EM Wedderburn channel $(2,2)$ of the molecular Markov trace carries the fine-structure scale exactly:*

$$
  \rho_{(2,2)}
  \;=\;
  \frac{\chi_{(2,2)}^{\mathrm{dressed}}}{\bigl(q\,[9]_q\,[10]_q\bigr)^{2}}
  \;=\;
  C(q)\,\alpha_{EM}^{2},
  \qquad
  C(q) \;=\; h\,\bigl(\dim_q V_{(2,2)}\bigr)^{2},
$$

*Here $\alpha_{EM} = 1/(q\,[9]_q\,[10]_q) \in R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$. The categorical coefficient $C(q)$ is the EM-block Plancherel-square, not a free parameter. The archimedean evaluation of $\rho_{(2,2)}$ up to the CAL-1 energy unit $m_e c^{2}$ is $E_h = m_e c_q^{2}\,\alpha_{EM}^{2}$.*

> **Historical framing.** The investigation opened from a weaker $J^{1}$-vanishing claim about the Markov-layer LP dual $y_{\mathrm{cov}} = c_2\,\alpha^{2} + O(\alpha^{4})$. The separated-atom point is a kink. Therefore $y_{\mathrm{cov}}$ is $O(\alpha)$, not $O(\alpha^{2})$. The $\alpha^{2}$ scaling is real but lives in the q-dimension layer, not the Markov layer. The trace-ratio above is the live statement; the $y_{\mathrm{cov}}$ form is superseded.

## Status: a conditional theorem

Every mechanism question is resolved. The coupling-parity routes are refuted. The $\alpha_{EM}^{2}$ scaling is exact in $R$. The archimedean realisation is the known $q_0$-evaluation / Bloch–Suslin pairing. The $(2,2) = \mathrm{EM}$ channel is grounded in the covalent-pair structure. The statement is not closed. By the framework's three-calibration design, the statement cannot be unconditional. The energy unit $m_e c^{2}$ is CAL-1. The residual contains exactly three named items:

1. **The $(2,2) = \mathrm{EM}$ identification.** The channel $(2,2)$ is the unique self-transpose summand of $\mathrm{Ind}_{S_2\times S_2}^{S_4}(\mathrm{sgn}\boxtimes\mathrm{sgn})$. This rests on the physical input that a covalent bond equals two EM singlets.
2. **The $m_e c^{2}$ CAL-1 unit.** This is not provable by design.
3. **The $\alpha^{2}$ magnitude algebra.** The squared force-carrier complexity normaliser sets the physical energy. The $\alpha^{2}$ scaling is exact. The magnitude remains conditional. It rests on the covalent Pauli-2 reuse of the bare EM complexity.

## Rigorous results

1. **The bare LP/SDP framework.** The $H_2$ molecular braid and its primal/dual program are set up rigorously in [LP dual binding](#prop:h2-lp-dual-binding) and [ILP covalent bond](#prop:ilp-covalent-bond). Strong duality ([operator-selection LP](#prop:operator-selection-lp)) gives $y_{\mathrm{cov}}^{*}$ as the binding energy per shared electron.

2. **The bare formula.** The singlet-idempotent / Bring force-carrier complexity ([EM coupling projection](#prop:em-coupling-projection)) rigorously derives the leading expression $1/\alpha_{EM} = q\,[9]_q\,[10]_q$. It lies in $R$. It admits the equivalent shift-exponent form $1/\alpha_{EM} = q \cdot [\alpha_{\mathrm{shift}}(T_{2,9})]_q \cdot [\alpha_{\mathrm{shift}}(T_{3,5})]_q$ ([multiplicative-chain form](#prop:alpha-em-shift-multiplicative-chain)). This exposes the same combinatorial primitive that controls the atomic-shift framework. The primitive is the pole order at $q = 0$ of a seminormal Hecke trace.

3. **The Frobenius / curvature-rank decomposition.** The Gröbner–Shirshov spectral sequence collapses at $E_1$ ([spectral sequence collapse](#prop:spectral-sequence-collapse)). The molecular operator decomposes by curvature rank ([curvature-rank GB stratification](#prop:curvature-rank-gb-stratification)). The covalent bond shares two electrons through two crossings. It sits at curvature rank $2$.

4. **Closed-form dressed characters.** All five irrep characters of the bare $H_2$ braid $\sigma_1\sigma_2\sigma_3 \in B_4$ are single $q$-monomials (See [Table 12](#tbl:e-hartree-categorical-derivation-table12-data)). The force-carrier sum is $\chi_{(3,1)} + \chi_{(2,1,1)} = -q + q^{-1} = -h$. Replacing the middle crossing with the K-shell-dressed $T^{\mathrm{dr}}$ with eigenvalues $q^{5}, -q^{-5}$ activates the $(2,2)$ channel. This breaks the bare $(2,2) = 0$ selection rule. It amplifies the force-carrier channel by $\approx [5]_q$ (See [Table 13](#tbl:e-hartree-categorical-derivation-table13-data)). This is the algebraic signature of the dressing power.

### Mechanism A — Pauli / two-electron combinatorial counting

A covalent bond shares exactly two electrons via Pauli exclusion and singlet pairing. In the Hecke braid representation, each shared electron contributes one crossing operator. The covalent operator $L_{\mathrm{cov}}$ is bilinear in Hecke generators: $L_{\mathrm{cov}} = \sigma_{i}\,\sigma_{j} + (\text{symmetrisation})$. If each Hecke crossing entering the operator-selection LP carries weight $\alpha_{EM}$, then $L_{\mathrm{cov}} \sim \alpha_{EM}^{2}$. The Markov trace inherits the $\alpha_{EM}^{2}$ leading order.

**Gap.** Each EM-mediating crossing must carry exactly one factor of $\alpha_{EM}$ in the LP-dual expansion. The bare formula $1/\alpha_{EM} = q\,[9]_q\,[10]_q$ is the operator-selection weight of a single force-carrier knot. It is not a per-crossing factor. Translating between per-knot weight and per-crossing factor requires an unestablished multiplicative-decomposition lemma.

### Mechanism B — quadratic-form structure of the Frobenius LP

The molecular SDP is a quadratic program over the Frobenius Gram matrix (**convention D**: read on the quotient $H_n/\mathrm{rad}\,\mathrm{tr}_M \cong \mathrm{TL}_n$, where the induced pairing is non-degenerate; on $H_n$ itself $\det G = 0$ exactly, the $(1^3)$ block being the radical) ([Knot operator selection as linear program with LP duality](#prop:operator-selection-lp), dual program). A single perturbation $\varepsilon$ turns on the covalent constraint in the quadratic primal. The Legendre/Schur-complement dual is $y_{\mathrm{cov}}(\varepsilon) = \tfrac{1}{2}\varepsilon^{2}\,(G^{-1})_{\mathrm{cov,cov}} + O(\varepsilon^{4})$. If $\varepsilon \propto \alpha_{EM}$, this gives $y_{\mathrm{cov}} \propto \alpha_{EM}^{2}$ with no linear term.

**Gap.** The bare separated-atom configuration must be a smooth interior point. The covalent constraint must be active at $\varepsilon = 0$ as an equality. In practice, the activation is a kink. The dual $y_{\mathrm{cov}}$ jumps non-smoothly. The linear coefficient is generically non-zero. A rigorous version requires the bare atoms to saturate the Frobenius-pairing equality. This is not verified. It is the source of the refutation of the $y_{\mathrm{cov}}$ form.

### Mechanism C — parity / antipode invariance of the Markov trace

The antipode $S$ of the Iwahori–Hecke algebra acts by $S(\sigma_i) = \sigma_i^{-1}$. The Markov trace is $S$-invariant. For a definite-parity ground state, the molecular braid is $S$-equivariant up to Markov equivalence. This would force a parity selection rule eliminating odd powers of $\alpha_{EM}$.

**Gap.** The antipode acts on the substrate parameter as $S(\alpha_{EM}) = \alpha_{EM}\bigl|_{q \mapsto q^{-1}} = q^{2}\,\alpha_{EM}$. This is a multiplicative scaling, not a sign flip. The quantum integer $[n]_q$ is palindromic, but the $q^{-1}$ prefactor is not. Therefore, $S$-invariance imposes the functional equation $f(\alpha_{EM}) = f(q^{2}\alpha_{EM})$. This does not force odd powers to vanish. A coupling-parity rule requires a different involution flipping the sign of $\alpha_{EM}$. No such involution exists.

### Mechanism D — virial / scaling (the route that survives)

Dimensional analysis at the Bohr radius $a_0 \sim 1/(m_e c \alpha)$ governs the $\alpha^{2}$ scaling of $E_{\mathrm{Hartree}}$. The kinetic energy $T \sim \hbar^{2}/(m_e a_0^{2})$ and Coulomb energy $V \sim e^{2}/a_0$ both scale as $m_e c^{2}\alpha^{2}$. The virial theorem balances them. The QOU analogue is a virial/scaling argument, not a parity argument. At the bound-state LP/SDP optimum, the molecular Markov trace decomposes into two contributions. Both scale as $\lambda_{\mathrm{bound}}^{-2}$. Here $\lambda_{\mathrm{bound}}$ is the characteristic eigenvalue of the molecular transfer matrix ($T_1 = T_{e_2 \mathfrak{p}_2}^{\mathrm{dressed}}$ in [LP dual gives optimal $H_2$ binding](#prop:h2-lp-dual-binding), with eigenvalues $q^{5}, -q^{-5}$). The inverse $\lambda_{\mathrm{bound}}^{-1}$ is the categorical analogue of $\alpha_{EM}$. The leading order is $\alpha_{EM}^{2}$ by dimensional matching. There is no linear term to suppress. Thus $J^{1}$-vanishing is not a theorem to prove. It is a consequence of the LP/SDP being quadratic in the bound-state scale. The conjecture sharpens to the claim that $\lambda_{\mathrm{bound}}^{-1} \in R$ and $\lambda_{\mathrm{bound}}^{-1}(q_0) = \alpha_{EM}(q_0)\,c_1$ for some $c_1 \in R$ of order unity. This is a direct symbolic computation (See [Table 11](#tbl:e-hartree-categorical-derivation-table11-data)). The $H_2$ computation gives the dimensionless ratio $E_{\mathrm{bind}}/E_{\mathrm{Hartree}} \approx 0.170$. This is of order unity. It matches the standard-physics $H_2$ ratio $\approx 1/6$. This is consistent with Mechanism D without any $J^{1}$-vanishing miracle.

## Absence of a coupling-level involution flipping $\alpha_{EM}$

Direct calculation rules out any involution $\iota$ of $R$ other than $q \leftrightarrow q^{-1}$ flipping the sign of $\alpha_{EM}$. All four automorphisms generated by $q \mapsto \pm q^{\pm 1}$ fail to flip the sign (See [Table 10](#tbl:e-hartree-categorical-derivation-table10-data)). Using $[n]_{-q^{\pm 1}} = (-1)^{n+1}[n]_q$, the sign factors from $q$ and $[10]_q$ cancel. None of the four maps $\alpha_{EM}$ to $-\alpha_{EM}$. This is a structural obstruction. The parameter $\alpha_{EM}$ is a positive scalar on the relevant component of the substrate variety. No positivity-preserving automorphism of $R$ flips its sign. A coupling-parity selection rule of the form "$f(\alpha_{EM}) = f(-\alpha_{EM}) \Rightarrow$ odd terms vanish" cannot be implemented by any Galois-style involution.

The viable analogue is operator-parity, not coupling-parity. The standard linear-Stark vanishing $\langle\psi_0|\hat r|\psi_0\rangle = 0$ makes the operator the parity-odd object. The categorical version seeks a $\sigma$-antisymmetric Hecke perturbation $\Delta_{\mathrm{cov}}$. This is built from $\sigma_i - \sigma_i^{-1}$ skein factors. A categorical parity rule requires $\Phi_1(\mathcal{M}_{\mathrm{atom}} \cdot \Delta_{\mathrm{cov}}) = 0$. This leaves an $\alpha_{EM}^{2}$-scaled second-order contribution. This aligns with how [antiparticle crossing reversal](#prop:antiparticle-crossing-reversal) realises $\sigma$ at the operator level.

## Companion remark — physical translation

In standard non-relativistic QED, $E_h \propto \alpha_{EM}^{2}$ because both kinetic energy and Coulomb potential are quadratic in $1/a_0 \propto \alpha_{EM}$. The virial theorem balances them at $E = -\tfrac{1}{2}V \propto \alpha_{EM}^{2}$. The $\alpha_{EM}^{1}$ contribution is the linear Stark shift. This vanishes in any definite-parity state by symmetry of the electric-dipole matrix element. A categorical proof requires identifying the categorical analogue of that linear-Stark vanishing. The QOU analogue of charge-conjugation parity is [antiparticle crossing reversal](#prop:antiparticle-crossing-reversal).

## Items still missing for closure

A genuinely categorical derivation of the $\alpha_{EM}^{2}$ scaling requires three concrete items:

1. **A Hecke-algebraic definition of $\Phi_1^{\mathrm{kin}}$ and $\Phi_1^{\mathrm{Coul}}$.** These must be distinct, computable components of the molecular Markov trace. The current LP/SDP framework does not separate them.
2. **A proof that these contributions balance at a specific categorical length.** This must derive from Hecke structure, not transported dimensional analysis. It requires a symbolic $q$-polynomial recompute of the optimal $\Phi_1^{H_2}(\pi^{*})$ tracking each crossing-type separately.
3. **An independent derivation of the archimedean energy unit per $\Phi_1$.** This must derive from algebraic structure. It cannot assume a match with QED in the $q \to 1$ limit. This deepest layer requires a functorial uniqueness statement about $\rho_\infty$ verifiable without experimental Hartree values.

## Non-claims

- No proof of $E_h \propto \alpha_{EM}^{2}$ from QOU principles is claimed. It claims only that this scaling is the expected leading behaviour. It identifies the open structural step. - No $\pi$, transcendentals, or PSLQ-fitted constants are introduced. The coefficient $c_2$ is conjecturally in $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$. - The existing usage of $E_{\mathrm{Hartree}} = m_e c^{2}\,\alpha_{EM}^{2}$ as a numerical scale is not overridden.

## Honest reporting

Three derivation mechanisms are recorded above. Each has an explicit identified gap. The operator-parity sharpening of Mechanism C and the virial-scaling Mechanism D are the two surviving lines of attack. Reporting the partial chain is deliberate. Post-hoc numerical identifications are avoided.

## Supporting data tables

Tables 1–13 collect the intermediate symbolic computations of the investigation. Tables 10–13 support the rigorous results and mechanisms above. Tables 1–9 record the intermediate data of the successive attempts.

---

What follows carries the distilled conditional theorem, the rigorous results, and the open closure programme; the intermediate candidate mechanisms, and how each was ruled out or sharpened, are not reproduced here.
