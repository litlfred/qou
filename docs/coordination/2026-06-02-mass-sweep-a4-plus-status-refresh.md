# Mass-sweep A≥4 atom→knot rule — 2026-06-02 status refresh

> Short status refresh for the A≥4 atom→knot rule gap, written as
> Branch C of the post-PR-#1690 dashboard tranche. Honest disposition:
> **no new derivation this session** — the gap is research-grade and
> blocked on objects being built by sibling PRs (#1712, #1443/#1524).

## What's open (STATUS.md row)

> Mass-sweep gap (A ≥ 4) | mean abs err 4.25%; ⁶Li / ⁷Li / ⁹Be / ¹¹B /
> ¹⁴N / ¹⁹F GAP (no atom→knot rule)

[STATUS.md](https://github.com/litlfred/qou/blob/claude/atom-knot-rule-a5plus-coord-2026-06-02/STATUS.md).

## Authoritative state of the gap

The honest current state is captured in two existing docs (no
new substantive math has landed since 2026-05-30):

1. [`docs/workplans/2026-05-29-a567-atom-knot-sdp.md`](https://github.com/litlfred/qou/blob/claude/atom-knot-rule-a5plus-coord-2026-06-02/docs/workplans/2026-05-29-a567-atom-knot-sdp.md)
   — the full workplan (with retraction).
2. [`docs/coordination/2026-05-30-a567-and-alpha-em-coupling.md`](https://github.com/litlfred/qou/blob/claude/atom-knot-rule-a5plus-coord-2026-06-02/docs/coordination/2026-05-30-a567-and-alpha-em-coupling.md)
   — the cross-thread coordination state.

### What survives the discipline bar (2026-05-30 critical-audit)

| structural piece | status |
|---|---|
| Δtr = ‖tr_M(free)‖ − ‖tr_M(atom)‖ from canonical `atom_braid_word_3A` | derived |
| Vol(Borromean) = 8G (Catalan / dilog identity) | derived |
| Factorisation form B = m_e · Vol(K_bind) · Δtr (Kashaev-class) | derived in form |
| f(Z,N) = B_AME / (m_e · 8G · Δtr) | AME-extracted, **not derived** |

### What was retracted as derivation (remain leads)

- `f ≈ Z·N` for D / 6Li / 7Li (0.19–0.62% near-match) — selection-bias
  fitting, not compute-precision derivation.
- ⁴He shell bonus 2.07 ≈ 1+q (1.8%) and ≈ 2√q (1.7%) — also retracted.
- κ_Coulomb ≈ 2√3 / (3π) (935 ppm off) — also retracted.

Source: workplan §"Critical-discipline audit (2026-05-30)" +
[`#1444` retraction comment](https://github.com/litlfred/qou/pull/1444#issuecomment-4581427035).

## What's blocking each level

| Level | Object needed | Where derived |
|-------|--------------|---------------|
| **A=2** (²H) | binding-link PSD-feasibility of L_H (Hopf) at H_3 | live in [PR #1712](https://github.com/litlfred/qou/pull/1712) Test plan item 1 |
| **A=3** (³H, ³He) | binding-link PSD-feasibility of 8_11-class at H_5 | live in [PR #1712](https://github.com/litlfred/qou/pull/1712) Test plan item 2 |
| **A=4** (⁴He) | derived shell-closure bonus (≈ 2.07, retracted) | open — needs operator-valued LR branching, blocked on [#1443](https://github.com/litlfred/qou/pull/1443) + [PR #1524](https://github.com/litlfred/qou/pull/1524) IwahoriHecke Sprint 2 |
| **A≥5** (5/6/7Li, 9Be, 11B, 14N, 19F) | derived K_bind(Z, N) generator | gated on A=4 |

## Recent landings (since 2026-05-30 audit) that touch the gap

- **#1690** (merged today): dashboard wiring + Lean sibling fill + q₀
  drift fixes. **No new derivation**, just regenerates witnesses at
  current q₀.
- **#1593** (Q_β c_3 order audit): the per-block Δtr_M is O(√u); ladder
  c_3 is O(u³) — accidental cross-order coincidence. This is *upstream*
  of the binding-factor f decomposition: the Hecke-block structure of
  Δtr_M is now characterised at compute precision, which clarifies that
  any f(Z, N) derivation must respect the bar-symmetric / paired
  structure shown at u¹ in #1602.
- **#1602** (Q_β eigenphase Taylor in u): "eigenphase = f" FALSIFIED at
  u¹. The cos eigenphase has a nonzero u¹ coefficient `−√3 / 12`.
  Constraint on the Q_β scaling map carries over: any f(Z, N)
  derivation that goes through a single eigenphase will also
  inherit a u¹ obstruction.
- **#1622** (Habiro q-difference Fourier mode-solve): partial-fraction
  decomposition of Δtr_M(u = √q) into three sectors — entire poly + ζ₄
  cyclotomic + Laurent tower. The ζ₄ cyclotomic sector's bar-even
  content is **exactly 1/2** (a clean constant). This is a *structural
  characterisation* of Δtr_M that any A≥4 binding-factor derivation
  must respect.
- **#1641 / #1643** (Φ_q signed-vs-modulus): the `‖·‖` in the
  factorisation form is a structural CHOICE, not a convergence
  requirement; at v = ±0.142 the signed/modulus ratio diverges 13.3×.
  Per-site audit on the binding-factor pipeline still pending.

## Live sibling PRs in scope

| PR | Scope | This branch's relation |
|----|-------|------------------------|
| **[#1712](https://github.com/litlfred/qou/pull/1712)** | m_p linking_weight (2.532780 → 2.461648) + ²H/³H binding-link canonical object | **direct overlap on A=2, A=3 levels**. Will post intent comment. |
| **[#1709](https://github.com/litlfred/qou/pull/1709)** | volume-Wedderburn Δ_λ probe; q-6j saddle isolated | adjacent — Δ_λ closure path runs in parallel to f(Z, N) derivation |
| **[#1713](https://github.com/litlfred/qou/pull/1713)** | Q_β Habiro fibre F(q) categorical ID | upstream — closes the same Hecke-block structure that A≥4 derivation needs |
| **[#1714](https://github.com/litlfred/qou/pull/1714)** | KL recursion S_5 / S_6 scaffold | upstream for Option-E PROBE 4; Demazure crystal closure path |
| **[#1516](https://github.com/litlfred/qou/pull/1516)** | Option-E Phase 2 H_3 + H_6 + PROBE 4 | parallel Δ_λ path |

## What WOULD be a productive next probe (next session, not this one)

Per CLAUDE.md Δ_λ gate ("**do not propose a seventh fit-based
ansatz**") and the 2026-05-30 retraction (selection-bias fitting is
forbidden), the productive directions are:

1. **Wait on PR #1712's PSD-feasibility test at A=2, A=3.** If L_H
   (Hopf) for ²H and 8_11-class for ³H pass PSD-feasibility at q₀,
   that's the binding-link canonical object derived. *Then* extend to
   A=4 via operator-valued LR branching (still gated on #1443 + Sprint 2).
2. **Wait on PR #1713's fibre F(q) identification.** If the Q_β Habiro
   element lands, the same fibre construction applies to the
   binding-factor f(Z, N) via the shared multi-Wedderburn-block
   structure recorded in the 2026-05-30 coord doc.
3. **No new ansatz attack** without one of the above first. The retracted
   leads stand as suggestive structure; they are NOT to be re-pitched
   as a new derivation candidate without a categorical chain replacing
   selection-bias fitting.

## This branch's scope

- One coord refresh (this doc)
- One intent comment on PR #1712 noting the A=2, A=3 overlap
- **No new derivations, no new code, no new witnesses, no production wiring**

This is a *coordination* PR, not a math PR. The math gap is real and
will close when #1712 + #1713 + #1443/#1524 each land their respective
upstream pieces.

## Cross-refs

- CLAUDE.md §Precision goals (L2 trio shared root)
- CLAUDE.md §Δ_λ gate (no 7th ansatz)
- CLAUDE.md §"Before declaring open math" checklist (corpus-grep)
- [`docs/coordination/2026-05-30-a567-and-alpha-em-coupling.md`](https://github.com/litlfred/qou/blob/claude/atom-knot-rule-a5plus-coord-2026-06-02/docs/coordination/2026-05-30-a567-and-alpha-em-coupling.md)
- [`docs/workplans/2026-05-29-a567-atom-knot-sdp.md`](https://github.com/litlfred/qou/blob/claude/atom-knot-rule-a5plus-coord-2026-06-02/docs/workplans/2026-05-29-a567-atom-knot-sdp.md)
