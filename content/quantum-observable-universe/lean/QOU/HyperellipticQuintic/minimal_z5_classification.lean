/-!
# QOU.HyperellipticQuintic.minimal_z5_classification

**Placeholder canonical** for content block at
[`quantum-observable-universe/braids-and-knots/hyperelliptic-z5-classification.ts`](quantum-observable-universe/braids-and-knots/hyperelliptic-z5-classification.ts).

The full Lean statement is pending; this stub exists so the
`lean.ref` URI `qou:QOU.HyperellipticQuintic.minimal_z5_classification` resolves to a real declaration in the `qou`
Lake package.
-/

namespace QOU.HyperellipticQuintic


/-- Abstract context for the `minimal_z5_classification` claim — manuscript-themed
    typed fields below; `holds` carries the residual `Prop` claim. -/
class MinimalZ5ClassificationContext where
  /-- Genus of the minimal hyperelliptic ℤ₅-curve. -/
  genus : ℕ
  /-- Branch-divisor cardinality `|Branch(π)|`. -/
  branch_count : ℕ
  /-- Manuscript identities: minimal genus `g = 2` and
      Riemann-Hurwitz forces `|Branch(π)| = 2g + 2 = 6`. -/
  claim_minimal_z5_classification :
    genus = 2 ∧ branch_count = 2 * genus + 2 ∧ branch_count = 6

/-- **Manuscript statement** (full body):

**Theorem.**
Let $X$ be a smooth projective Riemann surface of minimal genus
satisfying the two conditions

*(i)*  $X$ is hyperelliptic: there exists a degree-$2$ morphism
$\pi \colon X \to \mathbb{P}^1$ with involution $\iota$;

*(ii)* $X$ admits a faithful $\mathbb{Z}_5$ automorphism $\phi$
commuting with $\iota$.

Then $g(X) = 2$ and $X$ is isomorphic to
$\mathcal{X}_5 \colon y^2 = x^5 - 1$
([def:hyperelliptic-quintic](#def:hyperelliptic-quintic)).

*Proof.*
Because $\phi$ commutes with $\iota$ it descends along $\pi$ to an
automorphism $\bar\phi$ of $\mathbb{P}^1$; faithfulness of $\phi$ and
commutativity with $\iota$ force $\bar\phi$ to be an element of order
$5$ in $\mathrm{PGL}_2(\mathbb{C}) = \mathrm{Aut}(\mathbb{P}^1)$.  Every
order-$5$ element of $\mathrm{PGL}_2(\mathbb{C})$ is conjugate to
$x \mapsto \zeta_5 x$, which has exactly two fixed points on
$\mathbb{P}^1$, namely $\{0, \infty\}$.  After Möbius normalisation we
may take $\bar\phi \colon x \mapsto \zeta_5 x$.

Orbits of $\bar\phi$ on $\mathbb{P}^1$ have size $1$ (fixed points:
$0, \infty$) or $5$ (generic orbits
$\{a, \zeta_5 a, \zeta_5^{\,2} a, \zeta_5^{\,3} a, \zeta_5^{\,4} a\}$
for $a \notin \{0, \infty\}$).

The branch divisor of $\pi$ is $\phi$-invariant (since $\phi$ commutes
with $\iota$), hence a $\bar\phi$-invariant subset of $\mathbb{P}^1$.
Its cardinality is therefore a non-negative combination of $1$ and $5$:
$|\mathrm{Branch}(\pi)| \in \{0, 1, 2, 5, 6, 7, 10, 11, 12, \ldots\}$.

By Riemann--Hurwitz,

$$
  |\mathrm{Branch}(\pi)|  =  2g(X) + 2,
$$

so the size is even and at least $4$ (for $g \geq 1$, which is forced
by (ii): a sphere has $\mathrm{Aut}(\mathbb{P}^1) = \mathrm{PGL}_2$
admitting $\mathbb{Z}_5$ but is excluded from hyperelliptic indexing
$g \geq 2$; for $g = 0$ one takes $X = \mathbb{P}^1$ itself, not a
branched double cover).
The smallest admissible $|\mathrm{Branch}(\pi)|$ in the list above that
is even and at least $6$ is $6$, giving $g = 2$.

The combinatorial decomposi

[…truncated; see manuscript for remainder…]

    The Lean encoding below is a `theorem foo [ctx] : ctx.claim_minimal_z5_classification := by sorry`
    placeholder; the `ctx.claim_minimal_z5_classification : Prop` field carries the residual claim,
    awaiting per-block type-level translation. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/hyperelliptic-z5-classification.ts
theorem minimal_z5_classification [ctx : MinimalZ5ClassificationContext] :
    ctx.genus = 2 ∧ ctx.branch_count = 2 * ctx.genus + 2 ∧
    ctx.branch_count = 6 :=
  sorry

end QOU.HyperellipticQuintic
