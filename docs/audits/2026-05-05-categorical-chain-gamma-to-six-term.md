# Categorical chain γγ → trefoil → atomic braid → six-term mass formula

**Status.** Symbolic-q derivation, all-by-hand. Round-3 of PR #546
extends the closed-form $\mathrm{tr}_M$ work.

This document tracks each categorical operation from $\gamma\gamma$
pair production through the six-term mass formula, identifying which
quantities now have closed symbolic forms in $q$ and which remain
gaps.

## Notation

- $q$ — substrate parameter, $q_0 \approx 1.10998$.
- $h = q - q^{-1}$ — Hecke-skein amplitude.
- $z = 1/(\sqrt q + 1/\sqrt q)$ — Markov parameter (Ocneanu/Wenzl
  trace).
- $H_n(q)$ — Iwahori-Hecke algebra on $n$ strands.
- $\sigma_i \in H_n$ — i-th generator, satisfying
  $\sigma_i^2 = h\sigma_i + 1$.
- $\mathrm{tr}_M$ — Ocneanu Markov trace,
  $\mathrm{tr}_M = \sum_\lambda y_\lambda(q) \chi^\lambda$.
- $E_{0,\beta} \approx 0.782$ MeV — free-neutron β-decay $Q$.
- $\alpha = m_e \cdot 8G \approx 3.7445$ MeV — Borromean coupling.

## Step 1 — γγ pair production

Two photons → categorical morphism $\mathbf{1} \to A \otimes A^*$ in
$\mathbf{Rep}(\mathrm{SU}_q(2))$, where $A$ is the fundamental
2-dimensional irrep and $A^*$ its dual. Concretely, this is the
**rigidity unit** $\eta_A: \mathbf{1} \to A \otimes A^*$.

Categorically: each line is a vortex morphism $\varrho: \mathbf{1} \to V$
for some irrep $V$. The choice of $V$ determines the particle
species (electron, quark, etc.).

**Symbolic content.** $\dim_q(A) = [2]_q = q + q^{-1}$, so the trace
of the rigidity unit is $[2]_q$. This is the elementary "fermion
counting" weight.

## Step 2 — electron = trefoil $T_{2,3}$

The electron is realized as the trefoil knot $T_{2,3}$, which is the
closure of $\sigma_1^3 \in B_2$.

**Hecke reduction.** In $H_2(q)$:
$$
\sigma_1^2 = h\sigma_1 + 1
\;\Rightarrow\;
\sigma_1^3 = h\sigma_1^2 + \sigma_1 = (h^2 + 1)\sigma_1 + h.
$$

**Markov weights at $H_2$.** The two irreps $(2)$, $(1,1)$ are
1-dimensional with $\chi^{(2)}(\sigma_1) = q$,
$\chi^{(1,1)}(\sigma_1) = -q^{-1}$. Solving the linear system
$y_{(2)} + y_{(1,1)} = 1$ and $q y_{(2)} - q^{-1} y_{(1,1)} = z$:
$$
y_{(2)}(q) = \frac{q^{3/2} + q + 1}{q^3 + q^2 + q + 1}, \qquad
y_{(1,1)}(q) = \frac{q^{11/2} + q^{9/2} + q^{7/2} + q^{5/2} - q^4 - q^2}{q^{11/2} + q^{9/2} + 2 q^{7/2} + 2 q^{5/2} + q^{3/2} + \sqrt q}.
$$

**Trefoil Markov trace** (closed form):
$$
\mathrm{tr}_M(T_{2,3})
= y_{(2)} \cdot q^3 + y_{(1,1)} \cdot (-q^{-3}).
$$

At $q_0$: $\mathrm{tr}_M(T_{2,3}) \approx 0.7302$. Closed form is
a rational function in $\sqrt q$, fully symbolic. **No gap.**

## Step 3 — proton (uud) atomic braid

The proton is a 3-strand braid $\beta_p \in B_3$ whose intra-quark
crossings encode the uud quark composition:
- Three $B_3$-confinement crossings $(\sigma_0)^3 (\sigma_1^{-1})^3$.
- Three pair-coupling crossings: uu (gen 0, $\sigma$), ud (gen 0,
  averaged $\frac12(\sigma + \sigma^{-1})$), ud (gen 1, averaged).
- Two gluon self-coupling crossings on gen 0 (in the dressed word).

Total: 11 atomic crossings (canonical Markov-peel braid).

