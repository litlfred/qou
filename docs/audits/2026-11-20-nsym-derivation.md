# 2026-11-20 — Can 𝒩_sym of `conj:g-action-on-substrate` be derived?

Block: `conj:g-action-on-substrate`
(`folio/quantum-observable-universe/quantum-observable-universes/g-action-on-substrate.md`).
Owner ruling 2026-11-20: the host is left open; the owner asks whether the value can
be derived. Prior audits, not redone: `2026-11-20-nsym-host-trace-route.md`,
`2026-11-20-nsym-host-corpus-route.md`.

All numbers are at the **proton** pin
`q₀ = 1.10997858275138080759166909561` (`qou_substrate.constants.q_at`), symmetric
`[n]_q`, mpmath at 60 dps. The back-solved anchor 213.11 was **not** used to select
anything. Part B explains why it cannot even serve as a sanity check.

Artifacts:

| file | role |
|---|---|
| `folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/NSymSlotDerivation.lean` | Lean, generic `Field R`, sorry-free |
| `computations/nsym_slot_trace_derivation.py` | exact `ℚ(q)` check of Part A on `V^{⊗6}` (64×64, sympy) |
| `computations/probes/nsym_anchor_decomposition_probe.py` | exact and 60-dps check of Part B |

## Verdict

There are two results, and neither is a closure.

- **Part A, a conditional derivation.** The corpus constructs exactly one host
  structure: the Hoefsmit strand-pair slots of `V^{⊗6}`. On that host, (G-3) and (G-4)
  force `e_H`, and the carriers force `e_sym^EW`. With them, `tr_F(e_sym^EW · e_H)` is
  forced to `[3]_q² = 9.26414748386` at q₀. This value differs from (a), (b) and (c).
  It also contradicts (G-2): on this host, the symmetric image of every carrier has
  `dim_q = [3]_q`, not `[2k]_q`.
- **Part B, a no-go for the anchor (scope (b)).** The quantity
  `𝒩_sym^anchor ≈ 213.11` is exactly
  `3·(m_p/m_e)·(v/m_p)·[2]³/([4][6][8])²`. Under the proton-pin model of `m_p/m_e` it
  has a double pole at `q = 1`. Every `q`-dimension of an object of `Rep_q(SU(2))` is
  finite at `q = 1`. So no reading of 𝒩_sym as the trace of a host idempotent can equal
  the anchor *as a function of q*. Matching it at the single point q₀ would be selection
  against the target. The comparison section of the block is therefore ill-posed, not
  merely inaccurate.

Minimal missing input for a closure: the corpus does not state that the electroweak
host of (G-1) **is** the Hoefsmit slot object `V^{⊗6}`. (G-1) states a direct sum of
isotypic components instead, and (G-2) assigns `q`-dimensions that this object does not
have. Part A holds under hypothesis H1 below. Without H1 the value is undetermined, as
the two earlier audits found.

## Part A — what the slot host forces

### Hypotheses and tiers

| # | hypothesis | tier |
|---|---|---|
| H1 | The W, Z and H hosts are the strand pairs (1,2), (3,4), (5,6) of `V^{⊗6}`, with `V` the 2-dim `q`-fundamental. Carriers are `σ₁⁴, σ₃⁶, σ₅⁸`. | The realisation is a theorem of the Hecke relations (`thm:hoefsmit-ew-cell-content`, `carrierAlgebra`). The physical labels W/Z/H are conjectural (`conj:electroweak-higgs-torus-link-triplet`). Identifying (G-1)'s hosts with these slots is **an input not stated by the block**. |
| H2 | `e_sym^EW` is the symmetric (`q^{2k}`-eigenvalue) spectral projector of the W and Z carriers. | **Derived** from H1. `σ^{2k}` has the two eigenvalues `q^{±2k}`, distinct when `q^{4k} ≠ 1`, and its spectral projectors are `e±` for every `k` (`S_pow_mul_ep`, `S_pow_mul_em`). The *naming* sym = `+q` follows the corpus convention (`perCarrier true`). |
| H3 | (G-3)/(G-4): `ϱ_Φ : 𝟙 → A^{(H)}` in `Rep`, with `e_H = ϱϱ*/t`. | (G-3) is part of the conjecture. `tr_F(e_H) = 1` is **owner-ruled**. |
| H4 | `tr_F` is the pivotal trace of `Rep_q(SU(2))` on `V^{⊗6}`. | **Derived up to normalisation.** `tr_F` is cyclic and multiplicative on the slots. Its Markov parameter is `z_D = q³/(q²+1)` (`qtr_S_div_qtr_one`), i.e. convention D, the ruled convention. The normalisation is then fixed by (G-4): see below. |

