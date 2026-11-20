---
# qou-uir6
title: 'Omega_2 pairing vs D7: report the faithful-window scan of P(z) as the result; convention-D values are a two-row diagnostic'
status: todo
type: task
priority: high
created_at: 2026-10-12T19:30:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-za3q
---
**Recreated 2026-10-12** (stream 4 of #7735, session_01PmZzY27QHceKGXwNivRt64). The original bean,
its window-scan probe and its data lived only in a stalled container and were lost; the
coordinator searched all 131 `2026-10-1x` branches and found none of them.

## Owner ruling 2026-10-12 — options (ii) + (iii); "still leave issue open"

- **(ii)** Ω₂ is a binding quantity: the scan of `P(z) = Σ_λ w_λ(q₀, z)·tr(ρ_λ Ω₂)` across the faithful
  window `0 ≤ z ≤ h` is THE result.
- **(iii)** The convention-D numbers (`z_D = q³/(q²+1) ≈ 2.93h`, outside the window, where every
  three-row weight vanishes) are kept unchanged and relabelled a **two-row (Temperley–Lieb) diagnostic**.
- Keep this bean and `qou-za3q` open. Do not wire anything into the dashboard.

## Rebuilt scan (PR on branch claude/omega2-markov-window-scan-2026-10-12)

`computations/deltalambda/magnus_omega2_markov_window_scan_probe.py`, 5/5, mpmath 60 dps; P_A(z) is an
exact polynomial built from the committed per-partition `tr(ρ_λ Ω₂)` of the three sign witnesses.
Checks were fixed before any number was computed.

- W1: reproduces the recorded convention-D values −6.921 / −13.931 / −20.466 to ~1e-59.
- W2/W3: weights normalise and are positive across the window.
- W5: `mpmath.polyroots` finds no root the 4000-point grid missed.
- **Result (W4):** roots in `[0, h]`: A=2 none; A=3 at `z = 0.0038235h`; A=4 at `z = 0.0100209h`.
  Sign pattern over (A=2,3,4):

  | pattern | measure of window |
  |---|---|
  | (−,−,−) | **98.998 %** (`z ≥ 0.0100h`) |
  | (−,−,+) | 0.620 % |
  | (−,+,+) | 0.382 % (`z < 0.0038h`, the Molien end z = 0) |

**Against the lost run's recollection** (used only as a comparison, never as a target): "(−,+,+) only
within ~0.4 %h of the Molien end" — confirmed (0.382 %). "(−,−,−) on ≥ 99 %" — **not quite**: 98.998 %,
because an intermediate (−,−,+) band of 0.620 % sits between the two roots, which the recollection did
not mention.

**Reading (not a finding):** the A-dependent sign change the programme targets appears only in a
sliver next to the Molien (z = 0) trace; on essentially the whole faithful window the pairing is
negative at A = 2, 3, 4, as it is at convention D.

## Relabel (iii) done, label only

`diagnostic_frame` key added by hand to the three sign witnesses (deuteron / triton / he4); no number
changed (parsed-equal apart from the new key). The producers do not emit the key yet — regenerating
them would drop it; adding it to the producers is a follow-up.

**Status stays open (owner).** Not established: which z inside the window is physical; any MeV
normalisation; that the closed-form `ocneanuWeight` is the Markov weight system at n = 9, 12 (proved at
n = 3, checked to n = 6).

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## Progress Update (Round 93 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/FaithfulWindowAndPretzelWronskianBrick.lean` with 80-dps probe `computations/probes/faithful_window_and_pretzel_wronskian_brick_probe.py` and witness `computations/probes/faithful-window-and-pretzel-wronskian-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8353 (`feat/qou-b9cj-uir6-upbq-v1eu-v4in-v7ro`, HEAD `026764a8eae99d01d2339d820089a669110ba022`).

## Progress Update (Round 93 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/FaithfulWindowAndPretzelWronskianBrick.lean` with 80-dps probe `computations/probes/faithful_window_and_pretzel_wronskian_brick_probe.py` and witness `computations/probes/faithful-window-and-pretzel-wronskian-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8353 (`feat/qou-b9cj-uir6-upbq-v1eu-v4in-v7ro`, HEAD `026764a8eae99d01d2339d820089a669110ba022`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8353, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
