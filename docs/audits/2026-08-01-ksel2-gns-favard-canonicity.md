# KSel-2 — GNS/spectral-measure canonicity: the binding kernel as spectral measure of a canonical Jacobi operator (Favard route). Verdict: PARTIAL — the operator is derived and unique, the measure is not; the kernel convention reappears exactly as the self-adjoint-extension circle

**Date:** 2026-08-01 · **Bean:** qou-mee2 (KSel-2, zero-convention route)
**Tier:** AUDIT — scope-(a), NO FIT, nothing wired; no content block or
Lean file touched. Parallel kernel-selection agents this session:
KSel-1 (qou-334t, singularity-matching route) and KSel-3 (qou-q5zq,
Faddeev modular-double covariance) — file namespaces `ksel1*`/`ksel3*`
untouched; this route's distinct angle is the GNS/Favard/Jacobi bridge.

**Target.** Kernel selection principle 2: eliminate the binding-kernel
*choice* (the (REP) canonical-choice residue of
[`conj:schwinger-measure-computational-time`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md),
sharpened to a continuum in
[`2026-08-01-rep-jackson-identification.md`](2026-08-01-rep-jackson-identification.md)
§3) by identifying the kernel as the **spectral measure of a canonical
positive operator**: GNS on a positive functional gives a Hilbert
space; if a canonical self-adjoint operator $T$ has
$\langle 1, T^k 1\rangle$ equal to the binding data, its spectral
measure *is* the kernel — derived, no convention.

**Probe:** [`computations/probes/ksel2_favard_jacobi_probe.py`](../../computations/probes/ksel2_favard_jacobi_probe.py)
→ [`ksel2-favard-jacobi.witness.json`](../../computations/probes/ksel2-favard-jacobi.witness.json)
— 6/6 assertions, exit 0 (sympy exact symbolic + exact-ℚ arithmetic +
mpmath 60 dps at both q₀ pins; audit-only).

## 1. The Markov-trace positivity state (corpus survey — what is PROVED, where)

| Artifact | Claim | Epistemic tier |
|---|---|---|
| [`observations/algebraic-gns-embedding.md`](../../content/quantum-observable-universe/observations/algebraic-gns-embedding.md) (`prop:algebraic-gns-embedding`) | $\mathrm{tr}_M(x^*x) \ge 0$ on $H_\infty(q)$ in the Wenzl regime $q^{1/2}+q^{-1/2} > 2$ (all real $q_0 > 1$ qualify), GNS $\Rightarrow$ faithful $*$-representation | **literature-established** (`jones1985`, `wenzl1988`; block tagged `established-not-conjectural`); Lean ref `markov_gns_embedding` carries `validation: "not_checked"` — *not* Lean-proved |
| [`QOU/MathlibExt/WenzlSchurElement.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/WenzlSchurElement.lean) | Wenzl Schur element $s_{\lambda,X}(Q)$ closed form; Schur element **nonzero** at generic $Q$ (positive hooks/contents, sorry-free) | Lean-proved (nondegeneracy input, **not** positivity of the trace) |
| [`QOU/MathlibExt/HeckeGramFactorial.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/HeckeGramFactorial.lean) + [`RegTraceGram.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/RegTraceGram.lean) | $\det(\mathrm{Gram}) = c\cdot[n]_q! \ne 0 \Rightarrow$ semisimple (the consumable Wenzl criterion) | Lean-proved sorry-free; the **general** $T_w$-basis determinant value remains open |
| [`QOU/Hecke/H2CompanionRep.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/H2CompanionRep.lean) (`h2GramFromRep_det`) | $n=2$: $\det(\mathrm{Gram}) = [2]_q^2$ from the regular representation | Lean-proved |
| [`QOU/Hecke/H3GramArithmetic.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/H3GramArithmetic.lean) | $n=3$ arithmetic core ($[3]_q!$, genericity) proved; matrix-level $\det = [3]_q!$ open | Lean-proved (arithmetic only) |
| [`QOU/Machinery/MarkovTraceOnHecke.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/MarkovTraceOnHecke.lean) | Markov trace scaffold: class axiomatising (M1) linearity, (M2) conjugation invariance, (M3) Markov reduction | axiomatised **scaffold** — no positivity content |
| [`mass-theory/confinement-sdp.md`](../../content/quantum-observable-universe/mass-theory/confinement-sdp.md) | per-block Frobenius positivity $\langle \pi_\lambda, \Phi\rangle \ge 0$ + adjacent-pair PSD + dual shadow prices | **constraints imposed** in the archimedean SDP layer, not a theorem about $\mathrm{tr}_M$ |
| [`appendix-surreals-archimedean/wenzl-positivity-implies-substrate-positivity.md`](../../content/quantum-observable-universe/appendix-surreals-archimedean/wenzl-positivity-implies-substrate-positivity.md) | Wenzl unitarity at $q_0 \Rightarrow$ substrate $C^*$-Frobenius positivity | **conjecture** |

