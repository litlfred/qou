The growth profiles of the quaternionic spectral resolvents separate the space-like and time-like sectors of Bring's surface:

- *$\omega_1$ (space-like):* the factor $1/\ln_q(1+r)$ diverges as $r\to 0$. Thus $\omega_1$ achieves infinite density at the base stratum $M_0$, characterising the primordial vortex. This mode anchors the $U(1)$ longitudinal backbone of the $\mathrm{SU}(2)$ bundle.
- *$\omega_2,\omega_3$ (time-like):* the factor $\exp_q(r)-1$ vanishes at $r=0$ and grows rapidly for small $r$, driven by the $q$-deformed Reeb flow ([$q$-Reeb flow](#ex:q-reeb-flow)). These ladder modes expand at the big bang before tapering as the geometric viscosity ([$q$-harmonic physical interpretation](#rem:q-harmonic-physical)) takes hold.

Embed the radial parameter into $\mathrm{Sp}(1)$ via the unit quaternion to realise the rotation as a function of $r$:

```tex
\begin{equation}\label{eq:sp1-quaternion}
  \mathbf{q}(r)
  = 
  \cos_q\!\varTheta(r)+\mathbf{u}\sin_q\!\varTheta(r),
  \qquad
  \varTheta(r)=\tfrac{\pi}{2}e^{-r}.
\end{equation}
```

Here $\cos_q$ and $\sin_q$ are the $q$-deformed trigonometric functions built from $\exp_q$:

$$
  \cos_q(x)=\frac{\exp_q(ix)+\exp_q(-ix)}{2},
  \qquad
  \sin_q(x)=\frac{\exp_q(ix)-\exp_q(-ix)}{2i}.
$$

The element $\mathbf{u}\in\mathrm{Im}\mathbb{H}$ is a fixed unit imaginary quaternion. The conjugation $\boldsymbol{\omega}'=\mathbf{q}(r)\boldsymbol{\omega}\mathbf{q}(r)^{*}$ supplies maximum twist ($\varTheta=\pi/2$) in the deep-quantum regime $r\to 0$ and a classical freeze ($\varTheta\to 0$) as $r\to\infty$.
