-- Ref: [manuscript] docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md
--      §1 "The closed form: B_sym is an additive linear chain".
--
-- The log standard-part binding
--   B_sym(Z,N) = α · ln( tr_M(free) / tr_M(atom) )
-- is *exactly* additive over the (A−1)-bond chain of `atom_braid_word_3A`,
-- because each inter-nucleon crossing sits on a distinct Hecke generator,
-- so the per-knot trace factorises multiplicatively over the bond
-- positions:
--   tr_atom = tr_free · (tr_pp/tr_free)^{n_pp}
--                     · (tr_pn/tr_free)^{n_pn}
--                     · (tr_nn/tr_free)^{n_nn},
-- with (n_pp, n_pn, n_nn) = (Z−1, 1, N−1).  This file formalises the
-- algebraic content of that additivity: GIVEN the multiplicative
-- factorisation (the structural "distinct-generator" input verified to
-- the 50-dps floor in the audit), the log-binding is the additive
-- chain sum.  The proof is `Real.log` algebra; it depends on no open
-- conjecture (the factorisation is the explicit hypothesis).

import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace QOU.HadronicMass

open Real

/--
**Linear-chain additivity of the log standard-part binding.**

Let `tr_free, tr_pp, tr_pn, tr_nn` be the (positive) per-knot Markov
traces of the free nucleon and of the single p-p / p-n / n-n bonded
sub-braids, and let `tr_atom` be the trace of the full atom braid.  If
the atom trace factorises multiplicatively over the bond chain (the
distinct-generator structural fact of `atom_braid_word_3A`), then the
log-binding `log (tr_free / tr_atom)` is the additive sum of the
per-bond log factors `log (tr_free / tr_X)` weighted by their counts.

For a nucleus `(Z, N)` the bond counts are `n_pp = Z-1`, `n_pn = 1`,
`n_nn = N-1`, so this is exactly
`B_sym/α = (Z-1)·L_pp + L_pn + (N-1)·L_nn` of the audit's §1 closed form.
-/
theorem b_sym_chain_additive
    (tr_free tr_pp tr_pn tr_nn tr_atom : ℝ)
    (hfree : 0 < tr_free) (hpp : 0 < tr_pp) (hpn : 0 < tr_pn) (hnn : 0 < tr_nn)
    (n_pp n_pn n_nn : ℕ)
    (hfact : tr_atom = tr_free
        * (tr_pp / tr_free) ^ n_pp
        * (tr_pn / tr_free) ^ n_pn
        * (tr_nn / tr_free) ^ n_nn) :
    Real.log (tr_free / tr_atom)
      = (n_pp : ℝ) * Real.log (tr_free / tr_pp)
      + (n_pn : ℝ) * Real.log (tr_free / tr_pn)
      + (n_nn : ℝ) * Real.log (tr_free / tr_nn) := by
  have hpp' : (tr_pp / tr_free) ^ n_pp ≠ 0 := by positivity
  have hpn' : (tr_pn / tr_free) ^ n_pn ≠ 0 := by positivity
  have hnn' : (tr_nn / tr_free) ^ n_nn ≠ 0 := by positivity
  have hatom : 0 < tr_atom := by rw [hfact]; positivity
  -- expand log (tr_free / tr_atom) using the factorisation
  rw [hfact, Real.log_div (ne_of_gt hfree) (by positivity),
      Real.log_mul (by positivity) hnn',
      Real.log_mul (by positivity) hpn',
      Real.log_mul (ne_of_gt hfree) hpp',
      Real.log_pow, Real.log_pow, Real.log_pow,
      Real.log_div (ne_of_gt hpp) (ne_of_gt hfree),
      Real.log_div (ne_of_gt hpn) (ne_of_gt hfree),
      Real.log_div (ne_of_gt hnn) (ne_of_gt hfree),
      Real.log_div (ne_of_gt hfree) (ne_of_gt hpp),
      Real.log_div (ne_of_gt hfree) (ne_of_gt hpn),
      Real.log_div (ne_of_gt hfree) (ne_of_gt hnn)]
  ring

/--
**Scaled form** (multiply by the Archimedean unit `α = E₀`): the binding
energy `B_sym = α · log (tr_free / tr_atom)` is additive over the chain
with per-bond bindings `b_X = α · L_X`.  Immediate corollary of
`b_sym_chain_additive`.
-/
theorem b_sym_chain_additive_scaled
    (α tr_free tr_pp tr_pn tr_nn tr_atom : ℝ)
    (hfree : 0 < tr_free) (hpp : 0 < tr_pp) (hpn : 0 < tr_pn) (hnn : 0 < tr_nn)
    (n_pp n_pn n_nn : ℕ)
    (hfact : tr_atom = tr_free
        * (tr_pp / tr_free) ^ n_pp
        * (tr_pn / tr_free) ^ n_pn
        * (tr_nn / tr_free) ^ n_nn) :
    α * Real.log (tr_free / tr_atom)
      = (n_pp : ℝ) * (α * Real.log (tr_free / tr_pp))
      + (n_pn : ℝ) * (α * Real.log (tr_free / tr_pn))
      + (n_nn : ℝ) * (α * Real.log (tr_free / tr_nn)) := by
  rw [b_sym_chain_additive tr_free tr_pp tr_pn tr_nn tr_atom hfree hpp hpn hnn
        n_pp n_pn n_nn hfact]
  ring

end QOU.HadronicMass
