# Why the J_K calibration test "fails" — it crosses the Archimedean realization functor

**Source.** [`def:sqrt-q-ribbon-structure`](../../content/quantum-observable-universe/quantum-observable-universes/sqrt-q-ribbon-structure.md)
(commit `7dd547f6`, "part A: recast ribbon-structure block in
pre/post-Archimedean language").

## The key paragraph

> The braiding eigenvalues are q and −q^{-1}; neither involves
> q^{1/2}. The element v := q^{1/2} is *post-Archimedean naming*:
> pre-Archimedean it is a formal adjoined square root in the
> splitting field ℚ(q^{1/2}) and carries no geometric content;
> post-Archimedean (after the realization functor at q_0) it becomes
> the real number q_0^{1/2}, and the binary sign choice is the spin
> structure on the realized worldline.
>
> A *ribbon structure* on **C** is a natural twist Θ_V satisfying the
> ribbon axiom; on the defining SU_q(2) representation
> Θ_V = q^{1/2} id_V.
>
> The ribbon datum is post-Archimedean: it is needed exactly when
> the realization target carries a framing — e.g. for the
> Reshetikhin–Turaev functor or for an MTC structure on Rep(**C**)
> — and so it does not enter the QOU core axioms.

## How this resolves the calibration issue

The Jones polynomial J_K(q) is a **ribbon-framed** invariant — it
requires the ribbon twist Θ_V = q^{1/2}·id_V on the defining
representation. The Markov-trace value tr_M(β) computed in our
**pre-Archimedean** Hecke pipeline does NOT carry the ribbon datum.

Therefore there is **no canonical scalar k such that
tr_M(β) = q^k · J_K(q)** within QOU's pre-Archimedean framework —
the two quantities live in different categories. tr_M is in
ℚ(q) (pre-Archimedean Hecke); J_K is in ℚ(q^{1/2}) with a ribbon
framing (post-Archimedean SU_q(2)-Rep).

The trefoil sanity check failure (electron σ_1^3 → 3_1, log-ratio
−2.618) is therefore **structurally correct**, not a methodology
bug. The test is comparing across the Archimedean realization
functor; the writhe-correction formula
V_K(q) = (-1)^{n-1} · q^{(3w-n+1)/4} · tr_M / (q^{1/2}-q^{-1/2})^{n-1}
is exactly the post-Archimedean ribbon framing factor (the q^{1/2}
exponents are post-Archimedean), so applying it within the
pre-Archimedean tr_M evaluation isn't well-defined without the
ribbon datum.

## Implication for the master prop

The master proposition
[`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
already states this in the "Post-Archimedean interpretation
(borrowed, optional)" subsection:

> The QOU mass identity does not depend on the conjecture — it
> depends only on the finite-categorical tr_M(T_w). [...]
> the geometric construction (Reeb-vortex density → Mostow → Gromov)
> that one might run on the post-Archimedean side as another way to
> write the same number is not part of the QOU derivation.

Volume-conjecture / Jones-polynomial / writhe-normalisation
comparisons live entirely on the post-Archimedean side. They're
useful as borrowed naming but cannot be used to refute or confirm
the categorical identification within QOU's own framework.

## What this means for the "knot ID refutation" project

The earlier strategy — "compare tr_M(T_w, q_0) against J_K(q_0)
to test historical knot IDs" — is structurally a post-Archimedean
test, requiring:

1. The ribbon twist Θ_V applied to tr_M to lift it into
   ℚ(q^{1/2}) with framing data.
2. The writhe correction q^{(3w-n+1)/4} applied per representative.
3. The (q^{1/2}-q^{-1/2})^{n-1} normalisation applied per strand
   count.
4. Sign correction (-1)^{n-1}.

Any of these factors can be off depending on convention. **For the
QOU pipeline's actual mass derivation we need NONE of this** —
B(𝔥) = m_e · ρ · |tr_M(T_w)|_{q=q_0} is computed entirely
pre-Archimedean.

The "wrong knot ID" question is therefore an **external naming
question** (does our T_w post-Archimedean realise as the historical
K?), not a structural QOU question. R5-full SDP-as-solver produces
the correct categorical T_w; whether its post-Archimedean Markov
closure happens to equal one of {6_2, 8_11, L_6a4} or some other
hyperbolic knot is an interesting but not-blocking question.

## Within-pipeline check that IS fully pre-Archimedean

The 3A-strand vs SDP-witness ²H discrepancy
(commit `8a3bcb44`) IS a pre-Archimedean test:

| ²H representation | tr_M(q_0) |
|---|---|
| 3A-strand B_6 (atom_braid_word_3A) | 0.388286 |
| SDP-witness B_3 ([1,-2,1,1,1,-2]) | 0.288326 |

Both compute tr_M of a Hecke element in the same pre-Archimedean
Hecke algebra; both should land at the same value if they're
Markov-equivalent representatives of the same atom-link. They
don't — and `0.388/0.288 = 1.347` corresponds to no integer power
of q_0. This is a real internal-consistency failure of QOU's own
representation choices, independent of any external knot-table.

Resolving it requires identifying which of the two ²H braids is
the canonical Hecke element T_w(²H) for the categorical pipeline.
The R5-full SDP-as-solver is what produces this — until it lands
for ²H, neither representation is privileged.

## Action items (revised)

1. **Stop running the J_K integer-power test**; it's not a
   well-defined pre-Archimedean question. The
   `historical_K_comparison.writhe_match` field in
   `atomic-tr-m-wenzl-bridge.witness.json` should be marked
   "post-Archimedean / requires ribbon framing".
2. **Pursue the within-pipeline ²H discrepancy** — that one IS
   pre-Archimedean and IS resolvable.
3. **Master-prop α\* table caveat** still warranted (commit
   `077f3baf`): α\* presentation-dependence is a pre-Archimedean
   property of the bisection verifier, independent of ribbon /
   post-Archimedean naming.
