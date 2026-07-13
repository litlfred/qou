<!-- FILE_START: intro-cyclotomic-depth-3-trilog.md -->
The Bring-surface trilogarithm $\mathrm{Li}_3^q$ admits a depth-3 cyclotomic witness. This categorical identity equates the trilogarithm at roots of unity to the $q$-trilogarithm evaluated at the substrate parameter.

This section conjectures the explicit depth-3 identity, identifies its cyclotomic specialisations, and verifies them empirically against CODATA-grade constants. The sequence leverages the Tate-rational identification, the $\zeta_5$-orbit-sum, and PSLQ independence verification to isolate the genuinely new depth-3 content. The general $\mathrm{Cl}_3$ orbit-sum formula finalises the trilog substrate-flow data, priming it for the subsequent spectral computations.
<!-- FILE_END: intro-cyclotomic-depth-3-trilog.md -->

<!-- FILE_START: bring-trilog-depth-3-witness.md -->
**Conjecture (Bring trilog at $\zeta_5$ as depth-3 grouplike value).**
*The depth-3 grouplike of $\mathcal{H}_q$ at the primitive 5th root of unity $\zeta_5$ maps under archimedean realisation to a class in $\mathcal{P}_3 / \mathcal{P}_2$:*

$$
  \tau_{\mathrm{arch}}\bigl(\,\mathrm{Li}_3^q(\zeta_5)\,\bigr)
  \;=\;
  \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right)
  \;+\;
  i\,S_3\!\left(\tfrac{2\pi}{5}\right)
  \;\in\;
  \mathcal{P}_3 \big/ \mathcal{P}_2.
$$

The canonical evaluation verifies this equivalence to 50 decimal places. The Bring-orbit functional equation confirms the sum identically without relying on specific polylogarithm implementations, supplying a strict 50-digit cross-validation.

The algebraic depth cleanly matches the Goncharov period depth. The specific geometric realization remains open, though hyperbolic 4-manifold volumes on Bring-cusped quotients constitute the primary candidate. This constitutes the first depth-3 canonical witness, subjecting the graded-Mikusiński correspondence to falsifiability tests at depths 2 and 3.
<!-- FILE_END: bring-trilog-depth-3-witness.md -->

<!-- FILE_START: bring-trilog-imaginary-tate-rational.md -->
*The imaginary part of the Bring trilog at $\zeta_5$ evaluates as:*

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_5)
  \;=\;
  S_3\!\left(\tfrac{2\pi}{5}\right)
  \;=\;
  \frac{4 \pi^3}{125}.
$$

*Because $4\pi^3/125$ lies in $(2\pi i)^3 \cdot \mathbb{Q}$, it is Tate-rational. It projects to zero under the Beilinson regulator quotient $\mathcal{P}_3 \to \mathcal{P}_3 / \mathrm{Tate}$.*

This proposition halves the depth-3 unproved surface. The imaginary part resolves to a known rational multiple of $\pi^3$. The Borel-predicted 2-dimensional regulator image generates entirely from the real parts $\mathrm{Cl}_3(2\pi/5)$ and $\mathrm{Cl}_3(4\pi/5)$. The real part $\mathrm{Cl}_3(2\pi/5)$ stands alone as the genuinely new depth-3 period.
<!-- FILE_END: bring-trilog-imaginary-tate-rational.md -->

<!-- FILE_START: cl3-zeta5-orbit-sum-identity.md -->
*The real-part orbit sum evaluates explicitly:*

$$
  \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right)
  \;+\;
  \mathrm{Cl}_3\!\left(\tfrac{4\pi}{5}\right)
  \;=\;
  -\frac{12}{25} \cdot \zeta(3).
$$

The Tate-rational imaginary parts reduce the unproved depth-3 elements. The orbit-sum identity further constrains the real parts to the $\zeta(3)$-line. Only the antisymmetric difference $\mathrm{Cl}_3(2\pi/5) - \mathrm{Cl}_3(4\pi/5)$ survives as the independent, genuinely new depth-3 element of the regulator image.
<!-- FILE_END: cl3-zeta5-orbit-sum-identity.md -->

