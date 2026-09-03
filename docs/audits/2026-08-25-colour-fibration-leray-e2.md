# The Serre–Leray spectral sequence of the colour fibration does not supply an N = 3

**Bean:** `qou-ken6` (parent `qou-8lxd`, the eightfold epic).
**Probe:** [`computations/eightfold/colour_fibration_leray_e2_probe.py`](../../computations/eightfold/colour_fibration_leray_e2_probe.py) — exact sympy over ℚ(z), no floats.
**Date:** 2026-08-25.

## The question

Owner prompt: *"we have fibration and serre-leray spectral sequence — check corpus"*.

The bean asked it sharply. The Sym² parity exclusion (merged, `b457b8ad57`) is a
statement about **objects of the single-fibre tensor category**: any such object
passing the gate has even vector-space dimension, so none is 3-dimensional. A
fibration's total space is assembled from base *and* fibre, so it is not
obviously an object of that category, and the exclusion does not obviously apply
to it. The Serre–Leray spectral sequence is precisely the machine that computes
the total space from the two — and the corpus's colour fibration already carries
a three-dimensional colour space $\mathbb{A}^3$.

That is a shape match, which is exactly what the anti-laundering discipline
exists to catch. This audit runs the first concrete step the bean asked for:
write down $E_2$ from objects the corpus can actually supply, and see what comes
out.

## Answer, up front

**It does not supply a 3.** The fibration's representation-theoretic content is
the monodromy $\pi_1(B^\circ) \to \mathrm{SL}(2,\mathbb{Z})$ acting on
$H^1(\text{fibre}) = \mathbb{Z}^2$. That is **rank 2** — the same 2 the
framework already has. And the alternative reading, in which the three colours
$r,g,b$ are taken as a triple, gives the $S_3$ *permutation* representation,
which is self-dual and **already excluded** in the corpus.

Both readings land on results the corpus already has.

## 1. What the fibre actually is

The corpus was genuinely ambiguous here, and resolving it was the first real
step. `brings-surface/color-tube-interpretation.md` describes a curve inside the
colour space $\mathbb{A}^3$ with $c = (c_r, c_g, c_b)$; read naively as *"a cubic
in one variable"* the fibre would be **three points**, and everything below would
collapse. It is not: `brings-surface/t-duality-elliptic.md` gives the fibration
its Weierstrass form and the fibre is an **elliptic curve**.

The probe verifies the corpus's own two shifts symbolically, from the cubic in
`QOU.ColorTubeFibers`:

$$
c^3 + (4z+1)c^2 + (6z^2+3z+1)c + (4z^3+3z^2+2z+1) = 0 .
$$

* Shift 1, $X = c + z$ (`color-tube-fibers.lean`): leaves the $X^2$ coefficient
  **non-zero**, so this shift alone does *not* depress the cubic.
* Shift 2, $X = t - (z+1)/3$ (`t-duality-elliptic.md`, `eq:weierstrass-depressed`):
  gives $t^3 + p(z)\,t + q(z)$ with

$$
p(z) = \frac{2z^2+z+2}{3}, \qquad
q(z) = \frac{5\,(4z^3+3z^2+3z+4)}{27},
$$

  which **reproduces the corpus's published $p(z)$ and $q(z)$ exactly** (both
  checks return `True`).

The discriminant $\Delta(z) = -4p^3 - 27q^2$ has degree 6 in $z$ and is **not
identically zero**, so the generic fibre is a *smooth* genus-1 curve, singular
only over the finitely many roots of $\Delta$.

A genus-1 curve has $H^0 = \mathbb{Z}$, $H^1 = \mathbb{Z}^2$, $H^2 = \mathbb{Z}$.
**The rank that the fibration's cohomology makes available is 2.**

## 2. The $E_2$ page, and why the sequence degenerates

Over the smooth locus $B^\circ = \mathbb{P}^1 \smallsetminus \Delta^{-1}(0)$ the
map *is* a fibration, so the Serre spectral sequence applies. $B^\circ$ is an
open Riemann surface — homotopy equivalent to a wedge of $k-1$ circles for $k$
punctures — so

$$
H^0(B^\circ) = \mathbb{Z}, \quad H^1(B^\circ) = \mathbb{Z}^{k-1}, \quad
H^p(B^\circ) = 0 \ \ (p \ge 2).
$$

Hence $E_2^{p,q} = H^p(B^\circ; \mathcal{R}^q)$ is supported in $p \in \{0,1\}$
only. The differential $d_r : E_r^{p,q} \to E_r^{p+r,\,q-r+1}$ has target at
$p+r \ge 2$ for $r \ge 2$, where every group vanishes; any $d_r$ *into* $(p,q)$
has source at $p-r \le -1$, likewise zero. So

