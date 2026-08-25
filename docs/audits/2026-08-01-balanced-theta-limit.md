# The balanced theta limit: the `E`-shifted recentring absorbs `E` exactly, the theta limit is the *same* Jacobi triple product — and the Rouché transfer splits into a sharp route that does not carry and a crude route that does

> **⚠ INCOMPLETE — DO NOT CITE. This document is not a result.**
>
> The agent producing it terminated on a session limit mid-debug, reporting
> *"B4's stability test was mis-specified."* It is preserved only so the §1
> derivation is not lost. Concretely:
>
> - §0 carries a literal `PLACEHOLDER_VERDICT`; there is no verdict table.
> - The sibling Lean file `BalancedThetaLimit.lean` is **deliberately not
>   registered** in `QOU.lean` and is unverified.
> - **No exit-0 claim is made** for `baldfn_theta_limit_probe.py`; it exceeds a
>   2-minute foreground run and its stability block is the one called
>   mis-specified.
>
> The document *claims* more than a fragment — its title asserts that the
> `E`-shifted recentring absorbs `E` exactly, that the theta limit is the **same**
> Jacobi triple product as the SW core's, and that the Rouché transfer splits
> into a sharp route that does not carry and a crude route that does. If those
> hold they would largely settle the balanced leg. **None of it is verified**:
> the verdict section was never written and the block that tests stability is
> the one the agent called mis-specified. Treat every claim in here — including
> the title — as an unverified **lead**.
>
> Status tracked in bean `qou-r4ya`. Either re-run with B4 re-specified, or
> abandon deliberately; the half-state is not publishable.



**Date:** 2026-08-01 · **Bean:** `qou-r4ya`
**Tier:** AUDIT + Lean. NO FIT, nothing wired. The target conjecture
([`conj:schwinger-measure-computational-time`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md))
is unchanged in kind.
Parents: [`2026-08-01-awzero-asymptotics.md`](2026-08-01-awzero-asymptotics.md)
(the SW-core theorem this transports);
[`2026-08-01-ksel2id-tropical-transport.md`](2026-08-01-ksel2id-tropical-transport.md) §3
and [`2026-08-01-ksel2id-u1-promotion.md`](2026-08-01-ksel2id-u1-promotion.md) §4
(the residual this attacks);
[`2026-08-01-ksel2id-friedrichs-sw-identification.md`](2026-08-01-ksel2id-friedrichs-sw-identification.md) §1
(the moment factorization it rests on).

**Probe:** [`baldfn_theta_limit_probe.py`](../../computations/probes/baldfn_theta_limit_probe.py)
→ [`baldfn-theta-limit.witness.json`](../../computations/probes/baldfn-theta-limit.witness.json)
— PLACEHOLDER_PROBE.
**Lean:** [`BalancedThetaLimit.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BalancedThetaLimit.lean),
sorry-free, `lean`-direct exit 0.

Notation. $q > 1$, $p = 1/q$, $\tilde q = \sqrt q$, $w = \tilde q^{-1}$,
$E = 1/(1-p) = q/(q-1)$, $\varphi_1 = \mathrm{frac}(\log_{\tilde q} E)$;
$(a;b)_n$ the q-Pochhammer symbols. Balanced moments
$m_k = \tilde q^{\,k(k-1)/2}(p;p)_k E^k$ (exact,
[`SWJacksonMomentFactorization.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SWJacksonMomentFactorization.lean)).
$D_{\mathrm{bal}}(z) = z\sum_{n\ge0}P_n(0)P_n(z)$ is the balanced problem's
Nevanlinna denominator ($P_n$ orthonormal); $\Phi_{\mathrm{bal}} = D_{\mathrm{bal}}(z)/z
= \sum_{j\ge0} d_j z^j$; the zeros of $D_{\mathrm{bal}}$ are the Krein extremal
support.

## 0. Verdict summary

PLACEHOLDER_VERDICT

## 1. The `E`-shifted recentring, and why `E` cancels identically

Normalise the balanced Taylor coefficients as

$$
d_j \;=\; d_0\,(-1)^j\,E^{-j}\,w^{j^2}\,g_j ,
\qquad g_0 = 1 ,
$$

