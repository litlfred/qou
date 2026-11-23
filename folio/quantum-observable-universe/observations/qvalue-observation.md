The $q$-weighted method predicts $\beta^-$ decay $Q$-values from $q$ alone, with no fitted parameters. Every figure in the first three paragraphs below was obtained under the excised Markov convention C, $z = q^{1/2}/(q+1)$, by a float64 implementation. They are recorded here as the convention-C output of that method. Under the canonical convention D, $z = q^3/(q^2+1)$, they are not reproduced; the convention-D values are in the [interpretation table](#rem:spectral-decomposition-qvalue-interpretation).

**Predicted vs observed $Q$-values (convention C, $q$-weighted method).**

See [Table](#tbl:qvalue-observation-table-data). The table and the figures below are convention-C outputs of the $q$-weighted method.

Under convention C the MAE is $\approx 4.4\%$ and the RMS is $\approx 5.4\%$, and light nuclei ($A \leq 14$) reach errors $\leq 2.2\%$. The heavy-nucleus factors $F_{\mathrm{deg2}} = 0.5904$ and $F_{\mathrm{Pauli}} = 0.6382$ are constants hard-coded in that producer, not values it computes. Neither survives under convention D. The degree-$2$ factor evaluates to $F_{\mathrm{deg2}} \approx 3.68442$, which exceeds $1$ and so does not act as a suppression. The Markov-trace form of the Pauli factor vanishes, because the Ocneanu weight of $(1^3)$ is zero at $z = q^3/(q^2+1)$. The value $0.6382$ is not reproduced under either convention.

**Worked example: ${}^{90}\mathrm{Sr}$ (convention C).**

For ${}^{90}\mathrm{Sr}$ the convention-C bare prediction $\mathcal{Q}_{\mathrm{bare}} \approx 0.944\,\mathrm{MeV}$ overshoots $\mathcal{Q}_{\mathrm{exp}} = 0.546\,\mathrm{MeV}$ by $+73\%$, and applying $F_{\mathrm{deg2}} = 0.5904$ gives $Q \approx 0.557\,\mathrm{MeV}$ ($+2.1\%$). Under convention D, with the normalisation $|\log_q(P_{\mathrm{dau}}/P_{\mathrm{par}})|\cdot\hbar_q\cdot m_e/3$ of the corollary, the bare term is $\mathcal{Q}_{\mathrm{bare}} \approx 0.05482\,\mathrm{MeV}$ ($-90.0\%$) and the combined formula gives $Q \approx 0.20198\,\mathrm{MeV}$ ($-63.0\%$). The convention-C agreement for ${}^{90}\mathrm{Sr}$ therefore does not carry over to convention D.

**Convention-D status.**

The convention-D table recomputes the corollary's bare term and combined formula. It does not recompute the $q$-weighted stage, which weights the unbinding and rebinding channels by $q$ and $q^{-1}$; that stage has not been re-derived under convention D. Across six decays the convention-D bare term misses by $8$–$98\%$ and the combined formula by $1$–$100\%$. No convention-D replacement for the Pauli branch has been derived.

**Method.**

The method uses the eigenvalue asymmetry $q$ versus $-q^{-1}$ of the Iwahori--Hecke algebra to separate unbinding, rebinding and spectator channels. The shell correction factors were intended to derive from the $6 \times 6$ regular representation of $H_3(q)$.

**Error structure.**

The parametric uncertainty $\delta Q / \delta q_0$ is negligible. The residual errors stem from the shell correction and, under convention D, from the vanishing of the Pauli branch. Improving $F_{\mathrm{shell}}$ requires extending the spectral decomposition ([spectral decomposition](#cor:spectral-decomposition-qvalue)).
