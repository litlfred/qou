# How are the "H_3 weights at H_{3A}" derived?

**User question (2026-05-01)**: investigate the derivation of the
H_3 Wedderburn weights as applied to H_{3A} compute, since the
P2.1a witness shows they cause Φ_q divergence.

## Headline

The H_3 weights are **correctly derived for H_3** but **applied
incorrectly at H_{3A}** — a per-generator dimensional truncation
that's only valid when the 3A-strand braid factors into A
independent 3-strand pieces (intra-nucleon only). The
inter-nucleon generators couple nucleons and break the
factorization. The replacement (`schur_weyl_symbolic.py`) exists
in the repo but is not wired into the live mass-tower compute.

## (A) The H_3 weight derivation — correct at n = 3

In both [`mass_endomorphism.py`](../../computations/mass_endomorphism.py)
and [`crt_markov.py`](../../computations/crt_markov.py):

```python
nf3   = qfact(3)                       # = [1]_q · [2]_q · [3]_q  (always n=3)
w_sym = qdim((3,),     3) ** 2 / nf3   # 1²        / [3]_q!  → 1/[3]_q!
w_std = qdim((2, 1),   3) ** 2 / nf3   # [2]_q²    / [3]_q!
w_alt = qdim((1,1,1),  3) ** 2 / nf3   # 1²        / [3]_q!  → 1/[3]_q!
# Then normalised: w_sym + w_std + w_alt = 1
```

This is the **Wedderburn–Artin Plancherel formula at n = 3**:
$w_\lambda = \dim_q(\lambda)^2 / [n]_q!$ for each $\lambda \vdash n$.
With $n = 3$, three partitions $(3), (2,1), (1,1,1)$ give the
three "sym / std / alt" channels. The values
$\dim_q((3)) = 1$, $\dim_q((2,1)) = [2]_q$, $\dim_q((1,1,1)) = 1$
are the standard $q$-Weyl dimensions of those Specht modules.

🟢 The H_3 weights themselves are derived correctly. They are
**the canonical $w_\lambda$ of [`prop:wedderburn-weight-canonical`](../../content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.md) at $n = 3$**.

## (B) How they are applied to H_{3A} — the structural mistake

In `tower_mass_symbolic_eval` (`crt_markov.py:169`), the
**three** H_3 weights are applied **per H_{3A} generator**:

```python
for gen in range(n_strands - 1):       # n_strands = 3A
    a = mpmath.mpf(0); b = mpmath.mpf(1)
    sp = mpmath.mpf(1); ap = mpmath.mpf(1)
    for c, d in crossings[gen]:
        a, b = a*c*h + a*d + b*c,  a*c + b*d
        sp = sp * (c*q + d)            # sym channel accumulator
        ap = ap * (-c*qi + d)          # alt channel accumulator
    Vs = z*a + b                       # std channel
    V_full = w_sym*sp + w_std*Vs + w_alt*ap
    V_full_list.append(V_full)
```

Each of the $3A-1$ generators is decomposed into the **same three
H_3 channels**. The weights $(w_\text{sym}, w_\text{std}, w_\text{alt})$
do not change with $A$. This treats H_{3A} as if it were
**A independent copies of H_3** stitched together by per-generator
products.

🔴 **This is wrong for H_{3A}.** Two reasons:

1. **The Wedderburn decomposition of H_{3A} is by partitions
   $\lambda \vdash 3A$, not by H_3-channels.** The number of blocks
   grows fast: $p(6) = 11$ at $A=2$, $p(9) = 30$ at $A=3$,
   $p(12) = 77$ at $A=4$, $p(15) = 176$ at $A=5$. The "three
   channels" abstraction is a fiction past $n=3$.

2. **H_3-channel multiplication compounds eigenvalues.**
   A generator's $\sigma_i$ acts on $H_3$ via eigenvalues
   $\{q, -q^{-1}\}$ on the (2,1)-block (std), $q$ on the (3)-block
   (sym), $-q^{-1}$ on the (1,1,1)-block (alt). On a single H_3
   block the per-generator $V$ stays in a bounded range:
   $|V_\text{std}| \leq q + |z| \cdot q$ etc.
   Multiplying $V_\text{full}$ across $3A-1$ generators, the
   product accumulates as approximately $q^{3A-1}$. By $A = 2$
   this can already exceed $q$ (the Φ_q convergence bound).

