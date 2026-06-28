# W_λ keystone — Identity I needs no hook-length formula (gap re-scoped) + W_λ normalization

**Date:** 2026-06-28
**Bean / keystone:** `s5bb` — geometric `W_λ` ([`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md))
**Compute:** [`computations/substrate/wlambda_identity_i_structure_probe.py`](../../computations/substrate/wlambda_identity_i_structure_probe.py)
**Witness:** [`computations/substrate/wlambda-identity-i-structure-probe.witness.json`](../../computations/substrate/wlambda-identity-i-structure-probe.witness.json)

## Context

The `W_λ` keystone has a `q₀`-free, falsifiable sub-target: any index realizing `W_λ` must
reproduce the heat-kernel defect `144·C(n) = −n(n−1)(2n−13)`
([`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean),
sorry-free). Its **one** carried representation-theoretic input is **Identity I**

```
  M(n) = (1/n!) · Σ_{λ⊢n} (f^λ)² · ( Σ_{c∈λ} h_c² )  =  n(3n−1)/2 ,
```

held in the keystone Lean as a compute-verified `def twoM` (n=2..14). The s5-so3 ledger states:
*"Proving Identity I from the partition squared-hook sum needs SYT-dimension / hook-length
infrastructure not currently in Mathlib — a multi-session infra fill."*

## Finding 1 — Identity I needs no hook-length **formula**; the gap is narrower

Writing `E[g] := (1/n!) Σ_λ (f^λ)² g(λ)` (the Plancherel expectation), Identity I is
`E[Σ_c h_c²] = n(3n−1)/2`. The probe verifies, exactly for n=2..14:

| identity | status | infra needed |
|---|---|---|
| `E[Σ_c content(c)²] = C(n,2)` | ✓ | Jucys–Murphy `Σ Xᵢ²` second moment (RSK + center of `ℂ[Sₙ]`); **no HLF** |
| `E[Σ_c h_c²] − E[Σ_c content(c)²] = n²` | ✓ | elementary arm/leg/content (Plancherel mean of a hook–content combination) |
| `Σ_c h_c = n + Σ_i C(λ_i,2) + Σ_j C(λ'_j,2)` | ✓ (single-diagram, elementary) | none |
| arithmetic `C(n,2) + n² = n(3n−1)/2` | ✓ | `ring`/`omega` |

So Identity I **factors** as

```
  E[Σ h_c²]  =  E[Σ content²]  +  n²  =  C(n,2)  +  n²  =  n(3n−1)/2.
```

The **full hook-length formula** `f^λ = n!/∏ h_c` is *not* required to prove Identity I. The
ledger's "needs HLF" is over-stated: the genuine inputs are (1) RSK `Σ_λ (f^λ)² = n!` (Plancherel
normalization), (2) the content second moment `E[Σ content²] = C(n,2)` (Jucys–Murphy / Kerov), and
(3) the residual `E[Σ h² − Σ content²] = n²` (elementary hook–content combinatorics). This re-scopes
the keystone's Identity-I dependency from research-grade HLF to **content-moment + elementary-hook**
infrastructure.

> **Honest scope (a).** The content second moment `E[Σ content²] = C(n,2)` is itself a real theorem
> (the JM second-moment / Kerov polynomial degree-2 case); "no HLF" does not mean "trivial." But it
> is a **different, smaller** gap than the hook-length formula, and the *reduction* of Identity I to
> it is the new, parameter-free result here.

## Finding 2 — W_λ normalization: `Σ_λ d_q(λ)² ≠ [n]_q!` (the `D²` vs `[n]_q!` question)

