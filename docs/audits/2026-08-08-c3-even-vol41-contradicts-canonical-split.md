# c₃'s two "S"s do not share epistemic status — plus two self-corrections

> ## 🛑 CORRECTED TWICE, SAME DAY (2026-08-08) — read this first
>
> This audit was wrong twice, in opposite directions. Both errors are left
> visible; the surviving contribution is small and is stated plainly at the end.
>
> **Error 1 — the `κ·S` cross-check was CIRCULAR.** I claimed the `κ·S` split
> independently refutes `c₃^even = −Vol(4₁)`. But `S` is *defined* as
> `S := a₁/κ_(2,1)` with `a₁ = −c₃`
> ([`qbeta_s_complex_volume_rigidity_probe.py:69`](scripts/qbeta_s_complex_volume_rigidity_probe.py);
> [`2026-06-13-qbeta-root-of-unity-residue-program.md:177`](2026-06-13-qbeta-root-of-unity-residue-program.md)),
> so "reconstructing" it is an identity. The tell: agreement of `4.1e-5`/`1.1e-5`
> sits *inside* the 4-significant-figure rounding window (`5.5e-5`/`5.6e-5`) of
> the quoted `908.4`/`886.8`.
>
> **Error 2 — "(H1) is UNDERIVED, no derivation exists in the corpus" is also
> FALSE**, in the opposite direction. The Φ_b state-integral saddle supplies the
> `|S|` scale from geometry, **fit-free and anchor-blind**: at the real substrate
> meridian the saddle gives `Im 𝔙 = 0` exactly (amphichirality) and a volume
> deficit `0.0094 ≈ |S(muon)| = 0.00968` (PR #3654; [2026-07-12
> capstone](2026-07-12-c3-wall-resolution-capstone.md) result 5; registry
> **KC21**, tier symbolic-exact). That *is* a geometric motivation for
> subtracting a `4₁` volume.
>
> **Root cause of error 2:** AGENTS.md's corpus-grep checklist item 4 is *"check
> the relevant coordination ledger"*. I grepped `docs/`, `content/`,
> `computations/` for the strings `S_leak` and `c₃^even` and **skipped the
> ledger**. KC21 is indexed under Φ_b / volume-deficit / ladder vocabulary — a
> string search for my own framing could never have found it.
>
> **Also not new:** the "209× cancellation amplification" I reported is the
> corpus's known `1/u³` ladder artifact (capstone result 3: the extractor is
> `c₃ = (Q_β/Q_N2 − 1)/u³`, and `S′(q*) = 2.37 × (1/u³)` is a *smooth* `O(1)`
> prefactor). And the Skein factorisation I landed this morning — bar-odd
> `= (q − q⁻¹) × bar-even` — is the corpus's `S = h·D(ũ)` with `h = q − 1/q`
> (KC21). Both independently re-derived, neither discovered.

**Date:** 2026-08-08 · **Bean:** `qou-qb8f` · **PR:** #4742
· **Tier:** scope-(a); two claims withdrawn (see banner). Surviving finding: the two-S collision
· **Discipline:** no fit, no wiring, no tier change, no Lean edited.
Applies AGENTS.md §"Defined residual ≠ derived decomposition (STRICT, 2026-08-08)"
to the case that motivated it — and then to the arbiter I reached for.

## The question