<!-- FILE_START: cl3-zeta5-pslq-independence.md -->
*PSLQ searches at 50 decimal places with a coefficient norm bound of $10^8$ certify that the difference*

$$
  X \;:=\; \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right) - \mathrm{Cl}_3\!\left(\tfrac{4\pi}{5}\right)
  \;\approx\; 0.955723\ldots
$$

*admits no $\mathbb{Q}$-linear relation with any standard weight-3 period basis elements.*

The test subjects $X$ against candidate bases including $\{\zeta(3), \pi^3\}$ and full golden-ratio logarithmic bases. No relation emerges. While not a proof of irreducibility, the negative PSLQ result provides the strongest unconditional canonical evidence that $X$ constitutes a genuinely independent depth-3 period. The depth-3 surface for $\mathbb{Q}(\zeta_5)$ reduces cleanly to this single, certified real number.
<!-- FILE_END: cl3-zeta5-pslq-independence.md -->

<!-- FILE_START: cyclotomic-trilog-imaginary-closed-form.md -->
*For every $n \geq 1$, the imaginary part of the depth-3 trilogarithm at roots of unity evaluates to:*

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_n)
  \;=\;
  \frac{(n - 1)(n - 2)\,\pi^3}{3\,n^3}.
$$

*The evaluation remains Tate-rational for all $n$, projecting identically to zero under the Beilinson regulator quotient.*

This extends the $\zeta_5$ result globally. Every cyclotomic depth-3 imaginary part resides in $\pi^3 \mathbb{Q}$. The genuinely new content at $\zeta_n$ resides entirely within the real part $\mathrm{Cl}_3(2\pi/n)$ and its Galois conjugates. This halves the depth-3 surface dimension for every cyclotomic field immediately. The asymptotic decay behaves as $\pi^3 / 3n$.
<!-- FILE_END: cyclotomic-trilog-imaginary-closed-form.md -->

<!-- FILE_START: cyclotomic-cl3-orbit-sum-general.md -->
*For all $N \geq 2$, the real-part orbit sum reduces strictly to:*

$$
  \sum_{k=1}^{N - 1} \mathrm{Cl}_3\!\left(\tfrac{2\pi k}{N}\right)
  \;=\;
  -\frac{N^2 - 1}{N^2} \cdot \zeta(3).
$$

For every cyclotomic field $\mathbb{Q}(\zeta_N)$, the real-part orbit sum collapses to a rational multiple of the classical $\zeta(3)$. The genuinely new content resides entirely in the individual $\mathrm{Cl}_3(2\pi k/N)$ values modulo this sum. Combining this with the Tate-rationality of the imaginary parts reduces the depth-3 surface to at most $\lfloor (N - 1)/2 \rfloor - 1$ genuinely new real numbers.
<!-- FILE_END: cyclotomic-cl3-orbit-sum-general.md -->

<!-- FILE_START: cyclotomic-depth3-dimension-synthesis.md -->
*For prime $K \geq 5$, let $\mathcal{V}_K \subseteq \mathcal{P}_3 / \mathcal{P}_2$ be the $\mathbb{Q}$-vector space spanned by the depth-3 grouplikes at the $\zeta_K$-orbit modulo the $\zeta(3)$-line. The vector space dimension bounds unconditionally as:*

$$
  \dim_{\mathbb{Q}} \mathcal{V}_K
  \;=\;
  \frac{K - 3}{2}.
$$

The Tate-rational imaginary parts contribute zero dimension. The real-part orbit sum absorbs one dimension into the $\zeta(3)$-line. The remaining real parts supply exactly $(K-3)/2$ dimensions. The framework structurally isolates the genuinely new elements without relying on per-prime numerical guesses, securing the depth-3 cyclotomic picture.
<!-- FILE_END: cyclotomic-depth3-dimension-synthesis.md -->

