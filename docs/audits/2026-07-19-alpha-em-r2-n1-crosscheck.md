# α_EM R2 cross-check 1 — adversarially hardened (2026-07-19)

**Context:** owner picks after #4074 ("wall = R2 only"): run the n=1
cross-check, then *"take adversarial view; if you can resolve issues then
proceed."* Both done; one real issue found in my own first draft, resolved
by weakening the claim to what survives.

**Probe:** [`computations/alpha_em/alpha_em_r2_n1_crosscheck_probe.py`](../../computations/alpha_em/alpha_em_r2_n1_crosscheck_probe.py)
→ [`alpha-em-r2-n1-crosscheck.witness.json`](../../computations/alpha_em/alpha-em-r2-n1-crosscheck.witness.json)
— 5/5 PASS (hardened form; the withdrawn claim is recorded in-probe).

**Scope guard (STRICT):** consistency + species alignment, **not** a
derivation of R2; the ruling remains the owner's; no fit; nothing wired;
`1/(8π)` stays phase-4.

## The adversarial finding (against my own first draft)

The draft claimed the n=1 coefficient and R2's n=2 measure are "the two
ends of ONE heat trace." **Self-refuted:** the UV end of the *1-form* heat
trace carries the component factor `dim Λ¹ = 2` (`Tr ~ 2·a₀·Area/…`), and
the draft's model check silently divided by 2. The n=2 measure is the
**per-mode** unit on the doubled pair — the per-mode conversion (÷ dim Λ¹)
is precisely part of R2's premise, pinned by the working coefficient's q=1
total (`[2]₁·α/(8π) = α/(4π) = a₀α`, one unit), but it is *not* the raw UV
coefficient of the same trace. Claim withdrawn; hidden division removed;
the factor made explicit (V3).

## What survives adversarial review

1. **Full shared vocabulary, zero retuned constants** — `b₁ = 2g`,
   `Area = −2πχ`, real Δ₁ on H¹(Bring) are identical between the accepted
   n=1 identification and R2's chain; the exact parameter-free ratio
   `(n=1)/(n=2) = 16/3`.
2. **R2's irreducible content, now at full precision**: the
   *per-mode-unit-on-the-pair* premise — numerically pinned by the working
   coefficient, still an identification.
3. **Species alignment**: the accepted, Lean-backed n=1 statement
   ("b₁/Area is the physical zero-mode shift", #2114/#3920) is a physics
   identification of the *same species* as R2. R2 extends an accepted
   dictionary from the IR (harmonic-count) end to the UV (per-mode-unit)
   end — it does not introduce a new kind of claim.

## Bottom line — ruling made

R2 stands with: a second independent leg (the n=1 species alignment), its
premise stated at full precision (per-mode unit on the pair, component
factor explicit), zero remaining functorial or numerical freedom, and one
withdrawn over-claim on the record.

> **🟧 Owner ruling (2026-07-19): R2 is NOT Lean/derived-proved.** It
> remains an unproven physics identification; `1/(8π)` stays phase-4; the
> program's outcome is "derived **conditional on R2**; R2 is open."
> Read-first: [`2026-07-19-alpha-em-r2-owner-ruling.md`](2026-07-19-alpha-em-r2-owner-ruling.md).
