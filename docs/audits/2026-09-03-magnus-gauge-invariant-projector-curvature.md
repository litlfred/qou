# The free off-diagonal CAN be fixed by naturality: the gauge-invariant projector curvature (qou-o6ov)

**Date:** 2026-09-03
**Directive (owner):** "is there a gauge-invariant (q-curvature) formulation in which the free off-diagonal [of the germ] is fixed by a naturality condition [that both makes the germ canonical and preserves the seminormal answer]?"
**Scope:** scope-(a); one positive + one clean negative; no MeV, no fit, nothing wired.
**Probe:** [`magnus_gauge_invariant_curvature_probe.py`](../../computations/deltalambda/magnus_gauge_invariant_curvature_probe.py)
**Follows:** #6434 (the germ is underdetermined — diagonal fixed to ±1, off-diagonal free).

## The question

#6434 pinned the germ `A_i = q·∂_qσ_i·σ_i⁻¹` as **underdetermined**: the differentiated-Hecke
relation `{σ,σ'} = h'σ + hσ'` fixes its σ-eigenbasis **diagonal** to `±1` but leaves the
**off-diagonal FREE**, so the germ is representation-specific (seminormal vs R-matrix differ on
genuine blocks — the 6.5% two-row miss of #6432). The owner asked: can a **naturality condition**
fix the free off-diagonal so the germ becomes **canonical / gauge-invariant** — and ideally still
reproduce the seminormal decay object the arc uses?

## The construction — fix the off-diagonal by "function of σ alone"

The only realization-independent way to fill the free off-diagonal is to demand the germ be a
**function of σ alone** (no `∂P` intertwiner terms). That singles out the **spectral projector**:

```
P_i = (σ_i + q⁻¹·I)/[2]_q                    (projector onto σ_i's q-eigenspace, [2]_q = q+q⁻¹)
A_i^P = 2P_i − I = (2σ_i − h)/[2]_q          (the channel-sign operator: +1 on q, −1 on −q⁻¹)
Ω₂^P = Σ_a [A_a^P, A_{a+1}^P] = (4/[2]_q²)·Σ_a [σ_a, σ_{a+1}]
```

`A_i^P` has the **same** constraint-fixed diagonal (`±1`) as the true germ but an off-diagonal
that is **linear in σ**. Crucially `Ω₂^P` is a genuine **element of the Hecke algebra** (a
polynomial in the `σ`'s), unlike the germ (a log-derivative of the *representation matrix*).

**This is the object I retracted a closed form for in #6434 — correctly.** There I checked
whether the *seminormal germ itself* equals `(2σ−h)/[2]_q` and found NO (0.27 off on genuine
blocks). That retraction stands: `A_i^P` is **not** the seminormal germ. What is new here is that
`A_i^P` is nonetheless the **right canonical object** — it is what you get by *fixing* the free
off-diagonal, not by *reading off* the seminormal one.

## Result 1 — it IS gauge-invariant (the decisive contrast with the germ)

Because `Ω₂^P` is an algebra element, its trace is a **character**, realization-independent by
construction. Verified via the Schur–Weyl two-row identity `tr_{(ℂ²)^⊗n}(g) = Σ_k (n−2k+1)·tr_{(n−k,k)}(g)`
(A=2, n=6, exact mpf):

```
Σ_k (n−2k+1)·tr_{(n−k,k)}^{seminormal}(ρ·Ω₂^P) = −263.30852666765
tr_{(ℂ²)^⊗n}^{R-matrix}(ρ·Ω₂^P)              = −263.30852666765     |Δ_rel| = 9.4e-140  ✓
```

**The same test the germ FAILED by 6.5% (#6432), the projector curvature passes to 140 digits.**
That is exactly "gauge-invariant q-curvature": the seminormal per-irrep computation and the
full-tower R-matrix computation agree because `Ω₂^P` is a single algebra element seen in two
gauges.

## Result 2 — but it does NOT preserve the seminormal answer (the "ideally" clause fails)

Per irrep, `tr(ρ·Ω₂^P)` differs from the seminormal-germ `tr(ρ·Ω₂)` at **every** non-trivial
shape:

| λ | b(λ) | dim | tr(ρΩ₂^P) [gauge-inv] | tr(ρΩ₂) [seminormal germ] |
|---|---|---|---|---|
| (6) | 0 | 1 | 0 | 0 |
| (5,1) | 1 | 5 | −40.579 | −51.215 |
| (4,2) | 2 | 9 | −17.415 | −22.620 |
| (4,1,1) | 2 | 10 | −38.782 | −48.436 |
| (3,3) | 3 | 5 | −8.168 | −7.873 |
| (3,2,1) | 3 | 16 | −17.547 | −21.356 |
| (2,2,2) | 4 | 5 | +1.712 | +1.899 |
| (1⁶) | 5 | 1 | 0 | 0 |

So the owner's ideal — a condition that **both** canonicalizes the germ **and** preserves the
seminormal answer — is **not achievable**: canonicalization and the seminormal object are
genuinely different. Fixing the free off-diagonal by naturality *changes* the decay object. This
is the clean negative half, and it is forced: the seminormal germ's off-diagonal is *not* linear
in σ (#6434), so no function-of-σ can reproduce it.

## Result 3 — the gauge-invariant curvature STILL row-decays (the property the arc needs)

The whole point of the arc is that the trace decays with `b(λ) = n − λ_1`. The projector
curvature keeps that:

```
b=0  (6)      |tr|/dim = 0
b=1  (5,1)    |tr|/dim = 8.116     ← peak at b=1, same as the germ (Burau peak)
b=2  (4,1,1)  |tr|/dim = 3.878     (4,2) 1.935
b=3  (3,3)    1.634   (3,2,1) 1.097   (3,1³) 0.419
b=4  (2,2,2)  0.342   (2,2,1,1) 0.517  (2,1⁴) 0.295
b=5  (1⁶)     |tr|/dim = 0
```

Same envelope as the seminormal germ: **exact zero at both endpoints** (b=0 trivial, b=5 sign),
peak at b=1, decaying through the interior.

**And for `Ω₂^P` the exact-zero endpoints are MANIFEST, not argued.** On any 1-dim rep (trivial,
sign) every `σ_a` is a scalar (`q` or `−q⁻¹`), so every `[σ_a,σ_{a+1}] = 0` *identically* ⇒
`Ω₂^P = 0`. The arc needed a trace-orthogonality argument to get the germ's endpoint zero; the
projector curvature makes it a one-line scalar-commutes fact. That is a genuine conceptual
simplification the gauge-invariant object buys.

## Answer

**Yes — the free off-diagonal can be fixed by a naturality condition, and the result is a
gauge-invariant q-curvature that still row-decays.** The canonical choice is the spectral-projector
germ `A_i^P = (2σ_i − h)/[2]_q`, curvature `Ω₂^P = (4/[2]_q²)Σ[σ_a,σ_{a+1}]`. It is a genuine
Hecke-algebra element, hence gauge-invariant (two-row weighted trace = R-matrix tensor trace to
1e-140, where the germ misses by 6.5%), and it preserves the row-decay with manifest exact-zero
endpoints. **What it does NOT do is reproduce the seminormal germ** (every irrep differs) — so the
owner's optional "and preserve the seminormal answer" is impossible: canonicalizing the germ
necessarily changes the object.

## Consequence for the arc — a genuine fork

There are now **two** well-defined decay objects, and they are different:

1. **Seminormal germ** `Ω₂` — the true log-derivative `q·∂σ·σ⁻¹`, the arc's object. Faithful to
   the "germ-commutator = q-curvature" (`prop:germ-commutator-q-curvature`) reading, but
   **gauge-specific** (rep-dependent off-diagonal) and its endpoint-zero needs an argument.
2. **Projector curvature** `Ω₂^P` — the naturality-fixed canonical object. **Gauge-invariant**,
   a genuine algebra element, manifest endpoint-zero, same row-decay envelope — but **not** the
   log-derivative; it discards the germ's genuine off-diagonal content.

If the arc wants a *gauge-invariant* / full-tower statement of the row-decay, `Ω₂^P` is the object
to prove it for (it is an algebra element, so the reduced-Burau exterior-power handle of #6430 and
the Schur–Weyl two-row R-matrix of #6432 both apply to it directly — no germ-naturality caveat).
If it wants the *physical* log-derivative decay, the seminormal `Ω₂` remains the object, gauge and
all.

## Honest limits

- **A=2 (n=6) exact; decay is empirical over the 11 irreps of S_6.** The gauge-invariance (Result
  1) is a **structural** fact (algebra element ⇒ character), general in n; the *decay* (Result 3)
  is measured at n=6, not proved. The endpoint-zero (both ends) *is* structural (scalar σ on
  1-dim reps).
- **One positive, one negative.** Positive: a gauge-invariant curvature exists and row-decays.
  Negative: it is not the seminormal germ, so it does not "preserve the seminormal answer."
- **Nothing wired.** No witness, no production consumer; this resolves a geometric question about
  the germ, it does not change any number.

## Bottom line

The germ's free off-diagonal is fixed canonically by "be a function of σ" → the projector
curvature `Ω₂^P = (4/[2]_q²)Σ[σ_a,σ_{a+1}]`. It is **gauge-invariant** (140-digit two-row/R-matrix
agreement vs the germ's 6.5% miss), a **genuine algebra element**, **row-decays** with **manifest**
exact-zero endpoints — but is a **different object** from the seminormal germ (every irrep
differs). So a naturality condition *can* canonicalize the germ, but *cannot* simultaneously
preserve the seminormal answer; the arc gains a clean gauge-invariant decay object as an
alternative to the rep-specific log-derivative, not a reconciliation of the two.