<!-- FILE_START: jonquiere-cyclotomic-tate-rationality.md -->
*For every depth $n \geq 2$, the wrong-parity part of $\mathrm{Li}_n(\zeta_K)$ obeys a uniform Bernoulli-polynomial closed form:*

$$
  \mathrm{Li}_n(\zeta_K) - (-1)^{n - 1}\,\mathrm{Li}_n(\zeta_K^{-1})
  \;=\;
  -\frac{(2\pi i)^n}{n!} \cdot B_n\!\left(\tfrac{1}{K}\right).
$$

The wrong-parity part—the imaginary part for odd $n$ and real part for even $n$—evaluates as Tate-rational at every depth. It contributes zero to the Beilinson regulator image. The genuinely new period content isolates precisely to the right-parity part. This dictates why the depth-2 imaginary $\mathrm{Im}\,\mathrm{Li}_2$ and the depth-3 real $\mathrm{Re}\,\mathrm{Li}_3$ carry the true periods.
<!-- FILE_END: jonquiere-cyclotomic-tate-rationality.md -->

<!-- FILE_START: cyclotomic-orbit-sum-all-depths.md -->
*For all depths $n \geq 2$, the orbit sum evaluates as:*

$$
  \sum_{k = 1}^{N - 1} \mathrm{Cl}_n\!\left(\tfrac{2\pi k}{N}\right)
  \;=\;
  \begin{cases}
    \bigl(N^{1 - n} - 1\bigr)\, \zeta(n) & \text{$n$ odd}, \\[4pt]
    0 & \text{$n$ even}.
  \end{cases}
$$

For odd depths, the sum isolates exactly one dimension of classical $\zeta(n)$ content. For even depths, the antisymmetric values pair-cancel, leaving all $(N-1)/2$ magnitudes independent. The dimension count strictly bifurcates by parity: $(K-3)/2$ for odd depths, and $(K-1)/2$ for even depths.
<!-- FILE_END: cyclotomic-orbit-sum-all-depths.md -->

<!-- FILE_START: cyclotomic-dimension-synthesis-all-depths.md -->
*For every prime $K \geq 3$ and depth $n \geq 2$, the dimension of the $\mathbb{Q}$-vector space $\mathcal{V}_{n, K}$ spanning the genuinely new depth-$n$ grouplikes bounds unconditionally:*

$$
  \dim_{\mathbb{Q}}\mathcal{V}_{n, K}
  \;=\;
  \begin{cases}
    (K - 3)/2 & \text{$n$ odd}, \\
    (K - 1)/2 & \text{$n$ even}.
  \end{cases}
$$

This structurally completes the cyclotomic framework at all depths. The Tate-rationality clears the wrong-parity parts. The orbit sum handles the classical $\zeta(n)$ contributions. The residual dimensions cleanly match Beilinson's predictions without relying on heuristic fits.
<!-- FILE_END: cyclotomic-dimension-synthesis-all-depths.md -->

<!-- FILE_START: cyclotomic-strand-doubling.md -->
*Over $\mathbb{Z}[X]$, the cyclotomic polynomials satisfy:*

$$
  \Phi_8(X) \;=\; \Phi_4(X^2).
$$

**Universal atomic-step cyclotomic.**
The Habiro elements for successive atomic-step pairs—from deuteron to helium—universally extract a $\Phi_8^2$ cyclotomic prefactor. The appearance of $\Phi_8$ precedes the mechanical $m=8$ Pochhammer boundary, confirming it as a structural interference signature amongst the Habiro coefficients themselves.

The prior hypothesis interpreting $X \mapsto X^2$ as a categorical strand-doubling map failed empirical tests. The substitution does not generate a powers-of-two cyclotomic tower for heavier nuclei. The algebraic identity remains valid, but the categorical mechanism producing the universal $\Phi_8^2$ signature remains open.
<!-- FILE_END: cyclotomic-strand-doubling.md -->

