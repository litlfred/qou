# Δ_λ binding-magnitude: a NON-determinant object (jet-filtration graded dimension)

**Date:** 2026-07-18 · **Axis:** per-isotope binding
`B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` — the **magnitude** wall ·
**Tier:** derivation probe, scope-(a) honest negative + scope-(b) proved escape.
**No fit; nothing wired.** Gate: Δ_λ open-for-all for derivation routes
(owner reversal 2026-07-13).

Probe: [`computations/deltalambda/deltalambda_jet_filtration_magnitude_probe.py`](../../computations/deltalambda/deltalambda_jet_filtration_magnitude_probe.py)
· witness `deltalambda-jet-filtration-magnitude.witness.json` (7 assertions, exit 0).
Lean: [`QOU/MassTheory/JetFiltrationGradedDimEscape.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/JetFiltrationGradedDimEscape.lean)
(sorry-free, `lean`-direct exit 0).

## 0. The wall this attacks, and the family it avoids

The three merged, machine-verified Lean no-gos close the **entire
exchange-determinant-cumulant family**:

- [`IsospinMirrorInvariance.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/IsospinMirrorInvariance.lean)
  — signed-graph strong mirror split = 0 (wrong-mirror; excluded from strong).
- [`SaturationRhoCap.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/SaturationRhoCap.lean)
  — unsigned cumulant `b_A = −ln det(I + m(J−I))` gives `ρ_A = b_A/b_2 ≤ C(A,2)`,
  i.e. `ρ₃ ≤ 3`, `ρ₄ ≤ 6`, **below** the strong targets for all `m`.
- [`B4CumulantBarEven.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/B4CumulantBarEven.lean)
  — the A=4 det is even in `m` ⇒ bar-even symmetrization is a no-op.

The **root cause** of the cap: `−ln det` of an `A×A` exchange matrix is
**sub-extensive** in the mode count — it saturates (`b_A/A → −ln(1−m)`), and
saturation forces `ρ_A ≤ C(A,2)`. Any `−ln det(exchange matrix)` variant
inherits this ceiling. This probe therefore attacks from **outside** the
determinant family entirely.

## 1. The non-determinant object

The QOU principal grading `g_ρ` is **derived** as the Gröbner–Shirshov /
jet-order (Coxeter word-length) filtration on the A-nucleon Hecke module
`H_A(q)` (#3542, [`PrincipalGradingJetOrder.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/PrincipalGradingJetOrder.lean);
`n(λ) = min maj(SYT(λ))` is its bottom degree on `V_λ`, the fake-degree
valuation). The natural **extensive** object attached to that filtration is its
**graded dimension** — the Poincaré polynomial of the `S_A` coinvariant algebra:

```
W_A(q) = Σ_{w ∈ S_A} q^{ℓ(w)} = [A]_q! = ∏_{k=1}^{A} [k]_q,   [k]_q = 1+q+…+q^{k-1}
       = Σ_{λ⊢A} dim(λ)·f^λ(q)       (fake-degree sum; f^λ = graded multiplicity of V_λ)
```

`W_A(q) = Σ_k dim(gr_k)·q^k` is a **graded dimension**, a sum of **positive
q-powers**. It is **not** `−ln det` of any exchange matrix — it is genuinely
outside the Lean-excluded family (probe assertion
`W_A_is_length_gen_func_not_determinant`: `W_A(1)=A!`, `W_3(q)=1+2q+2q²+q³ =
Σ_{w∈S_3}q^{ℓ(w)}`). Magnitude candidate, deuteron-referenced and
parameter-free at the fixed substrate `q₀`:

```
ρ_grad(A) = W_A(q₀) / W_2(q₀).
```

This is the **cross-A extensive lift** of the per-partition `dim²` block-trace
lead (#3542, `deltalambda_binding_block_trace_probe.py`, which reached ~91–101 %
on the single deuteron sum): `Σ_λ dim(λ)² = A!` is exactly `W_A(1)`.

## 2. Does it escape the `C(A,2)` cap? — YES (proved, q-independent)

| A | `ρ_strong(A)` | det cap `C(A,2)` | classical `A!/2!` (q=1) | graded `W_A/W_2` at q₀ |
|---|---------------|------------------|--------------------------|-------------------------|
| 2 | 1 (ref) | 1 | 1 | 1 |
| 3 | **3.813** | 3 | 3 | 3.342 |
| 4 | **13.032** | 6 | 12 | 15.740 |

The graded dimension grows **factorially**, so it is not bounded by the
quadratic `C(A,2)`. The escape is **q-independent** — it holds already at
`q = 1`: `A!/2! = {3, 12}` and `12 > 6 = C(4,2)`. At the substrate `q₀`,
`ρ_grad(4) = 15.74 > 13.03 = ρ_strong(4)`, so this is the **first
non-determinant object that can even reach `ρ_4 = 13.03`** — the value the
determinant provably cannot.

