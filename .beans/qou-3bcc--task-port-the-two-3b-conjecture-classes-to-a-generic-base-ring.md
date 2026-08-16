---
# qou-3bcc
title: 'TASK: port the two §3b conjecture classes to a generic base ring'
status: completed
type: task
priority: medium
tags:
    - lean
    - wall-side
    - 7c
created_at: 2026-08-08T13:00:00Z
updated_at: 2026-08-15T14:48:16Z
---

Last two survivors of the `wall-side-correct` WEAK-33 read (see
`docs/audits/2026-08-08-lean-ref-molecular-namespace-and-weak-triage.md` §8).
Both are **compile-untested** — deliberately, because parameterising a `class`
rewrites every downstream instance binder, which is wider than a per-block fix.

| module | the `ℝ` |
|---|---|
| `lean/QOU/QGeometricLanglands/q_gl_classical_limit.lean` | `heckeEigenvalue : ℝ → ℝ → Prop`; `hecke_limit : ∀ T : ℝ, heckeEigenvalue 1 T → (T = 1 ∨ T = -1)` |
| `nuclear-interactions/cpt-d6-d7-d8-closure.lean` | `markovTrace : ClosedBraid → ℝ` |

Both look structurally independent of `ℝ`: no ordering, no radical, no `Real.*`.
`q_gl_classical_limit` needs `One` and `Neg` (the literals `1`, `-1`), so
`[Ring R]` is the natural target. `markovTrace` is the Jones invariant, whose
natural home is `ℤ[q, q⁻¹]`, not `ℝ`.

## Method — non-negotiable

**A GENUINE verdict is a compile result, never a read.** This session made three
GENUINE calls from surface reading and retracted all three; a fourth candidate
was refuted only by attempting the port (`opaque` semantics) and a fifth blocked
by an `extends` edge that a file-count actively hid. Attempt the port, then let
the compiler decide.

- Verify with `scripts/lean-direct-cone.sh` (NOT `lake build` — it evicts the
  restored `lake-cache` oleans). `-DautoImplicit=false` per `qou-4r5y`.
- Count the downstream instance binders BEFORE starting:
  `grep -rn "\[q_gl_classical_limit\]\|\[CPTD6D7D8Closure\]" --include=*.lean content/`
- If the blast radius is wide, say so and stop rather than half-porting.

## Definition of done

Either both compile generic with every downstream binder updated, or a recorded
refutation naming what forced `ℝ`.


## Verified complete + closed (2026-08-15)

Both target files are **already ported**; the bean's "definition of done" is met. Verified by compile, not by read (per the Method's non-negotiable).

| module | state |
|---|---|
| `lean/QOU/QGeometricLanglands/q_gl_classical_limit.lean` | `class q_gl_classical_limit (R : Type*) [Ring R]`; `heckeEigenvalue : R → R → Prop`; `hecke_limit : ∀ T : R, … → (T = 1 ∨ T = -1)`. Exactly the `[Ring R]` target this bean specified (weakest idiomatic class carrying `One` + `Neg`). Carries an explicit §7c base-ring rationale in the module docstring. Its single ℝ grep-hit is **prose** (line 26: "no `Real.*`"), not a type. **COMPILE: `lean-direct-cone` → ok=1.** |
| `nuclear-interactions/cpt-d6-d7-d8-closure.lean` | `class CPTClosure (R : Type*) [CommRing R]` with `markovTrace : ClosedBraid → R` and `cpt_trace_preserved` over `R`; `def cpt_closure {R : Type*} [CommRing R] [inst : CPTClosure R]`. The Jones-invariant Markov trace now lives over the generic ring, not ℝ — as this bean argued it should. |

Downstream binders intact (`QOU.lean` import + the `…_at_substrate` rename in `QOU/QGeometricLanglands.lean`); no half-port. No code change needed. Closing completed.