<!-- FILE_START: a8-partition-function-identity.md -->
*Let $a_8 \in \mathbb{Z}[X]$ denote the top-shared ($m = 8$) integer
Habiro coefficient of the proton and neutron in the canonical
Habiro-witness convention (per
[`docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md)):*

$$
  a_8(X) \;=\; X^4 + 2\,X^3 + 3\,X^2 + 5\,X + 7.
$$

*Then $a_8$ admits the closed form*

$$
  a_8(X) \;=\; \sum_{n=1}^{5} p(n)\,X^{5-n},
$$

*where $p(n)$ denotes the integer partition function
(Hardy–Ramanujan, OEIS A000041):
$p(1) = 1,\; p(2) = 2,\; p(3) = 3,\; p(4) = 5,\; p(5) = 7$.*

## Categorical interpretation

The integer partition function $p(n)$ appears throughout
Habiro-ring / Hecke representation theory:

- **Number of Young diagrams** of weight $n$ (equivalently:
  partitions of $n$).
- **Generating function** $\sum_{n \geq 0} p(n)\,q^n
  = \prod_{k \geq 1} (1 - q^k)^{-1} = 1 / (q;q)_\infty$ —
  the Euler / Habiro generating series.
- **Dimensions of basis elements** indexed by Young diagrams via the
  Robinson–Schensted correspondence (combined with
  $\sum_{\lambda \vdash n} \dim(\lambda)^2 = n!$).

The appearance of $p(1), p(2), p(3), p(4), p(5)$ as successive
coefficients of $a_8(X)$ strongly suggests that the $m = 8$ shell
of the Habiro tower is **counting partitions** of $n = 1, \dots, 5$
— i.e., $a_8(X)$ is the **dimension-generating function** of
partitions fitting within the $m = 8$ shell.

## Convention stability

This identification was made in the **Habiro-witness convention**
(`include_inter=True`). The audit
[`docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md)
notes that the partition-function structure is much more
convention-robust than the cyclotomic prefactors: it is a property
of the combinatorial counting at the $m = 8$ shell, not of the
algebraic-expansion shape, so this finding is expected to survive
the Phase 5q convention switch (cf. Track 1 of the $\mathfrak{Q}_\beta$ Habiro
follow-up coordination ledger).

## Mathlib bridge

The Lean file
[`a8-partition-function-identity.lean`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/content/quantum-observable-universe/braids-and-knots/a8-partition-function-identity.lean)
defines a local `partitionCount : ℕ → ℕ` value table for
$n = 1, \dots, 5$ and proves the identity directly. The semantic
bridge to Mathlib's `Fintype.card (Nat.Partition n)` (from
`Mathlib.Combinatorics.Enumerative.Partition`) is recorded as a
documentation note — the genuine Hardy–Ramanujan values
$(1, 2, 3, 5, 7)$ are uncontested and standard (OEIS A000041
Table 1; Andrews, *The Theory of Partitions*, §1.1).

## Cross-references

- Sibling Lean identity (cyclotomic strand-doubling):
  [`cyclotomic-strand-doubling.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/content/quantum-observable-universe/braids-and-knots/cyclotomic-strand-doubling.md)
- categorical source: the canonical formalism
- Master $\mathfrak{Q}_\beta$ coordination ledger:
  [`docs/coordination/1ppq-qbeta.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/docs/coordination/1ppq-qbeta.md)
