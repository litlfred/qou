---
# qou-fk19
title: 'Red-flag ledger(gemini q-saddle): NON-salvageable confabulations — v_offset(q) ODE, q=exp(2pi i tau) pin, closed-form R(q,x) theta-fn — do not chase'
status: completed
type: task
created_at: 2026-08-02T13:07:40Z
updated_at: 2026-08-02T13:07:40Z
---

## Purpose
Negative ledger from the Gemini "q-deformed saddle-offsets" brainstorm
(2026-08-02, branch `claude/q-deformed-saddle-offsets-bdn992`). Records what is
**NOT salvageable** so a future agent does not re-chase it. The salvageable
threads are separate beans `qou-r307` (1-loop=torsion probe) and `qou-0rp2`
(spherical partition algebra review).

## Non-salvageable / confabulated items
1. **v_offset(q) closed forms + the ODE `dZ/dq = −J(1−q⁻¹)/(Δ_q q)·Z`.**
   No derivation; the "boundary conditions" (Z→∞ at q=1, Z→0 at q→∞) were
   asserted then reversed within the same dialogue. The deuteron offset was
   given as BOTH `−1/sinh(λ)` AND `−2/h ≈ −9.566` in the same conversation —
   internally inconsistent. The sinh/cosh "fermion/boson" v_K,offset(q) formula
   is a transfer-matrix ratio dressed as contact geometry; not a rigorous
   object. Scope-(a): "not derived", not "impossible".
2. **`q = exp(2πiτ)` giving q_0 ≈ 1.110 as a topological requirement.**
   Dimensionally broken: for τ in the upper half-plane |exp(2πiτ)| < 1, but the
   substrate q_0 ≈ 1.10998 is REAL and > 1. The USER caught this in-dialogue
   ("NO THIS IS WRONG"). q_0 is dynamic (varies, big-bang-like), not a frozen
   nome of Bring's curve. Do not adopt.
3. **Closed-form `R(q,x) = θ_1(x;q)·θ_1(xq²;q)·Δ_Bring(τ)` as the binding
   q-difference kernel / q-Painlevé tau-function.** Pure confabulation — no
   derivation from the SW periods; the θ_1 product + "Bring modular
   discriminant" is asserted. The R(q,x) kernel is already an open GAP with its
   own beans (`qou-d8de`, `z2bn`); this "solution" adds nothing rigorous.
4. **Moscrop period matrix / `j(τ_0) = −(5·29³)/2⁵`.** Attributed to
   arXiv:2510.02055 but unverified; even if the paper is real, the pull-back to
   a QOU substrate anchor is confabulated. Verify against the actual paper
   before citing; do not adopt the q_0-from-Bring-coupling claim (killed by #2).
5. **Toroidal-JSJ elliptic-integral route (P_{−1/2}/P_{1/2}, overshoot ≈4.37 at
   q_0).** Already explored AND overclaim-audited in the corpus
   (docs/audits/2026-07-19-qbeta-toroidal-tower-overclaim-audit.md; beans
   `5cts`, `5y1a`, `tl1j`). Gemini's own conclusion ("massive overshoot, open")
   matches the corpus; nothing new. c_3 = −2 is REFUTED as a real-q fibre
   element (registry §3) — Gemini's "c_3 must equal the q=1 Hopf shadow"
   argument does not rescue it.

## Note
Items 1–4 are Gemini confabulations; the framework vocabulary they wear
(Reeb drag, contact chart, jet tower, ν_SDP) is real but the specific formulas
are not derived. Per Critical-distance license: flagged plainly as fitted /
undrived. This bean is a "do-not-chase" marker, not new math.
