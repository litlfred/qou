---
# qou-x4qm
title: 'GAP: three-generation structure — why three copies of each fermion; prior to CKM/PMNS'
status: todo
type: task
created_at: 2026-07-31T20:15:08Z
updated_at: 2026-08-02T00:00:00Z
---

## 2026-08-02 update (PR #4565, branch `claude/generation-bridge-2026-08-02`)

**Progress (sorry-free, `lean`-direct exit 0):** the general **forward**
harmonic law is now formalized for ALL windings, not just `{3,5,7,9}` —
`lepton_continuant_divisibility_general.lean`:
`morganVoyceB_add` (Fibonacci-polynomial addition formula) +
`morganVoyceB_dvd_of_dvd` (`a ∣ n ⟹ b_a ∣ b_n`). So *every composite
winding is a harmonic of a smaller one*; the lepton `b₃∣b₉` instance is
now a one-line corollary. Generations ⊆ odd primes, universally.

**Sub-front closed (corpus, not by me):** the naive "same continuant
divisibility at H₃ (quarks)" route is already NEGATIVE —
`QOU.Archimedean.stdRep3_M_cubed_eq_one` (sorry-free) gives `(σ₀σ₁)³ = I`
in the (2,1) rep, so the character is q-independent (period-3); the
Fibonacci pattern is H₂-specific (`t3n_binomial_pattern_probe.py`). Quark
3-generation count rides the shared winding index `n=2k+1`, not an
independent H₃ continuant.

**Sub-gaps still open:**
1. **Reverse direction** `b_a ∣ b_n ⟹ a ∣ n` (strong-divisibility /
   `gcd(b_m,b_n)=b_{gcd(m,n)}` over `Polynomial ℤ`). Would upgrade
   "generations ⊆ primes" to "generations = primes". Documented `-- GAP:`
   in the Lean file.
2. **Physical bridge** — why a harmonic (normal-form-dependent) winding
   carries no *independent* generation; plus the `net → mass` map. No
   rigorous structural argument found; not fabricated. Still the core of
   this bean.

Audit: `docs/audits/2026-08-02-generation-bridge-general-harmonic-law.md`.
