# λ_A is a fit — excised; use the per-knot Hecke density (owner ruling 2026-06-24)

**Owner ruling (litlfred, 2026-06-24).** The global Family-A linking
weight

```
λ_A = (1/4) Σ_{λ⊢4} dim_q V_λ = (3q²+4+3q⁻²)/4 = 5/2 + ¾h²  ≈ 2.5328 at q₀
```

(`_li_2_q_util.linking_weight_family_a`, re-exported as
`mass_vol_density.density_borromean` / `density_global`, consumed by
`vol_density_borromean`) is a **CODATA-implied fit**, not a derived
density. It is to be **excised**. The canonical mass density is the
**per-knot Hecke Markov trace**:

```
ρ(K) = tr_M(K) = Σ_λ y_λ χ^λ(β_K)
m(K) = m_e · Vol(𝓑₃) · tr_M(K) / ℏ_q²        (= m_e · vol_density_per_block)
```

## Why λ_A is a fit (the evidence)

- The paper-canonical density is **per-knot** `tr_M(K)`. Production
  silently substitutes the **global, knot-independent** scalar λ_A
  because the per-knot reading "looks wrong" (see below). That swap is
  the unresolved "per-block vs global / SU(2)-loss gate" (RED in
  `compare_density_readings`, ratio 2.378×).
- λ_A's constant term 5/2 is already a 2-sig-fig near-match to the value
  that round-trips m_p (λ ≈ 2.460); the q-correction ¾h² moves the
  prediction **away** from the target (+1.63% → +2.96%). A physical
  q-structure should improve, not degrade, the match.
- The "why H₄ for a 3-strand (H₃) proton" question has **no surviving
  derivation**: Bratteli induction (#1841), Markov stabilization
  (#1850), and 7 Δ_λ ansätze all refuted (audit
  `2026-06-04-three-paths-refuted-roadmap-update.md` §5: "the choice of
  H₄ is not structurally derived").

## The honest numbers (λ_A excised, per-knot density)

| | tr_M(K) @ q₀ | m(K) = m_e·Vol·tr_M/ℏ_q² | vs CODATA |
|---|--:|--:|--:|
| proton 𝓑₃ | 1.0653 | 406.3 MeV | −56.7% |
| neutron 𝓑₃ | 0.9232 | 352.1 MeV | −62.5% |

Note **m_n < m_p (inverted ordering)** and a large undershoot — the real
categorical gaps the λ_A fit was masking (+2.96% overshoot). Closing
them is the open **step-9a per-knot Vol(K) frontier**, NOT a density
refit (the "no seventh fit ansatz" gate stands).

## Hypothesis to test — refutations may be artifacts of the wrong density

Many binding / shell quadratic-correction closures were **refuted while
baselining against the global λ_A density** (uniform, and p=n-degenerate).
The per-knot density is **p≠n-distinct** (1.0653 vs 0.9232), a different
baseline. Owner flags that some of those refutations may be artifacts of
the wrong density and should be **re-examined** against per-knot `tr_M(K)`
before being treated as settled negatives. This is a hypothesis to test,
not yet established.

## Action for in-flight PRs

If your PR touches density / binding / Δ_λ / shell-corrections / mass:

1. Do **not** baseline against `λ_A` / `density_borromean` /
   `vol_density_borromean` (global). Use `vol_density_per_block` with the
   per-knot `tr_M(K)`.
2. Re-examine any refutation that used the global density; the p≠n
   per-knot baseline may flip the verdict.

## Reference implementation

`computations/mass_binding_dashboard.py::_nucleon_mass_canonical` (PR
#2662) — the dashboard now reports the per-knot Hecke-density masses
(λ_A excised), with the honest −57%/−62% undershoot shown rather than
masked.

## Scope note

This ledger records the **ruling + dashboard excision**. Excising λ_A
from the ~64 production scripts that still use `vol_density_borromean`
uniformly (per `audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md`)
is the broader follow-up — owner-sequenced, tracked here.
