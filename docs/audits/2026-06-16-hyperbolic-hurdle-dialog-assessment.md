# "Hyperbolic hurdle" dialog assessment — what (if anything) is actionable

**Date:** 2026-06-16
**Branch:** `claude/laughing-brahmagupta-e58uff`
**Trigger:** external dialog pitching a "separation of variables / addition
theorem" attack on the QOU hyperbolic-volume compute — by analogy with the
two-center quantum-mechanics problem (H₂⁺-style prolate-spheroidal
separation, $\operatorname{sech}(x\pm c)$ integrands, an "orthogonal basis"
$P_\lambda^\mu$, and a Jacobi/Legendre addition theorem for zonal spherical
functions).
**Audience:** anyone evaluating whether the dialog's "addition theorem"
should land in the hyperbolic-volume compute, the Wedderburn/Frobenius
decomposition, or the per-isotope binding combiner.
**Bottom-line up front:** the dialog has the right *shape* (a categorical
decomposition + an addition/fusion theorem + a two-center gluing) but
attaches it to the wrong objects. The correct QOU translation is: the
orthogonal basis is the irreducible characters $\chi_\lambda$ (not
$P_\lambda^\mu$); the addition theorem is the $q$-Littlewood–Richardson /
fusion rule in $\mathbf H_n(q)$ (whose $q\to1$ archimedean shadow *is* the
Jacobi/Legendre addition theorem the dialog names); and the **only genuine
two-center problem in QOU** is the Borromean-tower / operator-valued
branching combiner for per-isotope binding (Subgoal-1, Track B). Wiring
①/② into the hyperbolic-volume compute is the **dilog re-pitch failure
mode** again — the electron knot is the trefoil $T_{2,3}$, which is
Seifert-fibered and non-hyperbolic, so there is no $\operatorname{sech}$
integrand to separate. The one place ③ is real is sketched concretely in
§ "Going deeper on ③" below.

## What the dialog proposed

The dialog framed the QOU compute as a "hyperbolic hurdle" and pitched the
classical two-center toolkit against it:

1. **Separation of variables.** Re-coordinatize the hyperbolic-volume /
   mass integral so it separates the way the H₂⁺ molecular-ion Schrödinger
   equation separates in prolate spheroidal coordinates.
2. **An orthogonal basis $P_\lambda^\mu$.** Expand in associated-Legendre /
   Jacobi-type functions $P_\lambda^\mu$ as the "natural orthogonal basis"
   of the problem.
3. **A $\operatorname{sech}(x\pm c)$ integrand.** Treat the two-center
   structure as two displaced $\operatorname{sech}$ potentials at $\pm c$,
   so the cross term is handled by a translation/addition.
4. **A Jacobi/Legendre addition theorem.** Use the classical addition
   theorem for zonal spherical functions to recombine the two centers into
   a single closed form.

## The correct QOU translation

The dialog's three load-bearing pieces each map onto a real QOU object —
but a *different* one than the pitch names.

| # | Dialog object | Correct QOU object | Why |
|---|---------------|--------------------|-----|
| ① | orthogonal basis $P_\lambda^\mu$ | **irreducible characters $\chi_\lambda$** (orthogonal under the Markov/Frobenius pairing) | The decomposition that is actually orthogonal in QOU is the Wedderburn/Frobenius one, $\operatorname{tr}_M(\beta)=\sum_{\lambda\vdash n} y_\lambda\,\chi_\lambda(\beta)$; the $\chi_\lambda$ are orthogonal under the Frobenius/Markov inner product, not the $P_\lambda^\mu$. |
| ② | addition theorem (Jacobi/Legendre) | **$q$-Littlewood–Richardson / fusion rule** for the product in $\mathbf H_n(q)$ | The "addition" that QOU needs is the rule for the product/coproduct of two Wedderburn blocks; its $q\to1$ archimedean shadow *is* the classical Jacobi/Legendre addition theorem for zonal spherical functions. The explicit $q$-polynomial bridge is the Koornwinder / Macdonald–Askey–Wilson family ([`koornwinder1990`](../../content/schema/references.ts), [`macdonald1995`](../../content/schema/references.ts) — both already in `references.bib`), and AGENTS.md §7b already says "non-symmetric Macdonald evaluation under the Observation Frame ($\tau$)." |
| ③ | two-center / $\operatorname{sech}$ separation | **Borromean-tower / operator-valued branching combiner** for per-isotope binding (Subgoal-1, Track B) | The genuine "two-center" problem in QOU is gluing an $(A{-}1)$-nucleon inner braid to an outer nucleon block at an interface operator. The pre-archimedean "addition theorem" there is a branching/fusion coefficient ($q$-LR), **not** a new continuum coordinate scheme. |