With the symmetric quantum dimension `d_q(λ) = [n]_q!/∏[h_c]_q`, the probe finds
`Σ_λ d_q(λ)² ≠ [n]_q!` (n=1..6). So `W_λ = d_q²/[n]_q!` does **not** sum to 1 — exactly the open
normalization question the ledger records (*"#2524 proposes `d_q²/D²` (Σ=1) vs `d_q²/[n]_q!`
(Σ≈0.982)"*). The classical `Σ_λ (f^λ)² = n!` is the `q→1` limit, but the q-deformation is the
total-quantum-dimension `D² = Σ_λ d_q²` normalization, not `[n]_q!`. The witness records the per-λ
`W_λ` cyclotomic denominators (the Habiro habitat) for the colored-Σ(2,3,5)-WRT bridge.

## Finding 3 — q-Askey placement: binding = q-Hermite *moments*, W_λ = its *measure*, and the `𝔙` framing

Probe [`binding_qaskey_product_probe.py`](../../computations/substrate/binding_qaskey_product_probe.py)
(witness [`binding-qaskey-product-probe.witness.json`](../../computations/substrate/binding-qaskey-product-probe.witness.json))
places the binding side in the **q-Askey scheme**.

- **Simple q-Askey product form REFUTED (a).** If the binding generating function
  `Ĝ(z)=Σ S(m) z^m/N(m)` were a closed-form q-Pochhammer product `∏(z qᵃ;q)_∞^{cᵃ}`, each
  `L_m·(1−qᵐ)` would be a Laurent polynomial. It is not — in **both** the symmetric `[m]_q!` and
  the standard q-Askey `(q;q)_m` normalizations, residual cyclotomic factors survive — consistent
  with the not-low-order-q-holonomic result (PR #2899, Stages 3–4).
- **Family map (positive, stands).** The binding period `S(m)=Σ_λ dim_q(λ)` is the **q-Hermite /
  Rogers–Szegő MOMENT** sequence (q=1 → involution numbers = Hermite moments; main's
  `FollowsRogersSzego`/`rsSeq` is the same family). `W_λ = d_q²/D²` is that family's **Plancherel /
  orthogonality MEASURE**. The W_λ arena is the **Hahn–Exton q-Bessel** `E_q(2)` contraction — one
  q-Askey degeneration away. The bridge between moments and measure is the **three-term recurrence /
  orthogonality** (`FollowsRogersSzego`), **not** a product generating function.
- **`𝔙` framing (the unification).** `𝔙(K) = E₀·tr_M((Π_free−1)∘ℳ) ∈ ℂ` is the **complex-volume
  observable** (Neumann–Zagier `𝕍 = Vol + i·CS` analogue; `conj:binding-qbeta-complex-volume`):
  - `Re 𝔙 = 𝔈_bind` — binding, **bar-even / cosh** — *this is the binding q-Hermite moment*;
  - `Im 𝔙 = 𝔔_β` — β-decay Q-value, **bar-odd / sinh** — the `c_k` Habiro element.

  The q-Askey `q = e^η` cosh/sinh grading **is** the `Re/Im = binding/Q_β = Vol/CS` split of `𝔙`.
  So the binding side **describes `Re 𝔙`**; the full `𝔙` is the *complex* q-Hermite/Askey object
  whose real part is the binding moment and imaginary part the Q_β Habiro element — one object,
  two bar-parities. (This is also why the binding `D(m)` factors are real-q `ℤ[q]` while the Q_β
  `c_k` are ζ-fibre/complex: they are `Re` and `Im` of the same `𝔙`.)

## Finding 4 — `ζ₄ = i` is the moderator of `Re 𝔙` (binding) and `Im 𝔙` (Q_β)

Probe [`zeta4_complex_volume_moderator_probe.py`](../../computations/substrate/zeta4_complex_volume_moderator_probe.py)
(witness; **Lean cert** [`QOU/Mass/Zeta4ComplexVolumeModerator.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/Zeta4ComplexVolumeModerator.lean), sorry-free).

The bar involution `q ↔ q⁻¹` only *splits* `𝔙 = Vol + i·CS` into `Re 𝔙 = 𝔈_bind` (bar-even cosh)
and `Im 𝔙 = 𝔔_β` (bar-odd sinh). What *moderates* (couples) them is the `i` of `Vol + i·CS`, i.e.
`ζ₄ = i`:

- **Rotation (smooth).** `cosh(η + iπ/2) = i·sinh η` and `sinh(η + iπ/2) = i·cosh η` (sorry-free
  Lean `cosh_zeta4_rotation` / `sinh_zeta4_rotation`). The `ζ₄` rotation `η ↦ η + iπ/2` sends the
  bar-even (binding) channel to `i ×` the bar-odd (Q_β) channel — exactly `Re 𝔙 ↦ i·Im 𝔙`.
- **Locus (algebraic).** `Φ₄ = q²+1` — the cyclotomic factor **shared** by the binding side (`L₂`
  denominator `2·Φ₄`, PR #2929) and the Q_β `c_k` kernel (`a₁`'s ζ₄ residue) — has root `q = ζ₄ = i`
  (`phi4_root_zeta4`), where the bar-even `[2]_q = q+q⁻¹` **vanishes** (`barEven_zeta4`) and the
  bar-odd `h = q−q⁻¹ → 2i` (`barOdd_zeta4`).

So the `Φ₄` shared between the two sides is **not** a coincidence of common cyclotomy: it is the
algebraic locus of the `i = ζ₄` rotation interchanging the binding (`Re`) and Q_β (`Im`) channels of
the one complex-volume object `𝔙`. This also explains the localisation split flagged earlier (binding
`D(m)` real-q `ℤ[q]` vs Q_β `c_k` ζ-fibre/complex): they are `Re` and `Im` across the `ζ₄` rotation.

> **Scope (a).** Pinned at the *generator* level (cosh ↔ i·sinh; the `Φ₄ = ζ₄` locus). That the
> *full* binding and Q_β observables are exact `ζ₄`-rotates of one another is the stronger,
> value-gated claim — not asserted.

## Consequence for the next step

The Identity-I Lean closure splits into:
1. **`ring`/`omega` arithmetic reduction** `C(n,2) + n² = n(3n−1)/2` — trivial, lands now.
2. **Conditional Identity I (§3b-cond)** on the two named inputs (content second moment; `n²`
   residual) — makes the remaining gap explicit and *narrow*.
3. The content second moment — check Mathlib's RSK / symmetric-group character API; if present, the
   gap may close without the multi-session HLF build the ledger anticipated.