### Steps (Lean names in `NSymSlotDerivation`)

1. **`e_H` is forced.** Under H1 and H3, `A^{(H)} = V ⊗ V`. A morphism `𝟙 → V ⊗ V` is a
   `q`-singlet. On the Hecke side the singlet line is the `−q⁻¹`-eigenspace of `σ₅`,
   which is one-dimensional (`alt_eigvec_unique`). The identification of the
   `U_q`-invariants with that eigenspace is Schur–Weyl–Jimbo duality, cited, not proved
   here. So `e_H = e⁻(σ₅) = [2]⁻¹ · u wᵀ` (`em_eq_cup_cap`), with loop value
   `w·u = [2]_q` (`cap_cup`). This is exactly the "factors through `𝟙`" shape of (G-4).
2. **(G-4) fixes the trace normalisation.** The pivotal trace gives `qtr e⁻ = 1`
   (`qtr_em`), as (G-4) requires. The unit-normalised Markov trace `qtr/[2]^6` would
   give `1/[2]²` on this slot. So the owner ruling `tr_F(e_H) = 1` selects the pivotal
   trace, and the choice is made by a stated axiom, not by a value.
3. **The composite/tensor question dissolves.** On `V^{⊗6}`, the idempotents of
   different slots act on different tensor factors. Their composite *is* their tensor
   product (`composite_eq_tensor`). The ⊕ objection of `NSymTraceAlgebra` (orthogonal
   summands compose to 0) does not arise, because the slots are tensor factors, not
   summands.
4. **Value.** `qtr(e⁺) = q² + 1 + q⁻² = [3]_q` (`qtr_ep`), and the trace is
   multiplicative over slots (`qtr6_kron`). Hence

   `𝒩_sym = qtr₆(e⁺(σ₁) ⊗ e⁺(σ₃) ⊗ e⁻(σ₅)) = [3]_q²` (`nsym_slot`).

   Cross-check by spin decomposition: `V₁ ⊗ V₁ ⊗ V₀ = V₂ ⊕ V₁ ⊕ V₀`, and
   `[5] + [3] + 1 = [3]²` (sympy, in the compute script). Equivalently, the Markov trace
   at `z_D` gives `qtr₆/[2]⁶ = [3]²/[2]⁶ = 0.140109207266`.

   The all-symmetric idempotent `E(+,+,+)`, whose joint rank is the `11` of
   `weak-spectral-completeness`, has trace `[3]³` (`qtr6_all_sym`). Its Kostka-number
   multiplicities `(1,2,3,1)` on `(6),(5,1),(4,2),(3,3)` give `[7] + 2[5] + 3[3] + 1`.
   Read as `e_sym^EW · e_H` with `e_sym^EW` including the H slot, it would give `0`
   instead (`E(+,+,+)·E(+,+,−) = 0`). The block's `e_sym^EW` has EW hosts only, so it
   excludes the H slot.

### Consequences for the block

- **(G-2) is inconsistent with H1.** The image of `e⁺` on a slot is `V₁`, the adjoint,
  with `dim_q = [3]_q` for every carrier power `k`. Table 1 of the block also assigns
  `W^±` and `Z` to the adjoint `(1,0)`. So Table 1 agrees with H1 and (G-2) disagrees
  with both. `[4]` and `[6]` remain crossing counts, as `NSymHostStructure` found.