The structural error is identical to the KLR dialog
([`2026-05-30-klr-dialog-assessment.md`](2026-05-30-klr-dialog-assessment.md)):
a real categorical mechanism gets re-expressed in an *archimedean/analytic*
register (special functions, separable PDEs) and then proposed as if the
analytic register were where the compute lives. It is not — the compute
lives pre-$\tau$, in $\mathbf H_n(q)$.

## Mathematical assessment

### What is correct (textbook)

- The classical two-center problem (H₂⁺, prolate spheroidal coordinates)
  *does* separate, and zonal spherical functions *do* satisfy a
  Jacobi/Legendre addition theorem.
- There *is* an "addition theorem" in the QOU substrate — the
  Littlewood–Richardson / fusion rule is exactly the statement of how
  $V_\xi\otimes V_\nu$ decomposes into $\bigoplus_\lambda
  (V_\lambda)^{\oplus c^\lambda_{\xi\nu}}$, and its $q$-deformation governs
  the product in $\mathbf H_n(q)$.
- The $q\to1$ limit of the $q$-LR fusion coefficients *does* reduce to the
  classical zonal-spherical-function addition theorem the dialog names —
  the dialog correctly identifies the archimedean shadow, just inverts the
  direction of the bridge.

### What is wrong or misapplied

1. **Wrong orthogonal basis.** $P_\lambda^\mu$ is the orthogonal basis of
   the *separated archimedean PDE*. The orthogonal basis of the QOU
   decomposition is $\{\chi_\lambda\}$ under the Frobenius/Markov pairing.
   These coincide only in the $q\to1$ archimedean image, which is
   *downstream* of $\tau$ — not where the trace is computed.

2. **There is no $\operatorname{sech}$ integrand to separate.** This is the
   load-bearing error, and it is the **dilog re-pitch failure mode** in new
   clothes. The hyperbolic volume in QOU is **not** an integral of a smooth
   $\operatorname{sech}(x\pm c)$ kernel over a continuum. It is a *discrete*
   Lobachevsky / Bloch–Wigner sum over ideal tetrahedra:
   $\operatorname{Vol}(K)=\sum_j D(z_j)$ with $D$ the Bloch–Wigner
   dilogarithm and $z_j$ the tetrahedral shape parameters. There is no
   $x\pm c$ displacement, no separable PDE, and no continuum coordinate to
   factor.

3. **The electron knot is non-hyperbolic.** The electron knot ansatz is the
   trefoil $T_{2,3}$, which is Seifert-fibered, hence **non-hyperbolic**:
   its complement carries no complete hyperbolic structure, every
   tetrahedral shape degenerates, and $D(z)=0$ identically. So even the
   discrete sum is zero — there is nothing for a two-center separation to
   act on. (Same point as the KLR audit's §"Trefoil is not hyperbolic" and
   the recurrent Bloch–Wigner/dilog-transcendence failure mode flagged in
   AGENTS.md §7b.) Wiring ①/② into the hyperbolic-volume compute therefore
   produces a "$0=0$ separation" — formally consistent, physically empty.

4. **Mass-formula register.** Any version of the pitch that ends in
   "$m = m_0\cdot(\text{separated special function})$" reintroduces the
   purged $\lambda_{\text{scale}}$ / `Geom_full` wrapper. The canonical
   formula is $m(K)=m_e\cdot\operatorname{Vol}(K)\cdot\rho(K)/\hbar_q^2$,
   a single per-knot evaluation; there is no separate $m_0$ and no
   separable analytic factor (AGENTS.md "Critical framing — mass formula").

