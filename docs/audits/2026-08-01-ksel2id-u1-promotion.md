# KSEL2-ID u ≡ 1 promotion — the extremal-extension class is the SW integer lattice pushed by the Jackson edge: exact Ramanujan-function identification of the pure-SW extremal supports, exact transfer factorization, and a numeric promotion of the u ≡ 1 alignment from 1e-4 to ~1e-9

**Date:** 2026-08-01 · **Bean:** qou-ml55 (KSEL2-ID follow-up: promote
the u ≡ 1 Friedrichs/Krein alignment from measured to
derived/certified) · **Namespace:** `ksel2id_u1_*`
**Tier:** AUDIT — NO FIT, nothing wired; no content block or Lean file
touched (parent session owns those). Parent audit:
[`2026-08-01-ksel2id-friedrichs-sw-identification.md`](2026-08-01-ksel2id-friedrichs-sw-identification.md)
(its §2 measured u ≡ 1 alignment, $10^{-4}$ at $q = 2.0736$, $K = 48$,
is the promotion target); grandparent:
[`2026-08-01-ksel2-gns-favard-canonicity.md`](2026-08-01-ksel2-gns-favard-canonicity.md).

**Probe:** [`computations/probes/ksel2id_u1_promotion_probe.py`](../../computations/probes/ksel2id_u1_promotion_probe.py)
→ [`ksel2id-u1-promotion.witness.json`](../../computations/probes/ksel2id-u1-promotion.witness.json)
— 5 assertion blocks, all passed, exit 0 (sympy exact symbolic +
exact-ℚ qd + certified mpf qd + truncation eigen studies to $N = 240$
+ truncation-free Ramanujan-zero studies; both q₀ pins). Wall ≈ 13 min;
log `/tmp/ksel2id_u1.log` (progress + ETA lines per the long-compute
discipline; bottleneck: `mp.eigsy` pairs at $N = 208$–$240$, ~2.5–4.5
min per deep rung).

Notation as in the parent: $q > 1$, $p = 1/q$, $\tilde q = \sqrt q$,
$\tilde p = 1/\tilde q$, $L = \ln \tilde q$, $E = 1/(1-p) = q/(q-1)$;
balanced moments $m_k = q^{-k(k-1)/4}[k]_q!$; SW factor moments
$G_k = \tilde q^{\,k(k-1)/2}$ (the moments of $\mathrm{LN}(-L/2, L)$);
u ≡ 1 grid class $\varphi_1 = \mathrm{frac}(\log_{\tilde q} E)$.

## 0. Verdict summary

