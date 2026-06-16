# Sub-lemma 2.1 — refined statement (operator-valued $A^\lambda_{\mu\nu}$), 11/11 VERIFIED

**Date:** 2026-05-04
**Branch:** `claude/categorical-mass-divergence-audit` (PR #534)
**Status:** Refined statement is **numerically verified to ~$10^{-15}$ for all 11 partitions $\lambda \vdash 6$ in the deuteron case** (commit `eca6b5a43`). Combined with the [categorical proof](2026-05-04-sublemma-2-1-categorical-proof.md), this is effectively a full proof for $H_6 \downarrow H_3 \times H_3$.

**Update (2026-05-08):** The operator-valued residual flagged in
"Concrete next steps §1" below is now **categorically closed
conditional on `conj:crystal-graph-realization`** via the
combinatorial $R$-matrix on $B_\mu \otimes B_\nu$ at the
$q \to 0$ limit. See
[`docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md`](2026-05-08-crystal-r-matrix-sublemma-2-1.md)
— ~25-line proof replacing the 95-line seminormal-basis case
analysis, with the operator-valued generality the scalar audit
did not reach.

**Relation to main's [`2026-05-04-sub-lemma-2-1-categorical-proof.md`](2026-05-04-sub-lemma-2-1-categorical-proof.md)** (PR #539, landed 2026-05-04):
that document gives the categorical proof of the **scalar form** of Sub-lemma 2.1, which suffices for the W-3 D(u) shift formula at the maximizer (1-dim column irrep $V_{(1^p)}$). This document supplies the **operator-valued refinement** for the general (multi-dim irrep) case, with explicit numerical verification across all $\lambda \vdash 6$ and a recursive corner-content prediction. The two documents are complementary: main's covers the scalar specialisation needed for the W-3 closure; this one covers the general operator-valued statement.

**Refs:**
- [`docs/audits/2026-05-04-confinement-nf-structure-forcing-proof.md`](2026-05-04-confinement-nf-structure-forcing-proof.md) — original skeleton
- [`docs/audits/2026-05-04-sub-lemma-2-1-categorical-proof.md`](2026-05-04-sub-lemma-2-1-categorical-proof.md) — main's scalar-form proof (PR #539)
- [`docs/audits/2026-05-04-sublemma-2-1-categorical-proof.md`](2026-05-04-sublemma-2-1-categorical-proof.md) — operator-valued proof (this branch)
- [`computations/sublemma_2_1_A_operator_extract.py`](../../computations/sublemma_2_1_A_operator_extract.py) — operator-valued extraction
- [`computations/sublemma-2-1-A-operator-extract.witness.json`](../../computations/sublemma-2-1-A-operator-extract.witness.json)

## Empirical falsification of the scalar formula

Running the LR-system inversion across $100$ test braid pairs
$(\beta_1, \beta_2) \in (\text{H}_3 \text{ algebra})^2$ for the deuteron interface
$I = \sigma_2 - \tfrac{1}{2}(q - q^{-1}) \cdot \mathbf{1}$ in $H_6(q_0)$, the
scalar Sub-lemma 2.1 formula

$$
  \chi^\lambda(\beta_1 \cdot I \cdot \beta_2)
  \;\stackrel{?}{=}\;
  \sum_{(\mu, \nu)} c^\lambda_{\mu, \nu}
                     \cdot \chi^\mu(\beta_1)
                     \cdot \alpha_{\mathrm{shift}}(I; \lambda, \mu, \nu)
                     \cdot \chi^\nu(\beta_2)
$$

is consistent **only for 2 of 11** partitions:

| $\lambda \vdash 6$ | $N_\lambda$ | $c^\lambda_{\mathrm{max}}$ | max rel residual | scalar formula? |
|---|---:|---:|---:|---|
| $(6)$            | 1 | 1 | $7 \times 10^{-16}$ | ✅ scalar |
| $(5, 1)$         | 3 | 1 | $25.4$ | ❌ |
| $(4, 2)$         | 4 | 1 | $56.5$ | ❌ |
| $(4, 1, 1)$      | 5 | 1 | $277$ | ❌ |
| $(3, 3)$         | 2 | 1 | $38.7$ | ❌ |
| $(3, 2, 1)$      | 5 | 2 | $10^{12}$ | ❌ matrix-valued |
| $(3, 1, 1, 1)$   | 5 | 1 | $114$ | ❌ |
| $(2, 2, 2)$      | 2 | 1 | $33.3$ | ❌ |
| $(2, 2, 1, 1)$   | 4 | 1 | $78.5$ | ❌ |
| $(2, 1, 1, 1, 1)$ | 3 | 1 | $23.7$ | ❌ |
| $(1^6)$          | 1 | 1 | $4 \times 10^{-16}$ | ✅ scalar |

The two scalar-consistent cases are precisely the two **1-dimensional**
extremes:

- $\lambda = (6)$: $\dim V_{(6)} = 1$, support $((3), (3))$ with
  $c^\lambda_{\mu\nu} = 1$. The interface $I = \sigma_2 - h/2$ acts
  as $q - h/2 = (q + q^{-1})/2 \approx 1.005$ on the symmetric rep.
  $\alpha_{\mathrm{shift}}((6), (3), (3)) = +1.0054$.
- $\lambda = (1^6)$: $\dim V_{(1^6)} = 1$, support $((1^3), (1^3))$ with
  $c^\lambda_{\mu\nu} = 1$. The interface acts as $-q^{-1} - h/2 = -(q + q^{-1})/2 \approx -1.005$
  on the alternating rep. $\alpha_{\mathrm{shift}}((1^6), (1^3), (1^3)) = -1.0054$.

Note **even when $c^\lambda_{\mu\nu} = 1$** (e.g. $\lambda = (5, 1)$,
$(4, 2)$, $(3, 3)$), the scalar formula fails. This rules out the
"matrix-valued only when $c^\lambda \geq 2$" hypothesis: $A^\lambda_{\mu\nu}(I)$
is generically a **non-scalar operator** on $V_\mu \otimes V_\nu$.

## Refined Sub-lemma 2.1

The correct statement carries an **operator-valued** interface coefficient
$A^\lambda_{\mu\nu}(I) \in \mathrm{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu\nu}}$:

