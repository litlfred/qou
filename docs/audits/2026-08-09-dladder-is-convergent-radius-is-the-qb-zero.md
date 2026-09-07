# Correction: the c₃ D-ladder is CONVERGENT — the radius is `ρ = ũ(q*) = 0.1427999966446896889…`, the image of a **Q_b zero** that the singularity search omitted

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


**Date:** 2026-08-09 · **Bean:** `qou-qb8e` (resummation arm) ·
**Branch:** `claude/anchor-followups-2026-08-08` ·
**Corrects:** [`2026-07-12-dladder-divergence-correction.md`](2026-07-12-dladder-divergence-correction.md)
(which itself over-turned the correct reading), registry row **KC22**, and
`docs/precision-goals.md` §"Open compute levers" item (i) ·
**Tier:** analytic derivation + numerically verified, **no fit** (the amplitude
was predicted from a residue *before* it was compared to any `d_k`) ·
**Discipline:** scope-(b) structural claim **with a named invariant** (§2); no
`c_k` wired; no tier change on c₃; no witness written.

---

## 0. Result

`D(ũ) = Σ_k d_k ũ^k` is **not divergent**. It is the Taylor series at `ũ=0` of
the analytic function

```
D(w)  =  [ log R(q) − log R(1/q) ] / ( 2 (q − 1/q) ) ,        w = ũ(q),
```

and it has a **finite radius of convergence**

```
ρ  =  ũ(q*)  =  0.14279999664468968890572088577932032058109273315046…
1/ρ =         7.0028012849899955047002755670642702546578912740699…
```

where `q*` is the unique real root `> 1` of the irreducible degree-12 factor of
the `Δ_net` numerator,

```
q* = 1.4898947996883652482253115227781736826531279179281…
     root of  q¹²+2q¹¹−4q¹⁰−8q⁹+6q⁸+16q⁷−10q⁶−16q⁵+6q⁴+8q³−4q²−2q+1  (irreducible /ℚ)
```

i.e. **a zero of `Q_b`** — a point where `R → 0` and `log R` has a plain
logarithmic branch point.

**Consequence.** There is no instanton action, no Borel-plane singularity to
locate, no Stokes constant to extract, and no Écalle/`Φ_b` resummation to
perform, *because the series converges*. The whole resummation arm of the c₃
front (≈ 20 probe witnesses under `computations/qbeta/qbeta-dladder-*` and
`qbeta-*-borel-*`) is answering a question whose premise is false.

**What this does NOT do** (anti-laundering, load-bearing): it does **not**
derive c₃, does **not** change c₃'s `cal-anchored` tier, and does **not** close
L2. The μ–p anchor swing on Q_β is still **29.96 ppb = 3.84 × the 7.797 ppb L2
target** — c₃ remains necessary-but-not-sufficient. See §6.

---

## 1. What the earlier search missed

The 2026-07-12 correction rested on one argument:

> *"No singularity at ρ. A convergent series with radius 0.143 must have a
> singularity of `log R(q(ũ))` at `|ũ| = 0.143`. A full search found none: the
> sqrt branch points `q⁴+q²+1=0` and the `ũ'(q)=0` folds map to `ũ=0`, the
> `cos(α_eff)=0` roots sit at `|ũ| ≥ 1.47`, and the nearest singularity of any
> kind (a `QA` zero / a complex fold) is at `|ũ| = 0.45–0.78 ≫ 0.143`."*

Every item in that list is correct. The list is **incomplete**: it enumerates
the branch points of the algebraic ingredients, the folds of the `ũ` map, the
`Q_A` zeros and the `cos α_eff` zeros — but **not the zeros of `Q_b` itself**,
i.e. the roots of the `Δ_net/(q−1)` numerator. `log R = log Q_b − log Q_A −
log cos α_eff`, so a simple zero of `Q_b` is a logarithmic branch point of
`log R` exactly like a zero of `Q_A`. The three nearest singularities in the
`w = ũ` plane are all `Q_b` zeros.

Full inventory (verified this session, `mpmath` 50 dps):

