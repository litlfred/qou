import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Data.Fintype.Fin

/-!
# QOU.Archimedean.gram_weighted_qvalue

Canonical Lean declaration for content block at
[`quantum-observable-universe/particle-interactions/gram-weighted-qvalue.ts`](quantum-observable-universe/particle-interactions/gram-weighted-qvalue.ts).

The manuscript sub-claims (the Gram-weighted `Q`-value formula, the
weights summing to `1`, and their non-negativity) are stated over
**opaque Gram-matrix-derived data** (the NF-reduction costs `Δ_k` and the
Frobenius-norm Gram weights `w_k`, defined from the Gröbner–Shirshov
normal form of the typed Garside element); no faithful Mathlib structure
realises the Gram pairing here, so per the vacuity-fix playbook pattern C
the proposition is **named** as a `def … : Prop` over the context —
honestly recording the conditional conjecture rather than projecting
context fields.  A Lean instance would be the conjecture.
-/

namespace QOU.Archimedean


/-- Abstract context (inputs) for the `gram_weighted_qvalue` claim — the
    substrate parameter, the proton/neutron counts, the electron mass,
    the `Q`-value, and the per-channel NF-reduction costs `Δ` and Gram
    weights `w`.  No field asserts a conclusion. -/
class GramWeightedQvalueContext where
  /-- Substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- The electron mass `m_e : ℝ` (CODATA input). -/
  m_e : ℝ
  /-- The `Q`-value of the `β⁻`-decay channel. -/
  Q : ℝ
  /-- The NF-reduction cost per neutron-conversion channel `k`, indexed
      `Fin N → ℝ`. -/
  Δ : Fin N → ℝ
  /-- The Gram weight per channel `k`, indexed `Fin N → ℝ`; should sum to
      `1` (probability distribution over conversion channels). -/
  w : Fin N → ℝ

/-- **Manuscript statement** (full body):

**Proposition.**
*Let $\mathcal{G}_{\mathrm{par}} = \mathcal{G}(t_0, \ldots, t_{A-1})$
be the typed Garside element
([typed Garside element](#def:typed-garside-element)) of the parent
nucleus in $H_A(q)$, and let $G$ be the Gram matrix
$G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ restricted to the NF
subspace spanned by $\mathcal{G}_{\mathrm{par}}$ and all conversion
daughters.  Then the $Q$-value for $\beta^-$ decay is:*

```tex
\begin{equation}\label{eq:gram-weighted-qvalue}
  Q(Z, N)
  \;=\;
  \biggl(
    \sum_{k=0}^{N-1}
    w_k^G \;\cdot\; \Delta_k
  \biggr)
  \,\times\, N \,\times\, m_e
\end{equation}
```

*where:*

1. *The sum runs over all $N$ neutrons in the parent
   (all possible conversion channels).*

2. *$\mathcal{G}_{\mathrm{dau}}^{(k)}$ is the typed Garside
   element of the daughter obtained by converting neutron $k$
   ($t_k = n \mapsto p$), and*

```tex
\begin{equation}\label{eq:nf-reduction-cost}
  \Delta_k
  \;=\;
  \lVert \mathcal{G}_{\mathrm{par}} \rVert_1
  \;-\;
  \lVert \mathcal{G}_{\mathrm{dau}}^{(k)} \rVert_1
\end{equation}
```

   *is the NF reduction cost (change in $L^1$ norm of the
   Gröbner--Shirshov normal form).*

3. *The Gram weight for neutron $k$ is:*

```tex
\begin{equation}\label{eq:gram-weight}
  w_k^G
  \;=\;
  \frac{
    \lVert \delta_k \rVert_F
  }{
    \sum_{j=0}^{N-1} \lVert \delta_j \rVert_F
  },
  \qquad
  \delta_k
  \;=\;
  \mathcal{G}_{\mathrm{par}} - \mathcal{G}_{\mathrm{dau}}^{(k)},
  \qquad
  \lVert \delta_k \rVert_F
  \;=\;
  \sqrt{|\delta_k \cdot G \cdot \delta_k|}
\end{equation}
```

   *where $\lVert \cdot \rVert_F$ is the Frobenius norm induced
   by the Gram matrix.*

**Inputs.**  The substrate parameter $q$
(from $\mathrm{Vol}(4_1)$ and $m_\mu/m_e$) and the electron
mass $m_e$.  No other parameters.

## Structure of the formula

The $Q$-value has three factors:

- **$\Delta_k$** (NF reduction cost): measures how much algebraic
  complexity the nucleus sheds when neutron $k$ converts.  The
  daughter has fewer $

[…truncated; see manuscript for remainder…]

    The proposition is **named** below as a `def … : Prop` (pattern C):
    `Δ` and `w` are opaque Gram-matrix-derived inputs, so the
    three-part claim (formula, weights sum to one, weights non-negative)
    is recorded as the conditional conjecture over the context rather than
    discharged by a fake projection. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/gram-weighted-qvalue.ts
def gram_weighted_qvalue (ctx : GramWeightedQvalueContext) : Prop :=
  ctx.Q
      = (Finset.univ.sum (fun k : Fin ctx.N => ctx.w k * ctx.Δ k))
        * (ctx.N : ℝ) * ctx.m_e ∧
  (Finset.univ.sum (fun k : Fin ctx.N => ctx.w k) = 1) ∧
  (∀ k : Fin ctx.N, 0 ≤ ctx.w k)

end QOU.Archimedean
