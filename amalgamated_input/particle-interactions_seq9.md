<!-- FILE_START: atomic-braid-mass-intro.md -->
The transfer matrices of §7 act on the nuclear braid alone. We now attach the electron strands to obtain the full atomic braid and derive the Wedderburn mass formula.
Definition: Atomic braid $H_{A+Z}(q)$ names the $(A+Z)$-strand Hecke algebra carrying $A$ nucleon strands plus $Z$ electron strands. Proposition: LP stability of the atomic braid extends the LP confinement criterion to this larger braid. Proposition: Atomic braid normal form witness supplies the per-atom normal form witness against which we cross-check every mass calculation.

The mass formula proper opens with Conjecture: Seven-term atomic mass formula with $q$-integer coefficients. All seven mass-formula coefficients take the form of $q$-integer products $[n]_q$ times $m_e$, derived from $q_0$ alone. Definition: Universal ILP algorithm for operator selection shows that the same integer linear program drives confinement, gluon, electron-attachment, and molecular-bonding operator selection. Proposition: Neutron--proton mass splitting and Remark: Degree-2 color pairing as binding energy extract the explicit splittings. Remark: Predicted vs observed masses, $Z = 1$--$20$ cross-checks the seven-term formula against AME2020 for $Z \le 20$. Remark: Step-by-step LP stability verification and Remark: Gröbner--Shirshov reduction: methods and reproducibility record the computational procedure.

The structural decomposition behind the mass formula includes four components. Proposition: Nuclear binding energy from the $3$-channel brane tower establishes the 3-channel brane-tower binding decomposition. Proposition: QOU mass formula as descent decomposition of the mass endomorphism covers the descent decomposition into descended-central and exceptional-divisor components. Proposition: Thurston additivity of hyperbolic volume over ideal tetrahedra covers volume additivity over ideal tetrahedra. Conjecture: Mass-volume factorization of the categorical mass endomorphism states the conjectural mass-volume factorization.
Three locality statements supply the perturbative organization of the categorical mass endomorphism by crossing grade: Conjecture: Crossing-graded expansion of the categorical mass endomorphism, Conjecture: Locality of lifted-crossing contributions in the mass expansion, and Remark: Derivation: locality from flatness of the KZ connection.

Remark: Frobenius packing interpretation of the $q$-density reads the $q$-density as a Frobenius-packing measure on Wedderburn blocks. Two propositions derive the CPT-saturated density and its bar-involution invariance from the Type-B folded crystal of §7c: Proposition: CPT-saturation as Type-B fold-orbit closure: deriving $\rho_F \in \{m_e, 2m_e\}$ from crystal structure, and Proposition: Bar-involution invariance of Plancherel weights and Type-B-folded normal forms. 
Several of these propositions appear in two flavors: a generic-ring form over a `CommRing R` and an archimedean specialization over $\mathbb{R}$. We state the generic versions separately so the categorical content applies outside its archimedean context. 
The closing block **Soft confinement level $\ell_*(q_0)$ from Plancherel decay** (rem) packages the Plancherel-decay scale $\ell_*(q_0)$. Section 9 treats this scale as the truncation level for the branching $\mathcal{Q}_q$-value.

_(draft.)_
<!-- FILE_END: atomic-braid-mass-intro.md -->

<!-- FILE_START: atomic-lp-stability.md -->
**Proposition.**
The bare hydrogen atom $[e, \mathfrak{p}] = \sigma_0^{-1}$ in $H_2(q)$ is **LP-unstable**: there exists a Markov-normalised operator $X^* = \alpha \cdot \mathbf{1} + \beta \cdot \sigma_0$ that annihilates the traced volume ($V = 0$).

The $\mathcal{B}_3$ dressing (proton internal structure) **stabilises** the atom. The Borromean braid $(\sigma_1\sigma_2)^3$ is the identity in the standard (degree-2) representation of $H_3(q)$. This changes the annihilation ratio from $\lambda_s/\lambda_a = 0.537$ (bare) to $q^{-10} = 0.352$ (dressed). The original annihilator $X^*$ cannot satisfy the dressed condition, so the atom is stable.

For composite nuclei ($A \geq 2$): nuclear crossings ($\mathfrak{p}\mathfrak{p}$, $\mathfrak{n}\mathfrak{n}$, $\mathfrak{p}\mathfrak{n}$) break the simple $H_2(q)$ structure, providing LP stability without explicit $\mathcal{B}_3$ dressing.
<!-- FILE_END: atomic-lp-stability.md -->