| `\|ũ\|` | source | pre-image |
|---|---|---|
| **0.1427999966** | **`Q_b` zero** | **q\* = 1.4898947997 (real)** ← **the radius** |
| 0.2575435453 | `Q_b` zeros | q = 0.9960006825 ± 0.6037917847 i |
| 0.4501964644 | `ũ'=0` fold | t³ = 2, q = e^{±0.8895 i} |
| 0.4994123601 | `Q_b` zeros | q = 0.5274507931 ± 0.3868592278 i |
| 0.7283301958 | `Q_b` zero | q = 0.4244244436 |
| 0.7749226177 | `Q_A` zero | q = 1+√2 |
| ≥ 1.4686685750 | `cos α_eff` zeros | nearest q = 3.2208761531 |

The "0.45–0.78" the earlier search reported is rows 3 and 6. The Domb–Sykes
`ρ ≈ 0.143` that PR #3716 originally measured, and that the 2026-07-12
correction discarded as a "finite-n shadow", was **right**, and is row 1 to the
three digits it could resolve.

Sanity of the identified point (50 dps): `Δ_net_reg(q*) = 1.6×10⁻³⁴` (a genuine
zero), `Q_A(q*) = 0.6625179032 ≠ 0`, `cos α_eff(q*) = 0.9610340398 ≠ 0`. So the
branch point at `q*` is purely logarithmic and comes from `Q_b` alone.

### The clean coordinate

`ũ` is invariant under the bar involution `q ↦ 1/q` and is a rational-plus-sqrt
function of `t = q + 1/q` alone:

```
ũ = (t−2)·√(t²−1) / t ,        h = q − 1/q = √(t²−4) ,        t = q + 1/q
```

(`(q−1)²/q = t−2`, `√(q⁴+q²+1)/(q²+1) = √(t²−1)/t`, both exact.) `dũ/dt = 0`
iff **`t³ = 2`** — the "complex fold" — with critical value
`ũ = −(2^{2/3}−1)^{3/2} = −0.4501964644` (row 3, in closed form). Because `h` is
bar-odd and `ũ` bar-even, `D = (bar-odd part of log R)/h` is a *function of `t`*,
regular at `t = 2`; that is the structural reason `log R = E(ũ) + h·D(ũ)` holds
at all.

---

## 2. The named invariant

> **Invariant (local form at the dominant singularity).**
> `D(w) = φ(w)·log(1 − w/ρ) + ψ(w)` with `φ, ψ` analytic at `w = ρ`, and
> `φ(ρ) = 1/(2 h(q*))`, because `log R` has a **simple-zero logarithmic** branch
> point at `q*` and `w ↦ q` is conformal there.
>
> Hence, with **no free parameters**:
> ```
> d_k  =  − (1/(2h*)) · ρ^{−k} / k · (1 + O(1/k)) ,      all d_k < 0
> ```
> ```
> ρ  = ũ(q*) = 0.14279999664468968890572088577932032058109273315046…
> h* = q* − 1/q* = 0.81870647135191786409107809315126392490089020462376…
> 1/(2h*)      = 0.61071949165658530740674396151590239214873489246317…
> ```

Anything claiming Gevrey growth, a nonzero instanton action, or a Stokes
ambiguity in this ladder must **first exhibit a singularity of
`log R(q) − log R(1/q)` strictly inside `|ũ| < ρ`.** No such singularity exists:
the list in §1 is the complete singular set of `log R` (zeros/poles of the two
rational factors, zeros of `cos α_eff`, branch points of the two square roots),
and the folds of `ũ` are separately accounted. That is the reusable falsifier.

`ρ²` is algebraic of degree 12: it is a root of

```
54289 y¹² − 3911138 y¹¹ + 116808051 y¹⁰ − 1868914862 y⁹ + 17045659457 y⁸
 − 85085244936 y⁷ + 190185702360 y⁶ − 60555609576 y⁵ − 2279811744 y⁴
 − 4840969216 y³ + 460646672 y² − 30563712 y + 473344
```

(`t*` is a root of the irreducible `t¹²−24t¹⁰+234t⁸−1208t⁶+3529t⁴−5572t²+3728`.)

---

## 3. Verification — prediction first, then measurement

