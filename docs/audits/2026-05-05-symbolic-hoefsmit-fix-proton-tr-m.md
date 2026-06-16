# Symbolic Hoefsmit + canonical Jones–Markov weights → closed-form proton/neutron/deuteron tr_M

**Branch.** `claude/hoefsmit-2x2-fix`
**Module.** [`computations/hoefsmit_symbolic.py`](../../computations/hoefsmit_symbolic.py)
**Continues.** [PR #544](https://github.com/litlfred/qou/pull/544) open item:
"closed-form leading coefficient for higher atoms requires symbolic
2×2 Hoefsmit fix" — now closed for $A = 1$ (proton + neutron).

## What was wrong (round-1 of PR #544)

`ocneanu_cancellation_derivation.py` used the formulas
$1/[d]_q$ and $\sqrt{[d]^2 - 1}/[d]$ for the 2×2 block, which
**do not** match the existing numerical Hoefsmit construction in
`hecke_characters.build_seminormal_matrices`. Cross-validation:
$\chi^{(2,1)}(\text{proton})$ symbolic = 2.515 vs numerical = 1.808.

## Correct Hoefsmit formulas

For SYT $i$ with $k$-th and $(k+1)$-th entries at cells with axial
contents differing by $\rho$:

- **1×1 block** (no swap partner): $\sigma_k$ acts as
  $a = h / (1 - q^{-2\rho})$ on SYT $i$
  ($= q$ for $\rho = +1$, $= -q^{-1}$ for $\rho = -1$)
- **2×2 block** on $\{i, j\}$ ($j$ = swap partner):
  - $M[i, i] = a = h / (1 - q^{-2\rho})$
  - $M[j, j] = a' = h / (1 - q^{2\rho})$
  - $M[i, j] = M[j, i] = b$ where $b^2 = a \cdot a' + 1$ (from
    $\det = -1$)

These match the existing numerical implementation exactly. With
this fix, symbolic $\chi^{(2,1)}(\text{proton})$ at $q_0$ matches
numerical to 6+ decimal places.

## Closed-form characters for proton standalone

Cross-validated at $q_0$: all three irreps $\lambda \in \{(3), (2,1),
(1,1,1)\}$ match `build_seminormal_matrices` within $10^{-6}$.

> **Important (round-3 supersession).** The closed-form
> $\mathrm{tr}_M$ values shown in the next two sections (proton
> $\boxed{\frac{q^{20} + q^{18} + 3q^{12} - 3q^{8} - q^{2} - 1}{8q^{10}}}$
> with leading $-\frac{1}{8}$, and the analogous neutron form) are
> for the **partition-sum normalisation**
> $\mathrm{tr}_M^{\text{partition-sum}}(\beta) =
>  \sum_\lambda \frac{\dim_q(\lambda)^2}{[n]_q!\,f^\lambda} \chi^\lambda(\beta)$,
> which is **NOT** the canonical Ocneanu/Wenzl Markov trace. They
> agree only at $q = 1$. The canonical $\mathrm{tr}_M$ closed forms
> (using Jones-Markov weights $y_\lambda(q)$) are derived in the
> §Round-3 section below and yield $\mathrm{tr}_M(\text{proton}) =
>  1.06530622859239\ldots$ at $q_0$ — matching the canonical
> bridge to 14 decimal places. **Use the round-3 forms for any
> downstream six-term mass formula computation.** The round-2
> partition-sum forms remain accurate as a derived quantity but
> should not be confused with the canonical Markov trace.

