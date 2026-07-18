# α_EM bean B4, brick a — the classical origin of the ½ (2026-07-18)

**Bean:** `qou-1p06` (B4) of the τ-correspondence proof plan (milestone
`qou-b5qg`). Upstream: B1 merged
([#3955](https://github.com/litlfred/qou/pull/3955)), B2 shadow merged
([#3960](https://github.com/litlfred/qou/pull/3960)), B3 merged
([#3969](https://github.com/litlfred/qou/pull/3969) — Clause A = B2-lift + B4).

**Probe:** [`computations/alpha_em/alpha_em_b4_classical_half_origin_probe.py`](../../computations/alpha_em/alpha_em_b4_classical_half_origin_probe.py)
→ [`alpha-em-b4-classical-half-origin.witness.json`](../../computations/alpha_em/alpha-em-b4-classical-half-origin.witness.json)
— 4/4 assertions PASS, sympy-exact, using the corpus's canonical
`y_lambda_at` (Jones–Markov weights) and the §7a channel eigenvalues
`(q, −q⁻¹)`.

**Scope guard (STRICT):** scope-(a); derives no clause; no fit; nothing
wired; `1/(8π)` stays phase-4.

## B4's target, restated

The merged Clause-B sharpening leaves exactly one open statement: the tower's
one-loop coefficient is `−[2]_q·x` **exactly**, with the measure `x`
q-independent, so `x = α/(8π)` **iff** the q→1 one-loop total `2x` equals the
universal heat-kernel unit `a₀·α = α/(4π)`. The ½ in `½·a₀` is therefore a
**classical-limit normalization**. This brick asks: which canonical q=1
object *is* the ½ — and which candidate readings survive?

## Findings

**F1 — the canonical Markov weights are Schur–Weyl, not Plancherel.** The
corpus's canonical Jones–Markov weights at n=2 satisfy `y_[2]+y_[1,1] = 1`
identically and evaluate at q=1 to **(¾, ¼)** — the SU(2) Schur–Weyl
dimensions `(dim spin-1, dim spin-0)/4` of `V⊗V` — not the S₂-Plancherel
`(½, ½)`. The equal-weight reading of the ½ is *not* the canonical Markov
weight reading (consistent with merged F2, which excluded the weight reading
at q₀).

**F2 — a triple coincidence at q=1.** Three distinct canonical objects all
equal ½ exactly at the decategorification point:

| Reading | Object | At q=1 | q-dependence |
|---|---|---|---|
| (a) | idempotent normalization `1/[2]_q` | ½ | q-dependent (4/17 at q=4) |
| (b) | S₂-Plancherel weight `dim²/2!` | ½ | constant |
| (c) | canonical Markov trace of the crossing `tr_M(σ) = q·y_[2] − q⁻¹·y_[1,1]` | ½ (= ¾ − ¼, the crossing's signed channel content) | q-dependent (2/5 at q=4) |

**F3 — the q-independence of x discriminates.** Since the one-loop
coefficient is `−[2]_q·x` exactly (all q-dependence in `[2]_q`), neither
q-family (a) nor (c) can sit *inside* the measure — at q=4 they give 4/17 and
2/5, incompatible with a constant x. The classical normalization must be
**evaluated at q=1**: the ½ is a decategorification-*point* constant. This is
precisely the shape of the KL route (AGENTS §7b item 2 — the classical limit
is a functor applied at q=1, not a q-family).

**F4 — the KL carrier.** The positive KL element `b_s = σ + q⁻¹` has channel
eigenvalues `([2]_q, 0)`: identically `b_s = [2]_q·e₊` and
`b_s² = [2]_q·b_s`; at q=1 it decategorifies to `1 + s` — twice the Young
symmetrizer of S₂. So `e₊ = b_s/[2]_q`, and the ½ at q=1 **is** `1/[2]_1`,
the KL-to-idempotent conversion factor at the decategorification point. The
½ has a canonical KL carrier.

## Net effect on B4

The open statement sharpens from *"q→1 one-loop = a₀·α"* to the single
functorial normalization:

> the loop expansion weights the **q=1 KL-normalized channel projector**
> (`b_s/[2]_q` evaluated at q=1) by the universal heat-kernel unit `a₀·α`.

The carrier is now canonical; the equal-weight and trace-of-crossing readings
are excluded as q-carrying forms (they remain numerically equal *at* q=1 —
resolving that residual coincidence is part of what the functorial statement
must do). **B4 remains OPEN** — this brick derives the carrier candidates and
the discrimination, not the normalization itself.

## Position in the proof plan

```
B1 (ρ reality structure)          MERGED #3955
B2 (functorial statement)         shadow MERGED #3960; lift OPEN (Mathlib-gated)
B3 (conformal inheritance)        MERGED #3969 — Clause A = B2-lift + B4
B4 (classical-limit norm)         THIS brick (B4a) — carrier identified, ½ located at q=1;
                                  remaining: the functorial normalization itself
B5 (assembly)                     blocked on B2-lift + B4
```

Next inside B4: connect the q=1 KL-normalized projector to the heat-kernel
weighting — i.e. why one loop of the tower inserts exactly one `b_s/[2]_q`
worth of channel content with weight `a₀·α` (the physical-normalization leg,
where the McKean–Singer/heat side of B3 must meet the KL side of this brick).
