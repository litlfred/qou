---
# qou-3qla
title: 'Resurgence arc: 45 of 73 audits are convention-C-conditional and none says so; the Borel singularity and the Bring saddle are never connected'
status: todo
type: task
created_at: 2026-09-06T09:11:28Z
updated_at: 2026-09-06T09:11:28Z
---


Owner question (2026-09-06): *"Where are we alien calculus and resurgent
functions? Some doors may have been closed due to incorrect compute or on
convention C. Please do exhaustive re-analysis on the divergent functions on the
full tower. Where are the divergent points? Are they related to saddle points on
Brings?"*

Full write-up:
[`docs/audits/2026-09-06-resurgence-arc-convention-d-reanalysis.md`](../docs/audits/2026-09-06-resurgence-arc-convention-d-reanalysis.md).

## Measured

**73** audits on the resurgence surface. **45** reference the `c_k` ladder /
`Q_β`. **0** mention convention D. AGENTS.md says the ladder is C-frame
throughout and un-re-derived, and that every `c_k` conclusion is C-conditional —
**no audit in the arc carries that scope.**

Only **one** file names convention C or `z_C` at all. The exposure is almost
entirely **implicit through the ladder**, which is why grepping for "convention
C" makes the problem look absent.

## The two divergent-point families, and the gap between them

- **Borel plane:** binding kernel is **Gevrey-1/2** (Lean, `QOU.Mass.
  BindingGevreyHalf`), so the standard Gevrey-1 plane is the wrong one; the
  level-1/2 singularity is at **`ξ = 1/√2` at `q = 1`**; at `q₀` the class is
  **q-Gevrey** → q-Borel (RSZ theta kernel), Habiro ring as arithmetic home.
- **Bring's surface:** the colour-tube cubic's discriminant has **no real
  roots**; the critical pair nearest `z₀ = 0.104` is **`z_c ≈ 0.106 ± 0.937i`**,
  where `∂F/∂c → 0` — a saddle, accessed by a Picard–Lefschetz thimble.

**🛑 No document connects them.** `ξ = 1/√2` and `z_c` live in different planes,
and I found no derivation of a map, nor any claim of one. That is the *exact*
relation resurgence exists to assert — a Borel singularity should be a saddle's
action — so **"is `ξ = 1/√2` the action of the `z_c` saddle?" appears to be
open and unasked.** Absence of evidence, not evidence of absence: surface
searched was filename+content greps over `docs/ content/ computations/` for
saddle∧Bring (38 files) and for the two constants.

## 🛑 The Bring-saddle RESULT is a fit

`docs/picard-lefschetz-plan.md` is titled **"KEY RESULT — simultaneous 3-root
product yields m_p to 0.0006%"** and is listed uncaveated in `docs/README.md`.
Its own text reports **nine prescriptions tested** — ratios 1.09, 23.5, 0.99,
**2.46**, 1.26, 4.19, 7.74, 366.5, 0 — and marks the fourth **"← WINNER"**,
because 2.460 is the factor that lands `m_p` on CODATA. That is
**selection against the target**, named verbatim in the NO-FITTING directive.

It also targets **absolute `m_p` in MeV**, excised by owner ruling **2026-08-11
— one day after this file was last touched**.

The *geometry* is not retracted: the discriminant locus, the complex `z_c`, the
thimble and the `∂F/∂c → 0` pole are real structure, and are the right structure
for the open question above. The fit is the **choice of prescription** and the
accuracy claim on it.

## Recommended, none of it done here

1. Banner the 45 as C-conditional (cheap, reversible, no numbers move).
2. **Answer the §2c question** — the door most likely closed by accident.
3. Re-status `picard-lefschetz-plan.md`: keep the geometry, demote the KEY
   RESULT, note the 1-of-9 and the excision.
4. Do **not** re-derive the ladder here — that is `qou-cds1` and gates 1 and 2.

Not measured: whether anything downstream consumes `A(q₀) ≈ 2.46`. Twelve other
audits mention it; not triaged.

---

## Measured the Bring side directly (2026-09-06) — four new structural facts, one negative

Probe: [`computations/probes/colour_cubic_discriminant_structure_probe.py`](../computations/probes/colour_cubic_discriminant_structure_probe.py),
**9/9**, all `mpmath` + exact integer arithmetic, 0 NEW dirty on the ratchet.

`docs/picard-lefschetz-plan.md` records exactly one fact about the discriminant
locus: the roots are all complex, and the pair nearest `z₀ = 0.104` is
`z_c ≈ 0.106 ± 0.937i`. Four more fall straight out and none is written down
anywhere:

1. **The sextic `(16, 24, 35, 50, 35, 24, 16)` is PALINDROMIC**, so its roots
   come in reciprocal pairs `z, 1/z`. Verified: `|z_min|·|z_max| = 1` exactly.
2. **One conjugate pair lies EXACTLY on the unit circle** (`|z| − 1 = 0.0`),
   i.e. a pure phase `e^{±iθ}` with `θ = 2.9166887082513073529`,
   `θ/π = 0.92841085075702107917`.
3. **That phase is NOT a root of unity** at any order a Bring/cyclotomic reading
   would want — `θn/2π` for `n ∈ {5,7,10,12,20,24}` is
   `2.32, 3.25, 4.64, 5.57, 9.28, 11.14`, none integral. **So the unit-circle
   point sits at no cyclotomic evaluation point**, and a Habiro-ring reading
   does not pick it up for free. That is a constraint on any bridge to §2a.
4. **The palindromic reduction `w = z + 1/z` gives `16w³ + 24w² − 13w + 2`,
   whose integer discriminant is exactly `−80000 = −2⁷·5⁴`**, with no rational
   root over `p|2, q|16`. The `5⁴` is arithmetically suggestive beside Bring's
   quintic / icosahedral setting — **an observation, not a derivation, used for
   nothing.** Flagging it precisely because this is where numerology would start.

### The negative, which is the point

`ξ = 1/√2` tested directly against the simple invariants of `z_c`:

    |z_c|    /(1/√2) = 1.3337      Re z_c  /(1/√2) = 0.1497
    |z_c|²   /(1/√2) = 1.2578      |w_ℂ|   /(1/√2) = 0.3581
    Im z_c   /(1/√2) = 1.3253

**No clean ratio.** Scope-(a): the cheap identification fails.

**It does not exclude the connection**, and the honest test is named and NOT
done: whether `ξ = 1/√2` is the *action* `∫λ_SW` along a Picard–Lefschetz
thimble from `z_c`. That needs a definite `λ_SW` and a thimble integration.
What is now excluded is the version that would have been found by inspection —
which is usually how an unasked question dies.
