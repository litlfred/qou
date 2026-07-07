<!-- FILE_START: intro-confined-particles-shells.md -->
We now identify the confined particles—the categorical states that survive confinement—and arrange them into shells. The shell structure is forced by the categorical Frobenius positivity condition. A particle confined at level $\ell$ sits in the $\ell$-th shell exactly when the Frobenius pairing on its braid word is positive.

We define the confined particles and index their shells. We build a small library of explicit shells (the substrate-level analogues of the atomic $1s, 2s, 2p, \dots$ shells). Finally, we identify the shells of the lightest mesons and nucleons. This connects the indexing to the Hopf-fibration torus-knot factorization from the stable-nucleus section.
<!-- FILE_END: intro-confined-particles-shells.md -->

<!-- FILE_START: confined-particle.md -->
**Definition.**
*A **confined particle** is a tuple*

$$
  P \;=\; (\mathrm{name},\ \ell,\ [K]_M,\ n_0)
$$

*where:*

1. *$\mathrm{name}$ is a symbol drawn from a fixed registry of particle shortcuts (e.g., `quark`, `proton`, `neutron`, `electron`, `\He4`, `\C12`, `\benzene`). (The shortcut registry provides authoring convenience; we defer a formal `def:particle-shortcut` block as it does not affect this definition).*
2. *$\ell \in \mathbb{Z}_{\ge 0}$ is the **confinement level** (quark = 0, nucleon = 1, atom = 2, molecule/compound = 3, $\ldots$).*
3. *$[K]_M$ is the **Markov-equivalence class** of a closed braid $K$—the class of $K$ under braid-group conjugation and Markov stabilisation. It is represented canonically by the **Gröbner–Shirshov normal form** of its associated Hecke element $T_w \in H_{n_0}(q)$.*
4. *$n_0$ is the **coarse strand count** at level $\ell$: the minimal number of strands needed to express $K$ as a closed braid at its own level, independent of any deeper unfolding.*