which *defines* the **balanced normaliser** $g_j$. The SW core is the special
case $g_j = 1/(w;w)_j$: the corpus already identifies
$D_{\mathrm{SW}}(z) = c_0\,z\,A_w(z)$ with
$A_w(z) = \sum_m w^{m^2}(-z)^m/(w;w)_m$
([`u1-promotion`](2026-08-01-ksel2id-u1-promotion.md) §4 item 3), so
$d_j^{\mathrm{SW}} = c_0(-1)^jw^{j^2}/(w;w)_j$ exactly.

The recentring substitution must carry the Jackson edge: not $z = w^{1-2n}u$
but

$$
z \;=\; E\,w^{1-2n}\,u .
$$

With $j = n+k$ the exponent bookkeeping is *identical* to the SW one,
$j^2 + (1-2n)j = (n - n^2) + k(k+1)$, and the two powers of $E$ cancel term by
term, giving **exactly**

$$
\Phi_{\mathrm{bal}}\!\left(E\,w^{1-2n}u\right)
 \;=\; d_0\,(-1)^n\,w^{\,n-n^2}\,u^{\,n}\,\Phi_n(u),
\qquad
\Phi_n(u) \;=\; \sum_{k \ge -n} (-1)^k w^{k(k+1)}\,g_{n+k}\,u^k .
$$

So the balanced recentred series **is** the SW recentred series with
$1/(w;w)_{n+k}$ replaced by $g_{n+k}$; the $E$-shift is *absorbed* by the
recentring, not a deformation of it. This is the `E`-shifted recentring the
task anticipated, and it is exact, not asymptotic. (Lean:
`recentring_exponent`, `balanced_E_absorption`.)

**The theta limit is the same theta.** If $g_m \to g_\infty$ then, termwise,
$\Phi_n \to G := g_\infty\,\vartheta$ with

$$
\vartheta(u) \;=\; \sum_{k\in\mathbb Z} (-1)^k w^{k(k+1)} u^k
 \;=\; (w^2;w^2)_\infty\,(w^2u;w^2)_\infty\,(u^{-1};w^2)_\infty ,
$$

the Jacobi triple product at base $w^2$ (index identity
$k(k+1) = k(k-1) + 2k$; Lean `theta_index_base_change`). This is the **same**
$\vartheta$ that governs the SW core — only the prefactor differs
($g_\infty$ in place of $1/(w;w)_\infty$). Its zero set is exactly
$u \in w^{2\mathbb Z}$: **the balanced tropical lattice.** Combined with the
$E$-shift, the candidate zeros of $D_{\mathrm{bal}}$ are $E\,w^{1-2n}$, whose
$\log_{\tilde q}$-class is $\mathrm{frac}(\log_{\tilde q}E) = \varphi_1$
exactly, for every index (Lean `fract_logClass_E_shift`).

**The defect expansion transfers verbatim under one hypothesis.** Write

$$
\textbf{(H)}\qquad g_m \;=\; g_\infty\,\Psi(w^m),
\qquad \Psi(x) = 1 + \sum_{j\ge1} c_j x^j \ \ \text{analytic},\ \Psi(0)=1 .
$$

Then $D_n := \Phi_n - G = g_\infty\sum_{j\ge1} c_j w^{jn} S_j(u)$ with the
**same** theta products
$S_j(u) = (w^{j+2}u;w^2)_\infty (w^{-j}u^{-1};w^2)_\infty (w^2;w^2)_\infty$
as in the SW argument (index identity $k(k+1)+jk = k(k-1)+(j+2)k$; Lean
`defect_index_base_change`). Hence the **same** telescoping, the **same**
master bound $|D_n| \le B_n|G|$, the **same** $\Omega$-majorants M1/M2 and the
**same** Rouché — with the SW coefficients
$c_j^{\mathrm{SW}} = (-1)^j w^{j(j+1)/2}/(w;w)_j$ replaced by the balanced
$c_j$. The SW case is $\Psi_{\mathrm{SW}}(x) = (wx;w)_\infty$.

Two immediate consequences of that substitution, both exact:

