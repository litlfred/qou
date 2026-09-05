---
# qou-k4oq
title: Build the Hecke algebra foundation in Lean from scratch — Mathlib has NONE
status: in-progress
type: milestone
priority: normal
created_at: 2026-09-05T07:53:31Z
updated_at: 2026-09-05T08:02:10Z
---

LAYER 1 DONE 2026-09-05, sorry-free, lean-direct exit 0 (4.0 s), zero warnings.
AXIOMS: [propext, Quot.sound] only -- NOT EVEN Classical.choice, a cleaner footprint
than the rest of this arc (the q=1 files all pull Classical.choice).

BUILT FROM SCRATCH BECAUSE MATHLIB HAS NOTHING. Measured: zero files matching
HeckeAlgebra, IwahoriHecke, QuantumGroup, BraidGroup, RMatrix, YangBaxter,
TemperleyLieb. Only GroupTheory.Coxeter. Nothing to import, nothing to build on.

LAYER 1 (this file, QOU/IwahoriHecke/HeckePresentation.lean): H_{n+1}(q) as a
RingQuot of FreeAlgebra R (Fin n), generic CommRing R with q : R-units (no R-reals,
per 7c). sigma_sq, sigma_braid, sigma_far, sigma_eigen ((sigma-q)(sigma+q^-1)=0),
sigmaUnit (explicit inverse sigma - h), skein (sigma - sigma^-1 = q - q^-1),
hParam_one + sigma_sq_of_hParam_eq_zero (q=1 degenerates to sigma^2=1), and the
UNIVERSAL PROPERTY lift / lift_sigma / algHom_ext.

The universal property is not decoration: without it the presentation is INERT. It is
what lets a representation, a trace, or any map OUT of H_{n+1}(q) be defined by naming
generator images and checking three relations. Everything in layers 2-4 goes through it.

🛑 NONTRIVIALITY IS NOT PROVED, and this is a SOUNDNESS caveat not a wishlist item.
Nothing in layer 1 shows H_{n+1}(q) != 0. A presentation whose relations collapsed
would satisfy every theorem above VACUOUSLY -- the same failure mode as a LinearMap.trace
without Module.Free (see qou-mex9). Establishing dim = (n+1)! needs the T_w BASIS
THEOREM (Bourbaki/Matsumoto: a reduced word gives a well-defined T_w independent of the
reduction), which is the deep result of the subject. Until that lands, do NOT read
layer 1 as statements about a nonzero algebra.

REMAINING LAYERS:
  2. T_w basis + length function (Matsumoto). THE hard one; unlocks nontriviality.
  3. Markov trace on H_n(q).
  4. Wedderburn / Hoefsmit partition-indexed decomposition -- what qou-mpq5 scoped as
     multi-week, and what quantum Schur-Weyl's BRAIDING half needs.