The amplitude `1/(2h*)` above was computed from the residue **before** being
compared to any `d_k`. The ladder was then rebuilt and extended.

**Ladder extension.** The blocker at `k=41` was purely computational: the
production builder holds every coefficient as an exact `ℚ(√3)` **sympy** scalar
and calls `radsimp∘cancel∘together` on each one, and two steps are `O(ORD³)`
(Horner composition with `q↦1/q`, and `cos` by repeated powers). Timings this
session: exact builder ORD 43 → **80 s**, ORD 83 (`k=41`) → **570 s**. A
numeric-coefficient rebuild of the *same* pipeline (mpmath at high dps,
`O(ORD²)` Möbius composition and the coupled `c′=−α′s, s′=α′c` recursion) does
ORD 403 → `k=201` in **53 s**. It agrees with the exact `ℚ(√3)` ladder to **200+
digits for every `k ≤ 41`** and to 349 digits for `k ≤ 21` (against the
committed `d_k_exact`). The over-determination survives: the odd-order residuals
`G[2n+1] − model[2n+1]` vanish for all 201 over-determining orders, so
`log R = E(ũ) + h·D(ũ)` is now checked far past the recorded "ORD 19 with 9
over-determining orders zero".

**Test.** `e_k := k·|d_k|·ρ^k` must converge to `1/(2h*) = 0.610719491657`.

| k | `\|d_k\|^{1/k}` | `e_k` | `e_k / (1/(2h*))` | `k(e_k/AMP − 1)` |
|---|---|---|---|---|
| 21 | 5.910378342 | 0.596255456 | 0.976316 | −0.4974 |
| 41 | 6.318026968 | 0.603041457 | 0.987428 | −0.5029 |
| 101 | 6.657099336 | 0.607656399 | 0.994984 | −0.5066 |
| 201 | 6.803653488 | 0.609176634 | 0.997474 | −0.5078 |

`e_k → 1/(2h*)` with a clean `1 − 0.509/k` correction and **no oscillation**
(an oscillation would signal a second singularity at the same modulus; a
different limit would signal a nearer one). Richardson on `d_k/d_{k−1}` at
`k ≈ 201` gives **7.00289002** against the exact `1/ρ = 7.00280128`
(rel. 1.3×10⁻⁵).

**End-to-end.** The closed form `D(w) = [log R(q) − log R(1/q)]/(2(q−1/q))`,
with `q` obtained by inverting `ũ(q) = w`, reproduces `Σ_{k≤201} d_k w^k` to
**48 digits** at `w = 0.005…0.05` and 33 digits at `w = 0.10`; at `w = 0.13` the
agreement (1.7×10⁻¹⁰) is limited by the series' own truncation tail
`(0.13/ρ)²⁰¹/201 ≈ 3×10⁻¹¹`. The `d_k` are therefore the Taylor coefficients of
an honest analytic germ, not a formal-only object.

**Radius from both sides.** At `w = 0.1428` (just **outside** ρ) the terms
`|d_k w^k|` are `0.01209, 0.006076, 0.004058, 0.003031` at `k = 50, 100, 150,
201` — i.e. exactly `AMP/k` (`0.01221, 0.00611, 0.00407, 0.00304`), the boundary
`1/k` decay. At `w = 0.15` they grow (`0.14, 0.83, 6.50, 59.6`); at `w = 0.20`
they explode (`2.5e5 … 7.7e26`).

---

## 4. Every earlier diagnostic, re-explained (not merely contradicted)

The same `d_k` are involved — all four published diagnostics reproduce exactly:

| corpus value | reproduced |
|---|---|
| root test @ k=21 = 5.91 | 5.9103783 |
| root test @ k=27 = 6.08 | 6.0817125 |
| `log\|d\|/(k log k)` @ k=41 = 0.4963972525 | 0.496397252466 |
| `log\|d\|/k²` @ k=41 = 0.04496114563 | 0.044961145628 |

**(a) "Root test rises without plateau."** For `|d_k| = AMP·ρ^{−k}/k`, the root
test is `ρ^{−1}(AMP/k)^{1/k}`, which rises to `1/ρ` like `exp(−log k / k)` —
still 5 % low at k=101. Measured vs. this parameter-free prediction:

