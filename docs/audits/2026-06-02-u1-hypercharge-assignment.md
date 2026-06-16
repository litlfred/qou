# U(1) → quantum-number assignment: c=1/2 fixed by Coulomb-charge; writhe → I₃ (not Y)

**Date:** 2026-06-02
**Branch:** `claude/u1-hypercharge-assignment-2026-06-02` (PR #1683)
**Scope:** Derive the map from the framing-phase U(1) `q^{w·c}` (writhe `w`,
per-crossing coupling `c`) to a Standard-Model quantum number — or prove it
undefined with a precise missing object. Follow-up to the inter-nucleon
LINKED-channel audit
([`2026-06-01-inter-nucleon-linked-channel.md`](2026-06-01-inter-nucleon-linked-channel.md),
PR #1678), which established a LIVE derived U(1)_framing (writhe pp=+2, nn=−2)
but left `writhe → hypercharge Y` UNDEFINED: with `c=1` the pp/nn framing
difference (0.420) missed PDG `(m_n−m_p)/m_p` (0.00138) by ~305×, and the
author flagged that tuning `c` to match would be a FIT.
**Compute:**
[`u1_hypercharge_assignment.py`](../../computations/u1_hypercharge_assignment.py),
witness
[`u1-hypercharge-assignment.witness.json`](../../computations/u1-hypercharge-assignment.witness.json)
(audit-only, RAW @ canonical COMPUTE_DPS + symbolic-in-q, 10 assertions pass;
q0 is the proton-pinned `q_parameter.Q_MP`). **No tuning to
m_n−m_p, any charge, hypercharge, or any h^k.**

---

## VERDICT (one line)

**(a)-partial + (b)-with-precise-obstruction: the per-crossing coupling `c` is
NOT free — it is `c = 1/2`, STRUCTURALLY FIXED by `def:coulomb-charge`
(`Q(H) = ½(n₊ − n₋) = writhe/2`), which resolves the linked-channel audit's
open `c`. With `c` fixed, the writhe ladder matches **I₃** (the third isospin
component) by sign+ratio across the nucleon doublet (p:+, n:−, scale-free),
is **FALSIFIED as a hypercharge-Y map** by the sharp proton/neutron same-Y
test (Y(p)=Y(n)=+1, but writhe splits them), and does **not** match electric
charge Q either (neutron Q=0 while writhe(n)≠0). The ribbon twist
`θ_j = q^{j(j+1)}` is a spin/Casimir ladder, monotone in j with no sign change
— it is NOT a charge ladder. So `writhe → I₃` is DERIVED (no scale fit), but
**Y itself stays UNDEFINED**, and the precise missing object is a SECOND,
independent crossing invariant (a baryon-number / color-trace charge) — NOT a
free coupling. This is a missing-second-charge problem, not a free-c problem.**

---

## 1. Q1 — What is `c`, structurally? `c = 1/2`, fixed by `def:coulomb-charge`

The linked-channel audit (PR #1678 §5) wrote the framing phase as `q^{w·c}` and
*set* `c = 1` "(SET, not fitted)", noting that choosing `c` to match
`m_n − m_p` would be the fit the discipline review catches. The genuine
structural question it left open: **is `c` fixed by the framework, or free?**

**Finding (DERIVED from the corpus, NOT fitted):** the framework already
contains a canonical per-crossing charge coupling. `def:coulomb-charge`
([`coulomb-charge.lean`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-charge.lean),
`.ts`) defines the **electric / Coulomb charge of a knot composite** with braid
word β as

$$
  Q(H) \;=\; \tfrac{1}{2}\bigl(n_+ - n_-\bigr),
$$

where `n₊`, `n₋` are the positive/negative crossing counts. The **writhe** is
`w = n₊ − n₋`. Therefore

$$
  Q(H) \;=\; \frac{w}{2}, \qquad\text{i.e.}\qquad \boxed{c = \tfrac12}
$$

is the framework's own crossing→charge coupling. The same `1/2` appears in the
Coulomb-correction term `Q(H)·(q − q⁻¹)` in the same file (antisymmetric under
`q ↔ q⁻¹`, vanishing at `q=1`).

**Consequence:** `c` is **not** a free knob. The linked-channel audit's `c=1`
choice was the *q-momentum / writhe-as-momentum* normalisation
(`def:q-momentum`: `p_q(β) → w(β)`), which is a *different* observable from
charge. For the **charge** reading the framework fixes `c = 1/2`. Choosing `c`
to hit `m_n − m_p` would *contradict* this fixed Coulomb value, so the fit the
review guards against is structurally foreclosed — `c` is pinned.

Witness assertions (RAW, def:coulomb-charge):
`Q(pp, w=+2) = +1`, `Q(nn, w=−2) = −1`, `Q(pn, w=0) = 0`.

## 2. Q2 — Gell-Mann–Nishijima: which quantum number does the writhe match?

Gell-Mann–Nishijima: `Y = 2(Q − I₃)`. The framework has isospin
(`conj:isospin-from-canonical-bowtie`, D9 — the `u ↔ d` flavor swap maps pp's
`σ` to nn's `σ⁻¹`) and now a writhe-U(1). We test the **writhe ladder** against
the known `(Q, I₃, Y)` for the nucleon doublet using a **sign+ratio** comparison
(normalisation-independent — no scale parameter). The DERIVED per-nucleon writhe
datum is the inter-nucleon arc: `w(p) = +1`, `w(n) = −1` (linking-number
normalisation; the Hopf-link writhe ±2 is twice this — the sign+ratio pattern is
identical either way).

| Particle | writhe `w` | electric `Q` | isospin `I₃` | weak hypercharge `Y` |
|---|---:|---:|---:|---:|
| proton | **+1** | +1 | **+½** | +1 |
| neutron | **−1** | 0 | **−½** | +1 |
| sign pattern | (+, −) | (+, 0) | (+, −) | (+, +) |

(Reference `(Q, I₃, Y)` are PDG **falsification references only**; the table
satisfies `Q = I₃ + Y/2` for every entry — checked in the probe.)

**The sharp falsifier (author-supplied):** proton and neutron have the **same**
baryon weak hypercharge `Y = +1`. A `writhe → Y` map MUST therefore *not* split
them. But the writhe **does** split them (+1 vs −1). Hence:

- **`writhe → Y` is FALSIFIED** (writhe splits p/n; Y does not).
- **`writhe → Q` also fails**: the neutron has `Q = 0`, but `writhe(n) = −1 ≠ 0`
  — the sign pattern `(+, 0)` of Q does not match the writhe pattern `(+, −)`.
- **`writhe → I₃` MATCHES**: `I₃(p) = +½`, `I₃(n) = −½` — identical sign+ratio
  pattern `(+, −)` to the writhe ladder, with **zero scale parameter**.

This is consistent with D9 isospin: the `u ↔ d` Z/2 swap that *defines* isospin
is exactly the `σ ↔ σ⁻¹` crossing-sign flip — i.e. the writhe-sign flip. The
writhe sign IS the third isospin component's sign. Matching a sign+ratio
**pattern across the doublet** with no free parameter is a derivation; it is
**not** a one-number coincidence.

Witness assertions: `writhe_splits_p_n = True`, `Y_does_not_split_p_n = True`,
`writhe_to_Y_FALSIFIED` (match_Y = False), `writhe_matches_I3_signratio = True`,
`writhe_matches_Q_signratio = False`.

## 3. Q3 — The ribbon/twist route: a spin ladder, not a charge ladder

Spin = ribbon twist (s5-so3 audit). The ribbon element's eigenvalue on a spin-j
object is `θ_j = q^{j(j+1)}` (Reshetikhin–Turaev framing element). We compute the
twist-eigenvalue ladder per Wedderburn block (SU(2)_q content of Young diagrams
of spin-½ strands):

| Algebra | block λ | spin j | `θ_j = q^{j(j+1)}` | value at q₀ |
|---|---|---:|---|---|
| H₂(q) | (2) | 1 | `q²` | 1.232052… |
| H₂(q) | (1,1) | 0 | `1` | 1 (exact) |
| H₃(q) | (3) | 3/2 | `q^{15/4}` | 1.478869… |
| H₃(q) | (2,1) | 1/2 | `q^{3/4}` | 1.081399… |
| H₃(q) | (1³) | 0 | `1` | 1 (exact) |

The ladder is **monotone increasing in j** (since q₀ > 1), has **no sign
change**, and carries the **j(j+1) Casimir** structure — it is a **spin**
ladder, not an additive charge ladder. It has no half-integer additive charge
structure and does not encode Q, I₃, or Y. (It is the categorical home of spin,
exactly as the s5-so3 audit found: the twist is the framing/spin object, a
*different* gauge factor from the abelian writhe.)

Witness assertions: `twist_singlet_eq_one` (θ₀ = q⁰ = 1),
`twist_H2_sym_eq_q_squared` (θ₁ = q²).

## 4. Verdict per (a)/(b)

| | Question | Answer |
|---|---|---|
| **(a)** | A DERIVED quantum-number assignment with no scale fit? | **YES, partial.** Two derived results: (i) `c = 1/2` fixed by `def:coulomb-charge`; (ii) `writhe → I₃` — sign+ratio match across the nucleon doublet, scale-free, consistent with the D9 `σ↔σ⁻¹` isospin swap. |
| **(b)** | Or Y/charge UNDEFINED with a precise missing object? | **Y is UNDEFINED.** Gell-Mann–Nishijima `Y = 2(Q − I₃)` needs Q and I₃ *independently*. But `Q = writhe/2` and the writhe-derived `I₃` are the SAME inter-nucleon writhe datum — one integer per nucleon cannot fix two independent charges. The **missing object** is a **second, independent crossing/trace invariant** (a baryon-number / color-trace charge `B`) carrying the common baryon `Y = +1` on the color-tube trace, while I₃ = (inter-nucleon writhe)/2 carries the p/n split. |

**Why this is NOT a free-c problem.** The linked-channel audit framed the
obstruction as "`writhe → Y` undefined / not fittable without an unjustified
coupling `c`." This audit sharpens that: `c` is **not** unjustified — it is
`1/2` (Coulomb). The real obstruction is **degeneracy of the charge data**:
the single inter-nucleon writhe gives ONE number per nucleon, but `Y` requires
two independent inputs `(Q, I₃)`. The writhe supplies I₃ (and, via `c=1/2`, a Q
that is *not independent of* I₃ on this datum). A second, structurally
independent charge is the precise missing object.

## 5. Latent-fit flags (self-audit)

- **No coupling tuned.** `c = 1/2` is read off `def:coulomb-charge`, not chosen
  to match any target.
- **No scale parameter in the pattern match.** The `writhe → I₃` claim is a
  sign+ratio comparison; it would survive any rescaling of the writhe ladder.
- **PDG `(Q, I₃, Y)` and `m_n − m_p` are falsification references only.** The
  p/n same-Y test is used to *reject* a candidate map, not to fit one.
- **One-number matches explicitly avoided.** The single-number `m_n − m_p`
  comparison from the linked-channel audit is NOT used as evidence for any
  assignment; only the multi-particle sign+ratio pattern is.

## 6. What this audit does and does not claim

- **Does** DERIVE `c = 1/2` from `def:coulomb-charge` (resolving the
  linked-channel audit's open coupling).
- **Does** show, by sign+ratio across the nucleon doublet (scale-free), that
  the writhe ladder matches **I₃**, is **falsified as a Y map** (p/n same-Y),
  and does **not** match Q.
- **Does** compute the twist-eigenvalue ladder `θ_j = q^{j(j+1)}` per Wedderburn
  block and show it is a spin/Casimir ladder, not a charge ladder.
- **Does** state the precise missing object for Y: a second independent
  crossing/trace charge (baryon-number / color-trace), NOT a free coupling.
- **Does NOT** propose, fit, or tune any coupling, normalisation, charge, or
  h^k; does NOT wire to production; does NOT advance L2 numerically; does NOT
  discharge any Lean `sorry`. No LP/SDP solve appears (no dual emission
  required).

## Cross-references

- The open `c` this audit closes + the 305× falsification:
  [`2026-06-01-inter-nucleon-linked-channel.md`](2026-06-01-inter-nucleon-linked-channel.md)
  (PR #1678).
- U(1)=writhe; spin=ribbon-twist; the gauge-factor structure:
  [`2026-06-01-s5-so3-su2-u1-fiber-action.md`](2026-06-01-s5-so3-su2-u1-fiber-action.md)
  (PR #1672).
- Writhe per operator + the framing phase:
  [`2026-06-01-knot-operator-census-group-actions.md`](2026-06-01-knot-operator-census-group-actions.md)
  (PR #1677).
- The Coulomb-charge definition (the source of `c = 1/2`):
  [`coulomb-charge.lean`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-charge.lean).
- Writhe-as-momentum (the *other* normalisation, `c=1`, not charge):
  [`q-momentum.md`](../../content/quantum-observable-universe/climax-volume-mass/q-momentum.md).
- Isospin from the canonical bowtie (the `σ↔σ⁻¹` = `u↔d` swap):
  [`isospin-from-canonical-bowtie.md`](../../content/quantum-observable-universe/mass-theory/isospin-from-canonical-bowtie.md).
- The mirror-isobar Coulomb-sector localisation (the charge sector breaks both
  `σ` and Hopf-antipode):
  [`isospin-mass-split-em-localisation.md`](../../content/quantum-observable-universe/mass-theory/isospin-mass-split-em-localisation.md).
- Sibling probe on the same 2-strand U(1) (lepton tower; writhe tracks ℤ_n,
  not a gauge charge — consistent):
  PR #1682 (`claude/lepton-t2n-torus-tower-2026-06-02`).
