# `c₄ ≈ 46` (the u⁴ Habiro dressing on F_Bor) is the μ–p tension in disguise

**Date:** 2026-07-04
**Branch:** `claude/mu-p-tension-closure-uua4os`
**Probe:** [`docs/audits/scripts/c4_mu_p_tension_pin_dependence_probe.py`](scripts/c4_mu_p_tension_pin_dependence_probe.py)
+ [`c4-mu-p-tension-pin-dependence.witness.json`](scripts/c4-mu-p-tension-pin-dependence.witness.json)
**Supersedes-sharpens:** [`2026-05-28-mu-p-tension-substrate-floor.md`](2026-05-28-mu-p-tension-substrate-floor.md)
(quantifies its "46.02 is not a clean invariant" into a theorem)

## Task

> "The μ–p tension is one number away from closure or honest failure:
> derive c₄ ≈ 46 at u⁴ on F_Bor, categorically. The floor audit measured
> 46.02; if a categorical derivation produces 46-exactly (or a nearby
> q₀-dependent closed form), the tension closes parameter-free."

## Answer: honest failure — but a *productive*, scope-(a) one

**c₄ is not a categorical constant. It is the μ–p tension re-expressed as a
u⁴ coefficient.** The exact c₄ that lands m_p on CODATA is *exactly linear*
in the q₀ pin offset, running from **0 at the proton pin to 46.04 at the
muon pin** across the 11.5 ppb window that separates the two legitimate
calibrations:

| q₀ pin | q₀ | m_p(base, N=0) error | exact c₄ needed |
|---|---|---|---|
| **proton** (`base(q)=m_p`) | 1.10997858282 | 0 (by construction) | **−0.03 ≈ 0** |
| **muon** (`m_μ/m_e=Vol/ℏ²`) | 1.10997859564 | −242 ppb | **46.04** |

- **slope** `dc₄/d(q₀) ≈ 3.987 per ppb`, linear to `< 9e-6` across the
  whole window (probe: `max deviation from linear = 8.9e-6`).
- So `c₄ = 3.987 · (q₀ − q₀^proton)[ppb]`. The value **46 is precisely the
  choice to calibrate on the muon rather than the proton** — a convention,
  not a derivation.

The μ–p tension *is* the fact that these two pins disagree by 11.5 ppb.
Asking to "derive c₄=46 categorically" is asking the Borromean/s5bb
categorical data to know the 11.5 ppb muon–proton discrepancy — i.e. to
derive the tension itself. That is the substrate's honest predictive floor
(≈ 240 ppb on m_p); anything below it is noise (per the 2026-05-28 floor
audit). **c₄=46 does not resolve the tension; it is the tension.**

## The precision (entropy) bound makes "46-exactly" unfalsifiable

The exact target is determined only to the precision with which the pin
itself is fixed. Because the legitimate pin window spans 0 → 46 in c₄, and
even a fixed pin moves the target by O(1) in "46" under sub-ppb q₀ jitter,
**c₄ is a ~2–3 significant-figure quantity.** Any fixed closed form matching
to that precision — `46`, `4143/90 = 46.033`, the committed-q₀ target
`≈ 45.74` — is equally consistent and equally without predictive content
(the same PSLQ/entropy argument that killed the Q_β c_k ≥ 3 identifications:
*precision available < precision needed to identify a constant*). There is
no "46-exactly" to derive.

## Production defect: `c_4 = 4143/90` is mislabeled numerology

[`computations/m_p_substrate_identity_50dps.py`](../../computations/m_p_substrate_identity_50dps.py)
currently ships:

```python
# 4-loop anomaly derived geometrically from s5bb 5-manifold U(1) colour Reeb index
c_4 = mpf('4143') / mpf('90')     # = 46.0333…
```

Three independent problems:

1. **No derivation trail.** `4143` appears *only* on this line in the entire
   corpus (checked: `git log -S`, all `docs/`, all `*.witness.json`). Nothing
   computes it.
2. **The cited route is an honest-negative.** The comment credits the "s5bb
   5-manifold U(1) colour Reeb index," but that exact Reeb-resonance route
   was tested and **refuted** —
   [`2026-06-16-s5so3-reeb-resonance-probe-negative.md`](2026-06-16-s5so3-reeb-resonance-probe-negative.md)
   ("NO eigenvalue resonance realizes the dynamical spin–colour coupling").
3. **It does not even hit the target.** At the muon pin the exact target is
   46.04; `4143/90 = 46.033` (Δ = −0.008), and in the *committed* q₀ it
   overshoots CODATA to **+1.53 ppb** — a *worse* fit than the naked integer
   `46` (+1.35 ppb). A genuine 4-loop closure would land *nearer* the target
   than the integer, not further.

This is exactly the pattern the canonical-watcher and the 2026-05-28 floor
audit warn against: a sub-floor fit dressed with a categorical-sounding
comment. It should be relabeled honestly (see options below).

## What would actually close it (not in scope here)

The question becomes well-posed only if the substrate fixes **one** q₀:

- **Derive q₀ itself** from substrate structure (Subgoal-2, owner-declined
  2026-05-08). One pin ⇒ one c₄ ⇒ the number is a prediction.
- **Derive the 11.5 ppb muon–proton splitting** categorically — the actual
  physical content behind "46." This is the honest target, not a closed form
  for the integer.

Absent either, `c₄` stays a calibration artifact and the tension stays at
its ≈ 240 ppb floor.

## Scope discipline (AGENTS.md "before declaring refuted")

This is a **scope-(a)** result: *c₄, as a fixed categorical constant, is not
derivable at current substrate precision* (it is pin-dependent, sweeping
0→46 continuously; the target is 2–3 sig figs). It is **not** a scope-(b)
structural exclusion — a future derived-q₀ or derived-splitting could make
c₄ a genuine prediction. Nothing here excludes that path; it only shows the
current "46 / 4143/90" values encode the muon-pin choice, not categorical
structure.
