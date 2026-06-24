The Hoefsmit He-4 channel fixed the selector direction as a single
Markov-trace collapse, $T_\beta = S\cdot\mathbf{1}$
([`prop:t-beta-markov-frobenius-collapse`](#prop:t-beta-markov-frobenius-collapse)).
That collapse leaves one object to identify: the fibre-level Habiro
element $F(q)$ whose $q$-Taylor coefficients are the precision-ladder
$c_k$ of the $\mathfrak{Q}_\beta$ series
([`sec:mass-algebraic-complex-volume-ladder`](#sec:mass-algebraic-complex-volume-ladder)).
The question this section settles is not *what $F$ is* — that remains the
open keystone — but *which structural constraints any candidate $F$ must
satisfy before it is worth evaluating*. This is the formalize-first
discipline applied to the decay side: prove the invariants that prune the
hypothesis class, then search only the survivors.

Four gates do the pruning. A candidate generating function must have its
pole at the substrate radius
([`prop:q-beta-radius-of-convergence-gate`](#prop:q-beta-radius-of-convergence-gate)),
must be bar-even under $q\mapsto q^{-1}$ so the integer-$u$ ladder is
clean ([`prop:q-beta-bar-even-kernel-invariant`](#prop:q-beta-bar-even-kernel-invariant)),
must reproduce the classical shadows $c_2\to-1$, $c_3\to J_{\mathrm{Hopf}}(1)=-2$
at $q=1$ ([`prop:q-beta-q-eq-one-shadow-gate`](#prop:q-beta-q-eq-one-shadow-gate)),
and must carry a magnitude consistent with the target observable
([`prop:q-beta-direction-sanity-gate`](#prop:q-beta-direction-sanity-gate)).
The four bundle into one parametric typeclass
([`prop:q-beta-bar-even-kernel-typeclass`](#prop:q-beta-bar-even-kernel-typeclass)),
with the mass-side analogue assembled alongside
([`prop:mass-side-kernel-formalize-first-gates`](#prop:mass-side-kernel-formalize-first-gates)).
Between the gates sits the recursion machinery itself: the depth-$d$
linear recursion the $c_k$ inherit from the Habiro $q$-difference kernel
([`prop:q-beta-c-k-recursion-from-habiro-q-difference`](#prop:q-beta-c-k-recursion-from-habiro-q-difference)),
the bridge to the per-block $z$-recursion
([`prop:qbeta-z-recursion-to-ck-recursion-bridge`](#prop:qbeta-z-recursion-to-ck-recursion-bridge)),
and the exact rational forms read off at the silver ratio
([`prop:qbeta-c8-c10-silver-rationals`](#prop:qbeta-c8-c10-silver-rationals)).

The output is a verdict matrix, not a closed form. The gates settle which
coefficients are structural and which remain calibration-anchored: $c_2=-1$
is proved Taylor-exact, $c_3\approx-2$ is a near-match with a few-percent
cross-anchor swing, and $c_k$ for $k\ge4$ are fit to the CODATA residual
rather than derived. Nothing in this section is wired to production — the
$c_k$ stay cal-anchored, and the categorical construction of $F(q)$ that
would turn the recursion into a parameter-free predictor is deferred to the
brane-tower (contraction) limit where the binding $\Delta_\lambda$ ladder
also lives. What the gates buy is a sharper statement of the open problem:
any future $F$ that fails a gate is excluded without a numerical search.
