import QOU.QBeta.GammaGammaLeptonPair

/-!
# Gluon loops attached to the nucleon by the γγ rule (issue #8833)

A γγ word on `n` strands closes to `c` components with `n + c` even
(`gammaGamma_components_parity`). If the three quark strands close to three components and
the remaining strands close to `g` gluon loops, then `n + 3 + g` is even. On five strands with
one or two gluon loops this forces two: the two gluon strands close into two separate loops
(`five_strands_two_gluon_loops`). On four strands the one gluon strand is one loop, as it
must be (`four_strands_one_gluon_loop`).
-/

namespace QOU.QBeta.GluonLoopParity

open QOU.Mass.GammaGammaWordSelection QOU.QBeta.GammaGammaLeptonPair

/-- On `n` strands, three quark components plus `g` gluon loops forces `n + 3 + g` even. -/
theorem gluon_loops_parity {n g : ℕ} {w : Word} (hw : GammaGammaWord w) (hr : InRange n w)
    (hc : numComponents (wordPerm n w) = 3 + g) : Even (n + 3 + g) := by
  have := gammaGamma_components_parity hw hr
  rw [hc, ← add_assoc] at this
  exact this

/-- On five strands with three quark components, the gluon strands form an even number of
loops; with two gluon strands (one or two loops) that number is two. -/
theorem five_strands_two_gluon_loops {g : ℕ} {w : Word} (hw : GammaGammaWord w)
    (hr : InRange 5 w) (hc : numComponents (wordPerm 5 w) = 3 + g) (hg1 : 1 ≤ g)
    (hg : g ≤ 2) : g = 2 := by
  have h := gluon_loops_parity (n := 5) hw hr hc
  rcases h with ⟨k, hk⟩
  have hk' : 8 + g = k + k := by simpa [Nat.add_assoc] using hk
  omega

/-- On four strands with three quark components, there is an odd number of gluon loops. -/
theorem four_strands_one_gluon_loop {g : ℕ} {w : Word} (hw : GammaGammaWord w)
    (hr : InRange 4 w) (hc : numComponents (wordPerm 4 w) = 3 + g) (hg : g ≤ 1) :
    g = 1 := by
  have h := gluon_loops_parity (n := 4) hw hr hc
  rcases h with ⟨k, hk⟩
  have hk' : 7 + g = k + k := by simpa [Nat.add_assoc] using hk
  omega

end QOU.QBeta.GluonLoopParity
