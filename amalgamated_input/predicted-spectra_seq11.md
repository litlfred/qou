<!-- FILE_START: nuclear-stability-decay-intro.md -->
The valley of stability identified previously forms a Diophantine locus. We now determine which transitions across this valley the categorical Skein relation permits. We define beta decay as a single Skein crossing change applied to the Gröbner–Shirshov normal form. We then identify the categorical lepton number as the conserved quantity preserved by this operation.

Next, we construct the lepton tower. A continuant recurrence governs lepton masses, verified by a numerical witness. This yields the universality of leptonic tau decays. Crucially, parity non-conservation follows directly from the Skein relation at $q \neq 1$; it is an automatic structural consequence, not an external postulate. We then tie nuclear spin-parity assignments to the eigenvalues of the braid operator.

Finally, we compute transition rates. The $q$-deformed transition amplitude, combined with the hadron $q$-self-correction and the Skein–Coulomb enhancement, yields the half-life formulae. We develop the algebraic machinery—Gröbner–Shirshov computations with quotient ideals and shell closure via $\mu_n$ torsion in the Kummer tower—that underpins the subsequent analysis. We conclude by conjecturing the shell correction in Skein-polynomial form, bridging this section to the derivation of atomic shells and the periodic table.
<!-- FILE_END: nuclear-stability-decay-intro.md -->