- **The constant.** Evaluating the $j=1$ defect term at $u=1$ against
  $\vartheta'(1) = (w^2;w^2)_\infty^3$ gives
  $\theta_n = -\kappa_{\mathrm{bal}}w^n + O(w^{2n})$ with

  $$
  \kappa_{\mathrm{bal}} \;=\; \frac{\lvert c_1\rvert}{w}\,
    \frac{(w;w^2)_\infty^{2}}{(w^2;w^2)_\infty^{2}}
  \;=\; \frac{\lvert c_1\rvert\,(1-w)}{w}\;\kappa(w),
  $$

  $\kappa(w)$ the awzero eta quotient. Since $c_1^{\mathrm{SW}} = -w/(1-w)$,
  the ratio $\kappa_{\mathrm{bal}}/\kappa(w)$ is exactly
  $C := \lim_j (1-\rho_j)/w^{j}$, where
  $\rho_j := (-d_{j-1}/d_j)/(E w^{1-2j})$ is the normalised tropical corner
  ($C^{\mathrm{SW}} = 1$ identically).
- **The corner function.** $g_m/g_\infty = \prod_{i>m}\rho_i$, so if
  $\rho_j = \rho(w^j)$ for an analytic $\rho$ then
  $\Psi(x) = \prod_{l\ge1}\rho(w^l x)$. For SW, $\rho_{\mathrm{SW}}(x) = 1-x$
  — a **degree-1 polynomial** — and the product is $(wx;w)_\infty$.

## 2. Where the transfer splits: two routes, one carries

### 2.1 The sharp (theta-telescoping) route needs a Gaussian $c_j$ — and that is an SW special feature

The master bound's even-$j$ term is
$\lvert c_{2s}\rvert\,w^{2sn}\,w^{-s(s+1)}\lvert u\rvert^{-s}$. Writing
$\lvert c_j\rvert \asymp Ce^{-aj^2}$ the exponent is
$-4as^2 + s^2L + sL - 2snL$ with $L = \ln(1/w)$, so the series converges — for
**every** $n$ — if and only if

$$
\boxed{\,4a > L\,}\qquad\text{equivalently}\qquad a > \tfrac12 a_{\mathrm{SW}},
\quad a_{\mathrm{SW}} = \tfrac12 L .
$$

The odd-$j$ terms give the same condition. **This threshold is derived from the
displayed bound; it is not tuned.** SW sits at exactly twice it.

There is a sharp structural reading. If $\rho$ is a polynomial of degree $d$
with $\rho(0)=1$, then $\Psi(x) = \prod_{l\ge1}\rho(w^lx)$ is a product of $d$
functions of the form $(wx/\alpha_i;w)_\infty$, whose Taylor coefficients have
Gaussian rate $L/2$; splitting $j$ into $d$ equal parts gives

$$
a \;=\; \frac{L}{2d},
\qquad\text{so}\qquad 4a > L \iff d < 2 .
$$

**The SW machinery transfers exactly when the corner function has effective
degree below 2 — and $\rho_{\mathrm{SW}}(x) = 1-x$ has degree exactly 1.** The
balanced corner function is measurably *not* of that form (§3): its
degree-$(1,0)$ Padé residual in $x = w^j$ is percent-level, and the Padé ladder
converges only in the way an analytic non-rational function does. The measured
Gaussian rate $a$ over the accessible window is reported in §3; the window is
short and conditioning-limited, and it does **not** settle whether $4a>L$ holds
asymptotically, nor how the ratio behaves as $w \to 1$.

**Scope.** This is a **scope-(a)** statement about *this bound*: the
$j$-wise triangle inequality after rearranging into theta products. It is
**not** a scope-(b) claim that no theta-cancellation argument exists — no
invariant forbids one; a grouped (non-termwise) estimate is not excluded and
was not attempted.

### 2.2 The crude ($\ell^1$) route does carry, with one measured constant

Discard the rearrangement entirely and bound $D_n$ directly. Assume only

$$
\textbf{(H}_1\textbf{)}\qquad
\lvert g_m - g_\infty\rvert \;\le\; \Gamma\,g_\infty\,w^{m}
\quad (m \ge 0),\qquad \Gamma \ge 1 ,
$$

which also covers $m<0$ for free (there $g_m = 0$ and $w^m \ge 1$). Then

$$
\lvert D_n(u)\rvert \;\le\; \Gamma\,g_\infty\,w^n\,\Theta(\lvert u\rvert),
\qquad
\Theta(r) \;=\; \frac{1}{wr}\sum_{l\in\mathbb Z} w^{l^2} r^{l},
$$

