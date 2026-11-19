The third topological mass gap observable $c_3$ was initially measured via empirical extrapolation of the $N=3$ operator-valued calculations across the $Q_\beta$ manifold, resulting in a near-match physical measurement.
<!-- literal-source: initial N=3 empirical extrapolation reference value -->
$$ c_3^{\text{emp}} \approx -2.02162 $$

The canonical $q = 1$ shadow of this quantity is $J_{\text{Hopf}}(1) = -2$ (kernel-constraint registry KC10/KC20, $C_{\text{Hopf}}(2) = -2$). The question addressed below is whether the residual gap between $c_3^{\text{emp}}$ and $-2$ admits a continuum-geometric description. (Combinatorial constraints proposed over $S_5$ cells did not survive scrutiny.)

## The Continuum Limit Kashaev Integral

By transitioning to the full continuous Faddeev non-compact integration $\Phi_b(z)$ over the analytic contour $\mathbb{R} + i\delta$, the operator expansion is replaced entirely by the thermodynamic saddle point of the continuum potential. 

For the ground-state $4_1$ (figure-eight pion) topology, the non-compact potential transforms into the imaginary part of the quantum dilogarithm.
$$ V(\theta) = \text{Im}(\text{Li}_2(e^{i\theta})) $$

## The Saddle Point Construction

<!-- literal-source: Gieseking constant Cl_2(pi/3), volume of a regular ideal tetrahedron -->
The critical saddle point of the continuous action sits at $\theta = \pi/3$, where the potential evaluates to the volume of a regular ideal tetrahedron ($V(\pi/3) \approx 1.01494$) and the two-tetrahedron gluing of the $4_1$ complement gives the total macroscopic physical action $\text{Vol}(4_1) \approx 2.02988$. The saddle derivation is carried out once in [the dilog saddle regime](#rem:dilog-saddle-regime).

## The asymptotic bound (scope-limited)

The full non-perturbative Kashaev invariant (calculated via high-precision [Borel–Padé extrapolation](#def:ecalle-borel-resummation) across $N \in [1000, 2050]$) pins the topological action of the geometric envelope.
$$ A = \frac{\text{Vol}(4_1)}{\pi} \approx 0.6461318 $$

The candidate identification
$$ c_3 \xrightarrow{N \to \infty} -\text{Vol}(4_1) \approx -2.02988 $$
is **scope-limited, not exact**: $-\text{Vol}(4_1)$ is anchor-blind, missing both aether anchors (muon $+0.479\%$, proton $-1.907\%$) while the measured $c_3$ itself swings $2.43\%$ across anchors (muon $-2.0202$, proton $-2.0693$). At the muon (CAL-2) pin it is $6.9\times$ worse than the precision-ladder near-match $-\text{Vol}(4_1) + u - (10/3)\,u^2$. The residual between the observed $-2.0216$ and $-2.02988$ was previously attributed to finite-size truncation scaling; the cross-anchor swing shows the identification itself does not close.

What stands is the hyperbolic geometry: $\text{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$, with the Lobachevsky saddle at $\theta = \pi/3$, supplies the geometric envelope that anchor-sensitive corrections (the precision ladder) refine — not a rigorous continuum evaluation of $c_3$.

Every $c_3$ figure quoted above is stated in the **convention-C frame**, $z = \sqrt{q}/(q+1)$. The canonical Markov parameter is convention D, $z = q^3/(q^2+1)$, under which the $\mathfrak{Q}_\beta$ precision ladder has not been re-derived; the figures are correct as recorded and are scoped rather than corrected. The hyperbolic geometry — $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$, with the saddle at $\theta = \pi/3$ — is convention-independent and is unaffected.
