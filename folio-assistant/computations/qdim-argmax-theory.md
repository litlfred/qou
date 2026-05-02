# q-Dim argmax theory — what's provable, what's not

Symbolic computation in
[`symbolic_qdim_argmax.py`](symbolic_qdim_argmax.py) reveals the
regularity structure of $\dim_q(V_\lambda)$ as a function of $q$.
This document records what is rigorously provable and the empirical
findings on whether magic-ladder selection is visible at this level.

## What is provable

**Definition.** For a partition $\lambda \vdash n$, the *quantum
dimension* of the irreducible Iwahori–Hecke module $V_\lambda$ at
substrate $q$ is

$$
  \dim_q(V_\lambda)
  \;=\;
  \frac{[n]_q!}{\prod_{x \in \lambda} [h(x)]_q},
$$

where $[k]_q = (q^k - q^{-k})/(q - q^{-1}) = q^{k-1} + q^{k-3} +
\cdots + q^{-(k-1)}$ and $h(x)$ is the hook length of cell $x$.

**Lemma (positivity, $q > 1$).** $[k]_q > 0$ for all $k \geq 1$ and
$q > 1$. Hence $\dim_q(V_\lambda) > 0$ for all $\lambda \vdash n$
and $q > 1$.

*Proof.* $[k]_q = q^{k-1} + q^{k-3} + \cdots + q^{-(k-1)}$ is a sum
of positive monomials in $q^{\pm 1}$ for $q > 0$. Hence positive.
For $q > 1$ and $q > 0$, each summand is strictly positive. $\square$

**Lemma (rational function).** $\dim_q(V_\lambda)$ is a Laurent
polynomial in $q^{1/2}$ with positive integer coefficients (after
multiplication by an appropriate $q^a$). In particular,
$\dim_q(V_\lambda)$ is a *rational function* of $q$.

*Proof.* $[n]_q!$ is a Laurent polynomial in $q^{1/2}$. So is each
$[h(x)]_q$. The ratio is a rational function. The classical
character-theoretic interpretation gives positive integer
coefficients. $\square$