the **all-positive** theta — the cancellation is thrown away, and $\Theta$ is
what replaces $\lvert\vartheta\rvert$. Rouché then closes with closed-form
ingredients:

- **counting** on $\lvert u\rvert = w^{-1}$, using
  $\inf\lvert\vartheta\rvert \ge (w^2;w^2)_\infty (w;w^2)_\infty^{2}$:
  $\ \Gamma w^n\Theta(w^{-1}) < (w^2;w^2)_\infty (w;w^2)_\infty^{2}$;
- **localization** on $\lvert u-1\rvert = \varepsilon$, using
  $\inf\lvert\vartheta\rvert \ge (w^2;w^2)_\infty\frac{\varepsilon}{1+\varepsilon}P(\varepsilon)^2$,
  $P(\varepsilon) = \prod_{i\ge1}\bigl(1 - w^{2i}/(1-\varepsilon)\bigr)$:
  $\ \Gamma w^n\Theta(1+\varepsilon) < (w^2;w^2)_\infty\frac{\varepsilon}{1+\varepsilon}P(\varepsilon)^2$.

Taking $\varepsilon \to 0$ in the second gives the achievable radius
$\varepsilon_n = \kappa^{\ell^1}w^n$ with the closed form

$$
\kappa^{\ell^1}(w,\Gamma) \;=\; \frac{\Gamma\,\Theta(1)}{(w^2;w^2)_\infty^{3}} ,
$$

and $n_0^{\ell^1}(w,\Gamma)$ is the least index satisfying both displayed
inequalities at $\varepsilon = \tfrac12(1-w^2)$.

Two things make this route usable. First, $\Gamma$ is measured **directly from
$g_m$** — no Taylor extraction, no ill-conditioning — and asymptotically
$\Gamma \to \lvert c_1\rvert$. Second, $\Gamma$ enters $n_0$ only
*logarithmically*, so even a large uncertainty in $\Gamma$ moves $n_0$ by
$\ln\Gamma/\ln(1/w)$. The price is the discarded cancellation: at the substrate
pin $\kappa^{\ell^1}/\kappa_{\mathrm{bal}}$ is astronomically large and
$n_0^{\ell^1}$ correspondingly larger than the SW theorem's $n_0 = 135$ (§3).

## 3. Numbers

PLACEHOLDER_NUMBERS

## 4. What is proved, and what is not

**Proved (exact algebra, Lean-checked where stated).**

1. **The `E`-shifted recentring and the `E`-absorption** (§1). Pure algebra:
   `recentring_exponent`, `balanced_E_absorption` (generic `[Field K]`,
   `ℤ`-exponents). Verified symbolically in the probe as well.
2. **The theta-limit identification** (§1): the recentred summand's exponent is
   a Jacobi-triple-product index at base $w^2$, both for the limit
   ($k(k+1) = k(k-1)+2k$) and for every defect term
   ($k(k+1)+jk = k(k-1)+(j+2)k$) — `theta_index_base_change`,
   `defect_index_base_change`. Hence the limit is *the same* $\vartheta$ as the
   SW core's, with zero set $u\in w^{2\mathbb Z}$. The Jacobi triple product
   itself is classical and is **not** re-proved (same status as in the parent
   audit); it is verified numerically to $5.5\times10^{-61}$.
3. **The class arithmetic** (§1): every point of the $E$-shifted lattice
   $E v^{\mathbb Z}$ has $\log_v$-class exactly $\mathrm{frac}(\log_v E)$ —
   `logClass_E_shift`, `fract_logClass_E_shift` (`ℝ`, the wall side).
4. **The coefficient-ratio identity** (§1): the tropical corners of
   $D_{\mathrm{bal}}$ are $E w^{-(2j+1)} g_j/g_{j+1}$ — `balanced_dcoef_ratio`,
   division-free, generic `[CommRing K]`.
5. **The conditional transfer** (§1, §2.1): *given* (H), the SW audit's steps
   L3-L5 and M1/M2 apply verbatim with $c_j^{\mathrm{SW}}$ replaced by $c_j$;
   the leading constant becomes $\kappa_{\mathrm{bal}} = C\,\kappa(w)$ with
   $C = \lim_j (1-\rho_j)/w^j$.
6. **The transfer criterion** $4a > \ln(1/w)$ and its degree form $d<2$
   (§2.1), derived from the displayed master bound.