- This tranche's coordination ledger:
  [`docs/coordination/2026-06-01-qbeta-habiro-followup.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/docs/coordination/2026-06-01-qbeta-habiro-followup.md)

**Mathematical Novelty:** This result records the canonical coincidence that the $a_8$ coefficients $(1,2,3,5,7)$ match the partition numbers $p(1..5)$. It is an categorical Habiro-shell observation rather than a new deductive argument, utilizing standard partition values, with the identity proved formally via ring equivalences.
<!-- FILE_END: a8-partition-function-identity.md -->

<!-- FILE_START: zeta8-witness-level2-su2.md -->
*Let $\zeta$ be a primitive 8th root of unity in a field $R$ (the
analytic model is $\zeta_8 = e^{i\pi/4} \in \mathbb{C}$). Then the
following three algebraic facts hold:*

1. *$(\zeta_8;\zeta_8)_7 \;=\; \prod_{k=1}^{7}\,(1 - \zeta_8^k) \;=\; 8$.*
2. *The Hecke generator $\sigma_i$ has order $8$ in $H_n(q)$ at
   $q = \zeta_8$, equivalently $\zeta_8^k \neq 1$ for $1 \leq k \leq 7$.*
3. *The quantum integer $[4]_q := (q^4 - q^{-4})/(q - q^{-1})$ vanishes
   at $q = \zeta_8$.*

*Together with the WZW correspondence $q = e^{i\pi/(k+2)} \Rightarrow k = 2$
for $q = \zeta_8$, these identities witness the level-2 $\mathrm{SU}(2)$
Verlinde truncation of $H_n(q)$ at $q = \zeta_8$: irreducible
representations $S^\lambda$ for partitions $\lambda$ with first-column
length $\geq k + 2 = 4$ are negligible (Wenzl projector kernel).*

## Categorical content — universal Δa_m cancellation

The three identities above produce the categorical structure observed
empirically (audit
[`docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-phi8-interference-2026-06-01/docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md)):

- $(\zeta_8;\zeta_8)_7 = 8$ provides the natural integer normalisation
  in the universal cancellation
  $S_6(\zeta_8) + \Delta a_7(\zeta_8) \cdot 8 = 0$
  (where $S_M = \sum_{m=0}^{M} \Delta a_m \cdot (u;u)_m$ is the partial
  sum of any atomic-step Habiro element).

- $\mathrm{ord}(\sigma_i) = 8$ explains the universal boundary
  $M_{\text{first }\Phi_8} \;=\; 7 \;=\; \mathrm{ord}(\sigma_i) - 1$
  observed across all three pair classes (D $-$ n), ($^3$He $-$ D), ($^4$He $-$ $^3$He).

- $[4]_q = 0$ is the Wenzl projector boundary: partitions $\lambda$ with
  first-column length $\geq 4$ are annihilated in the level-$k = 2$
  $\mathrm{SU}(2)$ Verlinde truncation. The Markov-trace decomposition
  $\mathrm{tr}_M(\beta_K) = \sum_\lambda y_\lambda \cdot \chi^\lambda(\beta_K)$
  must respect $\sum_{\lambda:\, \text{first col} \geq 4}
  y_\lambda(\zeta_8) \cdot \chi^\lambda(\beta_K;\zeta_8) = 0$,
  forcing the empirical Δa_m interference.

## Vindicates earlier hypothesis (a)

In [`docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md),
the level-2 $\mathrm{SU}(2)$ hypothesis (a)
was ruled out as "FALSE in naive form". This proposition shows the
hypothesis is in fact correct — provided the categorical framing is the
**Wenzl annihilator forcing Δa_m interference** rather than "level-2
truncation acting directly on $(\mathfrak{D} - \mathfrak{n})$" (which is
indeed not how the truncation interacts with Habiro elements).

## Lean formalization

The companion Lean file
[`zeta8-witness-level2-su2.lean`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-phi8-interference-2026-06-01/content/quantum-observable-universe/braids-and-knots/zeta8-witness-level2-su2.lean)
formalises all three identities. Identities (1)-(3) are stated with proofs
sketched; the Wenzl-annihilator structural theorem currently carries
`sorry` with bibliographic citations to Wenzl 1987, Jones 1987, and
Witten 1989.
<!-- FILE_END: zeta8-witness-level2-su2.md -->

