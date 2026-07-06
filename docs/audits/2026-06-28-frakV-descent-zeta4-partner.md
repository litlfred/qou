# 𝔙 fibre-descent — ζ₄-partner relation + gap map (conj:binding-qbeta-complex-volume)

**Date:** 2026-06-28
**Bean:** `5nx8` (conjecture-gap, deeper descent)
**Conjecture:** `conj:binding-qbeta-complex-volume` — binding (`Re 𝔙`) and Q_β (`Im 𝔙`) descend from
one fibre object `𝔙 = E₀·tr_M((Π_free−1)∘ℳ)` (`= Vol + i·CS`).
**Lean:** [`QOU/Mass/ComplexVolumeZeta4Partner.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/ComplexVolumeZeta4Partner.lean) (sorry-free)
**Compute:** [`computations/substrate/frakV_descent_zeta4_partner_probe.py`](../../computations/substrate/frakV_descent_zeta4_partner_probe.py)

## What this advances

Prior merged work: the §3b descent class `ComplexVolumeFibre` + cosh/sinh model (#2951); the ζ₄
generator coupling `cosh(z+iπ/2)=i·sinh z` (#2941); the observable-level test is degenerate
(`Im(q₀)=0`) so the descent is a **fibre-level** claim, not an observable match (#2951).

**New (ζ₄-partner relation, Lean-certified).** For the model `V₀(z)=cosh z + i·sinh z`, the `ζ₄=i`
rotation `z ↦ z + iπ/2` gives

```
  V₀(z + iπ/2) = −cosh z + i·sinh z          (= −conj V₀(η) for real η).
```

It **negates the bar-even (binding / `Re`) channel and keeps the bar-odd (Q_β / `Im`) channel** —
the precise fibre-level signature of how `ζ₄` couples the two channels of `𝔙 = Vol + i·CS`. This is
one structural step beyond the generator coupling: the moderator acts on the *generators*
(`cosh ↔ i·sinh`); the partner relation acts on the *model object* `V₀`.

## Gap map — what closing the descent still requires (and what is gated)

| piece | status |
|---|---|
| `Re 𝔙` binding fibre kernel | **characterized, not closed** — q-Hermite/Rogers–Szegő moment with a Habiro `(q−1)·cyclotomic` log-coefficient tower (#2899/#2929); **not** a finite low-order q-difference operator (Stages 3–4, held-out-falsified) |
| `Im 𝔙` Q_β fibre kernel | **GATED** — the `c_k` Habiro element / SW-residue jet-prolongation symbol `R(q,ξ)` (`conj:qdifference-kernel-prolongation-symbol`); fitting `Φ₂` is the forbidden "seventh ansatz" (2026-06-09 scope) |
| single fibre `𝔙` (the descent) | **OPEN** — proved: ζ₄ generator coupling + ζ₄-partner relation + bar-parity class. Missing: both fibre kernels **and** their assembly into one `tr_M` trace object |
| observable-level match | **DEGENERATE** (`Im(q₀)=0`) — must **not** be used to claim closure (numerology guard) |

## Verdict (honest)

The descent is **advanced, not closed**. The ζ₄ structural layer (generator coupling → partner
relation → bar-parity class) is now Lean-certified; the kernel descent is **open and partly gated**
on the Q_β SW-residue keystone, and the observable-level test is degenerate. Closing
`conj:binding-qbeta-complex-volume` requires the two fibre kernels and their trace assembly — not a
numerical observable identity.