**Sub-lemma 2.1 (refined).** *Under the LR decomposition*
*$V_\lambda \big|_{H_{n_1}(q) \otimes H_{n_2}(q)} = \bigoplus_{(\mu, \nu)} c^\lambda_{\mu, \nu} \cdot V_\mu \otimes V_\nu$*
*(Wenzl 1988), the action of any element*
*$\beta = \beta_1 \cdot I \cdot \beta_2 \in H_n(q)$ where $\beta_1 \in H_{n_1}(q)$,*
*$I \in H_n(q)$ supported on the boundary strands $\{n_1, n_1+1\}$, and*
*$\beta_2 \in H_{n_2}(q)$, decomposes as*

$$
  \rho_\lambda(\beta_1 \cdot I \cdot \beta_2)
  \;=\;
  \bigoplus_{(\mu, \nu)} \,
  c^\lambda_{\mu, \nu} \cdot
  \bigl(\rho_\mu(\beta_1) \otimes \mathbf{1}_\nu\bigr) \cdot
  A^\lambda_{\mu, \nu}(I) \cdot
  \bigl(\mathbf{1}_\mu \otimes \rho_\nu(\beta_2)\bigr),
$$

*where $A^\lambda_{\mu, \nu}(I) \in \mathrm{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu, \nu}}$
is the* (μ, ν)-*block of $\rho_\lambda(I)$ in the LR basis. Taking traces:*

$$
  \chi^\lambda(\beta_1 \cdot I \cdot \beta_2)
  \;=\;
  \sum_{(\mu, \nu)} c^\lambda_{\mu, \nu} \cdot
    \mathrm{Tr}_{V_\mu \otimes V_\nu}\!\Bigl(
       \bigl(\rho_\mu(\beta_1) \otimes \rho_\nu(\beta_2)\bigr)
       \cdot A^\lambda_{\mu, \nu}(I)
    \Bigr).
$$

**Special case (proved scalar).** When $\dim V_\lambda = 1$ (i.e.
$\lambda \in \{(n), (1^n)\}$), the entire decomposition is trivial
and $A^\lambda_{\mu, \nu}(I)$ reduces to the scalar
$\rho_\lambda(I) \in R$ (a single matrix element). For
$I = \sigma_{n_1} + d \cdot \mathbf{1}$:

| $\lambda$ | Fundamental eigenvalue of $\sigma_{n_1}$ | $A^\lambda_{\mu\nu}(I)$ |
|---|---|---|
| $(n)$ | $+q$ | $q + d$ |
| $(1^n)$ | $-q^{-1}$ | $-q^{-1} + d$ |

The deuteron probe matches this exactly: at $q_0$, $d = -h/2 = -(q-q^{-1})/2$,
$A^{(6)} = q - h/2 = (q + q^{-1})/2 \approx +1.005$ ✓ and
$A^{(1^6)} = -q^{-1} - h/2 = -(q + q^{-1})/2 \approx -1.005$ ✓.

