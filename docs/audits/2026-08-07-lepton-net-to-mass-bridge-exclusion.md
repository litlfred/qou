# The `net(T(2,n)) → lepton mass` bridge does not exist (bean `qou-lsp9`)

**Date:** 2026-08-07
**Bean:** `qou-lsp9` — *"GAP: wire the net(T(2,n)) → lepton mass map"*
**Verdict:** the bean's premise is wrong. A scale factor is not
*missing* from the multiplicative bridge — no such bridge exists, and
the exclusion is **derived from a proved invariant**, not inferred from
a failed search.

## What the bean asked

`prop:lepton-continuant-recurrence` gives the Gröbner–Shirshov normal
form of the lepton-tower braid $T(2,n) = \sigma_0^n$ in $H_2(q)$:

$$
\mathrm{NF}(\sigma_0^n) = a_n \cdot \mathbf{1} + b_n \cdot \sigma_0,
\qquad
b_0 = 0,\; b_1 = 1,\; b_{n+1} = h\,b_n + b_{n-1},\; h = q - q^{-1},
$$

with $a_n = b_{n-1}$ and $\mathrm{net}(T(2,n)) = a_n + b_n$. The corpus
assigns $T(2,3), T(2,5), T(2,7)$ to $e, \mu, \tau$. The sibling probe on
PR #4456 found the net ratios are $1.2455$ and $1.2408$ against observed
$206.8$ and $16.8$, reported the validation as **FAILED**, and
deliberately declined to patch it with a fitted scale factor. `qou-lsp9`
recorded the missing map as a prerequisite to any numerical
falsification.

## 1. The invariant (proved)

Since $h = q - q^{-1}$, the characteristic polynomial $x^2 - hx - 1$ has
roots $q$ and $-q^{-1}$ (sum $h$, product $-1$). Hence the **Binet
closed form**

$$
b_n \cdot (q + q^{-1}) = q^n - (-1)^n q^{-n}.
$$

Sorry-free Lean:
[`morganVoyceBK_binet`](../../content/quantum-observable-universe/lean/QOU/Archimedean/lepton_continuant_binet.lean)
(`lean`-direct exit 0 against the restored `lake-cache/qou-v4-24-0`
oleans). Numerically verified against the recurrence to $7\times10^{-71}$
at 65 dps.

The consequence that matters:

$$
\frac{\mathrm{net}(n+2)}{\mathrm{net}(n)} = q^2\bigl(1 + O(q^{-2n})\bigr).
$$

**The net is log-linear in the winding number, up to an exponentially
decaying remainder.** At the substrate $q_0$ (proton pin), $q_0^2
\approx 1.23205$ and the measured ratios are $1.24547$ and $1.24080$ —
converging on $q_0^2$ from above, the gap shrinking by a factor $q_0^{-2}$
per step.

The observed tower is the opposite shape: log-increments $5.332$ then
$2.822$, i.e. strongly **log-concave**.

## 2. The exclusion

Take the whole multiplicative bridge class

$$
m_n = C \cdot g^n \cdot \mathrm{net}(n)^p,
$$

which covers every power law, every exponential-times-power, and in
particular the "missing scale factor" the bean posits ($p = 1$, $g = 1$).
Ratio rigidity (sorry-free Lean, `mass_ratio_rigidity`):

$$
\frac{m_{n+2}}{m_n} = g^2 \left(\frac{\mathrm{net}(n+2)}{\mathrm{net}(n)}\right)^{p}.
$$

So the step-to-step *variation* of the mass ratio is carried **entirely**
by the variation of the net ratio — which is the $O(q^{-2n})$ remainder,
$0.38\%$ here.

| route | result |
|---|---|
| pure power law ($g=1$), exponent per step | $p = 24.29$ (e→μ) vs $p = 13.08$ (μ→τ) — disagree by $1.86\times$; **no single $p$** |
| full class, both parameters free | solvable, uniquely: $p \approx 667.3$, $g^2 \approx 5.0\times10^{-62}$ |

The class does not fail by having no solution. It fails by requiring an
**exponentially fine-tuned exponent fitted to a vanishing remainder** —
$p$ must absorb a $12.3\times$ effect out of a $1.0038$ ratio, and since
the remainder decays like $q^{-2n}$, the required $p$ grows like $q^{2n}$
for any further generation. That is not a physical map; it is a fit to
noise in a quantity that tends to zero.

Probe: [`lepton_net_to_mass_bridge_exclusion.py`](../../computations/lepton_net_to_mass_bridge_exclusion.py);
witness `computations/lepton-net-to-mass-bridge-exclusion.witness.json`.
$q_0$ is the **experimental/proton** pin per the 2026-08-07 owner
directive; no ideal-layer cache is read, so no layer straddling is
possible.

## 3. Why — the structural diagnosis

$T(2,n)$ are **torus** knots: Seifert-fibred, not hyperbolic, hyperbolic
volume $0$. So the canonical mass route

$$
m(K) = m_e \cdot \mathrm{Vol}(K)\,\rho(K) / \hbar_q^2
$$

supplies **no generation dependence at all** through the lepton's own
identity knot. Consistently with this, the corpus's own working muon
mass does not use the muon's knot: CAL-2's proxy is
$m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ — the figure-eight **Higgs**
knot, which *is* hyperbolic. Mass in this framework enters through the
Higgs-knot coupling, not through the lepton's torus braid.

The continuant net is an amplitude of that torus braid's normal form. It
was never carrying the observable, which is why no scale factor could
repair it.

## 4. Scope (per AGENTS.md §"Before declaring refuted")

- **Scope-(b), structural exclusion — for the multiplicative class
  $m_n = C g^n \mathrm{net}(n)^p$ only.** The cited invariant is the
  proved Binet asymptotics, which forces log-linearity on every member
  of the class.
- **Scope-(a) everywhere else.** This does **not** show the continuant is
  irrelevant to generation structure. The divisibility result — $b_3 \mid
  b_9$, $T(2,9)$ a harmonic of generation 1 — stands untouched; it lives
  at the normal-form level and never claimed to be a mass. And a
  **non-multiplicative** bridge is not excluded: an additive interface
  term, or a Higgs-coupling route where $n$ enters through the linking of
  $T(2,n)$ with $4_1$ rather than through $\mathrm{net}$, remains open.

## 5. What this closes and what it leaves

**Closes:** `qou-lsp9` as posed. There is no scale factor to find; the
bean's framing ("until wired, the ladder has no predictive content")
should be re-read as "the ladder's predictive content cannot come from
the net."

**Leaves open** (new bean filed): the lepton mass tower's actual
generation dependence. The structural hint from §3 is that it should be
sought in the $T(2,n) \leftrightarrow 4_1$ coupling — a linking or
satellite quantity that is *not* multiplicative in a normal-form
amplitude — since that is where the corpus's own working muon mass
already comes from.

**A note on what was deliberately not done.** During this analysis
$(5/3)/\hbar_q = 16.821$ turned up against the observed $m_\tau/m_\mu =
16.817$ (0.024%). It is recorded here only to be dismissed: any target
can be written as $(\text{rational})/\hbar_q$, the $5/3$ has no
derivation, and presenting it as evidence is exactly the numerology the
three-calibration discipline exists to catch. It is not wired anywhere
and should not be revived without a derivation of the $5/3$.
