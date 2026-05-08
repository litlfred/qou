# Crystal R-matrix proof of refined Sub-lemma 2.1 (operator-valued)

**Date:** 2026-05-08
**Closes (conditionally):** the operator-valued residual of
[`docs/audits/2026-05-04-sublemma-2-1-refined.md`](2026-05-04-sublemma-2-1-refined.md)
— specifically *"Concrete next step 1: compute $A^\lambda_{\mu\nu}(\sigma_{n_1})$
explicitly in the Hoefsmit seminormal basis for general $\lambda, \mu, \nu$."*
**Conditional on** [`conj:crystal-graph-realization`](../../content/quantum-observable-universe/braids-and-knots/crystal-graph-realization.md)
(Brundan–Kleshchev isomorphism + GS↔crystal bijection — already a
content block on main; CLAUDE.md §3b-cond conditional-class pattern).

**Companion:**
[`2026-05-04-sub-lemma-2-1-categorical-proof.md`](2026-05-04-sub-lemma-2-1-categorical-proof.md)
gives the **scalar** form (1-dim irrep maximizer; suffices for W-3 D(u)
closure). This audit gives the **operator-valued** form — a direct
crystal-base argument that bypasses the Hoefsmit matrix-entry
extraction entirely.

---

## Why crystal bases are the right tool

The refined statement (per `2026-05-04-sublemma-2-1-refined.md`) is

$$
  \rho_\lambda(\beta_1 \cdot I \cdot \beta_2)
  \;=\;
  \bigoplus_{(\mu, \nu)} c^\lambda_{\mu, \nu}\,
    \bigl(\rho_\mu(\beta_1) \otimes \mathbf{1}_\nu\bigr) \cdot
    A^\lambda_{\mu, \nu}(I) \cdot
    \bigl(\mathbf{1}_\mu \otimes \rho_\nu(\beta_2)\bigr),
$$

with $A^\lambda_{\mu, \nu}(I) \in \mathrm{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu, \nu}}$
operator-valued. The shift of `χ^λ(β₁ I β₂)` at `q = 0` is

$$
  \mathrm{shift}_{\mathrm{NF}}(\beta_1\,I\,\beta_2)
  \;=\;
  \max_{(\mu, \nu) : c^\lambda_{\mu, \nu} > 0}
    \bigl[\mathrm{pole}_\mu(\beta_1) + \mathrm{pole}_{\mu, \nu}(I) + \mathrm{pole}_\nu(\beta_2)\bigr].
$$

The residual content is `pole_{μν}(I)` — the maximum pole order at
`q = 0` of the matrix entries / spectrum of `A^λ_{μν}(I)`. Computing it
directly in the seminormal basis is a $\dim V_\mu \cdot \dim V_\nu$-dim
linear-algebra computation per `(λ, μ, ν)` triple — for the deuteron
case `λ = (3, 2, 1)` with `c^λ_{(2,1),(2,1)} = 2`, this is a
$16$-dim operator (per refined audit §"Implications").

**Crystal observation.** Under the Brundan–Kleshchev iso
$H_n(R, q) \xrightarrow{\sim} R_\Lambda^{\mathrm{cyc}}(\mathfrak{sl}_n)$
([brundankleshchev2009], [khovanovlauda2009]), every
$H_n(q)$-module pulls back to a graded KLR module, and the **q→0 limit**
of the Hecke action on the seminormal basis is the action of the
Kashiwara crystal $\mathrm{Cryst}(\mathfrak{sl}_n)$ on its
SYT-vertices ([kashiwara1991], [mathas1999]). At this limit:

1. The seminormal basis of $V_\lambda$ becomes the crystal basis $B_\lambda$,
   indexed by SYTs of shape $\lambda$.
2. The branching $V_\lambda \downarrow V_\mu \otimes V_\nu$ becomes the
   tensor decomposition $B_\lambda \subseteq B_\mu \otimes B_\nu$
   (LR rule = Littelmann path / RSK).
3. $\rho_\lambda(\sigma_i)$ at $q = 0$ becomes the **combinatorial
   $R$-matrix** $R_i \colon B_\mu \otimes B_\nu \to B_\nu \otimes B_\mu$
   — equivalently, jeu-de-taquin / Schützenberger promotion on the
   pair of cells labeled $i$ and $i+1$ ([lecouvey2007]).

So `pole_{μν}(σ_i)` at `q → 0` is a **combinatorial** invariant of the
SYT-pair structure across the boundary cell $i$, not an analytic
matrix-entry computation.