## Implications for `conj:confinement-nf-structure-forcing`

The original Theorem 2 (shift decomposition) of the proof skeleton
relied on the scalar Sub-lemma 2.1. With the refined statement, it
becomes:

**Theorem 2 (refined).** *Under the confinement hypothesis,*

$$
  \mathrm{shift}_{\mathrm{NF}}(\beta_1 \cdot I \cdot \beta_2)
  \;=\;
  \max_{(\mu, \nu)} \Bigl[
    \mathrm{pole}_\mu(\beta_1)
    + \mathrm{pole}_{\mu, \nu}(I)
    + \mathrm{pole}_\nu(\beta_2)
  \Bigr],
$$

*where $\mathrm{pole}_{\mu, \nu}(I)$ is the maximum pole order at*
*$q = 0$ of the operator-valued $A^\lambda_{\mu, \nu}(I) \in \mathrm{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu, \nu}}$*
*(maximum over the matrix entries / spectrum, depending on whether*
*the surrounding $\beta_1, \beta_2$ trace selects diagonal or*
*off-diagonal contributions).*

The substantive content is now in $\mathrm{pole}_{\mu, \nu}(I)$ —
a max over matrix entries of a Hoefsmit block. For the deuteron
$\lambda = (3, 2, 1)$ case with $c^\lambda_{(2,1),(2,1)} = 2$, this
is a $2 \times 2 \times 4 = 16$-dim operator (acting on
$\mathbb{C}^2 \otimes \mathbb{C}^2$ with 2-fold multiplicity).

## Status of the three theorems (after refinement)

| Claim | Provability |
|---|---|
| Strong duality (Theorem 3) | ✅ Fully proved (standard LP) |
| $\lambda^* \in A$ (Theorem 1) | ✅ Fully proved (LP complementary slackness) |
| Branching factorisation (Wenzl 1988, $I = \mathrm{id}$ case) | ✅ Numerically verified to 1e-14, deuteron |
| Refined Sub-lemma 2.1 (operator-valued $A^\lambda_{\mu\nu}$) | 🆕 Statement now correct; proof is the standard branching theorem applied with the operator-valued $A$ |
| Decomposition formula (refined Theorem 2) | 🔓 Open — needs explicit $\mathrm{pole}_{\mu, \nu}(I)$ formula |
| Scalar special case ($\lambda$ extremes) | ✅ Proved + verified (deuteron) |

## Concrete next steps

1. **Compute $A^\lambda_{\mu\nu}(\sigma_{n_1})$ explicitly** in the
   Hoefsmit seminormal basis for general $\lambda, \mu, \nu$. This is
   the residual content of the refined Sub-lemma 2.1.

2. **Verify the deuteron prediction $\mathrm{shift} = 18Z + 21N + 1 = 40$** by:
   - Computing $A^\lambda_{\mu\nu}(I)$ for each $\lambda \vdash 6$
   - Maximising $\mathrm{pole}_\mu(\beta_p) + \mathrm{pole}_{\mu\nu}(I) + \mathrm{pole}_\nu(\beta_n)$
     over $(\mu, \nu)$ in the support of the maximizing $\lambda^*$.

3. **Update [`docs/audits/2026-05-04-confinement-nf-structure-forcing-proof.md`](2026-05-04-confinement-nf-structure-forcing-proof.md)**
   to use the refined statement.

4. **Lean formalisation.** With the refined statement and Wenzl 1988
   as a black box, Theorem 1 and Theorem 3 can be Lean-formalised
   immediately. The operator-valued $A^\lambda_{\mu\nu}$ requires
   either treating it as an abstract endomorphism (axiomatised) or
   a complete Hoefsmit-formula derivation.

## References

- [Wenzl 1988] *Hecke algebras of type $A_n$ and subfactors*,
  Inventiones Math. 92 (1988), 349–383. Theorem 3.4 (branching).
- [Hoefsmit 1974] *Representations of Hecke algebras of finite groups
  with $BN$-pairs of classical type*, PhD thesis, UBC. Seminormal
  matrix elements.
- [`prop:alpha-shift-torus-knot`](../../content/quantum-observable-universe/braids-and-knots/alpha-shift-torus-knot.md)
  — proved scalar case for column extremes (consistent with $(1^n)$ row above).
- [`prop:atomic-mass-gb-nf`](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md)
- [`conj:confinement-nf-structure-forcing`](../../content/quantum-observable-universe/braids-and-knots/confinement-nf-structure-forcing.md)
