# Geometric `W_λ` — the framing is a pure phase; the observable is framing-free for all blocks

**Date:** 2026-07-12 · **Axis:** s5-so3 keystone geometric `W_λ`, framing/observable ordering ·
**Branch:** `claude/keystone-wlambda-framing-phase-2026-07-12` · **Refines** #3701; follows #3685 /
#3699 / #3681 / #3662. **No fit; sharpens the frontier, does not close the gate.**

## Seifert framing pinned

`f = −1`: Σ(2,3,5) is `−1` surgery on the left-handed trefoil (corpus
[`keystone_colored_wrt_perblock_vs_dq.py`](../../computations/probes/keystone_colored_wrt_perblock_vs_dq.py));
orbifold Euler `e = −1/(2·3·5) = −1/30 ≠ 0`. The verdict below is framing-value-independent (any
`f≠0`), so `|f|=1` is not tuned.

## The framing is a pure phase → observable framing-free for ALL blocks

#3701 wrote the fibre→observable residual as the framing monomial `θ_λ^f = q₀^{f·c(λ)}`, trivial on
the self-conjugate electron block (`c=0`). Read through the fibre-vs-observable ordering (AGENTS.md;
#3681 Habiro carrier), the result sharpens:

- `d_q(λ) = [mark]_q` (#3685/#3699) is **real on the unit circle**: for `ζ = e^{iφ}`,
  `[m]_ζ = (ζ^m−ζ^{−m})/(ζ−ζ^{−1}) = sin(mφ)/sin(φ)` — the SU(2) character. So the vacuum-row modulus
  `|S_{0λ}(ζ)| = d_ζ(λ)/D(ζ)` is real and `θ_λ(ζ) = ζ^{c(λ)}` is a **pure phase** (`|θ_λ(ζ)|=1`).
- Hence the fibre probability `|S_{0λ}·θ_λ^f|² = |S_{0λ}|² = W_λ(ζ)` for **every** block — the framing
  phase contributes nothing to the probability (probe: verified at `ζ=e^{2πi/7}`, all 7 blocks).
- `W_λ(q) = d_q(λ)²/D(q)²` is one global rational function whose root-of-unity values are these fibre
  probabilities. By the #3681 Habiro/observable convention (the observable is the continuation of the
  root-of-unity probabilities), the observable `W_λ(q₀) = d_{q₀}²/D²` is **framing-free for all seven
  blocks**, not only the electron.

The `q₀^{f·c(λ)}` residual of #3701 is therefore an **amplitude-ordering artifact** — evaluate the
amplitude at real `q₀` *then* square, where `q₀^{f·c}` is a real factor `≠1`. It is not the physical
(probability) observable. The electron block (`c=0`) is the special case where the amplitude and
probability orderings agree.

## Honest refocus of the open object (anti-laundering)

This does **not** close the gate, and to be clear about what is *not* claimed: the framing being a
phase means it was **never the obstruction to the observable** — the genuine remaining piece is the
**modulus identification**

  `|S_{0λ}^{Σ(2,3,5)}(ζ)| = d_ζ(λ)/D(ζ)`,

i.e. that the **actual colored Lawrence–Rozansky amplitude** of Σ(2,3,5) has vacuum-row modulus equal
to the Hecke quantum dimension. #3685/#3699 supply the **value** (`d_q(λ)=[mark]_q`, McKay-labelled via
2I↔Ê₈ ∘ A₅⊂S₅); the identification with the actual geometric amplitude modulus — the deferred colored-LR
compute — is what remains open. No fit; no constant wired to production; no `Ψ^{(α)}=W_λ` numerology.

Probe + witness:
[`keystone_framing_is_phase.py`](../../computations/probes/keystone_framing_is_phase.py).
