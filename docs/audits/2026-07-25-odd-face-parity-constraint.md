# Odd-face parity constraint on the q-cubic graded split (2026-07-25)

**Branch:** `claude/odd-block-parity-constraint-jcip8e`
**Lean brick:** [`QOU/QBeta/OddDecayWeightParity.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/OddDecayWeightParity.lean)
**Feeds:** sibling PR #4140 (super-DM / Berezinian route), bean `qou-jqof`
(open wall `q_cubic = C1`), hook `qou-1dnr` (c₃ = Berezinian cross-term).

## Context — where this sits in the graded-split wall

PR #4140 Thread 2 narrows the open keystone target to the **graded pair**
`qCubicGradedSplit`: the q-cubic decomposes as

| face | content | bar-parity | trig |
|------|---------|-----------|------|
| **even** | C1 / mass / binding kernel | bar-even | cosh |
| **odd** | GGM / decay | bar-odd | sinh |

with the first even/odd **mixing** order `c₃` realized as the Berezinian
off-diagonal cross-term `B·D⁻¹·C` (`berezinian_offDiag_zero`: the ordinary
determinant equals the Berezinian only block-diagonally; the cross-term is
exactly the higher-order even/odd mixing). The concrete 1ppQ hook (`qou-1dnr`):
the missing Q_β term at `1279 ppb ≈ |c₃|·u³`.

The odd/decay face's bar-oddness is not new here — it is the `(−1)^m` GGM sign
alternation upgraded to a scope-(b) invariant in Door-v
([`QOU/Mass/DoorVParityNoIdentity.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/DoorVParityNoIdentity.lean),
[audit](2026-07-20-qlift-doorV-stokes.md)): a bar-even (cosh) profile has no sign
flip; a genuine bar-odd (sinh) alternation does.

## What this brick adds

A **standalone, on-`main` parity certificate** for the odd face — depending only
on established on-`main` facts (Door-v bar-oddness; the `QOU.QBeta` bar-parity
bookkeeping in `ZBarParity.lean`), **never** on PR #4140's unmerged
`SuperDMBerezinian.lean`. All theorems sorry-free.

| theorem | statement |
|---------|-----------|
| `oddWeight_shadow_zero` | the exactly-bar-odd odd/decay weight `γ` has vanishing q=1 (classical) shadow: `2·φ(γ)=0` for every bar-compatible `φ` (`φ∘σ=φ`) |
| `crossTerm_bar_odd` | the cross-term `c = g·γ` (bar-even even-block dressing `g` × bar-odd `γ`) is itself **bar-odd** — one even/odd mixing flips the parity |
| `crossTerm_shadow_zero` | hence the mixing cross-term `c₃` also has vanishing q=1 shadow |
| `classical_shadow_on_even_face` | for `qCubic = e + g·γ` (`e` bar-even), every bar-compatible field evaluation gives `φ(qCubic)=φ(e)`: the classical mass content is carried **entirely by the even face** |

All four reduce to `QOU.QBeta.fixed_eval_two_mul_kills_bar_odd` /
`bar_even_mul_bar_odd` / `shadow_carried_by_even_part` — the T3-2 shadow
machinery — specialized to the graded split.

## Honest scope — constraint, not closure

Per AGENTS.md §"Before declaring 'refuted'" and §"Axiomatization is NOT a
Proof", this is a **necessary condition** on any derivation of the open wall
`q_cubic = C1`, classified **scope-(b) structural** for the shadow-vanishing
(the cited invariant is the exact parity algebra `fixed_eval_two_mul_kills_bar_odd`,
not a numerical near-match):

- The classical (nonzero q=1) mass/binding content of the graded split **must**
  be sourced by the bar-even even face. The pure bar-odd odd/mixing sector
  contributes **zero** at the bar-fixed point q=1.
- In particular the c₃ "`−2 = J_Hopf(q=1)`" classical near-match **cannot** be
  the pure Berezinian cross-term evaluated at q=1 — that evaluation is forced to
  zero here. This is the T3-2 tension
  ([2026-07-07 a₁ parity-shadow audit](2026-07-07-a1-bar-odd-parity-shadow-investigation.md))
  made precise for the graded split: "exactly bar-odd" and "nonzero q=1 shadow"
  are jointly impossible.

**No c_k value is derived, no registry tier changes, nothing is wired.** This
narrows *how* the split can close (the classical shadow lives on the even block;
the odd/mixing sector's contribution is a pure q-deformation vanishing at q=1),
it does **not** close it. The open wall `qou-jqof` remains open.

## Even-face companion — [`QOU/QBeta/EvenFaceMassShadow.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/EvenFaceMassShadow.lean)

The positive complement to the odd brick (same PR, sorry-free, lean-direct exit 0):

| theorem | statement |
|---------|-----------|
| `evenFace_carries_shadow` | for `qCubic = e + o` (`e` bar-even, `o` bar-odd general) every bar-compatible field evaluation gives `φ(qCubic)=φ(e)` — the even/C1 face carries the whole classical value |
| `oddFace_shadow_null` | `φ(o)=0` — the decay face is classically inert |
| `parity_decomposition_unique` | **the graded split is canonical:** over char-`≠2`, `qCubic = e+o = e'+o'` (bar-even + bar-odd) forces `e=e'` and `o=o'`. Proof: `e−e'` is both bar-even and bar-odd ⇒ `2·(e−e')=0`. |
| `evenFace_shadow_faithful` | corollary — the even face's classical shadow is a split-independent invariant of `qCubic` |

`parity_decomposition_unique` is the structural keystone: the even/odd
(mass/decay) decomposition of the q-cubic has a **single well-defined home**, the
algebraic counterpart of the super-Berezinian block-diagonalization. Together the
two bricks say: the classical mass content lives on the uniquely-determined even
(C1/cosh) face; the odd (GGM/decay/sinh) face and its first mixing cross-term c₃
contribute exactly zero at q=1.

## Corpus-grep (per AGENTS.md STRICT)

- `grep -rln "graded.*split\|q_cubic.*C1"` — the target lives in PR #4140's
  unmerged branch; the open wall `qou-jqof` is genuinely open (not closed
  elsewhere in the corpus).
- The parity machinery consumed (`fixed_eval_two_mul_kills_bar_odd`,
  `bar_even_mul_bar_odd`, `shadow_carried_by_even_part`) is on `main`
  (`ZBarParity.lean`); the odd-face bar-oddness is on `main`
  (`DoorVParityNoIdentity.lean`). No duplication — this is the first application
  of the T3-2 shadow machinery to the graded-split odd face.
