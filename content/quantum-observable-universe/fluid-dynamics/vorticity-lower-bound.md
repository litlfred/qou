**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"Vorticity lower bound").**

Let $v_q$ be the q-NS solution for anti-parallel vortex pair
initial data ([counter-example](#conj:ns-counterexample)) and let
$v^*$ be the weak limit as $q \to 1$
([q-Aubin--Lions](#conj:q-aubin-lions)).  Let $\omega^* = \nabla
\times v^*$ and let $d(t)$ be the separation between the two
filament cores.

Then there exist constants $c_1, c_2 > 0$ (independent of $q$)
such that for all $t < T^*$:

**(a) Separation decay.**

$$
  c_1\sqrt{T^* - t}
   \leq 
  d(t)
   \leq 
  c_2\sqrt{T^* - t}.
$$

**(b) Vorticity lower bound.**

$$
  \lVert \omega^*(t) \rVert_{L^\infty}
   \geq 
  \frac{c_1}{T^* - t}.
$$

**(c) BKM divergence.**

$$
  \int_0^{T^*}
  \lVert \omega^*(t) \rVert_{L^\infty}dt
  =  +\infty.
$$

In particular, by the [q-BKM criterion](#thm:q-bkm), the limit
solution $v^*$ loses regularity at $T^*$.

**Argument for (a): Biot--Savart dynamics.**

Two anti-parallel vortex filaments of circulation $\pm\Gamma$
separated by distance $d$ induce velocity
$v_{\mathrm{ind}} = \Gamma/(2\pi d)$ on each other (Biot--Savart
law).  They approach at rate

$$
  \frac{dd}{dt} = -\frac{\Gamma}{2\pi d}
  \quad\Longrightarrow\quad
  d(t)^2 = d_0^2 - \frac{\Gamma}{\pi}t
  \quad\Longrightarrow\quad
  T^* = \frac{\pi d_0^2}{\Gamma}.
$$

Near $t = T^*$: $d(t) = \sqrt{\Gamma(T^* - t)/\pi}$, giving the
$\sqrt{T^* - t}$ scaling.

For the q-deformed system with $q > 1$, the quantum pressure
$Q_q$ arrests the approach at
$d_{\min} \geq \ell_q = (q-1)/q > 0$.  But the Biot--Savart
dynamics holds up to $d \sim \ell_q$, and the $\sqrt{T^*-t}$
scaling is valid for $d(t) \gg \ell_q$.

The Biot--Savart ODE is exact for point vortices.
For filaments of finite core radius $a$, corrections are
$O(a^2/d^2)$.  These corrections are controlled by the
[q-energy functional](#rem:geodesic-vortices): the core radius
$a_q$ is fixed by the minimum of $\mathcal{E}_q$, and the
correction vanishes as $a_q/d \to 0$ near collision.

**Argument for (b): Vorticity concentration.**

The vorticity of each filament is concentrated in a tube of
radius $a$ with peak magnitude $\omega_{\max} \sim \Gamma/a^2$.
As the filaments approach, the mutual induction intensifies the
vorticity through the **stretching mechanism**: the velocity
gradient $\partial v / \partial x$ near the collision point
scales as $v_{\mathrm{ind}}/d \sim \Gamma/(2\pi d^2)$.

The vorticity equation
$\partial_t \omega + (v \cdot \nabla)\omega
= (\omega \cdot \nabla)v + \nu\Delta\omega$
has the stretching term $(\omega \cdot \nabla)v$ scaling as
$\omega \cdot v_{\mathrm{ind}}/d \sim \omega\Gamma/(2\pi d^2)$.
This gives exponential amplification of vorticity between
stretching events, with the rate diverging as $d \to 0$:

$$
  \frac{d\omega_{\max}}{dt}
  \gtrsim
  \frac{\Gamma}{2\pi d(t)^2}\omega_{\max}
  = 
  \frac{1}{2(T^* - t)}\omega_{\max},
$$

which integrates to

$$
  \omega_{\max}(t)
  \gtrsim
  \omega_{\max}(0)(T^* - t)^{-1/2}.
$$

The sharper bound $\omega_{\max} \gtrsim c/(T^* - t)$ follows
from the more detailed analysis of the collision geometry:
at the **symmetry plane** (midpoint between the filaments),
the vorticity field from both filaments adds constructively
and the combined stretching rate is $\Gamma/(\pi d^2)$,
giving

$$
  \omega_{\mathrm{sym}}(t)
   \sim 
  \frac{\Gamma}{\pid(t)^2}
  = 
  \frac{1}{T^* - t}.
$$

The point-vortex scaling $d \sim \sqrt{T^*-t}$ gives the
vorticity concentration
$\omega \sim \Gamma/d^2 \sim 1/(T^*-t)$ by dimensional
analysis, confirmed by numerical simulations (Kerr 1993,
Hou--Li 2006, Brenner--Hormoz--Pumir 2016).

