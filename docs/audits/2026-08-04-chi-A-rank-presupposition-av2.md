# AV-2 verdict: $N=2$ is a reading of $\chi(A)$, not a derivation

**Date:** 2026-08-04
**Branch:** `claude/eightfold-way-a2-lattice-ijoegv`
**Bean:** `qou-w5fw` (T3f / AV-2), epic `qou-8lxd`
**Question:** is the Ocneanu/Markov trace parameter — equivalently the rank
$N$ of the Schur–Weyl partner — **derived** in QOU, or **chosen**?

**Verdict: chosen.** The Euler-characteristic constraint $\chi(A) = -6$ does
not determine $N$. It determines *one equation*; which equation depends on
which quantum dimension $\chi(A)$ is identified with, and that identification
presupposes the rank. Reading the same constraint at $N = 3$ is consistent,
solvable, and lands on the golden ratio exactly.

This **weakens** the conclusion of
[`2026-08-03-flavour-su3-schur-weyl-obstruction.md`](2026-08-03-flavour-su3-schur-weyl-obstruction.md)
§3b: the $\dim V = 2$ cap is downstream of a modelling choice, not of a
theorem.

## 1. What the corpus actually says

[`substrate-parameter-brings.md`](../../content/quantum-observable-universe/quantum-observable-universes/substrate-parameter-brings.md):

> "The Euler characteristic constraint $\chi(A) = -6$ **fixes the quantum
> dimension** $[2]_q = q + q^{-1} = -6$. Solving $q^2 + 6q + 1 = 0$ isolates
> the categorical parameter $q = -3 + 2\sqrt 2 \approx -0.172$."

and [`jones-markov-trace.lean`](../../content/quantum-observable-universe/braids-and-knots/jones-markov-trace.lean)
carries the Markov-trace **loop value** `z` as structure data.

The loop value of the Markov/Ocneanu trace *is* the quantum dimension of the
fundamental object, and for the $\mathfrak{gl}_N$ specialisation it is
$[N]_q$ (HOMFLY at $a = q^N$; Jones is the $N=2$ point). So the chain is

$$
  \text{genus }4\ (\text{Bring}) \;\Rightarrow\; \chi(A) = 2-2g = -6
  \;\xrightarrow{\ \text{identify } \chi(A) = [N]_q\ }\;
  q \;\Rightarrow\; \text{trace} \Rightarrow \text{invariant}.
$$

**$\chi(A) = -6$ is a topological integer. $[N]_q$ is a rank-dependent
expression. Writing $\chi(A) = [2]_q$ inserts $N = 2$ by hand.** Nothing
upstream of that line selects $N$.

## 2. The same constraint at $N = 3$

$$
  [3]_q = q^2 + 1 + q^{-2} = -6
  \;\Longrightarrow\; q^2 + q^{-2} = -7
  \;\Longrightarrow\; u^2 = -5, \quad u := q + q^{-1}.
$$

So $u = \pm i\sqrt 5$ and $q^2 - uq + 1 = 0$ gives

$$
  q \;=\; \pm i\,\frac{3 \pm \sqrt 5}{2}
  \;=\; \pm i\,\varphi^{\pm 2},
  \qquad \varphi = \tfrac{1+\sqrt5}{2}.
$$

Verified exactly: $|q| \in \{2.618034, 0.381966\} = \{\varphi^2,
\varphi^{-2}\}$, with $[3]_q = -6 + 0i$ in every case.

Side by side:

| reading | $q$ | character |
|---|---|---|
| $\chi(A) = [2]_q$ (corpus) | $-3+2\sqrt2 = -(\sqrt2-1)^2 \approx -0.1716$ | **silver** ratio, real |
| $\chi(A) = [3]_q$ | $\pm i\,\varphi^{\pm2}$, $\;\lvert q\rvert = \varphi^{\pm2}$ | **golden** ratio, purely imaginary |

## 3. Why this is interesting — and where to stop

