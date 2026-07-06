# 𝔙 ζ₄ coupling: fibre-level (exact) vs observable-level (degenerate) — numerology guard

**Date:** 2026-06-28
**Conjecture:** `conj:binding-qbeta-complex-volume` (𝔙 = Vol + i·CS; Re = 𝔈_bind, Im = 𝔔_β)
**Compute:** [`computations/substrate/frakV_zeta4_fibre_vs_observable_probe.py`](../../computations/substrate/frakV_zeta4_fibre_vs_observable_probe.py)
**Lean:** [`QOU/Mass/ComplexVolumeFibreDescent.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/ComplexVolumeFibreDescent.lean) (§3b class), [`QOU/Mass/Zeta4ComplexVolumeModerator.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/Zeta4ComplexVolumeModerator.lean) (ζ₄ moderator, merged)

## The question

Is the full complex-volume **observable** `𝔙` an exact ζ₄-rotate between `Re 𝔙` (binding) and
`Im 𝔙` (Q_β)? The merged ζ₄ moderator proves the *generator-level* coupling `cosh(η+iπ/2)=i·sinh η`;
this probe tests whether it lifts to the observables — and finds it must **not** be tested there.

## Result

| level | status |
|---|---|
| **Observable** (q₀ real, `Im(q₀)=0`) | **degenerate** — the ζ₄-rotate of a real Re-channel is pure imaginary (`Re = 0`); the two real observables `𝔈_bind`, `𝔔_β` are **not** observable-level ζ₄-rotates |
| **Fibre / generator** (`Im(q)≠0`) | **exact, Lean-certified** — `cosh ↔ i·sinh`; `Φ₄ = q²+1` is the shared ζ₄ = i residue |

1. **Observable level is degenerate (the guard).** At the substrate anchor q₀ is real
   (`η = log q₀` real, `Im(q₀)=0`). `cosh(η+iπ/2)=i·sinh η` is pure imaginary, so
   `Re(ζ₄-rotate of the real Re-channel) = 0` (verified symbolically and numerically). The two real
   observables are independent real MeV values; "are they ζ₄-rotates" at the observable level is a
   category error — testing it numerically would be a **numerology trap** and a fibre-vs-observable
   level conflation (AGENTS.md *Im(q) at fibre vs observable level* banner).
2. **Fibre level is where the coupling lives** and is exact: the ζ₄ moderator is the precise form of
   the corpus assertion that Q_β (bar-odd sinh) is the **sinh partner of the bar-even cosh** scale.

## The §3b descent class (Track C)

`ComplexVolumeFibre V` states the descent's structural content — `Re V` bar-even (binding), `Im V`
bar-odd (Q_β) — and the natural model `V₀(η)=cosh η + i·sinh η` is given as a **non-vacuous**
instance. **No instance is given for the trace object** `𝔙 = E₀·tr_M((Π_free−1)∘ℳ)`: that the
framework's *actual* binding and Q_β observables descend from a single `V` remains the **open
conjecture** — advanced (generator coupling proved), not closed.

## Why this matters

It prevents a future agent from "closing" `conj:binding-qbeta-complex-volume` by a spurious
observable-level numerical ζ₄ match. The honest status: **generator-level ζ₄ coupling proved;
fibre-level kernel descent open; observable-level test degenerate (must not be used).**
