# α_EM F-construction T4 — weight-value transport: (¾,¼) derived (2026-07-19)

**Bean:** `qou-bfdq` (T4) of milestone `qou-a46k`.
**Probe:** [`computations/alpha_em/alpha_em_f_t4_weight_value_transport_probe.py`](../../computations/alpha_em/alpha_em_f_t4_weight_value_transport_probe.py)
→ `alpha-em-f-t4-weight-value-transport.witness.json` — 5/5 PASS, symbolic-exact.
**Lean:** [`QOU/Archimedean/MarkovWeightValueTransport.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/MarkovWeightValueTransport.lean)
— sorry-free, `lean`-direct exit 0.

**Scope guard (STRICT):** T4 only — T5 (assembly + F = framework-τ residual,
the functorial provenance itself) remains THE open wall; nothing inhabits
`ArchimedeanTauRealization` with provenance; no fit; nothing wired; `1/(8π)`
stays phase-4.

## What T4 needed

T1 derived the isotypic **dims** (3,1) of H¹(Bring) under the deck action
(Chevalley–Weil, zero adjustable input). The plan's T4 line read "weight
transport (dims derived; VALUES (¾,¼) still to derive)". Three exact facts
close it:

1. **Value identity.** The canonical H₂ Jones–Markov weights (corpus
   `y_lambda_at`, Wenzl variable s = √q; closed forms symbolically matched
   to the corpus family):
   `y₂(s) = (s³+s²+1)/((s²+1)(s⁴+1))`, `y₁₁(s) = s³(s³+s−1)/((s²+1)(s⁴+1))`,
   `y₂+y₁₁ = 1` identically, and at the classical point
   **y₂(1) = ¾, y₁₁(1) = ¼ — exactly the T1 dims (3,1) over g = 4.** The
   framework's canonical weight at q = 1 *is* the normalized isotypic
   projector trace of the T1 cover.
2. **The anchor is forced.** `4·num − 3·den = −(s−1)(3s⁵+3s⁴+6s³+2s²+s+1)`
   with the quintic strictly positive on s > 0, so **q = 1 is the unique
   positive matching point** (`anchor_forced`, Lean iff). The transport
   point is derived, not chosen — the tranche-5 dictionary-vacuity prune
   does not apply to a forced anchor.
3. **The monodromy point is singular.** The weight denominator factors
   (§7c-generic, any commutative ring) as `q³+q²+q+1 = (q+1)(q²+1)` and
   **vanishes at the T2 Hecke evaluation q = i**. The value leg (q = 1) and
   the module leg (q = i) are structurally complementary — the weights
   cannot even be evaluated at the monodromy point.

## Plan state (milestone `qou-a46k`)

```
T1 cover structure                     MERGED #4039
T2 local monodromy = H₂(i) module      MERGED #4040
T3 ρ-equivariance (deck reality)       MERGED (main)
T4 weight-value transport (¾,¼)        THIS — derived, Lean sorry-free
T5 assembly + F = framework-τ residual open — THE wall
```

With T4, the #3999 Reality-realization premise has both its dims (T1) and
its values (T4) derived. What remains for T5 is exactly the target spec's
functorial provenance: naturality of the assignment in the categorical data
— the part no interface field can encode.