### Critical-distance flag

> If anyone wires ①/② into the hyperbolic-volume compute, it is the dilog
> re-pitch failure mode again. $\operatorname{Vol}$ is a discrete
> Lobachevsky/Bloch–Wigner sum over ideal tetrahedra, and the electron knot
> is the trefoil $T_{2,3}$ (Seifert-fibered, non-hyperbolic $\Rightarrow
> D(z)=0$). There is no $\operatorname{sech}(x\pm c)$ integrand to
> separate.

This is recorded so the next agent who meets a "separate the hyperbolic
integral" pitch can short-circuit it: **check whether the knot is
hyperbolic first** (trefoil and other torus/Seifert-fibered knots are
not), and **check whether the volume is an integral or a finite
Bloch–Wigner sum** (it is always the latter in QOU). Either check kills the
separation pitch on the electron knot in one line.

## Going deeper on ③ — the Borromean combiner's fusion-coefficient "addition theorem"

This is where the dialog's intuition is genuinely actionable. The only
honest "two-center" problem in QOU is the per-isotope binding combiner: an
$A$-nucleon atom whose Markov trace must be assembled from smaller braids.
Below is the concrete fusion-coefficient ("addition theorem") for the
tower, drawn from the existing operator-valued combiner
[`canonical_tr_m_via_branching.py`](../../computations/canonical_tr_m_via_branching.py).

### The two centers and the gluing operator

The canonical $A$-nucleon braid factorizes as

$$
\beta_{\text{atom}}
  = \beta_{p}^{Z}\cdot I_{1,2}\cdot \beta_{n}^{N}\cdot I_{2,3}
    \cdots I_{A-1,A}\cdot \beta_{\text{block }A},
$$

with each $\beta_{\bullet}$ a single-nucleon intra-block at $\mathbf H_3$
and each $I_{k,k+1}$ an **inter-nucleon interface**. Peeling the outermost
interface splits the $n=3A$ strands into an inner "center" of $n-3$ strands
(the $(A{-}1)$-nucleon prefix) and an outer "center" of $3$ strands (the
last nucleon block). This is the literal two-center decomposition the
dialog is reaching for — but the centers are **Wedderburn blocks
$V_\xi\otimes V_\nu$**, not spatial foci at $\pm c$.

### The addition theorem (operator-valued Wenzl branching)

The character on the glued braid is given by the operator-valued Wenzl
1988 branching identity:

$$
\chi^\lambda\!\left(W_{\text{inner}}\cdot I\cdot \beta_{\text{block}}\right)
  = \sum_{\substack{\xi\,\vdash\,n-3\\ \nu\,\vdash\,3}}
      c^{\lambda}_{\xi\nu}\;
      \operatorname{Tr}_{V_\xi\otimes V_\nu}\!\Big(
        A^{\lambda}_{\xi\nu}(I)\cdot
        \big(\rho_\xi(W_{\text{inner}})\otimes\rho_\nu(\beta_{\text{block}})\big)
      \Big).
$$

Reading off the dictionary:

| Two-center role | QOU object | Where |
|-----------------|------------|-------|
| "orthogonal basis" | irreducible characters $\chi^\lambda$, $\lambda\vdash 3A$ | the $\sum_\lambda$ Wedderburn sum |
| "addition / fusion coefficient" | $q$-Littlewood–Richardson coefficient $c^\lambda_{\xi\nu}$ | multiplicity of $V_\lambda$ in $V_\xi\otimes V_\nu$ |
| "inner center" | $\rho_\xi(W_{\text{inner}})$, the $(A{-}1)$-prefix block | recursive (Track B) |
| "outer center" | $\rho_\nu(\beta_{\text{block}})$, the last nucleon at $\mathbf H_3$ | base case (dim $\le 2$) |
| "two-center coupling kernel" | the **interface operator** $A^\lambda_{\xi\nu}(I)$ | replaces the $\operatorname{sech}$ cross term |

