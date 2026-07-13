<!-- FILE_START: nuclear-stability-decay-intro.md -->
The valley of stability forms a Diophantine locus. The categorical Skein relation permits specific transitions across this valley. Beta decay is a single Skein crossing change applied to the Gröbner–Shirshov normal form. The categorical lepton number is the conserved quantity preserved by this operation.

The lepton tower follows. A continuant recurrence governs lepton masses. A numerical witness verifies this. This yields the universality of leptonic tau decays. Parity non-conservation follows directly from the Skein relation at $q \neq 1$. It is an automatic structural consequence. Nuclear spin-parity assignments tie to the eigenvalues of the braid operator.

Transition rates follow. The $q$-deformed transition amplitude, the hadron $q$-self-correction, and the Skein–Coulomb enhancement yield the half-life formulae. Algebraic machinery underpins the analysis: Gröbner–Shirshov computations with quotient ideals and shell closure via $\mu_n$ torsion in the Kummer tower. The shell correction takes a conjectured Skein-polynomial form. This bridges the derivation of atomic shells and the periodic table.
<!-- FILE_END: nuclear-stability-decay-intro.md -->

<!-- FILE_START: beta-decay-skein.md -->
Beta decay inserts the weak-force torus knot $T_{3,5}$ at the converting quark of a nuclear Gröbner–Shirshov normal form $\mathcal{N}(Z, N)$. The braid word is $\beta_{T_{3,5}} = (\sigma_1\sigma_2)^5$. It has $10$ crossings. The operation concludes with re-reduction.

A $\beta^-$ transition inserts the $T_{3,5}$ braid at the converting $\mathfrak{d}$-quark crossing of $\mathcal{N}(Z, N)$, followed by re-reduction:

$$
  \mathcal{N}(Z, N) \cdot \beta_{T_{3,5}}
  \xrightarrow{ \text{reduce}}
  \mathcal{N}(Z + 1,  N - 1)
  \sqcup
  T_{2,3}
  \sqcup
  K_{0_1}.
$$

A $\beta^+$ transition is the mirror operation. It inserts the conjugate $T_{3,5}^{\sigma}$ braid with $q \leftrightarrow q^{-1}$:

$$
  \mathcal{N}(Z, N) \cdot \beta_{T_{3,5}}^{\sigma}
  \xrightarrow{ \text{reduce}}
  \mathcal{N}(Z - 1,  N + 1)
  \sqcup
  T_{2,3}^{\sigma}
  \sqcup
  K_{0_1}.
$$
<!-- FILE_END: beta-decay-skein.md -->

<!-- FILE_START: beta-decay-skein-properties.md -->
The $\beta$-decay Skein operation requires the $T_{3,5}$ weak vertex, the $10$-crossing budget, the $\mathbb{Z}/2$ involution relating $\beta^\pm$, the lepton-pair decomposition, and the $10$-crossing $Q$-value.

**Setup.**
A nucleus $\mathcal{N}(Z, N)$ is a satellite link of $A = Z + N$ Borromean components. Its braid word in $B_{3A}$ reduces to a unique Gröbner–Shirshov normal form $\mathcal{N}(Z, N)$ in the Iwahori–Hecke algebra $H_{3A}(q)$.

Each nucleon is a Borromean link $\mathcal{B}_3(q_1, q_2, q_3)$ with quark strands:
- Proton: $\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$
- Neutron: $\mathfrak{n} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$

The crossing type at each generator $\sigma_i$ depends on the quark flavours of the two strands. The $\mathfrak{u}\text{-}\mathfrak{u}$ crossing is positive. The $\mathfrak{d}\text{-}\mathfrak{d}$ crossing is negative. The $\mathfrak{u}\text{-}\mathfrak{d}$ crossing is mixed.

## The $T_{3,5}$ weak vertex

The weak interaction is mediated by the torus knot $T_{3,5}$. Its braid word in $B_3$ is:

$$
  \beta_{T_{3,5}} =  (\sigma_1 \sigma_2)^5
$$

This word has $10$ crossings. In the Iwahori–Hecke algebra $H_3(q)$, the Hecke reduction of $(\sigma_1 \sigma_2)^5$ eliminates squares via $T^2 = (q - q^{-1})T + 1$. This produces a polynomial in the reduced basis of $H_3(q)$. The Markov trace of this polynomial is the weak vertex form factor:

$$
  \mathcal{W}(q)
   := 
  \mathrm{tr}_{\mathrm{Markov}}\bigl((\sigma_1 \sigma_2)^5\bigr)
   \in  \mathbb{Z}[q^{\pm 1/2}]
$$

The single-crossing Skein amplitude $s = q^{1/2} - q^{-1/2}$ appears as the coupling at each crossing of the $T_{3,5}$ braid. The full vertex factor is the Markov trace $\mathcal{W}(q)$ of all $10$ crossings, not $s^2$.

## The $10$-crossing budget

The $T_{3,5}$ braid insertion introduces $10$ crossings into the nuclear braid word. Gröbner–Shirshov reduction resolves these crossings into three components:

| Crossings | Destination | Structure |
|:---------:|-------------|-----------|
| $3$ | Electron $T_{2,3}$ (trefoil) | $3$ positive crossings |
| $0$ | Antineutrino $K_{0_1}$ (unknot) | Trivial topology |
| $7$ | Nuclear re-reduction | R2 moves absorbed into daughter normal form |

The $7$ re-reduction crossings change the R2 step count between parent and daughter normal forms. This dominates the $Q$-value. The single-crossing approximation misses $6$ of these $7$ crossings.

## Crossing partition and the Skein relation

Gröbner–Shirshov reduction partitions the $10$ crossings of $T_{3,5}$. The electron trefoil takes $3$. The neutrino unknot takes $0$. The daughter nuclear braid absorbs the remaining $7$ as R2 moves.

The Skein relation acts at each of the $10$ crossings:

$$
  q  [L_+] -  q^{-1} [L_-]
  =  (q^{1/2} - q^{-1/2})  [L_0]
$$

The transition amplitude depends on the accumulated effect of $10$ such relations, not $1$.

## The $\mathbb{Z}/2$ symmetry

The involution $q \mapsto q^{-1}$ on the Iwahori–Hecke algebra relates $\beta^-$ and $\beta^+$. It acts as:

| $\beta^-$ | $\beta^+$ |
|:---:|:---:|
| $\mathfrak{d} \to \mathfrak{u}$ via $T_{3,5}$ | $\mathfrak{u} \to \mathfrak{d}$ via $T_{3,5}^{\sigma}$ |
| $q  [L_+]$ | $q^{-1} [L_+]$ |
| electron $T_{2,3}$ | positron $T_{2,3}^{\sigma}$ |
| antineutrino $K_{0_1}^{\sigma}$ | neutrino $K_{0_1}$ |
| $\mathcal{S}_{ab}(q)$ | $\mathcal{S}_{ba}(q) = \mathcal{S}_{ab}(q^{-1})$ |

This $\mathbb{Z}/2$ acts on the pair Skein mass formula:

$$
  \mathcal{S}_{ab}(q)
  = \frac{q \mu_a + q^{-1} \mu_b}{q^{1/2} + q^{-1/2}}
  \xrightarrow{q \leftrightarrow q^{-1}} 
  \mathcal{S}_{ba}(q)
  = \frac{q \mu_b + q^{-1} \mu_a}{q^{1/2} + q^{-1/2}}
$$

These are distinct when $\mu_a \neq \mu_b$. The asymmetry $\mathcal{S}_{ab} - \mathcal{S}_{ba} = (q - q^{-1})(\mu_a - \mu_b)/(q^{1/2} + q^{-1/2})$ is the weak asymmetry. This drives the $Q$-value.