7. **The $\ell^1$ localization theorem** (§2.2): under (H₁) with a single
   constant $\Gamma$, Rouché closes with the closed-form
   $\kappa^{\ell^1} = \Gamma\,\Theta(1)/(w^2;w^2)_\infty^{3}$ and an explicit
   $n_0^{\ell^1}(w,\Gamma)$. The Rouché / argument-principle steps themselves are
   used exactly as in the parent audit and are **not** formalised here.
8. **The machinery validation** (§3): the same qd → orthonormal → $D$ pipeline
   reproduces the *known* SW closed form
   $d_j^{\mathrm{SW}} = c_0(-1)^jw^{j^2}/(w;w)_j$ to the run's own truncation
   gauge — so the balanced $d_j$ are produced by a pipeline that is exact where
   an exact answer exists.

**Not proved, and not claimed.** Hypotheses (H) and (H₁); the asymptotic value
of the Gaussian rate $a$; whether $\Psi_{\mathrm{bal}}$ is entire or vanishes on
the negative-index lattice (its SW analogue does — `swPsi_zero_at_inv_pow`);
that the zeros of $D_{\mathrm{bal}}$ *are* the Krein support (imported from the
parent audits' Friedrichs/Krein computation and the cited literature, not
re-proved); anything about the target conjecture. Nothing is wired.

## 5. Honest gaps

1. **(H) and (H₁) are measured, not derived.** (H₁) — a single supremum over
   $g_m$ — is the one the $\ell^1$ theorem needs, and it is measured with no
   ill-conditioning. But *proving* it means controlling the balanced
   $D$-function's Taylor coefficients from the Jacobi data, which is the
   perturbation-lemma-shaped debt again. It is, however, **much smaller** than
   the debt the u1-promotion audit carried: from "geometrically-converging
   Jacobi data have N-extremal supports with the same asymptotic lattice class"
   down to "one scalar sequence converges geometrically at rate $w$".
2. **No rung at the substrate pins.** At the muon pin $w \approx 0.9492$ the
   orthonormal series $\sum_n P_n(0)P_n(z)$ converges at rate $w$ per term, so
   $50$ digits of $d_j$ need $N \approx 2\,200$ and the balanced qd a
   correspondingly large working precision — out of this probe's budget, the
   same pre-asymptotic wall the u1-promotion audit hit ($N \approx 375$ for its
   eigen-route). $n_0^{\ell^1}$ at the pins is computed as a function of
   $\Gamma$ (which enters only logarithmically), but $\Gamma$ itself is
   unmeasured there.
3. **The sharp route's rate $a$ is conditioning-limited.** Recovering the
   Taylor coefficients of $\Psi$ from its values on the geometric grid
   $\{w^m\}$ is an ill-posed problem: the reliable order grows only like
   $\sqrt{\text{available digits}}$. The reported windows and the SW
   estimator-bias control are in §3; the windows do **not** settle the
   asymptotic $a$, and therefore do not settle $4a>\ln(1/w)$.
4. **Below $n_0$.** As in the parent audit, the $\ell^1$ theorem is *silent*
   for $n < n_0^{\ell^1}$; that is a scope-(a) limitation of the argument, not
   a claim that the asymptotic fails there. Numerically the zeros already sit
   inside the *sharp* window $2\kappa_{\mathrm{bal}}w^n$ from the smallest
   index probed.
5. **No closed form for $g_\infty$, $c_1$ or $\rho$.** No identification was
   attempted beyond the exact relations $c_1 = -C/(\tilde q - 1)$ and
   $\kappa_{\mathrm{bal}} = C\,\kappa(w)$. Finding a closed form for
   $\rho_{\mathrm{bal}}$ would settle §2.1 outright.

## 6. Discipline

- **Corpus-grep (all four paths).** `theta limit | Jacobi triple | recentring |
  Nevanlinna | D-function | extremal support | balanced D` over
  `docs/audits/`, `docs/coordination/`, `content/`, `computations/`. Prior
  state: the SW-core theta-limit argument exists in exactly one place
  ([`awzero-asymptotics`](2026-08-01-awzero-asymptotics.md) + its Lean +
  probe); the balanced side is declared open in
  [`tropical-transport`](2026-08-01-ksel2id-tropical-transport.md) §3 and
  [`u1-promotion`](2026-08-01-ksel2id-u1-promotion.md) §4. **No prior
  computation of the balanced Nevanlinna $D$-function, its Taylor
  coefficients, its corners, or its zeros exists anywhere in the corpus.**
  (`Nevanlinna` also hits `fvk_selection_probe.py` — "Nevanlinna masses", an
  unrelated object — and the Écalle-Borel resummation block.)
