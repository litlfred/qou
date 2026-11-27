# Does the ħ² F-term of the Borromean core give a β₀-like number? Pre-registration (2026-11-22)

Written and committed **before** `mn_beta0_from_braid_probe.py` is written or run. Owner request,
relayed by the parent session: test, as research, whether the order-ħ² `f^{abc}` term of
`V³ = (σ₀σ₁⁻¹)³` (§49 of `LITERATURE-COMPARISON.md`) yields a scale-free number with the structure
of the QCD one-loop coefficient. **Expected outcome: a documented negative.** Algebra only; no
gluon is selected (owner ruling 2026-11-22: the gluon of step 4 of `def:derived-atom` stays open).

## Target (fixed here, not after the run)

QCD one loop, convention `β(α_s) = −β₀ α_s²/(2π)`:
`β₀ = 11 − (2/3) n_f = (11/3) C_A − (4/3) T_F n_f`, `C_A = 3`, `T_F = 1/2`.
The antiscreening part `(11/3) C_A` comes from the gluon self-coupling (`f f`); the screening part
`(4/3) T_F` per flavour comes from a closed quark loop (`T_F`).

- Per-flavour ratio, antiscreening : screening = `11 : 2/3`, i.e. **`33/2`**. This equals
  `((11/3)C_A) / ((4/3)T_F)` for SU(3), so stripping the group factors does not change it.
- Pure-glue value (n_f = 0) in common normalisations: the set
  **S = {11, 11/3, 22/3, 11/2, 11/6, 22, 11/12}** (β₀ = 11; (11/3)·C_A/C_A = 11/3; b₀ = 2β₀/3 and
  halvings/doublings that appear in `β = −b g³/(16π²)` vs `β = −β₀ α²/(2π)` vs `/(4π)` forms).
  Seven values are admitted; that is the look-elsewhere budget, stated now.

## Corpus already held (corpus grep, this session)

- `CORPUS-GREP-gluon-dynamics.md` row 2: QCD β₀ is **not found** in folio/computations/docs; no held
  library source states it. Row 4: antiscreening is a label only.
- `ElectroweakVevGaps.lean:197-225`: `oneLoopB0 CA weylT scalarT = −(11/3)C_A + (2/3)ΣT_Weyl + (1/3)ΣT_scalar`
  is a **definition taking β₀'s numbers as input** (sign rule for the EW-vev loop). It derives
  nothing; the 11/3 is typed in.
- Bean `qou-n1ks` (β₀..β₃ "proof"): **scrapped**; its Lean/probe never existed on main. Its
  2026-11-21 note records that Feynman loop sums rely on virtual quanta, excluded by an owner ruling
  of 2026-11-21 ("no virtual photons"). That ruling is **not** in
  `docs/coordination/owner-rulings.md` (grep `virtual`: 0 hits); it is cited here from the bean only.