## The lepton pair from $T_{3,5}$ decomposition

Gröbner–Shirshov reduction decomposes the $T_{3,5}$ braid $(\sigma_1 \sigma_2)^5$ into the lepton pair and a reduction residue. The electron trefoil $T_{2,3} = (\sigma_1)^3$ accounts for $3$ of the $10$ crossings. The antineutrino unknot $K_{0_1}$ accounts for $0$. The remaining $7$ crossings are the weak vertex residue. They are absorbed into R2 moves during re-reduction.

$$
  L_0^{-} =  T_{2,3} \sqcup T_{1,0}^{\sigma}
  \qquad (\beta^- \text{ decay: } e^- + \nu_e^{\sigma})
$$

$$
  L_0^{+} =  T_{2,3}^{\sigma} \sqcup T_{1,0}
  \qquad (\beta^+ \text{ decay: } e^+ + \nu_e)
$$

## The $Q$-value (10-crossing)

The transition energy is the difference in categorical actions between parent and daughter. It accounts for all $10$ crossings of the $T_{3,5}$ insertion:

$$
  Q
  = 
  \mathfrak{S}_q[\mathcal{N}(Z, N)]
  - 
  \mathfrak{S}_q[\mathcal{N}(Z \pm 1, N \mp 1)]
  - 
  m_e
$$

The parent and daughter normal forms differ at all crossings affected by the $T_{3,5}$ insertion and its re-reduction. The $7$ re-reduction crossings from the weak vertex residue modify inter-nucleon crossing types at the converting quark's strand. They change $\binom{A-1}{1} \cdot 3$ inter-nucleon crossings.

**Re-reduction cost (10-crossing).**
The $T_{3,5}$ insertion at the converting quark adds $10$ crossings to the braid word. The Gröbner–Shirshov reduction must:

1. Extract the $3$-crossing electron trefoil from the $T_{3,5}$ decomposition.
2. Reduce the remaining $7$ crossings via R2 moves ($T^2 = (q - q^{-1})T + 1$) and R3/far-commutativity moves.
3. Propagate the flavour change through all inter-nucleon crossings involving the converting quark's strand.

The net R2 step count from all $10$ crossings determines the $Q$-value:

$$
  Q =  \Delta(\text{R2 steps})
   \times  (q - q^{-1})
   \times  (\text{pair Skein scale})
$$

## Insufficiency of the single-crossing approximation

The previous single-crossing approximation captured only $1$ of the $10$ crossings in the weak vertex. This explains:

1. **Systematic overshoot.** Predictions for heavy-nucleus half-lives overshoot by $10$–$17\%$. The missing $9$ crossings contribute phase space. Including them shortens the half-life.
2. **Tritium accuracy.** The error for $A = 3$ is $< 2\%$. The nuclear braid is short. The $7$ re-reduction crossings have limited room to propagate. The single-crossing approximation succeeds accidentally.
3. **Mass-dependent correction.** Heavier nuclei have more inter-nucleon crossings affected by the flavour change. The $7$ re-reduction crossings modify more transfer matrices.

**Open computation.** The exact weak vertex form factor $\mathcal{W}(q) = \mathrm{tr}_{\mathrm{Markov}}((\sigma_1\sigma_2)^5)$ and the crossing budget ($3 + 0 + 7$) require verification by explicit Iwahori–Hecke algebra computation.
<!-- FILE_END: beta-decay-skein-properties.md -->

<!-- FILE_START: lepton-number-categorical.md -->
Lepton number is the count of Skein smoothings applied to the nuclear normal form.

**Definition.**
Let $\mathcal{N}$ be a nuclear link in Gröbner–Shirshov normal form. Let $\mathcal{N}'$ be obtained from $\mathcal{N}$ by a sequence of $k$ Skein crossing changes. The lepton number of this transition is $L = k$.
<!-- FILE_END: lepton-number-categorical.md -->

