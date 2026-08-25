# Low-isotope mass + binding error: staleness vs corpus gap

**Date:** 2026-08-25 · **PR:** [#5765](https://github.com/litlfred/qou/pull/5765) ·
**Beans:** `qou-9ot5` (session), `qou-fdjp`, `qou-04cj`, `qou-5d6k`, `qou-ib3g`, `qou-ahbz`

## Question

Owner ask: of the live low-isotope mass/binding error, how much is **compute that has
not been updated** to the recent canonical work (convention D, proton pin,
`bring_color_weighted`), and how much is a **gap in the corpus** — a term of the
derivation that does not exist yet?

## Verdict

**Staleness accounts for ≤ 10 % of the error, and 0 % at ⁴He. ≥ 90 % is a missing
term.** Further, the one lever with real leverage was **already pulled**, and pulling
it made the light-isotope accuracy **worse**.

## 1. What the dashboard actually runs (checked, not assumed)

| ingredient | state | evidence |
|---|---|---|
| Markov parameter | **convention D**, `z = q₀³/(q₀²+1) = 0.6126880` | `_bond_type_L`, `mass_binding_dashboard.py:352` — inline C literal fixed 2026-08-09 |
| q₀ pin | **proton**, `1.1099785827513808…` | `q_parameter.Q_50_DIGIT_STR`; stem absent from `q0_anchor_manifest.json` ⇒ proton by default |
| p/n colour weighting | **on**, `d_pn = −h(½ − δ/4)` | `_bond_type_L:356` via `flavor_split_leading` |
| writhe normalisation | **on**, Lean-proved `(1−h)^(Δe/2)` | `QOU/QBeta/WritheNormalisation.lean`, sorry-free |
| precision | mpmath end-to-end, 60 dps | `_bond_type_L` guard |

So all three owner rulings are **already applied on this cone**. The staleness
hypothesis was tested against a cone that had already been migrated.

## 2. Lever magnitudes — measured by toggling one ingredient at a time

To reach `err = 1.00`, `B_sym` must rise **226 %** at ⁴He, **120 %** at ⁶Li/⁷Li, and
**fall 21 %** at ²H.

| lever | measured effect | needed | shortfall |
|---|---|---|---|
| q₀ pin, proton ↔ muon | `B_sym` moves **123–136 ppb**; ⁴He err 3.25941 → 3.25941 | 226 % | **1.8 × 10⁷ ×** |
| colour weighting on/off | ⁴He err 3.2594 → 3.2590 (**1.2 × 10⁻⁴** rel.) | 226 % | **1.8 × 10⁴ ×** |
| writhe on/off | **zero** on N = Z (²H, ⁴He, ⁶Li); ³H 7.4 %, ³He 10 % | 226 % / 38 % | **∞** at ⁴He; **5 ×** at ³H |
| convention C → D (**already applied**) | ⁴He 2.3630 → **3.2594**; ³H 0.9890 → 1.3815; ²H 0.5720 → 0.7853 | 226 % | **8 ×**, and **wrong direction for every A ≥ 3** |

The pin bound is exact rather than empirical: `α = E₀ = m_e/(q₀(q₀−1))` enters every
binding form **linearly**, and `E₀` is 4.185981363 MeV (proton) vs 4.185980828 MeV
(muon) — **128 ppb** apart. A 128 ppb shift cannot produce a > 1 % change.

**The convention-D row is the finding.** D is the largest of the four levers and it
moved A ≥ 3 accuracy **against** the target by 27–40 %, because `z_D > z_C` gives
smaller per-bond energies. It helped only ²H.

## 3. The mass side is not a separate error

At ⁴He, `err m_qCLT = +0.529 % × 3727.379 = 19.72 MeV`, against
`B_AME − B_qCLT_fac = 28.296 − 8.59 = 19.71 MeV` — identical. Free-nucleon mass error
contributes `2 × 939.565 × 5.01e−7 = 0.00094 MeV`, **0.005 %** of the miss.
**There is no mass-side error to find; there is only the binding error.**

## 4. Residual shape — extend the lever arm past A = 7

Six light nuclei cannot separate `A` from `A^{2/3}`. Extending the same closed-form
chain to A = 238:

| iso | A | R = B_AME − B_sym | R/A | B_AME/A | **B_sym/A** |
|---|---|---|---|---|---|
| ²H | 2 | −0.61 | −0.30 | 1.112 | 1.416 |
| ⁴He | 4 | 19.61 | 4.90 | 7.074 | 2.170 |
| ¹²C | 12 | 60.09 | 5.01 | 7.680 | 2.673 |
| ⁵⁶Fe | 56 | 329.99 | **5.89** | **8.790** | 2.898 |
| ²⁰⁸Pb | 208 | 1014.37 | 4.88 | 7.867 | 2.991 |
| ²³⁸U | 238 | 1088.07 | 4.57 | 7.570 | 2.998 |

`B_sym/A` is monotone and **saturates at 2.998 MeV/nucleon**, so
**R/A = (B_AME/A) − ≈3.0** — the residual is the nuclear binding curve minus a
constant. It peaks at ⁵⁶Fe and falls, exactly like `B_AME/A`.

- `B_sym` is a pure saturating **volume** term at **2.93×** too small a coefficient
  (2.998 vs 8.790 peak; **5.25×** against SEMF `a_V ≈ 15.75`).
- **Every other SEMF term is absent.** The model's `B/A` rises monotonically and never
  turns over ⇒ no surface term. `B_AME/B_sym` falls 3.03 (⁵⁶Fe) → 2.53 (²³⁸U) purely
  because Coulomb eats `B_AME` and the model carries none.
- Light-A shell structure sits on top: against the 2.95 plateau (12 ≤ A ≤ 90), ⁴He
  reads **+10.5 %** and ⁶Li/⁹Be **−25 %** — the α-cluster signature.

## 5. ⁴He is beyond any pairwise edge set

`B_allpairs = α[C(Z,2)L_pp + ZN·L_pn + C(N,2)L_nn]` (the complete graph `K_A`, the
**maximum** edge set) vs truth:

| iso | B_AME | B_sym (chain) | B_allpairs (K_A) | B_AME/B_allpairs |
|---|---|---|---|---|
| ³H | 8.4818 | 6.1397 | 8.9726 | 0.945 |
| **⁴He** | **28.2957** | 8.6813 | **17.1798** | **1.647** |
| ⁶Li | 31.9940 | 14.5298 | 43.0409 | 0.743 |
| ⁷Li | 39.2451 | 17.8367 | 61.4601 | 0.639 |

Truth is bracketed by chain and complete graph for every nucleus **except ⁴He**, which
exceeds the complete-graph maximum by **11.12 MeV = 39.3 % of its binding**. In bond
equivalents `n_eff = B_AME/(αL_pn)`: ³H needs 2.99 ≈ C(3,2) = 3; ⁴He needs **9.99
against a hard ceiling of C(4,2) = 6**.

Three independent estimates of the ⁴He excess agree at **11–14 MeV**: vs the `K_A`
maximum (11.12), vs the linear-in-A trend through the other five (+11.95), vs
interpolating R/A between ³H and ⁶Li (+13.7).

**Scope-(b) structural exclusion**, invariant cited: the exact `K_A` Laplacian
spectrum `det_A(m) = (1+(A−1)m)(1−m)^{A−1}`. No pairwise edge set reaches ⁴He at the
derived bond constants — the ⁴He term is irreducibly ≥ 3-body.

## 6. The two gaps

**GAP-1 — a per-bond energy defect at A = 2, with no coordination to blame**
(`qou-5d6k`, cheapest to attack). `αL_pn = 2.833` vs `B_AME(²H) = 2.225`, **+27 %**.
²H is a *single* p–n bond with no coordination topology, so nothing else in the
calculation can carry it. Under D the target is **reachable** — the admissible
interface band `[2.051, 3.798]` contains it — but the **derived** colour weight gives
`t = 0.499656` where `t = 0.119453` is required. A live derivation gap in a single,
fully-specified, parameter-free quantity.

**GAP-2 — a missing additive extensive term** (`qou-ib3g`). Owned by the Δ_λ
**magnitude** leg (open), the "separate additive extensive object"
(`2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md` §4, open), and
the coordination-graph closure `qou-v0yw` (open) — the last of which brackets
everything *except* ⁴He.

## 7. ⁴He: what is derived and what is postdiction

| construct | derived? | note |
|---|---|---|
| SU(4) `[1⁴]` gate, `dim[1^A] = C(4,A)` | **yes**, sorry-free | supplies the **locality** (where a 4-body term can live), **not** the magnitude |
| `B_gate = E₀·ln(1/W_λ)` — err **0.944** | **no** | deprecated 2026-08-08, red-teamed 2026-08-22. `Σ_λ W_λ ≠ 1` (1.517 at n=12) so `ln(1/W)` is not a surprisal; never touches `tr_M`; reports 7.58 MeV of binding for a **free** nucleon |
| `B_vol = a_V·A` — err **0.933** | **no** | surprisal form *selected over* the linear alternative (3.50) because it lands near 8 |
| `B_magic = 2·m_e·A·8G` — err 0.944 | **no** | deprecated; hand-picked prefactor and `A·8G` rule |
| colour-tube weight | **conjectural** | conditional on open `conj:s5-so3-fiber-action`; fixes p/n sign, not extensive magnitude |

Two structurally unrelated constructs (`B_vol`'s `a_V = 7.5836` and
`2·m_e·8G ≈ 7.49`) independently land near the same ~8 MeV/nucleon. **That is a
numerology signature, not corroboration.** Nothing here should be presented as a ⁴He
binding prediction.

## 8. Coulomb

For a mirror pair the chain gives `B_sym(Z,N) − B_sym(N,Z) = α(L_nn − L_pp)` — a
**constant**, independent of Z, N, A:

| pair | A | exp. split | model (const.) | model/exp | E_C | E_C/exp |
|---|---|---|---|---|---|---|
| ³H/³He | 3 | 0.7638 | 0.7653 | **1.002** | 0.8474 | 1.110 |
| ⁷Li/⁷Be | 7 | 1.6442 | 0.7653 | 0.465 | 1.9167 | 1.166 |
| ¹³C/¹³N | 13 | 3.0028 | 0.7653 | 0.255 | 3.1187 | 1.039 |
| ¹⁵N/¹⁵O | 15 | 3.5365 | 0.7653 | 0.216 | 3.4690 | 0.981 |

The ³H/³He split is **doubly** explained — strong bond 0.7653 (0.2 % of experiment)
**plus** `E_C` 0.8474 (+11 %) = **2.11×** the observed split. So the dashboard's
additive (not subtracted) convention is arithmetically correct **given the current
strong core**, but it is a stopgap covering a defect:
`QOU.QBeta.InterfaceScalar.charge_independence_iff` proves `L_pp = L_nn` **iff h = 0**,
so the production bond assignment structurally violates charge independence for any
`q ≠ 1`, and `mirror_split_eq_L_diff` proves the flavour parameter cancels out of the
split entirely. The framework puts its charge-symmetry breaking in the **topological**
channel where the eightfold way puts it in the **flavour** channel (`qou-4waf`).

**The 0.2 % ³H/³He agreement is a single-point coincidence, not evidence** — the same
constant is 0.22× of experiment by A = 15.

## 9. Stale claims found in passing (all convention-C artefacts of the 2026-08-09 fix)

| location | says | live under D |
|---|---|---|
| dashboard `E_C` legend | "r₀ = 1.2 fm, α_EM·ℏc = 1.43996 CODATA" | module uses **λ̄_π = 1.41382 fm**, **derived** α_EM since 2026-08-09 |
| dashboard legend | production σ/σ⁻¹ mirror error "~200–350 %" | **0.2 %** at ³H/³He |
| dashboard legend, `B_gate` | "fixes ⁴He (err 2.36→0.94)" | B_sym err at ⁴He is **3.26**, not 2.36 |
| `inter-nucleon-channel-color-tube.md` | `L_nn/L_pp − 1 ≈ 78 %` | **30.1 %** |
| `SU4SupermultipletGate.lean` header | "×5.10 gap"; "2.09× super-pairwise at ⁴He" | **3.26×**; **1.647×** |
| `2026-07-18-…-k4-collective-magnitude.md` §3 | needs `deficit(³H)/deficit(³He) = 1.223` | **0.9993** — the "collective = isospin split" reading needs re-scoping |
| bean `qou-qlma` / `bond_energy_floor` | `α ≤ 3.2094` required, actual 4.1860 | **C-scoped**; Lean carries its own retraction. Under D the ²H target is *inside* the band |

## 10. Arity flag against AGENTS.md

AGENTS.md states the pairwise cap `ρ_A ≤ C(A,2)` is "proved in
`QOU.MassTheory.exchangeDet_pow_two_le_four`", and bean `qou-i8oq` is marked
**completed**. The file is `BindingSaturationCapA4.lean` and the theorem is
`(1−m²)^6 ≤ (1+3m)(1−m)^3` — the **A = 4 instance only**. No general-A version exists
in `content/`. This is the §"Grep the claim SHAPE" arity conflation. It changes no
conclusion here (A = 4 is the case that bites), but the general claim should be
re-scoped or proved.

## 11. A non-physical degree of freedom

`atom_braid_word_3A` hard-codes the ordering `['p']*Z + ['n']*N`. A nucleus has no
ordering. Spread over all orderings under D: ³H 5.6 %, ⁴He 2.7 %, ⁷Li 2.9 % of
`B_AME`. Not large enough to matter against 226 %, but `B_sym` should not be quoted to
four digits as if it were free of convention.

## Scope discipline

No item is newly declared open — every open item cited was already `todo`/`in-progress`
or already declared open in an audit, verified against `.beans/` this session. No fit is
proposed. The two negatives stated are scope-**(b)** with cited invariants (the exact
`K_A` Laplacian spectrum; `A = Z+N` isospin-blindness of an unsigned `K_A` invariant).
Everything else is scope-**(a)**: measured deficits of specific constructions as they
currently stand, not exclusions of ingredients.
