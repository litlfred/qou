The [depth–period correspondence](#conj:gb-depth-period-correspondence) asserts an inclusion $\tau_{\mathrm{arch}}(G^{(n)}) \subseteq \mathcal{P}_n$ plus a sharpness condition. The sharpness condition admits two formulations:

| Version | Statement | What it says |
|---|---|---|
| **Soft sharpness** | $\tau_{\mathrm{arch}}(G^{(n)}\rvert_F) \neq 0$ in $\mathcal{P}_n / \mathcal{P}_{n-1}$ for each Bring-natural $F$ | image is non-trivial at depth $n$ |
| **Strong sharpness** | image equals $\mathcal{P}_n / \mathcal{P}_{n-1}$ | image generates the full period quotient |

The soft version is theorem-level ([soft sharpness](#prop:b1-soft-sharpness-theorem)) via Borel's theorem and polylog non-vanishing. The strong version remains conditional, but the soft version suffices for QOU's predictive purposes.

Soft sharpness elevates the following consequences of the correspondence to theorems:

| Claim | Status before | Status after this prop |
|---|---|---|
| Each Bring-natural row of the depth correspondence lands non-by definition at its depth | conjectural | **theorem** |
| Per-knot $\mathrm{Vol}(K) \neq 0$ in $\mathcal{P}_2/\mathcal{P}_1$ for hyperbolic Bring-embeddable $K$ | conjectural (within the depth correspondence) | **theorem** (Bloch–Wigner non-vanishing) |
| $\mathrm{Cl}_3(2\pi/5)$ lives non-by definition in $\mathcal{P}_3/\mathcal{P}_2$ | conjectural | **theorem** (Borel + Lewin) |
| Each numerical witness in the [transcendental accounting](#rem:transcendental-accounting) ledger lands at the predicted depth | partly conjectural | **theorem** for non-triviality; depth-match is structural |

**Limitations of soft sharpness:**
Strong sharpness ($\tau_{\mathrm{arch}}(G^{(n)})$ equals all of $\mathcal{P}_n / \mathcal{P}_{n-1}$ over arbitrary $F$) remains Beilinson-conjectural. Soft sharpness permits additional periods in $\mathcal{P}_n / \mathcal{P}_{n-1}$ not coming from $\tau_{\mathrm{arch}}(G^{(n)})$. Strong sharpness denies this possibility.

For QOU's predictive use case, this distinction matters only when predicting that some specific period must equal a specific $G^{(n)}$ image. The framework's predictions concern non-trivial classes at specific depths rather than exhausting the period quotient.

**Significance: Goncharov is bigger than QOU needs.**
Goncharov's full conjecture asserts $K_{2n-1}^{\mathrm{ind}}(F) \otimes \mathbb{Q} \cong \mathfrak{B}_n(F) \otimes \mathbb{Q}$ via the Goncharov regulator, for all $F$ and $n$. QOU requires only that each Bring-natural depth-$n$ grouplike value lands non-by definition in $\mathcal{P}_n / \mathcal{P}_{n-1}$. This soft sharpness is a theorem of Borel + Lewin.

The soft version ensures QOU's framework predictions are non-vacuous. The strong version is required to claim the framework is complete. The latter is Goncharov-conditional; the former is unconditional.
