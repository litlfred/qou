# α_EM F-construction T4 — the weight values, derived at q=1 (2026-07-19)

**Bean:** `qou-cjsj` (T4) of milestone `qou-a46k`. Upstream, merged: T1
([#4039](https://github.com/litlfred/qou/pull/4039)), T2
([#4040](https://github.com/litlfred/qou/pull/4040)), T3
([#4042](https://github.com/litlfred/qou/pull/4042)).

**Probe:** [`computations/alpha_em/alpha_em_f_t4_weight_values_probe.py`](../../computations/alpha_em/alpha_em_f_t4_weight_values_probe.py)
→ [`alpha-em-f-t4-weight-values.witness.json`](../../computations/alpha_em/alpha-em-f-t4-weight-values.witness.json)
— 4/4 PASS, sympy-exact.

**Scope guard (STRICT):** conditional on the T1 correspondence; general-q
transport open (fibre-level, not needed for the measure); no fit; nothing
wired; `1/(8π)` stays phase-4.

## Why q = 1 suffices for the wall

B4a (#3973) proved the per-loop measure's ½ is a **decategorification-point
constant** — the q-families were excluded by the q-independence of x. So the
weight values the measure needs live at q = 1 and nowhere else.

## The derivation

At q = 1 both sides' weights are **the same invariant** — normalized
isotypic projector trace — of objects the T1 correspondence matches:

| Side | Computation | Values |
|---|---|---|
| corpus | canonical `y_λ(1)` (`y_lambda_at`) | (¾, ¼) |
| algebra | explicit 4×4 Schur–Weyl: `Tr P_sym/4`, `Tr P_asym/4` (`P_± = (1±s)/2`, complementary projectors) | (¾, ¼) |
| geometry | T1 Chevalley–Weil dims (3,1), normalized by dim H^{1,0} = 4 | (¾, ¼) |

Since the rule (trace of projector / total dimension) is the same on both
sides and carries **no freedom**, and T1 derived the dimensions with zero
adjustable input, the weight values transport exactly under any F matching
channel isotypes to deck isotypes. **The weight leg of the
Reality-realization premise is derived, conditional only on the T1
correspondence.**

## Plan state (milestone `qou-a46k`)

```
T1 cover structure                     MERGED #4039
T2 local monodromy = H₂(i) module      MERGED #4040
T3 ρ-equivariance (deck reality)       MERGED #4042
T4 weight values at q=1                THIS — derived
T5 assembly + F = framework-τ residual next (the last brick)
```

After T5's assembly, the surviving open content of the α_EM per-loop wall
will be exactly the residual identification: *the framework's τ restricts to
this cover-monodromy functor on the relevant data* — plus the general-q
weight transport (fibre-level, not measure-relevant).