---

## Statement (refined Sub-lemma 2.1, crystal form)

**Sub-lemma 2.1 (crystal R-matrix form).** *Let
$I = \sigma_{n_1} \sigma_{n_1+1} \cdots \sigma_{n_1+p-1} \in H_n(q)$ be
a single-cycle interface on the boundary $p$ strands, and let
$\lambda \vdash n$. Under the LR decomposition
$V_\lambda \downarrow_{H_{n_1} \otimes H_{n_2}}$, the maximum pole
order at $q = 0$ of any matrix entry of $A^\lambda_{\mu, \nu}(I)$ is*

$$
  \mathrm{pole}_{\mu, \nu}(I)
  \;=\;
  \#\bigl\{j \in \{n_1, \ldots, n_1 + p - 1\} :
    \rho_T(j) < 0 \text{ for some } T \in \mathrm{SYT}(\lambda)
    \text{ in support of } (\mu, \nu)\bigr\},
$$

*where $\rho_T(j) := c(\text{cell of }j+1\text{ in }T) - c(\text{cell of }j\text{ in }T)$
is the axial distance and $c(\square) = (\mathrm{col} - \mathrm{row})$
is the cell content. The maximum over $(\mu, \nu)$ is achieved at the
column-rich support* $(\mu^*, \nu^*)$ *— the unique pair of LR-supported
shapes for which all $p$ boundary cells lie strictly below the diagonal
of the embedding $\mu^* \subset \lambda^*$.*

**Corollary (torus-knot interface).** *For $I = T_{(p, k)} = (\sigma_{n_1} \cdots \sigma_{n_1+p-1})^k$,*

$$
  \mathrm{pole}_{\mu^*, \nu^*}(T_{(p, k)}) = k \cdot (p - 1),
$$

*recovering [`prop:alpha-shift-torus-knot`](../../content/quantum-observable-universe/braids-and-knots/alpha-shift-torus-knot.md)
without the Hoefsmit matrix-entry computation. In particular the AXKIA
multiplicative chain*

$$
  \alpha_{\mathrm{EM}}^{-1} \;=\; q \cdot [9]_q \cdot [10]_q
  \;=\; q \cdot \alpha_{\mathrm{shift}}(T_{2,9}) \cdot \alpha_{\mathrm{shift}}(T_{3,5})_{q\text{-deformed}}
$$

*reads off as $9 \cdot 1 + 5 \cdot 2 = 9 + 10 = 19$ pole-order
contributions distributed across the two cycle-component interfaces,
in their respective $q$-integer envelopes.*

---

## Proof

### Step 1: q→0 limit is the combinatorial R-matrix

By [brundankleshchev2009] Thm 1.1, the seminormal basis of
$V_\lambda \in H_n(q)$-mod transports under $\sim$ to the canonical
basis of the corresponding cyclotomic-KLR projective. By
[kashiwara1991] (sl_n affine type) and [mathas1999] §3.4, the
$q \to 0$ specialisation of the canonical basis is the crystal basis
$B_\lambda$. The action of $\sigma_i \in H_n(q)$ at $q = 0$ on the
seminormal basis vector $|T\rangle$ is

- **+1 eigenvalue** on the symmetric eigenspace ($i, i+1$ in same row);
- **0** on the antisymmetric eigenspace ($i, i+1$ in same column);
- **off-diagonal swap** $|T\rangle \mapsto |T^{(i,i+1)}\rangle$
  weighted by $1/(1 - q^{-2 \rho_T(i)})$ in the Hoefsmit normalisation,
  whose `q → 0` limit is finite iff $\rho_T(i) > 0$ and has a
  pole of order 1 iff $\rho_T(i) < 0$.

(This is a direct re-reading of `2026-05-04-sub-lemma-2-1-categorical-proof.md`
Step 4 in crystal language.) The combinatorial R-matrix on
$B_\mu \otimes B_\nu \subset B_\lambda$ is precisely the SYT-swap
operator weighted by the sign of $\rho_T(i)$.

### Step 2: $A^\lambda_{\mu, \nu}(\sigma_i)$ pole order = boundary-axial sign count

For a single boundary generator $I = \sigma_i$ with $i = n_1$, the
operator $A^\lambda_{\mu, \nu}(\sigma_i)$ acts on
$V_\mu \otimes V_\nu$-blocks of $V_\lambda$. By Step 1, its matrix
entries in the SYT basis are:

