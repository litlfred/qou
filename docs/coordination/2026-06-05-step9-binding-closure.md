# Step-9 binding closure — coordination ledger (flag-bearer hub)

**Flag-bearer:** PR #1871 (`claude/confident-newton-R8lIx`), 2026-06-05.
**Workplan:** [`docs/workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md`](../workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md).
**Common infra everyone rows toward (use these, do not fork):**
- Per-step status table — [`canonical-derivation-cheat-sheet.md §0/§9`](../canonical-derivation-cheat-sheet.md) (the step-9 box).
- This ledger — sibling roster + direction + report-backs.
- Watcher queues — `todos/{proof,canonical,compute,detangler}-*-queue.json`.
- Precision dashboards — `onepb-status-dashboard.witness.json` (L1), `per-observable-100x-status.witness.json` (L2).
- Anchor regression: the magic-A ⁴He **+5.87% no-fit** number is the falsification target for any ρ·A / n=4 claim.

---

## 0. The direction (which way to row)

Binding is **extensive / additive many-body**, not a per-block density (Δ_λ-as-density is dead, cheat §9.3). The closure is:

$$B(K)=\sum_n B_n,\quad \text{body-order }n=\text{jet/vertical degree }n=\lambda_{\mathrm{SW}}^{(n)},\quad B_n=m_e\!\sum_{p\in\mathcal S_c^{\mathrm{hyp}}}\!\operatorname{Res}_p\lambda_{\mathrm{SW}}^{(n)}.$$

- **Many-body series = jet-order filtration.** 2-body / 3-body / 4-body are jet orders of one generating function `G(x;q)=Σ B_n x^n`.
- **Each term = SW period = residue sum** over **hyperbolic** link-components (non-hyperbolic ⇒ Vol=0).
- **Scale rule ρ·A is OUTPUT** of the q-difference equation `G(qx)=R(q,x)G(x)` (→ Dirac/SW PDE post-τ), **not a fit**.
- **γγ / Breit–Wheeler** = the A≥3 validation channel (bar-even C-even vs bar-odd difference).

---

## 1. Sibling roster + per-PR direction (report-backs appended here)

| PR / branch | Their problem | Which way to row | Report back |
|---|---|---|---|
| **#1784** | binding-link assignment heuristic, chain-vs-Borromean | link-volume = **hyperbolic components of `λ_SW^(n)`**; magic-A `8G` is the n=4 instance — the assignment is the hyperbolicity gate (L4), not a free choice | _pending_ |
| **#1790** | 3-body joint-trace destructive (honest negative for A=3) | don't treat A=3 in isolation — it's the **n=3 term of the body-order series**; the q-difference recursion (L3) couples it to n=2/n=4 | _pending_ |
| **#1778** | all-pairs combiner, A=3 to −13% | structure the combiner as a **body-order series** (2+3+4), not flat all-pairs; this is the additive-series host | _pending_ |
| **#1839** | Residue-A kernel deepening (Lean engine, SDP-zero) | residue-A may **BE** the SW-period residue `Res_p λ_SW^(n)`; align on one residue engine (L1) | _pending_ |
| **#1789** | nuclear-binding derivation-completeness ledger | register the **SW-residue / jet-filtration** framing as the active step-9b direction; share completeness metric | _pending_ |
| **#1762** | 1ppQ roadmap + Geom_full bridge + 5-option attack | step-9a per-knot `Geom_full` wire-up is C1 here; fold the SW-residue route in as the step-9b option | _pending_ |
| **#1811 / #1880** | Q_β fibre / c_3 generating-function recurrence | same **q-difference machinery** (L3); the binding `G` and the Q_β `c_k` recursion share the Habiro kernel — reuse `R(q,x)` extraction | _pending_ |

---

## 2. The ask to every sibling

1. **Report relevant findings here** (append a row in §1 or comment on #1871) — esp. negatives that constrain the q-difference kernel or the hyperbolicity gate.
2. **Use the common infra above** (cheat §9 step-table + this ledger), don't fork a parallel status doc.
3. **Anchor to the ⁴He +5.87% magic-A number** for any n=4 / ρ·A claim.

_Append report-backs below this line._
