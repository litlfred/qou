import Mathlib.Tactic

/-!
# B_sym is a linear-chain (additive) binding — formalization

Formalizes the *provable structural* content of the `B_sym` linear-chain result
(`docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md`, PR #2343), per bean
`6z40`: `B_sym = α·ln(tr_free/tr_atom)` is itself a definition + empirical claim
(only `rfl`-trivial in Lean), but its **additive linear-chain decomposition** is a
theorem once the per-bond factorization is taken as the structural input.

The bound atom braid orders strands as `['p']·Z ++ ['n']·N` and places an
inter-nucleon crossing only between *adjacent* nucleons, so the chain carries
exactly

> `(Z−1)` p-p bonds · `1` p-n interface bond · `(N−1)` n-n bonds  = `(A−1)` total.

Because each crossing sits on a distinct Hecke generator, the per-knot trace
factorizes over bond positions and the log-binding is exactly additive:

    B_sym(Z,N) = α·[ (Z−1)·L_pp + L_pn + (N−1)·L_nn ],   L_X = ln(tr_free/tr_(1 X-bond)).

This file proves (i) the **bond-count combinatorics** (pure `ℕ`) and (ii) the
**additivity closed form** as a `List.sum` identity over the chain's bond
multiset. The per-bond values `L_X : Bond → R` are abstract parameters (base ring
generic `R`, per AGENTS.md §7c — the additivity is algebra, no archimedean input);
the empirical claim that this matches the actual 50-dps trace stays in the audit,
*not* asserted here. Complements
`QOU.BraidKnot.ChiralityTopologySelection` (which fixed the p-n bond counts
`chainPnBonds = 1`, `completePnBonds = Z·N`); this file gives the full
`(pp, pn, nn)` chain decomposition and its additivity.
-/

namespace QOU.BraidKnot.BsymLinearChain

/-- The three inter-nucleon bond types of the chain. -/
inductive Bond
  | pp   -- proton–proton
  | pn   -- proton–neutron (the single interface bond)
  | nn   -- neutron–neutron
deriving DecidableEq, Repr

/-- The ordered bond list of the linear chain `p^Z n^N`: `(Z−1)` adjacent p-p
bonds, the single p-n interface, then `(N−1)` adjacent n-n bonds. (`ℕ`
subtraction; the intended regime is `Z ≥ 1`, `N ≥ 1`, where the interface bond is
genuinely present.) -/
def chainBonds (Z N : ℕ) : List Bond :=
  List.replicate (Z - 1) Bond.pp ++ Bond.pn :: List.replicate (N - 1) Bond.nn

/-- **Bond-count total.** For `Z, N ≥ 1` the chain has exactly `A − 1 = Z + N − 1`
bonds — the `(Z−1) + 1 + (N−1)` decomposition. -/
theorem chain_num_bonds {Z N : ℕ} (hZ : 1 ≤ Z) (hN : 1 ≤ N) :
    (chainBonds Z N).length = Z + N - 1 := by
  simp only [chainBonds, List.length_append, List.length_cons,
    List.length_replicate]
  omega

/-- Per-type bond counts: `(Z−1)` p-p, `1` p-n, `(N−1)` n-n. -/
theorem chain_count_pp (Z N : ℕ) :
    (chainBonds Z N).count Bond.pp = Z - 1 := by
  simp [chainBonds, List.count_replicate]

theorem chain_count_pn (Z N : ℕ) :
    (chainBonds Z N).count Bond.pn = 1 := by
  simp [chainBonds, List.count_replicate]

theorem chain_count_nn (Z N : ℕ) :
    (chainBonds Z N).count Bond.nn = N - 1 := by
  simp [chainBonds, List.count_replicate]

variable {R : Type*} [CommRing R]

/-- **Additivity (the structural identity).** Summing an abstract per-bond energy
`L : Bond → R` over the chain's bond list gives the additive closed form
`(Z−1)·L_pp + L_pn + (N−1)·L_nn`. This is the log-binding factorization made
algebraic; it holds for all `Z, N` (with `ℕ`-`smul` coefficients). -/
theorem chain_binding_sum (L : Bond → R) (Z N : ℕ) :
    ((chainBonds Z N).map L).sum
      = (Z - 1) • L Bond.pp + L Bond.pn + (N - 1) • L Bond.nn := by
  simp only [chainBonds, List.map_append, List.map_cons, List.map_replicate,
    List.sum_append, List.sum_cons, List.sum_replicate]
  abel

/-- `B_sym` as the bond-weighted log-binding of the linear chain. -/
def Bsym (α : R) (L : Bond → R) (Z N : ℕ) : R :=
  α * ((chainBonds Z N).map L).sum

/-- **B_sym closed form.** `B_sym = α·[(Z−1)·L_pp + L_pn + (N−1)·L_nn]` — the
#2343 linear-chain additivity, now a theorem (given the per-bond factorization
encoded in `Bsym`). -/
theorem Bsym_closed_form (α : R) (L : Bond → R) (Z N : ℕ) :
    Bsym α L Z N
      = α * ((Z - 1) • L Bond.pp + L Bond.pn + (N - 1) • L Bond.nn) := by
  rw [Bsym, chain_binding_sum]

/-- The deuteron (`Z = N = 1`) is exactly the single p-n bond: `B_sym = α·L_pn`
(the `B_sym(²H) = b_pn = 3.890 MeV` row of the audit, structurally). -/
theorem Bsym_deuteron (α : R) (L : Bond → R) :
    Bsym α L 1 1 = α * L Bond.pn := by
  simp [Bsym_closed_form]

end QOU.BraidKnot.BsymLinearChain