**The interesting part.** QOU's substrate is *icosahedral*: Bring's curve,
$\mathrm{Aut} = S_5$, $A_5$, and golden-ratio structure throughout (e.g.
[`IcosahedralCharacterGoldenRatio.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/IcosahedralCharacterGoldenRatio.lean)).
The $N = 3$ reading returns $\varphi$ **exactly**; the $N = 2$ reading returns
a silver-ratio number with no other appearance in the corpus. And there is a
*candidate mechanism* rather than bare coincidence: $\chi = -6 \Leftrightarrow$
genus 4 $\Leftrightarrow$ Bring $\Rightarrow A_5 \Rightarrow \varphi$, so both
sides could trace to the same genus-4 structure.

**Where to stop — three disciplines, applied to my own finding.**

1. **$\varphi$ appearing is not evidence.** It arises because the discriminant
   is $-5$, which arises because $\chi = -6$. Nothing independent *predicted*
   $\varphi$ before the calculation. Until something does, this is a
   **signature to test**, not a result. (At $\chi = -4$ the same computation
   would give $u = i\sqrt3$; the output tracks the input.)
2. **Do not reuse the divisibility condition as support.**
   [`skein-resolution-obstruction.md`](../../content/quantum-observable-universe/braids-and-knots/skein-resolution-obstruction.md)
   says the obstruction vanishes for $n \mid 6$, so $n \in \{1,2,3,6\}$ and
   $N=3$ is *not excluded* there. But that $n$ is the **Kummer / root-of-unity
   torsion modulus**, and it is **not proved equal to the Schur–Weyl rank**.
   Treating "$3 \mid 6$" as licensing $N=3$ would be the third
   group-name/index homonym error of this line of work — after Gemini's
   `1803.04009` SU(3) and the corpus's Elliott SU(3). Recorded so nobody
   makes it.
3. **Purely-imaginary $q$ is fibre-level only.** Per `AGENTS.md`
   §"Im(q) at fibre vs observable level", $\mathrm{Im}(q)$ is unconstrained on
   the fibre but the archimedean evaluation needs $\mathrm{Im}(q_0)=0$. The
   corpus already separates these — $q = -3+2\sqrt2$ is called the
   *categorical* parameter, distinct from the physical $q_0 \approx 1.1099$.
   So $q = i\varphi^2$ is *permitted* at fibre level, but **no bridge to the
   observable level exists**, and none is claimed here.

**Scope.** This is a **scope-(a)** finding: it shows the $N=2$ cap is
*not established*, not that $N=3$ is correct. Nothing here is wired to any
production compute.

## 4. What changes

- [`2026-08-03-flavour-su3-schur-weyl-obstruction.md`](2026-08-03-flavour-su3-schur-weyl-obstruction.md)
  §3b said the single-fibre tower is "hard-capped at $N=2$" by a *derivation*.
  Corrected: it is capped by an **identification**, which is revisable. §3a
  (Elliott homonym) and §3c (icosahedral $T_1$ fails the $\mathrm{Sym}^2$
  gate) are untouched — those remain scope-(b).
- The forecast changes: flavour/colour $\mathrm{SU}(3)$ no longer needs an
  *inter-universe* construction as a matter of necessity. It needs the rank
  question settled, which is a much smaller and more tractable target.

## 5. Next

The decisive follow-up is **not** more algebra on $\chi(A)$ — it is to find
what, if anything, independently selects the rank. Two concrete tests:

1. **Does $V\otimes V \cong V_1 \oplus V_0$ force $N=2$?**
   `substrate-parameter-brings.md` opens with that decomposition, and a
   two-summand $V^{\otimes2}$ is the $\mathfrak{sl}_2$ signature ($N=3$ would
   give $\mathbf 3\otimes\mathbf 3 = \mathbf 6\oplus\bar{\mathbf 3}$, also two
   summands — so **this does not discriminate**, and the $R$-matrix having two
   eigenvalues $q, -q^{-1}$ is the *Hecke* relation, true for every $N$).
   Worth stating explicitly, because it looks like a derivation and is not.
2. **Is the loop value independently measurable in the corpus?** If any
   computed Markov-trace normalisation (Borromean $F_{\mathrm{Bor}}$, the
   $[3]_q!$ factor, $\mathrm{tr}_M$ witnesses) pins $z$ numerically without
   assuming $N$, that pins the rank. This is a witness-level check, not a
   derivation, and it is the fastest way to close the question either way.

Test 1 is a paper-level clarification; test 2 is a compute audit. Both are
cheap relative to what they settle.