**Hecke action.** Symbolic Hoefsmit seminormal matrices for
$\lambda \in \{(3), (2,1), (1,1,1)\}$, sizes $1, 2, 1$. Per-irrep
$\chi^\lambda(\beta_p)$ now closed-form in $q$
([`hoefsmit_symbolic.py`](../../computations/hoefsmit_symbolic.py)).

**Markov weights at $H_3$.** Solved via Markov axioms on
$\{1, \sigma_1, \sigma_1\sigma_2\}$
([`markov_weights_symbolic.py`](../../computations/markov/markov_weights_symbolic.py)):
$y_{(3)}, y_{(2,1)}, y_{(1,1,1)}$ as rational functions in $\sqrt q$.
At $q_0$ they match the bridge witness to 10 digits.

**Proton tr_M closed form**:
$$
\mathrm{tr}_M(\beta_p)
= \sum_\lambda y_\lambda \chi^\lambda(\beta_p).
$$
At $q_0$: $1.0653062285923887\ldots$, matching `markov_peel`'s
canonical value $1.0653062285923893$ to 14 decimal places. **Gap
closed.**

## Step 4 — neutron (udd) atomic braid

Same as proton with quark content $udd$. Distinct $\chi^\lambda(\beta_n)$
per irrep; same $y_\lambda$ at $H_3$. Closed form gives $0.9232333\ldots$
at $q_0$, machine-precision match.

## Step 5 — deuteron $A=2$ (Z=1, N=1)

23-crossing braid in $B_6$: 11 internal crossings each for proton and
neutron, plus 1 inter-nucleon averaged crossing (mixed
$pn$ pairing) on $\sigma_2$.

**Markov weights at $H_6$.** Linear ladder system rank-deficient (6
constraints, 11 partitions). Wenzl's Schur principal specialization
gives the closed form for any $n$:
$$
y_\lambda(q) = \frac{1}{Z}\, s_\lambda(1, Q, Q^2, \ldots, Q^{r-1}),
\qquad Q = q^2,\quad Q^r = \frac{z_W}{1 - Q + z_W},\quad z_W = q\,z,
$$
with normalization $Z = \sum_\mu f^\mu s_\mu$.

**Deuteron tr_M closed form** at $q_0$: $0.3882864715477131\ldots$
vs canonical bridge $0.3882864715477134$ — $3 \times 10^{-16}$
(machine precision). **Gap closed.**

## Step 6 — Six-term mass formula

Per [`docs/audits/2026-05-04-six-term-per-weight-derivation.md`](2026-05-04-six-term-per-weight-derivation.md),
the canonical six-term mass formula has **distinct scales per term**:

$$
\begin{aligned}
B(Z, N) &= E_{0,\beta} \cdot \big(|\mathrm{tr}_M(W_{\text{free}})|
                              - |\mathrm{tr}_M(W_{\text{atom}})|\big)
\quad &&\text{[T1: binding component]} \\
&\quad + \alpha \cdot \big(T_2^{\text{atom}} - T_2^{\text{free}}\big)
\quad &&\text{[T2: single-tower brane]} \\
&\quad + \alpha \cdot \big(T_3^{\text{atom}} - T_3^{\text{free}}\big)
\quad &&\text{[T3: pair-tower with $z^2$]} \\
&\quad + T_4^{\text{atom,MeV}} - T_4^{\text{free,MeV}}
\quad &&\text{[T4: Frobenius co-Casimir, $m_e \cdot \tau(C)$]} \\
&\quad + (a_K - 1) \cdot T_1^{\text{atom}} \cdot E_{0,\beta}
\quad &&\text{[T5: chirality, multiplicative on T1]} \\
&\quad + T_6^{\text{atom,MeV}} - T_6^{\text{free,MeV}}
\quad &&\text{[T6: cyclotomic residue tail]}
\end{aligned}
$$

### Symbolic status per term