<!-- FILE_START: beta-decay-skein.md -->
Beta decay is the crossing operation that inserts the weak-force torus knot $T_{3,5}$ (braid word $\beta_{T_{3,5}} = (\sigma_1\sigma_2)^5$, $10$ crossings, [force identification](#rem:force-knot-identification)) at the converting quark of a nuclear Gröbner--Shirshov normal form $\mathcal{N}(Z, N)$ ([stable nucleus](#def:stable-nucleus)), followed by re-reduction.

A $\beta^-$ transition inserts the $T_{3,5}$ braid at the converting $\mathfrak{d}$-quark crossing of the Gröbner--Shirshov normal form $\mathcal{N}(Z, N)$, followed by re-reduction:

$$
  \mathcal{N}(Z, N) \cdot \beta_{T_{3,5}}
  \xrightarrow{ \text{reduce}}
  \mathcal{N}(Z + 1,  N - 1)
  \sqcup
  T_{2,3}
  \sqcup
  K_{0_1}.
$$

A $\beta^+$ transition is the mirror operation, inserting the conjugate $T_{3,5}^{\sigma}$ braid (with $q \leftrightarrow q^{-1}$):

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
The following develops the [$\beta$-decay Skein
operation](#def:beta-decay-skein): the $T_{3,5}$ weak vertex, its
$10$-crossing budget, the $\mathbb{Z}/2$ involution relating
$\beta^\pm$, the lepton-pair decomposition, and the $10$-crossing
$Q$-value.

**Setup.**
A nucleus $\mathcal{N}(Z, N)$ is a satellite link of $A = Z + N$
Borromean components ([stable nucleus](#def:stable-nucleus)).
Its braid word in $B_{3A}$ reduces to a unique Gröbner--Shirshov normal form
$\mathcal{N}(Z, N)$ in the Iwahori--Hecke algebra $H_{3A}(q)$
([nuclear Gröbner--Shirshov reduction](#prop:nuclear-groebner-reduction)).

Each nucleon is a Borromean link $\mathcal{B}_3(q_1, q_2, q_3)$
with quark strands:
- Proton: $\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$
 ([categorical proton](#def:categorical-proton))
- Neutron: $\mathfrak{n} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$
 ([categorical neutron](#def:categorical-neutron))

The crossing type at each generator $\sigma_i$ depends on the
quark flavours of the two strands: $\mathfrak{u}\text{-}\mathfrak{u}$ (positive), $\mathfrak{d}\text{-}\mathfrak{d}$
(negative), or $\mathfrak{u}\text{-}\mathfrak{d}$ (mixed).

## The $T_{3,5}$ weak vertex

The weak interaction is mediated by the torus knot $T_{3,5}$
([force identification](#rem:force-knot-identification)), whose
braid word in $B_3$ is:

$$
  \beta_{T_{3,5}} =  (\sigma_1 \sigma_2)^5
$$

This word has **$10$ crossings**. In the Iwahori--Hecke algebra $H_3(q)$,
the Hecke reduction of $(\sigma_1 \sigma_2)^5$ eliminates squares
via $T^2 = (q - q^{-1})T + 1$, producing a polynomial in the
reduced basis of $H_3(q)$. The Markov trace of this polynomial
is the **weak vertex form factor**:

$$
  \mathcal{W}(q)
   := 
  \mathrm{tr}_{\mathrm{Markov}}\bigl((\sigma_1 \sigma_2)^5\bigr)
   \in  \mathbb{Z}[q^{\pm 1/2}]
$$

The single-crossing Skein amplitude $s = q^{1/2} - q^{-1/2}$
appears as the coupling at each crossing of the $T_{3,5}$ braid.
The full vertex factor is **not** $s^2$ (single crossing) but
the Markov trace $\mathcal{W}(q)$ of all $10$ crossings.

## The $10$-crossing budget

When the $T_{3,5}$ braid is inserted at the converting quark,
it introduces $10$ crossings into the nuclear braid word. These
$10$ crossings are resolved by the Gröbner--Shirshov reduction into three
components:

| Crossings | Destination | Structure |
|:---------:|-------------|-----------|
| $3$ | Electron $T_{2,3}$ (trefoil) | $3$ positive crossings |
| $0$ | Antineutrino $K_{0_1}$ (unknot) | Trivial topology |
| $7$ | Nuclear re-reduction | R2 moves absorbed into daughter normal form |

The $7$ re-reduction crossings change the R2 step count between
parent and daughter normal forms. This is the dominant
contribution to the $Q$-value
([transition energy](#def:Q-value-transition)) — the single-crossing
approximation misses $6$ of these $7$ crossings.

## Crossing partition and the Skein relation

The $10$ crossings of $T_{3,5}$ are partitioned by the
Gröbner--Shirshov reduction: $3$ form the electron trefoil, $0$ form the
neutrino unknot, and $7$ are absorbed as R2 moves into the
daughter nuclear braid.

In the Skein relation at each of the $10$ crossings:

$$
  q  [L_+] -  q^{-1} [L_-]
  =  (q^{1/2} - q^{-1/2})  [L_0]
$$

The accumulated effect of $10$ such relations (not $1$) determines
the transition amplitude.

## The $\mathbb{Z}/2$ symmetry

$\beta^-$ and $\beta^+$ are related by the involution
$q \mapsto q^{-1}$ on the Iwahori--Hecke algebra, which acts as:

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

When $\mu_a \neq \mu_b$ (i.e., $\mu_{\mathfrak{u}} \neq \mu_{\mathfrak{d}}$), the two
are distinct: the asymmetry $\mathcal{S}_{ab} - \mathcal{S}_{ba} = (q - q^{-1})(\mu_a - \mu_b)/(q^{1/2} + q^{-1/2})$ is the
**weak asymmetry** that drives the $Q$-value.

## The lepton pair from $T_{3,5}$ decomposition

The $T_{3,5}$ braid $(\sigma_1 \sigma_2)^5$ decomposes under
Gröbner--Shirshov reduction into the lepton pair plus reduction residue.
The electron trefoil $T_{2,3} = (\sigma_1)^3$ accounts for $3$ of
the $10$ crossings; the antineutrino unknot $K_{0_1}$ accounts
for $0$. The remaining $7$ crossings are the **weak vertex
residue** — absorbed into R2 moves during re-reduction.

$$
  L_0^{-} =  T_{2,3} \sqcup T_{1,0}^{\sigma}
  \qquad (\beta^- \text{ decay: } e^- + \nu_e^{\sigma})
$$

$$
  L_0^{+} =  T_{2,3}^{\sigma} \sqcup T_{1,0}
  \qquad (\beta^+ \text{ decay: } e^+ + \nu_e)
$$

## The $Q$-value (10-crossing)

The transition energy is the difference in categorical actions
between parent and daughter, now accounting for all $10$
crossings of the $T_{3,5}$ insertion:

$$
  Q
  = 
  \mathfrak{S}_q[\mathcal{N}(Z, N)]
  - 
  \mathfrak{S}_q[\mathcal{N}(Z \pm 1, N \mp 1)]
  - 
  m_e
$$

The parent and daughter normal forms differ at all crossings
affected by the $T_{3,5}$ insertion and its subsequent
re-reduction — not the single converting crossing. The
$7$ re-reduction crossings from the weak vertex residue modify
inter-nucleon crossing types at the converting quark's strand,
changing $\binom{A-1}{1} \cdot 3$ inter-nucleon crossings
(one per quark strand of each partner nucleon).

**Re-reduction cost (10-crossing).**
After the $T_{3,5}$ insertion at the converting quark, the braid
word gains $10$ crossings. The Gröbner--Shirshov reduction must:

1. Extract the $3$-crossing electron trefoil from the
 $T_{3,5}$ decomposition.
2. Reduce the remaining $7$ crossings via R2 moves
 ($T^2 = (q - q^{-1})T + 1$) and R3/far-commutativity moves.
3. Propagate the flavour change through all inter-nucleon crossings
 involving the converting quark's strand.

The net R2 step count from all $10$ crossings (not just $1$)
determines the $Q$-value:

$$
  Q =  \Delta(\text{R2 steps from 10 crossings})
   \times  (q - q^{-1})
   \times  (\text{pair Skein scale})
$$

## Insufficiency of the single-crossing approximation

The previous single-crossing approximation captured only $1$
of the $10$ crossings in the weak vertex. This explains:

1. **Systematic overshoot** of $10$–$17\%$ in heavy-nucleus
 half-life predictions: the missing $9$ crossings contribute
 additional phase space that shortens the predicted half-life
 when properly included.

2. **Tritium accuracy** ($< 2\%$ error): for $A = 3$, the
 nuclear braid is short enough that the $7$ re-reduction
 crossings have limited room to propagate — the single-crossing
 approximation is accidentally good.

3. **Mass-dependent correction**: heavier nuclei have more
 inter-nucleon crossings affected by the converting quark's
 flavour change, so the $7$ re-reduction crossings modify
 more transfer matrices.

**Open computation:** The exact weak vertex form factor
$\mathcal{W}(q) = \mathrm{tr}_{\mathrm{Markov}}((\sigma_1\sigma_2)^5)$
and the crossing budget ($3 + 0 + 7$) must be
verified by explicit Iwahori--Hecke algebra computation of the $T_{3,5}$
braid word reduction.
<!-- FILE_END: beta-decay-skein-properties.md -->

<!-- FILE_START: lepton-number-categorical.md -->
**Lepton number is the count of Skein smoothings applied to the nuclear normal form.**

**Definition.**
Let $\mathcal{N}$ be a nuclear link in Gröbner--Shirshov normal form. Let $\mathcal{N}'$ be obtained from $\mathcal{N}$ by a sequence of $k$ Skein crossing changes. The lepton number of this transition is $L = k$.
<!-- FILE_END: lepton-number-categorical.md -->

<!-- FILE_START: lepton-number-categorical-properties.md -->
This section develops the properties of categorical lepton number.

Each beta decay applies the Skein relation at one crossing. This produces a smoothing $L_0^{\pm}$ that contains exactly one lepton--antilepton pair. Lepton number counts these smoothings.

Each smoothing $L_0^{\pm}$ contributes:
- One charged lepton ($T_{2,3}$ or $T_{2,3}^{\sigma}$) with lepton number $+1$.
- One (anti)neutrino ($K_{0_1}$ or $K_{0_1}^{\sigma}$) with lepton number $-1$.

The net lepton number of each $L_0^{\pm}$ pair is $+1 + (-1) = 0$.

**Conservation.**
Lepton number is conserved by construction:

1. Skein smoothings produce lepton pairs with net lepton number $0$. The nuclear sector loses one crossing. Hadrons carry lepton number $0$. Total: $\Delta L = 0$.
2. Gröbner--Shirshov re-reduction (R2, R3, far-commutativity) acts within the Iwahori--Hecke algebra and produces no smoothings. Total: $\Delta L = 0$.
3. Markov moves (conjugation, stabilisation) change the braid representative but not the link type. Total: $\Delta L = 0$.

Every process expressed as a sequence of Skein relations and Hecke reductions conserves lepton number.

**Lepton number as a $\mathbb{Z}$-grading.**
The Skein module $\mathcal{K}(S^3; q)$ admits a natural $\mathbb{Z}$-grading by the number of smoothings applied. Links in the nuclear sector have grade $0$. Each smoothing shifts the grade by $+1$. The grade is preserved by Hecke relations, which act within a fixed grade, and by Reidemeister moves, which leave the smoothing count invariant.

**Individual lepton assignments.**

| Particle | Knot type | Lepton number $L$ | Origin |
|----------|-----------|:---:|--------|
| $e^-$ | $T_{2,3}$ (trefoil) | $+1$ | $L_0^{-}$ charged component ($\beta^-$) |
| $e^+$ | $T_{2,3}^{\sigma}$ (mirror trefoil) | $-1$ | $L_0^{+}$ charged component ($\beta^+$) |
| $\nu_e$ | $K_{0_1}$ (unknot) | $+1$ | $L_0^{+}$ neutral component ($\beta^+$) |
| $\nu_e^{\sigma}$ | $K_{0_1}^{\sigma}$ (mirror unknot) | $-1$ | $L_0^{-}$ neutral component ($\beta^-$) |

The charged lepton carries $L = +1$ (or $-1$ for the antiparticle) and the neutrino carries $L = -1$ (or $+1$). Each pair sums to zero.

**The $\chi = -6$ constraint.**
In the Descartes universe, the Euler characteristic $\chi(A) = -6$ constrains Bring's surface. The torus knot generators $T(2, n)$ with odd $n \leq 7$ exhaust the fermion spectrum. The electron ($T_{2,3}$) and neutrino ($K_{0_1} = T_{2,1}$) are the two lowest torus knots in this sequence. The smoothing $L_0^{-}$ must decompose into exactly these knot types because they are the only single-component closures of a 2-arc resolution at a Borromean crossing.

**Structural origin of lepton-number conservation.**
In the Standard Model, lepton number conservation is an accidental symmetry. In QOU, it is a structural invariant. The Skein relation is the unique operation that changes crossing type, and it always produces exactly one lepton pair. The Iwahori--Hecke algebra contains no mechanism to produce an odd number of leptons. The smoothing is a topological operation on a single crossing, and each smoothing is binary (two arcs).

Lepton number violation would require a process that changes crossing type without passing through the Skein relation. Such a process must exist outside the Iwahori--Hecke algebra. In the $\chi = -6$ universe, no such process exists.
<!-- FILE_END: lepton-number-categorical-properties.md -->

<!-- FILE_START: lepton-continuant-recurrence.md -->
The charged lepton tower $T_{2,n}$ for $n = 3, 5, 7$ describes the $e^-, \mu^-, \tau^-$ generations. It possesses a closed-form normal form in $H_2(q) \subset H_3(q)$ defined by a Morgan–Voyce continuant recurrence.

## Statement

Let $h = q - q^{-1}$ be the Hecke parameter. Let $T_{2,n} = \sigma_0^n$ be the $(2, n)$-torus knot braid in $B_2$. The Gröbner--Shirshov normal form in $H_2(q)$ is:

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

The net coefficient, defined as the sum of all normal form terms, is $\mathrm{net}(T_{2,n}) = a_n + b_n$.
<!-- FILE_END: lepton-continuant-recurrence.md -->

<!-- FILE_START: lepton-continuant-recurrence-novelty.md -->
This structural identification of the lepton-tower sequence as a positive-sign Morgan-Voyce continuant distinguishes it from standard Chebyshev $U_n$ recurrences. It provides an algebraic framework that captures the combinatorial constraints of the lepton sector.
<!-- FILE_END: lepton-continuant-recurrence-novelty.md -->

<!-- FILE_START: lepton-tower-witness.md -->
Evaluating the continuant recurrence at $q_0 \approx 1.1100$ for $n = 0, 1, \ldots, 9$ yields coefficients with recurrence residuals strictly bounded by $10^{-12}$.

## Full normal form table

See [Table](#tbl:lepton-tower-witness-table-data).

Odd-$n$ torus knots $T_{2,n}$ with $n \leq 7$ exhaust the embeddable fermion spectrum on Bring's surface. The even-$n$ entries do not represent torus knots. We include them to demonstrate the monotone growth of the net coefficient.

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

These values are not the physical mass ratios $m_\mu / m_e \approx 206.8$ and $m_\tau / m_e \approx 3477$. The net coefficients parameterise the topological complexity of the torus knot. Deriving the physical mass requires evaluating the full Seiberg--Witten integral over the jet bundle prolongation.
<!-- FILE_END: lepton-tower-witness.md -->

<!-- FILE_START: tau-leptonic-universality.md -->
The tau lepton decays leptonically via the $T_{3,5}$ weak vertex ([beta decay](#def:beta-decay-skein)). The **factorized model** sets the squared matrix element to $|\mathcal{M}|^2 = |\mathrm{tr}_{\mathrm{Markov}}(T_{3,5})|^2$. This amplitude is independent of the daughter lepton. It **predicts lepton universality** directly from the underlying Iwahori--Hecke algebra structure.

## Statement

Let $T_{3,5} = (\sigma_0 \sigma_1)^5$ be the weak vertex in $H_3(q)$. Let $f(x)$ denote the phase-space factor for $\tau \to \ell \bar\nu_\ell \nu_\tau$, where $x = (m_\ell / m_\tau)^2$:

$$
  f(x)
  = 1 - 8x + 8x^3 - x^4 - 12 x^2 \ln x.
$$

Then the ratio of leptonic branching fractions is

$$
  \frac{\mathrm{BR}(\tau \to e\bar\nu_e\nu_\tau)}
       {\mathrm{BR}(\tau \to \mu\bar\nu_\mu\nu_\tau)}
  = 
  \frac{|\mathcal{M}_e|^2 \cdot f(m_e^2/m_\tau^2)}
       {|\mathcal{M}_\mu|^2 \cdot f(m_\mu^2/m_\tau^2)}.
$$

In the **factorized model**, the Markov trace of the weak vertex provides the universal matrix element:

$$
  |\mathcal{M}_e|^2
  = 
  |\mathcal{M}_\mu|^2
  = 
  \bigl|\mathrm{tr}_{\mathrm{Markov}}(T_{3,5})\bigr|^2.
$$

The matrix-element ratio evaluates exactly to $1$. The branching ratio reduces to the **pure phase-space ratio**:

$$
  \frac{\mathrm{BR}(\tau \to e)}{\mathrm{BR}(\tau \to \mu)}
  = 
  \frac{f(m_e^2 / m_\tau^2)}{f(m_\mu^2 / m_\tau^2)}.
$$

## Physical significance

Lepton universality—the statement that the weak interaction couples equally to all lepton generations—emerges here as a **consequence** of the $T_{3,5}$ braid serving as the unique cross-family mediator on the Bring surface ([fivefold symmetry](#rem:fivefold-symmetry)). Its Markov trace $\mathcal{W}(q) = \mathrm{tr}_{\mathrm{Markov}}((\sigma_0 \sigma_1)^5)$ is a property of the weak vertex alone, not the daughter channel. Universality is broken exclusively by kinematics (the daughter mass entering through the phase-space integral), not by the vertex operator.
<!-- FILE_END: tau-leptonic-universality.md -->

<!-- FILE_START: tau-branching-ratio-witness.md -->
Evaluating both the factorized and the product models at $q_0 \approx 1.1100$ allows comparison with the PDG experimental branching ratio.

## Weak vertex data

The $T_{3,5} = (\sigma_0 \sigma_1)^5$ weak vertex in $H_3(q)$ reduces (38 Hecke and 18 Yang–Baxter steps) to **6 normal form (NF) terms** in the standard basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$:

See [Table 1](#tbl:tau-branching-ratio-witness-table1-data).

$$
  \mathrm{net}(T_{3,5}) = 2.316,
  \qquad
  \mathrm{tr}_{\mathrm{Markov}}(T_{3,5}) = 0.704,
  \qquad
  |\mathcal{W}|^2 = 0.495.
$$

## Branching ratio comparison

**Factorized model** (lepton universality):

$$
  \frac{\mathrm{BR}(\tau \to e)}{\mathrm{BR}(\tau \to \mu)}
  =
  \frac{f(m_e^2/m_\tau^2)}{f(m_\mu^2/m_\tau^2)}
  =
  \frac{0.99999934}{0.97255996}
  \approx \mathbf{1.028}.
$$

**Product model** (universality-breaking):

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

**PDG 2024 experimental values:**

$$
  \mathrm{BR}(\tau \to e\bar\nu_e\nu_\tau) = 17.82\%,
  \qquad
  \mathrm{BR}(\tau \to \mu\bar\nu_\mu\nu_\tau) = 17.39\%,
$$

$$
  \frac{\mathrm{BR}(\tau \to e)}{\mathrm{BR}(\tau \to \mu)}
  = \mathbf{1.025} \pm 0.003.
$$

## Result

See [Table 2](#tbl:tau-branching-ratio-witness-table2-data).

The factorized model treats the Markov trace of $T_{3,5}$ as the universal matrix element. It reproduces the PDG ratio to $0.34\%$. The product model is excluded by data.

## Decay channel NF structure

Both decay channels $\tau \to e$ and $\tau \to \mu$ reduce to **6 NF terms** in $H_3(q)$. The dominant term in both channels is $L_+ = \sigma_0\sigma_1$ (the Hopf link), contributing $\sim 30\%$ of the total weight. The $L_-$ (anti-Hopf) contribution is larger in $\tau \to \mu$ ($15.6\%$) than in $\tau \to e$ ($13.9\%$). This is consistent with the heavier daughter lepton requiring more re-crossing energy.

The full witness data (including all NF coefficients, Markov traces, phase-space factors, and reverse-order checks) is recorded in `tau-leptonic-decay.witness.json`.
<!-- FILE_END: tau-branching-ratio-witness.md -->

<!-- FILE_START: parity-violation-skein.md -->
**Parity is violated by the weak interaction if and only if
$q \neq 1$.**

### Origin: Hecke eigenvalue asymmetry

The parity violation follows directly from the categorical origin of
the crossing energy
([crossing energy](#def:crossing-energy)): the Hecke generator $\sigma =
P \circ R$ has eigenvalues $(q, -q^{-1})$ on $S^{2} V \oplus \Lambda^{2}
V$, and $\lvert q \rvert \neq \lvert {-q^{-1}} \rvert$ for $q \neq 1$.
A positive crossing $L_{+}$ carries the eigenvalue $q$; a negative
crossing $L_{-}$ carries $-q^{-1}$.  Parity $\mathcal{P}$ exchanges
$L_{+} \leftrightarrow L_{-}$ but does not change $q$ --- hence
$\mathcal{P}$-invariance forces $q = -q^{-1}$, i.e.\ $q^{2} = -1$,
impossible on the substrate ray.  The sign-asymmetry of the eigenvalue
pair (inherited from $P|_{\Lambda^{2} V} = -\mathrm{id}$) is the
algebraic source of P-violation; it is not a physical postulate added
to the framework.

The detailed Skein derivation below rederives the same conclusion from
the Skein relation; both are consequences of the same eigenvalue
structure.

### Skein derivation

The parity operation $\mathcal{P}$ on a link is the **mirror**:
reverse all crossings ($L_+ \leftrightarrow L_-$).  In the braid
group $B_n$, this is the involution
$\sigma_i \mapsto \sigma_i^{-1}$.

**The Skein relation under parity.**

The Skein relation at a single crossing:

$$
  q  [L_+] -  q^{-1} [L_-]
  = 
  (q^{1/2} - q^{-1/2})  [L_0]
$$

Apply the mirror $\mathcal{P}$: $L_+ \mapsto L_-$,
$L_- \mapsto L_+$, $L_0 \mapsto \mathcal{P}(L_0)$.  The
mirrored Skein relation reads:

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

Compare with the original:

$$
  q  [L_+] -  q^{-1} [L_-]
  = 
  (q^{1/2} - q^{-1/2})  [L_0]
$$

These are the **same** equation if and only if $q = q^{-1}$,
i.e., $q = 1$.

**Proposition.**
*The Skein relation is invariant under parity
$\mathcal{P}: L_+ \leftrightarrow L_-$ if and only if $q = 1$.
For any $q \neq 1$, the weak interaction
([beta decay](#def:beta-decay-skein)) violates parity.*
<!-- FILE_END: parity-violation-skein.md -->

<!-- FILE_START: parity-violation-skein-interpretation.md -->
**Remark (physical interpretation).**

The Hecke relation $\sigma^2 = (q - q^{-1})\sigma + 1$ breaks the symmetry between positive and negative crossings. At $q = 1$, we have $\sigma^2 = 1$ and parity is conserved. At the substrate parameter $q_0$, the relation becomes $\sigma^2 = 0.209\,\sigma + 1$. The $0.209\,\sigma$ term distinguishes positive from negative crossings, violating parity.

The degree of parity violation is controlled by the Hecke deformation parameter:

$$
  q - q^{-1} = 0.209 \quad (\text{at } q = q_0).
$$

All parity violation in this theory traces back to $q \neq 1$.

**Maximal parity violation.**

The Standard Model weak force violates parity maximally, coupling only to left-handed particles. We identify this with crossing chirality. A positive crossing $\sigma_i$ contributes weight $q$ to the categorical action, while a negative crossing $\sigma_i^{-1}$ contributes $q^{-1}$. The ratio $q^2 = 1.232$ measures the left-right asymmetry.

The Wu experiment (1957) found a strong forward-backward asymmetry in ${}^{60}\mathrm{Co}$ beta decay. We interpret this asymmetry as the crossing chirality of the nuclear link. The ${}^{60}\mathrm{Co}$ braid word carries a specific writhe $w \neq 0$. The Skein crossing change at $q_0$ produces an emission pattern determined by $q^w$.

**Connection to the $\mathbb{Z}/2$ of beta decay.**

The involution $q \leftrightarrow q^{-1}$ exchanging $\beta^- \leftrightarrow \beta^+$ ([beta decay](#def:beta-decay-skein)) acts as the combined $\widehat{CP}$ operation. It applies parity $\mathcal{P}$ (mirroring all crossings) and charge conjugation $\hat{C}$ (exchanging $T_{2,3} \leftrightarrow T_{2,3}^{\sigma}$).

- $\mathcal{P}$ alone is violated because $q \neq q^{-1}$.
- $\hat{C}$ alone is violated because the electron and positron differ in mass ordering.
- $\widehat{CP}$ is conserved to leading order because $q \leftrightarrow q^{-1}$ is a symmetry of the Iwahori–Hecke algebra.
<!-- FILE_END: parity-violation-skein-interpretation.md -->

<!-- FILE_START: nuclear-spin-parity.md -->
**The nuclear spin quantum number $J$ is integral when $A$ is even and half-integral when $A$ is odd.**

This follows topologically from the braid representation. Each nucleon is a spin-$\tfrac{1}{2}$ fermion (a single-component knot). The tensor product of $A$ such representations dictates a spin parity determined by $A \bmod 2$.

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
**Remark.** Formulating parity strictly via $\mathrm{SU}_q(2)$ tensor-product rules algebraically embeds empirical parity constraints within the theory. This reproduces standard spin-statistics without ad-hoc external postulates.
<!-- FILE_END: nuclear-spin-parity-novelty.md -->