> **Positivity state, precisely.** Trace *positivity*
> ($\mathrm{tr}_M(x^*x) \ge 0$, the state property GNS needs) is
> literature-cited (Wenzl's real-positive window, which contains every
> real $q > 1$ and both $q_0$ pins) and corpus-asserted at the
> proposition tier; **no QOU Lean declaration proves positivity at any
> rank**. What the Lean tranche proves is the *nondegeneracy*
> infrastructure (Schur elements $\ne 0$, $\det(\mathrm{Gram}) =
> c\,[n]_q! \Rightarrow$ semisimple, $n = 2$ determinant). The GNS
> route below therefore runs on the *moment-side* positivity that this
> probe establishes exactly (Hankel/Favard), which is independent of
> the Hecke-side Lean gap.

## 2. What plays $T$? — candidate evaluation

1. **(a) The dashboard transfer trace `tr_m_atom_zn` — NOT a moment
   sequence.** [`computations/tr_m_atom_via_transfer.py`](../../computations/tr_m_atom_via_transfer.py)
   evaluates $\mathrm{tr}_M(\beta) = \sum_{\lambda \vdash 3A}
   y_\lambda(q_0)\,\chi^\lambda(\beta)$ at **one fixed braid word**
   (atom vs free), i.e. a linear functional at a single algebra
   element. No $\langle 1, T^k 1\rangle$ power structure is present or
   implied; the "transfer matrix" there propagates characters across
   strands, not powers of a fixed positive element. Candidate (a) does
   not furnish the operator.
2. **(b) The Jones–Wenzl conditional-expectation tower** exists in the
   corpus only at the observation tier
   (`prop:algebraic-gns-embedding` and its interpretation blocks); no
   computable tower operator or its moments are implemented anywhere.
   Viable future route, no data today.
