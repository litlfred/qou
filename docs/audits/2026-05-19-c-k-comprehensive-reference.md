# Q_β precision-ladder $c_k$ comprehensive reference

**Date:** 2026-05-19
**Branch:** `claude/qbeta-followup-pending-2026-05-19` (PR #804)
**Context:** user direction to surface for each $c_k$: where used, value, derivation route, physical meaning, math meaning, mathematical spaces it lives in, alternative interpretations.

## Master formula (where ALL c_k live)

$$
\boxed{\;
Q_\beta^{\text{cat}}(q) \;=\;
\underbrace{m_e \cdot \tfrac{|q^2 - 2q - 1|(q+1)}{2q^3}}_{Q_A: \text{ Form A baseline}}
\;\cdot\;
\underbrace{\cos\!\bigl(\alpha - \tfrac{b\,\hbar_q^2}{2}\bigr)}_{N=1 \text{ rung}}
\;\cdot\;
\underbrace{\prod_{k=2}^{\infty}\bigl(1 + c_k(q)\cdot b(q)^k \cdot \hbar_q(q)^{2k}\bigr)}_{N\ge 2 \text{ rungs}}
\;}
$$

with:
- $b(q) = \sqrt{q^4 + q^2 + 1}/(q^2+1)$ — Hoefsmit off-diagonal coupling on $V_{(2,1)}$
- $\hbar_q = (q-1)/q$ — substrate quantum Planck constant
- $\alpha = (z-1)\cdot h / 2$ — single-wrap eigenphase
- $z = 1/(\sqrt q + 1/\sqrt q)$ — Markov parameter
- $h = q - q^{-1}$ — Hecke skein parameter
- $q_0 \approx 1.10998$ — substrate parameter (CAL-2)
- $m_e$ — electron mass (CAL-1)

## Per-rung comprehensive table

### $c_1$ — single-wrap Kashiwara phase

- **Where it lives in the formula**: $\cos\!\bigl(\alpha - \tfrac{b\,\hbar_q^2}{2}\bigr)$ — INSIDE the cos argument (not a multiplicative factor like $k \ge 2$).
- **Value at $q_0$**: $b(q_0) \approx 0.8676$ (real, $\in (0, 1)$).
- **Derivation route**: **DERIVED** — Hoefsmit seminormal $\sigma_2$ off-diagonal element on $V_{(2,1)}$ at H_3(q). See `prop:hoefsmit-V21-cos-symmetrization`.
- **Physical meaning**: single-wrap eigenphase shift in the V_(2,1) Wedderburn block — Larmor-like precession of the categorical "spin-1/2" under the Hecke generator $\sigma_2$.
- **Math meaning**: matrix element $\langle T_1 | \sigma_2 | T_2 \rangle$ in the Young seminormal basis $\{T_1, T_2\}$ of V_(2,1). Equivalent to $\tilde f_1$ Kashiwara crystal arrow weight at the (2,1) crystal-graph edge.
- **Space it lives in**: V_(2,1) ⊂ H_3(q), specifically its $\mathbb{C}^2$ representation space with the Young seminormal basis. Kashiwara crystal $B(2,1)$ at $q \to 0$ limit.
- **Alternative interpretations of this space**:
  - **Crystal graph**: $B(2,1) = \{T_1, T_2\}$ with one $\tilde f_1$ edge weighted by $b$
  - **GL_2 weight 2 rep**: $V_{(2,1)} \subset \mathrm{Sym}^2(\mathbb{C}^2)$ via Schur-Weyl
  - **Casimir-eigenspace**: eigenspace of the H_3 Jucys-Murphy operator with content $(2-1=1, 1-2=-1) \to 0$
  - **Spin chain XXZ-like**: 3-site spin-1/2 chain at the V_(2,1) "magnon-1" sector

### $c_2 = -1$ — Kashiwara return amplitude squared

- **Where it lives**: $(1 - b^2 \hbar_q^4)$ — first multiplicative correction at $\hbar_q^4$.
- **Value**: exactly $-1$ (by factor-convention; the $b^2$ is absorbed).
- **Derivation route**: **DERIVED** by factor convention — pure Kashiwara intra-block return amplitude $\langle T_1 | \tilde f_1^\dagger \tilde f_1 | T_1 \rangle = b^2$. See `prop:q-beta-categorical-precision-ladder` § N=2 row.
- **Physical meaning**: probability amplitude to "return" to the starting V_(2,1) state after one Kashiwara up-then-down. Pure intra-block effect (no inter-block coupling).
- **Math meaning**: $b^2 = \langle f_1, f_1\rangle$ on V_(2,1); equivalently $(q^4+q^2+1)/(q^2+1)^2$.
- **Space**: same V_(2,1) ⊂ H_3(q), but bilinear (b² = squared coupling).
- **Alternative interpretations**:
  - **Quantum probability**: $b^2 = |\tilde f_1|^2$ as a quantum-mechanical transition probability
  - **Frobenius pairing**: $b^2 = (T_1, T_1)_{\text{Frobenius}}$ in the Frobenius inner product on V_(2,1)
  - **Wenzl projector**: $b^2$ as a component of the Wenzl projector matrix on V_(2,1)

### $c_3 = -2 = J_{\text{Hopf}}(q{=}1)$ — proven

- **Where it lives**: $(1 - 2\,b^3\,\hbar_q^6)$ — N=3 rung.
- **Value**: exactly $-2 = J_{\text{Hopf}}(q{=}1)$.
- **Derivation route**: **DERIVED** — Fact 3 of `prop:q-beta-c3-hopf-three-fold-markov`. Two-strand sub-braid windings → Hopf-link Markov closure → KL classical limit at $q=1$ gives the Jones polynomial value $-2$.
- **Physical meaning**: leading-order entanglement contribution from inter-Wedderburn-block coupling at 3-fold Markov closure. The "two-strand Hopf substructure" inside the typed-B_3 braid that survives the KL classical limit.
- **Math meaning**: $J_{\text{Hopf}}(q=1) = -(q+q^{-1})|_{q=1} = -2$ (reduced Jones polynomial of positive Hopf link at $q=1$).
- **Space**: Skein module / Hecke algebra trace pairing $H_n(q) \otimes H_n(q) \to \mathbb{C}$ via Markov trace. At $q=1$ this is the centre of $\mathbb{C}[S_n]$ — a commutative ring of class functions.
- **Alternative interpretations**:
  - **Khovanov bigraded rank**: $|\mathrm{Kh}(\text{Hopf})(q=1, t=-1)| = 4$ unreduced; $J = -2$ reduced
  - **Witten-Reshetikhin-Turaev invariant**: $Z_{SU(2)_k}(\text{Hopf})$ at $k \to \infty$
  - **Linking number**: $\mathrm{lk}(\text{Hopf}) = \pm 1$ → Jones $\propto -q^{2\,\mathrm{lk}}$ at $q=1$ gives $-2$
  - **Kazhdan-Lusztig basis**: $C_{w_0}$ for the longest element of $S_2$ pairs to $-2$ under the bilinear form

### $c_4 \approx -1.144$ — empirical conjecture (closed form $c_3 \cdot b^4$, 0.9% off)

- **Where it lives**: $(1 + c_4 b^4 \hbar_q^8)$ — N=4 rung.
- **Empirical value at $q_0$**: $-1.143537$ (from SDP-T_β at 50dps).
- **Conjectured closed form**: $c_3 \cdot b^4 = -2 b^4 \approx -1.133$ (0.9% miss).
- **Derivation route**: **EMPIRICAL** — pattern-match. No first-principles derivation. See `conj:qbeta-c-k-closed-forms`.
- **Physical meaning** (conjectural): Hopf-Jones contribution multiplied by **two** Kashiwara return amplitudes ($b^4 = (b^2)^2$). "Hopf-link decoration with two extra Kashiwara loops."
- **Math meaning** (conjectural): $J_{\text{Hopf}}(q=1) \cdot b(q)^4$ — Jones value (constant) times 4th power of off-diagonal coupling. If true, this would come from a 4-strand sub-braid extraction at order $\hbar_q^8$.
- **Space**: hypothesised — $V_{(2,1)} \otimes V_{(2,1)}$ at $H_3 \times H_3$ (two copies, capturing two Kashiwara loops). OR $V_{(2,1)} \otimes V_{(2,1)}^{\vee}$ for the dual. Not pinned down.
- **Alternative interpretations of the conjectured space**:
  - **Khovanov-Rozansky bigraded module** at finite $q$ (vs $q=1$)
  - **KLR canonical-basis trace** at next-order in $\hbar_q$
  - **Spectral-sequence stratum** $E^{p,q}_\infty$ with $p+q = 4$
  - **Higher-genus torus knot decoration** (per FSC-derivation pattern): $\delta_q(T_{?,?})$ ratio
- **Status of these alternatives**: all conjectural; none discriminated by data alone at the 0.9% precision.

### $c_5 \approx -1.223$ — empirical (closed form $-(b^2 + 1/2)$, 2.4% off)

- **Where it lives**: $(1 + c_5 b^5 \hbar_q^{10})$ — N=5 rung.
- **Empirical value**: $-1.222913$ (sequential closure starting from $c_4 = c_3 \cdot b^4$).
- **Conjectured closed form**: $-(b^2 + 1/2)$ — Kashiwara $b^2$ plus half-Hopf integer offset.
- **Derivation route**: **EMPIRICAL** — pattern-match. The $-(b^2 + 1/2)$ form was originally proposed as $c_4$ in earlier drafts; the 2026-05-19 audit re-attributed it to $c_5$ (PR #777).
- **Physical meaning** (conjectural): Kashiwara return amplitude $b^2$ plus a "half-Hopf" topological integer offset. Mixed intra/inter contribution.
- **Math meaning**: unclear. The $-1/2$ offset doesn't have an obvious categorical source. **One open guess**: $1/2$ from the Markov-bridge weight $y_{(2,1)}(q=1) = 1/4$ doubled (since V_(2,1) has dimension 2). Speculative.
- **Space**: same H_3(q) but the half-integer suggests **two-fold cover** or **double-cover** at the Wedderburn level — concretely, $V_{(2,1)} \otimes V_{(2,1)}$ with a specific projection. Or the **anti-symmetrisation** $\wedge^2 V_{(2,1)}$.
- **Alternative interpretations**:
  - **Half-integer Wess-Zumino term** from anomaly cancellation
  - **Pfaffian-like contribution** at $\wedge^2 V_{(2,1)}$
  - **Modular S-matrix entry** $S_{0,(2,1)}$ in the WRT TQFT data
  - **Spin-statistics half-integer** in the q-deformed spin chain

### $c_6 \approx +3.498$ — empirical (closed form $c_3^2 \cdot b^2 = 4b^2$, 14% off)

- **Where it lives**: $(1 + c_6 b^6 \hbar_q^{12})$ — N=6 rung.
- **Empirical value**: $+3.497562$.
- **Conjectured closed form**: $c_3^2 \cdot b^2 = 4 b^2 \approx 3.011$ (14% miss — degraded match).
- **Derivation route**: **EMPIRICAL** — the match is 6.5× tighter than no-correction but not a clean closed form.
- **Physical meaning** (conjectural): Hopf-Jones SQUARED times Kashiwara return amplitude. "Two Hopf-link contributions with one Kashiwara loop."
- **Math meaning** (conjectural): $(J_{\text{Hopf}}(q=1))^2 \cdot b(q)^2$ — possibly from a 2nd-order expansion of a Hopf-link-squared categorical observable.
- **Space**: $V_{(2,1)}^{\otimes 2}$ at higher Hecke level, or a 6-strand sub-braid extraction. Speculative.
- **Alternative interpretations**:
  - **Square of Jones** — but $(J_{\text{Hopf}})^2$ at $q=1$ is $4$, not the empirical $+3.498$. The $b^2$ factor accounts for the discrepancy ($4 \cdot 0.753 = 3.011$).
  - **Multiplicity in Wedderburn product**: $V_{(2,1)} \otimes V_{(2,1)} = V_{(2)} \oplus V_{(1,1)} \oplus V_{(2,1)}$ (Clebsch-Gordan); coefficient 4 = 1+2+1 ?
  - **Borel-Weil-Bott contribution** at 2nd cohomological order
  - **Trace of Casimir squared** on a specific weight space

### $c_7 \approx +57.149$ — empirical (closed form $c_3^3 = -8$, signed error +114%)

- **Where it lives**: $(1 + c_7 b^7 \hbar_q^{14})$ — N=7 rung.
- **Empirical value**: $+57.149243$.
- **Conjectured closed form**: $c_3^3 = -8$ — **WRONG**: signed relative error $|{-8} - 57.149|/57.149 \approx 114\%$ (magnitude-only error $86\%$, opposite sign of conjecture).
- **Why retained**: at N=7 the **leverage limit** kicks in. $c_7 \cdot b^7 \hbar_q^{14}$ is at scale $10^{-13}$; ANY $c_7 \in [-100, +100]$ closes the residual to within $10^{-4}$ ppb. The actual value is **not uniquely determined** by closure data.
- **Derivation route**: **EMPIRICAL pattern guess** at the leverage floor. Categorical interpretation is highly speculative.
- **Physical meaning**: at this leverage scale, no clean physical interpretation. The framework's L2 100×-experimental target (7.8 ppb) is met at N=3 — c_4..c_7 are research-grade overprecision beyond physical relevance.
- **Math meaning**: $c_3^3 = -8$ was the "Jones cubed" guess. The actual +57 doesn't match. **No known categorical structure** generates +57 at q_0.
- **Space**: undetermined.
- **Alternative interpretations**: unconstrained — the data doesn't discriminate. Could be $J_{\text{trefoil}}^3 = -27$, sum of multiple Khovanov ranks, anything in the leverage band.

## Spaces summary

| $c_k$ | Primary space | Inner-product structure | Categorical role |
|:----:|:-:|:-:|:-:|
| $c_1$ | $V_{(2,1)}$ at $H_3(q)$ | Young seminormal | Kashiwara $\tilde f_1$ matrix element |
| $c_2$ | $V_{(2,1)}$ | Frobenius / Wenzl | Return amplitude $b^2$ |
| $c_3$ | $H_n(q)$ skein module | Markov trace (centre at $q=1$) | Hopf-link Jones invariant |
| $c_4$ | $V_{(2,1)}^{\otimes 2}$ ? | conjectural | conjectural (Jones × Kashiwara²) |
| $c_5$ | $\wedge^2 V_{(2,1)}$ ? | conjectural (half-integer hints anti-symmetrisation) | conjectural |
| $c_6$ | $V_{(2,1)}^{\otimes 2}$ ? Clebsch-Gordan | conjectural | conjectural (Jones² × Kashiwara) |
| $c_7$ | undetermined (leverage limit) | undetermined | pattern guess |

## FSC-derivation inspiration

The framework's fine-structure-constant derivation
([`prop:alpha-em-categorical-trace-ratio`](../../content/quantum-observable-universe/descartes-universe/alpha-em-categorical-trace-ratio.md))
gives:

$$
\alpha_{EM} \;=\; \frac{h^2}{q \cdot \delta_q(T_{2,9}) \cdot \delta_q(T_{3,5})}
$$

where $\delta_q(T_{p,k})$ is the q-dimension of a $(p,k)$-torus knot.
**This is a categorical-trace RATIO, NOT a Taylor-ladder expansion.**

The FSC structure suggests a possible new direction for $c_k$:

**Conjecture (speculative, motivated by FSC)**: maybe $Q_\beta$ admits a closed form

$$
Q_\beta \;\stackrel{?}{=}\; m_e \cdot \frac{P(q, h, b, \delta_q(T_{p,k}))}{Q(q, h, b, \delta_q(T_{p',k'}))}
$$

for SPECIFIC torus knots $T_{p,k}$ and a rational function $P/Q$. If true, the $c_k$ precision-ladder factors would be a **Taylor expansion** of this rational form — and the "closed forms" we've been chasing would be the cyclotomic / q-integer building blocks of this ratio.

Concrete probes inspired by FSC:
1. Express $Q_\beta$ at $q_0$ as a ratio $A/B$ where $A, B$ are products of $\delta_q(T_{p,k})$. Search systematically over $(p, k)$ ∈ small finite set.
2. Check if any product of $[n]_q$ q-integers (e.g., $[2]_q [3]_q$, $h \cdot [9]_q$ etc.) gives $Q_\beta$ to higher precision than Form A.
3. The FSC's denominator $\delta_q(T_{2,9}) \cdot \delta_q(T_{3,5}) = h \cdot [9]_q \cdot h \cdot [5]_q \cdot$ (something) suggests a "denominator-as-product-of-q-integers" pattern.

This is a **new direction** not in the closure-path roadmap. Could be productive in a follow-up session.

## Honest closing assessment

After exhausting:
- SDP-T_β operator identification (Path 1, negative)
- Per-block c_k decomposition (Path 2, falsified)
- Multi-loop Kashiwara counting (negative)
- Khovanov ranks at q=1 (only gives c_3)
- Per-block cyclotomic closed forms (verifies paper, doesn't extract c_k)
- Uniform y_λ-weighted rule (falsified at q_0)

**c_4..c_7 first-principles derivation remains OPEN.** The framework PROVES only c_3. Everything else is empirical pattern-match formalised as `conj:qbeta-c-k-closed-forms` in PR #804.

The new FSC-inspired direction (torus-knot ratio) is the **most concrete unexplored angle** — but pursuing it is research-grade work, not a session deliverable.

## Cross-references

- [`prop:q-beta-categorical-precision-ladder`](../../content/quantum-observable-universe/braids-and-knots/q-beta-categorical-precision-ladder.md) — master formula
- [`prop:q-beta-c3-hopf-three-fold-markov`](../../content/quantum-observable-universe/braids-and-knots/q-beta-c3-hopf-three-fold-markov.md) — c_3 derivation (Fact 3)
- [`rem:per-block-hopf-jones-absorption-pattern`](../../content/quantum-observable-universe/braids-and-knots/per-block-hopf-jones-absorption-pattern.md) — LO ε^1 pattern
- [`conj:qbeta-c-k-closed-forms`](../../content/quantum-observable-universe/braids-and-knots/conj-qbeta-c-k-closed-forms.md) — formalisation of c_4..c_7 as conjectures (this PR)
- [`prop:alpha-em-categorical-trace-ratio`](../../content/quantum-observable-universe/descartes-universe/alpha-em-categorical-trace-ratio.md) — FSC-derivation inspiration
- [`docs/audits/2026-05-19-qbeta-ladder-closure-path.md`](2026-05-19-qbeta-ladder-closure-path.md) — three closure paths (Path 1/2/3)
- [`docs/audits/2026-05-19-qbeta-ladder-sdp-c2-c3-derived.md`](2026-05-19-qbeta-ladder-sdp-c2-c3-derived.md) — SDP-T_β framework
