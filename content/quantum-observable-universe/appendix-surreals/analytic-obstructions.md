A first pass at a surreal lift of QOU would catalogue the
general-purpose obstructions — Lebesgue measure, Hilbert-space
completion, hyperbolic geometry — that surreal numbers famously
lack [@alling1987]. An honest audit of the **actual** QOU
content, however, finds that most of these obstructions are
*not triggered* by the main paper. This remark records which
obstructions genuinely bite and which are only apparent.

## 1. Lebesgue measure: one genuine use, no others

A text search for Lebesgue, Haar, and Hausdorff measures across
the content objects returns only a handful of matches, almost
all of which turn out to be *categorical* or *algebraic* by
closer inspection:

| Reference | What is actually used |
|---|---|
| `frobenius-integration.md` | Calls $\int_A$ a "categorical Haar measure" *by analogy*. The actual object is the Frobenius counit $A \to \mathbf{1}$, purely categorical — survives over any field. |
| `categorical-laplace-transform.md` | Compares to Haar on $\mathbb{R}_{\geq 0}$ as motivation; the categorical Laplace transform is defined over any ground ring. |
| `julia-set-reeb.md` | Mentions the Julia measure $\mu_J$ and Hausdorff dimension $d_H(q)$. The dimension is given by the **rational formula** $d_H(q) = (2q-1)^2/q^3$ (see [birthday grading](#def:birthday-grading)), so it lifts to $\mathbf{No}$ exactly. The measure itself is used only for intuitive language. |
| `statistical-mechanical-time.md`, `double-slit-two-modes.md` | Interpretive prose; no measure-theoretic computation is performed. |
| `mobius-energy-proof.md` | **Genuine use.** The Möbius energy integral $\int_{S^1 \times S^1} d\ell(x) d\ell(y) / |x - y|^2$ uses the Lebesgue measure on $S^1$, with diagonal regularisation. |

**Net effect.** The Möbius energy proof is the only block whose
argument genuinely depends on Lebesgue measure, and it is used
as a motivational cross-check rather than as a load-bearing step
in the mass formula. The mass formula itself — Hoefsmit $\to$
Markov trace $\to$ Jones $\to$ substrate value $\to$ categorical mass —
never integrates.

## 2. Hilbert-space completion: stylistic, not load-bearing

Only one block in the content objects writes down a Hilbert-
space completion: `knot-eigenbasis-complete-proof.md` (part 3 of
the proof). The passage reads:

> The direct limit $\varinjlim V^{\otimes n}$ is a pre-Hilbert
> space whose completion $\mathcal{H}_{\mathrm{phys}}$ is
> separable (each $V^{\otimes n}$ is finite-dimensional). The
> union of the finite-dimensional subspaces $V^{\otimes n}$ is
> dense by construction, and each is completely decomposed by
> (1). Hence the irreducible summands, indexed by knot types via
> the closure map, span a dense subspace.

Close reading shows that the only step that invokes Hilbert
structure is the word *dense* in the final sentence. Everything
else — the direct limit, the finite-dimensional decomposition,
the knot-closure indexing — is pure algebra. The conclusion can
be restated in its algebraic form without loss:

> The irreducible summands span the algebraic direct limit
> $\varinjlim V^{\otimes n}$.

This is the statement actually used downstream. The Hilbert
framing is a stylistic choice (anticipating a physical
interpretation) rather than a load-bearing argument. **No
spectral theorem, functional calculus, or unitary
representation is used anywhere in the paper**; Hoefsmit's
diagonalisation is an *algebraic* diagonalisation of a matrix
over $\mathbb{C}(q)$.

Consequence: the Hilbert obstruction is only an obstruction to
**future** work (e.g. a rigorous scattering-pipeline formulation
with physical Hilbert spaces). The current paper survives without
it.

## 3. Genuine obstructions that remain

Three narrow obstructions do bite:

1. **Möbius energy integral** (`mobius-energy-proof.md`).
   Requires Lebesgue on $S^1 \times S^1$ plus diagonal
   regularisation. A surreal Loeb-measure replacement is
   possible in principle (see
   [calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon),
   §5), but is not automatic.

2. **Hyperbolic volume $\mathrm{Vol}(S^3 \setminus K)$**. Used
   for cross-checking the Kashaev volume conjecture
   ([Kashaev volume--density](#rem:kashaev-volume-density)).
   Hyperbolic geometry requires conformal structure on
   $\mathbb{CP}^1$ and metric completion of a universal cover
   — neither is native to $\mathbf{No}$. A surreal
   reformulation is proposed in
   [Kashaev surreal reformulation](#conj:kashaev-surreal),
   but it **trades** the hyperbolic-volume problem for an
   asymptotic-surreal problem rather than solving it.

3. **Classical limit $q \to 1$**, interpreted as a topological
   limit ([classical limit functor](#def:classical-limit-functor)).
   This is not so much broken as *replaced*: the classical
   limit becomes the standard-part of evaluation at
   $q = 1 + \varepsilon$ (see
   [classical limit as standard-part](#conj:classical-limit-stpart)),
   which is an *exact substitute*, not a weakening.

## 4. Things that look like obstructions but are not

For bookkeeping, the following were considered and ruled out as
obstructions after audit:

- **Haar on $\mathrm{SU}_q(2)$** — not used computationally;
  the paper uses the Hopf-algebra counit and Hoefsmit
  seminormal form, both algebraic.
- **Julia set measure $\mu_J$** — used only for interpretive
  language; the Hausdorff dimension is rational in $q$.
- **Convergence of $q$-dilogarithm products** — only used as
  formal power series.
- **Smooth-manifold structure on $M$** — the main paper treats
  $M$ via the Yekutieli brane tower (algebraic) and the
  frame bundle $\mathcal{S}$ (algebraically described).
  Smoothness is a convenience, not load-bearing.
- **Spectral decomposition of Hecke generators** — Hoefsmit
  gives it algebraically over $\mathbb{Q}(q^{1/2})$.
- **$\mathrm{PSL}(2, \mathbb{C})$ action on $\mathbb{CP}^1$** —
  used only in knot-complement discussion and Möbius energy
  setup; not load-bearing for the mass formula.

## 5. Revised summary

| Apparent obstruction | Actually bites? |
|---|---|
| Lebesgue measure | Only in Möbius energy proof (1 block) |
| Haar measure | No — "categorical Haar" is Frobenius counit |
| Hausdorff measure | No — dimension is a rational function of $q$ |
| Hilbert completion | No — stylistic in 1 block, not load-bearing |
| Spectral theorems / unitarity | No — Hoefsmit is algebraic |
| Smooth-manifold structure | No — algebraic substitutes throughout |
| $\mathrm{PSL}(2, \mathbb{C})$ | Only in Möbius/knot-complement setup |
| Hyperbolic volume | Yes — for Kashaev cross-check |
| $q \to 1$ as topological limit | Replaced exactly by standard-part |

**Upshot.** The surreal lift is dramatically less lossy than a
first-pass survey suggests. With two narrow exceptions — the
Möbius energy integral and the hyperbolic-volume side of the
Kashaev comparison — every load-bearing step of the QOU mass
formula and the categorical axioms transfers to $\mathbf{No}$
without modification. The appendix's remaining work is
constructive, not defensive: building new structures
(birthday grading, $\varepsilon$-relaxed axioms, standard-part
functor) in the surreal ambient.