- **Tension with the torus-link block (flag, not resolved).**
  `electroweak-higgs-torus-link-triplet.md:42` makes the Higgs the **bar-even `A₊` part**
  of `σ₅⁸`, under the spin involution `q^{2k} ↔ q^{−2k}`. Step 1 makes `e_H` the
  `−q⁻¹`-**eigenprojector** of `σ₅`, i.e. the alt Hecke channel. These are different
  objects: a bar-grading component versus a spectral projector. Step 1 is what (G-3)
  forces if `A^{(H)}` is the slot `V ⊗ V`. If the Higgs is instead `A₊`, then (G-3) has
  no slot realisation.

### Values at proton q₀ (12 digits)

| object | closed form | value |
|---|---|---|
| **slot derivation** | `[3]_q²` | **9.26414748386** |
| all-sym `E(+,+,+)` | `[3]_q³` | 28.1973432134 |
| normalised Markov at `z_D` | `[3]²/[2]⁶` | 0.140109207266 |
| (a) | `[4]²[6]` | 107.891521558 |
| (b) | `2[4]+[6]` | 14.6074514146 |
| (c) | `[4][6]` | 26.2530071091 |

## Part B — what the anchor 213.11 is

`computations/n_sym_numerical_anchor.py` sets `μ₀ = m_e/(3E_×)` and
`N_v = v/(E_× μ₀)`. The `3` is `n_c_electron`, the crossing number of the trefoil
electron (`computations/beta-decay-from-q.py:48-54`; `rem:building-block-knots`,
`observations/building-block-knots.md:40`: `m_e = 3·E_×·μ₀`). So `E_×μ₀ = m_e/3` is one
crossing's energy, and

`N_v^script = 3v/m_e` (v in crossing units, ≈ 1.4455e6),

`𝒩_sym^anchor = N_v^script / ∏_{k=2,3,4}[2k]²/[2] = 3·(m_p/m_e)·(v/m_p)·[2]³/([4][6][8])²`.

The probe checks this identity exactly in sympy. It is a rewriting, not a result.