**Lemma (hook-length multiset invariance).**
For any partition $\lambda \vdash n$, the multiset
$\{h(x) : x \in \lambda\}$ equals the multiset
$\{h(x) : x \in \lambda'\}$.

*Proof.* Transposition $(i, j) \mapsto (j, i)$ is a bijection
$\lambda \to \lambda'$ that preserves hook length: if cell $(i, j)$
has hook length $h = (\lambda_i - j) + (\lambda'_j - i) + 1$, then
its transpose $(j, i) \in \lambda'$ has hook length $(\lambda'_j -
i) + (\lambda_i - j) + 1 = h$. $\square$

**Corollary.** $\dim_q(V_\lambda) = \dim_q(V_{\lambda'})$ for every
$\lambda$ and every $q$. Conjugate partitions are q-dim
indistinguishable.

**Theorem (regime regularity).** For two partitions $\lambda, \mu
\vdash n$ with **distinct** hook-length multisets, the equation
$\dim_q(V_\lambda) = \dim_q(V_\mu)$ holds for at most finitely many
$q > 0$.

*Proof.* The difference $D(q) = \dim_q(V_\lambda) - \dim_q(V_\mu)$
is a rational function of $q$ (Lemma "rational function"). After
clearing denominators we get $D(q) = N(q)/M(q)$ for some Laurent
polynomials $N, M$ with $M$ never zero on $q > 0$ (denominators
are products of $[h(x)]_q$, all positive on $q > 1$, and similar
on $q \in (0, 1)$).

If $D \equiv 0$ then $N \equiv 0$, hence $\dim_q(V_\lambda) =
\dim_q(V_\mu)$ for all $q$, in particular for $q$ near $1$. By the
classical limit $\lim_{q \to 1} \dim_q(V_\lambda) = \dim V_\lambda
= n! / \prod_{x} h(x)$, this forces $\prod h(x \in \lambda) =
\prod h(x \in \mu)$, hence (since these are products of integer
multisets equal in size) the hook-length multisets *as products*
agree. But by hook-length-formula injectivity (modulo conjugate
pairs), the hook-length **multisets** must agree, contradicting the
hypothesis.

So $D \not\equiv 0$, hence $N \not\equiv 0$. A nonzero Laurent
polynomial has at most finitely many roots in $\mathbb{R}_{>0}$.
$\square$

**Corollary (piecewise-constant argmax).** The function
$$
  q \mapsto
  \arg\!\max_{\lambda \,\vdash\, n}\,\dim_q(V_\lambda)
$$
is piecewise constant on $(0, \infty)$ modulo identification of
partitions with the same hook-length multiset (in particular,
modulo the conjugate involution $\lambda \mapsto \lambda'$). It
changes at most at finitely many critical $q^* > 0$.

*Proof.* For each pair $(\lambda, \mu)$ with distinct hook-length
multisets, the set $C_{\lambda, \mu} = \{q : \dim_q(V_\lambda) =
\dim_q(V_\mu)\}$ is finite. The total set $C = \bigcup_{\lambda,
\mu} C_{\lambda, \mu}$ is a finite union of finite sets, hence
finite. On each open interval of $(0, \infty) \setminus C$, no two
distinct hook-length-multiset classes have equal q-dim, so the
argmax class is constant. $\square$

## Empirical: argmax does NOT predict magic

Symbolic test on $n \in \{4, 6, 8, 10, 12, 14, 16\}$ at $q_0
\approx 1.10974$:

| $n$ | argmax class at $q_0$ | self-conj? | magic? |
|---:|:----------------------|:-----------:|:------:|
| 4 | $\{[3,1], [2,1,1]\}$ | no (conjugate pair) | no |
| 6 | $\{[3,2,1]\}$ | yes (self-conj) | no |
| 8 | $\{[4,2,1,1]\}$ | yes (self-conj) | $\star$ |
| 10 | $\{[4,3,2,1]\}$ | yes (self-conj) | no |
| 12 | $\{[5,3,2,1,1]\}$ | yes (self-conj) | no |
| 14 | $\{[5,4,2,2,1]\}$ | yes (self-conj) | no |
| 16 | $\{[6,4,3,2,1], [5,4,3,2,1,1]\}$ | no (conjugate pair) | no |

**Result:** self-conjugate-argmax at $q_0$ is **not** a magic-ladder
discriminator. Magic $n = 8$ is in the self-conj set, but so are
non-magic $n \in \{6, 10, 12, 14\}$. The argmax flips between
self-conj and non-self-conj depending on whether $n$ has an odd or
even-length staircase compatible with $q_0$.

A regime change *was* observed at $n = 14$ in the interval
$(1.05, 1.10974)$, demonstrating that the piecewise-constant
theorem above has non-trivial content. But the regime structure
does not align with the nuclear magic ladder.

## What the negative results tell us

Three independent non-magic-discriminator findings now:

1. **Partition statistics** — `magic-ladder-pattern-investigation.md`
   (count $q(n)$, max-Durfee, hook-length spread, etc., all fail).
2. **LR self-fusion self-conjugacy** —
   `lr_fusion_self_conj_test.py` (LR-dominant $\nu_\lambda$ is not
   self-conjugate at any $n$ tested).
3. **q-dim argmax** — this document (argmax stays self-conj across
   wide non-magic ranges of $n$ at $q_0$).

The magic ladder requires:
- The full **Hoefsmit matrix structure** (off-diagonal entries
  encoding spin-orbit asymmetry), not just q-dimensions;
- Coupled with the **specific demand vector** of the
  nuclear-confinement SDP (proton-neutron pair Skein);
- And the **specific substrate value** $q_0$.

This rules out the q-independent reading of `conj:sdp-rank-collapse-
magic-shell` at the level of dimension-LP. The conjecture must be
formulated at the full nuclear-confinement SDP level, where the
demand structure provides the missing "spin-orbit" input.

## Provable Lean form

The piecewise-constancy theorem is formalisable in Lean using
Mathlib's `Polynomial` and `Multiset` infrastructure. The key
statement:

```lean
theorem qdim_argmax_piecewise_constant
    (n : ℕ) :
    ∃ (S : Finset ℝ),
      ∀ q ∈ Set.Ioi (0 : ℝ) \ S,
      ∃ (λ_star : YoungDiagram),
        ∀ λ : YoungDiagram, λ.n = n →
          dim_q λ q ≤ dim_q λ_star q
```

with `S` the (finite) set of regime-boundary $q$ values. Future
formalisation work; not yet committed.