🔴 **Result: Φ_q divergence.** Per the P2.1a witness
[`2026-05-01-p2-1a-tower-vs-descended.witness.json`](2026-05-01-p2-1a-tower-vs-descended.witness.json),
$\Phi_q(|V_i^\text{full}|)$ blows up by $10^9$ already at A=2 (D)
and by $10^{16}$ at A=12 (¹²C). The tower formula is divergent,
not just inaccurate.

## (C) The correct H_{3A} derivation — `schur_weyl_symbolic.py`

[`schur_weyl_symbolic.py`](../../computations/schur_weyl_symbolic.py)
implements the proper formulation:

$$
  \mathrm{tr}_M(\mathcal{A})
  \;=\;
  \sum_{\lambda \vdash 3A}
    w_\lambda(q) \cdot \chi^\lambda(\mathcal{A}),
$$

with weights using the **Schur / q-hook formula**:

$$
  w_\lambda(q)
  \;=\;
  \frac{s_\lambda(q, q^{-1})}{H_q(\lambda)},
  \qquad
  H_q(\lambda) = \prod_{x \in \lambda}[h_x(\lambda)]_q,
$$

where $s_\lambda(q, q^{-1})$ is the Schur function specialised at
two variables and $H_q(\lambda)$ is the $q$-hook product.

For each $\lambda \vdash 3A$:

- $H_q(\lambda)$ via box-by-box hook lengths.
- $s_\lambda(q, q^{-1})$ via the principal-specialisation formula
  (vanishes for length $> 2$; explicit closed form for
  lengths 1 and 2).
- $\chi^\lambda(\mathcal{A})$ via Specht / Murnaghan–Nakayama on
  the cycle type of the atomic braid's underlying permutation.

Symbolic in $q$ throughout; final substitution at $q_0$ for
arbitrary precision via `sympy.evalf(dps)`.

🟢 The script's docstring explicitly notes:

> *"A = 4 (⁴He) is the first case where the additive-H_3
> approximation fails by ~5%."*

So the paper's authors **knew** the H_3-at-H_{3A} approach was an
approximation and wrote the correct H_{3A} replacement.

## (D) Why the replacement isn't yet live

`schur_weyl_symbolic.py` was added in the same PR (#419) that
deprecated `gb_residue_tower.py` (Apr 25 2026) — both moves
motivated by the archimedean-wall reasoning (dense roots of
unity → S¹ is a natural boundary, not analytic curve →
must work in $\mathbb{Q}(q)$ symbolically). But the live
compute pipeline (`tower_mass_symbolic_eval` and
`mass_endomorphism.mass_from_tower`) still calls into the
H_3-weighted construction.

**No script imports `schur_weyl_symbolic.global_wedderburn_sum_symbolic`**
to drive the live mass tower. It is the *correct* replacement that
**hasn't been wired in**.

## Implication for the workplan

This re-frames **P2.2** ("$H_{3A}$ Wedderburn coverage via CRT
polynomial reconstruction") as **two sub-tasks**:

- **P2.2a — Wire `schur_weyl_symbolic` into the live mass tower.**
  Replace the H_3-weighted `tower_mass_symbolic_eval` calls (or
  augment with a Schur–Weyl path). The math is already
  implemented; the wiring isn't.
- **P2.2b — CRT polynomial reconstruction at H_{3A}.** When
  symbolic Schur–Weyl gets too slow at high $A$ (per
  [`tower_binding_symbolic.py`](../../computations/tower_binding_symbolic.py)
  hitting polynomial explosion at A=4), use CRT polynomial
  reconstruction (evaluate at multiple rational $q_i$, reconstruct
  $\mathbb{Z}[q^{\pm 1}]$ coefficients) to scale beyond.

P2.2a is the "small optimization" entry point — wire the existing
correct math into the live pipeline. P2.2b is the multi-week heavy
compute work.

## Decision required

Three options for the live mass tower at higher A:

- **(A) Wire schur_weyl_symbolic now (P2.2a)** — small change,
  uses correct math, but slow at A ≥ 4 due to polynomial size.
- **(B) Skip directly to CRT (P2.2b)** — multi-week, scales to
  high A, but reproduces math that already exists symbolically.
- **(C) Hybrid** — P2.2a for low A (≤ 3), P2.2b for higher A.
  Lets us land *something* live now while building the scaling
  path.

**Recommendation: (C).** Wire schur_weyl_symbolic for D, ³He,
⁴He immediately so the audit can show convergent V̂_i values;
queue P2.2b for the heavy lift on ¹²C and beyond.