**Note (PR #546 round-2 update).**  The earlier draft of this module
duplicated the seminormal construction.  Per Copilot's review, the
duplicate has been removed and the matrix builder + braid-character
function now delegate to `hecke_character_symbolic.{hoefsmit_matrices_symbolic,
q_character_on_braid_word}`.  This guarantees a single source of truth
for the seminormal matrices and the matrix-multiplication order.  An
earlier `f^\lambda` bug (using `len(...)` of the 3-tuple returned by
`standard_young_tableaux` instead of the SYT list itself) was also
fixed; closed-form constants below reflect the corrected denominator
**under the partition-sum convention** (not the canonical Markov
trace — see the round-3 supersession note above).

## Closed-form Markov trace for proton standalone

Using $\mathrm{tr}_M(\beta) = \sum_\lambda w_\lambda \cdot \chi^\lambda(\beta) / f^\lambda$
with $w_\lambda = \dim_q(\lambda)^2 / [n]_q!$ and $f^\lambda = \#\mathrm{SYT}(\lambda)$:

$$
\boxed{\;\;
\mathrm{tr}_M(\text{proton})
\;=\;
\frac{q^{20} + q^{18} + 3 q^{12} - 3 q^{8} - q^{2} - 1}{8 \cdot q^{10}}
\;\;}
$$

**Pole order at $q = 0$ : exactly 10** (matching `dp_pole_probe`'s
empirical value).
**Leading coefficient : $-\dfrac{1}{8}$ EXACTLY**.

## Closed-form Markov trace for neutron standalone

$$
\mathrm{tr}_M(\text{neutron})
\;=\;
\frac{q^{20} + 2 q^{18} + 2 q^{16} + q^{14} + 3 q^{12} - 3 q^{8} - q^{6} - 2 q^{4} - 2 q^{2} - 1}{8 \cdot q^{8} \cdot (q^4 + q^2 + 1)}
$$

**Pole order = 8 EXACTLY**, leading coefficient $= -\dfrac{1}{8}$.

## Universal leading coefficient $-1/8$

Both proton and neutron standalone have leading coefficient at
$q=0$ EQUAL TO $-\dfrac{1}{8}$. This is a **universal structural
identity** across nucleon types — the same Wedderburn-weight
denominator emerges from the $\dim_q(\lambda)^2 / [3]_q!$ partition
sum at $q \to 0$.

Empirical pattern from $A = 1$:
- proton ($n=3$): leading = $-1/8$
- neutron ($n=3$): leading = $-1/8$

We conjecture (open) that this universality extends to all
$A \geq 2$ atoms:

> **Conjecture.** For every atom in canonical pppnnn ordering, the
> leading coefficient of $\mathrm{tr}_M$ at $q = 0$ is the same
> rational constant determined by the partition-sum normalization
> $\sum_\lambda \dim_q(\lambda)^2 / [n]_q!$ evaluated at $q \to 0$.

For $A = 1$ this constant is $-1/8$. Verifying the universality
for $A \geq 2$ is the natural extension once the $n = 6, 9, 12$
symbolic computations become tractable.

## Use case: m_p calculation?

**Comparison with canonical pipeline.** The closed form
$\mathrm{tr}_M(\text{proton}) \approx 0.702$ at $q_0$ refers to the
**internal** 3-strand braid of the proton (the "atomic" braid from
`atomic_braid_to_crossings(1, 0, include_inter=False)`). The
canonical mass pipeline,
`hecke_characters.compute_mass_at_level(Z, N, k=3A)`, short-circuits
for $A \le 1$ — `nuclear_braid_character` returns
`float(dim)` whenever $A \le 1$ — so it does **not** compute the
internal-braid character for a single nucleon. Its trivial output
$1.0$ at $A=1$ is the empty inter-nucleon braid, not a comparable
quantity.

In other words: the closed forms above are the **only** symbolic
expressions for the internal proton/neutron Markov traces in the
codebase. There is no separate canonical reference value to
normalize against; the per-irrep characters cross-validate against
`build_seminormal_matrices` to $10^{-6}$, and the partition sum uses
the same Wedderburn weight formula
$w_\lambda = \dim_q(\lambda)^2 / [n]_q!$ as
`compute_mass_at_level`'s loop body (verified by direct inspection).

For an **$A \geq 2$** atom, the inter-nucleon crossings dominate
the braid and `compute_mass_at_level` produces a non-trivial
Markov trace; the natural extension of this work is to derive
closed forms there ($n = 6, 9, 12$) once the symbolic pipeline is
made tractable.

**Where m_e enters:** the Wedderburn-Markov mass formula uses
$E_0 = Q_{\text{neutron}} = 0.7823$ MeV as the dimensional bridge,
not $m_e$ directly. $m_e$ enters elsewhere via the trefoil
$T_{2,3}$ (electron knot) Markov trace. The symbolic
$\mathrm{tr}_M(\text{proton})$ I derived is **dimensionless**;
multiplying by $E_0$ gives binding energies in MeV, but mass itself
needs the full Wedderburn structure that
`compute_mass_at_level` already encodes.

## Round-3 update — closed-form Jones–Markov weights $y_\lambda(q)$

The remaining $0.702$ vs $1.065$ "phantom" gap (round-2) was actually
real after all — but on a **different formula**. The
partition-sum normalisation $w_\lambda / f^\lambda
= \dim_q(\lambda)^2 / ([n]_q!\, f^\lambda)$ used in round-1/2 is
**not** the canonical Ocneanu–Wenzl Markov weight $y_\lambda(q)$;
the two coincide only at the classical Plancherel point $q = 1$.

### Derivation: $y_\lambda$ from Markov axioms (n = 3)

The Ocneanu Markov trace is the unique linear functional satisfying
$\mathrm{tr}_M(1) = 1$, $\mathrm{tr}_M(x\sigma_n) = z\cdot\mathrm{tr}_M(x)$
(Markov property) and $\mathrm{tr}_M(xy) = \mathrm{tr}_M(yx)$, with
$z = 1/(\sqrt{q} + 1/\sqrt{q})$. Its Wedderburn decomposition is
$\mathrm{tr}_M = \sum_\lambda y_\lambda(q) \cdot \chi^\lambda$.
At $H_3$ the system is $3\times 3$ and admits a closed-form solve
on the ladder basis $\{1, \sigma_1, \sigma_1\sigma_2\}$. The
solution reproduces the bridge witness $y_\lambda$ values to 10
digits and yields
$$
\mathrm{tr}_M(\text{proton}) \stackrel{q_0}{=} 1.0653062285923887\ldots
$$
matching `markov_peel`'s reference $1.0653062285923893$ to 14
decimal places (remaining drift is the float precision of $q_0$).

### Closed form for general $n$ via Schur principal specialization

For $n \ge 4$ the ladder system is rank-deficient. The Wenzl
closed form is
$$
y_\lambda(q) = \frac{1}{Z}\, s_\lambda(1, Q, Q^2, \ldots, Q^{r-1}),
\qquad Q = q^2,\quad Q^r = \frac{z_W}{1 - Q + z_W},\quad z_W = q\,z,
$$
with $s_\lambda$ the Schur polynomial principal specialization
$Q^{n(\lambda)} \prod_{x\in\lambda}(1 - Q^{r+c(x)})/(1 - Q^{h(x)})$
and normalisation $Z = \sum_\mu f^\mu \cdot s_\mu$ to enforce
$\mathrm{tr}_M(1) = 1$. At $n = 3$ the Schur and ladder formulas
agree exactly. At $n = 6$ the closed form gives the canonical
deuteron weights.

### Code

[`computations/markov/markov_weights_symbolic.py`](../../computations/markov/markov_weights_symbolic.py)
implements both paths (`solve_y_lambda` for $n \le 3$ via the
linear system; `y_lambda_symbolic` for any $n$ via Schur principal
specialisation). Witness:
[`markov_weights_symbolic.witness.json`](../../computations/markov/markov_weights_symbolic.witness.json).

The earlier closed forms in §"Closed-form Markov trace for proton
standalone" (and the deuteron $-1/8 / +1/128$ leading-coefficient
analysis) are **valid for the partition-sum normalisation
$w_\lambda/f^\lambda$**, but that quantity is *not* the canonical
$\mathrm{tr}_M$ — it differs from the Ocneanu Markov trace by a
$q$-rational factor that can be tracked symbolically through the
Schur formula. The canonical $\mathrm{tr}_M$ closed forms (from
$y_\lambda(q)$) supersede the earlier ones for any use that feeds
into the six-term mass formula.

