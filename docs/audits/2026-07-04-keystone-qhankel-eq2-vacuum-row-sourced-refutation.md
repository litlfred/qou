# Keystone value map (s013): the E_q(2) q-Hankel vacuum row refuted — the last disciplined q-Bessel form, fully sourced

**Date:** 2026-07-04
**Bean:** [`s013`](../../.beans/s013--keystone-value-map-colored-lawrence-rozansky-s-mat.md)
**Follows:** [`2026-07-04-keystone-qbessel-tricomi-c0q-sourced-refutation.md`](2026-07-04-keystone-qbessel-tricomi-c0q-sourced-refutation.md) and [`2026-07-04-keystone-valuemap-target-is-compact-hecke.md`](2026-07-04-keystone-valuemap-target-is-compact-hecke.md) (PR #3292)
**Source (owner upload, decisive):** `library/arxiv-1208.2521v1/1208.2521v1.pdf` — Koornwinder T.H., Swarttouw R.F., "On q-analogues of the Fourier and Hankel transforms", arXiv:1208.2521 = *Trans. Amer. Math. Soc.* **333** (1992) 445–461. Eq. (1.2) + the Hansen–Lommel orthogonality (roots of $C_\alpha(q;\mu)=0$ over the q-lattice) — the Plancherel kernel that #3292's open ask named.
**Script:** [`computations/probes/keystone_qhankel_eq2_vacuum_row.py`](../../computations/probes/keystone_qhankel_eq2_vacuum_row.py)
**Witness:** [`computations/probes/keystone-qhankel-eq2-vacuum-row.witness.json`](../../computations/probes/keystone-qhankel-eq2-vacuum-row.witness.json)
**Status:** the single remaining disciplined form of redirect (ii) is now tested and **refuted (scope a)**, fully sourced. No fit; nothing wired.

## Why this is the decisive test

Two prior q-Bessel refutations were partial: the single-argument row (2026-07-02
§4) was un-sourced, and the 0th-order q-Bessel **Tricomi** $C_{0,q}$
(2026-07-04, `library/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf`) is the *confluent* q-Bessel — it lacks the
Gaussian factor $q^{k(k-1)/2}$ and therefore has no discrete orthogonality, so
it is **not** the Plancherel object. #3292 named the one form that would be
genuinely falsifiable and still unbuilt: the **E_q(2) vacuum row** — the values
of the *third (Hahn–Exton)* q-Bessel at nodes **fixed** by its q-Hankel
Plancherel measure — and the one source that supplies it, Koornwinder–Swarttouw
1992. The owner uploaded exactly that paper.

Its eq. (1.2) (Exton normalisation) is

$$
C_\alpha(q;x)=\frac{(1-q)^\alpha}{(q;q)_\infty}
\sum_{k\ge0} q^{k(k-1)/2}\,(q^{\alpha+k+1};q)_\infty\,
\frac{\bigl(-x(1-q)^2\bigr)^k}{(q;q)_k},
$$

with the Hansen–Lommel orthogonality holding at the roots
$\mu_1<\mu_2<\dots$ of $C_\alpha(q;\mu)=0$, over
$\int_0^1 f\,d_qx=(1-q)\sum_k f(q^k)q^k$. The roots $\mu_j$ **are** the
Plancherel nodes — 0 free parameters at fixed $q$. (Computed with the identity
$(q^{\alpha+k+1};q)_\infty=(q^{\alpha+1};q)_\infty/(q^{\alpha+1};q)_k$ so no
infinite product sits inside the k-loop.)

## The 0-dof test and its result

Target (PR #3292 FACT 1, at $q=q_0^{-1}\approx0.90092$):

$$d_q=\big([1]_q,[4]_q,[5]_q,[4]_q[3]_q/[2]_q\big)\approx(1,\,4.02727,\,5.05460,\,6.22044).$$

First positive roots $\mu_j$ of $C_\alpha$ for $\alpha\in\{0,\tfrac12,1,2\}$
(the natural labels; $\alpha=\tfrac12$ is the q-cosine specialisation KS
single out), and $C_\alpha$ at the q-lattice nodes $q^k$, give a
**112-candidate** parameter-free menu (ordered roots $\mu_j$, $\sqrt{\mu_j}$,
non-trivial normalisations $\mu_j/\mu_1$, $\sqrt{\mu_j/\mu_1}$, and lattice
values).

**No coherent realisation.** No single $(\alpha,\text{form})$ pair reproduces
the **ordered** 4-vector $d_q$ within 1% — `coherent_4vector_match: false`. Per
$\alpha$, the ratio vectors $\mu_j/\mu_1$ are e.g.
$\alpha{=}2:\{1,2.68,5.08,8.18\}$, $\alpha{=}1:\{1,3.34,7.00,11.9\}$,
$\alpha{=}\tfrac12:\{1,3.99,8.95,15.8\}$ — the second entry can graze $[4]$ or
the third can graze $[5]$, but never both in one ordered vector, and the fourth
entry never approaches $[4][3]/[2]=6.220$.

**The scattered hits are menu coincidences.** Four single-index quantities fall
within 1% of a single target — `a1/2_mu_2/mu_1=3.991` vs $[4]=4.027$,
`a1_√(mu_6/mu_1)=5.046` and `a2_mu_3/mu_1=5.077` vs $[5]=5.055$,
`a2_√(mu_6/mu_1)=4.045` vs $[4]$ — but they come from **different** $\alpha$,
**different** root index $j$, and **different** functional form, and **no two
co-locate in the same ordered vector**. Across a 112-candidate menu against 3
targets with a ±1% window, a handful of one-index grazes is the expected chance
yield (the PSLQ/entropy caution: a large parameter-free menu will graze any
fixed value). They are recorded in the witness (`scattered_single_index_hits`)
as the sharpener, not as a realisation.

## Verdict — scope (a), sourced and decisive

**REFUTED-as-is (scope a):** the Plancherel-fixed non-compact E_q(2) vacuum row
(sourced Hahn–Exton $C_\alpha$, Koornwinder–Swarttouw 1992) does **not**
reproduce the compact quantum-dimension vector $d_q$ as an ordered realisation.
This is exactly what the compact/non-compact **type** argument (PR #3292 FACT 1)
predicts: a non-compact-group Plancherel object landing on a compact,
Laurent-polynomial (algebraic) target would be a coincidence, and at the
ordered-vector level it does not occur.

Per the STRICT "refuted" discipline this is **scope (a)**, not (b): it does not
prove *no* node/contraction convention can work (no invariant forbids it) — it
shows the natural Plancherel nodes of the sourced kernel do not. But it closes
the **last disciplined, still-testable** geometric/analytic form of redirect
(ii) that had a concrete in-repo source. All four geometric/analytic realisation
routes are now refuted with sources: $\Sigma(2,3,5)$ (golden, $D=2$),
$\Sigma(3,4,5)$ ($D=6$), colored Lawrence–Rozansky residues (pure $\pm1$ sign),
and the q-Bessel family (Tricomi + Hahn–Exton/q-Hankel, here).

## The standing value-step answer: the non-geometric "why" (redirect iii)

With the geometric realisation routes exhausted, the honest resolution of the
value step is **not** a deflation — it is the **compact, categorical "why"** that
does not need geometry at all:

$$
\frac{S_{0\lambda}}{S_{00}}=d_q(\lambda),
$$

the Verlinde vacuum-row identity for the SU_q(2)/Hecke modular category. The
non-circular content — *why this vector and not another* — is the
**Markov-trace uniqueness / Perron–Frobenius selection**: requiring the trace to
be a **Markov trace** (stable under adding a strand) forces the block weights to
be the **unique** positive solution, which is the normalised quantum-dimension
vector (Ocneanu; Wenzl). Equivalently $d_q$ is the Perron–Frobenius eigenvector
of the fusion/branching matrix — the unique positive ground state — and state
positivity is the corpus's own confinement-SDP PSD constraint. This "why" is
already in the corpus (`mass-theory/y-lambda-closed-form-wenzl-bridge.md`,
`wenzl-bridge-applicability-qou.lean`, `stochastic-mechanics/intro-markov-axioms-braid-link.md`)
and is categorical, not geometric. The geometric-realisation program (the
owner-reversed Subgoal-2 gate) was seeking a **redundant** second, geometric
"why"; its exhaustion does not leave the value step unexplained.
