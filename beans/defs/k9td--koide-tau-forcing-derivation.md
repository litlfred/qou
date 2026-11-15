---
# k9td
title: Koide tau-forcing derivation — is Q=2/3 a categorical constraint or a fit?
status: completed
type: task
priority: normal
created_at: 2026-06-16T02:14:00Z
updated_at: 2026-06-21T19:39:07Z
parent: qz9k
---

## Result (2026-06-16) — refuted against a fit (acceptance b); pending human close

Tiered finding delivered:
[`docs/audits/2026-06-16-koide-tau-forcing-assessment.md`](../docs/audits/2026-06-16-koide-tau-forcing-assessment.md).

- **TIER A (fact):** Koide forces m_τ ≈ 1776.97 MeV (62 ppm vs PDG 1776.86) —
  ~200× better than QOU's *own* structural attempt, which was exhaustively
  falsified at 1.33% (`2026-06-03-m-tau-knot-prediction-falsification.md`).
- **TIER B (verdict):** QOU derives no Z/3 generation democracy, no √m-amplitude,
  no categorical 2/3 for generations. Forcing m_τ from Koide is a **CAL-4 import**,
  not a derivation → out of scope for production.
- **TIER C (open):** the non-fitting route to m_τ is Path A (derive ξ_ℓ(q)) per
  `lepton-mass-tower-canonical.md`; Koide is at most an external check on a future
  derived ξ_ℓ, never an input.
- Corrected the first corpus-map agent's overstated "torus-Vol=0 dictionary
  inconsistency": canonical conjecture uses the per-braid q-volume (nonzero on
  torus braids; → hyperbolic vol only in Kashaev q→1 limit) and the electron is
  the calibration unit, so its hyperbolic Vol never enters. The Vol=0 fact bites
  only the SUPERSEDED Skein LO form.

## Goal

The Koide relation for charged leptons:
$$ Q \;=\; \frac{m_e + m_\mu + m_\tau}{\left(\sqrt{m_e}+\sqrt{m_\mu}+\sqrt{m_\tau}\right)^2} \;=\; \tfrac{2}{3}. $$
"Tau forcing" = using a structural constraint to **predict / derive** $m_\tau$
from the framework (given $m_e$, $m_\mu$), OR checking whether the framework's
own $(m_e, m_\mu, m_\tau)$ predictions land on $Q=2/3$.

## Corpus state (session start)

`grep -rli koide` over `content/ docs/ computations/`
returns **ZERO** — this is **greenfield**. (Background Explore agent
confirming/widening; results to be folded in.)

## Discipline (this bean is HIGH numerology-risk)

Koide $Q=2/3$ is famously numerology-adjacent. Per the repo critical-distance
license + three-calibration discipline:

- A Koide "derivation" that just **fits** $m_\tau$ to make $Q=2/3$ is a CAL-4
  in disguise and will be caught. Do NOT do that.
- The bar to clear: $Q=2/3$ (or whatever the framework predicts) must fall out
  of an **independent** categorical structure (generation $\mathbb{Z}/3$
  symmetry, $\sqrt{m}$-democracy, a brane-tower level rule) that was fixed for
  other reasons — not reverse-engineered from the lepton masses.

## Plan (formalize-first)

1. Confirm corpus greenfield + locate how $m_\mu$, $m_\tau$ are currently
   obtained (knot/braid assignment per lepton, if any).
2. State the hypothesis: is there a categorical object whose archimedean
   evaluation forces a $\sqrt{m}$-democracy / $2/3$ ratio?
3. Find the pruning invariant. If none exists, the honest verdict is
   "no structural hook — would be a fit", recorded as a TIER:fitted finding.
4. Only if a structural hook survives: a small probe + Lean/sketch.

## Acceptance

Either (a) a tiered finding doc establishing whether Koide can be a canonical
QOU constraint, with the structural hook (or its absence) made explicit; or
(b) a refutation that closes the question against a fit. NO fitted $m_\tau$.

TRIAGE VERDICT (2026-06-20, session intelligent-pasteur): REFUTED — Q=2/3 is a CAL-4 fit, NOT a categorical derivation. Three required ingredients all absent: (1) no Z/3 generation orbit (leptons are a braid tower in increasing H_n(q), not a cyclic orbit), (2) no √m-amplitude democracy, (3) the 2/3 ratio nowhere attaches to lepton generations. Already documented in docs/audits/2026-06-16-koide-tau-forcing-assessment.md. Koide can serve only as a post-hoc consistency check on a future DERIVED ξ_ℓ (Path A, operator-valued ℓ=3 branching), never as an input. The bean's question ("constraint or fit?") is ANSWERED: fit. Real m_τ route (Path A) is blocked on the conj:s5-so3-fiber-action q-closure (bean s5bb).