<!-- FILE_START: lepton-number-categorical-properties.md -->
The categorical lepton number possesses several structural properties.

Each beta decay applies the Skein relation at one crossing. This produces a smoothing $L_0^{\pm}$. It contains exactly one lepton–antilepton pair. Lepton number counts these smoothings.

Each smoothing $L_0^{\pm}$ contributes:
- One charged lepton ($T_{2,3}$ or $T_{2,3}^{\sigma}$) with lepton number $+1$.
- One neutrino or antineutrino ($K_{0_1}$ or $K_{0_1}^{\sigma}$) with lepton number $-1$.

The net lepton number of each $L_0^{\pm}$ pair is zero.

**Conservation.**
Lepton number is conserved by construction:

1. Skein smoothings produce lepton pairs with net lepton number $0$. The nuclear sector loses one crossing. Hadrons carry lepton number $0$. The total is $\Delta L = 0$.
2. Gröbner–Shirshov re-reduction acts within the Iwahori–Hecke algebra. It produces no smoothings. The total is $\Delta L = 0$.
3. Markov moves change the braid representative but not the link type. The total is $\Delta L = 0$.

Every process expressed as a sequence of Skein relations and Hecke reductions conserves lepton number.

**Lepton number as a $\mathbb{Z}$-grading.**
The Skein module $\mathcal{K}(S^3; q)$ admits a natural $\mathbb{Z}$-grading by the smoothing count. Links in the nuclear sector have grade $0$. Each smoothing shifts the grade by $+1$. Hecke relations act within a fixed grade. Reidemeister moves leave the smoothing count invariant. Both preserve the grade.

**Individual lepton assignments.**

| Particle | Knot type | Lepton number $L$ | Origin |
|----------|-----------|:---:|--------|
| $e^-$ | $T_{2,3}$ (trefoil) | $+1$ | $L_0^{-}$ charged component ($\beta^-$) |
| $e^+$ | $T_{2,3}^{\sigma}$ (mirror trefoil) | $-1$ | $L_0^{+}$ charged component ($\beta^+$) |
| $\nu_e$ | $K_{0_1}$ (unknot) | $+1$ | $L_0^{+}$ neutral component ($\beta^+$) |
| $\nu_e^{\sigma}$ | $K_{0_1}^{\sigma}$ (mirror unknot) | $-1$ | $L_0^{-}$ neutral component ($\beta^-$) |

The charged lepton carries $L = \pm 1$. The neutrino carries $L = \mp 1$. Each pair sums to zero.

**The $\chi = -6$ constraint.**
In the Descartes universe, the Euler characteristic $\chi(A) = -6$ constrains Bring's surface. The torus knot generators $T(2, n)$ with odd $n \leq 7$ exhaust the fermion spectrum. The electron ($T_{2,3}$) and neutrino ($K_{0_1} = T_{2,1}$) are the lowest torus knots in this sequence. The smoothing $L_0^{-}$ must decompose into exactly these knot types. They are the only single-component closures of a 2-arc resolution at a Borromean crossing.

**Structural origin of lepton-number conservation.**
In the Standard Model, lepton number conservation is an accidental symmetry. Here, it is a structural invariant. The Skein relation is the unique operation that changes crossing type. It always produces exactly one lepton pair. The Iwahori–Hecke algebra contains no mechanism to produce an odd number of leptons. The smoothing is a topological operation on a single crossing. Each smoothing is binary.

Lepton number violation requires a process that changes crossing type without passing through the Skein relation. Such a process must exist outside the Iwahori–Hecke algebra. In the $\chi = -6$ universe, no such process exists.
<!-- FILE_END: lepton-number-categorical-properties.md -->

