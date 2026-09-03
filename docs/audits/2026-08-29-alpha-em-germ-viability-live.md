# α_EM continuous-germ measure route is LIVE — the EM germ is non-sterile where the binding germ was sterile

**Date:** 2026-08-29 · **Bean:** `qou-rrgk` (germ-viability decision) ·
**Probe:** [`alpha_em_germ_viability_probe.py`](../../computations/alpha_em_germ_viability_probe.py)
(+ witness, exact ℚ(q)) · **Tier:** route-viability decision (necessary, not
sufficient) · **Scope:** (a); nothing wired; `1/(8π)` stays phase-4.

## The decision this settles

The α_EM per-loop measure `1/(8π)` is owner-gated on **MOC / Φ** (the q↔period
map, epic `08a2`), whose stated obstruction is *"the discrete `q=i`
F-construction shadow supplies **no germ**."* A Yekutieli holonomy
`Hol(q) = ∏σᵢ(q)` is a germ in `q` by construction (the owner's 2026-07-19
non-abelian-Stokes steer). The
[work-plan update](2026-08-29-alpha-em-measure-arc-workplan-update.md) flagged
the risk that this germ might be **sterile**, like the binding-side germ:
[`2026-08-09-nastokes-gauge-fixing-germ-root-vector.md`](2026-08-09-nastokes-gauge-fixing-germ-root-vector.md)
(PR #4848) found the deuteron transverse pairing **determined = 0** on `σ₁³`.

**This probe decides LIVE vs DEAD, cheaply, before any multi-week Φ commitment.**

## The precise discriminator

The binding sterility has a **named, narrow mechanism**: `σ₁³` is a *single*
generator, so the transport is **abelian** and the germ curvature
`F_q = [δq₁, δq₂]` (the corpus `germ-commutator-q-curvature` object,
`δqᵢ = q·(∂_q σᵢ)·σᵢ⁻¹`) has **no second generator to bracket** — it vanishes
for lack of non-abelianity, not for a deep reason. The **EM sector is
multi-generator** (`T_{2,9}`, `T_{3,5}`; the photon 4-term Hecke element; the
H₅ (4,1) block), so that mechanism need not apply.

## Result — LIVE

Exact fundamental-rep computation (Hecke/braid/`e₋` validated), H₃ (`σ₁, σ₂`):

| object | value | |
|---|---|---|
| **control** `[δq₁, δq₁]` | `0` | reproduces the deuteron single-generator sterility ✓ |
| **curvature** `F_q = [δq₁, δq₂]` | ≠ 0 | the non-abelian germ curvature the single-generator case lacks |
| **EM-singlet moment** `m_F = qTr(E·F_q·E)/qTr(E)` | `−(q²−1)/(q²+1) = −h/[2]_q` | non-zero |
| `m_F` at proton `q₀` | `−0.10396…` | |
| `‖F‖²`-moment at `q₀` | `9.717…` (O(1)) | non-degenerate |

The germ curvature is **non-sterile in the EM singlet channel** on two-generator
words. The single-generator binding sterility is exactly the control here, and
the EM sector escapes it because it is multi-generator.

**Structural bonus (not fitted):** the EM-channel moment is exactly
`m_F = −h/[2]_q` — the bar-odd `h = q−q⁻¹` over the bar-even `[2]_q = q+q⁻¹`,
i.e. the **bar-odd fraction of the fundamental channel**. It vanishes at `q=1`
(the classical/self-dual point) and grows as `q` deforms — the signature of a
genuine `q`-motion (a germ), not a static coincidence.

## Honest scope — necessary, not sufficient

This decides the route is **worth pursuing**; it does **not** derive Φ.

- It shows the germ carries non-zero, non-degenerate `q`-curvature *in the EM
  channel* — the property the discrete `q=i` shadow lacks and the binding
  single-generator germ lacks.
- It does **not** show that germ curvature *reproduces the period map* Φ
  (`q ↦ H¹(E_{τ(q)}) ⊂ H¹(Bring)`). That identification is the multi-week `08a2`
  Gauss–Manin keystone, proved not-derivable-from-the-abelian-model and
  owner-gated. `1/(8π)` stays phase-4.

## Consequence for the work plan

- **The continuous-germ / non-abelian-Stokes route to the measure is LIVE** and,
  per the survey, **uncontended** — no one has run a continuous-germ holonomy at
  the measure (all 2026-08 germ work went to binding).
- **The follow-on is the `08a2` keystone** (identify the germ curvature with the
  Φ period-motion), which is owner-gated multi-week infra — **not to be forked**
  solo per the ownership-map discipline. The right next move is to **flag this
  LIVE result + the clean `m_F = −h/[2]_q` object to the `08a2` keystone
  owners** as a concrete non-abelian handle on Φ, rather than open a parallel
  multi-week attack.

## Cross-references

- Work-plan update: [`2026-08-29-alpha-em-measure-arc-workplan-update.md`](2026-08-29-alpha-em-measure-arc-workplan-update.md)
- Binding-side sterility (the control): [`2026-08-09-nastokes-gauge-fixing-germ-root-vector.md`](2026-08-09-nastokes-gauge-fixing-germ-root-vector.md)
- Germ normalization: `content/quantum-observable-universes/germ-commutator-q-curvature.md`
- The measure wall: [`2026-08-02-moc-gauss-manin-not-derivable.md`](2026-08-02-moc-gauss-manin-not-derivable.md) (epic `08a2`)
