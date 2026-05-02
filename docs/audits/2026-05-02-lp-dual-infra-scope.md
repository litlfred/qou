# LP-dual infra scope — refined after refactor-branch audit

## Background

Initial validator pass flagged 58 witnesses as candidates needing
LP-dual fields. After auditing the refactor-computation-framework
branch (`claude/refactor-computation-framework-Dmvva`), the validator
was tightened: the broad hints (`confinement-`, `sdp` alone,
`knot-operator`) over-matched **symbolic certificate** witnesses
and **knot-particle feasibility** SDPs that don't compute LP duals.

## Two coexisting patterns (both legitimate)

| Pattern | Use case | Required fields |
|---------|----------|-----------------|
| **LP/SDP dual** (`lp_dual_solver.py`) | binding-energy / shadow-price extraction | `y0_star`, `y_star`, `active_set`, `primal_obj`, `dual_obj`, `duality_gap` |
| **SDP feasibility** (`joint_tower_sdp_solver.py`) | knot-particle assignment feasibility | `sdp_feasibility`, `sdp_feasibility_status` |
| **Symbolic certificate** (filtration cert) | Wedderburn-block × grade × jet-position structure | `filtration_certificate`, `filtration_shape`, `max_grade` |

The validator now only requires LP-dual fields on the FIRST
pattern. The other two answer different questions.

## After tightening

| | Before | After |
|---|------:|------:|
| Witnesses flagged | 58 | **6** |
| False positives | 52 | 0 |
| Genuine LP-dual targets | 6 | **6** |

The 6 genuine targets needing migration:

1. `fresh-derivation-pn-steps-E-G.witness.json`
2. `lp-duality-check.witness.json` (has `active_constraints`, partial)
3. `paper-six-term-shadow-price-sweep.witness.json`
4. `pn-alpha-lp-dual.witness.json` (has some primal data, partial)
5. `shadow-price-c-321-q0.witness.json`
6. `toffoli-lp-stability.witness.json`

## Migration path per script

Each script should be updated to call:

```python
from lp_dual_solver import solve_operator_selection_lp
result = solve_operator_selection_lp(t, G, n_target)
witness["lp_dual"] = result.to_dict()
```

The result includes all six required fields plus the strong-duality
gap (sanity check). Existing computation logic unchanged; only the
output structure expands.

## Status

Validator infra landed (warn-mode); 6 genuine targets identified.
Migration of the 6 is **deferred to a separate follow-up** so the
H_6 LP probe (4He binding via shadow prices) can proceed on the
new infrastructure rather than blocking on legacy script cleanup.

The `--strict` flag remains available; CI can enforce after
migration completes.

## Refactor branch — no contradiction

`claude/refactor-computation-framework-Dmvva` adds:

- `crt_markov_v2.py` — multichannel CRT (per `2026-05-02-crt-markov-multichannel-design.md`)
- `ew_higgs_sdp_probe.py` — EW/Higgs torus-knot identification SDP (uses `joint_tower_sdp_solver` — symbolic-certificate pattern, NOT LP-dual)
- `frob_filter_cancellation_test.py` — Σ_all symbolic decay test
- `sigma_all_symbolic_decay.py` — symbolic precision schedule
- `y_lambda_wenzl_bridge_n15_n18.py` — Wenzl-bridge n=15..18 extension
- New conjectures: NV-1, FROB-FILTER, electroweak-higgs-torus-link-triplet

None of these contradict the LP-dual infra; they operate on
different problem types (knot-particle assignment, symbolic
filtration certificates, Wenzl-bridge extension). The two patterns
coexist cleanly.