*The class $[K]_M$ is not intrinsically confined at any particular $q$. Confinement is a $q$-indexed predicate $\mathrm{confined}(P, q)$ that holds if and only if the matrix Frobenius PSD cone admits a feasible $\Phi^* \succeq 0$ ([confinement SDP](#prop:confinement-sdp)). A confined particle is **stable at $q$** if and only if it is additionally Frobenius-non-degenerate there ([topological confinement](#prop:confinement-topological)). Unstable species (e.g., $^3\mathrm{H}$, transient hadronic resonances) are confined particles for all $q$ in the generic locus even though their decay channels are open.*

**Canonical representative.**
*Among all closed-braid words in $[K]_M$, we choose the one with the shortlex-minimal Gröbner–Shirshov normal form as the canonical representative $\mathrm{GS}(P)$. We compute the witness data $k_{\max}(P, q)$ ([confinement level](#def:confinement-level)) on this representative. Two particles are equal if and only if their names are equal, which occurs if and only if $\mathrm{GS}(P_1) = \mathrm{GS}(P_2)$.*

**Examples.**

- *`quark`: $\ell = 0$, $n_0 = 1$, $[K]_M = [\sigma_0]$ in $H_1(q)$.*
- *`neutrino`: $\ell = 0$, $n_0 = 1$, $[K]_M = [\mathbf{1}]$ (unknot $0_1$, no crossings). Confined and stable at $q_0$ (vacuum-drag particle); the Frobenius-PSD cone is satisfied by definition since $\Phi^* = \mathbf{1} \succeq 0$.*
- *`photon`: $\ell = 0$, $n_0 = 4$, $[K]_M = [\mathbf{1}_{B_4}]$ (four-strand identity in $B_4$, no crossings; four polarisation $\times$ chirality components on the exceptional divisor $\mathcal{S}_p$). Confined at $q_0$ via the Reeb-bundle holonomy ([breit-wheeler-vertex](#rem:breit-wheeler-vertex)); see notation discussion in [knot-particle-dictionary](#rem:knot-particle-dictionary) Table 3.*
- *`proton`: $\ell = 1$, $n_0 = 3$, $[K]_M = [B_3(\mathrm{uud})]$ with crossing types $(pp, pn, pn)$.*
- *`neutron`: $\ell = 1$, $n_0 = 3$, $[K]_M = [B_3(\mathrm{udd})]$.*
- *`electron`: $\ell = 1$, $n_0 = 2$, $[K]_M = [\sigma_1^3]$ (trefoil $3_1$).*
- *`\He4`: $\ell = 2$, $n_0 = 4$ nucleons, $[K]_M$ determined by the canonical ILP ground-state configuration for $(Z,N)=(2,2)$.*
- *`\benzene`: $\ell = 3$, $n_0 = 6$ atom-strands (six C-atoms in an aromatic ring).*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs: real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: confined-particle.md -->

<!-- FILE_START: confinement-category.md -->
**Definition.**
*The **confinement category** $\mathbf{Conf}$ has:*

- ***Objects:** [confined particles](#def:confined-particle) $P$ at every level $\ell \ge 0$ (quark, nucleon, atom, compound).*
- ***Morphisms:** structure-preserving maps organised into three families:*

| *Family* | *Symbol* | *Action* |
|---|---|---|
| *Unfolding* | $\uparrow_\ell$ | *Replace each level-$\ell$ strand by its level-$(\ell-1)$ constituent braid* |
| *Folding* | $\downarrow_\ell$ | *Quotient a subbraid at level $\ell-1$ to a single level-$\ell$ strand* |
| *Dressing* | $\mathrm{dress}$ | *Extend $H_n(R, q) \hookrightarrow H_{n+m}(q)$ and attach $m$ additional strands via an SDP-feasible binding subword* |

- ***Composition:** concatenation of Hecke-algebra embeddings. We right-compose $\mathrm{dress}$ with $\uparrow_\ell$ and $\downarrow_\ell$.*
- ***Identity:** the identity embedding $\mathrm{id}_P: H_{n_0}(q) \hookrightarrow H_{n_0}(q)$.*

*Unfolding and folding are mutually inverse when restricted to particles whose coarse representation captures the full partition content ([level sufficiency](#prop:level-sufficiency)). The morphism $\mathrm{dress}$ is generally not invertible because the binding subword may not be uniquely reversible.*

**Functoriality of the Markov trace.**
*The Markov trace $\mathrm{tr}_M$ extends to a functor*

$$
  \mathrm{tr}_M: \mathbf{Conf} \to \mathbb{C}(q)
$$

*sending every confined particle to its trace value and every morphism to the induced trace transformation. By [level sufficiency](#prop:level-sufficiency), $\mathrm{tr}_M$ is invariant under $\uparrow_\ell$ and $\downarrow_\ell$. Under $\mathrm{dress}$, it multiplies by the binding weight determined by the [confinement SDP](#prop:confinement-sdp) active support.*

**Example: The atomic chain.**
*The chain $\mathrm{quark} \xrightarrow{\downarrow_1} \mathrm{nucleon} \xrightarrow{\downarrow_2} \mathrm{atom} \xrightarrow{\mathrm{dress}} \mathrm{neutral\ atom} \xrightarrow{\downarrow_3} \mathrm{molecule}$ is a composite morphism in $\mathbf{Conf}$ taking free quarks to a bonded molecule by successive foldings and one dressing (the electron shell). Each arrow preserves or extends the Markov trace according to the functoriality rule above.*
<!-- FILE_END: confinement-category.md -->

<!-- FILE_START: dressed-particle.md -->
**Definition.**
*Let $P_{\mathrm{bare}}$ be a [confined particle](#def:confined-particle) at level $\ell$ (typically a bare nucleus, $\ell = 2$). Let $S = (\{e_k\}, \iota, W_{\mathrm{bind}})$ be an electron shell of multiplicity $Z$ attached to it. The **dressing morphism** at $S$ is the arrow in the [confinement category](#def:confinement-category):*

$$
  \mathrm{dress}_S\,:\;P_{\mathrm{bare}}\;\longrightarrow\;P_{\mathrm{dressed}}
$$

*This morphism sends $P_{\mathrm{bare}}$ to the **dressed particle**:*

$$
  P_{\mathrm{dressed}}
  \;=\;
  \bigl(
    \mathrm{name}(P_{\mathrm{bare}}) \oplus \mathrm{name}(S),\;
    \ell,\;
    [\iota(K_{\mathrm{bare}}) \cdot W_{\mathrm{bind}}]_M,\;
    n_0 + Z
  \bigr)
$$

*Here $\mathrm{name}(S)$ is the shell label (e.g. `[He]`, `[Ne]`, `[Ar]`), $[\ \cdot\ ]_M$ denotes Markov equivalence, and the composite braid lives in $H_{n_0 + Z}(q)$ via the cabling embedding.*

**Examples.**

- *Bare proton $\xrightarrow{\mathrm{dress}_{[1s^1]}}$ neutral hydrogen ${}^1\mathrm{H}$.*
- *Bare $^4$He-nucleus $\xrightarrow{\mathrm{dress}_{[1s^2]}}$ neutral helium (noble gas, $Z = 2$).*
- *Bare $^{20}$Ne-nucleus $\xrightarrow{\mathrm{dress}_{[1s^2 2s^2 2p^6]}}$ neutral neon (noble gas, $Z = 10$).*

**Composition.**
*Dressing is not generally invertible. Stripping electrons changes the binding subword via the SDP. However, dressings compose:*

$$
  \mathrm{dress}_{S_2} \circ \mathrm{dress}_{S_1}
  \;=\;
  \mathrm{dress}_{S_1 \oplus S_2}
$$

*Here $\oplus$ concatenates shell data when the combined $Z$ remains SDP-feasible. Partial dressing ($0 < Z' < Z_{\max}$) yields **ions**.*

**Stability under dressing.**
*By [shell-closure stability](#prop:shell-closure-stability), the Frobenius-stability index of $P_{\mathrm{dressed}}$ is monotonically non-decreasing along the dressing chain toward closed-shell noble-gas configurations ($Z \in \{2, 10, 18, 36, 54, 86\}$). Each shell closure is a $\mu \ge 2$ multi-operator fixed point of the SDP. Breaking the bond requires simultaneously breaking every tight dual block. Noble-gas objects are therefore **local terminal objects** of the dressing sub-diagram of $\mathbf{Conf}$.*

**Functoriality of the Markov trace.**
*Under dressing, the Markov trace transforms as:*

$$
  \mathrm{tr}_M(P_{\mathrm{dressed}})
  \;=\;
  \mathrm{tr}_M(P_{\mathrm{bare}}) \cdot
  \prod_{\lambda \in \mathcal{S}^*(S, q)} w_\lambda^{\,\langle \pi_\lambda, \Phi^* \rangle}
$$

*Here $\mathcal{S}^*(S, q)$ is the SDP active support and $w_\lambda$ are the block shadow prices. For $\mu(S, q) = 1$, this collapses to the scalar-LP product. For $\mu \ge 2$, the full matrix shadow contributes. This constitutes the multi-operator binding regime.*
<!-- FILE_END: dressed-particle.md -->

<!-- FILE_START: shell-closure-stability.md -->
**Proposition.**
Fix a bare nuclear [confined particle](#def:confined-particle) $P_{\mathrm{bare}}$ at level $\ell = 2$ with atomic number $Z_{\max}$. Consider the dressing chain in the [confinement category](#def:confinement-category):
$$
  P_{\mathrm{bare}}
  \;\xrightarrow{\mathrm{dress}_{S_1}}\;
  P^{(1)}
  \;\xrightarrow{\mathrm{dress}_{S_2}}\;
  P^{(2)}
  \;\xrightarrow{\mathrm{dress}_{S_3}}\;
  \cdots
  \;\xrightarrow{\mathrm{dress}_{S_{Z_{\max}}}}\;
  P^{(Z_{\max})},
$$
where $P^{(Z)}$ is the dressed particle with $Z$ attached electrons ([dressed particle](#def:dressed-particle)). Let $\sigma_F(P^{(Z)}, q)$ denote the **Frobenius stability index**, the optimal dual objective value of the [confinement SDP](#prop:confinement-sdp) at $P^{(Z)}$:
$$
  \sigma_F(P, q)
  \;:=\;
  n_{\mathrm{target}} \cdot u_0^*(P, q),
$$
where $u_0^*(P, q)$ is the optimal shadow price of the normalisation constraint. By strong duality (Slater's condition holds at generic $q$ since $\Phi = \mathrm{id}/\mathrm{tr}(\mathrm{id})$ is strictly feasible), $\sigma_F(P, q)$ coincides with the optimal primal objective $\langle T, \Phi^*(P, q) \rangle$ and with the minimum-action Markov-trace weight of the confined operator. Then:

1. **Monotonic non-decrease.** $\sigma_F(P^{(Z)}, q)$ is non-decreasing in $Z$ along the dressing chain for every $q$ in the generic locus.

2. **Marginal gain maxima.** The marginal stability gain $\Delta\sigma_F(Z) := \sigma_F(P^{(Z)}, q) - \sigma_F(P^{(Z-1)}, q)$ attains a strict local maximum at each categorical shell closure, where the binding multiplicity satisfies $\mu(S_Z, q) \ge 2$. While $\sigma_F$ is monotone non-decreasing, its derivative $\Delta\sigma_F$ peaks. The categorical closures occur precisely at the cumulative dimensions $\{2, 10, 28, 60, \ldots\}$ of the representation sequence.

3. **Terminality.** For every closure index $Z \in \{2, 10, 28, 60, \ldots\}$, $P^{(Z)}$ is a local terminal object of the dressing sub-diagram. Any outgoing arrow $\mathrm{dress}_{S'}: P^{(Z)} \to P'$ requires simultaneously breaking $\mu(S_Z, q) \ge 2$ tight dual blocks of the confinement SDP.
<!-- FILE_END: shell-closure-stability.md -->

<!-- FILE_START: shell-closure-stability-interprets.md -->
**Remark.**
[Shell-closure stability](#prop:shell-closure-stability) gives a categorical origin for stable dressing sequences in the confinement category.

1. **Periodicity.** Dressing $\mathrm{dress}_{S_Z}: P^{(Z-1)} \to P^{(Z)}$ traces a chain in the confinement category. The Frobenius stability index $\sigma_F(P^{(Z)}, q)$ is monotone non-decreasing. Its marginal increment $\Delta\sigma_F(Z) = I_1(Z)$ has local maxima at the categorical shell closures $[2, 10, 28, 60, \ldots]$.
2. **Categorical inertness.** A categorical shell closure $P^{(Z)}$ is a local terminal object of the dressing sub-diagram. The single-electron dressing $\mathrm{dress}_{S_1}: P^{(Z)} \to P^{(Z+1)}$ is feasible only if every currently tight dual block of the confinement SDP is simultaneously broken.
3. **Marginal energy peaks.** The marginal increment $\Delta\sigma_F(Z)$ peaks at the shell closures and dips at the openings via the dual shadow-price structure.

**Valence as dressing-arrow availability.**
An object's valence $v(Z)$ in this model is the number of forward dressing arrows $\mathrm{dress}_{S_1}: P^{(Z)} \to P^{(Z+1)}$ that remain feasible. For closure indices $Z \in \{2, 10, 28, 60, \ldots\}$, $v(Z) = 0$ (terminal object).

<!-- FILE_END: shell-closure-stability-interprets.md -->

<!-- FILE_START: level-sufficiency.md -->
**Proposition.**
*Let $P = (\mathrm{name}, \ell, [K]_M, n_0)$ be a
[confined particle](#def:confined-particle) and let*

$$
  \uparrow_\ell \colon P \longrightarrow P^{\uparrow}
  \quad\text{with}\quad
  P^{\uparrow} = (\mathrm{name}, \ell - 1, [\iota(K)]_M, n_1)
$$

*be an unfolding morphism in the
[confinement category](#def:confinement-category), where
$\iota: H_{n_0}(R, q) \hookrightarrow H_{n_1}(R, q)$ is the Hecke inclusion
and $n_1 \ge n_0$.  If the coarse witnessed partition truncation
satisfies*

$$
  k_{\max}(P, q) \le n_0
  \qquad (\text{coarse SDP captures full content}),
$$

*then the Markov trace is preserved along the unfolding:*

$$
  \mathrm{tr}_M\!\left(T_w^{\downarrow}\right)
  \;=\;
  \mathrm{tr}_M\!\left(T_w^{\uparrow}\right)
  \quad\text{in }\mathbb{C}(q),
$$

*where $T_w^{\downarrow} \in H_{n_0}(q)$ and
$T_w^{\uparrow} \in H_{n_1}(q)$ are the Gröbner–Shirshov normal forms
of $K$ at coarse and fine levels respectively.  Consequently, every
trace-class invariant $\mathcal{F}$ of $P$ — mass
$\mathfrak{m}(P)$, binding $B(P)$, Jones polynomial
$J_P(q)$ — takes the same value on $P$ and $P^{\uparrow}$:*

$$
  \mathcal{F}(P) \;=\; \mathcal{F}(P^{\uparrow}).
$$

*The coarsest level at which
$k_{\max}(P, q, n) \le n$ is **computationally sufficient**:
unfolding to any deeper level is superfluous for trace-class
invariants.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: level-sufficiency.md -->

<!-- FILE_START: level-sufficiency-interprets.md -->
**Remark.**
*[Level sufficiency](#prop:level-sufficiency) is the formal justification for a default-coarse computational strategy across the full [confinement category](#def:confinement-category). The hierarchy has at least four relevant levels:*

| *Level $\ell$* | *Confined particle* | *Default strand count $n_0$* |
|---|---|---|
| *0* | *quark* | *1* |
| *1* | *nucleon (proton, neutron)* | *3 (quark-strands)* |
| *2* | *atom / nucleus* | *$A$ (nucleon-strands)* |
| *3* | *compound / molecule* | *# atoms* |

*At each level, [prop:level-sufficiency](#prop:level-sufficiency) implies that any trace-class invariant — mass $\mathfrak{m}(P)$, binding $B(P)$, Jones polynomial $J_P(q)$ — is exact at the coarsest representation satisfying $k_{\max}(P, q, n_0) \le n_0$.*

**Default-coarse rule.**
*Every computational pipeline (mass, binding, stability, decay channel, spectroscopy) executes the following steps:*

1. *Identify the [confined particle](#def:confined-particle) $P$ at its natural level $\ell$.*
2. *Read $k_{\max}(P, q, n_0)$ from the witness data ([confinement level](#def:confinement-level) paragraph "per-atom truncation").*
3. *If $k_{\max}(P, q, n_0) \le n_0$, compute $\mathrm{tr}_M$ at the coarse level and halt.*
4. *If $k_{\max}(P, q, n_0) > n_0$, apply the unfolding morphism $\uparrow_\ell$ in [confinement category](#def:confinement-category) and repeat at $\ell - 1$.*

**Unfolding triggers (two categories).**

- ***Magic shell closure.*** *Atoms at $A \in \{2, 8, 20, 28, 50, 82, 126\}$ and noble-gas electron counts $Z \in \{2, 10, 18, 36, 54, 86\}$ exhibit binding multiplicity $\mu(S, q) \ge 2$ (electron shell). This forces $k_{\max}$ above the coarse count. Atoms in these rows evaluate one level deeper.*
- ***SDP cross-channel demand.*** *The active dual support $\mathcal{S}^*$ of the [confinement SDP](#prop:confinement-sdp) spans blocks $\lambda_1, \lambda_2$. When $\max(|\lambda_1|, |\lambda_2|) > n_0$, the coarse representation cannot express the coupling. Unfolding is required.*

*Non-magic atoms and molecules without SDP cross-channel demand evaluate at their natural coarse level. This is not an approximation. It is the minimal exact representation.*

**Dressing preserves computational minimality.**
*Under the [dressing morphism](#def:dressed-particle) $\mathrm{dress}_S: P_{\mathrm{bare}} \to P_{\mathrm{dressed}}$, the witnessed truncation updates to*

$$
  k_{\max}(P_{\mathrm{dressed}}, q)
  \;=\;
  \max\bigl(k_{\max}(P_{\mathrm{bare}}, q),\;
            k_{\max}^{\mathrm{bind}}(S, q)\bigr),
$$

*where $k_{\max}^{\mathrm{bind}}$ is the partition reach of the binding subword $W_{\mathrm{bind}}$. The dressed particle's computational level follows from [prop:level-sufficiency](#prop:level-sufficiency) with the updated $k_{\max}$. Adding a single electron to a non-magic atom typically leaves the computational level unchanged. Closing to a noble gas triggers $\mu \ge 2$ and raises the required level.*

**Computational implication.**
*For a non-magic atom with $A$ nucleons, the Hecke algebra dimension drops from $|H_{3A}(q)| = (3A)!$ (quark-level) to $|H_A(R, q)| = A!$ (nucleon-level). Partition enumeration drops from $p(3A)$ to $p(A)$. For $A = 20$, this yields a factor of $p(60)/p(20) \approx 966{,}000/627 \approx 1540$. Default-coarse computation is not a performance heuristic. It is the computational content of [prop:level-sufficiency](#prop:level-sufficiency) applied via the [confinement category](#def:confinement-category).*

**Earlier special case.**
*The remark [nucleon-as-unit justification](#rem:confinement-nucleon-unit) is the special case of this framework at the atom$\to$nucleon transition ($\ell = 2 \to \ell = 1$). [Prop:level-sufficiency](#prop:level-sufficiency) generalises it uniformly across the full hierarchy — quark to molecule — and for any knot-operator content. This includes the multi-operator $\mu(S, q) \ge 2$ regime introduced by electron shells and [dressing](#def:dressed-particle).*
<!-- FILE_END: level-sufficiency-interprets.md -->

<!-- FILE_START: confinement-phase-stratification.md -->
**Proposition.** Let $P$ be a [confined particle](#def:confined-particle). Let $\mathcal{G} \subset \mathbb{R}_{>1}$ be the generic locus of the substrate parameter $q$. The **confinement locus** of $P$ is

$$
  \Omega(P) \;:=\; \{\, q \in \mathcal{G} : \mathrm{confined}(P, q) \,\},
$$

where $\mathrm{confined}(P, q)$ is the strict feasibility predicate of the [confinement SDP](#prop:confinement-sdp). Then:

1. **Openness.** $\Omega(P)$ is open in $\mathcal{G}$.
2. **Stratification.** The complement $\mathcal{G} \setminus \Omega(P)$ decomposes into a real-algebraic stratification. The strata have codimension $\ge 1$ and form the **phase boundaries** of $P$. Each stratum is the zero locus of a principal minor of the SDP Gram matrix.
3. **Local constancy.** Let $\Omega_\alpha \subset \Omega(P)$ be a connected component (a **confinement phase**). On $\Omega_\alpha$:
   - the active support $\mathcal{S}^*(P, q)$ is constant;
   - the binding multiplicity $\mu(P, q) = |\mathcal{S}^*(P, q)|$ is constant;
   - the Frobenius stability index $\sigma_F(P, q) = n_{\mathrm{target}} \cdot u_0^*(P, q)$ is real-analytic.
4. **Scope.** The statements of [prop:level-sufficiency](#prop:level-sufficiency) and [prop:shell-closure-stability](#prop:shell-closure-stability), and the Markov-trace preservation of the [confinement category](#def:confinement-category) functor, hold pointwise in each $\Omega_\alpha$ and fail on $\partial\Omega(P)$.
5. **Phase transitions.** If a continuous deformation $q: [0, 1] \to \mathcal{G}$ crosses a phase boundary at $q_0 \in \partial\Omega(P)$, then at $q_0$ one of the following holds:
   - **Deconfinement.** $P$ is not realisable as a closed-braid bound state at $q_0$ (cf. [deconfinement threshold](#rem:deconfinement-golden-threshold)).
   - **Regime switch.** $\mu$ jumps discretely across $q_0$; the active support gains or loses a Wedderburn block; $\sigma_F$ has a non-smooth point (cf. [parity regime selection](#thm:parity-regime-selection)).
   - **Both.**

**Archimedean specialisation (§7c).** This block invokes real- or complex-analytic constructs (observables, bounds, numerical evaluation). Categorical identities remain valid over an abstract coefficient ring; their archimedean realisation is specialised here.
<!-- FILE_END: confinement-phase-stratification.md -->

<!-- FILE_START: confinement-phase-stratification-interpretation.md -->
*For simple particles (e.g., quark, free nucleon), $\Omega(P)$ forms a single connected interval of $\mathcal{G}$ containing $q_0$. For composite particles with multi-block binding ($\mu \ge 2$, e.g., noble-gas dressed atoms), $\Omega(P)$ can be disconnected. Each component corresponds to a distinct configuration of the active support. We physically realise transitions between components as chemical or nuclear rearrangements (e.g., $\mathrm{sp}^3 \leftrightarrow \mathrm{sp}^2$ hybridisation of carbon). Computationally, they appear as regime switches in the witness files `sdp_cross_channel.py` and `parity-regime-selection`.*
<!-- FILE_END: confinement-phase-stratification-interpretation.md -->

<!-- FILE_START: phase-scoped-applicability.md -->
**Remark.**
*[Prop:confinement-phase-stratification](#prop:confinement-phase-stratification) is the scope caveat attached to every statement in the confinement framework. Any formal statement about a [confined particle](#def:confined-particle) $P$, its electron shell, a [dressing morphism](#def:dressed-particle) $\mathrm{dress}_S$, or a trace-class invariant $\mathcal{F}(P)$ includes the implicit quantifier:*

$$
  \forall\, q \in \Omega_\alpha(P),
$$

*where $\Omega_\alpha(P)$ is a fixed connected component of the confinement locus $\Omega(P)$ — a single confinement phase.*

**Phase-scoped theorems (these hold only within a single $\Omega_\alpha$):**

- *[prop:level-sufficiency](#prop:level-sufficiency) — preservation of Markov trace under unfolding.*
- *[prop:shell-closure-stability](#prop:shell-closure-stability) — monotonicity of $\sigma_F$ along the dressing chain and local maxima at noble-gas $Z$.*
- *Functoriality of $\mathrm{tr}_M: \mathbf{Conf} \to \mathbb{C}(q)$ ([confinement category](#def:confinement-category)).*
- *Multi-operator binding structure (electron shell) — constancy of the active support $\mathcal{S}^*(S, q)$.*

**Boundary phenomena — not covered by within-phase theorems:**

- ***Deconfinement events.*** *At $q \in \partial\Omega(P)$ with Slater-strict feasibility lost, $P$ ceases to be realisable as a closed-braid bound state; the archetype is the [deconfinement threshold](#rem:deconfinement-golden-threshold).*
- ***Regime switches.*** *At $q \in \partial\Omega(P)$ with a $\mu$-jump but preserved feasibility, the active support gains or loses a Wedderburn block; witnessed by [prop:parity-regime-selection](#thm:parity-regime-selection).*
- ***Critical scaling.*** *Near a phase boundary, $\sigma_F$ typically has a non-analytic limit. Scaling exponents and critical phenomena require separate analysis (see [phase-transition interpretation](#rem:phase-transition-interpretation)).*
- ***Chemical and nuclear rearrangements.*** *Transitions between disconnected components of $\Omega(P)$ for a composite $P$ are realised physically as structural rearrangements — $\mathrm{sp}^3 \leftrightarrow \mathrm{sp}^2$ hybridisations, isomerisations, $\alpha$-decay channel openings. These transitions require an explicit cross-component analysis using the stratification of $\Omega(P)$.*

**Practical reading.**
*When encountering a confinement-framework statement, treat $q$ as ranging over a fixed open phase unless the text addresses boundary behaviour. Numerical witnesses evaluate at a single $q = q_0 \approx 1.110$. As long as that point lies in $\Omega_\alpha(P)$, all within-phase theorems apply. Auditing behaviour across $q$ ranges requires explicit stratification analysis.*
<!-- FILE_END: phase-scoped-applicability.md -->

