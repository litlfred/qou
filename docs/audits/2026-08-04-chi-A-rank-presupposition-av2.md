# AV-2 complement: where $N=2$ enters, and why the "middle ground" is a hazard

**Date:** 2026-08-04
**Branch:** `claude/eightfold-way-a2-lattice-ijoegv`
**Bean:** `qou-w5fw` (T3f / AV-2), epic `qou-8lxd`
**Companion:** [`2026-08-04-ocneanu-trace-parameter-audit.md`](2026-08-04-ocneanu-trace-parameter-audit.md)
(branch `claude/eightfold-tg-t3f-2026-08-04`)

This was derived **independently and in parallel** with the companion audit,
by a different route, before either was aware of the other. Per
`AGENTS.md` §"Parallel exploration", the converging route re-scopes to
*verify / extend* rather than re-derive. That is what this document does.

## 0. Independent confirmation of the core

Both routes reached the same conclusion: **the Descartes condition does not
force the Ocneanu/Markov trace parameter.** The fibre gauge group and the
trace parameter are different objects, and $\chi(\mathcal A) = -6$
constrains the first, not the second. Two independent confirmations of an
open result are worth more than one; the core is not in dispute.

The companion's evidence is **stronger than mine** on the freedom side, and
is adopted here rather than restated:

- `HnMarkovTrace.lean` declares `z` as a **class field** with only
  `z_pos : 0 < z` — not a `def` computed from `q`. Machine-checkable
  evidence that `z` is free.
- `archimedean-image-table-table1-data.md` already writes HOMFLY-PT as the
  **family** $\{P(K; q_0^{N-1}, h_q)\}_{N \ge 2}$ — the corpus itself treats
  $N$ as a free index.
- The mass pipeline uses $z = 1/(q^{1/2}+q^{-1/2})$, the Jones ($N=2$) point.

This document contributes four things the companion does not have.

## 1. The insertion point — the exact line where $N=2$ enters

The companion establishes that $N$ is *free somewhere*. It does not locate
where the framework *fixes* it. That line is in
[`substrate-parameter-brings.md`](../../content/quantum-observable-universe/quantum-observable-universes/substrate-parameter-brings.md):

> "The Euler characteristic constraint $\chi(A) = -6$ **fixes the quantum
> dimension** $[2]_q = q + q^{-1} = -6$."

$\chi(A) = -6$ is a **topological integer** (Bring genus 4,
$\chi = 2-2g$). $[N]_q$ is a **rank-dependent expression**. Setting
$\chi(A) = [2]_q$ inserts $N=2$ by hand at exactly this point. Everything
downstream — $q = -3+2\sqrt2$, the Jones specialisation, the $\dim V = 2$
cap — descends from this one identification.

Locating it matters: it is the single line a future derivation must either
justify or replace.

## 2. A passage that looks like a derivation and is not

`substrate-parameter-brings.md` opens with two facts that appear to
independently force $N=2$. **Neither does:**

| stated | why it does not discriminate |
|---|---|
| $V \otimes V \cong V_1 \oplus V_0$ (two summands) | at $N=3$, $\mathbf3\otimes\mathbf3 = \mathbf6\oplus\bar{\mathbf3}$ is **also** two summands |
| "$R$-matrix eigenvalues are $q$ and $-q^{-1}$" | two eigenvalues **is** the Hecke relation $(\sigma-q)(\sigma+q^{-1})=0$ — true for **every** $N$ |

So the opening of that block reads as a derivation of rank 2 and supplies no
rank information at all. This should be said explicitly in the paper, because
a reader (and an agent) will take it as support.

## 3. The arithmetic at $N=3$ — and the brakes on it

Reading the *same* constraint at $N=3$ is consistent and solvable:

$$
  [3]_q = q^2+1+q^{-2} = -6
  \;\Longrightarrow\; q^2+q^{-2} = -7
  \;\Longrightarrow\; (q+q^{-1})^2 = -5
  \;\Longrightarrow\; q = \pm i\,\varphi^{\pm2}.
$$

Verified exactly: $|q| \in \{2.618034,\, 0.381966\} = \{\varphi^2,
\varphi^{-2}\}$, $[3]_q = -6 + 0i$ at all four roots.

| reading | $q$ | character |
|---|---|---|
| $\chi(A) = [2]_q$ (corpus) | $-3+2\sqrt2 = -(\sqrt2-1)^2$ | **silver**, real |
| $\chi(A) = [3]_q$ | $\pm i\varphi^{\pm2}$ | **golden**, imaginary |