| `v/m_p` used | value | `𝒩_sym^anchor` |
|---|---|---|
| experimental (`G_F = 1.1663788e-5 GeV⁻²`, the script's input) | 262.4181652782 | 213.111824847 |
| block fixed point (conj, `ElectroweakVevFixedPointClass`) | 262.418168819 | 213.111827723 |
| block `T_EW` (tree + 1/π) | 262.418473707 | 213.112075324 |
| block tree `q([2]/2)[4][6][8]` | 262.100163821 | 212.853573400 |

So the anchor is `(3·m_p/m_e) × (N_v^block · [2]³/([4][6][8])²)`. The second factor is
`0.0386881096195` and the first is ≈ 5508.46. The leading term is
`(3/2)(m_p/m_e)·q[2]⁴/([4][6][8])`.

The anchor's denominator holds **two** powers of `[4][6][8]`, while the block's
`N_v` holds **one**, one per carrier. The leftover is `[2]³/([4][6][8])`. No corpus
artifact derives `∏[2k]²/[2]`. The script states it as "conjectured product factor".

### No-go (scope (b); invariant: pole order at `q = 1`)

Under the proton-pin model, `m_p/m_e = F_p(q) = 2·Vol(4₁)·F_Bor(q)/ħ_q² − 12`. This is
`constants._solve_q_proton_f64`, and q₀ is its root (the probe asserts
`|F_p(q₀)/(m_p/m_e) − 1| < 1e-40`). With `N_v` the block fixed point, the anchor becomes
a function of `q`, and the probe measures

`(q−1)² · 𝒩_sym^anchor(q) → 3.0499` as `q → 1`

(values 2.6499, 3.0451, 3.0498, 3.04987 at `q − 1 = 1e-1 … 1e-4`). That is a double
pole, from `1/ħ_q²`. Any `q`-dimension of an object of `Rep_q(SU(2))` is a
non-negative-integer combination of `[n]_q`. It is therefore a Laurent polynomial in `q`
whose value at `q = 1` is the classical dimension: 9, 24, 96 and 14 for the candidates
above. Hence:

> **No reading of 𝒩_sym as `tr_F` of an idempotent on a `Rep_q(SU(2))` host equals the
> anchor as a function of `q`.** At the single point q₀, some integer combination of
> `[n]_{q₀}` will always come close to 213.11. Choosing one for that reason is selection
> against the target.

The invariant is the pole. It depends on taking `m_p/m_e` as the model function `F_p`.
If `m_p/m_e` is instead treated as a bare constant, the statement collapses to the
weaker point: the anchor carries a factor `3·m_p/m_e` that is not a weak-sector
quantity.

### Inversion: what each host value would require

Take `𝒩_sym = X` and `N_v = v/m_p` as the block fixed point. Then G_F requires
`m_p/m_e = X·([4][6][8])²/(3[2]³N_v)`:

| X | required `m_p/m_e` | vs CODATA 1836.152673426 |
|---|---|---|
| `[3]²` (Part A) | 79.81907598 | −95.653 % |
| `[3]³` | 242.9458171 | −86.769 % |
| (a) `[4]²[6]` | 929.5838146 | −49.373 % |
| (b) `2[4]+[6]` | 125.8565104 | −93.146 % |
| (c) `[4][6]` | 226.1935891 | −87.681 % |

These are honest misses. Per Part B they also measure the wrong thing: the factor
`m_p/m_e` was never a host quantity.

## Inconsistencies found (flagged; nothing edited)

1. **"Crossing count" has two units.**
   `electroweak-higgs-torus-link-triplet.md:59` calls `N_v = v/m_p` "the weak-scale
   crossing count". `v/m_p` is in proton units. The crossing count in the sense of
   `rem:building-block-knots` (unit `E_×μ₀ = m_e/3`) is `3v/m_e`, which is what the
   anchor script uses. The two differ by `3·m_p/m_e ≈ 5508`.
2. **Two `G_F` inputs.** `computations/substrate/experimental_constants.py` has
   `G_F = 1.1663788e-11 MeV⁻²`. `electroweak_bring_schwinger_bridge_probe.py` has
   `1.1663787e-5 GeV⁻²`. They differ by 8.6e-8 relative, so `v` moves by 43 ppb. The
   block fixed point is **+13.49 ppb** against the first input and **−29.37 ppb** (the
   block's quoted figure) against the second. The anchor's last digits depend on which
   input is used.
3. **The block's comparison table** (`g-action-on-substrate.md`, §Comparison with the
   anchor value) compares host `q`-dimensions with a quantity that Part B shows is not
   one. Changing the prose is an owner decision. Nothing was edited.

## Verification

- `lean -DautoImplicit=false -s 65536 …/NSymSlotDerivation.lean`: exit 0, 0 errors.
  Run against the restored oleans in `/home/claude/qou`, with `LEAN_PATH` from
  `scripts/lean-direct-env.sh`.
- `#print axioms` on `nsym_slot`, `qtr6_all_sym`, `alt_eigvec_unique`, `em_eq_cup_cap`,
  `S_pow_mul_ep`, `S_pow_mul_em`, `qtr_S_div_qtr_one`, `composite_eq_tensor`,
  `ep_add_em` and `S_hecke`: each gives `[propext, Classical.choice, Quot.sound]`, with
  no `sorryAx`. The module olean was compiled to a temp dir.
- `bun run folio/pipeline/lean-orphan-audit.ts --diff <file>`: no new orphans. The
  module is imported in `lean/QOU.lean`.
- `python3 computations/nsym_slot_trace_derivation.py`: all symbolic asserts pass,
  about 2 s.
- `python3 computations/probes/nsym_anchor_decomposition_probe.py`: produces the tables
  above.

## Corpus-grep record

- `corpus_search`: unavailable in this session.
- `docs/audits/`, `folio/` and `computations/` were grepped for `N_sym`, `mu_0`/`μ₀`,
  `E_cross`, `trefoil`, `A_+`/`A₊`, and the Hoefsmit and torus-link blocks.
- `library/` and `beans/` were not searched in this session. `beans/` is not mounted in
  this worktree.
- I found no corpus statement that identifies (G-1)'s hosts with the Hoefsmit slots
  (H1), and none deriving `∏[2k]²/[2]`. This describes what these searches found; it
  does not prove that no such statement exists.
