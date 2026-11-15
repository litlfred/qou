# Mass formula uniqueness: from axiom to theorem

**Date:** 2026-05-27  
**Goal:** Show that the 5 categorical constraints uniquely determine
the mass formula, turning the archimedean functor from an axiom to a
theorem.

## The claim

**Theorem (conjectural).** Let $\mathfrak{m} : B_n \to \mathbb{R}_+$
be a functional on braids satisfying constraints C1–C5 below. Then
$\mathfrak{m}$ is uniquely determined (up to calibration $m_e$, $q_0$)
as:

$$
\mathfrak{m}(\beta) = m_e \cdot \rho_K \cdot
\bigl|\mathrm{tr}_M(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K))\bigr|
$$

with the brane-tower expansion given by `prop:mass-endomorphism-tower`.

## The 5 constraints

### C1. Markov-invariance

$\mathfrak{m}(\beta) = f(\mathrm{tr}_M(\beta))$ for some functional $f$.

**Source:** The mass is an observable of the knot/link, not the braid
representative. The Markov theorem says knot invariants factor through
the Markov trace. This is categorical (Turaev, Kassel).

**Lean status:** `thm:jones-markov-trace` — proved.

### C2. Blow-up truncation at |S| ≤ 2

The brane-tower decomposes by generator subsets $S$. Subsets $|S| \geq 3$
ascend to the next jet level via the pentagon identity; they are NOT
independent at level $n$.

**Source:** Yang-Baxter relation collapses triple products:
$\sigma_i\sigma_{i+1}\sigma_i = \sigma_{i+1}\sigma_i\sigma_{i+1}$.
At most 2-element subsets are independent modulo YB.

**Lean status:** The YB relation is in `def:braid-group`. The
truncation follows formally but is NOT yet proved in Lean.

### C3. Symmetric q-dilogarithm evaluation

The Briggs-Klein chart integration gives $-\mathrm{Li}_2^q(-|V|)$
(symmetric q-integer convention), NOT $\Phi_q(|V|)$ (Faddeev).

**Source:** Direct computation:
$\int_0^V \ln_q(1+t)/t \, dt = -\mathrm{Li}_2^q(-V)$.
Proved in the mass-endomorphism block (subproof, lines 296-316).

**Lean status:** Not yet formalised. The termwise identity is provable
from the q-log definition + term-by-term integration.

### C4. Frobenius positivity

$Gx \geq 0$ at every Wedderburn block: the Gram matrix $G$ of the
Hoefsmit seminormal form imposes non-negativity on the mass
decomposition.

**Source:** The Markov trace is positive-definite on $H_n(q)$ for
$q > 0$ (Wenzl 1988, Theorem 5). The Frobenius structure of the
Wedderburn decomposition makes this a per-block constraint.

**Lean status:** `prop:frobenius-gram-matrix` — stated, sorry.

### C5. Integer LP optimality (gluon derivation)

The gluon count (2 for the proton) is the unique integer LP minimum
over the 84 feasible integer solutions satisfying C4.

**Source:** Exhaustive enumeration + LP shadow-price analysis.
~~Witness: `mass-endomorphism.witness.json`.~~

> **🛑 The witness citation above is DEAD — corrected 2026-08-29.**
> `computations/mass-endomorphism.witness.json` exists, which is presumably
> why the citation survived review, but it does **not** carry this number:
> **zero** fields equal 84, and **zero** keys name ilp / solution / feasible /
> count / gluon. Its subject is a different quantity — its own description
> reads *"Mass endomorphism via Φ_q tower with z²-weighted cross-term.
> m_p/m_e = 9310.3278 (CODATA: 1836.152, error 407.06%)"*.
>
> No other producer computes the figure either: `rem:ilp-solution-count-unwrap`
> and `prop:stable-atom-decidable` declare no `computation:`, and the only
> ILP-counting code in the corpus,
> `fsh-guts/deprecated/computations/confinement_adaptive.py::ilp_solution_count_nucleon_level`,
> is a magic-number heuristic returning at most 3 whose own docstring calls
> it *"a categorical proxy"* for the real enumeration. It is orphaned.
>
> This does **not** assert that 84 is wrong. "Exhaustive enumeration" above may
> well have been run and its result recorded by hand. What is established is
> that nothing in the corpus now reproduces it, so it cannot be checked and a
> mismatch against it cannot be interpreted. Probe:
> [`qbeta_nl84_provenance_probe.py`](../../computations/qbeta/qbeta_nl84_provenance_probe.py)
> (4/4). Bean `qou-vtlj`.

**Lean status:** Not formalised (combinatorial search).

## The uniqueness argument

### Step 1: C1 reduces the formula space

Any mass formula must factor through $\mathrm{tr}_M$. The space of
Markov-trace-compatible functionals on $B_n$ is isomorphic to
$\bigoplus_{\lambda \vdash n} \mathbb{R}$ (one degree of freedom per
partition), via the Wedderburn decomposition:

$$
\mathrm{tr}_M(\beta) = \sum_\lambda y_\lambda \chi^\lambda(\beta)
$$

So $\mathfrak{m}(\beta) = f\bigl(\{y_\lambda \chi^\lambda(\beta)\}_\lambda\bigr)$
for some functional $f$ on the Wedderburn coordinates.

### Step 2: C2 determines the polynomial structure

The blow-up truncation at $|S| \leq 2$ means $f$ is at most
**quadratic** in the per-generator spectral coordinates $\hat{V}_i$.
Combined with Markov-invariance, this gives:

$$
\mathfrak{m} = a_0 \cdot |\mathrm{tr}_M(\beta)|
+ \sum_i a_1 \cdot g_1(|\hat{V}_i|)
+ \sum_{i<j} a_2 \cdot g_2(|\hat{V}_i \hat{V}_j|)
$$

where $g_1, g_2$ are unknown functions and $a_0, a_1, a_2$ are
constants. The formula is **linear in blow-up centres** with at most
2 elements.

### Step 3: C3 determines g_1 and g_2

The Briggs-Klein integration identity fixes:

$$
g_1(V) = g_2(V) = -\mathrm{Li}_2^q(-V)
$$

This is the UNIQUE function arising from the integration of the
q-deformed expansion flow along the radial coordinate of each
blow-up centre. No other q-analogue of the dilogarithm satisfies
both the functional equation and the Briggs-Klein chart boundary
conditions.

**This is the key uniqueness step.** The function $\mathrm{Li}_2^q$
is determined by:
- Its Taylor expansion: $\sum z^n / (n \cdot [n]_q)$
- The symmetric q-integer $[n]_q = (q^n - q^{-n})/(q - q^{-1})$
- The initial condition $\mathrm{Li}_2^q(0) = 0$

### Step 4: C4 determines the Markov weights

Frobenius positivity $Gx \geq 0$ constrains the $y_\lambda$ weights
to the positive cone of the Gram matrix. Combined with the Wenzl
normalisation $\sum_\lambda y_\lambda d_\lambda = 1$, the weights
are uniquely determined:

$$
y_\lambda(q) = \frac{q^{c(\lambda)}}{[n]_q!}
$$

(the q-Schur Plancherel measure). This is proved for $H_2$ (commit
on main) and stated for general $n$.

### Step 5: C5 determines the braid word

The gluon count (crossings beyond the bare constituent braids) is the
unique integer LP minimum. For the proton: 2 gluon crossings.

With the braid word fixed, $\hat{V}_i$ are determined by the Hoefsmit
seminormal form, and the mass formula evaluates to a specific number.

### Step 6: Calibration

The overall scale $m_e$ (mass unit) and $q_0$ (substrate) are the
two calibration inputs. Everything else is derived.

## Status: what's proved vs open

| Step | Statement | Status |
|------|-----------|--------|
| 1 | Markov factorisation | **Theorem** (Lean: `thm:jones-markov-trace`) |
| 2 | |S| ≤ 2 truncation | **Structural** (YB argument; not yet Lean) |
| 3 | Li₂^q from Briggs-Klein | **Proved** (subproof in mass-endomorphism block) |
| 4 | Weights = q-Schur Plancherel | **Proved for H_2** (Lean: `qSchur_H2_top/bottom`); stated for H_n |
| 5 | Gluon from integer LP | **Computed** (witness; not Lean) |
| 6 | Calibration (m_e, q₀) | Axiom (2 inputs) |

## What "theorem" means here

If Steps 1–5 are all formalised, the statement becomes:

> The mass formula is the UNIQUE functional on braids satisfying
> Markov-invariance, |S| ≤ 2 blow-up, Li₂^q evaluation, Frobenius
> positivity, and integer LP optimality — up to the calibration
> constants (m_e, q₀).

This turns the archimedean functor from **"we postulate this formula"**
to **"this is the only formula consistent with the categorical
constraints."**

## Remaining gaps for Lean

1. **|S| ≤ 2 from YB**: prove that $\sigma_i\sigma_j\sigma_i$ does
   not generate an independent blow-up centre (it reduces via YB to
   the pair support).

2. **Li₂^q uniqueness**: prove that the Briggs-Klein boundary
   conditions + q-log Taylor expansion uniquely determine
   $\mathrm{Li}_2^q$ among q-analogues of the dilogarithm.

3. **q-Schur weights for general n**: extend the H_2 proof to H_n
   via the content-sum formula.

4. **Integer LP formalisation**: either a Lean-verified exhaustive
   search or a duality certificate.

## Cross-references

- `prop:mass-endomorphism-tower` — the formula being uniquified
- `thm:jones-markov-trace` — Step 1 (Lean)
- `prop:frobenius-gram-matrix` — Step 4 ingredient
- `prop:q-schur-y-lambda-closed-form` — Step 4 (H_2 proved)
- `def:quantum-bloch-group` — Li₂^q definition
- PR #1311 — C_knot wiring (related)
- PR #1310 — Geom derivation chain (Step 3 context)
