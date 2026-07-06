# Deriving the gauge (143) vs scalar (171) mass factors from categorical chains

**Date:** 2026-05-24
**Trigger:** Per [PR #1126 retraction audit §3.B](2026-05-24-pr1122-retraction-and-existing-canonical-adaptation.md) + [PR #1128 binomial cherry-pick](https://github.com/litlfred/qou/pull/1128) finding:

```
gauge bosons (W, Z): mass / P_m(h_0) ≈ 143  (within 1%)
Higgs scalar (H):    mass / P_m(h_0) ≈ 171  (within 1%)
ratio 171 / 143    ≈ 1.196
```

The two distinct factors split the SM mass spectrum into **gauge boson class** vs **scalar class**. Neither factor is currently derived; both are empirical fits to SM data. This audit lays out the categorical derivation path.

## §1. What's needed

Per `TorusKnotMass` class fields ([`TorusKnotMass.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/TorusKnotMass.lean), this branch):

- `gauge_mass_factor : ℝ` — the 143 constant
- `scalar_mass_factor : ℝ` — the 171 constant
- `factors_distinct` — they're genuinely different

For instance construction, we need categorical chains supplying:

1. The **gauge factor 143**: derives from $g, g'$ (SU(2)_L × U(1)_Y couplings) + the trace polynomial structure
2. The **scalar factor 171**: derives from $\lambda$ (Higgs self-coupling) + the same trace polynomial structure
3. The **ratio 171/143 ≈ 1.196**: a categorical statement tying gauge to scalar normalization

## §2. SM expressions to match

In the Standard Model:

$$
m_W = \frac{g v}{2}, \qquad m_Z = \frac{\sqrt{g^2 + g'^2}\,v}{2}, \qquad m_H = \sqrt{2\lambda}\,v
$$

Equivalently:

$$
\frac{m_W^2}{v^2/4} = g^2, \qquad \frac{m_Z^2}{v^2/4} = g^2 + g'^2, \qquad \frac{m_H^2}{v^2/2} = 2\lambda
$$

With $v \approx 246\;\text{GeV}$ and the measured masses, the SM gives:
- $g^2 \approx (2 \cdot 80.38 / 246)^2 \approx 0.4271$ ⇒ $g \approx 0.6535$
- $g^2 + g'^2 \approx (2 \cdot 91.19 / 246)^2 \approx 0.5499$ ⇒ $g'^2 \approx 0.1228$ ⇒ $g' \approx 0.3504$
- $2 \lambda \approx (125.1 / 246)^2 \cdot 2 \approx 0.5172$ ⇒ $\lambda \approx 0.2586$

These are the SM gauge couplings and Higgs self-coupling at the EW scale.

## §3. Connection to the trace polynomial P_m(h_0)

The empirical finding (PR #1128):

$$
\frac{m_W}{P_2(h_0)} = \frac{m_Z}{P_3(h_0)} \approx 143, \qquad \frac{m_H}{P_4(h_0)} \approx 171
$$

Substituting $m_W = gv/2$:

$$
\frac{g v / 2}{P_2(h_0)} = 143 \;\Rightarrow\; g v = 286 \cdot P_2(h_0) = 286 \cdot 0.5662 \approx 161.93\;\text{GeV}
$$

vs SM $gv = 0.6535 \cdot 246 \approx 160.76\;\text{GeV}$ — match within 0.7%.

Similarly for the scalar:

$$
\frac{\sqrt{2\lambda}\,v}{P_4(h_0)} = 171 \;\Rightarrow\; \sqrt{2\lambda}\,v = 171 \cdot 0.7320 \approx 125.17\;\text{GeV}
$$

vs SM $\sqrt{2\lambda}\,v = m_H = 125.10\;\text{GeV}$ — exact.

So the 143 and 171 constants are **structurally tied to specific SM phenomenological combinations**:

$$
143 = \frac{g v / 2}{P_2(h_0)} \;\Leftrightarrow\; g v = 2 \cdot 143 \cdot P_2(h_0)
$$
$$
171 = \frac{\sqrt{2 \lambda}\,v}{P_4(h_0)}
$$

## §4. Three derivation paths

### Path A: $v$ from substrate (research-grade)

If the VEV $v$ can be derived from substrate $q_0$ via the
`CategoricalHiggsIdempotent.vev_v_GeV` field, then the 143 and 171
constants reduce to:

$$
143 = \frac{g}{2 \cdot P_2(h_0)} \cdot v(q_0), \qquad 171 = \frac{\sqrt{2\lambda}}{P_4(h_0)} \cdot v(q_0)
$$

Substrate-derivation of $v$ is currently NOT in the framework. Per the
2026-05-08 substrate-derivation declination, this path is OUT OF SCOPE
unless the author reopens it.

### Path B: gauge couplings $g, g'$ from categorical chain (research-grade)

If $g, g'$ can be derived categorically from the substrate (e.g., from
the categorical action of $G = \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$
on the Frobenius–Hopf substrate), then the 143 factor becomes a
substrate-derived prediction:

$$
143 = \frac{g(q_0)}{2 \cdot P_2(h_0)} \cdot v
$$

where $v$ is still external (CAL-4 calibration). This is the
**conditional** path: derive $g, g'$ structurally; treat $v$ as input.

The categorical derivation of $g, g'$ would proceed via:
1. The 2-form on Bring's surface encoding the SU(2)_L bundle structure
2. The Chern–Simons level $k$ for the U(1)_Y line bundle
3. The induced couplings at the substrate $q_0$

Effort: research-grade, multi-week.

### Path C: ratio $\lambda / g^2$ from categorical chain (the most-tractable)

The ratio $171 / 143 \approx 1.196$ doesn't require knowing $v$
absolutely. Working out the ratio:

$$
\frac{\text{scalar factor}}{\text{gauge factor}} = \frac{m_H / P_4(h_0)}{m_W / P_2(h_0)} = \frac{P_2(h_0)}{P_4(h_0)} \cdot \frac{m_H}{m_W} = \frac{P_2}{P_4} \cdot \frac{\sqrt{2\lambda}\,v}{g v / 2} = \frac{2 \sqrt{2\lambda}}{g} \cdot \frac{P_2}{P_4}
$$

Numerically: $\frac{P_2}{P_4} = 0.5662/0.7320 = 0.7734$. So:

$$
\frac{171}{143} = \frac{2\sqrt{2\lambda}}{g} \cdot 0.7734 \Rightarrow \frac{\sqrt{2\lambda}}{g} = \frac{171/143}{2 \cdot 0.7734} = \frac{1.196}{1.547} = 0.7731
$$

i.e., $\sqrt{2\lambda} / g \approx 0.7731$. This is a **dimensionless ratio of SM couplings** that the framework could potentially derive.

Numerical check: $\sqrt{2\lambda} = \sqrt{0.5172} \approx 0.719$; $g \approx 0.6535$; ratio $\approx 1.100$. **Mismatch ~30%** — the formula
$$
\frac{171}{143} = \frac{2\sqrt{2\lambda}}{g} \cdot \frac{P_2}{P_4}
$$
does NOT hold under the SM values. The 143/171 split is more subtle than this simple combination.

## §5. Honest reassessment

The 143 / 171 empirical split is real (PR #1128 verified). The **derivation** of these constants from substrate is more complex than the SM-coupling relations above suggest:

- The SM relations $m_W = gv/2$ etc. are with $v = 246$ GeV (external constant)
- The framework's prediction $m_W = 143 \cdot P_2(h_0)$ comes from a DIFFERENT route (trace polynomial)
- The framework's $v$ is implicit in the 143 constant; it's NOT the SM v

If the framework's 143 is interpreted as a categorical analog of $gv/2$, then:

$$
v_{\text{framework}} = \frac{2 \cdot 143}{g} = \frac{286}{0.6535} \approx 437\;\text{GeV}
$$

— different from the SM $v = 246\;\text{GeV}$ by a factor of 1.78. This factor 1.78 ≈ $\sqrt{2 \cdot e/\sqrt{2}} \cdot \ldots$ — no clean ratio jumps out.

**Honest assessment**: the 143 and 171 constants encode SM phenomenology specific to the QOU framework's RT-route. Deriving them from substrate would require simultaneous determination of $g, v, \lambda$ — beyond the scope of the trace-polynomial chain alone.

## §6. Recommendation

**Don't promote** the 143/171 split as a structural identity. Treat it as:

- A **per-particle-class normalization** that the `TorusKnotMass` instance must supply (per Lean class field)
- An **empirical pattern** suggesting the framework's RT-route DOES respect the gauge-vs-scalar SM split
- A **research-grade target** for future categorical derivation (Path A/B/C all queue here)

The cleanest **structurally-defensible** statement that survives this audit:

> The framework's RT-route trace polynomial $P_m(h_0)$ on $T(2, 2m)$
> torus links reproduces the SM mass ratio $m_W/m_Z = \cos\theta_W$
> within ~1% via the binomial pattern alone (sibling PR #1125, this
> session PR #1128). The absolute mass scale, the W/H and Z/H ratios,
> and the gauge-vs-scalar normalization split remain open structural
> questions requiring categorical derivation of $g, g', \lambda, v$.

## §7. Cross-references

- [PR #1128](https://github.com/litlfred/qou/pull/1128) — binomial cherry-pick → W/Z within 1%
- [PR #1126](https://github.com/litlfred/qou/pull/1126) retraction audit §3 — adapts existing classes
- [PR #1125](https://github.com/litlfred/qou/pull/1125) (sibling) — binomial pattern sympy proof
- [`CategoricalHiggsIdempotent.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/CategoricalHiggsIdempotent.lean) (refined this branch) — encodes v, g, g', λ structurally
- [`TorusKnotMass.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/TorusKnotMass.lean) (new this branch) — encodes 143/171 + WZ_mass_ratio fields
- [`rt_binomial_trace_evaluation_probe.py`](../../computations/probes/rt_binomial_trace_evaluation_probe.py) — empirical measurement
