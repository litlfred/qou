Let $R$ be a field and $q \in R^\times$. Writing the substrate Planck quantum $\hbar_q = (q - 1)/q$, we have:
$$
  1 + \hbar_q - \hbar_q^2/2
  \;=\;
  1 + \frac{1 - q^{-2}}{2}
  \;=\;
  \frac{3 - q^{-2}}{2}
  \;=\;
  \frac{3 q^2 - 1}{2 q^2}.
$$
Substituting this closed form into the meson mass-squared ratio gives:
$$
  \frac{m_K^2}{m_\pi^2}
  \;=\;
  [3]_q \cdot [4]_q
  \;+\;
  \frac{\alpha_{\mathrm{em}}}{\pi}
  \cdot
  \frac{3 q^2 - 1}{2 q^2}.
$$
The strong fusion $[3]_q \cdot [4]_q$ is framework-derived and Lean-proved; it supplies $\approx 99.98\%$ of the ratio (the EM term is a $\approx 203$ ppm correction).

**Scope of the EM term (accuracy caveat).** The $\alpha_{\mathrm{em}}$ entering the EM correction is the *measured* (CODATA / CS-corrected) fine-structure constant, not the framework's own derived value. This matters for accuracy claims: substituting the derived $\alpha_{\mathrm{em}}^{-1} = q\,[9]_q\,[10]_q \approx 136.82$ (itself $\approx 1553$ ppm from CODATA) degrades $m_K^2/m_\pi^2$ from $\approx 47$ ppb to $\approx 363$ ppb ($\sim 8\times$). So the ratio's L2-100× pass is *$\alpha_{\mathrm{em}}$-anchored*, not parameter-free, and the factor $\tfrac{3q^2-1}{2q^2}$ is the leading two-term truncation of $1 + \log(1 + \hbar_q)$ (the full series fits worse). Full dissection: [`docs/audits/2026-08-02-ppq-attack-vectors-roast.md`](../../../docs/audits/2026-08-02-ppq-attack-vectors-roast.md) §Roast 1.
