# The RSZ route to C1's ∞ Stokes data is CLOSED — a mis-citation, not a failed computation

**Date:** 2026-08-08 · **Axis:** C1 ∞-residual (W2 `qou-xufp`; D-ladder `qou-dri7`,
`qou-b00b`) · **Tier:** literature verification + two proved prunes. **No fit,
nothing wired, no Stokes multiplier computed, no `symbol=C1` claim.**

Supersedes the framing (not the computations) of
[`2026-08-01-c1-inf-slope-half-rsz-stokes.md`](2026-08-01-c1-inf-slope-half-rsz-stokes.md)
and the RSZ-dependent parts of
[`2026-08-08-w2-stokes-qborel-attack-plan.md`](2026-08-08-w2-stokes-qborel-attack-plan.md).

## The chain that stood since 2026-08-01

> C1 has slope ½ ⇒ RSZ level `d = 2` ⇒ q-Borel `B_{q,2}` ⇒ `F(P₁,P₂) ≅ ℂ²`
> ⇒ **two Stokes multipliers `U ∈ ℂ²`**

It drove a staged work plan. Every *number* in it is right. The **reading** is not.

## What RSZ actually says

Read from `library/arxiv-0903.0853v3/0903.0853v3.pdf` (no `pdftotext` in this sandbox; text pulled
directly from the FlateDecode streams).

**1. §3.3 is restricted to integral slopes — by its title.**

> *"3.3. Explicit description of `F(P₁,…,P_k)` **in the case of integral slopes**"*

C1's slope is `½`. Not integral. The section does not apply.

**2. The "level `d`" is the slope DIFFERENCE, not a denominator.** RSZ p.38,
deriving the very recurrence the corpus formalized:

> *"…where we denoted `d := μ₂ − μ₁ ∈ ℕ` the **level** of the above inhomogeneous
> equation."*

It is a natural number *precisely because* §3.3 assumes integral slopes. The
08-01 reading — "slope ½ ⇒ level = denominator = 2" — **inverts the meaning of the
central parameter**. There is no level without two slopes.

**3. `P₁,…,P_k` are graded pieces of the slope filtration, one per DISTINCT
slope.** RSZ p.21, Def. 2.3.1 setup:

> *"…a pure module `M₀ := P₁ ⊕ ⋯ ⊕ P_k`. Here, each `Pᵢ` is pure isoclinic of
> slope `μᵢ ∈ ℚ` and rank `rᵢ ∈ ℕ` and we assume that `μ₁ < ⋯ < μ_k`."*

**4. The dimension count confirms `k = 1` is trivial.** Thm 3.3.5:
`dim F(P₁,…,P_k) = Σ_{i<j} rᵢrⱼ(μⱼ − μᵢ)`. At `k = 1` the sum is empty:
**dimension 0**. A pure isoclinic module has no isoformal moduli, hence no local
Stokes data.

## C1 has one slope at ∞ — computed, not recalled

From the operator `L1 = (q²x−1)σ² − (q−1)σ − (q−1)`: `deg_x a_i = {2:1, 1:0, 0:0}`,
so Newton points `(0,1), (1,1), (2,0)` and a **single edge** `(2,0)→(0,1)`, slope
`½`. Independently reproduces the edge the 08-01 audit records. Edge height at
`i=1` is `½` — not a lattice point — so `i=1` lies strictly above and drops out.

Hence `k = 1`, and by (3)+(4) there is nothing for `F(P₁,P₂)` to classify.

## Bugeaud [14] does not rescue it

RSZ names the non-integral generalisation:

> *"A generalisation of Birkhoff–Guenther normal form to the case of **arbitrary
> slopes** has recently been obtained by Virginie Bugeaud [14]."*

