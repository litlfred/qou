The chirality factor $a_K = 1 + w(K) \cdot h$, where $w(K)$ is the
writhe of the knot $K$ and $h = q - q^{-1}$, is derived to first
order in $h$ from the Kauffman framing formula applied to the ribbon
twist on $H_n(R, q)$
([prop:chirality-writhe-ribbon-derivation](#prop:chirality-writhe-ribbon-derivation)).
This conjecture states the exact (all-orders) form and asserts that
the first-order truncation is the correct chirality factor for all
confined knots in the model.

## Statement

**Status:** Refuted at the audited atomic braids.  The conjecture
*as originally stated* (below) has been falsified for $D, T, {}^3\mathrm{He}$ —
see the [refutation status note](#refutation-status-note) and
"Generalisation" subsection.  The statement is preserved here as the
historical conjecture text; the empirical $(1+h)(1-h) \approx 0.956$
pattern that motivated it requires a different construction
(see [Residual](#residual) below).

**Conjecture (historical, refuted at $A \geq 2$).**
*Let $K$ be a confined knot with writhe $w(K)$ and canonical Hecke
braid element $T_w \in H_{n_0}(R, q)$.  The chirality factor of $K$
in the mass formula
([thm:knot-mass-formula-unified](#thm:knot-mass-formula-unified))
is the exact Wedderburn-weighted ribbon-twist ratio:*

$$
  a_K
  \;=\;
  \frac{
    \sum_\lambda w_\lambda(q)\, q^{2 w(K) c(\lambda)}\, \chi_\lambda(T_w)
  }{
    \sum_\lambda w_\lambda(q)\, \chi_\lambda(T_w)
  },
$$

*where:*
- *$w_\lambda(q)$ are the Wenzl-bridge Markov weights
  ([prop:alpha-k-derivation-procedure](#prop:alpha-k-derivation-procedure)),*
- *$c(\lambda) = \sum_{x \in \lambda}(\mathrm{col}(x) - \mathrm{row}(x))$
  is the total content of the Young diagram $\lambda$,*
- *$\chi_\lambda(T_w)$ is the Hecke character of $T_w$ in the
  Wedderburn summand $\lambda$.*

*The conjecture further claimed that for all nucleon and nuclear knots
appearing in the QOU model, this exact form equals $1 + w(K) \cdot h$
to the precision required by the $0.75\%$ accuracy of the mass formula
— this claim is now refuted: at $D, T, {}^3\mathrm{He}$ the exact
ratio diverges by ${\sim}10^4$ from the empirical $(1+h)(1-h)$
pattern (per Copilot review #r3213373225, made consistent with the
"conclusively wrong" finding below).*

> **Status note (2026-05-09; refutation pending reconciliation).**
> Direct numerical evaluation of the ratio above for the audited
> atomic braids D ($H_6$), T ($H_9$), $^3$He ($H_9$) at $q_0$ — see
> `chirality-avg-content-atomic.witness.json` and the "Generalisation"
> subsection below — finds the exact ratio diverges by $\sim 10^4$
> (T) and $\sim 10^4$ (³He) from the empirical $(1+h)(1-h) \approx
> 0.956$ pattern, and the first-order linearisation does not match
> either.  The conjecture **Statement** above is therefore **scoped
> as historical/aspirational** for the audited atomic braids until
> reconciled.  Current best understanding: the chirality factor for
> atomic braids is *not* the ribbon-twist Markov-trace ratio above
> in its stated form; an alternate construction is needed (see
> "Implications" / "Residual" at the end of the **Generalisation**
> section).  The Hecke-character invariants $\langle c \rangle_\beta$
> from this conjecture are still well-defined and witnessed; only
> the specific way they feed into $a_K$ is in question.

## Derivation sketch

**Step 1: Ribbon twist.**  In the Hecke algebra $H_n(q)$, the ribbon
element $\theta$ acts on each irreducible $V_\lambda$ as scalar
multiplication by $\theta_\lambda = q^{c(\lambda)}$, where
$c(\lambda) = \sum_{x \in \lambda}(j(x) - i(x))$ is the
Frobenius content of $\lambda$ ($i(x)$ = row, $j(x)$ = column of
cell $x$).

**Step 2: Framing change.**  Under a $+1$ framing change
($w(K) \mapsto w(K) + 1$), the Kauffman framing formula gives:

$$
  J_K(q)\big|_{w+1}
  \;=\;
  q^{c(\mu)} \cdot J_K(q)\big|_w,
$$

where $\mu$ is the dominant representation label for the standard
colored Jones polynomial.  The factor $q^{c(\mu)}$ is exactly
$\theta_\mu$, the ribbon twist eigenvalue.

**Step 3: Full writhe.**  After $w(K)$ framing changes, each
$V_\lambda$-component picks up $q^{w(K) \cdot 2c(\lambda)}$
(squared because the twist appears twice — once for each end of
the strand that closes the braid).  The Markov trace then gives the
ratio in the conjecture statement.

**Step 4: First-order expansion.**

$$
  q^{2 w(K) c(\lambda)}
  \;=\;
  e^{2 w(K) c(\lambda) \log q}
  \;=\;
  1 + 2 w(K) c(\lambda) \log q + O(h^2).
$$

Since $\log q = \tfrac{1}{2} h + O(h^3)$ (with $q = e^{h/2}$
in the standard normalization), the leading correction is
$w(K) c(\lambda) h$.  After Markov-averaging over $\lambda$ with
weights $w_\lambda \chi_\lambda(T_w)$, the numerator gives
$1 + w(K) h \langle c(\lambda) \rangle_\beta + O(h^2)$, where
$\langle c(\lambda) \rangle_\beta$ is the Plancherel-weighted mean
content.

The conjecture splits along **chirality class**:

- **Amphichiral case (verified, 2026-05-09).** Writhe is a property
  of a chosen braid representative, not a knot invariant; for the
  *canonical* amphichiral representatives used in the QOU model
  (e.g. the figure-eight word
  $\sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$ in
  `chirality-avg-content.witness.json`) the chosen representative
  has writhe $w(\beta) = 0$.  The bar-involution / transposition
  symmetry $\chi^\lambda(T_w) = \chi^{\lambda^T}(T_w)$ then combines
  with $c(\lambda^T) = -c(\lambda)$ to give
  $\langle c(\lambda) \rangle_\beta = 0$ exactly.  The chirality
  factor is therefore $a_K = 1 + 0 \cdot 0 \cdot h + O(h^2) = 1 + O(h^2)$,
  matching the empirical pattern $(1+h)(1-h) = 1 - h^2$ observed for
  $D, T, {}^3\mathrm{He}, {}^4\mathrm{He}$.  Numerical confirmation
  for the figure-eight braid representative at $q_0$ is recorded in
  `chirality-avg-content.witness.json`:
  $\langle c(\lambda) \rangle_{4_1} = -2.3 \times 10^{-15}$
  (numerically zero at 50-dps precision).

- **Chiral case (closed-form formula identified, 2026-05-09).** For
  chiral 3-braids, $\langle c(\lambda) \rangle_\beta$ has a closed
  form in terms of the Hecke characters at $q_0$ alone:
  $$
    \langle c(\lambda) \rangle_\beta
    \;=\;
    \frac{3 \bigl(\chi^{(3)}(\beta) - \chi^{(1,1,1)}(\beta)\bigr)}{
      \chi^{(3)}(\beta)
      \;+\; \chi^{(1,1,1)}(\beta)
      \;+\; (w_{(2,1)} / w_{(3)}) \cdot \chi^{(2,1)}(\beta)
    },
  $$
  where the Plancherel-weight ratio at $q_0 \approx 1.10998$ is
  $w_{(2,1)} / w_{(3)} \approx 4.454$ (and $w_{(3)} = w_{(1,1,1)}$
  by transposition symmetry).  The reduction follows from
  $c(\lambda) \in \{+3, 0, -3\}$ for $\lambda \in \{(3), (2,1),
  (1,1,1)\}$: the $(2,1)$ contribution drops from the numerator
  ($c = 0$), and the symmetric/antisymmetric terms with
  $c = \pm 3$ pair into $3(\chi^{(3)} - \chi^{(1,1,1)})$.  At $q_0$
  this formula reproduces the witness data
  ([`chirality-avg-content-chiral.witness.json`](../../../folio-assistant/computations/chirality-avg-content-chiral.witness.json))
  to machine precision:

  | Braid                          | $w$ | predicted $\langle c \rangle_\beta$ |
  |--------------------------------|------|-------------------------------------|
  | $\sigma_1^3$                   | $+3$ | $+1.81492$ |
  | $\sigma_1^{-3}$                | $-3$ | $-1.81492$ |
  | $(\sigma_1 \sigma_2)^3$        | $+6$ | $+0.35428$ |
  | $\sigma_1^2 \sigma_2^{-1} \sigma_1^2 \sigma_2^{-1}$ | $+4$ | $+0.10724$ |

  The earlier conjectured universal value $\langle c \rangle = 1$
  was falsified for the deuteron $^2$H (see falsification table at
  `chirality-writhe-ribbon-derivation.md:122–126`); the closed
  form above replaces it.

  **Generalisation to $H_n(q_0)$, verified for D, T, $^3$He**
  (commit pending):

  $$
    \langle c(\lambda) \rangle_\beta
    \;=\;
    \frac{
      \sum_{\substack{[\lambda] \neq [\lambda^T] \\ [\lambda] < [\lambda^T]}}
        c(\lambda) \bigl(\chi^\lambda(\beta) - \chi^{\lambda^T}(\beta)\bigr) w_\lambda
    }{
      \sum_\lambda \chi^\lambda(\beta) w_\lambda
    },
  $$

  using $c(\lambda^T) = -c(\lambda)$ and $w_\lambda = w_{\lambda^T}$
  (hook-length symmetry).  Self-conjugate $\lambda = \lambda^T$
  contribute $0$ to the numerator since $c(\lambda) = 0$ for
  self-conjugate partitions of $n$.  The witness
  [`chirality-avg-content-atomic.witness.json`](../../../folio-assistant/computations/chirality-avg-content-atomic.witness.json)
  records the audited atomic values:

  | Atom | $H_n$ | writhe | $\langle c \rangle_\beta$ | $a_K$ (1st-order) |
  |------|-------|--------|---------------------------|-------------------|
  | $D$ ($^2$H) | $H_6$ | $+2$ | $+0.428$ | $+1.179$ |
  | $T$ ($^3$H) | $H_9$ | $+3$ | $-8.857$ | $-4.555$ |
  | $^3\mathrm{He}$ | $H_9$ | $+3$ | $+10.000$ | $+7.272$ |

  Direct-sum and per-pair-symmetric forms agree to $10^{-40}$ for
  all three atoms, confirming the partition-lattice cancellation
  pattern generalises.  $^3\mathrm{He}$'s $\langle c \rangle = 10.000$
  to f64 precision is suggestive of an exact integer structural
  value.

  **Both interpretations (i) and (ii) refuted (2026-05-09).**  The
  same witness records the **exact ribbon-twist formula**

  $$
    a_K^{\mathrm{exact}}
    \;=\;
    \frac{\sum_\lambda w_\lambda \cdot q_0^{2 w c(\lambda)} \cdot \chi^\lambda(T_w)}{\sum_\lambda w_\lambda \cdot \chi^\lambda(T_w)},
  $$

  evaluated at the audited atomic braids:

  | Atom | $a_K^{(1)}$ first-order | $a_K^{\mathrm{exact}}$ | $(1+h)(1-h)$ |
  |------|-------------------------|------------------------|---------------|
  | $D$  | $+1.18$ | $-3.82$    | $+0.956$ |
  | $T$  | $-4.56$ | $+15{,}589$ | $+0.956$ |
  | $^3\mathrm{He}$ | $+7.27$ | $-20{,}796$ | $+0.956$ |

  The exact form is *more* divergent, not less — at $H_9$ the
  factors $q_0^{2 w c(\lambda)}$ with $|c(\lambda)| \leq 36$ (for
  $\lambda = (9), (1^9)$) reach $q_0^{216} \approx 10^9$, blowing
  up the numerator.

  Therefore **neither (i) "$O(h^2)$ corrections fix it" nor (ii)
  "use exact exponential, not linearisation" recovers the empirical
  $(1+h)(1-h)$ pattern.**  The conjecture's stated formula —
  $a_K$ as a ribbon-twist-weighted Markov-trace ratio — does **not**
  apply at the audited atomic braids.

  Either the empirical $(1+h)(1-h) \approx 0.956$ pattern reflects
  a *different* underlying construction of the atomic chirality
  factor (e.g. a per-quark chirality contribution that nearly
  cancels at the atomic level, leaving a $1 - O(h^2)$ residual that
  is *not* the ribbon-twist Markov ratio above), or the empirical
  pattern itself is incidental to the mass derivation at $A \geq 2$.

  **Residual** (now a structural rather than computational gap):
  identify the construction that produces $a_K^{D, T, {}^3\mathrm{He}}
  \approx 0.956$ from the substrate data, given that the
  ribbon-twist Markov-ratio is conclusively wrong.  The closed-form
  $\langle c \rangle_\beta$ values committed here remain a valid
  invariant of the braid representative even if they no longer feed
  into the chirality factor in the form the conjecture stated.

## Proof obligations

1. **Ribbon-twist eigenvalue.**  Verify that
   $\theta_\lambda = q^{c(\lambda)}$ in the Hecke-algebra ribbon
   structure used in the QOU model (not the quantum-group normalization,
   which may differ by a global phase).

2. **Mean-content identity (amphichiral).**  *Discharged 2026-05-09
   for the figure-eight $4_1$ via direct $H_3(R, q_0)$ computation*
   (`chirality-avg-content.witness.json`).  Generalisation to all
   amphichiral knots follows from the bar-involution symmetry
   $\chi^\lambda = \chi^{\lambda^T}$, which is structural in
   $H_n(q)$.

3. **Mean-content identity (chiral, partially discharged 2026-05-09).**
   For chiral 3-braids the closed form
   $\langle c(\lambda) \rangle_\beta
   = 3(\chi^{(3)} - \chi^{(1,1,1)})
   / (\chi^{(3)} + \chi^{(1,1,1)} + (w_{(2,1)}/w_{(3)}) \chi^{(2,1)})$
   reproduces the witnessed values at $H_3(q_0)$ to machine
   precision (see "Chiral case" derivation above).  **Open piece:**
   generalise to $H_n(q)$ for $n > 3$ — for $5_2$ neutron, $6_2$
   deuteron, $8_{11}$ tritium, $L_{6a4}$ ${}^3\mathrm{He}$ etc.
   The pattern presumably involves a sum over transposition pairs
   $(\lambda, \lambda^T)$ with $c(\lambda^T) = -c(\lambda)$ and a
   denominator absorbing the self-conjugate $\lambda = \lambda^T$
   contributions.

4. **$O(h^2)$ bound.**  Estimate the second-order correction
   $O(h^2)$ at $q = q_0$ and show it is $< 0.75\%$ of the leading
   term (matching the overall mass-formula accuracy).

5. **Exact formula.**  For at least one chiral knot (trefoil $3_1$ as
   the proton model), evaluate the exact formula and compare with the
   first-order result.

## Relationship to GAP-A-2

This conjecture directly addresses GAP-A-2 of the
[derivation audit report](#prose:derivation-audit-report).

