# Reeb-bundle sinh holonomy as a bar-antisymmetric source for Q_β c_3 — formalize-first scope

**Date:** 2026-06-05
**Branch:** `claude/qbeta-reeb-sinh-parity-2026-06-05`
**Status:** SCOPING + formalize-first invariant (Lean parity lemma) + cheap pruning probe
**Predecessors (all merged):** PR #1866 (cosh even-parity refuted), PR #1880 (odd-parity reduces to saturated search; q-difference data-blocked) — together these resolve the *closed-form* + *recurrence* axes of PR #1824's generating-function hypothesis for c_3.

## Why this, and why formalize-first

After #1866 + #1880 the c_3 frontier is sharply localized. The closed-form
avatar family is refuted **because every cos/cosh avatar is even in u**
(⇒ c_3 = 0), and the odd extension collapses to the saturated
single-formula search. The structural feature that any genuine c_3 source
must have is therefore **bar-antisymmetry**: c_2 = −1 is bar-SYMMETRIC
(even under the bar involution q ↔ q⁻¹), and c_3 is the **first
bar-ANTISYMMETRIC coefficient**.

The framework already contains a working *even/bar-symmetric* hyperbolic
avatar — the trace-polynomial closed form (cheat-sheet §3):

    P_m(h) = cosh((2m+1)η) / (2 cosh η),
        η = log q,  h = q − q⁻¹ = 2 sinh η,  [2]_q = q + q⁻¹ = 2 cosh η,

which sources the bar-symmetric trace family. (Note `h = 2 sinh η`, the
bar-ODD scalar; `2 cosh η = [2]_q` is the bar-EVEN one — they are
distinct, which is the whole point of the parity split below.) Its natural **odd partner**
is the `sinh` counterpart `sinh((2m+1)η)/(2 cosh η)`, which is exactly the
holonomy that the **Reeb vector field** generates on the state bundle
𝒮 = P ×_G ℂP¹: the Reeb flow `exp(t·R)` is a hyperbolic (`SU(1,1)`-type)
rotation whose `cosh`/`sinh` decomposition splits cleanly into a
bar-even and a bar-odd part.

**Formalize-first** (AGENTS.md §3.3): before any numerical scan over Reeb
holonomy candidates, the prunable invariant is **parity under q ↔ q⁻¹**
(equivalently η ↔ −η). The class of candidates splits exactly by it:

| Reeb component | parity under η → −η | sources |
|---|---|---|
| `cosh(kη)` | EVEN (bar-symmetric) | even c_k (c_2 ✓) — **cannot** source c_3 |
| `sinh(kη)` | ODD (bar-antisymmetric) | odd c_k (c_3 candidate) |

This is the same parity wall that killed the cos/cosh avatars (#1866):
a bar-even object has zero odd content. So the **only** parity-admissible
Reeb source for c_3 is the `sinh` component. That is a Lean-checkable
statement (`Real.cosh` even, `Real.sinh` odd), formalized in
[`QBetaReebSinhParity.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaReebSinhParity.lean)
on this branch — three `simp`/`ring`-level lemmas off Mathlib's
`Real.cosh_neg` / `Real.sinh_neg`.

## The pruned numerical check (necessary, not sufficient)

With the parity invariant formalized, the cheap falsifiable check is:

> Does a `sinh`-based Reeb scalar reproduce c_3's **sign** and
> **cross-anchor swing direction**?

c_3 target (from PR #1831 `c3_target_at`): proton −2.06934, muon −2.02020
(swing +0.0491 — the muon value is *less negative*). A genuine bar-odd
Reeb source `S(η) = f(η)·sinh(kη)` must, at minimum, have:
  - the **right sign** at q₀ (negative), and
  - a cross-anchor swing of the **same direction** (η_proton vs η_muon).

This is a NECESSARY condition that prunes the candidate `k`/normalisation
before any wide search. It does NOT claim closure — per #1880 the c_3
*magnitude* match alone is the saturated single-formula problem; the value
here is whether the Reeb `sinh` *parity + swing structure* survives, which
would make it the first **non-refuted** structural lead for the residue-A
keystone (vs. the closed bracket).

## Deliverables on this branch

1. **Lean parity invariant** (`QBetaReebSinhParity.lean`) — `cosh(kη)`
   bar-even, `sinh(kη)` bar-odd, and the corollary that a Reeb holonomy
   `cosh + sinh` split isolates the bar-odd (c_3-admissible) part as the
   `sinh` term. Sorry-free, LSP-verified.
2. **Pruning probe** (`qbeta_reeb_sinh_parity_probe.py`) — evaluates the
   `sinh`-Reeb scalar at both anchors, checks sign + swing-direction
   against the c_3 target, and records a PASS (non-refuted lead) /
   FAIL (closed) verdict. Reuses `c3_target_at` (PR #1831). No fits.

## Honest expectation

Either outcome is informative. A **swing-direction match** is the first
positive structural signal in the residue-A search since the bracket
closed — it would justify scoping the Reeb-holonomy → q-difference-element
derivation (the structural route #1880 said is the only way to close the
data-blocked recurrence axis). A **mismatch** cleanly adds the Reeb `sinh`
to the refuted bracket with a one-line parity/swing reason.

## References
- Parity wall (even slice empty): PR #1866
- Odd reduction + recurrence data-block: PR #1880
- `P_m(h)` cosh avatar precedent: cheat-sheet §3
- Fibre-vs-observable Im(q) framing: AGENTS.md §"Im(q) at fibre vs observable level"
- c_3 cross-anchor target: `qbeta_utils.c3_target_at` (PR #1831)
- Fibre Composite-4 / Hopf sibling: PR #1811
