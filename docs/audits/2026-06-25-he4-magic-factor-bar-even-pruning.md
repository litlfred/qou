# ⁴He magic-closure factor must be bar-even — a symmetry pruning of w5tg's "magic-α"

**Date:** 2026-06-25
**Branch:** `claude/he4-magic-bareven-prune-2026-06-25`
**Probe:** [`computations/probe_he4_magic_baryeven_prune.py`](../../computations/probe_he4_magic_baryeven_prune.py)
**Witness:** `computations/probe-he4-magic-baryeven-prune.witness.json` (audit-only, EXPLORATORY)
**Bean:** `w5tg` (Lever 2 — the "magic-α" blocker)

## The blocker

The ⁴He doubly-magic shell-closure factor `f(⁴He)/Z·N ≈ 2.0715` (the +47%
super-additive enhancement over the `Z·N` inter-nucleon pair count; a567
workplan, `binding-factor-f-sequence.witness.json`) has no derived closed
form. a567 logged the two best near-misses — `1+q` (+1.86%) and `2√q`
(+1.72%) — as *"not close enough to claim, not far enough to rule out."*

## The pruning (a parity invariant — scope-(b))

The bar-involution `q ↦ q⁻¹` is the chirality / mirror operation. Per Lever-3
(thb7, A=3 mirror): the **bar-odd** (sinh) channel carries the p↔n (n−p)
isospin asymmetry; the **bar-even** (cosh) channel is mirror-symmetric. ⁴He
has **N = Z = 2**, so it is **self-mirror** under p↔n ⇒ its binding has
**zero bar-odd component** ⇒ the magic-closure factor must be a **bar-even**
function of `q` (invariant under `q ↦ q⁻¹`), i.e. a function of `[2]_q = q+q⁻¹`
alone. (The self-mirror atomic word maps to itself under the bar involution,
so `Δtr(⁴He, q)` — and the extracted `f` — inherit bar-evenness.)

**Consequence — the two published near-misses are structurally excluded:**

| candidate | value @ q₀ | err | bar-even? | verdict |
|---|---:|---:|:---:|---|
| `1+q` (a567) | 2.1100 | +1.86% | **no** | **EXCLUDED** (bar-odd) |
| `2√q` (a567) | 2.1071 | +1.72% | **no** | **EXCLUDED** (bar-odd) |
| `[2]_q` | 2.0109 | −2.93% | yes | admissible — not promoted |
| `[2]_q + (q−q⁻¹)²` | 2.0546 | −0.82% | yes | admissible — not promoted |
| `cosh(2 ln q)+1` | 2.0219 | −2.40% | yes | admissible — not promoted |

The `+1.7–1.9%` proximity of `1+q` / `2√q` is a **coincidence of the
forbidden (chirality-odd) family** — the q-locality / selection-bias trap
(production-vs-exploratory §Antipattern 2) made structural by a parity
invariant. This is a scope-(b) exclusion (a proved symmetry forbids the
ingredient), not merely a scope-(a) magnitude bound.

## Discipline — nothing promoted

Bar-even forms **do** sit near the target (e.g. `[2]_q+(q−q⁻¹)²` at −0.82%).
This probe **deliberately does not promote any of them**: a sub-1% bar-even
near-match selected by AME-match is the selection-bias form of fitting, not a
derivation (Δ_λ gate — no 7th ansatz). The **closure** of the magic factor
stays the open **Demazure crystal-closure / operator-valued LR-branching**
problem (a567's nominated mechanism). This note only **prunes** the search:
remove the bar-odd candidates; constrain survivors to the bar-even
(`= [2]_q`-functional) family.

## Relation to z2bn

Adjacent but distinct: z2bn just proved the binding-**kernel coefficient** τ
is bar-even in `[2]_q` (`tau_bar_even`, PR #2774) — τ is the depth-2
recurrence trace. The **magic factor** here is a separate 4-body object; this
is the orthogonal magic-factor leg of the same bar-even structure. Both say
the binding observables live in the `q ↦ q⁻¹`-symmetric (cosh) sector.

## Reproduce

```bash
cd computations && python3 -u probe_he4_magic_baryeven_prune.py
```

Pure-mpmath; the bar-symmetry argument is q-independent (the q₀ numerics are
illustrative).