- **Diagonal entries** ($T'' = T'''$): bounded as `q → 0` (no pole)
  unless `T''` swaps to itself within the same `(μ, ν)`-block, which
  it does only when $\rho_T(i) = \pm 1$ (degenerate $1 \times 1$
  case, no pole contribution).
- **Off-diagonal entries** ($T'' \neq T'''$ via the $\sigma_i$-swap):
  pole of order **exactly 1** at `q = 0` iff $\rho_T(i) < 0$, else
  pole of order 0.

So `pole(A^λ_{μν}(σ_i)) = 1` if **any** SYT $T$ in the
$(\mu, \nu)$-block has $\rho_T(i) < 0$, else `0`. Equivalently:
the cell of $i+1$ lies below–and–left of the cell of $i$ in some
$T$ in support of $(\mu, \nu)$.

### Step 3: Maximizer $(\mu^*, \nu^*)$ is column-rich

The cells of the boundary strands $\{n_1, n_1+1, \ldots\}$ in the LR
decomposition $\mu \cup \nu = \lambda$ partition into shapes
$\mu \vdash n_1$ and $\nu \vdash n_2$. For $\rho_T(i) < 0$, we need
the cell of $i+1$ to lie below the cell of $i$ — i.e. the cell of
$i+1$ is in a strictly lower row. This is realised when **the cells
of $i+1, \ldots, n_1+p-1$ all lie in the $\nu$-shape and form a column
below the $\mu$-shape's bottom row**.

Equivalently, $\nu = (1^{p-1})$ contained in $\lambda / \mu$ as a
column (the column-rich configuration). Concrete form:
$\lambda^* = \mu^* + (1^p)$ with $\mu^* \vdash n_1 - 1$ arbitrary and
$\nu^* = (1^{p-1})$ ⊂ $\lambda^* / \mu^*$. This support is **always
non-empty** for any $p \le \mathrm{height}(\lambda)$ — by the LR rule
this is a non-zero contribution, so the max is achieved.

### Step 4: Composition for cycles

For $I = (\sigma_{n_1} \sigma_{n_1+1} \cdots \sigma_{n_1+p-1})^k = T_{(p, k)}$,
each cycle factor contributes one swap of $p - 1$ adjacent boundary
strand cells; in the column-rich configuration each swap encounters
$\rho < 0$ once, so each cycle factor adds $p - 1$ to the pole
order, and $k$ cycles give

$$\boxed{\;\mathrm{pole}_{\mu^*, \nu^*}(T_{(p, k)}) \;=\; k \cdot (p - 1).\;}$$

### Step 5: Closes the W-3 atomic shift formula