$$
\textbf{all } d_r \textbf{ vanish for } r \ge 2 \implies E_2 = E_\infty .
$$

**The sequence degenerates for dimension reasons, before any QOU input is used.**
It contributes no differential, no extension problem beyond a single short exact
sequence, and no new object.

*Honest caveat on scope.* This is the **Serre** SS over the smooth locus. If one
instead takes the **Leray** SS of the map over all of $\mathbb{P}^1$, with the
constructible sheaves $R^q f_* \mathbb{Z}$, then $H^2(\mathbb{P}^1) \ne 0$ and a
$d_2 : E_2^{0,1} \to E_2^{2,0}$ *may* be non-zero. That variant is not
degenerate, and this audit does not claim it is. It does not change the
conclusion: the rank of $H^1$ of the fibre is 2 either way, and a differential
can only *reduce* what survives to $E_\infty$, never manufacture a rank-3
summand that was not present on $E_2$.

## 3. The other reading, and why it is already dead

One could ignore the cohomology and read the three colours $r,g,b$ — the three
coordinates of the ambient $\mathbb{A}^3$, equivalently the three roots of the
cubic — as the missing triple directly. The bean flagged this in advance as the
dimension-vs-object conflation the epic keeps having to retract, and it is.

Concretely: the root-permutation action gives the $S_3$ **permutation**
representation. Every permutation representation is self-dual — the permuted
basis is orthonormal for an invariant symmetric form — so its Frobenius–Schur
indicator is $+1$, $\mathrm{Sym}^2$ carries a singlet, and it **fails the Sym²
gate** for exactly the reason the SU(2) adjoint does. $S_3 = W(A_2)$ supplies the
*Weyl group* of the weight lattice, not the fundamental representation.

This is already established in the corpus:
[`docs/audits/2026-08-07-eightfold-live-surface-collapse.md` §4](2026-08-07-eightfold-live-surface-collapse.md)
records it as T3g §4 ("the naive route is dead").

## 4. Scope of the refutation

Per the AGENTS.md (a)/(b) discipline:

* **Scope (b), structural exclusion, with the invariant named.** *The
  Serre–Leray spectral sequence of the colour fibration cannot supply a rank-3
  object.* The invariant is a rank bound: $H^1$ of a genus-1 curve has rank 2,
  and an open Riemann surface has cohomological dimension 1, so $E_2$ (and,
  under the Leray variant, any $E_\infty$ subquotient of it) carries no rank-3
  summand. This is a bound, not a failed numerical fit.
* **Scope (a) only, NOT claimed as (b).** Nothing here excludes *fibrations in
  general*, other fibrations in the corpus (Seifert $S^3/2I \to S^2(2,3,5)$,
  Hopf $S^3 \to S^2$, the Reeb bundle), or groupoid-level structure as the source
  of $N = 3$. The bean's framing — that the Sym² exclusion is about single-fibre
  objects and something assembled from base *and* fibre might evade it — remains
  a live idea. This audit reports that the **colour** fibration, the one that
  looked most promising because it carries a visible three, does not do it.

## 5. Two findings on the existing spectral-sequence infrastructure

Recorded as findings, not fixed here — they touch
`QOU/Mathlib/SpectralSequence.lean`, which is another area's file, and neither
is caused by this work.

1. **The structure does not carry the $d \circ d = 0$ requirement its docstring
   claims.** The docstring says the pages are *"equipped with differentials $d_r$
   and the requirement $d_r \circ d_r = 0$"*. There is no such field. The only
   thing in the file resembling it is `trivial_d_squared_zero`, which holds for
   `PUnit` by `rfl`. Cells are bare `Type u` with no module structure, so the
   condition is not even statable as written.
2. **`GBFiltrationCollapsesAtE2 R` is always inhabited.** `instance canonical`
   supplies the trivial `PUnit` sequence, so every
   `[GBFiltrationCollapsesAtE2 R]`-conditional theorem downstream is conditional
   on nothing — the hypothesis can never fail. This is the failure mode
   AGENTS.md §3b-tax targets ("the carrier must assert something"): a class that
   can be discharged trivially does not make its consumers conditional results.

Neither undermines any claim in this audit — this work instantiates no Lean API;
it settles the geometry. They matter for anyone who reads
`CollapsesAt`-conditional statements in the corpus as carrying content.

## 6. Provenance

Everything in §1 is exact: sympy polynomial identities over $\mathbb{Q}(z)$, no
floating-point arithmetic anywhere, per AGENTS.md *"PROBES ARE NOT EXEMPT"*. The
probe exits non-zero if either corpus-agreement check fails.
