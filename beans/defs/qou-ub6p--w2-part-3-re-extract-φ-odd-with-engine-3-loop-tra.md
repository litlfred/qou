---
# qou-ub6p
title: 'W2 part 3: re-extract φ_odd with engine 3-loop transseries (c₁..c₃ from qbeta-g3-5two-deformed-loops witness) — replaces the flawed c1_printed input'
status: completed
type: task
priority: normal
created_at: 2026-07-24T20:44:55Z
updated_at: 2026-09-08T04:15:35Z
parent: qou-yaz3
---

---

## CLOSED 2026-09-08 — the re-extraction RAN, a month after this bean was queued, and it returned a decisive structural negative

This bean asked for one thing: *"re-extract φ_odd with engine 3-loop transseries
(c₁..c₃ from `qbeta-g3-5two-deformed-loops` witness) — replaces the flawed
`c1_printed` input"*. That is done.

**The artifact:** `computations/probes/qbeta_g3_5two_phiodd_engine_reextraction.py`
→ `qbeta-g3-5two-phiodd-engine-reextraction.witness.json`, computed
**2026-08-30**. Its docstring names this bean's task verbatim — *"W2 part 3: the
φ_odd re-extraction with the ENGINE 3-loop transseries (replacing the superseded
`c1_printed` transcription per the #4161 finding)"* — and delivers all three
upgrades the design called for: U1 exact 3-loop per-saddle models (truncation
O(ħ²) → O(ħ⁴)), U2 sector-constancy sweep as sheet-certification *and* error bar,
U3 rank-3 solve closing the σ₁ leak.

### The outcome is a NEGATIVE, and it is the useful kind

The probe's own framing was *"EITHER outcome is decisive"*. It got the second
one, and located the cause rather than merely reporting a failure:

    gates: held_out False | conjugation False | constancy False
    conjugation_dev 5027.75 | arg spread q/bar 4.14 / 5.47
    phi_odd = -1.507 with sweep_spread 7.60   ← i.e. no value at all

**Verdict, quoted:** *"THE SUBSTRATE IS A TRANSSERIES-RESONANT POINT AND
FINITE-RANK EXTRACTION IS STRUCTURALLY INADEQUATE THERE."* On the imaginary-τ ray
`|x̃| = 1` identically (`Re(u/τ) = 0`), so the GGM (13)-(14) ℓ-tower is
non-decaying; **at the substrate point `x̃ = e^{−4πi} = 1` EXACTLY**, so the whole
ℓ-tower degenerates onto the bare saddle exponents — the same coincidence lattice
as the 2c-2 0/0 node and the W1 pole-family swap. The drifting pseudo-amplitudes
are the tower aliasing into finite rank. Tilting the ray (θ = 0.1..0.35) suppresses
the tower but explodes the magnitude hierarchy (|a₂| ~ 1e20). All recorded.

**Its most consequential output is retroactive:** the #3987 preliminary
`φ_odd = −0.004145` was extracted **at** the resonance with a 2-term model *and*
the superseded (238) transcription, so it *"cannot be a derived σ-pair amplitude
phase"*. That is precisely what this bean suspected of the `c1_printed` input,
confirmed from a direction the bean did not anticipate.

**No φ_odd value is claimed. No fit; no c_k wired.** Scope-(a), method-level.

### The open question is NOT closed by this — where it went

Closing this bean closes the *task*, not the physics. The verdict names the two
live routes and neither is here: (2) a derived on-ray σ-pair φ_odd needs the
degenerate ℓ-tower **resummed** (the deformed M-dictionary lateral machinery), not
better finite-rank numerics; (3) the near-term derived-grade route to the 5₂
bar-odd datum is the **Masbaum cyclotomic face** (the exact Laurent-polynomial
`C_(5₂,n)` has landed) rather than state-integral amplitudes at the resonant point.

### Why the tracker matched the wrong commit

`bean-completion-candidates.py` flagged this on `1c4d35d2db7`, *"chore(beans): W2
complete (qou-3ndf, landed #4149+#4161); queue W2 part 3 — φ_odd re-extraction"*.
That is cause 2 in the tool's own taxonomy — the verb "complete" governs
**qou-3ndf**, and the clause naming *this* bean is the one that CREATED it. The
match was a false positive; the bean turned out closeable anyway, on evidence
from a month later that the matcher never saw. Worth recording: a cause-2 flag
is a reason to distrust the match, not a reason to skip the read.
