# NV-1 candidate (b) — bounded probe

**Date.** 2026-05-03
**Target.** $N_v = 1{,}445{,}519$
**Conjecture under probe.**
[`conj:nv-as-bring-period-rank`](2026-05-02-nv-frob-filter-conjectures.md)
(candidate (b) of the NV-1 trio).
**Witness.**
[`nv1-candidate-b-bounded-probe.witness.json`](../../folio-assistant/computations/nv1-candidate-b-bounded-probe.witness.json)

## Scope

This is a STRICT bounded probe — closed-form arithmetic only, no
DP arrays of size $> 10^4$.  It is **not** a closure of candidate
(b).  The full Bring-period-lattice machinery (Riemann period
integration on $y^2 = x^5 - 1$) is research-grade open work and
is not addressed here.

The probe is sharply diagnostic: if $N_v$ is prime, then any
"rank decomposition" by representation dimensions of $S_5$ (or
$S_5 \times \mathbb{Z}/2$) cannot use multiplicative factorisation
across irreps; the question becomes whether a *small, natural*
multiplicity vector reproduces $N_v$.

## Step 1 — primality

Using `sympy.isprime` and `sympy.factorint`:

| Field | Value |
|-------|-------|
| $N_v$ | $1{,}445{,}519$ |
| `isprime(N_v)` | `True` |
| `factorint(N_v)` | `{1445519: 1}` |
| $N_v \bmod 4$ | $3$ |
| $N_v \bmod 5$ | $4$ |
| $N_v \bmod 6$ | $5$ |

So $N_v$ is **prime**.

## Step 2 — minimum-coin decompositions

We compute $\min(a + b + c)$ subject to $4a + 5b + 6c = N_v$,
with $a, b, c \geq 0$.  Since $\gcd(4, 5, 6) = 1$, every
sufficiently large $N$ is representable (Chicken-McNugget /
Frobenius).

**Closed-form reduction.** Substituting $a = (N - 5b - 6c)/4$,
the count becomes
$$
a + b + c \;=\; \frac{N - 2c - b}{4}.
$$
So minimising the count is equivalent to **maximising
$2c + b$** subject to
$5b + 6c \leq N$ and $b + 2c \equiv N \pmod{4}$.
Since $N_v \bmod 4 = 3$, the parity constraint is
$b + 2c \equiv 3 \pmod{4}$.

Pushing $c$ to the maximum $\lfloor N_v / 6 \rfloor = 240{,}919$
and adjusting $b$ over a small modular residue window (200
iterations, well under the bounded-probe budget) yields the
global optimum.

| Coin set | Min count | Decomposition $(a, b, c)$ |
|----------|-----------|----------------------------|
| $\{4, 5, 6\}$ | **240,920** | $(0,\,1,\,240{,}919)$ |
| $S_5$, dims $\geq 4$, i.e. $\{4, 5, 6\}$-cone | **240,920** | same |
| $S_5 \times \mathbb{Z}/2$, dims $\geq 4$ | **240,920** | same |

(Duplicate dims in the $S_5$ multiset $\{1,1,4,4,5,5,6\}$ and
the $S_5 \times \mathbb{Z}/2$ multiset
$\{1,1,1,1,4,4,4,4,5,5,5,5,6,6\}$ do not enlarge the integer
cone of attainable sums; they only multiply the number of
*labellings* of a given decomposition.  Min-count is therefore
identical to the plain $\{4, 5, 6\}$ case.)

The lower bound $\lfloor N_v / 6 \rfloor = 240{,}919$ is missed
by exactly $1$, because $N_v \bmod 6 = 5$ forces a single
dim-$5$ replacement.

## Step 3 — verdict

**Falsification-leaning probe** (NOT a closure).

**Rationale.**

1. **Primality.**  $N_v$ has no non-trivial integer factorisation;
   any rank decomposition into $S_5$ irreps cannot exploit
   multiplicative structure across dim channels.
2. **Magnitude.**  The minimum multiplicity sum is
   $240{,}920 \gg 1000$, so by the probe rule
   (min count $> 1000$ $\Rightarrow$ falsification-leaning),
   candidate (b) loses its intuitive footing as a *small,
   natural* rank decomposition.
3. **Concentration.**  The unique optimum is highly degenerate:
   $\sim$ 240,919 copies of the dim-6 irrep plus a single dim-5
   copy, with **zero dim-4 copies**.  A Bring period sub-lattice
   that lands on this profile would itself need an explanation.

**Caveat.**  "Natural" is fuzzy.  A Bring-period rank could in
principle realise *any* specific positive integer, prime or
composite, without admitting an irrep-decomposition reading at
all.  The probe weakens the candidate as an *intuitively
appealing* path; it does not refute the rank-equality numerical
claim itself.

**Status.**  All three probe steps complete; verdict is final
within the bounded-probe scope.  Promotion of this verdict to
either falsification or closure of
`conj:nv-as-bring-period-rank` requires the research-grade Bring
period-lattice machinery described in the next section.

## Handoff

Full Bring-period-lattice machinery on $y^2 = x^5 - 1$ remains
research-grade open work.  Specifically, what is needed is:

- Riemann period integration on the genus-2 hyperelliptic
  curve $y^2 = x^5 - 1$ to extract the $S_5 \times
  \langle\hat\tau\rangle$-stable period sub-lattice;
- the rank computation of the projection
  $\rho_{\rm weak}\colon \widehat{\mathcal{M}} \to
  \mathbb{Z}[q] / \Phi_{p_w^{k_w}}(q)$ at $k_w = 9$;
- a numerical comparison of that rank with $N_v = 1{,}445{,}519$.

Until that machinery exists, this probe stands as
*falsification-leaning evidence*, not falsification.

See [`docs/audits/conjecture-cones.md`](conjecture-cones.md)
and the candidate-(b) entry of the
[NV-1 conjectures memo](2026-05-02-nv-frob-filter-conjectures.md).
