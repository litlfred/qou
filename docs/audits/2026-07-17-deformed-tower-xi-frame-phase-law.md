# The deformed κ̃-tower phase law: κ̃_n/ξⁿ ∈ (−i)ⁿ·ℝ — no intrinsic perturbative odd phase at the meridian

**Date:** 2026-07-17 · **Branch:** `claude/bar-odd-s-routes-byoiy8` · **Axis:**
bar-odd S / A_ω (G3) lane · **Tier:** exact-tier numerical identification
(rung 1 to ~6×10⁻²⁰) + Borel–Padé extension of #3692 to the deformed meridian ·
**Discipline:** no fit; no c_k wired; no tier change; no integer Stokes constant
claimed.

**Probe:** [`qbeta_c3_borel_pade_deformed_meridian_probe.py`](../../computations/qbeta/qbeta_c3_borel_pade_deformed_meridian_probe.py)
(+ witness, 5/5 assertions). Inputs: the four deformed rungs κ̃₁…κ̃₄(u_sub)
loaded from the committed #3691 tall-ladder witness (conf digits 19/14/10/6 on
Re; 16/12/8/4 on Im).

## The phase law (the headline)

The deformed rungs at the substrate meridian `u = 2 ln q₀`, `ξ = u + 2πi`,
satisfy

  `arg κ̃_n = −n·arctan(t/π)`,  `t = ln q₀`  —  equivalently  **`κ̃_n / ξⁿ ∈ (−i)ⁿ·ℝ`.**

Measured: rung 1 identification residual **6.2×10⁻²⁰** (machine-exact at
witness precision); rungs 2–4 satisfy the n-multiple law at 9.8×10⁻¹⁶ /
3.3×10⁻¹² / 4.0×10⁻⁹ — each tracking exactly its own rung's confident digits.
(Discovery path: all three large-order ratio arguments came out identical to
7 digits, forcing a single-phase ansatz; `arctan(t/π)` was then the only tested
candidate to survive at 20 digits — `t/π` itself misses at 3.7×10⁻⁴.)

**Meaning.** Since `ξ/2 = t + iπ`, the phase `arctan(t/π)` is exactly the
complement of `arg ξ` — so in the ξ-normalized frame (`ℏ = ξ/N`, the natural
deformed expansion parameter) the tower's coefficients `κ̃_n/ξⁿ` are **real up
to the rigid `(−i)ⁿ` alternation**: the u=0 parity structure (#3628: odd rungs
`ℚ·√3·πⁿ`, even rungs `ℚ·πⁿ`, all real with `ℏ = 2πi/N`) **carries to the
deformed meridian unchanged**. The entire imaginary content of the deformed
rungs — the `Im κ̃₁ = −0.0195` reported as an "intrinsic odd channel" in #3691 —
is the **kinematic frame rotation** of `ξ` off the imaginary axis, nothing more.

**A_ω-lane selection rule (for #3805/#3813).** The perturbative deformed tower
carries **no intrinsic odd phase**: any genuine odd-channel monodromy/Stokes
phase (the A_ω datum) must be **non-perturbative** — it cannot be read from the
κ̃ rungs at any order. This sharpens where A_ω can live and is consistent with
the GGM/3d-index route (#3805) attacking it on the non-perturbative side.

## Borel–Padé at the deformed meridian (extension of #3692)

| quantity | u = 0 (#3692) | u_sub (this probe) |
|---|---|---|
| resummed `Im 𝔙_b` | 0.05545 | **0.05855** (meridian correction +0.0031) |
| truncation | 0.05481 | 0.05706 (odd partial sum #3691: 0.05679) |
| Borel singularity | real `ξ = A ≈ 0.646` | `|Ã| ≈ 0.48–0.64`, **`arg Ã = arctan(t/π)`** (rotates off the real axis — the same frame phase) |
| Stokes-safety of the ray `x = i·t` | singularity off the ray | nearest Padé pole keeps **88.1°** angular margin ⇒ single-valuedness **extends** to the meridian |

So #3692's decisive conclusion — single-valued Borel sum, no median split, no
anchor-dependent trans-series on the imaginary ray — survives the meridian
deformation with a wide margin. Caveat: 4 rungs only (vs 6 at u=0); Padé[2/2]
values are indicative; the action estimate from 3 complex ratios is rough
(|Ã₃| = 0.477 vs Vol(u)/π = 0.643 — within the lenient 35% band asserted, and
the n=1 ratio 0.643 agrees closely; more rungs would settle it).

## The `ser_div` fix — verification record (task 2)

The `O/h` top-order shift-padding artifact diagnosed in #3691 is **fixed on
main**: `qbeta_ck_sseries_exact_rational.ser_div` is valuation-aware, zeroes
the undetermined rows, returns `valid_top`, and its docstring records the
artifact history; the route-1 probe now consumes it. A corpus sweep for the
historical idiom (`ser_mul(a[1:] + [0], ser_inv(b[1:] + [0]))` and variants)
finds **zero remaining offenders** outside `ser_div`'s own docstring. No code
change needed — recorded here so the task closes auditable.

## Cross-references

- Deformed rungs source: `qbeta-ohtsuki-deformed-kappa3-tall-ladder.witness.json` (#3691)
- u=0 resummation + Stokes argument: `qbeta_c3_borel_pade_resummation_probe.py` (#3692, merged)
- u=0 exact parity of the rungs: [`2026-07-12-ohtsuki-higher-rungs-exact.md`](2026-07-12-ohtsuki-higher-rungs-exact.md) (#3628)
- Three-routes audit (κ̃ extraction + the `π·u` meridian term): [`2026-07-12-bar-odd-s-three-routes.md`](2026-07-12-bar-odd-s-three-routes.md) (#3691)
- A_ω/G3 lane: #3805 (GGM 3d-index), #3813 (pentagon rigidity + cross-pin), [`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md)