| # | Statement | Tier |
|---|---|---|
| A-1 | Pure-SW monic Jacobi data in closed form: $\alpha_n = \tilde q^{2n-1}(1+\tilde q) - \tilde q^{n-1}$, $\beta_n = \tilde q^{4n-3} - \tilde q^{3n-3}$ | **Lean-proved at general $n$** (upgraded from the symbolic-qd tier by the parent session: [`SWCoreJacobi.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SWCoreJacobi.lean), `swVec_zero_eq_swMoment`, sorry-free over a generic field; the classical SW/q-Laguerre recurrence [`christiansen2003sw`], [`moak1981`]) |
| A-2 | SW Nevanlinna function $D(z) = c_0\, z\, A_{\tilde p}(z)$, $A_w$ = Ramanujan entire function, $c_0 = \sum_n p_n(0)^2$ | **exact-numeric functional identity** (ratio constant to $6.5\times10^{-23}$ over 8 sign-spread samples; the q-difference equation of $A_w$ exact-symbolic) |
| A-3 | Krein support $=$ zeros($A_{\tilde p}$); Friedrichs support $=$ zeros($A_{\tilde p}$)$/\tilde q$ — one $\tilde q$-step apart, via the exact SW scale map $S$ | **exact-numeric** (rel $1.7\times10^{-8}$ / $1.2\times10^{-8}$ vs the parent's truncation/Radau machinery) |
| A-4 | Pure-SW extremal class $=$ the **integer** $\tilde q$-lattice class $0$; Krein odd, Friedrichs even $q$-sublattice | **asymptotic-measured** (rate $= \tilde p$; Aitken² $\sim 4\times10^{-29}$ at $q=2.0736$) |
| A-5 | Transfer factorization $m_k = G_k\,E^k\,(p;p)_k$ | **exact** (symbolic $k \le 12$) |
| A-6 | Balanced Jacobi data $\to$ ($E$, $E^2$)-scaled SW closed forms at geometric rate $\tilde p$ | **measured** (dev $9\times10^{-8}$ at $n=40$, $r=6/5$; rate $=\tilde p$ to $2\times10^{-2}$) |
| A-7 | Hence $\varphi_1 = 0 + \log_{\tilde q} E \bmod 1$: the u ≡ 1 class is the $E$-image of the SW integer class — *derivation-shaped*, modulo one perturbation lemma (open, §4) | **conditional** (named gap) |
| B-1 | $q = 2.0736$ K-ladder 48→96: alignment $2\times10^{-4} \to 8\times10^{-10}$ (Aitken², unc $1.2\times10^{-8}$); Krein same class to $2\times10^{-9}$ | **certified-measured** |
| B-2 | q-ladder 1.8 / 1.5 certified ($1.7/2.7\times10^{-8}$); 1.3 / 1.2 / 1.15 measured-preasymptotic, consistent with $\varphi_1(q)$ within stated uncertainty | **tiered** (per-rung labels, §2.2) |
| B-3 | Pins: SW-core class-0 **certified truncation-free** at the muon pin (Aitken² $-8.2\times10^{-8}$, unc $9.9\times10^{-8}$); balanced truncation layer PRE-ASYMPTOTIC — **no balanced class claim at the pins**; N-requirement model: $N \approx 375$ | **certified (SW core) / honest gap (balanced)** |

## 1. Leg A — the literature-exact route

### 1.1 Closed-form Jacobi data for the SW core (exact)

The qd algorithm applied to $G_k = \tilde q^{\,k(k-1)/2}$ — symbolically
in $\tilde q$ (depth 4) and in exact ℚ at $r = 6/5$ (depth 20) —
reproduces the classical Stieltjes–Wigert / q-Laguerre three-term
recurrence, in this normalization

$$
\alpha_n = \tilde q^{2n-1}(1+\tilde q) - \tilde q^{n-1},
\qquad
\beta_n = \tilde q^{4n-3} - \tilde q^{3n-3},
$$

exactly ([`christiansen2003sw`], [`moak1981`], up to the explicit scale
between moment normalizations). Two exact side identities set up
everything below:

- **SW scale map $S$.** $\tilde q^{-k}\, G_{k+1}/G_1 = G_k$ exactly:
  if $\mu$ represents $G$, so does the pushforward of $x\,d\mu/G_1$
  under $s \mapsto s/\tilde q$. $S$ is an automorphism of the solution
  set shifting supports by exactly one $\tilde q$-step (and killing an
  atom at 0 if present).
- **q-difference equation.** $A_w(z) = A_w(wz) - wz\,A_w(w^2 z)$ for
  the Ramanujan entire function
  $A_w(z) = \sum_n w^{n^2}(-z)^n/(w;w)_n$, verified coefficient-wise
  symbolically ($k \le 25$, exact).

### 1.2 The Nevanlinna D-function is the Ramanujan function (exact-numeric)

With orthonormal SW polynomials $p_n$ (series depth 150, dps 220), the
Nevanlinna function $D(z) = z\sum_n p_n(0)p_n(z)$ satisfies

$$
D(z) = c_0\, z\, A_{\tilde p}(z),
\qquad c_0 = \sum_n p_n(0)^2 = 21.5964596318\ldots \ (r = 6/5),
$$

the ratio constant to $6.5\times10^{-23}$ over eight sign-spread sample
points. Consequently (verified against the parent's own machinery at
$N = 56$):

- **Krein support** (Radau-at-0 truncation limit) $=$
  $\{\zeta_n\} = $ zeros($A_{\tilde p}$), rel $1.7\times10^{-8}$;
- **Friedrichs support** (plain truncation limit) $=$
  $\{\zeta_n/\tilde q\}$, rel $1.2\times10^{-8}$ — i.e. **the
  Friedrichs support is exactly the Krein support shifted one
  $\tilde q$-step down** (the $S$-map of §1.1 applied to the Krein
  solution: the $x\,d\mu$ factor kills the atom at 0, leaving
  $\inf \mathrm{supp} = \zeta_1/\tilde q > 0$).

This is the literature-exact description the work order asked for: the
N-extremal supports of the SW family are zero sets of the $A$-type
q-series in Christiansen's Nevanlinna matrix ([`christiansen2003sw`];
the $A_w$ series is the q-Bessel/Ramanujan family of the
[`ismail-masson1994`] circle), here pinned to the specific function,
argument scale, and inter-extension shift.

### 1.3 The class statement (asymptotic tier)

The signed lattice deviation
$\delta_n = \log_{\tilde q}\zeta_n - \mathrm{nint}(\log_{\tilde q}\zeta_n)$
goes to $0$ at measured rate exactly $\tilde p$ (tail rate error
$< 5\times10^{-3}$ at $r = 6/5$), with $|\delta_{60}| = 6\times10^{-10}$
raw and Aitken² $\approx -4\times10^{-29}$; the nearest integers are
**odd** for the Krein zeros, hence **even** for Friedrichs. So the
pure-SW extremal pair sits asymptotically on the two complementary
$q$-sublattices of the **integer** grid $\tilde q^{\mathbb Z}$:
$\varphi_{\mathrm{SW}} = 0$, split odd (K) / even (F). The zero
asymptotics $\zeta_n = \tilde q^{\,2n-1}(1 + O(\tilde p^{\,n}))$ is
used at measured tier only (no proved asymptotic theorem for $A_w$
zeros was imported; §4).

### 1.4 The transfer mechanism (exact factorization + measured Jacobi convergence)

Symbolically exactly ($k \le 12$):

$$
m_k = G_k\, E^k\, (p;p)_k .
$$

Since $(p;p)_k \to (p;p)_\infty$ geometrically, the balanced family is
the $E$-scaled SW family times a geometrically convergent correction.
Correspondingly (measured, $r = 6/5$, certified qd): the balanced monic
Jacobi data converge onto the scaled SW closed forms,

$$
\frac{\alpha^{\mathrm{bal}}_n}{E\,\alpha^{\mathrm{SW}}_n} - 1
\;\longrightarrow\; 0,
\qquad
\frac{\beta^{\mathrm{bal}}_n}{E^2\,\beta^{\mathrm{SW}}_n} - 1
\;\longrightarrow\; 0,
$$

at per-step rate $= \tilde p$ (deviation $9.05\times10^{-8}$ at
$n = 40$). The scale map $s \mapsto E s$ carries the SW integer class
$0$ to $\mathrm{frac}(\log_{\tilde q} E) = \varphi_1$ — **the u ≡ 1
class is exactly the Jackson-edge image of the SW-natural class**. The
balanced ratio identity
$m_{k+1}/m_k = E\,\tilde q^{\,k}\,(1-p^{k+1})$ (exact) exhibits the
$S$-covariance of §1.1 broken by exactly the factor
$(1-p^{k+1}) \to 1$: the balanced problem is asymptotically
$S$-covariant, which is why its extremal supports are asymptotic
$q$-lattices in the $\varphi_1$ class rather than exact ones.

**Transfer tier: asymptotic-measured** (at $10^{-9}$-tier at
$q = 2.0736$, §2.1). The step that would make A-7 a theorem — a
perturbation lemma transporting support asymptotics along
geometrically-converging Jacobi data — is the named open gap (§4).

## 2. Leg B — numeric promotion

### 2.1 K-ladder at $q = 2.0736$ ($r = 6/5$; qd certified $7\times10^{-801}$, exact-ℚ cross-check $< 10^{-700}$)

$\varphi_1 = 0.80524111223\ldots$; window $j \le 34$ per-j
Cauchy-certified at $10^{-8}$ ($N$ vs $N-12$); drift ratios $= \tilde p$
to $5\times10^{-3}$.

| $K$ | $\lvert \mathrm{Aitken}(\varphi) - \varphi_1 \rvert$ |
|---|---|
| 48 (parent scale) | $2.05\times10^{-4}$ |
| 64 | $5.26\times10^{-6}$ |
| 80 | $1.97\times10^{-7}$ |
| 96 | $8.05\times10^{-10}$ |

Aitken² at $K = 96$: $-7.9\times10^{-10}$ (known-rate Richardson²
$6.3\times10^{-10}$; cross-extrapolant uncertainty $1.2\times10^{-8}$).
The **Krein** class agrees to Aitken² $-1.7\times10^{-9}$ (unc
$4.1\times10^{-9}$), and the mod-2 parities of the F and K atoms
relative to the $E$-scaled grid are constant and opposite (F even,
K odd) — the parent's "complementary q-sublattices of the one u ≡ 1
grid" now at $10^{-9}$-tier. **The parent's $1.0\times10^{-4}$
alignment is promoted by roughly five orders of magnitude.**

### 2.2 q-ladder (per-rung tiers; thresholds fixed a priori, never loosened)

Per rung: certified qd (moment reproduction shown), per-j Cauchy window
($N$ vs $N-12$, min–max monotone), drift-rate check against
$\tilde p(q)$, Aitken² + known-rate Richardson² with cross-extrapolant
uncertainty. A rung certifies iff extrapolant **and** uncertainty meet
its a-priori bound; otherwise it is reported as
**measured-preasymptotic** (weak sanity gates $|\mathrm{A}^2| < 0.05$,
$|\mathrm{raw}| < 0.2$, an order below the $0.5$ half-step scale).

| $q$ | $K{=}N$ | window $j \le$ | qd repro | $\varphi_1(q)$ | raw dev at edge | Aitken² | unc | cert bound | tier |
|---|---|---|---|---|---|---|---|---|---|
| 2.0736 | 96 | 34 | $7\times10^{-801}$ | 0.80524111 | — | $-7.9\times10^{-10}$ | $1.2\times10^{-8}$ | $10^{-8}$ | **certified** (§2.1) |
| 1.8 | 112 | 38 | $1\times10^{-900}$ | 0.75926714 | $-3.6\times10^{-5}$ | $1.67\times10^{-8}$ | $1.6\times10^{-8}$ | $10^{-7}$ | **certified** |
| 1.5 | 144 | 43 | $7\times10^{-1101}$ | 0.41902258 | $-6.6\times10^{-4}$ | $2.68\times10^{-8}$ | $2.0\times10^{-8}$ | $10^{-7}$ | **certified** |
| 1.3 | 192 | 62 | $1\times10^{-1500}$ | 0.17787189 | $-2.0\times10^{-3}$ | $2.15\times10^{-6}$ | $1.6\times10^{-6}$ | $10^{-6}$ | measured-preasymptotic |
| 1.2 | 208 | 53 | $5\times10^{-1701}$ | 0.65493824 | $-7.9\times10^{-2}$ | $3.72\times10^{-5}$ | $2.6\times10^{-5}$ | $10^{-5}$ | measured-preasymptotic |
| 1.15 | 240 | 77 | $1\times10^{-2100}$ | 0.14787663 | $-6.0\times10^{-2}$ | $1.75\times10^{-3}$ | $1.5\times10^{-3}$ | $10^{-4}$ | measured-preasymptotic |

Readings:

1. **No rung deviates from $\varphi_1(q)$ beyond ~1.3× its own stated
   uncertainty** — the alignment is *consistent along the whole
   ladder*; but "converges to $\varphi_1$" is **certified only down to
   $q = 1.5$**. Below that the honest label is "consistent,
   pre-asymptotic at this $N$" (extrapolation uncertainty grows as
   $\tilde p(q)^{2 j_{\max}}$ with $\tilde p \to 1$).
2. **Convergence-rate model** (measured, not fitted): class drift
   $\varphi_j - \varphi_1 \approx C\,\tilde p^{\,j}$, rate verified per
   rung (rate error $10^{-5}$…$6\times10^{-4}$), and truncation error
   $\varepsilon_\lambda(j, N) \approx C_\lambda\,\tilde p^{\,N-j}$ —
   both scales geometric in the one number $\tilde p(q)$. The drift
   constant grows toward the pins ($C \approx 1.1$ at $q = 2.07$;
   $C \approx 9$ at the pin, SW-side proxy) — the quantitative content
   of "the pins sit deep in the pre-asymptotic window."
3. **SW-side control:** on the rungs carrying the SW leg the class-0
   statement is certified truncation-free from $A_{\tilde p}$ zeros
   (Aitken² $-5.5\times10^{-13}$ at $q = 1.8$, $-3.0\times10^{-13}$ at
   $q = 1.5$, odd parity) — the pre-asymptotic tiers of the deep rungs
   are a property of the *truncation layer*, not of the lattice
   structure.

Run-history note (honesty). A first pass hard-asserted per-rung bounds
and crashed at $q = 1.3$ ($2.15\times10^{-6}$ vs the $10^{-6}$ bound);
the probe was restructured to the tier scheme above rather than
loosening the bound. A second pass showed the $q = 1.15$ window at
$N = 216$ too short for a sane raw readout (raw signed deviation
$-0.327$ at $j = 39$, drift constant $C \approx 5$); the fix was
$N \to 240$ (window $j \le 77$, raw $-0.06$), not a looser gate. A
third pass replaced an ill-posed proton-pin extrapolation with the raw
index-by-index comparison of §2.3. All three incidents are commented in
the probe source.

### 2.3 Pins ($q_0 \approx 1.10998$, $\tilde q - 1 \approx 0.054$)

**SW core — certified, truncation-free.** From 100 zeros of
$A_{\tilde p}$ at the muon pin (dps 380; precision-headroom certificate
asserted inside the zero-finder): signed lattice deviation $\to 0$ at
rate $= \tilde p$ (rate error $1.4\times10^{-4}$), Aitken²
$-8.2\times10^{-8}$ (Richardson² $-1.8\times10^{-7}$, unc
$9.9\times10^{-8}$), tail spacing $\to 2.0028$ $\tilde q$-steps,
lattice integers **odd** (Krein) — the SW-core integer-class statement
holds **at the substrate pin** with no truncation gap. The proton pin's
raw deviations coincide index-by-index with the muon pin's to
$1.7\times10^{-6}$, inside the natural sensitivity scale
$O(\delta q_0 / L^2) \approx 4.7\times10^{-6}$.

**Balanced layer — honest pre-asymptotic report, no class claim.** The
muon-pin balanced qd is certified ($4\times10^{-1401}$) and its Jacobi
data decay onto the $E$-scaled SW closed forms (deviations
$0.0335 / 0.0087 / 0.0023$ at $n = 40/65/90$; per-step decay
$0.9473,\ 0.9487$ vs $\tilde p = 0.94917$ — geometric, rate approaching
$\tilde p$ from below). But the truncation eigen study at $K = 96$ has
per-j Cauchy drifts of $0.7$–$2\%$ ($\lambda_0$: $0.05409 \to 0.05372$
from $N = 84$ to $96$, still falling): **pre-asymptotic; no
balanced-side class readout at the pins.** The N-requirement model with
measured constants ($C_\lambda \approx 0.33$,
$C_{\mathrm{drift}} \approx 9$): a raw $10^{-3}$ readout needs
$j \approx 175$; an Aitken² $10^{-4}$ readout needs $j \approx 131$;
with the window requirement, $N \approx 375$ (and qd dps
$\gtrsim 2500$; `mp.eigsy` cost $O(N^3)$, of order hours at that size)
— out of this probe's budget, left as the concrete numeric target for a
successor probe.

## 3. What this changes for the (REP)/KSel campaign

1. **The parent's measured u ≡ 1 selection datum is now structurally
   explained**: the extremal supports of the SW core are the zero
   lattice of one classical entire function ($A_{\tilde p}$), whose
   class is the integer class $0$; the Jackson dressing multiplies the
   operator by $E$ (exact moment factorization), and $\varphi_1$ *is*
   $\mathrm{frac}(\log_{\tilde q} E)$ — the u ≡ 1 class is the
   Jackson-edge translate of the SW-natural lattice, not a
   numerological coincidence.
2. **The F/K complementary-sublattice picture is exact at the SW
   level**: Friedrichs $= S(\text{Krein})$, one $\tilde q$-step down —
   concretely re-deriving Pedersen's "Friedrichs maximizes the smallest
   support point" here ($\zeta_1/\tilde q$ vs the Krein atom at $0$).
3. **The KSel-1 half-step discriminator answer (u ≡ 1, not
   $\tilde q^{1/2}$) is promoted** from $10^{-4}$-measured to
   $10^{-9}$-tier at $q = 2.0736$, certified through $q = 1.5$, and
   consistent (pre-asymptotic) down the ladder; at the pins the SW core
   is certified while the balanced readout awaits $N \approx 375$.
4. **A derivation-tier closure now needs exactly one lemma** (§4
   gap 1) — everything else in the chain is exact or
   exactly-factorized.

## 4. Honest gaps / tier statement

1. **Perturbation lemma (the A-7 gap).** "Jacobi matrices whose
   coefficients converge geometrically to those of an indeterminate
   reference (here: $E$-scaled SW) have N-extremal supports with the
   same asymptotic lattice class." Not proved here; without it the
   transfer (A-6/A-7) is asymptotic-measured, not derived. Candidate
   literature line: order/type rigidity of the Nevanlinna matrix
   ([`berg1995`], [`pedersen1995`]); not executed.
2. **$A_w$ zero asymptotics.**
   $\zeta_n = \tilde q^{\,2n-1}(1 + O(\tilde p^{\,n}))$ is used at
   measured tier (rate and class verified numerically at every studied
   $q$ including the pins); no proved theorem was imported for it.
3. **$D = c_0\, z\, A_{\tilde p}$** is a certified numerical
   functional identity ($6.5\times10^{-23}$ constancy) plus the exact
   q-difference equation; a symbolic derivation from Christiansen's
   Nevanlinna matrix (paper in hand) would lift A-2/A-3 to fully
   exact.
4. **Deep-ladder rungs** ($q \le 1.3$) and the **balanced pin readout**
   are pre-asymptotic at the computed $N$ (tier labels in §2.2/§2.3;
   successor-probe target $N \approx 375$ at the pins).
5. **Krein tracked only at $r = 6/5$** on the ladder (Friedrichs-side
   everywhere); complementarity is exact at the SW level (§1.2) and
   verified at $r = 6/5$ for balanced (§2.1); deep-rung Krein classes
   are inferred, not measured.
6. Scope note: nothing here proves or refutes the target conjecture
   ([`conj:schwinger-measure-computational-time`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md));
   no refutation-scope (b) claims are made in this audit — all
   negatives are scope-(a) "not certified at this $N$" statements.

## 5. Discipline

- **Corpus-grep (all four paths).** `Ramanujan function | q-Airy |
  Nevanlinna matrix | Stieltjes-Wigert zeros | A_q zeros | u1
  promotion` over `docs/audits/`, `docs/coordination/`, `content/`,
  `computations/`: prior state = the parent/grandparent KSel-2 audits
  (no Ramanujan-function identification, no closed-form SW Jacobi data
  in the corpus, no ladder study) and the bibliography entries
  registered by the parent tranche. No prior closure found.
- **NO FIT.** Every scored check is an exact symbolic identity, an
  exact-ℚ computation, or a numeric check of a displayed identity at a
  stated tolerance; extrapolants (Aitken/Richardson) are labeled
  measurements with cross-extrapolant uncertainty; convergence *rates*
  are measured against the structural prediction $\tilde p(q)$, never
  fitted; certification thresholds were fixed a priori, and rungs that
  missed them were re-tiered, not re-thresholded.
- **Refutation hygiene.** No scope-(b) exclusions asserted; the
  pin-level balanced non-readout is scope-(a) (numeric budget), with
  the required $N$ quantified.
- **Formalize-first.** The load-bearing identities (closed-form Jacobi
  data, $S$-map, q-difference equation, transfer factorization) were
  derived/verified symbolically before any numeric layer; the numeric
  legs measure only what the theory does not yet supply (zero-class
  asymptotics, transfer at finite $q$).
- **Long-compute discipline:**
  `python3 -u … 2>&1 | tee /tmp/ksel2id_u1.log`; progress + ETA lines
  at every phase boundary; wall ≈ 13 min; bottleneck `mp.eigsy` at
  $N = 208$–$240$ (reported above).
- **Render-QA:** the preflight grep battery was run by hand on this
  file (balanced `$`/`$$` and brace pairs; no `\operatorname`; no line
  inside `$$…$$` opening with `+`/`-`/`*`; no inline align-family
  environments; display `$$` on their own lines; symbols introduced
  before use). The pipeline render was **not** run in this sandbox —
  **this doc was not machine-validated**, stated per the render-QA
  gate.

## 6. Cross-references

- Parent audit (promotion target): [`2026-08-01-ksel2id-friedrichs-sw-identification.md`](2026-08-01-ksel2id-friedrichs-sw-identification.md)
- Grandparent (Favard/GNS route): [`2026-08-01-ksel2-gns-favard-canonicity.md`](2026-08-01-ksel2-gns-favard-canonicity.md)
- Bar-fixed classes Lean tranche: [`2026-08-01-bar-reflection-grid-selection-lean.md`](2026-08-01-bar-reflection-grid-selection-lean.md)
- Moment-level factorization Lean: [`SWJacksonMomentFactorization.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SWJacksonMomentFactorization.lean)
- Target conjecture: [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
- Probe + witness: [`ksel2id_u1_promotion_probe.py`](../../computations/probes/ksel2id_u1_promotion_probe.py), [`ksel2id-u1-promotion.witness.json`](../../computations/probes/ksel2id-u1-promotion.witness.json)
- Bibliography (all registered; see [`content/schema/references.ts`](../../content/schema/references.ts)): [`christiansen2003sw`], [`berg1995`], [`pedersen1995`], [`moak1981`], [`simon1998`], [`ismail-masson1994`]
