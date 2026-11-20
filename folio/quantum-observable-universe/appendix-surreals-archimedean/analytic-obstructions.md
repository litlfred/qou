A first pass at a surreal lift of QOU would catalogue the
general-purpose obstructions — Lebesgue measure, Hilbert-space
completion, hyperbolic geometry — that surreal numbers famously
lack \cite{alling1987}. An honest audit of the **actual** QOU
content, however, finds that most of these obstructions are
*not triggered* by the main paper. This remark records which
obstructions genuinely bite and which are only apparent.

## 0. An audit, not an axiomatisation

The shortcut of axiomatising a single integration operator on $\mathbf{No}$ is mathematically closed. Costin, Ehrlich, and Friedman \cite{costin-ehrlich-friedman2015} prove a two-sided result on integration over the surreals:

- **Positive direction.** A robust algebraic integral exists for
  the class of semi-algebraic, analytic, and
  [Écalle–Borel transserial functions](#def:ecalle-borel-resummation),
  obtained by routing through Hardy-
  field germs and the surreal–transseries correspondence
  \cite{berarducci-mantova2018}. On this class the integral satisfies
  the standard properties (linearity, FTC, translation
  invariance).
- **Negative direction.** Set-theoretic obstructions rule out
  extending the integral to a translation-invariant operator on
  the full ring $C(\mathbf{No})$ of continuous surreal-valued
  functions. The order topology on $\mathbf{No}$ is totally
  disconnected, $C(\mathbf{No})$ contains functions whose
  "support" violates well-ordering, and no measure on
  $C(\mathbf{No})$ can simultaneously be translation-invariant,
  $\sigma$-additive, and non-degenerate.

We do **not** postulate a measure on all of $C(\mathbf{No})$. That object does not exist. Manufacturing one via a categorical proxy (e.g.\ asserting the Frobenius pairing $\int_A : A \otimes A \to \mathbf{1}$ at $A = C(\mathbf{No})$) smuggles the obstruction into the axiom. Instead, we audit each genuine use of an analytic structure in this paper to determine whether the use lifts to $\mathbf{No}$ on the CEF-positive side (algebraic / transserial) or requires a custom workaround. We perform this audit below.

## 1. Lebesgue measure: one genuine use, no others

We evaluate Lebesgue, Haar, and Hausdorff measures throughout this paper. Almost all instances are *categorical* or *algebraic* upon inspection:

See [Table 1](#tbl:analytic-obstructions-table1-data).

**Net effect.** The Möbius energy proof is the only block whose
argument genuinely depends on Lebesgue measure, and it is used
as a motivational cross-check rather than as a load-bearing step
in the mass formula. The mass formula itself — Hoefsmit $\to$
Markov trace $\to$ Jones $\to$ substrate value $\to$ categorical mass —
never integrates.

## 2. Hilbert-space completion: stylistic, not load-bearing

Only one place in this paper writes down a Hilbert-
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

1. **Möbius energy integral**.
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
  $M$ via the brane tower (algebraic) and the
  frame bundle $\mathcal{S}$ (algebraically described).
  Smoothness is a convenience, not load-bearing.
- **Spectral decomposition of Hecke generators** — Hoefsmit
  gives it algebraically over $\mathbb{Q}(q^{1/2})$.
- **$\mathrm{PSL}(2, \mathbb{C})$ action on $\mathbb{CP}^1$** —
  used only in knot-complement discussion and Möbius energy
  setup; not load-bearing for the mass formula.

## 5. Revised summary

See [Table 2](#tbl:analytic-obstructions-table2-data).

**Conclusion.** The surreal lift preserves nearly all structure. With two narrow exceptions — the Möbius energy integral and the hyperbolic-volume side of the Kashaev comparison — every load-bearing step of the mass formula and categorical axioms transfers to $\mathbf{No}$ without modification. The remaining work constructs new structures (birthday grading, $\varepsilon$-relaxed axioms, standard-part map) in the surreal ambient.