- Beans `qou-5iaz` (α_s: no coupling extraction, `in-progress`, blocked on `qou-ni4b`) and
  `qou-ni4b` (SU(3) colour action on the framework's own 3-strand module: open). This probe does not
  touch either gap: it uses the standard `C³` colour tensors, not a framework-native action.
- `docs/audits/2026-11-20-ew-vev-gaps.md` §6: no corpus derivation of anti-screening or b₀.

## Why the prior is negative (stated before computing)

1. **No flavour count exists in a 3-strand word.** β₀ is linear in a free integer `n_f`, the number
   of quark species running in the loop. A braid word on three strands has a fixed number of strands
   and, after closure, a fixed number of closed components. "Number of closed strands" is fixed by
   the word (1 for a single partial closure), not a free parameter, and the strands are the three
   quarks of one baryon, not species summed over. So at most the pure-glue value or the per-flavour
   ratio can be tested; the `n_f`-dependence cannot.
2. **No spin.** In QCD `11/3 = 4 − 1/3` per C_A (paramagnetic spin-1 term minus diamagnetic orbital
   term; Nielsen–Hughes `−(−1)^{2s}((2s)² − 1/3)`) and `4/3` carries the Dirac spin-½ factor. The
   braid/Hecke data has colour only; nothing supplies Lorentz spin. The prime 11 in the numerator is
   therefore a strong discriminator.
3. **No loop integral.** β₀ is the coefficient of `log μ` from a one-loop integral; ħ = log q here
   is a deformation parameter, not a log of a momentum scale.

## Exact constructions (all exact: sympy rationals in q, Fraction series in ħ, q = e^ħ)

Common: V = C³, `T^a = λ^a/2`, `Ω = Σ T^a⊗T^a`, `F = i f^{abc}T^aT^bT^c`,
`G = f^{abe}f^{cde}T^aT^bT^cT^d`, Jimbo Ř of U_q(sl₃) exactly as in
`mn_three_gluon_vertex_probe.py` (σ_i ↦ Ř_{i,i+1}, unnormalised). Classical SU(3) Haar projection
onto the commutant, as in §49 (choice-dependent; stated as such).

**(i) ff : quark-loop ratio.**
- `X_ff` := the G-coefficient (modulo the degree-≤2 Ω span, as in §49 M5) of
  `W₄ := (σ₀σ₁⁻¹σ₂)⁴ ∈ B₄`, at its **leading** nonzero ħ order. Structural rule for W₄: extend the
  photon letter V = σ₀σ₁⁻¹ to four strands with alternating signs (+ − +), raised to the smallest
  power that is a pure braid (underlying permutation trivial) — the same rule that gives V³ from V
  (3-cycle ⇒ power 3; the 4-cycle ⇒ power 4). The leading-order G-coefficient is invariant under
  scalar framing normalisation, so Ř vs R̃ does not matter.
- `X_loop` := the Ω₁₂-coefficient (after projection onto span{1, P} on V⊗V, with
  `X = a·1 + b·P ⇒ Ω-coef = 2b`) of the **closure of strand 3** of V³, at its leading nonzero ħ
  order. Two closures, both reported:
  - **L1** colour partial quantum trace on strand 3 with weight `K = diag(q², 1, q⁻²)` or its
    reverse, **whichever makes `Tr_q,3(Ř₂₃)` a scalar (Markov property)** — decided by that check,
    not by the target — normalised so closure(1) = 1.
  - **L2** convention-D Ocneanu conditional expectation `E_D: H₃ → H₂`, `z_D = q³/(q²+1)`
    (`E(xσ₁y) = z·xy`, `E(x) = x` for x, y ∈ H₂), applied to the H₃ coordinates of V³, then
    represented on V⊗V.
- `r = X_ff / X_loop` for L1 and L2. **Scale-free only if both are at the same ħ order**; if the
  orders differ the ratio carries a power of ħ and counts as a **miss**.
- **HIT (i):** `|r| = 33/2` exactly, same ħ order, and `X_ff`, `X_loop` of opposite sign.
  Partial: `|r| = 33/2` with same sign → reported as "magnitude only", not a hit.

**(ii) ħ-expansion of the F-projection.** `c_F(V³) = −(q−1)²(q+1)⁴(q⁴+1)/(2q⁵)` (§49). It is
bar-invariant, so `c_F = c₂ħ²(1 + b ħ² + O(ħ⁴))`. Report `b` and `2b`
(the latter = the ħ² coefficient of `ħ d/dħ log c_F − 2`). Same for the H₃ commutator coefficient
`(q−1)²(q+1)²(q⁴+1)/(2q⁴)` (call it `b'`).
- **HIT (ii):** `b`, `2b`, `b'` or `2b'` ∈ S.
- **Disclosure (not blind):** while designing this, I expanded `c_F` by hand:
  `c_F = −16 sinh²ħ · cosh²(ħ/2) · cosh 2ħ`, giving `b = 1/3 + 1/4 + 2 = 31/12`, and the commutator
  coefficient `4 sinh²ħ · cosh 2ħ`, giving `b' = 7/3`. If correct both miss S. The probe re-derives
  them exactly; (ii) is therefore a recorded check, not a test.

**(iii) Casimir-weighted reading.** `P₂ := [ħ²] Haar(V³)` acts on the isotypic components of
V^⊗3 = 10 ⊕ 2·8 ⊕ 1 (quadratic Casimirs `C₂ = 6, 3, 0`). Read its eigenvalue on 10, on 1, and the
two eigenvalues of its 2×2 multiplicity block on 8. Test whether `λ_R = a + β_C·C₂(R)` holds on all
channels (3 or 4 data, 2 unknowns: overdetermined, so a consistency test, not a fit).
- If consistent, report `β_C` and `β_C·C_A`. **HIT (iii):** `β_C` or `β_C·C_A` ∈ S.
- If inconsistent (no single Casimir slope), (iii) is a **miss** by construction.

## Decision rule and honesty clause

- Each candidate is HIT or MISS by the rules above; nothing is re-defined after the run, no other
  power, word, closure, normalisation or ħ order is tried to rescue a miss.
- Even a HIT would be a **numerical coincidence candidate**, not a derivation: no mechanism for
  `n_f`, spin or a loop integral exists in the construction. It would be reported as such and
  beaned, not wired anywhere.
- Expected: all MISS. Report as scope (a): "the searched constructions do not produce β₀"; this is
  not a structural exclusion of any braid route to β₀.
