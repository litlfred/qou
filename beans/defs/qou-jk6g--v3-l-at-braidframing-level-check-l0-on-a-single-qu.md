---
# qou-jk6g
title: 'V3: L at braid/framing level + check L=0 on a single quark'
status: in-progress
type: task
priority: normal
tags:
    - 8f-open
    - reorg-2026-10-04
    - 8f-gen
created_at: 2026-08-10T18:23:24Z
updated_at: 2026-10-10T12:23:59Z
parent: qou-8lxd
blocked_by:
    - qou-h0zz
pr: 8229
---

Follows LeptonNumberCarrierChirality.lean: L cannot factor through the UNFRAMED
knot type (mirror must move the carrier; unknot is amphichiral). Corpus already
works at braid level -- AntiparticleCrossingReversalContext's mirror is
sigma_i -> sigma_i^-1 on BRAID WORDS and records that the mirror preserves the
knot type. So define L on braid words / framed objects and check it returns 0 on
a single quark (the B-L = 1/3 quark row currently has nothing behind it -- the
corpus's L table lists only leptons, 'hadrons L=0' is prose).
BLOCKED BY V2: if L needs framing while Y needs framing-independence, they cannot
be the same datum.


## Correction 2026-10-10 — this bean's recorded blocker was DISSOLVED two months ago

Its last line reads:

> BLOCKED BY V2: if L needs framing while Y needs framing-independence, they
> cannot be the same datum.

**`qou-h0zz`'s 2026-08-10 result addresses exactly that, and says so in as many
words:**

> KEY CONSEQUENCE for the writhe-independence tension: `L = sign(w)` is
> writhe-DEPENDENT, and that is FINE. `Y = B − L` still does not factor through
> `w` because `B` varies at fixed `w`. So the "second invariant independent of
> the writhe" is **B** (μ̄₁₂₃), NOT L. **The apparent L-needs-framing vs
> Y-needs-independence collision dissolves:** L needs the BRAID WORD (which
> carries writhe), not a free framing datum.

So the stated blocker is not a blocker: nothing requires `L` and `Y` to be the
same datum, and `L` never needed a *free framing* — only the braid word, which
already carries the writhe. Two months of this bean reading as blocked on a
tension the corpus had resolved.

**And `qou-h0zz` supplies this bean's own ask as a candidate**, which the body
asks for and does not know exists:

> CANDIDATE FOUND: `L(β) = sign(writhe(β))`, parameter-free, matches **6/6**
> corpus rows (both leptons, both antileptons, baryon, gluon unit).

That is `L` defined **on braid words**, which is precisely what this bean's
title asks for ("V3: L at braid/framing level"). It is in the Lean:
`leptonNumber (β : BraidWord) : ℤ := Int.sign (writhe β)`
(`ChiralFermionBraidWords.lean:100`).

### So what is actually left — and the title's second half is where it lives

The title asks two things. The first ("L at braid/framing level") is **done**.
The second — **"check L = 0 on a single quark"** — is **not**, and it is
blocked, but for a different reason than recorded:

- `L = sign(writhe)`, so `L = 0` ⟺ `writhe = 0`. The check is therefore the
  question *"is the quark braid word writhe-balanced?"*
- **There is no quark braid word.** `qou-h0zz` caveat 2, verbatim: *"The QUARK
  braid word is still NOT in the corpus; `w = 0` is ASSUMED (motivated by the
  gluon unit being writhe-balanced). **Every quark row rests on it.**"*

So the honest blocker is `htw2` / `qou-h0zz` (no per-chiral-fermion braid word),
not V2's framing tension. Re-pointed: `blocked-by qou-h0zz`.

**And the body's own premise is now the sharp part.** It says *"the B−L = 1/3
quark row currently has nothing behind it — the corpus's L table lists only
leptons, 'hadrons L = 0' is prose."* With `L = sign(writhe)` in hand, that row
rests on an **assumed** `w = 0` for a word that does not exist — so it is worse
than "nothing behind it": it has an assumption standing in for the object.

Also carried forward, since it constrains any fix: `L` cannot factor through the
**unframed** knot type (`LeptonNumberCarrierChirality.lean` — the mirror must
move the carrier and the unknot is amphichiral), and `L = sign(writhe)` respects
that, since `ν = σ₁¹` and `ν̄ = σ₁⁻¹` are different braid words with `w = ±1`
that both close to the unknot.

**Not a closure** — `sign()` is still a choice of function, not derived
(`qou-h0zz` caveat 1). Tagged `8f-open`.

## Implementation Note (PR #8229)
- Implemented in `folio/quantum-observable-universe/lean/QOU/Eightfold/SkeinResolutionQuarkWritheBalanceWorpitzkyDecupletOrderedContentAndGenerationFilters.lean` and `computations/probes/skein_resolution_quark_writhe_balance_worpitzky_decuplet_ordered_content_and_generation_filters_probe.py` (witness `computations/probes/skein-resolution-quark-writhe-balance-worpitzky-decuplet-ordered-content-and-generation-filters.witness.json`, `f1cdc284e299c69db7b5cdefc55f5ba3d747a9ab`).
