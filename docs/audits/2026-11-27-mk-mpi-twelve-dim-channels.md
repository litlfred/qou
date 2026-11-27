# m_K/m_π: the channel choice is not what selects `[3]_q[4]_q` (C5, option 2)

**Date:** 2026-11-27 · **Branch:** `claude/mk-mpi-channel-2026-11-27` · **Bean:** `qou-mk34` (stays open)
· **Builds on:** [`2026-11-27-mk-mpi-selection-status.md`](2026-11-27-mk-mpi-selection-status.md) (PR #9449).

## Question

PR #9449 left one reading of `m_K²/m_π² = [3]_q[4]_q` unexcluded: choosing the channel
`V₂ ⊗ Sym²_q W₃*`. Is that channel forced, or is it one of several?

## Answer

It is one of four, and the choice among them does not matter. Over `U_q(sl₂) × U_q(sl₃)`:

| isotype | classical dim | `dim_q` | first tensor degree in `(V₂ ⊕ W₃*)^{⊗k}` |
|---|---|---|---|
| `V₂ ⊗ W_(0,2)` = `V₂ ⊗ Sym²W₃*` | 12 | `[3][4]` | 3 |
| `V₄ ⊗ W_(0,1)` = `V₄ ⊗ W₃*` | 12 | `[3][4]` | 4 |
| `V₂ ⊗ W_(2,0)` | 12 | `[3][4]` | 5 |
| `V₄ ⊗ W_(1,0)` | 12 | `[3][4]` | 5 |
| `V₁₂ ⊗ W_(0,0)` (colourless) | 12 | `[12]` ≠ `[3][4]` | 11 |

These five are **all** isotypes of classical dimension 12, because no `sl₃` irrep has dimension 2, 4 or 12.

So `[3]_q[4]_q` follows from two premises, neither about channels:

1. the classical multiplicity is **12**;
2. the channel carries a **nontrivial colour** (`sl₃`) factor.

Premise 1 is still the selection. `12` is the integer nearest the classical ratio, and no corpus meson
object supplies it (pion total 6, kaon total 8; PR #9449). So the row stays **Selected**. What changed is
the premise behind the label: "pair (3,4) + channel" becomes "integer 12 + coloured".

## Evidence

- Lean, `folio/quantum-observable-universe/lean/QOU/EightfoldWay/MesonTwelveDimChannels.lean` (generic
  `Field K`, §7c; the only concrete ring is `ℚ` in the inequality witness):
  `classical_dim_twelve_channels` (the classification), `twelve_channel_qdim` (every coloured one has
  `dim_q = [3][4]`), `colourless_channel_qdim`, `qInt12_ne_qInt34_at_two`.
- Probe, `computations/meson/twelve_dim_channel_qdim_probe.py`: exact `sympy` Laurent polynomials. It
  re-derives the table and the first tensor degree with Pieri rules. ALL PASS.

## Does quark content force anything?

It does not. The kaon and pion clasp words carry labels (3,5) and (3,3), and at `q = 1` every function
of them agrees (PR #9449). No map from those labels to the integer 12 exists in the corpus. The open
question is now narrower: **derive the multiplicity 12** (or `[3][4]` directly) from a definition of K
and π. That is bean `qou-mk34`.
