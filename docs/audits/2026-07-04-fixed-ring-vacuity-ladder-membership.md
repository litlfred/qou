# Fixed-ring vacuity of one-variable bar-ladder membership tests + the 08ds odd-sector artifact

**Date:** 2026-07-04
**Branch:** `claude/mass-binding-gap-review-bbml6m` (PR #3278)
**Probe:** [`computations/qbeta/qbeta_zeta4_faithful_odd_probe.py`](../../computations/qbeta/qbeta_zeta4_faithful_odd_probe.py)
(witness `qbeta-zeta4-faithful-odd.witness.json`, 3 exact assertions)
**Origin:** bean `0zr0` (ζ₄-residue odd-sector route). The probe's own first
design fell to its own devils-advocate pass; the salvage is this theorem +
an exact artifact diagnosis affecting two landed verdicts.

## 1. The theorem (5 lines, standard)

Let σ be the bar involution q ↦ q⁻¹ acting on A = ℚ(√3)[[s]], s = q−1.
σ is an order-2 automorphism of the formal disk. Set t := (s − σ(s))/2;
then σ(t) = −t and ord(t) = 1, so A = ℚ(√3)[[t]] and

$$\mathrm{Fix}(\sigma) \;=\; \mathbb{Q}(\sqrt3)[[t^2]].$$

Consequently **any σ-fixed element of order exactly 2 generates Fix(σ)**:
if u = a·t² + O(t³) with a ≠ 0 and σ(u) = u, then ℚ(√3)[[u]] = ℚ(√3)[[t²]]
(the change of variable x ↦ u(x) is invertible on even-order series).
Likewise every σ-odd element is h × (σ-fixed), since h = q − q⁻¹ is σ-odd
of order 1.

Both ladder variables in play are σ-fixed of order 2 — verified **exactly**
through s¹⁷ in the witness (`sigma_fixed: {u_tilde: true, h_sq: true}`):
ũ = q·b·ℏ_q² and h². Hence

$$\mathbb{Q}(\sqrt3)[[\tilde u]] \;=\; \mathbb{Q}(\sqrt3)[[h^2]] \;=\; \mathrm{Fix}(\sigma).$$

## 2. What this makes vacuous

For any series F in the image of the bar split, membership statements of the
form "the bar-even part is exactly a ũ-series" or "the bar-odd part is
exactly h·D(v) for a σ-fixed order-2 v" are **identities** — they hold for
*every* σ-even/odd regular series, with the truncated rungs absorbing all
orders by construction. The over-determination "margins" are illusory: the
even/odd residual orders vanish automatically.

Recalibrated verdicts (the *numerical rung values* in each remain correct
and useful; only the *membership-as-finding* reading changes):

| Landed verdict | Recalibration |
|---|---|
| `ai81` (ORD 11): "E IS exactly a ũ-series (6 over-determining orders, all zero)" | identity, not evidence for ũ |
| `08ds` (ORD 17, §A): "E(ũ) persists, margin 9" | identity; the margin is not a test of ũ against alternatives — any σ-fixed ord-2 variable gives the same "persistence" |
| `08ds` (ORD 17, §B): "h·D(ũ) + h³·F(ũ) exactly REFUTED (`B_solvable: false`)" | **artifact** — see §3; the true statement is that O = h·D(ũ) holds exactly (identity) |
| this probe's first design: "ζ₄-faithful h-ladder HOLDS, margin 8" | identity (caught before landing; this doc is the honest replacement) |

**Why the mod-4 (ζ₄) grading doesn't rescue the test:** the genuine
ζ₄-faithfulness constraint (odd-q-degree support, the ±i isotypes of
q ↦ ζ₄q) is a statement about *Laurent* data. It does not survive s-adic
completion: ĥ = q + q⁻¹ = 2√(1 + h²/4) ∈ ℚ[[h²]] (verified exactly), so
even-degree elements land inside the h²-completion and the grading
collapses. Genuine ζ₄ structure must be imposed at the **Laurent/Habiro
level** (finite degree support per anchor), which is the honest restatement
of bean `0zr0`'s open direction.

## 3. The 08ds artifact, diagnosed exactly

By §1, O/h ∈ ℚ(√3)[[ũ]] identically, so the 08ds §B joint solve could not
be honestly inconsistent. The bug: `qbeta_bar_split_ord17_probe.py`
computes G = O/h by **shifted division**

```python
G = ser_mul(O[1:] + [0], ser_inv(h_ser[1:] + [0]))
```

which requires O[ORD+1] and pads it with 0 — corrupting G[ORD]. The
n = ORD equation of the joint `linsolve` then uses the corrupted
coefficient, and the system reports `B_solvable: false`.

Confirmed exactly two ways:

1. **Direct solve, no division:** matching O itself against
   {h·ũ^k, k ≤ 8} (rungs read at odd orders 1..17) leaves **zero residual
   at every order through s¹⁷** (`pure_D_on_O_exact: true`), with rungs
   d₀ = 0, d₁ = 1/8 − √3, d₂ = −97/6 + 5√3/288, … .
2. **The corrupted coefficient exhibited:** recomputing G at ORD 18 and
   comparing its s¹⁷ coefficient against the ORD-17 shifted-division value
   gives a nonzero exact discrepancy
   `7043497273/1024 − 13683938963388270847·√3/2056793937149952000`.

Per the (a)/(b) discipline this is not a re-scoping of a refutation — the
08ds §B "refutation" is **withdrawn as an artifact** (the underlying claim
is an identity, so there was nothing to refute or confirm).

## 4. What remains real

- **The exact rung values** — e_k (even/ũ), d_k (odd/ũ), c_j (odd/h²) —
  are canonical data of the net route; whether they carry Habiro/cyclotomic
  or Φ₄ structure is the genuine open question, now correctly located.
- **O[1] = 0 exactly** (`odd_sector_starts_at_h_cubed`): the bar-odd sector
  of log R has no h¹ rung — a real, basis-independent low-order fact.
- The DOF caveat 08ds itself stated ("representability is not the
  question") was correct and is now a theorem rather than an asymptotic
  remark; the two-variable (ũ, h²) family it worried about is in fact
  **one** variable.

## 5. Escalation (coordinate §6)

The 9fnm thread (`c₃^even via exact-rational ℚ[[s]] series`, PR #3262 and
successors) consumes the ũ-ladder framing; its *rung values* are unaffected
but any inference that leans on "margin-N persistence of ũ against
alternatives" or on the 08ds §B refutation should be re-read against §2–§3.
Escalated by PR comment; the owner decides whether the 08ds/ai81 audit docs
get inline errata or pointers to this record.
