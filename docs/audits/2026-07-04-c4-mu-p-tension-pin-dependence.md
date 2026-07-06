# `c₄ ≈ 46` (the u⁴ Habiro dressing on F_Bor) is the μ–p tension in disguise

**Date:** 2026-07-04
**Branch:** `claude/mu-p-tension-closure-uua4os`
**Probe:** [`docs/audits/scripts/c4_mu_p_tension_pin_dependence_probe.py`](scripts/c4_mu_p_tension_pin_dependence_probe.py)
(self-contained) + result artifact [`c4-mu-p-tension-pin-dependence.json`](scripts/c4-mu-p-tension-pin-dependence.json)
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

- Affine (two-endpoint) fit `c₄ = −0.032 + 3.990·(q₀ − q₀^proton)[ppb]`,
  matched to `< 9e-6` across the whole window (probe:
  `max deviation from affine = 8.9e-6`). The intercept is ≈ 0 (the proton
  pin needs no dressing).
- So c₄ is fixed entirely by the pin offset. The value **46 is precisely the
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

## Update (2026-07-04, same day): the tower was a live +242 ppb bug — DROPPED

After the **2026-07-03 owner ruling** re-pinned the canonical q₀ to the raw
**proton** pin (commit `7b95577a`), `computations/m_p_substrate_identity_50dps.py`
still multiplied the base formula by the **muon-era** fitted tower
`(1+46u⁴)(1+4u⁵)(1−29u⁶)`. At the proton pin the base already lands m_p at
**+1.35 ppb**, so the tower *added* its +242 ppb on top — pushing production
m_p to **+243.8 ppb**. The committed witness (`m-p-substrate-identity-50dps.witness.json`)
still held the old muon-q₀+tower value (938.2720882, −0.13 ppb), masking the
inconsistency; the next routine regen would have corrupted m_p to +243.8 ppb.

**Fix (this PR): the tower is dropped.** Production is now
`m_p = 2·m_μ·F_Bor − 12·m_e` (formula muon, `m_μ = m_e·Vol(4₁)/ℏ_q²`), giving
m_p = **+1.35 ppb** at the proton pin — the honest floor, and code↔witness
consistent. `canonical_mass.py` (the facade) is confirmed correct on both its
witness and direct paths.

**Why c₄ = 0 now (reconciliation with `mp_habiro_c4_keystone_probe.py`).**
That probe reports a pin-stable c₄ ≈ 46.03 — but it holds m_μ **fixed at the
CODATA measured value** (only F_Bor varies with q, and F_Bor is flat). *Production
uses the muon formula* (m_μ must be predicted, per the 3-calibration discipline).
Verified side by side:

| pin | c₄, **formula muon** (production) | c₄, measured muon (keystone) |
|---|---|---|
| proton | **≈ 0** | 40.2 |
| muon | 46.07 | 46.07 |

At the proton pin, the production (formula-muon) c₄ is **0** — no dressing is
needed, and the μ–p tension correctly surfaces instead as the m_μ prediction
missing CODATA by 211 ppb (9.5σ). The keystone's 46.03 is a *measured-muon
diagnostic*, not the object production's tower multiplied. So the whole
"derive c₄ = 46" quest was an artifact of the muon-pinned-q₀ era; after the
proton re-pin, m_p needs no c₄ at all.

## Addendum: are the c_k proved? is there a recursion? can we derive them?

Corpus-grep (STRICT) settles this — the authoritative source is
[`content/.../mass-theory/habiro-precision-ladder-equivalence.md`](../../content/quantum-observable-universe/mass-theory/habiro-precision-ladder-equivalence.md),
cross-checked against [`2026-05-18-all-c-i-status.md`](2026-05-18-all-c-i-status.md).
Probe: [`scripts/ck_habiro_ladder_derivation_probe.py`](scripts/ck_habiro_ladder_derivation_probe.py)
(self-contained, exit 0).

**There is exactly one proved, recursive, derivable c_k ladder — and it is
not the production tower.**

- **Proved / derivable (the Habiro integrality ladder).** The Markov trace
  has a *finite* expansion in the cyclotomic q-Pochhammer basis,
  `tr_M(β) = Σ_{m=0}^{M} a_m(u)·(u;u)_m`, with **integer** `a_m ∈ ℤ[u]` and
  `M < ∞` (proton `M = 8`). The **recursion is the (u;u)_m basis itself**
  (finite, cyclotomic). The probe reconstructs the proton `tr_M` from the
  block's listed `a_m` as an exact degree-76 polynomial in `u`, all
  coefficients integral — a genuine, fit-free, categorical ladder. This is
  what "derive c_k" *correctly* yields.
- **These derived a_m are O(10²) integer-scale objects.** Evaluated at
  `u₀=√q₀` the proton trace is ≈ 136 — nowhere near the O(10⁻⁷) correction
  the production tower supplies. The distinctive production coefficients
  `{46, −29}` do **not** appear among the `a_m` (the only overlap is the
  ubiquitous small integer `4`, a trivial coincidence).
- **The production tower `{46, 4, −29}` is not derivable and has no
  recursion.** The block disowns it in its own words: *"attempts to read
  them off as a precision ladder tuned the coefficients against the
  experimental value rather than evaluating them categorically … higher-order
  corrections that are **not** currently derived from the a_m."* And this
  audit's main result explains *why no fixed recursion can exist*: c_4 is
  affine in the q₀ pin (0 at the proton pin, 46 at the muon pin), so it is
  the μ–p tension, not a fibre Taylor coefficient. Deriving it is the open
  s5bb Habiro keystone (`beans s5bb`), the same object as the Q_β c_k ladder.

**Bottom line for "derive c_k":** the honest derivation is the Habiro `a_m`,
and it lands the observable at the substrate's ~240 ppb floor — it does
**not** reproduce 46. The Family-A precedent (`2026-05-18-all-c-i-status.md`)
is the same lesson: when the fibre object is an *exact closed form*
(π_HS = (3[2]_q²−2)/4) its c_k are provable and terminate; when the target is
solved from a single CODATA value (Family B), the coefficients are not
determined categorically. `{46, 4, −29}` is Family-B.

## Scope discipline (AGENTS.md "before declaring refuted")

This is a **scope-(a)** result: *c₄, as a fixed categorical constant, is not
derivable at current substrate precision* (it is pin-dependent, sweeping
0→46 continuously; the target is 2–3 sig figs). It is **not** a scope-(b)
structural exclusion — a future derived-q₀ or derived-splitting could make
c₄ a genuine prediction. Nothing here excludes that path; it only shows the
current "46 / 4143/90" values encode the muon-pin choice, not categorical
structure.
