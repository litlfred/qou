# The Universal Binding Architecture

It is a classical observation that the mass scales of the weak and strong interactions appear phenomenologically decoupled. This section proposes a candidate common structure (a $q$-difference generating function whose kernel is built from torus-knot traces) and states carefully which of its ingredients are *derived*, which are *empirical modeling inputs*, and which remain *open*. The genuinely fit-free part of the per-isotope binding is the linear-chain bond-count law of [linear-chain bond-count multiplicity](#prop:linear-chain-bond-count) ($B = m_e\sum_n (n-1)\,\mathrm{Vol}_n$, which reproduces $^3$H to $0.16\%$ with zero parameters); the recursion below is a compact organizing ansatz for that data rather than an independent first-principles closure.

## 1. The Torus-Knot Trace Ratios

Let $T_{p,q}$ denote the $(p,q)$-torus knot. Evaluating the relevant Markov traces at $q=1$ gives the ratios

1. **Weak channel:** $\lim_{q \to 1} \frac{\mathrm{tr}(T_{3,5})}{\mathrm{tr}(3_1)} = \frac{10}{3}$.
2. **Strong gluonic channel:** $\lim_{q \to 1} \frac{\mathrm{tr}(T_{2,9})}{\mathrm{tr}(T_{2,3})} = 3$.
3. **Strong residual channel:** $\lim_{q \to 1} \frac{\mathrm{tr}(T_{2,5})}{\mathrm{tr}(T_{2,2})} = \frac{5}{2}$.

Because $\mathrm{tr}(T_{2,n})|_{q=1} \propto n$, the $q=1$ values above are exactly the index ratios $9/3$ and $5/2$ of the chosen $(2,n)$ knots. The ratios are therefore *computed* invariants, but the **assignment of a particular knot pair to each interaction channel is a modeling input rather than a derivation**: nothing here fixes why $T_{2,9}/T_{2,3}$ is "gluonic" or $T_{2,5}/T_{2,2}$ is "residual." Any first-principles status requires deriving that assignment.

## 2. The q-Difference Generating Function

Let $G(x; q)$ be the generating function for the binding hierarchy, satisfying a $q$-difference equation
$$ G(qx) = R(q,x)\,G(x) $$
whose boundary kernel $R(q,x)$ is built from the ratios of §1. Unrolling $G$ into a power series induces a depth-$2$ linear recurrence, formalized as the `CKRecursion` operator; the bar-even parity of the kernel fixes the base prior $a_0 = 1/2$.

**Organizing ansatz.** The same depth-$2$ operator, seeded per channel, is used to compactly represent both the weak precision coefficients and the strong multi-body binding weights $w_n$.

**Weak channel.** Seeding with $10/3$ yields a coefficient $c_3 = 10/3$ in this construction. **Note (glyph collision):** this $c_3$ is *not* the bar-odd $Q_\beta$ precision-ladder coefficient, whose canonical value is the near-match $c_3 \approx -2 = J_{\mathrm{Hopf}}(q{=}1)$ (see the $c_k$ truncation-order framing); the two share a symbol but are different objects, and no identification between them is claimed.

**Strong channel.** With $r_{\text{res}}$ the residual trace *evaluated at the aether $q_0$* (numerically $r_{\text{res}} \approx 2.596$, which differs by $3.8\%$ from the $q=1$ limit $5/2$ of §1), the recurrence reads
$$ w_{n+1} = \tfrac{1}{2} w_n + r_{\text{res}}\, w_{n-1}. $$
For the $^4$He cluster it gives $w_4 \approx 15.6016$; with a fixed constituent-mass scale this matches the $^4$He binding to $\approx 3.4$ keV ($1.2\times10^{-4}$ relative). This is a **match at the aether value $r_{\text{res}}=2.596$** rather than a prediction from the advertised invariant $5/2$; the $q_0$ value of $r_{\text{res}}$ and the overall scale are inputs, so the $^4$He agreement is a consistency check of the ansatz rather than a parameter-free derivation.

## 3. The A=3 Isospin Splitting: an Empirical Input Rather Than a Derivation

The $\sim 0.76$ MeV binding difference between $^3$H and $^3$He is inserted rather than derived. In $m_e$ units the difference is $B(^3\mathrm{H}) - B(^3\mathrm{He}) = 0.7638\ \text{MeV} = 1.4946\, m_e$, meaning that the "$1.4947\,m_e$ $S_3$/SU(4) representation differential" is exactly the *measured* split relabeled. The algebraic identity $(\text{base}+\text{diff})-\text{base}=\text{diff}$ is a universal ring tautology with $\text{diff}$ an unconstrained free parameter. Per the standing anti-fit discipline (a fitted number relabeled in categorical language is not a derivation) this splitting is recorded as an **open empirical input**; the physical $^3$H/$^3$He difference is moreover Coulomb-dominated. A derived replacement (an isospin split obtained without reference to the measured value) is the open item here.
