**Definition (Quantum dilogarithm disambiguation).**
*Two distinct functions appear in the QOU mass formulae and must not be conflated:*

| Name | Symbol | Closed form | Behaviour near $z = 1$ |
|---|---|---|---|
| **Quantum dilogarithm product** | $\Phi_q(z)$ | $\prod_{k=1}^{\infty} (1 - q^{-k}z)^{-1}$ | Unbounded ($\Phi_q(0.989) \approx 6.7 \cdot 10^5$ at $q_0$) |
| **Symmetric q-dilogarithm (Kashaev limit)** | $\mathrm{Li}_2^q(z)$ | $\sum_{n \geq 1} \dfrac{z^n}{n \cdot [n]_q}$ | Bounded; $-\mathrm{Li}_2^q(-z) \in [0.1, 0.82]$ for $z \in (0,1)$ at $q_0$ |

*The historical paper-level identity:*
$$
  \Phi_q(z) \;\stackrel{?}{=}\; \int_0^z \frac{\ln_q(1+t)}{t}\,dt
       \;\stackrel{?}{=}\; \prod_{k\geq 1}(1 - q^{-k}z)^{-1}
$$
*is **false**. The integral evaluates to the bounded quantity $-\mathrm{Li}_2^q(-z)$, not the unbounded $\Phi_q(z)$. The two sides differ by six orders of magnitude at $z = 0.989$.*

## Discipline

The canonical form of the mass-endomorphism tower uses $-\mathrm{Li}_2^q(-|V|)$, never $\Phi_q(|V|)$, for every per-generator amplitude.

The $\Phi_q$ product form explains the $\sim 10^5 \times$ amplification at $|V| \to 1$ that originally caused the $-737$ MeV pathology. The corrected canonical mass formula abandons it entirely.
