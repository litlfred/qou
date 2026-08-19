# Overlap sweep of my merged volume-conjecture work — and a parallel Whitehead program nobody referenced

**Date**: 2026-08-19 · **Verdict**: three of four clear; the fourth is not a
duplication but a **convergence opportunity** — a second Whitehead-link
volume-conjecture program exists in the corpus, attacking the same theorem
from the opposite end, and neither side cites the other.

Third in a series: [E–M
retraction](2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md) →
[L4-1 already proved](2026-08-19-l41-was-already-proved-on-main.md) → this.
Having been wrong twice by not grepping, I swept the rest of the merged work
rather than assume it was clean.

## Result per item

| Work | Verdict |
|---|---|
| **4₁ volume conjecture** (`FigureEightVolumeSqueeze`, `tendsto_log_kashaev_vol`) | **Clear, and load-bearing.** It *supplies* `volumeConjecture41_of_literature`, replacing a cited-`sorry` instance with a proof (2026-07-26, bean `qou-f248`). It **predates** the `qou-mlgp` lane (2026-08-08), and that lane does not target the volume limit — its consumers are `KashaevPeakValue` / `KashaevTailBound` / `LobTaylorSaddle`, the saddle program. |
| **Borromean** (`BorromeanVolume`) | **Clear.** No competing proof of `Vol(𝓑₃) = 8G` in the corpus. |
| **Whitehead chain** `W_{a,2,1,0}` (`WhiteheadChainVolume`) | **Clear.** The other Whitehead program targets `W_{0,1,1,0}` — the `b = 1` link, a different object. |
| **L4-1** | Redundant — already recorded and merged. |

**The date boundary is ~2026-08-08.** My work before it was original; the
log-sine asymptotic work after it duplicated the `qou-mlgp` lane. That is a
cleaner statement of the failure than "I don't grep": I stopped grepping at the
point the corpus started moving fastest.

## The finding: a second Whitehead-link VC program

Beans `qou-t2sc` / `qou-dw20` / `qou-1gkf`, files I had never seen:

* [`WhiteheadVolumeConjecture.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/WhiteheadVolumeConjecture.lean)
  (309 lines, 1 `sorry`) — the **van der Veen Lemma-1 positive-sum route** for
  `W_{0,1,1,0}`: `whiteheadS` positivity, the inner sum, the saddle reduction.
* [`WhiteheadSaddleClausen.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/WhiteheadSaddleClausen.lean)
  (825 lines, **sorry-free**) — the saddle **value**:
  `V = 2π∫_0^{1/2}[log 2 + 2 log sin(π(u+¼)) − log sin(πu)]du = 4·Cl₂(π/2) = 4G`,
  ending in `whitehead_vc_innerSum_half`.

**Same theorem, opposite ends, and complementary rather than redundant:**

* **Their end** — the *magnitude*: the inner sum `Σ_k S_{n,k}` at the single
  slice `n = ⌊N/2⌋` has scaled log tending to `4G`. Sorry-free.
* **My end** — the *phases*: `WhiteheadLinkScaffold` /
  `WhiteheadMajorantRate` bound `‖J_N(W)‖` by a majorant, prove the majorant's
  limit is `4G`, and isolate what remains into `VdVWhiteheadLemma4` (phases
  cost at most `N^p`). Still no instance anywhere — genuinely open.

The gap between the two ends is exactly non-cancellation of the outer sum
`Σ_n (2n+1)·χ_{N,n}^{-1}·(Σ_k S_{n,k})`, which is what Lemma 4 supplies. **So
`qou-u1b5` is not redundant, and it is the natural partner of `qou-t2sc`.**

## One caution to flag, stated carefully

`whitehead_volume_conjecture` in that file is **not** the Whitehead volume
conjecture for `J_N(W)`. It takes an abstract `kashaev : ℕ → ℝ` together with

    hk : ∀ N, kashaev N = whiteheadInnerSum N ((N-1)/2)

so it is a statement about `whiteheadInnerSum` at one index, wearing a more
general name. The real `J_N(W)` does **not** satisfy that equality — collapsing
the phased outer sum to one slice is precisely the open problem.

**The file's authors were honest about this**: the docstring says "placeholder
link", the `sorry` is labelled an import-layering artefact, and bean `qou-1gkf`
tracks the fix. The hazard is only for a reader who meets the *name* in a
declaration list — as I did — and concludes the VC is proved. That is the
`AGENTS.md` "conditional-proved ≠ premise-established" shape: the hypothesis is
doing the load-bearing work, and the name does not say so.

Recorded as an observation for the `qou-t2sc` owners, not as a correction to
their work.

## Correction carried into this sweep

The two earlier audits dated the `qou-mlgp` infrastructure to **2026-08-10
19:24**. That is the date of `2c68d7f34`, a **29,711-file repo-wide re-file**
commit, not the work's origin. `git log --follow` gives `2a0d39c28`,
**2026-08-08 22:33**. Both audits and the five beans are corrected. The error
ran in the direction of *understating* the finding — eleven days, not nine;
three days before the L4-1 feasibility pass, not one.

Method note: `--diff-filter=A` is unreliable in this repo for exactly this
reason. Prefer `git log --follow`, or a direct `git cat-file -e <commit>:<path>`
existence check at the commit you care about.

## Actions

1. `qou-u1b5` re-affirmed **open and worth doing**, now cross-referenced to
   `qou-t2sc` / `qou-dw20` / `qou-1gkf`.
2. Cross-reference headers added so each program can find the other.
3. Dates corrected in the two prior audits and five beans.