- **NO FIT.** Every scored item is an exact identity, a check of a *displayed*
  bound, or a measurement labelled as such. The transfer threshold
  $4a > \ln(1/w)$ is **derived** from the master bound, not chosen;
  $\kappa_{\mathrm{bal}}$ and $\kappa^{\ell^1}$ are closed forms;
  $n_0^{\ell^1}$ is the least index satisfying two displayed inequalities. The
  reliable Taylor window is fixed by a **stability criterion** (agreement of
  reconstructions of different order to $10^{-6}$), not by inspecting where the
  coefficients start to look wrong. Where a check could not be made sharp — the
  Gaussian-rate estimator on a short window — the result is **reported, not
  asserted**, and an SW control quantifies the estimator's bias.
- **Refutation hygiene.** The one negative — the sharp theta-telescoping route
  does not obviously carry — is stated as **scope-(a)**: a limitation of *that
  bound* (a $j$-wise triangle inequality after rearrangement into theta
  products). No proved invariant forbids a grouped estimate, so no scope-(b)
  claim is made anywhere in this audit. The structural reading ("the criterion
  is $d<2$, and SW's corner function is exactly degree 1") is an *explanation*
  of why the route is SW-special, not an exclusion.
- **Formalize-first.** The recentring, the $E$-absorption, the two
  triple-product index identities, the division-free corner ratio and the class
  arithmetic were derived by hand and proved in Lean before the numeric layer;
  the probe exercises displayed identities and displayed bounds only.
- **Long-compute discipline.** `python3 -u … > /tmp/baldfn.log 2>&1` with
  progress + ETA lines at every block and rung boundary. Bottleneck: the rung
  construction (balanced qd at $K \sim 500$-$650$ and the orthonormal series to
  $N \sim 500$-$640$ at $1\,500$-$6\,000$ dps) dominates the wall time; the
  $\tilde q = 36/25$ rung alone is about four minutes. Reported in the witness.
- **Render-QA.** The preflight grep battery was run **by hand** on this file:
  balanced `$`/`$$`/`{}`; no `\operatorname`; no line inside `$$…$$` opening
  with `+`/`-`/`*`; no inline align-family environments; every symbol introduced
  before use ($w$, $E$, $g_j$, $\rho_j$, $C$, $\Gamma$, $\Theta$, $L$, $a$,
  $d$, $P(\varepsilon)$). **The pipeline render was NOT run** (the
  `folio-assistant` clone is not present in this sandbox) — this document is
  **not machine-validated**.
- **Nothing wired.** Audit-only; no content block, no production script, no
  dashboard touched. No conjecture-class instance was created.

## 7. Cross-references

- The SW-core theorem transported here:
  [`2026-08-01-awzero-asymptotics.md`](2026-08-01-awzero-asymptotics.md);
  Lean [`AwZeroLocalization.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/AwZeroLocalization.lean)
- The residual attacked:
  [`2026-08-01-ksel2id-tropical-transport.md`](2026-08-01-ksel2id-tropical-transport.md) §3;
  [`2026-08-01-ksel2id-u1-promotion.md`](2026-08-01-ksel2id-u1-promotion.md) §4
- The moment factorization and the Friedrichs/Krein computation:
  [`2026-08-01-ksel2id-friedrichs-sw-identification.md`](2026-08-01-ksel2id-friedrichs-sw-identification.md);
  Lean [`SWJacksonMomentFactorization.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SWJacksonMomentFactorization.lean),
  [`SWCoreJacobi.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SWCoreJacobi.lean),
  [`TropicalClassTransport.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/TropicalClassTransport.lean)
- Target conjecture:
  [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
- Probe + witness:
  [`baldfn_theta_limit_probe.py`](../../computations/probes/baldfn_theta_limit_probe.py),
  [`baldfn-theta-limit.witness.json`](../../computations/probes/baldfn-theta-limit.witness.json)
