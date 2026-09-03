# The Q_β `c_k` ladder under convention D: what parity pins, and what it leaves open

Bean `qou-cds1` (tranche S1 of the 2026-08-15 convention-D ruling).
PR #5748, branch `claude/qbeta-ck-ladder-convention-d-2026-08-25`.

**Outcome: the ladder does NOT close under convention D, and the block is
located precisely.** Bar-parity derives half of the D-frame eigenphase and
provably cannot supply the other half. Scope-(a) per AGENTS.md
§"Before declaring refuted". Nothing is wired; no `c_k` value, tier, or channel
registration changes.

Artifacts:

* [`computations/qbeta/qbeta_d_frame_eigenphase_window_probe.py`](../../computations/qbeta/qbeta_d_frame_eigenphase_window_probe.py)
  (+ witness `qbeta-d-frame-eigenphase-window.witness.json`)
* [`content/quantum-observable-universe/lean/QOU/QBeta/DFrameEigenphaseBarOdd.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/DFrameEigenphaseBarOdd.lean)
  — nine theorems, sorry-free, `#print axioms` clean on all nine.

## 1. What the wall actually is

The bean and the surrounding prose describe `QOU.QBeta.decayLadder_zC_threeRow_ne_zero`
as the reason the C→D move is not a `z`-swap. That theorem is real and it is
sorry-free, but it is worth stating what it does and does not say, because it is
easy to over-read.

**What it says.** Fix `s > 1` with `q = s²`. Suppose `z` is the C-frame ladder
parameter, i.e. `z·(s + s⁻¹) = 1`. Suppose `y₃, y₂₁, y₁₃` satisfy the three
Markov conditions on `H₃(q)` — normalisation, `tr(σ)`, `tr(σ²)` — at that `z`,
and suppose the trace is faithful (`y₂₁ ≠ 0`). Then `y₁₃ ≠ 0`.

So: **at the C parameter, the third Wedderburn row is forcibly present.** The
trace does not factor through Temperley–Lieb. Since the mass channel's forcing
runs the other way (`y₁₃ = 0 ⟹ z = z_D`), "keep the C-frame ladder" and "the
two-row forcing applies to the decay channel" cannot both hold.

**What it does not say.** It is a statement about `z_C` only. It says nothing
about substituting `z_D`, and on its own it does not forbid that substitution —
it forbids *retaining C while claiming the two-row structure*. The theorem that
actually blocks the substitution is a different one in the same file:
`eigenphase_bar_defect_of_fullBar`, which shows that feeding a full-bar
parameter into the C-frame eigenphase formula leaves a bar defect of exactly
`h²`, `z`-independently. That is the parity-side block, and it is the one this
work builds on.

Both blocks are needed, and they are about different things — one about which
rows the trace carries, one about the eigenphase's parity.

## 2. The hypothesis class and the invariant

**Class.** D-frame ladders `Q_β/Q_A = cos(α − u/2)·Π_{k≥2}(1 + c_k u^k)` with
`α = (ζ − 1)h/2` and `ζ` built from `z_D`.

**Invariant.** Bar-parity. Every downstream consumer of the ladder — (H1)
`c₃^even = −Vol(4₁)`, the `S_leak` program, `q*_S`, the KC13 prune — rests on
`α` being bar-ODD. Under C that is free: `z_C` is bar-even. Under D it fails.

**What parity pins.** Shift the parameter by `c = ce + co` (bar-even plus
bar-odd). Then

    bar(2α) + 2α = h·(h + 2·co)        [`generalShift_bar_defect`]

with **`ce` and `z` both absent**. So bar-oddness forces `co = −h/2` uniquely
(`barOdd_forces_oddPart`), and constrains `ce` not at all. The canonical member
(`ce = 0`) is

    z_D^even = z_D − h/2 = (q⁴+1)/(2q(q²+1)),   bar-even
    α_D^odd  = (z_D^even − 1)·h/2

and this is a **re-derivation, not a substitution**: `loopMean_eq_twoQ_mul_moment`
gives `2z − h = [2]_q·Ξ` in any convention, so `z_D^even = [2]_q·Ξ/2` is exactly
the weight-determined half of the Markov parameter (under D,
`Ξ = (1+q⁴)/(1+q²)²`), while the bar-odd half is the universal `h/2`.

This does **not** contradict `LadderPhaseFromWeights.no_weight_function_gives_phase`,
which excludes the weights determining the *full* `α`. The bar-odd projection is
strictly weaker, and it is the projection that is pinned.

> **Correction made mid-session.** The first version of this argument claimed the
> bar-odd shift is unique full stop. It is unique only within `h`-proportional
> shifts. `generalShift_bar_defect` is what establishes the correct, weaker
> statement, and the difference is the entire remaining gap.

## 3. Measurement (proton anchor; muon agrees to the anchors' 11.5 ppb)

Harness calibrated against two independently recorded answers before it was
trusted: it reproduces C's `c₃ = −2.06934258` and the bean's naive-D
`c₃ = −974.43`.

| candidate | eigenphase `A` | implied `c₂` | `c₃` | `|r₂/r₁|` |
|---|---|---|---|---|
| C, as recorded | −0.05659474 | **−1.0176** | −2.0693 | 0.017 |
| D, naive `z`-swap (banned) | −0.04474439 | −9.2989 | −974.43 | 0.893 |
| D, bar-odd derived (§2) | −0.05567095 | **−1.7331** | −86.081 | 0.423 |

The derived candidate improves the banned substitution by 11× and brings `|c₃|`
from 974 to 86, but does not reach the structural `c₂ = −1`.

**The window.** `c₂ = −1` is structural — the N=2 rung *is* `1 − u²` — so the
evidence for the ladder shape is that the empirically implied `c₂` lands near
`−1`. Asking AGENTS.md's question (*is the offset forced, or merely in range?*):
landing within `|c₂ + 1| ≤ 0.02` demands the eigenphase to **4.5×10⁻⁴
relative**. The C and derived-D candidates differ by **36 window-widths**; the
naive swap by **463**.

**The swing is not a discriminator.** The cross-anchor `c₃` swing, which the
corpus uses as the f-map search discriminator, is phase-independent to 0.5%
(ratio to C: 1.0052 naive, 1.00026 derived). It carries almost no information
about the trace convention.

**What the data actually demand.** The parameter that would give `c₂ = −1`
exactly is `z* = 0.4991045` — **0.043 % from `z_C`**, 1.81 % from `z_D^even`,
22.8 % from `z_D`. This is the sharpest statement of the situation: the ladder's
empirical content is *"z is within 0.043 % of `z_C`"*, which is why the C-frame
ladder looked derived, and the ruling says the trace parameter is `z_D`.

## 4. Where it blocks, and what would unblock it

Parity supplies the bar-odd half of the D eigenphase and provably leaves the
bar-even half free. The even shift that would close the ladder is

    ce = z* − z_D^even = −0.0090534

which is bar-even and therefore **not excluded by parity**. So the negative in
§3 is about the canonical member `ce = 0`, *not* about convention D as such.

**Unblocking requires deriving `ce` from convention-D data.** Two guards for
whoever attempts it, because `ce` invites precisely the near-match this corpus
keeps burning sessions on:

1. **`ce ≈ −u` is inadmissible, not merely missed.** `ce/u = −1.0630` looks like
   `−u` at 6.3 %. But `u` is not bar-even — `bar(u)/u = q²`, verified
   symbolically, because `ℏ_q` is not bar-even — while `h²` is. Parity excludes
   the candidate outright.
2. **`ce` is resolved to only 1.45 % (68.8σ).** From `σ(Q_β)/Q_β = 7.8×10⁻⁷`,
   `ce = −0.0090534 ± 0.00013`. `ce/h² = −0.207142` sits 1.7×10⁻⁴ from
   `(√2−1)/2` — **84× below experimental resolution**. Any identification of
   `ce` quoted to more digits than 1.5 % is reporting the arithmetic, not the
   measurement. Combined with the ~2.7 % window on `ce`, the entire game is at
   the couple-of-percent level, where many simple bar-even expressions live.

## 5. Scope

**Scope-(a)** per AGENTS.md §"Before declaring refuted": *this construction —
the C-frame ladder shape with the derived bar-odd D eigenphase — alone does not
reproduce the `c₂ = −1` band.* It constrains a magnitude, not an ingredient.

It is **not** scope-(b). No proved invariant excludes convention D from the
ladder. What is proved is narrower and is stated above: the bar-even part of the
eigenphase is outside parity's reach, and the specific candidate `ce = −u` is
excluded.

Two further honest limits. The ladder's *shape* — that `α` enters as
`cos(α − u/2)`, that the rungs are `(1 + c_k u^k)` — is asserted upstream in
both frames and is untouched here; §3's `z*` measurement is what says the
re-derivation must change the shape, not merely the parameter. And every `c_k`
conclusion in the corpus remains convention-C-frame and un-re-derived.
