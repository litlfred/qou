The $q$-weighted method evaluates $\beta^-$ decay $Q$-values from $q$ with zero fitted parameters. The figures in [Table](#tbl:qvalue-observation-table-data) and the first two subsections below record an unregenerated float64 evaluation at the auxiliary loop parameter $z_{\mathrm{aux}} = q^{1/2}/(q+1)$; they are not reproduced at the canonical Markov parameter $z = q^3/(q^2+1)$, whose bare and combined evaluations are tabulated in the [spectral-decomposition interpretation](#rem:spectral-decomposition-qvalue-interpretation).

**Tabulated $q$-weighted evaluation ($z_{\mathrm{aux}} = q^{1/2}/(q+1)$).**

See [Table](#tbl:qvalue-observation-table-data).

At $z_{\mathrm{aux}} = q^{1/2}/(q+1)$ the $q$-weighted table had MAE $\approx 4.4\%$ and RMS $\approx 5.4\%$ (errors $\leq 2.2\%$ for $A \leq 14$), using hard-coded heavy-nucleus factors $F_{\mathrm{deg2}} = 0.5904$ and $F_{\mathrm{Pauli}} = 0.6382$. At the canonical Markov parameter $z = q^3/(q^2+1)$, neither constant holds: the Rosso–Jones ratio evaluates to $F_{\mathrm{deg2}} \approx 3.68442 > 1$ (an amplification rather than a suppression), and the Markov-trace Pauli factor vanishes identically because $y_{(1^3)} = 0$ at $z = q^3/(q^2+1)$.

**Worked example: ${}^{90}\mathrm{Sr}$.**

At $z_{\mathrm{aux}} = q^{1/2}/(q+1)$, the bare $q$-weighted figure $\mathcal{Q}_{\mathrm{bare}} \approx 0.944\,\mathrm{MeV}$ exceeded $\mathcal{Q}_{\mathrm{exp}} = 0.546\,\mathrm{MeV}$ by $+73\%$, and multiplying by $0.5904$ gave $Q \approx 0.557\,\mathrm{MeV}$ ($+2.1\%$). At $z = q^3/(q^2+1)$, using the corollary normalisation $|\log_q(P_{\mathrm{dau}}/P_{\mathrm{par}})|\cdot\hbar_q\cdot m_e/3$, the bare term is $\mathcal{Q}_{\mathrm{bare}} \approx 0.05482\,\mathrm{MeV}$ ($-90.0\%$) and the combined formula gives $Q \approx 0.20198\,\mathrm{MeV}$ ($-63.0\%$).

**Evaluation at $z = q^3/(q^2+1)$.**

At $z = q^3/(q^2+1)$, recomputing the corollary's bare term and combined formula across six benchmark decays yields residuals of $8$–$98\%$ (bare) and $1$–$100\%$ (combined); the $q$-weighted unbinding/rebinding stage and a non-vanishing replacement for the filled-shell Pauli projection have not yet been derived at $z = q^3/(q^2+1)$.

**Method.**

The method uses the eigenvalue asymmetry $q$ versus $-q^{-1}$ of the Iwahori--Hecke algebra to separate unbinding, rebinding and spectator channels. The shell correction factors were intended to derive from the $6 \times 6$ regular representation of $H_3(q)$.

**Error structure.**

The parametric uncertainty $\delta Q / \delta q_0$ is negligible. The residual errors stem from the shell correction and, at $z = q^3/(q^2+1)$, from the vanishing of the $(1^3)$ Pauli branch. Improving $F_{\mathrm{shell}}$ requires extending the spectral decomposition ([spectral decomposition](#cor:spectral-decomposition-qvalue)).