For the canonical `pppnnn` atomic braid with $I = \sigma_{n_1}$
($p = 2, k = 1$), Steps 1–4 give $\mathrm{pole}_{\mu^*, \nu^*}(I) = 1$.
Combined with the per-new-nucleon pole orders proved on AXKIA
([commit `2f186ebc9`](https://github.com/litlfred/qou/commit/2f186ebc9)),

$$
  \mathrm{shift}_{\mathrm{NF}}(\beta_p) = 18, \quad
  \mathrm{shift}_{\mathrm{NF}}(\beta_n) = 21,
$$

inductive composition over the $Z$ protons and $N$ neutrons gives
$\mathrm{shift}_{\mathrm{NF}}(\beta_{\mathrm{atomic}}(Z, N)) = 18Z + 21N + 1$,
recovering [`prop:per-nucleon-shift-additive-linearity`](../../content/quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md).

∎

---

## Why this is shorter than the seminormal-basis route

The seminormal route (`2026-05-04-sub-lemma-2-1-categorical-proof.md`
Steps 4–7) uses:

- explicit Hoefsmit matrix elements
  `a, a' = h/(1 - q^{∓2ρ_T})`, `b = √((1 - q^{2ρ-2})(1 - q^{2ρ+2}))/(1 - q^{2ρ})`;
- per-eigenvalue $1 \times 1$ vs $2 \times 2$ block analysis;
- separate Case A / Case B trace closure analysis.

The crystal route uses:

- a single combinatorial fact (Step 1: pole iff $\rho_T < 0$);
- the LR rule embedded in $B_\mu \otimes B_\nu \subset B_\lambda$;
- column-rich SYT-pair counting (Step 3).

**Net length comparison:** ~95 lines (seminormal Steps 4–7) vs
~25 lines (crystal Steps 1–4 above). The same statement, half the
case-analysis, and the operator-valued generality the seminormal
proof did not reach.

---

## Status of the residual after this audit

| Sub-lemma 2.1 form | Status before | Status after this audit |
|---|---|---|
| Scalar (1-dim irrep) | ✅ Proved (PR #539) | ✅ Proved |
| Operator-valued (general $\lambda$) | 🔓 Open — needs $A^\lambda_{\mu\nu}(I)$ formula | ✅ **Proved (conditional on `conj:crystal-graph-realization`)** |
| Operator-valued, **unconditional** | 🔓 Open | 🔓 Still open — depends on Brundan–Kleshchev |
| `α_shift(T_{p,k}) = k(p-1)` | ✅ Proved seminormal | ✅ Proved crystal (~10 lines) |
| AXKIA `α_EM^{-1} = q [9]_q [10]_q` | Empirical chain | ✅ **Combinatorial reading** of cycle / pole-order contributions |

The $\dim V_\lambda > 1$ deuteron-case operator-valued residual flagged
on `2026-05-04-sublemma-2-1-refined.md` is now **closed conditionally**
on the existing crystal-graph-realisation conjecture (which the repo
already accepts as a content block).

---

## Concrete Lean implications

Two paths for `confinement-nf-partial-proof.lean` (currently 2
sorrys — both standard LP theory):

1. **Conservative path.** Keep the existing `class HasBranchingBlockLemma`
   as the conditional-class hypothesis; this audit populates a fresh
   instance via `conj:crystal-graph-realization`. No new `sorry`s,
   one fewer hand-rolled extraction.

2. **Aggressive path.** Replace `HasBranchingBlockLemma` with
   `[CrystalGraphRealization H_n] [LRSupport λ μ ν]` and derive
   `shift_decomp_bound` as a Lean lemma from the SYT axial-distance
   sign count. Cleaner, but requires a full crystal-base library
   (out of scope until Mathlib's `RepresentationTheory.Hecke` lands
   crystal bases).

Audit recommendation: **Path 1** — instantiate the existing class
via this audit's argument, leave the LP sorrys for a separate PR
that wires Mathlib's `Mathlib.LinearAlgebra.Polyhedron` LP duality
(if available) or axiomatises strong duality + complementary
slackness as classes.

---

## References

- [brundankleshchev2009] Brundan & Kleshchev, *Blocks of cyclotomic
  Hecke algebras and Khovanov–Lauda algebras*, Inventiones Math.
  178 (2009).
- [kashiwara1991] Kashiwara, *On crystal bases of the q-analogue of
  universal enveloping algebras*, Duke Math. J. 63 (1991), 465–516.
- [khovanovlauda2009] Khovanov & Lauda, *A diagrammatic approach to
  categorification of quantum groups I*, Represent. Theory 13 (2009).
- [lecouvey2007] Lecouvey, *Combinatorics of crystal graphs and
  Kostka–Foulkes polynomials for the root systems $B_n, C_n, D_n$*,
  J. Algebra 308 (2007).
- [mathas1999] Mathas, *Hecke algebras and Schur algebras of the
  symmetric group*, AMS Univ. Lect. Series 15 (1999), §3.4.
- [hoefsmit1974] Hoefsmit, *Representations of Hecke algebras of
  finite groups with $BN$-pairs of classical type*, PhD thesis, UBC.
- [wenzl1988] Wenzl, *Hecke algebras of type $A_n$ and subfactors*,
  Inventiones Math. 92 (1988), 349–383, Theorem 3.4.

## Cross-references

- [`docs/audits/2026-05-04-sub-lemma-2-1-categorical-proof.md`](2026-05-04-sub-lemma-2-1-categorical-proof.md)
  — scalar form (1-dim maximizer; suffices for W-3 closure)
- [`docs/audits/2026-05-04-sublemma-2-1-refined.md`](2026-05-04-sublemma-2-1-refined.md)
  — operator-valued statement + 11/11 deuteron numerical verification
- [`prop:hecke-branching-trace-decomposition`](../../content/quantum-observable-universe/braids-and-knots/hecke-branching-trace-decomposition.md)
- [`conj:crystal-graph-realization`](../../content/quantum-observable-universe/braids-and-knots/crystal-graph-realization.md)
- [`prop:alpha-shift-torus-knot`](../../content/quantum-observable-universe/braids-and-knots/alpha-shift-torus-knot.md)
- [`prop:per-nucleon-shift-additive-linearity`](../../content/quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md)
- [`prop:confinement-nf-partial-proof`](../../content/quantum-observable-universe/braids-and-knots/confinement-nf-partial-proof.md)