<!-- FILE_START: universal-ilp-algorithm.md -->
**Definition (Universal ILP Algorithm).**
*A single integer linear program selects the operator at every level of the QOU construction. The same Gram matrix $G$, the same Frobenius check $Gx \geq 0$, and the same ILP are applied to quarks, nucleons, atoms, and molecules.*

### Input

- *Current state $x \in H_3(q)$ (normal form vector in the 6-element basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$).*
- *Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ (computed once from the Hecke algebra relations).*
- *Markov traces $t_i = \mathrm{tr}_M(b_i)$.*

### Algorithm

*A single LP handles both unstable and stable states:*

$$
  \min_{K} \; \mathrm{cr}(K) \quad
  \text{s.t.} \quad K \in \{\text{knots}\} \setminus \{1\}, \quad
  G \cdot \mathrm{NF}(x \cdot K) \geq 0
$$

*with objective among feasible $K$: minimise $|\mathrm{tr}_M(x \cdot K)|$ at each crossing number. Select the smallest $\mathrm{cr}(K)$ that satisfies Frobenius positivity.*

*The two constraints are:*

1. **$K$ is a non-trivial knot** — a braid whose closure is a single-component curve, excluding the unknot (identity).
2. **Frobenius positivity** $G \cdot \mathrm{NF}(x \cdot K) \geq 0$ — the resulting state must be LP-stable.

*The unknot is excluded because it leaves the state unchanged ($x \cdot 1 = x$). Among non-trivial knots, the LP minimises crossing number first, then $|\mathrm{tr}_M|$ as tiebreaker.*

- *When the state is **unstable** ($Gx \not\geq 0$): the Frobenius constraint forces a non-trivial $K$ that restores stability. The LP selects the minimum-crossing knot that achieves $Gx' \geq 0$.*
- *When the state is **stable** ($Gx \geq 0$): any non-trivial knot is a candidate. The LP selects the minimum-crossing one, with $|\mathrm{tr}_M|$ minimised as tiebreaker. This is the bond operator.*

*Apply $K$ to the state: $x \leftarrow \mathrm{NF}(x \cdot K)$. Proceed to the next level.*

### Instantiations

| Level | Input | Frobenius | ILP selects | Crossings |
|:------|:------|:----------|:-----------|:----------|
| Quarks $\to$ confinement | uud (3 crossings) | **FAIL** ($Gx[\gamma] < 0$) | $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ | 6 |
| Proton $\to$ gluon | $\mathcal{B}_3 \times$ quarks (9) | **FAIL** ($Gx[\gamma] < 0$) | $\sigma_0 \sigma_0$ | 2 |
| Proton $\to$ H atom | proton + gluon (11) | **PASS** | $\sigma_1^{-1}$ (pe crossing) | 1 |
| H $\to$ H$_{2}$ molecule | H atom | **PASS** | $T_{2,3}^{-1} = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$ | 3 |

*At every level, the algorithm uses the same $6 \times 6$ Gram matrix $G$ and the same Frobenius positivity constraint $Gx \geq 0$. The only difference between levels is the **topological constraint**:*

- *Step 2a (unstable): the operator must be a **braid group element** — any product of generators $\sigma_0^{\pm 1}$, $\sigma_1^{\pm 1}$ that restores stability.*
- *Step 2b (stable): the operator must be a **knot** — a braid whose closure is a single-component curve. The unknot (identity) gives zero binding; the trefoil is the first non-trivial knot.*

### Topological hierarchy

*The topological constraint upgrades at each level:*

- *Level 1 (confinement): the operator must have the **Borromean property** — no proper subset of quarks is separable. This selects $\mathcal{B}_3$ over simpler braids.*
- *Level 2 (gluon): the operator must restore **Frobenius stability** — the minimum crossing fix.*
- *Level 3 (electron): the operator is the **pe crossing** — physically determined by the electromagnetic interaction.*
- *Level 4 (molecule): the operator must be a **knot** — a topologically non-trivial single-component bond. The inverse trefoil $T_{2,3}^{-1}$ is the minimum.*

### Consistency

*We use the same energy functional $\Phi_1 = \ln|\mathrm{tr}_M|$ and the same Wedderburn-Artin weights $(w_s, w_d, w_a) = (q^2, (q^2+1)^2, q^2)/(q^4+4q^2+1)$ at every level. The binding energy is:*

$$
  E_{\mathrm{bind}} = \bigl(\Phi_1^{\mathrm{unbonded}} - \Phi_1^{\mathrm{bonded}}\bigr) \times E_{\mathrm{scale}}
$$

*where $E_{\mathrm{scale}}$ is the appropriate energy unit:*

