# Aufbau order from the dominant-eigenvalue channel — the duality lever (promising, not a derivation)

**Date:** 2026-06-20
**Branch:** `claude/zealous-hypatia-05xyp9` (PR #2348, bean `e2nf`)
**Compute:** [`computations/aufbau_eigenvalue_channel.py`](../../computations/aufbau_eigenvalue_channel.py)
**Owner question:** "third categorical object? are we using duality / the Frobenius
pairing correctly? if we have something on compact and something on noncompact,
can duality replicate structures?"

## The result

`T_γe` eigenvalues: `λ₊ = q₀` (dominant), `λ₋ = −1/q₀` (sub-dominant),
`λ₊·λ₋ = det = −1` (bar-dual, duality-tracker **D1**). The angular `ℓ` can couple
on three channels, and **only the dominant-`λ₊` one reproduces the empirical
Aufbau order**:

| channel | object | key | `a` | fill order |
|---|---|---|---:|---|
| (A) sub-dominant `λ₋` via ratio | `(λ₋/λ₊)^ℓ = q^{−2ℓ}` | `n−2ℓ` | −2 | `6h 5g 4f…` (high-ℓ first) — #2531 |
| **(B) dominant `λ₊`** | **`λ₊^ℓ = q^{+ℓ}`** | **`n+ℓ`** | **+1** | **`1s 2s 2p 3s 3p 4s 3d 4p…` = Aufbau ✓** |
| (C) compact loop-trace `V_ℓ` | `[2ℓ+1]_q ~ q^{+2ℓ}` | `n+2ℓ` | +2 | `1s 2s 3s 2p…` (ns-dominated) |

## The duality answer (and why it's the best lever yet)

The Markov/Frobenius pairing `V̂(n) = z(Tⁿ)₁₁+(Tⁿ)₂₁ ~ λ₊ⁿ` is **Perron-dominated
by `λ₊`** — that is *why* the radial energy is `λ₊ⁿ`. If the angular `ℓ` couples
through the **same** dominant `λ₊` (channel B), then radial `n` and angular `ℓ`
enter the key **symmetrically** → `n+ℓ` = Madelung. The compact↔noncompact
duality (**D1**, `λ₊↔λ₋`) is exactly the choice of channel: the **noncompact-
Perron** reading (`λ₊`) gives Aufbau; #2531's **sub-dominant** reading (`λ₋`)
gives anti-penetration. So "use the Frobenius pairing correctly" ⇒ use its
Perron-leading eigenvalue `λ₊` for *both* radial and angular ⇒ Aufbau order.

This **supersedes** my earlier "radial:angular scale balance" framing: the issue
is not a tunable magnitude ratio but **which eigenvalue channel** the angular
couples to, and Perron-dominance singles out `λ₊`.

## Two honesty caveats — why this is promising, NOT a derivation

1. **`a=+1 ⟺ Madelung` is partly definitional.** The Madelung rule *is* "fill by
   `n+ℓ`," so "(B) matches Aufbau" is built in once you assert `a=+1`. The
   non-trivial content is the structural claim *"radial and angular share the
   dominant `λ₊`, hence enter symmetrically."* That claim — not the order-match —
   is what would need proving.

2. **The Frobenius *trace* of `V_ℓ` is the q-dim `~λ₊^{2ℓ}` (a=+2), not `λ₊^ℓ`
   (a=+1) — a factor of 2.** Because `dim V_ℓ = 2ℓ+1`, the natural Frobenius
   (loop-trace) object carries `2ℓ`, giving channel (C) which **overshoots**.
   Getting channel (B) needs the angular to enter as `λ₊^ℓ` (ℓ *open* dominant
   transfer steps) rather than the *loop-trace* `λ₊^{2ℓ}` — i.e. the **"half"**
   (`√` q-dim, the `2ℓ+1 → ℓ` reduction). The pairing alone does **not** force the
   open reading over the loop-trace; that is the open structural choice.

## Verdict

The duality / Perron-Frobenius angle is the **right place to look** and the most
promising lever so far: it explains *why* Aufbau wants the dominant `λ₊` channel
(symmetric `n,ℓ`) and *why* #2531's sub-dominant `λ₋` gives the wrong sign. But it
is **not yet a derivation** — the remaining gap is sharp and singular:

> **Why does the angular `ℓ` enter as `λ₊^ℓ` (open transfer, a=+1) and not as the
> Frobenius loop-trace `λ₊^{2ℓ}` (q-dim, a=+2)?** Equivalently: the `2ℓ+1 → ℓ`
> "half" / `√`-q-dimension. Forcing it gives Madelung; assuming it to match is
> fitting.

So Gap-2 is now localized one notch finer than the #2531 synthesis: from "the
ℓ-coefficient `a`" to **"the open (`λ₊^ℓ`) vs loop-trace (`λ₊^{2ℓ}`) reading of
the angular channel"** — a `√`/half-dimension question the Frobenius pairing
poses but does not settle.

## ⚠ Correction (2026-06-20, same day) — the `√`-q-dim bridge is REFUTED at `q₀`

Caveat 2 above proposed the `2ℓ+1 → ℓ` "half" = `√`-quantum-dimension as the
bridge to `a=+1`. **Tested at the real `q₀` and refuted**
([`aufbau_eigenvalue_channel.py`](../../computations/aufbau_eigenvalue_channel.py),
`√`-q-dim section): the `a = q-power` framework assumed `[2ℓ+1]_q ~ q^{2ℓ}`
(large-q), but **`q₀ ≈ 1.11` is near 1**, where `[2ℓ+1]_q ≈ 2ℓ+1` (classical).
There `½ln[2ℓ+1]_q ≈ 0.56` (ℓ=1) **≫** the radial spacing `lnq₀ ≈ 0.10`, so the
`√`-q-dim screening is **ℓ-dominated** (`1s 2s 3s 4s … 2p 3p …`) — **not** Aufbau.
The full q-dim is the same. So the "half/`√`" was a large-q artifact; it is **not**
the bridge.

**What survives:** the *only* object that reproduces the Aufbau order is the
**exact dominant-eigenvalue power `λ₊^ℓ = q₀^ℓ`** (matches through 4s<3d, …; a
benign 4d/5p `K=6` tie aside) — and it is **not** the `√`-q-dim. So "use the
Frobenius pairing's dominant eigenvalue" still points at the right object, but
the *derivation* of "angular `ℓ` enters as `λ₊^ℓ` (ℓ open dominant-transfer
steps)" is **not** supplied by the q-dim or its root — those overshoot at `q₀`.

**Honest net (and a pattern worth recording):** every attempt this session to
*derive* the `a=+1` angular weight from a cleaner categorical object — the q-dim
loop-trace (a=+2), its `√` (refuted here) — **overshoots at the physical `q₀`**.
The exact `λ₊^ℓ` works but rests on the un-derived "angular = ℓ λ₊-steps"
reading. Gap-2 (ordering) is therefore **genuinely open**: the duality/Perron
lever names the right eigenvalue (`λ₊`) and the right order (Aufbau), but no
categorical object tested *forces* the `λ₊^ℓ` (open) reading over the
overshooting trace. Three structural-derivation attempts (eigensplit a=−2;
q-dim a=+2; `√`-q-dim) have now each been ruled out by sign or overshoot.

**Per owner directive (STRICT): the ordering is NOT accepted as a semi-empirical
input.** Madelung's known fragility in standard QM (Cr, Cu, Pd exceptions) is
*why* a categorical derivation is hard — not a licence to accept it. The ordering
stays an **open derivation target**: prove that angular `ℓ` enters as `λ₊^ℓ` (ℓ
dominant-channel open-transfer steps) from the braid topology of the open
electron strand, exactly as radial `n` enters as `n` dominant curls.