The coefficient $c^\lambda_{\xi\nu}$ *is* the addition theorem: it is the
fusion rule for the product of two Wedderburn blocks, the pre-archimedean
object whose $q\to1$ shadow is the Jacobi/Legendre addition theorem the
dialog names. The interface operator $A^\lambda_{\xi\nu}(I)$ carries the
$q$-deformation of the cross term — the genuine content of "how the two
centers talk," and the thing that has no $\operatorname{sech}$
representation.

### The Markov trace then closes by the standard Wedderburn sum

$$
\operatorname{tr}_M(\beta_{\text{atom}})
  = \sum_{\lambda\,\vdash\,3A} y_\lambda\,\chi^\lambda(\beta_{\text{atom}}),
$$

with $y_\lambda$ the Jones–Markov weights. The combiner unwinds the inner
$\rho_\xi(W_{\text{inner}})$ recursively — at $A=2$ the inner is a single
$\mathbf H_3$ nucleon (base case); at $A\ge3$ it is itself a Wenzl branching
of the $(A{-}1)$-nucleon prefix. This recursive $\rho_\xi$ is exactly
**Track B**.

### Status — where the addition theorem closes and where it doesn't

| $A$ | inner level | interface extract | closes? |
|-----|-------------|-------------------|---------|
| $A=2$ (deuteron) | $\mathbf H_3$ single nucleon | $\mathbf H_6$ $pn$ — **full rank** | **YES** — operator-valued branching matches `markov_peel` to $7\times10^{-15}$ |
| $A\ge3$ (T, ³He, ⁴He, …) | $\mathbf H_6{+}$ inner | $\mathbf H_9{+}$ — **rank-deficient** | **NO** — the fitted $A^\lambda_{\xi\nu}$ are min-norm least-squares solutions over an $\mathbf H_3$ test family, **not universal interface operators** |

The blocker is documented in
[`2026-05-18-recursive-rho-xi-blocked-by-underdetermined-extracts.md`](2026-05-18-recursive-rho-xi-blocked-by-underdetermined-extracts.md):
at $\mathbf H_9$ a partition like $\lambda=[4,3,1,1]$ has
$n_{\text{unknowns}}=3390$ but the extract has rank $66$. The least-squares
$A$ reproduces $\chi^\lambda$ for the $\mathbf H_3$ single-nucleon test
words it was fit on, but predicts the wrong $\chi^\lambda$ when the inner is
a 2-nucleon deuteron at $\mathbf H_6$ — a $21$–$42\%$ error on T and ³He.
**The addition theorem is exact; the cached coupling kernel
$A^\lambda_{\xi\nu}$ is under-determined for $A\ge3$.**

(Production for $A\ge3$ therefore bypasses the combiner entirely and uses
the lossless fine-Bratteli transfer matrix
`tr_m_atom_via_transfer.tr_m_atom_zn` — $\sum_{\lambda\vdash3A} y_\lambda
\chi^\lambda$ over all $p(3A)$ partitions at 50 dps in one sweep, $\sim$5000×
the `markov_peel` symbolic path. The combiner is retained as the $A=2$ path
and as a structural cross-check.)

### What "making the addition theorem universal" concretely requires

The fix is to make $A^\lambda_{\xi\nu}(I)$ **universal by construction**
rather than fitted — i.e. derive it analytically from the Hoefsmit /
seminormal embedding $V_\lambda\hookrightarrow V_\xi\otimes V_\nu$ rather
than least-squares it from test words. This is closure path **(b)** of the
2026-05-18 blocker audit:

1. **Compute the $q$-LR coefficients $c^\lambda_{\xi\nu}$ directly**
   (already available via `lr_coefficients.get_lr_table`) — this is the
   exact "addition theorem," and it is *not* the bottleneck.
