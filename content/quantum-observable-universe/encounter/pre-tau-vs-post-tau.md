**Reading.** The encounter chapter is the place in the
manuscript where the Archimedean wall is most easily crossed by
accident.  The hyperbolic-volume language and the
$q$-Pochhammer language *coincide* under
[$\tau_{\mathrm{arch}}$](#def:archimedean-realization-functor),
which can lead an author to write a derivation step in one
language while it logically belongs to the other.  This remark
states the discipline once.

**The wall.**  Every derivation step in the manuscript belongs
to exactly one of two registers:

| Register      | Coefficient ring                                                  | Operative invariants                  | Examples                              |
|---------------|-------------------------------------------------------------------|---------------------------------------|---------------------------------------|
| **Pre-$\tau$**  | $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ (or its $z$-Habiro completion) | Hecke spectra; Markov traces; LP/SDP feasibility | Confinement SDP; Gröbner--Shirshov reductions |
| **Post-$\tau$** | $\mathbb{R}$ (or $\mathbb{C}$) via $\tau_{\mathrm{arch}}$        | Hyperbolic volumes; thimble depths; mass eigenvalues | Mostow rigidity; PL thimble flow; Bloch--Wigner $D(z)$ |

The functor $\tau_{\mathrm{arch}}$ is the **only** legal way to
cross from the left column to the right.  Specifically:

* No derivation step on the left may use a value from the right
  (e.g. a hyperbolic volume) as input.  Such values are *outputs*
  of $\tau_{\mathrm{arch}}$, not algebraic data.

* No derivation step on the right may claim algebraic-side
  identities (e.g. Hecke relations) — those hold in $R$ before
  $\tau_{\mathrm{arch}}$ is applied.  After $\tau_{\mathrm{arch}}$
  one has only the realised real numbers.

* When a numerical equality bridges the two sides — e.g. the
  mass formula
  $\tau_{\mathrm{arch}}(\mathfrak{m}^{\mathrm{trans}}(\varrho_K))
  = \rho_q \cdot \mathrm{Vol}_{\mathrm{hyp}}(U \setminus K)$ — it
  is a statement *about the functor*, not a derivation step on
  either side alone.  Numerical comparisons of such bridges with
  experimental data must use $\approx$ unless an explicit error
  term is present.

**Motivic shorthand.**  The cleanest algebraic-side home for
encounter data is the **$z$-Habiro completion**
$\hat{\mathbb{Z}}[q^{\pm 1}][z]_z$: it allows one to treat the
poles of the quantum dilogarithm $\Phi_q$ algebraically — as
quotients of cyclotomic ideals — rather than as divergent
analytic limits.  Under $\tau_{\mathrm{arch}}$ these algebraic
poles realise as the cusps of the hyperbolic triangulation
([pole-to-cusp bijection](#conj:algebraic-geometric-dilog-equivalence)).

**Self-check.**  When writing or reviewing an encounter-side
derivation, ask:

1. *Which column does my coefficient ring live in?*
2. *Have I used any data from the other column without going
   through $\tau_{\mathrm{arch}}$?*
3. *Are bridging equalities written with $\approx$ (or with an
   explicit error term)?*

If any answer is wrong, fix the derivation; do not hide the
crossing in prose.
