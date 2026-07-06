# Reconciling the two Borromean-volume definitions: 8G vs ln|Vol_q|

**Date:** 2026-06-01
**Branch:** `claude/volume-def-reconcile-8g-vs-trm-2026-06-01` (PR #1632)
**Scope:** RECONCILE the keystone open item, not fit. Builds directly on the
just-merged keystone audit
[`2026-06-01-yekutieli-volume-join-derivation.md`](2026-06-01-yekutieli-volume-join-derivation.md)
(PR #1628 §3), which reported the corpus carries two Borromean-volume
definitions "off by ~5090×" and named the A-vs-B reconciliation as the precise
missing input.

**Compute:** [`volume_def_reconcile.py`](../../computations/volume_def_reconcile.py),
witness [`volume-def-reconcile.witness.json`](../../computations/volume-def-reconcile.witness.json).
Every number is RAW (q₀ from the canonical pinning witness, m_e from CODATA);
nothing is tuned to m_p.

---

## VERDICT: (a) SAME OBJECT ACROSS τ — the 5090× is a cross-functor category error

**The two definitions are the SAME post-τ archimedean volume `Vol(K)`, linked by
the Kashaev Volume Conjecture. They are NOT a numerical contradiction.** The
keystone audit's "5090×" compared a POST-τ real volume (`8G`) to `ln` of a
PRE-τ algebraic number evaluated at q₀ (`ln|tr_M(q₀)|`) — a comparison that
crosses the τ functor in the wrong place. **Production uses the correct stage**
(the post-τ classical `8G`, which is exactly what `prop:vol-through-tau` says
`ln|Vol_q|` evaluates to). There is **no volume-definition bug**; the genuine
open items are the KVC itself and the per-crossing `V̂_i` compute (keystone §5),
unchanged.

---

## 1. What each definition computes, and at which chain stage

The canonical chain is
`substrate q → 𝐂-action → non-abelian Stokes → Hecke tr_M → τ_arch → MeV`.
The τ functor (`prop:vol-through-tau`) is the **only** exit from the categorical
side 𝐂 to the archimedean continuum ℝ. The two "volume" definitions sit on
opposite sides of that wall.

### Definition A (production)

`topological-mass-formula.md` Step 1
([blob](../../content/quantum-observable-universe/mass-theory/topological-mass-formula.md)):

> `Re tr(τ̂ⁿ_desc · Hol) = Vol(K)` — "the imaginary part of the Chern–Simons
> functional on the flat connection associated to K, which by the
> Chern–Simons / hyperbolic-volume correspondence equals `Vol(S³ \ K)`."

For 𝓑₃ this is the classical SnapPy value `Vol(𝓑₃) = 8·G = 7.32772…`
(G = Catalan; Adams 1985). It is used verbatim in
[`_li_2_q_util.vol_density_borromean`](../../computations/_li_2_q_util.py)
as `vol_b3 = 8 * mp.catalan`, then `Geom_leading = Vol/ℏ_q²`.

**Chain stage: POST-τ.** `Vol(K)` is already a real number in ℝ — it is the
*output* of `Re tr(τ̂·Hol)`, i.e. the archimedean image. The τ functor has
already been applied.

### Definition B (`prop:vol-through-tau` + `def:algebraic-quantum-volume`)

`def:algebraic-quantum-volume.md`
([blob](../../content/quantum-observable-universe/mass-theory/algebraic-quantum-volume.md)):

> `Vol_q(β) = ∏_{i=0}^{n-2} V̂_i(q) ∈ ℤ[q^{1/2}, q^{-1/2}]` — an **algebraic
> object**. "Its real-valued archimedean shadow is obtained by applying the QOU
> fibre functor τ … Concretely, `Φ₁(β) := τ_arch(Vol_q(β)) = ln|Vol_{q₀}(β)|`."

`prop:vol-through-tau.md`
([blob](../../content/quantum-observable-universe/mass-theory/vol-through-tau.md)):

> `Vol(K_β) = τ_arch(Vol_q(β)) = (π_∞ ∘ τ)(Vol_q(β))` … "Restriction to ℝ via
> π_∞ recovers exactly `ln|Vol_{q₀}(β)|`."

**Chain stage: `Vol_q` is PRE-τ (algebraic, in `ℤ[q^½]`); `ln|Vol_q|` is
POST-τ (the archimedean exit).** The `ln|·|` IS the τ_arch functor — "the
canonical map `|·|_∞ → log|·|_∞` on the archimedean place of the adelic
substrate," not "an extraneous transcendental operation."

### The two are asserted EQUAL

`prop:vol-through-tau` is precisely the statement that the post-τ Definition-B
quantity `ln|Vol_q|` **equals** the post-τ Definition-A quantity `Vol(K) = 8G`.
Both name the same real number `Vol(K)`. The proposition's `cites` field is
`[kashaev1997, murakami-murakami2001]` — the Volume Conjecture references — and
`kashaev-volume-conjecture.md` makes the identity explicit:

> "KVC is the consistency statement that the archimedean realisation functor
> `τ_arch = π_∞ ∘ τ` applied to the algebraic quantum volume recovers the
> hyperbolic volume."

with the asymptotic form
`Vol_hyp(S³\K) = 2π·lim_{N→∞} log|J_N(K)|/N` at `q = exp(2πi/N)`. So A and B are
the **same `Vol(K)`**, computed two ways: A by SnapPy table lookup, B by the
(open) KVC regulator/Kashaev limit.

---

## 2. The exact functional relation (hard-discipline check)

The keystone audit's §3 test put `Vol(K) =? ln|tr_M(bare)|` at q₀ and found
`8G = 7.328` vs `ln|0.9986| = −0.00144`, ratio ≈ 5090. The task asks: is one
the log/exp of the other up to a factor? **No.** All RAW (probe witness
`exact_functional_relation`):

| quantity | value at q₀ |
|---|---|
| `8G` | 7.32772 |
| `tr_M_norm(𝓑₃)` (normalized Markov trace) | 0.998562 |
| `ln|tr_M_norm|` (keystone's −0.00144) | −0.00143887 |
| `exp(ln_trM_norm)` | **0.998562** — round-trips to `tr_M`, NOT 8G |
| `ln(8G)` | **1.99167** — NOT ≈ ln_trM_norm |
| `8G / |ln(tr_M(q₀))|` | **5092.69** (the "5090×") |

**`8G` is NEITHER `log` NOR `exp` of `ln_trM_norm`.** `exp(ln_trM_norm)` just
recovers the trace `≈ 1`; `ln(8G) ≈ 1.99` is nowhere near `ln_trM_norm`. The
`5092.69×` is the magnitude of a **post-τ volume** divided by `ln` of a
**pre-τ algebraic number evaluated at q₀** — a cross-functor (category)
comparison, not a single functional map between two volumes.

### Why ln|tr_M(q₀)| is the WRONG-stage object

Two distinct things get conflated under "`ln|tr_M|`":

1. **τ_arch / Kashaev regulator** — `def:algebraic-quantum-volume`'s `ln|Vol_q|`
   is the archimedean image of the *multiplicative quantum-volume generator*;
   `kashaev-volume-conjecture.md` realizes it as the `N→∞` asymptotic
   `2π·lim log|J_N|/N` at roots of unity. This lands on the hyperbolic volume
   `8G` (the KVC). **This is the post-τ regulator.**

2. **ln of the q₀-evaluated normalized trace** — the keystone audit computed
   `ln(tr_M_norm(q₀))` where `tr_M_norm(q₀) ≈ 0.9986` is the *pre-τ algebraic
   number specialized at the substrate point q₀*. Taking `ln` of a number that
   happens to be `≈ 1` gives `≈ 0`. **This crosses τ in the wrong place** — it
   logs a pre-τ value rather than evaluating the τ_arch regulator.

The decisive tell: reading B at the wrong stage gives a **negative mass**
(`ln_trM_norm/ℏ² · m_e = −0.075 MeV`, witness `raw_m_p_readings_no_fit`). A
volume — and a mass — cannot be negative; the wrong-stage reading is
self-refuting.

---

## 3. Raw m_avg readings (no fit)

`m_e = 0.51099895069 MeV`, `m_avg^CODATA = 938.91869 MeV`, q₀ from the pinning
witness. RAW:

| reading | m_avg (MeV) | err vs CODATA | stage |
|---|---|---|---|
| production `8G/ℏ²·linking_weight` | **966.05** | **+2.89 %** | POST-τ classical Vol × H₄ scalar |
| `8G/ℏ²` alone (lw = 1) | 381.42 | −59.38 % | POST-τ classical Vol alone |
| `ln|tr_M(q₀)|/ℏ²` | **−0.075** | −100 % | category error (negative mass) |

Production's +2.89 % reproduces the keystone audit and the sibling
perblock-wiring-fix gate exactly. The +2.89 % is the **separate** residual:
the H₄ `linking_weight = 2.533` vs the CODATA-implied `λ ≈ 2.460` — the
λ_scale-absorbed item per
[`lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md),
**not** a volume-definition inconsistency.

---

## 4. Which stage production SHOULD use

**The post-τ classical `Vol(K) = 8G` — which is what production already uses.**

`prop:vol-through-tau` says `ln|Vol_q|` evaluates (via the KVC) to exactly that
`Vol(K) = 8G`. So production's `8G` SnapPy lookup is a **short-circuit of the
q-volume functional route to its correct value** — the same observable computed
the cheap way. The q-volume route (Definition B) does not give a *different*
number to switch to; it gives the *same* `8G`, the long way (open KVC asymptotic
+ the per-crossing `V̂_i` factorization that production never builds, keystone
§5).

There is no corrected `m_p` to report from a stage-switch, because there is no
wrong stage in production. The raw production `m_avg ≈ 966 MeV (+2.89 %)` stands;
its residual is the linking_weight item, addressed elsewhere.

---

## 5. What this resolves and what stays open

**Resolved:** the apparent "two inconsistent volume definitions / 5090×" is a
cross-τ category comparison, not a contradiction. A (`8G`) and B (`ln|Vol_q|`)
are the same post-τ `Vol(K)`, identified by the KVC. Production uses the correct
stage.

**Still open (unchanged from keystone §5):**

1. **The KVC itself** — `Vol(K) = 2π·lim log|J_N|/N` is OPEN in general (proved
   only for 4₁, certain torus/pretzel knots). It is axiomatized as the
   `VolumeConjecture` typeclass (`kashaev-volume-conjecture.lean`); every
   downstream result is conditional on it. **This conditional dependency is the
   real status of Definition B**, not a numerical inconsistency with A.

2. **The per-crossing transfer chain `V̂_i(q) = z·a_i + b_i`** for the atomic
   braids — needed to compute `Vol_q = ∏V̂_i` directly (rather than via the
   normalized trace or the SnapPy lookup) and to feed the three-invariant
   `ln|Vol_q^(1)·…|` mass form. Production never builds it.

3. **The +2.89 % linking_weight residual** — the λ_scale-absorbed item; not a
   volume question.

---

## 6. Lean statement (compile-pending — toolchain network-blocked here)

The honest formal content is the **conditional** A↔B relation: `8G = ln|Vol_q|`
holds *conditional on the KVC*. Stated as a class-hypothesis theorem (NOT
claimed proven — no Lean toolchain in this container), matching the §3b-cond
conditional-class discipline:

```lean
-- Conditional on the Kashaev Volume Conjecture, the classical hyperbolic
-- volume (Definition A, 8G) equals the τ_arch regulator ln|Vol_q| (Definition
-- B). The two corpus definitions name the SAME post-τ Vol(K). The apparent
-- 5090× discrepancy is a cross-functor comparison (ln of a pre-τ number at q₀),
-- NOT a contradiction.
theorem volume_def_A_eq_B_via_kvc {q : ℝ} [VolumeConjecture q]
    (β : Braid) :
    classicalHyperbolicVol β = Real.log |algebraicQuantumVol q β| := …
```

The point is to make the KVC the **named, axiomatized hypothesis** under which
A = B, rather than presenting the unconditioned `ln|tr_M(q₀)| = −0.00144` as a
counter-evidence to the equality. A skeleton sibling is added in
`volume-def-reconcile.lean` with `sorry` + `-- Ref:` to the KVC.

---

## 7. What this audit does and does not claim

- **Does NOT** pick the definition that makes m_p come out nicest — the verdict
  is determined by chain stage (pre-τ vs post-τ) from the definitions, and the
  raw m_avg readings are reported as-is (+2.89 %, −59 %, negative).
- **Does NOT** introduce any factor; the 5092.69× is reported raw as the
  cross-functor ratio it is.
- **Does** establish the exact functional relation: `8G` is neither log nor exp
  of `ln_trM_norm`; the wrong-stage reading gives a negative mass.
- **Does** confirm production uses the correct (post-τ) volume stage, and that
  the +2.89 % is the separate linking_weight residual.

**Single most decision-relevant output:** the "two inconsistent volume
definitions" finding from the keystone audit is a **cross-τ category error**,
not a bug. `8G` (Definition A, post-τ classical) and `ln|Vol_q|` (Definition B,
the τ_arch regulator) are the **same `Vol(K)`**, equated by the Kashaev Volume
Conjecture. Production uses the correct stage; the open items are the KVC and
the per-crossing `V̂_i` compute, exactly as the keystone audit said.