<!-- FILE_START: lepton-continuant-recurrence.md -->
The charged lepton tower $T_{2,n}$ for $n = 3, 5, 7$ describes the $e^-, \mu^-, \tau^-$ generations. It possesses a closed-form normal form in $H_2(q) \subset H_3(q)$. A Morgan–Voyce continuant recurrence defines this form.

## Statement

Let $h = q - q^{-1}$ be the Hecke parameter. Let $T_{2,n} = \sigma_0^n$ be the $(2, n)$-torus knot braid in $B_2$. The Gröbner–Shirshov normal form in $H_2(q)$ is:

$$
  \mathrm{NF}(\sigma_0^n)
  = 
  a_n \cdot \mathbf{1}
  + 
  b_n \cdot \sigma_0
$$

The sequences $\{a_n\}$ and $\{b_n\}$ satisfy:

$$
  a_{n+1} = b_n,
  \qquad
  b_{n+1} = h  b_n + b_{n-1},
  \qquad
  b_0 = 0,   b_1 = 1.
$$

The second relation is the Morgan–Voyce continuant. This three-term recurrence features a positive sign on $b_{n-1}$. It contrasts with the Chebyshev polynomials of the second kind $U_n(\cos\varTheta)$, which follow $b_{n+1} = 2\cos\varTheta \cdot b_n - b_{n-1}$.

The net coefficient is the sum of all normal form terms. It is $\mathrm{net}(T_{2,n}) = a_n + b_n$.
<!-- FILE_END: lepton-continuant-recurrence.md -->

<!-- FILE_START: lepton-continuant-recurrence-novelty.md -->
The structural identification of the lepton-tower sequence as a positive-sign Morgan–Voyce continuant distinguishes it from standard Chebyshev $U_n$ recurrences. This provides an algebraic framework that captures the combinatorial constraints of the lepton sector.
<!-- FILE_END: lepton-continuant-recurrence-novelty.md -->

<!-- FILE_START: lepton-tower-witness.md -->
Evaluating the continuant recurrence at $q_0 \approx 1.1100$ for $n = 0, 1, \ldots, 9$ yields coefficients. Their recurrence residuals are strictly bounded by $10^{-12}$.

## Full normal form table

See Table.

Odd-$n$ torus knots $T_{2,n}$ with $n \leq 7$ exhaust the embeddable fermion spectrum on Bring's surface. The even-$n$ entries do not represent torus knots. They demonstrate the monotone growth of the net coefficient.

## Lepton decay differences

$$
  \Delta\mathrm{net}(\tau \to e)
  = \mathrm{net}(T_{2,7}) - \mathrm{net}(T_{2,3})
  = 1.936 - 1.253
  = +0.683
$$

$$
  \Delta\mathrm{net}(\tau \to \mu)
  = \mathrm{net}(T_{2,7}) - \mathrm{net}(T_{2,5})
  = 1.936 - 1.560
  = +0.376
$$

The normal form difference ratio $\Delta(\tau \to e) / \Delta(\tau \to \mu) \approx 1.816$ reflects the crossing count difference. The $\tau \to e$ decay releases $4$ crossings. The $\tau \to \mu$ decay releases $2$ crossings. This ratio does not directly determine the physical branching ratio. The matrix element factorises through the weak vertex trace.

## Mass-ratio indicators

$$
  \frac{\mathrm{net}(\mu)}{\mathrm{net}(e)}
  = \frac{1.560}{1.253} = 1.245
  \qquad
  \frac{\mathrm{net}(\tau)}{\mathrm{net}(e)}
  = \frac{1.936}{1.253} = 1.545
$$

These values are not the physical mass ratios $m_\mu / m_e \approx 206.8$ and $m_\tau / m_e \approx 3477$. The net coefficients parameterise the topological complexity of the torus knot. Deriving the physical mass requires evaluating the full Seiberg–Witten integral over the jet bundle prolongation.
<!-- FILE_END: lepton-tower-witness.md -->