| Level | $E_{\mathrm{scale}}$ | Expression |
|:------|:--------------------|:-----------|
| Nuclear mass | $m_e$ | Electron mass |
| Molecular binding | $E_{\mathrm{hartree}}/[2]_q^2$ | $m_e \alpha_{\mathrm{EM}}^2 / (q+q^{-1})^2$ |
| $Q$-value | $E_\times \cdot \mu_0$ | $\frac{1}{2}(q-q^{-1}) \cdot \frac{m_e}{3(q-q^{-1})/2}$ |

*All energy scales are derived from $q_0$ and $m_e$ alone.*

**Archimedean specialisation (§7c).**
*This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs, such as real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical or $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.*
<!-- FILE_END: universal-ilp-algorithm.md -->

<!-- FILE_START: gram-matrix-h3-symbolic.md -->
**Proposition (symbolic Hoefsmit Gram on $H_3(q)$).** *Let $u = \sqrt{q}$ with $u > 0$ (equivalently $q > 0$). On the 6-element NF basis*

$$\{1, \sigma_0, \sigma_1, \sigma_0\sigma_1, \sigma_1\sigma_0, \sigma_0\sigma_1\sigma_0\}$$

*the Hoefsmit-seminormal Gram matrix $G(q)$ has the following 21 distinct (by symmetry) entries as Laurent polynomials in $u$:*

| Cell | Value |
|---|---|
| $G[0,0]$ | $1$ |
| $G[0,1] = G[0,2]$ | $u/(u^2+1) = \sqrt{q}/(q+1)$ |
| $G[0,3] = G[0,4] = G[1,2]$ | $u^2/(u^2+1)^2 = q/(q+1)^2$ |
| $G[0,5]$ | $(u^2 + u - 1)/(u^2+1)$ |
| $G[1,1] = G[2,2]$ | $(u^2 + u - 1)/u$ |
| $G[1,3] = G[1,4] = G[2,3] = G[2,4]$ | $(u^2 + u - 1)/(u^2+1)$ |
| $G[1,5] = G[2,5] = G[3,3] = G[4,4]$ | $(u^4 + u - 1)(u^4 + u^3 - 1)/[u^2(u^2+1)^2]$ |
| $G[3,4]$ | $((u^2 + u - 1)/u)^2$ |
| $G[3,5] = G[4,5]$ | $(u^{10} + u^9 - u^8 - u^5 + u^2 + u - 1)/[u^4(u^2+1)]$ |
| $G[5,5]$ | $(u^{12} + u^{11} - 2u^{10} - u^9 + 2u^8 + u^7 - u^6 - u^5 + 2u^4 + u^3 - 2u^2 - u + 1)/u^6$ |

*Then:*
1. *$G(q)$ is symmetric: $G[i,j] = G[j,i]$ for all $i, j$.*
2. *$G[0,0] = 1$.*
3. *$\det G(q) \neq 0$ for $q > 0,\ q \neq 1$.*

## Numerical evaluation at the substrate

Sympy-computed symbolic entries match `computations/gram-matrix-dual.witness.json` at $q_0 \approx 1.110$ to a maximum absolute difference $\approx 2.1 \times 10^{-16}$ across all 36 entries (see `gram-h3-symbolic-regression.witness.json` for the live value). The determinant at $u_0 = \sqrt{q_0}$ is $\det G(u_0) \approx -0.189205253071$. This includes one negative eigenvalue $\approx -0.855$, which shows that Frobenius positivity applies a non-trivial constraint.

## Role in the framework

This proposition delivers the Phase 1b instance of [`def:universal-ilp-algorithm`](universal-ilp-algorithm.md)'s [`HasH3GramMatrix`](universal-ilp-algorithm.lean) typeclass. It replaces the Phase 1a stub (`gram_matrix ≡ 0`) with categorical closed-form entries. Downstream consumers (operator-selection LP, Frobenius-positivity ILP, crystal-weight $\Delta_\lambda(K)$ derivation) can now rely on proven structural properties rather than empirical observation at $q_0$.

The remaining $\det \neq 0$ proof (Phase 1b-2) reduces the Option E Phase 1 workstream to a symbolic-determinant computation.

## Cross-references

- [`def:universal-ilp-algorithm`](universal-ilp-algorithm.md) — consumer of this proposition
- [`docs/audits/-option-e-crystal-weight-delta-lambda.md`](../../../docs/audits/-option-e-crystal-weight-delta-lambda.md) — full Phase 0/1/2/3/4 Option E workplan
<!-- FILE_END: gram-matrix-h3-symbolic.md -->

