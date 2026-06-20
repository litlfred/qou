---
# e2nf
title: Level-6 electron shell — σ_F dual, shell-closure fix, 2n² gap
status: in_progress
type: task
priority: normal
created_at: 2026-06-16T02:16:00Z
updated_at: 2026-06-20T03:00:00Z
---

Branch `claude/zealous-hypatia-05xyp9` → PR #2348. Picked up a stalled
electron-shell / atomic-mass discussion; tracked via docs/audits + the
low-isotope-mass-anatomy ledger before adopting this bean.

## Delivered

- **Level-6 atom→electron mass** (`computations/atom_electron_mass.py`):
  `m_atom = m_sym + Z·m_e − E_e_binding` vs AME atomic; ¹H exact; residual is
  ~100% nuclear B_sym. e-Hartree scale is canonical (`E_HARTREE_EV=27.21 eV`),
  correcting a prior 25-MeV/electron blunder.
- **SDP-capacity formalize-first correction** (`electron_shell_sdp_capacity.py`):
  "add electrons until SDP infeasible" is wrong — σ_F (dual) is monotone; the
  raw-Gram H=5/He=8 "capacity" is the excluded interlacing branch.
- **σ_F(Z) dual chain** (`electron_sigma_f_chain.py`, cvxpy cross-check) +
  **marginal demo** (`electron_sigma_f_marginal.py`).
- **Resolved a σ_F inconsistency** in `prop:shell-closure-stability` (claim 1
  monotone vs claim 2 strict-local-max) → marginal Δσ_F=I₁ peaks; σ_F monotone.
- **Coordinate §6 align**: reconciled with main's more-rigorous
  `sigma_f_electron_shell_chain.py` (8ecbbca9) + caveat (ae7e0813); made the
  noble-gas-peak LOCATION conditional on the open 2n²/Madelung derivation.
- **2n² diagnosis** (`docs/audits/2026-06-16-2n2-shell-capacity-derivation-gap.md`):
  genuinely open — 2×2 T_γe gives spin-2, not the orbital n²; needs an absent
  SO(4)/Runge-Lenz degeneracy; softened the unsupported overclaim.
- Removed a vacuous shadowing Lean stub (no-shadowing-stubs).

## Open

- [x] Rebase #2348 onto current main — done 2026-06-20: 15 commits replayed onto
      current main (0 behind); only the ledger both-appended (kept both);
      force-pushed-with-lease.
- [x] Research item resolved as a VERDICT (not a derivation): 2n² + the noble
      gases are **accept-as-input** — the framework is *two symmetries short*
      (an SO(4)/Runge-Lenz degeneracy for the orbital n²; a categorical
      screening/Madelung mechanism for the noble-gas ordering — both absent).
      Pure-2n² closes at [2,10,28,60] ≠ noble [2,10,18,36]. Audit
      `2026-06-20-2n2-noble-gas-accept-as-input-verdict.md`; fixed the
      electron-shells-hopf table mislabel (28→Ni, 60→Nd were tagged "noble gas").
- [~] CI: `staleness` check ✓ post-rebase; full content-validate + lean checks
      pending / billing-gated (validator absent locally; local sanity clean —
      balanced math, stub removed + library decl imported). Subscription surfaces
      any failure.

## Still open (genuine research, not this PR)

- [x] **(2026-06-20) 2n² constructed, owner's 'no second SU(2)' vindicated.**
      Exact (shell_capacity_chebyshev_bridge.py): [n]_q = U_{n-1}((q+q⁻¹)/2)
      (angular q-dim = cosh/bar-even); [n]_q² = Σ_{ℓ=0}^{n-1}[2ℓ+1]_q
      (q-Clebsch-Gordan self-square); 2[n]_q²|_{q=1}=2n². The (j,j) doubling is
      the self-fusion V⊗V of ONE element, not two SU(2)s. Residual conjecture:
      shell space = the self-square. Audit 2026-06-20-shell-2n2-from-self-square.
      Side-finding: shell-structure-eigenvalues.md (T^n)₂₁ Chebyshev claim wrong
      (det T=−1) — to fix.