| k | measured | predicted | rel |
|---|---|---|---|
| 21 | 5.91037834 | 5.91712806 | 1.1e-3 |
| 31 | 6.16632924 | 6.16957192 | 5.3e-4 |
| 41 | 6.31802697 | 6.31992959 | 3.0e-4 |
| 101 | 6.65709934 | 6.65743076 | 5.0e-5 |

A rising root test is what a convergent series with a `1/k` prefactor looks
like. It is not evidence of `radius → 0`.

**(b) "`C > 0` in `log|d_k| = A + Bk + C·k·log k`, and `C` drifts."** Fit that
same three-parameter form to the **exact convergent law**
`k·log(1/ρ) − log k + log(AMP)`, which has `C ≡ 0` by construction:

| window | `C` from real `d_k` | `C` from the convergent law |
|---|---|---|
| 6…21 | 0.0773736 | 0.0840706 |
| 6…27 | 0.0667280 | 0.0718886 |
| 14…27 | 0.0481509 | 0.0506422 |
| 10…41 | 0.0431487 | 0.0454707 |
| 20…61 | 0.0263786 | 0.0271488 |
| 40…101 | 0.0149125 | 0.0151510 |
| 80…101 | 0.0109762 | 0.0111009 |

The published values (0.077, 0.062/0.067, 0.048, and `C_full = 0.0613` at k=31)
are **exactly what a convergent series produces** under this diagnostic. `C` is
a spurious parameter absorbing the `−log k` term; it decays like `1/log k`. The
reading *"C drifts down ⇒ no fixed Gevrey index ⇒ structural q-Gevrey drift"* is
backwards: the drift is `C → 0`, i.e. **no** super-exponential term. Meanwhile
the fitted `B` climbs 1.5936 → 1.8749 toward `log(1/ρ) = 1.9463102525`.

**(c) The `Δ²log|d_k|` test, and the discriminator that was missing.** The
single-instanton probe fit `Δ² = m/k + b` and read `b → 0` as "ordinary
Gevrey". But *both* live hypotheses give `b → 0`; the discriminating question is
`1/k` versus `1/k²`. Measured:

| k | `k·Δ²` | `k²·Δ²` |
|---|---|---|
| 20 | 0.047983 | 0.95967 |
| 40 | 0.024382 | 0.97528 |
| 80 | 0.012343 | 0.98746 |
| 99 | 0.0099984 | 0.98984 |

`k²Δ² → 1` and `kΔ² → 0`. For `log|d_k| = −k log ρ − log k + const`,
`Δ² log|d_k| = −Δ² log k ≈ +1/k²` — **exactly 1**. The Gevrey index is
`κ = 0`. This is the cheap test that settles the k≤41 data as it stands.

**(d) "The carrier SATURATES at k=31 (`|O₃₁ − O₂₁| ≈ 6.94e-29`), so more terms
will not move it."** That number is reproduced exactly — and it is **geometric
convergence**, not a floor. At the CAL-2/muon pin
(`q₀ = 1.10997859555733471989…`, the pin `build_d_ladder` itself reads),
`ũ(q₀) = 0.00945395003124134625`, so `ũ/ρ = 0.0662041334` — the anchor sits
**15.10× inside** the radius, and each rung buys 1.18 decimal digits:

```
K=  21   h·D = −0.003486063636129187405605313860226143       |Δ| = 1.26667e-15
K=  31   h·D = −0.003486063636129187405605313929674525       |Δ| = 6.94484e-29   ← the "saturation"
K=  41   h·D = −0.003486063636129187405605313929674524979867 |Δ| = 7.78503e-41
K= 101   h·D = (unchanged to 40 digits)                      |Δ| = 9.63488e-53
K= 201   h·D = (unchanged to 40 digits)                      |Δ| = 7.56366e-124
```

