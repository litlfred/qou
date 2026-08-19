# The bar-odd c₃ action's closed-form home is ℚ(√−7) — via the owner's dilog-identities paper + the verified 5₂ volume

> **🛑 RETRACTED (2026-08-11) — the premise is false. 5₂'s invariant trace field
> is the CUBIC field of discriminant −23, not ℚ(√−7).**
>
> The opening sentence below reads the geometric trace field off `det(5₂)=7`.
> The determinant is an **Alexander-polynomial** datum — `Δ(t) = 2t²−3t+2`,
> `disc = −7`, `det = |Δ(−1)| = 7` — and ℚ(√−7) is genuinely attached to 5₂ **as
> the abelian layer**: the quadratic subfield of ℚ(ζ₇), where the metabelian data
> of the ℤ/7 double branched cover lives. It is not the geometric SL₂(ℂ) trace
> field, and **cannot** be a subfield of it: `[ℚ(√−7):ℚ] = 2` does not divide
> `[K:ℚ] = 3`, so the tower law forbids the embedding outright. That is a
> **scope-(b) structural exclusion on a proved invariant**, not a numerical
> near-miss — no precision improvement can rescue it.
>
> The quadratic field that *is* attached to K is **ℚ(√−23)**, the A₃-fixed
> subfield of the S₃ Galois closure. The corpus's own A6 σ-pair tower already
> records the bar-odd line as √−23.
>
> **What survives.** The Hakimoglu-Brown ℚ(√−7) identities verified in §Verified
> (1) are correct — they are simply not about 5₂ (the paper contains no
> occurrence of "knot", "hyperbolic", "volume", or "trace field"). The
> `Vol = 3·|D(z₁)|` structure in (2) is also correct, but it is *forced*, not a
> discovery: at m = 1 the gluing equation gives `z₂ = 1/(1−z₁)`, a standard
> six-fold Bloch–Wigner partner for which `D(z₂) = D(z₁)` is the textbook
> identity. It carries no field information either way. **No action value was
> claimed here and none is retracted** — the §Anti-laundering note was correct.
> What is retracted is the field a search should run in.
>
> Certification: [`qbeta_5two_trace_field_disc23_not_qsqrt7.py`](../../computations/probes/qbeta_5two_trace_field_disc23_not_qsqrt7.py)
> · correction: [`2026-08-11-5two-trace-field-is-disc-minus-23.md`](2026-08-11-5two-trace-field-is-disc-minus-23.md)
> · bean `qou-ynff`. Document retained rather than deleted, per corpus practice.

**Date:** 2026-07-18 · **Axis:** c₃ / Q_β bar-odd swing / 1ppQ · **Tier:** numerical
scope-(a)/(b) (paper toolbox verified + a structural ℚ(√−7) decomposition; the bar-odd
*action value* is **not** claimed) · **Discipline:** no fit, no c_k wired, nothing to
production, no tier change.

## Context

The merged b3ix result derived the **4₁ bar-even** Habiro-tail action = **π²/5** exactly
(a ℚ(√5) golden-ratio constant, real-q archimedean face) and flagged that the bar-**odd**
c₃ channel needs the **chiral 5₂** analog. The 5₂ invariant trace field is **ℚ(√−7)**
(`det(5₂)=7`), so the bar-odd action is expected as a **ℚ(√−7)** dilog constant. The owner
uploaded [`uploads/2506.10206v2.pdf`](../../uploads/2506.10206v2.pdf) (Hakimoglu-Brown,
*Analytic dilogarithm identities*), which supplies exactly the ℚ(√−7) closed-form machinery.

## Verified

[`qbeta_5two_dilog_qsqrt7_closed_form_probe.py`](../../computations/probes/qbeta_5two_dilog_qsqrt7_closed_form_probe.py):

1. **The paper's ℚ(√−7) toolbox is correct.** Example 5 holds to 22+ digits:
   `π²/24 − ln²(2)/4 + ⅓·arctan²(√7/5) = Re Li₂((3−i√7)/8)`. (Example 8's ℚ(√−7) ladder
   with `r=(1+i√7)/2` matches on its real part.)

2. **The verified 5₂ complex volume lives in ℚ(√−7).** The corpus-validated 5₂
   Neumann–Zagier saddle has three ideal-tetrahedron shapes `z₁, z₂, z₂` with
   **`D(z₁) = D(z₂) = −0.94270736`** (Bloch–Wigner) — the two *distinct* shapes
   `z₁ ≠ z₂` carry **equal** Bloch–Wigner dilog — and

   > **Vol(5₂) = 3·|D(z₁)| exactly** (`Vol/|D| = 3.0`), `= 2.82812208833`.

   A clean ℚ(√−7) dilog value, in the paper's field.

## The route to the bar-odd action (stated, not yet closed)

The paper's **Theorem 3** gives the closed form of the **three-term** dilog sum
`L(u) = Li₂(z_a) + Li₂(z_b) + Li₂(u)` — exactly the shape of the 5₂ three-tetrahedron
potential — and proves `L(u) = E(u)` is **elementary** (logs + π²) for all real `u > 0`.

The 4₁ bar-even action π²/5 was elementary at the golden real point (`arcsinh ½ = ln φ`).
By the same logic, **the 5₂ bar-odd archimedean action is `E(u)` at the substrate real-u
face of Theorem 3** — an elementary, ℚ(√−7)-flavoured closed form, the direct analog of
π²/5. This **reduces the gate**: from "the unknown 5₂ cyclotomic coefficients (Masbaum)"
to "identify the substrate real-`u` in Theorem 3." The uploaded Masbaum paper
(`agt-v3-n1-p17-p.pdf`) remains the cross-check for the cyclotomic route.

## Anti-laundering scope

The **geometric** Vol(5₂) is anchor-**smooth** (corpus: NOT the c₃ swing). This probe
verifies the paper's ℚ(√−7) toolbox and the `Vol=3D` structure, and **states** the
Theorem-3 route — it does **not** claim the bar-odd **action value** (that requires the
real-u evaluation of Theorem 3). No exact bar-odd action is claimed; no fit; no c_k.

## Cross-references

- Paper: [`uploads/2506.10206v2.pdf`](../../uploads/2506.10206v2.pdf) (Theorem 3; Examples 5–8, ℚ(√−7))
- Bar-even template: 4₁ Habiro-tail action π²/5 (b3ix, merged)
- Verified 5₂ volume: [`qbeta_5two_quantum_volume_probe.py`](../../computations/probes/qbeta_5two_quantum_volume_probe.py)
- Prior step (exact-route gate): [`2026-07-18-bar-odd-c3-action-exact-route-5two-gate.md`](2026-07-18-bar-odd-c3-action-exact-route-5two-gate.md)
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