<!-- FILE_START: color-pairing-binding.md -->
*The color-tube cubic $c^3 + a_2 c^2 + a_1 c + a_0 = 0$ generates four distinct terms. These map exactly to the four photon channels in $\gamma\gamma \to \mathfrak{q}\mathfrak{q}\mathfrak{q}$ production:*

| Degree | Symmetric function | Integral | Physical role |
|:-------|:-------------------|:---------|:-------------|
| 3 | $\prod \mathrm{d}c_k/\mathrm{d}z$ | $I_3$ | confinement $\to m_{\mathfrak{p}}$ |
| 2 | $\sum_{i<j} \mathrm{d}c_i \cdot \mathrm{d}c_j$ | $I_2$ | color pairing $\to$ binding |
| 1 | $\sum \mathrm{d}c_k/\mathrm{d}z$ | $I_1$ | quark sum |
| 0 | $c_0 + z$ | $I_0$ | electron period |

*The degree-2 amplification ratio $A_2/A_3$ rigidly fixes the weight $\beta_2 = -2[3]_q$ in the mass formula. The quantum 3-integer $[3]_q$ emerges because the baryon carries three color channels. The pairwise color interaction is initially weighted by the classical pair count $\binom{3}{2} = 3$, which resolves to $[3]_q$ at finite $q$.*
<!-- FILE_END: color-pairing-binding.md -->

<!-- FILE_START: atomic-nf-witness.md -->
**Proposition.**
*For each atom $(Z, N)$ with $Z = 1$--$20$, the atomic braid
construction produces an element of $H_{A+Z}(q)$ that is verified
to be in Gröbner--Shirshov normal form.  Specifically:*

