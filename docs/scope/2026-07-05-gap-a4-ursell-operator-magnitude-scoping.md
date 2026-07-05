# GAP-A-4 class-D — the [1⁴] connected-Ursell-operator magnitude (formalize-first scoping)

**Date:** 2026-07-05 · **Discipline:** formalize-first (AGENTS.md §Formalize-first
probe discipline; §Before declaring "refuted"). Read-only design note — **no
compute, no fit**. Sets up the magnitude leg of the A=4 interface operator so a
future session executes a *gated* construction, not a blind scan.

> **Anti-numerology guardrail (STRICT).** The measured ⁴He super-pairwise excess
> is **2.093×** (`su4-supermultiplet-locality.witness.json`). It is **not** a
> clean q-object (`[2]_q = 2.011` misses 4%; `b₄/b₂÷2 = 2.08` isn't clean). **Do
> NOT reverse-engineer 2.093 to any q-expression** — that is the Rule-14
> hidden-DOF numerology the corpus repeatedly warns against. The operator is
> constructed *parameter-free*; its trace value is then whatever it is (a
> scope-(a) verdict), never a target to fit.

## 1. Where the leg sits

The gate is proved (`QOU/MassTheory/SU4SupermultipletGate.lean`, `C(4,A)=0 ↔ A>4`)
and its locality is confirmed against data (§3 of the class-D scoping note): the
missing ⁴He binding is **≥4-body, A=4-local**, peaking at the unique [1⁴] singlet
(the α). What remains is the **magnitude**: derive the connected 4-body binding
contribution and read off its value at A=4 (compare to the measured 2.093× excess;
`0` at A=6 by the gate).

## 2. The object

In the Mayer/Ursell cluster expansion of the binding, `B/m_e = Σ_k (connected
k-body Ursell term b_k)`. The pairwise-assembly ceiling captures the `b₂`
(disconnected pairwise) content and tops out at `6.079×D` at ⁴He vs `12.72×D`
needed. The **missing object is the connected `b₄`** — the part of the joint
4-nucleon Markov trace that does **not** factor into lower clusters:

    b₄(⁴He) := tr_M( P_{[1⁴]} · β_{4-nucleon} )_connected
             = tr_M(full 4-body) − (disconnected 2+2, 3+1, 2+1+1, 1⁴ parts),

with `P_{[1⁴]}` the projector onto the fully-antisymmetric SU(4) supermultiplet
(the α closed shell). The gate guarantees `P_{[1⁴]} = 0` for A>4, so `b₄` is
automatically A=4-local — no separate locality assumption.

## 3. Formalize-first invariants — prove BEFORE the single b₄ compute

| # | Invariant | Status | Why it gates |
|---|---|---|---|
| **I-loc** | `C(4,A)=0 ↔ A>4` (the [1⁴] cluster is A=4-local) | **DONE** — `SU4SupermultipletGate.lean` | already prunes A>4 |
| **I-par** | The connected `b₄` is **bar-EVEN** (`q↦q⁻¹` symmetric) | TO PROVE (compute + Lean) | the absolute scale is bar-even (I-2, `BarParityExclusion`); a bar-odd `b₄` would live in the p−n channel, not the scale ⇒ wrong object. Decide parity *first*. |
| **I-conn** | `b₄` is genuinely **connected** — NOT a saturating pairwise product | anchor exists: `productModel_3body_nonpos` (`QOU/Mass/BindingRecurrenceSpectral.lean`) already excludes *attractive* binding from any pairwise product | if the "4-body" term factors into pairwise pieces it is already inside the ceiling (6.079×) — the operator must be irreducibly connected or it adds nothing |
| **I-ceil** | Upper bound on `|b₄|` from the trace/Frobenius norm at n=12 | TO CHECK (mirror the ℓ¹-ceiling method) | if `max|b₄| < needed`, the [1⁴] term alone cannot close ⇒ scope-(b) exclusion, stop before scanning |

**Execution order (gated):** prove **I-par** and **I-conn** first. Only if `b₄`
is bar-even AND irreducibly connected does the single `b₄`-at-A=4 computation run;
then check **I-ceil** (can it reach 2.093×?) and record the scope-(a)/(b) verdict.
A wide combiner scan is **not** authorized before I-par + I-conn clear.

## 4. Reuse (do not rebuild)

- `computations/probes/interface_4body_assembly_probe.py` — the 4-body assembly
  scaffold (chain vs complete/tetrahedron); extend to the *connected* projection.
- The complete ⁴He χ (77 partitions) is on main (`…-matrix-m` witness).
- `computations/gram_transfer_quadratic.py` — the exact doubled-Bratteli trace at
  n=12 (clears the dense wall) for the I-ceil norm bound.
- The operator-valued branching combiner cluster (#2369/#2371/#2372) for the
  cross-nucleon projection.

## 5. Anti-duplication

- Do **not** re-run the `f^λ`-sum (5.55 MeV, −80.4%) or the pairwise ceiling —
  both are committed; the connected `b₄` is the *new* object, orthogonal to them.
- Do **not** re-propose the additive/log linked-cluster (DONE, +1.07% but
  overshoots light atoms) or sign-only fixes (ℓ¹-ceiling 0.41<1, proved (b)).
- Do **not** fit 2.093 (guardrail §0).

## 6. Cross-references

- `docs/scope/2026-07-05-gap-a4-interface-operator-attack-scoping.md` — the
  parent class-D attack map (the ×5.10 gap, the graveyard).
- `QOU/MassTheory/SU4SupermultipletGate.lean` (I-loc, proved),
  `QOU/MassTheory/BarParityExclusion.lean` (I-2, the bar-parity machinery for I-par).
- `QOU/Mass/BindingRecurrenceSpectral.lean` — `productModel_3body_nonpos`
  (the I-conn anchor).
- `docs/coordination/option-e.md` — PROBE 2 / A=4 ledger + the ℓ¹-ceiling row
  (the I-ceil method).
- `computations/probes/su4-supermultiplet-locality.witness.json` — the measured
  2.093×/0.944× signature this leg must (parameter-free) reproduce.
