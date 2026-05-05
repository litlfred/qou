# Symbolic Hoefsmit 2×2 fix → closed-form proton tr_M

**Branch.** `claude/hoefsmit-2x2-fix`
**Module.** [`folio-assistant/computations/hoefsmit_symbolic.py`](../../folio-assistant/computations/hoefsmit_symbolic.py)
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

**Note (PR #546 round-2 update).**  The earlier draft of this module
duplicated the seminormal construction.  Per Copilot's review, the
duplicate has been removed and the matrix builder + braid-character
function now delegate to `hecke_character_symbolic.{hoefsmit_matrices_symbolic,
q_character_on_braid_word}`.  This guarantees a single source of truth
for the seminormal matrices and the matrix-multiplication order.  An
earlier `f^\lambda` bug (using `len(...)` of the 3-tuple returned by
`standard_young_tableaux` instead of the SYT list itself) was also
fixed; closed-form constants below reflect the corrected denominator.

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
- **No normalization gap**: the apparent $0.702$ vs $1.065$
  discrepancy (round-1 audit) was a phantom — the canonical
  pipeline short-circuits at $A \le 1$ and does not compute the
  internal proton braid character. The closed form here is the
  unique symbolic reference for $\mathrm{tr}_M(\text{atomic
  proton})$.

## Files

- [`folio-assistant/computations/hoefsmit_symbolic.py`](../../folio-assistant/computations/hoefsmit_symbolic.py)
  — reusable module with symbolic q-int, q-fac, dim_q, seminormal
  matrices, χ^λ, tr_M, and pole_order_at_zero.
- [Self-test](../../folio-assistant/computations/hoefsmit_symbolic.py#__main__):
  cross-validates against numerical at $q_0$ + prints closed-form
  proton tr_M.