| Term | Quantity | Closed form in $q$? |
|---|---|---|
| T1 | $|\mathrm{tr}_M(W_{\text{free/atom}})|$ | ✓ **Done** (round-3 PR #546) |
| T2 | $\mathrm{Li}_2^q(-|\hat V_i^{\text{full}}|)$ | Partial — need symbolic $\hat V_i$ |
| T3 | $z^2 \sum_{i,j} \mathrm{Li}_2^q(\cdot)$ | Partial — same as T2 |
| T4 | $m_e \cdot \tau(C_{\dim_q})$ | ✓ Frobenius co-Casimir is a $q$-rational dim trace |
| T5 | $a_K \cdot C_K$ where $a_K = \prod_{pn}(1 + \mathrm{sign}\cdot h)$ | ✓ Polynomial in $h$ via partition signs |
| T6 | Habiro residue at cyclotomic poles | Partial — Habiro tail-in-ideal axiomatized |

### The two critical gaps

**Gap A — Frobenius volumes $\hat V_i^{\text{full}}$.** These are
hyperbolic volumes of complement manifolds for the atomic link, and
appear inside $\mathrm{Li}_2^q$ for T2 / T3. They're the
"per-generator hyperbolic content" $\hat V = |\rho_\lambda(\sigma_i)|$
in the Hoefsmit basis. Symbolic forms exist per $\lambda$ but the
combined T2/T3 expansion is a sum of $\mathrm{Li}_2^q$ values.

**Gap B — Cyclotomic residue tail (T6).** Habiro completion residues
at roots of unity. The Habiro tail-in-ideal axiom
([`habiro_witness_validator.py`](../../computations/habiro/habiro_witness_validator.py))
gives the structural form, but evaluating individual residues
symbolically requires either:
- direct cyclotomic specialization of the closed-form $\mathrm{tr}_M$
  (now possible since T1 is symbolic), or
- a closed-form Habiro generating function (existing witness,
  numerical).

### Constants

| Constant | Symbolic? | Value |
|---|---|---|
| $E_{0,\beta}$ | calibrated | 0.782 MeV (free-neutron β-decay $Q$) |
| $\alpha = m_e \cdot 8G$ | partly | 3.7445 MeV ($G$ = Borromean hyperbolic volume) |
| $m_e$ | calibrated | 0.51099895 MeV |
| ratio $\alpha / E_{0,\beta}$ | structural | $\approx 4.79$ |

The constants $E_{0,\beta}$, $\alpha$, $m_e$ are **dimensional
calibrations** — necessary to convert dimensionless categorical
quantities into MeV. The dimensionless ratios between them
(e.g. $\alpha/E_{0,\beta} \approx 4.79$) are themselves predictions
of the categorical theory and reduce to $q$-rational expressions
modulo the choice of $G$ (Borromean volume) which is a topological
invariant of the link complement.

## Path to closing the remaining gaps

1. **Gap A — symbolic $\hat V_i$.** Each $\hat V_i$ is a per-generator
   spectral norm of the seminormal Hoefsmit matrix. For 1-dim irreps
   it's just $q$ or $q^{-1}$ (eigenvalues). For 2-dim irreps it's
   $\max(\text{eigenvalues})$ — closed form via the Hoefsmit 2×2
   block (already symbolic). $\mathrm{Li}_2^q(-x) = \sum_n x^n / [n]_q^2$
   is a $q$-deformed dilogarithm; its evaluation on rational $x$
   has a closed form via the Habiro-Garoufalidis quantum dilogarithm.

2. **Gap B — T6 from symbolic $\mathrm{tr}_M$.** Now that the
   atomic $\mathrm{tr}_M$ is closed-form rational in $q$, its
   residues at cyclotomic roots of unity $q^k = 1$ are computable
   directly via partial fractions. The Habiro residue tail is
   $T_6 = \sum_{\zeta_n} \mathrm{Res}_{q = \zeta_n}\mathrm{tr}_M$
   weighted by $1/[n]$. This is a finite calculation per witness.

3. **Combine.** Once Gap A and B are closed, the entire 6-term
   formula is rational in $q$ (modulo the dimensionful calibrations
   $E_{0,\beta}, m_e, G$). Mass predictions become
   $m(q_0) = (\text{rational in } q_0) \cdot (\text{calibration})$.

## What's new in PR #546 round-3

- Closed-form symbolic Jones-Markov weights $y_\lambda(q)$ at $H_3$
  (linear-system path) and any $n$ (Wenzl Schur principal
  specialisation path).
- $\mathrm{tr}_M(\text{proton, neutron, deuteron})$ to ≥14 decimal
  places at $q_0$ vs canonical bridge; formula is symbolic.
- Reusable infrastructure: `markov_weights_symbolic.solve_y_lambda(n)`
  and `y_lambda_symbolic(n)`.

The path forward is mechanical: substitute the closed-form
$\mathrm{tr}_M$ into T1, then attack Gap A (T2/T3) and Gap B (T6)
in sequence using the closed-form atomic Markov trace as the
generating object.