## Status

- **Closed for $A = 1$**: symbolic Hoefsmit construction now
  delegates to the canonical engine in `hecke_character_symbolic`;
  closed-form $\mathrm{tr}_M$ for proton + neutron derived in $R$,
  pole orders ($10$ and $8$) confirmed against `dp_pole_probe`,
  leading coefficient $-1/8$ universal.
- **Closed for $A = 2$**: deuteron internal Markov trace closed
  form derived (commit on PR #546, follow-up). All 11 partitions of
  6 contribute; per-partition $\chi^\lambda$ takes 0.1–22.8 s
  using the canonical engine's caching (total ~80 s). Pole order
  $19$, leading coefficient $+1/128 = +1/2^7$ — POSITIVE, opposite
  the $A = 1$ sign. The naive "universal $-1/(2 n!)$" conjecture is
  thereby falsified; the leading coefficient is still a power of 2,
  suggesting a refined conjecture.
- **Open for $A \geq 3$**: no symbolic computation attempted yet.
- **Closed-form Jones–Markov weights $y_\lambda(q)$ (round-3)**:
  derived in two equivalent ways — ladder linear system at $H_3$
  and Wenzl Schur principal specialisation for any $n$. Symbolic
  $\mathrm{tr}_M$ at $q_0$ now matches the canonical bridge for:
  - **proton** to 14 decimal places (using closed-form $y_\lambda$
    from the linear system + symbolic $\chi^\lambda$);
  - **deuteron** to $3.3 \times 10^{-16}$ (machine precision)
    using the canonical 23-crossing braid
    (`include_inter=True`) with bridge $y_\lambda$ for $n = 6$ and
    symbolic $\chi^\lambda$ from `chi_lambda_symbolic`.
  The partition-sum normalisation $w_\lambda/f^\lambda$ used in
  round-1/2 is NOT the canonical Markov weight; the two agree only
  at $q = 1$.
- **Deuteron braid convention**: the canonical $A = 2$ word includes
  one inter-nucleon crossing (gen $\sigma_2$), giving 23 crossings
  total. The 22-crossing form (`include_inter=False`) corresponds
  to two non-interacting nucleons in $H_6$ — useful for additivity
  audits but not the physical deuteron.

## Files

- [`computations/hoefsmit_symbolic.py`](../../computations/hoefsmit_symbolic.py)
  — reusable module with symbolic q-int, q-fac, dim_q, seminormal
  matrices, χ^λ, tr_M, and pole_order_at_zero.
- [Self-test](../../computations/hoefsmit_symbolic.py#__main__):
  cross-validates against numerical at $q_0$ + prints closed-form
  proton tr_M.
