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

| $\lambda$ | $\chi^\lambda(\text{proton})$ | pole at $q=0$ |
|---|---|---:|
| $(3)$ | $\dfrac{q^5}{4} + \dfrac{q^3}{2} + \dfrac{q}{4}$ | regular |
| $(2,1)$ | $\dfrac{q^{22} + q^{20} + q^{18} + q^{14} - q^8 - q^4 - q^2 - 1}{4\,q^{11}}$ | 11 |
| $(1,1,1)$ | $-\dfrac{q^4 + 2q^2 + 1}{4\,q^5}$ | 5 |

Cross-validated at $q_0$: all three match `build_seminormal_matrices`
within $10^{-6}$.

## Closed-form Markov trace for proton standalone

Using $\mathrm{tr}_M(\beta) = \sum_\lambda w_\lambda \cdot \chi^\lambda(\beta) / f^\lambda$
with $w_\lambda = \dim_q(\lambda)^2 / [n]_q!$ and $f^\lambda = \#\mathrm{SYT}(\lambda)$:

$$
\boxed{\;\;
\mathrm{tr}_M(\text{proton})
\;=\;
\frac{q^{20} + q^{18} + 2 q^{12} - 2 q^{8} - q^{2} - 1}{12 \cdot q^{10}}
\;\;}
$$

**Pole order at $q = 0$ : exactly 10** (matching `dp_pole_probe`'s
empirical value).
**Leading coefficient : $-\dfrac{1}{12}$ EXACTLY** (matching the
200-dps numerical verification from
[`docs/audits/2026-05-04-ocneanu-cancellation-numerical-verification.md`](2026-05-04-ocneanu-cancellation-numerical-verification.md)).

## Closed-form Markov trace for neutron standalone

$$
\mathrm{tr}_M(\text{neutron})
\;=\;
\frac{q^{20} + 2 q^{18} + 2 q^{16} + q^{14} + 2 q^{12} - 2 q^{8} - q^{6} - 2 q^{4} - 2 q^{2} - 1}{12 \cdot q^{8} \cdot (q^4 + q^2 + 1)}
$$

**Pole order = 8 EXACTLY**, leading coefficient $= -\dfrac{1}{12}$
(both match dp_pole_probe + numerical verification).

## Universal leading coefficient $-1/12$

Both proton and neutron standalone have leading coefficient at
$q=0$ EQUAL TO $-1/12$. This is a **universal structural identity**
across nucleon types (the same $1/12 = 1/[3]!$ Plancherel-style
denominator emerges).

We conjecture (open) that this universality extends to all
$A \geq 2$ atoms:

> **Conjecture.** For every atom in canonical pppnnn ordering, the
> leading coefficient of $\mathrm{tr}_M$ at $q = 0$ is $-1/[3A]!_{q=0}$
> (the inverse classical symmetric-group-algebra dimension).

For $A = 1$: $1/[3]!_{q=1} = 1/6$. But numerical was $-1/12$, half
of $-1/6$. So the conjecture above as stated is half-off; needs
refinement.

Empirical pattern from $A = 1$:
- proton (n=3): leading = $-1/12 = -1/(2 \cdot 3!)$
- neutron (n=3): leading = $-1/12$

So the universal coefficient may be $-1/(2 \cdot n!)$. Verifying
for $A \geq 2$ is the natural extension once the $n = 6, 9, 12$
symbolic computations become tractable.

## Use case: m_p calculation?

**Direct plug-in: NOT YET.** The existing
`hecke_characters.compute_mass_at_level(1, 0, k=3)` returns
$m_p \approx 938.78$ MeV (within 0.05% of CODATA 938.27). It uses
the same Wedderburn weight formula but produces $\mathrm{tr}_M = 1.065$
at $q_0$, while my symbolic closed form gives $0.433 \approx \frac{1}{2} \cdot 1.065$.

The factor-of-2 discrepancy is a **normalization issue** (likely
the `sqrt` choice in $b^2 = a \cdot a' + 1$ — sympy's `sp.sqrt`
returns the principal branch which may differ from `math.sqrt(abs(...))`
used in the existing numerical code).

**To use this for m_p calculation**, the symbolic closed form
needs to be aligned with the canonical pipeline normalization
(or the existing pipeline normalization needs to be expressed
symbolically). Both approaches are tractable next steps.

**Where m_e enters:** the Wedderburn-Markov mass formula uses
$E_0 = Q_{\text{neutron}} = 0.7823$ MeV as the dimensional bridge,
not $m_e$ directly. $m_e$ enters elsewhere via the trefoil
$T_{2,3}$ (electron knot) Markov trace. The symbolic
$\mathrm{tr}_M(\text{proton})$ I derived is **dimensionless**;
multiplying by $E_0$ gives binding energies in MeV, but mass itself
needs the full Wedderburn structure that
`compute_mass_at_level` already encodes.

## Status

- **Closed for $A = 1$**: symbolic Hoefsmit 2×2 fixed, closed-form
  $\mathrm{tr}_M$ for proton + neutron derived in $R$, pole order
  + leading coefficient $-1/12$ confirmed.
- **Open for $A \geq 2$**: symbolic deuteron tr_M timed out at 600s
  (n=6 has 11 partitions, $f^\lambda$ up to 16 — feasible with
  partition filtering or longer compute time).
- **Open: m_p direct plug-in**: factor-of-2 normalization
  discrepancy with the canonical pipeline; alignment needed.

## Files

- [`folio-assistant/computations/hoefsmit_symbolic.py`](../../folio-assistant/computations/hoefsmit_symbolic.py)
  — reusable module with symbolic q-int, q-fac, dim_q, seminormal
  matrices, χ^λ, tr_M, and pole_order_at_zero.
- [Self-test](../../folio-assistant/computations/hoefsmit_symbolic.py#__main__):
  cross-validates against numerical at $q_0$ + prints closed-form
  proton tr_M.