1. *The ground-state nucleon ordering is the global minimum of
   $\Phi_1$ over all $\binom{A}{Z}$ permutations (exact for
   $\binom{A}{Z} \leq 50000$, steepest :refterm[descent]{#descent} otherwise).*

2. *Each electron is inserted at the position minimizing $\Phi_1$
   (greedy, verified to produce ep pairs adjacent to protons).*

3. *At each construction step (adding strand $k$ with crossings
   to all previous strands $0, \ldots, k-1$): the
   Gröbner--Shirshov reduction is run to convergence
   ([inductive reduction](#prop:inductive-gb-reduction)).  Convergence
   is guaranteed by the Diamond Lemma (the three rewriting rules
   satisfy all overlap ambiguities).*

4. *The final NF element is accumulated without mid-construction
   stripping for $A \leq 9$ (exact).  For $A > 9$, the element is
   stripped at controlled thresholds (200k--500k words) and the
   stripped contributions are accumulated into the Pauli character
   $F_{\mathrm{Pauli}} = |\mathrm{tr}_{\mathrm{alt}}/\mathrm{net}|$.*

5. *Certificates (JSON) are committed to the repository for each
   computed atom.  Each certificate records: $F_{\mathrm{Pauli}}$,
   $\mathrm{tr}_{\mathrm{alt}}(q_0)$, $\mathrm{net}(q_0)$,
   computation time, word count, and engine version.*

*The three Wedderburn invariants $\Phi_1$, $\Phi_2$, $\Phi_3$ used
in the mass formula
([three-invariant mass formula](#thm:wedderburn-mass-formula))
are computed from the transfer matrix chain, which incorporates the
Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + \mathbf{1}$
at each crossing.  The transfer matrix output is in normal form by
construction: the $2 \times 2$ matrix product automatically absorbs
all Hecke reductions into the matrix entries.*
<!-- FILE_END: atomic-nf-witness.md -->

<!-- FILE_START: step-lp-verification.md -->
*We verify each atom to be LP-stable at every construction step. For each strand $k$ added to the braid:*

- *We compute the three Wedderburn channels (symmetric, standard, alternating) independently.*
- *No channel eigenvalue product is zero at any step.*
- *The symmetric and alternating channels maintain distinct signs. This prevents the channel-mixing annihilation that destabilizes the bare hydrogen atom.*

*We verify all $20$ atoms (all pass all-channel-nonzero at every step): ${}^1\mathrm{H}$, ${}^4\mathrm{He}$, ${}^7\mathrm{Li}$, ${}^9\mathrm{Be}$, ${}^{11}\mathrm{B}$, ${}^{12}\mathrm{C}$, ${}^{14}\mathrm{N}$, ${}^{16}\mathrm{O}$, ${}^{19}\mathrm{F}$, ${}^{20}\mathrm{Ne}$, ${}^{23}\mathrm{Na}$, ${}^{24}\mathrm{Mg}$, ${}^{27}\mathrm{Al}$, ${}^{28}\mathrm{Si}$, ${}^{31}\mathrm{P}$, ${}^{32}\mathrm{S}$, ${}^{35}\mathrm{Cl}$, ${}^{40}\mathrm{Ar}$, ${}^{39}\mathrm{K}$, ${}^{40}\mathrm{Ca}$.*

*We verify full LP stability (existence of an annihilator in the complete $H_n(q)$) for ${}^1\mathrm{H}$ (dressed, stable), the proton $\mathfrak{p}$ (stable), and the neutron $\mathfrak{n}$ (stable).*

**Witness**: `atom-mass-complete-wedderburn.witness.json`, Rust certificates in `tools/hecke-engine/certificate-*.json`.
<!-- FILE_END: step-lp-verification.md -->

<!-- FILE_START: groebner-reduction-methods.md -->
We compute the Hecke algebra normal form by iterative Gröbner–Shirshov reduction with three rewriting rules:

1. **Hecke relation** (Rule 0):
   $\sigma_i^2 \to (q - q^{-1})\sigma_i + \mathbf{1}$.
   Reduces word length by 1; produces two output words.

2. **Far commutativity** (Rule 1):
   $\sigma_i \sigma_j \to \sigma_j \sigma_i$ for $|i - j| \geq 2$.
   Permutes generators without changing length.

3. **Yang–Baxter relation** (Rule 2):
   $\sigma_i \sigma_{i+1} \sigma_i \to \sigma_{i+1} \sigma_i \sigma_{i+1}$.
   Applied in the direction that decreases shortlex order.

The reduction is confluent. The final normal form is independent of the order in which rules are applied. The intermediate word count, however, depends critically on the reduction strategy.

## The $H_A$-power factorization

For the $\mathfrak{p}\mathfrak{p}\cdots\mathfrak{n}\mathfrak{n}$ ordering (all protons first, then all neutrons), every normal form coefficient factors as $\pm 2^a \times H_A^k$. Here $a$ counts the number of $\mathfrak{p}\mathfrak{n}$ crossings in the reduction path and $k$ counts the number of Hecke-relation applications. We verify this for ${}^1\mathrm{H}$ through ${}^9\mathrm{Be}$.

The factorization enables a compressed representation. Each word stores only $(\mathrm{sign}, a, k)$ instead of a full Laurent polynomial. For atoms with mixed orderings ($\mathfrak{p}\mathfrak{n}\mathfrak{p}\mathfrak{n}\cdots$), the factorization breaks. The coefficients become general Laurent polynomials.

## Computational engines

Four Rust engines implement the reduction with increasing optimization:

| Engine | Representation | Peak memory | Speed |
|:-------|:---------------|:------------|:------|
| v9 (hecke-bigint) | BigInt polynomial | $O(A!)$ bytes | exact, slow |
| v11 (hecke-modular) | $\mathbb{F}_P$ dense array | $O(A! \times 200)$ bytes | 5$\times$ faster |
| v13 (hecke-stream) | streaming + leading-term cancel | $O(N)$ during reduce | lower peak |
| v14 (hecke-hapower) | sparse $H_A^k$ pairs | $O(A! \times 20)$ bytes | fits ${}^{11}\mathrm{B}$ |

The modular engine uses the Mersenne prime $P = 2^{127} - 1$ with fast Mersenne reduction: $x \bmod P = (x \gg 127) + (x \mathbin{\&} P)$. Modular multiplication uses four $\texttt{u64} \times \texttt{u64} \to \texttt{u128}$ products instead of the $O(128)$-step Russian peasant algorithm.

## LP-dual reduction ordering

Since confluent reductions permit arbitrary rule ordering, the LP dual determines the most efficient strategy:

- **Cancellation-first**. We apply Rule 0 when the shortened word already exists in the stable set. This produces immediate cancellation. It reduces the word count before other rules fire.

- **Leading-term cancellation**. We consolidate pending words before reduction. Words with opposite-sign coefficients on the same basis element cancel without any reduction work (the Buchberger S-polynomial criterion applied to Hecke algebras).

- **Crossing order**. Within the braid construction, the order of crossing multiplication affects intermediate size. Adjacent generators do not commute. Only far-commuting pairs ($|i - j| \geq 2$) may be reordered.

## Reproducibility

All computations are reproducible from the Rust source in `tools/hecke-engine/`. The engine generates certificates (JSON files containing $F_{\mathrm{Pauli}}$, $\mathrm{tr}_{\mathrm{alt}}$, and $\mathrm{net}$ polynomials evaluated at $q_0$) and commits them to the repository. Witness files in `computations/` record every mass prediction with full intermediate values.
<!-- FILE_END: groebner-reduction-methods.md -->