<!-- FILE_START: tau-leptonic-universality.md -->
The tau lepton decays leptonically via the $T_{3,5}$ weak vertex. The factorized model sets the squared matrix element to $|\mathcal{M}|^2 = |\mathrm{tr}_{\mathrm{Markov}}(T_{3,5})|^2$. This amplitude is independent of the daughter lepton. It predicts lepton universality directly from the underlying Iwahori–Hecke algebra structure.

## Statement

Let $T_{3,5} = (\sigma_0 \sigma_1)^5$ be the weak vertex in $H_3(q)$. Let $f(x)$ denote the phase-space factor for $\tau \to \ell \bar\nu_\ell \nu_\tau$. Here $x = (m_\ell / m_\tau)^2$:

$$
  f(x)
  = 1 - 8x + 8x^3 - x^4 - 12 x^2 \ln x.
$$

The ratio of leptonic branching fractions is

$$
  \frac{\mathrm{BR}(\tau \to e\bar\nu_e\nu_\tau)}
       {\mathrm{BR}(\tau \to \mu\bar\nu_\mu\nu_\tau)}
  = 
  \frac{|\mathcal{M}_e|^2 \cdot f(m_e^2/m_\tau^2)}
       {|\mathcal{M}_\mu|^2 \cdot f(m_\mu^2/m_\tau^2)}.
$$

In the factorized model, the Markov trace of the weak vertex provides the universal matrix element:

$$
  |\mathcal{M}_e|^2
  = 
  |\mathcal{M}_\mu|^2
  = 
  \bigl|\mathrm{tr}_{\mathrm{Markov}}(T_{3,5})\bigr|^2.
$$

The matrix-element ratio evaluates exactly to $1$. The branching ratio reduces to the pure phase-space ratio:

$$
  \frac{\mathrm{BR}(\tau \to e)}{\mathrm{BR}(\tau \to \mu)}
  = 
  \frac{f(m_e^2 / m_\tau^2)}{f(m_\mu^2 / m_\tau^2)}.
$$

## Physical significance

Lepton universality is the statement that the weak interaction couples equally to all lepton generations. It emerges here as a consequence of the $T_{3,5}$ braid serving as the unique cross-family mediator on the Bring surface. Its Markov trace $\mathcal{W}(q) = \mathrm{tr}_{\mathrm{Markov}}((\sigma_0 \sigma_1)^5)$ is a property of the weak vertex alone, not the daughter channel. Kinematics exclusively break universality. The daughter mass enters through the phase-space integral, not the vertex operator.
<!-- FILE_END: tau-leptonic-universality.md -->

<!-- FILE_START: tau-branching-ratio-witness.md -->
Evaluating both the factorized and the product models at $q_0 \approx 1.1100$ allows comparison with the PDG experimental branching ratio.

## Weak vertex data

The $T_{3,5} = (\sigma_0 \sigma_1)^5$ weak vertex in $H_3(q)$ reduces to 6 normal form terms in the standard basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$. This requires 38 Hecke and 18 Yang–Baxter steps.

See Table 1.

$$
  \mathrm{net}(T_{3,5}) = 2.316,
  \qquad
  \mathrm{tr}_{\mathrm{Markov}}(T_{3,5}) = 0.704,
  \qquad
  |\mathcal{W}|^2 = 0.495.
$$

## Branching ratio comparison

Factorized model:

$$
  \frac{\mathrm{BR}(\tau \to e)}{\mathrm{BR}(\tau \to \mu)}
  =
  \frac{f(m_e^2/m_\tau^2)}{f(m_\mu^2/m_\tau^2)}
  =
  \frac{0.99999934}{0.97255996}
  \approx 1.028.
$$

Product model:

$$
  \frac{|M_e|^2}{|M_\mu|^2}
  =
  \frac{|\mathrm{tr}_3(T_{2,3} \cdot T_{3,5} \cdot T_{2,7})|^2}
       {|\mathrm{tr}_3(T_{2,5} \cdot T_{3,5} \cdot T_{2,7})|^2}
  =
  \frac{5.426}{7.865}
  \approx 0.690.
