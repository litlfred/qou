# ρ_F(⁴He) item 2 — the CPT alt-block-doubling mechanism is refuted under the canonical convention

**Date:** 2026-08-21 · **Arc:** bk-crossing-coordination, open item 2 (`ρ_F(⁴He)` / `a_D^(4)`) · **PR:** (arc follow-up)
**Probe:** [`computations/he4_rho_F_cpt_mechanism_refuted.py`](../../computations/he4_rho_F_cpt_mechanism_refuted.py)
**Witness:** [`computations/he4-rho-F-cpt-mechanism-refuted.witness.json`](../../computations/he4-rho-F-cpt-mechanism-refuted.witness.json) (allPassed)
**Discipline:** scope-(a) mechanism refutation; resolves a corpus inconsistency; no fit; no wiring; q₀ proton-anchored.

## The corpus was internally split on ρ_F(⁴He)=2's status

| Source | Claim |
|---|---|
| `magic-A-binding-formula-context.md` (**authoritative**) | "The categorical derivation of the integer 2 — vs `[2]_q`, `2cos(π/3)`, or another natural candidate — is **not closed** … the value is consumed as an input hypothesis." |
| `2026-08-02-he4-nu-sdp-decisive-2-not-3.md` | ρ_F=2 "is **not derived**"; data-implied 1.889. |
| `frobenius-packing-density.md` (**over-claims**) | ρ_F ∈ {m_e, 2m_e} is derived from a CPT mechanism: "closed-shell clusters saturate all blocks internally, [the alternating antiparticle channel] populated ⇒ CPT doubling ⇒ ρ_F = 2m_e … **derives the {m_e, 2m_e} threshold … without phenomenological tuning**." |

## Adjudication — the alt block is structurally empty, so the CPT mechanism cannot operate

Reading the canonical ⁴He Wedderburn decomposition
(`chi-helium-4-h12-at-q0-50dps.witness.json`, convention `colour-weighted-averaged-crossing` = the
canonical colour-weighting + convention-D per the 2026-08-15 owner ruling), the H₁₂ Frobenius
weights show **exact two-row dominance**:

- **Nonzero (7 blocks, all ≤ 2 rows):** `[12]`, `[11,1]`, `[10,2]`, `[9,3]`, `[8,4]`, `[7,5]`, `[6,6]`.
- **Zero (70 blocks, all > 2 rows):** including the **alternating channel `[1¹²]` with `y = 0` exactly**, and `[2⁶]`.

The CPT-doubling mechanism doubles the density *by populating the alternating antiparticle channel*.
That channel carries **zero** colour-weighted Frobenius mass — there is nothing to double. So
`frobenius-packing-density.md`'s "derives ρ_F without tuning" is **refuted under the canonical
convention** (it is a convention-C-frame / pre-colour-weighting artifact), and the authoritative
"not closed" status is correct.

## Sharpened open problem

ρ_F(⁴He)=2 loses its one corpus candidate mechanism. Any derivation must live **inside the two-row
stratum** (`[12] … [6,6]` — the only blocks with nonzero colour-weighted mass), not in an alt-block
CPT doubling. And the target is a rounded empirical prefactor: data-implied `ρ_F = B_AME/(m_e·A·8G) =
1.889`, while the "natural" categorical candidates overshoot — integer `2`: +5.9%; `[2]_q ≈ 2.011`:
+6.4%; `2cos(π/3) = 1`: −47%. None matches 1.889 cleanly; the ~6% residual is attributed (he4-nu-sdp
audit) to Coulomb + `A·8G` being a magic-volume proxy.

**Recommendation:** re-scope `frobenius-packing-density.md`'s "derives … without tuning" claim to
"a candidate CPT mechanism, refuted under the canonical colour-weighted convention (the alt block is
empty)"; the ρ_F prefactor remains an open input hypothesis, to be derived (if at all) from the
two-row stratum. Scope-(a): the mechanism is tested and shown structurally unable; ρ_F=2 itself is
not excluded by every possible route.