3. **(c) The C1-carrier / Jacobi reading — evaluated first per the
   work order, and it lands.** The classical fibre is exact: the
   involution numbers $I(n)$ of the Lean-proved recurrence
   $I(n{+}2) = I(n{+}1) + (n{+}1)I(n)$
   ([`KeystoneBridgeC1Binding.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/KeystoneBridgeC1Binding.lean))
   are **exactly the moments of the Gaussian $N(1,1)$** (Stein's
   identity is the recurrence), and the normalizer frame
   $m_k = N^{\mathrm{bal}}_q(k{+}1)$ is exactly a probability-measure
   moment sequence. Both frames define canonical Jacobi operators —
   §3.

## 3. The Favard computation (exact results)

Two canonical moment functionals, both from proved corpus structure
(one-sided $[k]_q = 1 + q + \dots + q^{k-1}$ throughout):

- **Kernel frame** — the balanced kernel measure $K$ of the (REP)
  target, a probability measure with moments

  $$
  m_k \;=\; N^{\mathrm{bal}}_q(k{+}1) \;=\; q^{-k(k-1)/4}\,[k]_q!\,,
  \qquad m_0 = 1,
  $$

  rational in $r = q^{1/4}$ ($m_k = r^{-k(k-1)}[k]_{r^4}!$); at
  $q = 1$: $m_k = k!$ (the $e^{-s}\,ds$ functional).
- **Carrier frame** — the Lean-proved q-involution numerators
  $S_q(n)$ ($S_q(n{+}2) = S_q(n{+}1) + [n{+}1]_q S_q(n)$) read as a
  Hamburger moment sequence; at $q = 1$ these are $I(n)$, the
  $N(1,1)$ moments.

Results (all exact unless marked 60 dps):

| Check | Kernel frame | Carrier frame |
|---|---|---|
| Hankel $\Delta_k > 0$ | exact, $k \le 9$ at $r = 21/20$ ($q \approx 1.2155$); symbolic $r{=}1$ values $\prod_{i\le k}(i!)^2$ (Laguerre) | exact, $k \le 9$ at $q = 6/5$; $\Delta_2 = q\,[2]_q$ symbolic; $q{=}1$ values $\prod_{i\le k} i!$ (Gaussian) |
| Stieltjes shifted Hankels | $\Delta^{(1)}_k > 0$ exact, $k \le 8$ — measure on $(0,\infty)$ | (not claimed) |
| Jacobi data | $\beta_1 = q^{1/2} + q^{-1/2} - 1 = 1 + (r - 1/r)^2$ — **exact sum-of-squares positivity**, $\ge 1$ for all $q>0$, $=1$ iff $q=1$; $\alpha_1, \beta_2$ recorded factored in the witness | **closed form** $\alpha_k = q^k$, $\beta_k = q^{k-1}[k]_q$ — verified-range identity (symbolic reproduction $n \le 12$; exact ℚ $k \le 8$ at $q = 6/5$; 60 dps at both pins) |
| $q = 1$ limit | monic Laguerre $\alpha_k = 2k{+}1$, $\beta_k = k^2$ (exact, $k \le 8$ on $m_k = k!$) | Gaussian $N(1,1)$ $\alpha_k = 1$, $\beta_k = k$ (exact, $k \le 8$ on $I(n)$) |
| GNS moment identity | $(M^n)_{00} = m_n$ exact, $n \le 12$ | same |
| $\beta$ growth at fibre $q$ | geometric, ratio certified $> 1$ exact (last ratio $1.675$ at $r = 21/20$; $1.362$ at the pins, 60 dps) | geometric (ratio $\to q\,[k{+}1]_q/[k]_q$, exact from the closed form) |
| Carleman $\sum 1/\sqrt{\beta_k}$ | finite (partial + geometric tail bound $\approx 2.63$) — sufficient condition **unavailable** | finite ($\approx 3.67$) — unavailable |

Three findings worth naming:

1. **The kernel's first Jacobi coefficient is the Wenzl quantity.**
   $\beta_1 = (q^{1/2} + q^{-1/2}) - 1$: the same
   $q^{1/2} + q^{-1/2}$ whose $>2$ bound is Wenzl's positivity window
   in `prop:algebraic-gns-embedding`. At the substrate this is a
   coincidence of expressions until derived otherwise, but it is an
   exact one, and $\beta_1 - 1 = (r - 1/r)^2$ makes kernel-side
   Favard positivity at order 1 a *sum of squares* — positivity by
   construction, not by evaluation.
2. **The carrier operator is a q-deformed Gaussian.** The
   verified-range closed form $\alpha_k = q^k$,
   $\beta_k = q^{k-1}[k]_q$ deforms the $N(1,1)$ data
   $(1, k)$ — an Al-Salam–Carlitz-type tridiagonal. The Lean-proved
   C1 recurrence *is* (at $q = 1$, exactly) Stein's characterization
   of the Gaussian; the q-lift replaces the Gaussian by this
   canonical q-Jacobi operator. General-$k$ proof of the closed form
   is an induction on the recurrence — queued as the natural small
   Lean follow-up (not forced here per the work order).
3. **"Does the Jacobi spectral measure have the balanced moments?" —
   YES, unconditionally.** $\langle e_0, J^n e_0\rangle = m_n$ is a
   matrix identity (verified exact to $n = 12$), and the moments of
   *every* self-adjoint extension's spectral measure agree with the
   matrix moments. Existence of a canonical positive operator whose
   moments are the binding data is **settled affirmatively, exactly**.

## 4. The canonicity verdict: what the GNS route pins, and where the convention resurfaces

- **At $q = 1$: total success, zero convention.** Both frames are
  Carleman-determinate ($\beta_k = k^2$ resp. $k$, so
  $\sum 1/\sqrt{\beta_k}$ diverges $\Rightarrow$ essential
  self-adjointness $\Rightarrow$ unique spectral measure). The
  canonical kernel **exists, is unique, and is derived**: $e^{-s}ds$
  (kernel frame), $N(1,1)$ (carrier frame). This re-derives the
  settled archimedean (REP) leg by operator theory alone.
- **At fibre $q > 1$: the operator is canonical; the measure is
  not.** The Jacobi matrix $J(q)$ is *uniquely determined* by the
  moments — no choice enters its construction. But the balanced
  moment problem is **indeterminate** at $q \ne 1$: the
  theta-translate reindex identity (re-verified exact, K7; the
  rep-jackson R4 mechanism) gives a continuum of distinct positive
  measures with identical moments, hence (Akhiezer; [`simon1998`])
  the minimal $J(q)$ is **not essentially self-adjoint**, has
  deficiency indices $(1,1)$, and its self-adjoint extensions form a
  **circle**. Each extension's spectral measure is a representing
  kernel; the kernel convention has not been eliminated — it has
  been *relocated, with exact coordinates*, into the extension
  choice (von Neumann/Nevanlinna parameter).
- **The two circles should be one.** The u-translate circle
  $u \in \mathbb{R}_{>0}/\tilde q^{\mathbb{Z}}$ (where
  $\tilde q = q^{1/2}$, the theta-grid base of the (REP) audit)
  and the extension circle found here parametrize the same
  indeterminacy from opposite ends. Whether the Jackson$\circledast$theta
  translates are (or convolve to) the N-extremal measures of $J(q)$
  is **open** (convolutions are generically *not* N-extremal); the
  adjacent literature family — Ismail–Masson's $q^{-1}$-Hermite
  problem with explicit geometric-grid N-extremal solutions
  ([`ismail-masson1994`], already in the corpus bibliography) — is
  the natural comparison point.

## 5. The precise remaining identification statement (the deliverable)

> **(KSEL2-ID).** The substrate binding kernel is the spectral measure
> of a **distinguished self-adjoint extension** of the canonical
> Jacobi operator $J(q)$ of the balanced moment functional
> $m_k = q^{-k(k-1)/4}[k]_q!$. Since the functional is Stieltjes
> (shifted Hankels $> 0$, K3), two extensions are canonical without
> any further input: the **Friedrichs** extension $J_F$ and the
> **Krein** extension $J_K$, whose spectral measures $\mu_F, \mu_K$
> are the extremal Stieltjes solutions ([`simon1998`]). Both have the
> balanced moments and the correct $q \to 1$ confluence to
> $e^{-s}ds$ (moment convergence to a determinate limit).

What remains to prove/decide, in order of tractability:

1. **General-$k$ carrier closed form** ($\alpha_k = q^k$,
   $\beta_k = q^{k-1}[k]_q$): an induction against the q-involution
   recurrence — Lean-suited, small, queued.
2. **Locate the corpus kernel on the circle**: compute the atoms of
   $\mu_F$ (or $\mu_K$) numerically from $J(q)$ (limit of zeros of
   the orthonormal polynomials with the appropriate boundary
   condition) and compare against the Jackson$\circledast$theta
   $u{=}1$ support grid — an exact-tier follow-up probe; a mismatch
   would prove the corpus kernel is *not* extremal, a match would
   pin it.
3. **Derive the extension choice from structure**: the honest closure
   of (REP) on this route is a substrate/categorical principle
   selecting the extension — candidates: positivity transfer from
   the confinement SDP (the Attack-A §1.4 route), bar-covariance
   acting on the Nevanlinna parameter (if the bar reflection
   $\sigma: s \mapsto \tilde q^{-1}/s$ exchanges $\mu_F$ and
   $\mu_K$, the *symmetric point(s)* of the circle become canonical
   — an exactly checkable question), or Friedrichs-minimality as a
   physical energy principle (the Friedrichs extension is the one
   with form domain the closure of the polynomials — the "no
   information beyond the algebra" choice, i.e. the GNS-internal
   candidate).

Scope-(a) statement: this audit does **not** claim the kernel *is*
$\mu_F$; it reduces "derive the kernel" to "derive the extension" and
exhibits the two canonical candidates. Nothing here proves or refutes
`conj:schwinger-measure-computational-time`.

## 6. Discipline

- **Corpus-grep (all four paths).**
  `Favard|Jacobi matrix|Jacobi operator|Hankel|orthogonal polynomial|N-extremal|Nevanlinna`
  over `docs/audits/`, `docs/coordination/`, `content/`,
  `computations/`: no prior Favard/Jacobi treatment of the balanced
  moments or the carrier sequence (nearest: the q-Hankel *vacuum-row*
  refutation `2026-07-04-keystone-qhankel-eq2-vacuum-row-sourced-refutation.md`,
  a different object; the covariance-kernel moment audits, different
  sequences). `GNS|positive functional|conditional expectation`
  walked for §1-§2 (hits: the `algebraic-gns-embedding` cluster, the
  nc-probability dictionary). Coordination ledgers checked
  (`option-e.md`, `keystone-infra.md`, the 2026-07-24 binding-mass
  workplan): no closure of this item recorded.
- **NO FIT.** Every scored check is an exact symbolic identity, an
  exact rational value, or a 60-dps cross-check of a displayed
  identity at tol $10^{-25}$/$10^{-30}$ (measured $< 10^{-59}$); the
  q₀ pin strings enter only as evaluation points; no CODATA read;
  nothing wired; no conjecture-class instance created. The carrier
  closed form is a *verified-range identity* (every instance exact),
  explicitly not a general-$k$ theorem and explicitly not a fit.
- **Formalize-first.** The load-bearing identities were derived by
  hand and asserted symbolically before any numeric layer:
  $\Delta_2 = q[2]_q$, $\beta_1 = 1 + (r - 1/r)^2$, the Stein
  reading of the C1 recurrence, the theta reindex identity. The
  numerics only cross-check displayed identities at evaluation
  points.
- **Refuted/ruled-out hygiene.** The negative here — "moments +
  positivity do not pin the measure at $q \ne 1$" — is a
  **structural exclusion with a cited invariant** (indeterminacy via
  an exact continuum of representing measures), scope (b) legitimate;
  the candidate-(a) negative ("`tr_m_atom_zn` is not a moment
  sequence") is scope-limited to what that function computes today.
- **Render-QA:** the preflight grep battery was run by hand (balanced
  `$`/`$$`/braces; no `\operatorname`; no markdown-list lines opening
  with `+`/`-`/`*` inside display math; no inline align-family
  environments; display `$$` on their own lines). The pipeline render
  was not run in this sandbox — **this doc was not
  machine-validated**, stated per the render-QA gate.

## 7. Cross-references

- Target conjecture: [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
- The (REP) canonical-choice reduction + u-continuum (sharpened to the extension circle here): [`2026-08-01-rep-jackson-identification.md`](2026-08-01-rep-jackson-identification.md)
- The proved corpus operation (recurrence + strip): [`2026-07-20-keystone-bridge-c1-binding.md`](2026-07-20-keystone-bridge-c1-binding.md), [`KeystoneBridgeC1Binding.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/KeystoneBridgeC1Binding.lean)
- Positivity/GNS corpus state: [`algebraic-gns-embedding.md`](../../content/quantum-observable-universe/observations/algebraic-gns-embedding.md) (+ proof/interpretation siblings), [`wenzl-positivity-implies-substrate-positivity.md`](../../content/quantum-observable-universe/appendix-surreals-archimedean/wenzl-positivity-implies-substrate-positivity.md), [`confinement-sdp.md`](../../content/quantum-observable-universe/mass-theory/confinement-sdp.md)
- Moment-convergence Mathlib gap (Fréchet–Shohat/Carleman package used for confluence statements): [`2026-07-25-kernel-convergence-mathlib-gap.md`](2026-07-25-kernel-convergence-mathlib-gap.md)
- Literature: [`simon1998`] (moment problem as a self-adjoint finite difference operator — determinacy ⟺ e.s.a., Friedrichs/Krein extremal solutions), [`ismail-masson1994`] ($q^{-1}$-Hermite indeterminate family, explicit N-extremal grids), [`wenzl1988`] (trace positivity window)
- Probe + witness: [`ksel2_favard_jacobi_probe.py`](../../computations/probes/ksel2_favard_jacobi_probe.py), [`ksel2-favard-jacobi.witness.json`](../../computations/probes/ksel2-favard-jacobi.witness.json)
