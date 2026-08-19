# Whitehead-link Volume Conjecture — two programs, and the join

**Opened**: 2026-08-19 · **Status**: both halves live; the join is
`VdVWhiteheadLemma4`, still open · **Beans**: `qou-u1b5` (phases) ·
`qou-t2sc` / `qou-dw20` / `qou-1gkf` (magnitude)

This ledger exists because two independent programs in this corpus have been
proving complementary halves of the same theorem without referencing each
other. Neither is redundant. Read this before extending either.

## The theorem

    (2π/N) · log |J_N(W)(e^{2πi/N})|  →  Vol(Whitehead) = 4G = 4·Cl₂(π/2)

for the Whitehead link `W = W_{0,1,1,0}` in van der Veen's chain notation
(arXiv:math/0611181). Van der Veen's Lemma 1 gives the phased sum

    J_N(W) = φ_N · Σ_{n} (2n+1) · χ_{N,n}^{-1} · ( Σ_{k} S_{n,k} ),
    S_{n,k} = ∏_{j=1}^{n} 2 sin²((k+j)π/N) / sin(jπ/N)  >  0.

## Program A — the MAGNITUDE (`qou-t2sc`, sorry-free)

Files: `QOU/Knot/WhiteheadVolumeConjecture.lean`,
`QOU/Knot/WhiteheadSaddleClausen.lean` (825 lines, sorry-free).

| Result | Statement |
|---|---|
| `whiteheadS_explicit_saddle_tendsto` | `(2π/N)·log S_{⌊N/2⌋,⌊N/4⌋} → 4G` |
| `whitehead_vc_innerSum_half` | `(2π/N)·log (Σ_k S_{⌊N/2⌋,k}) → 4G` |
| `saddle_integral` | `V = 2π∫_0^{1/2}[log 2 + 2 log sin(π(u+¼)) − log sin(πu)]du = 4·clausen(π/2)` |

It handles the inner sum at the saddle slice. It does **not** touch the outer
`n`-sum or its phases.

## Program B — the PHASES (`qou-u1b5`, open at one named point)

Files: `QOU/Knot/WhiteheadLinkScaffold.lean`,
`QOU/Knot/WhiteheadMajorantRate.lean`, `QOU/Knot/WhiteheadPhaseAlgebra.lean`.

| Result | Statement |
|---|---|
| `norm_whiteheadLinkKashaev_le` | `‖J_N(W)‖ ≤ whiteheadLinkMajorant N` |
| `tendsto_log_whiteheadLinkMajorant_vol` | `(2π/N)·log(majorant) → 4G` |
| `whiteheadLink_volume_of_lemma4` | the VC, **conditional** on `[VdVWhiteheadLemma4]` |
| `VdVWhiteheadLemma4` | **open — no instance anywhere in the corpus** |

The majorant is the triangle-inequality bound; the conditional class says the
phases cost at most `N^p`, i.e. the majorant and the true modulus share
exponential growth.

## The join

**The gap between the two programs is exactly `VdVWhiteheadLemma4`.**

Program A bounds one slice from below in the right way; program B bounds the
whole thing from above and reduces the remaining question to non-cancellation
of the phased outer sum. Discharging Lemma 4 is what turns "majorant → 4G" plus
"a slice → 4G" into the VC for `J_N(W)` itself.

So: **not duplicate work, and neither program subsumes the other.**

## Two things to know before touching either side

### 1. `whitehead_volume_conjecture` is not the volume conjecture

`WhiteheadVolumeConjecture.whitehead_volume_conjecture` takes an abstract
`kashaev : ℕ → ℝ` with the hypothesis

    hk : ∀ N, kashaev N = whiteheadInnerSum N ((N-1)/2)

so it is a statement about the **inner sum at one slice**, under a name that
reads like the full conjecture. The real `J_N(W)` does not satisfy that
equality — collapsing the phased outer sum to a slice *is* the open problem.

The file is honest about this (docstring: "placeholder link"; the `sorry` is
labelled an import-layering artefact; `qou-1gkf` tracks the fix). The hazard is
meeting the **name** in a declaration list. This is the `AGENTS.md`
"conditional-proved ≠ premise-established" shape.

### 2. `qou-dw20` and `qou-1gkf` look done but read `in-progress`

`qou-dw20`'s target is "the single open `hsaddle` input of
`whitehead_vc_of_saddle_value`", i.e.
`(2π/N)·log S_{n*,k*} → 4G`. That is `whiteheadS_explicit_saddle_tendsto`, on
`main`, sorry-free. `qou-1gkf`'s convergence target likewise. Both beans were
last updated 2026-08-01/02 and still read `in-progress`.

Not closed here — they are another lane's beans and the owner should confirm
the match rather than take an outside agent's word for it.

## How this ledger came about

A three-audit series in which I found my own work duplicating the corpus:
[E–M retraction](../audits/2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md)
→ [L4-1 already proved](../audits/2026-08-19-l41-was-already-proved-on-main.md)
→ [the overlap sweep](../audits/2026-08-19-volume-conjecture-work-overlap-sweep.md).
The sweep that was meant to find more duplication found this instead: two
halves that fit together. Recorded so the next agent on either side starts from
the join rather than rediscovering it.
