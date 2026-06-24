**Proposition (Binding-energy error amplification).**
*Write the binding energy as the mass defect*

$$
  B \;=\; M_{\mathrm{free}} - M_{\mathrm{atom}},
  \qquad
  M_{\mathrm{free}} = \textstyle\sum_i \mathfrak{m}(\text{constituent}_i),
$$

*the difference between the free-constituent mass and the bound-state mass,
with $0 < B \ll M_{\mathrm{atom}}$. If the predicted bound-state mass carries
relative error $\delta$,*

$$
  M_{\mathrm{atom}}^{\mathrm{pred}} = M_{\mathrm{atom}}\,(1+\delta),
$$

*and $M_{\mathrm{free}}$ is taken exact, then the predicted binding
$B^{\mathrm{pred}} = M_{\mathrm{free}} - M_{\mathrm{atom}}^{\mathrm{pred}}$ has
relative error*

$$
  \frac{B^{\mathrm{pred}} - B}{B}
  \;=\; -\,\delta \cdot \frac{M_{\mathrm{atom}}}{B}.
$$

*The error is amplified by the dimensionless factor
$\mathcal{A} = M_{\mathrm{atom}}/B$.*

The amplification factor is large precisely because binding is a small
defect of two large, nearly equal masses. For the light nuclei
(CODATA / AME-2020 values):

| Nucleus | $M_{\mathrm{atom}}$ (MeV) | $B_{\mathrm{AME}}$ (MeV) | $\mathcal{A} = M_{\mathrm{atom}}/B$ |
|---|---|---|---|
| ${}^2\mathrm{H}$ | $\approx 1875.6$ | $\approx 2.225$ | $\approx 843$ |
| ${}^3\mathrm{H}$ | $\approx 2808.9$ | $\approx 8.482$ | $\approx 331$ |
| ${}^3\mathrm{He}$ | $\approx 2808.4$ | $\approx 7.718$ | $\approx 364$ |
| ${}^4\mathrm{He}$ | $\approx 3727.4$ | $\approx 28.296$ | $\approx 132$ |

A bound-state mass predicted to $0.1\%$ — already a demanding target for the
per-knot mass formula
[$\mathfrak{m}(K) = \mathfrak{m}_e\,\mathrm{Vol}(K)\,\varrho(K)/\hbar_q^2$](#prop:binding-scale-catalan) —
therefore yields a binding energy wrong by tens of percent
($0.1\% \times 843 \approx 84\%$ for the deuteron). The amplification is
worst for the lightest, most weakly bound nuclei.

**Consequence.** The per-knot mass-prediction accuracy (the step-9a frontier)
and the binding-energy accuracy (the step-9b frontier) are not independent
problems. Binding is the amplified shadow of the bound-state mass error: any
residual in the predicted nuclear mass is magnified by $\mathcal{A}$ in the
binding. A categorical derivation of binding to experimental precision
therefore requires the bound-state mass to be derived to a precision finer
than $B/M_{\mathrm{atom}} \approx 0.1\%$–$0.8\%$ of the experimental binding
target — i.e. the binding problem is gated by the mass problem, not
separable from it.

This also explains why computing binding as a difference of two large
Markov traces $\mathrm{tr}_M(W_{\mathrm{free}}) - \mathrm{tr}_M(W_{\mathrm{atom}})$
is numerically hostile: it subjects the small binding signal to the same
catastrophic cancellation, so any systematic in the trace is magnified by
$\mathcal{A}$. Forming the difference object *before* evaluating — so that
binding is computed as a single quantity rather than a cancellation of two
large ones — is the structural way to avoid the amplification.