2. **Reconstruct the interface operator $A^\lambda_{\xi\nu}(I)$ in
   operator form** from Wenzl's 1988 explicit branching matrices for the
   embedding $V_\lambda\hookrightarrow V_\xi\otimes V_\nu$, so it is the
   same matrix for *any* inner family (single nucleon, deuteron, …), not
   just the $\mathbf H_3$ test set. Estimated $\sim$500 LOC + verification
   against the validated $A=2$ deuteron.
3. **Verify universality** by re-deriving T, ³He, ⁴He through the operator
   form and matching the transfer-matrix reference to $\sim10^{-15}$.

This is the productive, *non*-$\Delta_\lambda$-gated continuation of Track B
— and it is the only place the dialog's "two-center addition theorem"
intuition does real work. It is a **branching/fusion problem in
$\mathbf H_n(q)$, not a continuum coordinate scheme**, and it touches the
hyperbolic-volume compute nowhere.

## What this audit does NOT endorse

- Does **not** endorse re-coordinatizing the hyperbolic-volume compute. The
  volume is a finite Bloch–Wigner sum; the electron knot (trefoil) is
  non-hyperbolic ($D(z)=0$). There is no integrand to separate.
- Does **not** endorse $P_\lambda^\mu$ as the QOU orthogonal basis. The
  orthogonal basis is $\{\chi_\lambda\}$ under the Frobenius/Markov
  pairing.
- Does **not** introduce a new closed form, a new constant, or a new fit.
  The $q$-LR coefficient and the Wenzl interface operator are existing
  categorical objects; the work is to compute $A^\lambda_{\xi\nu}$
  analytically, not to fit it.

## Cross-references

- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) §Refutations item 4 — the **period / z-Habiro axis** (cyclotomic-Galois, `Li₃(ζ₅)`) is orthogonal to the q-side keystone coupling; a period identity is not a keystone constraint. Same archimedean-re-register trap this audit flags for the `sech`/separation pitch — check the axis (period/z vs coupling/q) before treating any Galois fact as keystone-bearing.
- [`docs/audits/2026-05-30-klr-dialog-assessment.md`](2026-05-30-klr-dialog-assessment.md) — sibling dialog assessment; same "archimedean re-register of a categorical mechanism" failure mode; trefoil-non-hyperbolic point.
- [`docs/audits/2026-05-18-recursive-rho-xi-blocked-by-underdetermined-extracts.md`](2026-05-18-recursive-rho-xi-blocked-by-underdetermined-extracts.md) — why the $A\ge3$ interface extracts are rank-deficient; closure paths (a)/(b)/(c)/(d).
- [`docs/audits/2026-05-25-track-b-r5-full-sdp-extension-design.md`](2026-05-25-track-b-r5-full-sdp-extension-design.md) — Track B R5-full design; α-cluster cascade; Subgoal-1 leverage.
- [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — Track A vs Track B split; why Track B (recursive $\rho_\xi$) is the non-$\Delta_\lambda$-gated path.
- [`computations/canonical_tr_m_via_branching.py`](../../computations/canonical_tr_m_via_branching.py) — the operator-valued Wenzl branching combiner (the concrete "addition theorem").
- [`computations/substrate/lr_coefficients.py`](../../computations/substrate/lr_coefficients.py) — $q$-Littlewood–Richardson table `get_lr_table` (the $c^\lambda_{\xi\nu}$).
- [`content/quantum-observable-universe/braids-and-knots/f-bor-borromean-observable.md`](../../content/quantum-observable-universe/braids-and-knots/f-bor-borromean-observable.md) — Borromean observable content block.
- AGENTS.md §7b — Symmetric-crystal techniques; non-symmetric Macdonald under $\tau$; recurrent dilog/Bloch–Wigner failure mode.
- AGENTS.md "Critical framing — mass formula" — why $m=m_e\cdot\operatorname{Vol}(K)\cdot\rho(K)/\hbar_q^2$ has no separable $m_0$.
- `references.ts`: [`koornwinder1990`](../../content/schema/references.ts), [`macdonald1995`](../../content/schema/references.ts) — the $q$-polynomial bridge (Koornwinder / Macdonald–Askey–Wilson).
