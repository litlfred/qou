# GAP-A-4 class-D scoping — the A=4 interface operator (Δ_λ magnitude closure)

**Date:** 2026-07-05 · **Discipline:** formalize-first (AGENTS.md §Formalize-first
probe discipline). Read-only scoping; no new fit-based ansatz (Δ_λ gate). This
note maps the ~40-probe A=4 (⁴He) interface-operator graveyard, isolates the
genuinely-untried structural levers, and states the formalize-first invariant
that should gate each *before* any wide search — the class-D complement to the
now-landed I-1/I-6/I-2 gate trio (`QOU/MassTheory/TraceConventionGate.lean`,
`QOU/MassTheory/BarParityExclusion.lean`).

> **Status: DRAFT (stub).** The verdict table + untried-lever ranking are being
> synthesized from the T2–T18 probe docstrings, the option-E ledger, and the
> A=4 non-closure audits. This section will be filled before the PR leaves
> draft. Building this scoping note does **not** propose a new ansatz — it
> classifies what is refuted and names the one/two formalize-first invariants
> worth proving next.

## 1. The gap

The per-isotope binding closure `B(K)/m_e = Σ_λ y_λ χ^λ(β_K) Δ_λ(K)` is closed
for the co-Casimir-refuted / bar-parity-pruned classes (gate trio). The open
frontier is the **⁴He magnitude**: an `f^λ`-sum interface object reportedly
reaches ~5.5 MeV against `B_AME(⁴He) = 28.30` MeV — a **×5.1 gap**. Per the
"a compositional/trace object is already many-body" principle (AGENTS.md
§Before declaring "refuted"), the question is whether the gap is a *missing
higher-order/cross term* or a *wrong per-λ weight*.

## 2. Refutation map (to be filled)

_Verdict table: probe/lever → attempt → verdict + scope-(a)/(b) → backing
invariant. Source: `computations/gap_a4_T*_probe.py`,
`computations/a4_interface_*.py`, `docs/coordination/option-e.md`._

## 3. Untried structural levers (ranked, to be filled)

_The 1–2 genuinely-untried attacks + the formalize-first invariant
(parity / degree / orbit-count / entropy bound) that gates each._

## 4. Anti-duplication flags (to be filled)

_"Untried" ideas that are in fact already refuted — named with probe + verdict —
so no later session re-proposes them._

## 5. Cross-references

- Gate trio (landed): `QOU/MassTheory/TraceConventionGate.lean` (I-1/I-6),
  `QOU/MassTheory/BarParityExclusion.lean` (I-2),
  `docs/scope/2026-07-02-gap-a4-perknot-density-rule-scoping.md`.
- `docs/coordination/option-e.md` — PROBE 2 / A=4 non-closure rows.
- `docs/audits/2026-06-23-interface-operator-derivation-and-4body-assembly.md`.
- `docs/coordination/s5-so3-keystone.md` — the owner-authorized geometric `W_λ`
  route (class C), the alternative magnitude source.
