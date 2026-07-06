## Proof sketch

The proof of the proposition factors into three steps:

**Step 1: Uniqueness of the Markov trace.**  For $H_n(q)$, the
trace satisfying M1 (cyclicity), M2 (Markov axiom
$\mathrm{tr}^{(n)}(x \cdot \sigma_{n-1}) = z \cdot \mathrm{tr}^{(n-1)}(x)$),
and M3 ($\mathrm{tr}(1) = 1$) is **unique** (Jones 1985, Wenzl 1988).
Any two operator-volume conventions that respect the Hecke
quadratic relation and the Markov axiom evaluate to the same
$\tau$ value on a given $\beta$.

**Step 2: All probed conventions respect $\tau$.**  Each of the
six brane-tower convention families probed in
[`conj:brane-tower-z-habiro`](#conj:brane-tower-z-habiro) §"Closure"
(scalar uniform-$k$, $\ell n_0 + k$, per-eigenvalue operator-valued,
multiplicity / Type-B-fold, pair-knot product-volume, pair-knot
Markov-trace) is a regularization of the divergent analytic $\Phi_q$
tower — none of them VARY the categorical trace
$\tau(\beta_{\mathfrak{H}})$; they only differ in how the divergent
tower is regularized.

**Step 3: $\Delta_{\mathrm{cat}}$ is convention-independent.**
From Steps 1+2: any two probed conventions yield the same
$|\tau(\beta_{\mathfrak{H}})|$ and hence the same
$\Delta_{\mathrm{cat}}(\mathfrak{H})$, regardless of which
convention is used to *evaluate* the operators in the
endomorphism algebra. $\square$

## Falsifiable predictions

1. **Convention-independence of $\Delta_{\mathrm{cat}}({}^3\mathrm{He})$.**
   Compute $|\tau(\beta_{{}^3\mathrm{He}})|$ via Hoefsmit seminormal
   (per-eigenvalue), via `markov_peel` (recursive symbolic), and via
   `tr_M_via_wenzl_bridge_mpfr` (50 dps Wenzl bridge).  All three
   should give the same $|\tau|$ to 50 dps; the resulting
   $\Delta_{\mathrm{cat}}$ should be ATOM-DEPENDENT but
   CONVENTION-INDEPENDENT.

2. **Convention-dependent regularizer dominates the brane-tower
   variation.**  The non-categorical brane-tower regularization
   contributions vary by orders of magnitude across the six canonical evaluation
   families — but their *difference from* $|\tau|$ is the same
   non-categorical regularizer.  The structural gap
   $\Delta_{\mathrm{cat}}$ should be the same across all probed
   conventions, on each atom separately.

3. **Magic-shell decomposition.**  $\Delta_{\mathrm{cat}}(Z, N)$
   should decompose as
   $\Delta_{\mathrm{cat}}(Z, N) = \Delta_0(A) + \mathbb{1}_{Z \in \mathrm{magic}} \cdot \Delta_p + \mathbb{1}_{N \in \mathrm{magic}} \cdot \Delta_n$
   with $\Delta_p = \Delta_n$ (the Z$\leftrightarrow$N symmetry constraint).  This
   is the precise content of
   `conj:magic-shell-stabilization`.
