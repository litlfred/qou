# Chirality-Δ_λ binding wired all-A — the bare dim magnitude diverges (2026-06-17)

**Branch:** `claude/delta-lambda-bring-quadratic-2026-06-17` (PR #2417)
**Wires:** the PROVED per-block factor `Δ_λ = sgn(w₀^{S_λ'})·dim(V_λ)` (keystone
`S5SO3FiberAction.lean` / PR #1305 / audit
[`2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md`](2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md))
through the all-A χ^λ fine-Bratteli transfer (PR #2405, `tr_m_atom_via_transfer`).
**Discipline:** derive-or-refute; the FORMALIZED formula, no `C_knot` fit; no
production rewire, no witness.

## What was wired (the gap)

The categorical binding `B(K) = m_e·|Σ_{λ⊢3A} y_λ χ^λ(β_atom) Δ_λ|`
(`binding_energy_categorical_deuteron.py`, PR #1307) was only ever evaluated for
the **deuteron** (loaded from a precomputed sum: B(D)=0.380 MeV, −82.9 % vs AME).
[`computations/probes/chirality_delta_lambda_binding_sweep.py`](../../computations/probes/chirality_delta_lambda_binding_sweep.py)
extends that *exact* formula to D…⁷Li using the transfer χ^λ.

## Result — undershoot ≤⁴He, then divergent OVERSHOOT at A≥6

| iso | A | n | #λ | Σ_λ yχΔ | B_pred | B_AME | ratio AME/pred |
|---|---|---|---|--:|--:|--:|--:|
| D | 2 | 6 | 11 | −0.744 | 0.380 | 2.225 | 5.85 (under) |
| T | 3 | 9 | 30 | −3.735 | 1.909 | 8.482 | 4.44 (under) |
| ³He | 3 | 9 | 30 | −4.588 | 2.345 | 7.718 | 3.29 (under) |
| ⁴He | 4 | 12 | 77 | −5.946 | 3.038 | 28.296 | 9.31 (under) |
| ⁶Li | 6 | 18 | 385 | **+256.2** | 130.9 | 31.99 | **0.24 (4× over)** |
| ⁷Li | 7 | 21 | 792 | **+824.6** | 421.4 | 39.24 | **0.09 (10× over)** |

**Cross-check:** B(D)=0.3801 MeV reproduces the deuteron-only compute (0.380) to
the printed digits — the wiring is correct.

## What it shows (sharpens the Δ_λ gate)

The deuteron-only −82.9 % undershoot **masked** the real behaviour. Across A the
sum `Σ_λ y_λ χ^λ Δ_λ` runs −0.7 → −6 (A≤4) → **+256 → +825** (A≥6): it does not
merely undershoot, it **diverges into overshoot** because the magnitude factor
`dim(V_λ)` grows combinatorially (the high-dim deep partitions, ~hundreds of
blocks at n=18,21, dominate). So:

- The **sign** side is fine — `sgn(w₀^{S_λ'})` is the proved ±1 chirality
  (mixed `#sgn± ≈` balanced; bypasses the PROBE-4 KL wall, as designed).
- The **magnitude** side — bare `dim(V_λ)` — is the failure: it is **not** a
  viable all-A binding weight; it blows the sum up beyond A=4.

This is the precise numerical confirmation of the sibling template
([`2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md`](2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md)
§"Why this matters", PROBE 2 #2369/#2371/#2372): *"the interface operator should
supply the per-block magnitude (Wedderburn / quantum-dimension data), with the
sign factored as the chirality."* The bare `dim` magnitude diverges ⇒ the open
piece is **exactly** the interface-operator-corrected magnitude (not the sign,
which is proved, and not a global `C_knot` fit, which the deuteron retraction
already rejected).

## Magnitude-variant test (2026-06-17) — all four refuted; the LINEAR functional is wrong for A-scaling

Swept four magnitudes in `B = m_e·|Σ_λ y_λ χ^λ Δ_λ|` (sign = the proved
chirality throughout):

| Δ_λ | D | T | ³He | ⁴He | ⁶Li | ⁷Li | behaviour |
|---|--:|--:|--:|--:|--:|--:|---|
| `1` (raw \|tr_M\|) | 0.20 | 0.05 | 0.11 | 0.03 | 0.004 | 0.001 | **decays → 0** |
| `sgn` | 0.05 | 0.03 | 0.03 | 0.005 | 0.0003 | 0.0001 | **decays → 0** |
| `sgn·dim` (proved) | 0.38 | 1.91 | 2.34 | 3.04 | 131 | 421 | **diverges** |
| `sgn·dim_q` | 0.40 | 2.50 | 3.10 | 5.83 | 1721 | 17692 | **diverges harder** |
| **B_AME** | 2.22 | 8.48 | 7.72 | 28.3 | 32.0 | 39.2 | ~linear in A |

(B_pred in MeV; cross-check `sgn·dim` at D = 0.380 ✓.) **None tracks AME.** The
two unweighted/`sgn` forms make the bare trace `Σ_λ y_λ χ^λ` **decay** with A
(wrong direction); the two dim-weighted forms **diverge** (`dim_q` at `q₀>1`
worse than bare `dim`). There is no Goldilocks magnitude among the natural
categorical candidates: the trace shrinks, any dim-like weight explodes.

**Structural verdict (sharper than §Net below):** the *linear* functional
`Σ_λ y_λ χ^λ Δ_λ` cannot reproduce AME's ~linear-in-A binding with **any**
simple sign×magnitude. The functional with the **correct A-scaling is the LOG**
one — `B_sym = α·ln(tr_free/tr_atom)` (PR #2405), the exact additive (A−1)-bond
chain, which *does* grow ~linearly and lands within ~2× of AME. So the
cooperative α-term should be sought as a **correction to the log chain B_sym**,
**not** via the linear-Δ_λ sum, which is refuted at the A-scaling level (not just
the magnitude). This also reframes the PROBE-2 "interface-operator magnitude":
no per-block scalar magnitude rescues the *linear* functional — the issue is the
functional form, not just the weight.

## Net

The proved `Δ_λ = sgn·dim` factor is real (and the sign side is closed), but the
all-A binding **sum** is refuted twice over: as `sgn·dim` it diverges (≥⁶Li), and
across the full magnitude family `{1, sgn, dim, dim_q}` **none** tracks AME's
A-scaling. The categorical binding with the right A-scaling is the **log** form
(`B_sym`, #2405), not the linear `Σ_λ y_λ χ^λ Δ_λ`. So: sign = chirality
(closed); the linear-Δ_λ functional = refuted for the bulk; the cooperative
α-term is a correction to the **log chain**, the genuinely open piece (Δ_λ-gate /
α-unit magnitude, which the discipline blocks from fitting). No fit, not wired.

## Cross-links
- [`2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md`](2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md) — the proved sgn·dim decomposition + PROBE-2 template.
- `computations/binding_energy_categorical_deuteron.py` — the deuteron-only evaluation this extends.
- `computations/tr_m_atom_via_transfer.py` (PR #2405) — the all-A χ^λ transfer used here.
- [`2026-06-17-delta-lambda-master-formula-active-set-redesign.md`](2026-06-17-delta-lambda-master-formula-active-set-redesign.md) — the sibling Δ_λ-route finding (LP/quadratic refutations).
