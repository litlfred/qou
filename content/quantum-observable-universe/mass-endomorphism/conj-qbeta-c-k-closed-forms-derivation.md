## Derivation paths

Three formal derivation paths stand open:

1. **Khovanov–Rozansky polynomial at finite $q$**: Compute $\mathrm{Kh}(L)(q, t)$ for the typed-$\mathbf{B}_3$ Markov-closure link $L$ at the substrate $q_0$ (not merely $q = 1$). The Taylor coefficients should return $c_4, c_5, c_6, c_7$.
2. **KLR canonical-basis trace formula**: Calculate the per-Wedderburn-block canonical-basis Markov trace at orders $\varepsilon^8, \varepsilon^{10}, \varepsilon^{12}$. The Hecke–KLR bridge supplies scaffolding ([`conj:kazhdan-lusztig-classical-limit`](#conj:kazhdan-lusztig-classical-limit)). We require the explicit per-block trace formula.
3. **Spectral-sequence stratification**: Currently declined; the framework lacks a suitable candidate spectral sequence.

## Precision

The baseline $\mathfrak{Q}_\beta$ categorical prediction achieves a $+6.02$ ppb residual at $N=3$ **against the muon-anchored (ideal-math) $q_0$**. That figure is computed against the muon anchor; under the **experimental (proton-pinned) $q_0$** — the operative
convention — $\mathfrak{Q}_\beta$ currently **misses the 7.8 ppb accuracy target by $\approx 164\times$**. The higher-order corrections ($c_4$ to $c_7$) were tuned to the muon-anchored ladder; their proton-anchored precision is open, not established.

Under the three-calibration discipline, we flag these empirical fits as conditional inputs. Any prediction relying on them must declare this dependency explicitly.

## Evidence

Direct SDP-$T_\beta$ extraction at 50 decimal places reproduces the conjectured $c_k$:

```text
c_2 extracted = -1.0171   (vs framework -1)
c_3 extracted = -2.0098   (vs framework -2 = J_Hopf(q=1))
c_4 extracted = -1.1435   (matches empirical sweep exactly)
c_5 extracted = -1.2229   (matches empirical sweep exactly)
c_6 extracted = +3.4976   (matches empirical sweep exactly)
c_7 extracted = +57.149   (matches empirical sweep exactly)
```

The empirical $c_k$ from `binding_q_target_sweep` are **extracted (fit) against CODATA $\mathfrak{Q}_\beta$ values** by enforcing the precision-ladder structure — a calibration tautology, **not** a derivation. These conjectures supply a categorical *interpretation* of the extracted constants; they do not derive them.