$$

This gives a branching ratio of $\approx 0.709$. This is inconsistent with experiment.

PDG 2024 experimental values:

$$
  \mathrm{BR}(\tau \to e\bar\nu_e\nu_\tau) = 17.82\%,
  \qquad
  \mathrm{BR}(\tau \to \mu\bar\nu_\mu\nu_\tau) = 17.39\%,
$$

$$
  \frac{\mathrm{BR}(\tau \to e)}{\mathrm{BR}(\tau \to \mu)}
  = 1.025 \pm 0.003.
$$

## Result

See Table 2.

The factorized model treats the Markov trace of $T_{3,5}$ as the universal matrix element. It reproduces the PDG ratio to $0.34\%$. The product model is excluded by data.

## Decay channel normal form structure

Both decay channels $\tau \to e$ and $\tau \to \mu$ reduce to 6 normal form terms in $H_3(q)$. The dominant term in both channels is $L_+ = \sigma_0\sigma_1$. It contributes $\sim 30\%$ of the total weight. The $L_-$ contribution is larger in $\tau \to \mu$ ($15.6\%$) than in $\tau \to e$ ($13.9\%$). The heavier daughter lepton requires more re-crossing energy.

The full witness data is recorded in `tau-leptonic-decay.witness.json`.
<!-- FILE_END: tau-branching-ratio-witness.md -->

<!-- FILE_START: parity-violation-skein.md -->
Parity is violated by the weak interaction if and only if $q \neq 1$.

### Origin: Hecke eigenvalue asymmetry

Parity violation follows directly from the categorical origin of the crossing energy. The Hecke generator $\sigma = P \circ R$ has eigenvalues $(q, -q^{-1})$ on $S^{2} V \oplus \Lambda^{2} V$. The relation $\lvert q \rvert \neq \lvert {-q^{-1}} \rvert$ holds for $q \neq 1$. A positive crossing $L_{+}$ carries the eigenvalue $q$. A negative crossing $L_{-}$ carries $-q^{-1}$. Parity $\mathcal{P}$ exchanges $L_{+} \leftrightarrow L_{-}$ but does not change $q$. Hence $\mathcal{P}$-invariance forces $q = -q^{-1}$, giving $q^{2} = -1$. This is impossible on the substrate ray. The sign-asymmetry of the eigenvalue pair is the algebraic source of P-violation. It is inherited from $P|_{\Lambda^{2} V} = -\mathrm{id}$. It is not a physical postulate added to the framework.

The detailed Skein derivation below rederives the same conclusion from the Skein relation. Both are consequences of the same eigenvalue structure.

### Skein derivation

The parity operation $\mathcal{P}$ on a link is the mirror. It reverses all crossings ($L_+ \leftrightarrow L_-$). In the braid group $B_n$, this is the involution $\sigma_i \mapsto \sigma_i^{-1}$.

**The Skein relation under parity.**

The Skein relation at a single crossing:

$$
  q  [L_+] -  q^{-1} [L_-]
  = 
  (q^{1/2} - q^{-1/2})  [L_0]
$$

Apply the mirror $\mathcal{P}$. This sends $L_+ \mapsto L_-$, $L_- \mapsto L_+$, and $L_0 \mapsto \mathcal{P}(L_0)$. The mirrored Skein relation reads:

$$
  q  [L_-] -  q^{-1} [L_+]
  = 
  (q^{1/2} - q^{-1/2})  [\mathcal{P}(L_0)]
$$

Rearranging:

$$
  q^{-1} [L_+] -  q  [L_-]
  = 
  -(q^{1/2} - q^{-1/2})  [\mathcal{P}(L_0)]
$$

Compare this with the original:

$$
  q  [L_+] -  q^{-1} [L_-]
  = 
  (q^{1/2} - q^{-1/2})  [L_0]
