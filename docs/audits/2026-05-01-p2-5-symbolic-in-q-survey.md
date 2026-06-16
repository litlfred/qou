# P2.5 audit — symbolic-in-$q$ survey

**Pair**: [`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md) §P2.5
**Branch**: `claude/audit-math-framework-FXlp2`
**Method**: Bulk grep over
[`computations/`](../../computations/)
classifying scripts by sympy capability + early/late $q_0$ substitution.

## Headline

| Quantity | Count |
|----------|------:|
| Total `*.py` scripts | **605** |
| Use `q_parameter.Q` (`Q0_FLOAT`) | 229 |
| Use `Q0_FLOAT` AND import `sympy` | 122 |
| Use `Q0_FLOAT` only (purely numerical) | 107 |
| Currently expose a `polynomial_q` / `symbolic_q` field in their witness | **0** |

**P2.5 is bigger than estimated**: 122 sympy-capable scripts, none
currently emit a polynomial-form. Full refactor is many weeks, not
"one week paper-wide" as the original workplan estimated.

## High-value targets (feed the live mass tower / BW / Hecke pipeline)

| Script | sympy? | Late-substitution? | Status |
|--------|:------:|:------------------:|--------|
| `crt_markov.py` | ❌ | ❌ | Purely mpmath; substitutes $q_0$ at construction |
| `hecke_core.py` | ❌ | ❌ | Purely mpmath; substitutes $q_0$ at construction |
| `hecke_characters.py` | ❌ | ❌ | Purely mpmath; substitutes $q_0$ at construction |
| `mass_endomorphism.py` | ❌ | ❌ | Purely mpmath |
| `tower_binding_full.py` | ❌ | ❌ | Purely mpmath |
| `tower_binding_symbolic.py` | ✅ | partial | sympy version; "hits polynomial explosion at $A=4$" per INFRASTRUCTURE-AUDIT.md |
| `shell_closure_compute.py` | ❌ | ❌ | Purely mpmath; the magic-numbers compute |
| `shadow_price_c_321_q0.py` | ✅ | ✅ | Symbolic + emits final numerical |
| `bw_wenzl_shadow_equivalence.py` (P1.3a) | ✅ | ✅ | Reference example: full symbolic + late substitution |

**Live compute pipeline is purely numerical.** The mass tower's
~99%-of-mass missing terms (per [`AUDIT-crt-k-level.md`](../../computations/AUDIT-crt-k-level.md))
*and* the symbolic-$q$ witness gap are both downstream of the same
infrastructure decision: whether to keep mpmath direct or to pivot
to **CRT polynomial reconstruction** (P2.2).

## Why direct sympy refactor doesn't work

`tower_binding_symbolic.py` already exists as the sympy version of
the tower computation. Per
[`INFRASTRUCTURE-AUDIT.md`](../../computations/INFRASTRUCTURE-AUDIT.md)
§Track A: "sympy too slow → use CRT reconstruction of polynomial
coefficients from mod-$p$ evaluations". Polynomial explosion at
$A=4$ rules out direct symbolic computation.

**The unblocking move is CRT polynomial reconstruction** (workplan
P2.2): evaluate Markov traces at several rational $q_i$, reconstruct
the $\mathbb{Z}[q^{\pm 1}]$ polynomial coefficients, then evaluate at
$q_0$ exactly. Once that infrastructure lands, the live scripts
emit `polynomial_q` from the reconstruction, satisfying P2.5
without the explosion.

## Scope refinement for P2.5

The original workplan grouped 605 scripts under one task. The honest
scope is:

| Tier | Scope | Effort | Status |
|------|-------|-------:|--------|
| **A** | Live mass-tower scripts (the ~10 high-value targets above) | gated on P2.2 | Blocked |
| **B** | Sympy-capable scripts that already keep $q$ symbolic but don't emit `polynomial_q` (~110 scripts) | mechanical: ~1 day | **Tractable** |
| **C** | Purely numerical scripts (107) | not refactor — just label as "evaluation harness" | Documentation only |

Recommended next step: **Tier B**. Add a small `polynomial_q` field
to the witness JSONs of the ~110 already-symbolic scripts; keep
their numerical output for the actual numerical witness. This is
mechanical and immediately tightens the audit story.

## P2.5 status

🟡 **Partial**: scope refined; full refactor blocked on P2.2; Tier
B (~1 day) tractable as immediate follow-up. Tier A (live mass
pipeline) requires P2.2 first.

## Reference example for the canonical late-substitution pattern

[`bw_wenzl_shadow_equivalence.py`](../../computations/bw_wenzl_shadow_equivalence.py)
(written for P1.3a) demonstrates the pattern:

```python
import sympy as sp
q = sp.Symbol("q", positive=True, real=True)
# ... all computation symbolic in q ...
q_0 = sp.Rational("1.10998")
result_at_q0 = sp.N(result_symbolic.subs(q, q_0))
witness = {
    "polynomial_q": str(result_symbolic),     # polynomial form
    "value_at_q0": str(result_at_q0),          # numerical form
}
```

Tier B refactor consists of applying this pattern to ~110 scripts
that already use sympy.
