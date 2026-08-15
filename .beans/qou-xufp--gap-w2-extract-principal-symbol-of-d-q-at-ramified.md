---
# qou-xufp
title: 'GAP W2: extract principal symbol of D_q at ramified pole (Ramis-Sauloy-Zhang local q-difference classification)'
status: todo
type: task
created_at: 2026-08-01T01:47:27Z
updated_at: 2026-08-01T01:47:27Z
---


## The wall (W2 / G2 of the C1↔SW leg)

Parent: `qou-3cgi`; downstream of `qou-d8de` (W1, construct `D_q`). **Conditional on
W1** — cannot start until a q-difference prolongation `D_q` exists.

Given `D_q : Jⁿ E → Jⁿ⁺¹ E` on Σ, extract its **principal symbol at a ramification
point**. At a simple branch `z = z_c + t²` (local coord `t`) the jets acquire poles
(`X⁽¹⁾ = (dX/dt)/(2t)`, order rising by 2 per jet), so the symbol is the leading
Laurent coefficient / connection-matrix datum on the `t`-punctured disk.

**RSZ IS in the corpus (correction, per Copilot review #4449).** The Ramis–Sauloy–Zhang
local classification (Newton polygon, slopes, `q`-Gevrey/Stokes structure) has been
applied **by hand** in [`docs/audits/2026-07-20-qlift-routeA-rsz-invariants.md`](../docs/audits/2026-07-20-qlift-routeA-rsz-invariants.md):
C1 written as `L1 = (q²x−1)σ² − (q−1)σ − (q−1)` in `x=q^m`; its Newton polygon at
`x=∞` gives slope **½, mult 2** (pure isoclinic), vs GGM's `{−1,+1}`. That slope
comparison is even formalized on main (`ThetaSlopeArithmetic.lean`). RSZ Astérisque 355
is read directly (`library/arxiv-0903.0853v3/0903.0853v3.pdf`).

**What is genuinely missing** is therefore NOT "RSZ in the corpus" but:
(i) reusable **Lean/Python RSZ infra** (the Newton polygon is by-hand, not a checker);
and — the real gap — (ii) the slopes computed so far are those of the **C1 recurrence
operator itself**, NOT of a prolongation `D_q` built from Σ. Reading C1's own Newton
polygon and calling it "the SW symbol" is **circular** — exactly what the W3 anti-fit
gate (`qou-ailp`) forbids. W2 needs the symbol of an *independent* Σ-derived `D_q`
(from W1 `qou-d8de`), then compares THAT to C1's `{½,½}`.

**Next step:** import the q-difference local-classification framework (Sauloy,
*Systèmes aux q-différences singuliers réguliers*; Ramis–Sauloy–Zhang, *Local
analytic classification of q-difference equations*) before attempting extraction.