**Scope-(b), proved** ([`JetFiltrationGradedDimEscape.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/JetFiltrationGradedDimEscape.lean)):
for every `q ≥ 1`, `ρ_grad(4) = [3]_q·[4]_q ≥ 12`, with the exact factorisation

```
[3]_q·[4]_q − 12 = (q − 1)(q⁴ + 3q³ + 6q² + 9q + 11)  ≥ 0   on  q ≥ 1,
```

hence `jet_graded_rho4_exceeds_det_cap : 6 < [3]_q·[4]_q` — the graded ρ₄
strictly exceeds the `saturation_rho_cap_four` ceiling of `6`. Escaping the cap
is a **structural advance**, not a numerical near-match: the two Lean theorems
together read `det-route ρ₄ ≤ 6 < 12 ≤ graded-route ρ₄`.

## 3. Does it land both targets parameter-free? — NO (scope-(a) honest negative)

At the fixed `q₀` the object **undershoots A=3 and overshoots A=4**:

- `ρ_grad(3)(q₀) = 3.342` vs target `3.813` (**−12.3 %**).
- `ρ_grad(4)(q₀) = 15.740` vs target `13.032` (**+20.8 %**).

Two structural obstructions make a single parameter-free `q` impossible:

1. **A=3 exceeds even the classical ceiling.** `ρ_strong(3) = 3.813 > 3 =
   3!/2!` — the *full* classical coinvariant ratio. So A=3 requires `q > 1`
   (at `q₀`, `[3]_{q₀} = 3.34` still undershoots).
2. **The A=3→A=4 step is intrinsically too steep.** The data step is
   `T4/T3 = 3.418`, but the graded step is `[4]_q`, which is `4` at `q = 1`
   and monotone increasing — so `[4]_q ≥ 4 > 3.418` for **all** `q ≥ 1`. The
   graded dimension grows *faster* between A=3 and A=4 than the data.

Consequently, forcing `ρ_grad(3) = 3.813` requires `q ≈ 1.250`, at which
`ρ_grad(4) = 21.99` (**+68.7 %** over target). No single parameter-free `q`
lands both. (This solve is shown only to demonstrate the impossibility — it is
**not** wired; selecting `q` from the ratios would be the forbidden 7th fit.)

## 4. Reading — a two-sided bracket on the true magnitude

```
sub-extensive  −ln det   (ρ_A ≤ C(A,2);  undershoots BOTH targets, capped)
        <   true binding magnitude   <
super-extensive graded dim  W_A(q)  (overshoots the A=3→A=4 growth)
```

The physical binding magnitude lives **strictly between quadratic-capped and
factorial**. This is a genuine narrowing: the determinant fails by being *too
flat*; the coinvariant graded dimension fails by being *too steep*. The correct
object is a **damped** graded dimension — growing faster than `C(A,2)` but
slower than `[A]_q!`.

**Verdict (scope-(a)).** The coinvariant / jet-filtration graded dimension,
**alone**, does not reproduce `{ρ_strong(3), ρ_strong(4)} = {3.81, 13.03}` at a
single parameter-free `q₀`. It is **not excluded as an ingredient**
(permanence principle): a proved graded-dimension factor may combine with a
growth-damping term. What this probe establishes positively — and proves in
Lean — is that a **non-determinant graded-dimension object escapes the
`C(A,2)` cap** that permanently blocks the determinant family, and can reach
`ρ_4 = 13.03`. That is the first structural handle on the magnitude from
outside the excluded family. The missing piece is now a specific, bounded
correction: **damp the A=3→A=4 growth step from ≈4.7 toward the observed ≈3.4**,
without falling back below the cap.

## Cross-references

- No-go family: `SaturationRhoCap.lean`, `B4CumulantBarEven.lean`,
  `IsospinMirrorInvariance.lean`;
  [`docs/audits/2026-07-18-deltalambda-exchange-determinant-family-nogo.md`](2026-07-18-deltalambda-exchange-determinant-family-nogo.md).
- Attack-vector map: [`docs/audits/2026-07-18-deltalambda-attack-vector-map.md`](2026-07-18-deltalambda-attack-vector-map.md).
- Derived sign carrier `g_ρ` = jet-order grading:
  `deltalambda_grho_jet_order_derivation_probe.py`; `PrincipalGradingJetOrder.lean`.
- Per-partition block-trace lead (this object's single-A ancestor):
  `deltalambda_binding_block_trace_probe.py` (#3542).
- Strong-target construction (isospin/Coulomb premise): #3986 / #3990;
  `deltalambda_coulomb_mirror_split_probe.py`; `deltalambda_bareven_b4_magnitude_probe.py`.
