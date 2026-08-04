# T3f audit: Ocneanu/Markov trace parameter — derived or chosen?

**Date:** 2026-08-04
**Bean:** `qou-w5fw` (T3f), epic `qou-8lxd`
**Branch:** `claude/eightfold-tg-t3f-2026-08-04`

## Bottom line

The Ocneanu trace on the Hecke tower $H_\bullet(q)$ carries a **free
parameter** $s$ (or equivalently $a = q^{N-1}$) that selects the gauge
group rank $N$. QOU's mass/binding pipeline uses the **Jones
specialization** ($N = 2$, $a = q$, $z = 1/(q^{1/2} + q^{-1/2})$).
This specialization is **not forced** by the Descartes condition — the
Descartes condition constrains the fibre gauge group to $\mathrm{SU}(2)$,
but the Ocneanu trace parameter is a different object: it selects which
$\mathfrak{gl}_N$-weighted invariant the trace computes.

**Status: GENUINELY OPEN.** Neither "derived" nor "freely chosen" is
established. The truth may lie between: the Descartes condition may
constrain $N$ in the mass pipeline (where the trace feeds the physical
mass formula), while leaving $N$ free in the purely topological
(knot-invariant) setting.

## 1. The two objects that must not be conflated

| Object | What it governs | What constrains it |
|---|---|---|
| **Fibre gauge group** $\mathrm{SU}(2)$ | The categorical braid representation $V^{\otimes n}$ | Descartes condition $\chi(\mathcal{A}) = -6$ |
| **Ocneanu parameter** $a = q^{N-1}$ | Which $\mathfrak{gl}_N$-weighted link invariant the Markov trace computes | **Unknown** |

The Descartes condition says `dim V = 2`. This forces the Schur-Weyl
commutant to be $\mathcal{U}_q(\mathfrak{gl}_2)$. But the Ocneanu trace
is defined on $H_n(q)$ **abstractly** — it does not require a specific
$V$ to exist. The parameter $a$ in HOMFLY-PT is:

- $a = q$ → Jones polynomial ($\mathfrak{gl}_2$)
- $a = q^2$ → $\mathfrak{gl}_3$ invariant (eightfold way!)
- $a = q^{N-1}$ → $\mathfrak{gl}_N$ invariant

## 2. Corpus evidence

### 2a. The mass pipeline uses Jones ($N = 2$)

From `h3-markov-wenzl-weights-context.md`:
> "full-Hecke Ocneanu Markov trace, with parameter $z = 1/(q^{1/2}+q^{-1/2})$"

This $z$ is the Jones specialization. All mass ratios ($m_\mu/m_e$,
proton mass, etc.) are computed with this trace. Changing $N$ would
change these mass predictions.

### 2b. The archimedean image table shows $N$ is free

From `archimedean-image-table-table1-data.md` row 5:
> "HOMFLYPT $P(K; a, z)$ ... $\{P(K; q_0^{N-1}, h_q)\}_{N \geq 2}$"

This explicitly treats $N$ as a free parameter indexing a **family** of
observables. The Jones polynomial is the $N = 2$ member.

### 2c. The Markov trace class has $z$ as a field, not derived

From `HnMarkovTrace.lean`:
```lean
class MarkovTraceTower (q : ℝ) where
  z : ℝ
  z_pos : 0 < z
```

The $z$ is a **field of the class**, not a `def` computed from $q$.
The constraint is only `z_pos`. This is consistent with $z$ being
a free parameter.

## 3. Assessment

### 3a. If $N = 2$ is DERIVED (forced by Descartes)

Then the eightfold way **cannot** use $N = 3$ from the same Hecke
machinery. Flavor $\mathrm{SU}(3)$ must come from a genuinely different
construction (multi-fibre groupoid, octonionic $G_2$, etc.). This is
the position the current chapter takes.

### 3b. If $N = 2$ is CHOSEN (the Ocneanu parameter is free)

Then setting $a = q^2$ (i.e. $N = 3$) in the Ocneanu trace immediately
gives a $\mathfrak{gl}_3$-weighted link invariant, and the eightfold-way
multiplets follow by Schur-Weyl duality. The cost: all mass predictions
change (they were computed at $N = 2$). The question becomes: does the
$N = 3$ specialization reproduce the **same** mass ratios, or does it
break them?

### 3c. The honest middle ground

The most likely answer: $N$ is constrained **differently** in different
contexts:
- In the **mass pipeline**: $N = 2$ is required to reproduce $m_\mu/m_e$
  (because the $V_{(2,1)}$ representation governs the figure-eight knot
  operator, and dim $V_{(2,1)} = N - 1 = 1$ at $N = 2$... wait, that's
  wrong. dim $V_{(2,1)} = 2$ regardless of $N$ for $n = 3$ strands).

Actually: the irreducible dimensions in Schur-Weyl duality **do**
depend on $N$. At $N = 2$: dim $V_{(2,1)}^{\mathfrak{gl}_2} = 2$.
At $N = 3$: dim $V_{(2,1)}^{\mathfrak{gl}_3} = 8$. The mass pipeline
uses 2×2 matrices on $V_{(2,1)}$. Changing to $N = 3$ would require
8×8 matrices and different eigenvalues.

**Conclusion:** The mass pipeline is structurally tied to $N = 2$
(2-dimensional standard representation $V_{(2,1)}$). Setting $N = 3$
would not merely re-weight the same eigenvalues — it would change
the representation dimension and the operator structure entirely.
This is a **soft constraint** on $N = 2$: not a theorem, but a
structural compatibility.

## 4. Recommendation

1. **Do not claim** $N = 2$ is forced by the Descartes condition
   alone — the Ocneanu parameter is a separate degree of freedom.
2. **Do not claim** $N = 3$ is freely available — the mass pipeline's
   structural dependence on $V_{(2,1)}^{\mathfrak{gl}_2}$ (dim 2)
   would break.
3. **State as open:** the relationship between the Descartes-forced
   dim $V = 2$ and the Ocneanu parameter $a = q^{N-1}$ is not
   established. A Lean proof that the mass pipeline uniquely selects
   $N = 2$ (or that $N = 3$ is compatible) would resolve this.
4. **The Gavrilik test (TG)** is relevant: if the $N = 3$ Ocneanu
   trace at $q = q_0$ reproduces mass sum rules, that's evidence for
   $N = 3$ compatibility. If it doesn't, that's evidence for $N = 2$
   lock-in.
