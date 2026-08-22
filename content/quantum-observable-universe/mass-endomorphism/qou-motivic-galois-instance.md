# **QOU MotivicGaloisCharacter instance** via Habiro evaluation

The QOU brane-tower substrate carries a concrete instance of [`def:motivic-galois-character`](#def:motivic-galois-character) constructed by the Habiro evaluation map:

$$
  \mathrm{Frob}_p \;=\; f(u) \big|_{u = \zeta_{2p}}
  \;\in\; \mathbb{Z}[\zeta_{2p}].
$$

Here $f(u) = \sum_{m \geq 0} a_m(u) (u; u)_m$ represents the Habiro cyclotomic expansion of the atomic Markov trace $\mathrm{tr}_M(T_w, q)$ and $u = q^{1/2}$. The cyclotomic Pochhammer $(u; u)_m$ vanishes for $m \geq 2p$. This forces the sum to terminate after a finite number of terms.

The finite-place compatibility checks, the Lean instance, the
downstream consumers, and cross-prime coherence are recorded in
[the follow-on remark](#rem:qou-motivic-galois-instance-verification);
the per-cell $\mathrm{Frob}_p$ data appears in
[the accompanying example](#ex:qou-motivic-galois-instance-per-cell).

**Lean status (2026-08-12):** the co-located `.lean` file (which
contained a bare `axiom` laundering the perpetual obstruction into the
`MotivicGaloisCharacter` class) has been deleted.  The formalization
now lives in
`lean/QOU/LiftingDescent/MotivicPerpetualObstructionFromTrace.lean`
(Route A: prime-ideal-collapse proof, C = a₀(−1) + 2·a₁(−1), sorry-free).

**Block kind (2026-08-22):** demoted from `definition` to `remark`.  A
`definition` requires a Lean sibling, and the one this block had was the
axiom-laundering instance deleted above — so the block asserted a
formalized instance the corpus no longer carries.  It is not retargeted at
the theorems in `MotivicPerpetualObstructionFromTrace.lean`, because those
conclude `¬IsUnit (4 : ℤ)` and `¬IsUnit (−32 : ℤ)`: statements about two
integers, whose types mention neither the prime `p` nor the exception set
`S`, and whose proof terms discard both binders.  Pointing a definition at
them would record it as formalized by something that says nothing about it.
Tracked as bean `qou-lrnd`; the construction itself is unaffected and stays
witnessed by `computations/probes/habiro_frobenius_probe.py`.
