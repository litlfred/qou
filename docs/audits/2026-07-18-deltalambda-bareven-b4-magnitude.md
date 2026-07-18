# Bar-even symmetrisation of the b₄ cumulant does NOT crack the strong Δ_λ magnitude — it is a structural no-op

**Date:** 2026-07-18 · **Branch:** `claude/deltalambda-bareven-b4-2026-07-18` ·
**Type:** FINDING — honest negative (scope-(a)) with a scope-(b) sub-result.
Δ_λ magnitude front, **Vector 3** of the 2026-07-18 attack-vector map
([`2026-07-18-deltalambda-attack-vector-map.md`](2026-07-18-deltalambda-attack-vector-map.md) §4 row 3).
No fit, nothing wired.

- Probe: [`computations/deltalambda/deltalambda_bareven_b4_magnitude_probe.py`](../../computations/deltalambda/deltalambda_bareven_b4_magnitude_probe.py)
  (witness [`deltalambda-bareven-b4-magnitude.witness.json`](../../computations/deltalambda/deltalambda-bareven-b4-magnitude.witness.json), 9/9 assertions pass, mpmath 60 dps, exit 0).
- Lean scope-(b): [`content/quantum-observable-universe/lean/QOU/MassTheory/B4CumulantBarEven.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/B4CumulantBarEven.lean)
  (`he4WritheDet_bar_even`, sorry-free, `lean`-direct exit 0).

## 0. The hypothesis (Vector 3)

Following the c₃ precedent (`rem:ohtsuki-tower-bar-parity` + `OhtsukiTowerBarParity.lean`:
the bar involution `q ↦ q⁻¹` splits an object into a bar-even *mass* face and a
bar-odd *decay* face), the hypothesis was that the connected cumulant
`b_A = -ln det(I + m·G_A)` (#3924) mixes bar-even and bar-odd contributions, and
that **symmetrising under the bar involution before evaluating** —
`b_A^{even} = ½(b_A(q) + b_A(q⁻¹))` — would isolate the bar-even (mass/binding)
part and thereby tame the ⁴He magnitude overshoot (#3952: 2.6–10.6×). The forward
test: does `b_A^{even}/b_2^{even}` reproduce the isospin-corrected strong ratios
`{ρ_strong(3), ρ_strong(4)}` at a **single parameter-free** `m`, simultaneously
for A=3 and A=4?

## 1. Isospin-correcting the ρ targets (using #3990's E_C)

The AME absolute ratios `ρ = B/B_D` are `ρ(³H)=3.813`, `ρ(³He)=3.469`,
`ρ(⁴He)=12.72`. These carry Coulomb; the STRONG (isospin-even) part is what
Vector 3 must reproduce. Using the Lean-proved premise (PR #3986,
`IsospinMirrorInvariance.lean`: the strong ³H/³He split is **exactly 0**) plus
the parameter-free Coulomb of #3990:

- **A=3.** ³H has `Z=1` ⇒ no proton pair ⇒ `E_C(³H)=0`. By mirror invariance
  `strong(³He)=strong(³H)`, so the strong A=3 value **is** `B(³H)` itself:
  `ρ_strong(3) = B(³H)/B_D = 3.813`. (Cross-check: `ρ(³He) + E_C(³He)/B_D =
  3.469 + 0.344 = 3.813`, consistent.) **Note the task-hint "≈3.6" is the naive
  symmetric average `½(3.813+3.469)=3.641`, which is physically incorrect** — it
  under-counts because only ³He carries Coulomb, so the true strong value is the
  Coulomb-free ³H endpoint, not the midpoint.
- **A=4.** ⁴He has `Z=2` ⇒ one pp pair; the pp-Coulomb is added back:
  `E_C(⁴He) = E_C(³He)·(3/4)^{1/3} = 0.694 MeV` (same `Z(Z−1)=2`, same coef,
  radius `∝ A^{1/3}`). `ρ_strong(4) = (B(⁴He)+E_C(⁴He))/B_D = 13.03`.

**Isospin-corrected strong targets: `{ρ_strong(3), ρ_strong(4)} = {3.81, 13.03}`.**

## 2. The exchange matrices (#3924 writhe vs #3986 isospin-product)

Two candidate `G_A` appear in the corpus; the probe tests both:

| matrix | off-diag entry | det | even in m? | mirror-invariant? |
|---|---|---|---|---|
| **WRITHE** (#3924) | `sgn(type_i,type_j)·m`, pp=+1,nn=−1,pn=+1 | A=4: `(1−5m²)(1−m²)`; spectrum `{±√5,±1}` | **yes (A=4)** | no (A=3 isotope-dependent) |
| **ISO-product** (#3986) | `m·s_i·s_j`, s=±1 | `(1+(A−1)m)(1−m)^{A−1}` | no | yes (A-only) |

Both dets are **verified exactly** against `mp.det` in the probe (45-digit match).

## 3. The decisive obstruction — the parameter-free magnitude is ALREADY bar-even

The corpus's DERIVED parameter-free bond magnitudes are

- `g_reeb = 1/√(5+(q₀−1)²/q₀) = 0.44673`, and
- `z_naive = 1/[2]_v = 0.49932`,

and **both are bar-even**: `g_reeb(q⁻¹)=g_reeb(q)` and `z(q⁻¹)=z(q)` (proved
algebraically and confirmed to 40 digits, witness assertions `g_reeb_bar_even`,
`z_naive_bar_even`). Since `m(q⁻¹)=m(q)`, the cumulant satisfies `b_A(q)=b_A(q⁻¹)`
**identically for every A**, so

> **bar-even symmetrisation `½(b_A(q)+b_A(q⁻¹)) = b_A(q)` is a structural NO-OP
> on the actual construction.**

There is no bar-odd part to remove. The overshoot is a genuine **bar-even
magnitude** problem, not a bar-parity contamination. This is *consistent with*
(not a re-derivation of) the 2026-06-25 scope-(b) pruning
([`2026-06-25-he4-magic-factor-bar-even-pruning.md`](2026-06-25-he4-magic-factor-bar-even-pruning.md))
that ⁴He binding must be bar-even because ⁴He is self-mirror: the construction
already lives entirely in the bar-even (cosh) sector.

## 4. Forward test at the parameter-free magnitude (no fit)

At `m = g_reeb` (parameter-free, fixed before comparison):

| matrix | ρ3 | ρ4 | vs `{3.81, 13.03}` |
|---|---:|---:|---|
| WRITHE | 6.74 | **28.54** | ρ4 **+119%** overshoot (matches #3952) |
| ISO | 2.45 | **4.16** | ρ4 **−68%** undershoot |

Bar-even symmetrisation changes **none** of these (§3). `z_naive` is excluded for
WRITHE (`> 1/√5` ceiling ⇒ `det<0` at A=4); its ISO row is likewise far off
(ρ4=4.05). **Neither matrix lands the strong targets at the parameter-free
magnitude, and symmetrisation cannot move them.**

## 5. Steelman — even a hypothetical free bar-odd m fails the coherence gate

Granting (contrary to §3) a *free* bar-odd magnitude (`m(q⁻¹)=−m(q)`, so
symmetrisation projects onto the even-in-`m` part), the probe scans whether any
single `m` lands both strong targets:

- **WRITHE.** `det(I+mS)=(1−5m²)(1−m²)` is a function of `m²` alone — a scope-(b)
  Lean fact (`he4WritheDet_bar_even`, `det(I+m·S)=det(I−m·S)`, the symmetric
  `{±√5,±1}` spectrum). So bar-even = raw at A=4; symmetrisation is provably
  powerless at the **dominant** wall. Forcing `ρ4=13.03` gives `m*=0.4269` and
  `ρ3=6.02` (**+58%**); forcing `ρ3=3.81` gives `m=0.248` and `ρ4=6.79`
  (**−48%**). No coincidence.
- **ISO raw.** `ρ4 ∈ (3, 6)` monotone (limits `m→0: 6`, `m→1: 3`) — it **cannot
  reach 13.03 at any m**.
- **ISO bar-even.** Symmetrisation *does* lift ρ4 (the odd-in-`m` terms of the
  A≥3 det are removed), reaching `ρ4_even ≈ 13.3` near `m=0.32` — but that is
  exactly the ceiling where `det(I−mS)=1−3m` crosses zero (`m=1/3`), driving the
  cumulant complex/unphysical, while `ρ3_even` stalls near `3.44` (−10% vs 3.81).
  No physical single-`m` coherent match.

**Coherence gate FAILS on every route.** The witness assertion
`single_m_lands_both_targets = False` records this.

## 6. Verdict (anti-fit / anti-laundering, STRICT)

**(a) HONEST NEGATIVE — bar-even symmetrisation does not crack the strong
magnitude — carrying a (b) sub-result.**

> Vector 3 is a **structural no-op** on the actual construction: the corpus's
> parameter-free bond magnitude (`g_reeb`, `z_naive`) is already **bar-even**
> (proved), so `½(b_A(q)+b_A(q⁻¹)) = b_A(q)` for every A. The ⁴He overshoot
> (#3952) is therefore a genuine bar-**even** magnitude deficit, not a
> bar-parity contamination there is anything to remove. Steelmanned with a
> hypothetical free bar-odd magnitude, no single `m` reproduces the
> isospin-corrected strong ratios `{3.81, 13.03}` on any route (WRITHE
> `ρ4=13→ρ3=6.0`; ISO raw `ρ4` capped at 6; ISO bar-even reaches `ρ4≈13` only
> at the `det=0` unphysical boundary with `ρ3≈3.4`).
>
> **Scope-(b) sub-result** (proved invariant): the A=4 WRITHE cumulant
> determinant is a function of `m²` — `det(I+m·S)=det(I−m·S)` — so bar-even
> symmetrisation is provably powerless at the dominant A=4 wall regardless of
> magnitude parity (Lean `he4WritheDet_bar_even`, sorry-free).

Anti-laundering triple-check (task requirement): the magnitude `m` is fixed
parameter-free (`g_reeb`/`z_naive`, bar-even) **before** comparison; the §5
free-`m` scan is a *falsification* test (it shows the hypothesis fails even with
a free parameter), never a fit — nothing from it is promoted or wired. **Not
derived ⇒ not wired:** no production change, no tier change, no content-block
edit; nothing is canonical.

## 7. What this leaves and where the wall goes next

The strong magnitude wall stands. Bar-parity is **not** the missing ingredient —
the cumulant is already bar-even. This *narrows* the search: the deficit is in
the **magnitude scale / higher many-body structure**, consistent with the
attack-vector map's higher-value leads that do not rely on parity:

- **Vector 1** — per-pair hyperbolic volume on the `K₄` coordination graph
  (the collective, non-additive term #3943 measured).
- **Vector 2** — the icosahedral `1/√5` bridge (the `{±√5,±1}` ceiling ties to
  the Σ(2,3,5) S-matrix; a *proved* algebraic coincidence, not a fit).

## Notes on verification (disk-constrained sandbox)

The `lean`-direct verification of `B4CumulantBarEven.lean` (exit 0, sorry-free)
was run against a combined olean set (the restored Mathlib cache + the shared
checkout's `aesop`/`batteries`/`Qq`/`proofwidgets` dep oleans) because the full
cache could not be extracted in one pass (disk cap). The file imports only
`Mathlib.Tactic.Ring`; both theorems close by `ring`. The
determinant→closed-form link (`det(I+mS)=(1−5m²)(1−m²)`) is the probe's exact
`mp.det` check (assertion `writhe_det_matches_closed_form`); the Lean formalises
the evenness half.

## Files

- probe: [`computations/deltalambda/deltalambda_bareven_b4_magnitude_probe.py`](../../computations/deltalambda/deltalambda_bareven_b4_magnitude_probe.py) (new)
- witness: [`computations/deltalambda/deltalambda-bareven-b4-magnitude.witness.json`](../../computations/deltalambda/deltalambda-bareven-b4-magnitude.witness.json) (new, audit-only, 9/9 pass)
- Lean: [`content/quantum-observable-universe/lean/QOU/MassTheory/B4CumulantBarEven.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/B4CumulantBarEven.lean) (new, sorry-free) + registered in `QOU.lean`
- this audit: `docs/audits/2026-07-18-deltalambda-bareven-b4-magnitude.md`
- context consumed (unchanged): `2026-07-18-deltalambda-attack-vector-map.md`,
  `2026-07-18-deltalambda-coulomb-mirror-split.md` (#3990),
  `2026-06-25-he4-magic-factor-bar-even-pruning.md`,
  `b4_slater_antisymmetrizer_exchange_sign.py` (#3924),
  `IsospinMirrorInvariance.lean` (#3986),
  `rem-ohtsuki-tower-bar-parity.md` / `OhtsukiTowerBarParity.lean`