QOU's substrate is icosahedral (Bring, $S_5/A_5$, golden ratio throughout);
the $N=2$ reading returns a silver-ratio number appearing nowhere else in
the corpus.

**Three brakes, applied to my own finding:**

1. **$\varphi$ is not evidence.** It follows from the discriminant being
   $-5$, which follows from $\chi=-6$. Nothing independent predicted it — at
   $\chi=-4$ the same computation returns $i\sqrt3$. The output tracks the
   input. This is a *signature to test*, not a result.
2. **Do not use the $n \mid 6$ divisibility of
   [`skein-resolution-obstruction.md`](../../content/quantum-observable-universe/braids-and-knots/skein-resolution-obstruction.md)
   as support.** That $n$ is the Kummer / root-of-unity torsion modulus and
   is **not proved equal to the Schur–Weyl rank**. Treating "$3\mid6$" as
   licensing $N=3$ would be the third index/group-name homonym error in this
   line of work, after Gemini's `1803.04009` SU(3) and the corpus's Elliott
   SU(3).
3. **Purely-imaginary $q$ is fibre-level only.** No bridge to the observable
   level ($\mathrm{Im}(q_0)=0$) exists and none is claimed.

## 4. The companion's $\dim V_{(2,1)}$ lock — verified, and re-scoped

The companion's §3c contributes a constraint this route did not find: the
mass pipeline acts by $2\times2$ operators on $V_{(2,1)}$, and

$$
  \dim V_{(2,1)}^{\mathfrak{gl}_2} = 2,
  \qquad \dim V_{(2,1)}^{\mathfrak{gl}_3} = 8,
  \qquad \dim V_{(2,1)}^{\mathfrak{gl}_4} = 20 .
$$

**Verified here independently** (hook-content formula, exact integers). The
claim stands: moving to $N=3$ does not re-weight the same eigenvalues, it
changes the representation dimension and the operator structure.

**But the companion's reading of this as a "soft constraint on $N=2$"
over-reads it.** HOMFLY-PT is *one* object and $N$ is an evaluation index —
the corpus's own $\{P(K;q_0^{N-1},h_q)\}_{N\ge2}$ framing. So the two
statements do not compete:

> $N=2$ and $N=3$ are **two evaluations of one trace**, not two rival claims
> about one evaluation. The mass pipeline reads at $N=2$; a
> $\mathfrak{gl}_3$ multiplet structure would read at $N=3$. Nothing forces
> a choice between them.

That dissolves the apparent conflict — and immediately raises a worse
problem, which is the real contribution of this section.

## 5. The hazard: per-observable $N$ is an extra free parameter per observable

If each observable is permitted to select its own $N$, the framework gains
**one free integer per observable** and becomes correspondingly less
falsifiable. That is strictly worse than the current situation, in which
$N=2$ is at least uniform. Under the three-calibration discipline and
`AGENTS.md` §"Axiomatization is NOT a Proof", "read it at whichever $N$
works" is an **anti-fit violation**, not a resolution.

So the middle ground the companion proposes (§3c, "$N$ is constrained
differently in different contexts") is **admissible only with a rule**:

> **Gate.** A per-context $N$ is acceptable only if something *independent of
> the observable being predicted* fixes $N$ in that context. Absent such a
> rule, $N$ must stay uniform, and $N=2$ stands by default — not because it
> is derived, but because varying it is unfalsifiable.

This is the honest state, and it is narrower than either "derived" or
"chosen".

## 6. Net verdict and next step

- **Not derived.** The $\chi(A) = [2]_q$ identification (§1) inserts the
  rank; the surrounding text (§2) does not supply it. Scope-(a).
- **Not freely available either.** The $\dim V_{(2,1)}$ structure (§4) means
  $N=3$ is a *different evaluation*, not a drop-in — and §5 forbids picking
  $N$ per observable without an independent rule.
- **Genuinely open**, agreeing with the companion, with the disagreement
  confined to §4–§5: the lock is not a soft constraint on $N$, it is a
  demand for a *selection rule*.

**Next step** (bean `qou-mcwm`, T3h): the decisive test is not more algebra
on $\chi(A)$ — it is whether the Markov loop value $z$ is pinned numerically
anywhere in the corpus **without assuming $N$** ($F_{\mathrm{Bor}}$, the
$[3]_q!$ factor, `tr_M` witnesses). If some witness fixes $z$ independently,
that pins the rank and closes the question. That is a compute audit, not a
derivation, and it is the cheapest remaining move.
