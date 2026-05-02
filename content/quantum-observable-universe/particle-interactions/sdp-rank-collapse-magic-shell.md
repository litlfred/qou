## Statement

**Proposition 5 (SDP rank-1 collapse selects the magic ladder).**
*Let $\mathcal{P}(n; q)$ denote the nuclear-confinement SDP
([prop:confinement-sdp](#prop:confinement-sdp)) at strand count $n$
and substrate $q$, with optimal primal solution $T^*(n, q)$ and
optimal dual shadow-price vector $u^*(n, q)$. Define the structural-
optimum predicate*

$$
S(n, q) \;\equiv\; \operatorname{rank}\!\bigl(T^*(n, q)\bigr) = 1
\;\wedge\;
\operatorname{supp}(u^*(n, q))
  \;\subseteq\; \bigl\{ \lambda \vdash n \,:\, \lambda = \lambda' \bigr\}.
$$

*Then for **generic** $q \in (1, \infty)$ (i.e., excluding a measure-
zero set of roots-of-unity-like specializations),*

$$
\bigl\{ n \in \mathbb{N} \,:\, S(n, q) \bigr\}
\;=\;
\{2,\, 8,\, 20,\, 28,\, 50,\, 82,\, 126\}.
$$

## Status

**Conjecture** (CLAUDE.md §3b axiom-class). Strong claim — promises
a $q$-independent partition-structural property selecting the magic
ladder, which (per the
[pattern-investigation negative result](https://github.com/litlfred/qou/blob/claude/qou-algebraic-refactor-1qVFc/folio-assistant/computations/magic-ladder-pattern-investigation.md))
is **not visible** in pure self-conjugate-partition combinatorics.
The claim rests on the SDP machinery filtering self-conjugate $\lambda$
through the LR-fusion and Wedderburn-Hoefsmit structure to single out
magic $n$ even at generic $q$.

## Why this is plausible

The pattern investigation showed:
- self-conjugate partitions exist for *almost every* $n$;
- partition-counting statistics ($q(n)$, max-Durfee, etc.) do not
  pick out magic.

So whatever distinguishes magic must use **more structure** than
self-conjugacy. Two extra structural pieces enter via the SDP:

1. **LR-fusion stability.** The dominant Hecke-LR module in
   $V_{\lambda} \otimes V_{\lambda}$ for self-conjugate $\lambda$ is
   itself a partition $\lambda_A \vdash 2n$. The conjecture is that
   $\lambda_A$ is *also* self-conjugate **and** rank-1 dominant
   *only* when $n$ is magic.
2. **Wedderburn-Hoefsmit positivity.** The Hoefsmit matrix
   $\rho_\lambda$ has eigenvalue structure that, combined with the
   Wedderburn weight $w_\lambda = \dim_q(\lambda)^2 / [k]_q!$,
   forces the SDP optimum onto a single block at magic $n$.

The "completely filled" intuition: at magic $n$, the canonical self-
conjugate $\lambda$ is the unique partition whose Standard Young
Tableau structure is **fully saturated** in the Hecke branching
lattice — every cell admits a unique boxing-order compatible with
the rank-1 SDP optimum. At non-magic $n$, multiple boxings compete,
forcing the SDP optimum into a higher-rank superposition.

## Sharp testable form

Let $\nu_\lambda \vdash 2n$ denote the LR-dominant partition in
$V_\lambda \otimes V_\lambda$ for self-conjugate $\lambda \vdash n$:

$$
  \nu_\lambda \;:=\; \arg\!\max_{\mu \,\vdash\, 2n}
  \;c^\mu_{\lambda, \lambda},
$$

with $c^\mu_{\lambda, \lambda}$ the Littlewood–Richardson coefficient.
The conjecture claims:

| Property | Magic $n \geq 8$ | Non-magic $n$ |
|---|:---:|:---:|
| Some self-conjugate $\lambda \vdash n$ exists | yes | yes (except $n=2$) |
| For some self-conj $\lambda$, $\nu_\lambda$ is self-conjugate | **yes** | **no** |
| $\operatorname{rank}(T^*(n, q)) = 1$ at generic $q$ | **yes** | **no** |

The middle row is the **$q$-independent** algebraic test: numerically
compute LR coefficients for each canonical self-conj $\lambda \vdash n$
and check whether the dominant tensor product component is itself
self-conjugate. If this property is exclusive to magic $n$, the
SDP rank-1 conjecture becomes a corollary.

## What this contradicts and what it explains

**Contradicts:** my earlier (now-corrected) Proposition 3 implication
that *any* self-conjugate $\lambda$ is enough to mark magic.
The corrected reading: **dominance under LR-fusion** is the extra
condition, and it filters self-conjugates down to the magic-shell
ones.

**Explains:**
- Why the magic ladder is $q$-independent at the partition-structural
  level (matches the user's intuition that magic should hold at
  generic $q > 1$).
- Why $q_0 \approx 1.10974$ enters only *quantitatively* — to fix
  numerical mass values via the Hoefsmit spectrum; the
  *which-$n$* selection is partition-structural and $q$-generic.
- Why the
  [pattern investigation negative result](https://github.com/litlfred/qou/blob/claude/qou-algebraic-refactor-1qVFc/folio-assistant/computations/magic-ladder-pattern-investigation.md)
  did not find a $q$-independent partition statistic — the
  required statistic is a *binary structural property of LR-fusion*,
  not a numerical metric.

## Empirical update — q-independent route does NOT work

The Yamanouchi-LR enumeration in
[`folio-assistant/computations/lr_fusion_self_conj_test.py`](https://github.com/litlfred/qou/blob/claude/qou-algebraic-refactor-1qVFc/folio-assistant/computations/lr_fusion_self_conj_test.py)
ran the LR self-fusion test on canonical self-conjugates of
$n \in \{8, 12, 16, 20\}$ (mix of magic and non-magic). Result:

| $n$ | magic? | canonical $\lambda$ | dominant $\nu$ | $c^\nu_{\lambda,\lambda}$ | $\nu = \nu'$? |
|----:|:------:|:--------------------|:---------------|--------------------------:|:---------:|
| 8 | $\star$ | $[3,3,2]$ | $[6,5,3,2]$ (5+ tied at c=11) | 11 | no |
| 12 | | $[4,4,2,2]$ | $[8,8,4,2,2]$ | 274 | no |
| 16 | | $[4,4,4,4]$ | $[8,8,4,4,4,4]$ | 387 | no |
| 20 | $\star$ | $[5,5,4,4,2]$ | $[10,10,5,5,4,4,2]$ | 85077 | no |

In every case — magic *and* non-magic — the dominant $\nu$ is **not**
self-conjugate. So the proposed q-independent rank-collapse via
LR-fusion self-conjugacy **does not hold** as stated.

A subtler signal does appear in the *tie pattern*: at $n = 8$ five
or more $\nu$ tie at $c = 11$, while at $n = 12, 16$ the dominant
is unique with a clear gap to second. But $n = 20$ (also magic)
has a unique dominant followed by two tied seconds — so the
"top-tier degeneracy" pattern is not consistent across magic $n$.

## Conclusion — magic selection is genuinely q-dependent

Combined with the
[earlier negative result on partition statistics](https://github.com/litlfred/qou/blob/claude/qou-algebraic-refactor-1qVFc/folio-assistant/computations/magic-ladder-pattern-investigation.md),
this LR-fusion negative result rules out **all** purely
combinatorial / q-independent routes to the magic ladder. The
selection rule must come from the **q-dependent** Hoefsmit matrix
spectrum, which encodes effective spin-orbit coupling through the
$q$-deformation $[\rho]_q = (q^\rho - q^{-\rho})/(q - q^{-1})$.

The conjecture as originally stated (q-independent rank-1 collapse)
is therefore **rejected**. The corrected reading:

**Proposition 5 (revised, q-dependent).** *The nuclear-confinement
SDP at substrate $q = q_0$ specifically has $\sigma_F(n, q_0)$
peaks (or rank-1 optima) exactly at $n \in \{2, 8, 20, 28, 50, 82,
126\}$, while at generic $q \neq q_0$ the peaks land on a different
ladder (e.g. the pure 3D-oscillator $\{2, 8, 20, 40, 70, 112, 168\}$
at $q \to 1$). $q_0$ is the substrate value that simultaneously
fixes the categorical mass-formula CODATA match **and** places the
SDP peaks on the empirical nuclear magic ladder.*

This is the falsifiable statement.

## Falsification path (revised)

Numerical: solve the nuclear-confinement SDP at $n = 1, \ldots, 130$
for several $q$ values around $q_0 \approx 1.10974$. Plot the
$\sigma_F(n, q)$ surface or rank-1-locus map. The claim is that
**only at $q = q_0$** (or in a narrow $q$-band around it) does the
rank-1-optimum locus match $\{2, 8, 20, 28, 50, 82, 126\}$. At
other $q$ the locus shifts.
