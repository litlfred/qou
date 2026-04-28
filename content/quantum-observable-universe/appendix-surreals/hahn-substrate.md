The substrate parameter $q \in \mathbb{R}_{>0}$ in QOU controls
all $q$-deformed structures (Hecke algebra, $q$-Schur--Weyl,
quantum dimensions, etc.). Its archimedean value $q_0 \approx
1.1097$ is the substrate parameter at which the categorical mass
formula reproduces CODATA particle masses to $\sim 4\%$ MAE.

Under a surreal lift, one can ask: what is the natural ambient
*ring* in which $q$ should live? The conjecture: a **Hahn series
ring over $\mathbf{No}$ with infinitesimal indeterminate
$\varepsilon$**.

## Setup

Recall the Hahn series construction [@ehrlich2012; @alling1987]:
given a divisible ordered abelian group $G$ and a field $K$, the
**Hahn series ring** is

$$
  K(\!(t^G)\!) \;:=\; \Bigl\{
    \sum_{g \in G} a_g \, t^g  \,\Bigm|\,
    a_g \in K,\;
    \mathrm{supp}(a) \subset G \text{ well-ordered}
  \Bigr\}.
$$

Multiplication is by formal Cauchy product. The series is *not*
required to converge in any topology; the well-ordered-support
condition makes products well-defined formally.

For $G = \mathbb{R}$ (with addition) and $K = \mathbb{R}$, the
ring $\mathbb{R}(\!(t^{\mathbb{R}})\!)$ embeds in $\mathbf{No}$
under $t \mapsto \varepsilon$, $t^r \mapsto \varepsilon^r$ for
real $r$ [@ehrlich2012]. Larger $G$ give larger sub-fields of
$\mathbf{No}$.

## Conjecture

The substrate parameter $q$ is naturally an element of the Hahn
series ring

$$
  q \;\in\; \mathbb{R}(\!(\varepsilon^{\mathbb{Q}})\!)
   \;\subset\; \mathbf{No}
$$

with leading expansion

$$
  q \;=\; 1 + \varepsilon + \alpha_2 \varepsilon^2 + \alpha_3
  \varepsilon^3 + \cdots,
$$

where $\alpha_2, \alpha_3, \ldots \in \mathbb{R}$ are *not free
parameters* but are determined by the requirement that
$\mathrm{St}(q) = q_0$ (matching the archimedean substrate value).

Equivalently: $q = 1 + \varepsilon$ is the *first-order
truncation*, and the higher-order $\alpha_k$ are determined by a
*surreal completion procedure*.

## Why this is interesting

In the simplest interpretation, $q = 1 + \varepsilon$
identically — and then $\alpha_k = 0$ for all $k$. This is the
"naïve" surreal lift, and it suffices for the algebraic-core
results.

The conjecture asserts a *richer* possibility: the higher-order
$\alpha_k$ are *non-trivial* and encode physical content beyond
the $\sim 4\%$-MAE archimedean fit. Under standard-part, all
higher-order terms vanish, so the archimedean theory is
unchanged. But within the surreal ambient, the $\alpha_k$ store
information that can refine predictions:

- $\alpha_2$ might encode the leading-order quantum correction
  to particle masses (a single-parameter shift).
- $\alpha_3, \alpha_4, \ldots$ might encode higher-order
  corrections systematically.

If determined by a constraint (e.g., requiring that the surreal
mass formula agrees with measurement to $1$ ppb rather than
$\sim 4\%$), the $\alpha_k$ become a *predictive* extension of
the QOU mass formula.

## Comparison: standard-model parameters

This is structurally analogous to a perturbation expansion in
the Standard Model. There, $\alpha_{\mathrm{em}} \approx 1/137$
is treated as a free parameter, and observables are computed as
power series in it. Here, $q_0 - 1 \approx 0.11$ is the
analogous expansion parameter, and the $\alpha_k$ are the
analogues of higher-order Standard Model coefficients.