Obtained (owner upload, commit `733a88b8`) and registered as `bugeaud2011`:
*Classification analytique et théorie de Galois locales des modules aux
q-différences à pentes non entières*, CRAS **349** (2011) 1037–1039,
[doi:10.1016/j.crma.2011.09.002](https://doi.org/10.1016/j.crma.2011.09.002)
(identity metadata-verified; the body is a font-subset encoding that does not
extract, but `/Title`, `/Author` and `dc:description` are plain).

Its section bookmarks:

```
1 Introduction
2 Classification analytique isoformelle à DEUX PENTES
3 Opérateurs de Stokes
4 Groupe de Galois formel
```

**§2 is "…à deux pentes".** So the non-integral generalisation is *still a
two-slope theory*. Bugeaud lifts the **integrality** restriction, not the
**two-slope** requirement. No version of the apparatus supplies Stokes data at a
point where the module is pure isoclinic.

## Verdict

**The RSZ route to C1's ∞ Stokes data is closed.** This is a **mis-citation, not a
mathematical refutation**: C1's ∞ residual may well be genuinely wild and
interesting. What is wrong is the mapping onto §3.3 — a section explicitly about
integral slopes, whose central parameter was read with the opposite meaning, and
whose object requires a filtration C1 does not have at that point.

Scope-(a) throughout. Nothing is marked "refuted" about the physics.

## Two further findings from the same investigation

**A third singular site, never inventoried** (`qou-qbe9x`). The leading coefficient
`a₂ = q²x − 1` vanishes at `x = q⁻²` — inside `ℂ*`, neither `0` nor `∞`. On
`E_q = ℂ*/q^ℤ` that is the class `[q⁻²] = [1]`, the identity orbit. It is
**genuine, not removable**: the companion matrix has
`det A = −(q−1)/(q²x−1)`, so `deg div(det A)|_{ℂ*} = −1`, while gauge changes
`det A` by `σg/g` whose divisor has degree `0` always. A gauge-invariant `−1 ≠ 0`
means no normalisation clears the singularity out of `ℂ*`.

So the geometry is `E_q` with the two ends **plus** the identity orbit — and under
the actual symmetry (the dilation `x ↦ qx`, not `PGL₂`) that triple is
*(fixed point, identity orbit, fixed point)*: canonical, not chosen.

**The `ℙ¹∖{0,1,∞}` lead, pruned** (`qou-qbf0`). Tempting, since the corpus's only
`{0,1,∞}` is Goncharov's motivic groupoid. It fails two independent tests:

| test | result |
|---|---|
| local types | KZ is regular-singular at all three points; C1 is **irregular** (slope ½) at `∞` |
| classical limit | `a₁ = a₀ = −(q−1) → 0` while `a₂ → x−1 ≠ 0`, so `L1 → (x−1)σ²` — **not rank 2**. Rescaling diverges as `2/ε` |

Also note: Bring's spacetime `ℙ¹` has **six** branch points in three conjugate
pairs, not three marked points — so the C1 triple never aligned with it either.

## What SURVIVES, and is worth keeping

Independent of RSZ's framing, because computed from the operator or proved outright:

| result | where |
|---|---|
| `deg_q(cₙ) = n²` for all `n`, + bridge to `c1FormalDeg` | `QOU/QBeta/C1InfDegreeLaw.lean` |
| level-`d` q-Borel kernel, recurrence + degree law, level 1 ≡ existing kernel | `QOU/MathlibExt/QBorelKernelLevel.lean` |
| `√(q−1)` non-removable (degree parity) | `QOU/QBeta/C1NewtonRamification.lean` |
| typed RSZ interface — `rszLevel` binary, `dim = 0` at `k=1`, `¬IntegralSlopeSetting 1` | `QOU/MathlibExt/RSZIsoformalInterface.lean` |

All sorry-free, `lean`-direct exit 0, axioms `[propext, Classical.choice, Quot.sound]`
with no `sorryAx`.

The typed interface is the durable lesson: **prose citations do not typecheck.**
Had `rszLevel` been a binary operation and `IntegralSlopeSetting` carried its
`k ≥ 2` hypothesis as a field, the 08-01 chain would have failed to elaborate
rather than standing for a week.

## Where the work goes instead

**Alien calculus** — and not as a new idea: it is already the corpus's route
(`OneInstantonNormalization.lean`, PR #4246; assessment
[`2026-08-01-uq0-map-resurgence-surreal-tool-assessment.md`](2026-08-01-uq0-map-resurgence-surreal-tool-assessment.md) §2),
structurally done and quantitatively open.

The reason it is *right* is the reason RSZ was wrong: `F(P₁,…,P_k)` is built on the
slope filtration and needs `k ≥ 2`. **Alien derivations need no filtration** — they
act on the resurgent function and read Borel-plane singularities directly, which is
the natural home for exactly the irregular, q-Gevrey-divergent object that
`deg_q(cₙ) = n²` certifies C1 to be.

Caveat: classical alien calculus is well developed, the q-analogue less so, and the
classical-limit test above shows C1 **cannot** be confluenced to the classical
setting and handed to Écalle there. Whatever is used must be q-native.

-- Ref: [ramis-sauloy-zhang2013] https://arxiv.org/abs/0903.0853 (§3.3, Thm 3.3.5, p.21, p.38)
-- Ref: [bugeaud2011] https://doi.org/10.1016/j.crma.2011.09.002
-- Ref: [manuscript] docs/audits/2026-08-01-c1-inf-slope-half-rsz-stokes.md