$$

These are the same equation if and only if $q = q^{-1}$, meaning $q = 1$.

**Proposition.**
*The Skein relation is invariant under parity $\mathcal{P}: L_+ \leftrightarrow L_-$ if and only if $q = 1$. For any $q \neq 1$, the weak interaction violates parity.*
<!-- FILE_END: parity-violation-skein.md -->

<!-- FILE_START: parity-violation-skein-interpretation.md -->
The Hecke relation $\sigma^2 = (q - q^{-1})\sigma + 1$ breaks the symmetry between positive and negative crossings. At $q = 1$, we have $\sigma^2 = 1$. Parity is conserved. At the substrate parameter $q_0$, the relation becomes $\sigma^2 = 0.209\,\sigma + 1$. The $0.209\,\sigma$ term distinguishes positive from negative crossings. This violates parity.

The Hecke deformation parameter controls the degree of parity violation:

$$
  q - q^{-1} = 0.209 \quad (\text{at } q = q_0).
$$

All parity violation traces back to $q \neq 1$.

**Maximal parity violation.**

The Standard Model weak force violates parity maximally. It couples only to left-handed particles. This maps to crossing chirality. A positive crossing $\sigma_i$ contributes weight $q$ to the categorical action. A negative crossing $\sigma_i^{-1}$ contributes $q^{-1}$. The ratio $q^2 = 1.232$ measures the left-right asymmetry.

The Wu experiment found a strong forward-backward asymmetry in ${}^{60}\mathrm{Co}$ beta decay. This asymmetry represents the crossing chirality of the nuclear link. The ${}^{60}\mathrm{Co}$ braid word carries a specific writhe $w \neq 0$. The Skein crossing change at $q_0$ produces an emission pattern determined by $q^w$.

**Connection to the $\mathbb{Z}/2$ of beta decay.**

The involution $q \leftrightarrow q^{-1}$ exchanges $\beta^- \leftrightarrow \beta^+$. It acts as the combined $\widehat{CP}$ operation. It applies parity $\mathcal{P}$ by mirroring all crossings. It applies charge conjugation $\hat{C}$ by exchanging $T_{2,3} \leftrightarrow T_{2,3}^{\sigma}$.

- $\mathcal{P}$ alone is violated because $q \neq q^{-1}$.
- $\hat{C}$ alone is violated because the electron and positron differ in mass ordering.
- $\widehat{CP}$ is conserved to leading order because $q \leftrightarrow q^{-1}$ is a symmetry of the Iwahori–Hecke algebra.
<!-- FILE_END: parity-violation-skein-interpretation.md -->

<!-- FILE_START: nuclear-spin-parity.md -->
The nuclear spin quantum number $J$ is integral when $A$ is even and half-integral when $A$ is odd.

This follows topologically from the braid representation. Each nucleon is a spin-$\tfrac{1}{2}$ fermion. It is a single-component knot. The tensor product of $A$ such representations dictates a spin parity determined by $A \bmod 2$.

**Proposition.**
*Let $\mathcal{N}(Z, N)$ be a nucleus with mass number $A = Z + N$. The total angular momentum $J$ satisfies:*

$$
  J \in \mathbb{Z} \quad \Longleftrightarrow \quad A \in 2\mathbb{Z}
$$

$$
  J \in \mathbb{Z} + \tfrac{1}{2} \quad \Longleftrightarrow \quad A \in 2\mathbb{Z} + 1
$$
<!-- FILE_END: nuclear-spin-parity.md -->

<!-- FILE_START: nuclear-spin-parity-novelty.md -->
Formulating parity strictly via $\mathrm{SU}_q(2)$ tensor-product rules algebraically embeds empirical parity constraints within the theory. This reproduces standard spin-statistics without external postulates.
<!-- FILE_END: nuclear-spin-parity-novelty.md -->

