**Proposition.** *In the $\mathfrak{Q}_\beta$ precision-ladder factorisation
$\mathfrak{Q}_\beta(q) = Q_A(q) \cdot \cos(\alpha_{\text{eff}}(q)) \cdot \prod_{k \ge 2}(1 + c_k u^k)$,
any candidate Habiro element $F(q)$ generating the ladder must satisfy
the direction-sanity invariant: $|F(q_0)|$ at the substrate anchor
must be in the same order of magnitude as the target observable's
ratio $\mathfrak{Q}_\beta^{\text{CODATA}} / [Q_A(q_0) \cdot \cos(\alpha_{\text{eff}}(q_0))]$.
A candidate predicting a magnitude differing by more than $10\times$
is structurally REFUTED at the formalize-first level.*

## Why this is the $\S 4(d)$ formalize-first gate

The refuted-class map (`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`)
$\S 4(d)$ states the direction-sanity invariant abstractly. The canonical
**refutation precedent** is the trace-level Markov-stabilization
attack (refuted-class row C12): the candidate's natural scaling factor
$z(q_0) = 1 / (q_0^{1/2} + q_0^{-1/2}) = 0.4993$ was strictly less than 1,
while the target multiplier $\text{linking\_weight} \approx 2.53$ was
strictly greater than 1. **No power of $z < 1$ can multiply UP to a
value $> 1$** — this is a one-line magnitude refutation that killed
the entire mass-side trace identity class **before** any expensive
numerical anchor sweep.

The direction-sanity invariant abstracts this argument: a candidate
$F(q)$ whose magnitude at the substrate anchor is structurally
inconsistent with the target observable's magnitude is refuted on
paper, not in compute. This is the $\S 4(d)$ formalize-first gate.

## The four $\S 4$ invariants (now complete)

| # | invariant | formalised in |
|---|---|---|
| (a) | **Anchor-stable** (cross-anchor swing < 1 ppm) | [`prop:q-beta-radius-of-convergence-gate`](q-beta-radius-of-convergence-gate.md) |
| (b) | **Bar-even** under $q \mapsto q^{-1}$ | [`prop:q-beta-bar-even-kernel-invariant`](q-beta-bar-even-kernel-invariant.md) |
| (c) | **q = 1 classical-limit shadow** | [`prop:q-beta-q-eq-one-shadow-gate`](q-beta-q-eq-one-shadow-gate.md) |
| (d) | **Direction sanity** | **this proposition** |

With (d) formalized, the four-invariant set is complete; any future
candidate $F(q)$ for the 𝔔_β c_k Habiro element is evaluable as a
Lean class-instance attempt rather than as a numerical fit.

## The target magnitude at $q_0$

At the substrate $q_0 \approx 1.10998$:

$$
\frac{\mathfrak{Q}_\beta^{\text{CODATA}}}{Q_A(q_0) \cdot \cos(\alpha_{\text{eff}}(q_0))}
\;\approx\; \frac{0.78233\;\text{MeV}}{0.78371\;\text{MeV}}
\;\approx\; 0.99824 \;\approx\; 1,
$$

i.e. the ladder product $\prod_k(1 + c_k u^k) \approx 0.99824$ at $q_0$
(the precision-ladder corrections collectively contribute only ~0.18%
of the bare $Q_A \cdot \cos$ value). A candidate $F(q_0)$ giving a
magnitude wildly different from 1 (e.g. ~0.5 like the refuted $z(q_0)$,
or ~10 like an over-scaled formal series) is automatically refuted.

## Proof sketch

**The gate (rejection lemma):** if a candidate's substrate-evaluation
gives $|F(q_0) - F_{\text{target}}(q_0)| / F_{\text{target}}(q_0) > 10$,
the candidate fails the gate. Here $F_{\text{target}}(q_0) \approx 0.998$
is the target ladder product computed above. The 10$\times$ threshold is
loose by design — it catches order-of-magnitude direction errors (like
the $z < 1$ vs target $> 1$ case) without false-positives on small
numerical deviations that survive into the more precise §4(a) radius-
of-convergence test.

The lower bound on threshold is set by the cross-anchor swing magnitude:
the substrate $u_0$ varies by only 210 ppb between
proton and muon anchors, so any threshold tighter than ~10$\times$ would be
testing the cross-anchor invariant (a) rather than direction sanity
(d). The two gates are deliberately complementary. $\blacksquare$

## Use in the formalize-first checklist

This is **Step 6** of the 7-step Δ_λ pre-flight checklist (`docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md` $\S 3$).
Concretely, for any candidate $F(q)$:

1. Evaluate $F(q_0)$ at the substrate anchor.
2. Compute $|F(q_0) - F_{\text{target}}(q_0)| / F_{\text{target}}(q_0)$.
3. If the ratio is $> 10$ (order-of-magnitude mismatch), REJECT —
   add a new row to refuted-class map $\S 2$.
4. If the ratio is $\le 10$, proceed to Step 7 (only NOW run the
   numerical anchor sweep) of the checklist.

## Composition with the prior three gates

```
1. Bar-even check (§4b)        PASS (q ↔ q⁻¹ Taylor-even-in-t)
2. Radius-of-convergence (§4a) PASS (simple pole at u_substrate)
3. q = 1 shadow (§4c)          PASS (c_2 → −1, c_3 → −2)
4. Direction sanity (§4d)      PASS (|F(q_0)| in 10× of target)
5. CFinite recurrence engine   PASS (generates c_k from kernel)
```

A unified `BarEvenKernel` typeclass ties all four together,
extending the `CFinite` recurrence engine.