The *novelty* in the surreal framing is that the expansion is
exact (Hahn series have no convergence requirement), and that
the leading term has a clean categorical interpretation
(substrate parameter as $1 + \varepsilon$, with $\varepsilon \in
\mathbf{No}$).

## Status

**Speculative**. The conjecture has two layers:

1. **Mathematical layer**: $q \in \mathbf{No}$ does live in a
   Hahn-series sub-field — this is automatic from
   [@ehrlich2012].

2. **Physical layer**: the $\alpha_k$ are determined by some
   QOU-internal constraint (perhaps "the surreal categorical
   mass formula reproduces CODATA to $1$ ppb"). This is
   open, and might fail entirely — perhaps the only consistent
   $\alpha_k$ are $0$.

A serious test would be:

- pick the specific Hahn-series sub-field to work in (probably
  $\mathbb{R}(\!(\varepsilon^{\mathbb{Q}})\!)$);
- redo the QOU mass formula with $q = 1 + \varepsilon + \alpha_2
  \varepsilon^2$;
- ask: is there a *unique* choice of $\alpha_2 \in \mathbb{R}$
  for which the formula agrees with CODATA at second order?

If yes (and the $\alpha_2$ has a clean closed form), the
conjecture is plausible. If no (the choice is over-constrained
or under-constrained), the conjecture is rejected.

## Why it matters

The Hahn-series substrate offers a route to **systematic
quantum-correction expansion** for QOU, without having to
invoke an external regularisation scheme. All corrections live
in the same algebraic object as the leading term; they are
distinguished only by their birthday in the surreal grading.

## Proof strategy

The conjecture's two layers (mathematical existence and physical
constraint determination) need separate strategies.

**Layer 1: mathematical existence (provable now)**:

1. Cite Ehrlich [@ehrlich2012] Theorem 12.5: every Hahn series
   ring $\mathbb{R}((\varepsilon^G))$ for divisible ordered
   abelian $G$ embeds in $\mathbf{No}$.

2. Specifically $G = \mathbb{Q}$ gives the
   $\mathbb{R}((\varepsilon^{\mathbb{Q}}))$ sub-field of
   $\mathbf{No}$ used here.

3. Verify $1 + \varepsilon \in \mathbb{R}((\varepsilon^{\mathbb{Q}}))$
   (trivially: it's a finite sum).

This is provable as soon as mathlib has `HahnSeries` integrated
with `Surreal` (partial work exists).

**Layer 2: physical-constraint determination (open)**:

4. Recompute the QOU mass formula with $q = 1 + \varepsilon
   + \alpha_2 \varepsilon^2 + \cdots$ truncated at order 2.

5. Find $\alpha_2 \in \mathbb{R}$ such that the formula's
   second-order $\varepsilon$-coefficient matches measured
   particle-mass corrections (e.g., the residual $\sim 4\%$ MAE
   on $\mathcal{Q}$-values).

6. Determine: is $\alpha_2$ uniquely determined? Is it consistent
   across different particles?

7. If unique: declare the conjecture vindicated at order 2.
   Iterate to higher orders.

8. If non-unique or inconsistent: declare the conjecture
   refuted (the higher-order $\alpha_k$ are *free parameters*,
   not predictions).

**Required infrastructure** (Layer 2):
- A precise CODATA-comparison protocol for second-order
  corrections.
- A Lean (or Python) recomputation of the QOU mass spectrum
  with $q$ as a Hahn series.

**Falsification path**: Layer 2 falsification by inconsistency
across particles (e.g., $\alpha_2$ for the proton differs from
$\alpha_2$ for the neutron). Either inconsistency or
non-uniqueness refutes the predictive conjecture.

**Provability assessment**: Layer 1 mathematical: tractable in
Lean within reach of current mathlib. Layer 2 physical:
requires sustained computational physics work. Most
research-paper-worthy of the appendix's conjectures.