with the analytic tail bound `|Σ_{k>K} d_k ũ₀^k| ≤ AMP·x^{K+1}/((K+1)(1−x))`,
`x = ũ₀/ρ`, giving `3.41e-28 (K=21)`, `3.79e-40 (K=31)`, `4.67e-52 (K=41)` —
holding, and tight to within ~5×. So `h·D` at the anchor is **already pinned to
38 digits by the committed `k ≤ 41` ladder**, with a rigorous bound, and no
resummation. (Same to 1e-12 at the `q_parameter.Q_50_DIGIT_STR` pin;
`ũ₀` differs by 5×10⁻¹³ relative, `ũ₀/ρ` is unchanged to 10 digits.)

---

## 5. What is actually refuted, and at what scope

**Scope-(b), with the invariant in §2 —** *the D-ladder is convergent with
radius `ρ = ũ(q*)`; there is no Gevrey growth, no Borel-plane singularity, no
instanton action, and no Stokes ambiguity in `D`.* The falsifier is explicit: a
singularity of `log R(q) − log R(1/q)` strictly inside `|ũ| < ρ`.

Consequently these are **not open problems**, they are **ill-posed**:

- "identify the Borel-plane instanton action for the `exp(Bk + Ck log k)` class"
  (the bean's stated open gate) — there is no such class;
- the Leroy estimator gate failing at every scanned `s`; the `k=21`
  dlog-Padé/root-test inconsistency; the `s*` drift `0.1865 → 0.1594`; the
  "estimator gap 0.172 persists at k=31" — all are estimators for a divergent
  series applied to a convergent one;
- the parity-split / two-action / single-vs-two-level analyses of `D`'s
  "Borel action";
- "more terms alone will not move it" (§4d).

**Unaffected (all exact, all still stand):** the exact `ℚ(√3)` `d_k`; the parity
structure (odd `k` → `√3`-part small denominator); the 3-smooth Ohtsuki–Habiro
denominators and the 2-adic parity grading; the **non-holonomicity** of `D`
(KC22's exact linear algebra) — a convergent analytic function need not be
holonomic, and `log(cos(algebraic))` generically is not. What falls is only
KC22's *inference* "⇒ transcendental/**resurgent** (Écalle acceleration class)".

**Scope-(a) dead ends that stay dead:** fixed-order/anchor-invariant
resummation, geometric `q₀`, ratio-based `W_λ`. Nothing here re-opens them.

---

## 6. What this does NOT buy — the anchor is untouched

Per the STRICT pin discipline (`docs/precision-goals.md` §"Pin discipline",
bean `qou-qb8c`): the μ–p anchor swing on Q_β is **29.96 ppb**, i.e. **3.84×**
the entire 7.797 ppb L2 target, and 2.4 % of the 1248 ppb residual. Dissolving
the resummation blocker removes an obstruction on the road to a derived c₃; it
does not derive c₃, and a derived c₃ alone still would not meet L2 at both pins.

Also unchanged: the bean's own recorded finding that the carrier is
**anchor-blind** (spread 1.23e-9) and is therefore *not* the swinging empirical
`S` — so `S = h·D(ũ)` remains schematic rather than a tight identity, and this
audit says nothing about that gap. The honest statement is: **the resummation
arm was never the gate; it was an artifact.** The gate is still the map from a
bar-odd fibre-level object to an anchor-*dependent* number.

---

## 7. Reproduction

No production script was run and no witness was written (bean `qou-qb8e` is
read-only on production this session). Everything above is reproducible from
committed artifacts:

1. `d_k` for `k ≤ 21`: `computations/qbeta/qbeta-dladder-generating-function-structure.witness.json`
   → `data.d_k_exact` (exact `ℚ(√3)` strings).
2. `d_k` for `k ≤ 41`: import
   `qbeta_dladder_generating_function_structure_probe` with `argv[1]=83` and
   call `build_d_ladder()` (~570 s; does **not** run `main()`, writes nothing).
3. `q*`: `sympy.factor_list` of the numerator of `Δ_net/(q−1)` (with `Δ_net`
   from `free-neutron-decay.witness.json`), take the irreducible degree-12
   factor, real root `> 1`.
4. `ρ = ũ(q*)`, `h* = q* − 1/q*`, `AMP = 1/(2h*)`; then check
   `k·|d_k|·ρ^k → AMP`.

Step 4 needs no new tooling and settles the question on the `k ≤ 21` data
already committed (`e_21/AMP = 0.9763`, correction `−0.497/k`).

---

## 6. Witness ledger — which of the 29 stand, and which are now ill-posed

*Added 2026-08-09 by the foreground session, as the owed enumeration behind §5.
**No witness file was edited or regenerated**; this is a reading note. Producers
are unchanged and every one of the 29 still reports `allPassed: true` — that is
the point, and the reason a bulk re-run would not have caught this. They compute
what they say they compute; the question several of them answer is the one that
turned out to be ill-posed.*

**A. UNAFFECTED — the arithmetic stands in full (6).** Nothing here depends on
the growth class; a convergent series need not be holonomic, and
`φ(w)log(1−w/ρ) + ψ(w)` over a degree-12 field is exactly the sort of element
that is not low-order P-finite. The 2-adic parity grading and its Lean anchors
are likewise untouched.

    qbeta-dladder-generating-function-structure     (the exact d_k, k<=21 — the DATA)
    qbeta-dladder-coupled-qsqrt3-recurrence
    qbeta-dladder-q-holonomic-base3
    qbeta-dladder-log-q-holonomic
    qbeta-dladder-padic-graded-prime
    qbeta-dladder-qborel-2adic-transport

**B. ILL-POSED — divergent-series estimators applied to a convergent series
(11).** Each is a correct computation of a quantity that does not exist. Their
recorded failures ("gate fails at every `s`", "length-blocked", "estimator gap
persists") are not obstructions to be overcome; they are the estimators
detecting that there is nothing to estimate.

    qbeta-dladder-ecalle-acceleration               Leroy gate fails at every s
    qbeta-dladder-ecalle-phib-resummation
    qbeta-dladder-single-instanton-extraction       "length-blocked at k=41"
    qbeta-dladder-fibre-branch-stokes-ambiguity     r* = 0.147 IS the ratio est. of rho
    qbeta-dladder-fibre-two-action
    qbeta-dladder-jackson-qborel-acceleration
    qbeta-dladder-qborel-leroy-resummation
    qbeta-dladder-parity-split-resummation
    qbeta-dladder-parity-odd-singularity-even-order
    qbeta-dladder-barodd-borel-pade-laplace
    qbeta-dladder-parity-adjudication               "UNDECIDABLE at k=21"

**C. PARTIALLY superseded (1).**

    qbeta-dladder-extension-singularity   The exact extension to k=31 STANDS and is
                                          reusable. Its reading "Divergence-class C:
                                          0.07737 -> 0.06134" is the spurious 1/log k
                                          decay, not a converging exponent.

**D. NOT ASSESSED — different object, needs its own pass (4).** These concern
the *deformed meridian* and the odd-channel Stokes structure, not `D(ũ)`. The
radius result does not automatically transfer and no claim is made here either
way.

    qbeta-c3-borel-pade-deformed-meridian
    qbeta-c3-borel-pade-deformed-rungs
    qbeta-c3-borel-pade-resummation
    qbeta-odd-channel-stokes-borel

**What a maintainer should do with B.** Not delete them — they are the evidence
that the resummation arm was pursued properly and exhausted, and their inputs
(the exact ladder) remain live. Re-tier them as **scope-(b) closed / ill-posed**
rather than **scope-(a) negative**, so the next reader does not read "gate fails,
needs more terms" as an open lever. That re-tiering is a registry edit and is
**not made here**; it is tracked on bean `qou-qb8e`.

**Corrections landed alongside this note** (both were listed as owed):
`docs/precision-goals.md` "Open compute levers" item (i) — the c₃ resummation
lever is **withdrawn**, with the radius, closed form and the 38-digit pinned
`h·D(ũ₀)` recorded in its place; and registry row **KC22** in
`ck-dk-canonical-registry.md` — its exact non-holonomicity, 2-adic grading and
Lean anchors are kept verbatim, while "super-exponentially divergent (q-Gevrey,
radius → 0; the `≈0.143` ratio is the `(k!)^C` shadow, not a radius)" and the
"⇒ transcendental/**resurgent** (Écalle acceleration class)" inference are
struck. The `≈0.143` ratio was the radius all along.