Raised — deliberately **not adjudicated** — in
[#4724](https://github.com/litlfred/qou/pull/4724) when an `S_leak`-based
candidate filter was retracted.

[`SLeakZeroCrossing.lean:11`](../../content/quantum-observable-universe/lean/QOU/QBeta/SLeakZeroCrossing.lean)
defines

```
S_leak(q₀) := c₃(q₀) + Vol(4₁)
```

and reads it as *"the bar-odd residual of c₃ after removing the bar-even
amphichiral `−Vol(4₁)` face"*. That reading requires

> **(H1)** `c₃^even = −Vol(4₁) ≈ −2.0299` — exactly.

## Why the anchors cannot answer it

`c₃^even(q) = (c₃(q) + c₃(1/q))/2` requires c₃ at `q ≈ 0.901`. Both substrate
anchors sit at `q ≈ 1.10998`; the bar-partner `1/q_proton ≈ 0.900918283956` is
not an anchor. **No anchor data determines the bar-split** — it must come from an
assumed structural form.

## What I did, and why it was wrong

I tried to adjudicate (H1) against the corpus's other decomposition
([`2026-07-07-c3-even-solved-s-complex-volume-rigidity.md`](2026-07-07-c3-even-solved-s-complex-volume-rigidity.md) §2):

```
c₃^odd = κ_(2,1)(q) · S,      κ_(2,1)(q) = (q−1)³(q+1)/q²
```

treating that audit's quoted `S_p ≈ 908.4`, `S_μ ≈ 886.8` as independent data.
Inverting `c₃ = −κ·S` under `c₃^even = 0` returned them to ~1e-5, which I read as
confirming c₃ is purely bar-odd, hence `c₃^even ≈ 0`, hence (H1) refuted.

**`S` is defined as that quotient.** Two sources, both explicit:

| source | line |
|---|---|
| `qbeta_s_complex_volume_rigidity_probe.py:69` | `# S = a_1/κ_(2,1) = Q_β/E₀ at the two anchors` |
| `2026-06-13-qbeta-root-of-unity-residue-program.md:177` | `bar-ODD a_1 = -c_3 … carrier κ_(2,1) = (q-1)³(q+1)/q²` |

So `S := a₁/κ = −c₃/κ`, exactly the formula I "verified". I divided the same
numbers the same way and recovered them.

| anchor | reconstructed | quoted | rel dev | 4-s.f. rounding window |
|---|---|---|---|---|
| proton | 908.3624831 | 908.4 | 4.13e-5 | **5.5e-5** |
| muon | 886.7905751 | 886.8 | 1.06e-5 | **5.6e-5** |

Both deviations lie *inside* the rounding window. That is what identical numbers
look like.

**Root cause:** I treated "quoted in a different audit" as equivalent to
"independently derived", without tracing the provenance of the cross-check
target. That is the same error class as the one under audit — accepting a
defined quantity as a derived one.

## The corrected finding

Both named "splits" of c₃ are **definitions**:

```
S_leak := c₃ + Vol(4₁)          ← definition
S      := −c₃ / κ_(2,1)         ← definition
```

Each takes c₃, applies a fixed transformation, and names the result as though it
were an independently meaningful part of c₃. The probe verifies c₃ is recovered
*exactly* from either, both ways (`< 1e-40`) — the hallmark of a
reparametrisation, which adds no information. Consequently:

* the `κ·S` split **does not refute (H1)** — it says nothing about it;
* the `κ·S` split is **not itself a derived decomposition** of c₃;
* **the bar-parity of c₃ is undetermined by the present corpus** — the anchors
  cannot supply it, and neither named split is derived.

## A parity tension, recorded not resolved

`κ_(2,1)` is verifiably bar-odd (`κ(1/q) = −κ(q)`, checked symbolically at four
points, `< 1e-40`). The 2026-07-07 audit also says `S` "inherits bar-odd from
`Q_β`". But bar-odd × bar-odd = bar-**even**, which would make `c₃ = −κ·S`
bar-even and the label `c₃^odd` a misnomer.

The resolution is that `S`'s parity is not independent data: with `S := −c₃/κ`,
`S`'s parity is whatever makes the identity hold. So the tension is not a
contradiction — but it does confirm that the split carries no parity
information, which is the corrected finding above, arrived at from a second
direction.

## What survives, unchanged

**(A) The bar-split is inaccessible from the anchors.** Both sit at
`q ≈ 1.10998`; the split needs `q ≈ 0.901`.

**(B) `S_leak` is a cancellation artifact.**

| anchor | c₃ | `+ Vol(4₁)` → `S_leak` | cancelled |
|---|---|---|---|
| proton | −2.06934258 | −0.039459367 | **98.093%** |
| muon | −2.02020024 | +0.0096829728 | **99.521%** |

```
anchor swing of c₃      2.4325%      ← real
anchor swing of S_leak  507.51%
amplification           208.63×      ← arithmetic
```

**This is not new.** It is the corpus's known `1/u³` ladder artifact: the
extractor is `c₃ = (Q_β/Q_N2 − 1)/u³` with `u ≈ 0.0085`, and `S′(q*) =
2.37 × (1/u³)` — a *smooth* `O(1)` prefactor over a tiny `u³`
([capstone](2026-07-12-c3-wall-resolution-capstone.md) result 3; KC21). The
capstone's verdict is that **"the wall was never physical."** Re-derived here
independently, not discovered.

Arguments using the *absolute* difference `|S₁ − S₂|` are unaffected — the
offset cancels there identically.

**(C) ~~(H1) remains underived~~ — WITHDRAWN.** See the banner. The Φ_b saddle
supplies the `|S|` scale from geometry, fit-free and anchor-blind (volume deficit
`0.0094 ≈ |S(muon)| = 0.00968`, PR #3654, KC21 tier symbolic-exact). What is
still open is narrower: the match is a **~2.9% scale agreement**, not an exact
identity; the exact normalisation is open; and `conj:im-q-physical-role` remains
a **conjecture**. So (H1) *as an exact identity* is not established — but
"unmotivated" was false.

## The surviving contribution: the two "S"s do not share epistemic status

Two distinct objects are both called *"the c₃ bar-odd `S`"*:

| object | value at muon | status |
|---|---|---|
| `S_leak = c₃ + Vol(4₁)` | +0.00968 | **geometric backing** — Φ_b saddle volume deficit, fit-free, anchor-blind (KC21) |
| `S := −c₃/κ_(2,1)` | 886.79 | **definition** — carries no information (§ above) |

They differ by ~5 orders of magnitude (ratio 91582.5).

The [2026-07-12 capstone](2026-07-12-c3-wall-resolution-capstone.md) **straddles
them**: its header and numbers (`S(muon)=+0.00968`, `S(proton)=−0.03946`) are
`S_leak`, while its result 1 states *"the c₃ bar-odd `S = Q_β/E₀`"* (≈ 886.8).

This matters because **conflating them transfers unearned credibility** from the
geometrically-backed object to the definitional one. `SLeakZeroCrossing.lean`
carries a symbol-collision guard, so the collision is known — but the capstone
still crosses it, and KC21 inherits the same vocabulary.

> **THIRD NARROWING (2026-08-08).** The collision is **already guarded in the Lean
> file itself**. `SLeakZeroCrossing.lean` has carried, since before this audit, a
> section headed *"The object (notation-collision guard, AGENTS.md §'attributes do
> not transfer')"* stating that `S_leak` is `O(0.01)` and sign-flips, is
> **distinct** from `QOU.QBeta.SRigidity.S = Q_β/E₀` which is `O(900)` and does
> not, and *"Do not conflate the two symbols."* My own `qou-qb8f` bean recorded
> that guard on the morning of the same day — and I then presented the collision
> as this audit's unanticipated finding anyway. Withdrawn.
>
> What is left, and it is narrow: the **2026-07-12 capstone document** crosses the
> collision the Lean file guards — its header and numbers are `S_leak` (≈0.0097)
> while its result 1 says `S = Q_β/E₀` (≈887). A documentation defect in one audit
> doc. That is the whole of this audit's original content.
>
> **Partly anticipated — cite, do not claim.** The `S = h·D(ũ)` half of this was
> already re-scoped by
> [`qbeta-c3-qstar-k31-repin.witness.json`](../../computations/qbeta/qbeta-c3-qstar-k31-repin.witness.json):
> *"the carrier is anchor-blind (spread 1.23e-9) and is NOT the swinging
> empirical S, so `'S=h·D(u)'` is **schematic, not a tight identity** (the swing
> is the 1/u³ extractor, #3636)."* What appears **not** to be recorded elsewhere
> is the narrower documentation defect: the capstone's *result 1* states
> `S = Q_β/E₀` (≈ 887) while its own header and numbers are `S_leak` (≈ 0.0097)
> — two objects five orders apart inside one document. That, and only that, is
> this audit's unanticipated part.

That, and the honest record of two wrong turns, is this audit's actual
contribution. It is smaller than the two claims it replaces.

## Scope

**Scope-(a)** throughout. Not refuted: `Vol(4₁)` as an ingredient elsewhere;
`4₁`'s amphichirality; and **any theorem** in `SLeakZeroCrossing.lean`,
`SLeakMagnitudeOffsetRatio.lean`, `SLeakMagnitudeTaylorRatio.lean` —
`sleak_zero_between_anchors`, `sign_definite_carrier_excluded`,
`linear_ratio_slope_independent`, `exact_ratio_factorization` are each stated for
a *generic* function with the anchor signs (or a simple zero) as **hypotheses**,
and stand exactly as written.

**No Lean was edited.** The theorems are correct; only interpretive prose is at
issue, and those files belong to a sibling's active area (#4734 notified, twice —
including a correction of what I first told them).

## A correction to the bean that raised this

`qou-qb8f` cited `c₃^even ≈ +86.66` as a rival value. Wrong twice: it is a
**projection artifact** (the 2026-07-07 audit says so itself — *"the honest rungs
are the `e_k`"*), and it is a **different object** (the k=3 rung of the bar-even
channel of `log R`, not the bar-even *part of* the c₃ coefficient). Same glyph,
two referents.

## Reproduce

```bash
python3 -u computations/qbeta/c3_even_canonical_split_contradiction.py
```

11/11 assertions, ~1 s. `auditOnly`; no witness emitted, no fit, nothing wired.

## What stays open

* **`qou-qb8e`** — the c₃ magnitude channel: the actual open gate.
* **`qou-qb8g`** — c₃'s bar-parity is *undetermined*, not zero. Establishing it
  needs a genuinely derived decomposition, which neither current split is.
* Whether the registry's c₃ row should note that both splits are definitional
  (registry maintainers' call).

-- Ref: [manuscript] `docs/audits/2026-07-07-c3-even-solved-s-complex-volume-rigidity.md`
-- Ref: [manuscript] `docs/audits/2026-06-13-qbeta-root-of-unity-residue-program.md`
-- Ref: [manuscript] `docs/audits/2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md`
