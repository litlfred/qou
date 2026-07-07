Let $v^*$ be the weak limit as $q \to 1$ of the q-NS solution for anti-parallel vortex pair initial data. Let $\omega^* = \nabla \times v^*$ and let $d(t)$ be the separation between the two filament cores. There exist constants $c_1, c_2 > 0$ such that for all $t < T^*$:

**(a) Separation decay:** $c_1\sqrt{T^* - t} \leq d(t) \leq c_2\sqrt{T^* - t}$.
**(b) Vorticity lower bound:** $\lVert \omega^*(t) \rVert_{L^\infty} \geq c_1 / (T^* - t)$.
**(c) BKM divergence:** $\int_0^{T^*} \lVert \omega^*(t) \rVert_{L^\infty}dt = +\infty$.

In particular, the limit solution $v^*$ loses regularity at $T^*$.

**Argument for (a): Biot--Savart dynamics.**
Two anti-parallel vortex filaments induce velocity on each other. The Biot--Savart ODE gives $d(t) \sim \sqrt{T^*-t}$. For $q > 1$, quantum pressure arrests the approach. The Biot--Savart dynamics holds up to the quantum length scale.

**Argument for (b): Vorticity concentration.**
Mutual induction intensifies the vorticity through the stretching mechanism. The stretching term scales as $\Gamma / d^2$. This gives exponential amplification of vorticity between stretching events. The sharper bound $\omega_{\max} \gtrsim c/(T^* - t)$ follows from constructive addition at the symmetry plane.