- [x] Gap 2 (Madelung) — **TESTED 2026-06-20 (madelung_sdp_filling_order.py).**
      Result as predicted: the SDP optimiser is free (lp_dual_solver x* picks the
      min-cost orbital), BUT canonical bare T_ee gives NO ℓ-splitting (same σ
      crossing for every orbital) ⇒ closed shells stay at pure-2n² [2,10,28,60],
      NOT the noble gases [2,10,18,36]. Falsified "SDP+canonical-T_ee ⇒ Madelung".
      Audit 2026-06-20-madelung-from-sdp-falsifiable-test.md.
- [x] **STRUCTURAL try done (3', 2026-06-20).** screening ∝ [2ℓ+1]_q (angular
      q-dim, canonical T_ee weight, NO tuning) DOES rise with ℓ — right
      penetration DIRECTION — but OVERSHOOTS ~10× (s·[3]_q≈0.76 vs radial
      spacing≈0.09) ⇒ ℓ-dominated order [8,26,46,60], not n+ℓ. So the structure
      supplies BOTH ingredients but not the Madelung BALANCE.
- [x] **SYNTHESIS with #2531 (merged) 2026-06-20 — Gap-2 reduced to one number `a`.**
      Both probes converge on the ℓ-coefficient `a` in the filling key
      K(n,ℓ)=n+a·ℓ. #2531: eigenvalue-split grading gives a=−2 (wrong sign,
      anti-penetration, ruled out). #2348: bar-even q-dim [2ℓ+1]_q gives a>0
      (right sign) but overshoots +1; same object also gives the 2n² capacity
      (so capacity + penetration-sign are both bar-even). Madelung needs a=+1,
      strictly BETWEEN. Structure brackets {−2, >+1} but never pins +1 ⇒
      hitting +1 = tuning = fitting. Audit 2026-06-20-gap2-ordering-ell-coefficient-synthesis.md.
      (Corrects my earlier "radial:angular balance" framing — #2531's sign half
      sharpens it; my "~8.5×" was the z² convention, but sign-positive/>+1 robust.)
- [x] **DUALITY LEVER (owner duality question, 2026-06-20) — aufbau_eigenvalue_channel.py.**
      The ℓ-coefficient a depends on WHICH eigenvalue channel angular ℓ couples to
      (T_γe: λ₊=q₀ dominant, λ₋=−1/q₀ sub-dominant, λ₊λ₋=−1 bar-dual = D1).
      ONLY the dominant-λ₊ channel (λ₊^ℓ=q^{+ℓ}, a=+1) reproduces the empirical
      Aufbau order (4s<3d, 5s<4d…) EXACTLY; λ₋ (a=−2, #2531) and the loop-trace
      q-dim (a=+2) both diverge. The Markov/Frobenius trace is PERRON-dominated by
      λ₊ ⇒ using the pairing "correctly" (λ₊ for both radial & angular) gives
      symmetric n,ℓ → n+ℓ = Madelung. Supersedes the "balance" framing.
- [ ] **Gap-2 localized one notch finer (NOT a derivation — 2 caveats):**
      (1) a=+1 ⟺ Madelung is partly definitional; the real claim is "radial &
      angular share the dominant λ₊". (2) the Frobenius TRACE of V_ℓ is the q-dim
      ~λ₊^{2ℓ} (a=+2) because dim V_ℓ=2ℓ+1 — a FACTOR OF 2 from Madelung's λ₊^ℓ.
      Open: why does angular enter as λ₊^ℓ (open transfer, a=+1) not λ₊^{2ℓ}
      (loop-trace, a=+2)? = the 2ℓ+1→ℓ "half"/√-q-dim. Pairing poses it, doesn't
      settle it. Audit 2026-06-20-aufbau-from-dominant-eigenvalue-duality.md.
      (Capacity Gap-1: 2n² self-square, essentially derived.)

## Notes

- Audits: docs/audits/2026-06-16-{level6-atom-electron-wiring, electron-shell-sdp-
  capacity-formalize-first, sigma-f-electron-dressing-chain, shell-closure-sigma-f-
  inconsistency-resolved, 2n2-shell-capacity-derivation-gap}.md
- Ledger: docs/coordination/2026-05-24-low-isotope-mass-anatomy-ledger.md
- Bean adopted 2026-06-20 per owner ("are you using beans?"). bean-coordination
  skill redirects to folio-assistant (not in this checkout) — following observed
  file format, not the full protocol.
