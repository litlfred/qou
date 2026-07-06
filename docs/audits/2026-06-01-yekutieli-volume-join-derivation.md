# Yekutieli volume-join derivation — does the q-volume functional supply the 2.38× bridge?

**Date:** 2026-06-01
**Branch:** `claude/yekutieli-volume-join-derivation-2026-06-01` (PR #1623)
**Scope:** DERIVE-OR-REFUTE, order by order. No fit, no hard-coded factor,
no tuning to m_p / B_AME. Builds on the four sibling audits of 2026-06-01:
- `2026-06-01-vol-density-compute-vs-paper-audit.md` (PR #1613, order-by-order)
- `2026-06-01-vol-density-perblock-wiring-fix.md` (PR #1614 — merged, the RED 2.38× gate)
- `2026-06-01-qhyperbolic-nonabelian-stokes-wiring.md` (PR #1611, Stokes wiring)
- `2026-06-01-vol-density-derivation-trace.md` (PR #1608, derivation trace)

**Compute:** [`yekutieli_volume_join.py`](../../computations/yekutieli_volume_join.py),
witness [`yekutieli-volume-join.witness.json`](../../computations/yekutieli-volume-join.witness.json).
Every number below is RAW; the chi-caches (`chi-{proton,neutron}-h3*.witness.json`)
and the documented `markov_trace_for_knot` closed form are the only inputs.

---

## VERDICT: (C) GENUINELY-OPEN — with a clean (B) sub-finding

**The q-hyperbolic volume functional, as the framework actually defines it,
does NOT supply the 2.38× as a multiplicative factor at any order — and it
cannot, because the genuine functional is a *logarithm* of `tr_M`, not a
multiple of it. Production's `linking_weight` is neither the q-volume
functional nor the per-block trace; it is an independent H₄ empirical
near-match (the (B) sub-finding). The genuine `Vol_q → τ_arch` route needs
the per-crossing transfer-chain `V̂_i` that production never builds, so the
join cannot be derived as stated — this is (C), and the precise missing
input is named in §5.**

The hypothesis "the 2.38× IS the Archimedean volume evaluation, derivable as
a closed q-form with zero free parameters" is **refuted**: no zero-parameter
q-volume functional of `tr_M` reproduces the production scalar (§4), and the
two volume definitions in the corpus that *could* supply it disagree by
~5000× at q₀ (§3).

---

## 1. The two dimensionless factors — exact in q (confirming/correcting the audit)

Both readings share the bare hyperbolic prefactor `Vol(𝓑₃)/ℏ_q²`. The dispute
is purely between the dimensionless modulation factors. `h = q − q⁻¹`.

| object | exact in q | h-series (leading terms) |
|---|---|---|
| **production** `linking_weight` (H₄, ⊢4) | `(3q²+4+3q⁻²)/4` | `5/2 + (3/4)h²` — **terminates** |
| **paper** `J_proton` with **w_λ literal** (H₃, ⊢3) | `(q¹⁸+q¹¹+q¹⁰−q⁸−q⁷−1)/(4q⁹)` | `3h + (121/16)h³ + …` — leading **h¹** |
| **paper** `J_neutron` with **w_λ literal** | `(q²⁰−q¹⁹+…)/(4q¹¹−4q¹⁰+4q⁹)` | `(5/2)h + (119/16)h³ + …` — leading **h¹** |
| **bare-Borromean** `tr_M` (wenzl norm) | `(4+h²−3h⁴−h⁶)/(h²+4)` | `1 + 0·h² − (3/4)h⁴ − (1/16)h⁶ + …` — leading **1** |

`w_λ = dim_q(λ)²/[k]_q!` is the paper's Stage-2 Wedderburn weight (NOT the
Wenzl-bridge Plancherel `y_λ` that `markov_trace_for_knot` uses for the mass
formula). The two give structurally different objects.

### Order-by-order ratio production / paper

**(a) vs the literal w_λ trace** — the ratio has a **1/h pole**:

| h^k | proton ratio | neutron ratio |
|---|---|---|
| h⁻¹ | **5/6** | **1** |
| h⁰ | 0 | 0 |
| h¹ | −533/288 | −107/40 |
| h³ | 9647/3456 | 16801/3200 |

The literal w_λ trace **vanishes at q = 1** (no constant term), so the ratio
*diverges* as `q → 1`. This is a **stronger** statement than the sibling
audit's "ratio 4 at h²": with the paper's *literal* w_λ weights the two
objects are not even the same order in h.

**(b) vs the bare-Borromean tr_M (wenzl, leading 1)** — finite but
NON-constant:

| h^k | ratio production / bare tr_M |
|---|---|
| h⁰ | **5/2** |
| h² | **3/4** |
| h⁴ | **15/8** |
| h⁶ | **23/32** |
| h⁸ | **181/128** |

**Confirming + correcting the audit's `4 / (5/2) / divergent` finding.** The
audit's "5/2 at h⁰, 4 at h², divergent at h⁴" was computed in the **Jones**
normalisation (`Jones/(√q+√q⁻¹)²`, h² = 3/16, so production/Jones = 0.75/0.1875
= 4). In the **wenzl** normalisation that the mass formula actually uses, the
order-by-order ratio is `5/2, 3/4, 15/8, 23/32, …` — every coefficient finite
and DIFFERENT. **Both conventions agree on the structural conclusion: the
ratio is a genuine q-function with a different value at every order, so NO
constant factor (4, 5/2, or 2.38) reconciles the two objects.** The "divergent
at h⁴" in the audit's Jones convention corresponds to the wenzl ratio simply
continuing to change (15/8, 23/32, …) — production terminates at h², the trace
does not, so their ratio can never be constant.

---

## 2. What the genuine q-volume functional IS (the framework's own definition)

Three corpus blocks define the q-volume route precisely:

1. **`def:algebraic-quantum-volume`** ([algebraic-quantum-volume.md](../../content/quantum-observable-universe/mass-theory/algebraic-quantum-volume.md)):
   `Vol_q(β) = ∏_{i=0}^{n-2} V̂_i(q) ∈ ℤ[q^{1/2}, q^{-1/2}]`, where
   `V̂_i(q) = z·a_i + b_i` is the traced volume of generator `σ_i`.

2. **`thm:markov-trace-product`** ([markov-trace-product.md](../../content/quantum-observable-universe/mass-theory/markov-trace-product.md)):
   `tr_M(ρ(β)) = ∏_{i=0}^{n-2} V̂_i(q)` — i.e. **`Vol_q(β) = tr_M(ρ(β))`.**
   The algebraic quantum volume and the Markov trace are the *same object*.

3. **`prop:vol-through-tau`** ([vol-through-tau.md](../../content/quantum-observable-universe/mass-theory/vol-through-tau.md)):
   the classical volume is the Archimedean image of `Vol_q`:
   `Vol(K_β) = τ_arch(Vol_q(β)) = ln|Vol_q(β)|` at q₀
   (`Φ₁(β) = ln|Vol_{q₀}(β)|` per `def:algebraic-quantum-volume`).

So the genuine derivation chain is:

```
Vol_q(β) = tr_M(ρ(β))        (algebraic, in ℤ[q^½,q^-½])
         ↓ τ_arch = ln|·| at q₀          (the ONLY archimedean exit)
Vol(K)  = ln|tr_M(β)|·(scale)
         ↓ Stage 3
m(K)    = m_e · Vol(K)/ℏ_q²
```

**The Archimedean functor `τ_arch` is a LOGARITHM, not a multiplicative
factor.** This is the decisive structural fact: a "2.38× multiplicative
bridge" is the wrong *shape* for the q-volume functional, whatever its value.

---

## 3. Structural refutation — classical Vol(K) ≠ τ_arch(Vol_q) at q₀

`prop:vol-through-tau` claims `Vol(K) = ln|tr_M(β)|`. Test it on the bare
Borromean at q₀ (RAW, witness `structural_vol_vs_log_trM`):

| quantity | value at q₀ |
|---|---|
| classical SnapPy `Vol(𝓑₃) = 8·Catalan` (what production uses) | **7.32772** |
| bare-Borromean `tr_M(q₀)` | 0.998562 |
| `ln|tr_M(bare)|` (what `prop:vol-through-tau` says Vol should be) | **−0.0014389** |

**These disagree by a factor of ~5090** (and even differ in sign-of-deviation:
`8G` is large and positive, `ln|tr_M|` is tiny and negative). The framework
carries **two inconsistent volume definitions**:

- **Definition A** (`topological-mass-formula` Step 1 + production):
  `Vol(K)` = classical hyperbolic volume via the Chern–Simons/volume
  correspondence = `8G` (SnapPy table lookup, Adams 1985).
- **Definition B** (`def:algebraic-quantum-volume`, `prop:vol-through-tau`):
  `Vol(K) = ln|Vol_q(β)| = ln|tr_M(β)|`.

Production uses **A**. The q-volume *functional* the task asks about is **B**.
They are not the same number, not even close. So the 2.38× cannot be "the
q-volume functional reconciling A's `8G·linking_weight` with B's `tr_M`" —
A and B are not connected by any zero-parameter map (their *volumes* alone
differ by 5090×).

---

## 4. The join test — no zero-parameter q-volume functional reproduces 2.38×

Production dimensionless scalar `linking_weight(q₀) = 2.53278`;
`tr_M(proton) = 1.06531`; ratio = **2.37751** (this reproduces the sibling
perblock-wiring-fix doc's 2.38× exactly). Test every natural zero-parameter
functional of `tr_M` (witness `qvolume_join.candidates`):

| candidate q-volume functional of tr_M | value | rel. err vs production scalar |
|---|---|---|
| `tr_M` itself | 1.0653 | **−57.9 %** |
| `tr_M²` | 1.1349 | −55.2 % |
| `ln|tr_M|` | 0.06326 | −97.5 % |
| `tr_M/ℏ_q²` | 108.51 | +4184 % |
| `1 + ln|tr_M|/ℏ_q²` | 7.4440 | +194 % |

**None comes within 55 % of the production scalar**, and the closest (`tr_M²`)
has no structural justification. Matching it would require tuning a free
parameter — which is the exact fit-trap the task forbids. **There is no
zero-parameter q-volume functional that turns `tr_M = 1.0653` into the
production `2.53278` at q₀, let alone at all orders.**

(The 2.38× is `linking_weight/tr_M`, a ratio of two genuinely different
q-functions per §1; it is q-dependent and order-dependent, but it is the
*ratio of the wrong object to the right object*, not a derivable functional.)

---

## 5. (C): the precise missing input

The q-volume route (Definition B) is genuinely available in the paper but
un-wired, and closing it needs inputs the repo lacks:

1. **The per-crossing transfer chain `V̂_i(q) = z·a_i + b_i`** for the proton
   and neutron *atomic* braids. `thm:markov-trace-product` gives the product
   `∏ V̂_i = tr_M`, but the **individual** `V̂_i` (the per-generator factors)
   are what enter `Φ₂, Φ₃` (sym×alt, sym/alt) in the three-invariant mass
   formula `M = M_free + α·ln|Vol_q^(1)·(Vol_q^(2))^{−2[3]_q}·(Vol_q^(3))^{H_A²}|`.
   Production never computes the per-generator factorisation — it short-circuits
   to the classical `8G` and the H₄ scalar. **Missing: a compute that builds the
   per-crossing `V̂_i` for the atomic braids and evaluates the three-invariant
   `ln|·|` form** (which is the `descartes-universe`/archimedean side of the
   wall, not the `Vol/ℏ_q² × scalar` shortcut).

2. **The reconciliation of Definition A vs Definition B.** `topological-mass-
   formula` Step 1 asserts `Re tr(τ̂_n^desc · Hol) = Vol(K)` (the CS/volume
   correspondence → `8G`), while `prop:vol-through-tau` asserts
   `Vol(K) = ln|tr_M|`. These give 7.328 vs −0.00144. **Until the corpus
   resolves which `Vol(K)` the mass formula consumes, the q-volume route is
   not even self-consistent.** This is the load-bearing assertion the
   qhyperbolic-stokes-wiring audit (PR #1611 §4 step 3) flagged as "needs the
   Volume Conjecture (open) or a categorical Stokes evaluation the repo does
   not have."

3. **The non-abelian Stokes surface→boundary map**, still
   `braidSurfaceMultTrace z n := z^n` in Lean (`NonAbelianStokes.lean:192`).
   Provable steps 1–2 of PR #1611 (boundary holonomy = Hoefsmit ordered
   product; q-Reeb phase = `V_(2,1)` eigenphase) would ground `Vol_q = tr_M`
   rigorously, but the `ln|·|` archimedean evaluation and the A-vs-B
   reconciliation remain.

---

## 6. The (B) sub-finding — production uses the wrong object

Independently of (C): production's `linking_weight = (1/4)Σ_{λ⊢4} dim_q V_λ`
is an **H₄ (partitions of 4) quantum-dimension average**, applied to the
**H₃ (3-strand)** Borromean braid. It is not the q-volume functional of
`tr_M` (§4), not the per-block H₃ trace (§1), and not `ln|tr_M|` (§3). Per
`lambda-scale-substrate-form.md` it is an acknowledged **CAL-4 empirical
near-match** that lands near the CODATA-implied `λ ≈ 2.46` coincidentally.

**Raw m_p readings (no fit), m_e = 0.51099895 MeV, m_avg^CODATA = 938.919 MeV:**

| reading | m_avg (MeV) | err vs CODATA |
|---|---|---|
| production `8G/ℏ²·linking_weight` | **966.05** | **+2.89 %** |
| `8G/ℏ²·tr_M(proton)` (bare per-block restore) | 406.33 | −56.72 % |
| `8G/ℏ²` alone (linking_weight = 1) | 381.42 | −59.38 % |

The corrected raw m_p from restoring the literal per-block / q-volume reading
is **406 MeV (−56.7 %)** — far worse than production's +2.89 %. This
**reproduces and confirms** the sibling perblock-wiring-fix gate (RED) and the
compute-vs-paper FINDING-1 ("restore makes it ~20× worse"). So switching
production to the literal per-block object is ruled out; the +2.89 % is the
`linking_weight = 2.533` vs CODATA-implied `λ ≈ 2.460` residual, exactly as
`lambda-scale-absorbed-into-vol-density.md` records.

---

## 7. Why this is NOT verdict (A)

(A) would require the q-volume functional applied to `tr_M` to reproduce
production at all orders with zero free parameters. It fails three ways:

1. **Wrong shape.** The genuine `τ_arch` is `ln|·|`, not `×`. A multiplicative
   2.38× is not a logarithm of anything natural (§2–3).
2. **No zero-parameter functional matches even at q₀.** Closest is 55 % off
   (§4). Forcing a match needs a tuned parameter = fit-trap.
3. **The two volume definitions in the corpus disagree by 5090×** at q₀ (§3),
   so there is no consistent `Vol(K)` for the functional to land on.

A single-order coincidence (the audit's `(3/16)·4 = 3/4` h²-match) is exactly
the `mpmath.identify` fit-trap the task warns against; it does not survive to
h⁰ (5/2 vs 4) or h⁴ (production terminates).

---

## 8. Lean statement (compile-pending — toolchain network-blocked here)

No (A) closed q-form to formalise. The honest formal content is a **negative /
conditional** statement: the q-volume route is conditional on a single
class-axiomatised reconciliation of Definitions A and B. The compile-pending
statement (NOT claimed proven — no Lean toolchain in this container) would be:

```lean
-- conditional on the (currently asserted, A-vs-B-inconsistent) volume class
class QVolumeReconciliation (R : Type*) [Field R] where
  /-- The classical CS/volume Vol(K) and the archimedean ln|Vol_q(β)|
      agree (currently FALSE numerically at q₀: 7.328 vs −0.00144). -/
  cs_vol_eq_log_qvol : ∀ β, classicalVol β = Real.log |algebraicQVol β|

-- Then, and only then, the q-volume mass route is well-defined:
theorem qvolume_mass_route_wellposed
    [QVolumeReconciliation ℝ] (β : AtomicBraid) :
    massQVolRoute β = m_e * (classicalVol β) / hbar_q ^ 2 := …
```

The point of the Lean statement is to make the A-vs-B reconciliation an
**explicit, named hypothesis** rather than a silent `:= True` stub — matching
the §3b-cond conditional-class discipline. It is NOT a derivation of the
2.38×.

---

## 9. What this audit does and does not claim

- **Does NOT** introduce any factor to force a match (no fit; the 2.38× is
  reported as the raw `linking_weight/tr_M` ratio, q-dependent, order-dependent).
- **Does NOT** re-open "derive λ_scale" — per
  `lambda-scale-absorbed-into-vol-density.md` the residual is the categorical-
  exactness refinement of `VolDensity(𝓑₃)`.
- **Does** confirm the sibling 2.38× gate (RED) and the −56.7 % per-block m_p,
  independently, with exact-in-q symbolic objects.
- **Does** add one structural finding beyond the corpus: the framework's own
  `prop:vol-through-tau` definition of `Vol(K) = ln|tr_M|` is **numerically
  inconsistent** with the `Vol(K) = 8G` that production uses (5090× at q₀) —
  this A-vs-B inconsistency is the precise reason the q-volume route cannot be
  wired as a multiplicative bridge, and is the named missing input for (C).

**Single most decision-relevant output:** the 2.38× is NOT the Archimedean
volume evaluation. The genuine q-volume functional is `ln|tr_M|` (Definition B),
which gives `Vol(𝓑₃) = −0.00144`, not `8G = 7.328` (Definition A, production).
The two are unreconciled in the corpus, so the join is genuinely open (C); the
productive next step is the A-vs-B reconciliation + the per-crossing `V̂_i`
compute (§5), not a multiplicative 2.38× factor.
