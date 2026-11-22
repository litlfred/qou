# A crossing-covariant, strand-labelled QED operator on the nucleon: what it gives

**Date:** 2026-11-20
**Branch:** `claude/qed-crossing-covariant-mubar-2026-11-20` (PR #8557)
**Front:** owner-authorised option 4 (2026-11-20): a crossing-covariant, non-pairwise QED
operator and a derived scale `c_em`.
**Bean:** `qou-qcov` (the gap this front attacks; stays open — see §6).
**Lean:** [`QOU/BraidsAndKnots/CrossingCovariantQED.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/CrossingCovariantQED.lean) — sorry-free.
**Probe:** [`computations/crossing_covariant_qed_probe.py`](../../computations/crossing_covariant_qed_probe.py)
→ `computations/crossing-covariant-qed.witness.json` (70 dps, proton `q₀`).

## Verdict

**No.** A crossing-covariant operator of the proposed kind, with `c_em = α_em·E₀_tower`, does
**not** reach the μ–p gap. It gives **exactly zero** at first order on the Borromean nucleon
`V³ = (σ₁σ₂⁻¹)³`, for the proton and for the neutron, at every `q`. So `M_p^QED = 0` and
`Δm_QED = 0` from it. The μ̄ three-body channel does not rescue it: its linear term is forced to
zero, and its even term has a coefficient nothing here derives.

This is **(a) for the energy** (one construction class gives zero; it says nothing about operators
outside the class) and **(b) inside the class**, where the invariant is the braid relation itself.
The class is stated exactly in §1.

## 1. The construction, and the class it lives in

Read a braid word letter by letter and carry the **component labels** of the strands. At a letter
that exchanges strands `a, b`, deform the generator to first order:
`σ ↦ σ(1 + ε·Y_ab)`, `σ⁻¹ ↦ (1 − ε·Y_ab)σ⁻¹`. The second form makes `σσ⁻¹ = 1` hold to first
order automatically. A QED insertion has `Y_ab ∝ Q_a Q_b`.

The class is **first-order** and **local**: `Y_ab` lies in the subalgebra of the one crossing it sits
on. Two versions:

- **narrow:** `Y_ab = α_ab·1 + β_ab·σ` (the subalgebra `span{1, σ}` the crossing generates);
- **wide:** `Y_ab` anywhere in the commutant of that crossing's generator. This is 5-dimensional on
  the 3-dimensional `(2,1)` weight space.

Non-local insertions (an operator spread over several crossings) and second-order terms are
**outside** the class.

## 2. Covariance forces a scalar (proved), up to a central element (measured)

**Narrow class, proved.** The first-order defect of `σ₁σ₂σ₁ = σ₂σ₁σ₂` is exactly

    β_ac · (σ₁σ₂²σ₁ − σ₂σ₁²σ₂),

where `{a, c}` is the pair exchanged by the **middle** letter (`r3DefectG_eq`, generic commutative
ring, given only `h·q = q² − 1`). Its `(0,0)` entry is `q² − 1` (`mid_diff_00`). Every pair is the
middle pair of some labelling, so for `q² ≠ 1` **every `β` vanishes** (`beta_eq_zero_of_covariant`).
The scalar insertion is covariant for every `α` (`r3Defect_scalar`), and a nonzero `β` provably
breaks covariance (`r3Defect_ne_zero`).

**The fixed-position insertion is not covariant (proved).** Using the position operators `Q₁₂, Q₂₃`
of `NucleonWeightSpaceTwoTerm` as `Y` is natural, since each commutes with its own crossing. It
fails anyway: the `(2,2)` entry of the defect is `−(2/3)(q − q⁻¹)(q² + 1)` (`posDefect_22`), which
is nonzero for `q⁴ ≠ 1` (`posDefect_ne_zero`). On the weight space a flavour does not travel with its
strand when `q ≠ 1`, because `Ř` is not the permutation. This independently confirms the sibling's
T2 (`NucleonQEDCovariance`, PR #8552) for the deformation reading.

**Wide class, measured (not proved).** At `q = 2`, in exact rational arithmetic, the
first-order-covariant insertions inside the crossing commutants form a **6-dimensional** space.
That is 3 pairs × `span{1, Z}`, where `Z` is the non-scalar element commuting with **both**
generators: the sibling's `NucleonQEDCovariance.M`. All non-scalar solutions are central. The
classification is a single-`q` measurement. The consequence in §3 is proved for **every** central
`Z`.

## 3. What the covariant insertion computes: a coloured writhe, zero on `V³`

With a scalar `Y`, the deformed word is the undeformed word times a scalar (`defWord_eq_smul`). The
first-order coefficient of that scalar is the **coloured writhe** (`fac_first_order`):

    colWrithe = Σ_letters e · α(a, b)  =  Σ_{s<t} α_st · crossSum_st      (colWrithe_eq_pairs)

Here `crossSum_st = 2·lk_st` on a pure braid. It is invariant under R2 and R3 in any context whose
labelling stays a permutation (`colWrithe_r2_context`, `colWrithe_r3_context`,
`finalPerm_mem_perms3`). This is the braid-word form of the mutual-helicity term
`Σ_{i≠j} Φ_iΦ_j lk_ij` of Moffatt–Ricca [moffatt-ricca-helicity], with charges in place of fluxes.

On `V³` all three `crossSum` vanish (`BorromeanPairwiseLinking.borromean_crossSum_zero`). Hence:

- `borromean_firstOrder_trace_zero`: `tr(V³_ε) = tr(V³) + O(ε²)` for **every** symmetric `α` and
  every `q`;
- `np_split_firstOrder_zero`: the neutron and proton colored writhes agree, both 0;
- `borromean_firstOrder_traceZ_zero`: the same holds with a central `Z` in place of the scalar.

The task asked whether the pairwise version's `n − p` splitting reduces to linking numbers and is
zero at `q = 1` but possibly nonzero at `q ≠ 1`. **It reduces to linking numbers and is zero at every
`q`**: the trace factorises before any `q`-dependence can enter. Negative control: on the Hopf link
`σ₁²` with proton labels, the coloured writhe is `2·(2/3)² = 8/9 ≠ 0` (`colWrithe_hopf_ne_zero`).

## 4. The three-body (Milnor) channel

The Borromean nucleon's first non-vanishing linking invariant is `μ̄₁₂₃ = ±1`
(`MilnorTripleLinkingMagnus`, a port of `binding_mn_milnor_linking.py`). `μ̄` **alternates** under
an odd relabelling (`mubar_swap_eq_neg`).

- **Linear term pruned (b).** For a relabelling-covariant coupling to an alternating invariant, the
  charge coefficient must alternate under the same exchange. Such a coefficient vanishes when the two
  exchanged charges are equal (`alternating_coeff_vanishes_on_equal_charges`). Both nucleons have a
  repeated charge (`uu` in the proton, `dd` in the neutron). So `Q₁Q₂Q₃·μ̄` is not covariant, and its
  covariant replacement is zero. This sharpens the corpus's existing prune
  (`MilnorTripleLinkingMagnus.linear_coefficient_must_vanish`), which assumed exchange symmetry of
  the self-energy rather than deriving it from relabelling covariance.
- **Even term open.** `E₃ = c₃·Q₁Q₂Q₃·μ̄²` is covariant. Its `n − p` value is `(2/9)·c₃·μ̄²`
  (`evenThreeBody_np_split`), and its proton value is `−(4/27)·c₃`. **Nothing here derives `c₃`.**
  It is not a first-order crossing insertion: by §2 none of those can see `μ̄`. Whatever produces
  `μ̄²` is a second-order or non-local object, which is outside the class.
- **Not applicable to the canonical atom word.** The corpus has already measured `μ̄ = 0` on every
  triple of the canonical atom-word closures. See `MilnorTripleLinkingMagnus` §"third prune" and
  `milnor_mubar_vanishes_on_every_triple_probe.py`. The `±1` above is specific to the `(σ₁σ₂⁻¹)³`
  presentation used by the two-term arc.

## 5. Numbers (proton `q₀`, 70 dps; `crossing-covariant-qed.witness.json`)

| quantity | value | status |
|---|---|---|
| `q₀` (proton pin) | 1.1099785827513808076… | CAL-2, experimental anchor |
| `tr(V³)` on `(2,1)` | 2.994185812979964086728199 | exact form in sibling Lean |
| `d tr(V³_ε)/dε`, scalar insertion, p / n | 0 / 0 (`|·| < 1e-70`) | proved zero |
| same, central `Z` insertion, p / n | 0 / 0 | proved zero |
| same, fixed-position `Q₁₂/Q₂₃` (NOT covariant), p / n | ≈0 / 0.0042615761263751 | comparison only, not an energy |
| `α_em⁻¹(q₀)` | 137.03593509397560466 | derived; **conditional on the Witten-κ Gram `sorry`** |
| `E₀_tower` | 4.2274833556290305503 MeV | `m_e/(q₀(q₀−1)) / (1 − ℏ_q²)` |
| `c_em = α_em·E₀_tower` | **30.849450932194790699 keV** | single-functional scale |
| `M_p^QED` (this operator) | **0** | |
| `Δm_QED = M_n − M_p` (this operator) | **0** | |
| μ–p gap | 0.2288 keV | comparison point only, **not reached** |

The task's note quotes `α_em·E₀_tower = 0.0133 keV`. That figure includes the two-term arc's
connected-trace factor `4.307e-4`. The bare scale is 30.849 keV. Neither multiplies anything nonzero
here.

**Diagnostic, not adopted.** Write the even term as `c₃ = κ·c_em`. To reach the gap in the proton it
would need `κ = 0.0500624793418`. This number is what a derivation of `c₃` would have to produce. It
is recorded so that a later derivation can be checked against it. It is **not** a fitted parameter,
it is not used anywhere, and no structural reason for it is known.

## 6. What remains open

1. **`c₃`, the coefficient of the even three-body term** (§4). This needs a second-order or non-local
   construction that sees `μ̄²` and fixes its normalisation without reference to the gap.
   Proposed new GAP bean below.
2. **The wide-class classification (§2) at general `q`.** It is measured at `q = 2` only. A Lean
   proof would compute the R3-covariance kernel over the 5+5-dim commutants symbolically. The
   vanishing on `V³` does not depend on it: that holds for every central `Z`.
3. `qou-qcov` stays **open**. This PR closes its "strand-labelled crossing insertion" candidate in the
   negative within the stated class. It does not close the bean's question, which is whether a
   derived non-pairwise operator reaches the gap.

## 7. Corpus-grep (done before this note)

- Path 0 (`corpus_search` MCP): not available in this session. Paths 1–6 follow.
- `docs/audits/`: `2026-08-25-4b-pairwise-linking-prune` (pairwise lk vanishes on `V³`; this note
  is consistent with it and extends it from functionals of lk to all covariant local insertions);
  `2026-08-29-colour-antisymmetry-from-milnor-mu-bar`; `2026-08-30-helicity-ladder-cannot-supply-the-he4-surplus`;
  `2026-08-01-em-linking-reads-round1`. No coloured-writhe construction and no first-order R3
  covariance argument for a QED insertion was found.
- `folio/`, `computations/`: `BorromeanPairwiseLinking`, `MilnorTripleLinkingMagnus`,
  `NucleonWeightSpaceTwoTerm`, sibling `NucleonQEDCovariance` (PR #8552), and
  `binding_mn_milnor_linking.py` are reused, not re-derived. A grep for "colored/coloured writhe"
  and "linking-number energy" returned 0 hits.
- `library/` (INDEX, sections, `ocr/`): Moffatt–Ricca 1992 (`procrsoclondona92`, OCR only) gives
  the helicity decomposition that §3 mirrors. Evans–Berger 1992 (`1992evansberger`, OCR) gives
  higher-order linking integrals. Neither supplies a coefficient for a `μ̄²` energy.
- Beans: `qou-qcov` (this front), `qou-bn8e` (E_EM not derived), `qou-o6ml` (EM-linking attack,
  route (1) higher-order Milnor). Consistent with all three. `qou-o6ml` route (1) is narrowed by §4
  to its even, non-first-order part.

-- Refs: [kassel1995], [milnor1957], [moffatt-ricca-helicity], [evans-berger1992].
