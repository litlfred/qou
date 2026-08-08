# Extended-Bloch tetrahedron term — scoping, and the trefoil trap in the "flattening from the trefoil" plan

**Date:** 2026-08-08
**Branch:** `claude/extended-bloch-tetrahedron-wx3mc4` (PR #4824)
**Beans:** `qou-985x` (extended-Bloch flattening), parent `qou-kemt`; relates `qou-78pt`, `qou-0c19`, `qou-fl4t`, `qou-prjo` (na-Stokes, PR #4798)
**Scope:** this is a **scoping / redirect** note, **not** a claimed closure and **not** a refutation of the extended-Bloch route. It records (a) a trap in the stated plan, (b) what is already computed, (c) exactly what the route adds and the standing constraint on that increment, and (d) the one honestly-open sub-question. Per AGENTS.md §"Before declaring refuted" this stays scope-(a) except where a proved invariant is cited.

## 0. TL;DR

The prior session proposed workplan #1 as *"derive the extended-Bloch flattening from the **trefoil** gluing equations."* Two things narrow that as stated:

1. **Owner ruling (recorded in bean `qou-985x`, 2026-08-07):** *"hyperbolicity of the light-nucleus closures is ASSUMED GRANTED — assume it is there and work from there."* So the objection "the literal deuteron closure is non-hyperbolic" **stands down by owner directive** — do not re-litigate it. What the ruling does **not** dissolve is *which* hyperbolic representative, which is exactly the germ/handle freedom PR #4798 found.
2. Even granting hyperbolicity, the extended-Bloch object's **new** content over the already-landed pure-volume compute (`binding_link_volumes.py`) is exactly the **iCS leg**, and #4591 shows the muon anchor cannot calibrate it (CS-blindness). This constraint survives the owner ruling and is the durable finding here.

So: keep §1 as a *labelling* caution (the word "trefoil" points at the literal Vol=0 carrier; the work must proceed on a granted-hyperbolic representative), and treat §3 (CS-blindness) as the load-bearing constraint.

## 1. The "trefoil" label points at a Vol=0 carrier (labelling caution, not a veto)

The owner has ruled to assume hyperbolicity (§0.1), so this section is a *naming* caution, not a route-veto.

Neumann's extended Bloch group gives, for a hyperbolic 3-manifold `M`,

```
R̂(β̂(M)) = Vol(M) + i·CS(M),   β̂(M) = Σᵢ [zᵢ; pᵢ, qᵢ]   (flattened ideal tetrahedra)
```

additive over tetrahedra, with the flattening integers `(pᵢ,qᵢ)` **fixed by the gluing/parity equations** (this is the genuine appeal — it kills the branch-of-log freedom that PR #4798 found as an O(100×) germ/handle ambiguity).

But the framework's **deuteron carrier is the trefoil** T(2,3) = 3₁ (deuteron braid = σ₁³; closure = T(2,3); SnapPy Vol = 0; flat shapes {1/2, 2} in `computations/deltalambda/deuteron_octahedral_gluing_probe.py`). The trefoil complement is Seifert-fibred, **non-hyperbolic**, so:

- its ideal triangulation has **degenerate (flat) tetrahedra**, `Im Φ_q → 0`;
- `Vol = 0` identically — the extended-Bloch **volume leg contributes nothing** on the deuteron;
- AGENTS.md §7b (line ~2271) lists exactly *"Bloch-Wigner / dilog-transcendence arguments on the trefoil (non-hyperbolic → D(z)=0)"* as a recurrent re-pitch failure mode.

The honest deuteron probe already respects this: `deuteron_octahedral_gluing_probe.py` does **not** use `Vol`; it uses the surviving `Re Φ_q` phase and the bar-even shape modulus `s(z₀)=z₀+1/z₀` off its flat value. Under the owner's granted-hyperbolicity ruling one instead works from an *assumed* hyperbolic representative — but the volume of the **literal** deuteron carrier is 0, so the deuteron leg either uses the `Re Φ_q` route above or an explicitly-chosen hyperbolic representative (and then owes an account of that choice, per §4).

**The muon anchor 4₁ is a different knot and is genuinely hyperbolic** (Vol = 2Λ(π/3) ≈ 2.0299). "4₁ hyperbolic" ✓ and "deuteron = trefoil, Vol = 0" are both true and must not be conflated.

## 2. What is already computed (do not re-derive)

`computations/binding_link_volumes.py` already carries the A=3 hyperbolic carriers and the parameter-free ratio:

| carrier | link | Vol (SnapPy, verified) |
|---|---|---|
| ³H (T) | 8₁₁ | 8.2863168 |
| ³He | L6a4 = Borromean | 7.3277248 = 8·Catalan |
| ²H (deuteron) | Hopf L2a1 | 0 (Seifert-fibred) |

Parameter-free, zero free parameters, overall constant cancels:

```
Vol(8₁₁) / Vol(L6a4)      = 1.1308
B(³H) / B(³He)  (AME2020) = 1.0990
                            ------ +2.9%  (mirror-pair near-hit)
```

and the **absolute** single-link endomorphism `B = m_e·Vol(K)·Δtr` misses ³H/³He by **−60%** (Δtr ≈ 0.6–0.9 is nearly A-independent while B grows ~13×). This is the corpus's standing honest negative: the volume carries the *ratio* to a few %, not the *A-dependence*. The recommended "compute the A=3 ratio" step is therefore **not open** — it is done.

## 3. What extended-Bloch actually adds — and the standing constraint on it

Over `binding_link_volumes.py` (pure real `Vol`), the extended-Bloch object adds exactly one thing: the **imaginary Chern–Simons leg** `i·CS(M)` (with the flattening canonically fixing its branch). The value proposition of `qou-985x` is that this leg, being canonically pinned, could supply the germ+handle choice PR #4798 left free.

Standing constraint (PR #4591, `claude/tau-mass-complex-volume-2026-08-02`, sharpened negative): **the muon anchor is CS-blind.** `CS(4₁) ≈ 0` (4₁ is amphichiral), so *any* magnitude function `F(Vol, CS)` that reduces to `Vol` at `CS = 0` is equally muon-consistent — "a whole function's freedom." Consequence: an iCS-carrying magnitude introduces a degree of freedom the calibration cannot fix. **This does not refute the route** — it means the increment is currently *uncalibrated*, so wiring a CS-dependent closure to production would fail the three-calibration discipline until an independent CS anchor is found.

## 4. The one honestly-open sub-question (scoped)

Not "derive the deuteron magnitude from the trefoil" (trap, Vol=0), and not "compute the A=3 volume ratio" (done, §2). The surviving open item under `qou-985x` is:

> On the **A≥3 hyperbolic** carriers (8₁₁, L6a4/Borromean), does the extended-Bloch flattening `β̂ = Σ[zᵢ;pᵢ,qᵢ]` — with `(pᵢ,qᵢ)` fixed by the gluing/parity equations — yield the PR #4798 transverse surface-curvature coefficient `c₂` **parameter-free**, i.e. without the germ-normalization + handle-holonomy choices that made `c₂` range 0…897? And is that pinned value compatible with a CS anchor independent of the (CS-blind) muon?

That is a real derivation, on hyperbolic manifolds, with no free parameter if it works — and it is falsifiable (the flattening either pins `c₂` or it does not). It is the correct successor to #4798 and does **not** touch the trefoil.

## 5. Disposition

- No production wiring; no fit; no anchor inverted. Deuteron leg stays on the `Re Φ_q` / bar-even `s(z₀)` route (Vol=0), not a hyperbolic volume.
- `qou-985x` re-scoped to §4 (flattening pins #4798's `c₂` on A≥3 hyperbolic carriers), with the CS-calibration caveat (§3) attached.
- Sibling coordination: #4591 (CS-blindness, the constraining sibling), #4610 (SnapPy volumes), #4798 (the na-Stokes negative this succeeds).
