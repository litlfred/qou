# The deuteron 2nd-order Magnus term clears the non-negativity wall the quadrature could not

**Date:** 2026-08-29 · **Bean:** `qou-dp32` (Magnus continuation of `qou-jqof`) ·
**PR:** #6047 · **Probe:**
[`deuteron_magnus_omega2_sign_probe.py`](../../computations/deltalambda/deuteron_magnus_omega2_sign_probe.py)
(+ witness) · **Tier:** route-viability decision (necessary, not sufficient) ·
**Scope:** (a); no fit; nothing wired.

## The decision this settles

The deuteron **overbinds by +27% parameter-free**, so the missing ≈0.608 MeV
correction must **reduce** binding: it is **negative at A=2** (positive at A≥3).

The prior probe
[`deuteron_interface_handle_curvature_probe.py`](../../computations/deltalambda/deuteron_interface_handle_curvature_probe.py)
(bean `qou-jqof`) computed the interface germ curvature `F_q = [σ₂, σ₃]` in the
real H₆ seminormal rep and found it **exactly traceless**. A traceless curvature
enters the binding only in **quadrature** `‖F_q‖² ≥ 0`. A square cannot change
sign, so by the same non-negativity argument that governs Faddeev–Niemi energies
the quadrature is **structurally excluded** from being the negative-at-A=2 term.

That left the prior probe's own named open object: *"needs the pairing
`tr_M(ρ_deuteron·dF_q)` (raw trace is 0) + λ-weighting (open)"*. Bean `qou-dp32`
is its Magnus continuation. Both point at one question, settled here:

> Is the **linear** second-order Magnus pairing `tr_M(ρ·Ω₂)` sign-indefinite
> (can it be negative), where the quadrature `‖F_q‖²` structurally could not?

## The object (0-fit, canonical, derived)

| piece | definition |
|---|---|
| germ | `A_g = q·(∂_q σ_g)·σ_g⁻¹` (corpus `germ-commutator-q-curvature`; central finite-diff, validated vs the differentiated Hecke relation `{σ,σ'}=h'σ+hσ'` to 1e-60) |
| 2nd Magnus | `Ω₂ = ½ Σ_{i<j} [A_{gᵢ}, A_{gⱼ}]` over the ordered crossings |
| deuteron word | `β_D = atom_braid_word_3A(1,1)` — **source of truth**: proton `7σ₀,4σ₁` · interface `σ₂` · neutron `7σ₃,4σ₄`, 23 crossings |
| density | `ρ(β_D) = ∏ σ_{gᵢ}` — the literal bare braid-word image (`d·I` dressing is central ⇒ drops from every `[·,·]`) |
| pairing | `P = Σ_λ y_λ · tr(ρ_λ·Ω₂_λ)`, `y_λ = d_q(λ)²/[n]_q!` |

## Result — LIVE (clears the wall)

Real H₆ Hoefsmit seminormal rep, all λ⊢6, at the proton `q₀`, mpmath `mpf`
dps=140:

| observation | value | reading |
|---|---|---|
| **control** `tr_M(Ω₂)` (ρ=I) | `0` exactly | `Ω₂` has no Markov trace, so the quadrature's non-negativity argument provably does **not** transfer to the linear object — the sign requires the density |
| **sign-indefiniteness** | **2 positive, 7 negative** | `(2,2,2) = +93.76`, `(5,1) = −337.95`; a square cannot be both signs |
| `P_total` | `−12882.86` | definite, nonzero |
| `P_interface-only` | `−5794.40` | the σ₂-neighbour part alone is already net negative |

The second-order Magnus term is a **viable carrier** for the sign-changing
missing binding term — the role the traceless-⇒-quadrature `F_q` could not fill.

## Honest scope — what is and is NOT claimed

**Established (a fact about the object's sign structure):** the linear Magnus
pairing escapes the `‖F_q‖²≥0` non-negativity wall — control vanishes, the
per-partition pairing is genuinely sign-indefinite, and the weighted total is a
definite nonzero number.

**NOT claimed:**

- **Not the 0.608 MeV.** The pairing is a dimensionless germ-curvature number;
  converting it to MeV needs the `m_e·Δ_λ` normalization, which is the **open
  Δ_λ gate**. Asserting the magnitude would be a fit.
- **Not yet a sign-MATCH to the deuteron.** Mapping "net-negative `P`" →
  "reduces binding" needs the **binding-sign convention** of the mass functional
  (how `Ω₂` enters `tr_M(Hol)` and thence the binding), which is not derived
  here.
- **A=2 only.** The "flips positive at A≥3" half needs H₉ (triton) and is
  untested.

  > **ANSWERED 2026-09-13, and the answer is no.** H₉ and H₁₂ were both
  > measured, and the owner ruling of 2026-09-13 adopted the **Wenzl** weight
  > as the pairing (bean `qou-za3q` decision 1, derived in `qou-gba1` from the
  > Markov stabilisation axiom). Under it,
  >
  > ```
  > deuteron −6.921    triton −13.931    ⁴He −20.466      -, -, -
  > ```
  >
  > **there is NO sign change in A = 2, 3, 4** — the "flips positive at A≥3"
  > signature this document names is not exhibited. It appeared only under the
  > rejected quantum Plancherel measure (−, +, +), and the ruling did not turn
  > on the sign, so the phenomenon simply did not survive a measure chosen on
  > principle.
  >
  > **THIS DOCUMENT'S OWN RESULT IS UNAFFECTED.** Its finding is that the
  > linear Magnus pairing is *sign-indefinite* at A=2 and so clears the
  > non-negativity wall that excluded the quadrature ‖F_q‖². That holds under
  > **both** weight families and **both** intra-nucleon words, because it is a
  > statement about a commutator's trace pairing rather than about the weight.
  > `qou-dp32` stands. What is retired is the A-dependence, which this document
  > correctly flagged as untested rather than claimed.

## Consequence for the work plan — two bounded follow-ons

The quadrature route (`qou-jqof`) is closed as a *carrier* (excluded by
non-negativity); the linear Magnus route (`qou-dp32`) is **open and viable**. The
two next steps, each bounded and each a genuine open question (not a fit):

1. **The binding-sign convention.** Derive how `Ω₂` enters the mass functional
   `tr_M(Hol)` at second order (`tr_M(exp(Ω₁+Ω₂)) ≈ tr_M(ρ) + tr_M(ρ·Ω₂)`), so
   that the sign of `P` acquires a physical direction. Until then "LIVE" means
   "clears the wall", not "matches the deuteron".
2. **A=3 (H₉).** Compute the same pairing for the triton word to test whether
   `P` flips sign with `A` (the "negative at A=2, positive at A≥3" signature).

## Cross-references

- Prior probe (the control): [`deuteron_interface_handle_curvature_probe.py`](../../computations/deltalambda/deuteron_interface_handle_curvature_probe.py) (bean `qou-jqof`)
- Germ normalization: `content/quantum-observable-universes/germ-commutator-q-curvature.md`
- Δ_λ gate (the MeV-normalization blocker): [`2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`](2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md)
